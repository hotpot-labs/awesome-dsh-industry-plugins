# shengyvself/narrative-prompt-polish

- **仓库地址**: https://github.com/shengyvself/narrative-prompt-polish
- **收录分类**: 其他
- **插件简介**: DSH 主输入框旁的 ✨ 一键提示词打磨：点击后在侧边对话中由 Agent 多轮改写草稿，再手动回填。复刻会话前缀以命中 prompt cache，超大或非 live 会话按 full → partial → none 降级；每次调用留 JSONL trace；API 路由带信任围栏，CAS 写回在草稿已变时拒绝覆盖。需先安装 omdsh-dev/DSH-better-sidebar（>=0.16.1），缺失时显式报错而非静默失效。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-02
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
