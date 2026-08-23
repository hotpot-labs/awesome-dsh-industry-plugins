# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/AgentConnect/dsh-awiki
- **校验时间**: 2026-08-23 14:23:41
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 18 | 10 | 5 |
| 🟡 推荐 | 14 | 6 | 8 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2025-02-16 (553 天前); 公开仓库数: 12; 粉丝数: 11 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 2957; 包名: @awiki/dsh-plugin; 描述: AWiki identity and messaging plugin for DeepSeek Harness — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (16): v0.3.1, v0.2.4, v0.2.3, v0.2.2, v0.2.1; package.json version: 0.3.2; GitHub Releases (5): v0.2.4, v0.2.3, v0.2.2, v0.2.1, v0.2.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.1; @deepseek-ai/dsh-agent: 0.1.1-rc.2; @deepseek-ai/dsh-agent-default-model: 0.1.1-rc.2; @deepseek-ai/dsh-api-remotes: 0.1.1-rc.2; @deepseek-ai/dsh-brand: 0.1.1-rc.2 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": ["@deepseek-ai/dsh-client-runtime",; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-agent, @deepseek-ai/dsh-agent-default-model, @deepseek-ai/dsh-api-remotes, @deepseek-ai/dsh-brand; Cordis 配置文件: cordis.patch.yml<br>  - src/external-http-auth.ts:49 → Monkey patch / prototype pollution<br>  - tests/external-http-auth.spec.ts:164 → Monkey patch / prototype pollution<br>  - packages/dsh-model-proxy/lib/index.js:200 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 667 处, 函数: 4668 个, 比例: 14.3% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: src/index.ts; 发现清理逻辑: src/listener.ts; 发现清理逻辑: src/summary-provider.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .gitignore:8 → 读取环境变量配置 (3 处)<br>  - cordis.patch.yml:8 → 读取环境变量配置 (17 处)<br>  - README.md:286 → 读取环境变量配置 (1 处)<br>  - README.zh.md:241 → 读取环境变量配置 (1 处)<br>  - tsdown.config.ts:109 → 读取环境变量配置 (6 处)<br>  ... 共 19 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - src/index.ts:441 → 读取用户主目录 (1 处)<br>  - docs/dsh-device-join-design.md:5 → 深层目录穿越 (4 处)<br>  - packages/dsh-model-proxy/tsconfig.client.json:2 → 深层目录穿越 (1 处)<br>  - packages/dsh-model-proxy/vitest.config.ts:8 → 深层目录穿越 (3 处)<br>  - packages/dsh-model-proxy/tsconfig.json:2 → 深层目录穿越 (1 处)<br>  ... 共 16 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - pnpm-lock.yaml:341 → WebSocket 连接 (3 处)<br>  - pnpm-lock.yaml:341 → 浏览器网络 API (3 处)<br>  - design-qa.md:52 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - AWIKI_MAIL_UI_DESIGN.md:279 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - cordis.patch.yml:8 → 探测到 HTTP(S) 网络请求 (3 处)<br>涉及的域名: 127.0.0.1, alice, api.example, api.example.com, api.example.test, awiki.ai, awiki.example, bad.example, github.com, localhost (+16 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - tests/baseline/migration-contract.json:420 → 代理/隧道 (3 处)<br>  - packages/dsh-model-proxy/lib/client.js:2794 → 代理/隧道 (1 处)<br>  - packages/dsh-model-proxy/lib/types/client/index.js:3 → 代理/隧道 (1 处)<br>  - packages/dsh-model-proxy/lib/types/client/ModelProxySettingsSection.js:277 → 代理/隧道 (1 处)<br>  - scripts/check-generated.mjs:60 → 代理/隧道 (2 处)<br>  ... 共 6 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - pnpm-lock.yaml:301 → 敏感凭证读取 (56 处)<br>  - design-qa.md:46 → 敏感凭证读取 (1 处)<br>  - cordis.patch.yml:8 → 读取环境变量 API Key/凭证 (17 处)<br>  - README.md:30 → API Key / Token 读取 (2 处)<br>  - README.md:14 → 敏感凭证读取 (8 处)<br>  ... 共 98 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - tests/settings.spec.ts:117 → 修改设置 (2 处)<br>  - tests/loader-composition.spec.ts:42 → 写入配置文件 (1 处)<br>  - packages/dsh-model-proxy/src/index.ts:304 → 修改设置 (3 处)<br>  - packages/dsh-model-proxy/lib/index.js:223 → 修改设置 (3 处)<br>  - packages/dsh-model-proxy/lib/types/index.js:241 → 修改设置 (3 处)<br>  ... 共 6 处 — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - lib/client.js:152 → new Function() 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 42 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - design-qa.md:9 → 临时文件操作 (12 处)<br>  - src/index.ts:1118 → 定时任务 (2 处)<br>  - src/summary-provider.ts:173 → 定时任务 (1 处)<br>  - src/client/AwikiOverlay.tsx:1571 → 定时任务 (1 处)<br>  - src/client/controller.ts:687 → 定时任务 (2 处)<br>  ... 共 27 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - pnpm-lock.yaml:293 → 云服务 SDK (可能用于隐蔽上传) (100 处)<br>  - src/index.ts:1519 → 云存储上传 (1 处)<br>  - src/provider-api.ts:127 → 云存储上传 (4 处)<br>  - src/types.ts:424 → 云存储上传 (2 处)<br>  - src/tools.ts:155 → 云存储上传 (1 处)<br>  ... 共 13 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 42. repo: 3 deps + 39 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 55004, 注释行: 3299 (6.0%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 38 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - tests/mail-list-cache.client.spec.ts:49 → 明文写入敏感信息 (1 处)<br>  - tests/harness.ts:307 → 硬编码敏感信息 (1 处)<br>  - tests/sdk-adapter.spec.ts:513 → 硬编码敏感信息 (2 处)<br>  - tests/external-http-auth.spec.ts:34 → 硬编码敏感信息 (2 处)<br>  - packages/dsh-model-proxy/src/client/settings-locales.ts:174 → 硬编码敏感信息 (2 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (17 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (10 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - design-qa.md:47 → 创建开机自启/系统服务 (1 处) |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (3 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 80 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 10, Forks: 0, Watchers: 0 — 有一定社区基础 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-awiki |
| 校验 URL | https://github.com/AgentConnect/dsh-awiki |
| 必查项通过率 | 18/33 (55%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-23 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
