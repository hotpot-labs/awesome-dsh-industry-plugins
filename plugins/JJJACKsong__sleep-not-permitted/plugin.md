# JJJACKsong/sleep-not-permitted

- **仓库地址**: https://github.com/JJJACKsong/sleep-not-permitted
- **收录分类**: 其他
- **插件简介**: 禁止 Agent 前台等待：sleep / wait / tail -f / watch / ping 等等待型命令、wait_agent 与 job_output(wait) 等阻塞等待工具，用反复 check 代替等待的轮询（同一条命令在窗口内重复出现），以及需要人输入/确认的命令（sudo 不加 -n、ssh 不开 BatchMode、登录流程、交互式编辑器、docker -it）都会被拒绝，并给出改用后台作业或结束本轮等唤醒的可执行指令；等待预算与轮询窗口可配、文案跟随系统语言（中/英）、零运行时依赖。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-31
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
