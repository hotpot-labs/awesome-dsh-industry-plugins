# DanneLeung/dsh-multi-key-rotation

- **仓库地址**: https://github.com/DanneLeung/dsh-multi-key-rotation
- **收录分类**: 其他
- **插件简介**: 给 MiniMax Token Plan 路由配置多个具名 API Key，插件按剩余配额轮换：单个 Key 额度耗尽、触发限流或鉴权失败时，路由切到池中下一个 Key 并重试本次请求。下一个 Key 按重置时间排序，周窗口最先重置的先用。每个 Key 的 5 小时与周两个窗口的剩余比例、距重置倒计时都列在设置页；输入框模型选择器前的胶囊显示当前所用 Key 的两个窗口。仅支持 minimax 与 minimax-cn 路由。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-18
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
