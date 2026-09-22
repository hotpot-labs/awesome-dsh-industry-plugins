# BOWLUNA/dsh-zcode-breaker

- **仓库地址**: https://github.com/BOWLUNA/dsh-zcode-breaker
- **收录分类**: 其他
- **插件简介**: 自动压缩的 rapid-refill 熔断器。当上下文在连续 M 次压缩中、每次都于不足 N 个工具轮次内又满时，拒绝这次徒劳的压缩——无上限的步压力触发检测不到这种情形——并且不做「每一步都白烧一次摘要调用」的事，而是把情况连同建议一起报告出来，通常是一次读取或一份工具输出过大。用 /compaction-breaker 查看状态与重新武装，并注入一个 prompt 段让模型把它转述给用户。宿主平面会话由 profile bundle 覆盖；普通会话需要在 agent preset 里替换一行。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-22
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
