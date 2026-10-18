# ChenXu233/dsh-gemini-tool-schema

- **仓库地址**: https://github.com/ChenXu233/dsh-gemini-tool-schema
- **收录分类**: 其他
- **插件简介**: 把发给模型的工具 schema 统一归一化成 Gemini function declaration 能接受的 OpenAPI 3.0 子集：每个节点补 type、数组补 items、剔除空 enum 项、内联 $ref，让"任何一个 MCP 或内置工具不合规"不再把整包请求打成 HTTP 400。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-18
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
