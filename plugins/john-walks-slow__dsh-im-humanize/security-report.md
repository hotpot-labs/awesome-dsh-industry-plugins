# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/john-walks-slow/dsh-im-humanize
- **校验时间**: 2026-09-21 04:01:01
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 16 | 12 | 5 |
| 🟡 推荐 | 14 | 7 | 7 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2017-12-13 (3203 天前); 公开仓库数: 100; 粉丝数: 13 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1723; 包名: @xmanrui/dsh-im; 描述: 把九种 IM 机器人和公网 AI Office 接入本机 DeepSeek Harness。 Connect nine IM channels and a pu — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - test/channels/feishu/registration-manager.test.mjs:231 → 盗版/侵权 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ⚠️  需人工复核 | 无 git tag; package.json version: 4.13.0; 有版本号但无 git tag / release |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | engines: {"node": ">=22.19"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": ["@deepseek-ai/dsh-client-connectio; Cordis 配置文件: cordis.patch.yml<br>  - plugin-src/host/delivery-http.mjs:93 → Monkey patch / prototype pollution<br>  - test/channels/feishu/bridge.test.mjs:4706 → Monkey patch / prototype pollution<br>  - test/channels/feishu/feishu-runtime.test.mjs:531 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 1762 处, 函数: 16451 个, 比例: 10.7% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: plugin-src/client/index.js; 发现清理逻辑: plugin-src/client/lifecycle.js; 发现清理逻辑: plugin-src/client/update-panel.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .gitignore:4 → 读取环境变量配置 (3 处)<br>  - plugin-src/client/build.mjs:10 → 读取环境变量配置 (2 处)<br>  - plugin-src/client/update-panel.js:450 → 读取环境变量配置 (1 处)<br>  - plugin-src/host/humanize-rpc.mjs:50 → 读取环境变量配置 (1 处)<br>  - plugin-src/host/update-service.mjs:203 → 读取环境变量配置 (1 处)<br>  ... 共 32 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - plugin-src/client/context-enhancement.js:11 → 深层目录穿越 (1 处)<br>  - plugin-src/client/index.js:2 → 深层目录穿越 (1 处)<br>  - plugin-src/client/access-policy-settings.js:7 → 深层目录穿越 (1 处)<br>  - plugin-src/client/global-settings.js:7 → 深层目录穿越 (1 处)<br>  - plugin-src/client/model-setting.js:8 → 深层目录穿越 (1 处)<br>  ... 共 192 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - plugin-src/host/update-runtime.mjs:237 → 进程执行 (1 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - THIRD_PARTY_NOTICES.md:3 → 探测到 HTTP(S) 网络请求 (14 处)<br>  - README.en.md:12 → 探测到 HTTP(S) 网络请求 (21 处)<br>  - README.en.md:125 → WebSocket 连接 (5 处)<br>  - README.en.md:125 → 浏览器网络 API (5 处)<br>  - wrangler.jsonc:2 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: 127.0.0.1, 127.8.9.10, 127.9.8.7, 192.168.1.20, academic.oup.com, accounts.feishu.cn, acris.aalto.fi, api.dingtalk.com, api.slack.com, api.telegram.org (+104 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - README.en.md:39 → 敏感凭证读取 (20 处)<br>  - PROACTIVE_DELIVERY.en.md:186 → 敏感凭证读取 (2 处)<br>  - CHANGELOG.md:54 → 敏感凭证读取 (3 处)<br>  - CHANGELOG.md:197 → 会话历史读取 (1 处)<br>  - README.md:42 → 敏感凭证读取 (11 处)<br>  ... 共 230 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - test/host.test.mjs:300 → 写入配置文件 (1 处)<br>  - test/inbound-ttl.test.mjs:125 → 写入配置文件 (3 处)<br>  - test/channels/telegram/telegram.test.mjs:820 → 写入配置文件 (1 处)<br>  - test/channels/feishu/plugin-host.test.mjs:1378 → 写入配置文件 (1 处)<br>  - src/channels/shared/humanize-settings.mjs:174 → 写入配置文件 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 15 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - plugin-src/client/update-panel.js:302 → 定时任务 (1 处)<br>  - plugin-src/client/channels/shared/token-channel.js:255 → 定时任务 (1 处)<br>  - plugin-src/client/channels/dingtalk/index.js:520 → 定时任务 (3 处)<br>  - plugin-src/client/channels/weixin/index.js:436 → 定时任务 (3 处)<br>  - plugin-src/client/channels/whatsapp/index.js:368 → 定时任务 (3 处)<br>  ... 共 120 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - README.en.md:134 → 云存储上传 (6 处)<br>  - CHANGELOG.md:466 → 云存储上传 (1 处)<br>  - README.md:161 → 云存储上传 (1 处)<br>  - plugin-src/client/i18n.js:462 → 云存储上传 (2 处)<br>  - lib/client.js:1316 → 云存储上传 (2 处)<br>  ... 共 65 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 15. repo: 6 deps + 9 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 163244, 注释行: 4136 (2.5%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - plugin-src/host/channels/feishu/rpc.mjs:73 → 硬编码敏感信息 (1 处)<br>  - test/harness-reply-tracker.test.mjs:121 → 硬编码敏感信息 (1 处)<br>  - test/model-setting.test.mjs:71 → 硬编码敏感信息 (1 处)<br>  - test/history-bridge.test.mjs:133 → 硬编码敏感信息 (2 处)<br>  - test/client-last-message-error.test.mjs:90 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - docs/方案/Issue-95-九渠道私聊群聊白名单与命令权限方案.md:592 → 读取 git 历史 (1 处)<br>  - docs/方案/Issue-61-npm更新检查与手动更新方案.md:455 → 读取 git 历史 (1 处)<br>  - docs/方案/Issue-106-九渠道引用消息Prompt字段精简方案.md:339 → 读取 git 历史 (2 处)<br>  - docs/方案/Issue-70-九渠道Harness问题与审批兼容修复方案.md:319 → 读取 git 历史 (1 处)<br>  - docs/features/260909-humanize-status-reaction-reply-quote/260909-humanize-status-reaction-reply-quote.review.md:12 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (37 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (5 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - docs/issues/260909-dsh-web-slow-listing/260909-dsh-web-slow-listing.troubleshoot.md:11 → 修改系统目录 (1 处)<br>  - test/update-service.test.mjs:387 → 创建开机自启/系统服务 (1 处)<br>  - test/update-runtime.test.mjs:241 → 创建开机自启/系统服务 (1 处)<br>  - test/channels/feishu/bridge.test.mjs:2094 → 修改系统目录 (1 处)<br>  - src/channels/shared/i18n-en/shared-a.mjs:35 → 创建开机自启/系统服务 (1 处)<br>  ... 共 7 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: 隔离, workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (9 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 3 天; 提交总数: 477 |
| 7.2 | 未标记停止维护 | 必查 | ❌ 不通过 | 文档中发现弃用标记: archived |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-im-humanize |
| 校验 URL | https://github.com/john-walks-slow/dsh-im-humanize |
| 必查项通过率 | 16/33 (48%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-09-21 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
