# MingTXin/dsh-remote-workstation

- **仓库地址**: https://github.com/MingTXin/dsh-remote-workstation
- **收录分类**: 其他
- **插件简介**: 给 DeepSeek Harness 用的远程工作区：在侧栏选 SSH 主机，通过 SFTP 把服务器目录挂载成工作区，随后用普通文件工具直接读写远端文件；远端 watch 用轮询实现（文件树自动刷新），图片/二进制预览走字节区间读取，remote_exec / remote_search / remote_git 分别提供远端命令、搜索与 git 查询；可选补丁把 agent 自己的 bash/pwsh 命令也路由到服务器；远端写入与命令都遵循会话的 sandbox 模式与审批策略；主机凭据由插件自带的「主机」库维护（密码、私钥或 SSH agent）。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-29
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
