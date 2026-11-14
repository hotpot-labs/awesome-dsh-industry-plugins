# Azerz/dsh-video-insight

- **仓库地址**: https://github.com/Azerz/dsh-video-insight
- **收录分类**: 其他
- **插件简介**: DeepSeek Harness 侧边栏的视频解析面板。粘贴 YouTube / 哔哩哔哩链接即可抓取字幕，生成总结、章节、思维导图，以及带「依据」时间戳的转写稿问答；内置播放器，点时间戳会跳到对应位置并继续播放。没有字幕时用本机 Whisper / SenseVoice 转写兜底（音频不出本机），纯无声视频则用 macOS Vision 做画面文字识别，或让视觉模型描述画面。按视频缓存分析结果、保留最近 20 条历史，并注册 video_digest、video 两个 agent 工具。如果填了 B 站 SESSDATA Cookie，会保存在 ~/.dsh/video-credentials.json（权限 0600）；文字稿会发给当前模型；它的 HTTP 路由没有 DSH 的访问检查。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-14
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
