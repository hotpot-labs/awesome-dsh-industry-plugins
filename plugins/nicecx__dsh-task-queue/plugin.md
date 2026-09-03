# nicecx/dsh-task-queue

- **仓库地址**: https://github.com/nicecx/dsh-task-queue
- **收录分类**: 计算机
- **插件简介**: DSH↔Hermes 协作的缓存梯队任务队列（reset > approve > review，queue.json 唯一真相源）：全部提审路径入队、租约/认领模型并发 1、优先级 aging 防饿死、原子忙锁；Hermes 侧消费端（cron */1 + monitor 门控）出队执行、单槽检查写审核请求、调用重置 agent。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-03
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
