# Gaudi-XIX/dsbot-session-create

- **仓库地址**: https://github.com/Gaudi-XIX/dsbot-session-create
- **收录分类**: 其他
- **插件简介**: 给会话加四个工具：create_session 在指定工作区或任意一个已存在的文件夹里开一个新会话，并把一段提示词投进去；session_message 给一个已经在跑或已结束的会话再追加一条消息（排队投递，落在当前这一轮之后）；read_session_transcript 按会话 id 读回它说过什么、当前这一轮结束没有；list_dispatched_sessions 列出本插件派送过哪些会话、各自此刻什么状态。宿主半边插件，没有界面，调用的是宿主自己的建会话能力。装完需重启 DSH。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-31
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
