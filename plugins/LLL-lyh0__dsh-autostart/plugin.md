# LLL-lyh0/dsh-autostart

- **仓库地址**: https://github.com/LLL-lyh0/dsh-autostart
- **收录分类**: 计算机
- **插件简介**: 写 HKCU\Software\Microsoft\Windows\CurrentVersion\Run 让 DSH 在 Windows 登录时启动，插件被关闭或卸载时精确移除那一条。84 行，没有守护进程、没有后台进程、不装服务；通过 execFileSync 写入，安装路径含空格时仍保留引号，登录时确实能拉起。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-31
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
