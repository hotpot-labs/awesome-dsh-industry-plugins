# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/BillyChen123/qdd
- **校验时间**: 2026-08-23 14:28:04
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 20 | 8 | 5 |
| 🟡 推荐 | 14 | 6 | 8 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2021-12-13 (1714 天前); 公开仓库数: 9; 粉丝数: 3 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: Apache-2.0 (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1095; 包名: qdd; 描述: Question-Driven Discovery CLI — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - src/runtime/bootstrap-prompts/qdd-propose.md:103 → 盗版/侵权 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (1): v0.1.0-rc.1; package.json version: 0.1.0-rc.1; GitHub Releases (1): v0.1.0-rc.1 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | engines: {"node": ">=20.19.0"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ✅ 通过 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": ["@deepseek-ai/dsh-client-runtime",; Cordis 配置文件: cordis.patch.yml |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 267 处, 函数: 1481 个, 比例: 18.0% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: src/services/manuscript-package.ts; 发现清理逻辑: src/runtime/dsh-assets/plugins/qdd-auto.mjs; 发现清理逻辑: src/runtime/dsh-assets/plugins/qdd-worker.mjs |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .gitignore:6 → 读取环境变量配置 (2 处)<br>  - src/ui/auto-stream.ts:114 → 读取环境变量配置 (7 处)<br>  - src/services/manuscript-package.ts:36 → 读取环境变量配置 (1 处)<br>  - src/test-support/conclude-behavior-eval.ts:669 → 读取环境变量配置 (5 处)<br>  - src/test/dsh-bootstrap.test.ts:19 → 读取环境变量配置 (24 处)<br>  ... 共 22 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - src/ui/auto-stream.ts:20 → 深层目录穿越 (1 处)<br>  - src/services/closure.ts:47 → 目录遍历 (4 处)<br>  - src/services/tasks.ts:69 → 目录遍历 (1 处)<br>  - src/services/inspection.ts:464 → 目录遍历 (3 处)<br>  - src/test-support/conclude-eval-case.ts:100 → 目录遍历 (1 处)<br>  ... 共 24 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - README.zh-CN.md:132 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - CLAUDE.md:99 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - AGENTS.md:99 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - package.json:8 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - package-lock.json:35 → 探测到 HTTP(S) 网络请求 (181 处)<br>涉及的域名: 127.0.0.1, api.crossref.org, api.deepseek.com, api.github.com, awesome-dsh-plugin.com, bio-bigdata.hrbmu.edu.cn, biomni.stanford.edu, eutils.ncbi.nlm.nih.gov, example.test, github.com (+10 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - LICENSE:149 → 挖矿相关 (1 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - README.zh-CN.md:131 → API Key / Token 读取 (1 处)<br>  - CLAUDE.md:157 → API Key / Token 读取 (1 处)<br>  - CLAUDE.md:154 → 敏感凭证读取 (4 处)<br>  - AGENTS.md:157 → API Key / Token 读取 (1 处)<br>  - AGENTS.md:154 → 敏感凭证读取 (4 处)<br>  ... 共 63 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 11 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - openspec/changes/archive/2026-05-31-tighten-qdd-apply-packaging-and-patience/protocol.md:29 → 临时文件操作 (3 处)<br>  - openspec/changes/archive/2026-06-05-harden-apply-close-artifact-lifecycle/checklist.md:4 → 临时文件操作 (2 处)<br>  - openspec/changes/archive/2026-06-05-harden-apply-close-artifact-lifecycle/project.md:28 → 临时文件操作 (2 处)<br>  - openspec/changes/archive/2026-06-05-harden-apply-close-artifact-lifecycle/task.md:43 → 临时文件操作 (1 处)<br>  - openspec/changes/archive/2026-06-05-harden-apply-close-artifact-lifecycle/protocol.md:33 → 临时文件操作 (5 处)<br>  ... 共 79 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ✅ 通过 | 未检测到文件窃取/静默上传模式 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 11. repo: 8 deps + 3 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 31076, 注释行: 442 (1.4%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 20 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - README.zh-CN.md:131 → 硬编码敏感信息 (1 处)<br>  - README.md:133 → 硬编码敏感信息 (1 处)<br>  - src/test/smoke.test.ts:607 → 硬编码敏感信息 (1 处)<br>  - src/runtime/dsh-assets/plugins/qdd-tool.mjs:105 → 硬编码敏感信息 (1 处)<br>  - docs/10-symphony-setup-and-pitfalls.md:322 → 硬编码敏感信息 (2 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - openspec/changes/archive/2026-06-12-stabilize-managed-yaml-writes/checklist.md:30 → 读取 git 历史 (1 处)<br>  - openspec/changes/archive/2026-06-12-stabilize-managed-yaml-writes/task.md:44 → 读取 git 历史 (1 处)<br>  - openspec/changes/archive/2026-06-13-add-thesis-frontier-planning/checklist.md:51 → 读取 git 历史 (1 处)<br>  - openspec/changes/archive/2026-06-13-add-thesis-frontier-planning/task.md:55 → 读取 git 历史 (1 处)<br>  - openspec/changes/archive/2026-06-13-fix-auto-dissolution-continuation/checklist.md:31 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (32 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ⚠️  需人工复核 | 未发现一键清理功能, 需确认是否有数据清理机制 |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - bin/qdd.js:1 → 修改系统目录 (1 处)<br>  - domain-skills/singlecell/scrna/sc-group-stats/scripts/scrna_group_stats.py:1 → 修改系统目录 (1 处)<br>  - domain-skills/singlecell/scrna/sc-differential-expression/scripts/scrna_differential_expression.py:1 → 修改系统目录 (1 处)<br>  - domain-skills/singlecell/scrna/sc-pathway-enrichment/scripts/scrna_pathway_enrichment.py:1 → 修改系统目录 (1 处)<br>  - domain-skills/singlecell/scrna/sc-preprocess-qc/scripts/scrna_preprocess_qc.py:1 → 修改系统目录 (1 处)<br>  ... 共 30 处 |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (2 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 4 天; 提交总数: 148 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 5, Forks: 1, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | qdd |
| 校验 URL | https://github.com/BillyChen123/qdd |
| 必查项通过率 | 20/33 (61%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-23 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
