# ECCVIK/lmtagent

- **仓库地址**: https://github.com/ECCVIK/lmtagent
- **收录分类**: 其他
- **插件简介**: 软件研发与安全审计多智能体工作流：内置 8 个角色预设（Captain 主控与 CEO、Designer、Eng Manager、Reviewer/CSO、Builder、QA Lead、Release 七个执行预设）、默认 6 并发槽（1-12 可调）的 4-Wave DAG 调度、PostgreSQL Wire v3 与 SQLite WAL 双模事实库、29 个随包技能及右侧常驻 Web 控制台。是 Jueze-2019/dsh-redteam-mode 的分支，沿用其包名、挂载 id 与 redteam_* 工具名，不能与原版同时安装。环境变量里设了 REDTEAM_PG_URL、DSH_PG_URL、DATABASE_URL 或 PGHOST 时事实库用 PostgreSQL，否则用 $DSH_HOME/redteam 下的本地 SQLite；角色预设写入 $DSH_HOME/.agent-presets/redteam。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-11
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
