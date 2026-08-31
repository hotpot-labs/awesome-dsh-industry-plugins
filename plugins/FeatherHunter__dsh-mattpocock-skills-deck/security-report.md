# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/FeatherHunter/dsh-mattpocock-skills-deck
- **校验时间**: 2026-08-31 04:26:48
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 11 | 13 | 9 |
| 🟡 推荐 | 14 | 8 | 6 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2015-06-19 (4090 天前); 公开仓库数: 46; 粉丝数: 10 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 564; 包名: dsh-mattpocock-skills-deck — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - tests/verify-issue-detail.js:2 → 欺诈行为 (4 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (8): v1.7.8, v1.7.7, v1.7.6, v1.7.3, v1.7.2; package.json version: 1.7.8; GitHub Releases (5): v1.7.8, v1.7.7, v1.7.6, v1.7.3, v1.6.15 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ❌ 不通过 | 未在 package.json 中发现 DSH/Cordis 依赖或 engines 字段 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./package/cordis.patch.yml"}}<br>  - src/client/views/ChecksTab.js:114 → Monkey patch / prototype pollution<br>  - src/client/views/shared/ChainRenderer.js:60 → Monkey patch / prototype pollution<br>  - src/client/kernel/actions.js:39 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 2306 处, 函数: 5451 个, 比例: 42.3% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: examples/demo-mini/index.js; 发现清理逻辑: src/host/tracker/registry.js; 发现清理逻辑: tests/verify-tracker-contract.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - DEV-WORKFLOW.md:131 → 读取环境变量配置 (1 处)<br>  - src/client/statusbar/StatusBar.js:254 → 读取环境变量配置 (2 处)<br>  - src/client/kernel/locale.js:14 → 读取环境变量配置 (6 处)<br>  - src/shared/tracker/check-catalog.js:286 → 读取环境变量配置 (2 处)<br>  - src/shared/tracker/chain.js:66 → 读取环境变量配置 (2 处)<br>  ... 共 64 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - examples/demo-mini/normalize.js:11 → 深层目录穿越 (1 处)<br>  - examples/demo-mini/README.md:13 → 深层目录穿越 (6 处)<br>  - examples/demo-mini/index.js:13 → 深层目录穿越 (5 处)<br>  - src/client/kernel/actions.js:22 → 深层目录穿越 (5 处)<br>  - src/host/index.js:160 → 读取用户主目录 (1 处)<br>  ... 共 74 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - src/host/index.js:236 → 进程执行 (6 处)<br>  - tests/verify-detail-fog.js:7 → 加载 child_process (1 处)<br>  - tests/verify-detail-levels.js:7 → 加载 child_process (1 处)<br>  - tests/verify-build-artifacts.js:12 → 加载 child_process (1 处)<br>  - tests/playwright-e2e-probe.js:8 → 加载 child_process (1 处)<br>  ... 共 9 处<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - tests/verify-no-mixed-session.js:113 → 命令字符串拼接变量 (注入风险) (3 处)<br>  - tests/verify-no-mixed-session.js:113 → exec 命令拼接 (3 处)<br>  - scripts/generate-github-fixtures.js:44 → 命令字符串拼接变量 (注入风险) (2 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - ARCHITECTURE-SPLIT-DIAGRAM.svg:2 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - SPEC-T1-template-editor.md:27 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - DEV-WORKFLOW.md:139 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - ACCEPTANCE.md:72 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - package.json:6 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: 127.0.0.1, a.com, api.github.com, avatars, avatars.githubusercontent.com, b.com, cdn.jsdelivr.net, cli.github.com, example.com, featherhunter.github.io (+12 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - DEV-WORKFLOW.md:131 → 读取环境变量 API Key/凭证 (1 处)<br>  - src/shared/tracker/chain.js:66 → 读取环境变量 API Key/凭证 (1 处)<br>  - src/host/index.js:155 → 读取环境变量 API Key/凭证 (2 处)<br>  - src/host/index.js:356 → 敏感凭证读取 (3 处)<br>  - src/host/platform/darwin/index.js:5 → 读取环境变量 API Key/凭证 (1 处)<br>  ... 共 40 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - src/host/index.js:116 → 修改全局配置 (1 处)<br>  - docs/architecture/FINAL-ARCHITECTURE-VISUALIZATION.md:249 → 修改全局配置 (1 处)<br>  - docs/architecture/MattSkills-architecture.html:6587 → 修改全局配置 (3 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - src/shared/naming-guardian.js:73 → 连续十六进制转义 (混淆) (2 处)<br>  - package/shared/naming-guardian.js:73 → 连续十六进制转义 (混淆) (2 处) |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - src/seam/gate.js:16 → node:vm 任意代码执行 (2 处)<br>  - tests/verify-tabs-narrow.js:92 → new Function() 任意代码执行 (1 处)<br>  - tests/verify-t14-detail-badge.js:88 → new Function() 任意代码执行 (1 处)<br>  - tests/verify-detail-fog.js:44 → new Function() 任意代码执行 (1 处)<br>  - tests/verify-detail-fog.js:7 → 加载 child_process 模块 (1 处)<br>  ... 共 31 处 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 6 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - DEV-WORKFLOW.md:131 → 文件读取 (2 处)<br>  - DEV-WORKFLOW.md:131 → 进程控制 (1 处)<br>  - src/client/index.js:64 → 定时任务 (4 处)<br>  - src/client/statusbar/StatusBar.js:102 → 定时任务 (3 处)<br>  - src/client/floating/SkillFloatList.js:41 → 定时任务 (2 处)<br>  ... 共 227 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - src/host/tracker/backends/github/index.js:188 → 云存储上传 (1 处)<br>  - .github/workflows/verify.yml:56 → 云存储上传 (2 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 6. repo: 1 deps + 5 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 47952, 注释行: 7599 (15.8%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 7 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - src/client/kernel/config.js:27 → 明文写入敏感信息 (2 处)<br>  - src/client/kernel/store.js:22 → 明文写入敏感信息 (4 处)<br>  - src/host/platform/win32/index.js:30 → 从环境变量获取敏感信息 (1 处)<br>  - tests/verify-t1-getrepokey.js:58 → 明文写入敏感信息 (1 处)<br>  - tests/verify-t1-initpublish.js:90 → 明文写入敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - DEV-WORKFLOW.md:198 → 读取 git 历史 (1 处)<br>  - ARCHITECTURE-SPLIT.md:298 → 读取 git 历史 (1 处)<br>  - CHANGELOG.md:63 → 读取 git 历史 (1 处)<br>  - tests/verify-no-mixed-session.js:113 → 读取 git 历史 (5 处)<br>  - tests/verify-t1-initpublish.js:177 → 读取 git 历史 (2 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (117 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (6 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - src/host/index.js:3396 → 要求 root/sudo 权限<br>  - src/host/tracker/backends/github/preflight.js:18 → 要求 root/sudo 权限<br>  - src/host/tracker/backends/github/index.js:183 → 要求 root/sudo 权限<br>  - tests/.tmp-repo-out/backends/github/index.js:1232 → 要求 root/sudo 权限<br>  - tests/.tmp-repo-out2/backends/github/index.js:1232 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - tests/verify-panel-workspace-shared.js:1 → 修改系统目录 (1 处)<br>  - tests/verify-locale-completeness.js:1 → 修改系统目录 (1 处)<br>  - tests/verify-3-workspace-switch.js:1 → 修改系统目录 (1 处)<br>  - tests/verify-no-mixed-session.js:1 → 修改系统目录 (1 处)<br>  - tests/verify-platform-contract.js:510 → 修改系统目录 (6 处)<br>  ... 共 16 处 |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (6 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 471 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 34, Forks: 3, Watchers: 0 — 有一定社区基础 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-mattpocock-skills-deck |
| 校验 URL | https://github.com/FeatherHunter/dsh-mattpocock-skills-deck |
| 必查项通过率 | 11/33 (33%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-31 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
