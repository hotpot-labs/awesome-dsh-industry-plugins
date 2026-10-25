# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/AumiSatori/dsh-ui-beautify
- **校验时间**: 2026-10-25 03:47:52
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 15 | 11 | 7 |
| 🟡 推荐 | 14 | 8 | 6 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ⚠️  需人工复核 | 账号注册: 2026-10-13 (12 天前); 公开仓库数: 5; 粉丝数: 0; ⚠️ 账号注册不足 30 天 (12 天) |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 626; 包名: dsh-ui-beautify; 描述: DSH UI appearance settings: glass surfaces, task and Artifact cards, custom mess — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - THIRD_PARTY_NOTICES.md:44 → 盗版/侵权 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (20): v0.3.72, v0.3.71, v0.3.70, v0.3.69, v0.3.68; package.json version: 0.3.72; GitHub Releases (5): v0.3.72, v0.3.71, v0.3.70, v0.3.69, v0.3.68 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | engines: {"node": ">=22.13.0", "dsh": ">=0.2.1-rc.2 <0.3.0-0"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "inject": ["@deepseek-ai/d; Cordis 配置文件: cordis.patch.yml<br>  - test/composer-browser.mjs:77 → Monkey patch / prototype pollution<br>  - test/summary-scope-browser.mjs:53 → Monkey patch / prototype pollution<br>  - test/sidebar-browser.mjs:57 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 199 处, 函数: 5479 个, 比例: 3.6% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: vendor/lens/internal/renderer.js; 发现清理逻辑: test/summary-browser.mjs; 发现清理逻辑: test/startup-motion-browser.mjs |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .gitignore:2 → 读取环境变量配置 (2 处)<br>  - THIRD_PARTY_NOTICES.md:18 → 读取浏览器 Cookie/本地存储 (1 处)<br>  - scripts/restore-claude-slider.mjs:76 → 读取环境变量配置 (1 处)<br>  - scripts/profile.mjs:15 → 读取环境变量配置 (3 处)<br>  - scripts/desktop-startup-feedback.mjs:56 → 读取环境变量配置 (1 处)<br>  ... 共 48 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - prototypes/context-particles/check-refinement.mjs:7 → 深层目录穿越 (1 处)<br>  - prototypes/context-particles/check-shell.mjs:7 → 深层目录穿越 (1 处)<br>  - prototypes/context-particles/check-svg.mjs:7 → 深层目录穿越 (1 处)<br>  - prototypes/context-particles/check.mjs:8 → 深层目录穿越 (1 处)<br>  - scripts/restore-claude-slider.mjs:76 → 读取用户主目录 (1 处)<br>  ... 共 10 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package-lock.json:24 → 探测到 HTTP(S) 网络请求 (33 处)<br>  - README.md:43 → 探测到 HTTP(S) 网络请求 (7 处)<br>  - THIRD_PARTY_NOTICES.md:9 → 探测到 HTTP(S) 网络请求 (6 处)<br>  - package.json:8 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - prototypes/context-particles/check-refinement.mjs:86 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: 127.0.0.1, creativecommons.org, developer.apple.com, divider-settings.test, example.com, example.invalid, gitee.com, github.com, invalid.example, localhost (+7 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - prototypes/context-particles/shell.js:17 → 远控/反向 shell (1 处)<br>  - prototypes/context-particles/preview.html:45 → 远控/反向 shell (1 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - scripts/restore-claude-slider.mjs:76 → 读取环境变量 API Key/凭证 (1 处)<br>  - scripts/profile.mjs:15 → 读取环境变量 API Key/凭证 (3 处)<br>  - scripts/desktop-startup-feedback.mjs:56 → 读取环境变量 API Key/凭证 (1 处)<br>  - scripts/check-release.mjs:14 → 读取环境变量 API Key/凭证 (3 处)<br>  - scripts/verify.mjs:7 → 读取环境变量 API Key/凭证 (2 处)<br>  ... 共 43 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - prototypes/context-particles/preview.html:209 → 修改全局配置 (1 处)<br>  - test/conversation-tabs-browser.mjs:148 → 写入配置文件 (1 处)<br>  - src/context-particle-renderer.js:137 → 修改全局配置 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - test/summary-browser.mjs:140 → base64 混淆字符串 (超长) (1 处)<br>  - test/welcome.test.mjs:23 → 连续十六进制转义 (混淆) (1 处)<br>  - test/background.test.mjs:14 → 连续十六进制转义 (混淆) (2 处) |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - scripts/check-release.mjs:22 → node:vm 任意代码执行 (1 处)<br>  - test/context-particles-browser.mjs:21 → node:vm 任意代码执行 (1 处)<br>  - test/slider-restore.test.mjs:75 → node:vm 任意代码执行 (1 处)<br>  - test/reading-turn-performance-browser.mjs:36 → new Function() 任意代码执行 (1 处)<br>  - test/logic.test.mjs:8 → node:vm 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 4 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - prototypes/context-particles/serve.mjs:17 → 开启监听端口 (1 处)<br>  - prototypes/context-particles/preview.html:39 → 定时任务 (2 处)<br>  - scripts/verify.mjs:19 → 定时任务 (1 处)<br>  - test/summary-browser.mjs:63 → 开启监听端口 (1 处)<br>  - test/summary-browser.mjs:443 → 定时任务 (2 处)<br>  ... 共 49 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - prototypes/context-particles/check-svg.mjs:25 → 云存储上传 (6 处)<br>  - prototypes/context-particles/preview.html:185 → 云存储上传 (3 处)<br>  - test/background-browser.mjs:30 → 云存储上传 (8 处)<br>  - test/particle-image-browser.mjs:34 → 云存储上传 (6 处)<br>  - test/context-particles-browser.mjs:176 → 云存储上传 (3 处)<br>  ... 共 15 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 4. repo: 0 deps + 4 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 17978, 注释行: 313 (1.7%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - test/summary-browser.mjs:1277 → 明文写入敏感信息 (7 处)<br>  - test/background-browser.mjs:45 → 明文写入敏感信息 (3 处)<br>  - test/focus-header-browser.mjs:61 → 明文写入敏感信息 (1 处)<br>  - test/theme-switch-browser.mjs:140 → 明文写入敏感信息 (1 处)<br>  - test/particle-image-browser.mjs:40 → 明文写入敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (48 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (2 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - scripts/restore-claude-slider.mjs:1 → 修改系统目录 (1 处) |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (2 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 92 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-ui-beautify |
| 校验 URL | https://github.com/AumiSatori/dsh-ui-beautify |
| 必查项通过率 | 15/33 (45%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-25 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
