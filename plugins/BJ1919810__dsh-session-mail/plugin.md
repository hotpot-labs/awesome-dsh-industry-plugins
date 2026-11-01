# BJ1919810/dsh-session-mail

- **仓库地址**: https://github.com/BJ1919810/dsh-session-mail
- **收录分类**: 其他
- **插件简介**: 同一宿主内 DSH 会话之间的代理传话。`send_session_message` 可等对方回合结束再送达、也可插进正在跑的回合；发信方 id 由插件自己写，伪造的 From 抬头会被拒；每条消息带 id —— 回信可用 replyTo 引用、thread 防止同一件事排队两次、supersedes 撤回尚未投递的旧消息。`read_session_info` 只读地看对方：标题、最后一轮回复、最后一次 present 的文件、以及忙闲与队列深度。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-01
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
