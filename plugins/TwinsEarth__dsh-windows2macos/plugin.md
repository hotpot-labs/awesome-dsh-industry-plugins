# TwinsEarth/dsh-windows2macos

- **仓库地址**: https://github.com/TwinsEarth/dsh-windows2macos
- **收录分类**: 其他
- **插件简介**: 一条指令同时下发给所有在线的 Windows 与 macOS 机器，可跨网络跨区域：零依赖中继只通过出站连接与各机通信（Tailscale 内网、公网 VPS + TLS、或隧道），各机在各自的项目副本上执行，结果连同 commit、工作区指纹与命令哈希一并回传，因此"环境不一致"会被判为 unverifiable，而不会被误当成结果分歧。下发指令需要独立于设备令牌的 operator token。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-15
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
