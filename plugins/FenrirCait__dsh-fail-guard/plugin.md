# FenrirCait/dsh-fail-guard

- **仓库地址**: https://github.com/FenrirCait/dsh-fail-guard
- **收录分类**: 其他
- **插件简介**: 同一工具连续失败达阈值时叫停。不是再试一次，而是推送一条四部分停手指令：试过什么、完整错误原文、初判原因、需要用户做什么。判定读真实工具结果（isError 或 shell 退出码非零），通过 agent.steer 回灌，让 agent 把它当成收到的消息而不是日志。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-02
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
