# Elycheng/dsh-article-annotator

- **仓库地址**: https://github.com/Elycheng/dsh-article-annotator
- **收录分类**: 其他
- **插件简介**: 在 DSH 原生右侧栏做逐句文稿批注：把 Markdown、Word、PowerPoint、PDF 变成可按句点选的文本，给任意一句写意见，并把待处理批注作为草稿交给 Agent。6 个 Agent 工具让模型读取每条意见、改稿（Markdown 直接改原文件，二进制格式写同名 .revised.md）、勾销批注，并把反复出现的表达偏好记入长期写作风格记忆、注入之后的提示。DOCX/PPTX 为零依赖解析；PDF 文本提取在本机走宿主 Python + pypdf（或 poppler 的 pdftotext），两者都没有时 PDF 不可用。不联网、无遥测。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-09
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
