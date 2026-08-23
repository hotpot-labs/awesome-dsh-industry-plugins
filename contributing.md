# 投稿指南

感谢向「安全审核版 dsh 行业插件市场」投稿。本仓库只收录经过安全审核的插件，请按以下流程提交。

## 投稿要求

1. Fork 本仓库，基于最新 `main` 创建分支（**不要基于过期 fork 提交**：PR 若删除已有条目超过 2 条会被 CI 判定为 stale fork 而拒绝）。
2. 运行审核脚本生成本地审核产物：

   ```bash
   python3 scripts/audit_plugin.py \
     --url https://github.com/<owner>/<repo> \
     --category 通用 --source submission
   ```

   该脚本会：调用 `security/validate-plugin.py` 生成完整审核报告 → 解析定级 →
   写入 `plugins/<owner>__<repo>/`（`plugin.md` + `security-report.md`）→ 更新 `plugins.json`。

   也可以只改 `plugins.json` 并在 PR 描述中注明「由 CI 生成审核产物」，但**推荐本地先跑一次**，确认定级不是黑名单再投稿。
3. 提交 PR。单个 PR 新增收录不超过 3 条。

## 分类

投稿时选择且仅可选择一个分类：**通用、计算机、金融、法律、自媒体、电商、其他**。

## CI 检查项

PR 会触发以下自动检查（见 `.github/workflows/pr-check.yml`）：

- **结构校验**：`plugins.json` 合法、必填字段齐全、分类合法、`id` 与目录一致、审核产物（`plugin.md` + `security-report.md`）齐全。
- **自动安全审核**：对 PR 新增/变更的插件 URL 逐个跑审核。判定为**黑名单直接拒绝**；灰名单会在 PR 中输出 warning，需维护者人工复核后方可合并。
- **防绕过检查**：PR 不允许修改 `.github/workflows/` 与 `security/`（审核逻辑与 CI 仅维护者可改）。

## 维护者人工复核清单

CI 只是 sanity check。合并前维护者必须人工复核：

1. 打开 `plugins/<id>/security-report.md`，逐项确认所有标注「**需人工复核**」的检查项，重点包括：
   - 1.4 核心功能与 README 描述一致性；
   - 1.5 是否违反法律法规；
   - 2.2/2.3/2.4 Cordis 规范细节、异常捕获、卸载清理逻辑；
   - 3.x/4.x/5.x 中被标记的业务意图判断项（如网络外发、命令执行是否有正当用途）。
2. 对照 [`security/security-checklist.md`](./security/security-checklist.md) 完成最终分级：
   - 必查项全部通过 + 人工复核无问题 → 白名单；
   - 存在疑点但不构成明确危害 → 灰名单（测试可用）；
   - 必查项不通过或确认恶意 → 黑名单（禁止收录，仅留档）。
3. 若人工复核结论与 `verdict` 不一致，要求投稿者修改或拒绝合并。

## 审核标准

- 检查清单：[`security/security-checklist.md`](./security/security-checklist.md)
- 审核说明：[`security/security-docs.md`](./security/security-docs.md)
- 审核引擎：[`security/validate-plugin.py`](./security/validate-plugin.py)
