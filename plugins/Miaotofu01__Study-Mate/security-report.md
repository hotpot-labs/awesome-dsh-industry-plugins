# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/Miaotofu01/Study-Mate
- **校验时间**: 2026-09-25 04:01:07
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 15 | 13 | 5 |
| 🟡 推荐 | 14 | 9 | 5 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2025-01-27 (605 天前); 公开仓库数: 6; 粉丝数: 7 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 603; 包名: @yunmiao/studymate; 描述: StudyMate learning skills and lesson engine for DeepSeek Harness, Codex and Chat — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - scripts/render_lesson.py:129 → 破解授权 (1 处)<br>  - scripts/tests/test_render_lesson.py:1201 → 破解授权 (1 处)<br>  - docs/课件内容格式.md:84 → 破解授权 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (6): v0.2.0, v0.1.5, v0.1.4, v0.1.3, v0.1.2; package.json version: 0.2.0; GitHub Releases (5): v0.2.0, v0.1.5, v0.1.4, v0.1.3, v0.1.2 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | engines: {"node": "^22.19.0 \|\| >=24.0.0"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}}; Cordis 配置文件: cordis.patch.yml<br>  - scripts/install_preset.py:93 → Monkey patch / prototype pollution<br>  - scripts/tests/test_dsh_presets.py:284 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 122 处, 函数: 1604 个, 比例: 7.6% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: examples/.learning/assets/sayo/sayo.js; 发现清理逻辑: templates/assets/sayo/sayo.js; 发现清理逻辑: scripts/tests/test_dsh_plugin_cli.mjs |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - examples/.learning/subjects/linear-algebra/assets/lesson-toc.js:44 → 读取浏览器 Cookie/本地存储 (2 处)<br>  - examples/.learning/subjects/computer-networks/assets/lesson-toc.js:44 → 读取浏览器 Cookie/本地存储 (2 处)<br>  - templates/assets/lesson-toc.js:44 → 读取浏览器 Cookie/本地存储 (2 处)<br>  - scripts/gen_home.py:372 → 读取环境变量配置 (3 处)<br>  - scripts/tests/test_openai_plugin.mjs:19 → 读取环境变量配置 (3 处)<br>  ... 共 20 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - examples/.learning/subjects/linear-algebra/index.html:10 → 深层目录穿越 (7 处)<br>  - examples/.learning/subjects/linear-algebra/RESOURCES.html:7 → 深层目录穿越 (4 处)<br>  - examples/.learning/subjects/linear-algebra/GLOSSARY.html:7 → 深层目录穿越 (4 处)<br>  - examples/.learning/subjects/linear-algebra/learning-records/0002-matrix.transform.html:7 → 深层目录穿越 (4 处)<br>  - examples/.learning/subjects/linear-algebra/sessions/2026-09-24.html:7 → 深层目录穿越 (4 处)<br>  ... 共 52 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - scripts/preview_templates.py:440 → Python subprocess (2 处)<br>  - scripts/install_preset.py:62 → Python subprocess (1 处)<br>  - scripts/renumber_lessons.py:265 → Python subprocess (1 处)<br>  - scripts/tests/test_dsh_presets.py:53 → Python subprocess (2 处)<br>  - scripts/tests/test_lesson_scripts.py:92 → Python subprocess (1 处)<br>  ... 共 9 处<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - CHANGELOG.md:4 → 探测到 HTTP(S) 网络请求 (87 处)<br>  - README.md:8 → 探测到 HTTP(S) 网络请求 (8 处)<br>  - package.json:53 → 探测到 HTTP(S) 网络请求 (4 处)<br>  - examples/.learning/assets/sayo/sayo.css:137 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - examples/.learning/assets/sayo/icons/doc-components.svg:1 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: 127.0.0.1, api.github.com, api.star-history.com, ask.wireshark.org, developer.mozilla.org, docs.github.com, docs.npmjs.com, docs.python.org, docs.sympy.org, en.cppreference.com (+27 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - .github/workflows/ci.yml:24 → 敏感凭证读取 (1 处)<br>  - scripts/tests/probe_bundle.mjs:58 → 读取环境变量 API Key/凭证 (5 处)<br>  - scripts/tests/probe_bundle.mjs:34 → 敏感凭证读取 (1 处)<br>  - scripts/tests/test_dsh_plugin_cli.mjs:17 → 读取环境变量 API Key/凭证 (11 处)<br>  - scripts/tests/test_bundle.mjs:35 → 读取环境变量 API Key/凭证 (1 处)<br>  ... 共 13 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - scripts/install_preset.py:257 → 修改全局配置 (1 处)<br>  - scripts/tests/test_dsh_plugin_cli.mjs:73 → 写入配置文件 (2 处)<br>  - scripts/tests/test_dsh_plugin_cli.mjs:73 → 写入 DSH 配置 (2 处)<br>  - scripts/tests/test_bundle.mjs:87 → 写入配置文件 (2 处)<br>  - scripts/tests/test_bundle.mjs:87 → 写入 DSH 配置 (2 处)<br>  ... 共 11 处 — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - scripts/tests/test_dsh_presets.py:322 → new Function() 任意代码执行 (1 处)<br>  - scripts/tests/quiz_dom_test.js:62 → node:vm 任意代码执行 (1 处)<br>  - scripts/tests/toc_dom_test.js:105 → node:vm 任意代码执行 (2 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 0 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - examples/index.html:428 → 定时任务 (3 处)<br>  - examples/.learning/assets/sayo/sayo.js:125 → 定时任务 (12 处)<br>  - templates/home-index.html:387 → 定时任务 (3 处)<br>  - templates/assets/sayo/sayo.js:125 → 定时任务 (12 处)<br>  - .dsh/skills/curriculum-designer/SKILL.md:76 → 临时文件操作 (3 处)<br>  ... 共 59 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - scripts/release/release.test.mjs:159 → 云存储上传 (20 处)<br>  - scripts/release/release.mjs:260 → 云存储上传 (23 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 无第三方依赖 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 21449, 注释行: 853 (4.0%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - examples/index.html:476 → 明文写入敏感信息 (1 处)<br>  - examples/.learning/assets/learn-theme.js:67 → 明文写入敏感信息 (1 处)<br>  - examples/.learning/subjects/linear-algebra/index.html:895 → 明文写入敏感信息 (1 处)<br>  - examples/.learning/subjects/linear-algebra/assets/lesson-toc.js:49 → 明文写入敏感信息 (1 处)<br>  - examples/.learning/subjects/computer-networks/index.html:903 → 明文写入敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - scripts/tests/test_openai_skills.mjs:13 → 读取文档/压缩文件 (2 处)<br>  - scripts/tests/test_bundle.mjs:79 → 读取文档/压缩文件 (1 处)<br>  - scripts/tests/test_installer.mjs:119 → 遍历用户目录 (1 处)<br>  - scripts/tests/test_openai_skill_ui.mjs:57 → 读取文档/压缩文件 (1 处)<br>  - docs/learning-discovery-validation.md:20 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (15 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (9 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - openai/studymate/scripts/interaction_state.py:1 → 修改系统目录 (1 处)<br>  - scripts/check_lesson.py:1 → 修改系统目录 (1 处)<br>  - scripts/preview_templates.py:1 → 修改系统目录 (1 处)<br>  - scripts/check_skill.py:1 → 修改系统目录 (1 处)<br>  - scripts/gen_home.py:1 → 修改系统目录 (1 处)<br>  ... 共 28 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (5 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 258 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ✅ 通过 | Stars: 272, Forks: 18, Watchers: 1 — 高 Star 量 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | Study-Mate |
| 校验 URL | https://github.com/Miaotofu01/Study-Mate |
| 必查项通过率 | 15/33 (45%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-09-25 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
