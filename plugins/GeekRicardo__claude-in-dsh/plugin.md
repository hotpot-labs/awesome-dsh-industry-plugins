# GeekRicardo/claude-in-dsh

- **仓库地址**: https://github.com/GeekRicardo/claude-in-dsh
- **收录分类**: 其他
- **插件简介**: 把一个 dsh web 会话交给本机 Claude Code CLI 驱动：输入框内的引擎选择器（DSH | Claude Code）按会话切换，模型座换成 Claude 的模型与 reasoning effort，访问模式换成 Claude 权限档；权限请求、AskUserQuestion、ExitPlanMode 分别接到 dsh 原生的审批卡、提问卡与计划审核卡。Claude 的流写成 dsh 原生会话事件，由内建转录、工具卡片与嵌套子 agent 渲染；斜杠命令并入命令面板；CLI 由独立 broker 持有，插件更新与 dsh 重启都不中断进行中的轮次。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-08-28
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
