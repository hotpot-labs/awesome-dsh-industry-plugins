# HanYu-me/dsh-small-toolkit

- **仓库地址**: https://github.com/HanYu-me/dsh-small-toolkit
- **收录分类**: 其他
- **插件简介**: 一个插件里的两个 macOS 小功能。keepAwake：dsh 运行期间不让屏幕和系统休眠（caffeinate 跟随宿主进程，dsh 退出即解除）。taskNotify：主对话一轮结束时发系统通知，写明结果（完成、出错、被拦截、输出达到上限）和用时；点击通知会切回 DeepSeek Harness。点击切回需要 Xcode Command Line Tools 构建通知助手；没有工具链时仍会提醒，但点击打开的是「脚本编辑器」。子智能体和 Agent Teams 成员不提醒，你手动停止的任务默认不提醒。两个功能可以分别关闭。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-05
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
