# 01men/DeptAI-UI-DSH

- **仓库地址**: https://github.com/01men/DeptAI-UI-DSH
- **收录分类**: 其他
- **插件简介**: AI 代理与人类的协作前台——部门看板、工单、审批与行业计算都在 DSH 会话与面板里完成，代理在对话里干活，人在面板里负责。它通过既有契约调用 01men/ybkkasi 治理底座（资产台账、IAM、OIDC SSO、RBAC 与场景级授权），不重复实现治理。以 Cordis bundle 形式安装，挂载在 /gate01；自测套件每次推送全绿。请勿在同一 profile 同时安装本插件与 01men/ybkkasi 的 dsh bundle：两者都会注册 ops-platform-core / ops-iam / ops-authn 行。要求 DSH >=0.1.0-rc.7 <0.2.0。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-11-01
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
