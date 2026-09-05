# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/All3nCN/dsh-better-sidebar-N23
- **校验时间**: 2026-09-05 03:32:42
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
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2023-01-16 (1328 天前); 公开仓库数: 7; 粉丝数: 0 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 310; 包名: @all3cn/dsh-better-sidebar-n23; 描述: DSH web plugin: complete workbench (explorer / editors / previews / terminal / g — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - lib/client-editor.js:22945 → 破解授权 (3 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (1): v0.1.0; package.json version: 0.1.0; GitHub Releases (1): v0.1.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: >=0.1.0-rc.6 <0.2.0; @deepseek-ai/dsh-agent: >=0.1.0-rc.6 <0.2.0; @deepseek-ai/dsh-client-locale: >=0.1.0-rc.6 <0.2.0; @deepseek-ai/dsh-client-runtime: >=0.1.0-rc.6 <0.2.0; @deepseek-ai/dsh-client-schema-form: >=0.1.0-rc.6 <0.2.0 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": ["@deepseek-ai/dsh-client-runtime",; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-agent, @deepseek-ai/dsh-client-locale, @deepseek-ai/dsh-client-runtime, @deepseek-ai/dsh-client-schema-form; Cordis 配置文件: cordis.patch.yml<br>  - lib/client-editor.js:7180 → Monkey patch / prototype pollution<br>  - lib/types/index.d.ts:26 → Monkey patch / prototype pollution<br>  - src/index.ts:181 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 338 处, 函数: 3892 个, 比例: 8.7% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: tests/invariant.test.mjs; 发现清理逻辑: lib/client-registry.js; 发现清理逻辑: lib/index.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - lib/client-registry.js:1793 → 读取浏览器 Cookie/本地存储 (1 处)<br>  - lib/client-editor.js:18824 → 读取环境变量配置 (2 处)<br>  - lib/client-editor.js:33098 → 读取浏览器 Cookie/本地存储 (1 处)<br>  - lib/index.js:593 → 读取环境变量配置 (8 处)<br>  - lib/client.js:1796 → 读取浏览器 Cookie/本地存储 (1 处)<br>  ... 共 11 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - lib/index.js:875 → 读取用户主目录 (2 处)<br>  - lib/types/client/builtins/index.d.ts:9 → 深层目录穿越 (1 处)<br>  - lib/types/client/builtins/tabs.d.ts:1 → 深层目录穿越 (1 处)<br>  - src/pty-manager.ts:286 → 读取用户主目录 (2 处)<br>  - src/pty-deps.ts:139 → 读取用户主目录 (1 处)<br>  ... 共 7 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - lib/client-editor.js:16815 → exec 命令拼接 (4 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - UPSTREAM.md:7 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - CHANGELOG.md:4 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - README_EN.md:5 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - dsh-plugin.json:10 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - package.json:8 → 探测到 HTTP(S) 网络请求 (3 处)<br>涉及的域名: ., bellard.org, dsh.internal, github.com, keepachangelog.com, semver.org, www.w3.org<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - lib/client-editor.js:24452 → 挖矿相关 (1 处)<br>  - lib/client-editor.js:30776 → 代理/隧道 (5 处)<br>  - lib/client-terminal.js:6263 → DDoS 攻击 (1 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - lib/client-editor.js:18824 → 读取环境变量 API Key/凭证 (1 处)<br>  - lib/client-editor.js:24602 → 敏感凭证读取 (5 处)<br>  - lib/index.js:875 → 读取环境变量 API Key/凭证 (3 处)<br>  - lib/index.js:1119 → 敏感凭证读取 (3 处)<br>  - lib/types/context-types.d.ts:357 → 敏感凭证读取 (2 处)<br>  ... 共 12 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - lib/index.js:2607 → 修改设置 (1 处)<br>  - src/index.ts:521 → 修改设置 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - lib/client-editor.js:4389 → 超长 base64 字符串 (2 处) |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 45 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - lib/client-registry.js:960 → 定时任务 (9 处)<br>  - lib/client-editor.js:7391 → 定时任务 (15 处)<br>  - lib/index.js:599 → 定时任务 (4 处)<br>  - lib/client.js:963 → 定时任务 (9 处)<br>  - lib/client-terminal.js:859 → 定时任务 (15 处)<br>  ... 共 22 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - lib/client-editor.js:24565 → multipart 上传 (1 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 26. repo: 26 deps + 0 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 43637, 注释行: 9312 (21.3%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - lib/client-editor.js:31049 → 硬编码敏感信息 (13 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - lib/client-registry.js:3083 → 读取 git 历史 (7 处)<br>  - lib/index.js:557 → 读取 git 历史 (4 处)<br>  - lib/client.js:3090 → 读取 git 历史 (7 处)<br>  - lib/types/git.d.ts:13 → 读取 git 历史 (4 处)<br>  - lib/types/client/DiffView.d.ts:36 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (16 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (5 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - lib/index.js:1120 → 创建开机自启/系统服务 (1 处)<br>  - lib/client-terminal.js:733 → 创建开机自启/系统服务 (4 处)<br>  - lib/types/pty-manager.d.ts:103 → 创建开机自启/系统服务 (1 处)<br>  - scripts/install.sh:1 → 修改系统目录 (1 处)<br>  - scripts/package-registry.mjs:1 → 修改系统目录 (1 处)<br>  ... 共 7 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: 沙箱, 隔离 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (5 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 1 天; 提交总数: 10 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: 配置说明 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-better-sidebar-N23 |
| 校验 URL | https://github.com/All3nCN/dsh-better-sidebar-N23 |
| 必查项通过率 | 14/33 (42%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-09-05 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
