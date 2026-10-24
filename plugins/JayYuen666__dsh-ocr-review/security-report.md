# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/JayYuen666/dsh-ocr-review
- **校验时间**: 2026-10-24 03:48:50
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 18 | 11 | 4 |
| 🟡 推荐 | 14 | 6 | 8 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2019-08-01 (2640 天前); 公开仓库数: 13; 粉丝数: 5 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 6513; 包名: @jayyuen66/dsh-ocr-review; 描述: dsh 工作区代码审查插件：把 open-code-review（ocr CLI）封装为 5 个模型工具 + 设置卡片（从宿主设置服务的 provider 清单 — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (11): v0.1.7, v0.1.6, v0.1.5-rc, v0.1.5, v0.1.4-rc.1; package.json version: 0.1.7 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @jayyuen66/dsh-plugin-shared: catalog:; @deepseek-ai/dsh-atomic-write: 0.2.1-rc.2; @deepseek-ai/dsh-credentials: 0.2.1-rc.2; @deepseek-ai/dsh-home-paths: 0.2.1-rc.2; @deepseek-ai/dsh-typert-protocol: 0.2.1-rc.2 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"manifestVersion": 1, "bundle": {"patch": "./cordis.patch.yml"}, "client": {"platform": "web", "imm; Cordis/DSH 依赖: @jayyuen66/dsh-plugin-shared, @deepseek-ai/dsh-atomic-write, @deepseek-ai/dsh-credentials, @deepseek-ai/dsh-home-paths, @deepseek-ai/dsh-typert-protocol; Cordis 配置文件: cordis.patch.yml<br>  - lib/provider-projection.ts:48 → Monkey patch / prototype pollution<br>  - lib/severity.ts:57 → Monkey patch / prototype pollution<br>  - test/parse.test.ts:112 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 99 处, 函数: 1699 个, 比例: 5.8% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: host.ts; 发现清理逻辑: lib/messages.ts; 发现清理逻辑: test/client-card.test.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - host.ts:948 → 读取环境变量配置 (6 处)<br>  - README.zh-CN.md:143 → 读取环境变量配置 (7 处)<br>  - .npmrc:3 → 读取 npm 凭证 (2 处)<br>  - README.md:143 → 读取环境变量配置 (7 处)<br>  - lib/cli.ts:509 → 读取环境变量配置 (2 处)<br>  ... 共 15 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - host.ts:899 → 读取用户主目录 (3 处)<br>  - README.zh-CN.md:116 → 读取用户主目录 (1 处)<br>  - README.md:116 → 读取用户主目录 (1 处)<br>  - lib/cli.ts:575 → 读取用户主目录 (1 处)<br>  - lib/config-store.ts:100 → 读取用户主目录 (3 处)<br>  ... 共 13 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - .npmrc:5 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - icon.svg:1 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - THIRD_PARTY_NOTICES.md:19 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - package.json:15 → 探测到 HTTP(S) 网络请求 (4 处)<br>  - .github/workflows/publish.yml:23 → 探测到 HTTP(S) 网络请求 (3 处)<br>涉及的域名: alpha.example, api.xkiro.com, b, c, developer.amd.com.cn, example.inference, github.com, icones.js.org, junk, maas-api.antdigital.com (+8 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ✅ 通过 | 未检测到挖矿/远控/代理等恶意网络模式 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - host.ts:1585 → API Key / Token 读取 (6 处)<br>  - host.ts:19 → 敏感凭证读取 (42 处)<br>  - pnpm-lock.yaml:84 → 敏感凭证读取 (4 处)<br>  - pnpm-workspace.yaml:56 → 敏感凭证读取 (1 处)<br>  - README.zh-CN.md:11 → API Key / Token 读取 (7 处)<br>  ... 共 48 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - test/ocr-config.test.ts:673 → 写入配置文件 (19 处)<br>  - test/remote.test.ts:322 → 写入配置文件 (2 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - test/build-client.test.ts:248 → node:vm 任意代码执行 (1 处)<br>  - test/fixtures/delegate-rules.json:9 → eval() 任意代码执行 (1 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 45 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - host.ts:1932 → 临时文件操作 (1 处)<br>  - build-client.mjs:150 → 进程控制 (1 处)<br>  - lib/argv-guard.ts:159 → 临时文件操作 (1 处)<br>  - scripts/get-cred.mjs:95 → 进程控制 (3 处)<br>  - test/cli.test.ts:433 → 临时文件操作 (5 处)<br>  ... 共 9 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - pnpm-lock.yaml:66 → 云存储上传 (1 处)<br>  - pnpm-workspace.yaml:38 → 云存储上传 (1 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 45. repo: 2 deps + 43 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 20695, 注释行: 4470 (21.6%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 14 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ✅ 通过 | 检测到网络请求, 但 README 中有数据上传说明, 需确认 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - lib/output.ts:178 → 硬编码敏感信息 (1 处)<br>  - .github/workflows/publish.yml:69 → 硬编码敏感信息 (1 处)<br>  - test/ocr-config.test.ts:673 → 明文写入敏感信息 (10 处)<br>  - test/ocr-config.test.ts:480 → 硬编码敏感信息 (10 处)<br>  - test/get-cred.test.ts:65 → 明文写入敏感信息 (2 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - host.ts:2402 → 读取 git 历史 (2 处)<br>  - README.zh-CN.md:102 → 读取 git 历史 (1 处)<br>  - README.md:102 → 读取 git 历史 (1 处)<br>  - lib/cli.ts:685 → 读取 git 历史 (1 处)<br>  - lib/messages.ts:409 → 读取 git 历史 (11 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (3 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (3 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - build-client.mjs:1 → 修改系统目录 (1 处)<br>  - build-host.mjs:1 → 修改系统目录 (1 处)<br>  - lib/cli.ts:383 → 修改系统目录 (2 处)<br>  - scripts/get-cred.mjs:1 → 修改系统目录 (1 处)<br>  - test/cli.test.ts:328 → 修改系统目录 (2 处)<br>  ... 共 9 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (1 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 4 天; 提交总数: 12 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG, 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 0, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-ocr-review |
| 校验 URL | https://github.com/JayYuen666/dsh-ocr-review |
| 必查项通过率 | 18/33 (55%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-24 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
