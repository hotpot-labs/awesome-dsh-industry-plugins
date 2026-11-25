# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/EndWithHyphen/dsh-learning-quirky-stuff
- **校验时间**: 2026-11-25 07:36:32
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 20 | 8 | 5 |
| 🟡 推荐 | 14 | 5 | 9 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2015-08-02 (4132 天前); 公开仓库数: 13; 粉丝数: 4 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 456; 包名: dsh-learning-quirky-stuff; 描述: 学习画板：手写与截图笔记、AI 图文总结、系统学习、知识图谱、间隔复习和周报 — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (5): v4.6.0, v4.4.2, v4.4.1, v4.4.0, v4.3.1; package.json version: 4.6.0; GitHub Releases (5): v4.6.0, v4.4.2, v4.4.1, v4.4.0, v4.3.1 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: 4.1.0; @deepseek-ai/dsh: >=0.2.2-rc.1 <0.3.0; @deepseek-ai/dsh-attachment: 0.2.2-rc.1; @deepseek-ai/dsh-home-paths: 0.2.2-rc.1; @deepseek-ai/dsh-llm: 0.2.2-rc.1 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "immediately": true, "inje; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh, @deepseek-ai/dsh-attachment, @deepseek-ai/dsh-home-paths, @deepseek-ai/dsh-llm; Cordis 配置文件: cordis.patch.yml<br>  - core.js:316 → Monkey patch / prototype pollution<br>  - capture-server.js:304 → Monkey patch / prototype pollution<br>  - learning.js:495 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 341 处, 函数: 3085 个, 比例: 11.1% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: model.js; 发现清理逻辑: index.js; 发现清理逻辑: graph-ai.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .gitignore:24 → 读取环境变量配置 (2 处)<br>  - codex-provider.js:10 → 读取环境变量配置 (3 处)<br>  - .npmignore:3 → 读取环境变量配置 (1 处)<br>  - scripts/build.mjs:40 → 读取环境变量配置 (2 处)<br>  - scripts/render-summary-evaluation.mjs:38 → 读取环境变量配置 (1 处)<br>  ... 共 21 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - codex-provider.js:11 → 读取用户主目录 (1 处)<br>  - src/pdf/engine.js:2 → 深层目录穿越 (1 处)<br>  - src/pdf/workspace.jsx:3 → 深层目录穿越 (1 处)<br>  - src/pdf/reader.jsx:4 → 深层目录穿越 (2 处)<br>  - src/pdf/clip.jsx:4 → 深层目录穿越 (1 处)<br>  ... 共 26 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package.json:150 → 探测到 HTTP(S) 网络请求 (4 处)<br>  - .npmrc:1 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - package-lock.json:68 → 探测到 HTTP(S) 网络请求 (446 处)<br>  - icon.svg:1 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - SECURITY.md:5 → 探测到 HTTP(S) 网络请求 (2 处)<br>涉及的域名: 127.0.0.1, evil.example, example.com, example.org, example.test, extension.test, github.com, invalid, localhost, opencollective.com (+11 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - docs/images/chrome-sidepanel.png:868 → DDoS 攻击 (1 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - core.js:182 → 敏感凭证读取 (1 处)<br>  - codex-provider.js:10 → 读取环境变量 API Key/凭证 (2 处)<br>  - capture-server.js:125 → 敏感凭证读取 (1 处)<br>  - scripts/build.mjs:40 → 读取环境变量 API Key/凭证 (2 处)<br>  - scripts/market-index.mjs:13 → 敏感凭证读取 (1 处)<br>  ... 共 30 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - scripts/test-install.mjs:13 → 写入配置文件 (2 处)<br>  - tests/task-manager.test.mjs:90 → 修改全局配置 (1 处)<br>  - tests/task-manager.test.mjs:90 → 修改配置 (1 处)<br>  - tests/model.test.mjs:90 → 修改全局配置 (5 处)<br>  - tests/modules.test.mjs:216 → 修改全局配置 (1 处)<br>  ... 共 10 处 — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - tests/file-cancellation.test.mjs:23 → node:vm 任意代码执行 (2 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 32 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - model.js:21 → 定时任务 (2 处)<br>  - codex-provider.js:141 → 定时任务 (1 处)<br>  - capture-server.js:50 → 开启监听端口 (1 处)<br>  - graph-ai.js:288 → 定时任务 (1 处)<br>  - codex-models.js:24 → 定时任务 (1 处)<br>  ... 共 57 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - .github/workflows/ci.yml:33 → 云存储上传 (2 处)<br>  - src/pdf/workspace.jsx:39 → 云存储上传 (15 处)<br>  - tests/pdf.test.mjs:35 → 云存储上传 (18 处)<br>  - server/modules/pdf.js:26 → 云存储上传 (65 处)<br>  - chrome-extension/sidepanel.js:692 → 云存储上传 (5 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 31. repo: 5 deps + 26 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 28943, 注释行: 87 (0.3%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - src/features/shared.jsx:27 → 明文写入敏感信息 (1 处)<br>  - tests/chrome-page-study.test.mjs:23 → 硬编码敏感信息 (1 处)<br>  - tests/browser-connections.test.mjs:10 → 硬编码敏感信息 (3 处)<br>  - tests/chrome-background.test.mjs:11 → 硬编码敏感信息 (1 处)<br>  - tests/capture.test.mjs:23 → 硬编码敏感信息 (2 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (22 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (3 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - codex-provider.js:13 → 修改系统目录 (1 处)<br>  - scripts/build-native.mjs:20 → 修改系统目录 (2 处)<br>  - scripts/release-files.mjs:25 → 修改系统目录 (1 处)<br>  - src/summary-canvas.js:44 → Windows 系统配置修改 (6 处)<br>  - src/graph-layout.js:45 → Windows 系统配置修改 (2 处)<br>  ... 共 9 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ⚠️  需人工复核 | 未发现临时文件清理逻辑, 需确认 |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 22 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 1, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-learning-quirky-stuff |
| 校验 URL | https://github.com/EndWithHyphen/dsh-learning-quirky-stuff |
| 必查项通过率 | 20/33 (61%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-11-25 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
