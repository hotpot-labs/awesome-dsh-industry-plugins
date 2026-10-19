# JoblessJoe/dsh-restart-anywhere

- **仓库地址**: https://github.com/JoblessJoe/dsh-restart-anywhere
- **收录分类**: 计算机
- **插件简介**: 在「设置」上方添加「重启 dsh」按钮，原地重启：以 systemd 单元运行时由 systemd 重启，否则通过 process.execve 保持同一 PID（Windows 或 Node < 22.15 时保留一个轻量父进程），启动 dsh 的守护进程或终端无需额外配置（已在 Linux 实测，Docker、macOS、Windows 尚未实机测试）；新 boot id 响应后页面自动刷新。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-19
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
