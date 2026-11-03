# EviMing/dsh-qq-shell-commands

- **仓库地址**: https://github.com/EviMing/dsh-qq-shell-commands
- **收录分类**: 其他
- **插件简介**: 目的是能远程运行 Shell 命令，而不是让 DSH 运行，适用于需要重复工作或托管行为但不能直接给权限到 DSH 的情况。原理是通过 NapCat 进程与 QQ 进行交互，当 QQ 发送特定消息，判断是否完全相等与哪个键的字符串，并执行对应的 Shell 命令。执行 Shell="执行 Shell 命令：\n文本"。添加新的键值对="增加 Shell 命令：\n{"文本": ["Shell 命令", "使用哪个 Shell (例如 cmd，或 PowerShell) 运行 Shell 命令"]}"，最终会被拼接为 "Shell 命令" 的格式被系统运行，依赖前置插件 "EviMing/dsh-napcat-tools"需先安装 EviMing/dsh-napcat-tools，并准备 NapCat 与 Python 3.10+。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-03
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
