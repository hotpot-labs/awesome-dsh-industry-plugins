# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/Anionex/dsh-vision-toolkit
- **校验时间**: 2026-08-23 14:26:30
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 15 | 12 | 6 |
| 🟡 推荐 | 14 | 8 | 6 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2023-01-20 (1311 天前); 公开仓库数: 86; 粉丝数: 293 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 3250; 包名: @anionex/dsh-vision-toolkit; 描述: DeepSeek Harness-native integration for agent-vision-toolkit: image Q&A, OCR, gr — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - README.md:33 → 盗版/侵权 (1 处)<br>  - docs/aihubmix-gemini-vision.md:45 → 盗版/侵权 (1 处)<br>  - workers/moondream-openai-proxy/worker-configuration.d.ts:1894 → 盗版/侵权 (4 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (20): v0.1.38, v0.1.37, v0.1.36, v0.1.35, v0.1.34; package.json version: 0.1.38; GitHub Releases (5): v0.1.38, v0.1.37, v0.1.36, v0.1.35, v0.1.34 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/dsh-agent: ^0.1.0-rc.6; @deepseek-ai/dsh-api-remotes: ^0.1.0-rc.6; @deepseek-ai/dsh-attachment: ^0.1.0-rc.6; @deepseek-ai/dsh-client-locale: ^0.1.0-rc.6; @deepseek-ai/dsh-client-runtime: ^0.1.0-rc.6 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": ["@deepseek-ai/dsh-api-remotes", "@; Cordis/DSH 依赖: @deepseek-ai/dsh-agent, @deepseek-ai/dsh-api-remotes, @deepseek-ai/dsh-attachment, @deepseek-ai/dsh-client-locale, @deepseek-ai/dsh-client-runtime; Cordis 配置文件: cordis.patch.yml<br>  - tests/profile-install.e2e.spec.ts:265 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 743 处, 函数: 2954 个, 比例: 25.2% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: src/index.ts; 发现清理逻辑: src/runtime.ts; 发现清理逻辑: src/plugin-update.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - CONTRIBUTING.md:46 → 读取环境变量配置 (1 处)<br>  - CHANGELOG.md:322 → 读取环境变量配置 (1 处)<br>  - src/paste-images.ts:1 → 读取浏览器 Cookie/本地存储 (1 处)<br>  - src/paths.ts:45 → 读取环境变量配置 (1 处)<br>  - src/runtime.ts:710 → 读取环境变量配置 (2 处)<br>  ... 共 23 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - src/paths.ts:37 → 读取用户主目录 (2 处)<br>  - src/plugin-update.ts:459 → 读取用户主目录 (2 处)<br>  - src/runtime-install.ts:655 → 读取用户主目录 (3 处)<br>  - tests/paths.spec.ts:29 → 读取用户主目录 (1 处)<br>  - tests/paste-images.spec.ts:81 → 深层目录穿越 (2 处)<br>  ... 共 10 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - src/plugin-update.ts:839 → 进程执行 (1 处)<br>  - src/upstream.ts:776 → 进程执行 (3 处)<br>  - src/runtime-install.ts:134 → 进程执行 (1 处)<br>  - tests/vision-prompt-guard.spec.ts:58 → Python subprocess (1 处)<br>  - tests/html-screenshot-guard.spec.ts:50 → Python subprocess (1 处)<br>  ... 共 8 处<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - tests/ui-restoration-example.spec.ts:25 → 开启 shell 模式 (注入风险) (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - FUNDING.md:5 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - index.html:10 → 探测到 HTTP(S) 网络请求 (14 处)<br>  - SUPPORT.md:8 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - package.json:22 → 探测到 HTTP(S) 网络请求 (5 处)<br>  - README.md:9 → 探测到 HTTP(S) 网络请求 (30 处)<br>涉及的域名: 127.0.0.1, agent-vision.anionex.me, agentskills.io, aihubmix.com, alice, anionex.me, api.example.com, api.github.com, api.groq.com, api.inferera.com (+34 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - workers/moondream-openai-proxy/worker-configuration.d.ts:10326 → 挖矿相关 (2 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - pnpm-lock.yaml:47 → 敏感凭证读取 (6 处)<br>  - index.html:543 → 敏感凭证读取 (5 处)<br>  - tsconfig.client.json:32 → 敏感凭证读取 (2 处)<br>  - SECURITY.md:22 → 敏感凭证读取 (3 处)<br>  - package.json:115 → 敏感凭证读取 (1 处)<br>  ... 共 122 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - src/runtime-install.ts:729 → 写入配置文件 (1 处)<br>  - tests/profile-install.e2e.spec.ts:267 → 写入配置文件 (1 处)<br>  - lib/runtime-install.js:581 → 写入配置文件 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 40 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - CHANGELOG.md:121 → 临时文件操作 (2 处)<br>  - src/paths.ts:47 → 临时文件操作 (5 处)<br>  - src/runtime.ts:123 → 定时任务 (1 处)<br>  - src/plugin-update.ts:162 → 定时任务 (9 处)<br>  - src/plugin-update.ts:166 → 进程控制 (10 处)<br>  ... 共 42 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - SECURITY.md:32 → 云存储上传 (2 处)<br>  - src/paste-images.ts:56 → 云存储上传 (4 处)<br>  - src/index.ts:101 → 云存储上传 (1 处)<br>  - src/client/paste-images.tsx:605 → 云存储上传 (2 处)<br>  - src/client/index.tsx:41 → 云存储上传 (1 处)<br>  ... 共 21 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 17. repo: 4 deps + 13 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 40479, 注释行: 2761 (6.8%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 33 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - README.md:282 → 硬编码敏感信息 (1 处)<br>  - README.zh.md:280 → 硬编码敏感信息 (1 处)<br>  - CHANGELOG.md:197 → 硬编码敏感信息 (3 处)<br>  - src/plugin-update.ts:897 → 明文写入敏感信息 (1 处)<br>  - src/upstream.ts:751 → 从环境变量获取敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - CONTRIBUTING.md:54 → 读取 git 历史 (1 处)<br>  - .github/PULL_REQUEST_TEMPLATE.md:17 → 读取 git 历史 (1 处)<br>  - .github/workflows/ci.yml:92 → 读取 git 历史 (2 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (23 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (1 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - tests/html-screenshot-guard.spec.ts:31 → 修改系统目录 (1 处)<br>  - tests/plugin-update.spec.ts:29 → 修改系统目录 (5 处)<br>  - tests/upstream.spec.ts:28 → 修改系统目录 (1 处)<br>  - tests/fixtures/upstream/bin/glance:1 → 修改系统目录 (1 处)<br>  - tests/fixtures/upstream/bin/crop:1 → 修改系统目录 (1 处)<br>  ... 共 23 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (13 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 1 天; 提交总数: 282 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ✅ 通过 | Stars: 813, Forks: 34, Watchers: 2 — 高 Star 量 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-vision-toolkit |
| 校验 URL | https://github.com/Anionex/dsh-vision-toolkit |
| 必查项通过率 | 15/33 (45%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-23 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
