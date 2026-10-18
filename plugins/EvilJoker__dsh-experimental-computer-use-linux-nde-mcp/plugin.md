# EvilJoker/dsh-experimental-computer-use-linux-nde-mcp

- **仓库地址**: https://github.com/EvilJoker/dsh-experimental-computer-use-linux-nde-mcp
- **收录分类**: 计算机
- **插件简介**: 为中兴 Nde 桌面定制的 DSH Cordis computer-use provider。npm install 完成后由 postinstall 钩子从 computer-use-linux-zte-nde v0.7.7-nde.3 release 自动下载 musl 静态二进制到包内 bin/，SHA 校验后 chmod +x；cordis patch 里的 command 用相对路径，由 provider 内部 resolveCommand() 依据 import.meta.url 解析为绝对路径，不依赖 dsh web 的 cwd。占用 DSH 一等公民 ctx.computerUse slot，工具命名空间为 mcp__computer-use-linux-nde-mcp__*（screenshot、list_windows、click、type_text、doctor 等）。binary 本身携带两个 Nde 适配修复：KWin 窗口寻址的 caption+coords 兜底，以及 SnapshotCache——同一 (app, pid) 5 秒内的 AT-SPI 树结果复用、避免 Chrome 反复被唤醒。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-18
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
