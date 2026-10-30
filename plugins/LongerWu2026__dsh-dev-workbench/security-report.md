# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/LongerWu2026/dsh-dev-workbench
- **校验时间**: 2026-10-30 04:56:34
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 15 | 12 | 6 |
| 🟡 推荐 | 14 | 7 | 7 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2021-11-28 (1796 天前); 公开仓库数: 6; 粉丝数: 0 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 241; 包名: dsh-dev-workbench; 描述: 智能工作台 — DeepSeek Harness 原生插件：待办、待回复、AI 资讯、知识空间、多 AI 对话与开发工具。 — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - docs/IMPLEMENTATION-STATUS-0.2.0.md:56 → 绕过权限限制 (1 处)<br>  - host-integration/tests/runtime.mjs:60 → 盗版/侵权 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (2): v0.2.1, v0.2.0; package.json version: 0.2.1; GitHub Releases (2): v0.2.1, v0.2.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | engines: {"node": ">=22.19.0"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "inject": ["@deepseek-ai/d; Cordis 配置文件: cordis.patch.yml<br>  - index.js:214 → Monkey patch / prototype pollution<br>  - client.js:1213 → Monkey patch / prototype pollution<br>  - src/host/storage/change-history.ts:47 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 592 处, 函数: 5716 个, 比例: 10.4% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: index.js; 发现清理逻辑: host-integration/apply.mjs; 发现清理逻辑: src/host/plugin.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .gitignore:4 → 读取环境变量配置 (2 处)<br>  - index.js:73 → 读取环境变量配置 (8 处)<br>  - client.js:15263 → 读取环境变量配置 (1 处)<br>  - client.js:18133 → 读取浏览器 Cookie/本地存储 (2 处)<br>  - host-integration/prepare-local-app.mjs:33 → 读取环境变量配置 (5 处)<br>  ... 共 38 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - index.js:72 → 读取用户主目录 (7 处)<br>  - host-integration/prepare-local-app.mjs:33 → 读取用户主目录 (1 处)<br>  - proposals/persistent-browser/CONTRACT.md:3 → 深层目录穿越 (1 处)<br>  - src/host/platform/runtime.ts:42 → 读取用户主目录 (3 处)<br>  - src/host/application/web-ai-history.ts:1 → 深层目录穿越 (1 处)<br>  ... 共 105 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - index.js:2083 → 进程执行 (4 处)<br>  - host-integration/recover-loopback-cookies.py:52 → Python subprocess (1 处)<br>  - src/host/platform/command-runner.ts:82 → 进程执行 (1 处)<br>  - src/host/integrations/yunzhijia.ts:193 → 进程执行 (1 处)<br>  - src/host/integrations/project-runtime.ts:50 → 进程执行 (2 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package.json:7 → 探测到 HTTP(S) 网络请求 (4 处)<br>  - icon.svg:1 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - README.md:9 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - index.js:335 → 探测到 HTTP(S) 网络请求 (10 处)<br>  - index.js:3141 → fetch 网络请求 (9 处)<br>涉及的域名: 127.0.0.1, 127.0.0.1.example.com, 127.0.0.2, 192.168.1.20, 203.0.113.10, a, api-docs.deepseek.com, api.github.com, chatglm.cn, chatgpt.com (+35 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - index.js:73 → 读取环境变量 API Key/凭证 (6 处)<br>  - index.js:36 → 敏感凭证读取 (7 处)<br>  - client.js:17152 → 敏感凭证读取 (3 处)<br>  - docs/PROJECT-ARCHITECTURE-AND-FEATURES.md:128 → 敏感凭证读取 (1 处)<br>  - docs/IMPLEMENTATION-STATUS-0.2.0.md:56 → 敏感凭证读取 (1 处)<br>  ... 共 57 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - tests/message-boundary.mjs:20 → 写入配置文件 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - plugin-tests/tests/web-ai-attachments.test.jsx:22 → eval() 任意代码执行 (15 处)<br>  - plugin-tests/tests/load-plugin.mjs:28 → new Function() 任意代码执行 (1 处)<br>  - plugin-tests/tests/web-ai.test.jsx:29 → eval() 任意代码执行 (1 处)<br>  - plugin-tests/tests/web-ai-capture.test.jsx:11 → eval() 任意代码执行 (2 处)<br>  - tests/client-render.mjs:119 → new Function() 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 5 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - index.js:59 → 定时任务 (7 处)<br>  - client.js:194 → 定时任务 (30 处)<br>  - docs/WEB-AI-ANONYMOUS-VALIDATION-2026-10-29.md:34 → 临时文件操作 (2 处)<br>  - docs/MODULAR-REFACTOR-AND-OFFICE-UPGRADE-2026-10-28.md:140 → 临时文件操作 (1 处)<br>  - docs/WEB-AI-LOGIN-PERSISTENCE-2026-10-29.md:38 → 临时文件操作 (2 处)<br>  ... 共 59 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - client.js:271 → 云存储上传 (56 处)<br>  - docs/WEB-AI-ATTACHMENTS-2026-10-29.md:29 → 云存储上传 (1 处)<br>  - src/shared/web-ai-observation.ts:132 → 云存储上传 (9 处)<br>  - src/shared/web-ai-upload.ts:5 → 云存储上传 (20 处)<br>  - src/shared/web-ai-adapters.ts:3 → 云存储上传 (15 处)<br>  ... 共 13 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 5. repo: 1 deps + 4 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 36874, 注释行: 1466 (4.0%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 4 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - host-integration/harness-0.2.1-rc.3-persistence.patch:207 → 硬编码敏感信息 (1 处)<br>  - tests/web-ai-session.mjs:25 → 硬编码敏感信息 (1 处)<br>  - tests/knowledge-retrieval.mjs:51 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - docs/REASONING-HISTORY-RECOVERY-2026-10-28.md:17 → 读取 git 历史 (1 处)<br>  - docs/MODULE-BOUNDARIES-AND-SESSION-ARCHIVE-2026-10-28.md:37 → 读取 git 历史 (1 处)<br>  - docs/MESSAGE-ROUTING-RULES-2026-10-29.md:45 → 读取 git 历史 (1 处)<br>  - docs/AI-NEWS-DISCOVERY-2026-10-28.md:13 → 读取 git 历史 (1 处)<br>  - docs/TASK-MESSAGE-TIME-2026-10-29.md:15 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (51 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (6 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - docs/LONG-RUN-AND-RESPONSIVE-2026-10-28.md:24 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - index.js:2025 → 修改系统目录 (3 处)<br>  - host-integration/prepare-local-app.mjs:11 → 修改系统目录 (6 处)<br>  - src/host/web-ai/chrome.ts:19 → 修改系统目录 (3 处)<br>  - src/host/integrations/github.ts:30 → 修改系统目录 (1 处)<br>  - src/host/integrations/yunzhijia.ts:118 → 修改系统目录 (1 处)<br>  ... 共 7 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: 隔离 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (1 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 45 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-dev-workbench |
| 校验 URL | https://github.com/LongerWu2026/dsh-dev-workbench |
| 必查项通过率 | 15/33 (45%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-30 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
