# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge
- **校验时间**: 2026-10-15 03:47:44
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 16 | 13 | 4 |
| 🟡 推荐 | 14 | 5 | 8 | 1 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ⚠️  需人工复核 | 账号注册: 2026-10-10 (4 天前); 公开仓库数: 5; 粉丝数: 1; ⚠️ 账号注册不足 30 天 (4 天) |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 338; 包名: dsh-workbuddy-bridge; 描述: 将 WorkBuddy 桌面 App 包含的模型自动接入 DeepSeek Harness — bring WorkBuddy desktop app mode — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (4): v0.4.0, v0.3.1, v0.3.0, v0.2.0; package.json version: 0.4.0; GitHub Releases (4): v0.4.0, v0.3.1, v0.3.0, v0.2.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.4; @deepseek-ai/dsh-api-remotes: ^0.1.7-rc.1 \|\| ^0.2.0-rc.1; @deepseek-ai/dsh-atomic-write: ^0.1.7-rc.1 \|\| ^0.2.0-rc.1; @deepseek-ai/dsh-attachment: ^0.1.7-rc.1 \|\| ^0.2.0-rc.1; @deepseek-ai/dsh-client-locale: ^0.1.7-rc.1 \|\| ^0.2.0-rc.1 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": ["@deepseek-ai/dsh-api-remotes", "@; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-api-remotes, @deepseek-ai/dsh-atomic-write, @deepseek-ai/dsh-attachment, @deepseek-ai/dsh-client-locale; Cordis 配置文件: cordis.patch.yml<br>  - tests/credit-log.spec.ts:180 → Monkey patch / prototype pollution<br>  - src/llm/credit-log.ts:46 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 164 处, 函数: 2132 个, 比例: 7.7% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: tests/client-identity.spec.ts; 发现清理逻辑: tests/catalog-lifecycle.spec.ts; 发现清理逻辑: tests/variants.spec.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - tsdown.config.ts:22 → 读取环境变量配置 (1 处)<br>  - AGENTS.md:88 → 读取环境变量配置 (1 处)<br>  - scripts/issue-48-forced-fallback-e2e.mjs:90 → 读取环境变量配置 (1 处)<br>  - scripts/check-declaration.mjs:67 → 读取环境变量配置 (1 处)<br>  - tests/auth.spec.ts:263 → 读取环境变量配置 (17 处)<br>  ... 共 15 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - .agents/notes/2026-10-02-profile-install-as-link.md:43 → 深层目录穿越 (2 处)<br>  - .agents/notes/2026-09-29-docs-dir-dual-files-exception.md:8 → 深层目录穿越 (8 处)<br>  - .agents/notes/2026-10-03-card-two-line-template.md:103 → 深层目录穿越 (1 处)<br>  - .agents/notes/2026-09-25-composer-seat-single-occupancy.md:44 → 深层目录穿越 (4 处)<br>  - .agents/notes/2026-10-01-macos-front-half-real-guard.md:10 → 深层目录穿越 (2 处)<br>  ... 共 47 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - scripts/compat-swap.mjs:393 → 开启 shell 模式 (注入风险) (2 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - pnpm-lock.yaml:260 → WebSocket 连接 (3 处)<br>  - pnpm-lock.yaml:260 → 浏览器网络 API (3 处)<br>  - README_en.md:12 → 探测到 HTTP(S) 网络请求 (13 处)<br>  - NOTICE:3 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - AGENTS.md:5 → 探测到 HTTP(S) 网络请求 (3 处)<br>涉及的域名: 127.0.0.1, 127.0.0.1.evil.example, attacker.example, copilot.tencent.com, evil.com, evil.example, evil.example.com, github.com, img.shields.io, localhost (+5 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - tsdown.config.ts:22 → 读取环境变量 API Key/凭证 (1 处)<br>  - pnpm-lock.yaml:220 → 敏感凭证读取 (41 处)<br>  - README_en.md:34 → 敏感凭证读取 (3 处)<br>  - AGENTS.md:88 → 读取环境变量 API Key/凭证 (1 处)<br>  - .github/workflows/ci.yml:26 → 敏感凭证读取 (1 处)<br>  ... 共 97 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - tests/auth.spec.ts:532 → 写入配置文件 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 63 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - .github/workflows/release.yml:204 → 临时文件操作 (3 处)<br>  - scripts/issue-48-forced-fallback-e2e.mjs:42 → 进程控制 (1 处)<br>  - scripts/report-compat-failure.mjs:210 → 进程控制 (2 处)<br>  - scripts/verify-shim-hardening.mjs:183 → 进程控制 (1 处)<br>  - scripts/check-declaration.mjs:218 → 进程控制 (2 处)<br>  ... 共 25 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - pnpm-lock.yaml:212 → 云服务 SDK (可能用于隐蔽上传) (94 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ❌ 不通过 | 总依赖数: 63. repo: 0 deps + 63 devDeps — 依赖过多 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 26534, 注释行: 5939 (22.4%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 39 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - scripts/verify-shim-hardening.mjs:45 → 硬编码敏感信息 (3 处)<br>  - tests/chat-identity-wire.spec.ts:15 → 硬编码敏感信息 (3 处)<br>  - tests/auth.spec.ts:170 → 明文写入敏感信息 (2 处)<br>  - tests/auth.spec.ts:38 → 硬编码敏感信息 (28 处)<br>  - tests/catalog-lifecycle.spec.ts:172 → 明文写入敏感信息 (18 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - AGENTS.md:42 → 读取 git 历史 (1 处)<br>  - .github/workflows/release.yml:97 → 读取 git 历史 (2 处)<br>  - .agents/notes/2026-09-25-repo-rebuild-and-rename.md:12 → 读取 git 历史 (1 处)<br>  - scripts/release-guard.mjs:9 → 读取 git 历史 (2 处)<br>  - docs/README.md:21 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (14 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (1 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - .agents/notes/2026-10-01-macos-front-half-real-guard.md:19 → 修改系统目录 (1 处)<br>  - scripts/issue-48-forced-fallback-e2e.mjs:6 → 修改系统目录 (4 处)<br>  - scripts/report-compat-failure.mjs:1 → 修改系统目录 (1 处)<br>  - scripts/verify-shim-hardening.mjs:1 → 修改系统目录 (1 处)<br>  - scripts/check-declaration.mjs:1 → 修改系统目录 (1 处)<br>  ... 共 11 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: 隔离 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ⚠️  需人工复核 | 未发现临时文件清理逻辑, 需确认 |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 139 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 8, Forks: 2, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-workbuddy-bridge |
| 校验 URL | https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge |
| 必查项通过率 | 16/33 (48%) |
| 推荐项满足率 | 13/14 (约 93%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-15 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
