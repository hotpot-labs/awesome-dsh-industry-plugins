# john-walks-slow/dsh-wait-subagent

- **仓库地址**: https://github.com/john-walks-slow/dsh-wait-subagent
- **收录分类**: 其他
- **插件简介**: 为 DeepSeek Harness 提供后台子代理的主动等待：注册 wait_subagent 模型工具，阻塞等待指定的后台 continuable（可续会话）子代理收尾（settlement），返回停止原因与收尾消息——可选超时、成员资格门控拒绝未知 id、事件驱动零轮询。补齐 run_in_background 发后不管与异步收尾通知之间的缺口：等待后台子代理（subagent wait）不再轮询 list_agents、不再靠猜。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-28
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
