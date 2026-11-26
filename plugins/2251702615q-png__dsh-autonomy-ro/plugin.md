# 2251702615q-png/dsh-autonomy-ro

- **仓库地址**: https://github.com/2251702615q-png/dsh-autonomy-ro
- **收录分类**: 其他
- **插件简介**: DeepSeek Harness 的 Chat | Agent 开关插件，基于 dsh-autonomy 0.1.5（MIT）改造，只改一处行为：Chat 模式保留「读」的一半工具面（read、read_image、glob、grep、web_search、web_fetch、skill 与会话记忆只读工具），write、edit、pwsh 等一切会改动东西的工具一律拒绝；Agent 模式恢复全部工具。三道闸同时生效：下发给模型的工具清单先过滤，执行期 guard 再拒绝白名单外的调用，系统提示词里说明当前模式允许什么。模式按会话记录，刷新、重启、恢复后仍然有效。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-26
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
