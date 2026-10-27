# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/JayYuen666/dsh-dir-prep-organize
- **校验时间**: 2026-10-27 04:18:47
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 12 | 13 | 8 |
| 🟡 推荐 | 14 | 6 | 8 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2019-08-01 (2643 天前); 公开仓库数: 13; 粉丝数: 5 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 3533; 包名: @jayyuen66/dsh-dir-prep-organize; 描述: dsh 插件：对话输入框「润色」按钮（主键直接润色/▾ 以角色风格润色，结合当前目录 + session 模型润色草稿）+「模板」下拉（内置精选角色集生成自插件 — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - agents/finance/finance-fraud-detector.md:3 → 欺诈行为 (10 处)<br>  - agents/finance/finance-investment-researcher.md:262 → 非法爬取 (1 处)<br>  - agents/security/security-senior-secops.md:507 → 破解授权 (1 处)<br>  - agents/security/security-senior-secops.md:504 → 盗版/侵权 (2 处)<br>  - agents/security/security-incident-responder.md:308 → 欺诈行为 (3 处)<br>  ... 共 19 处 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (8): v0.1.6, v0.1.5, v0.1.4, v0.1.3, v0.1.2-rc; package.json version: 0.1.6 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @jayyuen66/dsh-plugin-shared: catalog:; @deepseek-ai/cordis: 4.0.5; @deepseek-ai/dsh: ^0.2.1-rc.3; @deepseek-ai/dsh-agent-default-model: 0.2.1-rc.3; @deepseek-ai/dsh-brand: 0.2.1-rc.3 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"manifestVersion": 1, "bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "imm; Cordis/DSH 依赖: @jayyuen66/dsh-plugin-shared, @deepseek-ai/cordis, @deepseek-ai/dsh, @deepseek-ai/dsh-agent-default-model, @deepseek-ai/dsh-brand; Cordis 配置文件: cordis.patch.yml<br>  - agents/security/security-penetration-tester.md:385 → Monkey patch / prototype pollution<br>  - agents/engineering/engineering-code-reviewer.md:112 → Monkey patch / prototype pollution<br>  - test/templates.test.ts:432 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 89 处, 函数: 2009 个, 比例: 4.4% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: test/client.test.ts; 发现清理逻辑: test/routes.test.ts; 发现清理逻辑: test/schema-coverage.test.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - host.ts:819 → 读取 SSH 私钥目录 (1 处)<br>  - host.ts:736 → 读取 AWS 凭证 (3 处)<br>  - host.ts:222 → 读取 SSH 私钥 (1 处)<br>  - host.ts:215 → 读取凭证文件 (1 处)<br>  - README.zh-CN.md:175 → 读取 SSH 私钥 (1 处)<br>  ... 共 28 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - host.ts:812 → 深层目录穿越 (2 处)<br>  - .github/workflows/ci.yml:40 → 读取用户主目录 (1 处)<br>  - agents/specialized/lsp-index-engineer.md:184 → 全局文件匹配 (1 处)<br>  - test/client.test.ts:100 → 读取用户主目录 (1 处)<br>  - test/host.test.ts:1201 → 深层目录穿越 (3 处)<br>  ... 共 9 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - agents/security/security-appsec-engineer.md:238 → Python subprocess (1 处)<br>  - agents/engineering/engineering-voice-ai-integration-engineer.md:120 → Python subprocess (4 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - .github/workflows/ci.yml:205 → exec 命令拼接 (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - CHANGELOG.md:3 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - README.zh-CN.md:2 → 探测到 HTTP(S) 网络请求 (39 处)<br>  - .npmrc:5 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - icon.svg:1 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - README.md:2 → 探测到 HTTP(S) 网络请求 (39 处)<br>涉及的域名: 127.0.0.1, aistudio.google.com, api.example.com, api.iconify.design, app.example.com, attack.mitre.org, auth.example.com, badge.fury.io, cdn.jsdelivr.net, creator.xiaohongshu.com (+40 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - agents/security/security-threat-detection-engineer.md:201 → 恶意软件 (2 处)<br>  - agents/security/security-incident-responder.md:295 → 恶意软件 (1 处)<br>  - agents/security/security-penetration-tester.md:278 → 代理/隧道 (1 处)<br>  - agents/strategy/runbooks/scenario-incident-response.md:15 → DDoS 攻击 (1 处)<br>  - agents/engineering/engineering-mechanical-design-engineer.md:38 → 挖矿相关 (1 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - host.ts:215 → API Key / Token 读取 (3 处)<br>  - host.ts:189 → 敏感凭证读取 (14 处)<br>  - pnpm-lock.yaml:93 → 敏感凭证读取 (1 处)<br>  - pnpm-workspace.yaml:59 → 敏感凭证读取 (1 处)<br>  - README.zh-CN.md:175 → 敏感凭证读取 (4 处)<br>  ... 共 54 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - test/host.test.ts:1945 → 写入配置文件 (1 处)<br>  - test/integration/settings-boot.test.ts:301 → 修改设置 (8 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - agents/security/security-senior-secops.md:314 → eval() 任意代码执行 (1 处)<br>  - agents/engineering/engineering-ai-engineer.md:50 → eval() 任意代码执行 (1 处)<br>  - agents/engineering/engineering-cms-developer.md:447 → eval() 任意代码执行 (1 处)<br>  - agents/engineering/engineering-ai-data-remediation-engineer.md:161 → eval() 任意代码执行 (1 处)<br>  - src/default-templates.generated.ts:84 → eval() 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 42 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - host.ts:1594 → 定时任务 (1 处)<br>  - .github/workflows/ci.yml:153 → 临时文件操作 (14 处)<br>  - agents/design/design-whimsy-injector.md:311 → 定时任务 (4 处)<br>  - agents/security/security-senior-secops.md:210 → 进程控制 (2 处)<br>  - agents/security/security-incident-responder.md:214 → 临时文件操作 (3 处)<br>  ... 共 17 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - pnpm-lock.yaml:74 → 云存储上传 (1 处)<br>  - pnpm-workspace.yaml:40 → 云存储上传 (1 处)<br>  - .github/dependabot.yml:22 → 云存储上传 (1 处)<br>  - .github/workflows/ci.yml:88 → 云存储上传 (2 处)<br>  - .github/workflows/scorecard.yml:57 → 云存储上传 (4 处)<br>  ... 共 19 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 41. repo: 1 deps + 40 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 19632, 注释行: 3316 (16.9%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 19 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - .github/workflows/publish.yml:100 → 硬编码敏感信息 (2 处)<br>  - agents/security/security-senior-secops.md:106 → 明文写入敏感信息 (2 处)<br>  - agents/security/security-senior-secops.md:36 → 硬编码敏感信息 (8 处)<br>  - agents/security/security-senior-secops.md:62 → 从环境变量获取敏感信息 (1 处)<br>  - agents/testing/testing-api-tester.md:68 → 从环境变量获取敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - agents/specialized/specialized-workflow-architect.md:473 → 读取 git 历史 (1 处)<br>  - agents/engineering/engineering-git-workflow-master.md:186 → 读取 git 历史 (2 处)<br>  - src/default-templates.generated.ts:110 → 读取 git 历史 (3 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (28 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (2 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - agents/security/security-incident-responder.md:282 → 要求 root/sudo 权限<br>  - agents/security/security-penetration-tester.md:301 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - host.ts:812 → 修改系统目录 (2 处)<br>  - build-client.mjs:1 → 修改系统目录 (1 处)<br>  - build-host.mjs:1 → 修改系统目录 (1 处)<br>  - build-types.mjs:1 → 修改系统目录 (1 处)<br>  - agents/support/support-infrastructure-maintainer.md:297 → 修改系统目录 (1 处)<br>  ... 共 17 处 |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (7 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 2 天; 提交总数: 8 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-dir-prep-organize |
| 校验 URL | https://github.com/JayYuen666/dsh-dir-prep-organize |
| 必查项通过率 | 12/33 (36%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-27 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
