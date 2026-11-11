# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/ECCVIK/lmtagent
- **校验时间**: 2026-11-11 05:19:44
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 16 | 10 | 7 |
| 🟡 推荐 | 14 | 7 | 7 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2025-08-24 (444 天前); 公开仓库数: 5; 粉丝数: 0 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1097; 包名: dsh-redteam-mode; 描述: LMTAgent：基于 DSH 的 8 角色 gstack 软件工程研发集群与可视化 DAG 工作流编排器（含主控架构师 Captain + CEO / Des — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - packages/redteam-ui/lib/index.js:4394 → 非法爬取 (1 处)<br>  - packages/redteam-bundle/lib/ui.js:4394 → 非法爬取 (1 处)<br>  - lib/ui.js:4394 → 非法爬取 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (7): v0.21.0, v0.20.0, v0.19.0, v0.18.0, v0.16.1; package.json version: 0.21.0; GitHub Releases (5): v0.20.0, v0.19.0, v0.18.0, v0.16.1, v0.16.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | engines: {"dsh": ">=0.1.0-rc.6"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "inject": []}}; Cordis 配置文件: cordis.patch.yml, worker.cordis.yml, agent.cordis.yml<br>  - packages/redteam-ui/lib/index.js:246 → Monkey patch / prototype pollution<br>  - packages/redteam-ui/test/tabs-render.test.mjs:110 → Monkey patch / prototype pollution<br>  - packages/redteam-tools/test/session-isolation.test.mjs:101 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 776 处, 函数: 4134 个, 比例: 18.8% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: packages/redteam-ui/lib/index.js; 发现清理逻辑: packages/redteam-ui/test/client-load.test.mjs; 发现清理逻辑: packages/redteam-ui/test/ui-smoke.test.mjs |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .gitignore:29 → 读取环境变量配置 (2 处)<br>  - skills/deepseek-web-intel.md:14 → 读取环境变量配置 (2 处)<br>  - skills/dir-bruteforce.md:16 → 读取环境变量配置 (1 处)<br>  - skills/opsec-hygiene.md:14 → 读取环境变量配置 (1 处)<br>  - skills/redteam-setup.md:15 → 读取环境变量配置 (1 处)<br>  ... 共 95 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - packages/redteam-ui/tools/assemble-client.mjs:41 → 目录遍历 (1 处)<br>  - packages/redteam-ui/lib/index.js:1254 → 读取用户主目录 (1 处)<br>  - packages/redteam-ui/lib/index.js:20 → 深层目录穿越 (3 处)<br>  - packages/redteam-tools/lib/index.js:19 → 深层目录穿越 (2 处)<br>  - packages/redteam-tools/lib/concurrency.js:44 → 读取用户主目录 (1 处)<br>  ... 共 56 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - packages/redteam-store/lib/core.js:984 → exec 命令拼接 (4 处)<br>  - packages/redteam-store/lib/pg-engine.js:970 → 命令字符串拼接变量 (注入风险) (1 处)<br>  - packages/redteam-store/lib/schema.js:643 → 命令字符串拼接变量 (注入风险) (3 处)<br>  - packages/redteam-bundle/lib/store-core.js:984 → exec 命令拼接 (4 处)<br>  - packages/redteam-bundle/lib/pg-engine.js:970 → 命令字符串拼接变量 (注入风险) (1 处)<br>  ... 共 9 处 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package.json:83 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - README.md:5 → 探测到 HTTP(S) 网络请求 (11 处)<br>  - skills/active-scan.md:22 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - skills/ad-attack.md:22 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - skills/api-data-exfil.md:22 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: 10.0.0.12, 10.0.0.5, 10.0.0.8, 10.0.0.9, 10.1.1.1, 10.20.30.11, 10.7.7.7, 10.7.7.8, 10.7.7.9, 10.9.9.9 (+25 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - skills/passive-recon.md:4 → 挖矿相关 (1 处)<br>  - skills/vps-reverse-shell.md:2 → 远控/反向 shell (1 处)<br>  - skills/suo5-tunnel.md:11 → 代理/隧道 (3 处)<br>  - skills/chisel-tunnel.md:4 → 代理/隧道 (4 处)<br>  - skills/fscan-intranet.md:21 → 代理/隧道 (2 处)<br>  ... 共 36 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - .gitignore:35 → 敏感凭证读取 (6 处)<br>  - skills/mobile-code-recon.md:4 → 敏感凭证读取 (1 处)<br>  - skills/deepseek-web-intel.md:14 → API Key / Token 读取 (6 处)<br>  - skills/webshell-toolkit.md:15 → 敏感凭证读取 (1 处)<br>  - skills/cloud-k8s.md:11 → 敏感凭证读取 (1 处)<br>  ... 共 112 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - packages/redteam-ui/lib/index.js:108 → 写入配置文件 (1 处)<br>  - packages/redteam-tools/lib/concurrency.js:378 → 写入配置文件 (1 处)<br>  - packages/redteam-store/lib/settings.js:372 → 写入配置文件 (1 处)<br>  - packages/redteam-bundle/lib/ui.js:108 → 写入配置文件 (1 处)<br>  - packages/redteam-bundle/lib/concurrency.js:378 → 写入配置文件 (1 处)<br>  ... 共 11 处 — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - packages/redteam-ui/tools/assemble-client.mjs:66 → node:vm 任意代码执行 (1 处)<br>  - packages/redteam-ui/test/client-load.test.mjs:77 → new Function() 任意代码执行 (1 处)<br>  - packages/redteam-ui/test/ui-smoke.test.mjs:94 → new Function() 任意代码执行 (1 处)<br>  - packages/redteam-ui/test/tabs-render.test.mjs:212 → new Function() 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 0 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - packages/redteam-ui/tools/assemble-client.mjs:89 → 文件写入 (1 处)<br>  - packages/redteam-ui/tools/assemble-client.mjs:54 → 文件读取 (2 处)<br>  - packages/redteam-ui/tools/assemble-client.mjs:38 → 进程控制 (7 处)<br>  - packages/redteam-ui/tools/assemble-styles.mjs:33 → 进程控制 (6 处)<br>  - packages/redteam-ui/lib/index.js:409 → 定时任务 (6 处)<br>  ... 共 95 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - packages/redteam-ui/lib/client.js:646 → 云存储上传 (1 处)<br>  - packages/redteam-ui/src/client/01-core-rpc.js:391 → 云存储上传 (1 处)<br>  - packages/redteam-tools/lib/index.js:2398 → 云存储上传 (2 处)<br>  - packages/redteam-tools/test/session-isolation.test.mjs:156 → 云存储上传 (7 处)<br>  - packages/redteam-tools/test/rule-tools.test.mjs:119 → 云存储上传 (1 处)<br>  ... 共 17 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 无第三方依赖 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 69125, 注释行: 5480 (7.9%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 4 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ✅ 通过 | README 中包含数据上报说明: 遥测 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - packages/redteam-ui/lib/client.js:570 → 明文写入敏感信息 (4 处)<br>  - packages/redteam-ui/src/client/01-core-rpc.js:315 → 明文写入敏感信息 (3 处)<br>  - packages/redteam-ui/src/client/07-cluster-shell.js:632 → 明文写入敏感信息 (1 处)<br>  - packages/redteam-store/lib/skill-fixes.js:164 → 硬编码敏感信息 (2 处)<br>  - packages/redteam-bundle/lib/skill-fixes.js:164 → 硬编码敏感信息 (2 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - skills/passive-recon.md:16 → 读取 git 历史 (2 处)<br>  - packages/redteam-bundle/skills/passive-recon.md:16 → 读取 git 历史 (2 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (51 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (6 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - docs/详细文档.md:60 → 要求 root/sudo 权限<br>  - scripts/redteam-setup.sh:195 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - packages/redteam-ui/tools/assemble-client.mjs:1 → 修改系统目录 (1 处)<br>  - packages/redteam-ui/lib/index.js:565 → 修改系统目录 (1 处)<br>  - packages/redteam-store/bin/cli.mjs:1 → 修改系统目录 (1 处)<br>  - packages/redteam-store/lib/core.js:8193 → 修改系统目录 (1 处)<br>  - packages/redteam-store/lib/score-rules.js:507 → 修改系统目录 (1 处)<br>  ... 共 35 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: sandbox, 沙箱, 隔离, workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (16 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 17 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 2, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | lmtagent |
| 校验 URL | https://github.com/ECCVIK/lmtagent |
| 必查项通过率 | 16/33 (48%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-11-11 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
