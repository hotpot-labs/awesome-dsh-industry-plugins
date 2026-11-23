# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/CM-Silence/dsh-mo-image
- **校验时间**: 2026-11-23 06:27:47
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
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: master |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2021-10-18 (1861 天前); 公开仓库数: 16; 粉丝数: 2 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 3589; 包名: dsh-mo-image; 描述: DSH plugin: generate and edit images with model-aware prompt guidance over an Op — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (10): v1.0.3, v1.0.2, v1.0.1, v1.0.0, v0.7.0; package.json version: 1.0.3; GitHub Releases (5): v1.0.3, v1.0.2, v1.0.1, v1.0.0, v0.7.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ~4.0.5; engines: {"dsh": ">=0.2.1-rc.2"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "inject": ["@deepseek-ai/d; Cordis/DSH 依赖: @deepseek-ai/cordis; Cordis 配置文件: cordis.patch.yml<br>  - test/async-adapter-hygiene.test.mjs:121 → Monkey patch / prototype pollution<br>  - lib/field-templates.js:86 → Monkey patch / prototype pollution<br>  - lib/adapters.js:548 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 464 处, 函数: 5809 个, 比例: 8.0% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: lib/update-service.js; 发现清理逻辑: lib/index.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - test/generate-credential.test.mjs:30 → 读取环境变量配置 (4 处)<br>  - test/two-step-flow.test.mjs:58 → 读取环境变量配置 (4 处)<br>  - test/edit-flow.test.mjs:27 → 读取环境变量配置 (1 处)<br>  - test/provider-operations.test.mjs:214 → 读取环境变量配置 (4 处)<br>  - test/config-route.test.mjs:40 → 读取环境变量配置 (16 处)<br>  ... 共 29 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - lib/index.js:56 → 读取用户主目录 (1 处) — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package.json:34 → 探测到 HTTP(S) 网络请求 (4 处)<br>  - LICENSE:33 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - README.md:3 → 探测到 HTTP(S) 网络请求 (43 处)<br>  - README.md:670 → WebSocket 连接 (1 处)<br>  - README.md:670 → 浏览器网络 API (1 处)<br>涉及的域名: 10.0.0.8, 11.0.0.1, 127.0.0.1, 127.1.2.3, 169.254.1.1, 172.15.0.1, 172.16.0.9, 172.31.255.254, 172.32.0.1, 192.168.1.5 (+142 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - test/async-output-profiles.test.mjs:66 → 代理/隧道 (1 处)<br>  - test/proxy.test.mjs:7 → 代理/隧道 (1 处)<br>  - lib/net.js:5 → 代理/隧道 (2 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - README.md:262 → API Key / Token 读取 (13 处)<br>  - README.md:244 → 敏感凭证读取 (4 处)<br>  - locale/messages.csv:37 → API Key / Token 读取 (18 处)<br>  - locale/messages.csv:45 → 敏感凭证读取 (15 处)<br>  - test/status.test.mjs:7 → API Key / Token 读取 (2 处)<br>  ... 共 121 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - test/generate-credential.test.mjs:18 → 写入配置文件 (1 处)<br>  - test/two-step-flow.test.mjs:31 → 写入配置文件 (12 处)<br>  - test/config-store.test.mjs:194 → 写入配置文件 (1 处)<br>  - test/edit-flow.test.mjs:14 → 写入配置文件 (1 处)<br>  - test/config-route.test.mjs:30 → 写入配置文件 (2 处)<br>  ... 共 22 处 — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - test/client-auto-row.test.mjs:73 → node:vm 任意代码执行 (1 处)<br>  - test/client-update.test.mjs:87 → node:vm 任意代码执行 (1 处)<br>  - test/client-protocol-dropdown.test.mjs:94 → node:vm 任意代码执行 (1 处)<br>  - test/client-model-catalog.test.mjs:99 → node:vm 任意代码执行 (2 处)<br>  - test/client-subagent-seat.test.mjs:55 → node:vm 任意代码执行 (1 处)<br>  ... 共 13 处 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 1 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - test/generate-credential.test.mjs:124 → 开启监听端口 (1 处)<br>  - test/generate-credential.test.mjs:12 → 临时文件操作 (1 处)<br>  - test/two-step-flow.test.mjs:339 → 定时任务 (4 处)<br>  - test/two-step-flow.test.mjs:28 → 临时文件操作 (2 处)<br>  - test/config-store.test.mjs:177 → 临时文件操作 (1 处)<br>  ... 共 57 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - README.md:281 → multipart 上传 (10 处)<br>  - test/image-template.test.mjs:4 → multipart 上传 (30 处)<br>  - test/param-injection.test.mjs:66 → multipart 上传 (2 处)<br>  - test/protocol-merge.test.mjs:71 → multipart 上传 (3 处)<br>  - test/config-store.test.mjs:164 → multipart 上传 (5 处)<br>  ... 共 41 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 无第三方依赖 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 53712, 注释行: 5160 (9.6%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - test/config-store.test.mjs:194 → 明文写入敏感信息 (1 处)<br>  - test/config-route.test.mjs:30 → 明文写入敏感信息 (1 处)<br>  - lib/adapter-kit.js:526 → 硬编码敏感信息 (1 处)<br>  - lib/index.js:147 → 明文写入敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - test/adapter-body-regression.test.mjs:78 → 读取 git 历史 (2 处)<br>  - scripts/release.mjs:119 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (3 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (1 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - test/model-options-config.test.mjs:243 → 修改系统目录 (1 处)<br>  - scripts/release.mjs:1 → 修改系统目录 (1 处)<br>  - scripts/build-locales.mjs:1 → 修改系统目录 (1 处) |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: 隔离 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (1 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 255 |
| 7.2 | 未标记停止维护 | 必查 | ❌ 不通过 | 文档中发现弃用标记: 不再支持 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 20, Forks: 0, Watchers: 0 — 有一定社区基础 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-mo-image |
| 校验 URL | https://github.com/CM-Silence/dsh-mo-image |
| 必查项通过率 | 15/33 (45%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-11-23 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
