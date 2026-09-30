# ethanwong-hk/dsh-thinking-guard

- **仓库地址**: https://github.com/ethanwong-hk/dsh-thinking-guard
- **收录分类**: 计算机
- **插件简介**: 空转回合熔断器：监听 agent/assistant-stream，对只产出 reasoning、零文本零工具调用的回合实施三重熔断——45 秒无进展、单次思考超 80000 字符、或命中退化重复模式（精确重复单元/句模重复/稀疏复读/6-gram 密度）。熔断后注入继续指令，要求下一个动作必须是工具调用；附 11 个回归用例与逐档调参。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-30
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
