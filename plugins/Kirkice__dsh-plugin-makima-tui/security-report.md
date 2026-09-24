# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/Kirkice/dsh-plugin-makima-tui
- **校验时间**: 2026-09-24 03:48:02
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 13 | 12 | 8 |
| 🟡 推荐 | 14 | 5 | 9 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2018-05-13 (3055 天前); 公开仓库数: 49; 粉丝数: 87 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1816; 包名: makima-tui; 描述: Makima TUI for deepseek-harness with JellyFish colors — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - src/types.ts:131 → 绕过权限限制 (1 处)<br>  - src/components/prompts.tsx:286 → 绕过权限限制 (1 处)<br>  - src/__tests__/planApproval.test.ts:21 → 绕过权限限制 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ⚠️  需人工复核 | 无 git tag; package.json version: 0.1.0; 有版本号但无 git tag / release |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.1; @deepseek-ai/dsh-agent: ^0.1.0-rc.7; @deepseek-ai/dsh-llm: ^0.1.0-rc.7; @deepseek-ai/dsh-session: ^0.1.0-rc.7; @deepseek-ai/dsh-tools: ^0.1.0-rc.7 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}}; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-agent, @deepseek-ai/dsh-llm, @deepseek-ai/dsh-session, @deepseek-ai/dsh-tools; Cordis 配置文件: cordis.patch.yml<br>  - src/gatewayClient.ts:964 → Monkey patch / prototype pollution<br>  - src/components/billingOverlay.tsx:99 → Monkey patch / prototype pollution<br>  - src/app/turnController.ts:1366 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 309 处, 函数: 6361 个, 比例: 4.9% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: scripts/profile-tui.mjs; 发现清理逻辑: test/ink-smoke.test.ts; 发现清理逻辑: test/app-layout-mount.test.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - cordis.patch.yml:17 → 读取环境变量配置 (2 处)<br>  - scripts/check-format.mjs:24 → 读取环境变量配置 (2 处)<br>  - scripts/capture-screenshot.py:42 → 读取环境变量配置 (1 处)<br>  - scripts/profile-tui.mjs:20 → 读取环境变量配置 (6 处)<br>  - scripts/tool-gallery.py:168 → 读取环境变量配置 (2 处)<br>  ... 共 99 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - src/components/branding.tsx:538 → 读取用户主目录 (2 处)<br>  - src/lib/appHome.ts:17 → 读取用户主目录 (1 处)<br>  - src/lib/terminalSetup.ts:165 → 读取用户主目录 (3 处)<br>  - src/lib/memoryEdit.ts:32 → 读取用户主目录 (3 处)<br>  - src/app/slash/commands/billing.ts:7 → 深层目录穿越 (4 处)<br>  ... 共 22 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - scripts/capture-screenshot.py:44 → Python subprocess (1 处)<br>  - scripts/tool-gallery.py:220 → Python subprocess (1 处)<br>  - scripts/e2e/run_install.py:36 → Python subprocess (2 处)<br>  - scripts/e2e/run_core.py:92 → Python subprocess (1 处)<br>  - packages/makima-tui-ink/src/utils/execFileNoThrow.ts:1 → 加载 child_process (1 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - src/lib/openExternalUrl.test.ts:152 → 开启 shell 模式 (注入风险) (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package-lock.json:76 → 探测到 HTTP(S) 网络请求 (1033 处)<br>  - package-lock.json:175 → WebSocket 连接 (4 处)<br>  - package-lock.json:175 → 浏览器网络 API (4 处)<br>  - install.sh:4 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - README.md:5 → 探测到 HTTP(S) 网络请求 (18 处)<br>涉及的域名: 127.0.0.1, a.com, a.example, anthropic.slack.com, api.example.test, api.fish.audio, api.openai.com, auth.example.test, auth.openai.com, b.com (+38 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - src/__tests__/text.test.ts:240 → 挖矿相关 (2 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - package-lock.json:172 → 敏感凭证读取 (57 处)<br>  - cordis.patch.yml:17 → 读取环境变量 API Key/凭证 (2 处)<br>  - cordis.patch.yml:16 → API Key / Token 读取 (2 处)<br>  - cordis.patch.yml:12 → 敏感凭证读取 (1 处)<br>  - README.md:194 → API Key / Token 读取 (3 处)<br>  ... 共 119 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - src/__tests__/logoPalettes.test.ts:152 → 写入配置文件 (1 处)<br>  - src/__tests__/harnessClient.test.ts:1920 → 写入配置文件 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - src/lib/text.ts:21 → 连续十六进制转义 (混淆) (1 处) |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 43 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - scripts/check-format.mjs:33 → 进程控制 (2 处)<br>  - scripts/verify-boundary.mjs:48 → 进程控制 (1 处)<br>  - scripts/profile-tui.mjs:213 → 进程控制 (1 处)<br>  - test/app-layout-mount.test.ts:115 → 定时任务 (1 处)<br>  - test/e2e/mock-llm.mjs:112 → 定时任务 (1 处)<br>  ... 共 91 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - package-lock.json:119 → 云服务 SDK (可能用于隐蔽上传) (103 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 43. repo: 1 deps + 42 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 83779, 注释行: 10934 (13.1%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 157 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - src/lib/terminalSetup.ts:373 → 明文写入敏感信息 (1 处)<br>  - src/harness/mcpManager.ts:90 → 从环境变量获取敏感信息 (1 处)<br>  - src/__tests__/openAiCodexAuth.test.ts:71 → 硬编码敏感信息 (8 处)<br>  - src/__tests__/osc52.test.ts:8 → 从环境变量获取敏感信息 (1 处)<br>  - src/__tests__/harnessClient.test.ts:1266 → 硬编码敏感信息 (2 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (16 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (7 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - src/components/appOverlays.tsx:130 → 要求 root/sudo 权限<br>  - src/app/createGatewayEventHandler.ts:902 → 要求 root/sudo 权限<br>  - src/app/useMainApp.ts:757 → 要求 root/sudo 权限<br>  - src/app/overlayStore.ts:86 → 要求 root/sudo 权限<br>  - src/app/usePet.ts:52 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - install.sh:1 → 修改系统目录 (1 处)<br>  - scripts/capture-screenshot.py:1 → 修改系统目录 (1 处)<br>  - scripts/pack-plugin.mjs:1 → 修改系统目录 (1 处)<br>  - scripts/verify-boundary.mjs:1 → 修改系统目录 (1 处)<br>  - scripts/build.mjs:1 → 修改系统目录 (2 处)<br>  ... 共 26 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (2 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 6 天; 提交总数: 37 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 1, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-plugin-makima-tui |
| 校验 URL | https://github.com/Kirkice/dsh-plugin-makima-tui |
| 必查项通过率 | 13/33 (39%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-09-24 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
