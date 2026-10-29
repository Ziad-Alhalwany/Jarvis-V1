# J.A.R.V.I.S. V1 — Federated Micro-OS Pod & Detachability Standard (`Detachability_Standard.md`)

**Governing Law:** `.specify/memory/constitution.md` (Principles II, III, VIII)

---

## 1. Purpose of the Detachability Standard

Every commercial venture in `20_businesses/` (`medicophilia`, `travelophilia`, and future ventures) and every personal life pillar in `10_pillars/` MUST be engineered as a **Standalone Micro-OS Pod**.

This standard guarantees three capabilities at all times:

1. **Zero-Breakage Spin-Off:** Any business pod folder can be copied out of `D:\AI_Workspace\Jarvis V1` onto an independent cloud VPS or dedicated company machine and operate at 100% capacity immediately.
2. **Safe Human Collaboration (`Human RBAC`):** Human employees, co-founders, or contractors can be granted access to collaborate with the AI workforce inside a single business pod (`e.g., Travelophilia`) with zero technical possibility of accessing Dr. Ziad's personal life pillars or other businesses.
3. **Live Website & CRM Integration:** Each pod houses its own gateway to push/pull data from its dedicated external website (`Travelophilia.com`, `Medicophilia.com`, or `ZiadAlhalwany.com`).

---

## 2. Mandatory Anatomy of `_pod_core/`

Every pod MUST contain a `_pod_core/` directory at its root with the following exact structure and contracts:

```text
<pod_root>/
└── _pod_core/
    ├── local_task_engine/
    │   ├── LOCAL_BOARD.md                   # Pod-isolated Eisenhower + WSJF task board
    │   ├── local_review_approvals.md        # Pod-scoped 5-button approval staging queue
    │   └── public_telemetry_rollup.json     # Sanitized summary read by global federation_rollup_sync.py
    ├── web_and_human_gateway/
    │   ├── website_cms_crm_connector.py     # Adapter for publishing to pod website & syncing CRM leads
    │   └── human_rbac_permissions.yaml      # Strict role-based access boundaries for human staff
    ├── local_mcp_and_plugins/
    │   ├── local_mcp.json                   # Pod-scoped MCP servers (portable across runtimes)
    │   └── runtime_adapter.yaml             # Runtime-agnostic bindings (Hermes / Claude / Codex / Ollama)
    ├── local_hooks/
    │   └── pod_isolation_guard.py           # Blocks any file path traversal outside <pod_root>
    └── _governance_and_registry/
        ├── pod_agents_directory.md          # Roster of all digital employees inside this pod
        ├── pod_scorecard_points.md          # Local 100-point leaderboard for this pod's agents & teams
        ├── okrs_12_week_sprint.md           # Active 12-week sprint goals and KPI progress
        └── pod_blockers.md                  # Overdue tasks and bottlenecks inside this pod
```

---

## 3. Contract Schemas for Pod Federation & Human RBAC

### 3.1 `public_telemetry_rollup.json` Schema

Pods never push data into global files; instead, they update their local `public_telemetry_rollup.json`, which `00_global_system/master_task_engine/federation_rollup_sync.py` reads in one direction:

```json
{
  "pod_id": "medicophilia",
  "pod_type": "business",
  "last_updated_iso": "2026-10-26T18:00:00Z",
  "health_score": 100,
  "completion_pct": 100.0,
  "active_wip_count": 0,
  "pending_approvals_count": 0,
  "top_wsjf_tasks": [],
  "active_blockers": []
}
```

### 3.2 `human_rbac_permissions.yaml` Schema

Enforces strict path jail and tool restrictions when a human collaborator interacts with a pod's agents:

```yaml
pod_id: "travelophilia"
isolation_jail_root: "./"
allow_parent_traversal: false
forbidden_files:
  - "identifiers/private_id.yaml"
  - ".env"
roles:
  venture_admin:
    allowed_departments: ["*"]
    can_approve_reversible_tasks: true
    can_approve_irreversible_tasks: false # Reserved strictly for Supreme Commander Dr. Ziad
  marketing_collaborator:
    allowed_departments: ["03_marketing_and_growth", "01_intelligence_and_rnd"]
    can_approve_reversible_tasks: false
    can_approve_irreversible_tasks: false
```

---

## 4. Mandatory Phase-Gate Detachability Test Protocol

Per Principle II of `.specify/memory/constitution.md`, no Phase Gate may pass without executing the automated **4-Step Detachability Verification**:

1. **Step 1 (`COPY`):** Copy the target pod folder (e.g., `20_businesses/medicophilia`) to an isolated temporary directory outside `D:\AI_Workspace\Jarvis V1` (e.g., `C:\Temp\jarvis_detach_test\medicophilia`).
2. **Step 2 (`BOOT`):** Load the pod's outer shell (`BUSINESS.md`/`PILLAR.md`, `distilled_context.md`, `_pod_core/local_mcp_and_plugins/local_mcp.json`) and verify zero broken path references or missing parent imports.
3. **Step 3 (`OPERATE`):** Create a test task on `_pod_core/local_task_engine/LOCAL_BOARD.md`, compute its deterministic `WSJF` score, verify `pod_isolation_guard.py` blocks `../` path traversal, and update `_pod_core/local_task_engine/public_telemetry_rollup.json`.
4. **Step 4 (`REPORT`):** Verify `STATE.md` and `pod_scorecard_points.md` update cleanly and remove the temporary test directory.
