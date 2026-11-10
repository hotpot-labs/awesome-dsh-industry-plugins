# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/Geng-zy/aurabot-qq-mac
- **校验时间**: 2026-11-10 06:32:24
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 15 | 10 | 8 |
| 🟡 推荐 | 14 | 8 | 6 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2022-12-29 (1412 天前); 公开仓库数: 4; 粉丝数: 2 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 576; 包名: dsh-aurabot-qq; 描述: Aurabot for macOS：aureth-labs/dsh-aurabot-qq 的 macOS（Apple 芯片）分叉 —— DeepSeek Har — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - test/memory-eval.test.js:19 → 欺诈行为 (2 处)<br>  - test/memory.test.js:24 → 欺诈行为 (11 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (20): v1.2.1, v1.2.0-rc.1, v1.2.0-beta.2, v1.2.0-beta.1, v1.2.0; package.json version: 1.2.1; GitHub Releases (1): v1.2.1 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | engines: {"node": ">=22.13.0"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "inject": ["slots"], "exte; Cordis 配置文件: cordis.patch.yml<br>  - test/persona-panel.test.js:114 → Monkey patch / prototype pollution<br>  - test/integration-carrier.test.js:45 → Monkey patch / prototype pollution<br>  - client/client.js:1206 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 1213 处, 函数: 8409 个, 比例: 14.4% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: test/bili-avatar-source.test.js; 发现清理逻辑: test/issue34-setup.test.js; 发现清理逻辑: test/panel-access-gate.test.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - test/memory-time-related-seen.test.js:22 → 读取环境变量配置 (4 处)<br>  - test/memory-upgrade.test.js:26 → 读取环境变量配置 (6 处)<br>  - test/text.test.js:33 → 读取环境变量配置 (1 处)<br>  - test/injection.test.js:8 → 读取环境变量配置 (1 处)<br>  - test/h03-consolidate-auth.test.js:8 → 读取环境变量配置 (1 处)<br>  ... 共 89 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - test/community.test.js:136 → 深层目录穿越 (2 处)<br>  - test/diary-media.test.js:151 → 深层目录穿越 (2 处)<br>  - test/helpers/memory-state.js:2 → 深层目录穿越 (1 处)<br>  - src/host.js:682 → 读取用户主目录 (1 处)<br>  - src/core/workspace-move.js:36 → 读取用户主目录 (1 处)<br>  ... 共 31 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - test/memory-upgrade.test.js:374 → 命令字符串拼接变量 (注入风险) (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - CHANGELOG.md:172 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - CHANGELOG.md:367 → WebSocket 连接 (1 处)<br>  - CHANGELOG.md:367 → 浏览器网络 API (1 处)<br>  - package.json:54 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - THIRD-PARTY-NOTICES.md:8 → 探测到 HTTP(S) 网络请求 (2 处)<br>涉及的域名: 127.0.0.1, 169.254.169.254, 192.168.1.10, 192.168.1.5, 8.8.8.8, a.com, api.bilibili.com, api.openai.com, api.siliconflow.cn, auth.openai.com (+51 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - test/memory-time-related-seen.test.js:22 → 读取环境变量 API Key/凭证 (4 处)<br>  - test/memory-time-related-seen.test.js:247 → 敏感凭证读取 (3 处)<br>  - test/memory-upgrade.test.js:26 → 读取环境变量 API Key/凭证 (5 处)<br>  - test/text.test.js:33 → 读取环境变量 API Key/凭证 (1 处)<br>  - test/injection.test.js:8 → 读取环境变量 API Key/凭证 (1 处)<br>  ... 共 133 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - test/memory-upgrade.test.js:30 → 写入配置文件 (1 处)<br>  - test/issue34-setup.test.js:20 → 写入配置文件 (1 处)<br>  - test/panel-access-gate.test.js:31 → 写入配置文件 (1 处)<br>  - test/backup.test.js:52 → 写入配置文件 (1 处)<br>  - test/csrf-publicbase.test.js:28 → 写入配置文件 (1 处)<br>  ... 共 24 处 — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - src/song/netease.js:8 → 超长 base64 字符串 (1 处) |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - client/client.js:3698 → new Function() 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 0 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - test/local.test.js:46 → 定时任务 (2 处)<br>  - test/file-relay.test.js:55 → 定时任务 (1 处)<br>  - test/bili-media.test.js:32 → 开启监听端口 (1 处)<br>  - test/qq-tools-file.test.js:11 → 临时文件操作 (8 处)<br>  - test/module-lifecycle.test.js:10 → 定时任务 (2 处)<br>  ... 共 60 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - test/qq-api.test.js:11 → 云存储上传 (1 处)<br>  - test/output-guard.test.js:317 → 云存储上传 (1 处)<br>  - test/e2e.test.js:760 → 云存储上传 (46 处)<br>  - test/modules.test.js:427 → 云存储上传 (4 处)<br>  - test/imagegen-img2img.test.js:37 → multipart 上传 (2 处)<br>  ... 共 19 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 无第三方依赖 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 51778, 注释行: 3443 (6.6%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 120 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - test/memory-time-related-seen.test.js:247 → 硬编码敏感信息 (1 处)<br>  - test/module-lifecycle.test.js:156 → 硬编码敏感信息 (1 处)<br>  - test/codex-image.test.js:34 → 硬编码敏感信息 (2 处)<br>  - test/e2e.test.js:848 → 硬编码敏感信息 (2 处)<br>  - test/diary-archive.test.js:78 → 明文写入敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (88 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (5 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - docs/USER-MANUAL.md:129 → 要求 root/sudo 权限<br>  - test/danger-rules.test.js:57 → 要求 root/sudo 权限<br>  - src/song/studio.js:580 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - test/vision.test.js:48 → 修改系统目录 (2 处)<br>  - test/qq-tools-file.test.js:82 → 修改系统目录 (1 处)<br>  - test/panel-pet-dialog.test.js:95 → 修改系统目录 (1 处)<br>  - test/sl-gaps.test.js:369 → 修改系统目录 (1 处)<br>  - test/danger-rules.test.js:61 → Windows 系统配置修改 (1 处)<br>  ... 共 12 处 |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (4 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 419 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | aurabot-qq-mac |
| 校验 URL | https://github.com/Geng-zy/aurabot-qq-mac |
| 必查项通过率 | 15/33 (45%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-11-10 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
