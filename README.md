# awesome-dsh-industry-plugins

提供经过安全审查的精选行业插件，插件分类有 通用、计算机、金融、法律、自媒体、电商、其他。

本仓库只收录**经过自动化安全审核**的 dsh 插件：每个插件都附完整安全审核报告，并按审核结论定级（白名单 / 灰名单 / 黑名单）。审核逻辑与判定标准见 [`security/`](./security/) 目录（复制自 `security-for-dsh-plugin` 项目）。

## 目录结构

```
plugins.json            # 集中收录名单（机器可读索引，schema 见 plugins.schema.json）
plugins/<owner>__<repo>/
├── plugin.md           # 插件基本信息（名称/URL/分类/描述/审核日期/定级）
└── security-report.md  # validate-plugin.py 生成的完整审核报告
security/               # 审核引擎与审核标准（自包含，CI 直接使用）
scripts/                # 审核编排 / PR 结构校验 / 上游每日同步
.github/workflows/      # PR 审核 CI 与每日增量审核 CI
```

## plugins.json 字段说明

| 字段 | 含义 |
| :--- | :--- |
| `id` | 插件唯一标识 `<owner>__<repo>`，与 `plugins/` 下目录名一致 |
| `name` / `url` | 插件全名 `owner/repo` 与 GitHub 仓库地址 |
| `category` | 收录分类，仅允许：通用、计算机、金融、法律、自媒体、电商、其他 |
| `description` | 插件一句话简介 |
| `verdict` | 审核定级：`whitelist` 白名单 / `greylist` 灰名单(需人工复核) / `blacklist` 黑名单 / `pending` 待审核 |
| `auditedAt` | 最近一次审核日期 |
| `source` | 收录来源：`submission`（PR 投稿）/ `awesome-dsh-plugin`（上游每日同步） |
| `dir` | 审核产物目录 |
| `removed` | 上游已删除时置 `true`（保留审核档案，不再展示） |

所有审核过的插件（含黑名单）都会记录在案，用 `verdict` 字段区分，便于追溯。

## 收录流程

1. **PR 投稿**：见 [contributing.md](./contributing.md)。CI 自动做结构校验、安全审核（黑名单直接拒绝、灰名单提示人工复核）与防绕过检查。
2. **每日同步**：GitHub Actions 每天北京时间 08:00 从上游 [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) 增量同步新增收录并自动审核，单次最多 20 个，结果直接提交回 main。

## 安全声明

- 自动审核**不等于**人工审计。审核报告中标注「需人工复核」的检查项，以维护者人工复核结论为准。
- 灰名单插件仅供测试使用；黑名单插件禁止安装，仅作留档警示。
- 审核标准与检查清单：[`security/security-checklist.md`](./security/security-checklist.md)、[`security/security-docs.md`](./security/security-docs.md)。
