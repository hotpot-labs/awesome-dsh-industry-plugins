# 1997liuyh-boop/dsh-desktop-tools

- **仓库地址**: https://github.com/1997liuyh-boop/dsh-desktop-tools
- **收录分类**: 其他
- **插件简介**: 为 DSH 桌面端提供划词工具栏、悬浮球，以及通过全局快捷键唤起、在屏幕顶部工具栏切换的截图、长截图和录屏，每项功能独立设置。截图支持形状、画笔、箭头、文本与序号、马赛克、钉在桌面、保存，以及转发到 DSH 对话或系统分享面板（Windows 和 macOS）；录屏可录制区域、窗口或全屏，输出 MP4、GIF 或 WebM，可选录制系统声音和麦克风。截图的提取文字、翻译和知识图谱使用 dsh-vision-router 的 OCR 工具，该插件需另行安装（设置页提供一键安装）。需要 DSH Desktop >=0.2.2-rc.1 <0.3.0-0。各项功能运行在单独的 Electron 辅助进程中，插件不会下载 Electron：安装版 DSH Desktop 需另备独立 Electron，可通过插件设置 electronExecutable、环境变量 DSH_DESKTOP_TOOLS_ELECTRON 或 $DSH_HOME/electron/ 提供；由裸 Electron 启动的 DSH Desktop 会直接复用它。Linux 不支持录制系统声音。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-13
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
