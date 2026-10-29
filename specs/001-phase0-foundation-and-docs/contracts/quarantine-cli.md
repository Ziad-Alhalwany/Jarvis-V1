# Contract: `quarantine_worker_seats.py` Command Line Interface

**Feature**: `specs/001-phase0-foundation-and-docs` | **Version**: 1 | **Date**: 2026-10-26

Moves pre-existing worker-level seats into the archive with a hash-verified manifest. This is the
only mutating move in Phase 0, so it is isolated in its own executable with an explicit plan mode
and a per-seat restore path.

**Owner**: `documentation_guardian` (archive custody)

---

## Invocation

```text
python "00_global_system/scripts/quarantine_worker_seats.py" --plan  [--json] [--root PATH]
python "00_global_system/scripts/quarantine_worker_seats.py" --apply [--json] [--root PATH]
python "00_global_system/scripts/quarantine_worker_seats.py" --restore ROLE_ID [--json] [--root PATH]
python "00_global_system/scripts/quarantine_worker_seats.py" --verify [--json] [--root PATH]
```

Exactly one mode is required. `--plan` is read-only and is the mandatory first step in the
quickstart.

---

## Candidate detection

A candidate seat is a directory that satisfies all of:

1. Its path matches `<domain>/<pod>/<department>/workers/<role_id>` under `10_pillars/` or
   `20_businesses/`.
2. `<role_id>` contains an `AGENT.md`.
3. `<role_id>` is not already recorded in the quarantine manifest.

Managers, leads, and C-suite seats are not candidates: their directories are `manager/`,
`00_pillar_lead/`, or `00_c_suite_leadership/*`, none of which sit under `workers/` (FR-035).

---

## Modes

| Mode | Behavior | Writes |
|---|---|---|
| `--plan` | Lists candidates, destination paths, file counts, total bytes, and any collision or refusal reason | None |
| `--apply` | Moves each department's `workers/` directory as a unit, records per-seat entries, verifies hashes after the move | Archive tree and `MANIFEST.json` |
| `--restore ROLE_ID` | Moves one recorded seat back to its original path, verifies content hash, marks the entry `RESTORED` | Pod tree and manifest |
| `--verify` | Recomputes hashes of every `QUARANTINED` entry against the manifest | None |

Apply is resumable and idempotent: entries already marked `QUARANTINED` are skipped, so an
interrupted run continues from the first unrecorded seat without duplicating moves.

---

## Exit codes

| Code | Meaning |
|---|---|
| 0 | Success, including a plan or verify with no findings |
| 1 | Refused or partial: destination occupied, path escapes the pod, hash mismatch |
| 2 | Invalid arguments, unreadable manifest, or schema violation |
| 3 | Lock held by another run |

---

## Manifest schema

Location: `99_archive/cold_storage/quarantined_worker_seats/MANIFEST.json`

```json
{
  "schema_version": 1,
  "generated_at": "2026-10-26",
  "workspace_root_name": "Jarvis V1",
  "counts": { "quarantined": 136, "restored": 0, "files": 136, "bytes": 0 },
  "entries": [
    {
      "role_id": "nutrition_and_bio_researcher",
      "pod_id": "01_health_and_growth",
      "department": "01_think_and_learn",
      "original_path": "10_pillars/01_health_and_growth/01_think_and_learn/workers/nutrition_and_bio_researcher",
      "archived_path": "99_archive/cold_storage/quarantined_worker_seats/10_pillars/01_health_and_growth/01_think_and_learn/workers/nutrition_and_bio_researcher",
      "files": [
        { "path": "AGENT.md", "sha256": "0000000000000000000000000000000000000000000000000000000000000000" }
      ],
      "file_count": 1,
      "status": "QUARANTINED",
      "moved_at": "2026-10-26"
    }
  ]
}
```

Guarantees:

- `entries` is sorted by `original_path` for deterministic output.
- Hashes are lowercase hex SHA-256 of file bytes, computed before the move and re-verified after.
- No absolute paths appear anywhere in the manifest, so the archive stays portable.
- `counts.quarantined` counts entries with status `QUARANTINED`; the refresh reads this figure
  rather than scanning the archive (FR-036).
- JSON keys are emitted in a fixed order and written with a fixed indent, so two runs over the
  same state produce identical bytes.

---

## Refusal conditions

Apply refuses and writes nothing when any of these is true:

1. An archive destination already exists and is not empty.
2. A resolved path escapes the pod root, for example through a link.
3. The live role directory contains no `AGENT.md`.
4. The role identifier appears twice in the same pod, which would make restore ambiguous.
5. The manifest is unreadable, has a different `schema_version`, or contains a path outside the
   archive.

Restore refuses when the original path is occupied. It never overwrites and never deletes.

---

## Safety properties

| Property | Enforcement |
|---|---|
| Lossless | Every file hashed before and after the move; mismatch aborts before recording |
| Reversible | Per-seat restore by role identifier, independent of the archive tree layout |
| Auditable | Manifest records dates, paths, counts, and hashes; human index in the architecture archive section |
| Non-destructive outside scope | Only paths under `workers/` and the archive destination are ever touched |
| No silent overwrite | Destination collision is exit 1, not a warning |
| Portability | No absolute paths in the manifest; archive can move with the repository |

---

## Human output

```text
quarantine: plan only, nothing moved
  candidates: 136 seats in 35 workers directories, 136 files, 0 bytes
  destination: 99_archive/cold_storage/quarantined_worker_seats
  collisions: 0   refusals: 0
```

```text
quarantine: applied
  moved: 136 seats (136 files)
  manifest: 99_archive/cold_storage/quarantined_worker_seats/MANIFEST.json
  remaining live worker seats: 0
```
