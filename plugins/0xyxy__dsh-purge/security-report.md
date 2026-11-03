# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/0xyxy/dsh-purge
- **校验时间**: 2026-11-03 05:48:56
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 12 | 12 | 9 |
| 🟡 推荐 | 14 | 7 | 7 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: master |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2023-03-16 (1327 天前); 公开仓库数: 10; 粉丝数: 0 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ❌ 不通过 | 未找到许可证声明 (package.json 无 license 字段且无 LICENSE 文件) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1009; 包名: dsh-purge-community; 描述: 让 AI 更专注地辅助学习与动手实验：DSH 附加组件，提供状态自检、提示词与规则管理、本机备份与回滚。 — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - bootstrap/payload/prompt-inject.md:144 → 破解授权 (5 处)<br>  - bootstrap/payload/prompt-inject.md:145 → 欺诈行为 (9 处)<br>  - bootstrap/payload/prompt-inject.md:163 → 盗版/侵权 (2 处)<br>  - bootstrap/payload/prompt-inject.md.bak-pre-emotion:113 → 破解授权 (5 处)<br>  - bootstrap/payload/prompt-inject.md.bak-pre-emotion:114 → 欺诈行为 (9 处)<br>  ... 共 16 处 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (20): v1.6.67, v1.6.66, v1.6.65, v1.6.64, v1.6.63; package.json version: 1.6.67; GitHub Releases (2): v1.6.67, v1.6.60 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.1; engines: {"node": ">=18"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "inject": ["@deepseek-ai/d; Cordis/DSH 依赖: @deepseek-ai/cordis; Cordis 配置文件: cordis.patch.yml<br>  - lib/core.js:964 → Monkey patch / prototype pollution<br>  - lib/market-migration.js:67 → Monkey patch / prototype pollution<br>  - lib/index.js:932 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 1824 处, 函数: 6802 个, 比例: 26.8% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: bin/dsh-purge.js; 发现清理逻辑: packages/purge-panel/test/rewind.mjs; 发现清理逻辑: packages/purge-panel/test/maintenance.test.cjs |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - client.js:5871 → 读取环境变量配置 (8 处)<br>  - client.js:6914 → 读取浏览器 Cookie/本地存储 (14 处)<br>  - bin/community.js:20 → 读取环境变量配置 (3 处)<br>  - bootstrap/pack-custom.mjs:212 → 读取环境变量配置 (2 处)<br>  - bootstrap/verify-layers.mjs:42 → 读取环境变量配置 (5 处)<br>  ... 共 140 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - bootstrap/sync-presets.mjs:38 → 目录遍历 (1 处)<br>  - bootstrap/pack-custom.mjs:59 → 目录遍历 (1 处)<br>  - bootstrap/verify-layers.mjs:56 → 目录遍历 (3 处)<br>  - bootstrap/verify-layers.mjs:42 → 读取用户主目录 (1 处)<br>  - bootstrap/test/release-layout.test.mjs:110 → 目录遍历 (1 处)<br>  ... 共 71 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - skills/redteam/vps-reverse-shell.md:85 → Python subprocess (1 处)<br>  - skills/redteam/shell-handler.md:76 → Python subprocess (1 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - lib/redteam/store-core.js:978 → exec 命令拼接 (2 处)<br>  - lib/redteam/ui.js:173 → 开启 shell 模式 (注入风险) (1 处)<br>  - lib/redteam/schema.js:479 → 命令字符串拼接变量 (注入风险) (3 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package-lock.json:30 → 探测到 HTTP(S) 网络请求 (5 处)<br>  - release-notes.md:20 → 探测到 HTTP(S) 网络请求 (14 处)<br>  - package.json:78 → 探测到 HTTP(S) 网络请求 (6 处)<br>  - README.md:9 → 探测到 HTTP(S) 网络请求 (63 处)<br>  - AGENTS.md:436 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: 0xyxy.github.io, 10.0.0.5, 10.0.0.8, 10.20.30.40, 127.0.0.1, 169.254.169.254, TARGET, api.github.com, api.openai.com, avatars.githubusercontent.com (+43 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - release-notes.md:190 → 挖矿相关 (2 处)<br>  - release-notes.md:186 → 代理/隧道 (1 处)<br>  - README.md:241 → 挖矿相关 (3 处)<br>  - AGENTS.md:408 → 代理/隧道 (1 处)<br>  - README.zh-CN.md:241 → 挖矿相关 (3 处)<br>  ... 共 54 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - package.json:42 → 敏感凭证读取 (1 处)<br>  - client.js:202 → 敏感凭证读取 (31 处)<br>  - bin/community.js:20 → 读取环境变量 API Key/凭证 (3 处)<br>  - bootstrap/pack-custom.mjs:212 → 读取环境变量 API Key/凭证 (2 处)<br>  - bootstrap/verify-layers.mjs:42 → 读取环境变量 API Key/凭证 (4 处)<br>  ... 共 141 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - lib/redteam/settings.js:38 → 写入配置文件 (1 处)<br>  - test/instance.test.mjs:35 → 写入配置文件 (1 处)<br>  - test/instance.test.mjs:35 → 写入 DSH 配置 (1 处)<br>  - test/bootstrap-install.test.mjs:16 → 写入配置文件 (1 处)<br>  - test/install-windows.ps1:19 → 写入配置文件 (1 处)<br>  ... 共 19 处 — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - packages/purge-panel/test/restart.test.cjs:51 → node:vm 任意代码执行 (1 处)<br>  - packages/purge-panel/test/maintenance.test.cjs:46 → node:vm 任意代码执行 (2 处)<br>  - packages/purge-panel/test/status.test.cjs:36 → node:vm 任意代码执行 (1 处)<br>  - packages/purge-panel/test/check.cjs:99 → node:vm 任意代码执行 (1 处)<br>  - packages/purge-panel/test/requests.cjs:104 → node:vm 任意代码执行 (1 处)<br>  ... 共 14 处 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 2 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - .gitignore:13 → 临时文件操作 (1 处)<br>  - client.js:197 → 定时任务 (27 处)<br>  - bin/community.js:232 → 进程控制 (1 处)<br>  - bin/dsh-purge.js:60 → 进程控制 (4 处)<br>  - bootstrap/sync-presets.mjs:54 → 文件读取 (1 处)<br>  ... 共 403 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - client.js:881 → 云存储上传 (2 处)<br>  - bootstrap/payload/prompt-inject.md:153 → 云存储上传 (2 处)<br>  - bootstrap/payload/prompt-inject.md.bak-pre-emotion:122 → 云存储上传 (2 处)<br>  - skills/redteam/browser-automation.md:42 → 云存储上传 (2 处)<br>  - skills/redteam/webshell-toolkit.md:47 → 云存储上传 (3 处)<br>  ... 共 17 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 2. repo: 1 deps + 1 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 78786, 注释行: 4612 (5.9%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 3 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - client.js:6923 → 明文写入敏感信息 (5 处)<br>  - skills/redteam/frp-tunnel.md:46 → 硬编码敏感信息 (2 处)<br>  - packages/purge-panel/client.js:6923 → 明文写入敏感信息 (5 处)<br>  - packages/purge-panel/test/maintenance.test.cjs:435 → 硬编码敏感信息 (1 处)<br>  - packages/purge-panel/src/components/welcome.js:20 → 明文写入敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - test/update-policy.test.mjs:24 → 遍历用户目录 (1 处)<br>  - test/bootstrap-download.test.mjs:71 → 遍历用户目录 (1 处)<br>  - test/installed-package.test.mjs:47 → 读取文档/压缩文件 (1 处)<br>  - test/desktop-presets.mjs:155 → 遍历用户目录 (2 处)<br>  - test/apply-missing-target.test.mjs:113 → 读取文档/压缩文件 (3 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (78 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (59 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - bootstrap/payload/prompt-inject.md:156 → 要求 root/sudo 权限<br>  - bootstrap/payload/prompt-inject.md.bak-pre-emotion:125 → 要求 root/sudo 权限<br>  - skills/redteam/kimi-webbridge.md:15 → 要求 root/sudo 权限<br>  - skills/redteam/vps-reverse-shell.md:27 → 要求 root/sudo 权限<br>  - skills/redteam/credential-attack.md:24 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - AGENTS.md:307 → 修改系统目录 (1 处)<br>  - bin/community.js:1 → 修改系统目录 (1 处)<br>  - bin/dsh-purge.js:1 → 修改系统目录 (1 处)<br>  - bootstrap/sync-presets.mjs:1 → 修改系统目录 (1 处)<br>  - bootstrap/pack-custom.mjs:1 → 修改系统目录 (1 处)<br>  ... 共 52 处 |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (36 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 1 天; 提交总数: 485 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 1, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-purge |
| 校验 URL | https://github.com/0xyxy/dsh-purge |
| 必查项通过率 | 12/33 (36%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-11-03 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
