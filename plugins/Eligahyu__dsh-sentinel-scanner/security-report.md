# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/Eligahyu/dsh-sentinel-scanner
- **校验时间**: 2026-08-23 16:23:48
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 16 | 10 | 7 |
| 🟡 推荐 | 14 | 8 | 6 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: master |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2024-11-21 (640 天前); 公开仓库数: 6; 粉丝数: 0 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 3191; 包名: deepseek-harness-sentinel; 描述: 🛡️ 给 DeepSeek Harness 插件拍 X 光 —— DSH 插件安全体检与健康检查。静态启发式审计:代码执行、凭据访问、外传端点、混淆、安装脚本、 — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (2): v0.4.4, v0.4; package.json version: 0.4.4; GitHub Releases (1): v0.4.4 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: *; @deepseek-ai/dsh-tools: *; engines: {"node": "^22.18.0 \|\| >=24.11.0"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}}; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-tools; Cordis 配置文件: cordis.patch.yml<br>  - engine/rules.js:130 → 直接修改内核源码<br>  - docs/rules.md:9 → 直接修改内核源码 — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 195 处, 函数: 1397 个, 比例: 14.0% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: engine/package/audit.js; 发现清理逻辑: engine/package/diff.js; 发现清理逻辑: test/hardening.test.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - CHANGELOG.md:161 → 读取环境变量配置 (3 处)<br>  - CHANGELOG.md:175 → 读取 PyPI 凭证 (1 处)<br>  - engine/rules.js:236 → 读取 SSH 私钥目录 (1 处)<br>  - engine/rules.js:172 → 读取 AWS 凭证 (1 处)<br>  - engine/rules.js:172 → 读取 npm 凭证 (5 处)<br>  ... 共 57 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - .final-test.txt:172 → 深层目录穿越 (1 处)<br>  - engine/rules.js:571 → 深层目录穿越 (2 处)<br>  - engine/path-safety.js:3 → 深层目录穿越 (1 处)<br>  - engine/index.js:43 → 读取用户主目录 (1 处)<br>  - engine/package/tar.js:5 → 深层目录穿越 (1 处)<br>  ... 共 13 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - docs/upgrade-spec.md:2216 → 加载 child_process (2 处)<br>  - docs/architecture.md:139 → 加载 child_process (1 处)<br>  - test/professional.test.js:226 → 加载 child_process (2 处)<br>  - test/v2.test.js:355 → 加载 child_process (2 处)<br>  - test/hardening.test.js:545 → 加载 child_process (1 处)<br>  ... 共 8 处<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - docs/upgrade-spec.md:1201 → 命令字符串拼接变量 (注入风险) (1 处)<br>  - test/professional.test.js:420 → exec 命令拼接 (1 处)<br>  - test/fixtures/bench/edge/edge-spawn-shell.js:6 → 开启 shell 模式 (注入风险) (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - .final-test.txt:70 → fetch 网络请求 (1 处)<br>  - package.json:9 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - package-lock.json:35 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - README.md:5 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - engine/rules.js:580 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: ..., 10.255.255.1, 127.0.0.1, 169.254.169.254, api.anthropic.com, api.deepseek.com, api.deepseek.com.evil.example, api.example.com, api.github.com, api.openai.com (+17 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - .final-test.txt:47 → 敏感凭证读取 (9 处)<br>  - SECURITY.md:38 → 敏感凭证读取 (2 处)<br>  - .v2-plan-done:23 → 敏感凭证读取 (2 处)<br>  - package.json:4 → 敏感凭证读取 (1 处)<br>  - README.md:29 → 敏感凭证读取 (10 处)<br>  ... 共 75 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - test/professional.test.js:563 → 写入配置文件 (1 处)<br>  - test/v2.test.js:439 → 写入配置文件 (2 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - test/fixtures/evil-plugin/plugin/index.js:19 → 连续十六进制转义 (混淆) (3 处)<br>  - test/fixtures/evil-plugin/plugin/index.js:31 → 超长 base64 字符串 (2 处) |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - .final-test.txt:167 → new Function() 任意代码执行 (2 处)<br>  - README.md:379 → eval() 任意代码执行 (2 处)<br>  - engine/report.js:66 → eval() 任意代码执行 (1 处)<br>  - engine/rules.js:154 → eval() 任意代码执行 (1 处)<br>  - engine/rules.js:142 → new Function() 任意代码执行 (2 处)<br>  ... 共 27 处 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 3 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - engine/rules.js:442 → 临时文件操作 (3 处)<br>  - bin/sentinel.mjs:409 → 进程控制 (1 处)<br>  - docs/submission-awesome.md:23 → 临时文件操作 (2 处)<br>  - docs/integration-github-action.md:79 → 进程控制 (1 处)<br>  - docs/rules.md:27 → 临时文件操作 (1 处)<br>  ... 共 11 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - action.yml:14 → 云存储上传 (2 处)<br>  - README.md:43 → 云存储上传 (6 处)<br>  - engine/semantic/harness.js:17 → 云存储上传 (1 处)<br>  - .github/workflows/sentinel.yml:6 → 云存储上传 (3 处)<br>  - bin/sentinel.mjs:56 → 云存储上传 (1 处)<br>  ... 共 9 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 1. repo: 1 deps + 0 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 18290, 注释行: 1791 (9.8%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 17 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - engine/semantic/taint.js:188 → 硬编码敏感信息 (1 处)<br>  - engine/semantic/taint.js:188 → 从环境变量获取敏感信息 (1 处)<br>  - docs/upgrade-spec.md:1749 → 从环境变量获取敏感信息 (1 处)<br>  - test/professional.test.js:167 → 硬编码敏感信息 (1 处)<br>  - test/hardening.test.js:820 → 明文写入敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - docs/superpowers/plans/2026-08-20-professional-upgrade.md:241 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (9 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (7 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - engine/rules.js:426 → 要求 root/sudo 权限<br>  - docs/upgrade-spec.md:80 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - engine/rules.js:756 → 创建开机自启/系统服务 (2 处)<br>  - bin/sentinel.mjs:1 → 修改系统目录 (1 处)<br>  - test/professional.test.js:129 → 修改系统目录 (1 处)<br>  - test/supplychain.test.js:108 → 修改系统目录 (3 处)<br>  - test/fixtures/bench/malicious/pkg5/package.json:6 → 修改系统目录 (1 处) |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: 隔离, workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (1 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 70 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 5, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-sentinel-scanner |
| 校验 URL | https://github.com/Eligahyu/dsh-sentinel-scanner |
| 必查项通过率 | 16/33 (48%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-23 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
