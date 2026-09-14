---
slug: studio
version: v0.1.0
materials_status: current
task_source: acceptance_criteria
---

# Tasks: studio

## Task Ledger

- [ ] TASK-001 Implement AC-001: Portfolio 注册与健康度判定：8 项目在 portfolio.json 全量注册，health 绿(7日活动)/黄(14日无活动)... · ac=AC-001 · evidence=`.beacon/evidence/implement/studio/AC-001.json`
- [ ] TASK-002 Implement AC-002: 需求池路由与状态机：requirements/pool.md 为唯一入口，状态 inbox→routed→doing→done，非法 do... · ac=AC-002 · evidence=`.beacon/evidence/implement/studio/AC-002.json`
- [ ] TASK-003 Implement AC-003: 跨项目需求真相冻结链：truth/tests/tasks/evidence 四件套事务闭环，B_fsm_audit 与 C_domain_... · ac=AC-003 · evidence=`.beacon/evidence/implement/studio/AC-003.json`
- [ ] TASK-004 Implement AC-004: 双轨执行与记忆：brain-loop 自动化与人工介入双轨并存，执行结果经 memory/workflow-lifecycle 与 knowl... · ac=AC-004 · evidence=`.beacon/evidence/implement/studio/AC-004.json`
- [ ] TASK-005 Implement AC-005: 全程 trace 五段回流：每 REQ 一 TRACE-*.md 走 采集→路由→执行→回流→沉淀，未回流即标 done 被拒绝，trac... · ac=AC-005 · evidence=`.beacon/evidence/implement/studio/AC-005.json`
- [ ] TASK-006 Implement AC-006: Q3 路线图决策（REQ-002）：产出 docs/beacon/v0.1.0/execution/roadmap-q3.md，明确 a-... · ac=AC-006 · evidence=`.beacon/evidence/implement/studio/AC-006.json`
- [ ] TASK-007 Implement AC-007: 健康看板日报（REQ-003）：每日自动汇总 8 项目绿黄红，数据源 portfolio.json，结果落 trace/knowledge... · ac=AC-007 · evidence=`.beacon/evidence/implement/studio/AC-007.json`
- [ ] TASK-008 Validate package gates (truth review + freeze ack) · ac=GATES · evidence=`.beacon/evidence/implement/studio/GATES.json`
- [ ] TASK-009 Run QA against AC↔TC matrix + exec-layer evidence · ac=QA · evidence=`.beacon/evidence/implement/studio/QA-MATRIX.json`

## Boundary

Checkboxes are AC-bound ledgers. `[x]` is valid only when the bound `evidence=` file exists (completion ≠ self-tick).
