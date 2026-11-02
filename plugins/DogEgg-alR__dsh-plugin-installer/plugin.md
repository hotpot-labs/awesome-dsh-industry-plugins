# DogEgg-alR/dsh-plugin-installer

- **仓库地址**: https://github.com/DogEgg-alR/dsh-plugin-installer
- **收录分类**: 其他
- **插件简介**: 在插件页的一个标签里安装、更新和卸载 DSH 插件。安装直接调用 profile 进程内的 pluginManager 服务，因此桌面端运行中也能装，不必只靠命令行。更新委托给 dsh-market 的公开 update API v1（该区需要装 dsh-market），把市场报告的阶段、百分比与已下载字节显示成进度条，市场提供恢复点时给出一键回滚。卸载被「插件正在使用中」拒绝时，先停用该组合包，再从 profile 清单里摘除，并把残留文件记入 profile 下的待清理队列，下次启动后自动清扫。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-02
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
