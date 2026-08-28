# maxmilian/dsh-odoo

- **仓库地址**: https://github.com/maxmilian/dsh-odoo
- **收录分类**: 其他
- **插件简介**: 经 JSON-RPC 的 Odoo 只读工具：服务器信息、模型字段自省，以及受限的 search_read——仅限白名单模型，且 domain 字段名不允许包含点号，因此无法沿关联关系穿透。草稿创建工具需显式开启 allowWrite 才会注册，且仅限 sale.order 与 project.task，草稿状态由插件强制。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-08-28
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
