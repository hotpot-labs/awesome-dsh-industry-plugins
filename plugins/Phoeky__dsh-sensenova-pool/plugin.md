# Phoeky/dsh-sensenova-pool

- **仓库地址**: https://github.com/Phoeky/dsh-sensenova-pool
- **收录分类**: 其他
- **插件简介**: 把商汤日日新（SenseNova）模型接入 dsh，并提供按 Key 轮换的 Key 池：粘贴任意多把 API Key，请求在多把 Key 之间轮转；遇 429 限流立即换下一把 Key 重试，每把 Key 独立指数退避冷却；本地 RPM 预限流从源头避开限流，池子耗尽时回报 503 与 Retry-After，使 429 不会传到调用方。内置可离线使用的模型目录并从 /v1/models 刷新，设置卡片提供脱敏 Key 列表、单把探活与删除。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-22
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
