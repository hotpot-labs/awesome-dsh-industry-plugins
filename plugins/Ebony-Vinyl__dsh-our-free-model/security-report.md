# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/Ebony-Vinyl/dsh-our-free-model
- **校验时间**: 2026-10-18 03:46:12
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 16 | 9 | 8 |
| 🟡 推荐 | 14 | 7 | 7 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2025-11-22 (329 天前); 公开仓库数: 23; 粉丝数: 145 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 3964; 包名: dsh-our-free-model; 描述: Our Free Model — 在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Ki — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - packages/standalone/web/app.js:10 → 破解授权 (2 处)<br>  - packages/standalone/web/app.js:2 → 盗版/侵权 (8 处)<br>  - docs/eac-seal-migration.md:45 → 盗版/侵权 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (19): v2.5.3, v2.5.2, v2.5.1, v2.5.0, v2.4.0; package.json version: 2.5.3; GitHub Releases (5): v2.5.3, v2.5.2, v2.5.1, v2.5.0, v2.4.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.2; @deepseek-ai/dsh-commands: ^0.1.2-rc.1 \|\| ^0.1.7-rc.2 \|\| ^0.2.0-rc.1; @deepseek-ai/dsh-credentials: ^0.1.2-rc.1 \|\| ^0.1.7-rc.2 \|\| ^0.2.0-rc.1; @deepseek-ai/dsh-llm: ^0.1.2-rc.1 \|\| ^0.1.7-rc.2 \|\| ^0.2.0-rc.1; engines: {"node": "^22.19.0 \|\| >=24.0.0"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "immediately": true, "inje; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-commands, @deepseek-ai/dsh-credentials, @deepseek-ai/dsh-llm; Cordis 配置文件: cordis.patch.yml<br>  - client.js:5496 → Monkey patch / prototype pollution<br>  - scripts/channel-credits-rpc-test.mjs:70 → Monkey patch / prototype pollution<br>  - scripts/standalone-lan-test.mjs:148 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 2155 处, 函数: 12744 个, 比例: 16.9% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: index.js; 发现清理逻辑: vendor/channel-pack/src/trae-auth.ts; 发现清理逻辑: vendor/channel-pack/src/auto-checkin.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - client.js:502 → 读取环境变量配置 (3 处)<br>  - client.js:4084 → 读取浏览器 Cookie/本地存储 (6 处)<br>  - .gitignore:22 → 读取环境变量配置 (1 处)<br>  - index.js:693 → 读取环境变量配置 (3 处)<br>  - scripts/standalone-login-ui-test.mjs:14 → 读取环境变量配置 (5 处)<br>  ... 共 83 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - scripts/prepare-desktop.mjs:20 → 目录遍历 (1 处)<br>  - scripts/speed-stat-test.mjs:161 → 目录遍历 (1 处)<br>  - scripts/release-e2e.mjs:113 → 目录遍历 (2 处)<br>  - scripts/vault-test.mjs:223 → 目录遍历 (1 处)<br>  - scripts/build-manifest.mjs:87 → 目录遍历 (1 处)<br>  ... 共 40 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package-lock.json:29 → 探测到 HTTP(S) 网络请求 (25 处)<br>  - README_EN.md:8 → 探测到 HTTP(S) 网络请求 (15 处)<br>  - client.js:1424 → 探测到 HTTP(S) 网络请求 (17 处)<br>  - client.js:2358 → fetch 网络请求 (1 处)<br>  - client.js:6430 → 浏览器网络 API (1 处)<br>涉及的域名: 127.0.0.1, a.internal, account.minimax.cn, account.xfinfr.com, accounts.google.com, agent.minimax.cn, agnes-ai.com, ai-gateway.vercel.sh, ai.azure.com, ai.dtyg123.dpdns.org (+252 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - README_EN.md:304 → 代理/隧道 (2 处)<br>  - client.js:3489 → 代理/隧道 (1 处)<br>  - scripts/egress-test.mjs:4 → 代理/隧道 (34 处)<br>  - scripts/probes/long-think-truncation.mjs:37 → 挖矿相关 (1 处)<br>  - src/store.js:175 → 代理/隧道 (2 处)<br>  ... 共 10 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - package-lock.json:22 → 敏感凭证读取 (4 处)<br>  - README_EN.md:360 → API Key / Token 读取 (1 处)<br>  - README_EN.md:67 → 敏感凭证读取 (14 处)<br>  - client.js:611 → API Key / Token 读取 (21 处)<br>  - client.js:560 → 敏感凭证读取 (23 处)<br>  ... 共 198 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - index.js:1818 → 修改设置 (2 处)<br>  - scripts/standalone-login-ui-test.mjs:22 → 写入配置文件 (1 处)<br>  - scripts/standalone-login-ui-test.mjs:22 → 写入 DSH 配置 (1 处)<br>  - scripts/ui-preview.mjs:204 → 写入配置文件 (1 处)<br>  - scripts/ui-preview.mjs:204 → 写入 DSH 配置 (1 处)<br>  ... 共 27 处 — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - src/vault-data.js:3 → 超长 base64 字符串 (1 处) |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - scripts/client-lint.mjs:38 → new Function() 任意代码执行 (1 处)<br>  - scripts/channel-model-actions-test.mjs:10 → new Function() 任意代码执行 (1 处)<br>  - scripts/channel-credits-ui-test.mjs:30 → new Function() 任意代码执行 (1 处)<br>  - scripts/ui-preview.mjs:508 → eval() 任意代码执行 (1 处)<br>  - scripts/standalone-frontend-test.mjs:30 → node:vm 任意代码执行 (1 处)<br>  ... 共 21 处 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 8 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - README_EN.md:656 → 定时任务 (1 处)<br>  - client.js:2356 → 定时任务 (24 处)<br>  - index.js:215 → 定时任务 (11 处)<br>  - index.js:75 → 文件读取 (2 处)<br>  - README.md:572 → 定时任务 (1 处)<br>  ... 共 289 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - README_EN.md:65 → 云存储上传 (2 处)<br>  - client.js:771 → 云存储上传 (1 处)<br>  - .github/workflows/build-macos.yml:33 → 云存储上传 (3 处)<br>  - .github/workflows/prepare-release.yml:52 → 云存储上传 (1 处)<br>  - scripts/forward-test.mjs:1001 → 云存储上传 (2 处)<br>  ... 共 12 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 3. repo: 0 deps + 3 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 140323, 注释行: 44985 (32.1%) |
| 4.9 | 具备测试覆盖 | 推荐 | ⚠️  需人工复核 | 未发现测试文件 |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - index.js:2186 → 硬编码敏感信息 (2 处)<br>  - scripts/stream-failure-test.mjs:38 → 硬编码敏感信息 (2 处)<br>  - scripts/channel-credits-rpc-test.mjs:15 → 硬编码敏感信息 (1 处)<br>  - scripts/ui-preview.mjs:222 → 硬编码敏感信息 (2 处)<br>  - scripts/standalone-test.mjs:141 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - README_EN.md:70 → 读取 git 历史 (7 处)<br>  - client.js:625 → 读取 git 历史 (2 处)<br>  - README.md:68 → 读取 git 历史 (7 处)<br>  - .github/workflows/release-sign.yml:43 → 读取 git 历史 (2 处)<br>  - scripts/ui-preview.mjs:47 → 读取 git 历史 (2 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (115 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (47 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - README_EN.md:223 → 要求 root/sudo 权限<br>  - README.md:243 → 要求 root/sudo 权限<br>  - .github/workflows/build-macos.yml:82 → 要求 root/sudo 权限<br>  - scripts/local-optimize-test.mjs:418 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - scripts/standalone-login-ui-test.mjs:50 → 修改系统目录 (8 处)<br>  - scripts/pack-standalone.mjs:91 → 修改系统目录 (5 处)<br>  - scripts/standalone-test.mjs:175 → 创建开机自启/系统服务 (4 处)<br>  - scripts/mint-eac-seal-test.mjs:80 → 修改系统目录 (1 处)<br>  - scripts/standalone-channels-test.mjs:133 → 创建开机自启/系统服务 (2 处)<br>  ... 共 27 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: 隔离 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (8 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 510 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ✅ 通过 | Stars: 22236, Forks: 478, Watchers: 17 — 高 Star 量 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-our-free-model |
| 校验 URL | https://github.com/Ebony-Vinyl/dsh-our-free-model |
| 必查项通过率 | 16/33 (48%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-18 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
