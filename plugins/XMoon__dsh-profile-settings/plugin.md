# XMoon/dsh-profile-settings

- **仓库地址**: https://github.com/XMoon/dsh-profile-settings
- **收录分类**: 其他
- **插件简介**: 为 DeepSeek Harness 提供按 profile 分层的设置覆盖：全局 settings.yaml 仍为基线，每个 profile 可用自己的 profiles/<name>/settings.patch.yml 覆盖任意设置命名空间——对象段递归合并，数组与标量整体替换，!unset 显式屏蔽继承值。覆盖层对现有插件透明（照常读 ctx.settings），写入只落在 profile 覆盖层；官方 schema 语义、revision、expectedRevision 冲突检测、watcher 与事件均不改动。附带 settings 命令族（get/set/unset/mask/unmask/promote/demote/migrate/diff/layers），并在 Web 设置面板经 loopback RPC 通道提供 Profile Settings 区块。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-08-26
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
