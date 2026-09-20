# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/Cloudto1/dsh-approval-chime
- **校验时间**: 2026-09-20 04:00:25
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 15 | 11 | 7 |
| 🟡 推荐 | 14 | 4 | 10 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ⚠️  需人工复核 | 账号注册: 2026-09-12 (7 天前); 公开仓库数: 2; 粉丝数: 0; ⚠️ 账号注册不足 30 天 (7 天) |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 369; 包名: dsh-approval-chime; 描述: DSH 审批提示音插件：申请权限时响一声，音色、音量、开关在「设置 → 通知提醒」里调。 — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ⚠️  需人工复核 | 无 git tag; package.json version: 0.2.0; 有版本号但无 git tag / release |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ❌ 不通过 | 未在 package.json 中发现 DSH/Cordis 依赖或 engines 字段 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web"}}; Cordis 配置文件: cordis.patch.yml<br>  - lib/index.js:806 → Monkey patch / prototype pollution<br>  - lib/client.js:545 → Monkey patch / prototype pollution<br>  - docs/契约调研.md:84 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 411 处, 函数: 3366 个, 比例: 12.2% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: verify/_harness.mjs; 发现清理逻辑: verify/custom-audio.test.mjs; 发现清理逻辑: verify/host-half.test.mjs |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - verify/_harness.mjs:32 → 读取环境变量配置 (2 处)<br>  - verify/host-half.test.mjs:328 → 读取环境变量配置 (9 处)<br>  - lib/index.js:165 → 读取环境变量配置 (1 处)<br>  - verify-independent/r13v-adv-probe-18-deadanchor.mjs:1020 → 读取环境变量配置 (9 处)<br>  - verify-independent/probe-13-r4-browser.mjs:155 → 读取环境变量配置 (1 处)<br>  ... 共 10 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - CHANGELOG.md:630 → 读取用户主目录 (1 处)<br>  - verify/_harness.mjs:33 → 读取用户主目录 (2 处)<br>  - verify/host-half.test.mjs:91 → 读取用户主目录 (2 处)<br>  - lib/index.js:170 → 读取用户主目录 (1 处)<br>  - docs/契约调研.md:1266 → 读取用户主目录 (3 处)<br>  ... 共 20 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - verify-independent/r13v-adv-probe-18-deadanchor.mjs:1629 → exec 命令拼接 (1 处)<br>  - verify-independent/r13v-adv-probe-18-drift.mjs:1629 → exec 命令拼接 (1 处)<br>  - verify-independent/r13v-adv-probe-18.mjs:1664 → exec 命令拼接 (1 处)<br>  - verify-independent/probe-18-r10-sessions.mjs:1629 → exec 命令拼接 (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - README.md:15 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - verify/client-half.test.mjs:120 → fetch 网络请求 (6 处)<br>  - lib/index.js:653 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - lib/client.js:748 → fetch 网络请求 (5 处)<br>  - docs/契约调研.md:1069 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: 127.0.0.1, codeload.github.com, localhost, x<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - verify/_harness.mjs:32 → 读取环境变量 API Key/凭证 (1 处)<br>  - verify/custom-audio.test.mjs:339 → 敏感凭证读取 (2 处)<br>  - verify/host-half.test.mjs:328 → 读取环境变量 API Key/凭证 (9 处)<br>  - verify/host-half.test.mjs:112 → 敏感凭证读取 (1 处)<br>  - verify/client-half.test.mjs:1153 → 敏感凭证读取 (2 处)<br>  ... 共 22 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - verify-independent/probe-13-r4-browser.mjs:144 → 连续十六进制转义 (混淆) (1 处) |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - verify/_harness.mjs:174 → node:vm 任意代码执行 (2 处)<br>  - verify-independent/r13v-adv-probe-18-deadanchor.mjs:442 → node:vm 任意代码执行 (1 处)<br>  - verify-independent/r13w-guard-probe-20-narrow.mjs:413 → node:vm 任意代码执行 (1 处)<br>  - verify-independent/r13v-adv-bell-checker.mjs:41 → node:vm 任意代码执行 (2 处)<br>  - verify-independent/r13v-adv-probe-19-deadanchor.mjs:450 → node:vm 任意代码执行 (1 处)<br>  ... 共 19 处 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 1 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - verify/_harness.mjs:669 → 定时任务 (1 处)<br>  - verify/client-half.test.mjs:155 → 定时任务 (1 处)<br>  - lib/index.js:457 → 定时任务 (1 处)<br>  - lib/client.js:1463 → 定时任务 (1 处)<br>  - docs/rev10-独立验证.md:23 → 临时文件操作 (1 处)<br>  ... 共 61 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - CHANGELOG.md:861 → 云存储上传 (1 处)<br>  - verify/custom-audio.test.mjs:4 → 云存储上传 (31 处)<br>  - verify/client-half.test.mjs:714 → 云存储上传 (1 处)<br>  - lib/index.js:92 → 云存储上传 (11 处)<br>  - lib/client.js:171 → 云存储上传 (18 处)<br>  ... 共 33 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 无第三方依赖 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 40455, 注释行: 5246 (13.0%) |
| 4.9 | 具备测试覆盖 | 推荐 | ⚠️  需人工复核 | 未发现测试文件 |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ✅ 通过 | 未检测到明文存储敏感信息 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - CHANGELOG.md:517 → 读取 git 历史 (3 处)<br>  - docs/rev10-需求符合性审查.md:44 → 读取 git 历史 (3 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (65 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ⚠️  需人工复核 | 未发现一键清理功能, 需确认是否有数据清理机制 |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - docs/rev4-独立验证.md:55 → 修改系统目录 (1 处)<br>  - verify-independent/r13v-adv-probe-19-deadanchor.mjs:1 → 修改系统目录 (1 处)<br>  - verify-independent/r15t3-legacy-inventory.mjs:1 → 修改系统目录 (1 处)<br>  - verify-independent/r15t2-assertion-inventory.mjs:1 → 修改系统目录 (1 处)<br>  - verify-independent/r15t2-independent-probe.mjs:1 → 修改系统目录 (1 处)<br>  ... 共 9 处 |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (3 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 8 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-approval-chime |
| 校验 URL | https://github.com/Cloudto1/dsh-approval-chime |
| 必查项通过率 | 15/33 (45%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-09-20 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
