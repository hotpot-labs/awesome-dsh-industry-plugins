# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/01men/ybkkasi
- **校验时间**: 2026-10-19 03:48:02
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 16 | 11 | 6 |
| 🟡 推荐 | 14 | 8 | 6 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2019-04-26 (2732 天前); 公开仓库数: 20; 粉丝数: 0 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1227; 包名: dsh-enterprise-ops; 描述: 企业 AI 资源统一管理平台 —— 基于 DeepSeek Harness「一切皆插件」架构 — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - docs/internal/handoff-w1-marketing-launch-20261017.md:104 → 非法爬取 (1 处)<br>  - docs/internal/dev-plan-app-sso.md:267 → 绕过权限限制 (1 处)<br>  - docs/internal/dev-plan-app-sso.md:101 → 欺诈行为 (2 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (6): refactor-stage-4-final, refactor-stage-3, refactor-stage-2, refactor-stage-1, refactor-stage-0; package.json version: 1.3.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | engines: {"node": ">=22.6"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "compatibility": {"dsh": ">=0.1.0-rc.7 <0.2.0", "dshRele; Cordis 配置文件: cordis.patch.yml, cordis.yml<br>  - packages/plugin-console/public/js/pages/audit.js:167 → Monkey patch / prototype pollution<br>  - packages/plugin-console/public/js/pages/agents.js:420 → Monkey patch / prototype pollution<br>  - packages/plugin-console/public/js/pages/nas.js:184 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 1469 处, 函数: 6340 个, 比例: 23.2% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: scripts/storage-bench.mjs; 发现清理逻辑: packages/plugin-console/public/js/pages/home.js; 发现清理逻辑: packages/plugin-rq-card/lib/client.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - 交互重设计-设计稿.html:127 → 读取环境变量配置 (4 处)<br>  - integrations/synology-filestation-mcp/src/authz.js:91 → 读取环境变量配置 (9 处)<br>  - integrations/hermes-patch/nas_authz_guard.py:50 → 读取环境变量配置 (5 处)<br>  - scripts/register-dsh-agent.mjs:28 → 读取环境变量配置 (4 处)<br>  - scripts/release-manifest.mjs:32 → 读取环境变量配置 (2 处)<br>  ... 共 53 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - 测试报告-前后端整体适配验收-20261015/00-总测试报告.md:92 → 深层目录穿越 (1 处)<br>  - scripts/check-dsh-compat.mjs:203 → 目录遍历 (2 处)<br>  - cli/dshctl.mjs:61 → 目录遍历 (1 处)<br>  - packages/plugin-agent/src/onboarding.ts:9 → 深层目录穿越 (1 处)<br>  - packages/plugin-agent/src/index.ts:15 → 深层目录穿越 (8 处)<br>  ... 共 142 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - packages/platform-core/src/sqlite.ts:53 → 命令字符串拼接变量 (注入风险) (3 处)<br>  - packages/plugin-update/src/git.ts:74 → 开启 shell 模式 (注入风险) (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - docker-compose.yml:2 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - docker-compose.yml:25 → fetch 网络请求 (1 处)<br>  - package-lock.json:25 → 探测到 HTTP(S) 网络请求 (61 处)<br>  - CHANGELOG.md:109 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - CONTRIBUTING.md:18 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: 0.0.0.0, 10.0.0.3, 127.0.0.1, 172.16.1.9, 172.32.1.9, 192.168.0.4, 192.168.0.7, 192.168.1.5, 192.168.1.9, 8.8.8.8 (+55 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - docs/connector-integration.md:203 → 代理/隧道 (2 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - README.md:71 → 敏感凭证读取 (4 处)<br>  - Dockerfile:32 → 敏感凭证读取 (1 处)<br>  - integrations/synology-filestation-mcp/test/authz-smoke.mjs:25 → 敏感凭证读取 (6 处)<br>  - integrations/synology-filestation-mcp/src/authz.js:91 → 读取环境变量 API Key/凭证 (9 处)<br>  - integrations/synology-filestation-mcp/src/authz.js:93 → 敏感凭证读取 (10 处)<br>  ... 共 293 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - packages/plugin-console/public/js/pages/home.js:425 → 修改全局配置 (1 处)<br>  - packages/plugin-console/src/routes/apps.ts:143 → 修改全局配置 (1 处)<br>  - packages/plugin-connect/src/client.ts:121 → 写入配置文件 (2 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 3 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - 交互重设计-设计稿.html:1264 → 定时任务 (1 处)<br>  - docker-compose.yml:25 → 进程控制 (2 处)<br>  - integrations/synology-filestation-mcp/test/authz-smoke.mjs:46 → 定时任务 (3 处)<br>  - integrations/synology-filestation-mcp/test/authz-smoke.mjs:187 → 进程控制 (1 处)<br>  - integrations/synology-filestation-mcp/test/authz-smoke.mjs:93 → 临时文件操作 (1 处)<br>  ... 共 111 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - README.md:221 → 云存储上传 (1 处)<br>  - integrations/synology-filestation-mcp/test/authz-smoke.mjs:93 → 云存储上传 (4 处)<br>  - integrations/synology-filestation-mcp/src/authz.js:27 → 云存储上传 (1 处)<br>  - integrations/hermes-patch/nas_authz_guard.py:26 → 云存储上传 (1 处)<br>  - scripts/selftest.mjs:145 → 云存储上传 (57 处)<br>  ... 共 43 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 3. repo: 0 deps + 3 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 79639, 注释行: 9078 (11.4%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 4 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - README.md:71 → 硬编码敏感信息 (1 处)<br>  - integrations/synology-filestation-mcp/test/authz-smoke.mjs:16 → 硬编码敏感信息 (3 处)<br>  - integrations/synology-filestation-mcp/src/authz.js:91 → 从环境变量获取敏感信息 (9 处)<br>  - scripts/release-manifest.mjs:48 → 明文写入敏感信息 (1 处)<br>  - scripts/page-smoke.mjs:88 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - docs/host-features-ops-notes.md:57 → 读取 git 历史 (1 处)<br>  - docs/internal/handoff-f-remainder-adoption-20260910.md:4 → 读取 git 历史 (1 处)<br>  - docs/internal/EXEC-CHECKLIST-20261016.md:39 → 读取 git 历史 (1 处)<br>  - docs/internal/dev-plan-access-hardening.md:26 → 读取 git 历史 (1 处)<br>  - docs/internal/release-notes-2026-09-16-m2.md:33 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (59 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (17 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - scripts/register-dsh-agent.mjs:1 → 修改系统目录 (1 处)<br>  - scripts/billing-archive-export.mjs:1 → 修改系统目录 (1 处)<br>  - scripts/guard-port.sh:1 → 修改系统目录 (6 处)<br>  - scripts/guard-port.sh:5 → 创建开机自启/系统服务 (2 处)<br>  - scripts/check-dsh-compat.mjs:1 → 修改系统目录 (1 处)<br>  ... 共 23 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: 隔离 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (16 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 206 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | ybkkasi |
| 校验 URL | https://github.com/01men/ybkkasi |
| 必查项通过率 | 16/33 (48%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-19 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
