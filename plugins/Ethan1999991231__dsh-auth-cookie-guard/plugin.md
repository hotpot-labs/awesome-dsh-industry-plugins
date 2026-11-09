# Ethan1999991231/dsh-auth-cookie-guard

- **仓库地址**: https://github.com/Ethan1999991231/dsh-auth-cookie-guard
- **收录分类**: 其他
- **插件简介**: 当一次响应里已经带上 4 条以上 dsh-auth-* Cookie 时，把更早启动绑定到其它端口的那些逐条过期；对已经撞上 HTTP 头长度上限的请求回一个顺带清掉它们的跳转，让卡住的桌面端无需手动清 Cookie 也能重新打开。是 jitianjiyan/dsh-auth-cookie-guard 的衍生版本（目录中已收录）；两者声明同名 npm 包，不能同时安装。需要 DSH 0.2.1-rc.5 或更新版本。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-09
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
