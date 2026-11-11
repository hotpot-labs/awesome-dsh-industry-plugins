# Domush/dsh-plugin-context-mode

- **仓库地址**: https://github.com/Domush/dsh-plugin-context-mode
- **收录分类**: 其他
- **插件简介**: 原生支持 context-mode (mksglu/context-mode)，通过 SQLite FTS5 拦截工具大输出并提供 BM25+RRF 搜索与会话连续性恢复。默认开启：超过 4 KB 的工具输出会被替换成简短预览，全文索引进 ~/.context-mode/context.db，并在系统提示里加一段说明。其 ctx_execute、ctx_batch 工具以 DSH 自身的权限和环境变量运行 shell / Node / Python / PowerShell / cmd 命令（没有沙箱），ctx_index 可读取任意本地文件路径或抓取任意 http(s) 地址。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-11
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
