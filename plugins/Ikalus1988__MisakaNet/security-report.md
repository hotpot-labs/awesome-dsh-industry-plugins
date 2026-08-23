# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/Ikalus1988/MisakaNet
- **校验时间**: 2026-08-23 16:31:45
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 11 | 12 | 10 |
| 🟡 推荐 | 14 | 8 | 6 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2023-06-17 (1163 天前); 公开仓库数: 44; 粉丝数: 49 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: Apache-2.0 (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 2738; 包名: misakanet; 描述: Deployment scripts for MisakaNet Workers — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - data/lessons.json:2118 → 非法爬取 (1 处)<br>  - data/retrieval_noisebench_queries.json:52 → 非法爬取 (1 处)<br>  - data/retrieval_noisebench_report.json:194 → 非法爬取 (1 处)<br>  - data/okf/lessons.jsonl:75 → 非法爬取 (1 处)<br>  - lessons/index.md:81 → 非法爬取 (1 处)<br>  ... 共 30 处 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ⚠️  需人工复核 | Git tags (20): v2.20.1, v2.20.0, v2.19.1, v2.19.0, v2.18.0; GitHub Releases (5): v2.20.1, v2.20.0, v2.19.1, v2.19.0, v2.18.0; 未发现版本信息 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ❌ 不通过 | 未在 package.json 中发现 DSH/Cordis 依赖或 engines 字段 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}}; Cordis 配置文件: cordis.patch.yml<br>  - misakanet/scripts/hub_poller.py:68 → Monkey patch / prototype pollution<br>  - tests/test_mcp_fallback.py:23 → Monkey patch / prototype pollution<br>  - tests/test_benchmark_sag_lite.py:86 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 108 处, 函数: 498 个, 比例: 21.7% |
| 2.4 | 卸载后完整释放资源 | 必查 | ⚠️  需人工复核 | 使用了定时器但未发现清理逻辑, 需人工确认 |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .gitignore:16 → 读取环境变量配置 (3 处)<br>  - API.md:147 → 读取 git 凭证 (1 处)<br>  - DEPLOYMENT.md:339 → 读取环境变量配置 (2 处)<br>  - archive/conversation-dumps/hermes-mmx-config-issue.md:21 → 读取环境变量配置 (5 处)<br>  - misakanet/guard.py:97 → 读取环境变量配置 (1 处)<br>  ... 共 126 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - archive/wiki/Home.md:4 → 深层目录穿越 (4 处)<br>  - archive/wiki/Contributing.md:3 → 深层目录穿越 (1 处)<br>  - misakanet/search/engine.py:181 → 全局文件匹配 (1 处)<br>  - misakanet/scripts/inject_to_claude.py:37 → 全局文件匹配 (1 处)<br>  - misakanet/scripts/draft_reminder.py:92 → 全局文件匹配 (1 处)<br>  ... 共 25 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - misakanet/guard.py:139 → Python subprocess (2 处)<br>  - misakanet/profile.py:63 → Python subprocess (1 处)<br>  - misakanet/scripts/standby_poller.py:48 → Python subprocess (1 处)<br>  - misakanet/scripts/skill_cron.py:14 → Python subprocess (1 处)<br>  - misakanet/scripts/queue_hook_stats.py:63 → Python subprocess (9 处)<br>  ... 共 51 处<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - lessons/contrib/openclaw-fatal-error-hook-protocol.md:19 → 开启 shell 模式 (注入风险) (3 处)<br>  - docs/pr-openclaw-error-handler.md:35 → 开启 shell 模式 (注入风险) (2 处)<br>  - docs/security-audit-report.md:105 → 开启 shell 模式 (注入风险) (1 处)<br>  - docs/openclaw-pr/PR_BODY.md:26 → 开启 shell 模式 (注入风险) (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - README.zh-CN.md:10 → 探测到 HTTP(S) 网络请求 (28 处)<br>  - CLAUDE.md:18 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - llms.txt:34 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - search_knowledge.py:397 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - README.ja.md:20 → 探测到 HTTP(S) 网络请求 (55 处)<br>涉及的域名: ..., 127.0.0.1, 172.19.128.1, 192.168.1.10, TOKEN, USERNAME, airtable.com, api.airtable.com, api.anthropic.com, api.bilibili.com (+166 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - LICENSE:149 → 挖矿相关 (1 处)<br>  - DEPLOYMENT.md:208 → 代理/隧道 (1 处)<br>  - tests/test_helpful_button.py:67 → 代理/隧道 (2 处)<br>  - tests/test_demand_board.py:3 → 代理/隧道 (2 处)<br>  - lessons/contrib/tor-orbot-privacy-in-react-native-tr.md:19 → 代理/隧道 (2 处)<br>  ... 共 13 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - SKILL.md:119 → 敏感凭证读取 (1 处)<br>  - llms.txt:11 → 敏感凭证读取 (3 处)<br>  - ROADMAP.md:89 → 敏感凭证读取 (2 处)<br>  - README.ja.md:117 → 敏感凭证读取 (2 处)<br>  - SECURITY.md:30 → 敏感凭证读取 (4 处)<br>  ... 共 313 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - tests/test_frontmatter_parsing.py:157 → 连续十六进制转义 (混淆) (2 处)<br>  - tests/test_search_fuzz.py:103 → 连续十六进制转义 (混淆) (1 处)<br>  - lessons/contrib/cc-connect-feishu-setup-complete.md:123 → 连续十六进制转义 (混淆) (2 处) |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - lessons/en/json-parse-failure-handling.md:118 → eval() 任意代码执行 (1 处)<br>  - lessons/contrib/misakanet-heal-engine-bootstrap-workflow.md:133 → child_process 命令执行 (1 处)<br>  - lessons/contrib/browser-automation-csp-bypass.md:48 → eval() 任意代码执行 (1 处)<br>  - lessons/contrib/windows-ci-splitcommand-backslash-unicode-detached.md:52 → 加载 child_process 模块 (2 处)<br>  - lessons/contrib/openclaw-fatal-error-hook-protocol.md:26 → child_process 命令执行 (1 处)<br>  ... 共 6 处 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 1 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - archive/hook-raw/cc-haha-network-timeout.md:75 → 定时任务 (1 处)<br>  - archive/skills/browser-harness.SKILL.md:46 → 临时文件操作 (3 处)<br>  - misakanet/guard.py:200 → 临时文件操作 (1 处)<br>  - misakanet/scripts/bulk_import_lessons.py:14 → 临时文件操作 (2 处)<br>  - misakanet/scripts/draft_reminder.sh:13 → 临时文件操作 (3 处)<br>  ... 共 110 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - llms.txt:11 → 云存储上传 (1 处)<br>  - server.mcpb:5053 → 云服务 SDK (可能用于隐蔽上传) (2 处)<br>  - server.mcpb:3553 → 云存储上传 (2 处)<br>  - data/lessons.json:4566 → 云服务 SDK (可能用于隐蔽上传) (5 处)<br>  - data/lessons.json:1900 → 云存储上传 (3 处)<br>  ... 共 39 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 1. repo: 0 deps + 1 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 49183, 注释行: 2498 (5.1%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 6 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - DEPLOYMENT.md:250 → 硬编码敏感信息 (1 处)<br>  - misakanet/README.md:45 → 硬编码敏感信息 (1 处)<br>  - misakanet/scripts/queue_hook_stats.py:186 → 硬编码敏感信息 (1 处)<br>  - misakanet/scripts/feedback_report.py:72 → 硬编码敏感信息 (1 处)<br>  - tests/test_intake_redaction.py:35 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - archive/_merged/write-file-sandbox-worktree-git-path.md:44 → 读取 git 历史 (1 处)<br>  - archive/_merged/agent-write-file-sandbox-worktree-path-breakage.md:58 → 读取 git 历史 (1 处)<br>  - archive/hub/orchestrator/dedup_engine.py:3 → 读取 git 历史 (2 处)<br>  - misakanet/profile.py:50 → 读取 git 历史 (2 处)<br>  - misakanet/scripts/sync_lessons.sh:34 → 读取 git 历史 (2 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (66 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (36 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - archive/_merged/wsl-permission-ntfs-fix.md:32 → 要求 root/sudo 权限<br>  - misakanet/scripts/lesson_watcher.sh:13 → 要求 root/sudo 权限<br>  - data/lessons.json:2494 → 要求 root/sudo 权限<br>  - tasks/lesson-python-gbk-encoding-error.json:13 → 要求 root/sudo 权限<br>  - tasks/lesson-cron-job-not-running.json:12 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - search_knowledge.py:1 → 修改系统目录 (1 处)<br>  - DEPLOYMENT.md:182 → 修改系统目录 (3 处)<br>  - archive/_merged/hx-state-database-lock-issues-cleanup-protocol.md:27 → 创建开机自启/系统服务 (2 处)<br>  - archive/hook-raw/cc-haha-model-output-error.md:21 → 修改系统目录 (8 处)<br>  - archive/hook-raw/cc-haha-network-ws-error.md:29 → 修改系统目录 (1 处)<br>  ... 共 224 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: sandbox |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (8 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 2354 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ⚠️  需人工复核 | 发现 2 个公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ✅ 通过 | Stars: 424, Forks: 159, Watchers: 27 — 高 Star 量 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | MisakaNet |
| 校验 URL | https://github.com/Ikalus1988/MisakaNet |
| 必查项通过率 | 11/33 (33%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-23 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
