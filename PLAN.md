# PROJECT J.A.R.V.I.S. (V1) — EXECUTIVE SUMMARY, ARCHITECTURE & SPEC KIT MASTER ROADMAP

**Workspace Root:** `D:\AI_Workspace\Jarvis V1`  
**Owner & Supreme Commander:** Dr. Ziad Mohamed Alhalwany  
**Development Methodology:** Spec-Driven Development (SDD) via GitHub Spec Kit (`specify-cli`)  
**Compatible Runtimes:** Hermes Agent (24/7 Autonomous Loops), Claude Code / Cowork, OpenAI Codex, Local Ollama + Frontier LLMs

---

## PART 0: Execution Philosophy: Golden Blueprint First, Clone Second

To guarantee zero structural errors across 140+ digital employees and 7 standalone pods, implementation follows a strict **Golden Template & Progressive Verification** strategy:

1. Build the **Shared Global Core (`00_global_system`)** and **Master Templates (`01_templates`)** once with 100% test coverage.
2. Build and verify **one Golden Business Pod (`20_businesses/medicophilia`)** and **one Golden Life Pillar Pod (`10_pillars/01_health_and_growth`)** from top to bottom.
3. Clone the verified Golden Templates to instantiate `travelophilia` and the remaining 4 Life Pillars (`02_spiritual`, `03_clinical_and_learning`, `04_personal_branding`, `05_personal_finance`).
4. Every Phase Gate requires passing automated unit tests, `doc_guardian.py` synchronization, and the **Pod Detachability Test (`copy -> boot -> operate -> report`)**.

## PART 1: EXECUTIVE SUMMARY

### 1.1 Core Problem & Strategic Vision

Dr. Ziad Mohamed Alhalwany operates across multiple high-output arenas simultaneously: clinical medical training, entrepreneurship (`Travelophilia` in travel/student transport/Erasmus and `Medicophilia` in medical education/healthcare SaaS), multi-channel personal branding (`Ziad Alhalwany`, `medwithziad`, `travelwithziad`), polymath learning, spiritual discipline, health optimization, and wealth management.

- **The Root Bottleneck:** Manual execution across fragmented domains creates cognitive overload, context switching, lost ideas, and stalled execution.
- **The J.A.R.V.I.S. Solution:** A federated, self-evolving **Life & Enterprise Operating System** housed in `D:\AI_Workspace\Jarvis V1`. It elevates Ziad from a manual executor to a **Supreme Commander & Strategic Decision-Maker** supported by a 24/7 digital workforce of specialized AI executives, managers, and workers.

### 1.2 The 7 Non-Negotiable Architectural Laws (`.specify/memory/constitution.md`)

1. **Law 1 — Dual-Topology Organization (Strict Authority Tree + Flexible Knowledge Graph):**
   - **Authority Layer (Vertical Tree):** Enforces strict command hierarchy, permissions, and 100% tenant data isolation. `JARVIS Prime` is the **sole** agent allowed to message, notify, or call Ziad directly on Telegram. Sub-agents only interact with Ziad when explicitly summoned into a private Discord War Room.
   - **Knowledge & Social Layer (Horizontal Graph — `The Café`):** Hosted in `30_infrastructure/the_cafe/` and moderated by the `Global Knowledge Officer (CKO)`. Agents never engage in wasteful free-form chat loops. Instead, `The Café` operates on **Event-Driven Protocols**: (a) _Eureka Broadcasts_ (anonymized winning methods), (b) _CKO Smart Matchmaking_ (cross-pollinating ideas across ventures/pillars), and (c) _Peer Consultations_ (method-only Q&A stripped of private data).

2. **Law 2 — Federated Self-Contained Pods (`_pod_core`) & 100% Detachability:**
   - Every commercial business in `20_businesses/` and every personal life pillar in `10_pillars/` is built as a **Standalone Micro-OS Pod** containing its own `_pod_core/` directory:
     - `_pod_core/local_task_engine/`: Local task board (`LOCAL_BOARD.md`), local approval queue, and `public_telemetry_rollup.json`.
     - `_pod_core/web_and_human_gateway/`: Live website/CMS/CRM API connectors (so agents can publish trips, medical courses, blogs, or update CRM leads on the venture's website or Ziad's personal portfolio site) plus `human_rbac_permissions.yaml` (allowing human employees to collaborate with a single business's agents without any access to Ziad's personal life or other businesses).
     - `_pod_core/local_mcp_and_plugins/` & `_pod_core/_governance_and_registry/`: Local MCP configs, hooks, scorecards, and blockers.
   - **Detachability Guarantee:** Any business or pillar folder can be copied out of `D:\AI_Workspace\Jarvis V1` onto a separate server and operate at 100% capacity without breaking.

3. **Law 3 — Standardized Outer Shell & 6 Power Amplifiers per Pod:**
   - Every business and life pillar pod contains a standardized outer shell:
     1. `BUSINESS.md` or `PILLAR.md` (Charter, vision, ICP, boundaries).
     2. `DNA_AND_VOICE.md` (Psycholinguistic persona, tone, human-natural writing rules, zero AI-tell punctuation/em-dashes).
     3. `STATE.md` (Live telemetry, KPIs, active streaks, sprint health).
     4. `DECISION_LOG.md` (Historical archive of approved and rejected ideas so agents never re-pitch rejected concepts).
     5. `distilled_context.md` (Ultra-compressed 2-page context summary saving 80% of tokens on agent boot).
     6. `triggers_and_watchers.yaml` (Scheduled routines and event triggers).
     7. `identifiers/public_id.yaml` (Shareable marketing hooks) vs. `identifiers/private_id.yaml` (Locked financials, contracts, API keys).
     8. `swipe_files_and_benchmarks/`, `reference_library/` (raw sources), `knowledge_vault/` (synced Obsidian notes), `sessions_traces/` (raw thinking scratchpads), and `reports_deliverables/` (clean, human-grade shareable reports).

4. **Law 4 — Dual-Tier Memory, Deterministic MCP Server & Zero-Loss Queue:**
   - **Working vs. Permanent Memory:** Short-term tactical scratchpads live in the agent runtime; all permanent knowledge and structured data live in Ziad's owned storage (`Obsidian` Markdown vaults for linked knowledge + `AppFlowy` / SQLite / Postgres for structured tables).
   - **5 Universal Deterministic Functions:** Agents never call storage APIs directly. All operations pass through `00_global_system/memory_layer/mcp_memory_server.py` (`save_entity`, `query_memory`, `update_state`, `link_entities`, `check_health`) governed by a declarative `memory_schema.yaml`.
   - **Write-Ahead Buffer (`wal_queue.db`):** Every incoming Telegram voice note, text, or task is written within 10ms to `wal_queue.db` (`PENDING`). If Obsidian or AppFlowy is offline, zero requests are ever lost.
   - **Bidirectional Semantic IDs:** Every note and task receives an atomic ID (`JAR-2026-0001`, `MED-2026-0001`, `TRV-2026-0001`, `CLN-2026-0001`) linking the Obsidian `.md` file and the AppFlowy database row in both directions.
   - **Human-Gated Watchdog:** `memory_watchdog_agent.py` monitors queue health, fixes minor formatting errors, and proposes `memory_schema.yaml` upgrades for Ziad's approval without ever modifying core code autonomously.

5. **Law 5 — Quad-Shield Master Task Engine & Cognitive Load Protection:**
   - **Shield 1 (Eisenhower Matrix):** Routes tasks into `Do Immediately (Ziad)`, `Schedule (Manager)`, `Delegate (Worker)`, or `Eliminate (Archive)`.
   - **Shield 2 (Deterministic Python WSJF):** `wsjf_engine.py` calculates `WSJF = (Value + Urgency + Risk Reduction) / Effort Size` deterministically at zero token cost so high-value, short-duration tasks always rank first.
   - **Shield 3 (Kanban WIP Limits):** Max 3 concurrent active tasks per agent team; max 3 heavy cognitive tasks assigned to Ziad per day.
   - **Shield 4 (85% Confidence Gate + Reversibility Gate):**
     - If task clarity is below `85%`, `pre_task_confidence_gate.py` halts execution and switches to `Explain & Discuss First` mode to ask Ziad clarifying questions rather than guessing.
     - Any irreversible action (`is_reversible: false`: spending money, publishing publicly, deleting data, messaging external clients) is intercepted by `pre_write_reversibility_gate.py` and placed in `review_queue_approvals.md` for Ziad's **5-Button Decision** (`Approve`, `Cancel`, `Edit`, `Explain & Discuss First`, plus a **Mandatory Feedback Comment**).
   - **Federated One-Way Rollup:** `federation_rollup_sync.py` pulls sanitized progress telemetry from each isolated pod's `LOCAL_BOARD.md` into the global `MASTER_BOARD.md`.

6. **Law 6 — Self-Evolution Loop, Do-Document-Delegate (SOPs) & Gamified 100-Point Scorecards:**
   - **Feedback-to-Rule & Scratchpad-to-Skill:** `skill_evolver_pipeline.py` parses Ziad's mandatory dashboard comments and `sessions_traces/` scratchpads into proposed `SKILL.md` bundles and `DNA_AND_VOICE.md` rule patches awaiting Ziad's approval.
   - **Do-Document-Delegate:** Routine tasks performed by Ziad 1–2 times are observed and converted into `playbooks_and_sops/` for autonomous execution thereafter.
   - **Gamified 100-Point Scorecard:** `scorecard_engine.py` awards `+5 pts` for first-pass approval, `-3 pts` for rejection/edit, `+10 pts` for creating verified SOPs, `+5 pts` for Café synergy, and `-5 pts` for overdue tasks (automatically logged in `blockers.md`).

7. **Law 7 — Tiered Model Routing & Frugal Engineering:**
   - Routine extraction, sorting, and formatting route to zero-cost deterministic Python scripts or local models (`Ollama`); heavy synthesis and coding route to frontier models (`Claude / Codex`) with `distilled_context.md` pre-loading.

---

## PART 2: COMPLETE DIGITAL WORKFORCE ROSTER & ORG HIERARCHY

```text
[LEVEL 0: DR. ZIAD MOHAMED ALHALWANY] (Supreme Commander & Final Approver)
   │
   ▼
[LEVEL 1: JARVIS PRIME] (Supreme AI Interface — Sole agent permitted to call/message Ziad on Telegram)
   │
   ├──► [LEVEL 2A: GLOBAL HOLDING C-SUITE] (Shared Cross-Ecosystem Governance in 30_infrastructure/executive_command)
   │      ├── 1. Global Chief of Staff (Nader): Cross-venture synthesis, daily briefings & report QA gatekeeper
   │      ├── 2. Global Ops Prioritizer (Tarek): Master Task Board, WSJF/WIP enforcement & Ziad's time protector
   │      ├── 3. Global Memory Curator (Hares): MCP Memory Layer watchdog, WAL Queue & Semantic ID guardian
   │      ├── 4. Global Knowledge Officer (Hakim - CKO): Head of all Think & Know Teams, Learning Loop & The Café
   │      └── 5. Documentation Guardian (Raqib): Automated living documentation & directory synchronizer
   │
   ├──► [LEVEL 2B: PERSONAL LIFE OS EXECUTIVE]
   │      └── 6. Personal Chief of Staff (Amen): Oversees all 5 Personal Life Pillars & ZiadAlhalwany.com
   │
   └──► [LEVEL 2C: COMMERCIAL VENTURE C-SUITE CABINETS] (100% Isolated inside each Business Pod)
          ├── 7. Medicophilia C-Suite Cabinet (CEO, CTO/CPO, CMO/CRO, COO, CFO/CLO, Venture CKO)
          └── 8. Travelophilia C-Suite Cabinet (CEO, CTO/CPO, CMO/CRO, COO, CFO/CLO, Venture CKO)
```

### 2.1 Detailed Workforce Inside Each Commercial Business Pod (`Medicophilia` & `Travelophilia`)

Each business houses **6 C-Suite Executives**, **11 Department Managers**, and **44 Hyper-Specialized Workers** across 7 Functional Departments:

- **`00_c_suite_leadership/`**:
  - `venture_ceo` (Sole link to JARVIS Prime / Human Venture Director), `venture_cto_cpo`, `venture_cmo_cro`, `venture_coo`, `venture_cfo_clo`, `venture_cko`.
- **`01_intelligence_and_rnd/` (Reports to Venture CKO)**:
  - _Manager:_ `think_and_know_team_manager` (Operates in 4 Modes: `Discuss`, `Research`, `Plan`, `Learn`).
  - _Workers (6):_ `market_competitor_intel`, `deep_reader_transcriber`, `executive_summarizer`, `devils_advocate_critic`, `customer_psychologist`, `obsidian_skill_linker`.
- **`02_product_and_engineering/` (Reports to Venture CTO/CPO)**:
  - _Managers (3):_ `platform_engineering_manager`, `automation_and_site_ai_lead`, `qa_and_security_lead`.
  - _Workers (9):_ `frontend_ui_ux_builder`, `backend_api_architect`, `database_schema_engineer`, `cms_website_publisher`, `webhook_mcp_integrator`, `site_chatbot_operator`, `web_scraper_pipeline`, `automated_test_hunter`, `security_privacy_auditor`.
- **`03_marketing_and_growth/` (Reports to Venture CMO/CRO)**:
  - _Managers (3):_ `content_factory_manager`, `seo_and_community_manager`, `performance_ads_lead`.
  - _Workers (11):_ `short_form_reels_writer`, `carousel_thread_architect`, `long_form_blog_writer`, `visual_prompt_art_director`, `trojan_horse_funnel_integrator`, `technical_seo_worker`, `social_scheduler`, `community_responder`, `ad_creative_tester`, `cro_landing_optimizer`, `cac_ltv_analyst`.
- **`04_sales_and_crm/` (Reports to Venture CMO/CRO)**:
  - _Manager (1):_ `sales_and_crm_manager`.
  - _Workers (5):_ `inbound_lead_qualifier`, `b2b_outbound_prospector`, `proposal_pitch_builder`, `objection_closing_coach`, `crm_pipeline_tracker`.
- **`05_supply_partnerships_and_fulfillment/` (Reports to Venture COO)**:
  - _Managers (2):_ `supply_partnerships_manager`, `customer_success_manager`.
  - _Workers (6):_ `partner_vetting_sourcing` (DMCs/Airlines in Travel; Doctors/Clinics in Med), `grant_and_opportunity_scout` (Erasmus/Zero-Fee in Travel; Fellowships/Grants in Med), `package_itinerary_architect`, `client_onboarding_concierge`, `issue_support_resolver`, `review_referral_collector`.
- **`06_operations_task_tracking_and_admin/` (Reports to Venture COO)**:
  - _Manager (1):_ `internal_ops_and_task_manager`.
  - _Workers (4):_ `local_task_wsjf_coordinator`, `sop_playbook_writer`, `sprint_blocker_watchdog`, `human_coworker_liaison`.
- **`07_finance_and_legal/` (Reports to Venture CFO/CLO)**:
  - _Manager (1):_ `finance_and_legal_manager`.
  - _Workers (3):_ `bookkeeping_invoice_tracker`, `unit_economics_pricer`, `international_corp_tax_researcher`.

### 2.2 Detailed Workforce Across the 5 Personal Life Pillars (`10_pillars/`)

Every life pillar is structured under a **Pillar Lead (`00_pillar_lead`)** and **4 Capability Managers** (`01_think_and_learn`, `02_execute_and_build`, `03_delegate_and_automate`, `04_monitor_and_metrics`) merging **Capabilities + PARA + GTD + Quantified Self Trackers + 12-Week Sprints**:

1. **`01_health_and_growth` (12 Workers):** `nutrition_and_bio_researcher`, `fitness_performance_researcher`, `sleep_neuro_recovery_researcher`, `behavioral_habit_psychologist`, `workout_recovery_planner`, `meal_and_macro_architect`, `style_wardrobe_advisor`, `presence_and_communication_coach`, `clinic_and_gym_booker`, `personal_procurement_worker`, `biometrics_and_habit_tracker`, `fitness_event_and_opportunity_scout`.
2. **`02_spiritual` (8 Workers — Strict Verified Sources Only):** `quran_tafsir_verifier`, `hadith_and_fiqh_verifier`, `tazkiyah_insights_synthesizer`, `wards_and_khatmah_planner`, `seasonal_worship_architect`, `charity_and_sadaqah_automator`, `prayer_and_ward_consistency_tracker`, `spiritual_reflection_logger`.
3. **`03_clinical_and_learning` (10 Workers):** `hospital_clinical_case_logger`, `differential_diagnosis_analyst`, `pubmed_guidelines_researcher`, `polymath_cross_domain_researcher`, `medical_board_case_simulator`, `spaced_repetition_study_planner`, `book_and_lecture_distiller`, `cme_and_medical_portfolio_organizer`, `clinical_procedure_logbook_tracker`, `medical_fellowship_and_grant_scout`.
4. **`04_personal_branding` (12 Workers — Connected to `ZiadAlhalwany.com`):** `viral_trend_deconstructor`, `audience_psychology_researcher`, `short_form_reels_hook_writer`, `carousel_and_thread_writer`, `long_form_article_writer`, `photorealistic_prompt_art_director`, `trojan_horse_funnel_architect`, `personal_website_portfolio_publisher`, `multi_platform_social_scheduler`, `brand_growth_analytics_tracker`, `pr_podcast_and_media_scout`, `vip_networking_crm_worker`.
5. **`05_personal_finance` (6 Workers — Maximum Security Lock):** `sharia_compliant_wealth_researcher`, `personal_budget_and_asset_planner`, `emergency_fund_and_goal_modeler`, `subscriptions_and_bills_coordinator`, `official_documents_vault_keeper`, `net_worth_and_expense_anomaly_tracker`.

---

## PART 3: COMPLETE TARGET DIRECTORY TREE (`D:\AI_Workspace\Jarvis V1`)

```text
D:\AI_Workspace\Jarvis V1\
│   README.md                                        # Quick-start portal & ecosystem overview
│   ARCHITECTURE.md                                  # Living macro-to-micro explanation of every folder & file
│   JARVIS_V1_MASTER_BLUEPRINT.md                    # This master executive summary & Spec Kit roadmap
│   PROJECT_GENESIS_AND_DISCUSSIONS_DRAFT.md         # Complete intellectual history & architectural debates
│   CLAUDE.md                                        # Root entry hook for Claude Code / Cowork / Codex / Hermes
│   .mcp.json                                        # Root MCP server mounting configuration
│   .env.example                                     # Isolated environment variables template
│   .gitignore                                       # Protects secrets, SQLite WAL files & temp caches
│
├── .specify\                                        # [GitHub Spec Kit Core]
│   ├── memory\
│   │   └── constitution.md                          # Immutable 7 Architectural Laws governing all specs
│   ├── scripts\
│   └── templates\
│
├── specs\                                           # [Spec Kit Phase Specifications 001 to 008]
│   ├── 001-phase0-foundation-and-docs\              # spec.md, plan.md, tasks.md
│   ├── 002-phase1-memory-layer-and-wal-queue\       # spec.md, plan.md, tasks.md
│   ├── 003-phase2-master-task-engine-and-federation\# spec.md, plan.md, tasks.md
│   ├── 004-phase3-agent-registry-templates-learning\# spec.md, plan.md, tasks.md
│   ├── 005-phase4-executive-command-cafe-channels\  # spec.md, plan.md, tasks.md
│   ├── 006-phase5-golden-business-pod-medicophilia\ # spec.md, plan.md, tasks.md
│   ├── 007-phase6-golden-pillar-pod-health-life-os\ # spec.md, plan.md, tasks.md
│   └── 008-phase7-command-dashboard-runtime-wiring\ # spec.md, plan.md, tasks.md
│
├── 00_global_system\                                # [Layer 0: Shared Core Engine]
│   ├── directives\
│   │   ├── Ziad_Cognitive_DNA.md
│   │   ├── Global_Governance_Rules.md
│   │   └── Detachability_Standard.md
│   ├── memory_layer\
│   │   ├── mcp_memory_server.py                     # 5 deterministic CRUD+Link MCP tools
│   │   ├── memory_schema.yaml                       # Declarative routing schema (Obsidian <-> AppFlowy/SQLite)
│   │   ├── semantic_id_generator.py                 # Atomic ID generator (MED-2026-0001, TRV-2026-0001...)
│   │   └── memory_watchdog_agent.py                 # Monitors queue & proposes human-gated schema fixes
│   ├── queue_vault\
│   │   ├── wal_queue_manager.py                     # Zero-loss SQLite Write-Ahead Buffer manager
│   │   ├── wal_queue.db                             # Persistent SQLite queue database
│   │   └── staging_media_inbox\                     # Raw voice notes, screenshots & files before ingestion
│   ├── master_task_engine\
│   │   ├── MASTER_BOARD.md                          # Global aggregated task board
│   │   ├── review_queue_approvals.md                # 5-Button Approval Queue + Mandatory Comment log
│   │   ├── eisenhower_wsjf_wip_engine.py            # Deterministic WSJF calculator & WIP limit enforcer
│   │   ├── federation_rollup_sync.py                # One-way telemetry sync from isolated pods to Master Board
│   │   └── task_engine_config.yaml                  # WIP limits (3/team, 3 heavy/day for Ziad) & SLA rules
│   ├── agent_registry\
│   │   ├── DIRECTORY.md                             # Auto-synced roster & headcount of all digital employees
│   │   ├── scorecards_leaderboard.md                # Live 100-point gamified ranking of agents, teams & pods
│   │   ├── scorecard_engine.py                      # Deterministic points calculator (+5/-3/+10/+5)
│   │   └── cards\                                   # Central index of all AGENT.md profiles
│   ├── learning_loop\
│   │   ├── skill_evolver_pipeline.py                # Converts Ziad's comments & session traces into skills/SOPs
│   │   ├── proposed_skills\                         # Staged SKILL.md bundles awaiting Ziad's approval
│   │   ├── feedback_patches\                        # Staged DNA_AND_VOICE.md / instruction patches
│   │   └── extracted_sops\                          # Do-Document-Delegate playbooks distilled from Ziad
│   ├── mcp_servers\
│   │   └── global_mcp_registry.json
│   ├── plugins_and_integrations\
│   │   └── global_plugins_config.yaml
│   ├── hooks_and_guardrails\
│   │   ├── pre_task_confidence_gate.py              # Enforces >= 85% clarity or halts in Explain & Discuss mode
│   │   ├── pre_write_reversibility_gate.py          # Blocks irreversible actions until Ziad approves
│   │   └── cafe_privacy_sanitizer.py                # Strips private identifiers from Cafe broadcasts
│   ├── skills\                                      # Universal skills (deep_web_research, voice_ingestor, sop_distiller)
│   ├── reference_library\                           # Global raw books, papers & reference documents
│   └── scripts\
│       ├── doc_guardian.py                          # Auto-updates DIRECTORY.md & ARCHITECTURE.md tree stats
│       └── clone_pod.py                             # Instant cloner for new businesses or pillars
│
├── 01_templates\                                    # [Master Cloning Blueprints]
│   ├── standalone_business_pod_template\
│   ├── standalone_pillar_pod_template\
│   ├── department_module_template\
│   ├── think_and_know_team_template\
│   ├── agent_card_template\
│   │   └── AGENT.md
│   └── skill_bundle_template\
│       ├── SKILL.md
│       ├── scripts\
│       ├── templates\
│       └── references\
│
├── 10_pillars\                                      # [Personal Life OS — 5 Standalone Pods]
│   ├── 01_health_and_growth\                        # ★ Golden Pillar Pod ★
│   │   ├── PILLAR.md
│   │   ├── DNA_AND_VOICE.md
│   │   ├── STATE.md
│   │   ├── DECISION_LOG.md
│   │   ├── distilled_context.md
│   │   ├── triggers_and_watchers.yaml
│   │   ├── identifiers\ (public_id.yaml, private_id.yaml)
│   │   ├── _pod_core\ (local_task_engine\, local_mcp_and_plugins\, local_hooks\, _governance_and_registry\)
│   │   ├── 00_pillar_lead\ (AGENT.md)
│   │   ├── 01_think_and_learn\ (manager\, workers\, reference_library\, knowledge_vault\)
│   │   ├── 02_execute_and_build\ (manager\, workers\, active_projects\, areas_and_sops\)
│   │   ├── 03_delegate_and_automate\ (manager\, workers\)
│   │   ├── 04_monitor_and_metrics\ (manager\, workers\, metrics_and_logs\)
│   │   ├── swipe_files_and_benchmarks\
│   │   ├── skills\
│   │   ├── sessions_traces\
│   │   └── reports_deliverables\
│   ├── 02_spiritual\
│   ├── 03_clinical_and_learning\
│   ├── 04_personal_branding\
│   └── 05_personal_finance\
│
├── 20_businesses\                                   # [Commercial Ventures — 100% Isolated Standalone Pods]
│   ├── medicophilia\                                # ★ Golden Business Pod ★
│   │   ├── BUSINESS.md
│   │   ├── DNA_AND_VOICE.md
│   │   ├── STATE.md
│   │   ├── DECISION_LOG.md
│   │   ├── distilled_context.md
│   │   ├── triggers_and_watchers.yaml
│   │   ├── identifiers\ (public_id.yaml, private_id.yaml)
│   │   ├── _pod_core\
│   │   │   ├── local_task_engine\ (VENTURE_TASK_BOARD.md, venture_review_approvals.md, public_telemetry_rollup.json)
│   │   │   ├── web_and_human_gateway\ (website_cms_crm_connector.py, human_rbac_permissions.yaml)
│   │   │   ├── local_mcp_and_plugins\
│   │   │   ├── local_hooks\
│   │   │   └── _governance_and_registry\ (venture_agents_directory.md, venture_scorecard_points.md, okrs_12_week_sprint.md, venture_blockers.md)
│   │   ├── 00_c_suite_leadership\ (venture_ceo\, venture_cto_cpo\, venture_cmo_cro\, venture_coo\, venture_cfo_clo\, venture_cko\, strategy_and_okrs\)
│   │   ├── 01_intelligence_and_rnd\ (think_and_know_team\, reference_library\, company_knowledge\)
│   │   ├── 02_product_and_engineering\ (3 managers, 9 workers, playbooks_and_sops\, active_tasks\)
│   │   ├── 03_marketing_and_growth\ (3 managers, 11 workers, playbooks_and_sops\, active_tasks\)
│   │   ├── 04_sales_and_crm\ (1 manager, 5 workers, playbooks_and_sops\, active_tasks\)
│   │   ├── 05_supply_partnerships_and_fulfillment\ (2 managers, 6 workers, playbooks_and_sops\, active_tasks\)
│   │   ├── 06_operations_task_tracking_and_admin\ (1 manager, 4 workers, playbooks_and_sops\, active_tasks\)
│   │   ├── 07_finance_and_legal\ (1 manager, 3 workers, playbooks_and_sops\, active_tasks\)
│   │   ├── swipe_files_and_benchmarks\
│   │   ├── skills\
│   │   ├── sessions_traces\
│   │   └── reports_deliverables\
│   └── travelophilia\                               # Cloned & customized for Travel/Transport/Erasmus
│
├── 30_infrastructure\                               # [Supreme Command, The Café & Communication Gateways]
│   ├── executive_command\ (jarvis_prime\, global_chief_of_staff\, global_ops_prioritizer\, global_memory_curator\, global_knowledge_officer\, personal_chief_of_staff\)
│   ├── the_cafe\ (cafe_protocol_and_moderator.py, eureka_broadcasts\, cross_pollination_proposals\, peer_consultations\)
│   ├── channels_bridge\ (telegram_hotline\, discord_war_rooms\, cron_autonomous_scheduler\)
│   └── brain_bindings\ (obsidian_config\, appflowy_config\)
│
├── 90_dashboard\                                    # [Ziad's Visual Command Center]
│   ├── OVERVIEW.md
│   ├── dashboard_server.py                          # Local FastAPI reactive UI for the 5 Action Buttons
│   ├── action_center_5_buttons\
│   ├── ziad_daily_focus_sheet\
│   ├── live_org_graph_and_scorecards\
│   └── global_blockers_radar\
│
└── 99_archive\
    └── cold_storage\
```

---

## PART 4: PHASE-BY-PHASE SPEC KIT IMPLEMENTATION SPECIFICATIONS

Below are the 8 sequential phases designed for execution via GitHub Spec Kit (`/speckit.specify` -> `/speckit.plan` -> `/speckit.tasks` -> `/speckit.implement`).

---

### PHASE 0: Foundation, Federated Directory Skeleton & Living Documentation

- **Spec Kit Feature Directory:** `specs/001-phase0-foundation-and-docs`

#### 1. Specification (`spec.md`)

- **Objective:** Establish the complete federated directory tree inside `D:\AI_Workspace\Jarvis V1`, author the foundational governance and architectural documents (`README.md`, `ARCHITECTURE.md`, `PROJECT_GENESIS_AND_DISCUSSIONS_DRAFT.md`, `CLAUDE.md`), and deploy the automated Documentation Guardian (`doc_guardian.py`).
- **Functional Requirements:**
  - `FR-0.1`: Create all top-level and nested directories for `00_global_system`, `01_templates`, `10_pillars`, `20_businesses`, `30_infrastructure`, `90_dashboard`, and `99_archive`.
  - `FR-0.2`: Author `ARCHITECTURE.md` with protected auto-sync markers (`<!-- AUTO-STATS-START -->` / `<!-- AUTO-STATS-END -->`) explaining every folder and file from macro to micro levels.
  - `FR-0.3`: Implement `00_global_system/scripts/doc_guardian.py` to scan `D:\AI_Workspace\Jarvis V1`, count active directories, `AGENT.md` cards, `SKILL.md` bundles, and `specs/`, and update `DIRECTORY.md` and `ARCHITECTURE.md` deterministically.
- **Acceptance Criteria:**
  - Running `python "00_global_system/scripts/doc_guardian.py"` completes in under 2 seconds with zero errors and outputs an accurate `DIRECTORY.md` table.

#### 2. Technical Plan (`plan.md`)

- **Language & Runtime:** Python 3.11+ standard library (`pathlib`, `datetime`, `json`, `shutil`).
- **Key Artifacts:**
  - `D:\AI_Workspace\Jarvis V1\README.md`
  - `D:\AI_Workspace\Jarvis V1\ARCHITECTURE.md`
  - `D:\AI_Workspace\Jarvis V1\PROJECT_GENESIS_AND_DISCUSSIONS_DRAFT.md`
  - `D:\AI_Workspace\Jarvis V1\CLAUDE.md`
  - `D:\AI_Workspace\Jarvis V1\00_global_system\directives\{Ziad_Cognitive_DNA.md,Global_Governance_Rules.md,Detachability_Standard.md}`
  - `D:\AI_Workspace\Jarvis V1\00_global_system\scripts\doc_guardian.py`

#### 3. Execution Tasks (`tasks.md`)

- [ ] **T001:** Scaffold the root and all 7 top-level directory trees in `D:\AI_Workspace\Jarvis V1`.
- [ ] **T002 [P]:** Generate `README.md`, `CLAUDE.md`, and `PROJECT_GENESIS_AND_DISCUSSIONS_DRAFT.md`.
- [ ] **T003 [P]:** Generate `00_global_system/directives/Ziad_Cognitive_DNA.md`, `Global_Governance_Rules.md`, and `Detachability_Standard.md`.
- [ ] **T004:** Generate `ARCHITECTURE.md` with full macro-to-micro documentation and auto-sync markers.
- [ ] **T005:** Implement `00_global_system/scripts/doc_guardian.py` and run initial synchronization.

---

### PHASE 1: Deterministic Memory Layer, Write-Ahead Queue & Semantic ID Bridge

- **Spec Kit Feature Directory:** `specs/002-phase1-memory-layer-and-wal-queue`

#### 1. Specification (`spec.md`)

- **Objective:** Build the deterministic Python MCP Memory Server, the SQLite Write-Ahead Queue (`wal_queue.db`), the declarative `memory_schema.yaml`, the bidirectional Semantic ID generator linking `Obsidian` and `AppFlowy`/SQLite, and the human-gated `memory_watchdog_agent.py`.
- **Functional Requirements:**
  - `FR-1.1 (Zero-Loss Queue)`: Every incoming request is logged immediately to `00_global_system/queue_vault/wal_queue.db` with status `PENDING` before tool execution.
  - `FR-1.2 (Semantic IDs)`: Generate thread-safe atomic IDs (`JAR-2026-0001`, `MED-2026-0001`, `TRV-2026-0001`, `HLT-2026-0001`, `SPR-2026-0001`, `CLN-2026-0001`, `BRD-2026-0001`, `FIN-2026-0001`) with bidirectional `obsidian://open?vault=...` URIs.
  - `FR-1.3 (5 Universal MCP Tools)`: Expose `save_entity`, `query_memory`, `update_state`, `link_entities`, and `check_health` driven by `memory_schema.yaml`.
  - `FR-1.4 (Strict Tenant Isolation)`: Reject any cross-tenant write/read attempt where `caller_pod != target_pod` unless explicitly targeting `00_global_system` or `30_infrastructure/the_cafe`.
  - `FR-1.5 (Human-Gated Watchdog)`: `memory_watchdog_agent.py` replays stalled queue items, normalizes ISO dates, and writes schema modification proposals to `review_queue_approvals.md`.

#### 2. Technical Plan (`plan.md`)

- **Database Engine:** SQLite3 in `WAL` (Write-Ahead Logging) mode (`00_global_system/queue_vault/wal_queue.db`).
- **Modules:**
  - `00_global_system/queue_vault/wal_queue_manager.py`
  - `00_global_system/memory_layer/semantic_id_generator.py`
  - `00_global_system/memory_layer/memory_schema.yaml`
  - `00_global_system/memory_layer/mcp_memory_server.py`
  - `00_global_system/memory_layer/memory_watchdog_agent.py`

#### 3. Execution Tasks (`tasks.md`)

- [ ] **T101:** Implement `wal_queue_manager.py` with SQLite WAL mode, status transitions (`PENDING -> PROCESSING -> COMPLETED / FAILED`), and retry counters.
- [ ] **T102:** Implement `semantic_id_generator.py` with atomic counter persistence and Obsidian/AppFlowy URI builders.
- [ ] **T103:** Author declarative `memory_schema.yaml` mapping entity types (`idea_note`, `clinical_case`, `task_item`, `sop_playbook`, `crm_lead`, `decision_record`) to target pod folders.
- [ ] **T104:** Implement `mcp_memory_server.py` providing the 5 universal functions and cross-pod isolation assertions.
- [ ] **T105:** Implement `memory_watchdog_agent.py` and verify queue replay and schema proposal staging.

---

### PHASE 2: Quad-Shield Master Task Engine, Guardrail Hooks & Federated Rollup

- **Spec Kit Feature Directory:** `specs/003-phase2-master-task-engine-and-federation`

#### 1. Specification (`spec.md`)

- **Objective:** Build the hybrid Task Management Engine combining **Eisenhower Matrix + Deterministic WSJF Scoring + Kanban WIP Limits + 85% Confidence Gate + Reversibility Gate**, operating locally inside every pod and syncing summaries up to `MASTER_BOARD.md`.
- **Functional Requirements:**
  - `FR-2.1 (WSJF Formula)`: Compute `WSJF = round((value + urgency + risk_reduction) / max(effort, 1), 2)` in pure Python (`eisenhower_wsjf_wip_engine.py`).
  - `FR-2.2 (WIP Limits)`: Enforce max 3 `IN_PROGRESS` tasks per team and max 3 heavy daily tasks on Ziad's personal action sheet.
  - `FR-2.3 (85% Confidence Gate)`: `pre_task_confidence_gate.py` blocks execution if `clarity_score < 0.85` or required parameters are missing, switching task status to `DISCUSS_FIRST`.
  - `FR-2.4 (Reversibility Gate)`: `pre_write_reversibility_gate.py` routes any action with `is_reversible == False` to `review_queue_approvals.md` awaiting Ziad's 5-button decision + mandatory comment.
  - `FR-2.5 (Federated Rollup)`: `federation_rollup_sync.py` aggregates each pod's `public_telemetry_rollup.json` into `00_global_system/master_task_engine/MASTER_BOARD.md`.

#### 2. Technical Plan (`plan.md`)

- **Modules:**
  - `00_global_system/master_task_engine/task_engine_config.yaml`
  - `00_global_system/master_task_engine/eisenhower_wsjf_wip_engine.py`
  - `00_global_system/hooks_and_guardrails/pre_task_confidence_gate.py`
  - `00_global_system/hooks_and_guardrails/pre_write_reversibility_gate.py`
  - `00_global_system/master_task_engine/federation_rollup_sync.py`

#### 3. Execution Tasks (`tasks.md`)

- [ ] **T201:** Create `task_engine_config.yaml` defining Eisenhower thresholds, WIP caps, and SLA deadlines.
- [ ] **T202:** Implement `eisenhower_wsjf_wip_engine.py` for local pod boards and the global board.
- [ ] **T203 [P]:** Implement `pre_task_confidence_gate.py` and `pre_write_reversibility_gate.py`.
- [ ] **T204:** Implement `federation_rollup_sync.py` to update `MASTER_BOARD.md`, `review_queue_approvals.md`, and `global_blockers_radar`.

---

### PHASE 3: Agent Registry, Gamified 100-Point Scorecards, Cloning Templates & Self-Evolution Loop

- **Spec Kit Feature Directory:** `specs/004-phase3-agent-registry-templates-learning`

#### 1. Specification (`spec.md`)

- **Objective:** Build the Central HR Agent Registry, the Gamified 100-Point Scorecard Engine, the Self-Evolution Pipeline (`Comment-to-Rule` & `Scratchpad-to-Skill`), and the Master Cloning Templates in `01_templates/`.
- **Functional Requirements:**
  - `FR-3.1 (Gamified Scoring)`: `scorecard_engine.py` updates agent, team, and pod scores (`+5` first-pass approval, `-3` edit/cancel, `+10` verified SOP created, `+5` Café synergy, `-5` SLA delay) and writes `scorecards_leaderboard.md`.
  - `FR-3.2 (Self-Evolution Loop)`: `skill_evolver_pipeline.py` ingests Ziad's mandatory dashboard comments and `sessions_traces/` logs to stage proposed `SKILL.md` files in `proposed_skills/` and rule updates in `feedback_patches/`.
  - `FR-3.3 (Master Templates & Cloner)`: Populate `01_templates/` and build `00_global_system/scripts/clone_pod.py` to instantiate any new business or pillar pod in one command.

#### 2. Technical Plan (`plan.md`)

- **Modules:**
  - `01_templates/{standalone_business_pod_template,standalone_pillar_pod_template,department_module_template,think_and_know_team_template,agent_card_template,skill_bundle_template}`
  - `00_global_system/agent_registry/scorecard_engine.py`
  - `00_global_system/learning_loop/skill_evolver_pipeline.py`
  - `00_global_system/scripts/clone_pod.py`

#### 3. Execution Tasks (`tasks.md`)

- [ ] **T301 [P]:** Populate all 6 master templates inside `01_templates/`.
- [ ] **T302:** Implement `scorecard_engine.py` and initialize `scorecards_leaderboard.md`.
- [ ] **T303:** Implement `skill_evolver_pipeline.py` for comment-driven rule patching and SOP extraction.
- [ ] **T304 [P]:** Author the 3 universal skill bundles in `00_global_system/skills/` (`deep_web_research`, `voice_and_media_ingestor`, `sop_playbook_distiller`).
- [ ] **T305:** Implement `clone_pod.py` and test cloning a sandbox pod.

---

### PHASE 4: Supreme Command (`JARVIS Prime`), Global C-Suite, Event-Driven Café & Channels

- **Spec Kit Feature Directory:** `specs/005-phase4-executive-command-cafe-channels`

#### 1. Specification (`spec.md`)

- **Objective:** Configure `30_infrastructure/` including `JARVIS Prime` (with graduated `autonomy_matrix.yaml`), the 5 Layer-2 Executive Command officers, the Event-Driven Café (`the_cafe/`), the Telegram 1-on-1 Hotline, and the Private Discord Roundtable War Rooms.
- **Functional Requirements:**
  - `FR-4.1 (JARVIS Prime & Autonomy Matrix)`: Route quick notes via 1-hop Fast-Path to the Memory Layer and complex initiatives via Deep-Path to C-Suite executives; enforce `autonomy_matrix.yaml` (`Wait for Approval` -> `Execute & Notify` -> `Full Autonomous after 10 consecutive approvals`).
  - `FR-4.2 (Event-Driven Café)`: `cafe_protocol_and_moderator.py` processes `Eureka Broadcasts`, `CKO Cross-Pollination Proposals`, and `Peer Consultations` after passing payloads through `cafe_privacy_sanitizer.py`.
  - `FR-4.3 (Telegram & Private Discord Bridges)`: `telegram_gateway.py` connects Ziad 1-on-1 with `JARVIS Prime`; `roundtable_moderator.py` enforces structured turn-taking (`Discuss`, `Research`, `Plan`, `Learn`) in private Discord channels with zero infinite bot-to-bot loops.

#### 2. Technical Plan (`plan.md`)

- **Modules:**
  - `30_infrastructure/executive_command/jarvis_prime/{AGENT.md,autonomy_matrix.yaml,intent_router.py}`
  - `30_infrastructure/the_cafe/cafe_protocol_and_moderator.py`
  - `00_global_system/hooks_and_guardrails/cafe_privacy_sanitizer.py`
  - `30_infrastructure/channels_bridge/telegram_hotline/telegram_gateway.py`
  - `30_infrastructure/channels_bridge/discord_war_rooms/roundtable_moderator.py`
  - `30_infrastructure/channels_bridge/cron_autonomous_scheduler/scheduler_daemon.py`

#### 3. Execution Tasks (`tasks.md`)

- [ ] **T401:** Configure `AGENT.md` cards for `JARVIS Prime` and all 5 Layer-2 Executive Command officers, plus `autonomy_matrix.yaml`.
- [ ] **T402:** Implement `intent_router.py` supporting Fast-Path note capture and Deep-Path delegation.
- [ ] **T403 [P]:** Implement `cafe_privacy_sanitizer.py` and `cafe_protocol_and_moderator.py`.
- [ ] **T404 [P]:** Implement `telegram_gateway.py`, `roundtable_moderator.py`, and `scheduler_daemon.py`.

---

### PHASE 5: Golden Standalone Business Pod (`Medicophilia`) & Cloning `Travelophilia`

- **Spec Kit Feature Directory:** `specs/006-phase5-golden-business-pod-medicophilia`

#### 1. Specification (`spec.md`)

- **Objective:** Build `20_businesses/medicophilia` as the complete Golden Business Pod with its `_pod_core/` (local task board, website/CMS/CRM gateway, `human_rbac_permissions.yaml`), 6-member C-Suite Cabinet, 7 functional departments, and 44 hyper-specialized workers, then clone and customize `20_businesses/travelophilia`.
- **Functional Requirements:**
  - `FR-5.1`: Populate all 6 outer-shell power files (`BUSINESS.md`, `DNA_AND_VOICE.md`, `STATE.md`, `DECISION_LOG.md`, `distilled_context.md`, `triggers_and_watchers.yaml`) and `identifiers/{public_id.yaml,private_id.yaml}`.
  - `FR-5.2`: Configure `_pod_core/web_and_human_gateway/website_cms_crm_connector.py` and `human_rbac_permissions.yaml` so human staff can collaborate strictly inside the venture pod.
  - `FR-5.3`: Author complete `AGENT.md` cards for all 6 C-Suite executives, 11 Department Managers, and 44 specialized workers in `medicophilia`, then clone and customize `travelophilia`.

#### 2. Execution Tasks (`tasks.md`)

- [ ] **T501:** Configure `_pod_core/` and the 6 outer-shell power files inside `20_businesses/medicophilia`.
- [ ] **T502:** Populate all C-Suite, Manager, and Worker `AGENT.md` profiles and department `DEPARTMENT.md` charters for `medicophilia`.
- [ ] **T503:** Implement `website_cms_crm_connector.py` and `human_rbac_permissions.yaml`.
- [ ] **T504:** Clone `medicophilia` to `20_businesses/travelophilia` and customize all travel, B2B DMC, student transport, and Erasmus worker directives.

---

### PHASE 6: Golden Standalone Life Pillar Pod (`01_health_and_growth`) & All 5 Life Pillars

- **Spec Kit Feature Directory:** `specs/007-phase6-golden-pillar-pod-health-life-os`

#### 1. Specification (`spec.md`)

- **Objective:** Build `10_pillars/01_health_and_growth` combining the 4 Capabilities (`Learn, Execute, Delegate, Monitor`) with `PARA + GTD + Quantified Self Metrics + 12-Week Sprints`, then instantiate and customize `02_spiritual`, `03_clinical_and_learning`, `04_personal_branding` (with `ZiadAlhalwany.com` connector), and `05_personal_finance`.

#### 2. Execution Tasks (`tasks.md`)

- [ ] **T601:** Configure `10_pillars/01_health_and_growth` outer shell, `_pod_core/`, 4 Capability Managers, and 12 specialized worker `AGENT.md` cards.
- [ ] **T602 [P]:** Configure `10_pillars/02_spiritual` (8 workers with strict verified Sharia source rules) and `10_pillars/03_clinical_and_learning` (10 workers with hospital clinical case logging schemas).
- [ ] **T603 [P]:** Configure `10_pillars/04_personal_branding` (12 workers + `personal_website_portfolio_publisher` + Trojan-Horse funnels) and `10_pillars/05_personal_finance` (6 workers with maximum security lock).

---

### PHASE 7: Visual Command Dashboard (`90_dashboard`) & Runtime Wiring

- **Spec Kit Feature Directory:** `specs/008-phase7-command-dashboard-runtime-wiring`

#### 1. Specification (`spec.md`)

- **Objective:** Build Ziad's Visual Command Center (`90_dashboard/dashboard_server.py` and `OVERVIEW.md`) featuring the **5-Button Interactive Action Center (`Approve`, `Cancel`, `Edit`, `Explain & Discuss First` + Mandatory Comment)**, Ziad's Daily Focus Sheet, Live Org Graph & Scorecards, Global Blockers Radar, and root `.mcp.json` runtime wiring for Claude Code / Cowork and Hermes Agent.

#### 2. Execution Tasks (`tasks.md`)

- [ ] **T701:** Implement `90_dashboard/dashboard_server.py` (FastAPI local web dashboard reading live markdown/SQLite state).
- [ ] **T702:** Wire the 5-Button Decision API endpoint to automatically trigger `scorecard_engine.py` and `skill_evolver_pipeline.py` upon comment submission.
- [ ] **T703:** Create `D:\AI_Workspace\Jarvis V1\.mcp.json` mounting `mcp_memory_server.py` for Claude Code / Cowork and Hermes Agent.
- [ ] **T704:** Execute full end-to-end integration test across all 8 phases and run `doc_guardian.py`.
