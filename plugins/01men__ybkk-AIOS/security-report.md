# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/01men/ybkk-AIOS
- **校验时间**: 2026-08-25 01:21:50
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 17 | 9 | 7 |
| 🟡 推荐 | 14 | 4 | 10 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2019-04-26 (2677 天前); 公开仓库数: 12; 粉丝数: 0 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ❌ 不通过 | 未找到许可证声明 (package.json 无 license 字段且无 LICENSE 文件) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1940; 包名: dsh-enterprise-ops; 描述: 企业 AI 资源统一管理平台 —— 基于 DeepSeek Harness「一切皆插件」架构 — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - docs/dev-plan-app-sso.md:267 → 绕过权限限制 (1 处)<br>  - docs/dev-plan-app-sso.md:101 → 欺诈行为 (2 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ⚠️  需人工复核 | 无 git tag; package.json version: 1.1.0; 有版本号但无 git tag / release |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | engines: {"node": ">=22.6"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}}; Cordis 配置文件: cordis.patch.yml, cordis.yml<br>  - packages/plugin-usage/src/index.ts:201 → Monkey patch / prototype pollution<br>  - packages/plugin-connect/src/config-page.ts:43 → Monkey patch / prototype pollution<br>  - packages/platform-core/src/http.ts:83 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 501 处, 函数: 2229 个, 比例: 22.5% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: packages/plugin-connect/src/config-page.ts; 发现清理逻辑: packages/platform-core/src/http.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - docs/app-sso-integration.md:36 → 读取环境变量配置 (2 处)<br>  - packages/plugin-market/src/index.ts:246 → 读取环境变量配置 (1 处)<br>  - packages/plugin-authn/src/oidc.ts:119 → 读取环境变量配置 (5 处)<br>  - packages/plugin-iam/src/index.ts:435 → 读取环境变量配置 (2 处)<br>  - packages/plugin-connect/src/index.ts:273 → 读取环境变量配置 (1 处)<br>  ... 共 14 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - docs/app-sso-实施计划-执行版.md:33 → 读取用户主目录 (1 处)<br>  - packages/plugin-market/src/index.ts:20 → 深层目录穿越 (1 处)<br>  - packages/plugin-market/src/tools.ts:5 → 深层目录穿越 (1 处)<br>  - packages/plugin-authn/src/index.ts:17 → 深层目录穿越 (1 处)<br>  - packages/plugin-authn/src/oidc.ts:25 → 深层目录穿越 (1 处)<br>  ... 共 35 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - packages/platform-core/src/sqlite.ts:53 → 命令字符串拼接变量 (注入风险) (3 处)<br>  - packages/plugin-update/src/git.ts:74 → 开启 shell 模式 (注入风险) (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - cordis.patch.yml:27 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - package.json:12 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - package-lock.json:23 → 探测到 HTTP(S) 网络请求 (9 处)<br>  - README.md:17 → 探测到 HTTP(S) 网络请求 (6 处)<br>  - src/main.ts:26 → 探测到 HTTP(S) 网络请求 (2 处)<br>涉及的域名: 0.0.0.0, 127.0.0.1, 192.168.0.7, 192.168.1.5, api.deepseek.com, api.dingtalk.com, api.github.com, app.example.com, app.partner.example, bi.yuanbingke.com (+23 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - README.md:23 → 敏感凭证读取 (10 处)<br>  - docs/dev-plan-nas.md:54 → API Key / Token 读取 (2 处)<br>  - docs/dev-plan.md:48 → API Key / Token 读取 (1 处)<br>  - docs/ecosystem-design-v1.2.md:102 → API Key / Token 读取 (2 处)<br>  - docs/ecosystem-design-v1.2.md:102 → 敏感凭证读取 (1 处)<br>  ... 共 71 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - packages/plugin-connect/src/client.ts:115 → 写入配置文件 (2 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 2 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - src/main.ts:30 → 进程控制 (2 处)<br>  - docs/deploy-enterprise.md:82 → 临时文件操作 (2 处)<br>  - packages/plugin-authn/src/index.ts:153 → 定时任务 (1 处)<br>  - packages/plugin-authn/src/oidc.ts:139 → 定时任务 (1 处)<br>  - packages/plugin-iam/src/index.ts:411 → 定时任务 (1 处)<br>  ... 共 34 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - README.md:284 → 云存储上传 (7 处)<br>  - docs/dev-plan-nas.md:70 → multipart 上传 (1 处)<br>  - docs/dev-plan-nas.md:34 → 云存储上传 (9 处)<br>  - packages/plugin-skillhub/src/index.ts:43 → 云存储上传 (6 处)<br>  - packages/plugin-nas/src/index.ts:242 → 云存储上传 (7 处)<br>  ... 共 14 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 2. repo: 0 deps + 2 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 27496, 注释行: 1713 (6.2%) |
| 4.9 | 具备测试覆盖 | 推荐 | ⚠️  需人工复核 | 未发现测试文件 |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - docs/deploy-enterprise.md:37 → 硬编码敏感信息 (2 处)<br>  - packages/plugin-authn/src/index.ts:465 → 明文写入敏感信息 (3 处)<br>  - packages/plugin-authn/src/oidc.ts:806 → 明文写入敏感信息 (2 处)<br>  - packages/plugin-console/public/js/api.js:10 → 明文写入敏感信息 (5 处)<br>  - packages/plugin-console/public/js/pages/agents.js:432 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (16 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (1 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - docs/deploy-enterprise.md:50 → 修改系统目录 (3 处)<br>  - docs/deploy-enterprise.md:66 → 创建开机自启/系统服务 (1 处)<br>  - cli/dshctl.mjs:1 → 修改系统目录 (1 处) |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: 沙箱, 隔离 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ⚠️  需人工复核 | 未发现临时文件清理逻辑, 需确认 |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 32 |
| 7.2 | 未标记停止维护 | 必查 | ❌ 不通过 | 文档中发现弃用标记: 弃用, deprecated, archived |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | ybkk-AIOS |
| 校验 URL | https://github.com/01men/ybkk-AIOS |
| 必查项通过率 | 17/33 (52%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-25 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
