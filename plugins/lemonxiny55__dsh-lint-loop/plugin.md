# lemonxiny55/dsh-lint-loop

- **仓库地址**: https://github.com/lemonxiny55/dsh-lint-loop
- **收录分类**: 其他
- **插件简介**: 零配置 lint 反馈闭环：由仓库已有的 eslint / biome / ruff 驱动（从配置文件自动探测、优先解析仓库本地 node_modules/.bin、不捆绑任何 linter）提供 lint_diagnostics / lint_workspace_errors / lint_fix 工具，并订阅 harness 的 fs/observed 事件自动注入「本次编辑引入的发现增量」——为 dsh Agent 带来编辑→lint→一键自动修复的闭环体验。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-13
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
