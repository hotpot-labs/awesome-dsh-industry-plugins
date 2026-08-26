# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/muyuanjin/dsh-ptc-plus
- **校验时间**: 2026-08-26 01:28:46
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 16 | 11 | 6 |
| 🟡 推荐 | 14 | 7 | 7 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2016-11-28 (3557 天前); 公开仓库数: 32; 粉丝数: 1 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1264; 包名: dsh-ptc-plus; 描述: A session-bound agent-native REPL for DeepSeek Harness PTC mode. — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (3): v0.2.3, v0.2.2, v0.2.1; package.json version: 0.2.3; GitHub Releases (2): v0.2.3, v0.2.2 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/dsh-settings: next; @deepseek-ai/dsh-skill-filesystem: next; @deepseek-ai/dsh-tool-cordis: next; @deepseek-ai/dsh-tools: next; engines: {"node": "^22.19.0 \|\| >=24.0.0"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "external": ["react"], "in; Cordis/DSH 依赖: @deepseek-ai/dsh-settings, @deepseek-ai/dsh-skill-filesystem, @deepseek-ai/dsh-tool-cordis, @deepseek-ai/dsh-tools; Cordis 配置文件: cordis.patch.yml<br>  - CONTEXT.md:50 → Monkey patch / prototype pollution<br>  - internal/value-wire.js:35 → Monkey patch / prototype pollution<br>  - internal/tool-call-canonicalizer.js:31 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 261 处, 函数: 3323 个, 比例: 7.9% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: index.js; 发现清理逻辑: internal/worker-client.js; 发现清理逻辑: internal/direct-surface-owner.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - internal/worker-client.js:101 → 读取环境变量配置 (2 处)<br>  - test/ab-headless-trajectories.test.js:175 → 读取环境变量配置 (2 处)<br>  - test/worker-client.test.js:47 → 读取环境变量配置 (8 处)<br>  - test/plugin-durability-recovery.test.js:146 → 读取环境变量配置 (11 处)<br>  - test/cell-analysis.test.js:144 → 读取环境变量配置 (1 处)<br>  ... 共 12 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - docs/adr/0006-rewrite-module-syntax-with-an-ast.md:9 → 深层目录穿越 (3 处)<br>  - docs/adr/0007-separate-worker-transport-from-session-semantics.md:9 → 深层目录穿越 (6 处)<br>  - docs/adr/0015-preserve-source-positions-through-rewrites.md:9 → 深层目录穿越 (2 处) — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - test/plugin-repl-language-modules.test.js:470 → 进程执行 (1 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - test/ab-headless-trajectories.test.js:388 → 开启 shell 模式 (注入风险) (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package.json:71 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - package-lock.json:41 → 探测到 HTTP(S) 网络请求 (79 处)<br>  - README.md:20 → 探测到 HTTP(S) 网络请求 (8 处)<br>  - README.zh.md:20 → 探测到 HTTP(S) 网络请求 (8 处)<br>  - internal/module-policy.js:13 → WebSocket 连接 (1 处)<br>涉及的域名: awesome-dsh-plugin.com, example.test, github.com, img.shields.io, paulmillr.com, registry.npmjs.org, registry.npmmirror.com, www.npmjs.com<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - AGENTS.md:27 → 敏感凭证读取 (3 处)<br>  - docs/evaluation.md:49 → API Key / Token 读取 (6 处)<br>  - docs/evaluation.md:44 → 敏感凭证读取 (4 处)<br>  - docs/adr/0022-stage-npm-releases-with-oidc.md:5 → 敏感凭证读取 (7 处)<br>  - test/headless-host.test.js:29 → API Key / Token 读取 (6 处)<br>  ... 共 16 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - scripts/expensive-headless-acceptance.mjs:474 → 写入配置文件 (5 处)<br>  - scripts/ab-headless-trajectories.mjs:675 → 写入配置文件 (2 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - test/plugin-durability-recovery.test.js:530 → 字符混淆 (1 处) |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - internal/kernel-worker.js:253 → eval() 任意代码执行 (1 处)<br>  - test/plugin-repl-language.test.js:894 → eval() 任意代码执行 (1 处)<br>  - test/tool-call-canonicalizer.test.js:235 → new Function() 任意代码执行 (2 处)<br>  - test/cell-rewriter.test.js:405 → eval() 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 11 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - internal/session-cell-executor.js:325 → 定时任务 (2 处)<br>  - test/headless-host.test.js:135 → 定时任务 (1 处)<br>  - test/headless-host.test.js:137 → 临时文件操作 (1 处)<br>  - test/plugin-durability-recovery-boundaries.test.js:194 → 定时任务 (1 处)<br>  - test/session-runtime-faults.test.js:79 → 定时任务 (1 处)<br>  ... 共 17 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ✅ 通过 | 未检测到文件窃取/静默上传模式 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 11. repo: 5 deps + 6 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 30578, 注释行: 212 (0.7%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 51 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - test/headless-host.test.js:67 → 硬编码敏感信息 (1 处)<br>  - scripts/expensive-headless-acceptance.mjs:502 → 明文写入敏感信息 (2 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - AGENTS.md:50 → 读取 git 历史 (1 处)<br>  - .github/workflows/release.yml:111 → 读取 git 历史 (1 处)<br>  - docs/publishing.md:44 → 读取 git 历史 (1 处)<br>  - test/plugin-repl-language.test.js:737 → 读取文档/压缩文件 (2 处)<br>  - test/plugin-repl-language-modules.test.js:332 → 读取文档/压缩文件 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (7 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (2 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - test/cell-rewriter.test.js:211 → 修改系统目录 (1 处) |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: sandbox |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (7 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 30 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG, 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 1, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-ptc-plus |
| 校验 URL | https://github.com/muyuanjin/dsh-ptc-plus |
| 必查项通过率 | 16/33 (48%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-26 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
