# J.A.R.V.I.S. V1 — Master Macro-to-Micro Architectural Bible (`ARCHITECTURE.md`)

**Workspace Root:** `D:\AI_Workspace\Jarvis V1`  
**Governing Law:** `.specify/memory/constitution.md` (v1.0.0)  
**Maintenance Protocol:** Living Documentation — Structural statistics between `<!-- AUTO-STATS-START -->` and `<!-- AUTO-STATS-END -->` are automatically synchronized by `00_global_system/scripts/doc_guardian.py`.

---

## 1. Architectural Philosophy: Why J.A.R.V.I.S. V1 Is Built This Way

### 1.1 The Dual-Topology Breakthrough (Tree of Authority + Graph of Knowledge)

Traditional hierarchies fail AI ecosystems because a rigid tree prevents cross-domain innovation, while a flat swarm causes context pollution, infinite chat loops, and security leaks. J.A.R.V.I.S. V1 separates **Authority** from **Knowledge**:

1. **The Authority Layer (Strict Vertical Tree):**
   - Governs command delegation, tool permissions, budgets, and tenant isolation.
   - Every agent has **exactly one** direct supervisor (`reports_to` in `AGENT.md`).
   - **Supreme Communication Rule:** Only `JARVIS Prime` (Layer 1) has permission to message, notify, or call Dr. Ziad on Telegram. Lower-tier agents never interrupt Ziad directly; they surface outputs through their managers or participate in structured Discord War Rooms when explicitly summoned by Ziad.
2. **The Knowledge & Social Layer (Horizontal Event-Driven Graph — `The Café`):**
   - Hosted in `30_infrastructure/the_cafe/` and governed by the `Global Knowledge Officer (CKO - Hakim)`.
   - Agents across `Travelophilia`, `Medicophilia`, and the 5 Personal Life Pillars share **how** they solved a problem (methodology, prompt patterns, code architecture, funnel mechanics) without ever sharing **what** the private data was (client names, patient records, financials, API keys).

### 1.2 The Federated Micro-OS Pod Model (`_pod_core`)

A critical requirement set by Dr. Ziad is that any business (`Travelophilia`, `Medicophilia`) or personal life pillar must be **100% detachable** and capable of hosting **human employees** or connecting to **live external websites** (`Travelophilia.com`, `Medicophilia.com`, `ZiadAlhalwany.com`) without exposing the rest of Ziad's life OS.

Therefore, every business and pillar is built as a **Self-Contained Pod**:

- Inside each pod sits `_pod_core/`, which provides a local task board (`LOCAL_BOARD.md`), a local approval queue, a website/CMS/CRM gateway (`website_cms_crm_connector.py`), human role-based access control (`human_rbac_permissions.yaml`), local MCP servers, and local scorecards.
- **One-Way Federated Rollup:** Pods do not know other pods exist. They emit sanitized metrics into `_pod_core/local_task_engine/public_telemetry_rollup.json`. The global script `federation_rollup_sync.py` pulls those summaries into `00_global_system/master_task_engine/MASTER_BOARD.md` and `90_dashboard/` for Ziad's eyes only.

---

## 2. Live Workspace Telemetry (Auto-Synchronized by `doc_guardian.py`)

<!-- AUTO-STATS-START -->

- **Last Synchronized:** `2026-10-26 18:00:00`
- **Total Active Structural Directories:** `215`
- **Total Registered Digital Employees (`AGENT.md`):** `142`
- **Total Registered Skill Bundles (`SKILL.md`):** `3`
- **Total Spec Kit Phase Specifications (`specs/`):** `8`
<!-- AUTO-STATS-END -->

---

## 3. Macro-to-Micro Directory & File Anatomy

Every directory and canonical file in `D:\AI_Workspace\Jarvis V1` exists to solve a specific engineering problem. Renaming numbered prefixes or canonical shell files is prohibited by Constitutional Directory Law.

### 3.1 Root Directory (`D:\AI_Workspace\Jarvis V1\`)

| File / Folder                              | Purpose & Problem Solved                                                                                                                   |
| :----------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| `.specify/memory/constitution.md`          | The Supreme Law of the ecosystem. Supersedes all other files. Enforces the 8 Core Principles and performance baselines.                    |
| `specs/`                                   | Houses `001` through `008` Spec Kit feature directories (`spec.md`, `plan.md`, `tasks.md`). Prevents vibe-coding and undocumented changes. |
| `README.md`                                | Fast onboarding portal for humans and AI agents.                                                                                           |
| `ARCHITECTURE.md`                          | This document. Explains every folder, file, agent, and data flow from macro to micro scale.                                                |
| `PROJECT_GENESIS_AND_DISCUSSIONS_DRAFT.md` | Complete historical archive of all architectural discussions, refinements, and design rationales.                                          |
| `PLAN.md`                                  | The 8-Phase Spec-Driven execution roadmap and model-tier budget allocation.                                                                |
| `CLAUDE.md`                                | Automatic root instruction hook read by Claude Code, Cowork, Codex, and Hermes Agent upon opening the workspace.                           |
| `.mcp.json`                                | Standard Model Context Protocol manifest mounting `mcp_memory_server.py` for any compatible agent runtime.                                 |
| `.env` / `.env.example`                    | Stores API keys and database URIs. `.env` is strictly gitignored; secrets never touch Markdown or YAML files.                              |

---

### 3.2 Layer 0: Shared Core Engine (`00_global_system/`)

**Why it exists:** Houses the single-instance deterministic engines, global directives, central HR registry, and self-evolution pipelines shared across the holding ecosystem.

#### A. `00_global_system/directives/`

- `Ziad_Cognitive_DNA.md`: Encodes Dr. Ziad's thinking style, radical candor standard, natural Arabic/English bilingual rules, and ban on robotic AI punctuation.
- `Global_Governance_Rules.md`: Defines the state machines for the 85% Confidence Gate, Reversibility Gate, 5-Button Action Center, The Café, and Discord Roundtables.
- `Detachability_Standard.md`: Defines the exact contract every `_pod_core/` must satisfy to pass Phase Gate Detachability Tests.

#### B. `00_global_system/memory_layer/` & `00_global_system/queue_vault/`

- **Problem Solved:** If 140+ agents talk directly to Obsidian or AppFlowy APIs, any tool update breaks 140 agents, and if an app is closed when Ziad sends a voice note on Telegram, the note is lost.
- `wal_queue_manager.py` & `wal_queue.db`: SQLite database running in `WAL` (Write-Ahead Logging) mode. Persists every inbound request as `PENDING` in `< 10ms` before any processing occurs.
- `staging_media_inbox/`: Temporary holding folder for raw voice notes, screenshots, and PDFs before transcription/parsing.
- `semantic_id_generator.py`: Generates atomic, sequential IDs per domain (`JAR-2026-0001`, `MED-2026-0001`, `TRV-2026-0001`, `HLT-2026-0001`, `SPR-2026-0001`, `CLN-2026-0001`, `BRD-2026-0001`, `FIN-2026-0001`) and constructs bidirectional links (`obsidian://open?vault=...` <-> AppFlowy row ID).
- `memory_schema.yaml`: Declarative routing configuration mapping entity types to target pod vaults and structured tables. Adding a new note or table type requires editing only this YAML file—never Python code.
- `mcp_memory_server.py`: Exposes exactly **5 deterministic functions** over MCP:
  1. `save_entity(caller_pod, target_pod, entity_type, title, content, metadata, tags)`
  2. `query_memory(caller_pod, target_pod, query_str, filters, limit)`
  3. `update_state(caller_pod, target_pod, semantic_id, patch_data)`
  4. `link_entities(caller_pod, source_id, target_id, relation_type)`
  5. `check_health(caller_pod)`
- `memory_watchdog_agent.py`: Monitors `wal_queue.db`, replays stalled items, auto-repairs minor formatting issues (e.g., non-ISO dates), and stages proposed `memory_schema.yaml` enhancements into `review_queue_approvals.md` for Ziad's approval.

#### C. `00_global_system/master_task_engine/`

- **Problem Solved:** Protects Ziad's time from low-value tasks, prevents agents from opening 20 unfinished tasks at once, and stops agents from guessing when instructions are vague.
- `task_engine_config.yaml`: Stores WIP caps (`team_wip_limit: 3`, `ziad_daily_heavy_limit: 3`), SLA timers, and token budgets.
- `eisenhower_wsjf_wip_engine.py`: Pure Python engine (zero LLM tokens, `< 50ms` per 100 tasks) that classifies tasks into the 4 Eisenhower quadrants and ranks them by **Weighted Shortest Job First**:
  $$\text{WSJF} = \text{round}\left(\frac{\text{Value} + \text{Urgency} + \text{Risk Reduction}}{\max(\text{Effort}, 1)}, 2\right)$$
- `federation_rollup_sync.py`: One-way aggregator that reads `public_telemetry_rollup.json` from all 7 pods and builds `MASTER_BOARD.md`.
- `MASTER_BOARD.md`: The global task board showing Ziad's Red Quadrant tasks (max 3 heavy/day) and active delegated WIP across all pods.
- `review_queue_approvals.md`: Staging queue for 90%-complete deliverables and irreversible actions awaiting Ziad's 5-Button Decision (`Approve`, `Cancel`, `Edit`, `Explain & Discuss First` + Mandatory Comment).

#### D. `00_global_system/hooks_and_guardrails/`

- `pre_task_confidence_gate.py`: Evaluates task prompt clarity and required schema inputs before execution. If clarity `< 0.85`, halts the task in `DISCUSS_FIRST` status and sends clarifying questions to Ziad via `JARVIS Prime`.
- `pre_write_reversibility_gate.py`: Intercepts any action marked `is_reversible: false` (external publishing, financial transactions, database deletions, external client messages) and diverts it to `review_queue_approvals.md`.
- `cafe_privacy_sanitizer.py`: Scans outbound Café broadcasts against `private_id.yaml` patterns, regex rules (emails, phone numbers, API keys, dollar figures, patient identifiers), and blocks any leak before publication.

#### E. `00_global_system/agent_registry/`

- `DIRECTORY.md`: Auto-generated master table of every `AGENT.md` card, its pod scope, and its supervisor.
- `scorecard_engine.py` & `scorecards_leaderboard.md`: Deterministic 100-point performance tracker:
  - First-pass `Approve` without edits: **`+5 pts`**
  - `Edit`, `Cancel`, or rejection: **`-3 pts`**
  - Verified SOP created via Do-Document-Delegate: **`+10 pts`**
  - Verified Café Eureka broadcast adopted by another pod: **`+5 pts`**
  - Overdue task / SLA miss: **`-5 pts`** (and auto-logged to `blockers.md`).

#### F. `00_global_system/learning_loop/`

- `skill_evolver_pipeline.py`: Reads Ziad's mandatory dashboard comments and raw `sessions_traces/` scratchpads. Extracts reusable lessons and stages them into:
  - `proposed_skills/`: New `SKILL.md` bundles awaiting Ziad's approval.
  - `feedback_patches/`: Proposed rule additions to `DNA_AND_VOICE.md` or `AGENT.md`.
  - `extracted_sops/`: Step-by-step SOP playbooks distilled after observing Ziad perform a routine task twice.

---

### 3.3 Master Cloning Archive (`01_templates/`)

**Why it exists:** Ensures we build each pattern **once** and clone it infinitely with zero structural drift.

- `standalone_business_pod_template/`: Complete skeleton of a commercial venture pod (`_pod_core/`, 6-member C-Suite, 7 departments, outer shell).
- `standalone_pillar_pod_template/`: Complete skeleton of a personal life pillar pod (`_pod_core/`, Pillar Lead, 4 Capability departments, PARA/GTD/Metrics folders, outer shell).
- `department_module_template/`: Standard department folder (`DEPARTMENT.md`, `manager/AGENT.md`, `workers/`, `playbooks_and_sops/`, `active_tasks/`).
- `think_and_know_team_template/`: Blueprint for the 4-mode intelligence team (`Discuss`, `Research`, `Plan`, `Learn`).
- `agent_card_template/AGENT.md`: Machine-readable YAML frontmatter + Markdown body template for digital employees.
- `skill_bundle_template/`: Standard `SKILL.md` + `scripts/` + `templates/` + `references/` bundle compliant with `agentskills.io`.

---

### 3.4 Standardized Pod Outer Shell (Present in Every Business & Life Pillar)

Every pod inside `10_pillars/*` and `20_businesses/*` contains these exact root files:

1. `BUSINESS.md` (or `PILLAR.md`): Charter, vision, Ideal Customer Profile (ICP) or life standard, and scope boundaries.
2. `DNA_AND_VOICE.md`: Psycholinguistic tone, terminology, and formatting rules specific to that domain.
3. `STATE.md`: Verified live metrics, active sprint progress, and health score.
4. `DECISION_LOG.md`: Chronological table of approved and rejected ideas so agents never re-propose rejected concepts.
5. `distilled_context.md`: Maximum 2-page high-signal summary loaded by agents on boot before touching any raw file.
6. `triggers_and_watchers.yaml`: Cron schedules and file/webhook watchers that wake up pod agents automatically.
7. `identifiers/public_id.yaml`: Public brand hooks and value propositions safe for cross-promotion.
8. `identifiers/private_id.yaml`: Strictly locked secrets, contracts, and private identifiers that never leave the pod.
9. `_pod_core/`:
   - `local_task_engine/LOCAL_BOARD.md`, `local_review_approvals.md`, `public_telemetry_rollup.json`
   - `web_and_human_gateway/website_cms_crm_connector.py`, `human_rbac_permissions.yaml`
   - `local_mcp_and_plugins/local_mcp.json`, `local_plugins.yaml`
   - `local_hooks/pod_isolation_guard.py`
   - `_governance_and_registry/pod_agents_directory.md`, `pod_scorecard_points.md`, `okrs_12_week_sprint.md`, `pod_blockers.md`
10. `swipe_files_and_benchmarks/`: Curated inspiration, competitor teardowns, and gold-standard examples.
11. `skills/`: Domain-specific executable skill bundles loaded only inside this pod (Progressive Disclosure).
12. `sessions_traces/`: Raw agent reasoning scratchpads used as fuel for `skill_evolver_pipeline.py`.
13. `reports_deliverables/`: Polished, human-natural reports ready for Ziad or external stakeholders.

---

### 3.5 Personal Life Operating System (`10_pillars/`) — 5 Standalone Pods

Each Life Pillar merges **5 Frameworks**: (1) **4 Operational Capabilities (`Learn / Execute / Delegate / Monitor`)**, (2) **`PARA`** (`active_projects/`, `knowledge_vault/`), (3) **`GTD Horizons`** (`areas_and_sops/`), (4) **`Quantified Self Telemetry`** (`metrics_and_logs/`), and (5) **`12-Week Year Sprints`** (`okrs_12_week_sprint.md`).

Internal department layout inside every Life Pillar:

- `00_pillar_lead/`: Houses the 24/7 Pillar Director Agent reporting to `personal_chief_of_staff`.
- `01_think_and_learn/`: Capability 1 (`Learn`) — Manager + Research Workers + `reference_library/` (raw books/papers) + `knowledge_vault/` (linked Obsidian notes).
- `02_execute_and_build/`: Capability 2 (`Execute`) — Manager + Planning/Building Workers + `active_projects/` (time-bound PARA projects) + `areas_and_sops/` (ongoing GTD responsibilities & routines).
- `03_delegate_and_automate/`: Capability 3 (`Delegate`) — Manager + Booking, procurement, publishing, and external task workers.
- `04_monitor_and_metrics/`: Capability 4 (`Monitor`) — Manager + Habit trackers, opportunity scouts + `metrics_and_logs/` (structured numerical trackers).

---

### 3.6 Commercial Ventures (`20_businesses/medicophilia` & `20_businesses/travelophilia`)

Each Commercial Venture is structured as a full AI-native corporation with an isolated **6-Member C-Suite Cabinet** and **7 Functional Departments**:

- `00_c_suite_leadership/`:
  - `venture_ceo/`: Managing Director of the business. The **only** agent in the business that reports upward to `JARVIS Prime` (or interacts with a designated human director).
  - `venture_cto_cpo/`: Chief Technology & Product Officer (oversees `02_product_and_engineering`).
  - `venture_cmo_cro/`: Chief Marketing & Revenue Officer (oversees `03_marketing_and_growth` and `04_sales_and_crm`).
  - `venture_coo/`: Chief Operating Officer (oversees `05_supply_partnerships_and_fulfillment` and `06_operations_task_tracking_and_admin`).
  - `venture_cfo_clo/`: Chief Financial & Legal Officer (oversees `07_finance_and_legal`).
  - `venture_cko/`: Venture Chief Knowledge Officer (oversees `01_intelligence_and_rnd` and links to the Global CKO in `The Café`).
  - `strategy_and_okrs/`: Venture-wide 12-week OKRs and capital allocation strategy.
- `01_intelligence_and_rnd/`: Houses the venture's 4-mode `Think & Know Team` (`Discuss`, `Research`, `Plan`, `Learn`), `reference_library/`, and unified `company_knowledge/` vault.
- `02_product_and_engineering/`: Houses 3 Managers (`platform_engineering_manager`, `automation_and_site_ai_lead`, `qa_and_security_lead`) and 9 specialized engineering workers.
- `03_marketing_and_growth/`: Houses 3 Managers (`content_factory_manager`, `seo_and_community_manager`, `performance_ads_lead`) and 11 specialized growth workers.
- `04_sales_and_crm/`: Houses `sales_and_crm_manager` and 5 outbound/inbound/CRM workers.
- `05_supply_partnerships_and_fulfillment/`: Houses 2 Managers (`supply_partnerships_manager`, `customer_success_manager`) and 6 sourcing/packaging/onboarding workers.
- `06_operations_task_tracking_and_admin/`: Houses `internal_ops_and_task_manager` and 4 workers managing the local WSJF task board, SOP writing, blocker detection, and human coworker coordination.
- `07_finance_and_legal/`: Houses `finance_and_legal_manager` and 3 bookkeeping, unit-economics, and corporate compliance workers.

---

### 3.7 Supreme Command, The Café & Gateways (`30_infrastructure/`)

- `executive_command/`:
  - `jarvis_prime/`: Layer 1 Supreme Interface, intent router (`intent_router.py`), and `autonomy_matrix.yaml`.
  - `global_chief_of_staff/` (Nader): Cross-ecosystem briefing synthesizer and report quality gatekeeper.
  - `global_ops_prioritizer/` (Tarek): Master Task Engine controller and guardian of Ziad's 3-heavy-task daily cap.
  - `global_memory_curator/` (Hares): Guardian of the MCP Memory Layer, WAL Queue, and Semantic IDs.
  - `global_knowledge_officer/` (Hakim - CKO): Supreme head of all `Think & Know Teams`, the `learning_loop`, and moderator of `the_cafe`.
  - `personal_chief_of_staff/` (Amen): Chief executive overseeing all 5 Personal Life Pillars and `ZiadAlhalwany.com`.
- `the_cafe/`:
  - `cafe_protocol_and_moderator.py`: Event-driven networking engine.
  - `eureka_broadcasts/`: Sanitized method cards published when an agent achieves a breakthrough.
  - `cross_pollination_proposals/`: CKO-authored proposals adapting a winning pattern from one pod to another.
  - `peer_consultations/`: Structured technical/methodological Q&A between specialists across pods.
- `channels_bridge/`:
  - `telegram_hotline/`: 1-on-1 bridge between Dr. Ziad and `JARVIS Prime` (voice, text, photos, alerts).
  - `discord_war_rooms/`: Private Discord server bridge running `roundtable_moderator.py` for turn-based multi-agent discussions.
  - `cron_autonomous_scheduler/`: Runs the 07:00 AM morning briefing, 10:00 PM nightly distillation, and automated Git backups.
- `brain_bindings/`: Runtime-agnostic adapter configurations for `Obsidian` and `AppFlowy`.

---

### 3.8 Visual Command Center (`90_dashboard/`)

- `OVERVIEW.md`: Real-time executive pulse across all pillars and ventures.
- `dashboard_server.py`: Local FastAPI web application rendering the visual command center.
- `action_center_5_buttons/`: Interactive review interface presenting pending tasks/proposals with **5 mandatory action buttons**:
  1. **`Approve`** (`+5 pts` to agent; executes action; records Ziad's comment).
  2. **`Cancel`** (`-3 pts` to agent; aborts action; feeds rejection reason to `DECISION_LOG.md` and `skill_evolver_pipeline.py`).
  3. **`Edit`** (`-3 pts` to agent; applies Ziad's inline modifications and extracts a permanent rule patch from the comment).
  4. **`Explain & Discuss First`** (Opens a turn-based Discord War Room or Telegram thread to debate the plan before execution).
  5. **`Mandatory Feedback Comment`** (Required input field that fuels continuous agent self-improvement).
- `ziad_daily_focus_sheet/`: Displays strictly Ziad's personal daily tasks (hard-capped at 3 heavy tasks/day) split into one-time projects and recurring routines.
- `live_org_graph_and_scorecards/`: Visual authority tree, Café synergy links, total headcount, active WIP per team, and the 100-point agent leaderboard.
- `global_blockers_radar/`: Real-time list of stalled or overdue tasks across the entire ecosystem sorted by WSJF impact.
