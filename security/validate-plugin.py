#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DSH 插件安全自动化校验脚本
===========================

按照 security-for-dsh-plugin/ 目录下 security-checklist.md 与 security-docs.md
的要求, 对指定 GitHub 链接的 DSH 插件进行自动化安全校验。

用法:
    python3 validate-plugin.py https://github.com/owner/repo [--out report.md] [--no-clone] [--keep] [--token GITHUB_TOKEN]
    python3 validate-plugin.py https://github.com/owner/repo/tree/main/packages/my-plugin

参数:
    URL               DSH 插件 GitHub 仓库/子目录链接 (支持 GitHub / GitLab)
    --out FILE        将 Markdown 报告写入文件 (默认只输出到 stdout)
    --no-clone        不克隆仓库, 仅基于 GitHub API 做仓库级检查
    --keep            校验完成后保留克隆的临时目录 (默认自动清理)
    --token TOKEN     GitHub/GitLab Personal Access Token (可选, 提升 API 配额)
    --quiet           仅输出 PASS/FAIL 摘要, 不输出详细检查项
    --severity LEVEL  只显示 >= 该级别的结果: critical|major|minor|info

说明:
    * 本脚本为自动化辅助工具, 以下检查项无法 100% 自动化, 需要人工复核:
      - 1.4 核心功能与 README 描述一致性
      - 1.5 是否违反法律法规
      - 2.2/2.3/2.4 Cordis 规范细节、异常捕获、卸载清理逻辑评估
      - 3.x/4.x/5.x 中涉及业务意图判断的项 (识别到风险模式后需人工判断)
    * 脚本输出将风险检查项标记为 "需人工复核", 请结合 checklist 完成最终分级。
"""

import os
import re
import sys
import json
import shutil
import argparse
import subprocess
import tempfile
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path


# ---------------------------------------------------------------------------
# 常量定义
# ---------------------------------------------------------------------------

MIT_COMPATIBLE_LICENSES = {
    'mit', 'apache-2.0', 'apache2', 'apache', 'bsd', 'bsd-2-clause', 'bsd-3-clause',
    'bsd-2', 'bsd-3', 'isc', 'zlib', 'unlicense', 'cc0', '0bsd', 'wtfpl',
}
GPL_LICENSES = {'gpl', 'gpl-2.0', 'gpl-3.0', 'lgpl', 'lgpl-2.1', 'lgpl-3.0', 'agpl', 'agpl-3.0'}

# 敏感路径 / 敏感文件模式 (3.1)
SENSITIVE_PATH_PATTERNS = [
    (r'[~/]?\.ssh[/\\]', '读取 SSH 私钥目录'),
    (r'\.aws[/\\]credentials', '读取 AWS 凭证'),
    (r'\.npmrc', '读取 npm 凭证'),
    (r'\.env([.\w]*)', '读取环境变量配置'),
    (r'\.git-credentials', '读取 git 凭证'),
    (r'\.config[/\\]google-chrome|\.config[/\\]chromium|\.config[/\\]microsoft-edge', '读取浏览器配置'),
    (r'Cookies\.db|\.cookies\.txt|Local Storage|\.localstorage', '读取浏览器 Cookie/本地存储'),
    (r'\.git[/\\]config', '读取 git 配置'),
    (r'\.netrc', '读取 .netrc 凭证'),
    (r'\.pypirc', '读取 PyPI 凭证'),
    (r'id_rsa|id_ed25519|id_dsa', '读取 SSH 私钥'),
    (r'\.kube[/\\]config', '读取 k8s 配置'),
    (r'\.docker[/\\]config\.json', '读取 Docker 凭证'),
    (r'security\.json|credentials\.json|token\.json', '读取凭证文件'),
]

# 敏感 API Key / 配置读取模式 (3.7)
SENSITIVE_CONFIG_PATTERNS = [
    (r'process\.env\.[A-Z_]+', '读取环境变量 API Key/凭证'),
    (r'api[_-]?key|apikey|api_token|apitoken|access[_-]?token', 'API Key / Token 读取'),
    (r'secret|password|passwd|credential', '敏感凭证读取'),
    (r'session[_-]?history|session_archive|conversation[_-]??history', '会话历史读取'),
]

# 危险 API / 代码执行模式 (4.2)
DANGEROUS_CODE_PATTERNS = [
    (r'\beval\s*\(', 'eval() 任意代码执行'),
    (r'\bnew\s+Function\s*\(', 'new Function() 任意代码执行'),
    (r'\bvm\.(runInNewContext|runInThisContext|runInContext|compileFunction|createScript|Script)\s*\(', 'node:vm 任意代码执行'),
    (r'\bchild_process\.(exec|execSync|spawn|spawnSync|fork|execFile|execFileSync)\s*\(', 'child_process 命令执行'),
    (r'require\([\'"]child_process[\'"]\)', '加载 child_process 模块'),
    (r'from[\'"]child_process[\'"]', 'ESM 导入 child_process'),
    (r'\bprocess\.(dlopen|binding)\s*\(', '动态加载原生模块'),
]

# 命令注入风险模式 (3.4)
COMMAND_INJECTION_PATTERNS = [
    (r'(exec|execSync|spawn|spawnSync|fork)\s*\(\s*[`"].*(\$\{|%s|\+).*', '命令字符串拼接变量 (注入风险)'),
    (r'exec(Sync)?\s*\(\s*[^)]*\+', 'exec 命令拼接'),
    (r'shell\s*:\s*true', '开启 shell 模式 (注入风险)'),
]

# 网络外发 / 隐藏上报模式 (3.5, 3.6)
NETWORK_EXFIL_PATTERNS = [
    (r'https?://', '探测到 HTTP(S) 网络请求'),
    (r'WebSocket|ws://|wss://', 'WebSocket 连接'),
    (r'fetch\s*\(', 'fetch 网络请求'),
    (r'axios\.(get|post|put|delete|request)\s*\(', 'axios 网络请求'),
    (r'http\.request|https\.request|http\.get|https\.get', 'Node http/https 请求'),
    (r'XMLHttpRequest|WebSocket|EventSource\s*\(', '浏览器网络 API'),
]

# 挖矿 / 远控 / 代理模式 (3.6)
MALICIOUS_NETWORK_PATTERNS = [
    (r'miner|mining|coinhive|cryptonight|stratum', '挖矿相关'),
    (r'reverse[_-]?shell|bind[_-]?shell|remote[_-]?control|teamviewer|anydesk', '远控/反向 shell'),
    (r'proxy[a-z]*\.js|proxy_pass|socks5|tor\.onion', '代理/隧道'),
    (r'ddos|syn[_-]?flood|udp[_-]?flood', 'DDoS 攻击'),
    (r'ransomware|keylogger|spyware|banking[_-]?trojan', '恶意软件'),
]


# 后门 / 隐藏逻辑模式 (4.5, 4.6)
BACKDOOR_PATTERNS = [
    (r'debugger\s*;', 'debugger 断点 (可能为调试后门)'),
    (r'process\.env\.(PORT|DEBUG_PORT|DEBUG)[A-Z_]*\s*=\s*', '动态设置调试端口'),
    (r'app\.listen\s*\(|server\.listen\s*\(|net\.createServer\s*\(', '开启监听端口'),
    (r'setInterval\s*\(|setTimeout\s*\(', '定时任务'),
    (r'cron\.schedule|cron\.job|node-cron', '定时任务 (cron)'),
    (r'fs\.(writeFile|writeFileSync|appendFile|appendFileSync|createWriteStream)\s*\(', '文件写入'),
    (r'fs\.(readFile|readFileSync|createReadStream)\s*\(', '文件读取'),
    (r'process\.exit\s*\(|process\.kill\s*\(', '进程控制'),
    (r'os\.tmpdir|tmp\[|\/tmp', '临时文件操作'),
]

# 系统配置修改 / 提权 (6.2, 6.1)
SYSTEM_MODIFY_PATTERNS = [
    (r'sudo\s+|require\([\'"]os[\'"]\)\.userInfo\(\)\.uid\s*==\s*0|process\.getuid\s*\(\s*\)\s*==\s*0', '要求 root/sudo 权限'),
    (r'\/etc\/|\/usr\/|\/System\/', '修改系统目录'),
    (r'launchctl|systemctl|service\s+.*\s+(start|stop|restart)|update-rc\.d|chkconfig', '创建开机自启/系统服务'),
    (r'/Library/LaunchAgents|/Library/LaunchDaemons|/etc/init\.d', '创建系统启动项'),
    (r'setx\s+|reg\s+add|sc\s+create', 'Windows 系统配置修改'),
]

# 文件窃取 / 静默上传 (4.6)
FILE_THEFT_PATTERNS = [
    (r'fs\.(readFile|readFileSync|createReadStream)\s*\([^)]*\)\s*\.?\s*(then|pipe|send|post|upload)', '读取文件后上传'),
    (r'formdata\.append|FormData\([^)]*\)\.append|new\s+FormData', 'FormData 上传'),
    (r'multipart|multipart/form-data', 'multipart 上传'),
    (r'aws-sdk|@aws-sdk|google-cloud|firebase-admin|supabase', '云服务 SDK (可能用于隐蔽上传)'),
    (r'upload|s3\.putObject|storage\.bucket|bucket\.upload', '云存储上传'),
]

# 混淆 / 加密脚本 (4.1)
OBFUSCATION_PATTERNS = [
    (r'atob\s*\(\s*[\'\"][A-Za-z0-9+/=]{30,}', 'base64 混淆字符串 (超长)'),
    (r'String\.fromCharCode\s*\(\s*\d+,\s*\d+', '字符混淆'),
    (r'\.replace\([^)]*,[^)]*charCodeAt|split\([\'\"]{2}\s*\)\s*\.map\s*\(\s*[\'\"]\\x', '十六进制混淆'),
    (r'\\x[0-9a-fA-F]{2}\\x[0-9a-fA-F]{2}\\x[0-9a-fA-F]{2}', '连续十六进制转义 (混淆)'),
    (r'["\'][A-Za-z0-9+/]{200,}=*["\']', '超长 base64 字符串'),
    (r'\_0x[a-f0-9]{4,}', 'JS 混淆器变量模式'),
]

ABANDON_MARKERS = ['停止维护', '不再更新', '不再维护', '不再支持', '弃用', 'deprecated', 'abandoned', 'no longer maintained', 'archived', 'discontinued', '不再活跃']


# ---------------------------------------------------------------------------
# 工具函数
# ---------------------------------------------------------------------------

class CheckResult:
    def __init__(self, item_id, title, check_type, result='⚠️  需人工复核', detail='', severity='info'):
        self.item_id = item_id
        self.title = title
        self.check_type = check_type  # '必查' or '推荐'
        self.result = result          # '✅ 通过' / '❌ 不通过' / '⚠️ 需人工复核' / '⬜ 不适用'
        self.detail = detail
        self.severity = severity      # critical / major / minor / info


def normalize_license(license_str):
    """规范化许可证字符串."""
    if not license_str:
        return ''
    return license_str.strip().lower().replace(' ', '-')


def is_mit_compatible(license_str):
    """检查许可证是否与 MIT 兼容."""
    lic = normalize_license(license_str)
    if lic in MIT_COMPATIBLE_LICENSES:
        return True
    for base in MIT_COMPATIBLE_LICENSES:
        if base in lic:
            return True
    return False


def is_gpl(license_str):
    """检查是否为 GPL 强传染协议."""
    lic = normalize_license(license_str)
    for g in GPL_LICENSES:
        if g in lic:
            return True
    return False


def run_cmd(cmd, cwd=None, timeout=120):
    """运行 shell 命令, 返回 (returncode, stdout, stderr)."""
    try:
        p = subprocess.run(
            cmd, shell=True, capture_output=True, text=True,
            cwd=cwd, timeout=timeout
        )
        return p.returncode, p.stdout, p.stderr
    except subprocess.TimeoutExpired:
        return -1, '', 'timeout'
    except Exception as e:
        return -1, '', str(e)


def extract_github_info(url):
    """从 GitHub/GitLab URL 提取 owner/repo 信息."""
    url = url.strip()
    patterns = [
        r'github\.com[/:]([\w.-]+)/([\w.-]+?)(?:\.git)?(?:/)?(?:$|[/?#])',
        r'gitlab\.com[/:]([\w.-]+)/([\w.-]+?)(?:\.git)?(?:/)?(?:$|[/?#])',
    ]
    for pat in patterns:
        m = re.search(pat, url)
        if m:
            return m.group(1), m.group(2)
    m = re.match(r'^([\w.-]+)/([\w.-]+?)(?:\.git)?$', url)
    if m:
        return m.group(1), m.group(2)
    return None, None


def http_get(url, token=None, timeout=30):
    """简单的 HTTP GET 请求."""
    req = urllib.request.Request(url, headers={'User-Agent': 'dsh-plugin-security-checker', 'Accept': 'application/vnd.github+json'})
    if token:
        req.add_header('Authorization', f'Bearer {token}')
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode('utf-8', errors='replace')
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8', errors='replace')
    except Exception as e:
        return -1, str(e)


def scan_file_content(content, patterns):
    """在文件内容中扫描匹配模式, 返回 [(pattern_desc, match_count, sample_line), ...]."""
    findings = []
    for pat, desc in patterns:
        matches = list(re.finditer(pat, content, re.IGNORECASE | re.MULTILINE))
        if matches:
            sample = matches[0].group(0)[:80] if matches else ''
            line_no = content[:matches[0].start()].count('\n') + 1
            findings.append((desc, len(matches), line_no, sample))
    return findings


def scan_file(path, patterns):
    """扫描单个文件的模式."""
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception:
        return []
    return scan_file_content(content, patterns)


def scan_directory(root, patterns, exclude_dirs=None):
    """递归扫描目录中的文件."""
    exclude_dirs = exclude_dirs or {'node_modules', '.git', 'dist', 'build', '.next', '.nuxt', '.output', 'coverage', '.cache', 'target', '__pycache__', '.venv', 'vendor'}
    all_findings = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
        for fn in filenames:
            if fn.endswith(('.min.js', '.map', '.lock', '.min.css')):
                continue
            full = os.path.join(dirpath, fn)
            if os.path.getsize(full) > 2 * 1024 * 1024:  # 跳过 >2MB 文件
                continue
            try:
                findings = scan_file(full, patterns)
                for desc, count, line, sample in findings:
                    all_findings.append((full, desc, count, line, sample))
            except Exception:
                continue
    return all_findings


def find_package_json(root):
    """在仓库中查找 package.json (优先仓库根, 也可在子目录)."""
    pkg = os.path.join(root, 'package.json')
    if os.path.exists(pkg):
        return [os.path.join(root, 'package.json')]
    results = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in {'node_modules', '.git'}]
        if 'package.json' in filenames:
            results.append(os.path.join(dirpath, 'package.json'))
            if len(results) > 20:
                break
    return results


def find_readme(root):
    """查找 README 文件."""
    for name in ['README.md', 'README.MD', 'README.rst', 'readme.md', 'Readme.md', 'README']:
        p = os.path.join(root, name)
        if os.path.exists(p):
            return p
    for dirpath, dirnames, filenames in os.walk(root):
        depth = dirpath[len(root):].count(os.sep)
        if depth > 2:
            continue
        dirnames[:] = [d for d in dirnames if d not in {'node_modules', '.git'}]
        for fn in filenames:
            if fn.lower().startswith('readme'):
                return os.path.join(dirpath, fn)
    return None


def find_license(root):
    """查找 LICENSE 文件."""
    for dirpath, dirnames, filenames in os.walk(root):
        depth = dirpath[len(root):].count(os.sep)
        if depth > 1:
            continue
        dirnames[:] = [d for d in dirnames if d not in {'node_modules', '.git'}]
        for fn in filenames:
            if fn.upper().startswith('LICENSE') or fn.upper().startswith('COPYING'):
                return os.path.join(dirpath, fn)
    return None


def read_file_safe(path, max_bytes=512 * 1024):
    """安全读取文件内容."""
    try:
        if os.path.getsize(path) > max_bytes:
            return ''
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    except Exception:
        return ''


def is_cordis_plugin(pkg_json):
    """判断是否为 Cordis/DSH 插件."""
    dsh = pkg_json.get('dsh', {})
    has_dsh = bool(dsh)
    has_cordis_dep = any(k.startswith('@deepseek-ai/cordis') or 'cordis' in k for k in pkg_json.get('dependencies', {}))
    has_cordis_peer = any(k.startswith('@deepseek-ai/cordis') or 'cordis' in k for k in pkg_json.get('peerDependencies', {}))
    return has_dsh or has_cordis_dep or has_cordis_peer


def parse_github_repo_info(owner, repo, token=None):
    """通过 GitHub API 获取仓库及作者信息."""
    base_url = f'https://api.github.com/repos/{owner}/{repo}'
    status, body = http_get(base_url, token)
    if status != 200:
        return None, f'GitHub API 请求失败 (HTTP {status}): {body[:200]}'
    try:
        repo_info = json.loads(body)
    except json.JSONDecodeError:
        return None, f'GitHub API 返回无效 JSON: {body[:200]}'

    # 获取作者信息
    owner_name = repo_info.get('owner', {}).get('login', '')
    owner_url = f'https://api.github.com/users/{owner_name}'
    status2, body2 = http_get(owner_url, token)
    owner_info = None
    if status2 == 200:
        try:
            owner_info = json.loads(body2)
        except json.JSONDecodeError:
            pass

    # 获取最近提交
    commits_url = f'https://api.github.com/repos/{owner}/{repo}/commits?per_page=5'
    status3, body3 = http_get(commits_url, token)
    commits = []
    if status3 == 200:
        try:
            commits = json.loads(body3)
        except json.JSONDecodeError:
            pass

    return {
        'repo': repo_info,
        'owner': owner_info,
        'commits': commits,
    }, None


def get_git_tags(repo_dir):
    """获取仓库 git tags."""
    rc, out, _ = run_cmd('git tag --sort=-version:refname | head -20', cwd=repo_dir)
    if rc != 0:
        return []
    return [t.strip() for t in out.strip().split('\n') if t.strip()]


def get_git_commit_count(repo_dir):
    """获取 git 提交数量."""
    rc, out, _ = run_cmd('git rev-list --count HEAD', cwd=repo_dir)
    if rc == 0:
        try:
            return int(out.strip())
        except ValueError:
            return -1
    return -1


def get_repo_age_days(repo_dir):
    """获取仓库最早提交距今的天数."""
    rc, out, _ = run_cmd("git log --reverse --format='%aI' | head -1", cwd=repo_dir)
    if rc == 0 and out.strip():
        try:
            first_commit = datetime.fromisoformat(out.strip().replace('Z', '+00:00'))
            if first_commit.tzinfo:
                now = datetime.now(timezone.utc)
                return (now - first_commit).days
        except Exception:
            pass
    return -1


def get_last_commit_days(repo_dir):
    """获取最近一次提交距今的天数."""
    rc, out, _ = run_cmd("git log -1 --format='%aI'", cwd=repo_dir)
    if rc == 0 and out.strip():
        try:
            last_commit = datetime.fromisoformat(out.strip().replace('Z', '+00:00'))
            if last_commit.tzinfo:
                now = datetime.now(timezone.utc)
                return (now - last_commit).days
        except Exception:
            pass
    return -1


# ---------------------------------------------------------------------------
# 主校验逻辑
# ---------------------------------------------------------------------------

class PluginValidator:
    """DSH 插件安全校验器."""

    def __init__(self, url, token=None, keep=False, no_clone=False):
        self.url = url
        self.token = token
        self.keep = keep
        self.no_clone = no_clone
        self.owner = None
        self.repo = None
        self.repo_dir = None
        self.temp_dir = None
        self.results = []
        self.repo_info = None
        self.repo_meta = None
        self.owner_meta = None
        self.commits = []

    def add_result(self, item_id, title, check_type, result, detail='', severity='info'):
        self.results.append(CheckResult(item_id, title, check_type, result, detail, severity))

    def setup(self):
        """解析 URL 并准备克隆."""
        self.owner, self.repo = extract_github_info(self.url)
        if not self.owner or not self.repo:
            raise ValueError(f'无法从 URL 解析 GitHub/GitLab 仓库信息: {self.url}')

        # 尝试通过 API 获取仓库元数据
        try:
            self.repo_meta, err = parse_github_repo_info(self.owner, self.repo, self.token)
            if err:
                print(f'[info] GitHub API: {err}', file=sys.stderr)
            if self.repo_meta:
                self.repo_info = self.repo_meta['repo']
                self.owner_meta = self.repo_meta['owner']
                self.commits = self.repo_meta['commits']
        except Exception as e:
            print(f'[warn] 获取 GitHub 元数据失败: {e}', file=sys.stderr)

        if not self.no_clone:
            self.temp_dir = tempfile.mkdtemp(prefix='dsh-plugin-check-')
            clone_url = f'https://github.com/{self.owner}/{self.repo}.git'
            print(f'[info] 正在克隆仓库: {clone_url}')
            rc, out, err = run_cmd(f'git clone --depth 1 {clone_url} {self.temp_dir}/repo', timeout=180)
            if rc != 0:
                rc, out, err = run_cmd(f'git clone {clone_url} {self.temp_dir}/repo', timeout=300)
            if rc != 0:
                raise RuntimeError(f'克隆仓库失败: {err[:500]}')
            self.repo_dir = os.path.join(self.temp_dir, 'repo')

            # 获取完整 git 历史
            run_cmd('git fetch --unshallow', cwd=self.repo_dir, timeout=120)

    def cleanup(self):
        """清理临时目录."""
        if self.temp_dir and not self.keep:
            shutil.rmtree(self.temp_dir, ignore_errors=True)

    def run_all_checks(self):
        """运行所有检查项."""
        self.check_1_1_source_platform()
        self.check_1_2_author()
        self.check_1_3_license()
        self.check_1_4_function_consistency()
        self.check_1_5_legal_compliance()
        self.check_1_6_version_release()

        self.check_2_1_dsh_version()
        self.check_2_2_cordis_spec()
        self.check_2_3_exception_handling()
        self.check_2_4_cleanup()
        self.check_2_5_init_performance()
        self.check_2_6_resource_usage()
        self.check_2_7_conflicts()

        self.check_3_1_file_permissions()
        self.check_3_2_global_file_access()
        self.check_3_3_command_execution()
        self.check_3_4_command_injection()
        self.check_3_5_network()
        self.check_3_6_malicious_network()
        self.check_3_7_sensitive_config()
        self.check_3_8_config_modification()

        self.check_4_1_obfuscation()
        self.check_4_2_dangerous_api()
        self.check_4_3_npm_audit()
        self.check_4_4_deprecated_deps()
        self.check_4_5_backdoors()
        self.check_4_6_file_theft()
        self.check_4_7_dependency_count()
        self.check_4_8_code_quality()
        self.check_4_9_tests()

        self.check_5_1_local_processing()
        self.check_5_2_data_reporting()
        self.check_5_3_sensitive_storage()
        self.check_5_4_unauthorized_access()
        self.check_5_5_logging()
        self.check_5_6_data_cleanup()

        self.check_6_1_privileges()
        self.check_6_2_system_config()
        self.check_6_3_sandbox()
        self.check_6_4_memory_leaks()
        self.check_6_5_temp_cleanup()

        self.check_7_1_maintenance()
        self.check_7_2_abandonment()
        self.check_7_3_security_feedback()
        self.check_7_4_response_time()
        self.check_7_5_documentation()
        self.check_7_6_community()


    # --- 一、基础准入审计 ---

    def check_1_1_source_platform(self):
        """1.1 插件源码托管于 GitHub/GitLab 等公开可追溯平台"""
        if self.owner and self.repo:
            is_github = 'github.com' in self.url or ('github' in self.url.lower())
            is_gitlab = 'gitlab.com' in self.url or ('gitlab' in self.url.lower())
            # Support bare "owner/repo" format - default to GitHub
            if not self.url.startswith(('http://', 'https://', 'git@', 'ssh://')):
                is_github = True
            if is_github or is_gitlab:
                detail_parts = []
                if self.repo_info:
                    if self.repo_info.get('private'):
                        detail_parts.append('⚠️ 仓库为私有')
                    else:
                        detail_parts.append('✅ 仓库公开')
                    if self.repo_info.get('archived'):
                        detail_parts.append('⚠️ 仓库已归档')
                    if self.repo_info.get('default_branch'):
                        detail_parts.append(f"默认分支: {self.repo_info['default_branch']}")
                if detail_parts:
                    detail = '; '.join(detail_parts)
                else:
                    detail = f'来源: {self.url}'
                self.add_result('1.1', '源码托管于公开可追溯平台', '必查', '✅ 通过', detail)
            else:
                self.add_result('1.1', '源码托管于公开可追溯平台', '必查', '❌ 不通过',
                                f'来源 URL: {self.url} — 仅支持 GitHub/GitLab 等公开平台', 'critical')
        else:
            self.add_result('1.1', '源码托管于公开可追溯平台', '必查', '❌ 不通过', '无法解析仓库信息', 'critical')

    def check_1_2_author(self):
        """1.2 发布账号非匿名一次性账号, 有可追溯的开源贡献记录"""
        if not self.owner_meta:
            if self.repo_dir:
                rc, out, _ = run_cmd('git log --format="%an|%ae" | sort | uniq -c | sort -rn | head -5', cwd=self.repo_dir)
                authors = out.strip().split('\n') if rc == 0 else []
                if authors:
                    detail = '本地提交者: ' + '; '.join(a.strip() for a in authors[:3] if a.strip())
                    self.add_result('1.2', '发布账号非匿名一次性账号', '必查', '⚠️  需人工复核',
                                    detail + ' — 无 GitHub API 信息, 建议人工确认账号可信度')
                else:
                    self.add_result('1.2', '发布账号非匿名一次性账号', '必查', '⚠️  需人工复核', '无法获取作者信息')
            else:
                self.add_result('1.2', '发布账号非匿名一次性账号', '必查', '⚠️  需人工复核',
                                '无克隆仓库, 且 GitHub API 不可用')
            return

        created_at = self.owner_meta.get('created_at', '')
        public_repos = self.owner_meta.get('public_repos', 0)
        followers = self.owner_meta.get('followers', 0)

        detail_parts = []
        issues = []

        account_age_days = -1
        if created_at:
            try:
                created_dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                if created_dt.tzinfo:
                    account_age_days = (datetime.now(timezone.utc) - created_dt).days
            except Exception:
                pass

        if account_age_days >= 0:
            detail_parts.append(f"账号注册: {created_at[:10]} ({account_age_days} 天前)")
            if account_age_days < 30:
                issues.append(f'⚠️ 账号注册不足 30 天 ({account_age_days} 天)')
        else:
            issues.append('⚠️ 无法获取账号注册时间')

        detail_parts.append(f"公开仓库数: {public_repos}")
        detail_parts.append(f"粉丝数: {followers}")

        if public_repos < 1 and followers < 1:
            issues.append('⚠️ 疑似一次性账号 (无公开仓库、无关注者)')

        if issues:
            detail = '; '.join(detail_parts) + '; ' + '; '.join(issues)
            self.add_result('1.2', '发布账号非匿名一次性账号', '必查', '⚠️  需人工复核', detail)
        else:
            detail = '; '.join(detail_parts)
            self.add_result('1.2', '发布账号非匿名一次性账号', '必查', '✅ 通过', detail)

    def check_1_3_license(self):
        """1.3 开源协议与 DSH 主框架 (MIT) 兼容"""
        if not self.repo_dir:
            self.add_result('1.3', '开源协议与 MIT 兼容', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查许可证')
            return

        license_str = None
        pkg_files = find_package_json(self.repo_dir)
        if pkg_files:
            try:
                with open(pkg_files[0], 'r', encoding='utf-8') as f:
                    pkg = json.load(f)
                license_str = pkg.get('license') or pkg.get('licenses')
                if isinstance(license_str, list):
                    license_str = ','.join(l.get('type', '') for l in license_str)
            except Exception:
                pass

        license_file = find_license(self.repo_dir)
        license_file_name = ''
        if license_file:
            license_file_name = os.path.basename(license_file)
            content = read_file_safe(license_file)
            if license_str is None and content:
                low = content.lower()
                if 'mit license' in low or 'permission is hereby granted' in low:
                    license_str = 'MIT'
                elif 'apache license' in low:
                    license_str = 'Apache-2.0'
                elif 'gnu general public license' in low:
                    if 'version 3' in low:
                        license_str = 'GPL-3.0'
                    elif 'version 2' in low:
                        license_str = 'GPL-2.0'
                elif 'bsd' in low:
                    license_str = 'BSD'

        if not license_str:
            self.add_result('1.3', '开源协议与 MIT 兼容', '必查', '❌ 不通过',
                            '未找到许可证声明 (package.json 无 license 字段且无 LICENSE 文件)', 'critical')
            return

        if is_gpl(str(license_str)):
            self.add_result('1.3', '开源协议与 MIT 兼容', '必查', '❌ 不通过',
                            f'许可证: {license_str} — GPL 强传染协议, 商用场景禁止', 'critical')
        elif is_mit_compatible(str(license_str)):
            self.add_result('1.3', '开源协议与 MIT 兼容', '必查', '✅ 通过',
                            f'许可证: {license_str}' + (f' (来自 {license_file_name})' if license_file_name else ''))
        else:
            self.add_result('1.3', '开源协议与 MIT 兼容', '必查', '⚠️  需人工复核',
                            f'许可证: {license_str} — 需确认与 MIT 兼容性')

    def check_1_4_function_consistency(self):
        """1.4 插件核心功能与 README 描述一致"""
        if not self.repo_dir:
            self.add_result('1.4', '核心功能与 README 描述一致', '必查', '⚠️  需人工复核', '未克隆仓库, 无法比对')
            return

        readme = find_readme(self.repo_dir)
        pkg_files = find_package_json(self.repo_dir)
        pkg_desc = ''
        pkg_name = ''
        if pkg_files:
            try:
                with open(pkg_files[0], 'r', encoding='utf-8') as f:
                    pkg = json.load(f)
                pkg_desc = pkg.get('description', '') or ''
                pkg_name = pkg.get('name', '') or ''
            except Exception:
                pass

        if readme and pkg_files:
            readme_content = read_file_safe(readme).lower()
            word_count = len(read_file_safe(readme).split())
            detail_parts = [f'README 字数: {word_count}']
            if pkg_name:
                detail_parts.append(f'包名: {pkg_name}')
            if pkg_desc:
                detail_parts.append(f'描述: {pkg_desc[:80]}')

            has_features = any(kw in readme_content for kw in ['feature', '功能', 'usage', '使用', 'install', '安装', 'example', '示例', 'config', '配置'])
            if has_features and word_count < 30:
                self.add_result('1.4', '核心功能与 README 描述一致', '必查', '⚠️  需人工复核',
                                '; '.join(detail_parts) + ' — README 内容较少, 需人工比对')
            elif has_features:
                self.add_result('1.4', '核心功能与 README 描述一致', '必查', '✅ 通过',
                                '; '.join(detail_parts) + ' — README 包含功能/使用说明')
            else:
                self.add_result('1.4', '核心功能与 README 描述一致', '必查', '⚠️  需人工复核',
                                '; '.join(detail_parts) + ' — README 缺少功能/使用说明, 需人工比对')
        elif readme:
            self.add_result('1.4', '核心功能与 README 描述一致', '必查', '⚠️  需人工复核',
                            f'找到 README: {os.path.basename(readme)}, 但未找到 package.json')
        else:
            self.add_result('1.4', '核心功能与 README 描述一致', '必查', '⚠️  需人工复核', '未找到 README, 无法自动比对')

    def check_1_5_legal_compliance(self):
        """1.5 插件功能不违反法律法规"""
        if not self.repo_dir:
            self.add_result('1.5', '不违反法律法规', '必查', '⚠️  需人工复核', '未克隆仓库, 无法自动检查')
            return

        illegal_patterns = [
            (r'crack\s*\(|keygen|serial\s*key|activation\s*code\s*bypass|license\s*bypass', '破解授权'),
            (r'scrap(e|ing)?\s*\(|web\s*scrap|爬虫|爬取', '非法爬取'),
            (r'bypass\s+(auth|login|password|permission|rate\s*limit)|绕过(权限|认证|登录)', '绕过权限限制'),
            (r'steal\s*(password|credential|token|api)|窃取(密码|凭证|数据)', '窃取数据'),
            (r'phishing|钓鱼|fraud|诈骗|money\s*launder', '欺诈行为'),
            (r'pirat|盗版|侵权|copyright\s*infring', '盗版/侵权'),
        ]
        findings = scan_directory(self.repo_dir, illegal_patterns)
        if findings:
            detail_lines = []
            for full, desc, count, line, sample in findings[:5]:
                rel = os.path.relpath(full, self.repo_dir)
                detail_lines.append(f'  - {rel}:{line} → {desc} ({count} 处)')
            detail = '检测到潜在违规模式:\n' + '\n'.join(detail_lines)
            if len(findings) > 5:
                detail += f'\n  ... 共 {len(findings)} 处'
            self.add_result('1.5', '不违反法律法规', '必查', '❌ 不通过', detail, 'critical')
        else:
            self.add_result('1.5', '不违反法律法规', '必查', '✅ 通过', '未检测到明显的违法违规模式')

    def check_1_6_version_release(self):
        """1.6 插件有明确的版本号与正式 Release 版本 (推荐)"""
        result = '⚠️  需人工复核'
        detail_parts = []

        tag_count = 0
        if self.repo_dir:
            tags = get_git_tags(self.repo_dir)
            tag_count = len(tags)
            if tags:
                detail_parts.append(f"Git tags ({tag_count}): {', '.join(tags[:5])}")
            else:
                detail_parts.append('无 git tag')

        pkg_version = None
        if self.repo_dir:
            pkg_files = find_package_json(self.repo_dir)
            if pkg_files:
                try:
                    with open(pkg_files[0], 'r', encoding='utf-8') as f:
                        pkg = json.load(f)
                    pkg_version = pkg.get('version')
                    if pkg_version:
                        detail_parts.append(f"package.json version: {pkg_version}")
                except Exception:
                    pass

        release_count = 0
        if self.owner and self.repo:
            rel_url = f'https://api.github.com/repos/{self.owner}/{self.repo}/releases?per_page=5'
            status, body = http_get(rel_url, self.token)
            if status == 200:
                try:
                    releases = json.loads(body)
                    release_count = len(releases)
                    if releases:
                        release_names = [r.get('tag_name', '') for r in releases if r.get('tag_name')]
                        detail_parts.append(f"GitHub Releases ({release_count}): {', '.join(release_names[:5])}")
                except Exception:
                    pass

        if pkg_version and (tag_count > 0 or release_count > 0):
            result = '✅ 通过'
        elif pkg_version:
            result = '⚠️  需人工复核'
            detail_parts.append('有版本号但无 git tag / release')
        else:
            result = '⚠️  需人工复核'
            detail_parts.append('未发现版本信息')

        self.add_result('1.6', '有明确的版本号与正式 Release', '推荐', result, '; '.join(detail_parts))


    # --- 二、技术规范审计 ---

    def check_2_1_dsh_version(self):
        """2.1 明确标注支持的 DSH 核心版本范围"""
        if not self.repo_dir:
            self.add_result('2.1', '明确标注支持的 DSH 版本范围', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        pkg_files = find_package_json(self.repo_dir)
        details = []
        found = False
        for pf in pkg_files:
            try:
                with open(pf, 'r', encoding='utf-8') as f:
                    pkg = json.load(f)
                deps = {**pkg.get('dependencies', {}), **pkg.get('peerDependencies', {})}
                for name, ver in deps.items():
                    if 'cordis' in name.lower() or 'dsh' in name.lower():
                        details.append(f"{name}: {ver}")
                        found = True
                engines = pkg.get('engines', {})
                if engines:
                    details.append(f"engines: {json.dumps(engines)}")
                    found = True
            except Exception:
                continue

        if found:
            self.add_result('2.1', '明确标注支持的 DSH 版本范围', '必查', '✅ 通过', '; '.join(details[:5]))
        else:
            self.add_result('2.1', '明确标注支持的 DSH 版本范围', '必查', '❌ 不通过',
                            '未在 package.json 中发现 DSH/Cordis 依赖或 engines 字段', 'major')

    def check_2_2_cordis_spec(self):
        """2.2 严格遵循 Cordis 插件开发规范"""
        if not self.repo_dir:
            self.add_result('2.2', '遵循 Cordis 插件开发规范', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        pkg_files = find_package_json(self.repo_dir)
        cordis_markers = []
        dsh_field = None
        for pf in pkg_files:
            try:
                with open(pf, 'r', encoding='utf-8') as f:
                    pkg = json.load(f)
                dsh = pkg.get('dsh')
                if dsh:
                    dsh_field = dsh
                deps = {**pkg.get('dependencies', {}), **pkg.get('peerDependencies', {})}
                for name in deps:
                    if 'cordis' in name.lower() or 'dsh' in name.lower():
                        cordis_markers.append(name)
            except Exception:
                continue

        cordis_files = []
        for root_dir, _, files in os.walk(self.repo_dir):
            depth = root_dir[len(self.repo_dir):].count(os.sep)
            if depth > 3:
                continue
            for fn in files:
                if fn.endswith(('.yml', '.yaml')) and ('cordis' in fn.lower() or 'dsh' in fn.lower()):
                    cordis_files.append(os.path.join(root_dir, fn))
            if depth > 2:
                break

        details = []
        if dsh_field is not None:
            details.append(f"dsh 配置: {json.dumps(dsh_field)[:100]}")
        if cordis_markers:
            details.append(f"Cordis/DSH 依赖: {', '.join(cordis_markers[:5])}")
        if cordis_files:
            details.append(f"Cordis 配置文件: {', '.join(os.path.basename(f) for f in cordis_files[:3])}")

        # 检查是否有修改内核源码 / hack 行为
        hack_patterns = [
            (r'patch\s*\(.*\)|monkey[-_ ]?patch|prototype pollution|\b__proto__\b|constructor\.prototype', 'Monkey patch / prototype pollution'),
            (r'process\.binding|require\([\'"]fs[\'"]\)\.readFileSync\([\'"].*node_modules.*@deepseek-ai.*[\'"]\)', '直接修改内核源码'),
        ]
        hack_findings = scan_directory(self.repo_dir, hack_patterns) if self.repo_dir else []

        if dsh_field is not None or (cordis_markers and (cordis_files or True)):
            if hack_findings:
                detail = '; '.join(details) if details else ''
                for full, desc, count, line, sample in hack_findings[:3]:
                    rel = os.path.relpath(full, self.repo_dir)
                    detail += f"\n  - {rel}:{line} → {desc}"
                self.add_result('2.2', '遵循 Cordis 插件开发规范', '必查', '⚠️  需人工复核',
                                detail + ' — 发现潜在 hack 模式, 需人工确认')
            else:
                detail = '; '.join(details) if details else '检测到 Cordis 相关配置'
                self.add_result('2.2', '遵循 Cordis 插件开发规范', '必查', '✅ 通过', detail)
        else:
            self.add_result('2.2', '遵循 Cordis 插件开发规范', '必查', '❌ 不通过',
                            '未检测到 Cordis 插件特征 (无 dsh 字段, 无 cordis 依赖)', 'major')

    def check_2_3_exception_handling(self):
        """2.3 核心逻辑具备异常捕获机制"""
        if not self.repo_dir:
            self.add_result('2.3', '具备异常捕获机制', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        source_files = []
        for dirpath, dirnames, filenames in os.walk(self.repo_dir):
            dirnames[:] = [d for d in dirnames if d not in {'node_modules', '.git', 'dist', 'build'}]
            for fn in filenames:
                if fn.endswith(('.js', '.ts', '.mjs', '.cjs', '.py')):
                    source_files.append(os.path.join(dirpath, fn))

        total_try_catch = 0
        total_funcs = 0
        for sf in source_files:
            try:
                content = read_file_safe(sf)
                if not content:
                    continue
                total_try_catch += len(re.findall(r'try\s*\{|catch\s*\(', content))
                total_funcs += len(re.findall(r'(?:function|=>|async\s+function)', content))
            except Exception:
                continue

        if total_funcs > 0:
            ratio = total_try_catch / total_funcs
            detail = f"try/catch: {total_try_catch} 处, 函数: {total_funcs} 个, 比例: {ratio:.1%}"
            if total_try_catch == 0:
                self.add_result('2.3', '具备异常捕获机制', '必查', '❌ 不通过',
                                detail + ' — 未检测到任何 try/catch', 'major')
            elif ratio < 0.1:
                self.add_result('2.3', '具备异常捕获机制', '必查', '⚠️  需人工复核',
                                detail + ' — try/catch 覆盖比例较低')
            else:
                self.add_result('2.3', '具备异常捕获机制', '必查', '✅ 通过', detail)
        else:
            self.add_result('2.3', '具备异常捕获机制', '必查', '⚠️  需人工复核', '未检测到 JS/TS/Python 源文件')

    def check_2_4_cleanup(self):
        """2.4 禁用/卸载后可完整释放定时器、事件监听、临时文件"""
        if not self.repo_dir:
            self.add_result('2.4', '卸载后完整释放资源', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        source_files = []
        for dirpath, dirnames, filenames in os.walk(self.repo_dir):
            dirnames[:] = [d for d in dirnames if d not in {'node_modules', '.git', 'dist', 'build'}]
            for fn in filenames:
                if fn.endswith(('.js', '.ts', '.mjs', '.cjs')):
                    source_files.append(os.path.join(dirpath, fn))

        has_cleanup = False
        has_timers = False
        details = []

        for sf in source_files:
            content = read_file_safe(sf)
            if not content:
                continue
            if re.search(r'dispose\s*\(|\.dispose\b|stop\s*\(|cleanup\s*\(|onStop|beforeUnload|teardown\s*\(|\.unmount\s*\(', content, re.IGNORECASE):
                has_cleanup = True
                details.append(f"发现清理逻辑: {os.path.relpath(sf, self.repo_dir)}")
            if re.search(r'setInterval\s*\(|setTimeout\s*\(', content):
                has_timers = True

        if has_cleanup:
            self.add_result('2.4', '卸载后完整释放资源', '必查', '✅ 通过',
                            '; '.join(details[:3]) or '检测到清理逻辑')
        elif not has_timers:
            self.add_result('2.4', '卸载后完整释放资源', '必查', '✅ 通过', '未使用定时器, 无资源释放问题')
        else:
            self.add_result('2.4', '卸载后完整释放资源', '必查', '⚠️  需人工复核',
                            '使用了定时器但未发现清理逻辑, 需人工确认')

    def check_2_5_init_performance(self):
        """2.5 插件初始化耗时 ≤ 500ms (推荐)"""
        self.add_result('2.5', '初始化耗时 ≤ 500ms', '推荐', '⚠️  需人工复核', '静态分析无法测量, 需在运行环境中实测')

    def check_2_6_resource_usage(self):
        """2.6 空闲运行状态下内存/CPU 占用 (推荐)"""
        self.add_result('2.6', '空闲内存 ≤ 50MB, 无异常 CPU', '推荐', '⚠️  需人工复核', '静态分析无法测量, 需在运行环境中实测')

    def check_2_7_conflicts(self):
        """2.7 与 DSH 官方/主流插件无已知功能冲突 (推荐)"""
        self.add_result('2.7', '与官方/主流插件无功能冲突', '推荐', '⚠️  需人工复核',
                        '需人工比对 DSH 官方插件及主流社区插件')


    # --- 三、权限安全审计 ---

    def check_3_1_file_permissions(self):
        """3.1 文件系统权限最小化"""
        if not self.repo_dir:
            self.add_result('3.1', '文件系统权限最小化', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        findings = scan_directory(self.repo_dir, SENSITIVE_PATH_PATTERNS)
        if findings:
            detail_lines = []
            for full, desc, count, line, sample in findings[:5]:
                rel = os.path.relpath(full, self.repo_dir)
                detail_lines.append(f'  - {rel}:{line} → {desc} ({count} 处)')
            detail = '检测到敏感路径访问:\n' + '\n'.join(detail_lines)
            if len(findings) > 5:
                detail += f'\n  ... 共 {len(findings)} 处'
            self.add_result('3.1', '文件系统权限最小化', '必查', '❌ 不通过', detail, 'critical')
        else:
            self.add_result('3.1', '文件系统权限最小化', '必查', '✅ 通过', '未检测到敏感路径访问模式')

    def check_3_2_global_file_access(self):
        """3.2 无全局文件读写、跨目录遍历能力"""
        if not self.repo_dir:
            self.add_result('3.2', '无全局文件读写', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        global_fs_patterns = [
            (r'fs\.(readFile|readFileSync|writeFile|writeFileSync|appendFile|appendFileSync|createReadStream|createWriteStream|unlink|unlinkSync|rm|rmSync|rename|renameSync|copyFile|copyFileSync)\s*\(\s*[\'\"](?:/|~|\.\./)', '访问绝对路径/上级目录'),
            (r'fs\.(readdir|readdirSync|opendir|opendirSync|watch|watchFile)\s*\(', '目录遍历'),
            (r'userInfo\(\)|homedir\(\)', '读取用户主目录'),
            (r'path\.resolve\s*\(\s*[\'\"][\'\"],\s*\.\.', '路径穿越'),
            (r'\.\.\/\.\.\/|\.\.\/\.\.\\|\.\.\\\.\.\\', '深层目录穿越'),
            (r'glob\s*\(\s*[\'\"](?:/|~|\*\*)', '全局文件匹配'),
        ]
        findings = scan_directory(self.repo_dir, global_fs_patterns)
        if findings:
            detail_lines = []
            for full, desc, count, line, sample in findings[:5]:
                rel = os.path.relpath(full, self.repo_dir)
                detail_lines.append(f'  - {rel}:{line} → {desc} ({count} 处)')
            detail = '检测到全局文件访问:\n' + '\n'.join(detail_lines)
            if len(findings) > 5:
                detail += f'\n  ... 共 {len(findings)} 处'
            self.add_result('3.2', '无全局文件读写', '必查', '⚠️  需人工复核',
                            detail + ' — 需人工判断是否有业务必要性')
        else:
            self.add_result('3.2', '无全局文件读写', '必查', '✅ 通过', '未检测到全局文件访问模式')

    def check_3_3_command_execution(self):
        """3.3 无无限制的系统命令执行"""
        if not self.repo_dir:
            self.add_result('3.3', '无无限制系统命令执行', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        findings = scan_directory(self.repo_dir, [
            (r'child_process\.(exec|execSync|spawn|spawnSync|fork|execFile|execFileSync)\s*\(', 'child_process 命令执行'),
            (r'require\([\'"]child_process[\'"]\)|from[\s\S]{0,10}[\'"]child_process[\'"]', '加载 child_process'),
            (r'process\.(exec|spawn|system)\s*\(', '进程执行'),
            (r'subprocess\.(run|call|Popen|check_output|check_call)\s*\(', 'Python subprocess'),
            (r'os\.system\s*\(', 'os.system 命令执行'),
        ])
        if findings:
            detail_lines = []
            for full, desc, count, line, sample in findings[:5]:
                rel = os.path.relpath(full, self.repo_dir)
                detail_lines.append(f'  - {rel}:{line} → {desc} ({count} 处)')
            detail = '检测到命令执行:\n' + '\n'.join(detail_lines)
            if len(findings) > 5:
                detail += f'\n  ... 共 {len(findings)} 处'
            # 检查是否有白名单机制
            has_whitelist = scan_directory(self.repo_dir, [
                (r'allowlist|whitelist|command\s*list|allowed\s*commands|白名单', '命令白名单'),
            ])
            if has_whitelist:
                detail += '\n⚠️ 检测到可能存在命令白名单机制, 需人工确认'
                self.add_result('3.3', '无无限制系统命令执行', '必查', '⚠️  需人工复核', detail)
            else:
                self.add_result('3.3', '无无限制系统命令执行', '必查', '❌ 不通过', detail, 'critical')
        else:
            self.add_result('3.3', '无无限制系统命令执行', '必查', '✅ 通过', '未检测到命令执行调用')

    def check_3_4_command_injection(self):
        """3.4 命令执行逻辑无注入风险"""
        if not self.repo_dir:
            self.add_result('3.4', '无命令注入风险', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        findings = scan_directory(self.repo_dir, COMMAND_INJECTION_PATTERNS)
        if findings:
            detail_lines = []
            for full, desc, count, line, sample in findings[:5]:
                rel = os.path.relpath(full, self.repo_dir)
                detail_lines.append(f'  - {rel}:{line} → {desc} ({count} 处)')
            detail = '检测到命令注入风险:\n' + '\n'.join(detail_lines)
            if len(findings) > 5:
                detail += f'\n  ... 共 {len(findings)} 处'
            self.add_result('3.4', '无命令注入风险', '必查', '❌ 不通过', detail, 'critical')
        else:
            self.add_result('3.4', '无命令注入风险', '必查', '✅ 通过', '未检测到命令注入模式')

    def check_3_5_network(self):
        """3.5 所有对外网络请求的域名、用途明确"""
        if not self.repo_dir:
            self.add_result('3.5', '对外网络请求域名明确', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        findings = scan_directory(self.repo_dir, NETWORK_EXFIL_PATTERNS)
        if findings:
            urls = set()
            for dirpath, dirnames, filenames in os.walk(self.repo_dir):
                dirnames[:] = [d for d in dirnames if d not in {'node_modules', '.git', 'dist', 'build'}]
                for fn in filenames:
                    if fn.endswith(('.js', '.ts', '.mjs', '.cjs', '.py', '.html', '.md', '.json')):
                        content = read_file_safe(os.path.join(dirpath, fn))
                        for m in re.finditer(r'https?://([\w.-]+)', content):
                            urls.add(m.group(1))

            detail_lines = []
            for full, desc, count, line, sample in findings[:5]:
                rel = os.path.relpath(full, self.repo_dir)
                detail_lines.append(f'  - {rel}:{line} → {desc} ({count} 处)')
            detail = '检测到网络请求:\n' + '\n'.join(detail_lines)
            if urls:
                detail += '\n涉及的域名: ' + ', '.join(sorted(urls)[:10])
                if len(urls) > 10:
                    detail += f' (+{len(urls)-10} 更多)'
            detail += '\n需人工确认每个网络请求的用途是否明确'
            self.add_result('3.5', '对外网络请求域名明确', '必查', '⚠️  需人工复核', detail)
        else:
            self.add_result('3.5', '对外网络请求域名明确', '必查', '✅ 通过', '未检测到网络请求模式')

    def check_3_6_malicious_network(self):
        """3.6 无恶意网络逻辑"""
        if not self.repo_dir:
            self.add_result('3.6', '无恶意网络逻辑', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        findings = scan_directory(self.repo_dir, MALICIOUS_NETWORK_PATTERNS)
        if findings:
            detail_lines = []
            for full, desc, count, line, sample in findings[:5]:
                rel = os.path.relpath(full, self.repo_dir)
                detail_lines.append(f'  - {rel}:{line} → {desc} ({count} 处)')
            detail = '检测到恶意网络模式:\n' + '\n'.join(detail_lines)
            if len(findings) > 5:
                detail += f'\n  ... 共 {len(findings)} 处'
            self.add_result('3.6', '无恶意网络逻辑', '必查', '❌ 不通过', detail, 'critical')
        else:
            self.add_result('3.6', '无恶意网络逻辑', '必查', '✅ 通过', '未检测到挖矿/远控/代理等恶意网络模式')

    def check_3_7_sensitive_config(self):
        """3.7 不读取全局会话历史、API Key 等敏感配置"""
        if not self.repo_dir:
            self.add_result('3.7', '不读取敏感配置', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        findings = scan_directory(self.repo_dir, SENSITIVE_CONFIG_PATTERNS)
        if findings:
            detail_lines = []
            for full, desc, count, line, sample in findings[:5]:
                rel = os.path.relpath(full, self.repo_dir)
                detail_lines.append(f'  - {rel}:{line} → {desc} ({count} 处)')
            detail = '检测到敏感配置读取:\n' + '\n'.join(detail_lines)
            if len(findings) > 5:
                detail += f'\n  ... 共 {len(findings)} 处'
            self.add_result('3.7', '不读取敏感配置', '必查', '⚠️  需人工复核',
                            detail + ' — 需人工判断是否读取的是当前会话上下文')
        else:
            self.add_result('3.7', '不读取敏感配置', '必查', '✅ 通过', '未检测到敏感配置读取模式')

    def check_3_8_config_modification(self):
        """3.8 不未经授权篡改全局配置"""
        if not self.repo_dir:
            self.add_result('3.8', '不篡改全局配置', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        config_modify_patterns = [
            (r'(?:ctx|app|global|config)\.(?:set|update|modify|write|save)\s*\(', '修改全局配置'),
            (r'\.settings\.(?:set|update|put|write)\s*\(', '修改设置'),
            (r'\.config\.(?:set|update|put|write|assign)\s*\(', '修改配置'),
            (r'writeFile(Sync)?\s*\([^)]*(?:settings|config|\.dsh)', '写入配置文件'),
            (r'fs\.(?:writeFile|writeFileSync)\s*\([^)]*(?:\.dsh|settings|config)', '写入 DSH 配置'),
        ]
        findings = scan_directory(self.repo_dir, config_modify_patterns)
        findings = [f for f in findings if 'package.json' not in f[0]]

        if findings:
            detail_lines = []
            for full, desc, count, line, sample in findings[:5]:
                rel = os.path.relpath(full, self.repo_dir)
                detail_lines.append(f'  - {rel}:{line} → {desc} ({count} 处)')
            detail = '检测到配置修改:\n' + '\n'.join(detail_lines)
            if len(findings) > 5:
                detail += f'\n  ... 共 {len(findings)} 处'
            self.add_result('3.8', '不篡改全局配置', '必查', '⚠️  需人工复核',
                            detail + ' — 需人工判断是否涉及全局配置篡改')
        else:
            self.add_result('3.8', '不篡改全局配置', '必查', '✅ 通过', '未检测到明显的全局配置修改模式')


    # --- 四、代码与依赖安全审计 ---

    def check_4_1_obfuscation(self):
        """4.1 核心逻辑全部开源可读, 无混淆代码"""
        if not self.repo_dir:
            self.add_result('4.1', '无混淆代码', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        findings = scan_directory(self.repo_dir, OBFUSCATION_PATTERNS)
        if findings:
            detail_lines = []
            for full, desc, count, line, sample in findings[:5]:
                rel = os.path.relpath(full, self.repo_dir)
                detail_lines.append(f'  - {rel}:{line} → {desc} ({count} 处)')
            detail = '检测到潜在混淆代码:\n' + '\n'.join(detail_lines)
            if len(findings) > 5:
                detail += f'\n  ... 共 {len(findings)} 处'
            self.add_result('4.1', '无混淆代码', '必查', '❌ 不通过', detail, 'critical')
        else:
            self.add_result('4.1', '无混淆代码', '必查', '✅ 通过', '未检测到混淆代码模式')

    def check_4_2_dangerous_api(self):
        """4.2 无 eval/vm/new Function 等危险 API"""
        if not self.repo_dir:
            self.add_result('4.2', '无 eval/vm/new Function', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        findings = scan_directory(self.repo_dir, DANGEROUS_CODE_PATTERNS)
        if findings:
            detail_lines = []
            for full, desc, count, line, sample in findings[:5]:
                rel = os.path.relpath(full, self.repo_dir)
                detail_lines.append(f'  - {rel}:{line} → {desc} ({count} 处)')
            detail = '检测到危险 API:\n' + '\n'.join(detail_lines)
            if len(findings) > 5:
                detail += f'\n  ... 共 {len(findings)} 处'
            self.add_result('4.2', '无 eval/vm/new Function', '必查', '❌ 不通过', detail, 'critical')
        else:
            self.add_result('4.2', '无 eval/vm/new Function', '必查', '✅ 通过', '未检测到危险 API 调用')

    def check_4_3_npm_audit(self):
        """4.3 执行 npm audit 检测, 无高危/严重依赖漏洞"""
        if not self.repo_dir:
            self.add_result('4.3', 'npm audit 无高危漏洞', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        has_pkg_lock = os.path.exists(os.path.join(self.repo_dir, 'package-lock.json'))
        has_package_json = os.path.exists(os.path.join(self.repo_dir, 'package.json'))

        if not has_package_json:
            self.add_result('4.3', 'npm audit 无高危漏洞', '必查', '⚠️  需人工复核', '未找到 package.json, 可能不是 npm 项目')
            return

        rc, out, err = run_cmd('npm audit --json 2>/dev/null || npm audit 2>/dev/null || echo "NPM_AUDIT_UNAVAILABLE"', cwd=self.repo_dir, timeout=120)
        if 'NPM_AUDIT_UNAVAILABLE' in out or 'command not found' in err or 'not found' in err:
            self.add_result('4.3', 'npm audit 无高危漏洞', '必查', '⚠️  需人工复核',
                            'npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit`')
        else:
            try:
                audit_data = json.loads(out) if out.strip().startswith('{') else None
            except Exception:
                audit_data = None

            if audit_data:
                vulns = audit_data.get('metadata', {}).get('vulnerabilities', {})
                high = vulns.get('high', 0)
                critical = vulns.get('critical', 0)
                moderate = vulns.get('moderate', 0)
                if high > 0 or critical > 0:
                    self.add_result('4.3', 'npm audit 无高危漏洞', '必查', '❌ 不通过',
                                    f'npm audit: 高危 {high}, 严重 {critical}, 中危 {moderate}')
                else:
                    self.add_result('4.3', 'npm audit 无高危漏洞', '必查', '✅ 通过',
                                    f'npm audit: 高危 {high}, 严重 {critical}, 中危 {moderate}')
            else:
                if 'found 0 vulnerabilities' in out.lower():
                    self.add_result('4.3', 'npm audit 无高危漏洞', '必查', '✅ 通过', 'npm audit: 0 漏洞')
                elif 'high' in out.lower() or 'critical' in out.lower():
                    self.add_result('4.3', 'npm audit 无高危漏洞', '必查', '❌ 不通过',
                                    f'npm audit 输出:\n{out[:500]}')
                else:
                    self.add_result('4.3', 'npm audit 无高危漏洞', '必查', '⚠️  需人工复核',
                                    f'npm audit 输出:\n{out[:300]}')

    def check_4_4_deprecated_deps(self):
        """4.4 不使用已废弃、停止维护超过 1 年的第三方依赖包"""
        if not self.repo_dir:
            self.add_result('4.4', '不使用废弃依赖', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        pkg_files = find_package_json(self.repo_dir)
        deps = {}
        for pf in pkg_files:
            try:
                with open(pf, 'r', encoding='utf-8') as f:
                    pkg = json.load(f)
                deps.update(pkg.get('dependencies', {}))
                deps.update(pkg.get('devDependencies', {}))
                deps.update(pkg.get('peerDependencies', {}))
            except Exception:
                continue

        deprecated_pkgs = {
            'request': 'request 已停止维护 (2020-02)',
            'gulp-util': 'gulp-util 已废弃',
            'babel-preset-es2015': 'babel-preset-es2015 已废弃, 请使用 @babel/preset-env',
            'core-js@2': 'core-js@2 已停止维护',
            'left-pad': 'left-pad 已废弃',
            'node-uuid': 'node-uuid 已废弃, 请使用 uuid',
            'har-validator': 'har-validator 已停止维护',
            'resolve-url': 'resolve-url 已废弃',
            'object-assign': 'object-assign 已废弃 (Node >=4)',
        }

        deprecated_found = []
        for dep, version in deps.items():
            for pat, desc in deprecated_pkgs.items():
                if pat in dep:
                    deprecated_found.append(f'{dep}@{version} — {desc}')
                    break

        if deprecated_found:
            detail = '检测到可能废弃的依赖:\n' + '\n'.join(f'  - {d}' for d in deprecated_found[:5])
            if len(deprecated_found) > 5:
                detail += f'\n  ... 共 {len(deprecated_found)} 个'
            self.add_result('4.4', '不使用废弃依赖', '必查', '⚠️  需人工复核', detail)
        else:
            self.add_result('4.4', '不使用废弃依赖', '必查', '✅ 通过', f'共检查 {len(deps)} 个依赖, 未发现已知废弃包')

    def check_4_5_backdoors(self):
        """4.5 无隐藏的定时任务、未公开的调试端口、特殊指令后门"""
        if not self.repo_dir:
            self.add_result('4.5', '无隐藏后门', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        findings = scan_directory(self.repo_dir, BACKDOOR_PATTERNS)
        if findings:
            detail_lines = []
            for full, desc, count, line, sample in findings[:5]:
                rel = os.path.relpath(full, self.repo_dir)
                detail_lines.append(f'  - {rel}:{line} → {desc} ({count} 处)')
            detail = '检测到潜在后门/隐藏逻辑:\n' + '\n'.join(detail_lines)
            if len(findings) > 5:
                detail += f'\n  ... 共 {len(findings)} 处'
            self.add_result('4.5', '无隐藏后门', '必查', '⚠️  需人工复核',
                            detail + ' — 需人工判断是否有恶意意图')
        else:
            self.add_result('4.5', '无隐藏后门', '必查', '✅ 通过', '未检测到明显的后门/隐藏逻辑模式')

    def check_4_6_file_theft(self):
        """4.6 无隐藏的文件窃取、静默上传、环境信息收集逻辑"""
        if not self.repo_dir:
            self.add_result('4.6', '无文件窃取/静默上传', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        findings = scan_directory(self.repo_dir, FILE_THEFT_PATTERNS)
        if findings:
            detail_lines = []
            for full, desc, count, line, sample in findings[:5]:
                rel = os.path.relpath(full, self.repo_dir)
                detail_lines.append(f'  - {rel}:{line} → {desc} ({count} 处)')
            detail = '检测到潜在文件窃取/上传模式:\n' + '\n'.join(detail_lines)
            if len(findings) > 5:
                detail += f'\n  ... 共 {len(findings)} 处'
            self.add_result('4.6', '无文件窃取/静默上传', '必查', '⚠️  需人工复核',
                            detail + ' — 需人工判断是否有恶意意图')
        else:
            self.add_result('4.6', '无文件窃取/静默上传', '必查', '✅ 通过', '未检测到文件窃取/静默上传模式')

    def check_4_7_dependency_count(self):
        """4.7 第三方依赖数量可控 (推荐)"""
        if not self.repo_dir:
            self.add_result('4.7', '依赖数量可控', '推荐', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        pkg_files = find_package_json(self.repo_dir)
        total_deps = 0
        details = []
        for pf in pkg_files:
            try:
                with open(pf, 'r', encoding='utf-8') as f:
                    pkg = json.load(f)
                deps = pkg.get('dependencies', {})
                dev_deps = pkg.get('devDependencies', {})
                total_deps += len(deps) + len(dev_deps)
                details.append(f'{os.path.basename(os.path.dirname(pf))}: {len(deps)} deps + {len(dev_deps)} devDeps')
            except Exception:
                continue

        if total_deps == 0:
            self.add_result('4.7', '依赖数量可控', '推荐', '✅ 通过', '无第三方依赖')
        elif total_deps <= 15:
            self.add_result('4.7', '依赖数量可控', '推荐', '✅ 通过', f'总依赖数: {total_deps}. ' + '; '.join(details[:3]))
        elif total_deps <= 50:
            self.add_result('4.7', '依赖数量可控', '推荐', '⚠️  需人工复核',
                            f'总依赖数: {total_deps}. ' + '; '.join(details[:3]) + ' — 依赖较多, 需人工审查')
        else:
            self.add_result('4.7', '依赖数量可控', '推荐', '❌ 不通过',
                            f'总依赖数: {total_deps}. ' + '; '.join(details[:3]) + ' — 依赖过多', 'major')

    def check_4_8_code_quality(self):
        """4.8 代码结构清晰, 无大量废弃注释代码 (推荐)"""
        if not self.repo_dir:
            self.add_result('4.8', '代码结构清晰', '推荐', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        source_files = []
        for dirpath, dirnames, filenames in os.walk(self.repo_dir):
            dirnames[:] = [d for d in dirnames if d not in {'node_modules', '.git', 'dist', 'build'}]
            for fn in filenames:
                if fn.endswith(('.js', '.ts', '.mjs', '.cjs', '.py')):
                    source_files.append(os.path.join(dirpath, fn))

        total_lines = 0
        commented_lines = 0
        for sf in source_files:
            content = read_file_safe(sf)
            if not content:
                continue
            lines = content.split('\n')
            total_lines += len(lines)
            for line in lines:
                stripped = line.strip()
                if stripped.startswith('//') or stripped.startswith('#') or stripped.startswith('/*') or stripped.startswith('*'):
                    commented_lines += 1

        if total_lines == 0:
            self.add_result('4.8', '代码结构清晰', '推荐', '⚠️  需人工复核', '未找到源文件')
        else:
            comment_ratio = commented_lines / total_lines
            detail = f'总行数: {total_lines}, 注释行: {commented_lines} ({comment_ratio:.1%})'
            if comment_ratio > 0.5:
                self.add_result('4.8', '代码结构清晰', '推荐', '⚠️  需人工复核',
                                detail + ' — 注释占比过高, 可能有废弃代码')
            else:
                self.add_result('4.8', '代码结构清晰', '推荐', '✅ 通过', detail)

    def check_4_9_tests(self):
        """4.9 核心功能具备单元测试/集成测试覆盖 (推荐)"""
        if not self.repo_dir:
            self.add_result('4.9', '具备测试覆盖', '推荐', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        test_dirs = ['test', 'tests', '__tests__', 'spec']
        test_files = []
        for dirpath, dirnames, filenames in os.walk(self.repo_dir):
            dirnames[:] = [d for d in dirnames if d not in {'node_modules', '.git'}]
            for name in dirnames:
                if name.lower() in test_dirs:
                    test_files.append(os.path.join(dirpath, name))
            for fn in filenames:
                if fn.endswith(('.test.js', '.test.ts', '.spec.js', '.spec.ts', '.test.py', '_test.py')):
                    test_files.append(os.path.join(dirpath, fn))

        if test_files:
            self.add_result('4.9', '具备测试覆盖', '推荐', '✅ 通过',
                            f'发现测试文件/目录: {len(test_files)} 个, 例如: {os.path.basename(test_files[0])}')
        else:
            self.add_result('4.9', '具备测试覆盖', '推荐', '⚠️  需人工复核', '未发现测试文件')


    # --- 五、数据安全与隐私审计 ---

    def check_5_1_local_processing(self):
        """5.1 核心业务数据默认在本地完成处理"""
        if not self.repo_dir:
            self.add_result('5.1', '数据本地处理', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        findings = scan_directory(self.repo_dir, NETWORK_EXFIL_PATTERNS)
        if findings:
            readme = find_readme(self.repo_dir)
            readme_content = ''
            if readme:
                readme_content = read_file_safe(readme).lower()
            has_disclosure = any(kw in readme_content for kw in ['数据上传', 'data upload', '远程处理', 'remote processing', 'privacy', '隐私', 'telemetry', '遥测', '数据采集', 'data collection'])
            if has_disclosure:
                self.add_result('5.1', '数据本地处理', '必查', '✅ 通过',
                                '检测到网络请求, 但 README 中有数据上传说明, 需确认')
            else:
                self.add_result('5.1', '数据本地处理', '必查', '⚠️  需人工复核',
                                '检测到网络请求, 但未在 README 中发现数据上传说明')
        else:
            self.add_result('5.1', '数据本地处理', '必查', '✅ 通过', '未检测到网络请求, 数据默认为本地处理')

    def check_5_2_data_reporting(self):
        """5.2 数据上报已在文档中明确"""
        if not self.repo_dir:
            self.add_result('5.2', '数据上报透明', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        readme = find_readme(self.repo_dir)
        readme_content = ''
        if readme:
            readme_content = read_file_safe(readme)

        disclosure_keywords = ['数据上报', '数据采集', '错误统计', '使用分析', '遥测', 'telemetry', 'error tracking', 'analytics', 'data collection', 'usage data', 'privacy policy', '隐私政策']
        found_disclosures = [kw for kw in disclosure_keywords if kw in readme_content.lower()]

        if found_disclosures:
            self.add_result('5.2', '数据上报透明', '必查', '✅ 通过',
                            f'README 中包含数据上报说明: {", ".join(found_disclosures[:5])}')
        else:
            findings = scan_directory(self.repo_dir, NETWORK_EXFIL_PATTERNS)
            if findings:
                self.add_result('5.2', '数据上报透明', '必查', '❌ 不通过',
                                '检测到网络请求但 README 中未说明数据上报内容、接收方、用途', 'major')
            else:
                self.add_result('5.2', '数据上报透明', '必查', '✅ 通过', '未检测到数据上报/网络请求逻辑')

    def check_5_3_sensitive_storage(self):
        """5.3 不明文存储敏感信息"""
        if not self.repo_dir:
            self.add_result('5.3', '敏感信息加密存储', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        plaintext_storage_patterns = [
            (r'(writeFile|writeFileSync|appendFile|appendFileSync|localStorage\.setItem|\.set\s*\(.*key|\.set\s*\(.*token)\s*\([^)]*(api|key|token|password|secret|credential)', '明文写入敏感信息'),
            (r'(api[_-]?key|password|secret|token)\s*[:=]\s*[\'\"][^\'\"]+[\'\"]', '硬编码敏感信息'),
            (r'\.env\s*=\s*|process\.env\.(AUTH|TOKEN|API|SECRET)', '从环境变量获取敏感信息'),
        ]
        findings = scan_directory(self.repo_dir, plaintext_storage_patterns)
        if findings:
            detail_lines = []
            for full, desc, count, line, sample in findings[:5]:
                rel = os.path.relpath(full, self.repo_dir)
                detail_lines.append(f'  - {rel}:{line} → {desc} ({count} 处)')
            detail = '检测到敏感信息存储:\n' + '\n'.join(detail_lines)
            self.add_result('5.3', '敏感信息加密存储', '必查', '⚠️  需人工复核',
                            detail + ' — 需确认是否加密存储')
        else:
            self.add_result('5.3', '敏感信息加密存储', '必查', '✅ 通过', '未检测到明文存储敏感信息')

    def check_5_4_unauthorized_access(self):
        """5.4 不对用户本地文档/代码仓库/私有文件进行未授权读取与上传"""
        if not self.repo_dir:
            self.add_result('5.4', '无未授权读取', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        unauthorized_patterns = [
            (r'fs\.(readFile|readFileSync|createReadStream)\s*\([^)]*(\.md|\.docx?|\.txt|\.pdf|\.zip|\.tar)', '读取文档/压缩文件'),
            (r'fs\.(readdir|readdirSync)\s*\([^)]*(?:home|~|/Users|/home|C:\\\\Users)', '遍历用户目录'),
            (r'git\s+log|git\s+show|git\s+diff', '读取 git 历史'),
            (r'child_process.*git\s+(log|show|diff|cat-file|ls-files)', '通过 git 命令读取仓库内容'),
        ]
        findings = scan_directory(self.repo_dir, unauthorized_patterns)
        if findings:
            detail_lines = []
            for full, desc, count, line, sample in findings[:5]:
                rel = os.path.relpath(full, self.repo_dir)
                detail_lines.append(f'  - {rel}:{line} → {desc} ({count} 处)')
            detail = '检测到潜在未授权读取:\n' + '\n'.join(detail_lines)
            self.add_result('5.4', '无未授权读取', '必查', '⚠️  需人工复核',
                            detail + ' — 需人工判断是否在授权范围内')
        else:
            self.add_result('5.4', '无未授权读取', '必查', '✅ 通过', '未检测到明显的未授权读取模式')

    def check_5_5_logging(self):
        """5.5 关键操作具备可追溯日志 (推荐)"""
        if not self.repo_dir:
            self.add_result('5.5', '关键操作有日志', '推荐', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        logging_patterns = [
            (r'console\.(log|info|warn|error)\s*\(', 'console 日志'),
            (r'logger\.(info|warn|error|debug|log)\s*\(', 'logger 日志'),
            (r'log\.(info|warn|error|debug)\s*\(', 'log 日志'),
            (r'logging|winston|pino|bunyan|debug\s*\(', '日志库'),
        ]
        findings = scan_directory(self.repo_dir, logging_patterns)
        if findings:
            self.add_result('5.5', '关键操作有日志', '推荐', '✅ 通过', f'发现日志记录模式 ({len(findings)} 处)')
        else:
            self.add_result('5.5', '关键操作有日志', '推荐', '⚠️  需人工复核', '未发现日志记录模式')

    def check_5_6_data_cleanup(self):
        """5.6 支持一键清理插件产生的所有本地数据 (推荐)"""
        if not self.repo_dir:
            self.add_result('5.6', '支持一键清理数据', '推荐', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        cleanup_patterns = [
            (r'(clear|clean|reset|purge|wipe|uninstall|卸载|清理)\s*(all|data|cache|everything)', '数据清理命令'),
            (r'rm\s*-rf|fs\.rmSync\s*\(', '删除文件'),
            (r'clear\s+data|clean\s+data|清除.*数据|清理.*数据', '清理数据逻辑'),
        ]
        findings = scan_directory(self.repo_dir, cleanup_patterns)
        if findings:
            self.add_result('5.6', '支持一键清理数据', '推荐', '✅ 通过', f'发现数据清理相关代码 ({len(findings)} 处)')
        else:
            self.add_result('5.6', '支持一键清理数据', '推荐', '⚠️  需人工复核', '未发现一键清理功能, 需确认是否有数据清理机制')


    # --- 六、运行时安全审计 ---

    def check_6_1_privileges(self):
        """6.1 无需管理员/root 权限即可运行"""
        if not self.repo_dir:
            self.add_result('6.1', '无需 root 权限', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        findings = scan_directory(self.repo_dir, SYSTEM_MODIFY_PATTERNS)
        sudo_findings = [f for f in findings if 'root' in f[1].lower() or 'sudo' in f[1].lower() or '权限' in f[1]]
        if sudo_findings:
            detail_lines = []
            for full, desc, count, line, sample in sudo_findings[:5]:
                rel = os.path.relpath(full, self.repo_dir)
                detail_lines.append(f'  - {rel}:{line} → {desc}')
            self.add_result('6.1', '无需 root 权限', '必查', '❌ 不通过', '\n'.join(detail_lines), 'critical')
        else:
            self.add_result('6.1', '无需 root 权限', '必查', '✅ 通过', '未检测到需要 root/sudo 的代码')

    def check_6_2_system_config(self):
        """6.2 不修改系统全局配置、不创建开机自启项"""
        if not self.repo_dir:
            self.add_result('6.2', '不修改系统配置', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        findings = scan_directory(self.repo_dir, SYSTEM_MODIFY_PATTERNS)
        system_findings = [f for f in findings if 'root' not in f[1].lower() and 'sudo' not in f[1].lower() and '权限' not in f[1]]
        if system_findings:
            detail_lines = []
            for full, desc, count, line, sample in system_findings[:5]:
                rel = os.path.relpath(full, self.repo_dir)
                detail_lines.append(f'  - {rel}:{line} → {desc} ({count} 处)')
            detail = '检测到系统配置修改:\n' + '\n'.join(detail_lines)
            if len(system_findings) > 5:
                detail += f'\n  ... 共 {len(system_findings)} 处'
            self.add_result('6.2', '不修改系统配置', '必查', '❌ 不通过', detail, 'critical')
        else:
            self.add_result('6.2', '不修改系统配置', '必查', '✅ 通过', '未检测到系统配置修改/开机自启逻辑')

    def check_6_3_sandbox(self):
        """6.3 支持 DSH 官方沙箱机制运行"""
        if not self.repo_dir:
            self.add_result('6.3', '支持沙箱运行', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        readme = find_readme(self.repo_dir)
        readme_content = ''
        if readme:
            readme_content = read_file_safe(readme).lower()
        sandbox_keywords = ['sandbox', '沙箱', 'landlock', '隔离', 'isolation', 'workspace']
        found = [kw for kw in sandbox_keywords if kw in readme_content]

        pkg_files = find_package_json(self.repo_dir)
        for pf in pkg_files:
            try:
                with open(pf, 'r', encoding='utf-8') as f:
                    pkg = json.load(f)
                dsh = pkg.get('dsh', {})
                if dsh:
                    dsh_str = json.dumps(dsh).lower()
                    if any(kw in dsh_str for kw in ['sandbox', '隔离']):
                        found.append('dsh config sandbox')
            except Exception:
                pass

        if found:
            self.add_result('6.3', '支持沙箱运行', '必查', '✅ 通过', f'检测到沙箱支持声明: {", ".join(found[:5])}')
        else:
            self.add_result('6.3', '支持沙箱运行', '必查', '⚠️  需人工复核', '未在文档/配置中检测到沙箱支持声明, 需确认')

    def check_6_4_memory_leaks(self):
        """6.4 长时间空闲运行无内存泄漏 (推荐)"""
        self.add_result('6.4', '无内存泄漏', '推荐', '⚠️  需人工复核', '需在运行环境中长时间测试')

    def check_6_5_temp_cleanup(self):
        """6.5 临时文件自动清理 (推荐)"""
        if not self.repo_dir:
            self.add_result('6.5', '临时文件自动清理', '推荐', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        temp_cleanup_patterns = [
            (r'rm\s+.*(tmp|temp)|fs\.rm(Sync)?\s*\([^)]*tmp', '清理临时文件'),
            (r'delete.*(tmp|temp)|remove.*(tmp|temp)|清理.*临时', '清理临时文件'),
            (r'os\.tmpdir\(\).*?(unlink|rm)', '删除系统临时文件'),
        ]
        findings = scan_directory(self.repo_dir, temp_cleanup_patterns)
        if findings:
            self.add_result('6.5', '临时文件自动清理', '推荐', '✅ 通过', f'发现临时文件清理逻辑 ({len(findings)} 处)')
        else:
            self.add_result('6.5', '临时文件自动清理', '推荐', '⚠️  需人工复核', '未发现临时文件清理逻辑, 需确认')

    # --- 七、维护与社区审计 ---

    def check_7_1_maintenance(self):
        """7.1 近 3 个月内有代码提交或版本更新"""
        last_commit_days = -1
        commit_count = -1

        if self.repo_dir:
            last_commit_days = get_last_commit_days(self.repo_dir)
            commit_count = get_git_commit_count(self.repo_dir)

        if last_commit_days < 0 and self.commits:
            try:
                date_str = self.commits[0].get('commit', {}).get('committer', {}).get('date', '')
                if date_str:
                    dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                    if dt.tzinfo:
                        last_commit_days = (datetime.now(timezone.utc) - dt).days
            except Exception:
                pass

        detail_parts = []
        if last_commit_days >= 0:
            detail_parts.append(f'最近提交距今: {last_commit_days} 天')
        if commit_count >= 0:
            detail_parts.append(f'提交总数: {commit_count}')
        if not detail_parts:
            detail_parts.append('无法获取提交信息')

        if last_commit_days >= 0:
            if last_commit_days <= 90:
                self.add_result('7.1', '近 3 个月内有更新', '必查', '✅ 通过', '; '.join(detail_parts))
            elif last_commit_days <= 180:
                self.add_result('7.1', '近 3 个月内有更新', '必查', '⚠️  需人工复核',
                                '; '.join(detail_parts) + ' — 建议降级为灰名单')
            else:
                self.add_result('7.1', '近 3 个月内有更新', '必查', '❌ 不通过',
                                '; '.join(detail_parts) + ' — 超过 6 个月未更新, 应降级', 'major')
        else:
            self.add_result('7.1', '近 3 个月内有更新', '必查', '⚠️  需人工复核', '; '.join(detail_parts))

    def check_7_2_abandonment(self):
        """7.2 作者未明确标注停止维护"""
        if not self.repo_dir:
            self.add_result('7.2', '未标记停止维护', '必查', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        readme = find_readme(self.repo_dir)
        readme_content = read_file_safe(readme) if readme else ''

        for doc_name in ['CHANGELOG.md', 'CHANGELOG', 'CONTRIBUTING.md', 'NOTICE.md', 'ARCHIVED.md']:
            doc_path = os.path.join(self.repo_dir, doc_name)
            if os.path.exists(doc_path):
                readme_content += '\n' + read_file_safe(doc_path)

        abandon_found = [marker for marker in ABANDON_MARKERS if marker.lower() in readme_content.lower()]
        if abandon_found:
            self.add_result('7.2', '未标记停止维护', '必查', '❌ 不通过',
                            f'文档中发现弃用标记: {", ".join(abandon_found[:5])}', 'critical')
        else:
            self.add_result('7.2', '未标记停止维护', '必查', '✅ 通过', '未发现停止维护/弃用声明')

    def check_7_3_security_feedback(self):
        """7.3 无大量未解决的安全反馈、恶意行为举报"""
        if not (self.owner and self.repo):
            self.add_result('7.3', '无大量未解决安全反馈', '必查', '⚠️  需人工复核', '无法访问 GitHub API')
            return

        issues_url = f'https://api.github.com/search/issues?q=repo:{self.owner}/{self.repo}+is:issue+is:open+security'
        status, body = http_get(issues_url, self.token)
        if status == 200:
            try:
                data = json.loads(body)
                open_security_issues = data.get('total_count', 0)
                if open_security_issues > 5:
                    self.add_result('7.3', '无大量未解决安全反馈', '必查', '❌ 不通过',
                                    f'发现 {open_security_issues} 个公开安全问题', 'major')
                elif open_security_issues > 0:
                    self.add_result('7.3', '无大量未解决安全反馈', '必查', '⚠️  需人工复核',
                                    f'发现 {open_security_issues} 个公开安全问题')
                else:
                    self.add_result('7.3', '无大量未解决安全反馈', '必查', '✅ 通过', '未发现公开安全问题')
            except Exception:
                self.add_result('7.3', '无大量未解决安全反馈', '必查', '⚠️  需人工复核', 'GitHub API 响应解析失败')
        else:
            self.add_result('7.3', '无大量未解决安全反馈', '必查', '⚠️  需人工复核', f'GitHub API 请求失败 (HTTP {status})')

    def check_7_4_response_time(self):
        """7.4 开发者对高危安全问题的响应周期 ≤ 7 天 (推荐)"""
        self.add_result('7.4', '安全问题响应 ≤ 7 天', '推荐', '⚠️  需人工复核', '需通过 GitHub Issues/PR 历史人工评估')

    def check_7_5_documentation(self):
        """7.5 提供完整 README、配置项说明、使用示例、CHANGELOG (推荐)"""
        if not self.repo_dir:
            self.add_result('7.5', '完整文档', '推荐', '⚠️  需人工复核', '未克隆仓库, 无法检查')
            return

        readme = find_readme(self.repo_dir)
        changelog = os.path.join(self.repo_dir, 'CHANGELOG.md')

        missing = []
        found_docs = []
        if not readme:
            missing.append('README')
        else:
            found_docs.append('README')
        if not os.path.exists(changelog):
            missing.append('CHANGELOG')
        else:
            found_docs.append('CHANGELOG')

        if readme:
            content = read_file_safe(readme)
            has_config = any(kw in content.lower() for kw in ['config', '配置', 'setting', '设置'])
            has_example = any(kw in content.lower() for kw in ['example', '示例', 'usage', '使用', 'demo', '演示'])
            has_install = any(kw in content.lower() for kw in ['install', '安装', 'getting started', '快速开始'])

            if has_config:
                found_docs.append('配置说明')
            else:
                missing.append('配置说明')
            if has_example:
                found_docs.append('使用示例')
            else:
                missing.append('使用示例')
            if has_install:
                found_docs.append('安装说明')
            else:
                missing.append('安装说明')

        if len(missing) == 0:
            self.add_result('7.5', '完整文档', '推荐', '✅ 通过', '文档齐全: ' + ', '.join(found_docs))
        elif len(missing) <= 2:
            self.add_result('7.5', '完整文档', '推荐', '⚠️  需人工复核', '有文档但缺少: ' + ', '.join(missing))
        else:
            self.add_result('7.5', '完整文档', '推荐', '❌ 不通过', '缺少文档: ' + ', '.join(missing), 'major')

    def check_7_6_community(self):
        """7.6 有社区背书 (推荐)"""
        if not self.repo_info:
            self.add_result('7.6', '有社区背书', '推荐', '⚠️  需人工复核', '无法获取仓库元数据')
            return

        stars = self.repo_info.get('stargazers_count', 0)
        forks = self.repo_info.get('forks_count', 0)
        watchers = self.repo_info.get('subscribers_count', 0)

        detail = f'Stars: {stars}, Forks: {forks}, Watchers: {watchers}'
        if stars >= 100:
            self.add_result('7.6', '有社区背书', '推荐', '✅ 通过', detail + ' — 高 Star 量')
        elif stars >= 10:
            self.add_result('7.6', '有社区背书', '推荐', '⚠️  需人工复核', detail + ' — 有一定社区基础')
        else:
            self.add_result('7.6', '有社区背书', '推荐', '⚠️  需人工复核', detail + ' — 社区背书不足, 需人工判断')


    # --- 报告生成 ---

    def generate_report(self):
        """生成 Markdown 格式的审计报告."""
        lines = []
        lines.append('# DSH 插件安全自动化校验报告\n')
        lines.append(f'- **校验对象**: {self.url}')
        lines.append(f'- **校验时间**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        lines.append(f'- **校验方式**: 自动化静态分析 + GitHub API')
        lines.append('')

        required = [r for r in self.results if r.check_type == '必查']
        recommended = [r for r in self.results if r.check_type == '推荐']
        required_pass = sum(1 for r in required if r.result.startswith('✅'))
        required_fail = sum(1 for r in required if r.result.startswith('❌'))
        required_review = sum(1 for r in required if r.result.startswith('⚠️'))
        rec_pass = sum(1 for r in recommended if r.result.startswith('✅'))
        rec_review = sum(1 for r in recommended if r.result.startswith('⚠️'))
        rec_fail = sum(1 for r in recommended if r.result.startswith('❌'))

        lines.append('## 检查结果统计\n')
        lines.append('| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |')
        lines.append('| :--- | :---: | :---: | :---: | :---: |')
        lines.append(f'| 🔴 必查 | {len(required)} | {required_pass} | {required_review} | {required_fail} |')
        lines.append(f'| 🟡 推荐 | {len(recommended)} | {rec_pass} | {rec_review} | {rec_fail} |')
        lines.append('')

        has_critical_fail = any(r.result.startswith('❌') and r.severity in ('critical', 'major') for r in required)
        total_rec = len(recommended) or 1
        rec_rate = (rec_pass + rec_review) / total_rec * 100

        lines.append('## 自动判定结果\n')
        if has_critical_fail:
            lines.append(f'> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**')
        else:
            if rec_rate >= 80:
                lines.append(f'> ✅ **必查项全通过, 推荐项满足率约 {rec_rate:.0f}% — 初步建议: 白名单 (需人工复核通过后确认)**')
            elif rec_rate >= 30:
                lines.append(f'> 🟡 **必查项全通过, 推荐项满足率约 {rec_rate:.0f}% — 初步建议: 灰名单 (测试可用)**')
            else:
                lines.append(f'> 🔴 **必查项全通过但推荐项满足率较低 ({rec_rate:.0f}%) — 初步建议: 黑名单/谨慎评估**')
        lines.append('')

        sections = [
            ('一、基础准入审计', ['1.1', '1.2', '1.3', '1.4', '1.5', '1.6']),
            ('二、技术规范审计', ['2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7']),
            ('三、权限安全审计', ['3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8']),
            ('四、代码与依赖安全审计', ['4.1', '4.2', '4.3', '4.4', '4.5', '4.6', '4.7', '4.8', '4.9']),
            ('五、数据安全与隐私审计', ['5.1', '5.2', '5.3', '5.4', '5.5', '5.6']),
            ('六、运行时安全审计', ['6.1', '6.2', '6.3', '6.4', '6.5']),
            ('七、维护与社区审计', ['7.1', '7.2', '7.3', '7.4', '7.5', '7.6']),
        ]

        for section_title, item_ids in sections:
            lines.append(f'\n## {section_title}\n')
            lines.append('| 序号 | 检查项 | 类型 | 结果 | 详情 |')
            lines.append('| :--- | :--- | :---: | :---: | :--- |')
            for item_id in item_ids:
                matches = [r for r in self.results if r.item_id == item_id]
                for r in matches:
                    detail_escaped = r.detail.replace('|', '\\|').replace('\n', '<br>')
                    lines.append(f'| {r.item_id} | {r.title} | {r.check_type} | {r.result} | {detail_escaped} |')
            lines.append('')

        lines.append('\n## 审计结论\n')
        lines.append('| 项目 | 内容 |')
        lines.append('| :--- | :--- |')
        lines.append(f'| 插件名称 | {self.repo or "-"} |')
        lines.append(f'| 校验 URL | {self.url} |')
        required_pass_rate = (required_pass / len(required) * 100) if required else 0
        lines.append(f'| 必查项通过率 | {required_pass}/{len(required)} ({required_pass_rate:.0f}%) |')
        lines.append(f'| 推荐项满足率 | {rec_pass + rec_review}/{len(recommended)} (约 {rec_rate:.0f}%) |')
        lines.append(f'| 最终分级 | {"🔴 黑名单" if has_critical_fail else "🟡 灰名单 (需人工复核)"} |')
        lines.append(f'| 主要风险说明 | 详见各检查项结果 |')
        lines.append(f'| 审计方式 | 自动化静态分析 (需人工复核标记项) |')
        lines.append(f'| 审计日期 | {datetime.now().strftime("%Y-%m-%d")} |')
        lines.append('')
        lines.append('> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。')
        lines.append('')

        return '\n'.join(lines)

    def print_summary(self):
        """输出简洁的摘要信息."""
        required = [r for r in self.results if r.check_type == '必查']
        recommended = [r for r in self.results if r.check_type == '推荐']
        required_pass = sum(1 for r in required if r.result.startswith('✅'))
        required_fail = sum(1 for r in required if r.result.startswith('❌'))
        required_review = sum(1 for r in required if r.result.startswith('⚠️'))
        rec_pass = sum(1 for r in recommended if r.result.startswith('✅'))
        rec_fail = sum(1 for r in recommended if r.result.startswith('❌'))
        rec_review = sum(1 for r in recommended if r.result.startswith('⚠️'))

        print()
        print('=' * 60)
        print('DSH 插件安全自动化校验摘要')
        print('=' * 60)
        print(f'校验对象: {self.url}')
        print()
        print(f'✅ 必查通过: {required_pass}')
        print(f'⚠️  必查需人工复核: {required_review}')
        print(f'❌ 必查不通过: {required_fail}')
        print(f'✅ 推荐通过: {rec_pass}')
        print(f'⚠️  推荐需人工复核: {rec_review}')
        print(f'❌ 推荐不通过: {rec_fail}')
        print()

        fails = [r for r in self.results if r.result.startswith('❌')]
        if fails:
            print('不通过项:')
            for r in fails:
                print(f'  ❌ [{r.item_id}] {r.title} ({r.check_type})')
            print()

        reviews = [r for r in self.results if r.check_type == '必查' and r.result.startswith('⚠️')]
        if reviews:
            print('必查项中需人工复核:')
            for r in reviews:
                print(f'  ⚠️  [{r.item_id}] {r.title}')
            print()


def main():
    parser = argparse.ArgumentParser(
        description='DSH 插件安全自动化校验脚本 (根据 security-for-dsh-plugin 文档要求)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('url', help='DSH 插件的 GitHub/GitLab 仓库链接 (如 https://github.com/owner/repo)')
    parser.add_argument('--out', '-o', help='将 Markdown 报告写入指定文件')
    parser.add_argument('--no-clone', action='store_true', help='不克隆仓库, 仅执行 GitHub API 检查')
    parser.add_argument('--keep', '-k', action='store_true', help='校验完成后保留克隆的临时目录')
    parser.add_argument('--token', '-t', help='GitHub/GitLab Personal Access Token')
    parser.add_argument('--quiet', '-q', action='store_true', help='只输出摘要')
    parser.add_argument('--severity', choices=['critical', 'major', 'minor', 'info'], default=None,
                        help='只显示 >= 该级别的检查项')

    args = parser.parse_args()

    validator = PluginValidator(args.url, token=args.token, keep=args.keep, no_clone=args.no_clone)

    try:
        validator.setup()
        validator.run_all_checks()

        report = validator.generate_report()

        if args.out:
            with open(args.out, 'w', encoding='utf-8') as f:
                f.write(report)
            if not args.quiet:
                print(f'[info] 报告已写入: {args.out}')

        if args.quiet:
            validator.print_summary()
        else:
            print(report)

    except Exception as e:
        print(f'[error] 校验失败: {e}', file=sys.stderr)
        sys.exit(1)
    finally:
        validator.cleanup()

    return 0


if __name__ == '__main__':
    sys.exit(main())
