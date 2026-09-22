# BOWLUNA/dsh-zcode-git

- **仓库地址**: https://github.com/BOWLUNA/dsh-zcode-git
- **收录分类**: 其他
- **插件简介**: 给 DeepSeek Harness 智能体用的结构化 Git 工具：status、diff、log、branch、commit 与 stash。输出由十项 `git -c` 覆盖钉死，因此用户的 pager、颜色或 quotepath 设置无法改变智能体读到的东西；每次调用都是 argv 数组，任何 shell 都不解析参数；写入动作走 harness 的审批服务，没有装审批服务时拒绝执行而不是放行。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-22
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
