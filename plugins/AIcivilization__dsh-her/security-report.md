# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/AIcivilization/dsh-her
- **校验时间**: 2026-11-14 05:30:16
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 20 | 8 | 5 |
| 🟡 推荐 | 14 | 7 | 7 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2026-03-16 (242 天前); 公开仓库数: 42; 粉丝数: 1 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 181; 包名: dsh-her; 描述: A desktop companion for DeepSeek Harness (dsh): she lives on your real desktop ( — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (20): v0.8.5, v0.8.4, v0.8.3, v0.8.2, v0.8.1; package.json version: 0.8.5; GitHub Releases (5): v0.8.5, v0.8.3, v0.8.2, v0.8.1, v0.8.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.1; engines: {"node": ">=22.18", "dsh": ">=0.2.0-0 <0.3.0-0"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ✅ 通过 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "immediately": true}, "cat; Cordis/DSH 依赖: @deepseek-ai/cordis; Cordis 配置文件: cordis.patch.yml |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 322 处, 函数: 2794 个, 比例: 11.5% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: body/renderer/mic.ts; 发现清理逻辑: body/renderer/speech-player.ts; 发现清理逻辑: body/renderer/main.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - body/scripts/package.mjs:139 → 读取环境变量配置 (1 处)<br>  - body/main/index.ts:61 → 读取环境变量配置 (2 处)<br>  - body/main/brain-link.ts:54 → 读取环境变量配置 (2 处)<br>  - scripts/make-preset.mjs:69 → 读取环境变量配置 (1 处)<br>  - scripts/voice-bench.ts:20 → 读取环境变量配置 (1 处)<br>  ... 共 17 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - body/renderer/talk-bar.ts:11 → 深层目录穿越 (1 处)<br>  - body/renderer/speech-player.ts:11 → 深层目录穿越 (1 处)<br>  - body/renderer/main.ts:27 → 深层目录穿越 (3 处)<br>  - body/scripts/make-test-pack.mjs:17 → 读取用户主目录 (1 处)<br>  - body/scripts/make-dev-pack.mjs:43 → 读取用户主目录 (2 处)<br>  ... 共 30 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package-lock.json:35 → 探测到 HTTP(S) 网络请求 (46 处)<br>  - package.json:26 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - README.md:3 → 探测到 HTTP(S) 网络请求 (7 处)<br>  - .github/workflows/release-windows.yml:38 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - .github/workflows/ci.yml:98 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: 127.0.0.1, a, a.b, evil.example, example.com, ffmpeg.org, gh-proxy.com, ghfast.top, github.com, help.aliyun.com (+14 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - src/dsh/plugin.ts:1181 → 挖矿相关 (4 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - README.md:63 → API Key / Token 读取 (1 处)<br>  - body/scripts/package.mjs:139 → 读取环境变量 API Key/凭证 (1 处)<br>  - body/main/index.ts:61 → 读取环境变量 API Key/凭证 (2 处)<br>  - body/main/brain-link.ts:54 → 读取环境变量 API Key/凭证 (2 处)<br>  - tests/web-body.test.ts:35 → 敏感凭证读取 (4 处)<br>  ... 共 44 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - src/dsh/initiative.ts:71 → 写入配置文件 (1 处)<br>  - src/dsh/plugin.ts:1142 → 写入配置文件 (1 处)<br>  - src/voice/ming-voices.ts:138 → 写入配置文件 (1 处)<br>  - src/voice/ming-audiocpp.ts:383 → 写入配置文件 (1 处)<br>  - src/pack/settings.ts:45 → 写入配置文件 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 9 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - body/renderer/bubble.ts:93 → 定时任务 (1 处)<br>  - body/renderer/mic.ts:67 → 定时任务 (1 处)<br>  - body/renderer/intro.html:14 → 定时任务 (1 处)<br>  - body/renderer/player.ts:65 → 定时任务 (3 处)<br>  - body/renderer/speech-player.ts:149 → 定时任务 (1 处)<br>  ... 共 43 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - .github/workflows/release-windows.yml:2 → 云存储上传 (3 处)<br>  - .github/workflows/ci.yml:119 → 云存储上传 (1 处)<br>  - tests/web-body.test.ts:10 → 云存储上传 (15 处)<br>  - tests/material-guide.test.ts:15 → 云存储上传 (1 处)<br>  - tests/library.test.ts:23 → 云存储上传 (1 处)<br>  ... 共 24 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 9. repo: 2 deps + 7 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 25327, 注释行: 2974 (11.7%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 41 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - tests/external-voice.test.ts:20 → 硬编码敏感信息 (1 处)<br>  - src/voice/external.ts:89 → 硬编码敏感信息 (1 处)<br>  - src/client/chat-mode.ts:53 → 明文写入敏感信息 (1 处)<br>  - src/client/web-float.ts:80 → 明文写入敏感信息 (1 处)<br>  - src/client/MaterialGuide.tsx:81 → 明文写入敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (26 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (1 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - .github/workflows/ci.yml:69 → 要求 root/sudo 权限<br>  - docs/VPS部署.md:65 → 要求 root/sudo 权限<br>  - src/dsh/ffmpeg-fetch.ts:68 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - .github/workflows/ci.yml:69 → 修改系统目录 (1 处)<br>  - body/scripts/make-test-pack.mjs:25 → 修改系统目录 (1 处)<br>  - body/scripts/package.mjs:51 → 修改系统目录 (4 处)<br>  - tests/web-body.test.ts:35 → 修改系统目录 (2 处)<br>  - tests/presets.test.ts:22 → 修改系统目录 (2 处)<br>  ... 共 12 处 |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (2 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 59 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-her |
| 校验 URL | https://github.com/AIcivilization/dsh-her |
| 必查项通过率 | 20/33 (61%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-11-14 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
