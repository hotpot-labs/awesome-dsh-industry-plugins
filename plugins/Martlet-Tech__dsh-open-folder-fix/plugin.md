# Martlet-Tech/dsh-open-folder-fix

- **仓库地址**: https://github.com/Martlet-Tech/dsh-open-folder-fix
- **收录分类**: 其他
- **插件简介**: 修正 Windows 上「打开工作目录」的行为。官方调用 `explorer.exe "<file:// URI>"`，在某些主机上会报告成功却不弹窗口——因为成功判据是退出码，分不出「窗口开了」和「什么都没发生」。本插件把该操作改走 `explorer.exe /e,<目录>`，稳定新开窗口；菜单里其它应用仍走官方路径。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-25
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
