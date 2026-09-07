# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/cyjyyd/dsh-ssh-tui
- **校验时间**: 2026-09-07 03:37:04
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 21 | 8 | 4 |
| 🟡 推荐 | 14 | 6 | 8 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2018-07-07 (2983 天前); 公开仓库数: 17; 粉丝数: 3 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1370; 包名: dsh-ssh-tui; 描述: SSH-friendly interactive terminal TUI plugin for DeepSeek Harness — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (12): v0.4.1, v0.4.0, v0.3.10, v0.3.9, v0.3.8; package.json version: 0.5.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.1; @deepseek-ai/dsh-agent: >=0.1.1-rc.2 \|\| >=0.1.2-a; @deepseek-ai/dsh-agent-default-model: >=0.1.1-rc.2 \|\| >=0.1.2-a; @deepseek-ai/dsh-agent-loop: >=0.1.1-rc.2 \|\| >=0.1.2-a; @deepseek-ai/dsh-agent-presets: >=0.1.1-rc.2 \|\| >=0.1.2-a |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ✅ 通过 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}}; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-agent, @deepseek-ai/dsh-agent-default-model, @deepseek-ai/dsh-agent-loop, @deepseek-ai/dsh-agent-presets; Cordis 配置文件: cordis.patch.yml |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 163 处, 函数: 1130 个, 比例: 14.4% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: src/picker.ts; 发现清理逻辑: src/index.ts; 发现清理逻辑: src/tui.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - README.en.md:166 → 读取环境变量配置 (2 处)<br>  - .gitignore:14 → 读取环境变量配置 (2 处)<br>  - README.md:347 → 读取环境变量配置 (2 处)<br>  - cordis.patch.yml:28 → 读取环境变量配置 (2 处)<br>  - tests/helpers.test.mjs:1380 → 读取环境变量配置 (8 处)<br>  ... 共 20 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - src/supergrok-token.ts:14 → 读取用户主目录 (2 处)<br>  - src/index.ts:22 → 读取用户主目录 (1 处)<br>  - src/tui.ts:887 → 读取用户主目录 (9 处)<br>  - src/display-sock.ts:97 → 读取用户主目录 (1 处)<br>  - src/session-lock.ts:40 → 读取用户主目录 (5 处) — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - scripts/ansi-to-png.py:224 → Python subprocess (1 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - README.en.md:3 → 探测到 HTTP(S) 网络请求 (14 处)<br>  - package.json:18 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - package-lock.json:87 → 探测到 HTTP(S) 网络请求 (51 处)<br>  - README.md:3 → 探测到 HTTP(S) 网络请求 (15 处)<br>  - tests/helpers.test.mjs:845 → 探测到 HTTP(S) 网络请求 (7 处)<br>涉及的域名: api.deepseek.com, api.example.com, api.minimax.chat, api.minimaxi.com, auth.x.ai, cli-chat-proxy.grok.com, dshfind.com, github.com, img.shields.io, opencode.ai (+5 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - README.en.md:166 → API Key / Token 读取 (3 处)<br>  - README.en.md:167 → 敏感凭证读取 (7 处)<br>  - package.json:89 → 敏感凭证读取 (3 处)<br>  - package-lock.json:27 → 敏感凭证读取 (6 处)<br>  - .gitignore:13 → 敏感凭证读取 (3 处)<br>  ... 共 30 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 35 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - tests/session-list.test.mjs:107 → 定时任务 (1 处)<br>  - tests/session-list.test.mjs:125 → 临时文件操作 (6 处)<br>  - tests/helpers.test.mjs:284 → 临时文件操作 (4 处)<br>  - tests/session-lock.test.mjs:31 → 临时文件操作 (2 处)<br>  - tests/auto-approval.test.mjs:58 → 临时文件操作 (1 处)<br>  ... 共 21 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - README.en.md:465 → 云存储上传 (1 处)<br>  - .gitignore:13 → 云存储上传 (1 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 35. repo: 2 deps + 33 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 17343, 注释行: 1013 (5.8%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - tests/helpers.test.mjs:2069 → 硬编码敏感信息 (4 处)<br>  - src/supergrok-token.ts:151 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - tests/auto-approval.test.mjs:15 → 读取 git 历史 (1 处)<br>  - scripts/capture-readme-frames.mjs:22 → 读取 git 历史 (2 处)<br>  - scripts/capture-slow-link.mjs:31 → 读取 git 历史 (2 处)<br>  - src/tui.ts:2600 → 读取 git 历史 (2 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (3 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (6 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - tests/auto-approval.test.mjs:34 → 要求 root/sudo 权限<br>  - tests/approval-reviewer.test.mjs:14 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - README.en.md:198 → 修改系统目录 (1 处)<br>  - tests/auto-approval.test.mjs:60 → 修改系统目录 (1 处)<br>  - tests/display-sock.test.mjs:80 → 修改系统目录 (1 处)<br>  - scripts/uninstall.sh:1 → 修改系统目录 (1 处)<br>  - scripts/capture-readme-frames.mjs:1 → 修改系统目录 (1 处)<br>  ... 共 15 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (1 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 57 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 1, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-ssh-tui |
| 校验 URL | https://github.com/cyjyyd/dsh-ssh-tui |
| 必查项通过率 | 21/33 (64%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-09-07 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
