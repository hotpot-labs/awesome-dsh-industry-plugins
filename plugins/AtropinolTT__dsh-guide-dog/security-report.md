# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/AtropinolTT/dsh-guide-dog
- **校验时间**: 2026-08-23 14:27:04
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 17 | 11 | 5 |
| 🟡 推荐 | 14 | 5 | 9 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2022-04-05 (1601 天前); 公开仓库数: 14; 粉丝数: 1 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 5106; 包名: dsh-guide-dog; 描述: Guide Dog for DSH, powered by MiniMax — multimodal plugin: image/video/music/spe — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ⚠️  需人工复核 | 无 git tag; package.json version: 0.1.0; 有版本号但无 git tag / release |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ❌ 不通过 | 未在 package.json 中发现 DSH/Cordis 依赖或 engines 字段 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./bundle/cordis.patch.yml"}, "client": {"platform": "web", "inject": ["@deepse; Cordis 配置文件: cordis.patch.yml<br>  - plans/2026-08-14-phase2-call-mode.md:302 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 1177 处, 函数: 1644 个, 比例: 71.6% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: plugin-source.js; 发现清理逻辑: plugin-client.js; 发现清理逻辑: plugin-host.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - plugin-source.js:137 → 读取环境变量配置 (1 处)<br>  - plugin-host.js:167 → 读取环境变量配置 (1 处)<br>  - bundle/lib/index.js:260 → 读取环境变量配置 (1 处)<br>  - deploy/push-via-api.py:44 → 读取环境变量配置 (1 处)<br>  - scripts/whisper_transcribe.py:20 → 读取环境变量配置 (1 处) |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - plans/2026-08-14-phase2-call-mode.md:25 → 读取用户主目录 (1 处)<br>  - bundle/lib/index.js:32 → 读取用户主目录 (1 处)<br>  - deploy/convert_bundle.py:63 → 读取用户主目录 (1 处)<br>  - specs/2026-08-14-guide-dog-v2-design.md:66 → 读取用户主目录 (2 处) — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - plugin-source.js:351 → 进程执行 (5 处)<br>  - plugin-host.js:381 → 进程执行 (5 处)<br>  - plans/2026-08-14-phase1-voice-mode-and-voice-input.md:22 → 进程执行 (2 处)<br>  - plans/2026-08-14-phase2-call-mode.md:7 → 进程执行 (4 处)<br>  - bundle/lib/index.js:474 → 进程执行 (5 处)<br>  ... 共 6 处<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - plugin-source.js:137 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - plugin-source.js:933 → fetch 网络请求 (1 处)<br>  - plugin-client.js:273 → fetch 网络请求 (3 处)<br>  - README.zh-CN.md:3 → 探测到 HTTP(S) 网络请求 (13 处)<br>  - README.zh-CN.md:262 → WebSocket 连接 (2 处)<br>涉及的域名: 127.0.0.1, aihero.dev, api.github.com, api.minimax.io, deepwiki.com, developer.chrome.com, developer.mozilla.org, developers.openai.com, docs.livekit.io, docs.pipecat.ai (+17 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - plugin-source.js:1793 → API Key / Token 读取 (2 处)<br>  - plugin-source.js:1786 → 敏感凭证读取 (3 处)<br>  - plugin-client.js:523 → API Key / Token 读取 (2 处)<br>  - plugin-client.js:516 → 敏感凭证读取 (3 处)<br>  - README.zh-CN.md:513 → API Key / Token 读取 (2 处)<br>  ... 共 10 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - plans/2026-08-17-rc15-playback-fixes.md:78 → new Function() 任意代码执行 (2 处)<br>  - repro/repro-rc14.js:101 → eval() 任意代码执行 (2 处)<br>  - repro/repro-stream-drain.js:29 → eval() 任意代码执行 (1 处)<br>  - repro/repro-rc15.js:32 → new Function() 任意代码执行 (6 处)<br>  - repro/repro-progress.js:20 → eval() 任意代码执行 (5 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 0 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - plugin-source.js:941 → 定时任务 (1 处)<br>  - plugin-source.js:287 → 临时文件操作 (7 处)<br>  - plugin-client.js:272 → 定时任务 (7 处)<br>  - plugin-host.js:991 → 定时任务 (1 处)<br>  - plugin-host.js:317 → 临时文件操作 (8 处)<br>  ... 共 40 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - plugin-source.js:933 → 云存储上传 (2 处)<br>  - plugin-client.js:58 → 云存储上传 (7 处)<br>  - README.zh-CN.md:194 → 云存储上传 (1 处)<br>  - plugin-host.js:983 → 云存储上传 (2 处)<br>  - README.md:210 → 云存储上传 (1 处)<br>  ... 共 13 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 无第三方依赖 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 12947, 注释行: 1218 (9.4%) |
| 4.9 | 具备测试覆盖 | 推荐 | ⚠️  需人工复核 | 未发现测试文件 |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - plugin-client.js:1559 → 硬编码敏感信息 (1 处)<br>  - plugin-host.js:1546 → 硬编码敏感信息 (1 处)<br>  - plans/2026-08-14-phase2-call-mode.md:352 → 硬编码敏感信息 (3 处)<br>  - bundle/lib/client.js:1596 → 硬编码敏感信息 (1 处)<br>  - bundle/lib/index.js:1633 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - plans/2026-08-17-rc14-call-fixes.md:279 → 读取 git 历史 (1 处)<br>  - plans/2026-08-14-phase1-voice-mode-and-voice-input.md:57 → 读取 git 历史 (2 处)<br>  - plans/2026-08-17-rc15-playback-fixes.md:575 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (30 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (5 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - plugin-source.js:118 → 修改系统目录 (1 处)<br>  - plugin-host.js:148 → 修改系统目录 (2 处)<br>  - plans/2026-08-14-phase1-voice-mode-and-voice-input.md:255 → 修改系统目录 (2 处)<br>  - bundle/lib/index.js:241 → 修改系统目录 (2 处)<br>  - deploy/convert_bundle.py:1 → 修改系统目录 (1 处)<br>  ... 共 12 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: sandbox, workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (5 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 5 天; 提交总数: 130 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 5, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-guide-dog |
| 校验 URL | https://github.com/AtropinolTT/dsh-guide-dog |
| 必查项通过率 | 17/33 (52%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-23 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
