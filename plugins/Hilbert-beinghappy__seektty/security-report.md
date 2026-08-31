# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/Hilbert-beinghappy/seektty
- **校验时间**: 2026-08-31 04:27:14
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 17 | 12 | 4 |
| 🟡 推荐 | 14 | 7 | 6 | 1 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2024-08-31 (729 天前); 公开仓库数: 20; 粉丝数: 14 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 4836; 包名: seektty; 描述: SeekTTY, a pluggable DeepSeek-colored terminal surface for DeepSeek Harness — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (10): v1.2.5, v1.2.4, v1.2.3, v1.2.2, v1.2.1; package.json version: 1.2.5; GitHub Releases (5): v1.2.5, v1.2.4, v1.2.3, v1.2.2, v1.2.1 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.1; @deepseek-ai/cordis-plugin-include: 1.0.6; @deepseek-ai/cordis-plugin-loader: 1.0.2; @deepseek-ai/dsh-agent-presets: >=0.1.0-rc.6 <=0.1.0-rc.8 \|\| 0.1.1-rc.2; @deepseek-ai/dsh-api-gateway: >=0.1.0-rc.6 <=0.1.0-rc.8 \|\| 0.1.1-rc.2 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "compatibility": {"minimum": "0.1.0-rc.6", "tested": "0.; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/cordis-plugin-include, @deepseek-ai/cordis-plugin-loader, @deepseek-ai/dsh-agent-presets, @deepseek-ai/dsh-api-gateway; Cordis 配置文件: cordis.patch.yml<br>  - src/client/provider-onboarding.ts:325 → Monkey patch / prototype pollution<br>  - src/client/overlays.ts:1227 → Monkey patch / prototype pollution<br>  - src/host/in-process.ts:94 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 546 处, 函数: 9056 个, 比例: 6.0% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: vendor/api-remotes/client/index.js; 发现清理逻辑: vendor/client-runtime/client/slots.js; 发现清理逻辑: vendor/client-runtime/client/index.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .gitignore:7 → 读取环境变量配置 (3 处)<br>  - AGENTS.md:8 → 读取环境变量配置 (1 处)<br>  - cordis.patch.yml:15 → 读取环境变量配置 (1 处)<br>  - src/startup-trace.ts:8 → 读取环境变量配置 (3 处)<br>  - src/bin.ts:46 → 读取环境变量配置 (13 处)<br>  ... 共 38 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - src/bin.ts:62 → 读取用户主目录 (3 处)<br>  - src/client/theme-import.ts:79 → 读取用户主目录 (2 处)<br>  - src/client/workspace-path.ts:25 → 读取用户主目录 (2 处)<br>  - src/client/welcome-logo.ts:5 → 深层目录穿越 (1 处)<br>  - src/compat/client-connection.ts:3 → 深层目录穿越 (2 处)<br>  ... 共 8 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - lib/index.js:10 → 加载 child_process (1 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - docs/鼠标与输入缺陷修复任务书-2026-08-28.md:626 → 开启 shell 模式 (注入风险) (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - THIRD_PARTY_NOTICES.md:3 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - package.json:17 → 探测到 HTTP(S) 网络请求 (4 处)<br>  - README.md:10 → 探测到 HTTP(S) 网络请求 (9 处)<br>  - README.zh.md:10 → 探测到 HTTP(S) 网络请求 (9 处)<br>  - src/version-scan.ts:15 → 探测到 HTTP(S) 网络请求 (2 处)<br>涉及的域名: a, api.github.com, developer.apple.com, docs.deepseek.com, dsh.internal, example, example.com, example.invalid, ghostty.org, github.com (+7 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - pnpm-lock.yaml:105 → 敏感凭证读取 (6 处)<br>  - AGENTS.md:8 → 敏感凭证读取 (1 处)<br>  - cordis.patch.yml:15 → 读取环境变量 API Key/凭证 (1 处)<br>  - package.json:115 → 敏感凭证读取 (3 处)<br>  - README.md:117 → API Key / Token 读取 (1 处)<br>  ... 共 106 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - tests/actions-theme.test.ts:319 → 写入配置文件 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 57 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - src/process-guards.ts:64 → 定时任务 (1 处)<br>  - src/process-guards.ts:151 → 进程控制 (1 处)<br>  - src/client/terminal-background.ts:71 → 定时任务 (1 处)<br>  - src/client/actions.ts:2014 → 定时任务 (3 处)<br>  - src/client/tui-performance.ts:259 → 定时任务 (1 处)<br>  ... 共 49 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - .github/workflows/ci.yml:52 → 云存储上传 (2 处)<br>  - docs/pnpm11-layout-acceptance.md:20 → 云存储上传 (1 处)<br>  - docs/release-v1.2.5-verification.md:107 → 云存储上传 (1 处)<br>  - docs/release-v1.2.4-verification.md:115 → 云存储上传 (1 处)<br>  - lib/index.js:13029 → 云存储上传 (1 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ❌ 不通过 | 总依赖数: 57. repo: 10 deps + 47 devDeps — 依赖过多 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 104856, 注释行: 14683 (14.0%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 134 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - tests/version-scan.test.ts:553 → 硬编码敏感信息 (1 处)<br>  - tests/provider-onboarding.test.ts:217 → 硬编码敏感信息 (1 处)<br>  - tests/installer-output.test.ts:27 → 硬编码敏感信息 (1 处)<br>  - tests/actions-theme.test.ts:319 → 明文写入敏感信息 (1 处)<br>  - tests/pnpm-compat.test.ts:94 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - tests/package-contract.test.ts:150 → 读取 git 历史 (1 处)<br>  - .github/workflows/ci.yml:34 → 读取 git 历史 (1 处)<br>  - docs/任务书C-dsh版本适配与自动更新.md:31 → 读取 git 历史 (1 处)<br>  - docs/issue-163-overlay-description-verification.md:31 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (7 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (5 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - src/bin.ts:1 → 修改系统目录 (1 处)<br>  - tests/version-scan.test.ts:556 → 修改系统目录 (2 处)<br>  - scripts/tui-perf-harness.mjs:1 → 修改系统目录 (1 处)<br>  - scripts/bump-dsh.mjs:1 → 修改系统目录 (1 处)<br>  - scripts/stock-dsh-cycle.mjs:1 → 修改系统目录 (1 处)<br>  ... 共 13 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (6 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 227 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ✅ 通过 | Stars: 126, Forks: 8, Watchers: 2 — 高 Star 量 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | seektty |
| 校验 URL | https://github.com/Hilbert-beinghappy/seektty |
| 必查项通过率 | 17/33 (52%) |
| 推荐项满足率 | 13/14 (约 93%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-31 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
