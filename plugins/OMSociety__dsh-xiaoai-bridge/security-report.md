# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/OMSociety/dsh-xiaoai-bridge
- **校验时间**: 2026-10-17 03:38:51
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 14 | 12 | 7 |
| 🟡 推荐 | 14 | 8 | 6 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2021-06-14 (1950 天前); 公开仓库数: 21; 粉丝数: 4 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 2190; 包名: dsh-xiaoai-bridge; 描述: XiaoAI speaker bridge for DeepSeek Harness: wake word, speech capture, DSH conve — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - DISCLAIMER.md:5 → 盗版/侵权 (2 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (1): v1.0.0; package.json version: 1.0.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.4; @deepseek-ai/dsh-agent: ^0.2.0-rc.1; @deepseek-ai/dsh-api-remotes: ^0.2.0-rc.1; @deepseek-ai/dsh-client-ui-plugin-manager: ^0.2.0-rc.1; @deepseek-ai/dsh-client-ui-primitives: ^0.2.0-rc.1 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": ["@deepseek-ai/dsh-client-ui-plugin; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-agent, @deepseek-ai/dsh-api-remotes, @deepseek-ai/dsh-client-ui-plugin-manager, @deepseek-ai/dsh-client-ui-primitives; Cordis 配置文件: cordis.patch.yml<br>  - bridge/tests/test_api_server_auth.py:98 → Monkey patch / prototype pollution<br>  - bridge/tests/test_sherpa_asr_load.py:123 → Monkey patch / prototype pollution<br>  - bridge/tests/test_wakeup_kws_pairing.py:96 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 200 处, 函数: 1240 个, 比例: 16.1% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: lib/exposure.js; 发现清理逻辑: lib/auto-speak.js; 发现清理逻辑: lib/index.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - CONTRIBUTING.md:69 → 读取凭证文件 (1 处)<br>  - .gitignore:52 → 读取环境变量配置 (2 处)<br>  - .gitignore:90 → 读取凭证文件 (2 处)<br>  - AGENTS.md:101 → 读取凭证文件 (1 处)<br>  - .npmignore:25 → 读取凭证文件 (1 处)<br>  ... 共 26 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - bridge/core/services/audio/kws/keywords.py:11 → 深层目录穿越 (1 处)<br>  - bridge/core/services/audio/kws/__init__.py:126 → 深层目录穿越 (1 处)<br>  - lib/index.js:121 → 读取用户主目录 (1 处)<br>  - lib/session.js:354 → 读取用户主目录 (1 处)<br>  - docs/agents/change-contract.md:3 → 深层目录穿越 (6 处)<br>  ... 共 7 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - bridge/tests/test_tts.py:85 → Python subprocess (2 处)<br>  - bridge/skills/xiaoai-tts/tools/xiaoai-tts:25 → Python subprocess (2 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - CHANGELOG.md:7 → 探测到 HTTP(S) 网络请求 (4 处)<br>  - CONTRIBUTING.md:75 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - icon.svg:1 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - README.md:2 → 探测到 HTTP(S) 网络请求 (23 处)<br>  - README.md:184 → WebSocket 连接 (4 处)<br>涉及的域名: 127.0.0.1, 192.168.3.6, 192.168.x.x, api.openai.com, console.volcengine.com, evil.example, example.com, github.com, host, img.shields.io (+10 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - CHANGELOG.md:41 → 敏感凭证读取 (2 处)<br>  - CONTRIBUTING.md:69 → 敏感凭证读取 (1 处)<br>  - .gitignore:90 → 敏感凭证读取 (2 处)<br>  - AGENTS.md:55 → 敏感凭证读取 (2 处)<br>  - .npmignore:25 → 敏感凭证读取 (1 处)<br>  ... 共 64 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - cordis.patch.yml:5 → 修改设置 (1 处)<br>  - lib/http.js:548 → 修改设置 (1 处)<br>  - scripts/check-cleanup.mjs:38 → 写入配置文件 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - bridge/tests/test_doubao_asr.py:9 → 连续十六进制转义 (混淆) (1 处) |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - bridge/native/src/python.rs:74 → eval() 任意代码执行 (1 处)<br>  - tools/render-outline.mjs:18 → node:vm 任意代码执行 (1 处)<br>  - scripts/check-client.mjs:54 → node:vm 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 14 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - bridge/core/services/speaker.py:225 → 临时文件操作 (1 处)<br>  - lib/ports.js:46 → 定时任务 (1 处)<br>  - lib/bridge.js:185 → 定时任务 (1 处)<br>  - lib/index.js:874 → 定时任务 (1 处)<br>  - lib/process.js:86 → 定时任务 (3 处)<br>  ... 共 25 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - bridge/native/src/tts/mod.rs:1038 → 云存储上传 (1 处)<br>  - bridge/core/services/api_server.py:363 → multipart 上传 (2 处)<br>  - bridge/core/services/api_server.py:361 → 云存储上传 (3 处)<br>  - bridge/skills/xiaoai-tts/scripts/play_file.py:29 → multipart 上传 (2 处)<br>  - lib/http.js:94 → 云存储上传 (2 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 1. repo: 1 deps + 0 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 28683, 注释行: 4506 (15.7%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - bridge/tests/test_mlx_audio_tts.py:107 → 硬编码敏感信息 (1 处)<br>  - bridge/tests/test_skill_api_client.py:50 → 从环境变量获取敏感信息 (1 处)<br>  - bridge/tests/test_openai.py:51 → 硬编码敏感信息 (1 处)<br>  - bridge/tests/test_openai_tts.py:62 → 硬编码敏感信息 (1 处)<br>  - bridge/skills/xiaoai-tts/SKILL.md:16 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - CONTRIBUTING.md:81 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (50 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (5 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - bridge/scripts/clone_voice.py:1 → 修改系统目录 (1 处)<br>  - bridge/scripts/generate_tts.py:1 → 修改系统目录 (1 处)<br>  - bridge/tests/test_tts.py:1 → 修改系统目录 (1 处)<br>  - bridge/tests/test_tts_latency.py:1 → 修改系统目录 (1 处)<br>  - bridge/tests/test_tts_stream.py:1 → 修改系统目录 (1 处)<br>  ... 共 19 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: 沙箱 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (6 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 5 天; 提交总数: 235 |
| 7.2 | 未标记停止维护 | 必查 | ❌ 不通过 | 文档中发现弃用标记: archived |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 2, Forks: 0, Watchers: 1 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-xiaoai-bridge |
| 校验 URL | https://github.com/OMSociety/dsh-xiaoai-bridge |
| 必查项通过率 | 14/33 (42%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-17 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
