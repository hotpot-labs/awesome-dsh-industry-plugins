# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/FYZB2020/dsh-fy-code-animation
- **校验时间**: 2026-11-22 05:45:37
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 16 | 12 | 5 |
| 🟡 推荐 | 14 | 6 | 8 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2020-04-12 (2414 天前); 公开仓库数: 6; 粉丝数: 0 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE.md) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1198; 包名: dsh-fy-code-animation; 描述: Turn a Chinese script into a finished MP4 with code, not a video editor: 341 cod — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - skills/fy-code-animation/references/motion-craft/reference/property-selection.md:13 → 盗版/侵权 (1 处)<br>  - skills/fy-code-animation/references/motion-craft/director/decision-framework.md:77 → 盗版/侵权 (1 处)<br>  - style-library/风格提示词/L_Lemo-Opuscar/L35_装饰艺术.md:63 → 盗版/侵权 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ⚠️  需人工复核 | 无 git tag; package.json version: 1.2.3; 有版本号但无 git tag / release |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | engines: {"node": ">=20"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ✅ 通过 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": [], "platform": "web", "immediately; Cordis 配置文件: cordis.patch.yml |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 88 处, 函数: 430 个, 比例: 20.5% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: style-library/风格提示词/A-G_代码样片/_公共函数.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - skills/fy-code-animation/implementations/specimen/VolumeScene.tsx:155 → 读取环境变量配置 (1 处)<br>  - skills/fy-code-animation/implementations/specimen/StudioEnv.tsx:9 → 读取环境变量配置 (4 处)<br>  - skills/fy-code-animation/tests/test_contracts.py:5 → 读取环境变量配置 (1 处)<br>  - skills/fy-code-animation/scripts/style_library.py:28 → 读取环境变量配置 (1 处)<br>  - tests/harness.mjs:11 → 读取环境变量配置 (3 处)<br>  ... 共 19 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - skills/fy-code-animation/implementations/transitions/README.md:3 → 深层目录穿越 (1 处)<br>  - skills/fy-code-animation/implementations/character/README.md:3 → 深层目录穿越 (1 处)<br>  - skills/fy-code-animation/implementations/audio-sync/README.md:3 → 深层目录穿越 (1 处)<br>  - skills/fy-code-animation/implementations/type-cn/README.md:26 → 深层目录穿越 (1 处)<br>  - skills/fy-code-animation/implementations/backgrounds/README.md:3 → 深层目录穿越 (1 处)<br>  ... 共 33 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - skills/code-animation-prompts/scripts/render_video.py:75 → Python subprocess (1 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package.json:73 → 探测到 HTTP(S) 网络请求 (4 处)<br>  - LICENSE.md:31 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - README.md:146 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - README.zh.md:154 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - skills/code-animation-prompts/references/attribution.md:11 → 探测到 HTTP(S) 网络请求 (2 处)<br>涉及的域名: 127.0.0.1, catalog.archives.gov., cdn.npmmirror.com, ffmpeg.org, gitee.com, github.com, images.nasa.gov., localhost, prompt-motion.com, pypi.org (+3 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - skills/fy-code-animation/LICENSES/HeyGen-Apache-2.0.txt:149 → 挖矿相关 (1 处)<br>  - style-library/风格挑选.html:153 → 挖矿相关 (1 处)<br>  - style-library/_alt-flux/风格提示词/M_动态风格/M9_情绪弧线：混乱、掌控、清晰.jpg:89 → DDoS 攻击 (1 处)<br>  - style-library/风格提示词/O_奥斯卡98部/O60_末代皇帝.md:17 → 挖矿相关 (1 处)<br>  - style-library/风格提示词/L_Lemo-Opuscar/L50_HD-2D.md:38 → 挖矿相关 (1 处)<br>  ... 共 6 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - tests/harness.mjs:11 → 读取环境变量 API Key/凭证 (3 处)<br>  - lib/paths.js:15 → 读取环境变量 API Key/凭证 (4 处)<br>  - lib/index.js:74 → 读取环境变量 API Key/凭证 (2 处)<br>  - lib/deps.js:59 → 读取环境变量 API Key/凭证 (7 处)<br>  - lib/render.js:94 → 读取环境变量 API Key/凭证 (1 处)<br>  ... 共 18 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - skills/code-animation-prompts/assets/starter/index.html:19 → 修改全局配置 (1 处)<br>  - skills/fy-code-animation/implementations/canvas-contract.mjs:23 → 修改全局配置 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 0 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - skills/code-animation-prompts/scripts/render_video.py:91 → 进程控制 (1 处)<br>  - tests/contract.mjs:72 → 进程控制 (2 处)<br>  - tests/harness.mjs:13 → 临时文件操作 (1 处)<br>  - lib/sync.js:88 → 文件写入 (2 处)<br>  - lib/sync.js:13 → 文件读取 (2 处)<br>  ... 共 35 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - style-library/风格提示词/L_Lemo-Opuscar/L39_ASCII · CRT 终端.md:97 → 云存储上传 (1 处)<br>  - style-library/风格提示词/L_Lemo-Opuscar/L7_体育战术板.md:110 → 云存储上传 (3 处)<br>  - style-library/风格提示词/L_Lemo-Opuscar/L23_钢笔淡彩.md:113 → 云存储上传 (1 处)<br>  - style-library/风格提示词/L_Lemo-Opuscar/L1_字幕新闻.md:104 → 云存储上传 (1 处)<br>  - style-library/风格提示词/L_Lemo-Opuscar/L3_倒计时分屏.md:116 → 云存储上传 (2 处)<br>  ... 共 9 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 无第三方依赖 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 4770, 注释行: 248 (5.2%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 2 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - lib/client.js:101 → 明文写入敏感信息 (1 处)<br>  - style-library/风格挑选.html:162 → 明文写入敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - README.md:14 → 读取 git 历史 (1 处)<br>  - README.zh.md:17 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (15 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (7 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - skills/fy-code-animation/scripts/glyph_outline.py:1 → 修改系统目录 (1 处) |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (4 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 11 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 1, Forks: 1, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-fy-code-animation |
| 校验 URL | https://github.com/FYZB2020/dsh-fy-code-animation |
| 必查项通过率 | 16/33 (48%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-11-22 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
