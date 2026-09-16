# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/NanmiCoder/dsh-auto-mode
- **校验时间**: 2026-09-16 03:57:43
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 15 | 12 | 6 |
| 🟡 推荐 | 14 | 7 | 7 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2019-01-30 (2785 天前); 公开仓库数: 49; 粉丝数: 2852 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1600; 包名: @nanmicoder/dsh-auto-mode; 描述: Sandbox-first automatic permission policy for DeepSeek Harness — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - skills/plugin-upgrade/references/v0.1.2-alpha.1.md:218 → 绕过权限限制 (1 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (8): v0.1.9, v0.1.8, v0.1.7, v0.1.6, v0.1.5; package.json version: 0.1.9; GitHub Releases (2): v0.1.9, v0.1.7 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: ^4.0.2; @deepseek-ai/dsh-client-locale: 0.1.5-rc.1 \|\| 0.1.2-rc.1 \|\| 0.1.2-alpha.5 \|\| 0.1.2-alpha.3 \|\| 0.1.2-alpha.2; @deepseek-ai/dsh-llm: 0.1.5-rc.1 \|\| 0.1.2-rc.1 \|\| 0.1.2-alpha.5 \|\| 0.1.2-alpha.3 \|\| 0.1.2-alpha.2; @deepseek-ai/dsh-permission-presets: 0.1.5-rc.1 \|\| 0.1.2-rc.1 \|\| 0.1.2-alpha.5 \|\| 0.1.2-alpha.3 \|\| 0.1.2-alpha.2; @deepseek-ai/dsh-tools: 0.1.5-rc.1 \|\| 0.1.2-rc.1 \|\| 0.1.2-alpha.5 \|\| 0.1.2-alpha.3 \|\| 0.1.2-alpha.2 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": [], "platform": "web"}}; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-client-locale, @deepseek-ai/dsh-llm, @deepseek-ai/dsh-permission-presets, @deepseek-ai/dsh-tools; Cordis 配置文件: cordis.patch.yml<br>  - skills/plugin-upgrade/references/pre-flight-patterns.json:8 → Monkey patch / prototype pollution<br>  - skills/plugin-upgrade/references/pre-flight.md:17 → Monkey patch / prototype pollution<br>  - skills/plugin-upgrade/references/v0.1.3-alpha.2.md:144 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 123 处, 函数: 1294 个, 比例: 9.5% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: tests/security-boundary.spec.ts; 发现清理逻辑: tests/recovery.spec.ts; 发现清理逻辑: tests/client-locale.spec.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - skills/plugin-test/scripts/container-runner.mjs:68 → 读取环境变量配置 (12 处)<br>  - skills/plugin-test/scripts/docker-release-smoke.mjs:266 → 读取环境变量配置 (2 处)<br>  - skills/plugin-upgrade/SKILL.zh-CN.md:44 → 读取 npm 凭证 (1 处)<br>  - skills/plugin-upgrade/SKILL.zh-CN.md:144 → 读取环境变量配置 (1 处)<br>  - skills/plugin-upgrade/SKILL.md:55 → 读取 npm 凭证 (1 处)<br>  ... 共 44 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - skills/dsh-benchmark-case/assets/test.sh.example:9 → 访问绝对路径/上级目录 (2 处)<br>  - skills/plugin-upgrade/examples/06-real-world-batch-migration.md:212 → 深层目录穿越 (1 处)<br>  - skills/plugin-upgrade/examples/06-real-world-batch-migration.en.md:212 → 深层目录穿越 (1 处)<br>  - skills/plugin-upgrade/examples/legacy-plugin/README.en.md:5 → 深层目录穿越 (2 处)<br>  - skills/plugin-upgrade/examples/legacy-plugin/README.md:6 → 深层目录穿越 (2 处)<br>  ... 共 12 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - skills/dsh-benchmark-case/assets/judge-utils.mjs:106 → 命令字符串拼接变量 (注入风险) (6 处)<br>  - tests/patch.spec.ts:24 → exec 命令拼接 (1 处)<br>  - src/patch.ts:38 → exec 命令拼接 (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - pnpm-lock.yaml:458 → WebSocket 连接 (3 处)<br>  - pnpm-lock.yaml:458 → 浏览器网络 API (3 处)<br>  - package.json:16 → 探测到 HTTP(S) 网络请求 (4 处)<br>  - README_ZH.md:10 → 探测到 HTTP(S) 网络请求 (5 处)<br>  - RELEASE_NOTES.md:23 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: 127.0.0.1, api.github.com, classifier.invalid, example.invalid, github.com, img.shields.io, json-schema.org, localhost, nodejs.org, raw.githubusercontent.com (+5 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - skills/plugin-upgrade/references/v0.1.2-rc.1.md:96 → 挖矿相关 (1 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - VALIDATION.md:42 → 敏感凭证读取 (1 处)<br>  - pnpm-lock.yaml:99 → 敏感凭证读取 (67 处)<br>  - package.json:240 → 敏感凭证读取 (4 处)<br>  - RELEASE_NOTES.md:19 → 敏感凭证读取 (2 处)<br>  - README.md:85 → 敏感凭证读取 (2 处)<br>  ... 共 82 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - skills/plugin-test/scripts/docker-release-smoke.mjs:362 → 写入配置文件 (1 处)<br>  - tests/loader-composition.spec.ts:29 → 写入配置文件 (1 处)<br>  - scripts/harness-runtime-verify.mjs:34 → 写入配置文件 (1 处)<br>  - scripts/release-metadata.test.mjs:18 → 写入配置文件 (1 处) — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 33 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - release-candidate.json:10 → 临时文件操作 (1 处)<br>  - VALIDATION.md:3 → 临时文件操作 (3 处)<br>  - AGENTS.md:7 → 临时文件操作 (1 处)<br>  - DESIGN.md:37 → 临时文件操作 (1 处)<br>  - skills/README.md:24 → 临时文件操作 (2 处)<br>  ... 共 58 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - pnpm-lock.yaml:410 → 云服务 SDK (可能用于隐蔽上传) (100 处)<br>  - pnpm-lock.yaml:36 → 云存储上传 (6 处)<br>  - package.json:177 → 云存储上传 (2 处)<br>  - skills/plugin-upgrade/references/v0.1.2-rc.1.md:128 → 云存储上传 (1 处)<br>  - skills/plugin-upgrade/references/v0.1.3-alpha.1.md:256 → 云存储上传 (1 处)<br>  ... 共 12 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 33. repo: 1 deps + 32 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 13580, 注释行: 628 (4.6%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 20 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - skills/plugin-test/scripts/docker-release-smoke.test.mjs:45 → 硬编码敏感信息 (1 处)<br>  - skills/plugin-upgrade/scripts/verify-runtime.mjs:348 → 明文写入敏感信息 (1 处)<br>  - skills/plugin-upgrade/scripts/verify-runtime.mjs:262 → 硬编码敏感信息 (1 处)<br>  - tests/security-boundary.spec.ts:13 → 硬编码敏感信息 (1 处)<br>  - tests/classifier.spec.ts:61 → 硬编码敏感信息 (2 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - README_ZH.md:144 → 读取 git 历史 (1 处)<br>  - README.md:144 → 读取 git 历史 (1 处)<br>  - skills/dsh-plugin-development/SKILL.md:63 → 读取 git 历史 (2 处)<br>  - skills/plugin-upgrade/examples/07-multi-repo-batch-migration.md:71 → 读取 git 历史 (4 处)<br>  - skills/plugin-upgrade/examples/07-multi-repo-batch-migration.en.md:57 → 读取 git 历史 (4 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (37 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (9 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ✅ 通过 | 未检测到需要 root/sudo 的代码 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - skills/plugin-test/scripts/container-runner.mjs:1 → 修改系统目录 (1 处)<br>  - skills/plugin-test/scripts/docker-release-smoke.mjs:1 → 修改系统目录 (1 处)<br>  - skills/dsh-benchmark-case/references/host-archaeology.md:108 → 修改系统目录 (1 处)<br>  - skills/plugin-upgrade/references/v0.1.2-rc.1.md:83 → 创建开机自启/系统服务 (1 处)<br>  - skills/plugin-upgrade/references/rollup-0.1.2.md:207 → 创建开机自启/系统服务 (1 处)<br>  ... 共 21 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: sandbox, workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (13 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 2 天; 提交总数: 34 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG, 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ✅ 通过 | Stars: 156, Forks: 4, Watchers: 0 — 高 Star 量 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-auto-mode |
| 校验 URL | https://github.com/NanmiCoder/dsh-auto-mode |
| 必查项通过率 | 15/33 (45%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-09-16 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
