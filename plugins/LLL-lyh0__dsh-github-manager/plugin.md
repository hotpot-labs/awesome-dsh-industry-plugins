# LLL-lyh0/dsh-github-manager

- **仓库地址**: https://github.com/LLL-lyh0/dsh-github-manager
- **收录分类**: 其他
- **插件简介**: 同一个账户库的两半：左侧「GitHub 仓库」面板是结构性只读（只有三个 GET 端点，任何非 GET 在路由前直接 405，请求体从不读取，令牌不出宿主），以及一个 github-manager 技能，只暴露两个工具 —— github_accounts 与 github_api —— 写入动作交给 Agent。登录走 GitHub Device Flow，账户库按 mtime 自动失效，后加进来的令牌无需重启即可生效。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-31
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
