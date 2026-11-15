# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/439436269-ctrl/dsh-superagent
- **校验时间**: 2026-11-15 05:27:59
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 14 | 13 | 6 |
| 🟡 推荐 | 14 | 4 | 10 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2026-09-19 (56 天前); 公开仓库数: 49; 粉丝数: 0 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 227; 包名: @vfvrpq/dsh-superagent; 描述: A proactive agent for one GitHub repository, as a DSH (DeepSeek Harness) bundle: — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - src/core/model.ts:150 → 盗版/侵权 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ⚠️  需人工复核 | 无 git tag; package.json version: 0.3.0; 有版本号但无 git tag / release |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: 4.0.5-alpha.1; @deepseek-ai/dsh-agent: ^0.2.1-alpha.2; @deepseek-ai/dsh-api-session-controller: ^0.2.1-alpha.2; @deepseek-ai/dsh-client-locale: ^0.2.1-alpha.2; @deepseek-ai/dsh-client-ui-renderer: ^0.2.1-alpha.2 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "inject": ["@deepseek-ai/d; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-agent, @deepseek-ai/dsh-api-session-controller, @deepseek-ai/dsh-client-locale, @deepseek-ai/dsh-client-ui-renderer; Cordis 配置文件: cordis.patch.yml<br>  - docs/008-cookbook.md:325 → Monkey patch / prototype pollution<br>  - docs/013-multi-repository.md:444 → Monkey patch / prototype pollution<br>  - docs/014-progress.md:219 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 250 处, 函数: 4730 个, 比例: 5.3% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: src/index.ts; 发现清理逻辑: src/sessions/bus.ts; 发现清理逻辑: src/app/passes.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - README.en.md:72 → 读取环境变量配置 (1 处)<br>  - README.md:66 → 读取环境变量配置 (1 处)<br>  - .gitignore:4 → 读取环境变量配置 (1 处)<br>  - docs/006-deployment.md:262 → 读取 git 配置 (1 处)<br>  - docs/013-multi-repository.md:160 → 读取环境变量配置 (2 处)<br>  ... 共 36 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - src/sessions/bus.ts:61 → 读取用户主目录 (1 处)<br>  - src/app/tools/executor.ts:3 → 深层目录穿越 (5 处)<br>  - src/app/tools/tool.ts:3 → 深层目录穿越 (1 处)<br>  - src/app/tools/session-bus.ts:11 → 深层目录穿越 (1 处)<br>  - src/app/tools/reviewer.ts:2 → 深层目录穿越 (1 处)<br>  ... 共 18 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - scripts/dsh-superagent:76 → Python subprocess (7 处)<br>  - src/infra/environment.ts:243 → 进程执行 (1 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - cordis.patch.yml:50 → 开启 shell 模式 (注入风险) (3 处)<br>  - src/app/store.ts:111 → 命令字符串拼接变量 (注入风险) (6 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - README.en.md:9 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - README.en.md:73 → WebSocket 连接 (1 处)<br>  - README.en.md:73 → 浏览器网络 API (1 处)<br>  - README.md:9 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - README.md:67 → WebSocket 连接 (1 处)<br>涉及的域名: 127.0.0.1, 439436269-ctrl, api.dingtalk.com, api.github.com, api.telegram.org, applink, applink., applink.feishu.cn, applink.larksuite.com, avatars (+13 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - README.en.md:72 → 敏感凭证读取 (1 处)<br>  - SETUP.md:13 → 敏感凭证读取 (3 处)<br>  - pnpm-lock.yaml:279 → 敏感凭证读取 (5 处)<br>  - prompts/team/delivery.md:4 → 敏感凭证读取 (1 处)<br>  - docs/003-execution.md:81 → 敏感凭证读取 (1 处)<br>  ... 共 58 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - tests/environment.spec.ts:60 → 写入配置文件 (3 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - src/app/views/overview.ts:31 → eval() 任意代码执行 (1 处)<br>  - src/core/model.ts:172 → eval() 任意代码执行 (1 处)<br>  - tests/panel-overview.spec.tsx:136 → eval() 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 38 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - docs/014-progress.md:71 → 定时任务 (1 处)<br>  - examples/im-bridges/telegram.mjs:21 → 定时任务 (1 处)<br>  - examples/im-bridges/telegram.mjs:14 → 进程控制 (8 处)<br>  - examples/im-bridges/wecom.mjs:144 → 开启监听端口 (1 处)<br>  - examples/im-bridges/wecom.mjs:183 → 进程控制 (3 处)<br>  ... 共 36 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - pnpm-lock.yaml:277 → 云存储上传 (4 处)<br>  - tests/session-bus.spec.ts:16 → 云存储上传 (4 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 38. repo: 2 deps + 36 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 29266, 注释行: 3589 (12.3%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 59 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - examples/im-bridges/wecom.mjs:157 → 明文写入敏感信息 (1 处)<br>  - examples/im-bridges/wecom.test.mjs:12 → 硬编码敏感信息 (2 处)<br>  - tests/feishu-read.spec.ts:21 → 硬编码敏感信息 (3 处)<br>  - tests/dingtalk.spec.ts:8 → 硬编码敏感信息 (1 处)<br>  - tests/sources.spec.ts:233 → 硬编码敏感信息 (2 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - prompts/review.md:9 → 读取 git 历史 (3 处)<br>  - src/app/sessions.ts:75 → 读取 git 历史 (1 处)<br>  - src/executor/review.ts:144 → 读取 git 历史 (2 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (12 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ⚠️  需人工复核 | 未发现一键清理功能, 需确认是否有数据清理机制 |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - docs/007-architecture.md:619 → 创建开机自启/系统服务 (1 处)<br>  - examples/im-bridges/telegram.mjs:1 → 修改系统目录 (1 处)<br>  - examples/im-bridges/wecom.mjs:1 → 修改系统目录 (1 处)<br>  - examples/im-bridges/probe.mjs:1 → 修改系统目录 (1 处)<br>  - examples/im-bridges/dingtalk-stream.mjs:1 → 修改系统目录 (1 处)<br>  ... 共 14 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (3 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 155 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-superagent |
| 校验 URL | https://github.com/439436269-ctrl/dsh-superagent |
| 必查项通过率 | 14/33 (42%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-11-15 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
