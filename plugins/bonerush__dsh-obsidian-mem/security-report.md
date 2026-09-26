# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/bonerush/dsh-obsidian-mem
- **校验时间**: 2026-09-26 04:07:48
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 19 | 9 | 5 |
| 🟡 推荐 | 14 | 6 | 8 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2021-12-20 (1740 天前); 公开仓库数: 15; 粉丝数: 8 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 5511; 包名: dsh-obsidian-mem; 描述: DeepSeek Harness host plugin that keeps project documents and long-term memory a — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - research/obsidian-agent-memory-prior-art.md:278 → 盗版/侵权 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ⚠️  需人工复核 | 无 git tag; package.json version: 0.1.0; 有版本号但无 git tag / release |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.1; @deepseek-ai/dsh-tools: ^0.1.5-rc.1; engines: {"node": ">=22.22.2", "dsh": ">=0.1.5-rc.2"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}}; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-tools; Cordis 配置文件: cordis.patch.yml<br>  - test/smoke/run-smoke.mjs:409 → Monkey patch / prototype pollution<br>  - research/dsh-plugin-api-reference.md:77 → Monkey patch / prototype pollution<br>  - research/dsh-agent-session-events.md:36 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 571 处, 函数: 3153 个, 比例: 18.1% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: lib/capture.js; 发现清理逻辑: lib/index.js; 发现清理逻辑: lib/hooks.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - lib/git.js:197 → 读取环境变量配置 (1 处)<br>  - lib/paths.js:59 → 读取环境变量配置 (1 处)<br>  - lib/debug.js:108 → 读取环境变量配置 (1 处)<br>  - lib/assets.js:84 → 读取环境变量配置 (1 处)<br>  - scripts/verify-pack.mjs:68 → 读取环境变量配置 (1 处)<br>  ... 共 38 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - CHANGELOG.md:725 → 深层目录穿越 (1 处)<br>  - lib/vault.js:114 → 读取用户主目录 (2 处)<br>  - lib/paths.js:59 → 读取用户主目录 (5 处)<br>  - lib/frontmatter.js:636 → 目录遍历 (1 处)<br>  - lib/frontmatter.js:354 → 读取用户主目录 (1 处)<br>  ... 共 34 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package-lock.json:44 → 探测到 HTTP(S) 网络请求 (129 处)<br>  - CHANGELOG.md:4 → 探测到 HTTP(S) 网络请求 (4 处)<br>  - README.zh.md:5 → 探测到 HTTP(S) 网络请求 (5 处)<br>  - README.md:5 → 探测到 HTTP(S) 网络请求 (5 处)<br>  - package.json:16 → 探测到 HTTP(S) 网络请求 (3 处)<br>涉及的域名: 127.0.0.1, awesome-dsh-plugin.com, bugs.openjdk.org, coddingtonbear.github.io, developers.openai.com, direct.mit.edu, docs.basicmemory.com, docs.github.com, esbuild.github.io, eslint.org (+26 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - CHANGELOG.md:179 → 敏感凭证读取 (4 处)<br>  - README.md:337 → API Key / Token 读取 (1 处)<br>  - README.md:333 → 敏感凭证读取 (5 处)<br>  - lib/distill.js:205 → 敏感凭证读取 (2 处)<br>  - lib/paths.js:59 → 读取环境变量 API Key/凭证 (1 处)<br>  ... 共 65 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - test/smoke/run-smoke.mjs:969 → 写入配置文件 (1 处)<br>  - research/dsh-plugin-api/dsh-plugin-config-and-durable-storage.md:963 → 修改设置 (1 处)<br>  - research/dsh-plugin-api/examples/run-demo-counter.mjs:20 → 修改设置 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - research/obsidian-agent-memory-prior-art.md:624 → 连续十六进制转义 (混淆) (1 处) |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - research/dsh-plugin-api-reference.md:438 → eval() 任意代码执行 (2 处)<br>  - research/dsh-plugin-api-reference.md:438 → new Function() 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 10 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - README.zh.md:194 → 临时文件操作 (1 处)<br>  - README.md:207 → 临时文件操作 (1 处)<br>  - lib/vault.js:520 → 文件写入 (1 处)<br>  - lib/vault.js:505 → 文件读取 (3 处)<br>  - lib/registry.js:236 → 文件读取 (1 处)<br>  ... 共 72 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - research/dsh-plugin-api-reference.md:880 → 云存储上传 (2 处)<br>  - research/obsidian-agent-memory-prior-art.md:42 → 云存储上传 (3 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 10. repo: 2 deps + 8 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 50072, 注释行: 11114 (22.2%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 29 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ✅ 通过 | README 中包含数据上报说明: telemetry |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - test/transaction.test.js:1079 → 明文写入敏感信息 (3 处)<br>  - test/transaction.test.js:1085 → 硬编码敏感信息 (4 处)<br>  - test/binding.test.js:235 → 明文写入敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - CHANGELOG.md:194 → 读取 git 历史 (2 处)<br>  - AGENTS.md:150 → 读取 git 历史 (1 处)<br>  - scripts/verify-changelog.mjs:60 → 读取 git 历史 (1 处)<br>  - scripts/check-staged.mjs:8 → 读取 git 历史 (1 处)<br>  - docs/dogfood-results.md:20 → 读取 git 历史 (4 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (15 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (2 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - lib/distill.js:205 → 修改系统目录 (1 处)<br>  - lib/tool-schema.js:22 → 创建开机自启/系统服务 (1 处)<br>  - scripts/verify-changelog.mjs:1 → 修改系统目录 (1 处)<br>  - scripts/install-hooks.mjs:1 → 修改系统目录 (1 处)<br>  - scripts/verify-pack.mjs:1 → 修改系统目录 (1 处)<br>  ... 共 26 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: sandbox |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (8 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 77 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 1, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-obsidian-mem |
| 校验 URL | https://github.com/bonerush/dsh-obsidian-mem |
| 必查项通过率 | 19/33 (58%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-09-26 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
