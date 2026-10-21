# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/Oxygen-Wang/dsh-cursorlike-sidebar
- **校验时间**: 2026-10-21 03:52:47
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 12 | 12 | 9 |
| 🟡 推荐 | 14 | 7 | 6 | 1 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2021-09-12 (1864 天前); 公开仓库数: 10; 粉丝数: 1 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1327; 包名: dsh-cursorlike-sidebar; 描述: CursorLike Sidebar：嵌入 DSH 的文件树、代码编辑、终端、Git、侧边对话与 Ctrl+L/拖放引用交互 — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - lib/client-terminal.js:10595 → 盗版/侵权 (2 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (1): v0.28.0-cursorlike.1; package.json version: 0.28.0-cursorlike.4-beta.1; GitHub Releases (1): v0.28.0-cursorlike.1 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.5; @deepseek-ai/dsh-agent: ^0.2.1-rc.1; @deepseek-ai/dsh-client-locale: ^0.2.1-rc.1; @deepseek-ai/dsh-client-ui-conversation: ^0.2.1-rc.1; @deepseek-ai/dsh-client-ui-primitives: ^0.2.1-rc.1 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": ["@deepseek-ai/dsh-client-locale", ; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-agent, @deepseek-ai/dsh-client-locale, @deepseek-ai/dsh-client-ui-conversation, @deepseek-ai/dsh-client-ui-primitives; Cordis 配置文件: cordis.patch.yml<br>  - CHANGELOG.md:81 → Monkey patch / prototype pollution<br>  - lib/types/index.d.ts:65 → Monkey patch / prototype pollution<br>  - tests/terminal-tab.spec.tsx:168 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 805 处, 函数: 9820 个, 比例: 8.2% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: lib/index.js; 发现清理逻辑: lib/types/context-types.d.ts; 发现清理逻辑: lib/types/sidechat-push.d.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - vitest.config.ts:16 → 读取环境变量配置 (1 处)<br>  - .gitignore:14 → 读取环境变量配置 (2 处)<br>  - tsdown.config.ts:139 → 读取环境变量配置 (12 处)<br>  - CHANGELOG.md:179 → 读取环境变量配置 (1 处)<br>  - lib/client-locale.js:623 → 读取 SSH 私钥目录 (17 处)<br>  ... 共 92 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - tsdown.config.ts:115 → 深层目录穿越 (1 处)<br>  - lib/index.js:1714 → 读取用户主目录 (5 处)<br>  - lib/types/client/changes/GitLens.d.ts:1 → 深层目录穿越 (1 处)<br>  - lib/types/client/changes/DiffPane.d.ts:20 → 深层目录穿越 (1 处)<br>  - lib/types/client/changes/ops.d.ts:4 → 深层目录穿越 (1 处)<br>  ... 共 42 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - lib/client-registry.js:16546 → exec 命令拼接 (1 处)<br>  - lib/client.js:16546 → exec 命令拼接 (1 处)<br>  - src/client/diff/rows.ts:370 → exec 命令拼接 (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - CHANGELOG_EN.md:3 → 探测到 HTTP(S) 网络请求 (116 处)<br>  - CHANGELOG_EN.md:40 → WebSocket 连接 (2 处)<br>  - CHANGELOG_EN.md:40 → 浏览器网络 API (2 处)<br>  - package.json:8 → 探测到 HTTP(S) 网络请求 (5 处)<br>  - README.md:159 → 探测到 HTTP(S) 网络请求 (6 处)<br>涉及的域名: 127.0.0.1, 192.168.1.1, a.example, a.test, b.example, claimed.example.com, code.visualstudio.com, docs.cursor.com, docs.example.com, dsh.internal (+21 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - lib/client-locale.js:1898 → 挖矿相关 (1 处)<br>  - lib/client-terminal.js:6283 → DDoS 攻击 (1 处)<br>  - src/client/locales-fr.ts:550 → 挖矿相关 (1 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - CHANGELOG_EN.md:226 → 敏感凭证读取 (1 处)<br>  - vitest.config.ts:16 → 读取环境变量 API Key/凭证 (1 处)<br>  - tsdown.config.ts:139 → 读取环境变量 API Key/凭证 (8 处)<br>  - pnpm-workspace.yaml:36 → 敏感凭证读取 (1 处)<br>  - lib/client-locale.js:617 → 敏感凭证读取 (31 处)<br>  ... 共 78 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - lib/index.js:9334 → 修改设置 (1 处)<br>  - tests/smoke.spec.ts:1780 → 写入配置文件 (2 处)<br>  - tests/fs-search.spec.ts:56 → 写入配置文件 (1 处)<br>  - tests/session-path.spec.ts:80 → 写入配置文件 (2 处)<br>  - src/index.ts:1416 → 修改设置 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - tests/helpers/github-slug-reference.ts:29 → 连续十六进制转义 (混淆) (1 处) |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - tests/chunk-artifact.spec.ts:46 → new Function() 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 106 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - CHANGELOG.md:43 → 定时任务 (1 处)<br>  - CHANGELOG.md:72 → 临时文件操作 (2 处)<br>  - lib/client-terminal.js:922 → 定时任务 (33 处)<br>  - lib/index.js:453 → 定时任务 (7 处)<br>  - lib/index.js:1627 → 临时文件操作 (2 处)<br>  ... 共 132 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - CHANGELOG_EN.md:58 → 云存储上传 (20 处)<br>  - playwright.config.ts:29 → 云存储上传 (1 处)<br>  - CHANGELOG.md:95 → 云存储上传 (3 处)<br>  - lib/client-locale.js:338 → 云存储上传 (260 处)<br>  - lib/client-terminal.js:13415 → 云存储上传 (37 处)<br>  ... 共 87 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ❌ 不通过 | 总依赖数: 106. repo: 32 deps + 74 devDeps — 依赖过多 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 114408, 注释行: 32357 (28.3%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 145 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - lib/client-registry.js:11656 → 明文写入敏感信息 (10 处)<br>  - lib/client.js:11656 → 明文写入敏感信息 (10 处)<br>  - tests/redact.spec.ts:35 → 硬编码敏感信息 (4 处)<br>  - tests/archive.spec.ts:799 → 明文写入敏感信息 (1 处)<br>  - tests/e2e-aggregate-auth.spec.ts:59 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - CHANGELOG_EN.md:232 → 读取 git 历史 (1 处)<br>  - README.md:9 → 读取 git 历史 (2 处)<br>  - vitest.config.ts:68 → 读取 git 历史 (1 处)<br>  - CHANGELOG.md:87 → 读取 git 历史 (2 处)<br>  - lib/index.js:273 → 读取 git 历史 (4 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (66 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (14 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - lib/client-terminal.js:507 → 创建开机自启/系统服务 (3 处)<br>  - lib/client-terminal.js:8672 → Windows 系统配置修改 (1 处)<br>  - lib/index.js:1629 → 修改系统目录 (7 处)<br>  - lib/types/session-path.d.ts:21 → 修改系统目录 (1 处)<br>  - docs/plans/2026-09-08-terminal-shell-config-hardening-plan.md:76 → 修改系统目录 (7 处)<br>  ... 共 21 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (48 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 34 |
| 7.2 | 未标记停止维护 | 必查 | ❌ 不通过 | 文档中发现弃用标记: 不再支持, 弃用 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 1, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-cursorlike-sidebar |
| 校验 URL | https://github.com/Oxygen-Wang/dsh-cursorlike-sidebar |
| 必查项通过率 | 12/33 (36%) |
| 推荐项满足率 | 13/14 (约 93%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-21 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
