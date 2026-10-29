# Phase 0 Research: Foundation, Directory Skeleton & Living Documentation

**Feature**: `specs/001-phase0-foundation-and-docs` | **Date**: 2026-10-26

All Technical Context unknowns are resolved below. No `NEEDS CLARIFICATION` markers remain.

---

## R1. Utility decomposition: three executables instead of one

**Decision**: Ship `scaffold_structure.py`, `doc_guardian.py`, and
`quarantine_worker_seats.py` as separate entry points.

**Rationale**: The three operations have incompatible risk profiles. Scaffolding creates
directories and must never delete. The refresh must be provably unable to write outside two
generated regions, because it runs at every phase gate and will run unattended. Quarantine is the
only destructive move in the phase and must be isolated, auditable, and reversible. Combining
them behind an operation flag means the verify path and the mutate path share argument parsing,
lock acquisition, and failure handling, which is exactly the coupling that a fail-closed
guardrail should not have.

**Alternatives considered**:
- One `doc_guardian.py --mode scaffold|refresh|quarantine`: fewer files, but a bug in the
  quarantine branch can be reached from the verification path, and `--check` could never be
  argued to be read-only by inspection.
- Shell or PowerShell wrappers: violates the deterministic-core rule and adds a second language
  to review.

---

## R2. Structure manifest as the single expected-tree source

**Decision**: Declare the expected tree in `01_templates/structure_manifest.yaml`. Scaffold
materializes it. The refresh verifies the filesystem against it and reports missing, unexpected,
and misclassified directories. Phase 3's clone tool will extend the same file.

**Rationale**: SC-001 requires 100 percent path coverage with zero undocumented additions, which
is only checkable against a machine-readable expectation. Prose in `ARCHITECTURE.md` cannot be
the source of truth because it is formatted for humans and must stay readable. Putting the
manifest in `01_templates/` places it with the cloning blueprints, and keeps
`00_global_system/directives/` at exactly the three governance documents FR-020 requires.

**Alternatives considered**:
- Parse the directory tree out of `ARCHITECTURE.md`: fragile, breaks when prose improves, and
  turns the documentation into a schema.
- Hardcode the tree in Python: fast to write, guaranteed to drift, and unreviewable by the
  Commander.
- One YAML per domain: more files, no benefit at this size.

**Manifest contents**: `schema_version`, `naming_law`, `domains[]`, and `entries[]` where each
entry has `path`, `owner`, `purpose`, `phase`, `scope` (`active`, `placeholder`, `archive`,
`tooling`), and `required`. Directories only. Files are validated by dedicated checks in the
refresh and by the required-document list, because file existence and file content are separate
concerns.

---

## R3. Determinism versus timestamps

**Decision**: Generated regions carry no wall-clock time. They carry `Last verified` as an ISO
date, and that date is rewritten only when at least one measured value changes. When nothing
changed, the file is not written at all.

**Rationale**: The existing architecture block claimed synchronization at `2026-10-26 18:00:00`
while no generator existed. Any per-run timestamp guarantees that two consecutive runs differ,
which directly contradicts FR-025 and FR-026 and SC-004. Removing the clock makes idempotency a
property of the data rather than a promise. Operators still get run timing from the console and
from JSON output.

**Alternatives considered**:
- Keep the timestamp and define idempotency as ignoring that line: weakens the check and creates
  a special case in the golden-file test.
- Use the maximum file mtime: unstable on checkout, and meaningless in a copied pod.

---

## R4. Count definitions

**Decision**:

- **Active structural directory**: a directory within the counted scopes that directly contains
  at least one file after exclusions.
- **Placeholder directory**: an expected directory with no files anywhere in its subtree.
- **Archived directory**: anything under `99_archive/`. Counted separately and excluded from all
  active figures.
- **Role card**: a file named `AGENT.md`. Live cards are counted outside the archive; quarantined
  cards are counted from the manifest, not from the filesystem.
- **Skill bundle**: a file named `SKILL.md`.
- **Specification feature**: a directory whose name matches three digits, a hyphen, then a short
  name, directly under `specs/`.
- **Excluded scopes**: `.git`, `.vs`, `.agents`, `.claude`, `.opencode`, `.specify`,
  `__pycache__`, `node_modules`, `.pytest_cache`, and editor or sync residue such as `~$*`,
  `*.tmp`, `Thumbs.db`, and `.DS_Store`.

**Rationale**: FR-029 requires placeholders to be counted separately, and FR-036 requires
archived seats to be excluded from active counts. "Contains a file directly" is cheap to compute
and does not change when a subtree grows, which keeps the figure stable across edits deep inside a
pod. Counting archived cards from the manifest, not the filesystem, makes the manifest the sole
authority exactly as FR-036 demands, and gives SC-007 an independent cross-check.

**Alternatives considered**:
- Count any non-empty subtree as active: a single file at the top of a pod would mark every
  descendant active, inflating the number and hiding placeholders.
- Count only leaf directories: loses the hierarchy the Commander reads.

---

## R5. Protected-region parsing and write scope

**Decision**: Parse regions with exact single-line markers. Require exactly one start marker and
one end marker, start before end, both on their own lines, no nesting. Any deviation aborts with
exit code 2 before a single byte is written.

**Rationale**: FR-027 demands fail-closed behavior and FR-024 demands exact preservation of
prose. A tolerant parser that appends a second region converts a documentation error into silent
duplication, which is the failure mode the phase exists to remove. Aborting is recoverable;
duplicating is not.

**Write scope**: `00_global_system/agent_registry/DIRECTORY.md` is regenerated in full. In
`ARCHITECTURE.md`, only the bytes between the markers are replaced. Writes use a temporary file
in the same directory followed by an atomic replace, so an interrupted run leaves the previous
version intact.

**Alternatives considered**:
- Regex-based tolerant replacement: silently matches the wrong region when a marker appears in a
  code sample.
- Append-only inventory file with history: grows without bound and defeats idempotency.

---

## R6. Single-writer lock

**Decision**: A lock file beside the scripts, containing pid, host, and ISO start time. A live
lock exits with code 3. A lock older than 300 seconds, or belonging to a dead pid on the same
host, is reclaimed with a warning.

**Rationale**: SC-004 and FR-026 are evaluated by consecutive runs, and concurrent runs produce
interleaved writes that are neither idempotent nor diagnosable. Five minutes is comfortably
longer than the two-second performance budget while short enough that a crashed run does not
block a phase gate for long.

**Alternatives considered**:
- No lock, rely on operator discipline: violates the spec's single-writer assumption.
- OS-level exclusive file handle: not portable to the small test harness and harder to inspect
  after a crash.

---

## R7. Credential scanning

**Decision**: A bounded, read-only scan of documentation files for credential families: private
key headers, cloud access key identifiers, bearer tokens, bot tokens with the characteristic
numeric prefix, and long high-entropy strings adjacent to key-like words. Findings report path,
line number, and family only. Values are never printed, logged, or written.

**Rationale**: FR-032 requires flagging without reproduction, and FR-018 requires no credential
values in documentation. Reporting the family and location is enough for a human to fix it
without the value entering a log, a JSON payload, or the conversation transcript.

**Limit**: Files above 256 KB and binary files are skipped. The scan is heuristic and is a
guardrail, not a security control; the ignore configuration from FR-017 remains the primary
protection.

**Alternatives considered**:
- Full secret-scanning toolchain: a third-party dependency for a documentation tree, and it would
  need network access for signature updates.
- Hash-and-compare against known keys: no known keys exist yet.

---

## R8. Quarantine schema, hashing, and restore

**Decision**: One JSON manifest at
`99_archive/cold_storage/quarantined_worker_seats/MANIFEST.json`. Each entry records role
identifier, original path, archived path, per-file relative path and SHA-256, file count, and a
status of `QUARANTINED` or `RESTORED`. Entries are sorted by original path. The move relocates
each department's `workers/` directory as a unit, while entries remain per seat so a single seat
can be restored.

**Rationale**: FR-033 requires path, role, and archive path. FR-034 requires lossless and
reversible, which is only demonstrable if the content hash is recorded before and verified after.
Per-seat entries give Phase 5 and Phase 6 a lookup table by role identifier, and a unit move keeps
the operation fast and atomic at the filesystem level.

**Refusals**: An apply run refuses to overwrite an existing archive destination, refuses to move a
seat already recorded as quarantined, and refuses to move when the live `workers/` path resolves
outside the named pod. Restore refuses when the original destination is occupied.

**Alternatives considered**:
- Copy then delete: doubles peak disk use and creates a window where two copies exist.
- Markdown-only manifest: human-friendly but unsafe to parse for exact paths and hashes. The
  human-readable index lives in the architecture document's archive section instead.
- Zip archive: opaque, and hostile to single-seat restore.

---

## R9. Empty directories and version control

**Decision**: Do not add `.gitkeep` files. Empty expected directories are part of the declared
manifest and are recreated by scaffold. Check mode reports a missing-but-expected directory as
drift.

**Rationale**: A `.gitkeep` makes an empty placeholder count as an active directory under R4,
which corrupts the very metric the phase introduces, and it adds 200 files whose only purpose is
to defeat a version-control convention that the project does not require (version control is
optional per the spec's assumptions). Declaring intent in the manifest plus a check mode gives the
same protection without polluting counts.

**Alternatives considered**:
- `.gitkeep` everywhere: simple, but conflicts with placeholder classification.
- Ignore missing directories: makes SC-001 unverifiable.

---

## R10. Markdown as human truth, JSON for machine records, PyYAML for the manifest

**Decision**: All prose, tables, and governance remain Markdown. JSON is used only for the
quarantine manifest, which is machine-read and hash-verified. The structure manifest is YAML and
is parsed with PyYAML at version 6 or newer, pinned in `00_global_system/scripts/requirements.txt`.

**Rationale**: The constitution pre-approves PyYAML for declarative config and schema parsing, so
this needs no amendment. The Commander chose the maintained parser over a hand-written subset
reader, which removes the only custom parser in the design, eliminates a class of YAML edge-case
bugs, and lets validation focus on the manifest's semantics rather than on its syntax. PyYAML is
one pinned dependency, present on the target host before the phase runs, and never fetched at run
time.

**Alternatives considered**:
- Hand-written subset reader: zero dependencies, but it is a liability the project would maintain
  forever, and its failure modes look like manifest bugs.
- JSON manifest: no parser needed, but a human annotating 200 entries with purpose and owner
  deserves comments and readable structure.
- Defer the dependency to Phase 3: the manifest is used from Phase 0 onward, so this would leave
  the first phase on the throwaway parser and force a rewrite.

**Guard**: Validation is explicit and strict regardless of parser. Unknown top-level keys,
duplicate paths under case-insensitive comparison, undeclared parents, absolute paths, `..`
segments, and names that violate the naming law are all hard failures with exit code 2.

---

## R11. Testing strategy

**Decision**: `unittest` discovery under `00_global_system/scripts/tests/`, with fixtures that
build throwaway directory trees under the system temp directory. Real workspace data is never
copied into tests.

**Coverage required by the spec**:
- Golden-file comparison proving two consecutive refreshes are byte-identical (SC-004).
- Prose preservation: sentinel text outside the region survives and the region changes (SC-005).
- Fail-closed: missing, duplicated, and reversed markers each exit 2 with unchanged file hashes
  (FR-027).
- Drift detection: five injected mismatches each exit non-zero (SC-009).
- Scaffold idempotency and non-destruction (FR-009).
- Quarantine round trip: apply, verify hashes, restore one seat, verify byte identity (FR-034).
- Count accuracy against a hand-built fixture with known totals (SC-007).
- Path handling: workspace path containing a space, and a case-differing duplicate name.

**Rationale**: Every success criterion that can be checked mechanically gets a test, and every
test runs without the real workspace so it cannot corrupt the baseline. `unittest` is chosen over
`pytest` so the approved dependency list stays at exactly one package, PyYAML; the tradeoff is
terser assertions, not weaker coverage.

---

## R12. Performance approach

**Decision**: One `os.scandir` walk per scope with pruning at excluded directory names. Content is
read only for the credential scan and only below the size cap. Directory-level totals are
accumulated in a single pass. Markdown rendering happens after measurement, from in-memory
structures.

**Rationale**: SC-003 sets 2 seconds at 200 or more directories; the current tree is roughly 484
before quarantine. A pruned single walk is O(directories) with no repeated stat calls and no
per-directory process spawn. Sorting is done once per table.

**Measurement**: The quickstart records wall-clock timing on the real workspace and asserts the
budget. The JSON output includes elapsed milliseconds for diagnosis without writing it into the
generated Markdown.

---

## R13. Documentation adoption strategy

**Decision**: Adopt and amend `README.md`, `CLAUDE.md`, and
`PROJECT_GENESIS_AND_DISCUSSIONS_DRAFT.md`. Rewrite `ARCHITECTURE.md` except for its philosophy
sections, which remain accurate and are preserved. Regenerate `DIRECTORY.md` entirely.

**Rationale**: The existing files are substantial and largely consistent with the constitution;
rewriting them would discard the Commander's voice and the intellectual history the genesis
document exists to preserve. The architecture document, by contrast, contains the fabricated
telemetry, a missing archive section, and the superseded `local_plugins.yaml` naming, so it needs
structural repair rather than cosmetic edits.

**Specific corrections required in `ARCHITECTURE.md`**:
- Replace the telemetry region with the generated block and its owner.
- Add an anatomy section for the archive domain and for the seven top-level domains in the root
  table.
- Replace `local_plugins.yaml` with `runtime_adapter.yaml`, and `venture_*` pod-core names with
  the canonical `pod_*` set.
- Mark `.mcp.json` and `.env` as planned artifacts of later phases rather than present ones.
- Describe the documentation guardian seat and its ownership of both generated regions.

---

## R14. Cross-platform path handling

**Decision**: Store and compare paths as workspace-relative POSIX-style strings internally
(`/` separators), convert to native form only for filesystem calls, and preserve the original
spelling in generated output. Comparisons are case-insensitive for duplicate detection but
case-preserving for display.

**Rationale**: The host is Windows and the root contains a space, while pod copies may travel to
Linux servers. Normalizing separators internally prevents the backslash-versus-slash class of bug
in table generation, and keeping display spelling avoids rewriting paths the Commander already
reads. Case-insensitive duplicate detection catches the class of error where a path differs only
by case and silently resolves to the same directory.

**Alternatives considered**:
- `os.path.realpath` everywhere: resolves symlinks, which the spec forbids following outside the
  root, and loses the original spelling.

---

## R15. Treatment of the pre-existing artifact discrepancy

**Decision**: Treat every pre-existing generated figure as unverified. Recompute all figures from
the filesystem during the first apply run, and record the discrepancy in
`PROJECT_GENESIS_AND_DISCUSSIONS_DRAFT.md` as part of the history rather than silently replacing
the numbers.

**Measured discrepancy on 2026-10-26**:

| Figure | Architecture claim | Directory claim | Measured |
|---|---|---|---|
| `AGENT.md` cards | 142 | 203 | 203 |
| `SKILL.md` bundles | 3 | not stated | 0 |
| Structural directories | 215 | not stated | 484 |
| Specification features | 8 | not stated | 8 |

**Rationale**: The spec's edge case on stale telemetry requires regeneration plus a history note.
Two documents disagreeing by 61 employees, both claiming machine generation, and neither having a
generator, is precisely the failure this phase is chartered to end. Recording it keeps the
evidence that the guardrail was needed and prevents the same block from being restored from an old
copy without scrutiny.

**Alternatives considered**:
- Silently overwrite: loses the audit trail and the argument for why the guardian exists.
- Trust `DIRECTORY.md` because it is larger: correct by accident for cards, wrong for skills, and
  wrong as a method.

---

## Resolved unknowns summary

| Technical Context field | Resolution |
|---|---|
| Language and version | Python 3.11+ (R1, R11) |
| Dependencies | PyYAML 6.x for the manifest; standard library otherwise (R10) |
| Storage | Filesystem; Markdown and JSON only (R8, R10) |
| Testing | `unittest` with temp-tree fixtures and golden files (R11) |
| Target platform | Windows 11, space in path, case-insensitive (R14) |
| Project type | Domain-indexed single repository (plan Structure Decision) |
| Performance | Under 2 seconds at 500 directories (R12) |
| Constraints | Fail closed, single writer, no deletion outside quarantine (R5, R6, R8) |
| Scale | 7 domains, 8 features, 7 pods, 6 executive seats (R4) |
