# Phase 0 Data Model: Foundation, Directory Skeleton & Living Documentation

**Feature**: `specs/001-phase0-foundation-and-docs` | **Date**: 2026-10-26

Every entity below is derived from [spec.md](./spec.md) requirements. Nothing is persisted in a
database; all state is either on the filesystem or inside a generated artifact or manifest.

---

## 1. Domain

A numbered top-level area of the ecosystem.

| Field | Type | Required | Description |
|---|---|---|---|
| `number` | integer | yes | Display prefix: 0, 1, 10, 20, 30, 90, 99 |
| `id` | string | yes | Directory name, for example `00_global_system` |
| `purpose` | string | yes | One sentence, reused verbatim in generated tables |
| `owner` | role identifier | yes | Exactly one accountable role (FR-038) |
| `scope` | enum | yes | `active`, `archive`, or `tooling` |
| `inventory_default` | enum | yes | `counted` or `excluded` |

Validation rules:

- The seven product domains plus `specs` are required; `.specify`, `.agents`, `.claude`, and
  `.opencode` are `tooling` and are excluded from counts (FR-029).
- `99_archive` is `archive`, so its directories never appear in active figures (FR-029, FR-036).
- `owner` must resolve to a role card path or to a documented seat whose card is planned by a
  later phase; in Phase 0 all seven owners resolve to existing cards (FR-038, SC-014).

Relationship: a domain contains zero or more structure entries and directory nodes.

---

## 2. Structure Entry

One declared expectation inside `01_templates/structure_manifest.yaml`. This is the contract
between scaffolding and verification.

| Field | Type | Required | Description |
|---|---|---|---|
| `path` | string | yes | Workspace-relative, POSIX separators, no trailing slash |
| `owner` | role identifier | yes | Accountable role for that directory |
| `purpose` | string | yes | Short noun phrase, used in the architecture anatomy |
| `phase` | integer | yes | Phase that populates it, 0 through 8 |
| `scope` | enum | yes | `active`, `placeholder`, `archive`, or `tooling` |
| `required` | boolean | yes | If true, absence is drift |

Validation rules:

- Paths are unique after case-insensitive comparison (R14).
- Every path's parent must also be declared, except for a domain root.
- Naming law from FR-008: numbered prefix where the roadmap specifies one, otherwise lowercase
  underscore-separated words, no spaces, no trailing punctuation.
- `phase` 0 means "exists empty at baseline"; higher phases mean "planned, may be absent now" and
  are excluded from required-drift reporting until their phase gate.
- Quarantined paths are not declared here; the archive tree is derived from the manifest
  (Section 8), which remains the sole authority (FR-036).

---

## 3. Directory Node

A directory as observed on disk, reconciled against its structure entry.

| Field | Type | Description |
|---|---|---|
| `path` | string | Workspace-relative, display spelling preserved |
| `domain` | string | Owning domain id |
| `state` | enum | `planned`, `empty`, `populated`, `unexpected` |
| `direct_file_count` | integer | Files directly inside, after exclusions |
| `subtree_file_count` | integer | Files anywhere below |
| `owner` | role identifier | From the structure entry, else unassigned |

State transitions:

```text
planned ──scaffold──► empty ──first file──► populated
   │                    │
   └──── missing ───────┴──► DRIFT (check mode reports, apply never deletes)

unexpected (exists on disk, absent from manifest) ──► DRIFT
```

Rules:

- `empty` means no file anywhere in the subtree (R4).
- `unexpected` is reported but never removed by any tool (FR-009 forbids deletion).
- A `planned` node whose `phase` is greater than 0 is not drift until that phase's gate.

---

## 4. Documentation Artifact

A governed document with a known audience and owner.

| Field | Type | Description |
|---|---|---|
| `path` | string | Workspace-relative |
| `audience` | enum | `commander`, `agent`, `human-collaborator` |
| `owner` | role identifier | Accountable role |
| `generated` | boolean | Fully generated or hand-written |
| `regions` | list of Protected Region | Empty when fully hand-written |
| `required` | boolean | Absence is drift (FR-012 to FR-016) |

Required artifacts at baseline: `README.md`, `ARCHITECTURE.md`,
`PROJECT_GENESIS_AND_DISCUSSIONS_DRAFT.md`, `CLAUDE.md`,
`00_global_system/agent_registry/DIRECTORY.md`, and the three directives under
`00_global_system/directives/`.

| Artifact | Generated | Owner |
|---|---|---|
| `DIRECTORY.md` | fully generated | documentation guardian |
| `ARCHITECTURE.md` | hand-written with one generated region | documentation guardian for the region |
| `README.md` | hand-written | global chief of staff |
| `CLAUDE.md` | hand-written | prime interface |
| Genesis draft | hand-written | documentation guardian |
| Three directives | hand-written | prime interface |

---

## 5. Protected Region

A writable slice inside a hand-written artifact.

| Field | Type | Description |
|---|---|---|
| `id` | string | For example `architecture-telemetry` |
| `artifact` | path | Owning file |
| `start_marker` | string | Exact line `<!-- AUTO-STATS-START -->` |
| `end_marker` | string | Exact line `<!-- AUTO-STATS-END -->` |
| `generator` | path | `00_global_system/scripts/doc_guardian.py` |
| `owner` | role identifier | documentation guardian (FR-038) |
| `payload` | enum | `telemetry-list` |

Parsing rules (fail closed, FR-027):

1. Exactly one start marker line and one end marker line.
2. Start appears before end.
3. Markers occupy their own line with no leading or trailing characters other than line endings.
4. Regions do not nest.
5. Any violation aborts before writing, exit code 2.

---

## 6. Inventory Snapshot

The measured state at one run. Exists in memory and in console or JSON output; only a subset is
written into generated artifacts.

| Field | Type | Description |
|---|---|---|
| `measured_at` | ISO date | Date only; written only when a figure changes (R3) |
| `active_directories` | integer | Directories with at least one direct file |
| `placeholder_directories` | integer | Declared directories with no files in subtree |
| `live_role_cards` | integer | `AGENT.md` files outside the archive |
| `quarantined_role_cards` | integer | Count from the quarantine manifest, not the filesystem |
| `skill_bundles` | integer | `SKILL.md` files |
| `specification_features` | integer | Matching directories under `specs/` |
| `per_domain` | map | Domain id to active, placeholder, cards, bundles |
| `elapsed_ms` | integer | Runtime diagnostics; console and JSON only |

Rules:

- Counts are computed once per run, never accumulated across runs.
- No figure may be entered by a human (assumptions: counts come from the filesystem).
- `quarantined_role_cards` is read from the manifest, so the archive remains authoritative even
  if files are manually moved (FR-036).

---

## 7. Role Seat

An occupied position in the authority tree.

| Field | Type | Description |
|---|---|---|
| `role_id` | string | For example `documentation_guardian` |
| `level` | integer | 0 Commander, 1 prime, 2 executive, 3 manager, 4 worker |
| `reports_to` | role identifier | Exactly one supervisor (Principle I) |
| `scope` | string | Pod id, `global`, or `personal` |
| `card_path` | string | Path to `AGENT.md` |
| `owned_regions` | list of region ids | Generated regions this role writes |

Validation rules:

- `reports_to` is mandatory and singular; a seat with zero or multiple supervisors is invalid.
- A role may own zero or more generated regions, but a region has exactly one owner (FR-038).
- The documentation guardian is level 2, scope `global`, reports to the prime interface, and owns
  `architecture-telemetry` (FR-037, FR-038).
- Cards quarantined under Section 8 keep their `role_id` and remain resolvable by it (FR-034).

---

## 8. Quarantine Manifest and Entry

Canonical record of the archive move. JSON at
`99_archive/cold_storage/quarantined_worker_seats/MANIFEST.json`.

Manifest fields:

| Field | Type | Description |
|---|---|---|
| `schema_version` | integer | 1 |
| `generated_at` | ISO date | Date of first successful apply |
| `workspace_root_name` | string | Final path component only, no absolute path |
| `counts` | map | `quarantined`, `restored`, `files`, `bytes` |
| `entries` | list | Sorted by `original_path` |

Entry fields:

| Field | Type | Description |
|---|---|---|
| `role_id` | string | Directory name of the seat |
| `pod_id` | string | Owning pod |
| `department` | string | Relative department path |
| `original_path` | string | Workspace-relative path before the move |
| `archived_path` | string | Workspace-relative path inside the archive |
| `files` | list | Each with `path` and `sha256` |
| `file_count` | integer | Length of `files` |
| `status` | enum | `QUARANTINED` or `RESTORED` |
| `moved_at` | ISO date | Date of the move |

State transitions:

```text
CANDIDATE --apply--> QUARANTINED --restore--> RESTORED
     │                    │
     └─ refused if destination occupied, path escapes pod, or entry already recorded
```

Rules:

- Apply is idempotent: an entry already recorded as `QUARANTINED` is skipped, not re-moved.
- Hashes are computed before the move and verified after; a mismatch is a hard failure.
- Restore refuses when the original path is occupied and writes nothing.
- Entries are the only authority for how many seats were quarantined (FR-036, SC-013).

---

## 9. Secret Finding

Transient result of the credential scan. Never persisted.

| Field | Type | Description |
|---|---|---|
| `path` | string | Workspace-relative file |
| `line` | integer | 1-based line number |
| `family` | enum | `private-key`, `cloud-key`, `bearer-token`, `bot-token`, `high-entropy` |

Rules: the matched value is never stored, printed, or included in JSON output (FR-032, FR-018).

---

## 10. Specification Feature

A reserved work slot under `specs/`.

| Field | Type | Description |
|---|---|---|
| `number` | string | Three-digit prefix |
| `short_name` | string | Remaining directory name after the prefix |
| `path` | string | Workspace-relative |
| `has_spec` | boolean | `spec.md` present |
| `has_plan` | boolean | `plan.md` present |
| `has_tasks` | boolean | `tasks.md` present |

Rules: a feature with a stub specification still counts as reserved, not completed (assumptions).
Counted from directory names, so an empty or partially stubbed feature is still visible (SC-007).

---

## Invariant summary

| Invariant | Requirement |
|---|---|
| Exactly one supervisor per seat | Principle I, FR-037 |
| Exactly one owner per generated region | FR-038, SC-014 |
| Every declared path exists or is reported | FR-009, SC-001 |
| No deletion by any tool except the recorded quarantine move | FR-009, FR-034 |
| Prose outside a region is byte-identical across runs | FR-024, SC-005 |
| Two runs with no change are byte-identical | FR-025, FR-026, SC-004 |
| Archive excluded from active counts, counted separately | FR-029, FR-036, SC-013 |
| Credential values never reproduced | FR-018, FR-032, SC-008 |
| Pod core names use exactly one contract | FR-039, SC-015 |
| No cross-pod links or absolute references | FR-011, FR-019 |
