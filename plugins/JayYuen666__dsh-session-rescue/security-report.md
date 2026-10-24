# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/JayYuen666/dsh-session-rescue
- **校验时间**: 2026-10-24 03:48:59
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 17 | 10 | 6 |
| 🟡 推荐 | 14 | 4 | 9 | 1 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2019-08-01 (2640 天前); 公开仓库数: 13; 粉丝数: 5 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 2190; 包名: @jayyuen66/dsh-session-rescue; 描述: Session rescue for dsh web: auto-resume on transient model failures, max-tokens  — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (4): v0.1.3, v0.1.2, v0.1.1, v0.1.0; package.json version: 0.1.3 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @jayyuen66/dsh-plugin-shared: catalog:; @deepseek-ai/dsh: ^0.2.1-rc.2; @deepseek-ai/dsh-brand: 0.2.1-rc.2; @deepseek-ai/dsh-typert-protocol: 0.2.1-rc.2; engines: {"dsh": "^0.2.1-rc.2", "node": ">=22.12.0"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"manifestVersion": 1, "bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "imm; Cordis/DSH 依赖: @jayyuen66/dsh-plugin-shared, @deepseek-ai/dsh, @deepseek-ai/dsh-brand, @deepseek-ai/dsh-typert-protocol; Cordis 配置文件: cordis.patch.yml<br>  - host.ts:1833 → Monkey patch / prototype pollution<br>  - lib/dock-state.ts:89 → Monkey patch / prototype pollution<br>  - test/host-contract.test.ts:1057 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 55 处, 函数: 2360 个, 比例: 2.3% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: host.ts; 发现清理逻辑: lib/resume-scheduler.ts; 发现清理逻辑: test/host-contract.test.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .npmrc:3 → 读取 npm 凭证 (2 处)<br>  - .github/workflows/publish.yml:71 → 读取 npm 凭证 (2 处)<br>  - test/profile-bundle.ts:52 → 读取环境变量配置 (1 处) |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - test/profile-bundle.ts:54 → 读取用户主目录 (1 处)<br>  - test/integration/agent-loop.test.ts:27 → 深层目录穿越 (1 处)<br>  - test/integration/goal-round.test.ts:34 → 深层目录穿越 (1 处)<br>  - test/integration/abort-semantics.test.ts:29 → 深层目录穿越 (1 处)<br>  - test/integration/loader-boot.test.ts:7 → 深层目录穿越 (1 处)<br>  ... 共 9 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - CHANGELOG.md:52 → 开启 shell 模式 (注入风险) (1 处)<br>  - build-types.mjs:56 → 开启 shell 模式 (注入风险) (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - CHANGELOG.md:3 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - .npmrc:5 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - icon.svg:1 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - package.json:12 → 探测到 HTTP(S) 网络请求 (4 处)<br>  - .github/workflows/publish.yml:28 → 探测到 HTTP(S) 网络请求 (4 处)<br>涉及的域名: github.com, keepachangelog.com, registry.npmjs.org, semver.org<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - pnpm-lock.yaml:269 → API Key / Token 读取 (3 处)<br>  - pnpm-lock.yaml:90 → 敏感凭证读取 (10 处)<br>  - pnpm-workspace.yaml:56 → 敏感凭证读取 (1 处)<br>  - README.zh-CN.md:33 → 敏感凭证读取 (2 处)<br>  - README.md:35 → 敏感凭证读取 (3 处)<br>  ... 共 15 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - test/build-client.test.ts:148 → node:vm 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 79 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - build-client.mjs:107 → 进程控制 (1 处)<br>  - test/client-ui.test.ts:172 → 定时任务 (2 处)<br>  - src/client-entry.ts:354 → 定时任务 (1 处) — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - pnpm-lock.yaml:72 → 云存储上传 (6 处)<br>  - pnpm-workspace.yaml:38 → 云存储上传 (1 处)<br>  - package.json:80 → 云存储上传 (1 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ❌ 不通过 | 总依赖数: 78. repo: 2 deps + 76 devDeps — 依赖过多 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 23171, 注释行: 3805 (16.4%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 27 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - .github/workflows/publish.yml:81 → 硬编码敏感信息 (1 处)<br>  - test/integration/agent-loop.test.ts:100 → 硬编码敏感信息 (1 处)<br>  - test/integration/goal-round.test.ts:74 → 硬编码敏感信息 (1 处)<br>  - test/integration/abort-semantics.test.ts:54 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (4 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ⚠️  需人工复核 | 未发现一键清理功能, 需确认是否有数据清理机制 |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - build-client.mjs:1 → 修改系统目录 (1 处)<br>  - build-host.mjs:1 → 修改系统目录 (1 处)<br>  - build-types.mjs:1 → 修改系统目录 (1 处) |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ⚠️  需人工复核 | 未发现临时文件清理逻辑, 需确认 |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 4 天; 提交总数: 9 |
| 7.2 | 未标记停止维护 | 必查 | ❌ 不通过 | 文档中发现弃用标记: deprecated |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-session-rescue |
| 校验 URL | https://github.com/JayYuen666/dsh-session-rescue |
| 必查项通过率 | 17/33 (52%) |
| 推荐项满足率 | 13/14 (约 93%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-24 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
