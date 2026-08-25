# qinyre/dsh-plugin-install

- **仓库地址**: https://github.com/qinyre/dsh-plugin-install
- **收录分类**: 其他
- **插件简介**: 设置 → 插件里的「安装」标签页：按 npm spec、`github:user/repo` 或本地路径安装、更新、卸载任意插件，走的都是 `dsh plugin add` 这条 CLI 路径；更新检查对照 npm latest 或 GitHub HEAD，带降级保护与装后版本核对，每次 add/remove 均附带 pnpm 11 发布冷静期豁免；服务重启在 DSH Desktop 由壳层执行，独立 `dsh web` 下由中转进程接力并交接回原终端。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-08-25
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
