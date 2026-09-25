# flandre2233/dsh-recovery-resume

- **仓库地址**: https://github.com/flandre2233/dsh-recovery-resume
- **收录分类**: 其他
- **插件简介**: DSH 重启后自动续跑被中断的回合：在会话激活后读取崩溃修复写入的 turn/end，投出要求先核对真实状态（不假定外部操作成功或失败）的续跑消息；永久性失败（认证、配额、上下文超限）直接跳过，并有跨重启次数预算、自适应退避与最小上下文注入。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-25
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
