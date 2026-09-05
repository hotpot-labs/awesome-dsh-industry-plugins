# Shaw529/dsh-token-saver

- **仓库地址**: https://github.com/Shaw529/dsh-token-saver
- **收录分类**: 其他
- **插件简介**: 为 DeepSeek Harness 设计的 token 节省插件：不损失任务效果。默认 conservative 档对工具结果做无损头尾裁剪与 grep 折叠；balanced 档在压力阈值委托 dsh-compaction-basic；aggressive 档以 LLM-summary 引擎子类化替换官方压缩。8 个合成场景累计节省 97.6% 输入 tokens，所有削减走 dsh 事件流，model-visible = logged 不变式仍成立。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-05
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
