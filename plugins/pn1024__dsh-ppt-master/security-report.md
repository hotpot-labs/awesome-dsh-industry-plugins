# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/pn1024/dsh-ppt-master
- **校验时间**: 2026-09-02 03:42:08
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 13 | 12 | 8 |
| 🟡 推荐 | 14 | 6 | 8 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2018-12-17 (2815 天前); 公开仓库数: 6; 粉丝数: 2 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 216; 包名: dsh-ppt-master; 描述: PPT Master skill for DeepSeek Harness: AI-driven presentation workflow for gener — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - skills/ppt-master/workflows/profiles/image-to-pptx.md:25 → 盗版/侵权 (1 处)<br>  - skills/ppt-master/templates/icons/tabler-outline/mood-spark.svg:3 → 盗版/侵权 (1 处)<br>  - skills/ppt-master/templates/icons/tabler-outline/lungs.svg:2 → 盗版/侵权 (1 处)<br>  - skills/ppt-master/templates/icons/tabler-outline/treasure-chest.svg:2 → 盗版/侵权 (1 处)<br>  - skills/ppt-master/templates/icons/tabler-outline/skull.svg:2 → 盗版/侵权 (1 处)<br>  ... 共 9 处 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ⚠️  需人工复核 | 无 git tag; package.json version: 6.1.0; 有版本号但无 git tag / release |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | engines: {"node": ">=20.0.0"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"engines": {"dsh": ">=0.1.1-rc.1"}, "bundle": {"patch": "./cordis.patch.yml"}}; Cordis 配置文件: cordis.patch.yml<br>  - skills/ppt-master/references/template-designer.md:66 → Monkey patch / prototype pollution<br>  - skills/ppt-master/scripts/pptx_to_svg/converter.py:7 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 110 处, 函数: 849 个, 比例: 13.0% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: skills/ppt-master/scripts/svg_editor/static/app.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .gitignore:11 → 读取环境变量配置 (2 处)<br>  - package.json:17 → 读取环境变量配置 (1 处)<br>  - README.md:38 → 读取环境变量配置 (3 处)<br>  - .env.example:11 → 读取环境变量配置 (12 处)<br>  - skills/ppt-master/.env.example:11 → 读取环境变量配置 (12 处)<br>  ... 共 45 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - skills/ppt-master/workflows/stages/customize-animations.md:7 → 深层目录穿越 (6 处)<br>  - skills/ppt-master/workflows/stages/live-preview.md:7 → 深层目录穿越 (1 处)<br>  - skills/ppt-master/workflows/stages/verify-charts.md:33 → 深层目录穿越 (3 处)<br>  - skills/ppt-master/workflows/stages/generate-audio.md:7 → 深层目录穿越 (1 处)<br>  - skills/ppt-master/workflows/stages/refine-spec.md:31 → 深层目录穿越 (2 处)<br>  ... 共 32 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - skills/ppt-master/scripts/narration_sync.py:1536 → Python subprocess (1 处)<br>  - skills/ppt-master/scripts/server_common.py:90 → Python subprocess (3 处)<br>  - skills/ppt-master/scripts/source_to_md.py:97 → Python subprocess (1 处)<br>  - skills/ppt-master/scripts/powerpoint_video.py:281 → Python subprocess (1 处)<br>  - skills/ppt-master/scripts/update_repo.py:81 → Python subprocess (1 处)<br>  ... 共 16 处<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package.json:37 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - README.md:18 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - .env.example:49 → 探测到 HTTP(S) 网络请求 (24 处)<br>  - skills/ppt-master/SKILL.md:15 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - skills/ppt-master/.env.example:42 → 探测到 HTTP(S) 网络请求 (24 处)<br>涉及的域名: ..., 11j.powerchina.cn, 127.0.0.1, about.google, api-inference.modelscope.cn, api.bfl.ai, api.elevenlabs.io, api.ideogram.ai, api.minimax.io, api.minimaxi.com (+48 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - skills/ppt-master/templates/icons/tabler-outline/diamond.svg:3 → 挖矿相关 (1 处)<br>  - skills/ppt-master/templates/icons/tabler-outline/currency-solana.svg:2 → 挖矿相关 (1 处)<br>  - skills/ppt-master/templates/icons/tabler-outline/brand-cloudflare.svg:2 → DDoS 攻击 (1 处)<br>  - skills/ppt-master/templates/icons/tabler-outline/diamond-off.svg:3 → 挖矿相关 (1 处)<br>  - skills/ppt-master/templates/icons/tabler-outline/currency-dogecoin.svg:2 → 挖矿相关 (1 处)<br>  ... 共 11 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - .gitignore:11 → 敏感凭证读取 (1 处)<br>  - .env.example:35 → API Key / Token 读取 (29 处)<br>  - skills/ppt-master/.env.example:30 → API Key / Token 读取 (29 处)<br>  - skills/ppt-master/workflows/profiles/quick-generate.md:124 → 敏感凭证读取 (2 处)<br>  - skills/ppt-master/templates/icons/tabler-outline/login.svg:2 → 敏感凭证读取 (1 处)<br>  ... 共 73 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - skills/ppt-master/scripts/pptx_to_svg/chart_to_svg.py:2614 → 修改全局配置 (2 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - skills/ppt-master/scripts/console_encoding.py:25 → 连续十六进制转义 (混淆) (1 处)<br>  - skills/ppt-master/scripts/attribution_guard.py:60 → 连续十六进制转义 (混淆) (1 处)<br>  - skills/ppt-master/scripts/mirror_template_materialize.py:2653 → 连续十六进制转义 (混淆) (1 处)<br>  - skills/ppt-master/scripts/pptx_workspace.py:296 → 连续十六进制转义 (混淆) (9 处)<br>  - skills/ppt-master/scripts/image_backends/backend_common.py:151 → 连续十六进制转义 (混淆) (1 处)<br>  ... 共 9 处 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - skills/ppt-master/scripts/slice_images.py:312 → eval() 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 0 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - skills/ppt-master/workflows/create-template.md:37 → 临时文件操作 (1 处)<br>  - skills/ppt-master/workflows/stages/visual-review.md:72 → 临时文件操作 (1 处)<br>  - skills/ppt-master/scripts/svg_authoring_view.py:19 → 临时文件操作 (1 处)<br>  - skills/ppt-master/scripts/confirm_ui/static/app.js:4041 → 定时任务 (5 处)<br>  - skills/ppt-master/scripts/svg_editor/static/app.js:1402 → 定时任务 (5 处)<br>  ... 共 7 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - skills/ppt-master/templates/icons/tabler-outline/brand-supabase.svg:2 → 云服务 SDK (可能用于隐蔽上传) (1 处)<br>  - skills/ppt-master/templates/icons/tabler-outline/loader-3.svg:2 → 云存储上传 (1 处)<br>  - skills/ppt-master/templates/icons/tabler-outline/message-2-up.svg:3 → 云存储上传 (1 处)<br>  - skills/ppt-master/templates/icons/tabler-outline/camera-up.svg:3 → 云存储上传 (1 处)<br>  - skills/ppt-master/templates/icons/tabler-outline/cloud-upload.svg:2 → 云存储上传 (1 处)<br>  ... 共 23 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 无第三方依赖 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 181692, 注释行: 3348 (1.8%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - skills/ppt-master/scripts/svg_quality/checker.py:6470 → 硬编码敏感信息 (1 处)<br>  - skills/ppt-master/scripts/tests/test_text_measure.py:96 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (9 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (7 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - skills/ppt-master/requirements.txt:67 → 要求 root/sudo 权限<br>  - skills/ppt-master/scripts/source_to_md/doc_to_md.py:1327 → 要求 root/sudo 权限<br>  - skills/ppt-master/scripts/docs/conversion.md:137 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - skills/ppt-master/scripts/pptx_animations.py:1 → 修改系统目录 (1 处)<br>  - skills/ppt-master/scripts/language_tags.py:1 → 修改系统目录 (1 处)<br>  - skills/ppt-master/scripts/workflow_transcript.py:1 → 修改系统目录 (1 处)<br>  - skills/ppt-master/scripts/project_specs.py:1 → 修改系统目录 (1 处)<br>  - skills/ppt-master/scripts/pptx_delivery_check.py:1 → 修改系统目录 (1 处)<br>  ... 共 159 处 |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (28 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 1 天; 提交总数: 14 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 1, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-ppt-master |
| 校验 URL | https://github.com/pn1024/dsh-ppt-master |
| 必查项通过率 | 13/33 (39%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-09-02 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
