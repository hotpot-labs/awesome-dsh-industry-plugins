# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/joekytc/dsh-swarm
- **校验时间**: 2026-08-28 10:24:44
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 20 | 8 | 5 |
| 🟡 推荐 | 14 | 5 | 9 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2021-12-13 (1719 天前); 公开仓库数: 20; 粉丝数: 0 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 3708; 包名: @joekytc/dsh-swarm; 描述: A governed swarm of six specialist DSH agents (orchestrator, planner, knowledge- — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ⚠️  需人工复核 | 无 git tag; package.json version: 0.1.1; 有版本号但无 git tag / release |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.1; @deepseek-ai/dsh-agent: ^0.1.0-rc.6; @deepseek-ai/dsh-persona: ^0.1.0-rc.6; @deepseek-ai/dsh-session: ^0.1.0-rc.6; @deepseek-ai/dsh-tools: ^0.1.0-rc.6 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "inject": ["@deepseek-ai/d; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-agent, @deepseek-ai/dsh-persona, @deepseek-ai/dsh-session, @deepseek-ai/dsh-tools; Cordis 配置文件: cordis.patch.yml, agent.cordis.yml, agent.cordis.yml<br>  - tests/dispatcher/watchdog.test.ts:49 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 320 处, 函数: 2204 个, 比例: 14.5% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: client/board-store.ts; 发现清理逻辑: src/tools/main-session-tools.ts; 发现清理逻辑: src/dispatcher/watchdog.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - src/services/kanban-provider.ts:17 → 读取环境变量配置 (1 处)<br>  - src/roles/preset-installer.ts:28 → 读取环境变量配置 (1 处)<br>  - src/roles/wiki-worker.ts:8 → 读取环境变量配置 (1 处)<br>  - src/dispatcher/git-credentials.ts:34 → 读取环境变量配置 (1 处)<br>  - src/dispatcher/git-credentials.ts:8 → 读取 git 配置 (1 处)<br>  ... 共 21 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - src/services/kanban-provider.ts:17 → 读取用户主目录 (1 处)<br>  - src/roles/preset-installer.ts:28 → 读取用户主目录 (1 处)<br>  - src/roles/preset-installer.ts:21 → 深层目录穿越 (2 处)<br>  - tests/domain/permissions.test.ts:2 → 深层目录穿越 (2 处)<br>  - tests/domain/delivery-contract.test.ts:2 → 深层目录穿越 (2 处)<br>  ... 共 63 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - README.zh-CN.md:9 → 探测到 HTTP(S) 网络请求 (6 处)<br>  - AGENTS.md:12 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - cordis.patch.yml:23 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - package.json:9 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - package-lock.json:41 → 探测到 HTTP(S) 网络请求 (500 处)<br>涉及的域名: 127.0.0.1, 192.168.122.111, github.com, gitlab.jianzhikeji.com, img.shields.io, localhost, mock, opencollective.com, registry.npmmirror.com, tidelift.com (+2 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - AGENTS.md:22 → 敏感凭证读取 (1 处)<br>  - package-lock.json:343 → 敏感凭证读取 (5 处)<br>  - README.md:489 → 敏感凭证读取 (1 处)<br>  - personas/kanban-dt/agent.cordis.yml:24 → 敏感凭证读取 (1 处)<br>  - src/services/kanban-provider.ts:17 → 读取环境变量 API Key/凭证 (1 处)<br>  ... 共 30 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - tests/client/client-bundle.test.ts:26 → new Function() 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 23 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - client/TaskDrawer.tsx:56 → 定时任务 (1 处)<br>  - src/index.ts:16 → 定时任务 (4 处)<br>  - src/wiki/memory-recall.ts:11 → 定时任务 (1 处)<br>  - src/roles/toolsets.ts:104 → 临时文件操作 (1 处)<br>  - src/dispatcher/watchdog.ts:30 → 定时任务 (1 处)<br>  ... 共 28 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ✅ 通过 | 未检测到文件窃取/静默上传模式 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 14. repo: 0 deps + 14 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 19852, 注释行: 2135 (10.8%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 51 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - src/dispatcher/git-credentials.ts:52 → 硬编码敏感信息 (1 处)<br>  - tests/dispatcher/git-credentials.test.ts:12 → 硬编码敏感信息 (3 处)<br>  - lib/dispatcher/git-credentials.js:48 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - personas/persona-dt.md:8 → 读取 git 历史 (1 处)<br>  - personas/persona-w.md:9 → 读取 git 历史 (1 处)<br>  - personas/persona-d.md:15 → 读取 git 历史 (1 处)<br>  - personas/persona-pt.md:13 → 读取 git 历史 (1 处)<br>  - personas/kanban-pt/agent.cordis.yml:21 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (22 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ⚠️  需人工复核 | 未发现一键清理功能, 需确认是否有数据清理机制 |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - tests/roles/wiki-worker.test.ts:32 → 修改系统目录 (1 处)<br>  - tests/roles/toolsets.test.ts:89 → 修改系统目录 (2 处)<br>  - tests/e2e/install-check.sh:1 → 修改系统目录 (1 处)<br>  - tests/e2e/gui-check.py:1 → 修改系统目录 (1 处) |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: sandbox, isolation, workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (1 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 126 |
| 7.2 | 未标记停止维护 | 必查 | ❌ 不通过 | 文档中发现弃用标记: archived |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG, 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 2, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-swarm |
| 校验 URL | https://github.com/joekytc/dsh-swarm |
| 必查项通过率 | 20/33 (61%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-28 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
