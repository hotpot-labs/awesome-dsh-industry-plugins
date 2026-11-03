# Jisiyong-A/dsh-plugin-background-compaction

- **仓库地址**: https://github.com/Jisiyong-A/dsh-plugin-background-compaction
- **收录分类**: 其他
- **插件简介**: 作为会话压缩引擎注册，后台预计算压缩摘要，压力压缩触发时直接提交已持有的结果，省去前台模型往返。锁定已摘要的区间以保证提交时载荷指纹仍然匹配，提交前先裁剪工具结果；载荷漂移或上下文溢出时回退到原生前台路径。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-03
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
