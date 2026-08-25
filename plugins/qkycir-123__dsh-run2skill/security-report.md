# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/qkycir-123/dsh-run2skill
- **校验时间**: 2026-08-25 01:27:30
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 18 | 12 | 3 |
| 🟡 推荐 | 14 | 6 | 8 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ⚠️  需人工复核 | 账号注册: 2026-08-18 (6 天前); 公开仓库数: 3; 粉丝数: 0; ⚠️ 账号注册不足 30 天 (6 天) |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 301; 包名: dsh-run2skill; 描述: Turn explicit DSH session experience into reviewable native Skills — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (4): v0.3.0, v0.2.0, v0.1.1-alpha, v0.1.0-alpha; package.json version: 0.3.0; GitHub Releases (4): v0.3.0, v0.2.0, v0.1.1-alpha, v0.1.0-alpha |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/dsh-agent-presets: 0.1.1-rc.2; @deepseek-ai/dsh-client-ui-primitives: 0.1.1-rc.2; engines: {"node": "^22.19.0 \|\| >=24.0.0"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ✅ 通过 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "inject": ["@deepseek-ai/d; Cordis/DSH 依赖: @deepseek-ai/dsh-agent-presets, @deepseek-ai/dsh-client-ui-primitives; Cordis 配置文件: cordis.patch.yml |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 430 处, 函数: 5920 个, 比例: 7.3% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: src/application/publication/publication-scheduler.ts; 发现清理逻辑: src/application/capture/recovery-lifecycle.ts; 发现清理逻辑: src/application/capture/bounded-signal-retry.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .gitignore:1 → 读取环境变量配置 (3 处)<br>  - src/application/learn/learning-worker.ts:262 → 读取环境变量配置 (1 处)<br>  - src/client/purge-settings.ts:219 → 读取环境变量配置 (8 处)<br>  - src/client/proposal-inbox.ts:314 → 读取环境变量配置 (11 处)<br>  - src/client/observe-summary-poller.ts:81 → 读取环境变量配置 (8 处)<br>  ... 共 18 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - src/application/detection/batch-detector-worker.ts:2 → 深层目录穿越 (5 处)<br>  - src/application/generation/generation-worker.ts:2 → 深层目录穿越 (6 处)<br>  - src/application/recall/complete-catalog-recall.ts:2 → 深层目录穿越 (5 处)<br>  - src/application/publication/publication-scheduler.ts:1 → 深层目录穿越 (2 处)<br>  - src/application/publication/approved-proposal-revalidator.ts:1 → 深层目录穿越 (1 处)<br>  ... 共 92 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - README.en.md:124 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - package.json:16 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - CONTRIBUTING.md:3 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - README.md:128 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - tests/v2-dsh-turn-observation.spec.ts:192 → 探测到 HTTP(S) 网络请求 (2 处)<br>涉及的域名: 127.0.0.1, evil.example, example.invalid, github.com, harness.example, user<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - src/domain/observe/redaction.ts:63 → API Key / Token 读取 (2 处)<br>  - src/domain/observe/redaction.ts:59 → 敏感凭证读取 (6 处)<br>  - src/domain/observe/constants.ts:14 → API Key / Token 读取 (1 处)<br>  - src/domain/observe/constants.ts:15 → 敏感凭证读取 (2 处)<br>  - src/adapters/dsh-llm/v2-stage-client.ts:41 → 敏感凭证读取 (1 处)<br>  ... 共 42 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - src/application/purge/purge-service.ts:513 → 修改全局配置 (3 处)<br>  - src/application/capture/write-behind-checkpoint.ts:260 → 修改全局配置 (1 处)<br>  - src/application/migration/v1-to-v2.ts:158 → 修改全局配置 (1 处)<br>  - src/adapters/dsh-session/v2-gap-scanner.ts:239 → 修改全局配置 (1 处)<br>  - src/adapters/dsh-storage/recent-skill-activity-store.ts:141 → 修改全局配置 (2 处)<br>  ... 共 33 处 — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 30 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - src/application/capture/recovery-lifecycle.ts:46 → 定时任务 (3 处)<br>  - src/application/capture/bounded-gap-scanner.ts:121 → 定时任务 (1 处)<br>  - src/application/capture/bounded-signal-retry.ts:13 → 定时任务 (1 处)<br>  - src/application/learn/learning-scheduler.ts:47 → 定时任务 (2 处)<br>  - src/application/learn/learning-worker.ts:143 → 定时任务 (2 处)<br>  ... 共 36 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - docs/product/prd.md:598 → 云存储上传 (1 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 30. repo: 3 deps + 27 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 75243, 注释行: 413 (0.5%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 121 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - tests/observe-summary-rpc.spec.ts:60 → 硬编码敏感信息 (1 处)<br>  - tests/trigger.spec.ts:77 → 硬编码敏感信息 (5 处)<br>  - tests/turn-capture-processor.spec.ts:81 → 硬编码敏感信息 (1 处)<br>  - tests/frozen-evaluation.spec.ts:71 → 硬编码敏感信息 (1 处)<br>  - tests/redaction.spec.ts:53 → 硬编码敏感信息 (3 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (8 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (10 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - probes/candidate/verify.mjs:323 → 修改系统目录 (2 处) |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ⚠️  需人工复核 | 未发现临时文件清理逻辑, 需确认 |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 83 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 10, Forks: 2, Watchers: 1 — 有一定社区基础 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-run2skill |
| 校验 URL | https://github.com/qkycir-123/dsh-run2skill |
| 必查项通过率 | 18/33 (55%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-25 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
