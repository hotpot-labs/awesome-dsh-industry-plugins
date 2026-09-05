# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/WODE25500/dsh-google-skills
- **校验时间**: 2026-09-05 03:35:36
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 16 | 11 | 6 |
| 🟡 推荐 | 14 | 4 | 10 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ⚠️  需人工复核 | 账号注册: 2026-08-19 (16 天前); 公开仓库数: 38; 粉丝数: 0; ⚠️ 账号注册不足 30 天 (16 天) |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 122; 包名: dsh-google-skills; 描述: Google's Agent Skills (google/skills) for DeepSeek Harness: 128 SKILL.md for Goo — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - skills/developer-device-platform-basics/SKILL.md:162 → 盗版/侵权 (7 处)<br>  - skills/google-cloud-solution-multi-agent-security/SKILL.md:87 → 欺诈行为 (1 处)<br>  - skills/google-cloud-scc-query/SKILL.md:47 → 盗版/侵权 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ⚠️  需人工复核 | 无 git tag; package.json version: 0.1.0; 有版本号但无 git tag / release |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.1 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ✅ 通过 | dsh 配置: {"bundle": {"patch": "cordis.patch.yml"}}; Cordis/DSH 依赖: @deepseek-ai/cordis; Cordis 配置文件: cordis.patch.yml |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 2 处, 函数: 3 个, 比例: 66.7% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 未使用定时器, 无资源释放问题 |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - skills/managed-airflow-dag-authoring/SKILL.md:173 → 读取环境变量配置 (1 处)<br>  - skills/managed-airflow-migrations/SKILL.md:320 → 读取环境变量配置 (1 处)<br>  - skills/agent-platform-migrate-from-ai-studio/SKILL.md:277 → 读取凭证文件 (2 处)<br>  - skills/gke-cluster-autoscaler/SKILL.md:16 → 读取浏览器 Cookie/本地存储 (3 处)<br>  - skills/google-ads-api-quickstart/SKILL.md:145 → 读取凭证文件 (1 处)<br>  ... 共 7 处 |
| 3.2 | 无全局文件读写 | 必查 | ✅ 通过 | 未检测到全局文件访问模式 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - skills/agent-platform-inference/SKILL.md:356 → Python subprocess (2 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - README.md:3 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - README.zh.md:3 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - skills/google-mobile-ads-android-migrate-to-next-gen/SKILL.md:28 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - skills/google-cloud-solution-rag-enterprise-search-gke-sqldb/SKILL.md:153 → 探测到 HTTP(S) 网络请求 (6 处)<br>  - skills/gemini-api/SKILL.md:39 → 探测到 HTTP(S) 网络请求 (9 处)<br>涉及的域名: 0.0.0.0, adk.dev, ads.google.com, agentregistry.googleapis.com, ai.google.dev, aiplatform., aiplatform.googleapis.com, aiplatform.mtls.googleapis.com, antigravity.google, api.github.com (+39 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - skills/gke-service-networking/SKILL.md:73 → DDoS 攻击 (1 处)<br>  - skills/google-cloud-waf-security/SKILL.md:127 → DDoS 攻击 (2 处)<br>  - skills/google-cloud-recipe-auth/SKILL.md:14 → 挖矿相关 (1 处)<br>  - skills/google-cloud-global-frontend-configuration/SKILL.md:94 → DDoS 攻击 (1 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - skills/gemini-api/SKILL.md:76 → API Key / Token 读取 (3 处)<br>  - skills/gemini-api/SKILL.md:6 → 敏感凭证读取 (2 处)<br>  - skills/alloydb-basics/SKILL.md:37 → 敏感凭证读取 (6 处)<br>  - skills/gke-service-networking/SKILL.md:127 → 敏感凭证读取 (1 处)<br>  - skills/gke-app-onboarding/SKILL.md:30 → 敏感凭证读取 (2 处)<br>  ... 共 64 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - skills/agent-platform-eval-flywheel/SKILL.md:421 → eval() 任意代码执行 (2 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 1 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - skills/gemini-live-api/SKILL.md:42 → 临时文件操作 (1 处)<br>  - skills/iam-helper-for-policy-simulator/SKILL.md:38 → 临时文件操作 (19 处)<br>  - skills/gke-manifest-generation/SKILL.md:79 → 临时文件操作 (1 处)<br>  - skills/gke-workload-troubleshooting/SKILL.md:172 → 临时文件操作 (1 处)<br>  - scripts/check-skills.mjs:32 → 进程控制 (1 处) — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - package.json:28 → 云服务 SDK (可能用于隐蔽上传) (1 处)<br>  - skills/google-cloud-solution-rag-enterprise-search-gke-sqldb/SKILL.md:2 → 云服务 SDK (可能用于隐蔽上传) (1 处)<br>  - skills/google-cloud-solution-rag-enterprise-search-gke-sqldb/SKILL.md:68 → 云存储上传 (1 处)<br>  - skills/gemini-api/SKILL.md:29 → 云服务 SDK (可能用于隐蔽上传) (4 处)<br>  - skills/bigquery-bigframes/SKILL.md:6 → 云服务 SDK (可能用于隐蔽上传) (1 处)<br>  ... 共 53 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 无第三方依赖 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 43, 注释行: 8 (18.6%) |
| 4.9 | 具备测试覆盖 | 推荐 | ⚠️  需人工复核 | 未发现测试文件 |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ✅ 通过 | README 中包含数据上报说明: analytics |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - skills/gemini-api/SKILL.md:79 → 硬编码敏感信息 (1 处)<br>  - skills/agent-platform-deploy/SKILL.md:277 → 硬编码敏感信息 (1 处)<br>  - skills/agent-platform-inference/SKILL.md:392 → 硬编码敏感信息 (1 处)<br>  - skills/google-ads-api-mcp-setup/SKILL.md:197 → 硬编码敏感信息 (3 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - skills/gke-workload-troubleshooting/SKILL.md:134 → 读取 git 历史 (2 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (37 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ⚠️  需人工复核 | 未发现一键清理功能, 需确认是否有数据清理机制 |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - skills/gemini-live-api/SKILL.md:92 → 要求 root/sudo 权限<br>  - skills/google-ads-api-mcp-setup/SKILL.md:99 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - skills/google-ads-api-mcp-setup/SKILL.md:412 → 修改系统目录 (1 处) |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (9 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 11 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: 配置说明, 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-google-skills |
| 校验 URL | https://github.com/WODE25500/dsh-google-skills |
| 必查项通过率 | 16/33 (48%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-09-05 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
