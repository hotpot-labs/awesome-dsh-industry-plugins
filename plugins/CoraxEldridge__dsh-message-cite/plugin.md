# CoraxEldridge/dsh-message-cite

- **仓库地址**: https://github.com/CoraxEldridge/dsh-message-cite
- **收录分类**: 其他
- **插件简介**: 引用另一段对话里的某一条具体消息：在输入框 @ 菜单里选中后插入 chip，发送时把原文作为不可信背景注入本轮；另有一个 conversation_history 工具，让模型自己搜索并读取本工作区内的其他对话。@ 菜单会搜索所有工作区里已建索引的会话（只有给模型用的工具限定在当前工作区）；插件的 HTTP 路由（/dsh-message-cite/api/…）只靠一个标记头把关，没有 DSH 的访问检查。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-12
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
