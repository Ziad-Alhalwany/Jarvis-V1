#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT J.A.R.V.I.S. V1 — SPEC KIT & FEDERATED WORKSPACE SCAFFOLDER
Target Root: D:\\AI_Workspace\\Jarvis V1
"""

import json
import sys
from pathlib import Path
from datetime import datetime

ROOT = Path(r"D:\AI_Workspace\Jarvis V1")

# 1. Core Directories
CORE_DIRS = [
    ".specify/memory",
    "00_global_system/directives",
    "00_global_system/memory_layer",
    "00_global_system/queue_vault/staging_media_inbox",
    "00_global_system/master_task_engine",
    "00_global_system/agent_registry/cards",
    "00_global_system/learning_loop/proposed_skills",
    "00_global_system/learning_loop/feedback_patches",
    "00_global_system/learning_loop/extracted_sops",
    "00_global_system/mcp_servers",
    "00_global_system/plugins_and_integrations",
    "00_global_system/hooks_and_guardrails",
    "00_global_system/skills/deep_web_research/scripts",
    "00_global_system/skills/voice_and_media_ingestor/scripts",
    "00_global_system/skills/sop_playbook_distiller/scripts",
    "00_global_system/reference_library",
    "00_global_system/scripts",
    "01_templates/standalone_business_pod_template",
    "01_templates/standalone_pillar_pod_template",
    "01_templates/department_module_template/manager",
    "01_templates/department_module_template/workers",
    "01_templates/department_module_template/playbooks_and_sops",
    "01_templates/department_module_template/active_tasks",
    "01_templates/think_and_know_team_template",
    "01_templates/agent_card_template",
    "01_templates/skill_bundle_template/scripts",
    "01_templates/skill_bundle_template/templates",
    "01_templates/skill_bundle_template/references",
    "30_infrastructure/executive_command/jarvis_prime",
    "30_infrastructure/executive_command/global_chief_of_staff",
    "30_infrastructure/executive_command/global_ops_prioritizer",
    "30_infrastructure/executive_command/global_memory_curator",
    "30_infrastructure/executive_command/global_knowledge_officer",
    "30_infrastructure/executive_command/personal_chief_of_staff",
    "30_infrastructure/the_cafe/eureka_broadcasts",
    "30_infrastructure/the_cafe/cross_pollination_proposals",
    "30_infrastructure/the_cafe/peer_consultations",
    "30_infrastructure/channels_bridge/telegram_hotline",
    "30_infrastructure/channels_bridge/discord_war_rooms",
    "30_infrastructure/channels_bridge/cron_autonomous_scheduler",
    "30_infrastructure/brain_bindings/obsidian_config",
    "30_infrastructure/brain_bindings/appflowy_config",
    "90_dashboard/action_center_5_buttons",
    "90_dashboard/ziad_daily_focus_sheet",
    "90_dashboard/live_org_graph_and_scorecards",
    "90_dashboard/global_blockers_radar",
    "99_archive/cold_storage",
]

BUSINESS_SUBDIRS = [
    "identifiers",
    "_pod_core/local_task_engine",
    "_pod_core/web_and_human_gateway",
    "_pod_core/local_mcp_and_plugins",
    "_pod_core/local_hooks",
    "_pod_core/_governance_and_registry",
    "00_c_suite_leadership/venture_ceo",
    "00_c_suite_leadership/venture_cto_cpo",
    "00_c_suite_leadership/venture_cmo_cro",
    "00_c_suite_leadership/venture_coo",
    "00_c_suite_leadership/venture_cfo_clo",
    "00_c_suite_leadership/venture_cko",
    "00_c_suite_leadership/strategy_and_okrs",
    "01_intelligence_and_rnd/think_and_know_team/manager",
    "01_intelligence_and_rnd/think_and_know_team/workers/market_competitor_intel",
    "01_intelligence_and_rnd/think_and_know_team/workers/deep_reader_transcriber",
    "01_intelligence_and_rnd/think_and_know_team/workers/executive_summarizer",
    "01_intelligence_and_rnd/think_and_know_team/workers/devils_advocate_critic",
    "01_intelligence_and_rnd/think_and_know_team/workers/customer_psychologist",
    "01_intelligence_and_rnd/think_and_know_team/workers/obsidian_skill_linker",
    "01_intelligence_and_rnd/reference_library",
    "01_intelligence_and_rnd/company_knowledge",
    "02_product_and_engineering/platform_engineering_manager",
    "02_product_and_engineering/automation_and_site_ai_lead",
    "02_product_and_engineering/qa_and_security_lead",
    "02_product_and_engineering/workers/frontend_ui_ux_builder",
    "02_product_and_engineering/workers/backend_api_architect",
    "02_product_and_engineering/workers/database_schema_engineer",
    "02_product_and_engineering/workers/cms_website_publisher",
    "02_product_and_engineering/workers/webhook_mcp_integrator",
    "02_product_and_engineering/workers/site_chatbot_operator",
    "02_product_and_engineering/workers/web_scraper_pipeline",
    "02_product_and_engineering/workers/automated_test_hunter",
    "02_product_and_engineering/workers/security_privacy_auditor",
    "02_product_and_engineering/playbooks_and_sops",
    "02_product_and_engineering/active_tasks",
    "03_marketing_and_growth/content_factory_manager",
    "03_marketing_and_growth/seo_and_community_manager",
    "03_marketing_and_growth/performance_ads_lead",
    "03_marketing_and_growth/workers/short_form_reels_writer",
    "03_marketing_and_growth/workers/carousel_thread_architect",
    "03_marketing_and_growth/workers/long_form_blog_writer",
    "03_marketing_and_growth/workers/visual_prompt_art_director",
    "03_marketing_and_growth/workers/trojan_horse_funnel_integrator",
    "03_marketing_and_growth/workers/technical_seo_worker",
    "03_marketing_and_growth/workers/social_scheduler",
    "03_marketing_and_growth/workers/community_responder",
    "03_marketing_and_growth/workers/ad_creative_tester",
    "03_marketing_and_growth/workers/cro_landing_optimizer",
    "03_marketing_and_growth/workers/cac_ltv_analyst",
    "03_marketing_and_growth/playbooks_and_sops",
    "03_marketing_and_growth/active_tasks",
    "04_sales_and_crm/manager",
    "04_sales_and_crm/workers/inbound_lead_qualifier",
    "04_sales_and_crm/workers/b2b_outbound_prospector",
    "04_sales_and_crm/workers/proposal_pitch_builder",
    "04_sales_and_crm/workers/objection_closing_coach",
    "04_sales_and_crm/workers/crm_pipeline_tracker",
    "04_sales_and_crm/playbooks_and_sops",
    "04_sales_and_crm/active_tasks",
    "05_supply_partnerships_and_fulfillment/supply_partnerships_manager",
    "05_supply_partnerships_and_fulfillment/customer_success_manager",
    "05_supply_partnerships_and_fulfillment/workers/partner_vetting_sourcing",
    "05_supply_partnerships_and_fulfillment/workers/grant_and_opportunity_scout",
    "05_supply_partnerships_and_fulfillment/workers/package_itinerary_architect",
    "05_supply_partnerships_and_fulfillment/workers/client_onboarding_concierge",
    "05_supply_partnerships_and_fulfillment/workers/issue_support_resolver",
    "05_supply_partnerships_and_fulfillment/workers/review_referral_collector",
    "05_supply_partnerships_and_fulfillment/playbooks_and_sops",
    "05_supply_partnerships_and_fulfillment/active_tasks",
    "06_operations_task_tracking_and_admin/manager",
    "06_operations_task_tracking_and_admin/workers/local_task_wsjf_coordinator",
    "06_operations_task_tracking_and_admin/workers/sop_playbook_writer",
    "06_operations_task_tracking_and_admin/workers/sprint_blocker_watchdog",
    "06_operations_task_tracking_and_admin/workers/human_coworker_liaison",
    "06_operations_task_tracking_and_admin/playbooks_and_sops",
    "06_operations_task_tracking_and_admin/active_tasks",
    "07_finance_and_legal/manager",
    "07_finance_and_legal/workers/bookkeeping_invoice_tracker",
    "07_finance_and_legal/workers/unit_economics_pricer",
    "07_finance_and_legal/workers/international_corp_tax_researcher",
    "07_finance_and_legal/playbooks_and_sops",
    "07_finance_and_legal/active_tasks",
    "swipe_files_and_benchmarks",
    "skills",
    "sessions_traces",
    "reports_deliverables",
]

PILLAR_WORKERS = {
    "01_health_and_growth": {
        "01_think_and_learn": ["nutrition_and_bio_researcher", "fitness_performance_researcher", "sleep_neuro_recovery_researcher", "behavioral_habit_psychologist"],
        "02_execute_and_build": ["workout_recovery_planner", "meal_and_macro_architect", "style_wardrobe_advisor", "presence_and_communication_coach"],
        "03_delegate_and_automate": ["clinic_and_gym_booker", "personal_procurement_worker"],
        "04_monitor_and_metrics": ["biometrics_and_habit_tracker", "fitness_event_and_opportunity_scout"],
    },
    "02_spiritual": {
        "01_think_and_learn": ["quran_tafsir_verifier", "hadith_and_fiqh_verifier", "tazkiyah_insights_synthesizer"],
        "02_execute_and_build": ["wards_and_khatmah_planner", "seasonal_worship_architect"],
        "03_delegate_and_automate": ["charity_and_sadaqah_automator"],
        "04_monitor_and_metrics": ["prayer_and_ward_consistency_tracker", "spiritual_reflection_logger"],
    },
    "03_clinical_and_learning": {
        "01_think_and_learn": ["hospital_clinical_case_logger", "differential_diagnosis_analyst", "pubmed_guidelines_researcher", "polymath_cross_domain_researcher"],
        "02_execute_and_build": ["medical_board_case_simulator", "spaced_repetition_study_planner", "book_and_lecture_distiller"],
        "03_delegate_and_automate": ["cme_and_medical_portfolio_organizer"],
        "04_monitor_and_metrics": ["clinical_procedure_logbook_tracker", "medical_fellowship_and_grant_scout"],
    },
    "04_personal_branding": {
        "01_think_and_learn": ["viral_trend_deconstructor", "audience_psychology_researcher"],
        "02_execute_and_build": ["short_form_reels_hook_writer", "carousel_and_thread_writer", "long_form_article_writer", "photorealistic_prompt_art_director", "trojan_horse_funnel_architect"],
        "03_delegate_and_automate": ["personal_website_portfolio_publisher", "multi_platform_social_scheduler"],
        "04_monitor_and_metrics": ["brand_growth_analytics_tracker", "pr_podcast_and_media_scout", "vip_networking_crm_worker"],
    },
    "05_personal_finance": {
        "01_think_and_learn": ["sharia_compliant_wealth_researcher"],
        "02_execute_and_build": ["personal_budget_and_asset_planner", "emergency_fund_and_goal_modeler"],
        "03_delegate_and_automate": ["subscriptions_and_bills_coordinator", "official_documents_vault_keeper"],
        "04_monitor_and_metrics": ["net_worth_and_expense_anomaly_tracker"],
    },
}

SPECS = [
    ("001-phase0-foundation-and-docs", "Phase 0: Foundation, Federated Directory Skeleton & Living Documentation"),
    ("002-phase1-memory-layer-and-wal-queue", "Phase 1: Deterministic Memory Layer, SQLite WAL Queue & Semantic ID Bridge"),
    ("003-phase2-master-task-engine-and-federation", "Phase 2: Quad-Shield Master Task Engine, Guardrail Hooks & Federated Rollup"),
    ("004-phase3-agent-registry-templates-learning", "Phase 3: Agent Registry, Gamified 100-Point Scorecards, Templates & Learning Loop"),
    ("005-phase4-executive-command-cafe-channels", "Phase 4: Supreme Command (JARVIS Prime), Global C-Suite, Event-Driven Cafe & Channels"),
    ("006-phase5-golden-business-pod-medicophilia", "Phase 5: Golden Standalone Business Pod (Medicophilia) & Travelophilia Clone"),
    ("007-phase6-golden-pillar-pod-health-life-os", "Phase 6: Golden Standalone Life Pillar Pod (Health) & All 5 Personal Life Pillars"),
    ("008-phase7-command-dashboard-runtime-wiring", "Phase 7: Visual Command Dashboard (90_dashboard) & Runtime Wiring"),
]


def ensure_agent_card(folder: Path):
    card = folder / "AGENT.md"
    if not card.exists():
        rel = folder.relative_to(ROOT)
        card.write_text(
            f"# Digital Employee Profile: {folder.name}\n"
            f"- **Role ID:** `{folder.name}`\n"
            f"- **Workspace Path:** `{rel}`\n"
            f"- **Clarity Gate:** `>= 85%` (Halt in Explain & Discuss mode if below threshold)\n"
            f"- **Scorecard Baseline:** `100 pts`\n",
            encoding="utf-8",
        )


def populate_pod_shell(pod_dir: Path, name: str, is_biz: bool):
    main_doc = "BUSINESS.md" if is_biz else "PILLAR.md"
    shell_files = {
        main_doc: f"# {name.upper()} — Master Charter & Boundaries\n",
        "DNA_AND_VOICE.md": f"# {name.upper()} — Voice, Persona & Zero-AI-Fluff Rules\n",
        "STATE.md": f"# {name.upper()} — Live Telemetry & Sprint State\n- **Score:** 100/100\n",
        "DECISION_LOG.md": f"# {name.upper()} — Historical Decision & Rejection Log\n",
        "distilled_context.md": f"# {name.upper()} — 2-Page Distilled Context Summary\n",
        "triggers_and_watchers.yaml": "schedules:\n  morning_sync: '07:00'\n  nightly_distill: '22:00'\n",
        "identifiers/public_id.yaml": f"pod_id: {name}\nshareable_hooks: []\n",
        "identifiers/private_id.yaml": f"pod_id: {name}\nstrict_isolation: true\n",
        "_pod_core/local_task_engine/LOCAL_BOARD.md": f"# {name.upper()} — Local Pod Task Board\n",
        "_pod_core/local_task_engine/public_telemetry_rollup.json": json.dumps(
            {"pod": name, "completion_pct": 100, "active_wip": 0, "blockers": [], "pending_approvals": 0}, indent=2
        ),
    }
    for rel, text in shell_files.items():
        fp = pod_dir / rel
        fp.parent.mkdir(parents=True, exist_ok=True)
        if not fp.exists():
            fp.write_text(text, encoding="utf-8")


def main():
    ROOT.mkdir(parents=True, exist_ok=True)

    for d in CORE_DIRS:
        p = ROOT / d
        p.mkdir(parents=True, exist_ok=True)
        if "executive_command" in p.parts and p.name != "executive_command":
            ensure_agent_card(p)

    for biz in ["medicophilia", "travelophilia"]:
        b_root = ROOT / "20_businesses" / biz
        for sub in BUSINESS_SUBDIRS:
            p = b_root / sub
            p.mkdir(parents=True, exist_ok=True)
            if (
                ("00_c_suite_leadership" in p.parts and p.name not in {"00_c_suite_leadership", "strategy_and_okrs"})
                or p.name.endswith("_manager")
                or p.name.endswith("_lead")
                or p.name == "manager"
                or ("workers" in p.parts and p.name != "workers")
            ):
                ensure_agent_card(p)
        populate_pod_shell(b_root, biz, is_biz=True)

    for pillar, caps in PILLAR_WORKERS.items():
        p_root = ROOT / "10_pillars" / pillar
        for sub in [
            "identifiers",
            "_pod_core/local_task_engine",
            "_pod_core/local_mcp_and_plugins",
            "_pod_core/local_hooks",
            "_pod_core/_governance_and_registry",
            "00_pillar_lead",
            "01_think_and_learn/manager",
            "01_think_and_learn/reference_library",
            "01_think_and_learn/knowledge_vault",
            "02_execute_and_build/manager",
            "02_execute_and_build/active_projects",
            "02_execute_and_build/areas_and_sops",
            "03_delegate_and_automate/manager",
            "04_monitor_and_metrics/manager",
            "04_monitor_and_metrics/metrics_and_logs",
            "swipe_files_and_benchmarks",
            "skills",
            "sessions_traces",
            "reports_deliverables",
        ]:
            d = p_root / sub
            d.mkdir(parents=True, exist_ok=True)
            if d.name in {"00_pillar_lead", "manager"}:
                ensure_agent_card(d)
        for cap_dir, workers in caps.items():
            for w in workers:
                w_path = p_root / cap_dir / "workers" / w
                w_path.mkdir(parents=True, exist_ok=True)
                ensure_agent_card(w_path)
        populate_pod_shell(p_root, pillar, is_biz=False)

    for slug, title in SPECS:
        s_dir = ROOT / "specs" / slug
        s_dir.mkdir(parents=True, exist_ok=True)
        for fname in ["spec.md", "plan.md", "tasks.md"]:
            fpath = s_dir / fname
            if not fpath.exists():
                fpath.write_text(f"# {title} — {fname}\n\nWorkspace: `D:\\AI_Workspace\\Jarvis V1`\n", encoding="utf-8")

    cards = sorted(ROOT.rglob("AGENT.md"))
    dir_md = ROOT / "00_global_system" / "agent_registry" / "DIRECTORY.md"
    lines = [
        "# J.A.R.V.I.S. V1 — Central Digital Employee Registry",
        f"**Synchronized:** `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`",
        f"**Total Registered Digital Employees (`AGENT.md`):** `{len(cards)}`",
        "",
        "| # | Role Identifier | Relative Path |",
        "| :--- | :--- | :--- |",
    ]
    for i, c in enumerate(cards, 1):
        lines.append(f"| `{i:03d}` | **{c.parent.name}** | `{c.relative_to(ROOT)}` |")
    dir_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[SUCCESS] Initialized D:\\AI_Workspace\\Jarvis V1 with {len(cards)} agent cards and 8 Spec Kit phases.")


if __name__ == "__main__":
    main()