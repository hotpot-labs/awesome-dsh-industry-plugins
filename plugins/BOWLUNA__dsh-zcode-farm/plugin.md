# BOWLUNA/dsh-zcode-farm

- **仓库地址**: https://github.com/BOWLUNA/dsh-zcode-farm
- **收录分类**: 其他
- **插件简介**: 多实例 ComfyUI 编排：探测每个已配置 ComfyUI 端点的 GPU、空闲显存与队列深度，再把生成任务派给最空闲且满足条件的实例。提供三个工具（comfyui_farm_status、comfyui_farm_pick、comfyui_farm_run）。一个实例只有在可达、空闲显存不低于要求、且队列不深于上限时才算候选；候选按「空闲显存 － 队列深 × 权重」排序，因此空闲的浅队列胜过忙碌的大显存。零运行时依赖。探测失败可选重试——跨 SSH 隧道的一次超时不足以证明实例已下线。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-22
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
