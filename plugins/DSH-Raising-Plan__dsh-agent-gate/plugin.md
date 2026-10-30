# DSH-Raising-Plan/dsh-agent-gate

- **仓库地址**: https://github.com/DSH-Raising-Plan/dsh-agent-gate
- **收录分类**: 其他
- **插件简介**: DSH 工具调用的咨询式权限检查：风险分级、路径沙箱（allowed_roots 为空时一律拒绝）、每分钟调用限额与 JSONL 审计，通过 gate_check / gate_check_path / gate_policy 与 ctx.gate 提供——需由其他插件或提示主动调用，本身不拦截工具调用。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-30
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
