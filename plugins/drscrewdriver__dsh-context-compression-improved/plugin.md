# drscrewdriver/dsh-context-compression-improved

- **仓库地址**: https://github.com/drscrewdriver/dsh-context-compression-improved
- **收录分类**: 其他
- **插件简介**: 机制上与上下文压缩领域最响的两条公开路线同源：代码骨架闸门沿用 Headroom（Apache-2.0）的骨架化思路，其公开头条为「编程 agent 少 20% token、JSON 载荷少 60–95% token，答案不变」；估计器通道沿用 TokenPilot（arXiv:2606.17016）的缓存感知上下文管理思路，该论文报告长会话 agent 成本最高降低 60%。这两个数字都是来源方自己的口径，此处照引；本插件不自带 benchmark，不自称任何降幅。在此之上为 DeepSeek Harness 提供：在同一设置区选择压缩 Profile、调整 Auto Compact 触发水位并开关代码骨架压缩；基于 DeepSeek V4 官方 tokenizer 的精确计量与同修订计数校验；非支持模型自动 fail-open，保留原始工具结果。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-18
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
