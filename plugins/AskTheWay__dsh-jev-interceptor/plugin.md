# AskTheWay/dsh-jev-interceptor

- **仓库地址**: https://github.com/AskTheWay/dsh-jev-interceptor
- **收录分类**: 其他
- **插件简介**: 在 tools/pre-execute 上用 Jev（TypeSafe AI 的非生成式决策模型）对待执行的工具调用分类——高置信高危拒绝、存疑转审批——并在 approval/request 上对明确授权且可逆的调用做带参数证据门控的自动批准。另子类化 session-reference resolver，让引用快照按 Jev 打分保留消息而非最旧优先丢弃。任何 provider 故障均回退原生行为；提供 shadow 模式与 /jev-stats 统计命令；支持 TypeSafe 或 OpenRouter 入口；64 个测试。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-25
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
