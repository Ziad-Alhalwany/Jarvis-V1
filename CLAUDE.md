# CLAUDE.md — Universal AI Runtime Entry Hook & Operating Directives

**Workspace Root:** `D:\AI_Workspace\Jarvis V1`  
**Supreme Commander:** Dr. Ziad Mohamed Alhalwany  
**Governing Law:** `.specify/memory/constitution.md` (v1.0.0)

This file is automatically loaded by Claude Code, Claude Cowork, OpenAI Codex, Hermes Agent, and compatible MCP/CLI runtimes upon entering `D:\AI_Workspace\Jarvis V1`. You MUST obey these directives on every turn.

---

## 1. Constitutional Supremacy & Mandatory Boot Sequence

1. **Read Order on Boot:**
   - First, enforce `.specify/memory/constitution.md` (Principles I through VIII).
   - Second, when operating inside any Business Pod (`20_businesses/<pod>/`) or Life Pillar Pod (`10_pillars/<pod>/`), read **only** that pod's `distilled_context.md` (max 2 pages), `STATE.md`, and `DECISION_LOG.md` first.
   - **Prohibition:** NEVER load the entire `reference_library/` or `knowledge_vault/` on boot. Use **Progressive Disclosure**—load specific files or local `skills/` only when required by the active task.
2. **Consult `DECISION_LOG.md` Before Proposing:** Never pitch an idea, tool, or strategy that has already been rejected in `DECISION_LOG.md`.

---

## 2. Strict Tenant Isolation & Security Boundaries

1. **Zero Cross-Pod Leakage:**
   - When operating in `20_businesses/medicophilia`, you MUST NOT read, import, or write files inside `20_businesses/travelophilia` or `10_pillars/*` (and vice versa).
   - All storage operations MUST pass through `00_global_system/memory_layer/mcp_memory_server.py` (`save_entity`, `query_memory`, `update_state`, `link_entities`, `check_health`).
2. **Private Identifier Lock (`private_id.yaml`):**
   - Never expose contents of `identifiers/private_id.yaml` or `.env` in reports, marketing copy, telemetry rollups, or `30_infrastructure/the_cafe/` broadcasts.
3. **Human Collaborator Scope:**
   - If invoked by a non-Commander human user, enforce `_pod_core/web_and_human_gateway/human_rbac_permissions.yaml` strictly.

---

## 3. Execution Guardrails (Confidence Gate, Reversibility Gate & Zero-Placeholder Code)

1. **The 85% Confidence Gate:**
   - Before executing any multi-step task, evaluate whether the requirements, target paths, and constraints are at least `85%` clear.
   - If clarity is `< 85%`, **DO NOT GUESS OR HALLUCINATE**. Halt execution, set status to `DISCUSS_FIRST`, and ask Dr. Ziad concise, high-signal clarifying questions.
2. **The Reversibility Gate (Human-in-the-Loop):**
   - Any irreversible action (`is_reversible: false`: spending money, publishing live to a website/social platform, sending external emails, deleting records, or altering `memory_schema.yaml` semantics) MUST be staged in `00_global_system/master_task_engine/review_queue_approvals.md` for Dr. Ziad's 5-Button Decision (`Approve`, `Cancel`, `Edit`, `Explain & Discuss First` + Mandatory Comment).
3. **Deterministic First & Zero Placeholders:**
   - Never use an LLM call to do math, WSJF sorting, ID generation, or file counting—run the deterministic Python engines (`eisenhower_wsjf_wip_engine.py`, `semantic_id_generator.py`, `scorecard_engine.py`, `doc_guardian.py`).
   - Never write placeholder code (`# TODO`, `pass`, `...`). Every script must be production-ready Python 3.11+ with type hints, structured logging, and error handling.
4. **Living Documentation Synchronization:**
   - Whenever you add, move, or remove a directory, `AGENT.md` card, `SKILL.md` bundle, or spec file, you MUST run:
     ```powershell
     python "D:\AI_Workspace\Jarvis V1\00_global_system\scripts\doc_guardian.py"
     ```
