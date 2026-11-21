# 3309602454/dsh-edge-pilot

- **仓库地址**: https://github.com/3309602454/dsh-edge-pilot
- **收录分类**: 其他
- **插件简介**: 用 playwright-core 直接驱动 Windows 上已装好的 Microsoft Edge，不下载 Chromium。插件把页面编译成带编号的 ref 清单（e1、e2……），模型只需回一个 ref 而不必写 CSS 选择器；点击会先滚入视口、检测遮挡，点完再比对地址与正文确认是否真的生效。还能重放保存好的技能文件（JSON 步骤表 + {{参数}} 替换，不含 ref），固化流程一次调用跑完；并防止标签页越攒越多——启动前清理会话还原文件、限制标签数量、空闲自动回收、退出前统一关闭。另附 ChatGPT 网页版工具（问答、生图、GIF），走独立 profile。仅限 Windows。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-21
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
