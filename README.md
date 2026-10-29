# J.A.R.V.I.S. V1 — Federated Life & Enterprise Operating System

**Owner & Supreme Commander:** Dr. Ziad Mohamed Alhalwany  
**Workspace Root:** `D:\AI_Workspace\Jarvis V1`  
**Constitutional Version:** `1.0.0` (Ratified `2026-10-26`)  
**Development Paradigm:** Spec-Driven Development (SDD) via GitHub Spec Kit (`specify-cli`)  
**Runtime Fabric:** Runtime-Agnostic (Hermes Agent, Claude Code / Cowork, OpenAI Codex, Local Ollama Stack)

---

## 1. Executive Vision & Core Problem Solved

Dr. Ziad Mohamed Alhalwany manages a highly interconnected, multi-disciplinary life and commercial ecosystem:

1. **Clinical Medicine & Polymath Learning:** Medical internship and clinical rotations (surgical oncology, GI surgery, internal medicine), medical board preparation, and cross-disciplinary research.
2. **Commercial Ventures (`20_businesses/`):**
   - **Travelophilia:** Regional travel agency, inter-governorate student transport SaaS, B2B DMC partnerships, and zero-fee international youth/Erasmus+ programs.
   - **Medicophilia:** Medical education platform, clinical roadmaps, healthcare SaaS, and medical podcast/content ecosystem.
3. **Personal Brand Umbrella (`Ziad Alhalwany`):** Overarching personal brand uniting entrepreneurship, clinical life (`medwithziad`), and travel lifestyle (`travelwithziad`), anchored by `ZiadAlhalwany.com`.
4. **Personal Life Pillars (`10_pillars/`):** Spiritual discipline, physical health and personal growth, clinical mastery, personal branding, and personal wealth management.

### The Core Bottleneck

A single human has two hands and 24 hours per day. Acting as the manual executor across all five personal pillars and multiple commercial ventures leads to context-switching fatigue, unrecorded ideas, delayed follow-ups, and stalled growth.

### The J.A.R.V.I.S. Solution

J.A.R.V.I.S. V1 is not a chatbot. It is a **federated, hierarchical, and networked digital enterprise** composed of over **140 hyper-specialized AI digital employees** organized into executive cabinets, functional departments, and capability teams. It transforms Dr. Ziad from a manual executor into a **Supreme Commander & Strategic Decision-Maker**.

---

## 2. The 8 Governing Constitutional Principles

All specifications, scripts, agents, and skills in this repository are strictly bound by `.specify/memory/constitution.md`:

| Principle          | Title                                         | Core Mandate                                                                                                                                                                                                                                                                                                                                                                                                            |
| :----------------- | :-------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Principle I**    | **Dual-Topology Organization**                | **Strict Vertical Authority Tree** (`Ziad -> JARVIS Prime -> Level 2 Executives -> Managers -> Workers`) for command and isolation + **Flexible Horizontal Knowledge Graph (`The Café`)** for sanitized, event-driven method sharing. `JARVIS Prime` is the **only** agent permitted to contact Ziad on Telegram.                                                                                                       |
| **Principle II**   | **Federated Self-Contained Pods**             | Every business (`20_businesses/*`) and life pillar (`10_pillars/*`) is a standalone micro-OS containing its own `_pod_core/` (local task board, website/CRM gateway, human RBAC, local MCP/hooks). Any pod copied to another machine operates at 100% capacity.                                                                                                                                                         |
| **Principle III**  | **Standardized Pod Shell & Context Economy**  | Every pod exposes an identical outer shell (`BUSINESS.md`/`PILLAR.md`, `DNA_AND_VOICE.md`, `STATE.md`, `DECISION_LOG.md`, `distilled_context.md`, `triggers_and_watchers.yaml`, `identifiers/`, `swipe_files_and_benchmarks/`, `reference_library/`, `knowledge_vault/`, `sessions_traces/`, `reports_deliverables/`). Agents boot exclusively from `distilled_context.md` (max 2 pages) to save 80% of context tokens. |
| **Principle IV**   | **Dual-Tier Memory & Zero-Loss Queue**        | Tactical scratchpads stay in runtime memory; permanent data lives in **Obsidian** (linked Markdown) and **AppFlowy / SQLite / Postgres** (structured tables). All storage access passes through the 5 deterministic functions of `mcp_memory_server.py`. Inbound requests hit `wal_queue.db` (`PENDING`) within 10ms so zero data is ever lost.                                                                         |
| **Principle V**    | **Quad-Shield Task Engine**                   | Tasks pass through (1) **Eisenhower Routing**, (2) **Deterministic Python WSJF** (`(Value + Urgency + Risk) / Effort`), (3) **Hard Kanban WIP Limits** (max 3/team, max 3 heavy daily tasks for Ziad), and (4) **85% Confidence Gate** (ask Ziad, never guess) + **Reversibility Gate** (5-Button Approval + Mandatory Comment).                                                                                        |
| **Principle VI**   | **Self-Evolution, SOPs & Scorecards**         | Dashboard comments and `sessions_traces/` feed `skill_evolver_pipeline.py` to stage proposed skills and DNA patches. Routines performed twice by Ziad become autonomous SOPs (`Do-Document-Delegate`). Deterministic 100-point scorecards track every agent (`+5` approval, `-3` edit/cancel, `+10` SOP, `+5` Café synergy, `-5` overdue).                                                                              |
| **Principle VII**  | **Tiered Model Routing & Frugal Engineering** | Deterministic Python handles math, sorting, IDs, and validation at zero token cost. Local models (`Ollama`) handle routine triage; frontier models (`Claude / Codex`) handle complex synthesis and code with `distilled_context.md` preloaded.                                                                                                                                                                          |
| **Principle VIII** | **Runtime-Agnostic Agent Fabric**             | All agent intelligence lives in plain-text `AGENT.md`, `SKILL.md`, YAML, and MCP manifests. Vendor-specific glue is isolated inside adapter folders (`_pod_core/local_mcp_and_plugins/` and `30_infrastructure/brain_bindings/`).                                                                                                                                                                                       |

---

## 3. Top-Level Directory Map

```text
D:\AI_Workspace\Jarvis V1\
├── .specify\                                  # Spec Kit governance engine & constitution.md
├── specs\                                     # Phase 0 to Phase 7 Spec-Driven Development artifacts
├── 00_global_system\                          # Shared Core: Directives, Memory Layer, WAL Queue, Master Task Engine, HR Registry, Learning Loop
├── 01_templates\                              # Master Cloning Blueprints for Businesses, Pillars, Departments, Teams, Agents & Skills
├── 10_pillars\                                # Personal Life OS: 5 Standalone Pods (Health, Spiritual, Clinical/Learning, Branding, Finance)
├── 20_businesses\                             # Commercial Ventures: 100% Isolated Pods (Medicophilia, Travelophilia)
├── 30_infrastructure\                         # Executive Command (JARVIS Prime + Global C-Suite), The Café, Telegram/Discord Bridges, Brain Bindings
├── 90_dashboard\                              # Visual Command Center: 5-Button Approvals, Ziad's Daily Sheet, Org Graph, Scorecards, Blockers Radar
└── 99_archive\                                # Cold storage & legacy backups
```

---

## 4. Essential Navigation Links

- **Governing Law:** [`.specify/memory/constitution.md`](.specify/memory/constitution.md)
- **Architectural Bible:** [`ARCHITECTURE.md`](ARCHITECTURE.md)
- **Complete Intellectual History & Discussions:** [`PROJECT_GENESIS_AND_DISCUSSIONS_DRAFT.md`](PROJECT_GENESIS_AND_DISCUSSIONS_DRAFT.md)
- **8-Phase Spec Kit Roadmap:** [`PLAN.md`](PLAN.md)
- **Root Agent Directives:** [`CLAUDE.md`](CLAUDE.md)
- **Central HR Workforce Directory:** [`00_global_system/agent_registry/DIRECTORY.md`](00_global_system/agent_registry/DIRECTORY.md)
- **Global Master Task Board:** [`00_global_system/master_task_engine/MASTER_BOARD.md`](00_global_system/master_task_engine/MASTER_BOARD.md)
- **Visual Command Center Overview:** [`90_dashboard/OVERVIEW.md`](90_dashboard/OVERVIEW.md)

---

## 5. Spec-Driven Development Workflow (`specify-cli`)

No code or structural mutation is permitted outside the Spec Kit lifecycle:

1. **`/speckit.constitution`**: Review or amend `.specify/memory/constitution.md`.
2. **`/speckit.specify`**: Define user stories, functional requirements, and acceptance criteria in `specs/NNN-phase-name/spec.md`.
3. **`/speckit.clarify`**: Resolve any under-specified requirements before planning.
4. **`/speckit.plan`**: Generate technical design, schemas, and Constitution Check in `specs/NNN-phase-name/plan.md`.
5. **`/speckit.tasks`**: Generate ordered, testable implementation tasks in `specs/NNN-phase-name/tasks.md`.
6. **`/speckit.analyze`**: Audit cross-artifact consistency against the 8 Constitutional Principles.
7. **`/speckit.implement`**: Execute tasks Test-First (TDD), run `doc_guardian.py`, and pass the Phase Detachability Test.

---

## 6. Mandatory Performance Baselines

| Subsystem                                       | Metric                                         | Hard Baseline Target                |
| :---------------------------------------------- | :--------------------------------------------- | :---------------------------------- |
| **WAL Queue Intake (`wal_queue_manager.py`)**   | Inbound request persistence latency (`p95`)    | `< 10 ms`                           |
| **Documentation Guardian (`doc_guardian.py`)**  | Full workspace scan & registry synchronization | `< 2.0 seconds`                     |
| **WSJF & Scorecard Engine**                     | Batch calculation & sorting per 100 tasks      | `< 50 ms` (Zero LLM tokens)         |
| **Agent Boot Context (`distilled_context.md`)** | Preloaded pod context size                     | `<= 2 pages` (~80% token reduction) |
