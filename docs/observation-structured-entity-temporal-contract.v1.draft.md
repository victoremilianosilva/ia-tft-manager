# Structured Entity and Temporal Evidence Contract v1 — Draft

**Status:** proposed semantic contract; not runtime-approved.
**Schema basis:** Observation Schema v2.
**Consumer basis:** Observation Projection Consumer Matrix v1.
**Machine-readable manifest:** `spec/observation-structured-entity-temporal-contract.v1.draft.json`.

## 1. Purpose

The consumer matrix identifies which semantic fields may be considered by Actor, Critic or control/diagnostic consumers. It does not yet guarantee that aggregate structures can be represented without losing physical identity, ownership, completeness, temporal scope or provenance.

This contract defines those semantics before tensor encoding. It intentionally does not select dimensions, offsets, padding, feature order, normalization, vocabularies or encoder families.

## 2. Core entity distinctions

- **Physical unit instance:** identified by `instance_id`, scoped to match/player and its lifecycle. It is not identified by champion ID or board slot.
- **Champion catalog entry:** identified by `champion_id` plus catalog fingerprint. It is a grouping key, not an owned copy.
- **Board/bench slot:** stable slot identity within its domain and snapshot. Occupied, empty, unknown, stale and incompatible are distinct.
- **Shop offer:** a temporary opportunity scoped to the exact shop snapshot/slot. It is not a physical owned unit and must not reuse unit-instance identity.
- **Pool availability:** a separate shared-pool domain. No local board/bench/shop count may be used to infer it.
- **Item instance:** physical identity distinct from item catalog ID. Current schema does not yet provide enough identity to guarantee lossless attachment/inventory mapping.
- **Component inventory:** current schema is an aggregate count by component ID, not a set of physical component instances.
- **Anvil option:** explicit pending-choice record with option identity; it is not a catalog index or an already-owned item.
- **Trait:** catalog identity and observed unit membership are distinct from derived active counts, completed traits, core traits and focus weights.
- **Position:** spatial evidence bound to a physical unit instance or explicitly empty slot and exact board snapshot.
- **Unit assessment / anchor candidate:** derived evidence records, never observed facts, commands or accepted transitions.
- **Action opportunity:** decision-local candidate record; withheld until a complete authoritative producer exists.
- **Temporal history:** sequence-bound descriptive context, never a legality mask.

## 3. Identity and ownership rules

| Entity | Identity | Scope | Domain |
|---|---|---|---|
| Unit instance | `instance_id` | match + player | board or bench |
| Champion entry | `champion_id` | catalog fingerprint | catalog |
| Board slot | `slot_index` | match + player + board + snapshot | board |
| Bench slot | `slot_index` | match + player + bench + snapshot | bench |
| Shop offer | snapshot + slot + offer revision | exact shop snapshot | shop opportunity |
| Pool availability | champion + catalog + source sequence | shared pool | shared pool |
| Item instance | future `item_instance_id` | match + player + owner | inventory or attachment |
| Component aggregate | `component_id` | match + player + catalog | inventory aggregate |
| Anvil option | `option_id` | pending decision sequence | pending choice |
| Anchor candidate | `candidate_id` | match + player + direction/composition + sequence | strategic candidate |
| Action candidate | `candidate_id` | match + player + decision + candidate-set ID | decision opportunity |

The machine-readable manifest defines relationships, cardinalities, sequence scopes and gaps for every entity family.

## 4. Collection completeness and missingness

- `complete`: producer attests all members in the declared scope were observed at this exact sequence.
- `partial`: some members are known, but completeness is not guaranteed.
- `empty`: complete collection with zero members, explicitly observed.
- `unknown`: producer cannot determine membership or completeness.
- `missing`: source did not supply the collection.
- `stale`: collection belongs to an earlier source sequence.
- `incompatible`: schema/catalog/identity cannot be consumed safely.
- `not_applicable`: collection does not apply in this phase/state.

An absent array is not automatically a complete empty collection. A partial shop is not a complete shop. Child values do not prove that a parent candidate set exists.

## 5. Unit, shop and item invariants

1. A physical unit has one stable instance identity across board/bench movement; its slot is a relationship that changes by snapshot.
2. Multiple units with the same champion ID remain distinct physical copies; upgrade progress derives from exact instances and star tiers.
3. Shop offers are not owned copies. Offer identity expires with shop snapshot/reroll generation.
4. Board, bench, shop and pool remain separate domains.
5. Inventory item catalog ID does not prove physical item-instance identity. Attached item strings do not prove an exact attachment relationship.
6. Components represented as counts are aggregates; do not invent per-component instance IDs.
7. Anvil options retain explicit option identity, kind, catalog identity and target-fit provenance.

## 6. Derived and estimated evidence

Every derived/estimated field must retain nature, producer, exact source path, source sequence, match/player identity, formula ID/version, input paths, unit, validity/missingness, input completeness and quality/uncertainty where estimated.

Observed facts require direct source evidence. Heuristic `item_fit`, `board_contribution`, `composition_fit`, `anchor_value`, candidate transition cost and target-fit scores must not become factual scalars through projection. Uncalibrated estimates remain diagnostic or unavailable.

## 7. Strategic and candidate semantics

- Direction, active composition, anchor, focus, core traits, completed traits, progression and lock remain distinct.
- An anchor candidate is a proposal with evidence and identity, not a confirmed pivot or active composition.
- Candidate-set state must distinguish ready, partial, empty, stale, invalid and unavailable.
- The current action-opportunity producer gap remains blocking. Do not project candidate rows until complete set, exact physical parameters, costs, availability and source decision sequence are supplied.
- Shadow recommendations, evaluator scores, baseline outputs, executor resolutions and diagnostic Unified Shadow snapshots remain excluded from PPO inputs and targets.

## 8. Spatial and temporal semantics

Positioning must bind to board slots/physical instances and preserve coordinate system, orientation, row/column/front-back meaning and empty/unknown cells. Candidate unit lists cannot substitute for selected board layout.

Every temporal collection binds to match, player, round/episode and exact source decision/snapshot sequence. Decision-local history resets at the declared episode boundary. Stale or cross-sequence data is rejected or explicitly marked stale; there is no latest-value fallback. Anti-loop history is context only and never overrides exact Engine masks.

## 9. Current schema gaps requiring explicit follow-up

1. Shop schema has no explicit offer ID/revision/reroll generation or observed price field.
2. Inventory and unit attachments lack physical item-instance identity and explicit attachment owner references.
3. Pool availability has no authoritative producer/schema field.
4. Board slot index has no documented coordinate/orientation contract.
5. Positioning and trait aggregates use open maps without complete typed key/catalog contracts.
6. Unit assessments and anchor candidates need explicit collection completeness and source-sequence contracts.
7. Action-opportunity candidates have no populated authoritative producer.

These are not permission to fabricate fields. They require source audit and, where justified, a versioned schema revision before runtime projection.

## 10. Architecture reconstruction review

1. **Prior problem:** the semantic matrix classifies broad fields, but aggregate objects/arrays can still hide lossy flattening, ambiguous identity, ordering and completeness.
2. **Technical rationale:** policy learning must distinguish physical entities, ownership, opportunities and temporal evidence; flattening before these semantics are stable can erase information or leak incidental order.
3. **New responsibility:** this contract owns record granularity, identity, relationships, ordering and completeness; Schema v2 owns field/provenance contracts; producers own evidence; future projection owns tensor encoding.
4. **Contracts/invariants:** physical identity, separate ownership domains, typed missingness, stable ordering, exact temporal correlation, no fabricated facts, no Shadow imitation, no mask substitution.
5. **Cross-component impact:** Schema v2, consumer matrix, native producers, strategic/economic owners, Engine→Python binding, Actor/Critic projection, checkpoint lineage, replay and evaluation.
6. **Objective validation:** every structured field maps to an entity/relationship or explicit gap; identities are scoped; collection completeness is typed; derived fields retain provenance; schema gaps are listed.

**Gate status:** documentary proposal only. Gate 1 and Gate 4 remain open. Gate 8 and explicit authorization remain required before runtime implementation.
