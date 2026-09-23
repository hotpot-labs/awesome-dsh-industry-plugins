# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/hoyyang/dsh-best-ponytail
- **校验时间**: 2026-09-23 03:55:12
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 13 | 13 | 7 |
| 🟡 推荐 | 14 | 8 | 6 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2019-08-27 (2583 天前); 公开仓库数: 16; 粉丝数: 0 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 714; 包名: dsh-best-ponytail; 描述: ponytail as a DeepSeek Harness plugin: the laziest-senior-dev ruleset — 6 skills — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - upstream/benchmarks/agentic/tasks.py:927 → 非法爬取 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (1): v0.1.0; package.json version: 0.1.0; GitHub Releases (1): v0.1.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ❌ 不通过 | 未在 package.json 中发现 DSH/Cordis 依赖或 engines 字段 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ✅ 通过 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}}; Cordis 配置文件: cordis.patch.yml |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 84 处, 函数: 410 个, 比例: 20.5% |
| 2.4 | 卸载后完整释放资源 | 必查 | ⚠️  需人工复核 | 使用了定时器但未发现清理逻辑, 需人工确认 |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - upstream/.gitignore:2 → 读取环境变量配置 (3 处)<br>  - upstream/.env.example:1 → 读取环境变量配置 (1 处)<br>  - upstream/__init__.py:45 → 读取环境变量配置 (4 处)<br>  - upstream/benchmarks/model-email.js:6 → 读取环境变量配置 (3 处)<br>  - upstream/benchmarks/promptfooconfig.gemini.yaml:2 → 读取环境变量配置 (2 处)<br>  ... 共 32 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - upstream/benchmarks/agentic/judge.py:13 → 深层目录穿越 (1 处)<br>  - upstream/benchmarks/agentic/complete.py:20 → 深层目录穿越 (1 处)<br>  - upstream/benchmarks/agentic/README.md:52 → 深层目录穿越 (1 处)<br>  - upstream/benchmarks/agentic/tasks.py:68 → 深层目录穿越 (1 处)<br>  - upstream/benchmarks/results/2026-06-18-agentic.md:141 → 深层目录穿越 (1 处)<br>  ... 共 13 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - upstream/benchmarks/correctness.js:9 → 加载 child_process (1 处)<br>  - upstream/benchmarks/robustness-audit.js:6 → 加载 child_process (1 处)<br>  - upstream/benchmarks/agentic/run.py:152 → Python subprocess (6 处)<br>  - upstream/benchmarks/agentic/tasks.py:543 → Python subprocess (1 处)<br>  - upstream/scripts/publish-openclaw-skills.js:21 → 加载 child_process (1 处)<br>  ... 共 10 处<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - upstream/benchmarks/correctness.js:55 → 命令字符串拼接变量 (注入风险) (4 处)<br>  - upstream/benchmarks/robustness-audit.js:16 → 命令字符串拼接变量 (注入风险) (2 处)<br>  - upstream/scripts/publish-openclaw-skills.js:64 → 开启 shell 模式 (注入风险) (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - LICENSE:4 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - README.md:5 → 探测到 HTTP(S) 网络请求 (8 处)<br>  - README.en.md:5 → 探测到 HTTP(S) 网络请求 (8 处)<br>  - package.json:10 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - upstream/README.es.md:15 → 探测到 HTTP(S) 网络请求 (26 处)<br>涉及的域名: 127.0.0.1, a.b, anthropic.com, api.anthropic.com, api.openai.com, api.star-history.com, example.com, github.com, greenpt.com, img.shields.io (+9 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - README.en.md:155 → 敏感凭证读取 (1 处)<br>  - upstream/.gitignore:1 → 敏感凭证读取 (1 处)<br>  - upstream/.env.example:2 → API Key / Token 读取 (1 处)<br>  - upstream/benchmarks/model-email.js:6 → 读取环境变量 API Key/凭证 (2 处)<br>  - upstream/benchmarks/model-email.js:12 → API Key / Token 读取 (1 处)<br>  ... 共 36 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - upstream/pi-extension/test/extension.test.js:215 → 写入配置文件 (1 处)<br>  - upstream/pi-extension/test/helpers.test.js:89 → 写入配置文件 (1 处)<br>  - upstream/hooks/ponytail-config.js:149 → 写入配置文件 (1 处)<br>  - upstream/hooks/ponytail-config.js:149 → 写入 DSH 配置 (1 处)<br>  - upstream/scripts/uninstall.js:60 → 写入配置文件 (2 处)<br>  ... 共 14 处 — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - upstream/benchmarks/correctness.js:86 → eval() 任意代码执行 (2 处)<br>  - upstream/benchmarks/correctness.js:9 → 加载 child_process 模块 (1 处)<br>  - upstream/benchmarks/robustness-audit.js:134 → eval() 任意代码执行 (2 处)<br>  - upstream/benchmarks/robustness-audit.js:6 → 加载 child_process 模块 (1 处)<br>  - upstream/scripts/publish-openclaw-skills.js:21 → 加载 child_process 模块 (1 处)<br>  ... 共 10 处 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 1 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - upstream/examples/debounce.md:20 → 定时任务 (3 处)<br>  - upstream/examples/react-countdown.md:26 → 定时任务 (5 处)<br>  - upstream/benchmarks/model-email.js:4 → 文件读取 (2 处)<br>  - upstream/benchmarks/correctness.js:162 → 定时任务 (1 处)<br>  - upstream/benchmarks/correctness.js:67 → 文件写入 (1 处)<br>  ... 共 68 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - upstream/benchmarks/agentic/judge.py:111 → 云存储上传 (1 处)<br>  - upstream/benchmarks/agentic/complete.py:74 → 云存储上传 (1 处)<br>  - upstream/benchmarks/agentic/README.md:52 → 云存储上传 (1 处)<br>  - upstream/benchmarks/agentic/tasks.py:71 → 云存储上传 (14 处)<br>  - upstream/scripts/publish-openclaw-skills.js:16 → 云存储上传 (1 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 1. repo: 0 deps + 1 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 7323, 注释行: 774 (10.6%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 25 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - upstream/benchmarks/agentic/judge.py:44 → 硬编码敏感信息 (1 处)<br>  - upstream/benchmarks/agentic/tasks.py:220 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - upstream/README.es.md:66 → 读取 git 历史 (1 处)<br>  - upstream/README.ko.md:66 → 读取 git 历史 (1 处)<br>  - upstream/README.md:77 → 读取 git 历史 (1 处)<br>  - upstream/benchmarks/model-email.js:4 → 读取文档/压缩文件 (1 处)<br>  - upstream/benchmarks/robustness-audit.js:32 → 读取文档/压缩文件 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (19 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (6 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - upstream/benchmarks/agentic/judge.py:1 → 修改系统目录 (1 处)<br>  - upstream/benchmarks/agentic/run.py:1 → 修改系统目录 (1 处)<br>  - upstream/benchmarks/agentic/complete.py:1 → 修改系统目录 (1 处)<br>  - upstream/benchmarks/agentic/README.md:52 → 修改系统目录 (1 处)<br>  - upstream/benchmarks/agentic/tasks.py:68 → 修改系统目录 (1 处)<br>  ... 共 35 处 |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (8 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 2 天; 提交总数: 8 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-best-ponytail |
| 校验 URL | https://github.com/hoyyang/dsh-best-ponytail |
| 必查项通过率 | 13/33 (39%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-09-23 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
