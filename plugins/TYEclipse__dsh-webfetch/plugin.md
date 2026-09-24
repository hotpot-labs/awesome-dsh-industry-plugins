# TYEclipse/dsh-webfetch

- **仓库地址**: https://github.com/TYEclipse/dsh-webfetch
- **收录分类**: 其他
- **插件简介**: 纯文本 agent 的网页阅读工具。五个只读工具：web_fetch（把任意 URL 渲染成干净的 Markdown 或纯文本）、web_links（清单页内链接）、web_feed（RSS 2.0 / Atom 条目解析）、web_headers（不下正文即取 HTTP 状态、响应头与重定向链，HEAD 失败自动回退 GET）、web_table（把 HTML 表格抽成结构化行，含表头识别与 colspan/rowspan 网格展开）。传输层为 Node fetch 加一套零依赖 HTTP 代理实现（CONNECT 隧道、绝对 URI 请求、NO_PROXY 的后缀/通配/IPv4 CIDR 匹配、Proxy-Authorization）。零运行时依赖。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-24
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
