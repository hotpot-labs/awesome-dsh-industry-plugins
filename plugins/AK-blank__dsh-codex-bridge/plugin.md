# AK-blank/dsh-codex-bridge

- **仓库地址**: https://github.com/AK-blank/dsh-codex-bridge
- **收录分类**: 其他
- **插件简介**: 读取本机 Codex CLI 的 ChatGPT 计划额度（5 小时与每周窗口），默认统一使用 gpt-6.1-sol + high 推理强度，任一窗口剩余不超过 10% 时回退 gpt-5.6-sol，并通过 codex exec 外派任务；昂贵的 gpt-6-astra 需要显式开启。需已登录的 Codex CLI（`codex login`）。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-22
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
