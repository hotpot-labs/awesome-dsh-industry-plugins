# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/beartackler/dsh-bridge
- **校验时间**: 2026-09-01 04:11:59
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 11 | 14 | 8 |
| 🟡 推荐 | 14 | 6 | 8 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2019-09-06 (2551 天前); 公开仓库数: 16; 粉丝数: 1 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1179; 包名: dsh-bridge; 描述: Familiar-face commands, connectors flow, and the trust layer for DeepSeek Harnes — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - docs/reviews/pm-product-review.md:15 → 盗版/侵权 (1 处)<br>  - docs/trust/provenance-options.md:22 → 破解授权 (6 处)<br>  - docs/specs/commands/connect.md:300 → 盗版/侵权 (1 处)<br>  - docs/design/onboarding-wizard.md:24 → 盗版/侵权 (1 处)<br>  - docs/design/trust-report-card.md:143 → 窃取数据 (1 处)<br>  ... 共 18 处 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ⚠️  需人工复核 | 无 git tag; package.json version: 0.1.0; 有版本号但无 git tag / release |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | engines: {"node": ">=20"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}}; Cordis 配置文件: cordis.patch.yml<br>  - tools/scan/README.md:77 → 直接修改内核源码<br>  - tools/scan/src/rules/dynamic-eval.ts:23 → 直接修改内核源码<br>  - tools/scan/src/rules/credential-access.ts:149 → 直接修改内核源码 — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 156 处, 函数: 2421 个, 比例: 6.4% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ⚠️  需人工复核 | 使用了定时器但未发现清理逻辑, 需人工确认 |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .gitignore:4 → 读取环境变量配置 (3 处)<br>  - site/demo/mock.html:118 → 读取凭证文件 (3 处)<br>  - templates/plugin-starter/.github/workflows/ci.yml:21 → 读取 npm 凭证 (1 处)<br>  - tools/scan/README.md:79 → 读取环境变量配置 (10 处)<br>  - tools/scan/src/self-test.ts:62 → 读取 SSH 私钥目录 (5 处)<br>  ... 共 297 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - tools/scan/README.md:8 → 深层目录穿越 (1 处)<br>  - docs/glossary.md:3 → 深层目录穿越 (1 处)<br>  - docs/growth/tracking.md:46 → 深层目录穿越 (1 处)<br>  - docs/research/portable-features.md:3 → 深层目录穿越 (1 处)<br>  - docs/research/dsh-capability-seams.md:3 → 深层目录穿越 (1 处)<br>  ... 共 37 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - docs/trust/provenance-options.md:352 → 加载 child_process (1 处)<br>  - docs/catalog/cards/distilly.md:34 → Python subprocess (1 处)<br>  - docs/catalog/cards/memsearch.md:38 → os.system 命令执行 (2 处)<br>  - packages/dsh-bridge/data/cards/distilly.md:34 → Python subprocess (1 处)<br>  - packages/dsh-bridge/data/cards/memsearch.md:38 → os.system 命令执行 (2 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - tools/scan/README.md:83 → 开启 shell 模式 (注入风险) (2 处)<br>  - tools/scan/src/self-test.ts:768 → 命令字符串拼接变量 (注入风险) (4 处)<br>  - tools/scan/src/self-test.ts:781 → exec 命令拼接 (1 处)<br>  - tools/scan/src/self-test.ts:88 → 开启 shell 模式 (注入风险) (4 处)<br>  - tools/scan/src/rules/shell-invocation.ts:28 → 开启 shell 模式 (注入风险) (2 处)<br>  ... 共 41 处 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - ROADMAP.md:3 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - package.json:33 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - CONTRIBUTING.md:100 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - README.md:12 → 探测到 HTTP(S) 网络请求 (8 处)<br>  - site/app.js:113 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: ..., ...repository.url, 127.0.0.1, 169.254.169.254, 192.168.3.23, 45.13.x.x, a, a.example, abc123.trycloudflare.com, agent-vision.anionex.me (+113 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - docs/trust/npm-incident-cases.md:44 → 挖矿相关 (4 处)<br>  - docs/catalog/new-since-sweep.json:5755 → 挖矿相关 (13 处)<br>  - docs/catalog/new-since-sweep.json:1179 → 远控/反向 shell (7 处)<br>  - docs/catalog/new-since-sweep.json:29818 → 代理/隧道 (2 处)<br>  - docs/catalog/discovered-plugins.json:10234 → 挖矿相关 (7 处)<br>  ... 共 28 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - ROADMAP.md:19 → 敏感凭证读取 (2 处)<br>  - SECURITY.md:35 → 敏感凭证读取 (7 处)<br>  - CONTRIBUTING.md:61 → 敏感凭证读取 (2 处)<br>  - README.md:16 → 敏感凭证读取 (4 处)<br>  - CHARTER.md:18 → 敏感凭证读取 (3 处)<br>  ... 共 493 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - docs/reviews/eng-quality-review.md:57 → 写入配置文件 (1 处)<br>  - docs/specs/commands/model.md:23 → 修改设置 (2 处)<br>  - packages/dsh-bridge/test/connect-test.ts:172 → 写入配置文件 (2 处)<br>  - packages/dsh-bridge/test/mcp-test.ts:301 → 写入配置文件 (2 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - tools/scan/src/self-test.ts:390 → base64 混淆字符串 (超长) (1 处)<br>  - tools/scan/src/self-test.ts:74 → JS 混淆器变量模式 (2 处)<br>  - docs/reviews/scanner-selfaudit.md:28 → base64 混淆字符串 (超长) (1 处) |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - CHARTER.md:21 → eval() 任意代码执行 (1 处)<br>  - tools/scan/README.md:77 → eval() 任意代码执行 (2 处)<br>  - tools/scan/src/self-test.ts:50 → eval() 任意代码执行 (14 处)<br>  - tools/scan/src/self-test.ts:50 → new Function() 任意代码执行 (2 处)<br>  - tools/scan/src/rules/obfuscation.ts:118 → eval() 任意代码执行 (2 处)<br>  ... 共 164 处 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 0 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - site/build.mjs:122 → 进程控制 (1 处)<br>  - tools/scan/src/self-test.ts:505 → 定时任务 (8 处)<br>  - docs/upstream-reports.md:221 → 临时文件操作 (7 处)<br>  - docs/plugin-author-guide.md:93 → 定时任务 (1 处)<br>  - docs/growth/npm-publish-checklist.md:63 → 临时文件操作 (3 处)<br>  ... 共 247 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - site/data.json:68 → 云存储上传 (1 处)<br>  - tools/scan/README.md:82 → 云存储上传 (2 处)<br>  - tools/scan/src/rules/telemetry-beacons.ts:40 → 云存储上传 (2 处)<br>  - docs/growth/npm-publish-checklist.md:55 → 云存储上传 (1 处)<br>  - docs/trust/npm-incident-cases.md:34 → 云存储上传 (2 处)<br>  ... 共 51 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 无第三方依赖 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 29963, 注释行: 4557 (15.2%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 2 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ✅ 通过 | README 中包含数据上报说明: telemetry |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - docs/reviews/scanner-selfaudit.md:80 → 从环境变量获取敏感信息 (1 处)<br>  - docs/specs/commands/connect.md:333 → 硬编码敏感信息 (1 处)<br>  - docs/specs/commands/mcp.md:211 → 硬编码敏感信息 (1 处)<br>  - packages/dsh-bridge/src/commands/connect.ts:56 → 硬编码敏感信息 (5 处)<br>  - packages/dsh-bridge/test/connect-apply-test.ts:37 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - .github/workflows/ci.yml:48 → 读取 git 历史 (1 处)<br>  - docs/growth/launch-checklist.md:196 → 读取 git 历史 (1 处)<br>  - docs/research/portable-features.md:34 → 读取 git 历史 (1 处)<br>  - docs/research/e2e-verification.md:96 → 读取 git 历史 (3 处)<br>  - docs/reviews/self-security-audit.md:97 → 读取 git 历史 (2 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (62 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (11 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - docs/specs/commands/doctor.md:27 → 要求 root/sudo 权限<br>  - docs/catalog/discovered-plugins.json:16678 → 要求 root/sudo 权限<br>  - docs/catalog/cards/codeg.md:33 → 要求 root/sudo 权限<br>  - packages/dsh-bridge/data/cards/codeg.md:33 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - site/build.mjs:1 → 修改系统目录 (1 处)<br>  - site/data.json:776 → 修改系统目录 (1 处)<br>  - tools/scan/src/index.ts:1 → 修改系统目录 (1 处)<br>  - tools/scan/src/bench.ts:1 → 修改系统目录 (1 处)<br>  - docs/reviews/eng-quality-review.md:182 → 修改系统目录 (2 处)<br>  ... 共 34 处 |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (27 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 1 天; 提交总数: 52 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 1, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-bridge |
| 校验 URL | https://github.com/beartackler/dsh-bridge |
| 必查项通过率 | 11/33 (33%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-09-01 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
