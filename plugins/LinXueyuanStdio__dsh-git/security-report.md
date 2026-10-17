# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/LinXueyuanStdio/dsh-git
- **校验时间**: 2026-10-17 03:36:59
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 15 | 12 | 6 |
| 🟡 推荐 | 14 | 5 | 8 | 1 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2016-11-02 (3635 天前); 公开仓库数: 200; 粉丝数: 341 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 463; 包名: @linxueyuan/dsh-git; 描述: DSH 插件:在官方右侧栏提供「dsh-git」本地仓库工作台——多仓库下拉 + Changes/History 本地 git(暂存·提交·同步) + Code — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - CHANGELOG.md:85 → 盗版/侵权 (1 处)<br>  - cordis.patch.yml:24 → 盗版/侵权 (1 处)<br>  - src/client/highlighter-worker.generated.ts:20 → 破解授权 (2 处)<br>  - src/core/desktop/ui/lib/expiring-operation-cache.ts:5 → 盗版/侵权 (3 处)<br>  - src/host/token-refresh.ts:327 → 盗版/侵权 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (4): v1.2.0, v1.1.1, v1.1.0, v1.0.0; package.json version: 1.2.0; GitHub Releases (4): v1.2.0, v1.1.1, v1.1.0, v1.0.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/dsh-client-ui-primitives: >=0.2.0-rc.2 \|\| >=0.3.0-rc.1 \|\| >=0.4.0-rc.1 \|\| >=0.5.0-rc.1; engines: {"node": "^22.19.0 \|\| >=24.0.0"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": ["slots", "@deepseek-ai/dsh-client-; Cordis/DSH 依赖: @deepseek-ai/dsh-client-ui-primitives; Cordis 配置文件: cordis.patch.yml<br>  - cordis.patch.yml:1 → Monkey patch / prototype pollution<br>  - src/client/diff-rows.ts:173 → Monkey patch / prototype pollution<br>  - src/client/notifications.ts:673 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 690 处, 函数: 6375 个, 比例: 10.8% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: src/index.ts; 发现清理逻辑: src/client/alive.ts; 发现清理逻辑: src/client/notifications.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - CHANGELOG.md:172 → 读取 git 配置 (1 处)<br>  - .gitignore:150 → 读取环境变量配置 (2 处)<br>  - .gitignore:209 → 读取 PyPI 凭证 (1 处)<br>  - .npmrc:9 → 读取 npm 凭证 (1 处)<br>  - tsconfig.json:16 → 读取环境变量配置 (1 处)<br>  ... 共 54 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - scripts/verify-install.mjs:29 → 读取用户主目录 (4 处)<br>  - scripts/styles.mjs:420 → 深层目录穿越 (1 处)<br>  - scripts/e2e-deploy.mjs:227 → 读取用户主目录 (4 处)<br>  - scripts/highlighter-worker.mjs:38 → 深层目录穿越 (6 处)<br>  - scripts/verify-mirror.mjs:53 → 深层目录穿越 (16 处)<br>  ... 共 333 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - tsconfig.json:108 → 加载 child_process (1 处)<br>  - src/core/desktop/lib/shells/index.ts:14 → 加载 child_process (1 处)<br>  - src/core/desktop/lib/git/rebase.ts:1 → 加载 child_process (1 处)<br>  - src/host/mirror/lib/git/rebase.ts:1 → 加载 child_process (1 处)<br>  - src/host/mirror/lib/git/cherry-pick.ts:18 → 加载 child_process (1 处)<br>  ... 共 6 处<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - scripts/check-base-recipes.mjs:454 → exec 命令拼接 (1 处)<br>  - src/core/desktop/ui/preferences/integrations.tsx:185 → 开启 shell 模式 (注入风险) (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package-lock.json:96 → 探测到 HTTP(S) 网络请求 (595 处)<br>  - CHANGELOG.md:3 → 探测到 HTTP(S) 网络请求 (9 处)<br>  - THIRD-PARTY-NOTICES.md:62 → 探测到 HTTP(S) 网络请求 (8 处)<br>  - .gitignore:106 → 探测到 HTTP(S) 网络请求 (5 处)<br>  - .eslintrc.yml:203 → fetch 网络请求 (2 处)<br>涉及的域名: ..., 127.0.0.1, HOSTNAME, alive.github.com, api., api.github.com, apidock.com, avatars.githubusercontent.com, code.visualstudio.com, css-tricks.com (+42 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - THIRD-PARTY-NOTICES.md:246 → 挖矿相关 (1 处)<br>  - src/core/desktop/lib/email.ts:114 → 挖矿相关 (1 处)<br>  - src/core/desktop/lib/ci-checks/ci-checks.ts:286 → 挖矿相关 (1 处)<br>  - src/core/desktop/ui/multi-commit-operation/choose-branch/merge-choose-branch-dialog.tsx:110 → 挖矿相关 (2 处)<br>  - src/core/desktop/ui/lib/tooltip.tsx:100 → 挖矿相关 (1 处)<br>  ... 共 14 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - CHANGELOG.md:84 → 敏感凭证读取 (5 处)<br>  - CONTRIBUTING.md:94 → 敏感凭证读取 (1 处)<br>  - .gitignore:192 → 敏感凭证读取 (2 处)<br>  - .eslintrc.yml:315 → 敏感凭证读取 (2 处)<br>  - cordis.patch.yml:17 → 敏感凭证读取 (3 处)<br>  ... 共 84 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - scripts/e2e-deploy.mjs:416 → 写入配置文件 (1 处)<br>  - src/host/repo-registry.ts:5 → 修改全局配置 (2 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 59 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - CONTRIBUTING.md:70 → 临时文件操作 (1 处)<br>  - scripts/probe-toolbar-geometry.mjs:541 → 进程控制 (1 处)<br>  - scripts/upstream-watch.mjs:236 → 定时任务 (1 处)<br>  - scripts/upstream-watch.mjs:177 → 进程控制 (9 处)<br>  - scripts/static-gates.md:142 → 临时文件操作 (1 处)<br>  ... 共 74 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - .github/workflows/ci.yml:130 → 云存储上传 (1 处)<br>  - .github/workflows/upstream-watch.yml:345 → 云存储上传 (1 处)<br>  - scripts/e2e-deploy.mjs:40 → 云存储上传 (11 处)<br>  - scripts/lib/ci-assets.mjs:10 → 云存储上传 (8 处)<br>  - src/client/styles.ts:64 → 云存储上传 (1 处)<br>  ... 共 10 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ❌ 不通过 | 总依赖数: 58. repo: 1 deps + 57 devDeps — 依赖过多 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 136628, 注释行: 41868 (30.6%) |
| 4.9 | 具备测试覆盖 | 推荐 | ⚠️  需人工复核 | 未发现测试文件 |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - .github/workflows/release.yml:123 → 硬编码敏感信息 (1 处)<br>  - scripts/check-scope-roots.mjs:272 → 明文写入敏感信息 (1 处)<br>  - scripts/check-unreachable-ancestors.mjs:269 → 明文写入敏感信息 (1 处)<br>  - scripts/check-scripts-types.mjs:189 → 明文写入敏感信息 (1 处)<br>  - scripts/check-sass-leaks.mjs:241 → 明文写入敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - .github/workflows/upstream-watch.yml:244 → 读取 git 历史 (1 处)<br>  - scripts/static-gates.md:153 → 读取 git 历史 (2 处)<br>  - scripts/check-generated.mjs:10 → 读取 git 历史 (2 处)<br>  - scripts/verify-mirror.mjs:77 → 读取 git 历史 (1 处)<br>  - src/client/diff-rows.ts:17 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (123 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (8 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - scripts/check-base-recipes.mjs:1 → 修改系统目录 (1 处)<br>  - scripts/upstream-watch.mjs:1 → 修改系统目录 (1 处)<br>  - scripts/check-template-literals.mjs:1 → 修改系统目录 (1 处)<br>  - scripts/check-lint.mjs:1 → 修改系统目录 (1 处)<br>  - scripts/check-types.mjs:1 → 修改系统目录 (1 处)<br>  ... 共 16 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (4 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 2 天; 提交总数: 109 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 1, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-git |
| 校验 URL | https://github.com/LinXueyuanStdio/dsh-git |
| 必查项通过率 | 15/33 (45%) |
| 推荐项满足率 | 13/14 (约 93%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-17 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
