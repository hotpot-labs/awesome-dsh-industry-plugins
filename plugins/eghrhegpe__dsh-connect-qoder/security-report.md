# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/eghrhegpe/dsh-connect-qoder
- **校验时间**: 2026-09-30 04:39:08
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 22 | 7 | 4 |
| 🟡 推荐 | 14 | 7 | 7 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: fix/0.1.7-settings-rewrite |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2023-05-29 (1220 天前); 公开仓库数: 8; 粉丝数: 1 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1010; 包名: @eghrhegpe/dsh-connect-qoder; 描述: 将本机已登录的 Qoder（国内版 Qoder CN / 国际版 Qoder）模型接入 DeepSeek Harness —— bring locally si — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - test/shim.test.js:190 → 绕过权限限制 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (1): v0.1.0; package.json version: 0.2.1 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: >=4.0.2 <5.0.0; @deepseek-ai/dsh-llm: >=0.1.5 <0.2; @deepseek-ai/dsh-llm-pi-ai: >=0.1.5 <0.2; @deepseek-ai/dsh-settings: >=0.1.5 <0.2; @deepseek-ai/dsh-home-paths: >=0.1.5 <0.2 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": ["@deepseek-ai/dsh-client-ui-settin; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-llm, @deepseek-ai/dsh-llm-pi-ai, @deepseek-ai/dsh-settings, @deepseek-ai/dsh-home-paths; Cordis 配置文件: cordis.patch.yml<br>  - lib/settings-save.js:142 → Monkey patch / prototype pollution<br>  - test/settings-save.test.js:103 → Monkey patch / prototype pollution<br>  - test/preferences.test.js:136 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 210 处, 函数: 1224 个, 比例: 17.2% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: lib/credentials.js; 发现清理逻辑: lib/index.js; 发现清理逻辑: test/credential-cleanup.test.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .gitignore:18 → 读取环境变量配置 (2 处)<br>  - README.md:209 → 读取 npm 凭证 (1 处)<br>  - lib/credentials.js:370 → 读取环境变量配置 (4 处)<br>  - lib/account-state.js:68 → 读取环境变量配置 (2 处)<br>  - lib/client.js:320 → 读取环境变量配置 (3 处)<br>  ... 共 13 处 |
| 3.2 | 无全局文件读写 | 必查 | ✅ 通过 | 未检测到全局文件访问模式 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package-lock.json:38 → 探测到 HTTP(S) 网络请求 (85 处)<br>  - README.md:3 → 探测到 HTTP(S) 网络请求 (4 处)<br>  - package.json:7 → 探测到 HTTP(S) 网络请求 (4 处)<br>  - lib/credentials.js:86 → 探测到 HTTP(S) 网络请求 (8 处)<br>  - lib/client.js:461 → fetch 网络请求 (7 处)<br>涉及的域名: 127.0.0.1, api3.qoder.sh, center.qoder.sh, docs.qoder.cn, evil.example, gateway.qoder.com.cn, github.com, openapi.qoder.com.cn, openapi.qoder.sh, opencollective.com (+5 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - .gitignore:15 → 敏感凭证读取 (1 处)<br>  - README.md:13 → 敏感凭证读取 (6 处)<br>  - lib/credentials.js:370 → 读取环境变量 API Key/凭证 (1 处)<br>  - lib/credentials.js:90 → API Key / Token 读取 (4 处)<br>  - lib/credentials.js:2 → 敏感凭证读取 (40 处)<br>  ... 共 44 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - scripts/verify-bundle-behaviour.mjs:93 → new Function() 任意代码执行 (1 处)<br>  - test/client-bundle.test.js:71 → new Function() 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 12 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - lib/client.js:1383 → 定时任务 (2 处)<br>  - lib/index.js:1277 → 定时任务 (1 处)<br>  - lib/shim.js:179 → 开启监听端口 (1 处)<br>  - lib/upstream.js:91 → 定时任务 (1 处)<br>  - scripts/build-client.mjs:194 → 进程控制 (2 处)<br>  ... 共 7 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ✅ 通过 | 未检测到文件窃取/静默上传模式 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 1. repo: 0 deps + 1 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 16747, 注释行: 5337 (31.9%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 27 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - test/oscrypt.test.js:61 → 硬编码敏感信息 (1 处)<br>  - test/userinfo-headers.test.js:42 → 硬编码敏感信息 (1 处)<br>  - test/upstream-protocol.test.js:153 → 硬编码敏感信息 (6 处)<br>  - test/shim.test.js:69 → 硬编码敏感信息 (2 处)<br>  - test/credential-cleanup.test.js:329 → 明文写入敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - .github/workflows/test.yml:70 → 读取 git 历史 (1 处)<br>  - scripts/verify-bundle-behaviour.mjs:16 → 读取 git 历史 (1 处)<br>  - docs/KNOWN_GAPS.md:185 → 读取 git 历史 (1 处)<br>  - docs/issues/17-client-source-restore.md:79 → 读取 git 历史 (3 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (9 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (1 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ✅ 通过 | 未检测到系统配置修改/开机自启逻辑 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: 沙箱 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (2 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 3 天; 提交总数: 76 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 2, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-connect-qoder |
| 校验 URL | https://github.com/eghrhegpe/dsh-connect-qoder |
| 必查项通过率 | 22/33 (67%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-09-30 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
