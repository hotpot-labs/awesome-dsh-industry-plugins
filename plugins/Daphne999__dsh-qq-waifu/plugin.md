# Daphne999/dsh-qq-waifu

- **仓库地址**: https://github.com/Daphne999/dsh-qq-waifu
- **收录分类**: 其他
- **插件简介**: 让 AI 在 QQ 里一句一句发消息：把每条回复拆成几个气泡、按字数给打字停顿、句末不留句号；表格和代码块整条不切。做法是给 desktop profile 里的 @tencent-connect/dsh-qqbot 发送链打补丁：先手动运行一次 node outbound/apply-patch.mjs、把 im-qqbot 的 streaming 设为 false 并重启；在此之前只有 waifu_* 工具可用。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-08
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
