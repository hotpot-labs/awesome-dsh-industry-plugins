# DSH 插件安全自动化校验报告

- **校验对象**: https://github.com/Yang-wudi/dsh-video-gen
- **校验时间**: 2026-08-30 04:30:11
- **校验方式**: 自动化静态分析 + GitHub API

## 检查结果统计

| 类型 | 总数 | 通过 | 需人工复核 | 不通过 |
| :--- | :---: | :---: | :---: | :---: |
| 🔴 必查 | 33 | 12 | 12 | 9 |
| 🟡 推荐 | 14 | 8 | 6 | 0 |

## 自动判定结果

> 🔴 **该插件存在必查项不通过, 自动判定为黑名单 (禁止使用)**


## 一、基础准入审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 1.1 | 源码托管于公开可追溯平台 | 必查 | ✅ 通过 | ✅ 仓库公开; 默认分支: main |
| 1.2 | 发布账号非匿名一次性账号 | 必查 | ✅ 通过 | 账号注册: 2024-12-10 (628 天前); 公开仓库数: 10; 粉丝数: 0 |
| 1.3 | 开源协议与 MIT 兼容 | 必查 | ✅ 通过 | 许可证: MIT (来自 LICENSE) |
| 1.4 | 核心功能与 README 描述一致 | 必查 | ✅ 通过 | README 字数: 1011; 包名: dsh-video-gen; 描述: Bring text-to-video and image-to-video generation to DeepSeek Harness — DashScop — README 包含功能/使用说明 |
| 1.5 | 不违反法律法规 | 必查 | ❌ 不通过 | 检测到潜在违规模式:<br>  - .pnpm-store/v3/files/2a/bfe86e5f589621ab83f10f51549b0aad027153d838c05b078f8c7d62f827b517cff6e4fc34913dd1995fbd71fd2026350d5a46c187292dfa23bfc6ec771a55:1 → 破解授权 (1 处)<br>  - .pnpm-store/v3/files/0e/d5f6e7c44346dcc478b756b10ab4680608ff84fdc1dac3a88cc06ef79f4492e75764b1b1ca9f62140c8b4fc094a58a7b98c0c7eb6a11599ba05fba7216c95e:24 → 破解授权 (2 处)<br>  - .pnpm-store/v3/files/23/865d1430c0a63d9a9e90fb4c1d3744e3b4e2447cb72860bbf7eb89a0004171b04b5d1e08ee84632b57f3e9102f96946f54bc10cf3ed88ef363d320fccdb275:2793 → 破解授权 (2 处)<br>  - .pnpm-store/v3/files/4d/b7ad8f5b41a9098541dd4caa877531c04d74c39a3c0ca40f3c78ffb480345b0af5a32740d6d845ed14c34abbb417185188a1949162e008e2ef6e67ecaf88a5:22 → 破解授权 (2 处)<br>  - .pnpm-store/v3/files/dc/d50f648a5a6525e93f4dd01456380273a1c9c63f374f082030a0a41aa67f9c1d553e6cc4cacaf30bbcd805880dc004bb6bdbcc57d0a5049e9f024c41656fa4:20 → 破解授权 (1 处)<br>  ... 共 65 处 |
| 1.6 | 有明确的版本号与正式 Release | 推荐 | ✅ 通过 | Git tags (1): v0.2.1; package.json version: 0.2.1; GitHub Releases (1): v0.2.1 |


## 二、技术规范审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 2.1 | 明确标注支持的 DSH 版本范围 | 必查 | ✅ 通过 | @deepseek-ai/cordis: >=4.0.0 <5; @deepseek-ai/dsh-credentials: >=0.1.0-rc.5 <0.2.0; @deepseek-ai/dsh-host-webserver: >=0.1.0-rc.5 <0.2.0; @deepseek-ai/dsh-settings: >=0.1.0-rc.5 <0.2.0; @deepseek-ai/dsh-tools: >=0.1.0-rc.5 <0.2.0 |
| 2.2 | 遵循 Cordis 插件开发规范 | 必查 | ⚠️  需人工复核 | dsh 配置: {"bundle": {"patch": "./cordis.patch.yml"}, "client": {"inject": ["@deepseek-ai/dsh-client-connectio; Cordis/DSH 依赖: @deepseek-ai/cordis, @deepseek-ai/dsh-credentials, @deepseek-ai/dsh-host-webserver, @deepseek-ai/dsh-settings, @deepseek-ai/dsh-tools; Cordis 配置文件: cordis.patch.yml<br>  - .pnpm-store/v3/files/61/c3d2f13f2caff87d1c1859b8b883bddc4c4a0b9579b6e0928a27866b3afd9009aba27ec6b9e85e48d4f85ae7e280b727bb95d51efbc42d6880b4962bf2c25d:62 → Monkey patch / prototype pollution<br>  - .pnpm-store/v3/files/72/b7cbb02ddc88cb0e7eda9b6b911f4d89ad6516c6044e8cc581de96762107a7570dd68a24eaebf409b74c9ed852004a635cbffc764b95dc47ccc8ff52d0c835:801 → Monkey patch / prototype pollution<br>  - .pnpm-store/v3/files/c0/cc6c473afb873b0b6f31e39cad992a33b481d875ea4732a5d6e7a222db7ae09879df912e15b824969c2b876055970178c30276c9461e0137f0e787ed01e070:40 → Monkey patch / prototype pollution — 发现潜在 hack 模式, 需人工确认 |
| 2.3 | 具备异常捕获机制 | 必查 | ✅ 通过 | try/catch: 104 处, 函数: 336 个, 比例: 31.0% |
| 2.4 | 卸载后完整释放资源 | 必查 | ✅ 通过 | 发现清理逻辑: tests/client-bundle.test.mjs |
| 2.5 | 初始化耗时 ≤ 500ms | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.6 | 空闲内存 ≤ 50MB, 无异常 CPU | 推荐 | ⚠️  需人工复核 | 静态分析无法测量, 需在运行环境中实测 |
| 2.7 | 与官方/主流插件无功能冲突 | 推荐 | ⚠️  需人工复核 | 需人工比对 DSH 官方插件及主流社区插件 |


## 三、权限安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 3.1 | 文件系统权限最小化 | 必查 | ❌ 不通过 | 检测到敏感路径访问:<br>  - .pnpm-store/v3/files/53/47a16b7e802653b35afbeb69e61be55f95987ad1bc2b259d3694cd440d6959926dd62b993616dc2ccec97a9386adb7be4b06967c0225e5dfc6b81898c75ef9:72 → 读取环境变量配置 (1 处)<br>  - .pnpm-store/v3/files/53/45986bee2cc4c2a0d56f116341b363897dfe3fe5f7e018a0d4d293a7f52920415000c98630feed2ada143483a3b3b3fe8fda68736e74fa727d86bf9c783346:9512 → 读取环境变量配置 (16 处)<br>  - .pnpm-store/v3/files/72/bbe05d3b4ce73f12bf9843917f2050a5a7c870c41f3c04db3a616f02aa6f73b95f027d89214d68b33ed0a9a259d6de63fa4291dcbf748fb818c46159fd0d52:4 → 读取环境变量配置 (1 处)<br>  - .pnpm-store/v3/files/72/b7cbb02ddc88cb0e7eda9b6b911f4d89ad6516c6044e8cc581de96762107a7570dd68a24eaebf409b74c9ed852004a635cbffc764b95dc47ccc8ff52d0c835:24 → 读取环境变量配置 (6 处)<br>  - .pnpm-store/v3/files/1b/953240b7234bb2935e599470db6594a5bf396513da558dab17249936268eb2a70429c7035b8a52242b9604fbfbdfd6af226d8daa842005d25b2ce2216d2470:660 → 读取环境变量配置 (2 处)<br>  ... 共 193 处 |
| 3.2 | 无全局文件读写 | 必查 | ⚠️  需人工复核 | 检测到全局文件访问:<br>  - .pnpm-store/v3/files/53/ca2ec01b0edd94aebef2952e60b07343bb799c1c1f224e082f1443a12c36ef1d7dd76eb7818c05016e4fffdb5615c6abfff49ae2d8485e3a89506b722835ec:9 → 深层目录穿越 (1 处)<br>  - .pnpm-store/v3/files/53/ac70b7017e94b72322363f3785be7c22c1c9b1d1d4553475a556d0eab5c560c3561850a52dba7a26eb3be28d55d94367146a19549112468e3d0a257b60ef38:5 → 深层目录穿越 (1 处)<br>  - .pnpm-store/v3/files/53/10d9d2bdaefac8682e99ed8051b01d8a1780045b9ae54ddcbbd682f39841964a1aefc5d7f69f2f3e26c5b832afe300d1c1c6c383492a38a36ad9d7d7b39f31:1 → 深层目录穿越 (1 处)<br>  - .pnpm-store/v3/files/61/c3d2f13f2caff87d1c1859b8b883bddc4c4a0b9579b6e0928a27866b3afd9009aba27ec6b9e85e48d4f85ae7e280b727bb95d51efbc42d6880b4962bf2c25d:2745 → 深层目录穿越 (2 处)<br>  - .pnpm-store/v3/files/2a/5055d0f2bd218ed3549bac1032d3d169a5b634b74015884b3e39435907e40b28eb4047a4052f497f4370023fc88a64617b00f44c813b5de449ee0be4a4479f:3 → 深层目录穿越 (6 处)<br>  ... 共 297 处 — 需人工判断是否有业务必要性 |
| 3.3 | 无无限制系统命令执行 | 必查 | ⚠️  需人工复核 | 检测到命令执行:<br>  - .pnpm-store/v3/files/c0/e2ca284adb5d513fa4688e7e98c79bc8e2fb85ee9d77d7111b258f848b89eadbc2cc88419f4cf1b887cf1683b7260c80507389428d7722ca3d5d36549087c5:11144 → 加载 child_process (3 处)<br>  - .pnpm-store/v3/files/c0/e2ca284adb5d513fa4688e7e98c79bc8e2fb85ee9d77d7111b258f848b89eadbc2cc88419f4cf1b887cf1683b7260c80507389428d7722ca3d5d36549087c5:13090 → 进程执行 (1 处)<br>  - .pnpm-store/v3/files/23/5855b7308db233f8ec8853c13b3527668c72de6f0eddd23663c41532c47e5190f28f7e2d4a9f0b6839ef8e1a269d36a61ccbacc25ad61dc6e832496692252f:43 → 加载 child_process (1 处)<br>  - .pnpm-store/v3/files/d1/29222c3f531e56958b9e1c9bd7bff2e7aa8be9dd55d3860c07764128c69f0df623bb30735e17e5816cdd5b5c409627fb23db67f8831934e62f5224fde42c92-exec:3 → 加载 child_process (1 处)<br>  - .pnpm-store/v3/files/30/5a6d5f347fb13a3a2dc008212cfeacae89cc91bc59af3e0b277a8d10a6e60bc6fd0f8582e04029ce918d050a19cf0480e69ce400a9820e57bc013fe8a0ca47:50 → 加载 child_process (1 处)<br>  ... 共 17 处<br>⚠️ 检测到可能存在命令白名单机制, 需人工确认 |
| 3.4 | 无命令注入风险 | 必查 | ❌ 不通过 | 检测到命令注入风险:<br>  - .pnpm-store/v3/files/c0/e2ca284adb5d513fa4688e7e98c79bc8e2fb85ee9d77d7111b258f848b89eadbc2cc88419f4cf1b887cf1683b7260c80507389428d7722ca3d5d36549087c5:26780 → 命令字符串拼接变量 (注入风险) (1 处)<br>  - .pnpm-store/v3/files/c0/e2ca284adb5d513fa4688e7e98c79bc8e2fb85ee9d77d7111b258f848b89eadbc2cc88419f4cf1b887cf1683b7260c80507389428d7722ca3d5d36549087c5:11378 → 开启 shell 模式 (注入风险) (1 处)<br>  - .pnpm-store/v3/files/c4/6a2a60af0d573eee8f51cf0883463e72d763b42ad3dee916125aa73d29bde59e818f6d7c44fb6983d74ad4516e2e3ffc8189041f0e7dba791e3fdfcef68b3c:167 → 开启 shell 模式 (注入风险) (1 处)<br>  - .pnpm-store/v3/files/84/2cf1d03eaa8e9c9e56ae03b89b67e0a1e6610b3b14638dd17754f3c10aa7057feb15f72d9d3d03c079ee82b11837ef856dac79f73558b92f646dd660ddf7e1:324 → 命令字符串拼接变量 (注入风险) (1 处)<br>  - .pnpm-store/v3/files/67/7bba0093501bf5fe5377bc4de6a64fa1532e0bdb4fcb684471cd212ec06b7b2711f1113c52f5f5964c8d1a3fb28a53ad5d2793aed79f075b0f1ba8d923552b:4 → exec 命令拼接 (1 处)<br>  ... 共 6 处 |
| 3.5 | 对外网络请求域名明确 | 必查 | ⚠️  需人工复核 | 检测到网络请求:<br>  - README.zh-CN.md:5 → 探测到 HTTP(S) 网络请求 (8 处)<br>  - package.json:9 → 探测到 HTTP(S) 网络请求 (3 处)<br>  - README.md:5 → 探测到 HTTP(S) 网络请求 (13 处)<br>  - LICENSE:7 → 探测到 HTTP(S) 网络请求 (1 处)<br>  - CHANGELOG.md:3 → 探测到 HTTP(S) 网络请求 (4 处)<br>涉及的域名: 127.0.0.1, api.openai.com, ark.cn-beijing.volces.com, dashscope.aliyuncs.com, evil.example, generativelanguage.googleapis.com, github.com, img.shields.io, keepachangelog.com, localhost (+2 更多)<br>需人工确认每个网络请求的用途是否明确 |
| 3.6 | 无恶意网络逻辑 | 必查 | ❌ 不通过 | 检测到恶意网络模式:<br>  - .pnpm-store/v3/files/53/45986bee2cc4c2a0d56f116341b363897dfe3fe5f7e018a0d4d293a7f52920415000c98630feed2ada143483a3b3b3fe8fda68736e74fa727d86bf9c783346:3753 → 挖矿相关 (5 处)<br>  - .pnpm-store/v3/files/72/cb90f71dd8af470422cfd9831fce12df62070f6fa88ba700f424c75f51fdf88cab6a0655381c32a3bf57761ba9e7ebd5306fa2c23a8d4e77f64b1a0542c9c8-index.json:1 → DDoS 攻击 (1 处)<br>  - .pnpm-store/v3/files/1b/7e655a1d5e1145c41c3710b31c994b2b431bd76fe6dc98763b5e6d69fc2613bcc20bb27c60f03a8d92fa77eab9ae0944238c9131d66380dfa7609dc2ca8d21:91 → 挖矿相关 (1 处)<br>  - .pnpm-store/v3/files/c0/92d57c33f88ba07f85806e30b8350da475beaacc853f8c62931596ddec9511c5a45f56cf5d2484ecbf11980faba5e651460c11e6d69a0f3cd811ddae1e6cce:164 → 挖矿相关 (1 处)<br>  - .pnpm-store/v3/files/00/4e4be732c507b37c08efc9165ef64ccbdacda06ecdbf98e3542523f7076172d337f3349a30aa5b1c9a0ea7c1cc9513567beb45f4ad53acc501e3c8f45a9ff5:97 → 挖矿相关 (3 处)<br>  ... 共 39 处 |
| 3.7 | 不读取敏感配置 | 必查 | ⚠️  需人工复核 | 检测到敏感配置读取:<br>  - README.zh-CN.md:39 → API Key / Token 读取 (4 处)<br>  - SECURITY.md:3 → 敏感凭证读取 (2 处)<br>  - package.json:86 → 敏感凭证读取 (1 处)<br>  - README.md:53 → API Key / Token 读取 (4 处)<br>  - README.md:52 → 敏感凭证读取 (2 处)<br>  ... 共 362 处 — 需人工判断是否读取的是当前会话上下文 |
| 3.8 | 不篡改全局配置 | 必查 | ⚠️  需人工复核 | 检测到配置修改:<br>  - .pnpm-store/v3/files/c4/6a2a60af0d573eee8f51cf0883463e72d763b42ad3dee916125aa73d29bde59e818f6d7c44fb6983d74ad4516e2e3ffc8189041f0e7dba791e3fdfcef68b3c:631 → 写入配置文件 (1 处)<br>  - .pnpm-store/v3/files/d1/f1fb0a6e13cb33f68d2d95cb7965d2a1fdc72bc1e9e0cb01a4392a5118feed6efb337f7582401f86a2a00bcdeb47e675bc31de5e08ff5a4b78ab1b0b84d5d9:743 → 修改全局配置 (1 处)<br>  - .pnpm-store/v3/files/47/4b5af63461b160a2f60f2c1a323c9eb0eed325853e19f78ec5953b5c61f87d7a7db86fc216e599a9c2a5bd77df3d3818c1ea5dab7489ce9856a64248ff693e:9938 → 修改设置 (1 处)<br>  - .pnpm-store/v3/files/86/39f5aef592751752a92e4034931e46df3b4b73b49df174708e2c65a8b218115b93cf346b5a41d265f1ebe1aca727e525e3ace9bdb8c62be8b9cad3db92e8e5:3620 → 修改全局配置 (1 处)<br>  - .pnpm-store/v3/files/c9/a51ea7320017ab530ea57d7db3b9ef6a64a2a7e264cede456cf1f58027ecc31501019860d022978402d473ebe4eec99cdb3b8964bcfe8b3ecc73b674e60a06:584 → 修改全局配置 (1 处)<br>  ... 共 13 处 — 需人工判断是否涉及全局配置篡改 |


## 四、代码与依赖安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 4.1 | 无混淆代码 | 必查 | ❌ 不通过 | 检测到潜在混淆代码:<br>  - .pnpm-store/v3/files/c0/e2ca284adb5d513fa4688e7e98c79bc8e2fb85ee9d77d7111b258f848b89eadbc2cc88419f4cf1b887cf1683b7260c80507389428d7722ca3d5d36549087c5:6085 → 连续十六进制转义 (混淆) (3 处)<br>  - .pnpm-store/v3/files/c0/e2ca284adb5d513fa4688e7e98c79bc8e2fb85ee9d77d7111b258f848b89eadbc2cc88419f4cf1b887cf1683b7260c80507389428d7722ca3d5d36549087c5:4028 → 超长 base64 字符串 (1 处)<br>  - .pnpm-store/v3/files/c0/1fe72430b32f23fe99e1b6fb47dfce45af6016465b5368187b3039d47da6952f5127cf8ac1a355e8b162aa201c2ca09b11caf21c8ae187c3dc13edf8b1eea2:2 → 超长 base64 字符串 (1 处)<br>  - .pnpm-store/v3/files/a5/5022b7784b8858ca35fd702e9d60e70bf2947248e5be48eec9341ceba64d40a45f6e7010877285e95a93fac42303481365ea6fcbd4faa1fa4787a7d62a4a54:247 → JS 混淆器变量模式 (1 处)<br>  - .pnpm-store/v3/files/05/7140f32d01554566bc68a99e196d4e3da8fa5df7c8077d6f1adab404570b034450045c59ddd73cc146af40c3fbd5034890558a20a2e8305570ca67522b8f7d:2 → 超长 base64 字符串 (1 处)<br>  ... 共 41 处 |
| 4.2 | 无 eval/vm/new Function | 必查 | ❌ 不通过 | 检测到危险 API:<br>  - .pnpm-store/v3/files/1b/953240b7234bb2935e599470db6594a5bf396513da558dab17249936268eb2a70429c7035b8a52242b9604fbfbdfd6af226d8daa842005d25b2ce2216d2470:281 → eval() 任意代码执行 (1 处)<br>  - .pnpm-store/v3/files/1b/953240b7234bb2935e599470db6594a5bf396513da558dab17249936268eb2a70429c7035b8a52242b9604fbfbdfd6af226d8daa842005d25b2ce2216d2470:279 → new Function() 任意代码执行 (1 处)<br>  - .pnpm-store/v3/files/c0/e2ca284adb5d513fa4688e7e98c79bc8e2fb85ee9d77d7111b258f848b89eadbc2cc88419f4cf1b887cf1683b7260c80507389428d7722ca3d5d36549087c5:3566 → eval() 任意代码执行 (1 处)<br>  - .pnpm-store/v3/files/c0/e2ca284adb5d513fa4688e7e98c79bc8e2fb85ee9d77d7111b258f848b89eadbc2cc88419f4cf1b887cf1683b7260c80507389428d7722ca3d5d36549087c5:3031 → new Function() 任意代码执行 (2 处)<br>  - .pnpm-store/v3/files/c0/e2ca284adb5d513fa4688e7e98c79bc8e2fb85ee9d77d7111b258f848b89eadbc2cc88419f4cf1b887cf1683b7260c80507389428d7722ca3d5d36549087c5:11144 → 加载 child_process 模块 (3 处)<br>  ... 共 40 处 |
| 4.3 | npm audit 无高危漏洞 | 必查 | ⚠️  需人工复核 | npm 不可用, 无法执行 npm audit. 建议在具备 npm 的环境中运行 `npm audit` |
| 4.4 | 不使用废弃依赖 | 必查 | ✅ 通过 | 共检查 10 个依赖, 未发现已知废弃包 |
| 4.5 | 无隐藏后门 | 必查 | ⚠️  需人工复核 | 检测到潜在后门/隐藏逻辑:<br>  - .pnpm-store/v3/files/c0/e2ca284adb5d513fa4688e7e98c79bc8e2fb85ee9d77d7111b258f848b89eadbc2cc88419f4cf1b887cf1683b7260c80507389428d7722ca3d5d36549087c5:1588 → 动态设置调试端口 (1 处)<br>  - .pnpm-store/v3/files/c0/e2ca284adb5d513fa4688e7e98c79bc8e2fb85ee9d77d7111b258f848b89eadbc2cc88419f4cf1b887cf1683b7260c80507389428d7722ca3d5d36549087c5:11630 → 开启监听端口 (6 处)<br>  - .pnpm-store/v3/files/c0/e2ca284adb5d513fa4688e7e98c79bc8e2fb85ee9d77d7111b258f848b89eadbc2cc88419f4cf1b887cf1683b7260c80507389428d7722ca3d5d36549087c5:10555 → 定时任务 (21 处)<br>  - .pnpm-store/v3/files/c0/e2ca284adb5d513fa4688e7e98c79bc8e2fb85ee9d77d7111b258f848b89eadbc2cc88419f4cf1b887cf1683b7260c80507389428d7722ca3d5d36549087c5:32220 → 文件写入 (2 处)<br>  - .pnpm-store/v3/files/c0/e2ca284adb5d513fa4688e7e98c79bc8e2fb85ee9d77d7111b258f848b89eadbc2cc88419f4cf1b887cf1683b7260c80507389428d7722ca3d5d36549087c5:1950 → 文件读取 (17 处)<br>  ... 共 189 处 — 需人工判断是否有恶意意图 |
| 4.6 | 无文件窃取/静默上传 | 必查 | ⚠️  需人工复核 | 检测到潜在文件窃取/上传模式:<br>  - .pnpm-store/v3/files/1b/a2a2b6903557a9b786b4f635ba94c93bc2c4088398566ea098319b282ee2313b3cf9c1ff4822e5803cc32ea359f2bd2f50cf0554a744f6d7c039c1480bfbf1:29 → 云存储上传 (1 处)<br>  - .pnpm-store/v3/files/00/635f9f79fc4a2bff52638ea10e4fdcc0acd69e1fdeb9d1399e70c8d1e83511ccc0d534a0efcf9cd148200c89d4bf4f98bf8c3a9abe52263c851fcc02479887:1 → 云存储上传 (6 处)<br>  - .pnpm-store/v3/files/fc/80911ad5eb4298834dafb1ee3a17d16f590342939db652b20fd523e18181c4d902dd444ef4a381127ca6ce2f287738ee1b3e5a2df649bc5d03d4162ac8d64a:7197 → 云存储上传 (1 处)<br>  - .pnpm-store/v3/files/ff/c23ebcfb6aa533a27bc9a8d8ab300a229094f97132033106f7a520774562d7363666af7b258473758aefac7ac6790ae1954ca733e42d72be5903ff4fb611af:13 → multipart 上传 (1 处)<br>  - .pnpm-store/v3/files/ff/40690450d34b292ae93f4cd5f2536cc6bd6db19c029504bbc074ba9534da984c96120f8ac53a49bd37b5556945661125bfaaa667586d7ff48315f25bb37e20:1006 → 云存储上传 (1 处)<br>  ... 共 49 处 — 需人工判断是否有恶意意图 |
| 4.7 | 依赖数量可控 | 推荐 | ✅ 通过 | 总依赖数: 3. repo: 0 deps + 3 devDeps |
| 4.8 | 代码结构清晰 | 推荐 | ✅ 通过 | 总行数: 4347, 注释行: 280 (6.4%) |
| 4.9 | 具备测试覆盖 | 推荐 | ✅ 通过 | 发现测试文件/目录: 1 个, 例如: tests |


## 五、数据安全与隐私审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 5.1 | 数据本地处理 | 必查 | ⚠️  需人工复核 | 检测到网络请求, 但未在 README 中发现数据上传说明 |
| 5.2 | 数据上报透明 | 必查 | ❌ 不通过 | 检测到网络请求但 README 中未说明数据上报内容、接收方、用途 |
| 5.3 | 敏感信息加密存储 | 必查 | ⚠️  需人工复核 | 检测到敏感信息存储:<br>  - .pnpm-store/v3/files/c0/e2ca284adb5d513fa4688e7e98c79bc8e2fb85ee9d77d7111b258f848b89eadbc2cc88419f4cf1b887cf1683b7260c80507389428d7722ca3d5d36549087c5:20880 → 硬编码敏感信息 (12 处)<br>  - .pnpm-store/v3/files/c0/e2ca284adb5d513fa4688e7e98c79bc8e2fb85ee9d77d7111b258f848b89eadbc2cc88419f4cf1b887cf1683b7260c80507389428d7722ca3d5d36549087c5:28014 → 从环境变量获取敏感信息 (1 处)<br>  - .pnpm-store/v3/files/24/1726cfc894a53631059293013dd33924acb0e909676f84b2ba8e5e0795e70b634ea97b982fa718741c712acf8d7b96333d65902c66442903dd90596c00a876:1070 → 硬编码敏感信息 (2 处)<br>  - .pnpm-store/v3/files/9b/189e933adaf69f24bb34e18386135e669dcc564cccda2b356c8c29b109fa213dbc78f84aa91dbf90043e593b5ffd2abdab41292ce563d5c9fb0f4dd21f2dc2:308 → 硬编码敏感信息 (2 处)<br>  - .pnpm-store/v3/files/21/15359ca3df657062d43665ae698b74c1a294f827dce2666ca9aaff1a184c7235244fa17d45172edb907cfdbc3ceab1089c72ee510b3ad938f42e2f7915c93c:66 → 硬编码敏感信息 (11 处) — 需确认是否加密存储 |
| 5.4 | 无未授权读取 | 必查 | ⚠️  需人工复核 | 检测到潜在未授权读取:<br>  - .pnpm-store/v3/files/dc/5eafda97fbd9a7326d72bcbec02c92dca8b80084e928e434c9c6ccbe27da941d62d7fec52907116c88f172920a6cf2d27222ba95ca60ada688eca578cb178a:120 → 读取文档/压缩文件 (1 处)<br>  - .pnpm-store/v3/files/ff/85dc02cc19caf950463f25ff722912908cc8fb575bc5d0bf7c39cd515ff6ab6a47c6cc980b6aa1119e7d4134987cd1a4bf78c336bacf8b44736a1b2b4ec510:109 → 读取文档/压缩文件 (1 处)<br>  - .pnpm-store/v3/files/84/d6ffb5694dec01231d1187e12bdcf0fcf970a43c0e7a4831601cbc266233091e63aec1df0815cfe145959db84a6c189f889d9008a3092637dc3ab69c8a03d0:1387 → 读取文档/压缩文件 (3 处)<br>  - .pnpm-store/v3/files/79/c4c73213816a1d5675af864b76e2f25a37b5fcd363b6786d32aab6097db014e46cfa3f68ed1f36a317afa9b2f2069d853025ceaf4a1722969b0c7f20d75860:111 → 读取文档/压缩文件 (1 处)<br>  - .pnpm-store/v3/files/28/0dda5ec197bd08aca7cdba4904187194506f841986ae9322027cb584b5befeb3a7eb7c5848f3726cb6e10d5812d82d7f5cd29ec1392d409449a827e9b81095:121 → 读取文档/压缩文件 (1 处) — 需人工判断是否在授权范围内 |
| 5.5 | 关键操作有日志 | 推荐 | ✅ 通过 | 发现日志记录模式 (493 处) |
| 5.6 | 支持一键清理数据 | 推荐 | ✅ 通过 | 发现数据清理相关代码 (37 处) |


## 六、运行时安全审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 6.1 | 无需 root 权限 | 必查 | ❌ 不通过 |   - .pnpm-store/v3/files/06/5e6dac1c2ef34152cda7b35b1b4dc81468e32bdf2c3f5195edc2d90d3a3c6f7888dc869797f137f4a4f9e0c9800ac87f9bd117152f4c3f7ce4e5b347a43593:3094 → 要求 root/sudo 权限 |
| 6.2 | 不修改系统配置 | 必查 | ❌ 不通过 | 检测到系统配置修改:<br>  - .pnpm-store/v3/files/1b/a2a2b6903557a9b786b4f635ba94c93bc2c4088398566ea098319b282ee2313b3cf9c1ff4822e5803cc32ea359f2bd2f50cf0554a744f6d7c039c1480bfbf1:47 → 创建开机自启/系统服务 (1 处)<br>  - .pnpm-store/v3/files/c0/e2ca284adb5d513fa4688e7e98c79bc8e2fb85ee9d77d7111b258f848b89eadbc2cc88419f4cf1b887cf1683b7260c80507389428d7722ca3d5d36549087c5:12758 → 修改系统目录 (1 处)<br>  - .pnpm-store/v3/files/0e/66a201540b7121e848ea8f2c67b6cb3ace49d27dddb3c108e4d18707b298148bb00dac6b7e71c32aa66b7b637e883c0c9924f7b4b55e5fd19b7b8dfedfaed5:262 → 创建开机自启/系统服务 (1 处)<br>  - .pnpm-store/v3/files/d8/c6261c384b4bd9279a2da06d9b9d195917967577ec3a5c603fbabcdaa60aa457e6f36d2d885b6d3487d13d1d4107490fa3fdbeae5b8dd35855f23ae20aabc1:208 → 创建开机自启/系统服务 (1 处)<br>  - .pnpm-store/v3/files/4d/86796805c9bebbd687fd42703e644dd98e9b5c63350a8b439f3761846fb26c7a10306a36fbe4b68fe5437299573cc9a6cdb83b6006bed7e67b6213e16ef5ff-exec:1 → 修改系统目录 (1 处)<br>  ... 共 49 处 |
| 6.3 | 支持沙箱运行 | 必查 | ✅ 通过 | 检测到沙箱支持声明: workspace |
| 6.4 | 无内存泄漏 | 推荐 | ⚠️  需人工复核 | 需在运行环境中长时间测试 |
| 6.5 | 临时文件自动清理 | 推荐 | ✅ 通过 | 发现临时文件清理逻辑 (141 处) |


## 七、维护与社区审计

| 序号 | 检查项 | 类型 | 结果 | 详情 |
| :--- | :--- | :---: | :---: | :--- |
| 7.1 | 近 3 个月内有更新 | 必查 | ✅ 通过 | 最近提交距今: 0 天; 提交总数: 12 |
| 7.2 | 未标记停止维护 | 必查 | ✅ 通过 | 未发现停止维护/弃用声明 |
| 7.3 | 无大量未解决安全反馈 | 必查 | ✅ 通过 | 未发现公开安全问题 |
| 7.4 | 安全问题响应 ≤ 7 天 | 推荐 | ⚠️  需人工复核 | 需通过 GitHub Issues/PR 历史人工评估 |
| 7.5 | 完整文档 | 推荐 | ✅ 通过 | 文档齐全: README, CHANGELOG, 配置说明, 使用示例, 安装说明 |
| 7.6 | 有社区背书 | 推荐 | ⚠️  需人工复核 | Stars: 1, Forks: 0, Watchers: 0 — 社区背书不足, 需人工判断 |


## 审计结论

| 项目 | 内容 |
| :--- | :--- |
| 插件名称 | dsh-video-gen |
| 校验 URL | https://github.com/Yang-wudi/dsh-video-gen |
| 必查项通过率 | 12/33 (36%) |
| 推荐项满足率 | 14/14 (约 100%) |
| 最终分级 | 🔴 黑名单 |
| 主要风险说明 | 详见各检查项结果 |
| 审计方式 | 自动化静态分析 (需人工复核标记项) |
| 审计日期 | 2026-08-30 |

> ⚠️ **注意**: 本报告由自动化脚本生成, 标注为 "需人工复核" 的检查项必须由安全审计人员人工确认后方可最终定级。
