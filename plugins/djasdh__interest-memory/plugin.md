# djasdh/interest-memory

- **仓库地址**: https://github.com/djasdh/interest-memory
- **收录分类**: 其他
- **插件简介**: 由本地 Go 服务支撑的跨会话长期记忆（约 50MB 内存，SQLite-vec + 经验证增强的论断）：每条用户消息零延迟注入召回、会话结束时摄入对话记录，提供 memory_search / memory_logs / memory_ingest 工具。安装：`dsh plugin --profile web add @djasdh/interest-memory-dsh-bridge`。仅为协议桥：Go 主服务不随 `dsh plugin add` 安装，需先按仓库 README 安装并启动；服务未运行时工具静默返回空。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-09
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
