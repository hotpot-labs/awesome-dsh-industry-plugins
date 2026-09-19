# bycall/dsh-engineer-tools

- **仓库地址**: https://github.com/bycall/dsh-engineer-tools
- **收录分类**: 其他
- **插件简介**: 面向软件工程师的 DeepSeek Harness 插件：注册两个模型可直接调用的 Host Tool——受工作区约束的 `git` 运行器，以及按 lockfile 自动识别 npm/pnpm/yarn/bun 并选择正确动词的包管理器运行器（`dev`）。两者都经 dsh 沙箱 shell 执行，返回规整的 stdout/stderr/exitCode，让 agent 拿到聚焦、可复核的结果而不是裸 bash；再加一个工具只需复制一个 register 块。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-19
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
