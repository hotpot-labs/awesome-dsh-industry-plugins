# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/Anarrogantcat/dsh-identity
- **校验时间**: 2026-10-31 04:39:51
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 16 | 11 | 6 |
| 🟡 推荐 | 14 | 7 | 7 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2018-06-12 (3062 天前); 公开仓库数: 6; 粉丝数: 0 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 583; 包名: dsh-identity; 描述: DSH 身份系统：给「大肥鱼」一套持续运行的身份状态——可编辑内核、证据制 traits、记忆/日记/复盘、心情 v2、关系与精力、自主提议、共情与学习闭环。身 — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (20): v1.9.212, v1.9.211, v1.9.210, v1.9.209, v1.9.208; package.json version: 1.9.212 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | engines: {"node": ">=20", "dsh": ">=0.2.0"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"id": "dsh-identity", "name": "\u5927\u80a5\u9c7c \u00b7 \u8eab\u4efd\u7cfb\u7edf", "version": "1.9; Cordis 配置文件: cordis.patch.yml, awesome-dsh-plugin-entry.yml<br>  - lib/onebot-channel.js:560 → Monkey patch / prototype pollution<br>  - test/onebot-channel-test.mjs:197 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 1124 处, 函数: 2915 个, 比例: 38.6% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: lib/transport.js; 发现清理逻辑: lib/onebot-client.js; 发现清理逻辑: lib/onebot-channel.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - panel.html:1304 → 读取环境变量配置 (1 处)<br>  - lib/guard.js:36 → 读取环境变量配置 (1 处)<br>  - lib/bili-browser.js:16 → 读取环境变量配置 (2 处)<br>  - lib/bridge.js:17 → 读取环境变量配置 (1 处)<br>  - lib/payqr.js:169 → 读取环境变量配置 (2 处)<br>  ... 共 160 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - README.md:66 → 深层目录穿越 (1 处)<br>  - docs/INSTALL.md:39 → 深层目录穿越 (1 处)<br>  - docs/qqbot-refine-PLAN-FINAL.md:32 → 深层目录穿越 (3 处)<br>  - lib/guard.js:18 → 读取用户主目录 (1 处)<br>  - lib/toolgate.js:54 → 读取用户主目录 (2 处)<br>  ... 共 9 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - scripts/feiyu_cover.py:8 → Python subprocess (4 处)<br>  - scripts/feiyu_sing.py:47 → Python subprocess (3 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - README.md:172 → 开启 shell 模式 (注入风险) (1 处)<br>  - lib/stt.js:22 → 开启 shell 模式 (注入风险) (1 处)<br>  - lib/toolgate.js:533 → 开启 shell 模式 (注入风险) (2 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package.json:67 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - README.md:140 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - index.js:990 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - panel.html:786 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - panel.html:870 → fetch 网络请求 (41 处)<br>涉及的域名: 127.0.0.1, a.com, api.bilibili.com, api.sgroup.qq.com, b23.tv, bots.qq.com, cnmeme.wiki, codeload.github.com, esports-api.lolesports.com, esports.op.gg (+23 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - README.md:141 → API Key / Token 读取 (1 处)<br>  - panel.html:578 → API Key / Token 读取 (3 处)<br>  - docs/INSTALL.md:124 → API Key / Token 读取 (1 处)<br>  - docs/INSTALL.md:10 → 敏感凭证读取 (2 处)<br>  - docs/qqbot-refine-MIGRATION-PLAN.md:48 → 敏感凭证读取 (2 处)<br>  ... 共 238 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - test/llm-fix-test.mjs:9 → 写入配置文件 (1 处)<br>  - test/payqr-live-test.mjs:6 → 写入配置文件 (1 处)<br>  - test/profile-aging-test.mjs:9 → 写入配置文件 (1 处)<br>  - test/update-test.mjs:6 → 写入配置文件 (1 处)<br>  - test/cost-gate-test.mjs:9 → 写入配置文件 (1 处)<br>  ... 共 60 处 — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - test/ui-render-smoke-test.mjs:16 → eval() 任意代码执行 (1 处)<br>  - test/ui-interaction-smoke-test.mjs:16 → eval() 任意代码执行 (1 处)<br>  - test/client-drag-test.mjs:61 → new Function() 任意代码执行 (1 处)<br>  - scripts/panel-live-check.mjs:27 → eval() 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 1 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - index.js:647 → 定时任务 (17 处)<br>  - client.js:221 → 定时任务 (4 处)<br>  - panel.html:926 → 定时任务 (9 处)<br>  - lib/stt.js:72 → 定时任务 (1 处)<br>  - lib/roles.js:23 → 定时任务 (1 处)<br>  ... 共 158 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - assets/comfyui/sd15_img2img.json:6 → 云存储上传 (1 处)<br>  - docs/sample-img2img.png:4 → 云存储上传 (1 处)<br>  - docs/qqbot-refine-MIGRATION-PLAN.md:322 → 云存储上传 (2 处)<br>  - lib/draw.js:88 → FormData 上传 (1 处)<br>  - lib/draw.js:85 → 云存储上传 (11 处)<br>  ... 共 7 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 1. repo: 0 deps + 1 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 29576, 注释行: 2710 (9.2%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - client.js:109 → 明文写入敏感信息 (2 处)<br>  - lib/onebot-channel.js:946 → 明文写入敏感信息 (1 处)<br>  - test/llm-fix-test.mjs:9 → 明文写入敏感信息 (1 处)<br>  - test/payqr-live-test.mjs:6 → 明文写入敏感信息 (1 处)<br>  - test/profile-aging-test.mjs:9 → 明文写入敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (156 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (10 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - scripts/install-voice.ps1:38 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - test/run-all.mjs:1 → 修改系统目录 (1 处)<br>  - scripts/kbimport.py:1 → 修改系统目录 (1 处)<br>  - scripts/wiring-scan.mjs:1 → 修改系统目录 (1 处) |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (3 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 500 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 1, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-identity |
| 校验 URL | https://github.com/Anarrogantcat/dsh-identity |
| 必查项通过率 | 16/33 (48%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-31 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
