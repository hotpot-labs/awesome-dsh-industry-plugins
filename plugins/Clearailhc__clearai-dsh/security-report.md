# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/Clearailhc/clearai-dsh
- **校验时间**: 2026-10-09 05:11:53
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
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2017-07-18 (3369 天前); 公开仓库数: 26; 粉丝数: 42 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: Apache-2.0 (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 2710; 包名: clearai-dsh; 描述: ClearAI: an ontology-first DSH agent preset — evidence-checked research that gro — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - docs/research-openrsi.md:50 → 非法爬取 (2 处) |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (20): v0.5.1, v0.5.0, v0.4.0, v0.3.1, v0.3.0; package.json version: 0.5.1; GitHub Releases (5): v0.5.1, v0.5.0, v0.4.0, v0.3.1, v0.3.0 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | engines: {"node": ">=22", "dsh": ">=0.2.0-rc.2"} |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": ["./cordis.patch.yml", "./presets/clearai/clearai.patch.yml"]}, "client": {"pla; Cordis 配置文件: cordis.patch.yml<br>  - docs/marketing/zhihu/clearai-dsh-知乎稿.md:264 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ⚠️  需人工复核 | try/catch: 270 处, 函数: 3539 个, 比例: 7.6% — try/catch 覆盖比例较低 |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: preset/plugins/clearai-kernel.js |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - brand/build-icons.mjs:28 → 读取环境变量配置 (1 处)<br>  - brand/build-social-preview.mjs:39 → 读取环境变量配置 (1 处)<br>  - pack/bin/clearai.mjs:31 → 读取环境变量配置 (8 处)<br>  - tools/install-native.mjs:36 → 读取环境变量配置 (3 处)<br>  - tools/e2e-run.mjs:38 → 读取环境变量配置 (6 处)<br>  ... 共 25 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - pack/bin/clearai.mjs:31 → 读取用户主目录 (1 处)<br>  - tools/install-native.mjs:36 → 读取用户主目录 (1 处)<br>  - tools/e2e-run.mjs:38 → 读取用户主目录 (3 处)<br>  - tools/panel-preview.mjs:27 → 读取用户主目录 (1 处)<br>  - tools/verify-lifecycle.mjs:45 → 读取用户主目录 (1 处)<br>  ... 共 20 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ✅ 通过 | 未检测到命令执行调用 |
| 3.4 | 无命令注入风险 | 必查 | ✅ 通过 | 未检测到命令注入模式 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - package-lock.json:31 → 探测到 HTTP(S) 网络请求 (81 处)<br>  - CHANGELOG.md:3 → 探测到 HTTP(S) 网络请求 (5 处)<br>  - LICENSE:3 → 探测到 HTTP(S) 网络请求 (2 处)<br>  - README.zh-CN.md:11 → 探测到 HTTP(S) 网络请求 (7 处)<br>  - README.md:11 → 探测到 HTTP(S) 网络请求 (7 处)<br>涉及的域名: 127.0.0.1, api.star-history.com, arxiv.org, autotechinsight.spglobal.com, battery-news.de, blog.computationalcomplexity.org, carnewschina.com, cdn.openai.com, cims.nyu.edu, claude.ai (+45 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - LICENSE:149 → 挖矿相关 (1 处)<br>  - preset/plugins/clearai-kernel.js:2889 → 挖矿相关 (1 处)<br>  - ui/lib/fold.js:1944 → 挖矿相关 (7 处)<br>  - ui/lib/client.js:341 → 挖矿相关 (6 处)<br>  - ui/lib/knowledge-view.js:435 → 挖矿相关 (3 处)<br>  ... 共 7 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - brand/build-icons.mjs:28 → 读取环境变量 API Key/凭证 (1 处)<br>  - brand/build-social-preview.mjs:39 → 读取环境变量 API Key/凭证 (1 处)<br>  - pack/bin/clearai.mjs:31 → 读取环境变量 API Key/凭证 (6 处)<br>  - tools/install-native.mjs:36 → 读取环境变量 API Key/凭证 (2 处)<br>  - tools/e2e-run.mjs:38 → 读取环境变量 API Key/凭证 (4 处)<br>  ... 共 31 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ✅ 通过 | 未检测到明显的全局配置修改模式 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ✅ 通过 | 未检测到混淆代码模式 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - tools/panel-preview.mjs:120 → new Function() 任意代码执行 (1 处)<br>  - tools/recheck.mjs:105 → new Function() 任意代码执行 (1 处)<br>  - test/readability.test.mjs:69 → new Function() 任意代码执行 (1 处)<br>  - test/prompt-budget.test.mjs:78 → new Function() 任意代码执行 (1 处)<br>  - test/client.test.mjs:105 → new Function() 任意代码执行 (5 处) |
| 4.3 | npm audit 无高危漏洞 | 必查 | ✅ 通过 | npm audit: 高危 0, 严重 0, 中危 0 |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 7 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - brand/build-icons.mjs:81 → 进程控制 (1 处)<br>  - brand/build-social-preview.mjs:171 → 定时任务 (1 处)<br>  - brand/build-social-preview.mjs:203 → 进程控制 (1 处)<br>  - pack/bin/clearai.mjs:251 → 进程控制 (3 处)<br>  - tools/capture-ui.sh:27 → 临时文件操作 (3 处)<br>  ... 共 178 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - brand/README.md:23 → 云存储上传 (1 处)<br>  - preset/plugins/ontology.js:223 → 云存储上传 (2 处)<br>  - preset/plugins/clearai-kernel.js:3878 → 云存储上传 (1 处)<br>  - docs/research-openrsi.md:166 → 云存储上传 (1 处)<br>  - docs/known-gaps.md:11 → 云存储上传 (1 处) — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 7. repo: 1 deps + 6 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 32325, 注释行: 6556 (20.3%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: test |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - .github/workflows/release.yml:87 → 硬编码敏感信息 (1 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - tools/build-package.mjs:108 → 读取 git 历史 (1 处)<br>  - tools/spike-git-worldlines.mjs:126 → 读取 git 历史 (2 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (64 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (4 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - test/kernel.test.mjs:1921 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - package-lock.json:564 → 修改系统目录 (1 处)<br>  - install.sh:1 → 修改系统目录 (1 处)<br>  - pack/bin/clearai.mjs:1 → 修改系统目录 (1 处)<br>  - tools/capture-ui.sh:1 → 修改系统目录 (1 处)<br>  - tools/check-workspace-residue.mjs:1 → 修改系统目录 (1 处)<br>  ... 共 11 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (3 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 1 天; 提交总数: 442 |
| 7.2 | 未标记停止维护 | 必查 | ❌ 不通过 | 文档中发现弃用标记: 不再支持, deprecated, abandoned |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ⚠️  需人工复核 | 有文档但缺少: 使用示例 |
| 7.6 | 有社区背书 | 推荐 | ✅ 通过 | Stars: 1374, Forks: 48, Watchers: 25 — 高 Star 量 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | clearai-dsh |
| 校验 URL | https://github.com/Clearailhc/clearai-dsh |
| 必查项通过率 | 15/33 (45%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-10-09 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
