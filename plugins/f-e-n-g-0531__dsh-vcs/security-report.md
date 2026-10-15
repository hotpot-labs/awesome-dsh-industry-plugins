# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/f-e-n-g-0531/dsh-vcs
- **校验时间**: 2026-10-15 03:48:16
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 13 | 12 | 8 |
| 🟡 推荐 | 14 | 8 | 6 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2016-04-19 (3831 天前); 公开仓库数: 6; 粉丝数: 0 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ⚠️  需人工复核 | 许可证: SEE LICENSE IN LICENSE — 需确认与 MIT 兼容性 |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 310; 包名: @feng0531/dsh-vcs; 描述: Read-only Git and SVN change preview for DSH — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - LICENSE:39 → 盗版/侵权 (2 处)<br>  - src/commit-signature.mjs:3 → 破解授权 (1 处)<br>  - docs/LIVE-ACCEPTANCE.md:24 → 绕过权限限制 (1 处)<br>  - docs/releases/0.3.92.md:8 → 破解授权 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (20): v0.3.101, v0.3.100, v0.3.99, v0.3.98, v0.3.97; package.json version: 0.3.101; GitHub Releases (5): v0.3.101, v0.3.100, v0.3.99, v0.3.98, v0.3.97 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/dsh: 0.1.7-rc.2 \|\| 0.2.0-rc.2; engines: {"node": ">=22.0.0"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "immediately": true, "inje; Cordis/DSH 依赖: @deepseek-ai/dsh; Cordis 配置文件: cordis.patch.yml<br>  - src/svn-runtime.mjs:29 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 192 处, 函数: 1971 个, 比例: 9.7% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: local-command.mjs; 发现清理逻辑: index.mjs; 发现清理逻辑: scripts/monaco-fixture.mjs |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - local-command.mjs:11 → 读取环境变量配置 (1 处)<br>  - .gitignore:7 → 读取环境变量配置 (3 处)<br>  - .github/workflows/release.yml:52 → 读取环境变量配置 (10 处)<br>  - scripts/run-svn-live-browser.mjs:2 → 读取环境变量配置 (1 处)<br>  - scripts/monaco-fixture.mjs:5 → 读取环境变量配置 (6 处)<br>  ... 共 25 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - vcs.mjs:144 → 目录遍历 (1 处)<br>  - scripts/svn-dav-fixture.mjs:15 → 读取用户主目录 (1 处)<br>  - test/vcs.test.mjs:481 → 深层目录穿越 (1 处) — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - git-history.mjs:64 → exec 命令拼接 (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package-lock.json:34 → 探测到 HTTP(S) 网络请求 (47 处)<br>  - index.mjs:235 → fetch 网络请求 (1 处)<br>  - LICENSE:5 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - SECURITY.md:29 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - icon.svg:1 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: 127.0.0.1, EXAMPLE.test, example.com, example.test, fork.dev, github.com, invalid.example, localhost, other.test, registry.npmjs.org (+4 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - .github/workflows/layout.yml:13 → 敏感凭证读取 (1 处)<br>  - .github/workflows/release.yml:52 → 读取环境变量 API Key/凭证 (10 处)<br>  - .github/workflows/release.yml:41 → 敏感凭证读取 (4 处)<br>  - scripts/history-browser.jsx:49 → 敏感凭证读取 (1 处)<br>  - scripts/run-svn-live-browser.mjs:2 → 读取环境变量 API Key/凭证 (1 处)<br>  ... 共 28 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - scripts/svn-dav-fixture.mjs:15 → 写入配置文件 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - test/pack-report.test.mjs:5 → 字符混淆 (1 处) |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - scripts/test-host-compat.mjs:27 → node:vm 任意代码执行 (2 处)<br>  - test/text-fallback.test.mjs:7 → node:vm 任意代码执行 (1 处)<br>  - test/client.test.mjs:20 → node:vm 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 6 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - local-command.mjs:22 → 定时任务 (1 处)<br>  - .github/workflows/release.yml:161 → 定时任务 (1 处)<br>  - scripts/svn-live-browser.jsx:2 → 定时任务 (1 处)<br>  - scripts/history-browser.jsx:17 → 定时任务 (2 处)<br>  - scripts/svn-identity-browser.jsx:2 → 定时任务 (2 处)<br>  ... 共 110 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - .github/workflows/ci.yml:54 → 云存储上传 (1 处)<br>  - .github/workflows/layout.yml:58 → 云存储上传 (1 处)<br>  - .github/workflows/release.yml:163 → 云存储上传 (1 处)<br>  - test/vcs.test.mjs:300 → 云存储上传 (1 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 5. repo: 1 deps + 4 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 7276, 注释行: 173 (2.4%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - scripts/keyboard-fixture.mjs:37 → 明文写入敏感信息 (1 处)<br>  - scripts/svn-remote-browser.jsx:2 → 硬编码敏感信息 (3 处)<br>  - scripts/verify-keyboard-result.mjs:7 → 明文写入敏感信息 (1 处)<br>  - scripts/svn-dav-fixture.mjs:15 → 明文写入敏感信息 (1 处)<br>  - scripts/svn-dav-fixture.mjs:39 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - git-history.mjs:106 → 读取 git 历史 (1 处)<br>  - test/large-compare.test.mjs:76 → 读取文档/压缩文件 (1 处)<br>  - test/svn-history-local.test.mjs:65 → 读取文档/压缩文件 (2 处)<br>  - test/vcs.test.mjs:30 → 读取文档/压缩文件 (5 处)<br>  - test/history-integration.test.mjs:24 → 读取文档/压缩文件 (2 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (14 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (1 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - .github/workflows/ci.yml:27 → 要求 root/sudo 权限<br>  - .github/workflows/layout.yml:43 → 要求 root/sudo 权限<br>  - .github/workflows/release.yml:72 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - scripts/svn-dav-fixture.mjs:15 → 修改系统目录 (8 处)<br>  - test/bounded-https-tls.test.mjs:2 → 修改系统目录 (2 处)<br>  - test/svn-dav-chain-tls.test.mjs:2 → 修改系统目录 (2 处) |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: 隔离 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (11 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 713 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-vcs |
| 校验 URL | https://github.com/f-e-n-g-0531/dsh-vcs |
| 必查项通过率 | 13/33 (39%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-15 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
