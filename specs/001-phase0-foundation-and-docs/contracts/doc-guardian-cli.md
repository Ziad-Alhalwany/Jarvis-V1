# Contract: `doc_guardian.py` Command Line Interface

**Feature**: `specs/001-phase0-foundation-and-docs` | **Version**: 1 | **Date**: 2026-10-26

The living-documentation refresh. Deterministic, fail-closed, and limited to one approved
dependency (PyYAML, for the structure manifest). It is the only
writer of `00_global_system/agent_registry/DIRECTORY.md` and of the region between
`<!-- AUTO-STATS-START -->` and `<!-- AUTO-STATS-END -->` in `ARCHITECTURE.md`.

**Owner**: `documentation_guardian` (FR-037, FR-038)

---

## Invocation

```text
python "00_global_system/scripts/doc_guardian.py" [options]
```

| Option | Type | Default | Behavior |
|---|---|---|---|
| `--check` | flag | off | Verify only. Never writes. Exits non-zero on drift |
| `--root PATH` | path | inferred workspace root | Overrides the root; used by tests |
| `--json` | flag | off | Emits one JSON object on stdout, human text suppressed |
| `--verbose` | flag | off | Adds per-directory detail to human output |
| `--timeout SECONDS` | integer | 300 | Lock staleness threshold |
| `--force` | flag | off | Reclaims a live lock; operator only, never in automation |

There is no `--apply` flag. Apply is the default, and every write is scoped by the contract below.

---

## Exit codes

| Code | Meaning | Side effects |
|---|---|---|
| 0 | Success; no drift in check mode, or writes completed | Files possibly rewritten |
| 1 | Drift detected in check mode; or a write failed | No partial writes |
| 2 | Configuration error: markers missing, duplicated, reversed, nested, or manifest unreadable | None, byte-for-byte |
| 3 | Another run holds the lock | None |

Automation may treat any non-zero as failure. Phase gates use `--check`.

---

## Measurement contract

Counts follow R4 in [research.md](../research.md):

- Active directory: directly contains at least one non-excluded file.
- Placeholder: declared, exists, and no files anywhere in its subtree.
- Live role card: `AGENT.md` outside the archive.
- Quarantined role card: counted from the quarantine manifest, never from the archive filesystem.
- Skill bundle: `SKILL.md`.
- Feature: directory under `specs/` matching `^\d{3}-[a-z0-9-]+$`.
- Excluded: `.git`, `.vs`, `.agents`, `.claude`, `.opencode`, `.specify`, `__pycache__`,
  `node_modules`, `.pytest_cache`, `~$*`, `*.tmp`, `Thumbs.db`, `.DS_Store`.

Drift kinds reported by check mode:

| Kind | Meaning |
|---|---|
| `missing_required` | A required structure entry with phase 0 to current phase is absent |
| `unexpected_directory` | A directory exists under a counted domain but is not declared |
| `count_mismatch` | A generated figure differs from the measured figure |
| `ownership_gap` | A generated region has no unique owner, or its owner card is absent |
| `region_malformed` | Marker rules violated; exits 2, not 1 |

---

## Write contract

| Target | Mode |
|---|---|
| `00_global_system/agent_registry/DIRECTORY.md` | Full regeneration |
| `ARCHITECTURE.md` | Replace only bytes between the two markers |

Rules:

1. Write only when the rendered content differs. An unchanged run leaves mtime untouched (R3).
2. Write via temporary file in the same directory, then atomic replace.
3. Never touch any other file. In particular, never write to `specs/`, agent cards, pod state,
   `CLAUDE.md`, the directives, or the constitution (FR-030).
4. Never delete, rename, or move anything.
5. Refuse to write if the resulting file would be identical except for the `Last verified` date
   (prevents date-only churn).

---

## stdout JSON schema (`--json`)

```json
{
  "status": "ok | drift | error",
  "mode": "apply | check",
  "workspace_root": "D:/AI_Workspace/Jarvis V1",
  "measured_at": "2026-10-26",
  "counts": {
    "active_directories": 0,
    "placeholder_directories": 0,
    "live_role_cards": 0,
    "quarantined_role_cards": 0,
    "skill_bundles": 0,
    "specification_features": 0,
    "per_domain": { "00_global_system": { "active": 0, "placeholder": 0, "cards": 0, "bundles": 0 } }
  },
  "drift": [
    { "kind": "missing_required", "path": "10_pillars/01_health_and_growth/_pod_core", "expected": "present", "actual": "absent" }
  ],
  "findings": [
    { "path": "README.md", "line": 12, "family": "bot-token" }
  ],
  "warnings": [],
  "errors": [],
  "elapsed_ms": 0
}
```

Guarantees: stable key order; arrays sorted by `path`, then `line`; no credential values; no
absolute paths except `workspace_root`; exit code agrees with `status` (`drift` maps to 1,
`error` to 2 or 3).

---

## Human output

Check mode, clean:

```text
doc_guardian: check passed (active=197 placeholder=38 cards=65 bundles=0 features=8) in 412ms
```

Check mode, drift:

```text
doc_guardian: DRIFT detected (2 issues)
  missing_required 10_pillars/01_health_and_growth/_pod_core  expected=present actual=absent
  count_mismatch   ARCHITECTURE.md: active_directories expected=197 actual=196
doc_guardian: no files written
```

Configuration error:

```text
doc_guardian: config error in ARCHITECTURE.md
  region start marker appears 2 times (expected 1)
doc_guardian: aborted before writing; no files changed
```

---

## Lock contract

- Lock path: `00_global_system/scripts/.doc_guardian.lock`
- Content: pid, host name, ISO start time.
- A lock older than `--timeout` or owned by a dead pid on the same host is reclaimed with a
  warning on stderr.
- `--force` reclaims unconditionally; it prints the displaced lock owner.
- The lock is removed in a `finally` block, including on interrupted runs.

---

## Performance budget

Full scan of 500 or more directories under 2 seconds on the target host (SC-003). The implementation
uses one pruned `os.scandir` walk per scope and reads file content only for the credential scan,
below a 256 KB cap. If the budget is exceeded, `elapsed_ms` makes it visible in JSON and the
quickstart fails the gate.

---

## Required companion checks

`--check` must also verify:

1. Every generated region declares the documentation guardian as owner, and the guardian card
   exists (SC-014).
2. `ARCHITECTURE.md` mentions no superseded pod-core name such as `local_plugins.yaml` or
   `venture_review_approvals.md` (SC-015).
3. `.gitignore` exists and lists `private_id.yaml`, `.env`, and queue or database artifacts
   (FR-017).
