# apex-mochen/dsh-todo-continuity

- **仓库地址**: https://github.com/apex-mochen/dsh-todo-continuity
- **收录分类**: 其他
- **插件简介**: 让没做完的任务清单跨回合保留。DSH 在每个回合开始时清空 todos 投影，指望模型重写整份清单，于是回合一旦被中断，计划虽然durable 地留在会话日志里，界面上却永久消失——而 todo_write 只写不读，用户和模型都拿不回来。本插件只注册一个普通的 session/event 监听器，按会话记住最后一份清单；当 turn/start 到来而那份清单仍有未完成项时，把它补折回去，投影就不再显示空计划。不 fork tool-todo、不注册任何 waterfall：插件换不掉投影（注册表对 stateVersion 不一致直接抛错），追加折叠所反应的那条事件才是够得着的缝。刻意收得很窄——只管未完成的清单、每次回合开始最多补一条、失败即放行。已用真实会话上的受控 A/B 验证：两次运行内容相同，唯一差别是插件装没装，都用真实的投影定义折叠。零依赖。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-17
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
