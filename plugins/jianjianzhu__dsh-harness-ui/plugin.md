# jianjianzhu/dsh-harness-ui

- **仓库地址**: https://github.com/jianjianzhu/dsh-harness-ui
- **收录分类**: 其他
- **插件简介**: 从侧栏打开的整页控制台面板，含八个标签：总览；从 sessions 服务读取的会话列表（标题、目录、运行状态、更新时间，带筛选）；从 pluginInventory 与 pluginManager 读取的已装 bundle 与 Loader 条目，每个 bundle 带启用开关；列出 GitHub 搜索 API 中 topic:dsh-plugin 公开仓库的插件市场；一个模型与供应商编辑器，通过 remote.settings.mutate 写入 llm-pi-ai 配置命名空间（切换会话模型、新增或编辑供应商及其模型列表、经 remote.credentials 保存 API Key，并以合并方式写入以免表单未暴露的字段被覆盖）；MCP 与技能两个标签；以及一个读取宿主回环 /api/dsh-usage/overview 文档的用量标签。所需服务通过 ctx.inject 声明，缺少任一服务的部署只是不挂载该面板，不会崩溃。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-21
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
