# Geng-zy/aurabot-qq-mac

- **仓库地址**: https://github.com/Geng-zy/aurabot-qq-mac
- **收录分类**: 其他
- **插件简介**: 把 aureth-labs/dsh-aurabot-qq 移植到 macOS（Apple 芯片）的分叉：同样是住进 QQ 的人设机器人（聊天、语音条、表情包、记忆、翻唱、模块），删掉了 Windows 专用代码。接 OrbStack 或 Docker 里的 SnowLuma 等 OneBot v11 网关，语音兜底用 macOS 自带的 say，超过 30 MB 的文件通过只对本机开放的临时下载口发给容器里的网关，翻唱环境（Applio、audio-separator、uv、Rubber Band、分离模型）按固定版本一键安装。与上游同包名、同插件 id（dsh-aurabot-qq），安装即替换上游，不能与上游同装；Windows 请用上游。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-10
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
