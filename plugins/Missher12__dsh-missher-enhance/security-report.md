# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/Missher12/dsh-missher-enhance
- **校验时间**: 2026-09-19 03:46:19
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 20 | 10 | 3 |
| 🟡 推荐 | 14 | 5 | 9 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2019-12-04 (2481 天前); 公开仓库数: 16; 粉丝数: 0 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 503; 包名: dsh-missher-enhance; 描述: Optional enhancement modules for official DeepSeek Harness — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - src/messenger/tools.ts:63 → 绕过权限限制 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (2): v0.1.0-rc.2, v0.1.0-rc.1; package.json version: 0.1.0-rc.2; GitHub Releases (2): v0.1.0-rc.2, v0.1.0-rc.1 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: 4.0.2; @deepseek-ai/dsh-agent: 0.1.5-rc.2; @deepseek-ai/dsh-api-remotes: 0.1.5-rc.2; @deepseek-ai/dsh-api-session-controller: 0.1.5-rc.2; @deepseek-ai/dsh-attachment: 0.1.5-rc.2 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ✅ 通过 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "inject": ["@deepseek-ai/d; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-agent, @deepseek-ai/dsh-api-remotes, @deepseek-ai/dsh-api-session-controller, @deepseek-ai/dsh-attachment; Cordis 配置文件: cordis.patch.yml |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 194 处, 函数: 1643 个, 比例: 11.8% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: tests/sessions-settings-client.test.ts; 发现清理逻辑: tests/documents-client-interaction.test.ts; 发现清理逻辑: tests/persistence.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - tests/messenger-recovery-review.test.ts:46 → 读取环境变量配置 (2 处)<br>  - tests/piano-browser.ts:10 → 读取环境变量配置 (3 处)<br>  - scripts/build.mjs:49 → 读取环境变量配置 (1 处)<br>  - scripts/cli-diagnostic.mjs:5 → 读取环境变量配置 (1 处)<br>  - scripts/verify-maintenance-profile.mjs:56 → 读取环境变量配置 (1 处)<br>  ... 共 10 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - tests/personalization.test.ts:34 → 目录遍历 (5 处)<br>  - src/sessions/host.ts:45 → 读取用户主目录 (1 处)<br>  - src/client/index.tsx:7 → 深层目录穿越 (1 处)<br>  - src/client/reasoning/index.tsx:5 → 深层目录穿越 (1 处)<br>  - src/client/reasoning/preferences.ts:4 → 深层目录穿越 (1 处)<br>  ... 共 17 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package.json:179 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - package-lock.json:89 → 探测到 HTTP(S) 网络请求 (812 处)<br>  - package-lock.json:179 → WebSocket 连接 (4 处)<br>  - package-lock.json:179 → 浏览器网络 API (4 处)<br>  - AGENT_INTEGRATION.md:10 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: 127.0.0.1, alpha.test, api.deepseek.com, api.deepseek.com.evil.test, beta.test, feross.org, github.com, liberapay.com, new.test, opencollective.com (+8 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - package.json:129 → 敏感凭证读取 (1 处)<br>  - package-lock.json:63 → 敏感凭证读取 (60 处)<br>  - tests/maintenance-ipc-consumer.test.ts:80 → 敏感凭证读取 (2 处)<br>  - tests/messenger-transcript.test.ts:93 → 敏感凭证读取 (1 处)<br>  - tests/balance.test.ts:1 → 敏感凭证读取 (29 处)<br>  ... 共 27 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - tests/maintenance-ipc-consumer.test.ts:48 → 修改全局配置 (1 处)<br>  - tests/maintenance.test.ts:31 → 修改全局配置 (5 处)<br>  - scripts/build.mjs:28 → 写入配置文件 (3 处)<br>  - scripts/verify-maintenance-profile.mjs:43 → 修改全局配置 (1 处)<br>  - src/maintenance/index.ts:117 → 修改全局配置 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 64 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - tests/sessions.test.ts:133 → 临时文件操作 (1 处)<br>  - tests/personalization.test.ts:22 → 文件写入 (5 处)<br>  - tests/personalization.test.ts:48 → 文件读取 (12 处)<br>  - tests/documents-workflow.test.ts:135 → 定时任务 (1 处)<br>  - tests/maintenance-ipc-consumer.test.ts:96 → 临时文件操作 (1 处)<br>  ... 共 26 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - package.json:96 → 云存储上传 (2 处)<br>  - package-lock.json:127 → 云服务 SDK (可能用于隐蔽上传) (103 处)<br>  - package-lock.json:46 → 云存储上传 (6 处)<br>  - tests/documents-config.test.ts:6 → 云存储上传 (3 处)<br>  - tests/documents-client-interaction.test.ts:25 → 云存储上传 (1 处)<br>  ... 共 19 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 20. repo: 5 deps + 15 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 13081, 注释行: 1015 (7.8%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 34 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - tests/messenger-transcript.test.ts:93 → 硬编码敏感信息 (1 处)<br>  - tests/models.test.ts:42 → 硬编码敏感信息 (1 处)<br>  - tests/messenger.test.ts:97 → 硬编码敏感信息 (1 处)<br>  - tests/archive-restore-client.test.ts:43 → 硬编码敏感信息 (1 处)<br>  - scripts/lifecycle.mjs:163 → 明文写入敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (7 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ⚠️  需人工复核 | 未发现一键清理功能, 需确认是否有数据清理机制 |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ✅ 通过 | 未检测到系统配置修改/开机自启逻辑 |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (1 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 4 天; 提交总数: 2 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-missher-enhance |
| 校验 URL | https://github.com/Missher12/dsh-missher-enhance |
| 必查项通过率 | 20/33 (61%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-09-19 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
