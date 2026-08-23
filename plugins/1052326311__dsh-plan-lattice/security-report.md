# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/1052326311/dsh-plan-lattice
- **校验时间**: 2026-08-23 13:04:53
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 14 | 10 | 9 |
| 🟡 推荐 | 14 | 6 | 8 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2020-05-23 (2283 天前); 公开仓库数: 10; 粉丝数: 2 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 6456; 包名: dsh-plan-lattice; 描述: Native continuity recovery for long-running DeepSeek Harness agents — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - eval/router-corpus/v6/annotations-c.jsonl:239 → 绕过权限限制 (1 处)<br>  - eval/router-corpus/v4/blind-v4.prompts.jsonl:63 → 破解授权 (1 处)<br>  - eval/router-corpus/v4/adjudication-packet.jsonl:38 → 破解授权 (1 处)<br>  - eval/router-corpus/v4/candidates.jsonl:211 → 破解授权 (1 处)<br>  - eval/router-corpus/v7/annotations-c.jsonl:235 → 非法爬取 (2 处)<br>  ... 共 11 处 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (20): v0.4.0-rc.6, v0.4.0-rc.5, v0.4.0-rc.4, v0.4.0-rc.3, v0.4.0-rc.2; package.json version: 0.4.0-rc.8; GitHub Releases (5): v0.4.0-rc.6, v0.4.0-rc.5, router-v14-rc4-candidate-freeze, router-v14-protocol-freeze-v2, router-v14-protocol-freeze |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.1; @deepseek-ai/dsh-agent: 0.1.0-rc.7; @deepseek-ai/dsh-llm: 0.1.0-rc.7; @deepseek-ai/dsh-plan-mode: 0.1.0-rc.7; @deepseek-ai/dsh-session: 0.1.0-rc.7 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}}; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-agent, @deepseek-ai/dsh-llm, @deepseek-ai/dsh-plan-mode, @deepseek-ai/dsh-session; Cordis 配置文件: cordis.patch.yml<br>  - src/index.ts:4248 → Monkey patch / prototype pollution<br>  - eval/router-corpus/v4/supplement-raw.jsonl:14 → 直接修改内核源码<br>  - eval/router-corpus/v4/supplement-candidates.jsonl:14 → 直接修改内核源码 — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 1212 处, 函数: 9630 个, 比例: 12.6% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: demo/crash-continuity-worker.mjs; 发现清理逻辑: demo/first-drift-benchmark.mjs; 发现清理逻辑: prospective/router-v14/runtime-artifact.mjs |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - src/contract-anchor.ts:20 → 读取环境变量配置 (1 处)<br>  - .github/workflows/verify.yml:172 → 读取环境变量配置 (7 处)<br>  - prospective/router-v14/workflow.mjs:10 → 读取环境变量配置 (2 处)<br>  - prospective/model-rc4-study/v14-evidence.mjs:134 → 读取环境变量配置 (1 处)<br>  - prospective/model-rc4-study/prepare-execution.mjs:208 → 读取环境变量配置 (2 处)<br>  ... 共 145 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - src/contract-anchor.ts:20 → 读取用户主目录 (1 处)<br>  - prospective/router-v14/candidate-reveal.mjs:1 → 深层目录穿越 (3 处)<br>  - prospective/router-v14/shared-corpus.mjs:3 → 深层目录穿越 (2 处)<br>  - prospective/router-v14/workflow.mjs:12 → 深层目录穿越 (1 处)<br>  - prospective/model-rc4-study/v14-evidence.mjs:21 → 深层目录穿越 (2 处)<br>  ... 共 125 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - eval/pilots/driver/icae_adapter.py:252 → Python subprocess (1 处)<br>  - eval/v0.4/driver/icae_adapter.py:165 → Python subprocess (1 处)<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - eval/v0.4/tests/icae-pilot-driver.testcase.mjs:51 → 命令字符串拼接变量 (注入风险) (4 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package.json:15 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - README.md:5 → 探测到 HTTP(S) 网络请求 (17 处)<br>  - BENCHMARK.md:81 → 探测到 HTTP(S) 网络请求 (9 处)<br>  - demo/first-drift-benchmark.mjs:875 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - demo/results/first-drift-summary.svg:1 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: 127.0.0.1, api.deepseek.com, api.github.com, awesome-dsh-plugin.com, data.gharchive.org, docs.example.com, evaluation-proxy.invalid, example.com, example.test, frozen-endpoint.example (+6 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - README.md:154 → 挖矿相关 (1 处)<br>  - EVAL_PROTOCOL.md:15 → 挖矿相关 (3 处)<br>  - eval/router-corpus/blind-real.prompts.jsonl:68 → 代理/隧道 (1 处)<br>  - eval/router-corpus/v5/freeze-blind.mjs:129 → 挖矿相关 (1 处)<br>  - eval/router-corpus/v8/assemble-candidates.mjs:167 → 挖矿相关 (4 处)<br>  ... 共 44 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - SECURITY.md:11 → 敏感凭证读取 (2 处)<br>  - package.json:66 → 敏感凭证读取 (13 处)<br>  - CONTRIBUTING.md:39 → 敏感凭证读取 (1 处)<br>  - README.md:72 → 敏感凭证读取 (5 处)<br>  - EVAL_PROTOCOL.md:144 → 敏感凭证读取 (3 处)<br>  ... 共 387 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - eval/v0.4/tests/long-system-pilot.testcase.mjs:29 → 写入配置文件 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - eval/router-corpus/v4/supplement-raw.jsonl:14 → 动态加载原生模块 (5 处)<br>  - eval/router-corpus/v4/supplement-candidates.jsonl:14 → 动态加载原生模块 (5 处)<br>  - eval/router-corpus/v4/supplement-english.jsonl:9 → 动态加载原生模块 (5 处)<br>  - eval/router-corpus/v7/candidates.jsonl:156 → eval() 任意代码执行 (2 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 24 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - demo/crash-continuity-worker.mjs:29 → 定时任务 (2 处)<br>  - demo/crash-continuity-benchmark.mjs:63 → 定时任务 (2 处)<br>  - src/execution-state.ts:285 → 定时任务 (2 处)<br>  - src/execution-state.ts:353 → 进程控制 (1 处)<br>  - src/store.ts:91 → 定时任务 (3 处)<br>  ... 共 111 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - .github/workflows/freeze-eval-runtimes.yml:155 → 云存储上传 (2 处)<br>  - .github/workflows/attest-rc4-freezes.yml:83 → 云存储上传 (1 处)<br>  - .github/workflows/verify.yml:64 → 云存储上传 (4 处)<br>  - eval/v0.4/README.md:31 → 云存储上传 (1 处)<br>  - eval/v0.4/driver/harbor_plan_lattice_agent.py:41 → 云存储上传 (1 处)<br>  ... 共 50 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 24. repo: 0 deps + 24 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 112669, 注释行: 1072 (1.0%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 98 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - prospective/model-rc4-study/secure-run.sh:94 → 硬编码敏感信息 (3 处)<br>  - eval/grade.mjs:36 → 硬编码敏感信息 (4 处)<br>  - eval/long-system/v20/smoke.mjs:253 → 硬编码敏感信息 (1 处)<br>  - eval/long-system/v19/smoke.mjs:235 → 硬编码敏感信息 (1 处)<br>  - eval/long-system/v17/smoke.mjs:153 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (109 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (25 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - eval/router-corpus/v6/candidates.jsonl:32 → 要求 root/sudo 权限<br>  - eval/router-corpus/v7/candidates.jsonl:81 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - demo/crash-continuity-worker.mjs:1 → 修改系统目录 (1 处)<br>  - demo/first-drift-benchmark.mjs:1 → 修改系统目录 (1 处)<br>  - demo/crash-continuity-benchmark.mjs:1 → 修改系统目录 (1 处)<br>  - prospective/router-v14/workflow.mjs:1 → 修改系统目录 (1 处)<br>  - prospective/model-rc4-study/prepare-execution.mjs:1 → 修改系统目录 (1 处)<br>  ... 共 230 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: sandbox, isolation, workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (34 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 3 天; 提交总数: 177 |
| 7.2 | 未标记停止维护 | 必查 | ❌ 不通过 | 文档中发现弃用标记: archived |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 2, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-plan-lattice |
| 校验 URL | https://github.com/1052326311/dsh-plan-lattice |
| 必查项通过率 | 14/33 (42%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-23 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
