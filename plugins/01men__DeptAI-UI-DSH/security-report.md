# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/01men/DeptAI-UI-DSH
- **校验时间**: 2026-11-01 04:58:57
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 14 | 12 | 7 |
| 🟡 推荐 | 14 | 6 | 8 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2019-04-26 (2746 天前); 公开仓库数: 30; 粉丝数: 0 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 283; 包名: @ybkk/gate-01; 描述: 01门 —— AI 代理与人类的协作前台（基于 DeepSeek Harness「一切皆插件」架构） — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - docs/dev-plan-app-sso.md:267 → 绕过权限限制 (1 处)<br>  - docs/dev-plan-app-sso.md:101 → 欺诈行为 (2 处)<br>  - packages/plugin-rq-card/src/hostlink.ts:18 → 欺诈行为 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ⚠️  需人工复核 | 无 git tag; package.json version: 1.2.1; 有版本号但无 git tag / release |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | engines: {"node": ">=22.6"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "immediately": true, "inje; Cordis 配置文件: cordis.yml, cordis.patch.yml<br>  - docs/plan-gate01.md:144 → Monkey patch / prototype pollution<br>  - docs/dev-plan-agent-host-unification.md:27 → Monkey patch / prototype pollution<br>  - docs/handoff-host-features-to-main.md:31 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 1309 处, 函数: 5874 个, 比例: 22.3% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: docs/qa-evidence/served-client-3080.js; 发现清理逻辑: packages/plugin-connect/src/config-page.ts; 发现清理逻辑: packages/platform-core/src/http.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - docs/dev-plan-connector.md:98 → 读取环境变量配置 (1 处)<br>  - docs/rebrand-yuanbingke-20261014.md:71 → 读取 SSH 私钥目录 (1 处)<br>  - docs/connector-integration.md:89 → 读取环境变量配置 (5 处)<br>  - docs/app-sso-integration.md:47 → 读取环境变量配置 (2 处)<br>  - docs/dev-log-connector/PROGRESS.md:121 → 读取环境变量配置 (1 处)<br>  ... 共 47 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - archive/plugin-billing/src/index.ts:24 → 深层目录穿越 (2 处)<br>  - archive/plugin-billing/src/tools.ts:5 → 深层目录穿越 (1 处)<br>  - docs/dev-plan-access-hardening.md:191 → 深层目录穿越 (1 处)<br>  - docs/app-sso-实施计划-执行版.md:33 → 读取用户主目录 (1 处)<br>  - packages/plugin-agent/src/index.ts:15 → 深层目录穿越 (6 处)<br>  ... 共 61 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - packages/plugin-panel-core/src/dws.ts:366 → exec 命令拼接 (2 处)<br>  - packages/plugin-panel-core/src/dws.ts:96 → 开启 shell 模式 (注入风险) (2 处)<br>  - packages/platform-core/src/sqlite.ts:53 → 命令字符串拼接变量 (注入风险) (3 处)<br>  - packages/plugin-update/src/git.ts:74 → 开启 shell 模式 (注入风险) (1 处)<br>  - scripts/release.mjs:55 → 开启 shell 模式 (注入风险) (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package-lock.json:26 → 探测到 HTTP(S) 网络请求 (88 处)<br>  - llms.txt:7 → 探测到 HTTP(S) 网络请求 (11 处)<br>  - 产品.html:8 → 探测到 HTTP(S) 网络请求 (11 处)<br>  - package.json:6 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - README.md:6 → 探测到 HTTP(S) 网络请求 (9 处)<br>涉及的域名: ..., 0.0.0.0, 10.0.0.3, 127.0.0.1, 172.16.1.9, 172.32.1.9, 192.168.0.4, 192.168.0.7, 192.168.1.5, 8.8.8.8 (+53 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - docs/connector-integration.md:203 → 代理/隧道 (2 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - skills/dsh-ops-iam/SKILL.md:9 → 敏感凭证读取 (1 处)<br>  - skills/dsh-ops-agent/SKILL.md:32 → 敏感凭证读取 (2 处)<br>  - skills/dsh-ops-admin/SKILL.md:15 → 敏感凭证读取 (2 处)<br>  - skills/dsh-ops-connector/SKILL.md:30 → API Key / Token 读取 (2 处)<br>  - skills/dsh-ops-connector/SKILL.md:30 → 敏感凭证读取 (2 处)<br>  ... 共 197 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - packages/plugin-connect/src/client.ts:120 → 写入配置文件 (2 处)<br>  - packages/plugin-console/src/index.ts:3747 → 修改全局配置 (1 处)<br>  - packages/plugin-rq-card/src/hostlink.ts:365 → 写入配置文件 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - scripts/extract-panel-seed.mjs:20 → new Function() 任意代码执行 (1 处)<br>  - tests/selftest.mjs:800 → node:vm 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 4 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - 产品.html:1053 → 定时任务 (11 处)<br>  - docs/workflow-issue-patrol-automation-20261029.md:37 → 临时文件操作 (1 处)<br>  - docs/spike-cordis-optional-inject.md:89 → 定时任务 (6 处)<br>  - docs/spike-cordis-optional-inject.md:111 → 进程控制 (1 处)<br>  - docs/deploy-enterprise.md:133 → 临时文件操作 (2 处)<br>  ... 共 91 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - docs/dev-plan-nas.md:70 → multipart 上传 (2 处)<br>  - docs/dev-plan-nas.md:34 → 云存储上传 (13 处)<br>  - docs/drill-full-chain-l3.md:87 → 云存储上传 (2 处)<br>  - docs/dev-plan-nas-authz.md:104 → 云存储上传 (1 处)<br>  - docs/integrations/synology-filestation-mcp/test/authz-smoke.mjs:93 → 云存储上传 (4 处)<br>  ... 共 25 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 4. repo: 0 deps + 4 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 66631, 注释行: 6936 (10.4%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 2 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - docs/deploy-enterprise.md:46 → 硬编码敏感信息 (2 处)<br>  - docs/connector-integration.md:91 → 硬编码敏感信息 (1 处)<br>  - docs/qa-report-20260912-group-a-security.md:59 → 硬编码敏感信息 (3 处)<br>  - docs/integrations/synology-filestation-mcp/test/authz-smoke.mjs:16 → 硬编码敏感信息 (3 处)<br>  - docs/integrations/synology-filestation-mcp/src/authz.js:91 → 从环境变量获取敏感信息 (9 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - AGENTS.md:81 → 读取 git 历史 (2 处)<br>  - docs/dev-plan-access-hardening.md:26 → 读取 git 历史 (1 处)<br>  - docs/handoff-f-remainder-adoption-20260910.md:4 → 读取 git 历史 (1 处)<br>  - docs/handoff-f-remainder-to-main.md:13 → 读取 git 历史 (1 处)<br>  - docs/host-features-ops-notes.md:57 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (48 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (11 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - docs/portal-integration.md:103 → 创建开机自启/系统服务 (1 处)<br>  - docs/deploy-enterprise.md:87 → 修改系统目录 (3 处)<br>  - docs/deploy-enterprise.md:102 → 创建开机自启/系统服务 (3 处)<br>  - docs/connector-integration.md:201 → 修改系统目录 (1 处)<br>  - docs/deploy-mac-form-b.md:47 → 创建开机自启/系统服务 (3 处)<br>  ... 共 19 处 |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (6 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 2 天; 提交总数: 263 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 2, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | DeptAI-UI-DSH |
| 校验 URL | https://github.com/01men/DeptAI-UI-DSH |
| 必查项通过率 | 14/33 (42%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-11-01 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
