# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/ChenXu233/dsh-agent-teams
- **校验时间**: 2026-11-07 05:11:11
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 14 | 11 | 8 |
| 🟡 推荐 | 14 | 5 | 9 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2021-10-05 (1858 天前); 公开仓库数: 69; 粉丝数: 58 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 3573; 包名: @chenxu233/dsh-agent-teams; 描述: AgentTeams for DeepSeek Harness: multi-agent team collaboration (captain, member — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - .dsh/skills/plugin-upgrade/references/v0.1.2-alpha.1.md:218 → 绕过权限限制 (1 处)<br>  - skills/plugin-upgrade/references/v0.1.2-alpha.1.md:218 → 绕过权限限制 (1 处)<br>  - scripts/verify.mjs:702 → 破解授权 (3 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (4): v0.2.2, v0.2.1-rc.2, v0.2.1-rc.1, v0.2.1; package.json version: 0.2.2; GitHub Releases (4): v0.2.2, v0.2.1, v0.2.1-rc.2, v0.2.1-rc.1 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.2; @deepseek-ai/dsh-agent: *; @deepseek-ai/dsh-api-session-controller: *; @deepseek-ai/dsh-client-connection: *; @deepseek-ai/dsh-client-locale: * |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": ["@deepseek-ai/dsh-client-locale", ; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-agent, @deepseek-ai/dsh-api-session-controller, @deepseek-ai/dsh-client-connection, @deepseek-ai/dsh-client-locale; Cordis 配置文件: cordis.patch.yml<br>  - .dsh/skills/plugin-upgrade/references/v0.1.6-alpha.1.md:466 → Monkey patch / prototype pollution<br>  - .dsh/skills/plugin-upgrade/references/v0.1.3-alpha.2.md:144 → Monkey patch / prototype pollution<br>  - .dsh/skills/plugin-upgrade/references/pre-flight.md:17 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 880 处, 函数: 7427 个, 比例: 11.8% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: lib/members.js; 发现清理逻辑: lib/harness-compat.js; 发现清理逻辑: lib/capabilities.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - tsdown.config.ts:75 → 读取环境变量配置 (6 处)<br>  - .dsh/skills/plugin-upgrade/SKILL.zh-CN.md:44 → 读取 npm 凭证 (1 处)<br>  - .dsh/skills/plugin-upgrade/SKILL.zh-CN.md:144 → 读取环境变量配置 (1 处)<br>  - .dsh/skills/plugin-upgrade/SKILL.md:55 → 读取 npm 凭证 (1 处)<br>  - .dsh/skills/plugin-upgrade/SKILL.md:125 → 读取环境变量配置 (1 处)<br>  ... 共 86 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - .dsh/skills/plugin-upgrade/examples/06-real-world-batch-migration.md:212 → 深层目录穿越 (1 处)<br>  - .dsh/skills/plugin-upgrade/examples/06-real-world-batch-migration.en.md:212 → 深层目录穿越 (1 处)<br>  - .dsh/skills/plugin-upgrade/examples/legacy-plugin/README.md:6 → 深层目录穿越 (2 处)<br>  - .dsh/skills/plugin-upgrade/examples/legacy-plugin/README.en.md:5 → 深层目录穿越 (2 处)<br>  - .dsh/skills/plugin-upgrade/examples/legacy-plugin/src/index.ts:36 → 读取用户主目录 (1 处)<br>  ... 共 26 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - .dsh/skills/dsh-benchmark-case/assets/judge-utils.mjs:106 → 命令字符串拼接变量 (注入风险) (6 处)<br>  - skills/dsh-benchmark-case/assets/judge-utils.mjs:106 → 命令字符串拼接变量 (注入风险) (6 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - LICENSE:3 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - package.json:37 → 探测到 HTTP(S) 网络请求 (6 处)<br>  - README.md:11 → 探测到 HTTP(S) 网络请求 (13 处)<br>  - pnpm-lock.yaml:492 → WebSocket 连接 (3 处)<br>  - pnpm-lock.yaml:492 → 浏览器网络 API (3 处)<br>涉及的域名: 127.0.0.1, api.deepseek.com, api.github.com, example.com, github.com, img.shields.io, json-schema.org, localhost, raw.githubusercontent.com, registry.npmjs.org (+4 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - .dsh/skills/plugin-upgrade/references/v0.1.2-rc.1.md:96 → 挖矿相关 (1 处)<br>  - skills/plugin-upgrade/references/v0.1.2-rc.1.md:96 → 挖矿相关 (1 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - tsdown.config.ts:75 → 读取环境变量 API Key/凭证 (4 处)<br>  - pnpm-lock.yaml:123 → API Key / Token 读取 (9 处)<br>  - pnpm-lock.yaml:118 → 敏感凭证读取 (108 处)<br>  - CONTRIBUTING.md:9 → 敏感凭证读取 (3 处)<br>  - pnpm-workspace.yaml:121 → API Key / Token 读取 (1 处)<br>  ... 共 151 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - .dsh/skills/plugin-test/scripts/docker-release-smoke.mjs:362 → 写入配置文件 (1 处)<br>  - skills/plugin-test/scripts/docker-release-smoke.mjs:362 → 写入配置文件 (1 处)<br>  - scripts/quality-gates-work-order.test.mjs:239 → 写入配置文件 (1 处)<br>  - scripts/check-install-channel.mjs:19 → 写入配置文件 (1 处)<br>  - scripts/fixtures/harness-model-driver.mjs:61 → 写入配置文件 (3 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - scripts/compatibility.test.mjs:105 → 十六进制混淆 (1 处)<br>  - scripts/compatibility.mjs:175 → 十六进制混淆 (1 处) |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 36 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - CONTRIBUTING.md:31 → 临时文件操作 (1 处)<br>  - .dsh/skills/dsh-upgrade-audit/evals/evals.json:6 → 临时文件操作 (1 处)<br>  - .dsh/skills/dsh-upgrade-audit/scripts/gen-artifacts.mjs:18 → 进程控制 (2 处)<br>  - .dsh/skills/dsh-upgrade-audit/scripts/materialize-npm.mjs:25 → 进程控制 (2 处)<br>  - .dsh/skills/plugin-upgrade/examples/07-multi-repo-batch-migration.en.md:27 → 临时文件操作 (4 处)<br>  ... 共 115 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - pnpm-lock.yaml:444 → 云服务 SDK (可能用于隐蔽上传) (105 处)<br>  - pnpm-lock.yaml:179 → 云存储上传 (6 处)<br>  - pnpm-workspace.yaml:177 → 云存储上传 (1 处)<br>  - .dsh/skills/plugin-upgrade/SKILL.md:131 → 云存储上传 (1 处)<br>  - .dsh/skills/plugin-upgrade/references/v0.1.2-alpha.1.md:39 → 云存储上传 (2 处)<br>  ... 共 24 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 36. repo: 0 deps + 36 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 75116, 注释行: 11149 (14.8%) |
| 4.9 | 具备测试覆盖 | 推荐 | ⚠️  需人工复核 | 未发现测试文件 |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - .dsh/skills/plugin-upgrade/scripts/verify-runtime.mjs:348 → 明文写入敏感信息 (1 处)<br>  - .dsh/skills/plugin-upgrade/scripts/verify-runtime.mjs:262 → 硬编码敏感信息 (1 处)<br>  - .dsh/skills/plugin-test/scripts/docker-release-smoke.test.mjs:45 → 硬编码敏感信息 (1 处)<br>  - skills/plugin-upgrade/scripts/verify-runtime.mjs:348 → 明文写入敏感信息 (1 处)<br>  - skills/plugin-upgrade/scripts/verify-runtime.mjs:262 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - .dsh/skills/dsh-upgrade-audit/SKILL.zh-CN.md:57 → 读取 git 历史 (2 处)<br>  - .dsh/skills/dsh-upgrade-audit/SKILL.md:64 → 读取 git 历史 (2 处)<br>  - .dsh/skills/dsh-upgrade-audit/examples/0.1.2alpha1-to-0.1.2alpha2/CHANGELOG.md:3 → 读取 git 历史 (1 处)<br>  - .dsh/skills/dsh-upgrade-audit/references/audit-playbook.md:16 → 读取 git 历史 (4 处)<br>  - .dsh/skills/dsh-upgrade-audit/scripts/gen-artifacts.mjs:80 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (109 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (9 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - .gitattributes:14 → 修改系统目录 (1 处)<br>  - .dsh/skills/plugin-workflow/scripts/plan-workflow.mjs:1 → 修改系统目录 (1 处)<br>  - .dsh/skills/dsh-upgrade-audit/scripts/gen-artifacts.mjs:1 → 修改系统目录 (1 处)<br>  - .dsh/skills/dsh-upgrade-audit/scripts/materialize-npm.mjs:1 → 修改系统目录 (1 处)<br>  - .dsh/skills/plugin-upgrade/references/rollup-0.1.2.md:207 → 创建开机自启/系统服务 (1 处)<br>  ... 共 56 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: sandbox, workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (19 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 3 天; 提交总数: 374 |
| 7.2 | 未标记停止维护 | 必查 | ❌ 不通过 | 文档中发现弃用标记: archived |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 1, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-agent-teams |
| 校验 URL | https://github.com/ChenXu233/dsh-agent-teams |
| 必查项通过率 | 14/33 (42%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-11-07 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
