# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/FleetingEcho/dsh-powerdesk
- **校验时间**: 2026-08-23 16:25:27
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 15 | 10 | 8 |
| 🟡 推荐 | 14 | 5 | 9 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2019-01-27 (2764 天前); 公开仓库数: 58; 粉丝数: 37 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 2806; 包名: dsh-powerdesk; 描述: DSH web plugin: a GPU-accelerated terminal (restty renderer: WebGPU/WebGL2 + WAS — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - lib/client-editor.js:27846 → 破解授权 (3 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ⚠️  需人工复核 | 无 git tag; package.json version: 0.1.0; 有版本号但无 git tag / release |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/dsh-client-locale: ^0.1.0-rc.6; @deepseek-ai/dsh-client-runtime: ^0.1.0-rc.6; @deepseek-ai/dsh-client-ui-primitives: ^0.1.0-rc.6; @deepseek-ai/dsh-client-ui-slots: ^0.1.0-rc.6; @deepseek-ai/dsh-client-web-react: ^0.1.0-rc.6 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": ["@deepseek-ai/dsh-client-runtime",; Cordis/DSH 依赖: @deepseek-ai/dsh-client-locale, @deepseek-ai/dsh-client-runtime, @deepseek-ai/dsh-client-ui-primitives, @deepseek-ai/dsh-client-ui-slots, @deepseek-ai/dsh-client-web-react; Cordis 配置文件: cordis.patch.yml<br>  - tests/extension-install.spec.ts:369 → Monkey patch / prototype pollution<br>  - lib/client-calendar.js:4639 → Monkey patch / prototype pollution<br>  - lib/client-settings.js:3862 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 273 处, 函数: 3920 个, 比例: 7.0% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: src/client/extensions.ts; 发现清理逻辑: tests/extension-client.spec.ts; 发现清理逻辑: lib/client-registry.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .gitignore:14 → 读取环境变量配置 (2 处)<br>  - tsdown.config.ts:125 → 读取环境变量配置 (12 处)<br>  - prebuilt/win32-x64-msvc/dsh_powerdesk_sqlite.node:10976 → 读取浏览器 Cookie/本地存储 (1 处)<br>  - prebuilt/win32-x64-msvc/dsh_powerdesk_pty.node:1400 → 读取环境变量配置 (1 处)<br>  - prebuilt/win32-x64-msvc/dsh_powerdesk_pty.node:1559 → 读取浏览器 Cookie/本地存储 (1 处)<br>  ... 共 21 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - tsdown.config.ts:106 → 深层目录穿越 (1 处)<br>  - prebuilt/win32-x64-msvc/dsh_powerdesk_sqlite.node:10973 → 深层目录穿越 (2 处)<br>  - prebuilt/win32-x64-msvc/dsh_powerdesk_pty.node:1556 → 深层目录穿越 (2 处)<br>  - prebuilt/linux-x64-gnu/dsh_powerdesk_pty.node:355 → 深层目录穿越 (6 处)<br>  - prebuilt/darwin-arm64/dsh_powerdesk_pty.node:4315 → 深层目录穿越 (5 处)<br>  ... 共 19 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - src/calendar-api.ts:56 → 命令字符串拼接变量 (注入风险) (1 处)<br>  - lib/index.js:1671 → 命令字符串拼接变量 (注入风险) (1 处)<br>  - lib/client-editor.js:18715 → exec 命令拼接 (4 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package.json:8 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - package.json:4 → WebSocket 连接 (1 处)<br>  - package.json:4 → 浏览器网络 API (1 处)<br>  - README_ZH.md:5 → 探测到 HTTP(S) 网络请求 (17 处)<br>  - README.md:5 → 探测到 HTTP(S) 网络请求 (17 处)<br>涉及的域名: ., 127.0.0.1, 127.1.2.3, 192.168.1.10, a.com, b.com, cdn.jsdelivr.net, codemirror.net, developer.mozilla.org, docs.rs (+12 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - lib/client-editor.js:27710 → 挖矿相关 (1 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - pnpm-lock.yaml:338 → 敏感凭证读取 (5 处)<br>  - tsdown.config.ts:125 → 读取环境变量 API Key/凭证 (8 处)<br>  - examples/hello-powerdesk/tsdown.config.ts:48 → 读取环境变量 API Key/凭证 (1 处)<br>  - templates/extension/tsdown.config.ts:51 → 读取环境变量 API Key/凭证 (1 处)<br>  - src/rust-pty-deps.ts:132 → 读取环境变量 API Key/凭证 (3 处)<br>  ... 共 16 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - lib/client-editor.js:4406 → 超长 base64 字符串 (2 处) |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - tests/extension-e2e.spec.ts:83 → new Function() 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 47 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - src/index.ts:160 → 定时任务 (1 处)<br>  - src/rust-pty-manager.ts:132 → 定时任务 (1 处)<br>  - src/search-api.ts:117 → 定时任务 (1 处)<br>  - src/client/state.ts:1203 → 定时任务 (1 处)<br>  - src/client/SearchView.tsx:103 → 定时任务 (1 处)<br>  ... 共 15 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - README.md:254 → 云存储上传 (4 处)<br>  - examples/hello-powerdesk/README.md:5 → 云存储上传 (3 处)<br>  - examples/hello-powerdesk/src/index.tsx:13 → 云存储上传 (1 处)<br>  - templates/extension/README.md:16 → 云存储上传 (1 处)<br>  - src/index.ts:32 → 云存储上传 (5 处)<br>  ... 共 33 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 47. repo: 28 deps + 19 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 39599, 注释行: 9304 (23.5%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 37 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - prebuilt/win32-x64-msvc/dsh_powerdesk_sqlite.node:11193 → 硬编码敏感信息 (2 处)<br>  - src/client/notes-prefs.ts:24 → 明文写入敏感信息 (2 处)<br>  - src/client/service.ts:498 → 明文写入敏感信息 (1 处)<br>  - src/client/prefs.ts:232 → 明文写入敏感信息 (1 处)<br>  - src/client/explorer-prefs.ts:54 → 明文写入敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (15 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (3 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - prebuilt/linux-x64-gnu/dsh_powerdesk_pty.node:493 → 修改系统目录 (3 处)<br>  - prebuilt/darwin-arm64/dsh_powerdesk_pty.node:3 → 修改系统目录 (2 处)<br>  - prebuilt/darwin-x64/dsh_powerdesk_pty.node:4 → 修改系统目录 (2 处)<br>  - src/index.ts:303 → 创建开机自启/系统服务 (1 处)<br>  - src/shell.ts:7 → 创建开机自启/系统服务 (1 处)<br>  ... 共 14 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: sandbox |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (15 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 5 天; 提交总数: 35 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG, 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 1, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-powerdesk |
| 校验 URL | https://github.com/FleetingEcho/dsh-powerdesk |
| 必查项通过率 | 15/33 (45%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-23 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
