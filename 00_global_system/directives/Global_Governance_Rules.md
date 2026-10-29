# J.A.R.V.I.S. V1 — Global Governance, Guardrails & Operational Protocols (`Global_Governance_Rules.md`)

**Governing Law:** `.specify/memory/constitution.md` (Principles I, IV, V, VI, VII, VIII)

---

## 1. Chain of Command & Communication Protocol

1. **Single Point of Personal Contact (`JARVIS Prime`):**
   - `JARVIS Prime` (`30_infrastructure/executive_command/jarvis_prime`) is the **only** digital employee permitted to send messages, voice summaries, alerts, or phone calls to Dr. Ziad on Telegram.
   - No C-Suite officer, Department Manager, or Worker may message Dr. Ziad directly on Telegram.
2. **Compressed Fast-Path vs. Hierarchical Deep-Path:**
   - **Fast-Path (1-Hop Execution):** When Dr. Ziad sends a quick capture (voice note, clinical case log, quick task, bookmark), `JARVIS Prime` writes it to `wal_queue.db` (`< 10ms`) and invokes `mcp_memory_server.py` directly without waking up 4 layers of managers.
   - **Deep-Path (Multi-Layer Delegation):** When Dr. Ziad initiates a strategic project, feature build, campaign, or research directive, `JARVIS Prime` routes the brief to the appropriate Level-2 Executive (`Global C-Suite`, `Personal Chief of Staff`, or `Venture CEO`), who decomposes and assigns it to Level-3 Managers and Level-4 Workers.
3. **Graduated Autonomy Matrix (`autonomy_matrix.yaml`):**
   - **Level 1 (`HUMAN_GATED`):** Default for all new workflows and all irreversible actions. Agent prepares work to `90%` completion and stages it in `review_queue_approvals.md`.
   - **Level 2 (`EXECUTE_AND_NOTIFY`):** Unlocked for reversible internal tasks after `5` consecutive first-pass approvals (`+25 pts`) with zero edits. Agent executes and logs a summary in the daily briefing.
   - **Level 3 (`FULL_AUTONOMOUS`):** Unlocked for routine, reversible SOPs after `10` consecutive first-pass approvals (`+50 pts`) and explicit promotion by Dr. Ziad. Any single rejection (`-3 pts`) immediately demotes the task type back to `Level 1`.

---

## 2. The Quad-Shield Task Engine Protocol

Every task entering the global inbox or any pod's `LOCAL_BOARD.md` passes through four mandatory shields:

### Shield 1: Eisenhower Matrix Classification

| Quadrant                         | Criteria                                                                            | Routing Destination                                                                      |
| :------------------------------- | :---------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------- |
| **Q1: Do Immediately (Red)**     | High Importance + High Urgency + Requires Ziad's personal physical/strategic action | Routed to `ziad_daily_focus_sheet` (Hard cap: **Max 3 heavy tasks/day**).                |
| **Q2: Schedule & Plan (Yellow)** | High Importance + Not Urgent                                                        | Routed to Level-3 Department/Capability Manager to structure into a 12-Week Sprint plan. |
| **Q3: Delegate (Blue)**          | Low Personal Requirement + Urgent/Routine                                           | Routed directly to Level-4 Specialized Worker for immediate autonomous execution.        |
| **Q4: Eliminate (White)**        | Low Importance + Low Value                                                          | Archived automatically to `99_archive/cold_storage`; zero time or tokens spent.          |

### Shield 2: Deterministic WSJF Prioritization

Inside each quadrant, `eisenhower_wsjf_wip_engine.py` scores and sorts tasks in pure Python (`0 LLM tokens`):

- **Inputs (1 to 10 integer scale):**
  - `value`: Business revenue, clinical growth, or life impact.
  - `urgency`: Time criticality / deadline decay.
  - `risk_reduction`: Risk mitigated or new opportunity unlocked.
  - `effort`: Estimated job duration/complexity.
- **Formula:** `WSJF = round((value + urgency + risk_reduction) / max(effort, 1), 2)`
- **Rule:** Higher `WSJF` always executes first. Ties are broken by `urgency`, then FIFO timestamp.

### Shield 3: Hard Kanban WIP Limits

- **Team WIP Limit:** Maximum **`3`** tasks in `IN_PROGRESS` status per department/capability team at any given moment. A 4th task cannot transition to `IN_PROGRESS` until an active task moves to `REVIEW_QUEUE` or `COMPLETED`.
- **Commander Cognitive Limit:** Maximum **`3`** heavy cognitive tasks assigned to Dr. Ziad per day on `ziad_daily_focus_sheet`.

### Shield 4: The 85% Confidence Gate & Reversibility Gate

1. **85% Confidence Gate (`pre_task_confidence_gate.py`):**
   - Before a worker begins execution, it checks whether all required schema parameters exist and computes a clarity score (`0.0` to `1.0`).
   - If `clarity_score < 0.85`, the task transitions to `DISCUSS_FIRST` and formulates a maximum of 3 sharp clarifying questions for Dr. Ziad. Guessing is a constitutional violation.
2. **Reversibility Gate (`pre_write_reversibility_gate.py`):**
   - Any action with `is_reversible: false` (publishing to live websites/social media, spending money, modifying production schemas, deleting files, contacting external clients) is blocked prior to execution and staged in `review_queue_approvals.md`.

---

## 3. The 5-Button Action Center & Self-Evolution Loop

Every item in `review_queue_approvals.md` and `90_dashboard/action_center_5_buttons/` requires Dr. Ziad to select one of four action buttons accompanied by the **5th mandatory element (Feedback Comment)**:

| Action Button                    | System Behavior                                                                           | Scorecard Impact              | Learning Loop Trigger (`skill_evolver_pipeline.py`)                                                               |
| :------------------------------- | :---------------------------------------------------------------------------------------- | :---------------------------- | :---------------------------------------------------------------------------------------------------------------- |
| **1. `Approve`**                 | Releases the staged action for final execution and marks task `COMPLETED`.                | **`+5 pts`** to Worker & Team | If comment contains praise or a specific nuance, logs positive pattern in `sessions_traces/`.                     |
| **2. `Cancel`**                  | Aborts execution, archives draft, and logs rejection in `DECISION_LOG.md`.                | **`-3 pts`** to Worker & Team | Parses mandatory comment to extract an anti-pattern rule in `feedback_patches/` so the mistake is never repeated. |
| **3. `Edit`**                    | Applies Ziad's edits, executes the modified output, and diffs before vs. after.           | **`-3 pts`** to Worker & Team | Diffs Ziad's edit + comment to stage a permanent update to `DNA_AND_VOICE.md` or `SKILL.md`.                      |
| **4. `Explain & Discuss First`** | Pauses execution and opens a turn-based thread in Telegram or a Private Discord War Room. | `0 pts` (Neutral)             | Captures the ensuing discussion transcript into `sessions_traces/` to refine the plan.                            |
| **5. `Mandatory Comment`**       | Required text/voice note explaining _why_ the decision was made.                          | N/A                           | Primary training signal for `skill_evolver_pipeline.py` and `DECISION_LOG.md`.                                    |

---

## 4. Event-Driven Café Protocol (`30_infrastructure/the_cafe/`)

To enable cross-project innovation while preventing token-burning chat loops and data leaks:

1. **Zero Free-Form Chat:** Agents cannot open casual conversations in `the_cafe/`.
2. **Three Allowed Event Payloads (All filtered by `cafe_privacy_sanitizer.py`):**
   - **Event A — `Eureka Broadcast` (`eureka_broadcasts/`):** Triggered automatically when a task receives a first-pass `Approve` (`+5 pts`) on a novel problem or creates a new SOP (`+10 pts`). Contains strictly: _Problem Archetype_, _Abstracted Methodology/Workflow_, and _Measured Outcome_.
   - **Event B — `CKO Cross-Pollination Proposal` (`cross_pollination_proposals/`):** The `Global Knowledge Officer (Hakim)` matches a Eureka Broadcast from Pod A to a known goal or blocker in Pod B and sends a proposal to Pod B's leadership. If adopted and approved by Ziad, the originating agent earns a **`+5 pts` Café Synergy Bonus**.
   - **Event C — `Peer Consultation` (`peer_consultations/`):** An agent in Pod A posts a method-only technical question tagged for a specialist in Pod B. The specialist replies in a single structured turn.

---

## 5. Private Discord War Room Roundtable Protocol (`roundtable_moderator.py`)

1. **Private Server Mandate:** Discord integration operates exclusively on Dr. Ziad's locked, private Discord server. Connecting agents with file/code permissions to any public Discord server is strictly prohibited (mitigating `CVE-2026-25253` class risks).
2. **Turn-Based Roundtable Execution (Zero Infinite Loops):**
   - Bots ignore direct bot triggers unless orchestrated by `roundtable_moderator.py`.
   - When Dr. Ziad posts a topic in a project War Room and selects a mode (`Discuss`, `Research`, `Plan`, or `Learn`), the moderator invokes the relevant specialists sequentially (e.g., _Turn 1: Market Intel -> Turn 2: Devil's Advocate Critic -> Turn 3: Team Lead Synthesis_) and then **locks the room to wait for Dr. Ziad's next message**.
