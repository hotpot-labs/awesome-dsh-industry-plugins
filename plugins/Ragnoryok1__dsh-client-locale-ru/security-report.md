# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/Ragnoryok1/dsh-client-locale-ru
- **校验时间**: 2026-10-23 03:57:04
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 15 | 9 | 9 |
| 🟡 推荐 | 14 | 7 | 7 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2019-05-24 (2708 天前); 公开仓库数: 8; 粉丝数: 1 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 5594; 包名: @ragnoryok1/dsh-client-locale-ru; 描述: Russian (ru) interface for the DeepSeek Harness web GUI: 584 namespaces, 67724 s — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - plugins/dsh-server-monitor.json:81 → 破解授权 (1 处)<br>  - plugins/settings.codexSubscription.json:499 → 盗版/侵权 (3 处)<br>  - plugins/dsh-subscriptions.json:104 → 盗版/侵权 (1 处)<br>  - plugins/dshhub-market.json:262 → 欺诈行为 (2 处)<br>  - plugins/xiaomi-mimo-tts.json:189 → 盗版/侵权 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (20): v0.2.15, v0.2.14, v0.2.13, v0.2.12, v0.2.11; package.json version: 0.2.15; GitHub Releases (2): v0.2.15, v0.2.14 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.2 \|\| >=4.0.5-0 <4.0.6-0; @deepseek-ai/dsh-client-locale: >=0.1.0-rc.2 <0.1.1-0 \|\| >=0.1.1-0 <0.1.2-0 \|\| >=0.1.2-0 <0.1.3-0 \|\| >=0.1.3-0 <0.1.5-0 \|\| >=0.1.5-0 <0.1.6-0 \|\| >=0.1.6-0 <0.1.7-0 \|\| >=0.1.7-0 <0.2.0-0 \|\| >=0.2.0-rc.1 <0.2.1-0 \|\| >=0.2.1-0 <0.3.0-0 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": ["@deepseek-ai/dsh-client-locale"],; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-client-locale; Cordis 配置文件: cordis.patch.yml<br>  - README.en.md:184 → Monkey patch / prototype pollution<br>  - plugins/acp_turn_sep_.json:141 → Monkey patch / prototype pollution<br>  - plugins/foldPositions.json:140 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 42 处, 函数: 499 个, 比例: 8.4% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: scripts/check-plugin-names-dom.mjs; 发现清理逻辑: scripts/check-typography-dom.mjs; 发现清理逻辑: scripts/check-locale.mjs |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - CHANGELOG.md:420 → 读取 SSH 私钥目录 (2 处)<br>  - .gitignore:26 → 读取 npm 凭证 (1 处)<br>  - .gitignore:24 → 读取环境变量配置 (2 处)<br>  - plugins/dsh-winrm.json:26 → 读取环境变量配置 (2 处)<br>  - plugins/clawock.json:325 → 读取环境变量配置 (1 处)<br>  ... 共 67 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - scripts/report-plugins.mjs:29 → 读取用户主目录 (1 处) — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - scripts/fetch-plugin-dicts.mjs:108 → exec 命令拼接 (4 处)<br>  - scripts/check-tarball.mjs:37 → 命令字符串拼接变量 (注入风险) (1 处)<br>  - scripts/check-tarball.mjs:36 → 开启 shell 模式 (注入风险) (1 处)<br>  - scripts/check-built.mjs:22 → 开启 shell 模式 (注入风险) (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package-lock.json:26 → 探测到 HTTP(S) 网络请求 (140 处)<br>  - CHANGELOG.md:25 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - README.zh.md:7 → 探测到 HTTP(S) 网络请求 (16 处)<br>  - README.md:7 → 探测到 HTTP(S) 网络请求 (15 处)<br>  - README.en.md:7 → 探测到 HTTP(S) 网络请求 (16 处)<br>涉及的域名: ., ..., 127.0.0.1, 192.168.1.111, 192.168.1.5, 192.168.1.50, api.bytedanceapi.com, api.commandcode.ai, api.day.app, api.deepgram.com (+47 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - NAMESPACES.md:170 → 挖矿相关 (4 处)<br>  - CHANGELOG.md:96 → 挖矿相关 (2 处)<br>  - plugins/dsh-pdf-mineru.json:2 → 挖矿相关 (10 处)<br>  - plugins/dsh-mineru.json:2 → 挖矿相关 (8 处)<br>  - plugins/ds-harness-remote.json:203 → 远控/反向 shell (1 处)<br>  ... 共 25 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - NAMESPACES.md:415 → API Key / Token 读取 (1 处)<br>  - NAMESPACES.md:283 → 敏感凭证读取 (4 处)<br>  - CHANGELOG.md:117 → API Key / Token 读取 (1 处)<br>  - CHANGELOG.md:105 → 敏感凭证读取 (4 处)<br>  - README.zh.md:214 → 敏感凭证读取 (1 处)<br>  ... 共 223 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - plugins/dsh-shadow-auditor.json:31 → eval() 任意代码执行 (1 处)<br>  - scripts/check-plugin-names-dom.mjs:91 → node:vm 任意代码执行 (1 处)<br>  - scripts/build-plugin-names.mjs:46 → node:vm 任意代码执行 (1 处)<br>  - scripts/check-locale.mjs:22 → node:vm 任意代码执行 (2 处)<br>  - scripts/namespaces.mjs:34 → node:vm 任意代码执行 (1 处)<br>  ... 共 8 处 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 6 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - plugins/dsh-vsceditor.json:89 → 临时文件操作 (1 处)<br>  - plugins/dsh-ssh.json:146 → 临时文件操作 (1 处)<br>  - plugins/gitbashShell.json:27 → 临时文件操作 (4 处)<br>  - plugins/dsw.json:243 → 临时文件操作 (1 处)<br>  - .github/workflows/publish.yml:66 → 文件读取 (1 处)<br>  ... 共 34 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - CHANGELOG.md:1128 → 云存储上传 (2 处)<br>  - README.en.md:376 → 云存储上传 (1 处)<br>  - plugins/dsh-winrm.json:116 → 云存储上传 (6 处)<br>  - plugins/settings.runninghub.json:93 → multipart 上传 (1 处)<br>  - plugins/settings.runninghub.json:92 → 云存储上传 (4 处)<br>  ... 共 53 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 6. repo: 0 deps + 6 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 7992, 注释行: 2401 (30.0%) |
| 4.9 | 具备测试覆盖 | 推荐 | ⚠️  需人工复核 | 未发现测试文件 |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ✅ 通过 | 未检测到明文存储敏感信息 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - CHANGELOG.md:220 → 读取 git 历史 (2 处)<br>  - plugins/dsh-goal.json:28 → 读取 git 历史 (1 处)<br>  - plugins/dshAdmin.json:550 → 读取 git 历史 (2 处)<br>  - plugins/git.json:62 → 读取 git 历史 (1 处)<br>  - plugins/worktree.json:26 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (46 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (40 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - plugins/dsh-kanban.json:226 → 要求 root/sudo 权限<br>  - plugins/settings.packyCodeApi.json:35 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - plugins/goodandready-smart-restart.json:41 → 创建开机自启/系统服务 (2 处)<br>  - plugins/dsh-acp.json:18 → 创建开机自启/系统服务 (1 处)<br>  - plugins/dsh-server-monitor.json:61 → 修改系统目录 (1 处)<br>  - plugins/whale-pet.json:47 → 创建开机自启/系统服务 (2 处)<br>  - plugins/dsh-market.json:579 → 修改系统目录 (1 处)<br>  ... 共 32 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (9 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 184 |
| 7.2 | 未标记停止维护 | 必查 | ❌ 不通过 | 文档中发现弃用标记: archived |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 3, Forks: 2, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-client-locale-ru |
| 校验 URL | https://github.com/Ragnoryok1/dsh-client-locale-ru |
| 必查项通过率 | 15/33 (45%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-23 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
