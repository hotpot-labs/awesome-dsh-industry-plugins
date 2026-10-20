# NIRVANA-APOC/dsh-api-cost

- **仓库地址**: https://github.com/NIRVANA-APOC/dsh-api-cost
- **收录分类**: 其他
- **插件简介**: 注册 apiCost 会话投影，按官方公布的峰谷价目表把上报的 token 用量折算成 ¥/$ 花费，覆盖本会话、委派树与经校验的团队三种范围：输入框下方的胶囊与其详情面板、/cost 命令、session_cost 工具，以及读取视图与当前价目表的 GET 路由。面板上的开关可在高峰时段把模型请求停在 llm/stream 上，待谷时窗口开启后原样派发，于是按谷时价计费，且会话中不会出现任何失败。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-20
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
