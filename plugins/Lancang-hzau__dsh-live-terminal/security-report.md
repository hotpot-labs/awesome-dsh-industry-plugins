# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/Lancang-hzau/dsh-live-terminal
- **校验时间**: 2026-10-21 03:50:36
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 18 | 8 | 7 |
| 🟡 推荐 | 14 | 7 | 7 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2025-12-01 (323 天前); 公开仓库数: 3; 粉丝数: 0 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 762; 包名: dsh-live-terminal; 描述: Visible terminal panel for DeepSeek Harness: stream agent shell commands into an — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - research/existing-plugins.md:172 → 盗版/侵权 (1 处)<br>  - research/readmes/dsh-remote-gui.md:109 → 非法爬取 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (3): v1.2.0, v1.1.0, v1.0.0; package.json version: 1.2.0; GitHub Releases (3): v1.2.0, v1.1.0, v1.0.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | engines: {"node": "^22.19.0 \|\| >=24.0.0", "dsh": ">=0.2.1-rc.2 <0.3.0-0"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "inject": ["@deepseek-ai/d; Cordis 配置文件: cordis.patch.yml<br>  - research/readmes/dsh-gitbash-shell.md:115 → Monkey patch / prototype pollution<br>  - research/readmes/dsh-screenshot-capture.md:154 → Monkey patch / prototype pollution<br>  - docs/plugin-dev-notes.md:285 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 310 处, 函数: 2173 个, 比例: 14.3% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: lib/index.js; 发现清理逻辑: lib/client.js; 发现清理逻辑: lib/host/screen.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - PUBLISHING.md:95 → 读取 npm 凭证 (1 处)<br>  - research/readmes/_hyzyn_dsh-tty.md:515 → 读取 SSH 私钥目录 (8 处)<br>  - research/readmes/_hyzyn_dsh-tty.md:353 → 读取环境变量配置 (6 处)<br>  - research/readmes/_xgone_dsh-netshell.md:102 → 读取 SSH 私钥目录 (1 处)<br>  - research/readmes/dsh-remote-gui.md:82 → 读取 SSH 私钥目录 (1 处)<br>  ... 共 25 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - research/readmes/_hyzyn_dsh-tty.md:203 → 深层目录穿越 (5 处)<br>  - research/readmes/dsh-tweaks-git-bash-terminal-tool.md:73 → 深层目录穿越 (2 处)<br>  - research/npm-json/_hyzyn_dsh-tty.json:195 → 深层目录穿越 (2 处)<br>  - docs/plugin-dev-notes.md:2311 → 深层目录穿越 (3 处)<br>  - qa/probes/session-ring-probe.mjs:16 → 深层目录穿越 (2 处) — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - lib/host/wrapper.js:97 → exec 命令拼接 (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package.json:8 → 探测到 HTTP(S) 网络请求 (4 处)<br>  - README.md:3 → 探测到 HTTP(S) 网络请求 (9 处)<br>  - PUBLISHING.md:18 → 探测到 HTTP(S) 网络请求 (31 处)<br>  - package-lock.json:31 → 探测到 HTTP(S) 网络请求 (37 处)<br>  - icon.svg:1 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: 127.0.0.1, api.github.com, astral.sh, awesome-dsh-plugin.com, bellard.org, cdn.cooltea.top, cdn.jsdelivr.net, dashscope.aliyuncs.com, deepseek.com, docs.npmjs.com (+21 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - lib/client.js:326 → DDoS 攻击 (1 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - research/npm-dsh-remote-gui.json:24 → 敏感凭证读取 (1 处)<br>  - research/existing-plugins.md:189 → 敏感凭证读取 (1 处)<br>  - research/npm-dsh-remote-shell.json:19 → 敏感凭证读取 (1 处)<br>  - research/readmes/dsh-remote-shell.md:3 → 敏感凭证读取 (7 处)<br>  - research/readmes/_hyzyn_dsh-tty.md:306 → 敏感凭证读取 (31 处)<br>  ... 共 39 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - tools/build-client.mjs:142 → new Function() 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 9 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - PUBLISHING.md:75 → 文件写入 (1 处)<br>  - PUBLISHING.md:75 → 文件读取 (1 处)<br>  - research/readmes/dsh-gitbash-shell.md:455 → 文件读取 (1 处)<br>  - research/readmes/dsh-gitbash-shell.md:389 → 临时文件操作 (4 处)<br>  - research/readmes/dsh-plugin-console.md:18 → 临时文件操作 (2 处)<br>  ... 共 31 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - research/readmes/dsh-remote-shell.md:28 → 云存储上传 (1 处)<br>  - research/readmes/_hyzyn_dsh-tty.md:482 → 云存储上传 (9 处)<br>  - research/readmes/dsh-terminal-manager.md:22 → 云存储上传 (1 处)<br>  - research/readmes/dsh-task-console.md:271 → 云存储上传 (1 处)<br>  - research/readmes/seektty.md:441 → 云存储上传 (1 处)<br>  ... 共 7 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 9. repo: 2 deps + 7 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 13493, 注释行: 2120 (15.7%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ✅ 通过 | 未检测到明文存储敏感信息 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - README.md:171 → 读取 git 历史 (1 处)<br>  - PUBLISHING.md:25 → 读取 git 历史 (2 处)<br>  - docs/test-report.md:299 → 读取 git 历史 (1 处)<br>  - .github/workflows/ci.yml:29 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (28 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (6 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - research/readmes/_hyzyn_dsh-tty.md:771 → 修改系统目录 (1 处)<br>  - research/readmes/dsh-bash-terminal.md:12 → 修改系统目录 (1 处)<br>  - research/readmes/dsh-tmux-cc.md:176 → 修改系统目录 (1 处)<br>  - research/readmes/dsh-bash-terminal-ts.md:24 → 修改系统目录 (16 处)<br>  - lib/client.js:292 → 创建开机自启/系统服务 (1 处)<br>  ... 共 13 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: sandbox, 沙箱 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (6 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 21 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-live-terminal |
| 校验 URL | https://github.com/Lancang-hzau/dsh-live-terminal |
| 必查项通过率 | 18/33 (55%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-21 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
