# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/ding112/MoneyPal
- **校验时间**: 2026-09-09 03:45:12
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 22 | 5 | 6 |
| 🟡 推荐 | 14 | 5 | 9 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2013-03-02 (4938 天前); 公开仓库数: 52; 粉丝数: 23 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ❌ 不通过 | 未找到许可证声明 (package.json 无 license 字段且无 LICENSE 文件) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1049; 包名: moneypal-workspace; 描述: MoneyPal 的 DSH 与 MCP npm 包工作区。 — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ⚠️  需人工复核 | 无 git tag; package.json version: 1.0.0-rc.2; 有版本号但无 git tag / release |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | engines: {"node": ">=22.18"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}}; Cordis 配置文件: cordis.patch.yml<br>  - src/mcp/server.ts:95 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 158 处, 函数: 1084 个, 比例: 14.6% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: test/client-ui.test.ts; 发现清理逻辑: test/balance-host.test.ts; 发现清理逻辑: src/client.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - scripts/release-tarballs.mjs:89 → 读取环境变量配置 (1 处)<br>  - scripts/release-acceptance.mjs:11 → 读取环境变量配置 (3 处)<br>  - scripts/release-promote.mjs:25 → 读取环境变量配置 (1 处)<br>  - test/confirmed-write.test.ts:58 → 读取环境变量配置 (5 处)<br>  - test/dsh-plugin.test.ts:31 → 读取环境变量配置 (16 处)<br>  ... 共 17 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - docs/research/beancount-semantic-parity.md:21 → 深层目录穿越 (6 处)<br>  - docs/research/balance-sidebar-improvements.md:13 → 深层目录穿越 (52 处)<br>  - test/release-gates.test.ts:12 → 深层目录穿越 (15 处)<br>  - test/package-split.test.ts:7 → 深层目录穿越 (2 处)<br>  - test/client-ui.test.ts:286 → 深层目录穿越 (1 处)<br>  ... 共 11 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - scripts/release-promote.mjs:59 → 命令字符串拼接变量 (注入风险) (3 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package-lock.json:20 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - docs/research/beancount-semantic-parity.md:26 → 探测到 HTTP(S) 网络请求 (36 处)<br>  - docs/research/hledger-windows-utf8.md:8 → 探测到 HTTP(S) 网络请求 (35 处)<br>  - docs/research/beancount-v3-runtime-integration.md:11 → 探测到 HTTP(S) 网络请求 (44 处)<br>  - docs/research/beancount-replacement.md:10 → 探测到 HTTP(S) 网络请求 (11 处)<br>涉及的域名: beancount.github.io, code.visualstudio.com, docs.python.org, downloads.haskell.org, ghc.gitlab.haskell.org, github.com, hledger.org, learn.microsoft.com, nodejs.org, pypi.org (+1 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - scripts/release-acceptance.mjs:11 → 读取环境变量 API Key/凭证 (3 处)<br>  - test/dsh-plugin.test.ts:31 → 读取环境变量 API Key/凭证 (16 处)<br>  - test/bridge-process.test.ts:149 → 读取环境变量 API Key/凭证 (2 处)<br>  - test/write-interruption.test.ts:62 → 读取环境变量 API Key/凭证 (3 处)<br>  - test/balance-host.test.ts:16 → 读取环境变量 API Key/凭证 (7 处)<br>  ... 共 9 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 2 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - test/confirmed-write.test.ts:290 → 定时任务 (1 处)<br>  - test/bridge-process.test.ts:176 → 临时文件操作 (1 处)<br>  - test/write-interruption.test.ts:17 → 定时任务 (1 处)<br>  - test/mcp.test.ts:28 → 定时任务 (2 处)<br>  - test/mcp.test.ts:195 → 进程控制 (1 处)<br>  ... 共 8 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ✅ 通过 | 未检测到文件窃取/静默上传模式 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 2. repo: 0 deps + 2 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 7984, 注释行: 240 (3.0%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 21 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ✅ 通过 | 未检测到明文存储敏感信息 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (9 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (1 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - skills/mcp-moneypal/references/bootstrap.md:11 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - test/cli.test.ts:90 → 修改系统目录 (1 处)<br>  - src/main.ts:1 → 修改系统目录 (1 处)<br>  - src/mcp-main.ts:1 → 修改系统目录 (1 处)<br>  - src/finance/bridge.py:1 → 修改系统目录 (1 处) |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: 沙箱, 隔离, workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ⚠️  需人工复核 | 未发现临时文件清理逻辑, 需确认 |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 1 天; 提交总数: 5 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | MoneyPal |
| 校验 URL | https://github.com/ding112/MoneyPal |
| 必查项通过率 | 22/33 (67%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-09-09 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
