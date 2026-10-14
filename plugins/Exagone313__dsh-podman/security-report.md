# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/Exagone313/dsh-podman
- **校验时间**: 2026-10-14 04:02:53
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 16 | 10 | 7 |
| 🟡 推荐 | 14 | 6 | 8 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: master |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2015-04-06 (4208 天前); 公开仓库数: 85; 粉丝数: 34 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 140; 包名: @exagone313/dsh-podman; 描述: Podman-backed execution for DeepSeek Harness (dsh). — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ✅ 通过 | 未检测到明显的违法违规模式 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (15): 1.2.1, 1.2.0, 1.1.1, 1.1.0, 1.0.4; package.json version: 1.2.1; GitHub Releases (5): 1.2.1, 1.2.0, 1.1.1, 1.1.0, 1.0.4 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: 4.0.4; @deepseek-ai/dsh-client-locale: 0.2.0-rc.2; @deepseek-ai/dsh-client-shortcuts: 0.2.0-rc.2; @deepseek-ai/dsh-client-store: 0.2.0-rc.2; @deepseek-ai/dsh-client-ui-plugin-manager: 0.2.0-rc.2 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": ["@deepseek-ai/dsh-client-locale", ; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-client-locale, @deepseek-ai/dsh-client-shortcuts, @deepseek-ai/dsh-client-store, @deepseek-ai/dsh-client-ui-plugin-manager; Cordis 配置文件: cordis.patch.yml, defaults.cordis.patch.yml<br>  - src/approval.test.ts:20 → Monkey patch / prototype pollution<br>  - src/client/container-card-controller.ts:333 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 111 处, 函数: 1716 个, 比例: 6.5% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: src/subprocess.ts; 发现清理逻辑: src/terminal-sessions.ts; 发现清理逻辑: src/guest-rpc.ts |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - scripts/bump-version.mjs:18 → 读取环境变量配置 (1 处)<br>  - src/subprocess.ts:236 → 读取环境变量配置 (3 处)<br>  - src/secrets.test.ts:68 → 读取环境变量配置 (1 处)<br>  - src/guest-terminal.ts:151 → 读取环境变量配置 (1 处)<br>  - src/card-route.ts:311 → 读取环境变量配置 (7 处)<br>  ... 共 40 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - src/project-path.test.ts:72 → 深层目录穿越 (2 处)<br>  - src/misc.test.ts:97 → 深层目录穿越 (1 处)<br>  - src/fs-provider.test.ts:55 → 深层目录穿越 (1 处)<br>  - src/spill-store.test.ts:63 → 深层目录穿越 (2 处)<br>  - src/index.ts:139 → 读取用户主目录 (1 处)<br>  ... 共 7 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - scripts/generate-version.mjs:17 → 命令字符串拼接变量 (注入风险) (1 处) |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - README.zh.md:9 → 探测到 HTTP(S) 网络请求 (15 处)<br>  - dprint.json:31 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - Containerfile.dsh:14 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - README.md:9 → 探测到 HTTP(S) 网络请求 (15 处)<br>  - package.json:8 → 探测到 HTTP(S) 网络请求 (1 处)<br>涉及的域名: 127.0.0.1, deepseek.com, docs.podman.io, dsh.internal, dsh.test, github.com, img.shields.io, plugins.dprint.dev, podman.io, www.freedesktop.org (+1 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - LICENSES/Apache-2.0.txt:49 → 挖矿相关 (1 处)<br>  - third_party/json-canonicalization/LICENSE:53 → 挖矿相关 (1 处) |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - pnpm-lock.yaml:370 → 敏感凭证读取 (3 处)<br>  - go.mod:47 → 敏感凭证读取 (1 处)<br>  - SECURITY.md:32 → 敏感凭证读取 (9 处)<br>  - go.sum:73 → 敏感凭证读取 (2 处)<br>  - AGENTS.md:57 → 敏感凭证读取 (2 处)<br>  ... 共 118 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - internal/genproto/dshguest/v1/guest.pb.go:3280 → 连续十六进制转义 (混淆) (3 处)<br>  - internal/genproto/dshgateway/v1/gateway.pb.go:673 → 连续十六进制转义 (混淆) (3 处)<br>  - internal/genproto/dshctl/v1/control.pb.go:3966 → 连续十六进制转义 (混淆) (18 处) |
| 4.2 | 无 eval/vm/new Function | 必查 | ✅ 通过 | 未检测到危险 API 调用 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 29 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - scripts/bump-version.mjs:24 → 进程控制 (7 处)<br>  - src/subprocess.ts:114 → 定时任务 (1 处)<br>  - src/terminal-sessions.ts:95 → 定时任务 (1 处)<br>  - src/runtime-client.test.ts:20 → 临时文件操作 (1 处)<br>  - src/guest-rpc.ts:489 → 定时任务 (2 处)<br>  ... 共 38 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - .github/workflows/ci-code.yml:46 → 云存储上传 (2 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ⚠️  需人工复核 | 总依赖数: 28. repo: 6 deps + 22 devDeps — 依赖较多, 需人工审查 |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 24164, 注释行: 1852 (7.7%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 44 个, 例如: card-route.test.ts |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - src/daemons.test.ts:47 → 硬编码敏感信息 (3 处)<br>  - src/mounts.test.ts:34 → 硬编码敏感信息 (9 处)<br>  - src/guest-rpc.ts:318 → 明文写入敏感信息 (1 处)<br>  - src/secrets.test.ts:110 → 硬编码敏感信息 (8 处)<br>  - src/fs-provider.test.ts:93 → 硬编码敏感信息 (4 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ✅ 通过 | 未检测到明显的未授权读取模式 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (23 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (18 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - docs/install-dsh-and-dsh-podman.zh.md:54 → 要求 root/sudo 权限<br>  - docs/install-dsh-and-dsh-podman.md:67 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - Containerfile.orchestrator:10 → 修改系统目录 (1 处)<br>  - Containerfile.gateway:10 → 修改系统目录 (1 处)<br>  - Containerfile.guestagent:10 → 修改系统目录 (1 处)<br>  - quadlet/dsh-podman-gateway.container:17 → 修改系统目录 (2 处)<br>  - quadlet/dsh.container:32 → 修改系统目录 (5 处)<br>  ... 共 56 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (11 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 1 天; 提交总数: 754 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: CHANGELOG |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 6, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-podman |
| 校验 URL | https://github.com/Exagone313/dsh-podman |
| 必查项通过率 | 16/33 (48%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-14 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
