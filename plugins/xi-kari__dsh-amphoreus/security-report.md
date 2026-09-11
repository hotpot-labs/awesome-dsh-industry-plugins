# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/xi-kari/dsh-amphoreus
- **校验时间**: 2026-09-11 03:39:50
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 17 | 10 | 6 |
| 🟡 推荐 | 14 | 6 | 7 | 1 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2022-06-08 (1555 天前); 公开仓库数: 11; 粉丝数: 1 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 2012; 包名: dsh-amphoreus; 描述: 翁法罗斯 × DSH：黄金裔席位工作区、技能无损桥接与画布工作台（基于 DeepSeek Harness 构建，非官方） — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (5): v0.3.0, v0.2.2, v0.2.1, v0.2.0, chapter-F; package.json version: 0.3.0; GitHub Releases (4): v0.3.0, v0.2.2, v0.2.1, v0.2.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.2; @deepseek-ai/dsh-home-paths: 0.1.2-alpha.4; @deepseek-ai/dsh-llm: 0.1.2-alpha.4; @deepseek-ai/dsh-skill: 0.1.2-alpha.4; @deepseek-ai/dsh-storage-domain: 0.1.2-alpha.4 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "immediately": false, "inj; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-home-paths, @deepseek-ai/dsh-llm, @deepseek-ai/dsh-skill, @deepseek-ai/dsh-storage-domain; Cordis 配置文件: cordis.patch.yml<br>  - tests/client-conference.test.ts:479 → Monkey patch / prototype pollution<br>  - tests/client-seat-sounds.test.ts:229 → Monkey patch / prototype pollution<br>  - tests/client-pipeline-rail.test.ts:30 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 442 处, 函数: 4694 个, 比例: 9.4% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: tests/client-seat-hotkeys.test.ts; 发现清理逻辑: tests/seat-prompt.test.ts; 发现清理逻辑: tests/observer.test.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - BUILD-LOG.md:1067 → 读取 npm 凭证 (6 处)<br>  - tsdown.config.ts:49 → 读取环境变量配置 (5 处)<br>  - HANDOFF.md:313 → 读取 npm 凭证 (2 处)<br>  - tests/suite-real.test.ts:9 → 读取环境变量配置 (1 处)<br>  - tests/stickers-webapi.test.ts:251 → 读取环境变量配置 (3 处)<br>  ... 共 13 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - tests/suite-real.test.ts:56 → 读取用户主目录 (2 处)<br>  - tests/host-derive.test.ts:137 → 深层目录穿越 (1 处)<br>  - tests/firewall-words.test.ts:141 → 读取用户主目录 (2 处)<br>  - docs/E2E-CHECKLIST.md:108 → 深层目录穿越 (1 处)<br>  - src/host/suite/roots.ts:53 → 读取用户主目录 (3 处) — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - BUILD-LOG.md:1092 → 开启 shell 模式 (注入风险) (2 处)<br>  - HANDOFF.md:60 → 开启 shell 模式 (注入风险) (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - BUILD-LOG.md:1065 → 探测到 HTTP(S) 网络请求 (7 处)<br>  - package.json:7 → 探测到 HTTP(S) 网络请求 (4 处)<br>  - package-lock.json:81 → 探测到 HTTP(S) 网络请求 (400 处)<br>  - NOTICE:3 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - README.md:3 → 探测到 HTTP(S) 网络请求 (13 处)<br>涉及的域名: 127.0.0.1, codeload.github.com, dsh.local, example.com, example.invalid, feross.org, github.com, imagemagick.org, img.shields.io, localhost (+7 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - BUILD-LOG.md:1114 → 敏感凭证读取 (3 处)<br>  - tsdown.config.ts:49 → 读取环境变量 API Key/凭证 (2 处)<br>  - package.json:160 → 敏感凭证读取 (1 处)<br>  - package-lock.json:263 → 敏感凭证读取 (5 处)<br>  - HANDOFF.md:306 → 敏感凭证读取 (2 处)<br>  ... 共 28 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - tests/webapi-assets-root.test.ts:299 → 修改全局配置 (4 处)<br>  - src/host/store.ts:216 → 修改全局配置 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - tests/derived-assets-webapi.test.ts:118 → 连续十六进制转义 (混淆) (1 处)<br>  - tests/stickers-webapi.test.ts:16 → 连续十六进制转义 (混淆) (3 处) |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - tests/workbench-ledger.test.ts:59 → node:vm 任意代码执行 (2 处)<br>  - tests/client-handoff-dock.test.ts:28 → node:vm 任意代码执行 (1 处)<br>  - tests/workbench-conference-panel.test.ts:62 → node:vm 任意代码执行 (2 处)<br>  - tests/client-portal.test.ts:165 → node:vm 任意代码执行 (1 处)<br>  - tests/workbench-bridge.test.ts:32 → node:vm 任意代码执行 (1 处)<br>  ... 共 23 处 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 52 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - BUILD-LOG.md:1180 → 临时文件操作 (4 处)<br>  - HANDOFF.md:170 → 临时文件操作 (1 处)<br>  - tests/webapi-assets-root.test.ts:82 → 开启监听端口 (1 处)<br>  - tests/webapi-assets-root.test.ts:30 → 定时任务 (1 处)<br>  - tests/derived-assets-webapi.test.ts:123 → 开启监听端口 (1 处)<br>  ... 共 53 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - tests/client-scheme-panel.test.ts:114 → 云存储上传 (1 处)<br>  - tests/client-send-sound.test.ts:54 → 云存储上传 (3 处)<br>  - tests/custom-wallpapers.test.ts:41 → 云存储上传 (9 处)<br>  - tests/seat-sounds.test.ts:91 → 云存储上传 (16 处)<br>  - tests/client-seat-sounds.test.ts:132 → 云存储上传 (3 处)<br>  ... 共 20 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ❌ 不通过 | 总依赖数: 52. repo: 2 deps + 50 devDeps — 依赖过多 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 40626, 注释行: 1601 (3.9%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 100 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ✅ 通过 | 未检测到明文存储敏感信息 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - BUILD-LOG.md:126 → 读取 git 历史 (43 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (23 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (2 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - scripts/path-b.sh:1 → 修改系统目录 (2 处) |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (3 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 5 天; 提交总数: 137 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 2, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-amphoreus |
| 校验 URL | https://github.com/xi-kari/dsh-amphoreus |
| 必查项通过率 | 17/33 (52%) |
| 推荐项满足率 | 13/14 (约 93%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-09-11 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
