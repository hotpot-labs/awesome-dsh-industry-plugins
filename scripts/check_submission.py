#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PR 投稿结构校验脚本
===================

校验内容:
    1. plugins.json 是合法 JSON，且符合收录名单结构（必填字段、分类/定级/来源合法、
       id 与 dir 目录名一致、url 与 id 对应）。
    2. 每条 entry 的 dir 存在，且含 plugin.md 与 security-report.md（审核档案完整）。
    3. 防 stale-fork：与 base 分支相比，删除已有条目 > 2 即失败（需 rebase 后重提）。
    4. 单 PR 新增条目 ≤ 3 条（控制审核成本，对应 awesome-dsh-plugin 的提交门禁）。

用法:
    python3 scripts/check_submission.py [--base origin/main]

说明:
    * 不提供 --base 时只做 1、2 两项结构校验（本地自检用）。
    * --base 在 CI 中传入 PR 的目标分支（如 origin/main）。
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGINS_JSON = ROOT / 'plugins.json'

VALID_CATEGORIES = {'通用', '计算机', '金融', '法律', '自媒体', '电商', '其他'}
VALID_VERDICTS = {'whitelist', 'greylist', 'blacklist', 'pending'}
VALID_SOURCES = {'submission', 'awesome-dsh-plugin'}
REQUIRED_FIELDS = ['id', 'name', 'url', 'category', 'description', 'verdict', 'auditedAt', 'source', 'dir']

MAX_ADDED_PER_PR = 3
MAX_REMOVED_PER_PR = 2

errors = []


def fail(msg):
    errors.append(msg)
    print(f'[fail] {msg}', file=sys.stderr)


def load_plugins_json(path_label, text):
    """解析 plugins.json 文本，失败时记录错误并返回 None。"""
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        fail(f'{path_label} 不是合法 JSON: {e}')
        return None
    if not isinstance(data, dict) or not isinstance(data.get('plugins'), list):
        fail(f'{path_label} 结构错误: 顶层应为含 plugins 数组的对象')
        return None
    return data


def check_structure(data):
    """结构校验：字段完整、取值合法、id/url/dir 一致、审核产物齐全。"""
    seen_ids = set()
    for i, entry in enumerate(data['plugins']):
        where = f'plugins[{i}]'
        if not isinstance(entry, dict):
            fail(f'{where} 不是对象')
            continue

        for field in REQUIRED_FIELDS:
            if field not in entry or entry[field] in (None, ''):
                fail(f'{where} 缺少必填字段或字段为空: {field}')
        entry_id = entry.get('id', '?')

        if entry_id in seen_ids:
            fail(f'{where} id 重复: {entry_id}')
        seen_ids.add(entry_id)

        if not re.match(r'^[^/]+__[^/]+$', entry_id):
            fail(f'{entry_id}: id 格式应为 <owner>__<repo>')

        if entry.get('category') not in VALID_CATEGORIES:
            fail(f'{entry_id}: 非法分类 {entry.get("category")}')
        if entry.get('verdict') not in VALID_VERDICTS:
            fail(f'{entry_id}: 非法定级 {entry.get("verdict")}')
        if entry.get('source') not in VALID_SOURCES:
            fail(f'{entry_id}: 非法来源 {entry.get("source")}')

        # url 与 id 一致性
        url = entry.get('url', '')
        m = re.match(r'^https://github\.com/([^/]+)/([^/]+?)/?$', url)
        if not m:
            fail(f'{entry_id}: url 非法: {url}')
        elif f'{m.group(1)}__{m.group(2)}' != entry_id:
            fail(f'{entry_id}: url 与 id 不一致: {url}')
        if entry.get('name') and '/' in str(entry.get('name')):
            if entry['name'].replace('/', '__') != entry_id:
                fail(f'{entry_id}: name 与 id 不一致: {entry["name"]}')

        # dir 与审核产物
        entry_dir = entry.get('dir', '')
        if entry_dir != f'plugins/{entry_id}':
            fail(f'{entry_id}: dir 应为 plugins/{entry_id}，实际为 {entry_dir}')
        dir_path = ROOT / entry_dir
        if not dir_path.is_dir():
            fail(f'{entry_id}: 目录不存在: {entry_dir}')
        else:
            for fname in ('plugin.md', 'security-report.md'):
                if not (dir_path / fname).is_file():
                    fail(f'{entry_id}: 缺少审核产物: {entry_dir}/{fname}')

    return seen_ids


def load_base_plugins(base):
    """从 base 分支读取 plugins.json，失败返回 None（记录错误）。"""
    proc = subprocess.run(
        ['git', 'show', f'{base}:plugins.json'],
        capture_output=True, text=True, cwd=ROOT,
    )
    if proc.returncode != 0:
        fail(f'无法从 {base} 读取 plugins.json: {proc.stderr.strip()}')
        return None
    return load_plugins_json(f'{base}:plugins.json', proc.stdout)


def check_diff(current_ids, base):
    """diff 校验：删除 >2 失败（防 stale-fork），新增 >3 失败（控量）。"""
    base_data = load_base_plugins(base)
    if base_data is None:
        return
    base_ids = {e.get('id') for e in base_data['plugins'] if isinstance(e, dict)}
    removed = base_ids - current_ids
    added = current_ids - base_ids
    if len(removed) > MAX_REMOVED_PER_PR:
        fail(f'本 PR 删除了 {len(removed)} 条已有收录 (>{MAX_REMOVED_PER_PR})，疑似基于过期 fork，请 rebase 后重提: {sorted(removed)}')
    if len(added) > MAX_ADDED_PER_PR:
        fail(f'本 PR 新增 {len(added)} 条收录 (>{MAX_ADDED_PER_PR})，请拆分为多个 PR: {sorted(added)}')
    print(f'[info] 与 {base} 相比: 新增 {len(added)} 条, 删除 {len(removed)} 条')


def main():
    parser = argparse.ArgumentParser(description='dsh 行业插件市场 PR 投稿结构校验')
    parser.add_argument('--base', default=None, help='PR 目标分支（如 origin/main），用于 diff 校验')
    args = parser.parse_args()

    if not PLUGINS_JSON.is_file():
        fail('plugins.json 不存在')
    else:
        data = load_plugins_json('plugins.json', PLUGINS_JSON.read_text(encoding='utf-8'))
        if data is not None:
            current_ids = check_structure(data)
            if args.base:
                check_diff(current_ids, args.base)

    if errors:
        print(f'\n[result] 校验失败，共 {len(errors)} 个问题', file=sys.stderr)
        sys.exit(1)
    print('[result] 校验通过')


if __name__ == '__main__':
    main()
