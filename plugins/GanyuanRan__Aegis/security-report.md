# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/GanyuanRan/Aegis
- **校验时间**: 2026-08-23 16:27:58
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 12 | 13 | 8 |
| 🟡 推荐 | 14 | 8 | 6 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2025-03-15 (526 天前); 公开仓库数: 13; 粉丝数: 10 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1676; 包名: aegis — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - README.md:251 → 盗版/侵权 (1 处)<br>  - docs/README.antigravity.md:38 → 盗版/侵权 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (20): v2.8.7, v2.8.5, v2.8.4, v2.8.3, v2.8.2; package.json version: 2.8.7; GitHub Releases (5): v2.8.7, v2.8.5, v2.8.4, v2.8.3, v2.8.2 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/dsh-agent: ^0.1.0-rc.6; @deepseek-ai/dsh-llm: ^0.1.0-rc.6; @deepseek-ai/dsh-skill-filesystem: ^0.1.0-rc.6 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./extensions/dsh/cordis.patch.yml"}}; Cordis/DSH 依赖: @deepseek-ai/dsh-agent, @deepseek-ai/dsh-llm, @deepseek-ai/dsh-skill-filesystem<br>  - tests/helpers/test_agentic_benchmark_active_run.py:498 → Monkey patch / prototype pollution<br>  - tests/helpers/test_agentic_benchmark_atomic.py:39 → Monkey patch / prototype pollution<br>  - tests/helpers/test_agentic_benchmark_process_supervisor.py:462 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 22 处, 函数: 126 个, 比例: 17.5% |
| 2.4 | 卸载后完整释放资源 | 必查 | ⚠️  需人工复核 | 使用了定时器但未发现清理逻辑, 需人工确认 |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .opencode/plugins/aegis.js:70 → 读取环境变量配置 (6 处)<br>  - tests/deepseek-harness/test-bootstrap.mjs:19 → 读取环境变量配置 (10 处)<br>  - tests/helpers/test_session_start_hook.py:42 → 读取环境变量配置 (1 处)<br>  - tests/helpers/agentic_benchmark_isolation.py:62 → 读取环境变量配置 (4 处)<br>  - tests/helpers/run_controlled_replay_samples.py:324 → 读取环境变量配置 (1 处)<br>  ... 共 22 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - .opencode/plugins/aegis.js:199 → 目录遍历 (1 处)<br>  - .opencode/plugins/aegis.js:68 → 读取用户主目录 (2 处)<br>  - tests/deepseek-harness/test-bootstrap.mjs:14 → 深层目录穿越 (2 处)<br>  - tests/opencode/setup.sh:78 → 深层目录穿越 (1 处)<br>  - tests/e2e/layer2-behavior-check.sh:6 → 深层目录穿越 (1 处)<br>  ... 共 10 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - tests/helpers/test_session_start_hook.py:56 → Python subprocess (2 处)<br>  - tests/helpers/agentic_benchmark_isolation.py:200 → Python subprocess (2 处)<br>  - tests/helpers/agentic_benchmark_provider_preflight.py:310 → Python subprocess (2 处)<br>  - tests/helpers/run_controlled_replay_samples.py:308 → Python subprocess (2 处)<br>  - tests/helpers/test_agentic_benchmark_active_run.py:376 → Python subprocess (1 处)<br>  ... 共 15 处<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - README.zh-CN.md:2 → 探测到 HTTP(S) 网络请求 (21 处)<br>  - README.md:2 → 探测到 HTTP(S) 网络请求 (21 处)<br>  - RELEASE-NOTES.md:2308 → WebSocket 连接 (2 处)<br>  - RELEASE-NOTES.md:2308 → 浏览器网络 API (2 处)<br>  - CODE_OF_CONDUCT.md:119 → 探测到 HTTP(S) 网络请求 (5 处)<br>涉及的域名: -proxy.invalid, 127.0.0.1, agentskills.io, alice, antigravity.google, badgen.net, code.claude.com, deepseek.com, dev.to, developers.googleblog.com (+30 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - CODE_OF_CONDUCT.md:71 → 挖矿相关 (1 处)<br>  - tests/helpers/agentic_benchmark_provider_preflight.py:32 → 代理/隧道 (2 处)<br>  - tests/helpers/test_agentic_benchmark_preflight.py:61 → 代理/隧道 (5 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - AGENTS.md:169 → 敏感凭证读取 (1 处)<br>  - benchmarks/README.md:18 → 敏感凭证读取 (1 处)<br>  - .opencode/plugins/aegis.js:70 → 读取环境变量 API Key/凭证 (6 处)<br>  - tests/deepseek-harness/test-bootstrap.mjs:19 → 读取环境变量 API Key/凭证 (8 处)<br>  - tests/helpers/agentic_benchmark_provider_preflight.py:35 → API Key / Token 读取 (7 处)<br>  ... 共 47 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - .opencode/plugins/aegis.js:359 → 写入配置文件 (1 处)<br>  - .opencode/plugins/aegis.js:359 → 写入 DSH 配置 (1 处)<br>  - tests/deepseek-harness/test-bootstrap.mjs:192 → 写入配置文件 (1 处)<br>  - tests/deepseek-harness/test-bootstrap.mjs:192 → 写入 DSH 配置 (1 处)<br>  - tests/pi-omp-extensions/test-shared-core.sh:44 → 写入配置文件 (1 处)<br>  ... 共 6 处 — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - skills/writing-skills/render-graphs.js:18 → 加载 child_process 模块 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 3 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - .opencode/plugins/aegis.js:110 → 文件写入 (2 处)<br>  - .opencode/plugins/aegis.js:80 → 文件读取 (7 处)<br>  - tests/deepseek-harness/run-tests.sh:62 → 文件读取 (1 处)<br>  - tests/deepseek-harness/run-tests.sh:46 → 临时文件操作 (3 处)<br>  - tests/deepseek-harness/test-bootstrap.mjs:192 → 文件写入 (1 处)<br>  ... 共 43 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - tests/explicit-skill-requests/prompts/use-anti-entropy-governance.txt:3 → 云存储上传 (1 处)<br>  - tests/e2e/context-semantic-infrastructure-live-check.sh:287 → 云存储上传 (1 处)<br>  - tests/e2e/fixtures/workflow-quality-matrix.json:1022 → 云存储上传 (1 处)<br>  - tests/e2e/fixtures/context-semantic-infrastructure-matrix.json:234 → 云存储上传 (1 处)<br>  - skills/writing-skills/anthropic-best-practices.md:1148 → 云存储上传 (1 处)<br>  ... 共 6 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 无第三方依赖 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 24632, 注释行: 381 (1.5%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 4 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - tests/helpers/test_agentic_benchmark_process_supervisor.py:627 → 硬编码敏感信息 (1 处)<br>  - tests/helpers/test_run_agentic_benchmark.py:361 → 硬编码敏感信息 (5 处)<br>  - tests/e2e/agentic-benchmark-check.sh:968 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - CLAUDE.md:128 → 读取 git 历史 (1 处)<br>  - AGENTS.md:151 → 读取 git 历史 (1 处)<br>  - RELEASE-NOTES.md:23 → 读取 git 历史 (63 处)<br>  - tests/helpers/test_agentic_benchmark_codex_events.py:327 → 读取 git 历史 (1 处)<br>  - docs/current/AEGIS_PROMPT_HYGIENE_AND_INJECTION_BOUNDARY.md:145 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (12 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (26 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - .github/workflows/ci.yml:25 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - tests/deepseek-harness/run-tests.sh:1 → 修改系统目录 (1 处)<br>  - tests/subagent-driven-dev/run-test.sh:1 → 修改系统目录 (1 处)<br>  - tests/subagent-driven-dev/go-fractals/scaffold.sh:1 → 修改系统目录 (1 处)<br>  - tests/subagent-driven-dev/svelte-todo/scaffold.sh:1 → 修改系统目录 (1 处)<br>  - tests/codex-plugin-sync/test-sync-to-codex-plugin.sh:1 → 修改系统目录 (2 处)<br>  ... 共 125 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (21 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 281 |
| 7.2 | 未标记停止维护 | 必查 | ❌ 不通过 | 文档中发现弃用标记: deprecated |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG, 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ✅ 通过 | Stars: 1116, Forks: 50, Watchers: 5 — 高 Star 量 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | Aegis |
| 校验 URL | https://github.com/GanyuanRan/Aegis |
| 必查项通过率 | 12/33 (36%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-23 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
