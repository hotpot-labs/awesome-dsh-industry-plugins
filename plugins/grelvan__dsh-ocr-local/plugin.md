# grelvan/dsh-ocr-local

- **仓库地址**: https://github.com/grelvan/dsh-ocr-local
- **收录分类**: 其他
- **插件简介**: 纯文本路由的本地 OCR 兜底：会话模型明确声明不接受图片时，把附件的图片存入本地缓存并注入路径，模型调 ocr_image 用 PP-OCRv5 + ONNX Runtime 在纯 CPU 上离线识别，无需 API key，图片不出本机；模型能看图时静默。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-16
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
