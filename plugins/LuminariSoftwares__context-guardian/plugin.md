# LuminariSoftwares/context-guardian

- **仓库地址**: https://github.com/LuminariSoftwares/context-guardian
- **收录分类**: 其他
- **插件简介**: 为 compaction-basic 提供压缩兜底：当 LLM 摘要抛错、返回空内容或放不进上下文窗口时，改为确定性编译该区段，每行带 seq 指针（内置 dsh-compaction-instant 编译器）。提供 recall、search 工具与 /recall、/context 命令，占用超过窗口 45% 时空闲自动压缩，并将被压缩区段归档到磁盘。引擎以一行配置挂载到 agent preset（见 docs/dsh-integration.md）。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-22
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
