# Contract: Structure Manifest (`01_templates/structure_manifest.yaml`)

**Feature**: `specs/001-phase0-foundation-and-docs` | **Version**: 1 | **Date**: 2026-10-26

The single declarative source of truth for the expected workspace tree. Scaffolding materializes
it. The documentation refresh verifies against it. Phase 3 clone tooling extends it.

**Owner**: `documentation_guardian` for the file, with each entry carrying its own accountable
role (FR-038)

---

## Why this file exists

SC-001 requires 100 percent of documented paths to exist with zero undocumented additions. That is
only checkable against a machine-readable expectation. Prose in `ARCHITECTURE.md` stays readable
and cannot serve as a schema, and hardcoding the tree in Python guarantees drift.

Placement in `01_templates/` keeps `00_global_system/directives/` at exactly the three governance
documents required by FR-020, and sits with the cloning blueprints that Phase 3 will use.

---

## Parsing and validation

The manifest is parsed with PyYAML: `yaml.safe_load`, version 6 or newer, pinned in
`00_global_system/scripts/requirements.txt`. PyYAML is pre-approved by the constitution's
technology constraints. The loader uses no custom constructors and deserializes objects only into
built-in mappings, sequences, and scalars.

Parse failures and schema violations are exit code 2, never a guess. A `yaml.YAMLError` is
reported with its line and column, no partial manifest is returned, and nothing is written to disk.

Schema validation is explicit and mandatory even though the parser accepts more YAML than the
schema allows. Unknown top-level keys, unknown entry keys, wrong scalar types, duplicate paths
under case-insensitive comparison, undeclared parents, absolute paths, `..` segments, and names
that violate the naming law are all hard failures.

---

## Schema

```yaml
schema_version: 1
naming_law: "numbered prefixes where specified, otherwise lowercase underscore-separated words, no spaces"

domains:
  - id: "00_global_system"
    number: 0
    purpose: "Shared deterministic engines, directives, registry, and learning loop"
    owner: "jarvis_prime"
    scope: "active"
    inventory: "counted"

entries:
  - path: "00_global_system/directives"
    owner: "jarvis_prime"
    purpose: "Binding governance documents"
    phase: 0
    scope: "active"
    required: true
```

### Domain fields

| Field | Type | Rules |
|---|---|---|
| `id` | string | Matches the directory name exactly; unique |
| `number` | integer | Display prefix; unique |
| `purpose` | string | One sentence; reused verbatim in generated tables |
| `owner` | string | Role identifier that owns the domain |
| `scope` | enum | `active`, `archive`, or `tooling` |
| `inventory` | enum | `counted` or `excluded` |

### Entry fields

| Field | Type | Rules |
|---|---|---|
| `path` | string | Workspace-relative, POSIX separators, no trailing slash, no `..` |
| `owner` | string | Must be a declared or planned role identifier |
| `purpose` | string | Short noun phrase; feeds the architecture anatomy |
| `phase` | integer | 0 through 8; the phase that populates it |
| `scope` | enum | `active`, `placeholder`, `archive`, or `tooling` |
| `required` | boolean | When true, absence is drift once its phase gate is reached |

---

## Validation rules

1. `schema_version` must equal 1.
2. Every domain `id` and every entry `path` is unique under case-insensitive comparison (R14).
3. Every entry path must start with a declared domain id.
4. Every entry's parent directory must also be declared, except the domain root itself.
5. Naming law is enforced on every element of every path (FR-008).
6. No entry may resolve outside the workspace root; absolute paths and `..` segments are rejected.
7. No entry may declare a path under another pod, which keeps the no-cross-pod rule visible in
   data rather than only in prose (FR-011).
8. Phase 0 entries must be materializable with no file content: directories only.
9. The manifest never declares quarantined paths; the quarantine manifest is authoritative for
   the archive (FR-036).

---

## Materialization semantics (`scaffold_structure.py`)

| Behavior | Rule |
|---|---|
| Create | `mkdir` parents as needed, in sorted path order |
| Existing directory | Left untouched; never renamed, cleared, or modified |
| Existing file at a directory path | Hard failure, exit 1, no further writes |
| Deletion | Never. No tool in this phase removes an entry |
| Idempotency | A second run creates nothing and reports `created=0` |
| `--check` | Reports missing, unexpected, and misnamed directories without writing |
| Output | Human summary or `--json` with `created`, `existing`, `missing`, `errors` |

Empty directories are intentional (assumptions: placeholders stay empty). No `.gitkeep` is
created, because a placeholder with a file stops being a placeholder under the count rules and
would corrupt the inventory metric (R9).

---

## Consumer map

| Consumer | Uses the manifest for |
|---|---|
| `scaffold_structure.py` | Creating missing directories |
| `doc_guardian.py --check` | Drift: missing required, unexpected present |
| `ARCHITECTURE.md` authoring | Purpose and owner text for every anatomy entry |
| Phase 3 `clone_pod.py` | Subtree selection when instantiating a new pod |
