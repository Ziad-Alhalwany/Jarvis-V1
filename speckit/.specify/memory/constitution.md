<!--
SYNC IMPACT REPORT
==================
Amendment type : Initial ratification (empty scaffold -> ratified constitution)
Version change : unversioned scaffold -> 1.0.0
Ratified       : 2026-10-26
Last amended   : 2026-10-26

Modified principles : none (no previously ratified principles existed)
Added principles    :
  I.    Dual-Topology Organization - Strict Authority Tree, Flexible Knowledge Graph
  II.   Federated Self-Contained Pods & 100% Detachability
  III.  Standardized Pod Shell & Context Economy
  IV.   Dual-Tier Memory, Deterministic Memory Facade & Zero-Loss Queue
  V.    Quad-Shield Task Engine & Cognitive Load Protection
  VI.   Self-Evolution Loop, Do-Document-Delegate & Gamified Scorecards
  VII.  Tiered Model Routing & Frugal Engineering
  VIII. Runtime-Agnostic Agent Fabric (NON-NEGOTIABLE)

Added sections    :
  - Core Principles
  - Technology, Interoperability & Security Constraints
  - Development Workflow, Quality Gates & Enforcement
  - Governance

Removed sections  : none

Notes on scope:
  - Laws 1-7 are transcribed from PLAN.md Part 1.2 and remain intact.
  - Principle VIII is an additive amendment ratified with this document in
    response to the founder's directive that the workforce structure must stay
    compatible with any AI agent runtime. It is additive, not a redefinition of
    Law 2 (pod detachability) or Law 7 (model routing).

Deferred items:
  - TODO(RUNTIME_SELECTION): the concrete runtime/tooling evaluation
    (Hermes Agent, Claude Code / Cowork, OpenAI Codex, Ollama stack, MCP
    servers, dashboard framework) is deferred to its own decision record.
    Principle VIII governs compatibility until it is ratified.
  - TODO(PRIVATE_ID_SECRET_STORE): the concrete secret-store backend for
    private_id.yaml and API credentials is not yet chosen.

Templates/commands requiring follow-up: none. Dependent templates read this
file at runtime and were not modified by this amendment.

This comment block is temporary scratch material for human review and MUST be
deleted before the amended constitution is committed.
-->

# J.A.R.V.I.S. V1 Constitution

The Life & Enterprise Operating System of Dr. Ziad Mohamed Alhalwany. This
document is the governing law of the ecosystem: it constrains every specification,
plan, task, agent card, skill bundle, and runtime adapter that is added to
`D:\AI_Workspace\Jarvis V1`. It describes a digital workforce and orchestration
layer that must behave like a well-run company: explicit authority, explicit
ownership, explicit tracking, and explicit approval.

## Core Principles

### I. Dual-Topology Organization - Strict Authority Tree, Flexible Knowledge Graph

The organization MUST operate on two simultaneous topologies and MUST NOT collapse
them into one.

- **Authority Layer (vertical tree).** Command, permission, and approval flow
  downward and accountability flows upward. The chain is: Supreme Commander
  (Dr. Ziad Mohamed Alhalwany) -> JARVIS Prime -> Level 2 executives (Global
  C-Suite, Personal Chief of Staff, Venture C-Suite) -> managers -> workers.
  Every `AGENT.md` card MUST declare exactly one `reports_to`; orphaned or
  multiply-parented agents are invalid.
- **Core Communication Protocol.** JARVIS Prime MUST be the sole agent permitted
  to message, notify, or call the Supreme Commander on external personal channels
  (Telegram). Sub-agents MUST NOT contact the Commander directly; they may interact
  only when explicitly summoned into a private War Room (Discord).
- **Knowledge Layer (horizontal graph - The Café).** Cross-pollination MUST be
  event-driven and structured: Eureka Broadcasts, CKO Cross-Pollination
  Proposals, and Peer Consultations. Every payload MUST pass
  `cafe_privacy_sanitizer.py` before publication. Free-form agent-to-agent chat
  loops are prohibited.
- **Rationale.** A single escalation path protects the Commander's attention and
  makes accountability unambiguous; a separate graph layer lets method knowledge
  compound across ventures without leaking private data.

### II. Federated Self-Contained Pods & 100% Detachability

Every commercial venture (`20_businesses/*`) and every life pillar
(`10_pillars/*`) MUST be a standalone micro-OS pod.

- Each pod MUST contain its own `_pod_core/`: local task engine, human/web
  gateway, local MCP and plugin configuration, and governance/registry files.
- A pod directory copied to a separate host MUST operate at 100% capacity with no
  dependency on sibling pods or on paths outside its own root, other than
  documented read-only global contracts. Every phase gate MUST include a
  detachability test: copy -> boot -> operate -> report.
- Pods MUST NOT import, read, or write another pod's files. All cross-pod
  exchange MUST route through `00_global_system` contracts or `the_cafe`
  protocols.
- Human collaborators MUST be scoped by `human_rbac_permissions.yaml` to a single
  pod, with zero visibility into personal pillars or other ventures.
- **Rationale.** Isolation is a business-continuity, privacy, and sellability
  requirement, not an optimization to be traded away.

### III. Standardized Pod Shell & Context Economy

Every pod MUST expose the same outer shell, and agents MUST boot cheaply.

- The shell is mandatory and MUST NOT be renamed or partially omitted: charter
  (`BUSINESS.md` or `PILLAR.md`), `DNA_AND_VOICE.md`, `STATE.md`,
  `DECISION_LOG.md`, `distilled_context.md`, `triggers_and_watchers.yaml`,
  `identifiers/public_id.yaml`, `identifiers/private_id.yaml`,
  `swipe_files_and_benchmarks/`, `reference_library/`, `knowledge_vault/`,
  `sessions_traces/`, and `reports_deliverables/`. `01_templates/` is the single
  source of their structure.
- Agents MUST boot from `distilled_context.md` (maximum two pages) before loading
  any raw source. Loading a full library on agent boot is prohibited.
- `DECISION_LOG.md` MUST be consulted before any proposal is written; re-pitching
  a rejected concept is a defect, not a style issue.
- `private_id.yaml` MUST never be read by a branding, marketing, or Café-facing
  agent and MUST never leave its pod.
- `STATE.md` MUST reflect verified telemetry only; agents MUST NOT write
  optimistic or self-reported progress into it.
- **Rationale.** A uniform, machine-checkable shell makes pods clonable and
  auditable; context economy is the single largest lever on cost and quality.

### IV. Dual-Tier Memory, Deterministic Memory Facade & Zero-Loss Queue

Knowledge MUST be tiered and all storage access MUST be mediated.

- **Tiering.** Tactical, disposable scratchpads live in the agent runtime.
  Permanent knowledge and structured data live in Commander-owned storage:
  Obsidian Markdown vaults for linked knowledge, plus AppFlowy, SQLite, or
  Postgres for structured tables.
- **Single facade.** Agents MUST NOT call storage APIs directly. All operations
  MUST pass through `00_global_system/memory_layer/mcp_memory_server.py`, which
  exposes exactly five universal operations: `save_entity`, `query_memory`,
  `update_state`, `link_entities`, `check_health`, governed declaratively by
  `memory_schema.yaml`.
- **Zero-loss intake.** Every inbound request (Telegram voice note, text, task,
  or file) MUST be persisted to `wal_queue.db` with status `PENDING` within 10ms,
  before any tool execution. A downstream outage MUST NOT lose a request.
- **Identity.** Every durable entity MUST receive an atomic semantic ID of the
  form `<PREFIX>-<YYYY>-<NNNN>` and MUST keep bidirectional links between its
  Markdown note and its structured row.
- **Human-gated schema.** The watchdog MAY repair formatting and MAY propose
  `memory_schema.yaml` changes; it MUST NOT apply semantic schema changes or edit
  core code autonomously.
- **Rationale.** One facade keeps storage replaceable - a prerequisite for
  portability - and an explicit write-ahead queue makes losslessness testable
  rather than aspirational.

### V. Quad-Shield Task Engine & Cognitive Load Protection

Every task surface (global and per pod) MUST be governed by four shields.

1. **Eisenhower routing.** Every task MUST be classified into Do Immediately
   (Commander), Schedule (Manager), Delegate (Worker), or Eliminate (Archive).
2. **Deterministic WSJF.** Priority MUST be computed in pure Python as
   `WSJF = round((value + urgency + risk_reduction) / max(effort, 1), 2)`.
   Identical inputs MUST yield identical output, and the computation MUST consume
   zero model tokens.
3. **WIP limits.** Maximum 3 `IN_PROGRESS` tasks per team and maximum 3 heavy
   cognitive tasks per day on the Commander's action sheet. The engine MUST block
   excess work, not merely warn.
4. **Confidence and reversibility gates.** If clarity is below 0.85 or required
   parameters are missing, execution MUST halt with status `DISCUSS_FIRST` and
   clarifying questions MUST be asked instead of guessed. Any action declared
   `is_reversible: false` (spending, publishing, deleting, messaging external
   parties) MUST be staged in `review_queue_approvals.md` for a five-button
   decision - Approve, Cancel, Edit, Explain & Discuss First - with a mandatory
   comment.
5. **One-way federation.** Pods publish sanitized `public_telemetry_rollup.json`;
   only `federation_rollup_sync.py` aggregates into `MASTER_BOARD.md`. Global
   components MUST NOT write into pod boards.

- **Rationale.** Attention is the scarcest resource in the system. Determinism
  makes prioritization auditable, reproducible, and free.

### VI. Self-Evolution Loop, Do-Document-Delegate & Gamified Scorecards

The workforce MUST improve from evidence, under human control.

- Every decision made through the dashboard MUST capture a comment; dashboard
  comments and `sessions_traces/` are the only sanctioned learning signals.
- `skill_evolver_pipeline.py` MUST stage, never promote: proposed `SKILL.md`
  bundles in `proposed_skills/`, rule patches in `feedback_patches/`, and
  distilled playbooks in `extracted_sops/`. Promotion requires Commander approval.
- **Do-Document-Delegate.** A routine the Commander performs twice MUST be
  captured as a `playbooks_and_sops/` artifact before a third manual execution.
- **Scoring.** +5 first-pass approval, -3 edit, cancel, or rejection, +10 verified
  SOP created, +5 verified Café synergy, -5 overdue or SLA miss (also logged in
  `blockers.md`). Scores MUST be computed by deterministic code and MUST NOT be
  self-reported or editable by the scored agent.
- **Rationale.** Improvement must be auditable, reversible by the Commander, and
  structurally resistant to agent self-grading.

### VII. Tiered Model Routing & Frugal Engineering

Reasoning capacity MUST be spent deliberately.

- **Deterministic first.** Extraction, sorting, counting, formatting, ID
  generation, scoring, and validation MUST be Python, never a model call.
- **Tiered routing.** Routine classification and summarization route to local
  models (Ollama); heavy synthesis and coding route to frontier models with
  `distilled_context.md` preloaded.
- **Attribution.** Every model call MUST be attributable to an agent card and a
  task. Untracked background LLM loops are prohibited.
- **Budget.** Every phase plan MUST state its expected model-tier usage, and no
  feature may introduce a recurring autonomous loop without an explicit budget
  entry in `task_engine_config.yaml`.
- **Rationale.** Token spend is an operating expense of the enterprise and MUST
  be governed like one.

### VIII. Runtime-Agnostic Agent Fabric (NON-NEGOTIABLE)

The workforce MUST outlive any single tool. The structure is the asset; the
runtime is a replaceable host.

- No agent runtime, IDE, or vendor API may be hard-coded into pod logic, memory
  contracts, or engine code. The ecosystem MUST remain executable on Hermes Agent,
  Claude Code / Cowork, OpenAI Codex, a local Ollama stack, or a future
  replacement.
- Agent behavior MUST live in portable plain-text artifacts: `AGENT.md` cards,
  `SKILL.md` bundles, `playbooks_and_sops/`, `triggers_and_watchers.yaml`, and
  `.mcp.json` / MCP server manifests.
- Runtime-specific glue MUST be isolated in adapters under
  `_pod_core/local_mcp_and_plugins/` and `30_infrastructure/brain_bindings/`.
  Nothing outside those adapter boundaries may import a vendor SDK.
- Every `AGENT.md` card MUST carry machine-readable front-matter (id, role,
  `reports_to`, pod, tools, `autonomy_level`, inputs, outputs, KPIs) and MUST be
  valid without reference to any vendor-specific schema.
- A runtime swap MUST be achievable by replacing adapters only. Any change that
  requires editing pod content, `memory_schema.yaml` semantics, or engine code to
  switch runtime is a MAJOR violation of this constitution.
- Runtime and tool selection MUST be a documented, reversible decision: capability
  matrix, scored comparison, explicit Commander approval, and a record in
  `DECISION_LOG.md` plus the runtime capability matrix.
- **Rationale.** Portability maintained continuously costs a thin adapter layer;
  portability retrofitted after lock-in costs a rewrite of every pod.

## Technology, Interoperability & Security Constraints

**Deterministic core.** Python 3.11+ with the standard library first. A third-party
dependency MUST be justified by a requirement the standard library cannot meet
(FastAPI for the dashboard, PyYAML for declarative config/schema parsing are
pre-approved). Core engines MUST run offline with no network access.

**State and storage.** Markdown is the human-facing source of truth; SQLite in WAL
mode backs the queue and atomic counters; YAML carries declarative configuration;
Obsidian holds linked knowledge; AppFlowy/Postgres hold structured tables. Governed
state MUST NOT be stored in a proprietary binary-only format.

**Directory law.** Numbered prefixes (`00_`, `01_`, `10_`, `20_`, `30_`, `90_`,
`99_`) and canonical filenames MUST NOT be renamed, because agents, scripts, and
documentation reference them literally. Adding or removing a top-level directory
requires a constitutional amendment.

**Security and privacy.** Secrets MUST live only in `.env` (gitignored) or the OS
keychain - never in committed Markdown, YAML, or JSON. The memory facade MUST
enforce tenant isolation (`caller_pod != target_pod` => reject, except explicit
`00_global_system` and `the_cafe` targets). `private_id.yaml` MUST be excluded from
exports, external backups, telemetry rollups, and Café payloads. Every human-facing
connector MUST be authorized by `human_rbac_permissions.yaml`.

**Performance baselines.** WAL enqueue p95 under 10ms; `doc_guardian.py` full
workspace scan under 2 seconds; WSJF and scorecard batches under 50ms per 100
tasks; dashboard reads bounded to the data a view actually renders. A regression
against these baselines blocks a phase gate.

**Interoperability.** MCP is the default tool protocol; every MCP server MUST be
declared in `global_mcp_registry.json` with its capabilities and scopes. All
persisted conversation, task, and telemetry artifacts MUST be plain text or JSON
so that any runtime can read and hand off state.

## Development Workflow, Quality Gates & Enforcement

**Spec-Driven Development.** Work proceeds only through
`/speckit-specify` -> `/speckit-plan` -> `/speckit-tasks` -> `/speckit-implement`,
one feature directory per phase under `specs/NNN-phase-name/`. Implementation
without an approved spec, plan, and tasks list is prohibited.

**Constitution Check gate.** Every `plan.md` MUST contain a Constitution Check
that evaluates all eight principles explicitly. Any violation MUST be recorded in
Complexity Tracking with the specific need and the simpler alternative rejected.
An unjustified violation blocks planning.

**Test-first for deterministic code.** WSJF computation, scoring, semantic ID
generation, WAL status transitions, tenant-isolation assertions, and privacy
sanitization MUST have failing tests written before implementation. This is not
negotiable.

**Definition of Done.** A task is complete only when: acceptance criteria are met;
tests pass; `doc_guardian.py` runs clean; `STATE.md` and `DECISION_LOG.md` are
updated where behavior changed; no secrets or placeholder tokens remain; and the
Constitution Check is re-verified after design.

**Human approval gates.** The Commander's explicit approval with a comment is
required for: irreversible actions, semantic changes to `memory_schema.yaml`,
promotion of skills or DNA patches, new top-level directories, runtime or vendor
changes, and any spending.

**Phase gates.** Phase N+1 MUST NOT begin until Phase N's acceptance criteria pass,
its detachability test succeeds, and its documentation is synchronized.

## Governance

**Supremacy.** This constitution supersedes `PLAN.md`, `README.md`,
`ARCHITECTURE.md`, all `specs/` artifacts, and all agent cards. `PLAN.md` is a
roadmap and may be revised; it may not override this document. Precedence order is:
constitution > ratified decision records (`DECISION_LOG.md`) > specifications >
`PLAN.md`.

**Amendment procedure.** Any amendment MUST be proposed in writing (what changes,
why, affected principles, migration impact), approved by the Supreme Commander as
sole ratifier, versioned per the policy below, and accompanied by an updated Sync
Impact Report. Dependent templates read this file at runtime and therefore MUST NOT
be edited as part of an amendment. Amendments MUST NOT apply retroactively without
a migration note in `DECISION_LOG.md`.

**Versioning policy.** Semantic versioning: MAJOR for removal or redefinition of a
principle or a backward-incompatible governance change; MINOR for a new principle,
new section, or materially expanded guidance; PATCH for clarifications, wording, or
non-semantic refinements. Every ratified amendment increments the version and
records `Last Amended` in ISO `YYYY-MM-DD`.

**Compliance review.** Every phase gate and every quarterly review MUST verify all
eight principles, the performance baselines, and the security constraints. Findings
MUST be logged in the global blockers radar. An unresolved MAJOR violation halts
new work until remediated or amended.

**Open decisions.** Runtime and tooling selection is governed by Principle VIII and
remains open: `TODO(RUNTIME_SELECTION)`. The secret-store backend for
`private_id.yaml` remains open: `TODO(PRIVATE_ID_SECRET_STORE)`. Neither gap
permits vendor lock-in in the interim.

**Version**: 1.0.0 | **Ratified**: 2026-10-26 | **Last Amended**: 2026-10-26
