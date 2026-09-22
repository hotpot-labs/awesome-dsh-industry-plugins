# 7starsseeker/dsh-jev-guard

- **仓库地址**: https://github.com/7starsseeker/dsh-jev-guard
- **收录分类**: 其他
- **插件简介**: DSH 执行前安全阀门，用 TypeSafe Jev 模型做判定：挂载 tools/pre-execute，对每条 bash/pwsh 调用先过离线静态规则，再向 Jev 模型（TypeSafe 的 System One 模型，返回结构化判定而非散文）提一个是非问句——「这条命令会不可逆地删除或覆盖真实数据吗？」——把答案切成允许／修正／拦截／上报人工四态；修正给模型更安全的写法，上报提供一次性人工令牌；额度耗尽或没有可用密钥时大声降级而非静默失效，缺密钥时会直接在对话里要求录入（录入用 `guard key set`，只从标准输入读）；每条判定写入共享审计日志，面向人的文案中英双语。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-22
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
