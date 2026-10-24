# JayYuen666/dsh-quality-gate

- **仓库地址**: https://github.com/JayYuen666/dsh-quality-gate
- **收录分类**: 计算机
- **插件简介**: 回合收口质量门禁：本回合改过代码或配置时，把改过的文件逐个上溯到项目根，从固定白名单里为该根跑一条检查（`pnpm check` / `cargo check` / `ruff check .` / `tsc --noEmit`）；只有真跑过且失败才带着输出开新轮修复，而不是让回合直接收尾。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-24
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
