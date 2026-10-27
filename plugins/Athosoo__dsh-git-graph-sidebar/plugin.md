# Athosoo/dsh-git-graph-sidebar

- **仓库地址**: https://github.com/Athosoo/dsh-git-graph-sidebar
- **收录分类**: 其他
- **插件简介**: 给 dsh-better-sidebar 用的仓库图谱页，分叉自 @linxin666/dsh-client-ui-git-graph 0.4.8（上游开发仓库为 zhu1090093659/dsh-web）。两者都占用 /git 路由前缀，不能同时安装，只能二选一。它会发现工作区目录往下三层以内的 Git 仓库（最多 200 个，跳过 node_modules、dist、build、out、coverage、target、vendor 与点目录），按树状列出并显示分支、head、脏文件数与冲突数，把选中仓库的提交图渲染成 SVG 泳道画布（跨泳道曲线、合并菱形、ref 徽章、行缩放与可固定的提交详情卡）。它会写入仓库：「初始化 Git 仓库」按钮会执行 git init，规范选择器会把 GIT_CONVENTIONS.md 写进仓库（或写一份工作区级的 .dsh/GIT_CONVENTIONS.md 供子仓库继承），内容来自六套框架——约定式提交、GitHub Flow、Git Flow、主干开发、约定式分支、GitLab Flow。host 会在每个模型步骤前把该文档注入 system prompt，并按文档自己声明的规则标出最近 20 个提交里不符合的那些；中文、英文与中英混排的标题都接受，可选的强约束模式会写入 strict: true。同时保留了上游插件的输入框分支徽章、交互式提交图对话框与 worktree 管理器。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-27
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
