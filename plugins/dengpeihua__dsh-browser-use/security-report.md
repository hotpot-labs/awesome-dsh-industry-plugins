# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/dengpeihua/dsh-browser-use
- **校验时间**: 2026-09-18 03:59:41
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 16 | 10 | 7 |
| 🟡 推荐 | 14 | 5 | 9 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2022-03-23 (1639 天前); 公开仓库数: 3; 粉丝数: 5 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 3484; 包名: dsh-browser-plugin; 描述: Native DeepSeek Harness browser-agent plugin with Session-isolated Chromium, CDP — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - output/evals/webvoyager-109-20260916-concurrency1/Allrecipes--1/session.json:1048 → 盗版/侵权 (5 处)<br>  - output/evals/webvoyager-109-20260916-concurrency1/Allrecipes--35/session.json:1050 → 盗版/侵权 (5 处)<br>  - output/evals/webvoyager-109-20260916-concurrency1/Allrecipes--35/trace.ndjson:26 → 盗版/侵权 (6 处)<br>  - output/evals/webvoyager-109-20260916-concurrency1/Allrecipes--7/session.json:1046 → 盗版/侵权 (5 处)<br>  - output/evals/webvoyager-109-20260916-concurrency1/Amazon--24/session.json:1444 → 盗版/侵权 (5 处)<br>  ... 共 67 处 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ⚠️  需人工复核 | 无 git tag; package.json version: 0.1.0; 有版本号但无 git tag / release |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: >=4.0.1 <5; @deepseek-ai/dsh-agent: 0.1.2-alpha.2; @deepseek-ai/dsh-attachment: 0.1.2-alpha.2; @deepseek-ai/dsh-compaction: 0.1.2-alpha.2; @deepseek-ai/dsh-llm: 0.1.2-alpha.2 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "marketplace": {"profiles": ["web"], "requiresBuildAppro; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-agent, @deepseek-ai/dsh-attachment, @deepseek-ai/dsh-compaction, @deepseek-ai/dsh-llm; Cordis 配置文件: cordis.patch.yml<br>  - test/browser-evidence.test.mjs:60 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 187 处, 函数: 1539 个, 比例: 12.2% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: scripts/smoke-command-errors.mjs; 发现清理逻辑: scripts/smoke-reliability.mjs; 发现清理逻辑: scripts/dom-regression.mjs |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .gitignore:8 → 读取环境变量配置 (3 处)<br>  - scripts/verify-installed-package.mjs:10 → 读取环境变量配置 (1 处)<br>  - scripts/eval/run.mjs:70 → 读取环境变量配置 (2 处)<br>  - scripts/eval/config.mjs:32 → 读取环境变量配置 (1 处)<br>  - output/evals/webvoyager-109-20260916-concurrency1/Allrecipes--39/final.png:141 → 读取环境变量配置 (1 处)<br>  ... 共 13 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - scripts/eval/prepare.mjs:6 → 深层目录穿越 (1 处)<br>  - scripts/eval/host.mjs:14 → 深层目录穿越 (1 处)<br>  - scripts/eval/run.mjs:15 → 深层目录穿越 (1 处)<br>  - scripts/eval/config.mjs:33 → 读取用户主目录 (1 处)<br>  - src/browser/dom/utils/index.ts:20 → 读取用户主目录 (1 处)<br>  ... 共 8 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - SECURITY.md:24 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - package.json:67 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - package-lock.json:74 → 探测到 HTTP(S) 网络请求 (152 处)<br>  - README.md:12 → 探测到 HTTP(S) 网络请求 (6 处)<br>  - scripts/smoke-command-errors.mjs:34 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: 127.0.0.1, a.test, another-shop.test, api.minimax.io, api.minimaxi.com, b.test, duckduckgo.com, example.com, example.test, fixture.test (+21 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - output/evals/webvoyager-109-20260916-concurrency1/Allrecipes--1/session.json:8349 → 挖矿相关 (5 处)<br>  - output/evals/webvoyager-109-20260916-concurrency1/Amazon--28/session.json:4501 → 挖矿相关 (7 处)<br>  - output/evals/webvoyager-109-20260916-concurrency1/Apple--22/final.png:229 → DDoS 攻击 (2 处)<br>  - src/browser/dom/tree/pruner.ts:132 → 挖矿相关 (1 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - SECURITY.md:96 → 敏感凭证读取 (2 处)<br>  - README.md:306 → API Key / Token 读取 (1 处)<br>  - README.md:275 → 敏感凭证读取 (3 处)<br>  - AGENTS.md:87 → 敏感凭证读取 (6 处)<br>  - scripts/verify-installed-package.mjs:10 → 读取环境变量 API Key/凭证 (1 处)<br>  ... 共 162 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - test/eval.test.mjs:67 → 写入配置文件 (3 处)<br>  - test/eval-bailian-config.test.mjs:11 → 写入配置文件 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - scripts/smoke-command-errors.mjs:40 → eval() 任意代码执行 (4 处)<br>  - scripts/smoke-reliability.mjs:84 → eval() 任意代码执行 (3 处)<br>  - scripts/smoke-migration.mjs:58 → eval() 任意代码执行 (5 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 26 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - scripts/smoke-command-errors.mjs:15 → 开启监听端口 (1 处)<br>  - scripts/smoke-reliability.mjs:26 → 开启监听端口 (1 处)<br>  - scripts/smoke-reliability.mjs:10 → 定时任务 (1 处)<br>  - scripts/smoke-migration.mjs:24 → 开启监听端口 (1 处)<br>  - scripts/smoke-memory.mjs:27 → 开启监听端口 (1 处)<br>  ... 共 22 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - SECURITY.md:130 → 云存储上传 (1 处)<br>  - output/evals/webvoyager-109-20260916-concurrency1/Allrecipes--38/session.json:4832 → 云存储上传 (22 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 26. repo: 1 deps + 25 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 18635, 注释行: 1886 (10.1%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - scripts/eval/smoke.mjs:16 → 硬编码敏感信息 (1 处)<br>  - scripts/eval/core.mjs:110 → 明文写入敏感信息 (1 处)<br>  - test/eval-reliability.test.mjs:14 → 硬编码敏感信息 (1 处)<br>  - test/eval.test.mjs:68 → 明文写入敏感信息 (1 处)<br>  - test/eval.test.mjs:80 → 硬编码敏感信息 (12 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - AGENTS.md:133 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (24 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (3 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - output/evals/webvoyager-109-20260916-concurrency1/Amazon--31/session.json:5089 → 创建开机自启/系统服务 (3 处)<br>  - output/evals/webvoyager-109-20260916-concurrency1/Apple--35/trace.ndjson:192 → 创建开机自启/系统服务 (7 处)<br>  - output/evals/webvoyager-109-20260916-concurrency1/Amazon--5/trace.ndjson:90 → 创建开机自启/系统服务 (3 处)<br>  - output/evals/webvoyager-109-20260916-concurrency1/Amazon--5/judge-evidence.ndjson:1 → 创建开机自启/系统服务 (1 处)<br>  - output/evals/webvoyager-109-20260916-concurrency1/Apple--19/session.json:8763 → 创建开机自启/系统服务 (9 处)<br>  ... 共 14 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: sandbox, 隔离, isolation |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (82 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 11 |
| 7.2 | 未标记停止维护 | 必查 | ❌ 不通过 | 文档中发现弃用标记: archived |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 2, Forks: 1, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-browser-use |
| 校验 URL | https://github.com/dengpeihua/dsh-browser-use |
| 必查项通过率 | 16/33 (48%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-09-18 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
