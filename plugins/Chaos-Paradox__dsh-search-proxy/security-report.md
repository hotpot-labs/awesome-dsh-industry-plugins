# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/Chaos-Paradox/dsh-search-proxy
- **校验时间**: 2026-11-04 05:24:27
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 16 | 12 | 5 |
| 🟡 推荐 | 14 | 6 | 7 | 1 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2020-10-09 (2216 天前); 公开仓库数: 12; 粉丝数: 2 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 337; 包名: dsh-search-proxy; 描述: SearXNG web search and optional DSH process proxy, with profile-scoped settings  — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (6): v0.5.0, v0.4.1, v0.3.1, v0.3.0, v0.2.0; package.json version: 0.5.0; GitHub Releases (5): v0.5.0, v0.4.1, v0.3.1, v0.3.0, v0.2.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ~4.0.5-alpha.1; @deepseek-ai/dsh-credentials: >=0.2.1-alpha.2 <0.3.0; @deepseek-ai/dsh-http-proxy: >=0.2.1-alpha.2 <0.3.0; @deepseek-ai/dsh-launch-environment: >=0.2.1-alpha.2 <0.3.0; @deepseek-ai/dsh-typert-protocol: >=0.2.1-alpha.2 <0.3.0 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ✅ 通过 | dsh 配置: {"client": {"inject": ["@deepseek-ai/dsh-client-locale", "@deepseek-ai/dsh-client-ui-settings", "@de; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-credentials, @deepseek-ai/dsh-http-proxy, @deepseek-ai/dsh-launch-environment, @deepseek-ai/dsh-typert-protocol; Cordis 配置文件: cordis.patch.yml |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 164 处, 函数: 1193 个, 比例: 13.7% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: lib/index.js; 发现清理逻辑: lib/client.js; 发现清理逻辑: lib/client/searxng-search-card-controller.d.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - tsdown.config.ts:69 → 读取环境变量配置 (7 处)<br>  - docs/configuration.md:28 → 读取环境变量配置 (1 处)<br>  - docs/proxy-risk.md:35 → 读取环境变量配置 (1 处)<br>  - docs/proxy-risk.zh.md:34 → 读取环境变量配置 (1 处)<br>  - docs/configuration.zh.md:28 → 读取环境变量配置 (1 处)<br>  ... 共 21 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - lib/index.js:57 → 读取用户主目录 (3 处)<br>  - benchmarks/e2e-comparison.mjs:69 → 读取用户主目录 (1 处)<br>  - benchmarks/quality-comparison.mjs:34 → 读取用户主目录 (1 处)<br>  - src/runtime-log.ts:16 → 读取用户主目录 (3 处)<br>  - tests/runtime-log.spec.ts:8 → 读取用户主目录 (2 处) — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - lib/index.js:1150 → 进程执行 (1 处)<br>  - src/managed-runtime.ts:156 → 进程执行 (1 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package.json:150 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - README.md:5 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - README.zh.md:5 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - docs/reference.zh.md:38 → 探测到 HTTP(S) 网络请求 (13 处)<br>  - docs/configuration.md:18 → 探测到 HTTP(S) 网络请求 (2 处)<br>涉及的域名: 127.0.0.1, a.test, abcnews.com, ably.com, agupubs.onlinelibrary.wiley.com, akp.gov.kh, antfu.me, anthromuseum.missouri.edu, api-docs.deepseek.com, api.deepseek.com (+270 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - benchmarks/results/e2e-2026-10-07T01-09-52-970Z.json:22 → 挖矿相关 (1 处)<br>  - benchmarks/results/e2e-2026-10-08T15-59-45-721Z.json:23 → 挖矿相关 (2 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - package.json:71 → 敏感凭证读取 (2 处)<br>  - tsdown.config.ts:69 → 读取环境变量 API Key/凭证 (5 处)<br>  - tsdown.config.ts:27 → 敏感凭证读取 (1 处)<br>  - pnpm-lock.yaml:60 → 敏感凭证读取 (6 处)<br>  - pnpm-workspace.yaml:38 → 敏感凭证读取 (1 处)<br>  ... 共 99 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - lib/index.js:1237 → 写入配置文件 (1 处)<br>  - benchmarks/e2e-comparison.mjs:173 → 写入配置文件 (1 处)<br>  - benchmarks/quality-comparison.mjs:212 → 写入配置文件 (1 处)<br>  - src/managed-runtime.ts:201 → 写入配置文件 (1 处)<br>  - tests/host-composition.mjs:125 → 修改设置 (14 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - tests/build-decorators.spec.ts:9 → new Function() 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 58 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - docs/validation-2026-10-19-route-restore.md:35 → 临时文件操作 (3 处)<br>  - docs/configuration.md:42 → 临时文件操作 (1 处)<br>  - docs/host-compatibility.zh.md:56 → 临时文件操作 (8 处)<br>  - docs/host-compatibility.md:49 → 临时文件操作 (8 处)<br>  - docs/configuration.zh.md:42 → 临时文件操作 (1 处)<br>  ... 共 18 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - pnpm-lock.yaml:328 → 云存储上传 (4 处)<br>  - pnpm-workspace.yaml:19 → 云存储上传 (1 处)<br>  - benchmarks/results/e2e-2026-10-07T01-09-52-970Z.json:115 → 云存储上传 (1 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ❌ 不通过 | 总依赖数: 58. repo: 4 deps + 54 devDeps — 依赖过多 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 12459, 注释行: 1208 (9.7%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 21 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - lib/index.js:1233 → 明文写入敏感信息 (2 处)<br>  - benchmarks/e2e-comparison.mjs:71 → 硬编码敏感信息 (1 处)<br>  - benchmarks/quality-comparison.mjs:36 → 硬编码敏感信息 (1 处)<br>  - src/managed-runtime.ts:198 → 明文写入敏感信息 (2 处)<br>  - tests/proxy-panel.client.spec.tsx:85 → 硬编码敏感信息 (3 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - docs/validation-2026-10-10.md:19 → 读取 git 历史 (1 处)<br>  - docs/validation-managed-2026-10-10.md:12 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (12 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (7 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - README.md:24 → 创建开机自启/系统服务 (1 处)<br>  - docs/reference.zh.md:67 → 修改系统目录 (1 处)<br>  - docs/reference.md:67 → 修改系统目录 (1 处)<br>  - docs/reference.md:137 → 创建开机自启/系统服务 (2 处)<br>  - docs/validation-2026-10-10.md:9 → 创建开机自启/系统服务 (1 处)<br>  ... 共 17 处 |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (3 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 8 天; 提交总数: 27 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG, 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 2, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-search-proxy |
| 校验 URL | https://github.com/Chaos-Paradox/dsh-search-proxy |
| 必查项通过率 | 16/33 (48%) |
| 推荐项满足率 | 13/14 (约 93%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-11-04 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
