# TodayJin/dsh-trilogy

- **仓库地址**: https://github.com/TodayJin/dsh-trilogy
- **收录分类**: 其他
- **插件简介**: DeepSeek Harness 的项目记忆插件。每个工作区三份 Markdown 文件（PROJECT.md / DECISIONS.md / SESSIONS.md）：会话首个步骤自动创建、内容变了才重新注入（被上下文压缩挤掉也会重注入），并按分类经 memory_checkpoint 工具写回，在「干了实事却没记录」时给一次收尾提醒。memory_read 与 memory_search 可读活日志与归档，后者走零依赖 BM25 索引。会话日志上限 200 条，溢出搬进 SESSIONS-archive.md —— 不自动注入，但可见、可读、可搜，并能逐条恢复。设置界面：带路径筛选的工作区列表 / 三份记忆文件与归档的只读页签 / 重新读取 / 单个工作区记忆包的导出导入（JSON）/ 两步确认的清除 / AGENTS.md 指令段的重写或移除面板 / PROJECT.md 陈旧提醒。输入框状态图标显示该工作区的同步状态，无记忆时可点击创建。零依赖——不含向量库、embedding 或模型调用。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-19
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
