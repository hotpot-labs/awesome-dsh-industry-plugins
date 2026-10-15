# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/HerTa-st/Herta-dsh
- **校验时间**: 2026-10-15 03:45:57
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 14 | 12 | 7 |
| 🟡 推荐 | 14 | 6 | 8 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ⚠️  需人工复核 | 账号注册: 2026-09-30 (14 天前); 公开仓库数: 5; 粉丝数: 2; ⚠️ 账号注册不足 30 天 (14 天) |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 4790; 包名: dsh-herta; 描述: Installs Herta (黑塔) as a DeepSeek Harness agent — persona, memory, narrative lay — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - preset/herta.patch.yml:134 → 欺诈行为 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (10): v0.1.10, v0.1.9, v0.1.8, v0.1.7, v0.1.6; package.json version: 0.1.10; GitHub Releases (5): v0.1.10, v0.1.9, v0.1.8, v0.1.7, v0.1.6 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | dsh-theme-herta: ^0.1.0; engines: {"node": ">=20", "dsh": ">=0.1.7-rc.1 <0.3.0-0"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"manifestVersion": 1, "bundle": {"patch": ["./cordis.patch.yml", "./preset/herta.patch.yml"]}, "cli; Cordis/DSH 依赖: dsh-theme-herta; Cordis 配置文件: cordis.patch.yml<br>  - lib/minimax/pipeline.js:235 → Monkey patch / prototype pollution<br>  - lib/herta-ui/assets/pdf.worker.min.mjs:26 → Monkey patch / prototype pollution<br>  - src/host/minimax/pipeline.ts:235 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 676 处, 函数: 3332 个, 比例: 20.3% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: lib/client.js; 发现清理逻辑: lib/mimo-tts.js; 发现清理逻辑: lib/voice-model.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - lib/narrative-beacon.js:40 → 读取环境变量配置 (1 处)<br>  - lib/tts-runtime.js:75 → 读取环境变量配置 (3 处)<br>  - lib/index.js:28 → 读取环境变量配置 (3 处)<br>  - lib/mimo-tts.js:18 → 读取环境变量配置 (2 处)<br>  - lib/voice-model.js:68 → 读取环境变量配置 (1 处)<br>  ... 共 40 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - lib/narrative-beacon.js:40 → 读取用户主目录 (1 处)<br>  - lib/voice-model.js:68 → 读取用户主目录 (1 处)<br>  - lib/minimax/state.js:68 → 读取用户主目录 (1 处)<br>  - theme/dsh-theme-herta/NOTICE.md:18 → 深层目录穿越 (1 处)<br>  - theme/dsh-theme-herta/lib/opening/pick-opening-segment.js:5 → 深层目录穿越 (1 处)<br>  ... 共 19 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - scripts/preflight-release.mjs:77 → 开启 shell 模式 (注入风险) (2 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - NOTICE.md:33 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - package-lock.json:23 → 探测到 HTTP(S) 网络请求 (91 处)<br>  - THIRD-PARTY.md:8 → 探测到 HTTP(S) 网络请求 (4 处)<br>  - README.md:3 → 探测到 HTTP(S) 网络请求 (9 处)<br>  - package.json:8 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: 127.0.0.1, a, api.fish.audio, api.minimax.io, api.minimaxi.com, api.xiaomimimo.com, b, cfg, env, example.com (+19 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - lib/herta-ui/openings/b-1.json:1 → DDoS 攻击 (1 处)<br>  - theme/dsh-theme-herta/lib/opening-segments/b-1.json:1 → DDoS 攻击 (1 处)<br>  - assets/tts-runtime/LICENSES/espeak-ng-LICENSE.txt:323 → 挖矿相关 (1 处)<br>  - assets/tts-runtime/LICENSES/sherpa-onnx-LICENSE.txt:163 → 挖矿相关 (1 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - README.md:611 → API Key / Token 读取 (7 处)<br>  - README.md:64 → 敏感凭证读取 (4 处)<br>  - lib/voice-settings-shared.js:46 → API Key / Token 读取 (2 处)<br>  - lib/voice-settings-shared.js:46 → 敏感凭证读取 (1 处)<br>  - lib/narrative-beacon.js:40 → 读取环境变量 API Key/凭证 (1 处)<br>  ... 共 89 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - lib/tts-runtime.js:130 → 写入配置文件 (2 处)<br>  - src/host/tts-runtime.js:130 → 写入配置文件 (2 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - lib/herta-ui/openings/b-0.json:1 → 超长 base64 字符串 (1 处)<br>  - lib/herta-ui/openings/c-1.json:1 → 超长 base64 字符串 (1 处)<br>  - lib/herta-ui/openings/c-0.json:1 → 超长 base64 字符串 (1 处)<br>  - lib/herta-ui/openings/b-1.json:1 → 超长 base64 字符串 (1 处)<br>  - theme/dsh-theme-herta/lib/opening-segments/b-0.json:1 → 超长 base64 字符串 (1 处)<br>  ... 共 8 处 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 4 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - lib/tts-runtime.js:146 → 定时任务 (4 处)<br>  - lib/client.js:606 → 定时任务 (6 处)<br>  - lib/mimo-tts.js:324 → 定时任务 (1 处)<br>  - lib/voice-model.js:158 → 定时任务 (1 处)<br>  - lib/fish-fetch.cjs:74 → 定时任务 (1 处)<br>  ... 共 98 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - lib/minimax/api.js:8 → 云存储上传 (3 处)<br>  - theme/dsh-theme-herta/lib/opening/opening-draw.worker.js:80 → 云存储上传 (3 处)<br>  - src/host/minimax/api.ts:8 → 云存储上传 (3 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 4. repo: 1 deps + 3 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 62254, 注释行: 15350 (24.7%) |
| 4.9 | 具备测试覆盖 | 推荐 | ⚠️  需人工复核 | 未发现测试文件 |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - README.md:618 → 硬编码敏感信息 (1 处)<br>  - theme/dsh-theme-herta/lib/theme.js:116 → 明文写入敏感信息 (1 处)<br>  - scripts/test-fish-key.mjs:44 → 明文写入敏感信息 (3 处)<br>  - scripts/test-mimo-tts.mjs:90 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - .prettierignore:7 → 读取 git 历史 (1 处)<br>  - AGENTS.md:12 → 读取 git 历史 (2 处)<br>  - RELEASING.md:76 → 读取 git 历史 (3 处)<br>  - .husky/pre-commit:7 → 读取 git 历史 (1 处)<br>  - scripts/test-artifact-sync.mjs:21 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (91 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (2 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - theme/dsh-theme-herta/lib/opening/opening-player.js:263 → Windows 系统配置修改 (2 处)<br>  - scripts/test-tar-extract.mjs:132 → 修改系统目录 (1 处) |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: 隔离, workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (3 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 4 天; 提交总数: 155 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 15, Forks: 1, Watchers: 1 — 有一定社区基础 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | Herta-dsh |
| 校验 URL | https://github.com/HerTa-st/Herta-dsh |
| 必查项通过率 | 14/33 (42%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-15 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
