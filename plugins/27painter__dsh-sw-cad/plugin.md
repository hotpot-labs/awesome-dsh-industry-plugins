# 27painter/dsh-sw-cad

- **仓库地址**: https://github.com/27painter/dsh-sw-cad
- **收录分类**: 其他
- **插件简介**: 注册两个 MCP 服务器，在 Windows 上通过 COM 驱动本机安装的 AutoCAD 与 SolidWorks，另附两个按需技能。仅 Windows，需要 Python 3.11+；首次加载时自动安装钉死版本的上游服务器，并且只给真正装了的 CAD 应用注册对应的那一行。两者都只广告两个元工具而非完整工具表（SolidWorks 用本仓库的 discovery 垫片，AutoCAD 用上游 DISCOVERY_MODE=search），首次请求前加载的工具定义分别从 23,404 降到 256 token、从 83,732 降到 365 token。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-27
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
