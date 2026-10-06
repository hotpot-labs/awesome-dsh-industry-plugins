# ZhaoZeW/dsh-rollback

- **仓库地址**: https://github.com/ZhaoZeW/dsh-rollback
- **收录分类**: 其他
- **插件简介**: TRAE 式「回退到本轮对话发起前」：按轮次建立文件检查点，回滚工作区文件并在同一 session id 下原位截断模型上下文，已适配 DSH 0.1.7-rc.2。新增 /rollback doctor 契约自检、按当前磁盘状态实时计算的受影响文件 diff 预览（重启后依然准确）、一键「回退最近一轮」（快捷键 Ctrl+Shift+Z）、「回退后隐藏已回退消息」开关，以及英文界面文案。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-06
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
