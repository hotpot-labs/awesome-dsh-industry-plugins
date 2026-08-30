# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/stas130286-blip/dsh-brainagent
- **校验时间**: 2026-08-30 04:36:29
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 18 | 11 | 4 |
| 🟡 推荐 | 14 | 5 | 9 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2025-12-13 (259 天前); 公开仓库数: 4; 粉丝数: 0 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ⚠️  需人工复核 | 许可证: SEE LICENSE IN LICENSE — 需确认与 MIT 兼容性 |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1412; 包名: dsh-brainagent; 描述: BrainAgent — brain-inspired plugin for DeepSeek Harness (dsh): a pipeline of heu — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - src/modules/goal-stack.test.ts:236 → 盗版/侵权 (1 处)<br>  - src/modules/v0921-brain-wiring.test.ts:120 → 盗版/侵权 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (20): v0.9.27, v0.9.23, v0.9.22, v0.9.21, v0.9.20; package.json version: 0.9.27; GitHub Releases (5): v0.9.27, v0.9.19, v0.9.14, v0.9.9, v0.9.8 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/dsh-llm: *; @deepseek-ai/cordis: *; @deepseek-ai/dsh-agent: *; @deepseek-ai/dsh-commands: *; @deepseek-ai/dsh-session: * |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ✅ 通过 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}}; Cordis/DSH 依赖: @deepseek-ai/dsh-llm, @deepseek-ai/cordis, @deepseek-ai/dsh-agent, @deepseek-ai/dsh-commands, @deepseek-ai/dsh-session; Cordis 配置文件: cordis.patch.yml |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 178 处, 函数: 3567 个, 比例: 5.0% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: src/index.ts; 发现清理逻辑: src/modules/drives.test.ts; 发现清理逻辑: src/modules/temporal-awareness.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - src/modules/goal-round-pacer.ts:91 → 读取环境变量配置 (3 处)<br>  - src/modules/autonomous-research.ts:190 → 读取环境变量配置 (8 处)<br>  - src/modules/goal-reminder.ts:55 → 读取环境变量配置 (1 处)<br>  - src/modules/goal-round-pacer.test.ts:91 → 读取环境变量配置 (2 处)<br>  - src/modules/v0924-research-injection.test.ts:59 → 读取环境变量配置 (9 处)<br>  ... 共 11 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - src/plugin/config.ts:146 → 读取用户主目录 (1 处)<br>  - scripts/check-encoding.cjs:21 → 目录遍历 (1 处)<br>  - lib/index.js:639 → 读取用户主目录 (1 处) — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package.json:33 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - README.md:5 → 探测到 HTTP(S) 网络请求 (13 处)<br>  - CHANGELOG.md:725 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - src/modules/autonomous-research.ts:378 → 探测到 HTTP(S) 网络请求 (7 处)<br>  - src/modules/autonomous-research.ts:377 → fetch 网络请求 (6 处)<br>涉及的域名: ai.example.com, api.anthropic.com, api.deepseek.com, api.groq.com, api.openai.com, api.perplexity.ai, api.search.brave.com, api.tavily.com, api.x.ai, codeload.github.com (+15 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - CHANGELOG.md:61 → API Key / Token 读取 (1 处)<br>  - CHANGELOG.md:61 → 敏感凭证读取 (3 处)<br>  - src/modules/cerebellum.ts:146 → 敏感凭证读取 (1 处)<br>  - src/modules/goal-stack.test.ts:637 → API Key / Token 读取 (1 处)<br>  - src/modules/autonomous-research.ts:190 → 读取环境变量 API Key/凭证 (8 处)<br>  ... 共 30 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - src/modules/v0923-research-curiosity.test.ts:163 → 写入配置文件 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 17 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - src/index.ts:240 → 定时任务 (3 处)<br>  - src/modules/dream-mode.ts:159 → 定时任务 (2 处)<br>  - src/modules/goal-stack.test.ts:250 → 定时任务 (1 处)<br>  - src/modules/session-bridge.test.ts:139 → 定时任务 (8 处)<br>  - src/modules/goal-round-pacer.ts:115 → 定时任务 (1 处)<br>  ... 共 19 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ✅ 通过 | 未检测到文件窃取/静默上传模式 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 17. repo: 2 deps + 15 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 46082, 注释行: 6184 (13.4%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 60 个, 例如: procedural-dedupe-steps.test.ts |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - src/modules/goal-stack.test.ts:637 → 硬编码敏感信息 (1 处)<br>  - src/modules/v0926-extraction-salvage.test.ts:36 → 硬编码敏感信息 (1 处)<br>  - src/modules/v0924-research-injection.test.ts:173 → 硬编码敏感信息 (1 处)<br>  - src/modules/autonomous-research.test.ts:162 → 硬编码敏感信息 (7 处)<br>  - src/modules/emotional-memory.test.ts:226 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - .github/workflows/ci.yml:31 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (17 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (4 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - host-patches/apply-goal-round-pacing.cjs:1 → 修改系统目录 (1 处) |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ⚠️  需人工复核 | 未发现临时文件清理逻辑, 需确认 |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 86 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 2, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-brainagent |
| 校验 URL | https://github.com/stas130286-blip/dsh-brainagent |
| 必查项通过率 | 18/33 (55%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-30 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
