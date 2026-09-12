# 173787247/dsh-wsl-fetch

- **仓库地址**: https://github.com/173787247/dsh-wsl-fetch
- **收录分类**: 其他
- **插件简介**: 在 ctx.web 注册 wsl-proxy 抓取后端，让官方 web_fetch 经 HTTP(S)_PROXY 用 undici ProxyAgent 出网，避免官方实现在 WSL 里 DNS 钉死后直连公网 IP，从而在 Windows 代理后出现 TypeError: fetch failed。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-12
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
