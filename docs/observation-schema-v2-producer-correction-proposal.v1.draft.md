# Observation Schema v2 — Producer Reconciliation and Correction Proposal v1 (Draft)

**Status:** documentary correction proposal; not runtime-approved and not a tensor-layout decision.  
**Base:** `new-arquiteture`, after PR #353.  
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).

## 1. Purpose

The v2 schema contains required identities and structured records that the current Engine either does not produce, produces only as Shadow/diagnostic data, or cannot correlate safely. This proposal records the mismatches and the minimum contract correction needed to prevent a future adapter from fabricating IDs or marking unsupported entities as available.

This proposal does **not** change the schema in place yet. It first establishes which requirements are target requirements versus currently producible data. Any eventual schema revision must preserve the distinction between a valid future contract and the current runtime's capabilities.

The expanded [producer coverage CSV](../spec/observation-structured-entity-producer-coverage.v1.draft.csv) now includes 31 field-family rows, including the schema-required identity references below.

## 2. Critical schema-to-producer mismatches

| Schema path / required field | Declared requirement | Source-backed producer finding | Current disposition | Required correction |
|---|---|---|---|---|
| `$defs/unit.instance_id` | Required non-empty string for every occupied unit | Native field is `UnitInstance::uuid`; seeded RNG restarts on reset and repeats UUID with same seed; no match/player namespace or collision registry | `unverified` | Do not alias UUID directly. Define a scoped identity envelope and prove engine-match/player scope and reset uniqueness before the field can be populated |
| `$defs/unitAssessment.unit_instance_id` | Required physical unit reference | StrategicSharedContext assessments omit UUID and slot; UnitPrioritySnapshot aggregates by champion | `not_produced` | Assessment collection must carry a proven physical identity; until then parent collection must be explicitly unavailable, not populated with champion IDs |
| `$defs/anchorCandidate.candidate_id` | Required stable candidate identity | StrategicAnchorCandidate has no candidate ID/revision or candidate-set ID | `not_produced` | Require candidate ID, revision, parent set identity and completeness only when producer emits them; never derive ID from composition identity alone |
| `$defs/anchorCandidate.anchor_unit_id`, `candidate_unit_ids`, `main_carry_id` | Names imply unit references | Native candidates carry champion/catalog IDs, not physical UnitInstance references | `native_derived`, champion-level | Rename to champion references or add an explicit reference-kind discriminator; do not imply physical instance identity |
| `$defs/actionOpportunityCandidate.candidate_id/action_kind/available` | Required candidate record | Audited TftEngine path leaves StrategicSharedContext::action_candidates empty | `not_produced` | Parent collection must carry status/reason; an empty/unavailable set is not a valid comparison or HOLD; do not emit child records without an authoritative producer |
| `entities.items.anvil_options[].option_id` | Required stable option ID | ItemEngine API stores catalog IDs and selects by positional index; audited gameplay reward path does not call anvil grant methods | `not_produced` | Do not synthesize option ID from array index; require a gameplay producer, stable anvil identity and pending-decision sequence |
| `anvil_options[].target_fits[].target_instance_id` | Required physical target reference | No audited gameplay anvil producer; current item-fit features do not prove a stable physical-unit relation | `not_produced` | Withhold target fits until option producer, physical target identity and fit provenance are established |
| `derived_context.unit_roles[].instance_id` | Required physical unit reference | Current audit does not establish a UUID-linked role collection producer | `unverified` | Trace producer and prove physical identity/snapshot correlation; otherwise collection is unavailable |
| `derived_context.item_target_fit[].target_instance_id` | Required physical target reference | Existing ItemFitCache/observation values are heuristic target-fit features; a typed UUID-linked relation is not established | `unverified` | Preserve heuristic nature/formula/version and exact target identity; no champion/slot alias |
| `derived_context.decision_history.source_decision_sequence` | Typed decision sequence field | PPO receives normalized action-memory count and board-slot ages, not per-event history or source decision ID | `not_produced` | Do not infer sequence from round or observation order; require an authoritative decision-sequence producer |
| `legal_state_context.anti_loop_state.*[].decision_sequence` | Per-record sequence fields in target schema | Internal AntiLoopHistory records have round/slot data but no match/player/decision-sequence identity; ordered records are not exposed to Python | `not_correlated` / `not_exposed_to_python` | Keep records native-only; do not serialize fake sequence metadata; any future exposure needs explicit scope, sequence and reset contract |

## 3. Specific contract recommendations

### 3.1 Physical unit identity

Keep the concept of a physical unit identity, but do not equate it with the raw UUID. The raw UUID is a native identity component whose generation is deterministic from a seeded RNG and repeats after reset when the same seed is reused.

A future accepted identity must include an episode/match and player scope, with a producer guarantee that the scope is unique for the lifetime of the observation/replay lineage. The current `identity.engine_match_id` field cannot be assumed sufficient until its generation, reset behavior and uniqueness are audited.

Until then:
- occupied unit records cannot claim a globally/cross-episode-safe `instance_id`;
- champion ID and slot index remain separate keys;
- unit-assessment, unit-role and item-target-fit records requiring physical references remain withheld/unavailable.

### 3.2 Status-bearing collections

For entity collections whose producers are absent or incomplete (unit assessments, anchor candidates, action opportunities, anvil options, typed decision history), the parent collection needs an explicit status/reason/completeness envelope. A plain empty array must not ambiguously mean both "validly observed zero candidates" and "producer unavailable".

Required distinctions include:
- producer not present;
- producer present but no candidates;
- partial/incomplete candidate set;
- stale or incompatible source snapshot;
- complete non-empty set.

This is a contract recommendation only; no collection wrapper is implemented here.

### 3.3 Candidate identity and reference semantics

- Candidate IDs are not composition IDs, direction IDs, champion IDs or parent sequence values.
- Candidate sets need their own stable identity/revision and completeness.
- Candidate records must declare whether references identify champion catalog entries or physical unit instances.
- Shadow anchor candidates, direction hypotheses, active direction anchors and pivot candidates remain distinct semantic families.
- Strategic action candidates remain separate from composition/anchor candidates.

### 3.4 Position, traits and item relations

- The current board uses a 4×7 internal rectangular slot convention; canonical TFT hex coordinates, orientation and enemy-facing semantics are not proven.
- Catalog trait membership, board+bench PPO trait counts, item-adjusted active board traits, core traits and completed trait milestones are different values with different scopes.
- Item and component catalog IDs/multiplicity do not create physical item/component identity.
- Item-fit scores are heuristic and must carry formula/version/uncertainty; target references require physical unit identity.

### 3.5 Temporal and legality separation

- Flat action-memory scalars are not a structured decision history.
- AntiLoopHistory remains internal; its aggregate metrics do not represent ordered history records.
- Native anti-loop validation may affect masks, but history must never replace or weaken the exact identity-correlated action masks.
- The Critic-only history classification remains future consumer intent, not current PPO delivery.

## 4. What this proposal does not authorize

- No runtime producer, adapter, schema serializer or binding changes.
- No tensor dimensions, shapes, offsets, normalization, ordering or encoder decisions.
- No PPO, rewards, masks, training, checkpoints, Viewer, Overwolf or historical artifact changes.
- No claim that the current v2 schema is a runtime-valid payload schema for all 17 entities.

## 5. Remaining source proof

Before finalizing a versioned schema correction:
1. Audit generation, uniqueness, reset and scope of `engine_match_id` and every sequence namespace; raw UnitInstance UUID repetition on same-seed reset is already confirmed.
2. Use the [Unit Instance, Shop Offer and Shared Pool Lifecycle Follow-up](unit-instance-shop-pool-lifecycle-followup.v1.draft.md) as the current source-backed lifecycle baseline; use the completed Python (125-file) and C++ (127-file) explicit-reference inventories as call-site baselines; finish implicit C++ value-copy/assignment/destruction lifecycle proof, identity scope/collision policy and elimination equipment-cleanup proof before accepting a canonical identity.
3. Trace unit-role and item-target-fit producers to exact source records and physical identity.
4. Trace every schema-required identity reference to a producer, including candidate and anvil records.
5. Reconcile all 254 semantic leaf paths (including nested field wrappers) against producer/source-map evidence; distinguish semantic values from common status/provenance metadata.
6. Verify diagnostic sidecar, Python binding, trainer observation and PPO rollout delivery independently.

## 6. Architecture reconstruction review

1. **Prior problem:** Schema v2 required instance and candidate identifiers that current producers do not safely emit; some field names also implied physical unit references while native candidates use champion/catalog IDs.
2. **Technical justification:** false identity aliases break ownership, replay joins, stale detection and candidate comparison; a valid target schema must not be confused with current producer capability.
3. **New responsibility:** this proposal owns the producer-to-schema correction recommendations; the native producer audit remains authority for current capability.
4. **Contract/invariants:** no synthetic IDs; no UUID alias without scope proof; no champion/slot substitute; unavailable collections carry explicit status; exact masks remain independent.
5. **Cross-component impacts:** Schema v2, temporal entity contract, UnitInstanceFactory, strategic evidence, composition candidates, ItemEngine/anvil, positioning/item-fit, AntiLoopHistory, pybind, Python wrapper, PPO, replay and checkpoint lineage.
6. **Objective validation:** all 11 schema mismatch rows are linked to source-backed findings; the CSV retains 17 unique entity kinds and 31 field-family rows; proposal is documentation-only and makes no runtime/tensor decisions.

Issue #346 remains open. This proposal is not acceptance of the structured entity audit.
