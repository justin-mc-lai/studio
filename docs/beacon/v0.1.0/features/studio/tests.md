---
slug: studio
version: v0.1.0
materials_status: stale
---

# Tests: studio

| TC ID | AC ID | Command | Assertion |
|-------|-------|---------|-----------|
| TC-001 | AC-001 | `jq -e '.projects | length == 8' portfolio/portfolio.json` | 8 项目全量注册 |
| TC-002 | AC-001 | `jq -e '.projects["shop-ca"].health == "yellow"' portfolio/portfolio.json && jq -e '.projects["brain-loop"].health == "green"' portfolio/portfolio.json` | 健康度初值与阈值口径一致 |
| TC-003 | AC-001 | `rg -n 'green.*7天.*yellow.*14天.*red.*30天' docs/beacon/v0.1.0/state-model.md` | 状态机阈值文档可验 |
| TC-004 | AC-002 | `rg -n 'inbox --> routed' docs/beacon/v0.1.0/state-model.md && rg -n 'done --> inbox 禁止' docs/beacon/v0.1.0/features/studio/truth.md` | 路由 FSM 合法/非法声明可验 |
| TC-005 | AC-002 | `rg -n 'REQ-00[23]' requirements/pool.md` | REQ-002/003 在池可追溯 |
| TC-006 | AC-003 | `rg -n 'domain_required: true' docs/beacon/v0.1.0/features/studio/truth.md` | 紧口径域开关已启用 |
| TC-007 | AC-003 | `beacon truth review studio --project-root . --version v0.1.0 --json | jq -e '.checks.B_fsm_audit.pass == true and .checks.C_domain_exec_layer.pass == true'` | B 与 C_exec 紧口径通过（非 skipped） |
| TC-008 | AC-004 | `jq -e '.projects["brain-loop"].role == "brain-runtime" and .projects["dispatch-bus"].adb == true' portfolio/portfolio.json && rg -n 'knowledge/' docs/beacon/v0.1.0/features/studio/evidence.md` | 双轨与知识沉淀声明可验 |
| TC-009 | AC-005 | `ls trace/TRACE-*.md | wc -l | xargs -I{} test {} -ge 1 && rg -n '采集.*路由.*执行.*回流.*沉淀' docs/beacon/v0.1.0/state-model.md` | 五段回流模型与 trace 文件存在 |
| TC-010 | AC-005 | `rg -n '跳过路由直接执行' docs/beacon/v0.1.0/state-model.md && rg -n '未经 trace 回流禁止' docs/beacon/v0.1.0/features/studio/truth.md` | 非法流转禁止可验 |
| TC-011 | AC-006 | `test -f docs/beacon/v0.1.0/execution/roadmap-q3.md && rg -n 'quant-alpha.*ecommerce|metric.*10%|优先级.*资源分配' docs/beacon/v0.1.0/execution/roadmap-q3.md` | Q3 路线图文档存在且含优先级与资源分配 |
| TC-012 | AC-007 | `test -f knowledge/cross-cutting/portfolio-health.md || test -f trace/TRACE-003.md && rg -n 'green|yellow|red' portfolio/portfolio.json` | 健康日报产物或 trace 可追溯且阈值与 AC-001 一致 |
| TC-013 | AC-007 | `rg -n 'AC-007' docs/beacon/v0.1.0/features/studio/evidence.md` | 健康日报证据索引可验 |
| TC-014 | AC-002 | `python3 -m pytest tests/test_studio_contract.py -k fsm_legal_walk` | FSM 合法路径 legal walk: inbox→routed→doing→review→done 全路径可达 |
| TC-015 | AC-002 | `python3 -m pytest tests/test_studio_contract.py -k fsm_illegal_transitions` | FSM 非法路径 rejected: done→inbox 等非法转移不可达 |

