# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/jarvislee90s-dot/dsh-foxbell-pet
- **校验时间**: 2026-09-12 03:51:13
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 16 | 10 | 7 |
| 🟡 推荐 | 14 | 8 | 6 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2026-03-07 (188 天前); 公开仓库数: 20; 粉丝数: 1 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1025; 包名: dsh-foxbell-pet; 描述: DSH Web 右下角可拖拽的多宠物桌宠系统（内置小狐狸 Foxbell）：多项目状态监控（MAM 色彩口径：红待审批/黄运行/绿完成未读，深红错误）+ 语音提 — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - docs/superpowers/plans/2026-09-11-v2.2-usage-dashboard.md:869 → 盗版/侵权 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (1): v2.0.0; package.json version: 2.2.0; GitHub Releases (1): v2.0.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/dsh-settings: ^0.1.2-rc.1 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "inject": []}}; Cordis/DSH 依赖: @deepseek-ai/dsh-settings; Cordis 配置文件: cordis.patch.yml<br>  - lib/client.js:3186 → Monkey patch / prototype pollution<br>  - docs/superpowers/plans/2026-09-11-v2.2-usage-dashboard.md:671 → Monkey patch / prototype pollution<br>  - test/host-index.test.mjs:58 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 389 处, 函数: 2195 个, 比例: 17.7% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: lib/client.js; 发现清理逻辑: test/client-logic.test.ts; 发现清理逻辑: src/client/voices.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - lib/index.js:11 → 读取环境变量配置 (10 处)<br>  - scripts/build.mjs:52 → 读取环境变量配置 (1 处)<br>  - scripts/validate.mjs:194 → 读取环境变量配置 (1 处)<br>  - test/host-index.test.mjs:55 → 读取环境变量配置 (2 处)<br>  - test/routes.test.mjs:611 → 读取环境变量配置 (7 处)<br>  ... 共 8 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - lib/index.js:14 → 读取用户主目录 (2 处)<br>  - scripts/gen-builtin-manifest.mjs:41 → 目录遍历 (1 处)<br>  - test/petid-manifest.test.mjs:153 → 目录遍历 (1 处)<br>  - test/petdex.test.mjs:227 → 目录遍历 (1 处)<br>  - test/routes.test.mjs:369 → 目录遍历 (3 处)<br>  ... 共 12 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - scripts/validate.mjs:46 → 命令字符串拼接变量 (注入风险) (2 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package-lock.json:28 → 探测到 HTTP(S) 网络请求 (158 处)<br>  - lib/index.js:1789 → 探测到 HTTP(S) 网络请求 (11 处)<br>  - lib/client.js:1146 → 探测到 HTTP(S) 网络请求 (7 处)<br>  - lib/client.js:243 → fetch 网络请求 (7 处)<br>  - reference/桃子衣服粉狐狸形象.png:6 → 探测到 HTTP(S) 网络请求 (2 处)<br>涉及的域名: 127.0.0.1, assets.petdex.dev, deep.api.petdex.dev, evil.com, evil.example.com, evilpetdex.dev, github.com, localhost, opencollective.com, petdex.dev (+7 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - IMPLEMENTATION_NOTES.md:24 → 敏感凭证读取 (1 处)<br>  - scripts/build.mjs:52 → 读取环境变量 API Key/凭证 (1 处)<br>  - test/host-index.test.mjs:55 → 读取环境变量 API Key/凭证 (2 处)<br>  - test/routes.test.mjs:458 → 敏感凭证读取 (5 处)<br>  - test/zip.test.mjs:15 → 敏感凭证读取 (1 处) — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - test/bundle-smoke.test.mjs:58 → node:vm 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 10 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - IMPLEMENTATION_NOTES.md:82 → 临时文件操作 (2 处)<br>  - demo/index.html:60 → 定时任务 (2 处)<br>  - lib/index.js:1089 → 文件写入 (1 处)<br>  - lib/index.js:1063 → 文件读取 (1 处)<br>  - lib/client.js:297 → 定时任务 (19 处)<br>  ... 共 57 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - lib/index.js:1981 → 云存储上传 (6 处)<br>  - lib/client.js:3961 → 云存储上传 (2 处)<br>  - docs/superpowers/plans/2026-09-11-v2.2-usage-dashboard.md:824 → 读取文件后上传 (1 处)<br>  - test/staging.test.mjs:200 → 云存储上传 (1 处)<br>  - src/client/dialogs/ImportDialog.tsx:130 → 云存储上传 (3 处)<br>  ... 共 6 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 10. repo: 3 deps + 7 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 20097, 注释行: 1423 (7.1%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 4 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - lib/client.js:314 → 明文写入敏感信息 (6 处)<br>  - docs/superpowers/plans/2026-08-18-foxbell-interactive-upgrade.md:126 → 明文写入敏感信息 (1 处)<br>  - test/routes.test.mjs:485 → 明文写入敏感信息 (1 处)<br>  - src/client/config.ts:235 → 明文写入敏感信息 (6 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - IMPLEMENTATION_NOTES.md:461 → 读取 git 历史 (2 处)<br>  - docs/superpowers/plans/2026-09-11-v2.1-efficiency-dashboard-port.md:13 → 读取 git 历史 (10 处)<br>  - docs/superpowers/plans/2026-09-11-v2.1-port-report.md:5 → 读取 git 历史 (2 处)<br>  - docs/superpowers/plans/2026-09-12-v2.2-executor-report.md:30 → 读取 git 历史 (2 处)<br>  - docs/superpowers/specs/2026-09-11-v2.1-efficiency-dashboard-port.md:14 → 读取 git 历史 (2 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (11 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (14 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - docs/superpowers/plans/2026-09-12-v2.2-executor-report.md:62 → 修改系统目录 (1 处)<br>  - test/zip.test.mjs:15 → 修改系统目录 (1 处) |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (7 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 97 |
| 7.2 | 未标记停止维护 | 必查 | ❌ 不通过 | 文档中发现弃用标记: 不再支持 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-foxbell-pet |
| 校验 URL | https://github.com/jarvislee90s-dot/dsh-foxbell-pet |
| 必查项通过率 | 16/33 (48%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-09-12 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
