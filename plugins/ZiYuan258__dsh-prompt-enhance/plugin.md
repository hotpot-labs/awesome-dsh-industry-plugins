# ZiYuan258/dsh-prompt-enhance

- **仓库地址**: https://github.com/ZiYuan258/dsh-prompt-enhance
- **收录分类**: 其他
- **插件简介**: dsh-prompt-enhance 的维护分支，已适配 DSH 0.1.7——此前的版本在当前宿主上甚至无法加载（InputState.imageIds 已更名为 attachmentIds，输入框按钮会让整个输入区崩溃；settings.get() 已被移除；/enhance 读取了 agent 不再暴露的会话 id）。改写默认使用 reasoningEffort off：实测同一段草稿为 252 输出 token，而模型自身默认档要 2897；并内置覆盖全部 17 个字段的设置页。已在真实的 0.1.7-rc.2 宿主上验证：插件激活、真实 HTTP 增强请求、GUI 中 /enhance 执行，以及设置页读取并持久化配置。204 项测试。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-06
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
