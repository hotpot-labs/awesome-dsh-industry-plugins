# 27painter/dsh-nx

- **仓库地址**: https://github.com/27painter/dsh-nx
- **收录分类**: 其他
- **插件简介**: 从 DeepSeek Harness 驱动 Siemens NX 2406 与 2506，也支持 NX 12：一个按日志而非退出码判定 journal 成败的执行器（NX 对吞掉异常的 journal 返回 0，干净结束时返回 0xC0000409）、常驻批处理 NX 上的 16 个类型化工具，以及一个能分清三个版本的探测。仅 Windows；以 NX 2406 为基准版本，2506 为预期可用。需本机已安装 Siemens NX 并有一个空闲的 NX 许可席位；先运行一次 `dsh-nx install`；16 个 MCP 工具默认关闭，需设 `NX_ENABLE_MCP=1` 才注册（技能路线不受影响）。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-03
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
