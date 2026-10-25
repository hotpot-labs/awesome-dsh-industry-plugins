# Alterssss/dsh-bili-whale

- **仓库地址**: https://github.com/Alterssss/dsh-bili-whale
- **收录分类**: 其他
- **插件简介**: 一条按自己作息过日子的 B 站插件：宿主里每 60 秒一次心跳，在设定的作息窗口里随机挑一个时刻叫醒专用会话（今天不想看是按概率跳过），再交给自带的 38 个子命令——信息流、字幕、弹幕、评论、ffmpeg 抽帧、两本日记。每天最多发 N 条评论/动态并 @ 主人（默认 3，按配额账本计数，撞到限流或验证码就停手）。同时轮询评论回复、私信和直播间弹幕；除主人以外的回复先入队，等主人在设置页批准。设置 → 养鱼 写 ~/.dsh/bili-whale.config.json；cookie 单独在 ~/.bili-ai/credentials.json，只写不回显。HTTP 路由只认回环地址并过 DSH 信任栅栏。抽帧需要 Node 18+ 与 ffmpeg。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-25
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
