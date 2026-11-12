# BeastyZ/dsh-remote-agent

- **仓库地址**: https://github.com/BeastyZ/dsh-remote-agent
- **收录分类**: 其他
- **插件简介**: 连接 Linux 服务器的 Agent 工作台，支持持久会话、远程终端、文件编辑、Git worktree 和端口转发。通过本机 OpenSSH 客户端（macOS/Linux；远端为带 GNU coreutils 的 Linux，tmux 可选）在 ~/.ssh/config 里的任意主机上执行命令、编辑文件、做端口转发，主机密钥检查默认 accept-new；每个终端最近 512K 字符的输出会存到 ~/.dsh/remote-agent/terminals。与 zbzbhs/dsh-remote-agent 同包名、同挂载 id，两者同装会冲突。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-12
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
