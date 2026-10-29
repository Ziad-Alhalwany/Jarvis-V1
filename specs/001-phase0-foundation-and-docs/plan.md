# Implementation Plan: Phase 0 - Foundation, Federated Directory Skeleton & Living Documentation

**Branch**: `001-phase0-foundation-and-docs` | **Date**: 2026-10-26 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-phase0-foundation-and-docs/spec.md`

## Summary

Deliver the structural baseline that the remaining seven phases populate, and make it
self-describing and drift-proof. Four moves:

1. Reconcile the skeleton that already exists on disk against a declarative structure manifest,
   so the delivered tree is exactly the documented tree.
2. Quarantine the 136 pre-existing worker seats into the archive with a hash-verified manifest,
   keeping the live pods at shell, pod core, leadership, and manager depth.
3. Add the sixth global executive seat, the documentation guardian, as the single accountable
   owner of generated documentation and drift verification.
4. Generate the inventory and the architecture telemetry block from filesystem truth through a
   deterministic, fail-closed refresh utility, then correct the root documentation so it names
   only existing or explicitly planned artifacts and exactly one pod-core contract.

Technical approach: three small Python 3.11 utilities over one declarative YAML manifest, with
PyYAML as the single approved dependency. No network at run time, no model calls, no database.
Scaffolding, refresh, and quarantine are separate executables because they carry different risk:
verification must never be able to mutate, and the only destructive move must be auditable and
reversible.

## Technical Context

**Language/Version**: Python 3.11+ (CPython), standard library plus one approved package

**Primary Dependencies**: `PyYAML>=6.0,<7.0` for manifest parsing, pinned in
`00_global_system/scripts/requirements.txt`. PyYAML is explicitly pre-approved by the
constitution's technology constraints. Everything else is the standard library: `pathlib`,
`argparse`, `json`, `hashlib`, `datetime`, `logging`, `tempfile`, `os`, `re`, `unittest`

**Storage**: filesystem only. Generated Markdown plus JSON manifests. No database, no queue, no
external service

**Testing**: `unittest` discovery under `00_global_system/scripts/tests/`, temp-directory
fixtures, golden-file comparisons for byte-level idempotency

**Target Platform**: Windows 11 host, workspace path contains a space, case-insensitive
filesystem, no administrator rights, no network access at run time

**Project Type**: single repository indexed by organizational domain rather than by source
layout. Tooling sits under `00_global_system/scripts/`; pods and their phases remain untouched

**Performance Goals**: full refresh under 2 seconds at 500+ directories; scaffold idempotent in
under 1 second; quarantine of 136 seats under 5 seconds; no operation opens a file it does not
need

**Constraints**: writes confined to the workspace root; no deletion outside the documented
quarantine move; single writer enforced; fail closed on any ambiguity; zero model tokens;
generated tables ASCII-safe and stable-width; no `.gitkeep` files

**Scale/Scope**: 7 numbered domains, 8 specification features, 2 venture pods, 5 pillar pods,
6 global executive seats, roughly 67 live role cards after quarantine, 2 generated artifacts

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Gate question | Verdict | Evidence |
|---|---|---|---|
| I. Dual topology | Does this work create exactly one supervisor per role and preserve a single escalation path? | PASS | FR-037 adds one seat with one supervisor; FR-038 makes every generated region single-owner; no new channel to the Commander |
| II. Federated pods, 100% detachable | Does this work introduce a cross-pod dependency or an absolute reference? | PASS | FR-011 forbids links; FR-019 keeps references relative; quarantine leaves no pointer behind |
| III. Standard shell and context economy | Does this work add, rename, or omit a pod shell file? | PASS | No shell file is authored here; the manifest documents the shell without creating content |
| IV. Memory facade and zero-loss queue | Does this work bypass the memory facade or write durable entities? | PASS | Documentation and inventory only; FR-030 forbids reading pod state or card bodies |
| V. Quad-shield engine | Does this work write task state or exceed a WIP limit? | PASS | No task data is created or modified |
| VI. Self-evolution and scorecards | Does this work promote skills or patch agents without approval? | PASS | Nothing is staged or promoted; the guardian writes only its two regions |
| VII. Tiered routing, frugal engineering | Does this work spend model tokens on a deterministic outcome? | PASS | Counting, hashing, sorting, and writing are pure Python; zero model calls |
| VIII. Runtime-agnostic fabric | Does this work name a vendor or bind a runtime? | PASS | FR-016 and FR-022 keep prose vendor-neutral; FR-039 makes `runtime_adapter.yaml` the only binding point |

**Gate result: PASS. No violations.** Complexity Tracking is not required.

**Post-design re-check: PASS.** The design adds three utilities and one declarative manifest,
introduces no runtime coupling, adds no model calls, and confines writes to two generated
artifacts plus the documented archive move.

## Project Structure

### Documentation (this feature)

```text
specs/001-phase0-foundation-and-docs/
├── spec.md              # Feature specification (39 FRs, 15 SCs)
├── plan.md              # This file
├── research.md          # Phase 0 decisions and rejected alternatives
├── data-model.md        # Entities, validation rules, state transitions
├── quickstart.md        # Validation scenarios mapped to success criteria
├── contracts/
│   ├── doc-guardian-cli.md
│   ├── structure-manifest.md
│   ├── quarantine-cli.md
│   └── inventory-artifacts.md
├── checklists/
│   └── requirements.md
└── tasks.md             # Created by /speckit-tasks
```

### Source Code (repository root)

```text
00_global_system/
├── directives/
│   ├── Ziad_Cognitive_DNA.md          # Adopted; prose only, no structural change
│   ├── Global_Governance_Rules.md     # Adopted; no structural change
│   └── Detachability_Standard.md      # Canonical pod-core contract (FR-039)
├── agent_registry/
│   ├── DIRECTORY.md                   # Regenerated by doc_guardian.py
│   └── cards/                         # Existing seed cards, untouched
└── scripts/
    ├── requirements.txt               # PyYAML>=6.0,<7.0
    ├── _shared.py                     # Root resolution, path rules, atomic write, lock
    ├── _manifest.py                   # Manifest load and strict schema validation
    ├── _inventory.py                  # Measurement, counting, credential scan
    ├── _render.py                     # Table and region rendering, byte-stable output
    ├── scaffold_structure.py          # Materializes the manifest; never deletes
    ├── doc_guardian.py                # CLI, region splice, atomic writes, exit codes
    ├── quarantine_worker_seats.py     # Hash-verified archive move; --restore
    └── tests/
        ├── test_shared.py
        ├── test_manifest.py
        ├── test_inventory.py
        ├── test_render.py
        ├── test_scaffold_structure.py
        ├── test_doc_guardian.py
        ├── test_quarantine_worker_seats.py
        └── fixtures/                  # Temp-tree builders, no workspace data copied

01_templates/
└── structure_manifest.yaml            # Single source of truth for the expected tree

30_infrastructure/executive_command/
└── documentation_guardian/
    └── AGENT.md                       # Sixth global seat card (FR-037)

99_archive/cold_storage/quarantined_worker_seats/
├── MANIFEST.json                      # Generated, hash-verified, sole authority
└── <pod>/<department>/workers/<role>/ # Moved seats, byte-identical

ARCHITECTURE.md                        # Telemetry region plus full anatomy, corrected
README.md                              # Adopted and amended
PROJECT_GENESIS_AND_DISCUSSIONS_DRAFT.md  # Adopted, discrepancy note appended
CLAUDE.md                              # Adopted, verified against FR-016
.gitignore                             # New
.env.example                           # New
```

**Structure Decision**: The repository is indexed by organizational domain because the
constitution fixes the numbered top-level directories as law. Tooling therefore lives with its
domain (`00_global_system/scripts/`), tests sit beside the code they test, and the expected tree
is declared once in `01_templates/` because templates are the cloning blueprints that Phase 3
will extend. No `src/`, `backend/`, or `frontend/` split applies: this phase ships no server.

## Design Decisions

Full rationale and rejected alternatives are in [research.md](./research.md). The five decisions
that shape the task list:

1. **Three utilities, not one.** Scaffold must never delete, refresh must never write outside two
   regions, quarantine is the only mutating move. A single script with mode flags would put the
   destructive path in the same executable as verification. Rejected: one `doc_guardian.py`
   with an operation switch.
2. **Declarative structure manifest.** `01_templates/structure_manifest.yaml` declares every
   expected directory with its owning role, purpose, phase, and inventory scope. Scaffold
   materializes it; refresh verifies against it. Rejected: parsing `ARCHITECTURE.md` prose,
   which is human-formatted and fragile, and hardcoding the tree in Python, which drifts.
3. **No clock in generated output.** The pre-existing `Last Synchronized: 2026-10-26 18:00:00`
   makes byte-level idempotency impossible. The telemetry region carries `Last verified` as a
   date, refreshed only when a measured value changes. Unchanged runs produce identical bytes and
   do not even rewrite the files.
4. **Quarantine is a verified move, not a delete.** Each seat moves with a per-file SHA-256 into
   the archive, recorded in a manifest that supports single-seat restore. Phases 5 and 6
   regenerate from templates; restore exists for emergencies and for audits.
5. **Documentation is adopted, not rewritten.** `README.md`, `CLAUDE.md`, and the genesis draft
   already exist and are largely aligned. The plan amends them surgically and rewrites only the
   architecture telemetry region plus the missing anatomy sections.

## Risks and Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Quarantine interrupted mid-run | Half-moved tree, ambiguous inventory | Per-seat verification and recording; re-running skips recorded entries; `--plan` first shows the exact move set |
| A human edits inside a generated region | Silent wrong inventory | `--check` at every phase gate; mismatch exits non-zero with expected and actual values |
| Table width changes between runs | Non-idempotent output | Widths computed from data, no post-processing; golden-file test asserts byte identity |
| Empty placeholder directories are invisible to version control | Missing-but-expected drift | No `.gitkeep`; scaffold recreates them; check mode reports them as drift until re-materialized |
| Archived seats counted as live workforce | Inventory overstates headcount | FR-036 separates archived seats from active counts, and the region reports both |
| Rewritten prose loses the Commander's voice | Style regression | Cognitive DNA rules govern every rewritten line: no em-dash overuse, no robotic openings, direct cadence |
| Two refreshes run at once | Interleaved writes, corrupted table | Lock file with pid and host; stale lock reclaimed with a warning; live lock exits 3 |

## Complexity Tracking

> **No constitutional violations.** The three-utility split and the declarative manifest are
> risk-reduction choices, justified above. No violation entry required.

## Phase Outputs

- **Phase 0 research**: [research.md](./research.md), every Technical Context unknown resolved,
  no `NEEDS CLARIFICATION` remaining.
- **Phase 1 design**: [data-model.md](./data-model.md),
  [contracts/](./contracts/), [quickstart.md](./quickstart.md).
- **Phase 2 tasks**: not created here. Run `/speckit-tasks`.
