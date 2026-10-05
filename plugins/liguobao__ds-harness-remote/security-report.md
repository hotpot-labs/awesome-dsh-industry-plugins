# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/liguobao/ds-harness-remote
- **校验时间**: 2026-10-05 04:42:18
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 14 | 12 | 7 |
| 🟡 推荐 | 14 | 7 | 7 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2015-02-08 (4256 天前); 公开仓库数: 296; 粉丝数: 245 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1784; 包名: ds-harness-remote; 描述: End-to-end encrypted remote access to DeepSeek Harness and experimental Codex wo — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - packages/protocol/tests/account-authorization.test.ts:43 → 盗版/侵权 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (14): v0.4.27, v0.4.26, v0.4.25, v0.4.22, v0.4.19; package.json version: 0.4.27; GitHub Releases (5): v0.4.27, v0.4.26, v0.4.25, v0.4.22, v0.4.19 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: >=4.0.1 <5; @deepseek-ai/dsh-api-gateway: >=0.1.1-rc.2 <0.1.2 \|\| >=0.1.2-alpha.1 <=0.1.2-rc.1 \|\| >=0.1.5-alpha.1 \|\| >=0.2.0-rc.1; @deepseek-ai/dsh-client-connection: >=0.1.1-rc.2 <0.1.2 \|\| >=0.1.2-alpha.1 <=0.1.2-rc.1 \|\| >=0.1.5-alpha.1 \|\| >=0.2.0-rc.1; @deepseek-ai/dsh-client-locale: >=0.1.1-rc.2 <0.1.2 \|\| >=0.1.2-alpha.1 <=0.1.2-rc.1 \|\| >=0.1.5-alpha.1 \|\| >=0.2.0-rc.1; @deepseek-ai/dsh-client-ui-sidebar: >=0.1.1-rc.2 <0.1.2 \|\| >=0.1.2-alpha.1 <=0.1.2-rc.1 \|\| >=0.1.5-alpha.1 \|\| >=0.2.0-rc.1 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": ["@deepseek-ai/dsh-client-connectio; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-api-gateway, @deepseek-ai/dsh-client-connection, @deepseek-ai/dsh-client-locale, @deepseek-ai/dsh-client-ui-sidebar; Cordis 配置文件: cordis.patch.yml<br>  - packages/plugin/tests/typert-gateway-switch.test.ts:87 → Monkey patch / prototype pollution<br>  - packages/plugin/tests/remote-typert-gateway.test.ts:107 → Monkey patch / prototype pollution<br>  - packages/plugin/tests/control-stream.test.ts:189 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 738 处, 函数: 5768 个, 比例: 12.8% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: apps/vscode/tests/sign-out.test.ts; 发现清理逻辑: apps/vscode/tests/controller.test.ts; 发现清理逻辑: apps/vscode/src/extension.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .gitignore:18 → 读取环境变量配置 (1 处)<br>  - AGENTS.md:112 → 读取环境变量配置 (1 处)<br>  - examples/mock-host/index.ts:28 → 读取环境变量配置 (5 处)<br>  - examples/mock-host/smoke-client.ts:10 → 读取环境变量配置 (4 处)<br>  - .github/workflows/release.yml:115 → 读取 npm 凭证 (1 处)<br>  ... 共 35 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - pnpm-lock.yaml:111 → 深层目录穿越 (15 处)<br>  - examples/mock-host/tsconfig.json:2 → 深层目录穿越 (1 处)<br>  - examples/mock-host/tsconfig.check.json:2 → 深层目录穿越 (1 处)<br>  - examples/mock-host/smoke-client.ts:7 → 深层目录穿越 (2 处)<br>  - apps/server/tsconfig.json:2 → 深层目录穿越 (1 处)<br>  ... 共 27 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - vibe-coding.md:36 → 探测到 HTTP(S) 网络请求 (9 处)<br>  - vibe-coding.md:461 → WebSocket 连接 (8 处)<br>  - vibe-coding.md:461 → 浏览器网络 API (8 处)<br>  - CHANGELOG.md:62 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - CHANGELOG.md:7 → WebSocket 连接 (1 处)<br>涉及的域名: 10.0.2.2, 10.1.2.3, 100.64.0.3, 127.0.0.1, 169.254.1.1, 169.254.169.254, 172.20.0.2, 192.168.31.9, 8.8.8.8, REMOTE.example.com (+31 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - pnpm-lock.yaml:3144 → DDoS 攻击 (1 处)<br>  - packages/plugin/tests/remote-api-proxy.test.ts:6 → 代理/隧道 (1 处)<br>  - packages/plugin/tests/control-runtime.test.ts:352 → 远控/反向 shell (1 处)<br>  - packages/plugin/src/client.ts:307 → 远控/反向 shell (3 处)<br>  - packages/plugin/src/index.ts:446 → 代理/隧道 (1 处)<br>  ... 共 6 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - pnpm-lock.yaml:1118 → 敏感凭证读取 (70 处)<br>  - vibe-coding.md:597 → 敏感凭证读取 (8 处)<br>  - CHANGELOG.md:175 → 敏感凭证读取 (6 处)<br>  - README.zh.md:115 → 敏感凭证读取 (1 处)<br>  - TODO.md:54 → 敏感凭证读取 (9 处)<br>  ... 共 199 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - packages/plugin/tests/remote-api-proxy.test.ts:63 → 修改设置 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - fixtures/protocol/v1/control/limits.json:38 → 超长 base64 字符串 (3 处) |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 30 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - examples/mock-host/index.ts:493 → 定时任务 (1 处)<br>  - examples/mock-host/smoke-client.ts:135 → 定时任务 (1 处)<br>  - apps/vscode/src/extension.ts:60 → 定时任务 (3 处)<br>  - apps/vscode/src/remote.ts:313 → 定时任务 (1 处)<br>  - apps/vscode/src/werift-rtc.ts:521 → 定时任务 (1 处)<br>  ... 共 65 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - pnpm-lock.yaml:5006 → 云存储上传 (3 处)<br>  - CHANGELOG.md:448 → 云存储上传 (2 处)<br>  - TODO.md:54 → 云存储上传 (1 处)<br>  - README.md:219 → 云存储上传 (1 处)<br>  - .github/workflows/ci.yml:136 → 云存储上传 (6 处)<br>  ... 共 11 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 29. repo: 5 deps + 24 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 59998, 注释行: 1315 (2.2%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 91 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - apps/vscode/tests/sign-out.test.ts:78 → 硬编码敏感信息 (5 处)<br>  - apps/vscode/tests/controller.test.ts:81 → 硬编码敏感信息 (1 处)<br>  - apps/vscode/src/extension.ts:716 → 硬编码敏感信息 (2 处)<br>  - apps/server/web/src/theme.tsx:80 → 明文写入敏感信息 (1 处)<br>  - apps/server/tests/server.test.ts:12 → 硬编码敏感信息 (2 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - AGENTS.md:132 → 读取 git 历史 (1 处)<br>  - .github/workflows/ci.yml:85 → 读取 git 历史 (1 处)<br>  - docs/upgrade-0.1.7.md:146 → 读取 git 历史 (1 处)<br>  - docs/design/codex-session-history-projection-prompt.md:203 → 读取 git 历史 (2 处)<br>  - docs/screenshots/android-chat/README.md:28 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (44 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (7 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - scripts/install.sh:138 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - scripts/install.sh:1 → 修改系统目录 (4 处)<br>  - scripts/install.sh:134 → 创建开机自启/系统服务 (8 处)<br>  - scripts/install.sh:163 → 创建系统启动项 (1 处)<br>  - scripts/install-token.sh:1 → 修改系统目录 (1 处)<br>  - scripts/uninstall.sh:1 → 修改系统目录 (3 处)<br>  ... 共 10 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (8 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 1 天; 提交总数: 531 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ⚠️  需人工复核 | 发现 1 个公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ✅ 通过 | Stars: 266, Forks: 28, Watchers: 1 — 高 Star 量 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | ds-harness-remote |
| 校验 URL | https://github.com/liguobao/ds-harness-remote |
| 必查项通过率 | 14/33 (42%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-05 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
