# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/Fishsb/dsh-voice-prompt-enhancer
- **校验时间**: 2026-11-06 05:42:41
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 15 | 10 | 8 |
| 🟡 推荐 | 14 | 8 | 6 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2023-04-15 (1301 天前); 公开仓库数: 17; 粉丝数: 1 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: Apache-2.0 (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 183; 包名: dsh-voice-prompt-enhancer; 描述: DeepSeek Harness (DSH) plugin: prompt optimization (✨) + voice input enhancement — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (20): v3.5.1, v3.5.0, v3.4.2, v3.4.1, v3.4.0; package.json version: 3.5.1; GitHub Releases (5): v3.5.1, v3.5.0, v3.4.2, v3.4.1, v3.4.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/dsh-client-locale: >=0.1.0-rc.6; engines: {"dsh": ">=0.2.1-rc.1"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": ["@deepseek-ai/dsh-client-locale"],; Cordis/DSH 依赖: @deepseek-ai/dsh-client-locale; Cordis 配置文件: cordis.patch.yml<br>  - test/layout-geometry-lock.test.cjs:243 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 931 处, 函数: 5928 个, 比例: 15.7% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: plugin-host.js; 发现清理逻辑: lib/client.cjs; 发现清理逻辑: test/p0-stop-bleed.test.cjs |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - plugin-host.js:1314 → 读取 npm 凭证 (1 处)<br>  - plugin-host.js:1308 → 读取环境变量配置 (2 处)<br>  - plugin-host.js:1314 → 读取 .netrc 凭证 (1 处)<br>  - plugin-host.js:1314 → 读取 PyPI 凭证 (1 处)<br>  - plugin-host.js:1314 → 读取 SSH 私钥 (2 处)<br>  ... 共 53 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - lib/platform-service.cjs:294 → 读取用户主目录 (1 处)<br>  - lib/sys.cjs:535 → 目录遍历 (2 处)<br>  - test/rpc-registry-contract.test.cjs:89 → 目录遍历 (1 处)<br>  - test/maintain.test.cjs:326 → 目录遍历 (1 处)<br>  - test/test-inventory.test.cjs:74 → 目录遍历 (1 处)<br>  ... 共 48 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - LICENSE:4 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - package-lock.json:1054 → 探测到 HTTP(S) 网络请求 (95 处)<br>  - CHANGELOG.md:3 → 探测到 HTTP(S) 网络请求 (15 处)<br>  - package.json:54 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - README.md:7 → 探测到 HTTP(S) 网络请求 (8 处)<br>涉及的域名: 10.255.255.1, 127.0.0.1, api.github.com, evil.example, example.com, github.com, img.shields.io, keepachangelog.com, localhost, opencollective.com (+5 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - LICENSE:150 → 挖矿相关 (1 处)<br>  - lib/net-proxy.cjs:3 → 代理/隧道 (13 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - package-lock.json:156 → 敏感凭证读取 (3 处)<br>  - CHANGELOG.md:480 → API Key / Token 读取 (3 处)<br>  - CHANGELOG.md:432 → 会话历史读取 (1 处)<br>  - plugin-host.js:122 → 敏感凭证读取 (8 处)<br>  - plugin-host.js:814 → 会话历史读取 (4 处)<br>  ... 共 41 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - scripts/lib/mutation-ref-lock.mjs:28 → 字符混淆 (1 处) |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - CHANGELOG.md:22 → new Function() 任意代码执行 (17 处)<br>  - lib/index.cjs:39 → new Function() 任意代码执行 (2 处)<br>  - lib/client.cjs:546 → new Function() 任意代码执行 (1 处)<br>  - lib/harness.cjs:4 → new Function() 任意代码执行 (3 处)<br>  - test/p0-stop-bleed.test.cjs:9 → new Function() 任意代码执行 (2 处)<br>  ... 共 37 处 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 1 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - CHANGELOG.md:474 → 进程控制 (5 处)<br>  - CHANGELOG.md:183 → 临时文件操作 (35 处)<br>  - release-notes/3.4.2.md:3 → 进程控制 (2 处)<br>  - lib/platform-service.cjs:243 → 文件读取 (2 处)<br>  - lib/index.cjs:44 → 文件读取 (1 处)<br>  ... 共 196 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - CHANGELOG.md:538 → 云存储上传 (1 处)<br>  - scripts/release.mjs:145 → 云存储上传 (3 处)<br>  - .github/workflows/ci.yml:114 → 云存储上传 (2 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 无第三方依赖 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 58535, 注释行: 10398 (17.8%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - lib/client.cjs:1616 → 硬编码敏感信息 (2 处)<br>  - test/fixtures/ui-freeze/i18n.source.txt:308 → 硬编码敏感信息 (2 处)<br>  - src/client/common/i18n.cjs:312 → 硬编码敏感信息 (2 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - CHANGELOG.md:168 → 读取 git 历史 (27 处)<br>  - test/ui-freeze.test.cjs:15 → 读取文档/压缩文件 (1 处)<br>  - test/correction-misfire.test.cjs:146 → 读取文档/压缩文件 (1 处)<br>  - test/correction-step.test.cjs:360 → 读取文档/压缩文件 (4 处)<br>  - test/mutation-ref-lock.test.cjs:6 → 读取 git 历史 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (28 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (18 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - lib/platform-service.cjs:219 → 要求 root/sudo 权限<br>  - scripts/enhance-verify.mjs:146 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - CHANGELOG.md:504 → 创建开机自启/系统服务 (1 处)<br>  - lib/platform-service.cjs:15 → 创建开机自启/系统服务 (50 处)<br>  - lib/platform-service.cjs:295 → 创建系统启动项 (2 处)<br>  - lib/sys.cjs:281 → 创建开机自启/系统服务 (4 处)<br>  - lib/client.cjs:1710 → 创建开机自启/系统服务 (1 处)<br>  ... 共 27 处 |
| 6.3 | 支持沙箱运行 | 必查 | ⚠️  需人工复核 | 未在文档/配置中检测到沙箱支持声明, 需确认 |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (12 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 622 |
| 7.2 | 未标记停止维护 | 必查 | ❌ 不通过 | 文档中发现弃用标记: 不再维护, abandoned |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ✅ 通过 | Stars: 122, Forks: 14, Watchers: 0 — 高 Star 量 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-voice-prompt-enhancer |
| 校验 URL | https://github.com/Fishsb/dsh-voice-prompt-enhancer |
| 必查项通过率 | 15/33 (45%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-11-06 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
