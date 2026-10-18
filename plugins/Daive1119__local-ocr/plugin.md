# Daive1119/local-ocr

- **仓库地址**: https://github.com/Daive1119/local-ocr
- **收录分类**: 其他
- **插件简介**: 为纯文本模型注册一个 `ocr` 工具：调用仓库自带的离线脚本识别单张图片或 PDF 并返回文字——Windows 原生 OCR 优先，其次 RapidOCR，最后 Tesseract；识别过程在本机完成，不发网络请求、不需要 API key。需自备 PATH 上的 Python 3.11 并 `pip install winocr pillow`（winocr 为首选引擎，RapidOCR 与 Tesseract 为兜底）。图片返回逐行结果，PDF 返回逐页结果。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-18
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
