# HarunaTyan/dsh-rea-dispatcher

- **仓库地址**: https://github.com/HarunaTyan/dsh-rea-dispatcher
- **收录分类**: 其他
- **插件简介**: REA（逆向一切，上游 REA MCP 服务）的另一种接入方式：不把它的 207 个工具（每次请求约 77.5 万字节的工具表）直接挂进宿主，而是只暴露三个调用——rea_tools 按域列出目录、rea_help 取单个工具的 schema、rea_call 原样透传参数——超限结果落盘而不是静默截断。不代装引擎：需自行安装 REA（rea-agents 6.x）与 Ghidra 12.1.x；反编译质量由 REA/Ghidra 决定，不由插件决定。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-31
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
