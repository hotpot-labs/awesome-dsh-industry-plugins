# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/aa2246740/dsh-oauth-login
- **校验时间**: 2026-10-13 06:02:34
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 17 | 11 | 5 |
| 🟡 推荐 | 14 | 5 | 9 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2014-12-13 (4321 天前); 公开仓库数: 56; 粉丝数: 6 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: Apache-2.0 (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 375; 包名: dsh-oauth-login; 描述: DSH-owned subscription login powered by Pi AI adapters: OAuth plus official Plan — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - lib/bin.js:474 → 盗版/侵权 (3 处)<br>  - lib/index.js:690 → 盗版/侵权 (3 处)<br>  - tests/openrouter.spec.ts:31 → 盗版/侵权 (2 处)<br>  - src/openrouter-models.ts:97 → 盗版/侵权 (3 处)<br>  - docs/openrouter-sync.md:29 → 盗版/侵权 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (6): v0.2.8, v0.2.7, v0.2.6, v0.2.5, v0.2.4; package.json version: 0.2.8; GitHub Releases (5): v0.2.7, v0.2.6, v0.2.5, v0.2.4, v0.1.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.2; @deepseek-ai/dsh: >=0.2.0-rc.2 <0.2.1; @deepseek-ai/dsh-atomic-write: *; @deepseek-ai/dsh-attachment: *; @deepseek-ai/dsh-client-connection: >=0.2.0-rc.2 <0.2.1 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": ["@deepseek-ai/dsh-client-ui-conver; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh, @deepseek-ai/dsh-atomic-write, @deepseek-ai/dsh-attachment, @deepseek-ai/dsh-client-connection; Cordis 配置文件: cordis.patch.yml, cordis.yml, dshx.yml<br>  - lib/bin.js:1073 → Monkey patch / prototype pollution<br>  - lib/index.js:1589 → Monkey patch / prototype pollution<br>  - src/proxy-transport.ts:40 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 199 处, 函数: 1695 个, 比例: 11.7% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: lib/index.d.ts; 发现清理逻辑: lib/bin.js; 发现清理逻辑: lib/client.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - tsdown.config.ts:17 → 读取环境变量配置 (1 处)<br>  - lib/bin.js:876 → 读取环境变量配置 (6 处)<br>  - lib/index.js:1390 → 读取环境变量配置 (6 处)<br>  - tools/client-build.js:77 → 读取环境变量配置 (7 处)<br>  - scripts/verify-network-settings-ui.mjs:39 → 读取环境变量配置 (1 处)<br>  ... 共 8 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - tsdown.config.ts:18 → 读取用户主目录 (1 处)<br>  - scripts/verify-network-settings-ui.mjs:18 → 读取用户主目录 (1 处) — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - pnpm-lock.yaml:180 → WebSocket 连接 (3 处)<br>  - pnpm-lock.yaml:180 → 浏览器网络 API (3 处)<br>  - LICENSE:3 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - SECURITY.md:22 → WebSocket 连接 (1 处)<br>  - SECURITY.md:22 → 浏览器网络 API (1 处)<br>涉及的域名: 127.0.0.1, api.openai.com, api.x.ai, auth.openai.com, auth.x.ai, bigmodel.cn, chatgpt.com, claude.ai, developers.openai.com, docs.bigmodel.cn (+11 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - LICENSE:149 → 挖矿相关 (1 处)<br>  - lib/bin.js:956 → 代理/隧道 (1 处)<br>  - lib/index.js:1472 → 代理/隧道 (1 处)<br>  - tests/store.spec.ts:116 → 代理/隧道 (4 处)<br>  - tests/openrouter-routes.spec.ts:102 → 代理/隧道 (1 处)<br>  ... 共 8 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - tsdown.config.ts:17 → 读取环境变量 API Key/凭证 (1 处)<br>  - pnpm-lock.yaml:29 → 敏感凭证读取 (46 处)<br>  - SECURITY.md:9 → 敏感凭证读取 (5 处)<br>  - cordis.patch.yml:1 → API Key / Token 读取 (1 处)<br>  - README.en.md:25 → 敏感凭证读取 (3 处)<br>  ... 共 68 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - scripts/verify-network-settings-ui.mjs:30 → 写入配置文件 (2 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 37 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - lib/bin.js:860 → 定时任务 (2 处)<br>  - lib/client.js:38 → 定时任务 (4 处)<br>  - lib/index.js:1374 → 定时任务 (3 处)<br>  - .github/workflows/publish.yml:74 → 进程控制 (2 处)<br>  - scripts/verify-network-settings-ui.mjs:67 → 开启监听端口 (1 处)<br>  ... 共 17 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - pnpm-lock.yaml:132 → 云服务 SDK (可能用于隐蔽上传) (94 处)<br>  - pnpm-lock.yaml:250 → 云存储上传 (1 处)<br>  - lib/client.js:1384 → 云存储上传 (1 处)<br>  - src/client/SearchableModelSelect.tsx:482 → 云存储上传 (1 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 36. repo: 1 deps + 35 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 16055, 注释行: 876 (5.5%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 19 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - lib/bin.js:1465 → 从环境变量获取敏感信息 (1 处)<br>  - lib/index.js:1986 → 从环境变量获取敏感信息 (1 处)<br>  - tests/openrouter.spec.ts:330 → 硬编码敏感信息 (1 处)<br>  - tests/store.spec.ts:87 → 明文写入敏感信息 (1 处)<br>  - tests/native-tools.spec.ts:51 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (11 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ⚠️  需人工复核 | 未发现一键清理功能, 需确认是否有数据清理机制 |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - lib/bin.js:1 → 修改系统目录 (2 处)<br>  - lib/index.js:1341 → 修改系统目录 (1 处)<br>  - src/http.ts:88 → 修改系统目录 (1 处)<br>  - src/bin.ts:1 → 修改系统目录 (1 处) |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (1 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 5 天; 提交总数: 52 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 1, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-oauth-login |
| 校验 URL | https://github.com/aa2246740/dsh-oauth-login |
| 必查项通过率 | 17/33 (52%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-13 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
