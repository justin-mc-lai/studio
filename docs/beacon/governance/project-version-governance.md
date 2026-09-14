---
schema_version: "1.0"
project_root: "."
topology_kind: "single_repo"
default_execution_service: "studio"
transaction_id: "tx-project-governance-4982690e0e18af98"
committed_at: "2026-09-14T02:12:47.706292+00:00"
source_hash: "4982690e0e18af98db7d50064f8413ae431a21f13639f76ec0417b8e413339a7"
event_type: "freeze-version-contract"
parser_contract: "beacon-project-governance-v1"
---

# Project Version Governance

- project_root: `.`
- topology_kind: `single_repo`
- default_execution_service: `studio`

## Service Bindings
- `studio` repo=`.` role=`control-plane` writable=`true` worktree_policy=`follow-repo-root`

## Version Contracts

### v0.1.0
- participating_services: `studio`
- branch_guard_mode: `strict`
- validation_state: `active`
- per_service_canonical_branch:
  - `studio`: `beacon/v0.1.0`
- truth_canonical: `main`
- branch_governance_template: `standard-feature`
- previous_version_baseline_branch: `main`
- next_version_feature_branch: `beacon/v0.1.0/<feature-slug>`
- worktree_mode: `dedicated`
- worktree_path: `.beacon/worktrees/v0.1.0`
- require_workspace_admission: `true`
- merge_direction_policy: `master->beacon/v0.1.0`
- merge_direction_policy: `beacon/v0.1.0->uat`
- forbidden_directions: `uat->beacon/v0.1.0`
- forbidden_directions: `uat_as_feature_base`
