# 544244857/dsh-image2-plugin

- **仓库地址**: https://github.com/544244857/dsh-image2-plugin
- **收录分类**: 其他
- **插件简介**: 注册 `image2_generate` 工具：调用你自己的 OpenAI 兼容图片中转站生成或编辑图片（文生图走 POST /images/generations，图生图走 POST /images/edits 并接受本地 PNG/JPEG/WebP 参考图，兼容 b64_json 与图片 URL 返回），图片保存在会话工作目录内，并借助其 `@wisdoverse/dsh-inline-media-viewer` 依赖在对话里内联渲染。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-18
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
