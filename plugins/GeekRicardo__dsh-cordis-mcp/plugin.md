# GeekRicardo/dsh-cordis-mcp

- **仓库地址**: https://github.com/GeekRicardo/dsh-cordis-mcp
- **收录分类**: 计算机
- **插件简介**: 把 DSH 的动态 Cordis 工具集以 MCP（streamable HTTP，挂在现有 web 端口上，不新开监听）暴露给 Claude Code：10 个工具，可列出、查看、定义、运行、停止与永久删除某个活 DSH 会话里的动态插件；含 client half 的包仍走 GUI 那套审批流。强制 Bearer 认证——token 在 DSH 设置页配置，未配置时端点直接 503 而不是降级放行，只接受回环访问，且永不返回 CORS 头。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-08-23
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
