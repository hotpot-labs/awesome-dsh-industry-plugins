# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/imMamdouhaboammar/get-fable
- **校验时间**: 2026-09-02 03:38:04
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
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2019-12-15 (2452 天前); 公开仓库数: 70; 粉丝数: 18 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 3061; 包名: get-fable; 描述: A portable coding lifecycle for AI agents with deterministic routing across 25 s — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - assets/prompts/claude-design.md:646 → 盗版/侵权 (1 处)<br>  - assets/skills/claude-code/claude-api/python/claude-api/README.md:410 → 非法爬取 (1 处)<br>  - assets/skills/claude-code/claude-api/typescript/claude-api/README.md:310 → 非法爬取 (1 处)<br>  - assets/skills/claude-code/update-config/SKILL.md:656 → 绕过权限限制 (2 处)<br>  - assets/skills/claude-design/frontend-design/SKILL.md:14 → 盗版/侵权 (1 处)<br>  ... 共 9 处 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (4): v1.5.1, v1.5.0, v1.4.0, v1.3.0; package.json version: 1.5.1; GitHub Releases (4): v1.5.1, v1.5.0, v1.4.0, v1.3.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | engines: {"bun": ">=1.3.0"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web"}}; Cordis 配置文件: cordis.patch.yml<br>  - assets/skills/claude-code/security-review/SKILL.md:163 → Monkey patch / prototype pollution<br>  - test/hook-dispatch-v2.test.ts:142 → Monkey patch / prototype pollution<br>  - test/antigravity-contract-v2.test.ts:25 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 408 处, 函数: 2308 个, 比例: 17.7% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: src/router/index.ts; 发现清理逻辑: test/skill-package-security.test.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - System-Prompt:135 → 读取环境变量配置 (1 处)<br>  - .gitignore:6 → 读取环境变量配置 (3 处)<br>  - src/cli.ts:375 → 读取环境变量配置 (2 处)<br>  - src/installer.ts:475 → 读取环境变量配置 (2 处)<br>  - src/utils.ts:38 → 读取环境变量配置 (33 处)<br>  ... 共 61 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - src/fable-lint.ts:139 → 目录遍历 (1 处)<br>  - src/cli.ts:868 → 目录遍历 (2 处)<br>  - src/cli.ts:523 → 读取用户主目录 (1 处)<br>  - src/assets-manager.ts:22 → 目录遍历 (3 处)<br>  - src/installer.ts:474 → 读取用户主目录 (2 处)<br>  ... 共 59 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - hooks/fable_hook_dispatch.py:247 → Python subprocess (1 处)<br>  - assets/skills/claude-code/claude-api/shared/token-counting.md:51 → Python subprocess (1 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - System-Prompt:35 → 探测到 HTTP(S) 网络请求 (37 处)<br>  - System-Prompt:289 → WebSocket 连接 (7 处)<br>  - System-Prompt:289 → 浏览器网络 API (5 处)<br>  - THIRD_PARTY_NOTICES.md:13 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - skills.sh.json:2 → 探测到 HTTP(S) 网络请求 (4 处)<br>涉及的域名: ..., 127.0.0.1, 169.254.169.254, api.anthropic.com, api.githubcopilot.com, api.notion.com, aws-external-anthropic., bedrock-mantle., cdn.jsdelivr.net, claude.ai (+46 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - Fable-Spark:45 → 恶意软件 (1 处)<br>  - Fable-work:45 → 恶意软件 (1 处)<br>  - assets/prompts/claude-code-docs-assistant.md:33 → 远控/反向 shell (1 处)<br>  - assets/skills/claude-code/claude-api/LICENSE.txt:150 → 挖矿相关 (1 处)<br>  - assets/skills/claude-code/update-config/SKILL.md:1174 → 远控/反向 shell (4 处)<br>  ... 共 8 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - System-Prompt:7 → 敏感凭证读取 (3 处)<br>  - skills.sh.json:61 → 敏感凭证读取 (1 处)<br>  - Fable-Spark:849 → 敏感凭证读取 (4 处)<br>  - SECURITY.md:12 → 敏感凭证读取 (2 处)<br>  - AGENTS.md:19 → 敏感凭证读取 (1 处)<br>  ... 共 175 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - test/telemetry-privacy.test.ts:14 → 写入配置文件 (1 处)<br>  - test/telemetry-privacy.test.ts:14 → 写入 DSH 配置 (1 处)<br>  - test/installer.test.ts:102 → 写入配置文件 (2 处)<br>  - test/installer.test.ts:102 → 写入 DSH 配置 (2 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - assets/skills/claude-code/run-skill-generator/examples/electron.md:154 → eval() 任意代码执行 (1 处)<br>  - assets/skills/claude-code/design-sync/package-validate.mjs:65 → new Function() 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 5 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - System-Prompt:79 → 临时文件操作 (3 处)<br>  - Fable-Spark:749 → 临时文件操作 (1 处)<br>  - Fable-Simulator-Code-Assistant:41 → 临时文件操作 (3 处)<br>  - README.md:494 → 临时文件操作 (2 处)<br>  - Fable-work:749 → 临时文件操作 (1 处)<br>  ... 共 168 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - System-Prompt:184 → 云存储上传 (5 处)<br>  - Fable-Spark:81 → 云存储上传 (24 处)<br>  - Fable-work:81 → 云存储上传 (24 处)<br>  - assets/starter-components/image-slot.js:143 → 云存储上传 (1 处)<br>  - assets/mcp-servers/claude-in-chrome.md:290 → 云存储上传 (14 处)<br>  ... 共 60 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 5. repo: 0 deps + 5 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 34343, 注释行: 4126 (12.0%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 67 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ✅ 通过 | README 中包含数据上报说明: telemetry |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - assets/starter-components/animations-v2.jsx:569 → 明文写入敏感信息 (1 处)<br>  - assets/skills/claude-code/claude-api/python/managed-agents/README.md:24 → 硬编码敏感信息 (1 处)<br>  - assets/skills/claude-code/claude-api/python/claude-api/README.md:20 → 硬编码敏感信息 (1 处)<br>  - assets/skills/claude-code/claude-api/shared/managed-agents-tools.md:248 → 硬编码敏感信息 (2 处)<br>  - assets/skills/claude-code/claude-api/typescript/managed-agents/README.md:24 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - skills.sh.json:56 → 读取 git 历史 (1 处)<br>  - agents/reviewer.md:18 → 读取 git 历史 (1 处)<br>  - src/installer.ts:331 → 读取文档/压缩文件 (1 处)<br>  - registry/skills.json:343 → 读取 git 历史 (1 处)<br>  - assets/agents/Explore.md:35 → 读取 git 历史 (2 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (62 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (45 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - assets/skills/claude-code/claude-api/shared/anthropic-cli.md:25 → 要求 root/sudo 权限<br>  - assets/skills/claude-code/run-skill-generator/template.md:21 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - Fable-Spark:2226 → 创建开机自启/系统服务 (1 处)<br>  - Fable-Simulator-Code-Assistant:115 → 创建开机自启/系统服务 (1 处)<br>  - install.sh:1 → 修改系统目录 (1 处)<br>  - Fable-work:2226 → 创建开机自启/系统服务 (1 处)<br>  - hooks/fable_lint.py:1 → 修改系统目录 (1 处)<br>  ... 共 34 处 |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (19 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 234 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 3, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | get-fable |
| 校验 URL | https://github.com/imMamdouhaboammar/get-fable |
| 必查项通过率 | 15/33 (45%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-09-02 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
