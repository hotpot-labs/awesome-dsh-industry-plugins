# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/CNSeniorious000/dsh-generative-ui
- **校验时间**: 2026-08-30 04:22:26
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 14 | 13 | 6 |
| 🟡 推荐 | 14 | 6 | 7 | 1 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2020-11-16 (2113 天前); 公开仓库数: 115; 粉丝数: 164 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 717; 包名: dsh-generative-ui; 描述: Generative UI for DeepSeek Harness — the agent writes TSX, dsh web renders it li — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - .research/findings-r2-r4.json:5 → 盗版/侵权 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (2): v0.0.2, v0.0.1; package.json version: 0.0.2 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.1; @deepseek-ai/dsh-client-locale: ^0.1.0-rc.7; @deepseek-ai/dsh-client-runtime: ^0.1.0-rc.7; @deepseek-ai/dsh-client-ui-conversation: ^0.1.0-rc.7; @deepseek-ai/dsh-client-ui-slots: ^0.1.0-rc.7 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": ["@deepseek-ai/dsh-client-runtime",; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-client-locale, @deepseek-ai/dsh-client-runtime, @deepseek-ai/dsh-client-ui-conversation, @deepseek-ai/dsh-client-ui-slots; Cordis 配置文件: cordis.patch.yml<br>  - CLAUDE.md:261 → Monkey patch / prototype pollution<br>  - eval/card-driver.mjs:187 → Monkey patch / prototype pollution<br>  - test/canvas-sweep.test.ts:196 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 116 处, 函数: 2009 个, 比例: 5.8% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: src/index.ts; 发现清理逻辑: src/client/index.ts; 发现清理逻辑: src/client/canvas/index.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - src/client/runtime/state.ts:35 → 读取浏览器 Cookie/本地存储 (2 处)<br>  - eval/turns-runner.mjs:104 → 读取环境变量配置 (1 处)<br>  - eval/wave.py:29 → 读取环境变量配置 (5 处)<br>  - eval/judge.py:40 → 读取环境变量配置 (2 处)<br>  - eval/build-compare.py:26 → 读取环境变量配置 (1 处)<br>  ... 共 25 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - src/client/canvas/collect.ts:14 → 深层目录穿越 (1 处)<br>  - src/client/canvas/read.ts:7 → 深层目录穿越 (1 处)<br>  - src/client/canvas/CanvasPanel.tsx:11 → 深层目录穿越 (1 处)<br>  - src/client/runtime/segments.ts:8 → 深层目录穿越 (1 处)<br>  - src/client/runtime/compiler.ts:4 → 深层目录穿越 (1 处)<br>  ... 共 14 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - eval/wave.py:97 → Python subprocess (2 处)<br>  - scripts/ab-rule.sh:32 → Python subprocess (1 处)<br>  - scripts/run-wave.py:111 → Python subprocess (2 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package.json:135 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - README.md:3 → 探测到 HTTP(S) 网络请求 (8 处)<br>  - src/index.ts:124 → 探测到 HTTP(S) 网络请求 (7 处)<br>  - src/skill.ts:16 → 探测到 HTTP(S) 网络请求 (4 处)<br>  - src/client/index.ts:146 → fetch 网络请求 (1 处)<br>涉及的域名: 127.0.0.1, 34.177.103.253, a, docs.renovatebot.com, dsh-generative-ui.invalid, e.x, esm.sh, example.com, fonts.googleapis.com, fonts.gstatic.com (+11 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - docs/measurements-log.md:3286 → 挖矿相关 (5 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - CLAUDE.md:713 → API Key / Token 读取 (3 处)<br>  - CLAUDE.md:1183 → 敏感凭证读取 (1 处)<br>  - src/index.ts:392 → 敏感凭证读取 (2 处)<br>  - src/contract-assets.ts:14 → 敏感凭证读取 (1 处)<br>  - src/prompt.ts:100 → 敏感凭证读取 (2 处)<br>  ... 共 40 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - scripts/smoke.ts:53 → eval() 任意代码执行 (1 处)<br>  - scripts/smoke.ts:166 → new Function() 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 32 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - empty.tmp.ts:5 → 临时文件操作 (3 处)<br>  - CLAUDE.md:183 → 临时文件操作 (2 处)<br>  - package.json:67 → 临时文件操作 (1 处)<br>  - src/skill.ts:842 → 定时任务 (1 处)<br>  - src/client/canvas/mount.ts:49 → 定时任务 (1 处)<br>  ... 共 66 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - scripts/judge-cards.py:190 → 云存储上传 (1 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 32. repo: 5 deps + 27 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 19217, 注释行: 6045 (31.5%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 71 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - test/routes.test.ts:102 → 明文写入敏感信息 (3 处)<br>  - test/cards/piano.ui4a.tsx:54 → 明文写入敏感信息 (1 处)<br>  - test/fixtures/canvas/project-dashboard.ui4a.tsx:32 → 明文写入敏感信息 (1 处)<br>  - test/fixtures/canvas/project-dashboard/data.ts:108 → 明文写入敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - src/index.ts:76 → 读取 git 历史 (1 处)<br>  - src/skill.ts:852 → 读取 git 历史 (2 处)<br>  - src/prompt.ts:27 → 读取 git 历史 (4 处)<br>  - docs/examples.md:103 → 读取 git 历史 (21 处)<br>  - docs/demo.md:66 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (36 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (7 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - src/skill.ts:1137 → 创建开机自启/系统服务 (1 处)<br>  - docs/measurements-log.md:3409 → 修改系统目录 (3 处)<br>  - test/routes.test.ts:98 → 修改系统目录 (3 处)<br>  - test/contract.test.ts:39 → 修改系统目录 (2 处)<br>  - test/seed/setup.sh:1 → 修改系统目录 (1 处)<br>  ... 共 19 处 |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (11 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 1104 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ❌ 不通过 | 缺少文档: CHANGELOG, 配置说明, 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 1, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-generative-ui |
| 校验 URL | https://github.com/CNSeniorious000/dsh-generative-ui |
| 必查项通过率 | 14/33 (42%) |
| 推荐项满足率 | 13/14 (约 93%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-30 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
