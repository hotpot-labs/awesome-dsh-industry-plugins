# DWJZ/dsh-allow

- **仓库地址**: https://github.com/DWJZ/dsh-allow
- **收录分类**: 其他
- **插件简介**: 按路径与能力（read / write / create / delete / execute）授予 shell 调用的文件权限，而不是按命令名判断。命令行的文件效果由解析得出，缺哪个能力就出审批卡片而不是一律拒绝，同一套规则还会编译成进程、它的子进程、以及命令行根本没露出来的代码共同运行其下的 macOS Seatbelt profile。会话里的「审批」标签页把审计日志读回来，显示每次判定是规则、自动复核还是人拍的板。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-22
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
