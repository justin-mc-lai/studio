# Studio v0.1.0 — Design State Matrix

> Studio 是控制面（control plane），无高保真 UI；本矩阵把 3 个 domain FSM 的
> 状态/迁移投影为看板与管理面的状态可见性契约，供 QA 对 domain states 做绑定。

## Requirement 状态面

| State | 看板展示 | 可执行操作 | 迁移 |
|-------|----------|-----------|------|
| inbox | 待路由 | route | inbox → routed |
| routed | 已路由 | start / clarify | routed → doing / routed → inbox |
| doing | 执行中 | submit / clarify | doing → review / doing → inbox |
| review | 待验收 | pass / fail | review → done / review → doing |
| done | 已回流 | —（终态） | 无 |

## Project 健康度状态面

| State | 展示色 | 进入条件 |
|-------|--------|----------|
| green | 绿 | 最近活动 <14d |
| yellow | 黄 | 14d ≤ 无活动 <30d |
| red | 红 | ≥30d 无活动或构建失败 |

## 信息流状态面

| Stage | 面 | 产物 |
|-------|----|------|
| 采集 | portfolio / requirements | portfolio.json, pool.md |
| 路由 | Routing | REQ→project 绑定 |
| 执行 | Beacon / adb | implementation evidence |
| 回流 | Trace | trace/TRACE-*.md |
| 沉淀 | Knowledge / Memory | knowledge/cross-cutting/* |

## 非法状态（不可展示为通过）

- requirement: done→inbox、inbox→doing、doing→done（跳过 review/gate）
- project: red→green 需先有活动修复，禁止直接回绿
