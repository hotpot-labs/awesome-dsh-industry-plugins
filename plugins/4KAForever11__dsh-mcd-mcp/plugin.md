# 4KAForever11/dsh-mcd-mcp

- **仓库地址**: https://github.com/4KAForever11/dsh-mcd-mcp
- **收录分类**: 其他
- **插件简介**: 把麦当劳中国官方 MCP(mcp.mcd.cn)接入 DSH。粘贴自己在官网生成的 Token 后，插件会握手并调用 tools/list，把远端全部工具自动注册成 DSH 原生工具(mcd_ 前缀)，官方增删工具无需改代码，重启即同步。另附 mcd_status、mcd_test、mcd_tools、mcd_call 四个常驻工具用于自检与兜底直调，设置页可一键测试连通性。Token 只存本机 ~/.dsh/dsh-mcd-mcp.json(权限 600)，不进仓库、不进对话上下文。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-28
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
