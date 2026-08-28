# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/cuddly-guacamole/dsh-auto-approval-llm
- **校验时间**: 2026-08-28 10:22:02
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 18 | 10 | 5 |
| 🟡 推荐 | 14 | 7 | 7 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2019-12-06 (2457 天前); 公开仓库数: 15; 粉丝数: 4 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: BSD-3-Clause (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1222; 包名: @quill507/dsh-auto-approval-llm; 描述: LLM-assisted auto approval with timeout fallback for DeepSeek Harness — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - src/auto/decision.ts:512 → 窃取数据 (1 处)<br>  - docs/06-llm-reviewer.md:48 → 窃取数据 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (10): v0.0.10, v0.0.9, v0.0.8, v0.0.7, v0.0.6; package.json version: 0.0.10; GitHub Releases (5): v0.0.10, v0.0.9, v0.0.8, v0.0.7, v0.0.6 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: >=4.0.0-rc <5; @deepseek-ai/dsh-llm: >=0.1.0-rc.0 <2; @deepseek-ai/dsh-tools: >=0.1.0-rc.0 <2 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "inject": ["@deepseek-ai/d; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-llm, @deepseek-ai/dsh-tools; Cordis 配置文件: cordis.patch.yml<br>  - src/client/auto-icon.ts:28 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 200 处, 函数: 1542 个, 比例: 13.0% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: tests/editdiff.test.mjs; 发现清理逻辑: tests/category.test.mjs; 发现清理逻辑: tests/contract.test.mjs |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - README.en.md:193 → 读取环境变量配置 (1 处)<br>  - README.md:198 → 读取环境变量配置 (1 处)<br>  - tsdown.config.ts:25 → 读取环境变量配置 (2 处)<br>  - src/index.ts:247 → 读取环境变量配置 (6 处)<br>  - src/client/index.ts:1004 → 读取浏览器 Cookie/本地存储 (2 处)<br>  ... 共 57 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - src/index.ts:246 → 读取用户主目录 (4 处)<br>  - src/auto/paths.ts:72 → 读取用户主目录 (4 处) — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - README.en.md:201 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - package.json:11 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - package-lock.json:30 → 探测到 HTTP(S) 网络请求 (445 处)<br>  - README.md:11 → 探测到 HTTP(S) 网络请求 (4 处)<br>  - src/index.ts:1554 → 探测到 HTTP(S) 网络请求 (3 处)<br>涉及的域名: 127.0.0.1, 192.168.1.10, 9.9.9.9, api.example.com, corp, cuddly-guacamole.github.io, ev, evil, evil.com, evil.example (+14 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - README.en.md:11 → 敏感凭证读取 (9 处)<br>  - tsdown.config.ts:25 → 读取环境变量 API Key/凭证 (2 处)<br>  - src/index.ts:247 → 读取环境变量 API Key/凭证 (6 处)<br>  - src/index.ts:397 → API Key / Token 读取 (27 处)<br>  - src/index.ts:106 → 敏感凭证读取 (69 处)<br>  ... 共 36 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 12 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - src/index.ts:1629 → 定时任务 (3 处)<br>  - src/client/index.ts:93 → 定时任务 (6 处)<br>  - src/auto/decision.ts:115 → 定时任务 (1 处)<br>  - src/auto/paths.ts:65 → 临时文件操作 (1 处)<br>  - src/auto/retry.ts:111 → 定时任务 (1 处)<br>  ... 共 18 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - src/auto/category.ts:231 → 云存储上传 (1 处)<br>  - src/auto/policy.ts:123 → 云存储上传 (1 处)<br>  - src/auto/risk-tokens.ts:12 → 云存储上传 (1 处)<br>  - tests/category.test.mjs:76 → 云存储上传 (1 处)<br>  - .github/workflows/deploy-docs.yml:28 → 云存储上传 (1 处)<br>  ... 共 6 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 8. repo: 0 deps + 8 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 18418, 注释行: 2625 (14.3%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - tests/editdiff.test.mjs:294 → 明文写入敏感信息 (4 处)<br>  - tests/contract.test.mjs:1952 → 硬编码敏感信息 (3 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - tests/category.test.mjs:124 → 读取 git 历史 (3 处)<br>  - tests/contract-devloop.test.mjs:239 → 读取 git 历史 (3 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (9 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (12 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - src/auto/shell.ts:402 → 要求 root/sudo 权限<br>  - tests/category.test.mjs:169 → 要求 root/sudo 权限<br>  - tests/contract.test.mjs:815 → 要求 root/sudo 权限<br>  - tests/contract-devloop.test.mjs:62 → 要求 root/sudo 权限<br>  - docs/03-static-engine.md:66 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - src/index.ts:385 → 修改系统目录 (1 处)<br>  - src/auto/paths.ts:132 → 修改系统目录 (1 处)<br>  - src/auto/category.ts:320 → 创建开机自启/系统服务 (2 处)<br>  - src/auto/shell.ts:1089 → 创建开机自启/系统服务 (2 处)<br>  - tests/category.test.mjs:167 → 创建开机自启/系统服务 (1 处)<br>  ... 共 6 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: sandbox, 隔离, workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (2 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 1 天; 提交总数: 92 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 3, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-auto-approval-llm |
| 校验 URL | https://github.com/cuddly-guacamole/dsh-auto-approval-llm |
| 必查项通过率 | 18/33 (55%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-28 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
