# Destinhue/dsh-video-vision

- **仓库地址**: https://github.com/Destinhue/dsh-video-vision
- **收录分类**: 其他
- **插件简介**: 四个把视频当原料而不是当节目看的工具：video_probe 返回元数据与阅读计划，不解码画面；video_storyboard 把一个时间窗口压成一张分镜图，再给一份文本索引，把每一格绑到它的时间码、切点数与取帧时刻；video_zoom 把短窗口里的 1-9 格按更大尺寸重画；video_read 只解关键帧，用 Windows 自带的 OCR 引擎逐屏识字，返回大纲与 [mm:ss] 正文——讲课、幻灯片、录屏走这条，因为字才是内容。切点、叠化与单帧闪光由一次 ffmpeg 扫描得出，格子编号以位图写在图上，字幕按落在哪一格就写在哪一格。需要 ffmpeg，有 ffprobe 时会用，除此之外无运行时依赖。它与 SAOS-3624/dsh-video-storyboard 接口兼容，注册同名的 video_probe / video_storyboard / video_zoom 三个工具，两者不能同装。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-30
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
