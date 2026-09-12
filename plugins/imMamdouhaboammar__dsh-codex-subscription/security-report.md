# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/imMamdouhaboammar/dsh-codex-subscription
- **校验时间**: 2026-09-12 03:50:59
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 18 | 9 | 6 |
| 🟡 推荐 | 14 | 6 | 8 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2019-12-15 (2462 天前); 公开仓库数: 84; 粉丝数: 28 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1970; 包名: dsh-codex-subscription-en; 描述: Use ChatGPT and Codex subscriptions in DeepSeek Harness with OAuth, quota, safe  — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - tests/reset-credits.test.mjs:137 → 盗版/侵权 (1 处)<br>  - lib/index.js:2517 → 盗版/侵权 (7 处)<br>  - src/usage.js:107 → 盗版/侵权 (5 处)<br>  - src/reset-credits.js:37 → 盗版/侵权 (2 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (1): v1.0.0; package.json version: 1.0.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/dsh-home-paths: 0.1.1-rc.2; @deepseek-ai/cordis: 4.0.1 \|\| 4.0.2; @deepseek-ai/dsh-api-remotes: 0.1.0-rc.6 \|\| 0.1.0-rc.7 \|\| 0.1.0-rc.8 \|\| 0.1.1-rc.1 \|\| 0.1.1-rc.2 \|\| 0.1.2-alpha.2 \|\| 0.1.2-alpha.3 \|\| 0.1.2-alpha.4 \|\| 0.1.2-alpha.5 \|\| 0.1.2-rc.1; @deepseek-ai/dsh-client-connection: 0.1.0-rc.6 \|\| 0.1.0-rc.7 \|\| 0.1.0-rc.8 \|\| 0.1.1-rc.1 \|\| 0.1.1-rc.2 \|\| 0.1.2-alpha.2 \|\| 0.1.2-alpha.3 \|\| 0.1.2-alpha.4 \|\| 0.1.2-alpha.5 \|\| 0.1.2-rc.1; @deepseek-ai/dsh-client-locale: 0.1.0-rc.6 \|\| 0.1.0-rc.7 \|\| 0.1.0-rc.8 \|\| 0.1.1-rc.1 \|\| 0.1.1-rc.2 \|\| 0.1.2-alpha.2 \|\| 0.1.2-alpha.3 \|\| 0.1.2-alpha.4 \|\| 0.1.2-alpha.5 \|\| 0.1.2-rc.1 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ✅ 通过 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": ["@deepseek-ai/dsh-api-remotes", "@; Cordis/DSH 依赖: @deepseek-ai/dsh-home-paths, @deepseek-ai/cordis, @deepseek-ai/dsh-api-remotes, @deepseek-ai/dsh-client-connection, @deepseek-ai/dsh-client-locale; Cordis 配置文件: cordis.patch.yml |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 247 处, 函数: 1950 个, 比例: 12.7% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: tests/client-contract.test.mjs; 发现清理逻辑: tests/account-status-controller.test.mjs; 发现清理逻辑: tests/image-original-store.test.mjs |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - tsdown.config.mjs:37 → 读取环境变量配置 (2 处)<br>  - tests/powershell-manager.test.mjs:16 → 读取环境变量配置 (21 处)<br>  - lib/index.js:967 → 读取环境变量配置 (4 处)<br>  - scripts/ci-change-plan.mjs:91 → 读取环境变量配置 (3 处)<br>  - src/oauth-network.js:45 → 读取环境变量配置 (4 处)<br>  ... 共 6 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - lib/client.js:32 → 深层目录穿越 (1 处) — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - THIRD_PARTY_NOTICES.md:7 → 探测到 HTTP(S) 网络请求 (8 处)<br>  - THIRD_PARTY_NOTICES.md:8 → WebSocket 连接 (1 处)<br>  - THIRD_PARTY_NOTICES.md:8 → 浏览器网络 API (1 处)<br>  - README.en.md:5 → 探测到 HTTP(S) 网络请求 (23 处)<br>  - SECURITY.md:11 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: 127.0.0.1, api.openai.com, auth.openai.com, auth.openai.com.evil.example, chatgpt.com, codex.example, dsh.example, example.com, example.test, fallback.example (+7 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - tests/oauth-network.test.mjs:15 → 代理/隧道 (1 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - tsdown.config.mjs:37 → 读取环境变量 API Key/凭证 (2 处)<br>  - tsdown.config.mjs:7 → 敏感凭证读取 (1 处)<br>  - THIRD_PARTY_NOTICES.md:7 → 敏感凭证读取 (1 处)<br>  - README.en.md:43 → 敏感凭证读取 (4 处)<br>  - SECURITY.md:23 → API Key / Token 读取 (1 处)<br>  ... 共 68 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 26 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - tests/auth-security.test.mjs:149 → 定时任务 (4 处)<br>  - tests/account-status-controller.test.mjs:65 → 定时任务 (2 处)<br>  - tests/powershell-manager.test.mjs:630 → 开启监听端口 (1 处)<br>  - tests/powershell-manager.test.mjs:131 → 文件写入 (3 处)<br>  - tests/powershell-manager.test.mjs:80 → 文件读取 (5 处)<br>  ... 共 12 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - pnpm-lock.yaml:115 → 云服务 SDK (可能用于隐蔽上传) (101 处)<br>  - tests/release-notes.test.mjs:104 → 云存储上传 (2 处)<br>  - tests/release-contract.test.mjs:289 → 云存储上传 (3 处)<br>  - .github/workflows/publish.yml:133 → 云存储上传 (3 处)<br>  - .github/workflows/ci.yml:72 → 云存储上传 (1 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 26. repo: 2 deps + 24 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 18972, 注释行: 321 (1.7%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - tests/reset-credits.test.mjs:382 → 硬编码敏感信息 (1 处)<br>  - tests/model-catalog.test.mjs:53 → 硬编码敏感信息 (4 处)<br>  - tests/usage.test.mjs:52 → 硬编码敏感信息 (6 处)<br>  - tests/codex-images.test.mjs:75 → 硬编码敏感信息 (1 处)<br>  - tests/codex-search.test.mjs:41 → 硬编码敏感信息 (4 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - tests/release-contract.test.mjs:263 → 读取 git 历史 (3 处)<br>  - .github/workflows/publish.yml:125 → 读取 git 历史 (3 处)<br>  - .github/workflows/upstream-compatibility.yml:113 → 读取 git 历史 (3 处)<br>  - .github/workflows/ci.yml:65 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (3 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (5 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - docs/assets/social-preview.png:6064 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - lib/index.js:1011 → 修改系统目录 (1 处)<br>  - src/oauth-network.js:77 → 修改系统目录 (1 处) |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (2 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 4 天; 提交总数: 15 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG, 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-codex-subscription |
| 校验 URL | https://github.com/imMamdouhaboammar/dsh-codex-subscription |
| 必查项通过率 | 18/33 (55%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-09-12 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
