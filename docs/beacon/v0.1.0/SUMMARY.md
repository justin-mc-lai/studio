# Studio v0.1.0 — 版本摘要

## 定位

`studio` v0.1.0 是公司运营层的总控制面（control plane），不是领域实现：
统一注册 8 个项目 + brain-loop 大脑 + adb 派工，把需求从池子入口一路留痕到知识沉淀。
truth canonical: `main`；feature package: `docs/beacon/v0.1.0/features/studio/`。

## 交付内容

1. **Portfolio 注册与健康度**：`portfolio/portfolio.json` 全量 8 项目 + `last_activity`；
   `scripts/portfolio_health.py` 按 state-model 阈值计算绿黄红并写
   `knowledge/cross-cutting/portfolio-health.md`；由 `beacon task st-d0f67704026e`
   每日 09:00（launchd timer）自动执行。
2. **需求池状态机**：`requirements/pool.md` 为唯一入口，状态
   `inbox → routed → doing → review → done`，实测 REQ-001=doing / REQ-002,003=done，非法流转显式禁止。
3. **需求真相冻结链**：`truth/tests/tasks/evidence` 四件套 + Domain Model/FSM，
   7 AC 全覆盖，B_fsm_audit / C_domain_exec_layer 紧口径。
4. **全程 trace 五段回流**：每 REQ 一 `trace/TRACE-*.md`，采集→路由→执行→回流→沉淀。
5. **路线图与健康日报**：`execution/roadmap-q3.md`（REQ-002）、
   每日健康看板（REQ-003）。

## 范围

- Scope mode: `full_parity`（新建独立产品，非 brain-loop 接管；与 brain-loop/adb/beacon 平级）。
- 非目标：不新增公开一级主命令、不做 8 项目各自领域实现、不做 UI 高保真。

## 门禁与证据

- truth: `docs/beacon/v0.1.0/features/studio/truth.md`（status: frozen, domain_required: true）
- gates: `.beacon/evidence/implement/studio/GATES.json`
- qa: `.beacon/evidence/implement/studio/QA-MATRIX.json`
- release: `docs/beacon/v0.1.0/release/checklist-v0.1.0.md`

## 本次闭环修复

R1 实现证据曾存在三处口径缺口，已在本次修复中收敛：

1. `requirements/pool.md` 状态未真实流转 → 已按 FSM 归位并留回流证据。
2. 健康看板为手写静态文件 → 已换成可计算 + 可调度（beacon task timer）。
3. v0.1.0 未封 release → 已产出 release checklist，并清零 truth-map 哈希漂移。
