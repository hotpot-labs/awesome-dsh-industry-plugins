# BEAVER-fishcake/dsh-model-source-picker

- **仓库地址**: https://github.com/BEAVER-fishcake/dsh-model-source-picker
- **收录分类**: 其他
- **插件简介**: 把输入框上的模型选择器改成「先选来源、再选模型」的菜单：第一层放大列出模型来源，每个带首字母徽标、模型数量和当前模型，点进去才是该来源的模型；模型超过 6 个时出现搜索框，每行显示推理档数或模型描述。推理强度在第一层是独立一行，对带推理档的模型则展开为第三层。它以 priority -20 占用 conversation.input.model 座位，通过 modelDirectories 服务读与 /model 命令相同的目录，两者对「能选什么」保持一致；注册失败时打印日志并把座位交还原生选择器。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-28
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
