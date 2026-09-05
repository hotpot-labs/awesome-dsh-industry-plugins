# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/huaweicloud/huaweicloud-devkit
- **校验时间**: 2026-09-05 03:38:10
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 14 | 12 | 7 |
| 🟡 推荐 | 14 | 7 | 7 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2018-02-18 (3121 天前); 公开仓库数: 162; 粉丝数: 759 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: Apache-2.0 (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1127; 包名: huaweicloud-devkit; 描述: Agent toolkit that helps coding agents use Huawei Cloud Skills, KooCLI, APIs, SD — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - plugins/huaweicloud-core/skills/huawei-obs/references/bucket-lifecycle.md:17 → 盗版/侵权 (1 处)<br>  - plugins/huaweicloud-core/skills/huawei-ecs/SKILL.md:108 → 破解授权 (1 处)<br>  - plugins/huaweicloud-core/safety/rules/cloud-risk-rules.json:270 → 盗版/侵权 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (4): v1.1.0, v1.0.2, v1.0.1, v1.0.0; package.json version: 1.1.0; GitHub Releases (4): v1.1.0, v1.0.2, v1.0.1, v1.0.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | engines: {"node": ">=22"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}}; Cordis 配置文件: cordis.patch.yml<br>  - plugins/huaweicloud-core/src/setup-cli.mjs:1746 → Monkey patch / prototype pollution<br>  - plugins/huaweicloud-core/src/mcp-server.mjs:126 → Monkey patch / prototype pollution<br>  - test/dsh-adaptation.test.mjs:39 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 262 处, 函数: 1022 个, 比例: 25.6% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: plugins/huaweicloud-core/src/setup-cli.mjs; 发现清理逻辑: test/detect-framework.test.mjs |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .gitignore:8 → 读取环境变量配置 (3 处)<br>  - AGENTS.md:134 → 读取环境变量配置 (1 处)<br>  - plugins/huaweicloud-core/skills/huawei-functiongraph/references/triggers.md:53 → 读取环境变量配置 (4 处)<br>  - plugins/huaweicloud-core/skills/huaweicloud-cli-and-auth/SKILL.md:133 → 读取凭证文件 (1 处)<br>  - plugins/huaweicloud-core/skills/huawei-sandbox/SKILL.md:423 → 读取环境变量配置 (27 处)<br>  ... 共 35 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - plugins/huaweicloud-core/src/setup-cli.mjs:52 → 读取用户主目录 (50 处)<br>  - plugins/huaweicloud-core/src/hcloud-cli.mjs:105 → 读取用户主目录 (3 处)<br>  - plugins/huaweicloud-core/src/tools.mjs:44 → 读取用户主目录 (9 处)<br>  - plugins/huaweicloud-core/src/proxy/proxy-config.mjs:6 → 读取用户主目录 (1 处)<br>  - plugins/huaweicloud-core/src/auth/credentials.mjs:29 → 读取用户主目录 (5 处)<br>  ... 共 6 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - docs/hermes-windows.md:34 → Python subprocess (1 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - plugins/huaweicloud-core/src/setup-cli.mjs:596 → 命令字符串拼接变量 (注入风险) (7 处)<br>  - plugins/huaweicloud-core/src/setup-cli.mjs:470 → 开启 shell 模式 (注入风险) (10 处)<br>  - plugins/huaweicloud-core/src/auth/service.mjs:10 → 命令字符串拼接变量 (注入风险) (1 处)<br>  - plugins/huaweicloud-core/src/auth/service.mjs:11 → 开启 shell 模式 (注入风险) (1 处)<br>  - scripts/bump-version.mjs:15 → 命令字符串拼接变量 (注入风险) (5 处)<br>  ... 共 6 处 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - README.zh-CN.md:3 → 探测到 HTTP(S) 网络请求 (9 处)<br>  - OWNERS:9 → 探测到 HTTP(S) 网络请求 (4 处)<br>  - release-please-config.json:2 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - SUPPORT.md:7 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - CODE_OF_CONDUCT.md:119 → 探测到 HTTP(S) 网络请求 (5 处)<br>涉及的域名: 127.0.0.1, api.qrserver.com, clawhub.ai, cn-north-4-hdn-koocli.obs.cn-north-4.myhuaweicloud.com, codearts.huaweicloud.com, console.huaweicloud.com, contrib.rocks, developer.huaweicloud.com, devkit.huaweicloud.com, devstation.myhuaweicloud.com (+30 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - CODE_OF_CONDUCT.md:72 → 挖矿相关 (1 处)<br>  - LICENSE:149 → 挖矿相关 (1 处)<br>  - plugins/huaweicloud-core/skills/huawei-waf-aad/SKILL.md:3 → DDoS 攻击 (6 处)<br>  - plugins/huaweicloud-core/skills/huaweicloud-core/SKILL.md:35 → DDoS 攻击 (2 处)<br>  - plugins/huaweicloud-core/skills/huawei-sandbox/SKILL.md:733 → 代理/隧道 (2 处)<br>  ... 共 12 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - README.zh-CN.md:215 → 敏感凭证读取 (1 处)<br>  - CONTRIBUTING.md:62 → 敏感凭证读取 (2 处)<br>  - README.md:160 → 敏感凭证读取 (7 处)<br>  - AGENTS.md:134 → 读取环境变量 API Key/凭证 (1 处)<br>  - plugins/huaweicloud-core/skills/huaweicloud-capability-discovery/SKILL.md:63 → 敏感凭证读取 (1 处)<br>  ... 共 88 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - plugins/huaweicloud-core/src/setup-cli.mjs:555 → 写入配置文件 (15 处)<br>  - plugins/huaweicloud-core/src/tools.mjs:1169 → 写入配置文件 (1 处)<br>  - test/auth-credentials.test.mjs:220 → 写入配置文件 (3 处)<br>  - test/codearts-adaptation.test.mjs:151 → 写入配置文件 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 11 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - plugins/huaweicloud-core/skills/huawei-sandbox/SKILL.md:20 → 临时文件操作 (30 处)<br>  - plugins/huaweicloud-core/skills/huawei-sandbox/references/framework-commands.md:9 → 临时文件操作 (5 处)<br>  - plugins/huaweicloud-core/skills/huawei-sandbox/references/nginx-templates.md:96 → 临时文件操作 (1 处)<br>  - plugins/huaweicloud-core/src/setup-cli.mjs:440 → 进程控制 (6 处)<br>  - plugins/huaweicloud-core/src/mcp-server.mjs:62 → 定时任务 (1 处)<br>  ... 共 33 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - plugins/huaweicloud-core/skills/huawei-obs/SKILL.md:111 → multipart 上传 (1 处)<br>  - plugins/huaweicloud-core/skills/huawei-obs/SKILL.md:47 → 云存储上传 (5 处)<br>  - plugins/huaweicloud-core/skills/huawei-obs/references/static-website.md:8 → 云存储上传 (5 处)<br>  - plugins/huaweicloud-core/skills/huawei-functiongraph/SKILL.md:30 → 云存储上传 (2 处)<br>  - plugins/huaweicloud-core/skills/huawei-functiongraph/references/create-function.md:37 → 云存储上传 (1 处)<br>  ... 共 16 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 11. repo: 2 deps + 9 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 16208, 注释行: 178 (1.1%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - plugins/huaweicloud-core/src/tools.mjs:990 → 硬编码敏感信息 (2 处)<br>  - plugins/huaweicloud-core/src/sandbox/hdkitservice-api.mjs:81 → 从环境变量获取敏感信息 (1 处)<br>  - docs/plan-run-approval-contract.md:14 → 硬编码敏感信息 (1 处)<br>  - test/safety-policy.test.mjs:28 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - scripts/bump-version.mjs:97 → 读取 git 历史 (1 处)<br>  - scripts/create-release-pr.mjs:56 → 读取 git 历史 (2 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (21 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (5 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - plugins/huaweicloud-core/skills/huawei-sandbox/SKILL.md:108 → 要求 root/sudo 权限<br>  - plugins/huaweicloud-core/skills/huawei-sandbox/references/framework-commands.md:64 → 要求 root/sudo 权限<br>  - plugins/huaweicloud-core/skills/huawei-sandbox/references/nginx-templates.md:8 → 要求 root/sudo 权限<br>  - plugins/huaweicloud-core/src/sandbox/session-manager.mjs:716 → 要求 root/sudo 权限<br>  - skills/@huaweiclouddev/huawei-cloud-find-skills/SKILL.md:59 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - AGENTS.md:38 → 创建开机自启/系统服务 (1 处)<br>  - plugins/huaweicloud-core/skills/huawei-ecs/SKILL.md:121 → 创建开机自启/系统服务 (1 处)<br>  - plugins/huaweicloud-core/skills/huaweicloud-cli-and-auth/SKILL.md:63 → 修改系统目录 (1 处)<br>  - plugins/huaweicloud-core/skills/huawei-sandbox/SKILL.md:108 → 修改系统目录 (5 处)<br>  - plugins/huaweicloud-core/skills/huawei-sandbox/references/framework-commands.md:64 → 修改系统目录 (1 处)<br>  ... 共 17 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: sandbox |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (9 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 2 天; 提交总数: 452 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ⚠️  需人工复核 | 发现 2 个公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG, 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 44, Forks: 10, Watchers: 1 — 有一定社区基础 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | huaweicloud-devkit |
| 校验 URL | https://github.com/huaweicloud/huaweicloud-devkit |
| 必查项通过率 | 14/33 (42%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-09-05 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
