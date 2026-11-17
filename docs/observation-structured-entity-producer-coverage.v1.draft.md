# Structured Entity Producer Coverage Matrix v1 — Draft

**Status:** source-backed partial coverage; not runtime-approved.  
**Related audit:** [#346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).  
**Canonical branch:** `new-arquiteture`.

## Purpose and boundary

This matrix joins the 17 entity kinds in the structured-entity temporal contract to the producer facts established by the source audit. It records field-family availability, identity/scope, ownership/cardinality, completeness, provenance/formula, sequence, lifecycle/reset, Python exposure and actual PPO delivery.

The CSV is deliberately a separate artifact so it can be consumed by scripts or spreadsheet tooling without treating a schema declaration as runtime evidence. Each row is one audited entity field family; multiple rows for one entity preserve distinct semantics (for example, catalog trait membership versus derived active-trait counts).

- [Machine-readable CSV coverage matrix](../spec/observation-structured-entity-producer-coverage.v1.draft.csv)
- [Structured entity temporal contract](../spec/observation-structured-entity-temporal-contract.v1.draft.json)
- [Schema v2 draft](../spec/observation-schema.v2.draft.json)
- [Source-to-PPO binding audit](observation-producer-binding-audit.v1.draft.md)
- [Structured entity producer evidence audit](observation-structured-entity-producer-audit.v1.draft.md)

## Inventory

- 17 entity kinds covered.
- 31 field-family rows.
- 15 columns per row.
- All rows distinguish native availability from Python diagnostic exposure and PPO delivery.
- No row implies that structured entity records are currently delivered to PPO merely because a diagnostic snapshot or flat numeric feature exists.

## High-impact reconciliations

| Entity family | Source-backed status | Current Python/PPO boundary | Blocking issue |
|---|---|---|---|
| Unit instance | UUID is generated, but is not canonical cross-episode identity | Identity-bound native sidecar is preserved in per-player rollout metadata; not an Actor/Critic tensor | Seed reset repeats UUID; no global collision registry or formal lifecycle guarantee |
| Board/bench slots | Fixed 28/9 slot arrays and occupancy are native | Exact 28/9 slot records now travel in the native sidecar and rollout metadata; PPO still consumes flat features | No canonical hex geometry/orientation; no structured Actor/Critic projection |
| Shop offer | Five fixed offers and reroll/purchase lifecycle are native | Five slot records travel in the native sidecar and rollout metadata | No stable offer ID/revision/reroll generation; UnitInstance UUID is not offer identity |
| Pool availability | `UnitPool::available()` is an authoritative shared-lobby per-champion count query | Direct pybind query only; not in wrapper observation or PPO vector | No immutable decision-correlated pool snapshot or source sequence |
| Item instance | No physical item-instance object or ID; catalog IDs and multiplicity only | Equipped catalog IDs are carried beside unit records; bag/component catalog IDs are carried in player sidecar | No per-copy identity, typed owner relation or item event sequence |
| Component inventory | Native aggregate/multiplicity exists | Catalog IDs/multiplicity travel in the sidecar and remain aggregate PPO features | No component instance identity/acquisition sequence |
| Anvil option | ItemEngine queue API exists, but audited gameplay reward path does not produce it | Existing pending options are preserved in the sidecar when present | No authoritative gameplay producer, stable anvil/option IDs or decision sequence |
| Trait | Catalog membership and several derived count scopes exist | Fixed numeric trait features only | PPO and strategic counts differ; no typed trait records/catalog fingerprint |
| Position | Internal 4×7 slot mapping and read-only Shadow proposal exist | Aggregate positioning features; proposal diagnostic | No canonical hex semantics or physical UUID join |
| Unit assessment | Shadow-only heuristic assessment | Diagnostic/Shadow only; no structured PPO delivery | Champion-keyed/per-slot records lack physical UUID and formula provenance |
| Anchor candidate | Shadow-only generated composition/direction/pivot candidates | Diagnostic only; not PPO | No stable candidate ID/revision or complete candidate-set envelope |
| Action opportunity | No populated authoritative candidate set in audited path | Not delivered | Empty source vector is not a comparison or HOLD |
| Temporal decision history | Flat action-memory scalars are native and delivered | Flat PPO features | No typed ordered history or decision sequence |
| Anti-loop history | Ordered records remain internal native state | Python exposes aggregate metrics only; no PPO entity | No record-level sequence identity or Python delivery |

## Status interpretation

The CSV uses the status vocabulary required by #346:

- `native_observed`: direct native state/catalog fact is produced.
- `native_derived`: a value is computed from native state; formula and scope remain material.
- `shadow_only`: exists in the Shadow strategic/proposal path, not as canonical PPO input.
- `diagnostic_only`: available only through diagnostic serialization/snapshot paths.
- `not_produced`: no authoritative producer was found in the audited path.
- `not_correlated`: value exists, but exact identity/sequence correlation is not established.
- `not_exposed_to_python`: native state exists but is not exposed through the audited Python binding.
- `unverified`: producer exists, but identity/lifecycle/scope is not accepted.

Delivery is recorded separately as `diagnostic_sidecar_to_python`, `flat_ppo_feature`, `not_delivered`, and related values. This prevents a native or diagnostic value from being described as PPO input.

## Known limitations and next audit work

PR #455 adds a versioned `native_state_snapshot` sidecar to ResetResult/StepResult and carries one player record into each corresponding rollout metadata row. This proves transport for the existing AuditPlayerSnapshot fields only; it does not mean the 17 entity kinds are fully produced or projected into Actor/Critic tensors. See [Native State Snapshot Contract v1](native-state-snapshot-contract.v1.draft.md).

This matrix is a coverage index, not proof that every field in every nested Schema v2 object has been individually traced. In particular, the next pass must enumerate all nested declared fields and reconcile them against the matrix; resolve the schema's required `instance_id`, `unit_instance_id`, and `candidate_id` assumptions against absent or unsafe native identities; and complete repository-wide callsite/test coverage for UUID lifecycle, source sequences, reset behavior and delivery.

The existing CSV is intentionally conservative. Where a field is declared in the schema but no authoritative producer exists, the row says unavailable/not produced rather than inventing a value.

## Architecture reconstruction review

1. **Prior problem:** the temporal contract listed entity kinds, but there was no single machine-readable artifact joining field families to native producer, identity, lifecycle, provenance, sequence, Python exposure and PPO delivery.
2. **Technical justification:** producer existence, diagnostic serialization and PPO tensor delivery are distinct facts. Combining them without explicit columns creates false availability claims.
3. **New responsibility:** this matrix is the audit index for producer-to-entity coverage; it does not own runtime production or choose the future tensor projection.
4. **Contract and invariants:** 17 entity kinds; field-family rows; explicit status and delivery vocabularies; no synthetic IDs; no alias assumptions; masks remain independent.
5. **Cross-component impacts:** Schema v2, temporal entity contract, Engine native state, ItemEngine, ShopEngine, strategic Shadow producers, pybind, Python wrapper, PPO observation/rollout, replay and checkpoint lineage.
6. **Objective validation:** CSV has 31 data rows and 15 columns; 17 unique entity kinds; all rows include source, availability, identity, ownership/cardinality, completeness/provenance, formula/version, sequence, lifecycle/reset, Python delivery, PPO delivery and unresolved gaps. Documentation/specification only; no runtime or tensor-layout changes.


## Schema v2 nested field crosswalk — 2026-11-15

The [Schema v2 Field-to-Source Crosswalk](observation-schema-v2-field-source-crosswalk.v1.draft.md) enumerates 223 data paths under entities, derived_context, strategic_evidence and legal_state_context against the 77-entry source map: 43 exact matches, 164 ancestor/family matches and 16 paths with no source-map entry. Parent/family matches are explicitly not treated as field-level proof; Python and PPO delivery remain unestablished by the source map.


## Unmapped field dispositions — 2026-11-15

The [Schema v2 Unmapped Field Dispositions](observation-schema-v2-unmapped-field-dispositions.v1.draft.md) classifies all 16 paths without a source-map match as not-produced, Shadow-only, diagnostic-only, unverified, not-correlated or static contract metadata. This classification supplements but does not rewrite the mechanical match result.


## Unit identity, shop and shared pool lifecycle follow-up — 2026-11-15

The [Unit Instance, Shop Offer and Shared Pool Lifecycle Follow-up](unit-instance-shop-pool-lifecycle-followup.v1.draft.md) refines the ownership lifecycle and corrects the pool-availability row. It traces shop → bench → board moves, merge identity retention/consumption, sale and elimination cleanup, same-seed reset UUID repetition, implicit value-copy behavior, and the direct TFTEngine/pybind pool-count query.

**Correction:** the previous matrix wording that no authoritative per-champion pool count producer existed was too broad. `UnitPool::available()` and `TFTEngine::pool_available()` provide authoritative native queries, and pybind exposes them. The count is still not part of the immutable observation snapshot or PPO vector, and has no decision-sequence correlation. The shared champion pool is lobby-scoped, not player-owned.


## PvE loot versus anvil producer boundary — 2026-11-15

The [PvE Loot and Anvil Gameplay Producer Boundary Audit](anvil-gameplay-producer-boundary-audit.v1.draft.md) corrects a possible overreading of the earlier anvil proof. The Engine has an authoritative round-resolution PvE producer that directly grants components and completed items through `add_component()` and `add_completed_item()`. It does not enqueue an anvil. A scan of the 12 `cpp/src` implementation translation units found no gameplay call to `grant_component_anvil()` or `grant_completed_item_anvil()`. Pending-anvil state, masks, option projection and the conditional consumer remain real, but no audited gameplay producer populates that queue. Direct catalog-ID grants do not establish physical item identity or typed PPO entity delivery.


## PvE component pool and inventory lifecycle — 2026-11-15

The [PvE Component Pool and Item Inventory Lifecycle Audit](pve-component-inventory-lifecycle-audit.v1.draft.md) separates the per-player, episode-local Set 18 loot distribution pool from collected component multiplicity in ItemEngine. The pool is not projected to PPO. PPO receives ten catalog-order component counts divided by six and clamped, plus nine positional semantic inventory slots; neither is a lossless physical-item or loot-provenance representation. The audit also traces recipe consumption, craft-and-equip rollback, equipment ownership and reset behavior, and records existing test coverage and gaps.


## Item action policy-to-native binding — 2026-11-15

The [Item Action Policy-to-Native Binding Audit](item-action-policy-native-binding-audit.v1.draft.md) records the type-specific meaning of the six-wide action vector for inventory equip, both anvil choice kinds, and craft-and-equip. It confirms type 7 is conditionally overloaded: a pending anvil makes action[1] an option index and action[2] a forced zero sentinel; otherwise they are inventory slot and target. Type 8 binds two component indices and a target. Item masks remain separate conditional legality inputs. Existing tests cover policy sampling/replay for anvil and crafting, while full native/Python round-trip correlation remains open.
