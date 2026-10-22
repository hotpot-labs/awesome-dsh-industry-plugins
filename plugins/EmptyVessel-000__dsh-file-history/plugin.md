# EmptyVessel-000/dsh-file-history

- **仓库地址**: https://github.com/EmptyVessel-000/dsh-file-history
- **收录分类**: 其他
- **插件简介**: 按轮次给整个工作区留检查点：每轮结束存一份快照，本轮改了哪些文件直接列在聊天里那一条下方，任意一轮都能还原——只还原文件、只还原对话，或者全部还原。捕获靠扫描整棵树，而不是挂钩 write/edit 工具，所以 shell 命令、外部编辑器、git 操作改出来的东西同样留痕。还原对话是从那一轮分叉出新会话，不切断原来的会话；还原本身也能撤销。历史存放在 DSH_HOME 里的影子 git 仓库中，不碰项目的 .git。需 Git >= 2.20 与 Node.js >= 20。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-22
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
