# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/GuoMonth/dsh-erp
- **校验时间**: 2026-11-04 05:25:49
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 20 | 9 | 4 |
| 🟡 推荐 | 14 | 7 | 7 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2017-07-22 (3391 天前); 公开仓库数: 61; 粉丝数: 5 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 2256; 包名: @guosheng_047/dsh-erp; 描述: ERP 助手 (Adapt ERP): a DeepSeek Harness desktop workspace that learns your ERP si — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (12): v0.1.5, v0.1.3, v0.1.2, v0.1.1, v0.1.0-alpha.8; package.json version: 0.1.5; GitHub Releases (5): v0.1.5, v0.1.3, v0.1.2, v0.1.1, v0.1.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/dsh-browser-use: 0.2.1-rc.5; @deepseek-ai/dsh-experimental-browser-use-playwright-mcp: 0.2.1-rc.5; @deepseek-ai/cordis: 4.0.5; @deepseek-ai/dsh-llm: 0.2.1-rc.5; @deepseek-ai/dsh-tools: 0.2.1-rc.5 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ✅ 通过 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web"}}; Cordis/DSH 依赖: @deepseek-ai/dsh-browser-use, @deepseek-ai/dsh-experimental-browser-use-playwright-mcp, @deepseek-ai/cordis, @deepseek-ai/dsh-llm, @deepseek-ai/dsh-tools; Cordis 配置文件: cordis.patch.yml |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 155 处, 函数: 1010 个, 比例: 15.3% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: src/index.ts; 发现清理逻辑: src/worker-client.ts; 发现清理逻辑: src/product/channel.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .gitignore:5 → 读取环境变量配置 (3 处)<br>  - docs/system-configuration.en.md:45 → 读取浏览器 Cookie/本地存储 (1 处)<br>  - src/worker.ts:11 → 读取环境变量配置 (6 处)<br>  - src/index.ts:200 → 读取浏览器 Cookie/本地存储 (4 处)<br>  - src/worker-client.ts:59 → 读取环境变量配置 (2 处)<br>  ... 共 18 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - docs/adr/0001-local-first-ai-erp.md:3 → 深层目录穿越 (1 处)<br>  - docs/adr/0004-bookmark-workspace-share-pack.md:62 → 深层目录穿越 (1 处)<br>  - src/knowledge/pack.ts:17 → 深层目录穿越 (1 处)<br>  - src/storage/paths.ts:8 → 读取用户主目录 (3 处)<br>  - tests/fixtures/scm-alpha5/trace.mjs:2 → 深层目录穿越 (1 处)<br>  ... 共 7 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - src/storage/database.ts:89 → 命令字符串拼接变量 (注入风险) (1 处)<br>  - src/storage/database.ts:89 → exec 命令拼接 (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package-lock.json:56 → 探测到 HTTP(S) 网络请求 (910 处)<br>  - package-lock.json:97 → WebSocket 连接 (4 处)<br>  - package-lock.json:97 → 浏览器网络 API (4 处)<br>  - package.json:10 → 探测到 HTTP(S) 网络请求 (4 处)<br>  - README.md:3 → 探测到 HTTP(S) 网络请求 (2 处)<br>涉及的域名: 127.0.0.1, EXAMPLE.test, a.example, b.example, c.example, cdn.example, d.example, docs.npmjs.com, down.example, erp.example (+27 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - package-lock.json:1323 → API Key / Token 读取 (6 处)<br>  - package-lock.json:94 → 敏感凭证读取 (68 处)<br>  - CHANGELOG.md:17 → 敏感凭证读取 (3 处)<br>  - README.md:7 → 敏感凭证读取 (6 处)<br>  - NOTICE.md:15 → 敏感凭证读取 (1 处)<br>  ... 共 61 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - scripts/artifact-smoke.mjs:56 → 写入配置文件 (1 处)<br>  - tests/native.test.mjs:51 → 写入配置文件 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - tests/client-bundle.test.mjs:13 → node:vm 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 19 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - src/worker.ts:19 → 进程控制 (4 处)<br>  - src/worker-client.ts:76 → 定时任务 (4 处)<br>  - src/client/open.ts:31 → 定时任务 (1 处)<br>  - src/storage/client.ts:40 → 定时任务 (1 处)<br>  - src/browser/resources.ts:32 → 定时任务 (2 处)<br>  ... 共 25 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - package-lock.json:86 → 云服务 SDK (可能用于隐蔽上传) (99 处)<br>  - package-lock.json:1044 → 云存储上传 (6 处)<br>  - README.md:114 → 云存储上传 (1 处)<br>  - docs/native-and-sharing.en.md:22 → 云存储上传 (1 处)<br>  - src/knowledge/tools.ts:34 → 云存储上传 (2 处)<br>  ... 共 7 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 19. repo: 3 deps + 16 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 8844, 注释行: 137 (1.5%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - src/client/index.tsx:53 → 硬编码敏感信息 (2 处)<br>  - tests/storage.test.mjs:178 → 硬编码敏感信息 (1 处)<br>  - tests/native.test.mjs:51 → 明文写入敏感信息 (1 处)<br>  - tests/sites.test.mjs:56 → 硬编码敏感信息 (1 处)<br>  - tests/scm-learning.test.mjs:35 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (5 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (2 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ✅ 通过 | 未检测到系统配置修改/开机自启逻辑 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (1 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 51 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 1, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-erp |
| 校验 URL | https://github.com/GuoMonth/dsh-erp |
| 必查项通过率 | 20/33 (61%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-11-04 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
