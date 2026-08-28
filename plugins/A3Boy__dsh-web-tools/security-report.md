# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/A3Boy/dsh-web-tools
- **校验时间**: 2026-08-28 10:13:44
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 18 | 9 | 6 |
| 🟡 推荐 | 14 | 7 | 7 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2023-09-29 (1064 天前); 公开仓库数: 6; 粉丝数: 0 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1871; 包名: dsh-web-tools; 描述: Unified multi-provider web search and fetch for DeepSeek Harness — BYOK, per-pro — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - src/host/providers/firecrawl.ts:84 → 非法爬取 (1 处)<br>  - reports/p5/runs.jsonl:8 → 非法爬取 (75 处)<br>  - reports/p5/runs.jsonl:173 → 窃取数据 (1 处)<br>  - reports/p5/runs.jsonl:2 → 盗版/侵权 (3 处)<br>  - lib/host/providers/firecrawl.d.ts:27 → 非法爬取 (1 处)<br>  ... 共 6 处 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (5): v0.3.0, v0.2.0, p7-browser-bridge-final, backup/native-browser-final, backup/main-before-native-browser-merge; package.json version: 0.3.0; GitHub Releases (2): v0.3.0, v0.2.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.1; @deepseek-ai/dsh-api-remotes: ^0.1.0-rc.6; @deepseek-ai/dsh-client-connection: ^0.1.0-rc.6; @deepseek-ai/dsh-client-locale: ^0.1.0-rc.6; @deepseek-ai/dsh-client-runtime: ^0.1.0-rc.6 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "inject": ["@deepseek-ai/d; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-api-remotes, @deepseek-ai/dsh-client-connection, @deepseek-ai/dsh-client-locale, @deepseek-ai/dsh-client-runtime; Cordis 配置文件: cordis.patch.yml<br>  - lib/client/provider-preference-presets.d.ts:34 → Monkey patch / prototype pollution<br>  - lib/client/provider-preference-presets.js:37 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 408 处, 函数: 2999 个, 比例: 13.6% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: src/host/index.ts; 发现清理逻辑: src/host/routes.ts; 发现清理逻辑: src/host/providers/brave.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - take-screenshots.mjs:17 → 读取环境变量配置 (1 处)<br>  - shot-interactive.mjs:12 → 读取环境变量配置 (1 处)<br>  - .gitignore:20 → 读取环境变量配置 (3 处)<br>  - debug-page.mjs:8 → 读取环境变量配置 (1 处)<br>  - tsdown.config.ts:94 → 读取环境变量配置 (6 处)<br>  ... 共 21 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - src/host/providers/you.ts:4 → 深层目录穿越 (1 处)<br>  - src/host/providers/parallel.ts:29 → 深层目录穿越 (1 处)<br>  - src/host/providers/firecrawl.ts:14 → 深层目录穿越 (1 处)<br>  - src/host/providers/jina.ts:18 → 深层目录穿越 (1 处)<br>  - src/host/providers/exa.ts:14 → 深层目录穿越 (1 处)<br>  ... 共 23 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - take-screenshots.mjs:112 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - take-screenshots.mjs:29 → WebSocket 连接 (2 处)<br>  - take-screenshots.mjs:112 → fetch 网络请求 (2 处)<br>  - take-screenshots.mjs:29 → 浏览器网络 API (2 处)<br>  - README.zh-CN.md:4 → 探测到 HTTP(S) 网络请求 (17 处)<br>涉及的域名: 127.0.0.1, 192.168.1.10, a.example, anything.corp.example, api-dashboard.search.brave.com, api.exa.ai, api.firecrawl.dev, api.github.com, api.parallel.ai, api.search.brave.com (+61 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - reports/p5/runs.jsonl:22 → 挖矿相关 (3 处)<br>  - reports/p5/runs.jsonl:205 → DDoS 攻击 (1 处)<br>  - test/fetch-proxy.test.mjs:25 → 代理/隧道 (1 处)<br>  - lib/host/index.js:11 → 代理/隧道 (1 处)<br>  - lib/host/providers/you.js:2 → 代理/隧道 (1 处)<br>  ... 共 14 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - take-screenshots.mjs:17 → 读取环境变量 API Key/凭证 (1 处)<br>  - shot-interactive.mjs:12 → 读取环境变量 API Key/凭证 (1 处)<br>  - .gitignore:19 → 敏感凭证读取 (1 处)<br>  - package.json:4 → 敏感凭证读取 (2 处)<br>  - CONTRIBUTING.md:48 → 敏感凭证读取 (2 处)<br>  ... 共 123 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - take-screenshots.mjs:63 → eval() 任意代码执行 (10 处)<br>  - shot-interactive.mjs:39 → eval() 任意代码执行 (11 处)<br>  - debug-page.mjs:35 → eval() 任意代码执行 (3 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 21 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - take-screenshots.mjs:19 → 定时任务 (3 处)<br>  - shot-interactive.mjs:13 → 定时任务 (2 处)<br>  - debug-page.mjs:9 → 定时任务 (2 处)<br>  - src/client/SearchModeButton.tsx:97 → 定时任务 (1 处)<br>  - src/client/WebToolsSection.tsx:476 → 定时任务 (1 处)<br>  ... 共 85 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - reports/p5/runs.jsonl:69 → 云存储上传 (13 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 7. repo: 2 deps + 5 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 42751, 注释行: 5262 (12.3%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 30 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - reports/p5/runs.jsonl:62 → 硬编码敏感信息 (3 处)<br>  - test/xhs-structured-state.test.ts:64 → 硬编码敏感信息 (3 处)<br>  - scripts/e2e-xhs-search.mjs:45 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (28 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (11 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - src/host/browser/locator.ts:26 → 修改系统目录 (3 处)<br>  - reports/p5/runs.jsonl:65 → 修改系统目录 (4 处)<br>  - reports/p5/runs.jsonl:18 → 创建开机自启/系统服务 (4 处)<br>  - reports/p5/runs.jsonl:9 → Windows 系统配置修改 (1 处)<br>  - scripts/live-xhs-test.mjs:1 → 修改系统目录 (1 处)<br>  ... 共 19 处 |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (6 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 126 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 21, Forks: 4, Watchers: 0 — 有一定社区基础 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-web-tools |
| 校验 URL | https://github.com/A3Boy/dsh-web-tools |
| 必查项通过率 | 18/33 (55%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-28 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
