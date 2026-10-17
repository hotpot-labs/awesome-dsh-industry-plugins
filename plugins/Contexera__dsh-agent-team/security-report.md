# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/Contexera/dsh-agent-team
- **校验时间**: 2026-10-17 03:33:21
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 14 | 13 | 6 |
| 🟡 推荐 | 14 | 7 | 7 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: master |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ⚠️  需人工复核 | 账号注册: 2026-10-08 (9 天前); 公开仓库数: 2; 粉丝数: 0; ⚠️ 账号注册不足 30 天 (9 天) |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1328; 包名: @contexera/dsh-agent-team; 描述: A persistent agent team for long-running collaboration in DeepSeek Harness — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - CHANGELOG.md:218 → 盗版/侵权 (1 处)<br>  - packages/agent-team/tests/recovery-hints.spec.ts:109 → 盗版/侵权 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (20): v0.2.3, v0.2.2, v0.2.1, v0.2.0, v0.1.15; package.json version: 0.2.3; GitHub Releases (5): v0.2.3, v0.2.2, v0.2.1, v0.2.0, v0.1.15 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @contexera/dsh-context-continuity: ^0.4.0; @contexera/dsh-jev: ^0.1.1; @deepseek-ai/cordis: ^4.0.1; @deepseek-ai/dsh-agent: >=0.2.0-rc.2 <0.2.1; @deepseek-ai/dsh-agent-default-model: >=0.2.0-rc.2 <0.2.1 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "external": ["@deepseek-ai; Cordis/DSH 依赖: @contexera/dsh-context-continuity, @contexera/dsh-jev, @deepseek-ai/cordis, @deepseek-ai/dsh-agent, @deepseek-ai/dsh-agent-default-model; Cordis 配置文件: cordis.patch.yml<br>  - .scratch/archive/2026-08/agent-team-storage-architecture/issues/02-route-agent-team-to-sqlite.md:47 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 217 处, 函数: 5092 个, 比例: 4.3% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: .scratch/archive/2026-09/team-perf/materials/phase0/zz-p0-changes.spec.ts; 发现清理逻辑: .scratch/archive/2026-09/team-perf/materials/phase0/zz-p0-version.spec.ts; 发现清理逻辑: .scratch/archive/2026-09/team-perf/materials/phase0/zz-t04-measure.spec.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .scratch/archive/2026-09/team-perf/materials/vera-replay-ruler.md:135 → 读取环境变量配置 (9 处)<br>  - .scratch/archive/2026-09/team-perf/materials/phase0/zz-p0-changes.spec.ts:20 → 读取环境变量配置 (2 处)<br>  - .scratch/archive/2026-09/team-perf/materials/phase0/zz-p0-version.spec.ts:38 → 读取环境变量配置 (4 处)<br>  - .scratch/archive/2026-09/team-perf/materials/phase0/zz-t04-measure.spec.ts:32 → 读取环境变量配置 (4 处)<br>  - .scratch/archive/2026-09/agent-team-simplification-audit/instrument/ablate-delete.mjs:16 → 读取环境变量配置 (1 处)<br>  ... 共 40 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - .scratch/archive/2026-10/issue-43-triage/decisions.md:73 → 深层目录穿越 (1 处)<br>  - .scratch/archive/2026-10/state-requests-diagnostics/README.md:16 → 深层目录穿越 (8 处)<br>  - .scratch/archive/2026-10/state-requests-diagnostics/issues/06-scale-and-failure-acceptance.md:109 → 深层目录穿越 (8 处)<br>  - .scratch/archive/2026-10/state-requests-diagnostics/materials/initial-audit.md:35 → 深层目录穿越 (30 处)<br>  - .scratch/archive/2026-09/team-perf/README.md:49 → 深层目录穿越 (1 处)<br>  ... 共 62 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - .scratch/archive/2026-09/agent-team-simplification-audit/instrument/ablate-delete.mjs:35 → 命令字符串拼接变量 (注入风险) (3 处)<br>  - .scratch/archive/2026-09/agent-team-simplification-audit/instrument/ablate-delete.mjs:80 → 开启 shell 模式 (注入风险) (1 处)<br>  - .scratch/archive/2026-09/agent-team-simplification-audit/instrument/ablate-stub.mjs:31 → 命令字符串拼接变量 (注入风险) (2 处)<br>  - .scratch/archive/2026-09/agent-team-simplification-audit/instrument/ablate-stub.mjs:60 → 开启 shell 模式 (注入风险) (1 处)<br>  - .scratch/archive/2026-09/windows-e2e-validation/validation/report.md:24 → 开启 shell 模式 (注入风险) (2 处)<br>  ... 共 12 处 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - CHANGELOG.md:3 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - README.zh.md:5 → 探测到 HTTP(S) 网络请求 (13 处)<br>  - README.md:5 → 探测到 HTTP(S) 网络请求 (13 处)<br>  - package.json:9 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - .scratch/archive/2026-10/thread-quoting-and-mentions/README.md:139 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: ..., 127.0.0.1, api.typesafe.ai, awesome-dsh-plugin.com, blog.xlab.app, bytetech.info, creativecommons.org, docs.github.com, docs.raft.build, example.com (+21 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - CONTRIBUTING.zh.md:46 → 敏感凭证读取 (2 处)<br>  - tsconfig.build-deps.json:1151 → API Key / Token 读取 (2 处)<br>  - tsconfig.build-deps.json:102 → 敏感凭证读取 (19 处)<br>  - CONTRIBUTING.md:46 → 敏感凭证读取 (2 处)<br>  - README.zh.md:148 → API Key / Token 读取 (1 处)<br>  ... 共 104 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - scripts/verify-desktop-strip-boot.mjs:96 → 写入配置文件 (1 处)<br>  - scripts/generate-typert.mjs:100 → 写入配置文件 (2 处)<br>  - packages/agent-team/tests/loader-composition.spec.ts:49 → 写入配置文件 (1 处)<br>  - packages/agent-team/tests/human-profile.spec.ts:226 → 写入配置文件 (3 处)<br>  - docs/frontend-design/components.md:77 → 修改设置 (1 处)<br>  ... 共 6 处 — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 64 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - .scratch/archive/2026-10/inbox-write-gate-redesign/README.md:21 → 临时文件操作 (1 处)<br>  - .scratch/archive/2026-10/inbox-write-gate-redesign/materials/evidence.md:3 → 临时文件操作 (1 处)<br>  - .scratch/archive/2026-10/state-requests-diagnostics/materials/initial-audit.md:77 → 临时文件操作 (1 处)<br>  - .scratch/archive/2026-09/team-perf/materials/vera-replay-ruler.md:32 → 临时文件操作 (13 处)<br>  - .scratch/archive/2026-09/team-perf/materials/phase0/zz-p0-changes.spec.ts:56 → 定时任务 (2 处)<br>  ... 共 76 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - tsconfig.build-deps.json:677 → 云存储上传 (4 处)<br>  - CHANGELOG.md:83 → 云存储上传 (2 处)<br>  - tsconfig.json:680 → 云存储上传 (4 处)<br>  - tsconfig.types.json:680 → 云存储上传 (4 处)<br>  - .scratch/archive/2026-10/quality-improvement/spec.md:24 → 云存储上传 (3 处)<br>  ... 共 47 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 20. repo: 4 deps + 16 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 55339, 注释行: 10332 (18.7%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 66 个, 例如: zz-p0-changes.spec.ts |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - packages/agent-team/tests/context-judge.spec.ts:21 → 硬编码敏感信息 (6 处)<br>  - packages/client-agent-team/tests/navigation.spec.ts:39 → 明文写入敏感信息 (4 处)<br>  - packages/client-agent-team/tests/drafts.spec.ts:102 → 明文写入敏感信息 (2 处)<br>  - packages/client-agent-team/tests/judge-form.spec.ts:42 → 硬编码敏感信息 (1 处)<br>  - packages/client-agent-team/tests/team-mode-conversation.client.spec.tsx:694 → 明文写入敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - CONTRIBUTING.zh.md:46 → 读取 git 历史 (2 处)<br>  - CONTRIBUTING.md:46 → 读取 git 历史 (2 处)<br>  - AGENTS.md:45 → 读取 git 历史 (1 处)<br>  - .scratch/archive/2026-10/quality-improvement/validation/2026-10-01-first-pass.md:16 → 读取 git 历史 (1 处)<br>  - .scratch/archive/2026-10/issue-43-triage/decisions.md:118 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (44 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (5 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - tsconfig.build-deps.json:237 → 修改系统目录 (2 处)<br>  - README.zh.md:148 → 修改系统目录 (1 处)<br>  - tsconfig.json:240 → 修改系统目录 (2 处)<br>  - tsconfig.types.json:240 → 修改系统目录 (2 处)<br>  - README.md:148 → 修改系统目录 (1 处)<br>  ... 共 29 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (10 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 664 |
| 7.2 | 未标记停止维护 | 必查 | ❌ 不通过 | 文档中发现弃用标记: deprecated, abandoned, archived |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 68, Forks: 16, Watchers: 0 — 有一定社区基础 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-agent-team |
| 校验 URL | https://github.com/Contexera/dsh-agent-team |
| 必查项通过率 | 14/33 (42%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-17 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
