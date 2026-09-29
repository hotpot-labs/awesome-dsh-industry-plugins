# HapyRain/dsh-router-laya

- **仓库地址**: https://github.com/HapyRain/dsh-router-laya
- **收录分类**: 其他
- **插件简介**: 为 DeepSeek Harness 提供自动思考档位路由：本地微调的 7 题分类模型（ModernBERT，842MB，CPU 推理 <1s）对无档位指令的消息自动选择 low/high/max；会话内检测到重试自动沿阶梯升档，受「别用 max」类排除约束压制；判定服务不可达时熔断降级，会话不断。前端档位芯片实时显示当前档位与最近 20 轮判断原因。判定全程本地推理，任务文本不出本机。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-29
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
