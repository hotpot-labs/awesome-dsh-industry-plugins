# Ma354/dsh-limit-break

- **仓库地址**: https://github.com/Ma354/dsh-limit-break
- **收录分类**: 其他
- **插件简介**: 跨会话持久记忆，加一条绕开主机名级封锁的取数阶梯：四个工具——memory_recall / memory_save / memory_stats 读写 $DSH_HOME/memory/facts.json 里的纯 JSON，resilient_fetch 依次尝试直连 fetch → 同服务别名主机（目前仅 Wikipedia）→ curl IPv6 → curl IPv4（curl 需在 PATH 上）。无后台进程、无 npm 依赖、导入期不联网。（1.3.0 曾加入第五个工具 memory_prune，已在 1.4.0 撤下：给运行中的插件加工具，会让此前打开的会话报错。）
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-25
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
