# GaoHu1997/dsh-webdav

- **仓库地址**: https://github.com/GaoHu1997/dsh-webdav
- **收录分类**: 计算机
- **插件简介**: 通过任意 WebDAV 服务让一台机器上的 DSH profile 与其他机器保持一致。插件收集构成一套配置的五份内容——models（cordis.patch.yml 里的 llm-pi-ai 行）、defaults（agent-default-model 行）、patch（其余 loader 行）、plugins（package.json 的 dependencies 加 dsh.profile.bundles）与 dirs（在面板里挑选的 profile 之外绝对路径目录，连文件整体携带、恢复时写回同一路径，只增不减，最多 5 个、每个 2000 个文件 / 8 MiB）——在本机用口令加密（AES-256-GCM，PBKDF2-SHA256 600000 轮）后上传，服务器上只有一份密文文件 <address>/dsh-webdav/dsh-profile.prop（旧文件名 dsh-profile.dshsync 仍只读识别）。合并按份进行，并与上次同步的基线做三方合并；冲突时保留较新的一份，另一份留档到 sync/（每个 tag 保留最新 5 份），每次覆盖前先封存；删除会传播，但 plugins 份、首次同步与 dirs 份例外——在某一台机器上去掉一个附加目录只是这台不再同步它，里面的文件永不删除。上传带 ETag 的 If-Match 与 If-None-Match，并发改动会被拒绝而不是被覆盖。可从设置面板手动同步，或按 3/15/30/60 分钟定时；可选的本机转发（默认关闭，仅监听 127.0.0.1）用本机生成的账号把同一个目标重新对外提供，并重写 PROPFIND href、给无扩展名资源补 .prop 别名。本机状态在 <profileDir>/.dsh-webdav-sync/ 下（sync.json 以 0600 写入，存 WebDAV 密码与口令）。
- **收录来源**: awesome-dsh-plugin
- **审核日期**: 2026-10-23
- **审核定级**: 🔴 黑名单 (禁止使用)

完整审核报告见同目录 [security-report.md](./security-report.md)。

> ⚠️ 自动审核不等于人工审计，报告中标注「需人工复核」的检查项以人工复核结论为准。
