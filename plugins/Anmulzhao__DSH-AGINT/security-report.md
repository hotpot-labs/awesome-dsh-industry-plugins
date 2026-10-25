# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/Anmulzhao/DSH-AGINT
- **校验时间**: 2026-10-25 03:47:21
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 13 | 12 | 8 |
| 🟡 推荐 | 14 | 7 | 6 | 1 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2021-05-18 (1986 天前); 公开仓库数: 8; 粉丝数: 6 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 363; 包名: @agint/host; 描述: AGINT 智进 —— dsh bundle：自进化智能体框架（host 服务 + 4 个 preset + 插件热插拔） — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - presets/agint-blockchain/skills/wallet-security/SKILL.md:3 → 欺诈行为 (9 处)<br>  - presets/agint-blockchain/skills/defi-mechanics/SKILL.md:263 → 欺诈行为 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (20): v0.13.0, v0.12.0, v0.11.0, v0.10.0, v0.9.0; package.json version: 0.13.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | engines: {"node": ">=20"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}}; Cordis 配置文件: cordis.patch.yml<br>  - proposals/agint-mount-integrate-restart.md:252 → Monkey patch / prototype pollution<br>  - plugins/agint-family-panel/lib/v2-data.js:899 → Monkey patch / prototype pollution<br>  - plugins/agint-family-panel/test/proposal-board.test.mjs:34 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 2332 处, 函数: 15781 个, 比例: 14.8% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: archived-plugins/agint-voice-hotkey/lib/client.js; 发现清理逻辑: archived-plugins/agint-voice-hotkey/lib/index.js; 发现清理逻辑: plugins/agint-dream/lib/consolidation.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .gitignore:34 → 读取环境变量配置 (2 处)<br>  - AGENTS.md:53 → 读取环境变量配置 (1 处)<br>  - cordis.patch.yml:32 → 读取环境变量配置 (34 处)<br>  - .agint-env.local.example:7 → 读取环境变量配置 (2 处)<br>  - archived-plugins/agint-voice-hotkey/lib/index.js:28 → 读取环境变量配置 (1 处)<br>  ... 共 147 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - cordis.patch.yml:260 → 深层目录穿越 (4 处)<br>  - VERSION:23 → 深层目录穿越 (3 处)<br>  - archived-plugins/agint-voice-hotkey/manifest.json:2 → 深层目录穿越 (1 处)<br>  - proposals/agint-family-panel-v2-上线实施计划-20261004.md:960 → 读取用户主目录 (1 处)<br>  - proposals/agint-restart-rollback.md:292 → 深层目录穿越 (1 处)<br>  ... 共 177 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - plugins/agint-restart/test/respawn-zombie.test.mjs:65 → 加载 child_process (1 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - plugins/agint-input-gateway/lib/channels/external-git.js:44 → 命令字符串拼接变量 (注入风险) (1 处)<br>  - eval/e2e/sprint5-sdk-cli.js:36 → 命令字符串拼接变量 (注入风险) (1 处)<br>  - eval/e2e/sprint6-pipeline.js:82 → 命令字符串拼接变量 (注入风险) (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - AGENTS.md:85 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - README.md:13 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - README.en.md:13 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - package.json:9 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - archived-plugins/agint-voice-hotkey/CHANGELOG.md:17 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: ..., 127.0.0.1, 90759cff-, NAS_IP, abc.cdnkuaishou.com, api.avax.network, api.devnet.solana.com, api.github.com, api.mainnet-beta.solana.com, api.minimax.cn (+30 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - plugins/agint-family-panel/lib/client.js:184 → DDoS 攻击 (3 处)<br>  - plugins/agint-family-panel/test/dossier-view.test.mjs:51 → DDoS 攻击 (6 处)<br>  - plugins/agint-quality-sandbox/CHANGELOG.md:122 → 代理/隧道 (1 处)<br>  - plugins/agint-metrics/lib/metrics.js:49 → 挖矿相关 (1 处)<br>  - presets/agint/skills/github-push/SKILL.md:26 → 代理/隧道 (2 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - .gitignore:33 → 敏感凭证读取 (2 处)<br>  - AGENTS.md:54 → 敏感凭证读取 (2 处)<br>  - cordis.patch.yml:32 → 读取环境变量 API Key/凭证 (25 处)<br>  - cordis.patch.yml:222 → 敏感凭证读取 (2 处)<br>  - archived-plugins/agint-voice-hotkey/lib/index.js:28 → 读取环境变量 API Key/凭证 (1 处)<br>  ... 共 174 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - plugins/agint-family-panel/test/proposal-board.test.mjs:81 → node:vm 任意代码执行 (1 处)<br>  - plugins/agint-family-panel/test/helpers/browser-half.mjs:48 → new Function() 任意代码执行 (1 处)<br>  - plugins/agint-quality-eval/README.md:1 → eval() 任意代码执行 (1 处)<br>  - plugins/agint-quality-sandbox/lib/smoke.js:156 → eval() 任意代码执行 (1 处)<br>  - plugins/agint-restart/test/respawn-zombie.test.mjs:65 → 加载 child_process 模块 (1 处)<br>  ... 共 10 处 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 0 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - VERSION:23 → 进程控制 (1 处)<br>  - archived-plugins/agint-voice-hotkey/lib/client.js:122 → 定时任务 (4 处)<br>  - archived-plugins/agint-voice-hotkey/lib/index.js:54 → 定时任务 (1 处)<br>  - archived-plugins/agint-voice-hotkey/test/smoke.mjs:85 → 开启监听端口 (1 处)<br>  - archived-plugins/agint-voice-hotkey/test/smoke.mjs:101 → 定时任务 (3 处)<br>  ... 共 267 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - plugins/agint-skill-autocreate/lib/templates.js:23 → 云存储上传 (1 处)<br>  - plugins/agint-skill-autocreate/lib/detector.js:41 → 云存储上传 (1 处)<br>  - plugins/agint-skill-autocreate/test/release-specificity-gate.test.mjs:129 → 云存储上传 (2 处)<br>  - presets/agint/skills/github-push/SKILL.md:172 → 云存储上传 (1 处)<br>  - bin/export-evolution-package.mjs:15 → 云存储上传 (1 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 无第三方依赖 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 180781, 注释行: 36585 (20.2%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 70 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - plugins/agint-dream/test/recall-store.test.js:75 → 明文写入敏感信息 (1 处)<br>  - plugins/agint-quality-static/test/skill-checkers.test.mjs:96 → 硬编码敏感信息 (2 处)<br>  - plugins/agint-quality-static/test/checkers.test.mjs:197 → 从环境变量获取敏感信息 (1 处)<br>  - plugins/agint-restart/test/env-snapshot-redaction.test.mjs:39 → 硬编码敏感信息 (4 处)<br>  - docs/operations/codex-handshake-20260821.md:41 → 硬编码敏感信息 (2 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - cordis.patch.yml:209 → 读取 git 历史 (1 处)<br>  - proposals/agint-family-panel-v2-上线实施计划-20261004.md:1128 → 读取 git 历史 (1 处)<br>  - proposals/license-agint-template-20261004.md:116 → 读取 git 历史 (2 处)<br>  - plugins/agint-family-panel/test/fixtures/v2-scan-baseline.json:17 → 读取 git 历史 (1 处)<br>  - plugins/agint-quality-sdk/CHANGELOG.md:4 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (176 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (48 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - plugins/agint-quality-sandbox/lib/smoke.js:156 → 要求 root/sudo 权限<br>  - install/agint-zstd-bootstrap.sh:16 → 要求 root/sudo 权限<br>  - bundles/dsh-kill-switch/test/index.test.mjs:216 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - plugins/agint-dream/test/smoke.mjs:1 → 修改系统目录 (7 处)<br>  - plugins/agint-dream/test/consolidation-batch.test.mjs:1 → 修改系统目录 (1 处)<br>  - plugins/agint-dream/test/profile-name-parity.test.mjs:1 → 修改系统目录 (1 处)<br>  - plugins/agint-population/test/smoke.mjs:1 → 修改系统目录 (1 处)<br>  - plugins/agint-population/test/e2e.mjs:1 → 修改系统目录 (1 处)<br>  ... 共 133 处 |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (13 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 728 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ❌ 不通过 | 缺少文档: CHANGELOG, 配置说明, 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 1, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | DSH-AGINT |
| 校验 URL | https://github.com/Anmulzhao/DSH-AGINT |
| 必查项通过率 | 13/33 (39%) |
| 推荐项满足率 | 13/14 (约 93%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-25 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
