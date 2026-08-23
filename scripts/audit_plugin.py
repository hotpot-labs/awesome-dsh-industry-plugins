#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
单插件安全审核编排脚本
======================

流程：调用 security/validate-plugin.py 生成审核报告 → 解析报告定级 →
写 plugins/<id>/plugin.md → 幂等更新 plugins.json（按 id upsert）。

用法:
    python3 scripts/audit_plugin.py --url https://github.com/owner/repo \
        --category 通用 --source submission [--description "..."] [--token T]
    python3 scripts/audit_plugin.py --url ... --dry-run   # 只审不落盘（供 PR CI 使用）

说明:
    * validate-plugin.py 仅在自身异常时以非 0 退出，审核结论（含黑名单）也是 0，
      因此必须解析报告文本判定 verdict。
    * verdict 映射：报告「自动判定结果」段含「黑名单」→ blacklist；
      含「白名单」→ whitelist；含「灰名单」→ greylist；解析不到 → pending 并告警。
"""

import argparse
import json
import re
import subprocess
import sys
import urllib.request
import urllib.error
from datetime import date
from pathlib import Path

# 仓库根目录（本脚本位于 <root>/scripts/audit_plugin.py）
ROOT = Path(__file__).resolve().parent.parent
VALIDATE_SCRIPT = ROOT / 'security' / 'validate-plugin.py'
PLUGINS_JSON = ROOT / 'plugins.json'

# 单插件审核超时（秒），防止克隆巨大仓库拖死 CI
AUDIT_TIMEOUT = 600

VALID_CATEGORIES = ['通用', '计算机', '金融', '法律', '自媒体', '电商', '其他']
VALID_VERDICTS = ['whitelist', 'greylist', 'blacklist', 'pending']
VALID_SOURCES = ['submission', 'awesome-dsh-plugin']


def parse_plugin_id(url):
    """从 GitHub 仓库 URL 提取 (id, name)，id 格式为 <owner>__<repo>。"""
    m = re.match(r'^https://github\.com/([^/]+)/([^/]+?)/?$', url.strip())
    if not m:
        raise ValueError(f'无法解析 GitHub 仓库 URL: {url} (期望 https://github.com/owner/repo)')
    owner, repo = m.group(1), m.group(2)
    return f'{owner}__{repo}', f'{owner}/{repo}'


def run_audit(url, report_path, token=None):
    """调用 validate-plugin.py 生成审核报告，返回报告文本。"""
    cmd = [sys.executable, str(VALIDATE_SCRIPT), url, '--out', str(report_path), '--quiet']
    if token:
        cmd += ['--token', token]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=AUDIT_TIMEOUT)
    if proc.returncode != 0:
        raise RuntimeError(f'validate-plugin.py 执行失败 (exit {proc.returncode}): {proc.stderr.strip()}')
    if not report_path.exists():
        raise RuntimeError(f'审核报告未生成: {report_path}')
    return report_path.read_text(encoding='utf-8')


def parse_verdict(report_text):
    """解析报告「自动判定结果」段，返回 (verdict, 警告信息或 None)。"""
    m = re.search(r'## 自动判定结果\n(.*?)(?=\n## )', report_text, re.S)
    if not m:
        return 'pending', '报告中未找到「自动判定结果」段，verdict 置为 pending'
    section = m.group(1)
    if '黑名单' in section:
        return 'blacklist', None
    if '白名单' in section:
        return 'whitelist', None
    if '灰名单' in section:
        return 'greylist', None
    return 'pending', '「自动判定结果」段无法识别定级，verdict 置为 pending'


def fetch_repo_description(name, token=None):
    """通过 GitHub API 获取仓库描述，失败返回 None。"""
    req = urllib.request.Request(
        f'https://api.github.com/repos/{name}',
        headers={'Accept': 'application/vnd.github+json', 'User-Agent': 'dsh-industry-plugins-audit'},
    )
    if token:
        req.add_header('Authorization', f'Bearer {token}')
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
        return data.get('description') or None
    except (urllib.error.URLError, json.JSONDecodeError, KeyError):
        return None


def write_plugin_md(plugin_dir, entry, report_verdict_note):
    """生成 plugins/<id>/plugin.md（插件基本信息 + 定级摘要）。"""
    verdict_label = {
        'whitelist': '✅ 白名单',
        'greylist': '🟡 灰名单 (需人工复核)',
        'blacklist': '🔴 黑名单 (禁止使用)',
        'pending': '⏳ 待审核',
    }[entry['verdict']]
    lines = [
        f"# {entry['name']}",
        '',
        f"- **仓库地址**: {entry['url']}",
        f"- **收录分类**: {entry['category']}",
        f"- **插件简介**: {entry['description']}",
        f"- **收录来源**: {entry['source']}",
        f"- **审核日期**: {entry['auditedAt']}",
        f"- **审核定级**: {verdict_label}",
        '',
        '完整审核报告见同目录 [security-report.md](./security-report.md)。',
        '',
        '> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。',
        '',
    ]
    (plugin_dir / 'plugin.md').write_text('\n'.join(lines), encoding='utf-8')


def upsert_plugins_json(entry):
    """按 id 幂等 upsert plugins.json，并刷新 updatedAt。"""
    if PLUGINS_JSON.exists() and PLUGINS_JSON.read_text(encoding='utf-8').strip():
        data = json.loads(PLUGINS_JSON.read_text(encoding='utf-8'))
    else:
        data = {'$schema': './plugins.schema.json', 'plugins': []}
    plugins = data.setdefault('plugins', [])
    for i, old in enumerate(plugins):
        if old.get('id') == entry['id']:
            plugins[i] = entry
            break
    else:
        plugins.append(entry)
    data['updatedAt'] = date.today().isoformat()
    PLUGINS_JSON.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def audit_plugin(url, category, source, description=None, token=None, dry_run=False):
    """审核单个插件。dry_run=True 时只审核并打印结论，不写任何文件。

    返回 (entry, warning)。entry 为 plugins.json 条目字典。
    """
    plugin_id, name = parse_plugin_id(url)
    if category not in VALID_CATEGORIES:
        raise ValueError(f'非法分类: {category} (允许: {"/".join(VALID_CATEGORIES)})')
    if source not in VALID_SOURCES:
        raise ValueError(f'非法来源: {source} (允许: {"/".join(VALID_SOURCES)})')

    plugin_dir = ROOT / 'plugins' / plugin_id
    plugin_dir.mkdir(parents=True, exist_ok=True)
    report_path = plugin_dir / 'security-report.md'

    report_text = run_audit(url, report_path, token=token)
    verdict, warning = parse_verdict(report_text)

    if not description:
        description = fetch_repo_description(name, token=token) or '(暂无描述)'

    entry = {
        'id': plugin_id,
        'name': name,
        'url': url,
        'category': category,
        'description': description,
        'verdict': verdict,
        'auditedAt': date.today().isoformat(),
        'source': source,
        'dir': f'plugins/{plugin_id}',
    }

    if dry_run:
        # PR CI 用：报告只用于判定，不落盘（清理刚生成的报告与空目录）
        report_path.unlink(missing_ok=True)
        try:
            plugin_dir.rmdir()
        except OSError:
            pass
        return entry, warning

    write_plugin_md(plugin_dir, entry, warning)
    upsert_plugins_json(entry)
    return entry, warning


def main():
    parser = argparse.ArgumentParser(description='dsh 行业插件单插件安全审核编排')
    parser.add_argument('--url', required=True, help='插件 GitHub 仓库地址')
    parser.add_argument('--category', default='其他', help=f'收录分类 ({"/".join(VALID_CATEGORIES)})')
    parser.add_argument('--source', default='submission', help=f'收录来源 ({"/".join(VALID_SOURCES)})')
    parser.add_argument('--description', default=None, help='插件简介（缺省自动从 GitHub API 获取）')
    parser.add_argument('--token', default=None, help='GitHub Token（提升 API 配额）')
    parser.add_argument('--dry-run', action='store_true', help='只审核并输出结论，不写 plugins/ 与 plugins.json')
    args = parser.parse_args()

    try:
        entry, warning = audit_plugin(
            args.url, args.category, args.source,
            description=args.description, token=args.token, dry_run=args.dry_run,
        )
    except (ValueError, RuntimeError, subprocess.TimeoutExpired) as e:
        print(f'[error] 审核失败: {e}', file=sys.stderr)
        sys.exit(1)

    if warning:
        print(f'[warning] {warning}', file=sys.stderr)
    mode = 'dry-run' if args.dry_run else '已落盘'
    print(f"[ok] {entry['name']} -> verdict={entry['verdict']} ({mode})")
    # 供 CI 捕获：最后一行输出 JSON
    print(json.dumps(entry, ensure_ascii=False))


if __name__ == '__main__':
    main()
