# RUI-debug769/dsh-dotclaude

- **仓库地址**: https://github.com/RUI-debug769/dsh-dotclaude
- **收录分类**: 其他
- **插件简介**: 在 DeepSeek Harness 里运行 Claude Code 项目的 .claude/ 斜杠命令与 permissions.deny 规则。命令正文会把 $ARGUMENTS、位置参数与 @文件引用展开进模型的下一轮；命中的工具调用在执行前被拒绝。所有宿主服务都做探测：缺命令注册表、工作目录服务或 TUI 状态行时只降级一个功能，不会让宿主启动失败。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-22
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
