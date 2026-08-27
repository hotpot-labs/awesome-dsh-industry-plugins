# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/SeaOf0/dsh-redteam-model
- **校验时间**: 2026-08-27 08:13:52
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 12 | 12 | 9 |
| 🟡 推荐 | 14 | 6 | 8 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2021-01-30 (2035 天前); 公开仓库数: 7; 粉丝数: 9 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 827; 包名: @dsh-external/dsh-redteam-model; 描述: DSH redteam security research modes and runtime plugins, managed from one settin — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - plugins/dsh-hunter/lib/adapters.js:239 → 欺诈行为 (1 处)<br>  - plugins/dsh-route-boost/lib/scope.mjs:24 → 欺诈行为 (1 处)<br>  - plugins/dsh-attack-atlas/test/run.mjs:49 → 欺诈行为 (2 处)<br>  - plugins/dsh-attack-atlas/lib/taxonomy.js:1149 → 破解授权 (1 处)<br>  - plugins/dsh-attack-atlas/lib/taxonomy.js:215 → 欺诈行为 (8 处)<br>  ... 共 255 处 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ⚠️  需人工复核 | 无 git tag; package.json version: 1.1.1; 有版本号但无 git tag / release |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/dsh-settings: ^0.1.0-rc.6 \|\| ^0.1.1-rc.0; engines: {"node": ">=22"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "inject": ["@deepseek-ai/d; Cordis/DSH 依赖: @deepseek-ai/dsh-settings; Cordis 配置文件: cordis.patch.yml, cordis.patch.yml<br>  - plugins/dsh-redteam-results/test/run.mjs:148 → Monkey patch / prototype pollution<br>  - plugins/dsh-redteam-results/lib/index.js:205 → Monkey patch / prototype pollution<br>  - plugins/dsh-campaign-memory/test/run.mjs:98 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 671 处, 函数: 4522 个, 比例: 14.8% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: plugins/dsh-product-subagents/test/run.mjs; 发现清理逻辑: plugins/dsh-product-subagents/lib/index.js; 发现清理逻辑: plugins/dsh-refusal-guard/lib/index.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - plugins/dsh-redteam-results/test/run.mjs:496 → 读取环境变量配置 (2 处)<br>  - plugins/dsh-redteam-results/lib/index.js:41 → 读取环境变量配置 (1 处)<br>  - plugins/dsh-product-subagents/README.md:32 → 读取环境变量配置 (1 处)<br>  - plugins/dsh-product-subagents/test/run.mjs:148 → 读取环境变量配置 (2 处)<br>  - plugins/dsh-product-subagents/lib/index.js:172 → 读取环境变量配置 (2 处)<br>  ... 共 230 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - plugins/dsh-redteam-results/lib/index.js:41 → 读取用户主目录 (2 处)<br>  - plugins/dsh-campaign-memory/lib/index.js:29 → 读取用户主目录 (1 处)<br>  - plugins/dsh-hunter/lib/index.js:27 → 读取用户主目录 (2 处)<br>  - plugins/dsh-route-boost/README.md:55 → 深层目录穿越 (2 处)<br>  - plugins/dsh-route-boost/test/run.mjs:8 → 深层目录穿越 (3 处)<br>  ... 共 135 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - deploy/assets/kali-mcp-server/status_check.py:70 → Python subprocess (3 处)<br>  - deploy/assets/kali-mcp-server/kali_mcp/agents/specialized/code_analyze_agent.py:61 → os.system 命令执行 (1 处)<br>  - deploy/assets/kali-mcp-server/kali_mcp/agents/specialized/code_audit_agent.py:47 → os.system 命令执行 (1 处)<br>  - deploy/assets/kali-mcp-server/kali_mcp/diggers/command_injection_digger.py:572 → Python subprocess (1 处)<br>  - deploy/assets/kali-mcp-server/kali_mcp/diggers/base_digger.py:78 → Python subprocess (1 处)<br>  ... 共 104 处<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - plugins/dsh-redteam-results/lib/store.js:124 → 命令字符串拼接变量 (注入风险) (1 处)<br>  - plugins/dsh-route-boost/lib/skilltools.mjs:50 → 命令字符串拼接变量 (注入风险) (1 处)<br>  - deploy/deploy.mjs:61 → 开启 shell 模式 (注入风险) (2 处)<br>  - modes/pentest/refs/web/prototype-pollution.md:128 → 命令字符串拼接变量 (注入风险) (1 处)<br>  - modes/pentest/refs/web/cmdi-command-injection.md:81 → exec 命令拼接 (1 处)<br>  ... 共 23 处 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package.json:27 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - package-lock.json:32 → 探测到 HTTP(S) 网络请求 (238 处)<br>  - README.md:3 → 探测到 HTTP(S) 网络请求 (13 处)<br>  - plugins/dsh-redteam-results/package.json:28 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - plugins/dsh-redteam-results/test/run.mjs:17 → 探测到 HTTP(S) 网络请求 (14 处)<br>涉及的域名: ..., 0, 0.0.0.0, 0177.0.0.1, 0177.0x0.0.1, 017700000001, 0249.0376.0251.0376, 0251.0376.0251.0376, 0x7f.0.0.1, 0x7f.0x0.0x0.0x1 (+1151 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - plugins/dsh-webshell-mgr/README.md:145 → 代理/隧道 (1 处)<br>  - plugins/dsh-webshell-mgr/assets/payloads-java/WsmSocks.class:48 → 代理/隧道 (1 处)<br>  - plugins/dsh-webshell-mgr/assets/payloads-java/WsmReverse.class:40 → 远控/反向 shell (3 处)<br>  - plugins/dsh-webshell-mgr/payload-src/java/WsmReverse.java:13 → 远控/反向 shell (2 处)<br>  - plugins/dsh-webshell-mgr/payload-src/java/WsmSocks.java:1 → 代理/隧道 (2 处)<br>  ... 共 174 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - AGENTS.md:15 → 敏感凭证读取 (2 处)<br>  - plugins/dsh-redteam-results/test/run.mjs:496 → 读取环境变量 API Key/凭证 (2 处)<br>  - plugins/dsh-redteam-results/lib/index.js:41 → 读取环境变量 API Key/凭证 (1 处)<br>  - plugins/dsh-campaign-memory/package.json:4 → 敏感凭证读取 (1 处)<br>  - plugins/dsh-campaign-memory/test/run.mjs:19 → 敏感凭证读取 (1 处)<br>  ... 共 1103 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - tests/manager.test.mjs:127 → 写入配置文件 (3 处)<br>  - modes/pentest/refs/web/web-auth-bypass.md:366 → 修改全局配置 (1 处)<br>  - modes/pentest/refs/web/web-auth-bypass.md:366 → 修改配置 (1 处)<br>  - modes/code-audit/refs/lang/code-audit-python.md:1534 → 修改全局配置 (1 处)<br>  - modes/code-audit/refs/lang/code-audit-python.md:1534 → 修改配置 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - plugins/dsh-webshell-mgr/test/run.mjs:458 → 连续十六进制转义 (混淆) (1 处)<br>  - plugins/dsh-webshell-mgr/lib/protocol/payloads-java.js:6 → 超长 base64 字符串 (14 处)<br>  - plugins/dsh-webshell-mgr/lib/protocol/payloads-aspx.js:5 → 超长 base64 字符串 (2 处)<br>  - deploy/assets/kali-mcp-server/kali_mcp/diggers/file_upload_digger.py:88 → 连续十六进制转义 (混淆) (3 处)<br>  - deploy/assets/kali-mcp-server/kali_mcp/diggers/xss_digger.py:40 → 字符混淆 (2 处)<br>  ... 共 65 处 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - plugins/dsh-webshell-mgr/README.md:164 → eval() 任意代码执行 (1 处)<br>  - plugins/dsh-webshell-mgr/lib/plugins-registry.js:110 → eval() 任意代码执行 (1 处)<br>  - plugins/dsh-webshell-mgr/lib/generators.js:40 → eval() 任意代码执行 (4 处)<br>  - plugins/dsh-webshell-mgr/lib/protocol/cmd.js:5 → eval() 任意代码执行 (1 处)<br>  - plugins/dsh-webshell-mgr/lib/protocol/behinder.js:2 → eval() 任意代码执行 (3 处)<br>  ... 共 138 处 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 10 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - plugins/dsh-redteam-results/test/run.mjs:492 → 临时文件操作 (1 处)<br>  - plugins/dsh-redteam-results/lib/client.js:183 → 定时任务 (5 处)<br>  - plugins/dsh-campaign-memory/test/run.mjs:251 → 进程控制 (1 处)<br>  - plugins/dsh-campaign-memory/test/run.mjs:137 → 临时文件操作 (1 处)<br>  - plugins/dsh-campaign-memory/lib/client.js:129 → 定时任务 (1 处)<br>  ... 共 290 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - plugins/dsh-webshell-mgr/lib/client.js:753 → 云存储上传 (2 处)<br>  - plugins/dsh-webshell-mgr/lib/protocol/capabilities.js:25 → 云存储上传 (3 处)<br>  - plugins/dsh-attack-atlas/test/run.mjs:47 → 云存储上传 (10 处)<br>  - plugins/dsh-attack-atlas/lib/taxonomy.js:158 → 云存储上传 (5 处)<br>  - plugins/dsh-attack-atlas/lib/index.js:245 → 云存储上传 (1 处)<br>  ... 共 256 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 10. repo: 0 deps + 10 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 121695, 注释行: 6829 (5.6%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 21 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - plugins/dsh-webshell-mgr/test/run.mjs:146 → 硬编码敏感信息 (16 处)<br>  - plugins/dsh-webshell-mgr/lib/protocol/behinder-java.js:69 → 硬编码敏感信息 (1 处)<br>  - plugins/dsh-webshell-mgr/lib/protocol/behinder-aspx.js:54 → 硬编码敏感信息 (1 处)<br>  - plugins/dsh-webshell-mgr/lib/protocol/godzilla-java.js:127 → 硬编码敏感信息 (1 处)<br>  - plugins/dsh-webshell-mgr/lib/protocol/godzilla-aspx.js:93 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - plugins/dsh-sec-enforce/test/run.mjs:143 → 读取文档/压缩文件 (1 处)<br>  - plugins/dsh-sec-enforce/lib/index.js:181 → 读取文档/压缩文件 (1 处)<br>  - plugins/dsh-route-boost/test/run.mjs:157 → 读取文档/压缩文件 (1 处)<br>  - plugins/dsh-route-boost/lib/skilltools.mjs:28 → 读取文档/压缩文件 (1 处)<br>  - plugins/dsh-semgrep-audit/test/run.mjs:52 → 读取文档/压缩文件 (2 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (416 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (73 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - deploy/assets/kali-mcp-server/status_check.py:247 → 要求 root/sudo 权限<br>  - deploy/assets/kali-mcp-server/kali_mcp/agents/exploitation/privilege_agent.py:231 → 要求 root/sudo 权限<br>  - deploy/assets/kali-mcp-server/kali_mcp/diggers/privilege_escalation_digger.py:498 → 要求 root/sudo 权限<br>  - deploy/assets/kali-mcp-server/kali_mcp/vulnerabilities/nday_vulns.py:529 → 要求 root/sudo 权限<br>  - deploy/assets/kali-mcp-server/kali_mcp/core/deep_attack_engine.py:156 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - plugins/dsh-sec-enforce/test/run.mjs:43 → 修改系统目录 (6 处)<br>  - plugins/dsh-sec-enforce/test/run.mjs:54 → 创建开机自启/系统服务 (6 处)<br>  - plugins/dsh-sec-enforce/lib/index.js:94 → 创建开机自启/系统服务 (2 处)<br>  - plugins/dsh-webshell-mgr/mcp/server.mjs:1 → 修改系统目录 (1 处)<br>  - plugins/dsh-webshell-mgr/lib/client.js:452 → 修改系统目录 (1 处)<br>  ... 共 497 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: 隔离 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (41 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 57 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ⚠️  需人工复核 | 发现 1 个公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 79, Forks: 18, Watchers: 0 — 有一定社区基础 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-redteam-model |
| 校验 URL | https://github.com/SeaOf0/dsh-redteam-model |
| 必查项通过率 | 12/33 (36%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-27 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
