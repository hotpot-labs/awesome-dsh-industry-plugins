# apex-mochen/dsh-reasoning-only-guard

- **仓库地址**: https://github.com/apex-mochen/dsh-reasoning-only-guard
- **收录分类**: 其他
- **插件简介**: 防止「只有推理、没有正文」的一轮把整个会话变成不可用。某一轮没有可见文本也没有 tool-call 时，assistant 消息会以空内容落盘，此后该会话的每一次请求都会被网关以 "content or tool_calls must be set" 拒绝，会话彻底死亡且无法再从对话里找回。本插件只注册一个 llm/stream waterfall 监听器，且仅当这一轮没有任何可见产出时，在终止 finish 之前注入一小段文本，使落盘消息永远不为空。附带 DSH 自带 mock 造不出的夹具（严格只有推理的 SSE 服务，因为 llm-mock-server 不允许空 successText，且 reasoning_success 总会再补一段正文），以及把真实落盘会话经 DSH 自己的 serializeMessages 重放的端到端复现。属预防而非修复。零依赖、单文件、不访问进程与文件系统。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-17
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
