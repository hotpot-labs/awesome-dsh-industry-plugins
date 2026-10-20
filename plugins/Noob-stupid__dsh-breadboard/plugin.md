# Noob-stupid/dsh-breadboard

- **仓库地址**: https://github.com/Noob-stupid/dsh-breadboard
- **收录分类**: 其他
- **插件简介**: DSH 嵌入式硬件沙盒插件：在 3D 面包板场景里摆放 ESP32 / BME280 / PIR / LED 等器件、按协议与电压校验接线；让真实 Python 项目代码在环运行、经 Python shim 读虚拟 I2C/GPIO 的寄存器级读数，支持故障注入（断线 / NACK / busy / 强制读数）；联网设备模拟器可向真实 HTTP 后端周期上报（已在真实"智能选座"系统全链路验证）；还可只读观察真机状态，并用数据驱动的型号定义支持新硬件。随插件带 16 个 hw_* 工具与一份 SKILL.md。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-20
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
