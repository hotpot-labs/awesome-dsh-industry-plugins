# DanceElephant/dsh-codex-bridge

- **仓库地址**: https://github.com/DanceElephant/dsh-codex-bridge
- **收录分类**: 其他
- **插件简介**: 把本机 Codex 的技能导入 DSH 技能目录，且不执行其中代码：扫描 ~/.codex/skills 与插件缓存，按引用或快照两种方式登记（快照会改写副本正文里写死的 Codex 主目录路径，并保留上游 LICENSE/NOTICE），超长描述默认压到 220 字符预算，导入项记在原子锁文件里并在 DSH 启动时重放。同样六个操作以 codex_scan、codex_inspect、codex_import、codex_list、codex_remove、codex_doctor 工具和 bridge CLI 提供；零运行时依赖、无构建步骤，Node.js 20 或更新。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-17
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
