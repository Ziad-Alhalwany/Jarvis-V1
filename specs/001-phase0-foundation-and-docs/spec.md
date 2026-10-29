# Feature Specification: Phase 0 - Foundation, Federated Directory Skeleton & Living Documentation

**Feature Branch**: `001-phase0-foundation-and-docs`

**Created**: 2026-10-26

**Status**: Draft

**Input**: User description: "Read PLAN.md and create a specification for the PHASE 0: Foundation, Federated Directory Skeleton & Living Documentation only."

## Clarifications

### Session 2026-10-26

- Q: Phase 0 finds 203 pre-seeded AGENT.md cards and per-worker folders already on disk, but the approved skeleton depth excludes worker folders. What should Phase 0 do with them? → A: Quarantine worker-level cards to cold storage: move worker seats into the archive, keep pod shells plus lead and manager seats, and let Phases 5 and 6 rebuild workers from templates.
- Q: PLAN names Raqib as Documentation Guardian, but that seat is missing from ARCHITECTURE, from all 203 agent cards, and from every directive, while CLAUDE.md makes the guardian script mandatory after every structural change. Who should own the documentation refresh? → A: Add a sixth global seat, reporting to the prime interface, owning the generated inventory, the architecture telemetry block, and drift verification; the baseline seeds its agent card.
- Q: Which document defines the canonical pod core file names, given that PLAN.md uses venture_* names, ARCHITECTURE.md uses local_plugins.yaml, and the Detachability Standard uses runtime_adapter.yaml? → A: The Detachability Standard wins: local_review_approvals.md, runtime_adapter.yaml, and the pod_* names are canonical, and the roadmap and architecture references are corrected.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Every future artifact already has a canonical home (Priority: P1)

The Commander opens the workspace root and sees the federated skeleton: seven numbered
domains, each with its documented sub-areas, and every life pillar and commercial venture
already seated in its own pod folder with its outer shell, core, and department structure in
place. From this day forward no phase, agent, or collaborator has to invent a location or
negotiate a path: the layout is decided once, in public, and every later phase simply fills it.

**Why this priority**: It is the hard prerequisite for all seven remaining phases. Pod
detachability, tenant isolation, and the standard pod shell are only enforceable if the
directory boundaries exist before content is written into them. Without this story, every
later phase improvises structure and the constitution's pod boundary becomes unverifiable.

**Independent Test**: Enumerate every directory path named in the project roadmap, then walk
the filesystem. The story passes when zero documented paths are missing and a collaborator can
create a new file at any documented location without first creating a parent folder.

**Acceptance Scenarios**:

1. **Given** an empty workspace containing only the specification tooling, **When** the
   foundation is materialized, **Then** the seven numbered domains - global system, templates,
   personal pillars, commercial ventures, infrastructure, dashboard, and archive - exist at the
   workspace root alongside the existing specification and tooling areas.
2. **Given** the materialized skeleton, **When** the roadmap tree is compared against the
   filesystem path by path, **Then** every documented directory exists and none exists unnamed
   or undocumented.
3. **Given** a collaborator assigned to a single department of a single venture, **When** they
   write a new file into that department's folder, **Then** the write succeeds immediately with
   no parent creation and no access to any other pod.
4. **Given** the skeleton is materialized twice in a row, **When** the second run completes,
   **Then** no existing file or folder is deleted, renamed, or overwritten.
5. **Given** the global executive command area, **When** its seats are listed, **Then** the five
   existing global officers plus the documentation guardian are present, and the guardian's card
   claims ownership of the generated inventory and the architecture telemetry block.

---

### User Story 2 - Anyone can understand the ecosystem by reading, not by asking (Priority: P2)

A new human collaborator or a newly booted AI agent lands in the workspace with no prior
context. The quick-start portal tells them what this place is and where to begin; the
architecture document explains, from macro to micro, what every folder and governance file is
for and which role owns it. They stop needing the Commander as a human index.

**Why this priority**: The digital workforce is meant to be onboarded by written context. If
placement knowledge lives only in the Commander's head, every new agent and every new hire
becomes a bottleneck, and documentation drift makes the org chart fiction.

**Independent Test**: Give a person who has never seen the repository only the root
documentation, then ask ten placement questions ("where does a venture's qualified lead
record live?", "where does a pillar's habit metric live?", "where are scoring rules
defined?"). The story passes at ten out of ten correct answers with no verbal help.

**Acceptance Scenarios**:

1. **Given** only the root documentation, **When** asked where a named artifact class belongs,
   **Then** the documentation names the exact folder and the role that owns it.
2. **Given** the architecture document, **When** it is read top to bottom, **Then** every
   top-level domain and every nested directory shown in the roadmap is described with its
   purpose, its owning role, and what must never be stored there.
3. **Given** the workspace root path contains a space, **When** any reference in the
   documentation is followed, **Then** the reference resolves correctly.
4. **Given** the quick-start portal, **When** a reader wants the governing law or the binding
   rules, **Then** they reach both in no more than two navigation steps.

---

### User Story 3 - Binding rules sit in one place, independent of any tool (Priority: P3)

An agent booting under any agent runtime, editor, or orchestration host finds exactly one
directives location holding the Commander's cognitive DNA and voice rules, the global
governance rules, and the detachability standard. Whatever runtime is in fashion this quarter,
the rules are the same rules and they live in the same place.

**Why this priority**: The workforce must outlive any single vendor. Centralized, plain-text
directives are what make a runtime swap a configuration change instead of a rewrite. This
story also gives every later agent card a single, unambiguous boot reference.

**Independent Test**: Start from a clean agent boot with only the directives folder and the
constitution available. The story passes when the agent can state its authority chain, its
communication restrictions, and its detachability obligations without any tool-specific
instruction.

**Acceptance Scenarios**:

1. **Given** the directives area, **When** it is listed, **Then** it contains exactly one
   document for cognitive DNA and voice, one for global governance rules, and one for the
   detachability standard.
2. **Given** a governance directive, **When** it is read, **Then** it names the roles it binds
   and cites the constitutional principle it enforces.
3. **Given** the directives, **When** they are read on a different agent runtime, **Then** no
   content requires translation because none of it references a vendor, product, or tool
   interface.

---

### User Story 4 - Documentation that cannot silently go stale (Priority: P4)

The Commander, or a scheduled routine, runs a single documentation refresh. The living
inventory - how many active areas exist, how many agent cards, how many skill bundles, how
many specification features - is recomputed from filesystem truth and written back in place,
while every hand-written explanation is preserved exactly. The org map can no longer disagree
with reality.

**Why this priority**: Stale directory counts are the first lie in a documented organization.
Automating the counts makes every later phase gate cheap and trustworthy, and gives the
Commander a one-command answer to "what does the ecosystem actually contain right now?".

**Independent Test**: Record the current counts, add and remove a handful of files and
folders, run the refresh twice, then compare. The story passes when the first run updates the
counts to match reality, the second run changes nothing at all, and all prose outside the
generated regions is identical to the original.

**Acceptance Scenarios**:

1. **Given** documentation containing protected generated regions, **When** the refresh runs,
   **Then** only those regions change and all surrounding hand-written text is preserved
   character for character.
2. **Given** no changes since the previous run, **When** the refresh runs again, **Then** the
   documentation files are unchanged.
3. **Given** a protected region has been deleted or duplicated by a manual edit, **When** the
   refresh runs, **Then** it stops, reports the specific file and problem, and writes nothing.
4. **Given** a workspace holding at least two hundred directories, **When** the refresh runs,
   **Then** it completes in under two seconds and reports success.
5. **Given** a verification run with no write intent, **When** the documented inventory
   disagrees with the filesystem, **Then** the run reports the drift and signals failure
   without modifying anything.
6. **Given** a credential-looking value has been pasted into documentation, **When** the
   refresh runs, **Then** it flags the file and location without printing the value itself.

---

### Edge Cases

- **Empty placeholder folders**: They must exist and must be described in the architecture
  document, but they must be counted separately from populated areas and must never be deleted
  by a refresh.
- **Workspace path with a space**: Every internal reference must resolve without requiring
  angle-bracket or escape conventions from the reader.
- **Missing, duplicated, or reordered protected regions**: The refresh aborts with a precise
  message and leaves all files untouched.
- **Files changing during a scan**: Each run reads one consistent snapshot; a partially written
  inventory must never be left behind, and a re-run must always be safe.
- **Tooling and hidden areas** (version control, editor state, agent tooling, dependency caches,
  interpreter caches): Excluded from inventory counts, because they are not part of the
  ecosystem the Commander governs.
- **Archive domain**: Present and counted as a domain, but excluded from active-work metrics
  because nothing there is in flight.
- **Deep nesting**: Nesting depth is limited to what the roadmap defines; the refresh must fail
  loudly on paths that exceed platform limits rather than silently truncating a name.
- **Unreadable, locked, or oddly encoded files**: Skipped with a warning; the refresh must
  never crash because of one bad file.
- **Concurrent refreshes**: A single writer is enforced, so two runs cannot interleave writes.
- **Placeholder feature folders**: Folders whose specification is still a stub count as
  reserved feature slots and are counted as distinct features, not as finished work.
- **Root-level documents edited by hand while a refresh is pending**: The next refresh
  reports the conflict instead of discarding the human edit.
- **A pod that is copied out of the workspace**: Its documentation references must still resolve
  inside the copy, so no reference may depend on a sibling pod or on the global root.
- **Pre-existing worker seats**: Cards quarantined to the archive must remain byte-identical,
  keep their role identifiers, and appear in the manifest, so a later phase can restore one
  seat without archaeology or guessing.
- **Stale pre-existing telemetry**: Figures written before the refresh exists are unverified.
  They must be regenerated from the filesystem, and any material discrepancy must be recorded in
  the genesis draft instead of being silently overwritten.

## Requirements *(mandatory)*

### Functional Requirements

**Structure and naming**

- **FR-001**: The workspace root MUST contain seven numbered domains - global system,
  templates, personal pillars, commercial ventures, infrastructure, dashboard, and archive -
  alongside the specification area and the tooling area that already exist.
- **FR-002**: The global system domain MUST contain its documented sub-areas: directives,
  memory layer, queue vault, master task engine, agent registry, learning loop, tool-server
  registry, plugins and integrations, hooks and guardrails, skills, reference library, and
  scripts.
- **FR-003**: The templates domain MUST contain a blueprint for a standalone venture pod, a
  standalone pillar pod, a department module, a research team, an agent card, and a skill
  bundle.
- **FR-004**: The pillars domain MUST contain all five pillar pods (health and growth,
  spiritual, clinical and learning, personal branding, personal finance), each with its outer
  shell locations, its pod core, its lead seat, its four capability areas, and its shared
  sub-areas.
- **FR-005**: The ventures domain MUST contain both venture pods (medicophilia and
  travelophilia), each with its outer shell locations, its pod core, its six executive seats,
  its seven department folders, and the shared sub-areas named for each department.
- **FR-006**: The infrastructure domain MUST contain the executive command seats, the café
  area, the channels bridge with its three bridges, and the brain bindings area.
- **FR-007**: The dashboard domain and the archive domain MUST exist with their documented
  sub-areas.
- **FR-008**: Directory and canonical file names MUST follow one naming law: numbered
  prefixes where the roadmap specifies them, lowercase underscore-separated words otherwise,
  no spaces, and no renaming of any name given in the roadmap.
- **FR-009**: Materializing the skeleton MUST be repeatable without destruction: a second run
  creates only what is missing and never deletes, renames, or overwrites existing content.
- **FR-010**: Every directory the foundation creates MUST be described in the architecture
  document, including directories that remain empty until a later phase.
- **FR-011**: The foundation MUST NOT create any filesystem link, shortcut, or reference that
  makes one pod depend on another pod, because that would break the detachability guarantee
  before any pod content exists.

**Documentation**

- **FR-012**: A quick-start portal document MUST exist at the workspace root and MUST state the
  purpose of the ecosystem, the domain map, where to begin each phase, how to run the
  documentation refresh, and where the governing law lives.
- **FR-013**: An architecture document MUST exist at the workspace root and MUST explain every
  domain, every nested directory, and every foundation governance file from macro to micro,
  naming the purpose, the owning role, and the prohibited contents for each.
- **FR-014**: The architecture document MUST contain protected generated regions with the exact
  start and end markers `<!-- AUTO-STATS-START -->` and `<!-- AUTO-STATS-END -->`, and MUST
  carry its generated figures only inside those regions.
- **FR-015**: A genesis and discussions document MUST exist at the workspace root, MUST record
  the intellectual history and the rejected alternatives behind the architecture, and MUST be
  marked as a draft that is superseded by the constitution where they disagree.
- **FR-016**: A root entry document MUST exist for agent hosts and MUST define boot order, the
  mandatory reading list, the authority chain, and a pointer to the constitution, using wording
  that names no agent product, editor, or vendor.
- **FR-017**: The workspace MUST include a secrets-hygiene setup: an environment template that
  documents required variables with empty values, and an ignore configuration that excludes
  secrets, local databases, queue files, caches, and editor state from versioned history.
- **FR-018**: No documentation file MAY contain a credential, token, key, or personal
  identifier value; environment placeholders MUST be empty or obviously synthetic.
- **FR-019**: Internal references within documentation MUST be expressed relative to the
  referencing document so that a copied pod remains self-consistent, and the workspace root
  path MAY appear absolute only once, in the quick-start portal.

**Directives**

- **FR-020**: A directives area MUST contain exactly three governance documents: cognitive DNA
  and voice rules, global governance rules, and the detachability standard.
- **FR-021**: Each directive MUST name the roles and levels it binds and MUST cite the
  constitutional principle it operationalizes.
- **FR-022**: Directives MUST be plain text with no runtime-, editor-, or vendor-specific
  instruction, so that any agent host can consume them unchanged.

**Living inventory refresh**

- **FR-023**: A single documented action MUST recompute the living inventory from filesystem
  truth: active areas, empty placeholders, agent cards, skill bundles, specification features,
  and per-domain counts.
- **FR-024**: The refresh MUST write only inside protected generated regions and MUST preserve
  all content outside those regions exactly.
- **FR-025**: The refresh MUST produce deterministic output: identical inputs yield identical
  files, with a documented, stable ordering for every list and table it generates.
- **FR-026**: The refresh MUST be idempotent: running it twice with no intervening change leaves
  the documentation unchanged.
- **FR-027**: The refresh MUST fail closed: on a missing, duplicated, or malformed protected
  region, an unresolvable workspace root, or a concurrent writer, it reports the exact problem,
  modifies nothing, and signals failure.
- **FR-028**: The refresh MUST offer a verification mode that reports disagreement between the
  documented inventory and the filesystem without writing, suitable for use before a phase gate
  or a commit.
- **FR-029**: The refresh MUST exclude tooling, hidden, and cache areas from inventory counts,
  MUST count empty placeholders separately, and MUST exclude the archive domain from active-work
  counts.
- **FR-030**: The refresh MUST stay inside the workspace root, MUST NOT follow links that lead
  outside it, and MUST NOT read or modify the governing law, specification content, agent
  cards, or pod state.
- **FR-031**: The inventory document MUST be generated, MUST carry a header stating that it is
  machine-generated and must not be hand-edited, and MUST list each domain's path, purpose, and
  owning role.
- **FR-032**: The refresh MUST flag files containing credential-like values by path and
  location without reproducing the value.

**Pre-seeded state reconciliation**

- **FR-033**: Every per-worker card directory that exists under the pillars or ventures
  domain before the baseline is delivered MUST be relocated into the archive domain, and the
  relocation MUST produce a manifest recording the original path, the role identifier, and the
  archive path for each quarantined seat.
- **FR-034**: Quarantine MUST be lossless and reversible: archived seats retain their complete
  original content, and the manifest alone is sufficient to restore any single seat or to
  regenerate it during a later phase.
- **FR-035**: After quarantine, live pod trees MUST retain only the outer shell, the pod core,
  the leadership seat, and the manager seats. No worker-level card directory may remain outside
  the archive domain.
- **FR-036**: Quarantined seats MUST be excluded from active inventory counts and reported
  separately, and the manifest MUST be the sole authority for what was quarantined.
- **FR-037**: The foundation MUST establish a documentation guardian as the sixth global
  executive seat inside the infrastructure executive command area, reporting to the prime
  interface, and MUST seed its agent card in the same baseline as the other executive seats.
- **FR-038**: The documentation guardian MUST be the single accountable owner of the generated
  inventory, the architecture telemetry block, and drift verification. No other role may write
  those regions, and the architecture document MUST name this owner for each generated region.
- **FR-039**: The pod core contract MUST use one canonical set of names taken from the
  detachability standard: `local_review_approvals.md`, `runtime_adapter.yaml`,
  `pod_agents_directory.md`, `pod_scorecard_points.md`, and `pod_blockers.md`. The roadmap's
  `venture_*` names and the architecture document's `local_plugins.yaml` are superseded and MUST
  NOT be documented as alternatives.

### Key Entities *(include if feature involves data)*

- **Domain**: A numbered top-level area of the ecosystem. Attributes: number, name, path,
  purpose, owning executive role, active or archived status.
- **Directory Node**: A folder in the federated tree. Attributes: path, parent, domain,
  documented purpose, owning role, occupancy state (empty placeholder, scaffolded, populated),
  child count. Relationships: a domain contains many nodes; a pod subtree is self-contained.
- **Documentation Artifact**: A governed document. Attributes: path, audience, owner, whether it
  contains protected regions, last refresh timestamp. Relationships: the architecture document
  owns the catalog of nodes; the inventory document owns generated counts.
- **Protected Region**: A writable slice inside a documentation artifact. Attributes: start
  marker, end marker, owning generator, allowed content type.
- **Directive**: A binding rule document. Attributes: name, bound roles, referenced
  constitutional principle, authority level.
- **Inventory Snapshot**: The counted state of the ecosystem at one point in time. Attributes:
  timestamp, active area count, placeholder count, agent card count, skill bundle count,
  feature count, per-domain breakdown.
- **Specification Feature**: A reserved work slot under the specification area, identified by
  its numbered folder and short name, holding a specification, a plan, and a task list.
- **Role Seat**: An occupied position in the authority tree. Attributes: role identifier, level,
  supervisor, pod or domain scope, card path, owned generated artifacts. Relationships: every
  seat reports to exactly one supervising seat, and every generated region has exactly one
  owning seat.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of the directory paths named in the project roadmap exist after the
  foundation is in place, with zero missing and zero undocumented additions.
- **SC-002**: A reader who has never seen the repository answers 10 of 10 placement questions
  correctly using only the root documentation.
- **SC-003**: The documentation refresh completes in under 2 seconds on a workspace containing
  at least 200 directories, reporting success.
- **SC-004**: Two consecutive refreshes with no intervening change produce identical output,
  with zero changed characters.
- **SC-005**: Hand-written prose is preserved across refreshes with zero characters altered
  outside protected regions.
- **SC-006**: Zero broken internal references exist across the root documentation, including
  references from a path containing a space.
- **SC-007**: Inventory counts match an independent manual audit exactly - zero deviation for
  active areas, placeholders, agent cards, skill bundles, and features.
- **SC-008**: Zero credential-like values are present in versioned documentation.
- **SC-009**: A verification run detects 100% of injected drift cases (five deliberately
  introduced mismatches) and signals failure for each.
- **SC-010**: A reader reaches both the governing law and the binding directives from the
  quick-start portal in no more than two navigation steps.
- **SC-011**: All five pillar pods and both venture pods expose their outer shell, their pod
  core, their leadership seats, and their capability or department folders, so the later pod
  phases begin with zero folder creation.
- **SC-012**: A new collaborator can state the correct destination for a new document on their
  first attempt in 100% of sampled cases without asking the Commander.
- **SC-013**: After the baseline is delivered, zero worker-level card directories remain outside
  the archive domain, and the quarantine manifest maps 100% of relocated seats from original
  path to archive path with their role identifiers intact.
- **SC-014**: Every generated region has exactly one named owning role, that role has a seeded
  card in the baseline, and zero generated regions are unowned.
- **SC-015**: The delivered architecture document names pod core artifacts using exactly one
  contract, with zero occurrences of a superseded name.

## Assumptions

- **Scope boundary**: This phase delivers structure, foundational documentation, directives, and
  the documentation refresh only. It delivers no functional engine, no scoring, no memory or
  queue behavior, no dashboard, and no tool-server wiring; those belong to later phases. Agent
  card content is limited to the documentation guardian's seeded card, because pre-existing cards
  are retained or quarantined rather than authored here.
- **Depth decision**: Every path the roadmap shows as a directory is materialized - outer shell
  locations, pod cores, executive seats, department folders, capability areas, and the shared
  sub-areas named per department. Individual per-worker folders are deliberately not part of the
  delivered baseline. Worker seats that already existed before this phase are quarantined to the
  archive under FR-033 to FR-036, preserving their role identifiers and content so Phases 5 and 6
  can restore or regenerate them from templates. Adding physical worker seats back into the live
  pod trees would be an amendment to this phase.
- **Placeholders stay empty**: Foundation folders that a later phase populates ship empty and
  are described in the architecture document rather than filled with speculative content.
- **Host environment**: The workspace is hosted on a Windows machine whose path contains a
  space; the filesystem is case-insensitive; names are kept within platform path limits.
- **Single writer**: Only one documentation refresh runs at a time; the refresh enforces this
  rather than relying on operator discipline.
- **Version control is optional**: The foundation does not require a repository, a branch, or a
  commit convention to succeed.
- **Implementation is governed elsewhere**: Language, runtime, and tooling choices are fixed by
  the ratified constitution and are outside this specification's scope; this document fixes
  behavior and boundaries only.
- **Language**: All documentation is written in English with no localization in this version.
- **Precedence**: The ratified constitution governs. Where the roadmap and the constitution
  disagree - for example on how many outer-shell files a pod must carry - the constitution wins
  and the roadmap is read as a target, not a law.
- **Governing inputs**: The constitution, the three directives, and the architecture document are
  authoritative inputs to this feature. Where the roadmap disagrees with them, the roadmap yields.
- **Canonical pod-core naming**: Where governing documents disagree about pod core file names,
  the detachability standard wins. Superseded names are corrected on the next revision of the
  affected document and are not preserved as alternatives.
- **Counts come from the filesystem**: No human enters inventory numbers; every figure is
  derived, which is what makes staleness detectable.
- **Existing placeholder feature folders**: The specification folders already reserved for the
  eight phases are treated as feature slots and counted as such, not as completed work.
- **Pod copies**: Because references are relative, copying any pod folder elsewhere must leave
  its documentation resolvable without edits.
