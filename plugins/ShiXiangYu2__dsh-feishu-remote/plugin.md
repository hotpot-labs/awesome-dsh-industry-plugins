# ShiXiangYu2/dsh-feishu-remote

- **仓库地址**: https://github.com/ShiXiangYu2/dsh-feishu-remote
- **收录分类**: 其他
- **插件简介**: 从飞书/Lark 操作 DeepSeek Harness：私聊发送任务，agent 用你配置的模型执行并把结果回到会话；feishu_send 工具可让 agent 主动推送结果。基于 lark-cli 的 WebSocket 长连接，无需公网 webhook，并附常驻启动器。注意：插件不校验发送者身份，因此任何能私聊到该机器人的人（默认即该飞书应用所属企业内的成员）都能驱动一个使用宿主机自身模型凭据与文件权限运行的 agent。安装不是一条 `dsh plugin add` 就完事：需要先全局安装并登录一次 `lark-cli`，并在飞书开放平台建一个带 README 所列权限的自建应用。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-08
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
