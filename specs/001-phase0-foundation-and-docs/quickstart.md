# Quickstart: Phase 0 Validation Guide

**Feature**: `specs/001-phase0-foundation-and-docs` | **Date**: 2026-10-26

Runnable scenarios that prove the baseline works end to end. Each maps to success criteria from
[spec.md](./spec.md). Commands assume the workspace root and PowerShell, which is the target host.

Implementation details live in [plan.md](./plan.md), [data-model.md](./data-model.md), and
[contracts/](./contracts/). This file is a validation and operations guide only.

---

## Prerequisites

- Python 3.11 or newer on `PATH`
- PyYAML 6.x installed ahead of time:
  `python -m pip install -r "00_global_system/scripts/requirements.txt"`
- Workspace at `D:\AI_Workspace\Jarvis V1`, path contains a space, so quote every path
- No network access needed during a run; the dependency is installed once, beforehand
- Run from the workspace root

Set a convenience variable to keep the commands readable:

```powershell
Set-Location "D:\AI_Workspace\Jarvis V1"
```

---

## Scenario 1 - Structure matches the declared tree (SC-001, FR-009)

```powershell
python "00_global_system/scripts/scaffold_structure.py" --check
```

Expected: exit 0, `missing=0`, `unexpected=0`. On a fresh copy where placeholders were lost, the
check reports each missing path and exits 1.

Repair without risk of destruction:

```powershell
python "00_global_system/scripts/scaffold_structure.py"
python "00_global_system/scripts/scaffold_structure.py"
```

Expected: first run reports `created=N`, second run reports `created=0` and exits 0. No file is
ever deleted or overwritten; a pre-existing file at a directory path is a hard failure.

---

## Scenario 2 - Quarantine is planned, applied, and reversible (FR-033 to FR-036, SC-013)

Plan first. Nothing moves.

```powershell
python "00_global_system/scripts/quarantine_worker_seats.py" --plan
```

Expected: candidate count, destination, `collisions: 0`, `refusals: 0`.

Apply:

```powershell
python "00_global_system/scripts/quarantine_worker_seats.py" --apply
```

Expected: `moved=136 seats`, manifest written, `remaining live worker seats: 0`.

Verify no worker seat survives in the live trees:

```powershell
Get-ChildItem "10_pillars","20_businesses" -Recurse -Directory -Filter workers -ErrorAction SilentlyContinue
```

Expected: empty output.

Verify integrity and restore one seat:

```powershell
python "00_global_system/scripts/quarantine_worker_seats.py" --verify
python "00_global_system/scripts/quarantine_worker_seats.py" --restore nutrition_and_bio_researcher
```

Expected: verify exits 0 with an entry-per-file hash match. Restore recreates the original path
byte-identically; the manifest entry becomes `RESTORED`.

Put it back before delivery:

```powershell
python "00_global_system/scripts/quarantine_worker_seats.py" --apply
```

---

## Scenario 3 - Refresh is idempotent (SC-004, FR-025, FR-026)

```powershell
python "00_global_system/scripts/doc_guardian.py"
Get-FileHash "00_global_system/agent_registry/DIRECTORY.md","ARCHITECTURE.md" | Format-Table Path,Hash
python "00_global_system/scripts/doc_guardian.py"
Get-FileHash "00_global_system/agent_registry/DIRECTORY.md","ARCHITECTURE.md" | Format-Table Path,Hash
```

Expected: exit 0 both times, identical hashes, and the second run reports no writes. `Last
verified` does not change when no figure changed.

Negative control: create a directory and confirm the count moves exactly once.

```powershell
New-Item -ItemType Directory "99_archive/cold_storage/_probe" | Out-Null
python "00_global_system/scripts/doc_guardian.py"
python "00_global_system/scripts/doc_guardian.py"
Remove-Item "99_archive/cold_storage/_probe" -Recurse
python "00_global_system/scripts/doc_guardian.py"
```

Expected: archive scope is excluded, so counts do not move. For a counted scope, repeat under
`90_dashboard/` and expect `active_directories` to rise by one and return after removal.

---

## Scenario 4 - Hand-written prose is preserved (SC-005, FR-024)

```powershell
Copy-Item "ARCHITECTURE.md" "$env:TEMP/ARCHITECTURE.before.md"
# add a sentinel sentence outside the markers, then:
python "00_global_system/scripts/doc_guardian.py"
Compare-Object (Get-Content "$env:TEMP/ARCHITECTURE.before.md") (Get-Content "ARCHITECTURE.md")
```

Expected: the sentinel line appears identically in both; differences are confined to the block
between the markers. Byte comparison outside the region shows zero changes.

---

## Scenario 5 - Refresh fails closed (FR-027)

```powershell
Copy-Item "ARCHITECTURE.md" "$env:TEMP/ARCHITECTURE.good.md"
# delete the end marker, then:
python "00_global_system/scripts/doc_guardian.py"; $LASTEXITCODE
```

Expected: exit 2, the exact problem named, and `Compare-Object` shows no change to either artifact.
Recover by restoring the copy.

Repeat twice: once with the start marker duplicated, once with the markers reversed. Both must
exit 2 without writing.

---

## Scenario 6 - Drift detection catches injected mismatches (SC-009)

Introduce five mismatches one at a time, running `--check` after each:

1. Delete a required placeholder directory.
2. Create an undeclared directory under a counted domain.
3. Remove the documentation guardian card.
4. Edit a number inside the telemetry region.
5. Rename a feature directory under `specs/`.

```powershell
python "00_global_system/scripts/doc_guardian.py" --check; $LASTEXITCODE
```

Expected: exit 1 for each, with a drift entry naming the path and the expected versus actual
value, except case 4 which reports `count_mismatch` on the region.

---

## Scenario 7 - Counts match an independent audit (SC-007)

```powershell
python "00_global_system/scripts/doc_guardian.py" --json |
  ConvertFrom-Json | Select-Object -ExpandProperty counts

(Get-ChildItem -Recurse -File -Filter AGENT.md |
  Where-Object { $_.FullName -notmatch '\\99_archive\\' }).Count
```

Expected: `live_role_cards` equals the independent count, `quarantined_role_cards` equals the
manifest entry count, and `specification_features` equals `8`.

---

## Scenario 8 - Performance budget (SC-003)

```powershell
Measure-Command { python "00_global_system/scripts/doc_guardian.py" --check }
```

Expected: total under 2 seconds on the target host with 200 or more directories. `elapsed_ms` in
JSON is the in-process figure and should be lower than the wall-clock number.

---

## Scenario 9 - Credential hygiene (SC-008, FR-017, FR-018, FR-032)

```powershell
Test-Path ".gitignore"; Test-Path ".env.example"
Get-Content ".gitignore" | Select-String "private_id.yaml",".env",".db"
```

Expected: both files exist; the ignore rules cover private identifiers, environment files, queue
databases, caches, and editor state. `.env.example` lists variable names with empty values.

Scan behavior: append a synthetic token line to a scratch file inside the workspace, run
`--check`, and confirm the output names the path, the line, and the family without printing the
value. Delete the scratch file afterward.

---

## Scenario 10 - Canonical naming and ownership (SC-014, SC-015)

```powershell
Select-String -Path "ARCHITECTURE.md" -Pattern "local_plugins\.yaml","venture_review_approvals","venture_agents_directory","venture_scorecard","venture_blockers"
Select-String -Path "ARCHITECTURE.md" -Pattern "runtime_adapter\.yaml"
Select-String -Path "ARCHITECTURE.md","00_global_system/agent_registry/DIRECTORY.md" -Pattern "documentation_guardian"
```

Expected: first command returns nothing, second finds `runtime_adapter.yaml`, third shows one
owner per generated artifact.

---

## Scenario 11 - Human readability (SC-002, SC-006, SC-010, SC-012)

Manual checks, no command needed:

1. Using only `README.md` and `ARCHITECTURE.md`, answer ten placement questions with zero verbal
   help. Target 10 of 10.
2. From `README.md`, reach the constitution and the directives in two clicks or fewer.
3. Walk every relative reference in the root documents, including ones from the path containing a
   space. Target zero broken links.
4. Confirm the architecture document describes every domain, including the archive, and marks
   planned artifacts such as `.mcp.json` as planned rather than present.

---

## Scenario 12 - Full phase gate

Run in order and require exit 0 from each:

```powershell
python "00_global_system/scripts/scaffold_structure.py" --check
python "00_global_system/scripts/quarantine_worker_seats.py" --verify
python "00_global_system/scripts/doc_guardian.py" --check
python -m unittest discover -s "00_global_system/scripts/tests" -v
```

Expected: a clean gate. Any non-zero exit blocks the phase. This is the command set to schedule
before every commit and before `/speckit-tasks` marks the phase complete.

---

## Troubleshooting

| Symptom | Likely cause | Action |
|---|---|---|
| Exit 2 on markers | Region edited by hand, duplicated, or reversed | Restore the two marker lines exactly as in the contract |
| Exit 3 | Another refresh is running | Wait, or inspect and remove a stale lock after confirming the pid is dead |
| `count_mismatch` right after a manual move | Files moved outside the governed tools | Re-run apply; never fix numbers by hand |
| Restore refused | Original path already occupied | Inspect the path; restore never overwrites |
| Quarantined count is zero | Manifest missing | Confirm the archive path and that `--apply` completed |
