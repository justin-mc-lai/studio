#!/usr/bin/env python3
"""Portfolio health board generator (AC-007 / REQ-003).

Reads portfolio/portfolio.json, computes green/yellow/red from each project's
last_activity, writes knowledge/cross-cutting/portfolio-health.md.

Scheduled daily via `beacon task` (task: portfolio-health-daily).
"""
import json
import sys
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PORTFOLIO = ROOT / "portfolio" / "portfolio.json"
OUT = ROOT / "knowledge" / "cross-cutting" / "portfolio-health.md"

# ponytail: FSM guards from docs/beacon/v0.1.0/state-model.md (green --14d--> yellow --30d--> red).
# AC-001 的 "7天" 措辞与 FSM 14 天 guard 存在原文歧义；以 FSM 状态机为准，改口径只动这两个常量。
GREEN_MAX_DAYS = 14
YELLOW_MAX_DAYS = 30


def classify(age_days, build_ok=True):
    if not build_ok:
        return "red"
    if age_days < GREEN_MAX_DAYS:
        return "green"
    if age_days < YELLOW_MAX_DAYS:
        return "yellow"
    return "red"


def main(today=None):
    today = today or date.today()
    data = json.loads(PORTFOLIO.read_text(encoding="utf-8"))
    buckets = {"green": [], "yellow": [], "red": []}
    for key, project in data["projects"].items():
        last = project.get("last_activity")
        age = (today - date.fromisoformat(last)).days if last else 9999
        health = classify(age, project.get("build_ok", True))
        project["health"] = health
        buckets[health].append((key, age))
    data["updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    PORTFOLIO.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    lines = [f"# Portfolio Health — {today.isoformat()}", ""]
    for health in ("green", "yellow", "red"):
        names = ", ".join(f"{k}({a}d)" for k, a in sorted(buckets[health])) or "none"
        lines.append(f"- {health}: {names}")
    lines += [
        "",
        f"阈值: green<{GREEN_MAX_DAYS}d / yellow<{YELLOW_MAX_DAYS}d / red≥{YELLOW_MAX_DAYS}d 或构建失败 (state-model.md)",
        "数据源: portfolio/portfolio.json (last_activity, build_ok)",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    if "--check" in sys.argv:
        assert classify(0) == "green"
        assert classify(13) == "green"
        assert classify(14) == "yellow"
        assert classify(29) == "yellow"
        assert classify(30) == "red"
        assert classify(1, False) == "red"
        print("portfolio_health: ok")
    else:
        main()
