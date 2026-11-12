# Diomchen/dsh-cross-agent

- **仓库地址**: https://github.com/Diomchen/dsh-cross-agent
- **收录分类**: 其他
- **插件简介**: 同一局域网内两台机器上的 DSH 建立跨端会话：UDP 发现、显式单向放行与 open/confirm 审核、带 ±60 秒时间窗和 nonce 防重放的 HMAC 签名 HTTP、把指令投进 `跨端 · <对端名>` 会话、两阶段传输 ≤100 MiB 的文件并校验 sha256，以及七个只能调用对方 `exposedTools` 白名单内具名工具的 agent 工具。本机的 /cross-agent 面板路由只用回环地址检查把关，没有 DSH 的 Host/Origin 准入。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-12
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
