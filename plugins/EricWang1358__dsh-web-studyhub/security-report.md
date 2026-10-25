# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/EricWang1358/dsh-web-studyhub
- **校验时间**: 2026-10-25 03:50:04
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 11 | 12 | 10 |
| 🟡 推荐 | 14 | 8 | 6 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2023-01-10 (1383 天前); 公开仓库数: 27; 粉丝数: 5 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 4524; 包名: @ericwang1358/dsh-daily-flashcard; 描述: StudyHub: turn your lecture slides into questions that each link back to their p — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - lib/study-contracts.js:23 → 盗版/侵权 (1 处)<br>  - tests/wp12-grading.test.mjs:25 → 欺诈行为 (4 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (20): v3.6.2, v3.6.1, v3.6.0, v3.5.7, v3.5.6; package.json version: 3.6.2; GitHub Releases (5): v3.6.2, v3.6.1, v3.6.0, v3.5.7, v3.5.6 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/dsh-llm: >=0.2.0-rc.2 <0.3; @deepseek-ai/dsh-tools: >=0.2.0-rc.2 <0.3; engines: {"node": ">=22.19"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": ["./cordis.patch.yml", "./presets/study.patch.yml", "./presets/study-worker.pat; Cordis/DSH 依赖: @deepseek-ai/dsh-llm, @deepseek-ai/dsh-tools; Cordis 配置文件: cordis.patch.yml<br>  - lib/generation.js:664 → Monkey patch / prototype pollution<br>  - lib/store.js:61 → Monkey patch / prototype pollution<br>  - lib/study-contracts.js:27 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 2929 处, 函数: 52046 个, 比例: 5.6% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: lib/host-capabilities.js; 发现清理逻辑: lib/generation-agent.js; 发现清理逻辑: lib/coverage-run.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .gitignore:7 → 读取环境变量配置 (1 处)<br>  - web-demo/store.js:24 → 读取浏览器 Cookie/本地存储 (5 处)<br>  - lib/audio-dashboard.js:8 → 读取环境变量配置 (1 处)<br>  - lib/jev-providers.js:65 → 读取环境变量配置 (2 处)<br>  - lib/update-install.js:22 → 读取环境变量配置 (1 处)<br>  ... 共 343 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - lib/audio-dashboard.js:8 → 读取用户主目录 (1 处)<br>  - lib/update-install.js:22 → 读取用户主目录 (1 处)<br>  - lib/experimental.js:17 → 读取用户主目录 (1 处)<br>  - lib/notebooks.js:24 → 读取用户主目录 (1 处)<br>  - lib/marker-local.js:18 → 读取用户主目录 (1 处)<br>  ... 共 483 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - lib/marker-external.js:84 → Python subprocess (1 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - lib/card-autofix.js:137 → exec 命令拼接 (1 处)<br>  - lib/marker-install.js:117 → 命令字符串拼接变量 (注入风险) (1 处)<br>  - lib/math-text.js:21 → exec 命令拼接 (1 处)<br>  - lib/tex-text.js:51 → exec 命令拼接 (1 处)<br>  - lib/mineru-install.js:314 → 命令字符串拼接变量 (注入风险) (2 处)<br>  ... 共 8 处 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package-lock.json:66 → 探测到 HTTP(S) 网络请求 (507 处)<br>  - CHANGELOG.md:231 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - CHANGELOG.zh-CN.md:231 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - README.zh-CN.md:9 → 探测到 HTTP(S) 网络请求 (15 处)<br>  - README.md:9 → 探测到 HTTP(S) 网络请求 (14 处)<br>涉及的域名: 127.0.0.1, 192.168.1.5, Gateway.Example.com, ai.google.dev, aistudio.google.com, aka.ms, api-docs.deepseek.com, api.deepseek.com, api.github.com, api.groq.com (+81 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - CHANGELOG.md:23 → 挖矿相关 (48 处)<br>  - CHANGELOG.zh-CN.md:23 → 挖矿相关 (46 处)<br>  - README.zh-CN.md:81 → 挖矿相关 (10 处)<br>  - README.md:81 → 挖矿相关 (10 处)<br>  - package.json:75 → 挖矿相关 (2 处)<br>  ... 共 289 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - CHANGELOG.md:87 → API Key / Token 读取 (3 处)<br>  - CHANGELOG.md:370 → 敏感凭证读取 (1 处)<br>  - CHANGELOG.zh-CN.md:87 → API Key / Token 读取 (2 处)<br>  - README.zh-CN.md:165 → API Key / Token 读取 (4 处)<br>  - README.md:165 → API Key / Token 读取 (4 处)<br>  ... 共 547 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - lib/mineru-install.js:101 → 写入配置文件 (1 处)<br>  - tests/store-extensions.test.mjs:80 → 写入配置文件 (1 处)<br>  - tests/wp16-effort.test.mjs:127 → 写入配置文件 (2 处)<br>  - tests/jev-settings.test.mjs:81 → 写入配置文件 (1 处)<br>  - tests/jev-providers.test.mjs:75 → 写入配置文件 (2 处)<br>  ... 共 11 处 — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - lib/office/ppt.js:63 → 连续十六进制转义 (混淆) (1 处)<br>  - ui/document-preview/peek/assets/fonts.js:3 → 超长 base64 字符串 (2 处)<br>  - ui/document-preview/peek/assets/cmaps-korea.js:3 → 超长 base64 字符串 (20 处)<br>  - ui/document-preview/peek/assets/wasm-jbig2.js:3 → 超长 base64 字符串 (1 处)<br>  - ui/document-preview/peek/assets/wasm-openjpeg.js:3 → 超长 base64 字符串 (1 处)<br>  ... 共 11 处 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - tests/retry-generation.test.mjs:21 → new Function() 任意代码执行 (1 处)<br>  - tests/document-preview.test.mjs:48 → new Function() 任意代码执行 (1 处)<br>  - tests/wp25-exam-formats.test.mjs:18 → new Function() 任意代码执行 (1 处)<br>  - tests/study-markdown.test.mjs:10 → new Function() 任意代码执行 (1 处)<br>  - tests/wave3-s2-inbox-preview.test.mjs:15 → new Function() 任意代码执行 (1 处)<br>  ... 共 193 处 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 33 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - lib/model-retry.js:30 → 定时任务 (2 处)<br>  - lib/mineru-history.js:10 → 临时文件操作 (1 处)<br>  - lib/job-parallel.js:117 → 定时任务 (2 处)<br>  - lib/section-weights.js:63 → 定时任务 (1 处)<br>  - lib/audio-pool.js:30 → 定时任务 (3 处)<br>  ... 共 369 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - CHANGELOG.md:17 → 云存储上传 (6 处)<br>  - eslint.config.js:49 → 云存储上传 (9 处)<br>  - README.md:152 → 云存储上传 (3 处)<br>  - lib/audio-dashboard.js:115 → 云存储上传 (2 处)<br>  - lib/subtitle-job.js:15 → 云存储上传 (1 处)<br>  ... 共 178 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 33. repo: 13 deps + 20 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 271770, 注释行: 15927 (5.9%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - lib/course-book-inputs.js:23 → 明文写入敏感信息 (1 处)<br>  - lib/contexts/generation/outline/describe.js:74 → 明文写入敏感信息 (1 处)<br>  - lib/contexts/audio/convert.js:268 → 从环境变量获取敏感信息 (2 处)<br>  - ui/i18n.js:173 → 明文写入敏感信息 (1 处)<br>  - scripts/qa/original-shots.mjs:37 → 明文写入敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - scripts/changelog.mjs:18 → 读取 git 历史 (1 处)<br>  - scripts/qa/dead-css.mjs:3 → 读取 git 历史 (1 处)<br>  - docs/verification.md:81 → 读取 git 历史 (1 处)<br>  - docs/plans/2026-10-07-1834-feat-exam-blueprint-3.1-plan.md:380 → 读取 git 历史 (4 处)<br>  - docs/plans/unified-job-runtime/s1-1-compatibility-implementation.md:43 → 读取 git 历史 (2 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (138 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (7 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - ui/MarkerInstall.jsx:30 → 要求 root/sudo 权限<br>  - ui/locales/en.marker-install.json:13 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - CHANGELOG.md:433 → 创建开机自启/系统服务 (2 处)<br>  - lib/assistant-boundary.js:19 → 创建开机自启/系统服务 (1 处)<br>  - lib/mineru-local.js:116 → 创建开机自启/系统服务 (4 处)<br>  - lib/usage-frequency-operations.js:6 → 修改系统目录 (2 处)<br>  - lib/batch.js:39 → 创建开机自启/系统服务 (3 处)<br>  ... 共 75 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (34 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 1961 |
| 7.2 | 未标记停止维护 | 必查 | ❌ 不通过 | 文档中发现弃用标记: archived |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ✅ 通过 | Stars: 138, Forks: 4, Watchers: 0 — 高 Star 量 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-web-studyhub |
| 校验 URL | https://github.com/EricWang1358/dsh-web-studyhub |
| 必查项通过率 | 11/33 (33%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-25 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
