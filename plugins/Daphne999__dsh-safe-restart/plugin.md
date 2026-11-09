# Daphne999/dsh-safe-restart

- **仓库地址**: https://github.com/Daphne999/dsh-safe-restart
- **收录分类**: 其他
- **插件简介**: 重启 DSH 并告诉你到底成没成。Windows 上没有「从外部让 Electron 干净退出」的通道（发 WM_CLOSE 只会最小化窗口），所以这个插件不装优雅：强制结束宿主、带重试地重新拉起、再轮询宿主端口确认它真的在服务，最后把结果写进本地文件，并在 desktop profile 配好 qq-notify 凭据（appId/clientSecret/openid）时发一条 QQ 消息。2026-11-08 端到端实测通过。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-09
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
