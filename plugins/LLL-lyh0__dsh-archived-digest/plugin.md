# LLL-lyh0/dsh-archived-digest

- **仓库地址**: https://github.com/LLL-lyh0/dsh-archived-digest
- **收录分类**: 其他
- **插件简介**: 把已归档的会话变成可用的记忆，而不是躺在磁盘上的死数据。每条归档提炼成可复用技能、带 ADD/UPDATE/NOOP 判定与 validUntil / supersededBy 时效的事实台账（旧事实会退场而不是无限堆积），以及用 single-linkage 相似度聚合的主题簇。还能对仍在进行中的会话做增量提炼——用只读的 seq 水位线，会话日志一个字节都不改；并能自检精简不断变脏的记忆：合并重复事实、清退失效事实、归并重复技能。自检默认只测量不动手，且从不硬删除，只做取代。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-31
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
