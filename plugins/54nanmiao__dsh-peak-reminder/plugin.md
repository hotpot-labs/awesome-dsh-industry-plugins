# 54nanmiao/dsh-peak-reminder

- **仓库地址**: https://github.com/54nanmiao/dsh-peak-reminder
- **收录分类**: 其他
- **插件简介**: 峰时提醒：DeepSeek 走高峰计价时，每隔 N 分钟（默认 5，可设 1–120）在 DSH Web 界面顶部提醒一次「现在是峰时」，峰↔谷切换各提醒一条，谷时完全不打扰；侧边栏底部常驻一行显示当前峰/谷状态与下次切换倒计时。峰谷规则（北京时间工作日 09:00–12:00、14:00–18:00；周末、法定节假日与调休周末全天谷价）由宿主判定，经 /plugins/dsh-peak-reminder/state 与 /config 两个免鉴权路由供界面读取；开关与间隔在设置页一节里改，存到 ~/.dsh/peak-reminder.json。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-25
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
