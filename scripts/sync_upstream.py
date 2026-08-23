#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
上游 awesome-dsh-plugin 每日增量同步脚本
========================================

流程:
    1. 通过 GitHub Git Trees API 枚举上游仓库 awesome-dsh-plugin/awesome-dsh-plugin
       的 data/plugins/*.yml 收录列表（目录超 1000 条时 Contents API 会截断，故用 Trees API）。
    2. 与本地 plugins.json 求差：
       - 新增 → 拉取该 yml 原文解析 url/category/description，逐个调用
         audit_plugin 审核并落盘（单次最多 --max 个，默认 20，剩余下个工作日继续）；
       - 上游已删除 → 本地条目标记 "removed": true（保留审核档案）；
       - 已收录 → 跳过（增量）。
    3. 分类映射：上游英文 category 不在本地 7 类内 → 归「其他」。

用法:
    python3 scripts/sync_upstream.py [--token T] [--max 20] [--dry-run]

说明:
    * --dry-run 只枚举上游并计算差集，不拉取 yml、不审核、不写任何文件。
    * 依赖 PyYAML 解析上游 yml；缺失时会给出清晰报错（CI 中 pip install pyyaml）。
"""

import argparse
import json
import sys
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGINS_JSON = ROOT / 'plugins.json'

# 把 scripts/ 加入 import 路径，复用 audit_plugin 的审核逻辑
sys.path.insert(0, str(Path(__file__).resolve().parent))
import audit_plugin  # noqa: E402

UPSTREAM_REPO = 'awesome-dsh-plugin/awesome-dsh-plugin'
UPSTREAM_YML_DIR = 'data/plugins'
API_BASE = 'https://api.github.com'
RAW_BASE = f'https://raw.githubusercontent.com/{UPSTREAM_REPO}'

DEFAULT_MAX = 20
HTTP_TIMEOUT = 30

# 上游英文 category → 本地 7 类的尽力映射，映射不上归「其他」
CATEGORY_MAP = {
    'general': '通用',
    'dev': '计算机', 'developer-tools': '计算机', 'devtools': '计算机', 'programming': '计算机',
    'finance': '金融', 'fintech': '金融',
    'law': '法律', 'legal': '法律',
    'media': '自媒体', 'self-media': '自媒体', 'content': '自媒体',
    'ecommerce': '电商', 'e-commerce': '电商', 'shop': '电商',
}


def http_get_json(url, token=None):
    """GET JSON（带 UA 与可选 token），失败抛 RuntimeError。"""
    req = urllib.request.Request(url, headers={
        'Accept': 'application/vnd.github+json',
        'User-Agent': 'dsh-industry-plugins-sync',
    })
    if token:
        req.add_header('Authorization', f'Bearer {token}')
    try:
        with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        raise RuntimeError(f'GitHub API 请求失败 {e.code}: {url}') from e
    except urllib.error.URLError as e:
        raise RuntimeError(f'网络不可达: {url} ({e.reason})') from e


def http_get_text(url, token=None):
    """GET 纯文本（用于拉取 raw yml），失败抛 RuntimeError。"""
    req = urllib.request.Request(url, headers={'User-Agent': 'dsh-industry-plugins-sync'})
    if token:
        req.add_header('Authorization', f'Bearer {token}')
    try:
        with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
            return resp.read().decode('utf-8')
    except (urllib.error.HTTPError, urllib.error.URLError) as e:
        raise RuntimeError(f'拉取失败: {url} ({e})') from e


def list_upstream_yml(token=None):
    """枚举上游 data/plugins/ 下的 yml 文件名列表（不含扩展名）。

    用 Trees API 逐层定位 data/plugins 子树，避免 Contents API 1000 条上限。
    """
    repo = http_get_json(f'{API_BASE}/repos/{UPSTREAM_REPO}', token)
    branch = repo.get('default_branch', 'main')

    sha = branch
    for part in UPSTREAM_YML_DIR.split('/'):
        tree = http_get_json(f'{API_BASE}/repos/{UPSTREAM_REPO}/git/trees/{sha}', token)
        if tree.get('truncated'):
            raise RuntimeError(f'Git Trees API 结果被截断: {sha}')
        node = next((e for e in tree.get('tree', []) if e['path'] == part and e['type'] == 'tree'), None)
        if node is None:
            raise RuntimeError(f'上游仓库不存在目录: {UPSTREAM_YML_DIR} (缺少 {part})')
        sha = node['sha']

    tree = http_get_json(f'{API_BASE}/repos/{UPSTREAM_REPO}/git/trees/{sha}', token)
    stems = sorted(
        e['path'][:-4] for e in tree.get('tree', [])
        if e['type'] == 'blob' and e['path'].endswith('.yml')
    )
    return branch, stems


def load_local():
    """读取本地 plugins.json，返回 (data, {id: entry})。"""
    if PLUGINS_JSON.exists() and PLUGINS_JSON.read_text(encoding='utf-8').strip():
        data = json.loads(PLUGINS_JSON.read_text(encoding='utf-8'))
    else:
        data = {'$schema': './plugins.schema.json', 'plugins': []}
    entries = {e['id']: e for e in data.get('plugins', []) if isinstance(e, dict) and 'id' in e}
    return data, entries


def map_category(upstream_category):
    """上游 category 映射到本地 7 类，映射不上归「其他」。"""
    if not upstream_category:
        return '其他'
    c = str(upstream_category).strip()
    if c in audit_plugin.VALID_CATEGORIES:
        return c
    return CATEGORY_MAP.get(c.lower(), '其他')


def fetch_upstream_yml(branch, stem, token=None):
    """拉取并解析上游单条 yml，返回 dict。PyYAML 缺失时给出清晰报错。"""
    try:
        import yaml
    except ImportError:
        raise RuntimeError('缺少 PyYAML，无法解析上游 yml。请先执行: pip install pyyaml')
    text = http_get_text(f'{RAW_BASE}/{branch}/{UPSTREAM_YML_DIR}/{stem}.yml', token)
    data = yaml.safe_load(text)
    if not isinstance(data, dict) or not data.get('url'):
        raise RuntimeError(f'上游 yml 结构异常 (缺少 url): {stem}.yml')
    return data


def mark_removed(data, removed_ids):
    """把上游已删除的条目标记 removed: true 并写回 plugins.json。"""
    changed = False
    for entry in data.get('plugins', []):
        if entry.get('id') in removed_ids and not entry.get('removed'):
            entry['removed'] = True
            changed = True
    if changed:
        from datetime import date
        data['updatedAt'] = date.today().isoformat()
        PLUGINS_JSON.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return changed


def main():
    parser = argparse.ArgumentParser(description='上游 awesome-dsh-plugin 每日增量同步')
    parser.add_argument('--token', default=None, help='GitHub Token（提升 API 配额）')
    parser.add_argument('--max', type=int, default=DEFAULT_MAX, help=f'单次最多审核插件数（默认 {DEFAULT_MAX}）')
    parser.add_argument('--dry-run', action='store_true', help='只枚举并计算差集，不审核不写文件')
    args = parser.parse_args()

    try:
        branch, upstream_stems = list_upstream_yml(token=args.token)
    except RuntimeError as e:
        print(f'[error] 枚举上游收录列表失败: {e}', file=sys.stderr)
        sys.exit(1)
    print(f'[info] 上游 {UPSTREAM_REPO}@{branch} 共 {len(upstream_stems)} 条收录')

    data, local_entries = load_local()
    local_ids = set(local_entries)
    # 只对本来源条目做 removed 判定，投稿条目不受上游删除影响
    synced_ids = {i for i, e in local_entries.items()
                  if e.get('source') == 'awesome-dsh-plugin' and not e.get('removed')}

    new_ids = [s for s in upstream_stems if s not in local_ids]
    removed_ids = synced_ids - set(upstream_stems)
    print(f'[info] 差集: 新增 {len(new_ids)} 条, 上游已删除 {len(removed_ids)} 条, 已收录跳过 {len(upstream_stems) - len(new_ids)} 条')

    if args.dry_run:
        for s in new_ids[:10]:
            print(f'  [new] {s}')
        if len(new_ids) > 10:
            print(f'  [new] ... 以及另外 {len(new_ids) - 10} 条')
        for s in sorted(removed_ids):
            print(f'  [removed] {s}')
        print('[result] dry-run 完成，未做任何修改')
        return

    if removed_ids:
        mark_removed(data, removed_ids)
        print(f'[ok] 已将 {len(removed_ids)} 条上游删除的条目标记 removed=true')

    todo = new_ids[:args.max]
    if len(new_ids) > args.max:
        print(f'[info] 本次只审核前 {args.max} 条，剩余 {len(new_ids) - args.max} 条下个工作日继续')
    ok, failed = 0, 0
    for stem in todo:
        try:
            yml = fetch_upstream_yml(branch, stem, token=args.token)
            url = str(yml['url']).strip()
            desc = yml.get('description') or {}
            description = (desc.get('zh') or desc.get('en')) if isinstance(desc, dict) else str(desc)
            category = map_category(yml.get('category'))
            entry, warning = audit_plugin.audit_plugin(
                url, category, 'awesome-dsh-plugin',
                description=description, token=args.token,
            )
            if warning:
                print(f'[warning] {stem}: {warning}', file=sys.stderr)
            print(f"[ok] {stem} -> verdict={entry['verdict']}")
            ok += 1
        except Exception as e:  # 单插件失败不阻塞整体同步
            print(f'[error] 审核失败 {stem}: {e}', file=sys.stderr)
            failed += 1
    print(f'[result] 同步完成: 成功 {ok} 条, 失败 {failed} 条')


if __name__ == '__main__':
    main()
