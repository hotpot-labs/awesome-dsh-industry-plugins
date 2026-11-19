# DanceElephant/dsh-codex-skill-bridge

- **仓库地址**: https://github.com/DanceElephant/dsh-codex-skill-bridge
- **收录分类**: 其他
- **插件简介**: 把本机 Codex 已装的 skills，一条命令搬进 DeepSeek Harness —— 这个插件就是那座桥。装一次之后：DSH 里能直接扫描、检视、导入这些 skills，导入过的技能会出现在 DSH 的 skill 列表里，和原生 skill 一样被模型按需加载；导入的描述会按 DSH 提示词预算压缩好（默认 220 字符），不会把上下文撑爆；上游改了、删了能一条命令查出来；不想用了也能干净地撤掉。它自己不执行任何被导入的 skill：脚本只是被列出来给你看，正文只是被读取和登记。六个工具 + 一个 CLI，零运行时依赖，无需构建，Node.js 20 或更新。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-19
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
