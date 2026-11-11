# AfeyGu/dsh-compaction-tower

- **仓库地址**: https://github.com/AfeyGu/dsh-compaction-tower
- **收录分类**: 其他
- **插件简介**: 自动压缩上下文：后台观察者提前把早期历史蒸成摘要块，占用越过触发线时逐块提交直到回到目标线以下，提交路径不调模型；材料用尽后块可合并成更高层，decompress 与 search_context 可按块读回原文。后台观察者会消耗模型 token：默认沿用会话的 provider 与 model（可另选），默认最多同时进行 10 个蒸馏。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-11
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
