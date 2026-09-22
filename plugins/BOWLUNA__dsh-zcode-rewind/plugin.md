# BOWLUNA/dsh-zcode-rewind

- **仓库地址**: https://github.com/BOWLUNA/dsh-zcode-rewind
- **收录分类**: 其他
- **插件简介**: 逐工具调用的工作区检查点:记录工作区内每一次文件改动(默认排除 .git 与 node_modules),包括由 shell 命令而非 write/edit 造成的改动,并把每个被改路径的旧内容存进工作区之外的内容寻址库。恢复有两种模式——撤销单条记录,或回到某个时间点——带行级 diff 预览、默认 dry run,且每次恢复前都先写保护快照,所以恢复本身也能被撤销。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-22
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
