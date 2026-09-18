# apex-mochen/dsh-sandbox-arg-guard

- **仓库地址**: https://github.com/apex-mochen/dsh-sandbox-arg-guard
- **收录分类**: 其他
- **插件简介**: 让「同级或更窄的 sandbox_permissions」不再让工具调用直接失败。会升级的工具（pwsh、bash、write、edit）都广告完整的 sandbox_permissions 枚举，但 DSH 只接受严格更宽于当前生效级别的请求——其源码自称这是「deliberately not a schema constraint」。于是反射式带上该参数的模型往往填它已经在的那个级别，调用在执行前就死掉："sandbox escalation to \"workspace-write\" is not strictly wider than this call's current \"workspace-write\" mode"，某些模型还会为此烧掉一整轮重试。本插件只注册一个 tools/execute waterfall 监听器，且仅在那一条文档化拒绝上、且参数里确实带了升级字段时，把同一个调用去掉该参数重投一次。安全性由 DSH 自己的文档保证：拒绝发生在任何执行之前（"nothing has run"），且改过的参数无法再次匹配，因此重投在结构上不成环。已端到端复现并验证——改造前 isError 为 true 且命令从未执行；改造后拿到命令的真实输出、isError 为 false，会话里只有一个 tool/call 与一个 tool/result。零依赖。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-09-18
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
