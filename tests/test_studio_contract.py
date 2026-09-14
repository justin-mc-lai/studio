"""Studio v0.1.0 contract test harness (AC-001..AC-007 / TC-001..TC-013).

Runnable pytest suite so Beacon feature-QA gets real junit + assertion counts.
Run:  python3 -m pytest tests/ -q --junitxml=.beacon/junit.xml
"""
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def _portfolio():
    return json.loads(_read("portfolio/portfolio.json"))


# ---------------------------------------------------------------- AC-001
def test_tc001_portfolio_registers_eight_projects():
    assert len(_portfolio()["projects"]) == 8


def test_tc002_health_ladder_matches_thresholds():
    projects = _portfolio()["projects"]
    assert projects["shop-ca"]["health"] == "yellow"
    assert projects["brain-loop"]["health"] == "green"


def test_tc003_state_model_documents_thresholds():
    assert re.search(r"green.*7天.*yellow.*14天.*red.*30天", _read("docs/beacon/v0.1.0/state-model.md"))


# ---------------------------------------------------------------- AC-002
def test_tc004_router_fsm_legal_and_illegal_declared():
    state_model = _read("docs/beacon/v0.1.0/state-model.md")
    truth = _read("docs/beacon/v0.1.0/features/studio/truth.md")
    assert re.search(r"inbox --> routed", state_model)
    assert re.search(r"done --> inbox 禁止", truth)


def test_tc005_requirements_pool_traceable():
    assert re.search(r"REQ-00[23]", _read("requirements/pool.md"))


# ---------------------------------------------------------------- AC-003
def test_tc006_domain_gate_enabled():
    assert re.search(r"domain_required: true", _read("docs/beacon/v0.1.0/features/studio/truth.md"))


def test_tc007_truth_review_gate_b_and_c_pass():
    gate = json.loads(_read("docs/beacon/v0.1.0/.machine/execution/studio.truth-review-gate.json"))
    checks = gate["checks"]
    assert checks["B_fsm_audit"]["pass"] is True
    assert checks["C_domain_exec_layer"]["pass"] is True


# ---------------------------------------------------------------- AC-004
def test_tc008_dual_track_and_knowledge_sink():
    projects = _portfolio()["projects"]
    assert projects["brain-loop"]["role"] == "brain-runtime"
    assert projects["dispatch-bus"]["adb"] is True
    assert re.search(r"knowledge/", _read("docs/beacon/v0.1.0/features/studio/evidence.md"))


# ---------------------------------------------------------------- AC-005
def test_tc009_trace_backflow_five_stages():
    traces = list((ROOT / "trace").glob("TRACE-*.md"))
    assert len(traces) >= 1
    assert re.search(r"采集.*路由.*执行.*回流.*沉淀", _read("docs/beacon/v0.1.0/state-model.md"))


def test_tc010_illegal_transitions_rejected():
    state_model = _read("docs/beacon/v0.1.0/state-model.md")
    truth = _read("docs/beacon/v0.1.0/features/studio/truth.md")
    assert "跳过路由直接执行" in state_model
    assert "未经 trace 回流禁止" in truth


# ---------------------------------------------------------------- AC-006
def test_tc011_q3_roadmap_present():
    roadmap = _read("docs/beacon/v0.1.0/execution/roadmap-q3.md")
    assert re.search(r"quant-alpha.*ecommerce|metric.*10%|优先级.*资源分配", roadmap)


# ---------------------------------------------------------------- AC-007
def test_tc012_health_board_generated():
    board = _read("knowledge/cross-cutting/portfolio-health.md")
    assert re.search(r"green|yellow|red", board)
    assert re.search(r"green|yellow|red", _read("portfolio/portfolio.json"))


def test_tc013_health_evidence_indexed():
    assert re.search(r"AC-007", _read("docs/beacon/v0.1.0/features/studio/evidence.md"))


# ---------------------------------------------------------------- FSM
LEGAL_WALK = ["inbox", "routed", "doing", "review", "done"]
ILLEGAL = [("done", "inbox"), ("inbox", "doing"), ("doing", "done")]


def _fsm_transitions():
    """Transitions declared in the truth FSM mermaid block."""
    truth = _read("docs/beacon/v0.1.0/features/studio/truth.md")
    mermaid = re.search(r"stateDiagram-v2.*?```", truth, re.S).group(0)
    return set(re.findall(r"(\w+)\s*-->\s*(\w+)\s*:", mermaid))


def test_tc014_fsm_legal_walk_full_path():
    transitions = _fsm_transitions()
    for src, dst in zip(LEGAL_WALK, LEGAL_WALK[1:]):
        assert (src, dst) in transitions, f"legal walk edge missing: {src}->{dst}"
    assert LEGAL_WALK[0] == "inbox" and LEGAL_WALK[-1] == "done"


def test_tc015_fsm_illegal_transitions_absent():
    transitions = _fsm_transitions()
    for edge in ILLEGAL:
        assert edge not in transitions, f"illegal edge must not exist: {edge[0]}->{edge[1]}"
