# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/KouzakiUmi/dsh-antigravity-acp
- **校验时间**: 2026-10-23 03:55:46
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 21 | 8 | 4 |
| 🟡 推荐 | 14 | 6 | 8 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2024-08-15 (798 天前); 公开仓库数: 26; 粉丝数: 6 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 498; 包名: dsh-bundle-antigravity-host; 描述: DeepSeek Harness host bundle that talks to the official Antigravity ACP server o — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (1): v0.1.26; package.json version: 0.1.26 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ~4.0.4 \|\| 4.0.5-alpha.1 \|\| 4.0.5-alpha.2; @deepseek-ai/dsh-llm: >=0.2.0-rc.1 <0.2.1-0 \|\| >=0.2.1-0 <0.3.0-0; @deepseek-ai/dsh-subprocess: >=0.2.0-rc.1 <0.2.1-0 \|\| >=0.2.1-0 <0.3.0-0; @deepseek-ai/dsh-typert-protocol: >=0.2.0-rc.1 <0.2.1-0 \|\| >=0.2.1-0 <0.3.0-0; engines: {"node": ">=22.19"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "inject": ["@deepseek-ai/d; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-llm, @deepseek-ai/dsh-subprocess, @deepseek-ai/dsh-typert-protocol; Cordis 配置文件: cordis.patch.yml<br>  - src/runtime/session-map.ts:67 → Monkey patch / prototype pollution<br>  - src/pool/pooled-adapter.ts:84 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 278 处, 函数: 2494 个, 比例: 11.1% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: tests/quota-remote.test.ts; 发现清理逻辑: tests/client-loader.test.ts; 发现清理逻辑: tests/client-interaction.test.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - tests/hardening.test.ts:129 → 读取凭证文件 (1 处)<br>  - tests/agent-link.test.ts:418 → 读取环境变量配置 (5 处)<br>  - tests/credits.test.ts:37 → 读取环境变量配置 (3 处)<br>  - tests/usability.test.ts:114 → 读取凭证文件 (2 处)<br>  - tests/credentials.test.ts:5 → 读取凭证文件 (2 处)<br>  ... 共 16 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - tests/binary-url.test.ts:48 → 深层目录穿越 (1 处)<br>  - tests/binary-zip-safety.test.ts:120 → 深层目录穿越 (1 处)<br>  - src/runtime/agy-cli.ts:42 → 读取用户主目录 (1 处)<br>  - src/runtime/binary.ts:272 → 读取用户主目录 (2 处)<br>  - src/runtime/credentials.ts:255 → 读取用户主目录 (1 处)<br>  ... 共 6 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - src/index.ts:396 → 进程执行 (1 处)<br>  - src/runtime/agy-cli.ts:325 → 进程执行 (1 处)<br>  - src/protocol/agent-link.ts:642 → 进程执行 (1 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package-lock.json:44 → 探测到 HTTP(S) 网络请求 (254 处)<br>  - README.md:9 → 探测到 HTTP(S) 网络请求 (9 处)<br>  - package.json:18 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - .github/workflows/publish.yml:21 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - assets/banner.svg:1 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: 127.0.0.1, a.test, accounts.google.com, agentclientprotocol.com, alice, ambient, antigravity.google, c.test, daily-cloudcode-pa.googleapis.com, deepseek-harness.github.io (+26 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - tests/proxy-env.test.ts:25 → 代理/隧道 (16 处)<br>  - tests/proxied-fetch.test.ts:67 → 代理/隧道 (4 处)<br>  - tests/usability.test.ts:68 → 代理/隧道 (4 处)<br>  - src/runtime/proxy-env.ts:18 → 代理/隧道 (3 处)<br>  - src/runtime/proxied-fetch.ts:41 → 代理/隧道 (9 处)<br>  ... 共 8 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - scripts/preview-kit.mjs:56 → 敏感凭证读取 (1 处)<br>  - tests/tool-args.test.ts:78 → 敏感凭证读取 (1 处)<br>  - tests/hardening.test.ts:6 → 敏感凭证读取 (9 处)<br>  - tests/proxy-env.test.ts:37 → 敏感凭证读取 (8 处)<br>  - tests/redact.test.ts:49 → API Key / Token 读取 (1 处)<br>  ... 共 39 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 17 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - tests/hardening.test.ts:83 → 定时任务 (3 处)<br>  - tests/session-map.test.ts:86 → 定时任务 (1 处)<br>  - tests/proxied-fetch.test.ts:100 → 开启监听端口 (1 处)<br>  - tests/quota-remote.test.ts:33 → 定时任务 (5 处)<br>  - tests/client-loader.test.ts:221 → 定时任务 (5 处)<br>  ... 共 22 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ✅ 通过 | 未检测到文件窃取/静默上传模式 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 17. repo: 5 deps + 12 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 19925, 注释行: 2457 (12.3%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 37 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - tests/hardening.test.ts:132 → 硬编码敏感信息 (3 处)<br>  - tests/proxied-fetch.test.ts:69 → 硬编码敏感信息 (1 处)<br>  - tests/quota.test.ts:25 → 硬编码敏感信息 (15 处)<br>  - tests/permission-diagnostic.test.ts:14 → 硬编码敏感信息 (2 处)<br>  - tests/settings-control.test.ts:67 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (3 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (1 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - tests/binary-zip-safety.test.ts:115 → 修改系统目录 (2 处)<br>  - tests/agy-cli.test.ts:298 → 修改系统目录 (2 处)<br>  - tests/acp-adapter.test.ts:1418 → 修改系统目录 (1 处) |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: 沙箱, 隔离 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (4 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 25 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-antigravity-acp |
| 校验 URL | https://github.com/KouzakiUmi/dsh-antigravity-acp |
| 必查项通过率 | 21/33 (64%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-23 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
