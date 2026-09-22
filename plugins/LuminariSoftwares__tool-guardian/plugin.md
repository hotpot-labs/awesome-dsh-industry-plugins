# LuminariSoftwares/tool-guardian

- **仓库地址**: https://github.com/LuminariSoftwares/tool-guardian
- **收录分类**: 其他
- **插件简介**: 用三个路由工具（list_capabilities、describe_tool、call_tool）代理 stdio MCP 服务器，schema 按需加载，不再随每次请求发送；所有工具结果经过确定性输出阶梯压缩，有损处理前先归档原文（retrieve_spill 可读回）；按 token 为工具分组标价，并可按 agent 隐藏内置分组。桥接到纯标准库的 Python 路由器，需要 Python 3.9+。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-22
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
