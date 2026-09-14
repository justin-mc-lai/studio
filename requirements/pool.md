# Requirements Pool — Studio 统一需求池

> 唯一入口。状态机 `inbox → routed → doing → review → done`（见 `docs/beacon/v0.1.0/state-model.md`）。
> 非法流转：`done → inbox` 禁止；`doing` 未经 `routed` 禁止。
> 新需求只追加到 Inbox，路由/执行/回流时迁移到对应节并记 `证据`。

## Inbox (待路由)
- (空)

## Routed (已路由)
- (空)

## Doing (执行中)
### REQ-001: Studio P0 落地
- 来源: Owner 2026-09-01
- 绑定: studio (cross-project)
- 状态: doing
- 证据: trace/TRACE-001.md

## Review (待验收)
- (空)

## Done (已回流)
### REQ-002: Q3 跨项目路线图 — quant-alpha 全量数据 vs store-front metric+10% 优先级决策
- 来源: Owner 2026-09-01 (跨项目战略)
- 类型: planning
- 优先级: high
- 绑定: cross-project (quant-alpha, store-front)
- 状态: done
- 回流: docs/beacon/v0.1.0/execution/roadmap-q3.md · trace/TRACE-002.md

### REQ-003: 公司健康看板 — 8 项目绿/黄/红自动日报
- 来源: Owner 2026-09-01 (运营)
- 类型: ops
- 优先级: high
- 绑定: cross-project (portfolio 全量)
- 状态: done
- 回流: knowledge/cross-cutting/portfolio-health.md (scripts/portfolio_health.py + beacon task st-d0f67704026e 每日 09:00) · trace/TRACE-003.md

## Icebox
- (低优/暂缓)
