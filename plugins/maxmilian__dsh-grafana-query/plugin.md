# maxmilian/dsh-grafana-query

- **仓库地址**: https://github.com/maxmilian/dsh-grafana-query
- **收录分类**: 其他
- **插件简介**: 面向 Grafana 的只读工具，经数据源代理查询指标：实例健康、数据源列表、instant 与 range PromQL 查询、当前告警状态与已配置的告警规则。range 查询会按点数预算降采样；调用方显式指定的 step 若会超量则直接拒绝，而不是静默改写，避免模型拿到与预期不同分辨率的数据。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-08-28
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
