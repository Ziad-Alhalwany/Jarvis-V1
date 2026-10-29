---

description: "Task list for Phase 0: Foundation, Federated Directory Skeleton & Living Documentation"

---

# Tasks: Phase 0 - Foundation, Federated Directory Skeleton & Living Documentation

**Input**: Design documents from `/specs/001-phase0-foundation-and-docs/`

**Prerequisites**: [plan.md](./plan.md), [spec.md](./spec.md), [research.md](./research.md),
[data-model.md](./data-model.md), [contracts/](./contracts/), [quickstart.md](./quickstart.md)

**Tests**: MANDATORY. The tasks template treats tests as optional, but constitution Section 3
requires failing tests before implementation for every deterministic engine (WSJF, scoring, IDs,
file counting, drift detection). Tests are therefore written first in each phase and must fail
before the implementation task starts.

**Organization**: Tasks are grouped by user story. Each story is independently testable.

## How to execute this list

Read this before starting any task. These rules override convenience.

1. Work tasks in ID order unless a task is marked `[P]`. Never skip a failing verification.
2. Every file path is workspace-relative and exact. Do not invent names, rename directories, or
   "improve" the layout. The constitution's directory law makes names load-bearing.
3. Never delete, rename, or move anything, with one exception: T022's quarantine apply.
4. Never write outside the files a task names. In particular, never edit
   `.specify/memory/constitution.md`, `specs/*/spec.md`, or existing agent cards.
5. No placeholder code. `TODO`, `FIXME`, bare `pass`, `...`, and `NotImplementedError` are banned
   (CLAUDE.md, zero placeholders).
6. Every script: Python 3.11+, type hints, structured `logging`, explicit error handling, no
   network, no model calls, no subprocess.
7. Run commands from the workspace root. Quote every path, because the root contains a space.
8. A task is complete only when its verification is run and its output noted. Do not tick a box
   because the code "looks right".

## Format: `[ID] [P?] [Story] Description`

- **[P]**: safe to run in parallel with other `[P]` tasks in the same phase (different files)
- **[Story]**: US1, US2, US3, US4, mapping to spec.md user stories
- Every task names the exact file it creates or modifies

## Path Conventions

This repository has no `src/` or `tests/` root. Paths are repository-relative and follow the
numbered-domain law. Tooling lives in `00_global_system/scripts/`; its tests live in
`00_global_system/scripts/tests/`.

## Hard constraints (violating any of these fails the phase)

| Constraint | Source |
|---|---|
| Region markers are exactly `<!-- AUTO-STATS-START -->` and `<!-- AUTO-STATS-END -->` | FR-014 |
| Exit codes: 0 ok, 1 drift or refusal, 2 config error, 3 lock held | contracts |
| Only two generated artifacts: `DIRECTORY.md` and the `ARCHITECTURE.md` region | FR-024 |
| Counts come from the filesystem; quarantined count comes from the manifest | FR-036 |
| No absolute paths in generated output; no credential values anywhere | FR-019, FR-032 |
| No worker seats in the delivered live tree | FR-035 |
| One new agent card only: the documentation guardian | FR-037 |
| Pod core names are the detachability standard's set | FR-039 |

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Toolchain, dependency pin, secrets hygiene, and test scaffolding. No product code.

- [ ] T001 Verify the toolchain before writing anything: run `python --version` (3.11 or newer)
  and `python -c "import yaml; print(yaml.__version__)"` (6 or newer). If PyYAML is missing, run
  `python -m pip install "PyYAML>=6.0,<7.0"`. Record both versions in the task note. Creates no
  files.
- [ ] T002 Create `00_global_system/scripts/requirements.txt` with one comment line and exactly one
  requirement: `PyYAML>=6.0,<7.0`. No other packages.
- [ ] T003 [P] Create `.gitignore` at the workspace root excluding at minimum: `.env`, `*.env`
  with an exception for `!.env.example`, `*.db`, `*.db-wal`, `*.db-shm`, `**/private_id.yaml`,
  `__pycache__/`, `*.py[cod]`, `.vs/`, `.pytest_cache/`, `Thumbs.db`, `.DS_Store`, `~$*`,
  `*.tmp`. Header comment must say why each group is excluded. FR-017.
- [ ] T004 [P] Create `.env.example` at the workspace root with variable names and empty values
  only: `TELEGRAM_BOT_TOKEN=`, `DISCORD_BOT_TOKEN=`, `OPENAI_API_KEY=`, `ANTHROPIC_API_KEY=`,
  `OLLAMA_BASE_URL=`, `OBSIDIAN_VAULT_PATH=`, `APPFLOWY_API_URL=`, `APPFLOWY_API_KEY=`,
  `POSTGRES_DSN=`. No real values, no placeholder secrets that look real. FR-017, FR-018.
- [ ] T005 [P] Create package markers `00_global_system/scripts/tests/__init__.py` and
  `00_global_system/scripts/tests/fixtures/__init__.py`. Test command, to be used throughout:
  `python -m unittest discover -s "00_global_system/scripts/tests" -v`.
- [ ] T006 [P] Create `00_global_system/scripts/tests/fixtures/trees.py` with two helpers:
  `build(root, paths)` creating directories from relative POSIX path strings, and
  `write(root, relpath, text)` writing UTF-8 files with parent creation. Both accept and return
  `pathlib.Path`. Must never touch the real workspace.

**Checkpoint**: `python -c "import yaml"` succeeds and the test discovery command runs with zero
tests collected.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Two shared modules that every utility depends on. No user story can start until both
pass their tests.

**⚠️ CRITICAL**: US1 through US4 all import these modules.

- [ ] T007 Write failing tests in `00_global_system/scripts/tests/test_shared.py` for the module
  `00_global_system/scripts/_shared.py`. Cover: (a) root resolution walks up to the directory
  containing both `00_global_system` and `.specify`; (b) `to_posix` converts backslashes and
  collapses duplicated separators; (c) `is_excluded` is true for `.git`, `.vs`, `.agents`,
  `.claude`, `.opencode`, `.specify`, `__pycache__`, `node_modules`, `.pytest_cache`, `Thumbs.db`,
  `.DS_Store`, `~$x`, `x.tmp`; (d) `atomic_write_text` leaves no temporary file behind and
  replaces content; (e) `Lock` reports busy while a live lock exists, and reclaims a lock older
  than 300 seconds or held by a dead pid on the same host. Run the suite and confirm these fail.
- [ ] T008 Implement `00_global_system/scripts/_shared.py` to satisfy T007. Required public names:
  `find_workspace_root(start: Path) -> Path`, `to_posix(path: str) -> str`,
  `is_excluded(name: str) -> bool`, `EXCLUDED_NAMES: frozenset[str]`,
  `atomic_write_text(path: Path, text: str) -> None`, and `class Lock` usable as a context
  manager with `acquire()`, `release()`, and `stale_after_seconds = 300`. No prints; use
  `logging`. Verification: `python -m unittest "00_global_system/scripts/tests/test_shared.py" -v`
  passes.
- [ ] T009 Write failing tests in `00_global_system/scripts/tests/test_manifest.py` for
  `00_global_system/scripts/_manifest.py`, covering the nine validation rules in
  `contracts/structure-manifest.md`: `schema_version` equals 1; duplicate domain id or entry path
  under case-insensitive comparison rejected; entry path must start with a declared domain id;
  undeclared parent rejected; naming law enforced (lowercase, underscore-separated, numbered
  prefix allowed); absolute path rejected; `..` segment rejected; unknown top-level key rejected;
  `yaml.YAMLError` surfaces line and column. Fixtures build temporary YAML strings, never touching
  `01_templates/structure_manifest.yaml`.
- [ ] T010 Implement `00_global_system/scripts/_manifest.py` using `yaml.safe_load`. Public names:
  `load_manifest(path: Path) -> dict`, `class ManifestError(Exception)` carrying `path`, `line`,
  and `column` when known. Validation failures raise `ManifestError`. No partial manifest is ever
  returned. Verification: T009 tests pass.

**Checkpoint**: Both shared modules import cleanly and their tests are green.

---

## Phase 3: User Story 1 - Every future artifact has a canonical home (Priority: P1) 🎯 MVP

**Goal**: The declared tree exists, is idempotent to materialize, and the pre-existing worker
seats are quarantined with a verifiable manifest.

**Independent Test**: `scaffold_structure.py --check` exits 0, `quarantine_worker_seats.py
--verify` exits 0, and no directory named `workers` remains under `10_pillars/` or
`20_businesses/`.

### Tests for User Story 1

- [ ] T011 [P] [US1] Write failing tests in
  `00_global_system/scripts/tests/test_scaffold_structure.py`: creates every missing directory;
  a second run reports `created=0`; an existing directory with a file is untouched; a file sitting
  where a directory belongs causes exit 1 and no further writes; `--check` exits 1 listing missing
  paths; `--check` on a complete fixture exits 0; `--json` emits the documented keys.
- [ ] T012 [US1] Implement `00_global_system/scripts/scaffold_structure.py` with `--check`,
  `--json`, and `--root`, consuming `_manifest.py` and `_shared.py`. It creates directories only,
  in sorted path order, and never deletes, renames, or overwrites. Exit codes 0, 1, 2, 3 as
  contracted. Verification: T011 passes.
- [ ] T013 [US1] Create `01_templates/structure_manifest.yaml` with `schema_version: 1`,
  `naming_law`, and the complete `domains:` block for the seven numbered domains plus `specs`.
  Each domain needs `id`, `number`, `purpose`, `owner`, `scope`, `inventory`. Owners:
  `00_global_system` jarvis_prime, `01_templates` documentation_guardian, `10_pillars`
  personal_chief_of_staff, `20_businesses` jarvis_prime, `30_infrastructure` jarvis_prime,
  `90_dashboard` jarvis_prime, `99_archive` documentation_guardian, `specs`
  global_ops_prioritizer.
- [ ] T014 [US1] Add manifest `entries:` for `00_global_system` (directives, memory_layer,
  queue_vault with staging_media_inbox, master_task_engine, agent_registry with cards,
  learning_loop with its three staging folders, mcp_servers, plugins_and_integrations,
  hooks_and_guardrails, skills with its three bundles, reference_library, scripts, scripts/tests)
  and for `01_templates` (the six blueprint folders).
- [ ] T015 [US1] Add manifest entries for `30_infrastructure` (executive_command with all six
  officer seats including documentation_guardian plus jarvis_prime, the_cafe with its three
  event folders, channels_bridge with three bridges, brain_bindings), `90_dashboard` (four
  sub-areas), `99_archive` (cold_storage and quarantined_worker_seats), and `specs` (the eight
  feature folders).
- [ ] T016 [US1] Add manifest entries for `10_pillars`, all five pods: shell directories
  (`identifiers`, `_pod_core` with its five sub-areas, `00_pillar_lead`, the four capability
  folders with their documented sub-areas, `swipe_files_and_benchmarks`, `skills`,
  `sessions_traces`, `reports_deliverables`). Do NOT declare any `workers` directory, because
  T022 removes them. Use `ARCHITECTURE.md` sections 3.4 and 3.5 plus `PLAN.md` Part 3 as the
  enumeration source, and end at capability level.
- [ ] T017 [US1] Add manifest entries for `20_businesses`, both ventures: shell directories,
  `_pod_core` five sub-areas, `00_c_suite_leadership` with its six seats plus `strategy_and_okrs`,
  the seven departments with `manager`, `playbooks_and_sops`, and `active_tasks` where documented,
  plus the shared sub-areas. Do NOT declare `workers`. Source: `ARCHITECTURE.md` section 3.6 and
  `PLAN.md` Part 3.
- [ ] T018 [US1] Validate and materialize: run
  `python "00_global_system/scripts/scaffold_structure.py" --check`, then apply twice. Expect the
  first apply to create only what is missing and the second to report `created=0`. Confirm in the
  note that no existing file was modified.
- [ ] T019 [P] [US1] Write failing tests in
  `00_global_system/scripts/tests/test_quarantine_worker_seats.py`: `--plan` writes nothing;
  `--apply` moves seats and writes `MANIFEST.json` with sorted entries and per-file SHA-256; a
  second `--apply` skips recorded entries; `--restore` returns one seat byte-identically and flips
  status to `RESTORED`; occupied destination refuses with exit 1; a `..` path escape refuses;
  unreadable manifest exits 2.
- [ ] T020 [US1] Implement `00_global_system/scripts/quarantine_worker_seats.py` per
  `contracts/quarantine-cli.md`: modes `--plan`, `--apply`, `--restore ROLE_ID`, `--verify`, plus
  `--json` and `--root`. Detection rule: `<domain>/<pod>/<department>/workers/<role_id>` where
  `<role_id>` contains `AGENT.md`. Moves each department's `workers` directory as a unit, records
  per-seat entries, hashes before and after, refuses on collision. Exit codes 0, 1, 2, 3.
  Verification: T019 passes.
- [ ] T021 [US1] Run `--plan` against the real workspace. Expected: 136 candidate seats across 35
  `workers` directories, 0 collisions, 0 refusals. If the numbers differ, stop and report the
  diff before applying.
- [ ] T022 [US1] Run `--apply`, then `--verify`. Both exit 0. Confirm
  `99_archive/cold_storage/quarantined_worker_seats/MANIFEST.json` exists with 136
  `QUARANTINED` entries.
- [ ] T023 [US1] Verify the delivered tree:
  `Get-ChildItem "10_pillars","20_businesses" -Recurse -Directory -Filter workers` returns
  nothing, and the manifest entry count is 136 sorted by `original_path`. Record both results.
- [ ] T024 [US1] Reconcile completeness against the spec: list every directory under counted
  domains that the manifest does not declare, and every required entry that is missing. Add phase
  0 entries for genuine omissions; for higher-phase entries, confirm they are declared with the
  right phase. The goal is zero undeclared directories and zero unexplained missing ones. SC-001.

**Checkpoint**: The skeleton is declared, materialized, idempotent, and free of worker seats.

---

## Phase 4: User Story 2 - Understand the ecosystem by reading, not asking (Priority: P2)

**Goal**: Root documentation describes reality, distinguishes planned from present, and names one
pod-core contract.

**Independent Test**: A reader answers ten placement questions from the root documents alone, with
zero broken links and zero fabrications left in the telemetry block.

- [ ] T025 [P] [US2] Amend `README.md` to satisfy FR-012: purpose, domain map, phase entry points,
  the refresh command, and links to the constitution and the three directives within two
  navigation steps. Exactly one absolute path (the workspace root); every other reference is
  relative and survives a path containing a space.
- [ ] T026 [US2] Repair `ARCHITECTURE.md` anatomy: the root table lists all seven domains plus
  `specs`; add a dedicated archive domain section (including the quarantine manifest); mark
  `.mcp.json` and `.env` as planned artifacts of later phases rather than present ones. FR-013.
- [ ] T027 [US2] Replace the telemetry region in `ARCHITECTURE.md` with the contracted block:
  owner line first, then generator, `Last verified` as a date, then zeroed figures. Remove the
  fabricated `142`, `3`, `215`, and `18:00:00` claims entirely. Markers stay exactly
  `<!-- AUTO-STATS-START -->` and `<!-- AUTO-STATS-END -->`. FR-014, FR-038.
- [ ] T028 [US2] Correct pod-core naming throughout `ARCHITECTURE.md` to the canonical set:
  `local_review_approvals.md`, `runtime_adapter.yaml`, `pod_agents_directory.md`,
  `pod_scorecard_points.md`, `pod_blockers.md`. Remove every occurrence of `local_plugins.yaml`
  and the `venture_*` alternatives, and do not describe them as optional variants. FR-039,
  SC-015.
- [ ] T029 [US2] Add the documentation guardian to the executive command anatomy in
  `ARCHITECTURE.md`: seat, supervisor, and the two generated regions it owns, plus the archive
  index pointing at the quarantine manifest. FR-037, FR-038.
- [ ] T030 [P] [US2] Append the discrepancy record to
  `PROJECT_GENESIS_AND_DISCUSSIONS_DRAFT.md`: the measured table (cards 142 claimed versus 203
  actual, skills 3 versus 0, directories 215 versus 484, features 8), the note that no generator
  existed while two files claimed machine synchronization, and the decision that the guardian now
  derives figures from the filesystem. Mark the document as a draft superseded by the
  constitution. FR-015, R15.
- [ ] T031 [US2] Verify and, only if needed, amend `CLAUDE.md` against FR-016: boot order,
  mandatory reading list, authority chain, and a pointer to the constitution, with no agent
  product, editor, or vendor named as authoritative. Keep existing section numbering.
- [ ] T032 [US2] Link check every relative reference in `README.md`, `ARCHITECTURE.md`,
  `CLAUDE.md`, and the genesis draft. Resolve every failure, including references from a path with
  a space. Record the count of references checked. SC-006.
- [ ] T033 [US2] Run the placement test using only `README.md` and `ARCHITECTURE.md`. Answer all
  ten and record them: (1) a venture's qualified lead record, (2) a pillar habit metric, (3) the
  scoring rules, (4) the approval queue for irreversible actions, (5) a sanitized Café broadcast,
  (6) the pod core contract, (7) a new skill bundle, (8) decision records, (9) an archived worker
  seat, (10) the generated inventory. Target 10 of 10. SC-002, SC-012.

**Checkpoint**: Root documentation is trustworthy, and no figure in it is unsourced.

---

## Phase 5: User Story 3 - Binding rules sit in one place, independent of any tool (Priority: P3)

**Goal**: Exactly three directives, each naming its bound roles and its constitutional basis, with
no runtime-specific instruction.

**Independent Test**: The directives area holds exactly three files; each cites at least one
principle and names its bound roles; none names a runtime, editor, or vendor as required.

- [ ] T034 [P] [US3] Patch `00_global_system/directives/Ziad_Cognitive_DNA.md`: add a
  `**Governing Law:**` line citing Principles I and VI, and state the bound levels explicitly
  (Level 0 through Level 4 across all pods and the global system). Keep the existing voice rules
  intact. FR-021.
- [ ] T035 [P] [US3] Patch `00_global_system/directives/Global_Governance_Rules.md`: keep the
  existing principle citation (I, IV, V, VI, VII, VIII) and add an explicit bound-roles line
  covering the prime interface, global officers, venture executives, managers, workers, and human
  collaborators. FR-021.
- [ ] T036 [P] [US3] Patch `00_global_system/directives/Detachability_Standard.md`: keep the
  citation of Principles II, III, VIII and add an explicit bound-roles line covering pod leads,
  department managers, and human collaborators inside a pod. FR-021.
- [ ] T037 [US3] Remove runtime-specific wording from the directives. In
  `Detachability_Standard.md` section 2, replace the `runtime_adapter.yaml` comment listing
  specific agent products with neutral wording such as "runtime-agnostic bindings for any agent
  host". Then grep all three files for `Claude`, `Cowork`, `Codex`, `Hermes`, `Ollama`,
  `PowerShell`, and `Windows` and confirm zero matches. FR-022.
- [ ] T038 [US3] Verify the directives contract: the directory contains exactly three `.md` files,
  each cites at least one principle by number, each names bound roles, and none instructs a
  specific tool. Record the evidence line numbers. FR-020.

**Checkpoint**: Any agent host can consume the three directives unchanged.

---

## Phase 6: User Story 4 - Documentation that cannot silently go stale (Priority: P4)

**Goal**: One deterministic, fail-closed refresh owns both generated artifacts, and the
documentation guardian owns it.

**Independent Test**: Two consecutive applies produce byte-identical artifacts; malformed markers
exit 2 with zero writes; five injected drifts each exit 1; counts match an independent audit.

### Tests for User Story 4

- [ ] T039 [P] [US4] Write failing tests in
  `00_global_system/scripts/tests/test_inventory.py` for `_inventory.py`. Cover the count rules
  verbatim: active means "directly contains at least one non-excluded file"; placeholder means
  "declared and no files anywhere in its subtree"; archived cards counted from the manifest, never
  from the archive filesystem; feature directories match `^\d{3}-[a-z0-9-]+$`; skill bundles
  counted by `SKILL.md`; excluded names from `_shared.is_excluded`; credential findings contain
  path, line, and family, and never the matched value.
- [ ] T040 [US4] Implement `00_global_system/scripts/_inventory.py`: `measure(root, manifest,
  quarantine) -> dict` producing the Inventory Snapshot fields from `data-model.md`, and
  `scan_secrets(root) -> list[dict]` with families `private-key`, `cloud-key`, `bearer-token`,
  `bot-token`, `high-entropy`, a 256 KB per-file cap, and no value reproduction. Verification:
  T039 passes.
- [ ] T041 [P] [US4] Write failing tests in `00_global_system/scripts/tests/test_render.py` for
  `_render.py`. Cover: `DIRECTORY.md` heading and table order exactly as
  `contracts/inventory-artifacts.md`; region line order with the owner line first; domain rows in
  numeric order; features by number; roles by card path case-insensitive; right-aligned integer
  columns; date-only `Last verified`; no absolute paths; ASCII-only output; two renders of the same
  snapshot are byte-identical.
- [ ] T042 [US4] Implement `00_global_system/scripts/_render.py` with `render_directory_md(snapshot)
  -> str` and `render_stats_region(snapshot) -> str`. Fixed widths from data, no wrapping, single
  trailing newline, no timestamps beyond the date. Verification: T041 passes.
- [ ] T043 [US4] Write failing tests in `00_global_system/scripts/tests/test_doc_guardian.py`.
  Cover: apply twice is byte-identical and the second run writes nothing (mtime unchanged); prose
  outside the region is byte-identical after apply; missing, duplicated, and reversed markers each
  exit 2 with unchanged file hashes; five drift cases each exit 1 in `--check`; JSON output has the
  documented keys; a live lock causes exit 3; secrets findings appear without values.
- [ ] T044 [US4] Implement `00_global_system/scripts/doc_guardian.py` per
  `contracts/doc-guardian-cli.md`: flags `--check`, `--json`, `--verbose`, `--root`, `--timeout`,
  `--force`; exit codes 0, 1, 2, 3; region splice with atomic replace; write only when content
  changed; lock via `_shared.Lock`; human and JSON output; required companion checks for owner
  cards, superseded names, and `.gitignore` coverage. Verification: T043 passes.
- [ ] T045 [US4] Create
  `30_infrastructure/executive_command/documentation_guardian/AGENT.md` with machine-readable YAML
  front-matter: `id`, `role`, `level: 2`, `reports_to: jarvis_prime`, `scope: global`,
  `owned_regions: [architecture-telemetry, directory-inventory]`, responsibilities (refresh,
  drift verification, archive custody), KPIs, and a body that names no vendor. FR-037 and
  Principle VIII.
- [ ] T046 [US4] Run `python "00_global_system/scripts/doc_guardian.py"` and confirm the two
  artifacts regenerate: `DIRECTORY.md` with its generated header and owner line, and the
  `ARCHITECTURE.md` region with the owner line first. Expected figures: 67 live role cards, 136
  quarantined, 0 skill bundles, 8 features. If a figure differs, explain why before continuing.
- [ ] T047 [US4] Prove idempotency on the real workspace: hash both artifacts, run apply again,
  hash again. Hashes must match and the second run must report no writes. SC-004.
- [ ] T048 [US4] Prove ownership: confirm each generated artifact names `documentation_guardian`,
  that the card from T045 exists, and that `--check` reports no `ownership_gap`. SC-014.
- [ ] T049 [US4] Prove fail-closed and drift detection on a copy: inject five mismatches (delete a
  required placeholder, add an undeclared directory, remove the guardian card, edit a number in
  the region, rename a feature directory), run `--check` after each, and confirm exit 1 each time.
  Then duplicate the start marker and confirm exit 2 with no writes. Restore the copy afterward.
  SC-009, FR-027.

**Checkpoint**: The inventory and telemetry can no longer lie without a failing exit code.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final gate. Nothing new is built here.

- [ ] T050 Run the full phase gate from the workspace root and require exit 0 from each:
  `scaffold_structure.py --check`, `quarantine_worker_seats.py --verify`,
  `doc_guardian.py --check`, then
  `python -m unittest discover -s "00_global_system/scripts/tests" -v`.
- [ ] T051 [P] Measure performance (SC-003): time `doc_guardian.py --check` with
  `Measure-Command`. Record wall clock and `elapsed_ms`; both must be under 2000 ms.
- [ ] T052 [P] Placeholder sweep: search `00_global_system/scripts/` for `TODO`, `FIXME`, bare
  `pass` statements, `...`, and `NotImplementedError`. Zero matches allowed.
- [ ] T053 Run `doc_guardian.py` once more after every documentation edit, confirm `--check` is
  clean, and confirm no `.gitkeep` file exists anywhere in the workspace.
- [ ] T054 Confirm the safety invariants: no file was deleted or renamed outside the quarantine
  move, no worker seat remains live, and the archive manifest still lists 136 entries with
  verified hashes.
- [ ] T055 Final consistency pass before declaring the phase complete: zero `[NEEDS
  CLARIFICATION]` markers in the feature documents, zero fabricated telemetry figures, zero
  `local_plugins.yaml` or `venture_*` pod-core names in `ARCHITECTURE.md`, exactly three directive
  files. Record the results in this task's note.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: no dependencies, starts immediately
- **Foundational (Phase 2)**: depends on Setup, blocks US1 through US4
- **US1 (Phase 3)**: depends on Foundational
- **US2 (Phase 4)**: depends on US1 for the manifest, the quarantine outcome, and the counts it
  documents
- **US3 (Phase 5)**: depends only on Foundational, so it may run beside US1 or US2
- **US4 (Phase 6)**: depends on US1 (manifest and archive) and US2 (markers and anatomy)
- **Polish (Phase 7)**: depends on all four stories

### Within each story

Tests first and failing, then implementation, then the real-workspace run, then the verification.

### Task-level dependencies worth knowing

| Task | Depends on |
|---|---|
| T008 `_shared.py` | T007 tests |
| T010 `_manifest.py` | T009 tests |
| T012 `scaffold_structure.py` | T006, T008, T010 |
| T018 real scaffold run | T013 to T017 manifest content |
| T020 quarantine utility | T008, T019 |
| T022 quarantine apply | T021 plan reviewed |
| T026 to T029 ARCHITECTURE edits | T018 (tree), T022 (archive reality) |
| T042 `_render.py` | T040 snapshot shape |
| T044 `doc_guardian.py` | T008, T010, T040, T042 |
| T046 real apply | T027 markers, T045 owner card |
| T050 full gate | every prior task |

### Parallel Opportunities

- T003, T004, T005, T006 are independent files
- T034, T035, T036 patch three different directives
- T025 (README) and T030 (genesis) are independent of the ARCHITECTURE edits in T026 to T029
- T011, T019, T039, T041, T043 are test files for different modules
- T051 and T052 are independent checks

---

## Parallel Example: User Story 3

```text
Task: "Patch Ziad_Cognitive_DNA.md with governing law and bound levels"
Task: "Patch Global_Governance_Rules.md with bound roles"
Task: "Patch Detachability_Standard.md with bound roles"
```

Run all three together, then T037 and T038 sequentially, because both inspect all three files.

---

## Implementation Strategy

### MVP first (User Story 1 only)

1. Phase 1 Setup
2. Phase 2 Foundational
3. Phase 3 US1: manifest, scaffold, quarantine
4. Stop and validate: `scaffold_structure.py --check` exits 0 and no `workers` directory remains

That delivers a clean, declared, worker-free skeleton. Documentation and inventory can follow.

### Incremental delivery

1. Setup plus Foundational, then US1: structure is trustworthy (MVP)
2. US2: documentation describes reality
3. US3: directives are portable and cited
4. US4: inventory and telemetry become self-correcting
5. Polish: the gate holds

Each step leaves the workspace working; no step depends on a later one to be true.

---

## Notes

- `[P]` marks different files with no ordering between them.
- Tests are mandatory here, not optional, because of constitution Section 3.
- Do not "fix" a count by editing a number. Fix the cause, then rerun the tool.
- If a verification fails, stop and report; do not proceed to the next task on a red check.
- The archive is not a graveyard: Phase 5 and Phase 6 restore or regenerate from templates using
  the manifest's role identifiers.
