# 1jincheng/dsh-first-paint

- **仓库地址**: https://github.com/1jincheng/dsh-first-paint
- **收录分类**: 其他
- **插件简介**: 首帧启动页：把品牌启动页作为 index 注入行写进 DSH 的首帧 HTML，桌面端窗口出现时直接是启动页，而不是白屏或加载态。检测到启动动画插件开始（`window.__DSH_STARTUP_RUNNING__`）后自动淡出让位；默认 6 秒兜底（可用 maxMs 调整），不会把应用卡在启动页里。普通 dsh.bundle 插件，不改宿主、不碰 app.asar。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-06
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
