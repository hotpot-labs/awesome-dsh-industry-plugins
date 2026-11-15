# Donglin027/dsh-session-cleanup

- **仓库地址**: https://github.com/Donglin027/dsh-session-cleanup
- **收录分类**: 其他
- **插件简介**: 清理 DSH 删除会话后的残留：孤儿附件、会话投影缓存、dsh-spill 临时目录，以及 cost-meter 账本里 已不存在会话的行。宿主插件监听 api-session/removed 自动清理（去抖 800 ms，启动补扫一次）， 另带预览优先的 CLI。默认 dry-run，真删只移入 DSH_HOME\trash\session-cleanup\<时间戳>\ 并写 journal.json。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-15
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
