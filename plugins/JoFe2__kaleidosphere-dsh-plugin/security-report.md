# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/JoFe2/kaleidosphere-dsh-plugin
- **校验时间**: 2026-08-23 16:34:02
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 20 | 8 | 5 |
| 🟡 推荐 | 14 | 8 | 6 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2023-11-27 (1000 天前); 公开仓库数: 4; 粉丝数: 0 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: Apache-2.0 (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 941; 包名: kaleidosphere-dsh-plugin; 描述: Native KaleidoSphere database-analysis tools for DeepSeek Harness — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - third_party/oracledb-7.0.1/lib/aqQueue.js:117 → 盗版/侵权 (3 处)<br>  - third_party/oracledb-7.0.1/lib/aqMessage.js:79 → 盗版/侵权 (4 处)<br>  - third_party/oracledb-7.0.1/lib/impl/aqMessage.js:70 → 盗版/侵权 (4 处)<br>  - third_party/oracledb-7.0.1/lib/thin/aq.js:352 → 盗版/侵权 (9 处)<br>  - third_party/oracledb-7.0.1/lib/thin/protocol/constants.js:780 → 盗版/侵权 (1 处)<br>  ... 共 6 处 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (3): v0.1.0-preview.3, v0.1.0-preview.2, v0.1.0-preview.1; package.json version: 0.1.0-preview.3; GitHub Releases (3): v0.1.0-preview.3, v0.1.0-preview.2, v0.1.0-preview.1 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/dsh-tools: 0.1.0-rc.8; engines: {"node": "^22.19.0 \|\| >=24.0.0"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ✅ 通过 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}}; Cordis/DSH 依赖: @deepseek-ai/dsh-tools; Cordis 配置文件: cordis.patch.yml |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 213 处, 函数: 1204 个, 比例: 17.7% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: index.js; 发现清理逻辑: third_party/oracledb-7.0.1/lib/connection.js; 发现清理逻辑: test/runtime.test.mjs |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - third_party/oracledb-7.0.1/examples/dbconfig.js:76 → 读取环境变量配置 (12 处)<br>  - third_party/oracledb-7.0.1/examples/example.js:47 → 读取环境变量配置 (2 处)<br>  - third_party/oracledb-7.0.1/plugins/configProviders/awsCommon.js:47 → 读取环境变量配置 (8 处)<br>  - third_party/oracledb-7.0.1/lib/poolStatistics.js:83 → 读取环境变量配置 (1 处)<br>  - third_party/oracledb-7.0.1/lib/impl/parserHelpers.js:286 → 读取环境变量配置 (2 处)<br>  ... 共 12 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - third_party/oracledb-7.0.1/package/prunebinaries.js:53 → 目录遍历 (1 处)<br>  - third_party/oracledb-7.0.1/lib/impl/datahandlers/buffer.js:31 → 深层目录穿越 (3 处)<br>  - third_party/oracledb-7.0.1/lib/impl/datahandlers/oson.js:32 → 深层目录穿越 (3 处)<br>  - third_party/oracledb-7.0.1/lib/impl/datahandlers/constants.js:29 → 深层目录穿越 (1 处)<br>  - third_party/oracledb-7.0.1/lib/impl/datahandlers/vector.js:32 → 深层目录穿越 (2 处)<br>  ... 共 30 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - THIRD_PARTY_MANIFEST.json:7 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - package.json:51 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - CONTRIBUTING.md:24 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - package-lock.json:23 → 探测到 HTTP(S) 网络请求 (113 处)<br>  - VENDORED_MANIFEST.json:3 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: 127.0.0.1, blogs.oracle.com, docs.oracle.com, example.internal, feross.org, github.com, img.shields.io, join.slack.com, ks.example.com, learn.microsoft.com (+14 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - LICENSE:149 → 挖矿相关 (1 处)<br>  - third_party/oracledb-7.0.1/LICENSE.txt:204 → 挖矿相关 (1 处)<br>  - third_party/oracledb-7.0.1/lib/impl/connection.js:139 → 挖矿相关 (1 处)<br>  - third_party/oracledb-7.0.1/lib/impl/datahandlers/oson.js:51 → 挖矿相关 (1 处)<br>  - third_party/oracledb-7.0.1/lib/thin/statement.js:403 → 挖矿相关 (3 处)<br>  ... 共 6 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - SECURITY.md:20 → 敏感凭证读取 (4 处)<br>  - CONTRIBUTING.md:52 → 敏感凭证读取 (2 处)<br>  - README.md:49 → 敏感凭证读取 (7 处)<br>  - examples/live-mssql.patch.yml:18 → 敏感凭证读取 (2 处)<br>  - examples/live-oracle.patch.yml:18 → 敏感凭证读取 (2 处)<br>  ... 共 60 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 2 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - third_party/oracledb-7.0.1/plugins/configProviders/ociobject/index.js:109 → 文件读取 (1 处)<br>  - third_party/oracledb-7.0.1/plugins/token/extensionOci/index.js:159 → 文件读取 (1 处)<br>  - third_party/oracledb-7.0.1/package/install.js:99 → 进程控制 (1 处)<br>  - third_party/oracledb-7.0.1/lib/connection.js:2101 → 定时任务 (1 处)<br>  - third_party/oracledb-7.0.1/lib/pool.js:262 → 定时任务 (2 处)<br>  ... 共 29 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - third_party/oracledb-7.0.1/plugins/configProviders/awsCommon.js:39 → 云服务 SDK (可能用于隐蔽上传) (1 处)<br>  - third_party/oracledb-7.0.1/plugins/configProviders/awss3/index.js:50 → 云服务 SDK (可能用于隐蔽上传) (1 处)<br>  - third_party/oracledb-7.0.1/plugins/configProviders/awssecretsmanager/index.js:50 → 云服务 SDK (可能用于隐蔽上传) (1 处)<br>  - third_party/oracledb-7.0.1/package/README.md:30 → 云存储上传 (2 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 1. repo: 1 deps + 0 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 44941, 注释行: 10352 (23.0%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - README.md:52 → 硬编码敏感信息 (1 处)<br>  - test/capability-readback-receipt.test.mjs:173 → 硬编码敏感信息 (1 处)<br>  - scripts/test-dsh-agent-rc8.sh:75 → 硬编码敏感信息 (2 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (12 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (7 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - third_party/oracledb-7.0.1/examples/dbconfig.js:53 → 修改系统目录 (1 处)<br>  - third_party/oracledb-7.0.1/lib/util.js:138 → 修改系统目录 (1 处)<br>  - test/capability-readback-receipt.test.mjs:174 → 修改系统目录 (1 处)<br>  - scripts/ks-external-stub.mjs:1 → 修改系统目录 (1 处)<br>  - scripts/dsh-agent-stub.mjs:1 → 修改系统目录 (1 处)<br>  ... 共 8 处 |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (4 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 19 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 1, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | kaleidosphere-dsh-plugin |
| 校验 URL | https://github.com/JoFe2/kaleidosphere-dsh-plugin |
| 必查项通过率 | 20/33 (61%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-23 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
