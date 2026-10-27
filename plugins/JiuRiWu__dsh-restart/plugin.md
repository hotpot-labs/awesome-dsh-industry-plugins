# JiuRiWu/dsh-restart

- **仓库地址**: https://github.com/JiuRiWu/dsh-restart
- **收录分类**: 其他
- **插件简介**: 给 DSH Desktop 侧边栏底部加一个「重启」按钮：弹出与托盘「退出 DeepSeek Harness」完全相同的原生确认框，确认后优雅关闭并重新拉起。注意：本插件只负责画这个按钮，必须同时应用同一仓库 shell-patch/ 里的外壳补丁，且该补丁要在 DSH 关闭时由 DSH 之外的脚本执行。单独安装插件时按钮为禁用状态，悬停提示会说明原因。配套外壳补丁仅支持 Windows，会改写已安装的 app.asar。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-27
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
