# Studio v0.1.0 Research

## 健康度阈值口径校准

- 问题：AC-001 文本写「绿 7 天 / 黄 14 天 / 红 30 天」，而
  `docs/beacon/v0.1.0/state-model.md` 的 FSM guard 写
  「green --14 天--> yellow --30 天--> red」，两者不一致。
- 结论：以 FSM 状态机 guard 为准（14 / 30），「7 天」视为「活跃」描述性措辞。
- 落地：`scripts/portfolio_health.py` 的 `GREEN_MAX_DAYS` / `YELLOW_MAX_DAYS`
  两个常量即口径旋钮，统一口径只改常量、不改逻辑。
- 现状核对：`shop-ca` 14 天无活动 → yellow，其余 7 项目 ≤4 天 → green，与 FSM 一致。

## 活跃度数据源取舍

- 问题：健康度需要「最近活动」时间，取真实 commit 时间还是 portfolio 字段？
- 约束：8 项目为跨仓引用，`portfolio.json` 未存各仓 `path`，无法直接读各自的 git log。
- 结论：v0.1.0 采用 `portfolio.json.last_activity` 显式字段作为最小可计算模型，
  由 `beacon task st-d0f67704026e` 每日重算，字段老化会自动升级为黄 / 红。
- 升级路径：后续在 portfolio 增加 `path`，接入各仓 git 活跃度探测，替换字段来源。

## 需求池状态机单源

- 问题：`requirements/pool.md` 既是入口又是状态视图，易与 trace 漂移。
- 结论：pool.md 分状态节（Inbox/Routed/Doing/Review/Done）承载当前状态，
  `trace/TRACE-*.md` 承载流转历史，两者以 REQ-ID 对齐；
  本次修复把 REQ-002/003 由 Inbox 残留归位到 Done，并补回流证据。
