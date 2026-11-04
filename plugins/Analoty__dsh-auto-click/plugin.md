# Analoty/dsh-auto-click

- **仓库地址**: https://github.com/Analoty/dsh-auto-click
- **收录分类**: 其他
- **插件简介**: DSH Web 界面里的文件手势：Ctrl+左键点击文件树行、对话中的文件提及或文件链接，用系统默认应用打开；右键弹出菜单，可打开文件、调用系统自带的「打开方式」选择框、另存为、复制绝对路径、复制文件内容、在文件管理器中定位，右键普通超链接则提供「复制链接」。普通左键仍交给 DSH 自带的侧边栏预览，目录行交给页面处理。打开与定位走 DSH 自己的 sessionController，「打开方式」直接交给操作系统对话框（Windows 的 Shell 动词、macOS 的 open -a），插件不维护自己的应用列表；读取文件内容上限 8 MiB。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-04
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
