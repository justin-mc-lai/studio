# Test Cases: studio

## Overview

**Feature**: studio
**Test Type**: ALL
**Version**: v0.1.0
**Generated**: 2026-09-01 13:30
**Requested Mode**: auto
**Effective Mode**: host
**Fallback Reason**: N/A
**Memory Context**: N/A
**AC Matrix JSON**: docs/beacon/v0.1.0/.machine/qa/studio.ac-test-matrix.json
**QA9 Matrix JSON**: docs/beacon/v0.1.0/.machine/qa/studio.qa9-matrix.json
**Story Scenario Map JSON**: docs/beacon/v0.1.0/.machine/qa/studio.story-scenario-map.json
**Prototype Plan Present**: False
**Prototype Coverage Present**: False
**Prototype Navigation Contract**: False
**Prototype Interaction Contract**: False

---

## Executable AC Test Matrix

| AC ID | TC ID | Layer | Command | Assertion | Evidence Path |
|-------|-------|-------|---------|-----------|---------------|
| AC-001 | TC-001 | unit | `python3 -m pytest -q -k unit --junitxml "${BEACON_JUNIT_PATH:-.beacon/junit.xml}"` | studio core flow works | `.beacon/evidence/test-results/studio/TC-001.json` |

---

## Execution Results

| Test ID | Result | Notes |
|---------|--------|-------|
| TC-001 | Pending | from AC-001 |
