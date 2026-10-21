# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/LanJinGod/dsh-purge
- **校验时间**: 2026-10-21 03:50:29
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 15 | 10 | 8 |
| 🟡 推荐 | 14 | 6 | 8 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2022-06-11 (1592 天前); 公开仓库数: 3; 粉丝数: 0 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 4227; 包名: dsh-purge; 描述: DeepSeek Harness 破甲：让所有模型都能破甲，不同模型可换不同提示词；默认提示词面向国模「小码酱」。Jailbreak for every mod — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - README.zh-CN.md:128 → 欺诈行为 (1 处)<br>  - README.md:124 → 欺诈行为 (1 处)<br>  - client.js:144 → 窃取数据 (2 处)<br>  - client.js:7696 → 欺诈行为 (7 处)<br>  - lib/redteam/score-rules.js:781 → 欺诈行为 (1 处)<br>  ... 共 8 处 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (2): v1.1.73, v1.1.72; package.json version: 1.1.73+dsh0.2.1; GitHub Releases (2): v1.1.73, v1.1.72 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.1; engines: {"node": ">=18"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "inject": ["@deepseek-ai/d; Cordis/DSH 依赖: @deepseek-ai/cordis; Cordis 配置文件: cordis.patch.yml, cordis.patch.yml<br>  - client.js:685 → Monkey patch / prototype pollution<br>  - lib/core.js:998 → Monkey patch / prototype pollution<br>  - lib/index.js:918 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 1467 处, 函数: 4830 个, 比例: 30.4% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: client.js; 发现清理逻辑: lib/rewind.js; 发现清理逻辑: lib/index.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - client.js:163 → 读取环境变量配置 (8 处)<br>  - client.js:1778 → 读取浏览器 Cookie/本地存储 (16 处)<br>  - release-notes.md:377 → 读取环境变量配置 (2 处)<br>  - lib/desktop.js:20 → 读取环境变量配置 (22 处)<br>  - lib/restart-desktop.js:5 → 读取环境变量配置 (4 处)<br>  ... 共 54 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - README.zh-CN.md:250 → 深层目录穿越 (3 处)<br>  - README.md:246 → 深层目录穿越 (3 处)<br>  - release-notes.md:676 → 读取用户主目录 (2 处)<br>  - lib/desktop.js:134 → 目录遍历 (2 处)<br>  - lib/desktop.js:20 → 读取用户主目录 (5 处)<br>  ... 共 27 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - skills/redteam/vps-reverse-shell.md:85 → Python subprocess (1 处)<br>  - skills/redteam/shell-handler.md:76 → Python subprocess (1 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - lib/desktop.js:46 → 命令字符串拼接变量 (注入风险) (1 处)<br>  - lib/patch-effect.js:165 → exec 命令拼接 (1 处)<br>  - lib/redteam/store-core.js:977 → exec 命令拼接 (2 处)<br>  - lib/redteam/ui.js:173 → 开启 shell 模式 (注入风险) (1 处)<br>  - lib/redteam/schema.js:479 → 命令字符串拼接变量 (注入风险) (3 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - README.zh-CN.md:14 → 探测到 HTTP(S) 网络请求 (24 处)<br>  - package.json:61 → 探测到 HTTP(S) 网络请求 (6 处)<br>  - README.md:14 → 探测到 HTTP(S) 网络请求 (24 处)<br>  - client.js:143 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - client.js:64 → fetch 网络请求 (12 处)<br>涉及的域名: 10.0.0.5, 10.0.0.8, 10.20.30.40, 127.0.0.1, api.github.com, awesome-dsh-plugin.com, cdn.jsdelivr.net, chainreactors.github.io, codeload.github.com, crt.sh (+19 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - README.md:111 → 恶意软件 (1 处)<br>  - client.js:5660 → 代理/隧道 (6 处)<br>  - lib/redteam/score-rules.js:678 → 代理/隧道 (1 处)<br>  - lib/redteam/store-core.js:666 → 远控/反向 shell (2 处)<br>  - lib/redteam/store-core.js:254 → 代理/隧道 (21 处)<br>  ... 共 26 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - README.md:111 → 敏感凭证读取 (5 处)<br>  - client.js:64 → 敏感凭证读取 (30 处)<br>  - release-notes.md:793 → 敏感凭证读取 (2 处)<br>  - lib/desktop.js:20 → 读取环境变量 API Key/凭证 (5 处)<br>  - lib/restart-desktop.js:5 → 读取环境变量 API Key/凭证 (3 处)<br>  ... 共 41 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - lib/redteam/settings.js:38 → 写入配置文件 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - skills/redteam/unauth-exploit.md:39 → eval() 任意代码执行 (2 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 1 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - client.js:62 → 定时任务 (29 处)<br>  - .gitignore:13 → 临时文件操作 (1 处)<br>  - lib/desktop.js:948 → 定时任务 (3 处)<br>  - lib/desktop.js:37 → 文件写入 (10 处)<br>  - lib/desktop.js:1322 → 文件读取 (4 处)<br>  ... 共 86 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - client.js:743 → 云存储上传 (2 处)<br>  - release-notes.md:763 → 云存储上传 (1 处)<br>  - lib/core.js:4713 → 云存储上传 (5 处)<br>  - lib/redteam/store-core.js:5093 → 云存储上传 (1 处)<br>  - lib/redteam/tools.js:1820 → 云存储上传 (2 处)<br>  ... 共 12 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 无第三方依赖 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 58940, 注释行: 3853 (6.5%) |
| 4.9 | 具备测试覆盖 | 推荐 | ⚠️  需人工复核 | 未发现测试文件 |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - client.js:6590 → 明文写入敏感信息 (6 处)<br>  - lib/redteam/client.js:3106 → 明文写入敏感信息 (3 处)<br>  - lib/redteam/platform-config.js:91 → 从环境变量获取敏感信息 (2 处)<br>  - scripts/patch-client-dock.mjs:151 → 明文写入敏感信息 (1 处)<br>  - skills/redteam/frp-tunnel.md:46 → 硬编码敏感信息 (2 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (20 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (11 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - lib/redteam/skill-fixes.js:159 → 要求 root/sudo 权限<br>  - scripts/redteam-setup.sh:195 → 要求 root/sudo 权限<br>  - skills/redteam/vps-reverse-shell.md:27 → 要求 root/sudo 权限<br>  - skills/redteam/kimi-webbridge.md:15 → 要求 root/sudo 权限<br>  - skills/redteam/fscan-intranet.md:206 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - README.md:396 → 创建开机自启/系统服务 (1 处)<br>  - release-notes.md:1039 → 创建开机自启/系统服务 (1 处)<br>  - lib/desktop.js:683 → 修改系统目录 (4 处)<br>  - lib/core.js:1506 → 修改系统目录 (4 处)<br>  - lib/redteam/score-rules.js:564 → 修改系统目录 (1 处)<br>  ... 共 35 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: sandbox, workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (4 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 2 天; 提交总数: 4 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 6, Forks: 4, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-purge |
| 校验 URL | https://github.com/LanJinGod/dsh-purge |
| 必查项通过率 | 15/33 (45%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-21 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
