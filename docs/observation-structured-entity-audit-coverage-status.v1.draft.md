# Structured Entity Audit Coverage and Closure Status v1

**Status:** documentary coverage assessment; not an acceptance/closure decision.  
**Target:** new-arquiteture.  
**Tracking:** issue #346.  
**Source of field-level status:** spec/observation-structured-entity-producer-coverage.v1.draft.csv (31 rows, 17 unique entity kinds).

> This document consolidates where each structured entity family stands. “Audited” means a source-backed status/disposition is recorded; it does not mean the entity is fully available, canonical, correlated, or delivered to PPO.

## 1. Prior problem

The structured entity work is spread across producer audits, field proofs, lifecycle notes, identity/correlation audits and a machine-readable coverage CSV. The CSV already records 31 field-family rows across 17 entity kinds, but it is easy to mistake broad coverage for acceptance or to overlook that different rows within one entity kind can have different availability statuses.

This note creates one explicit closure view without upgrading any field's status.

## 2. Coverage summary

- **17** distinct entity kinds are represented in the producer coverage matrix.
- **31** field-family rows have explicit producer/status/delivery/gap dispositions.
- **125** tracked Python files have been inspected for identity and fixture-hook references.
- **127** tracked C++ files have been inspected for explicit UnitInstance/UUID/episode/test-hook references, including all 48 C++ test files.
- These inventories do not prove all missing producers exist, do not prove implicit C++ value-copy lifecycle acceptance, and do not establish end-to-end PPO delivery.

## 3. Entity-by-entity status

| Entity kind | Current evidence status | Principal source-backed evidence | Remaining acceptance gap |
|---|---|---|---|
| unit_instance | Native UUID exists; canonical cross-episode identity **unverified** | UnitInstanceFactory lifecycle, copy/test-hook audit, Engine reset/instance-scope audit, Python/C++ call-site inventories | Engine/player scope, collision policy, implicit copy/assignment/destruction proof, elimination cleanup, typed decision correlation |
| champion_catalog_entry | Native observed | ChampionCatalog and catalog-backed unit/trait audits | Stable catalog fingerprint and ordering contract in the entity envelope |
| board_slot | Native slot and occupancy observed | Structured entity producer audit; unit/item field proof; positioning audit | Canonical hex geometry/orientation/adjacency, exact source sequence, structured PPO entity delivery |
| bench_slot | Native slot and occupancy observed | Structured entity producer audit; unit/item field proof | Exact source sequence and structured PPO entity delivery |
| shop_offer | Native offer content observed; separate offer identity absent | Shop offer identity/reroll lifecycle audit; UnitInstance and pool lifecycle evidence | Stable offer ID/revision/generation and observation-mask-decision binding |
| pool_availability | Native shared-pool query observed | UnitPool producer audit and pool-availability correction | Immutable snapshot and exact decision correlation if the schema continues to require it; no current PPO feature |
| item_instance | Physical item-instance identity **not produced** | ItemEngine ownership, inventory-slot/action binding, elimination-item ownership audits | Physical per-copy ID, typed owner relation, item event sequence, lossless per-copy delivery |
| item_catalog_entry | Native catalog definition observed | Item catalog/schema/generator and item-fit field proof | Catalog fingerprint/order and typed catalog entity contract |
| component_inventory | Catalog IDs/multiplicity observed; physical identity not produced | PvE component inventory lifecycle and item inventory-slot/action audits | Physical component identity, acquisition sequence, catalog-order fingerprint |
| anvil_option | No gameplay producer in audited path; option identity not produced | Anvil gameplay producer-boundary audit; item action policy/native binding; item-fit/anvil proof | Actual gameplay grant producer, stable option IDs, complete option snapshot and sequence |
| trait | Catalog membership observed; counts/active/completed scopes derived; focus_weights new producer absent | Trait/position producer audit; derived-context exact source proof | Preserve board vs board+bench vs item-granted scopes; catalog/milestone formula versions |
| position | Native slot position observed; Shadow proposal diagnostic-only | Positioning producer audit; item-fit/anvil/role proof; derived-context proof | Canonical hex geometry and physical UUID references; lineup-to-executor replay proof |
| unit_assessment | Shadow-only assessment; schema-required physical reference not produced | Strategic evidence exact-source and owner-snapshot field proofs | UUID-backed identity, exact slot, formula/version/uncertainty and explicit collection status; no PPO delivery |
| anchor_candidate | Shadow candidate/derived champion references; stable candidate identity absent | Strategic evidence and owner-snapshot field proofs; composition/anchor contracts | Candidate ID/revision/set identity/completeness; distinguish champion references from physical instances |
| action_opportunity_candidate | Not produced | Action-opportunity/temporal field proof; Strategic Action Candidate Contract | Authoritative non-empty producer, exact action parameters, costs/benefits/horizon and truthful availability state |
| temporal_decision_history | Flat action-memory and board-age features derived; typed event history not produced | Action-opportunity/temporal field proof; AntiLoop history scope audit | Typed ordered events, source decision namespace, reset/stale semantics and Actor/Critic allocation |
| anti_loop_history | Native bounded records exist; not exposed to Python and not correlated to canonical decision identity | Decision AntiLoop history scope audit; wrapper/rollout correlation audit | Per-record identity/sequence, explicit scope/reset contract and approved delivery; masks remain separate |

## 4. Evidence index by audit family

### Identity and lifecycle
- docs/unit-instance-copy-test-hook-audit.v1.draft.md
- docs/unit-instance-shop-pool-lifecycle-followup.v1.draft.md
- docs/engine-episode-identity-reset-reconciliation.v1.draft.md
- docs/native-engine-instance-episode-identity-scope-audit.v1.draft.md
- docs/engine-identity-scope-reconciliation.v1.draft.md
- docs/python-identity-test-hook-callsite-inventory.v1.draft.md
- docs/cpp-identity-test-hook-caller-audit.v1.draft.md

### Board, bench, shop, pool, items and components
- docs/observation-structured-entity-producer-audit.v1.draft.md
- docs/observation-schema-v2-unit-item-field-proof.v1.draft.md
- docs/shop-offer-identity-reroll-lifecycle-audit.v1.draft.md
- docs/pve-component-inventory-lifecycle-audit.v1.draft.md
- docs/item-inventory-slot-action-binding-audit.v1.draft.md
- docs/item-action-policy-native-binding-audit.v1.draft.md
- docs/elimination-item-ownership-audit.v1.draft.md
- docs/anvil-gameplay-producer-boundary-audit.v1.draft.md

### Traits, positioning, strategic entities and temporal records
- docs/observation-schema-v2-derived-context-exact-source-proof.v1.draft.md
- docs/observation-schema-v2-item-fit-anvil-role-field-proof.v1.draft.md
- docs/observation-schema-v2-strategic-evidence-exact-source-proof.v1.draft.md
- docs/observation-schema-v2-strategic-owner-snapshot-field-proof.v1.draft.md
- docs/observation-schema-v2-action-opportunity-temporal-field-proof.v1.draft.md
- docs/decision-antiloop-history-scope-audit.v1.draft.md
- docs/observation-structured-entity-temporal-contract.v1.draft.md

### Delivery and replay
- docs/observation-producer-binding-audit.v1.draft.md
- docs/python-wrapper-rollout-decision-correlation-audit.v1.draft.md
- docs/python-lobby-vector-exception-and-episode-boundary-audit.v1.draft.md
- docs/python-lobby-vector-episode-boundary-test-coverage-audit.v1.draft.md
- docs/strategic-shadow-integrated-replay-contract.v1.draft.md
- docs/current-replay-correlation-evaluation-gap-audit.v1.draft.md

## 5. What is covered versus what is accepted

The current work establishes a useful but important distinction:

- **Field disposition coverage:** every one of the 31 CSV rows has a status and unresolved-gap description.
- **Source audit coverage:** the linked notes trace many producers and explicitly classify missing, diagnostic-only, Shadow-only, derived, uncorrelated and unexposed fields.
- **Canonical acceptance:** still blocked where identity, uniqueness, sequence, completeness, formula/version, reset or cross-boundary delivery is not proven.
- **PPO delivery:** diagnostic JSON/pybind exposure does not count as Actor/Critic or RolloutBuffer delivery.
- **Runtime readiness:** none of the documentation status changes authorizes a producer, adapter, tensor, PPO, reward, mask, Viewer or checkpoint change.

In particular, a schema-required field may correctly remain unavailable. The correct outcome is not to fabricate a value but to preserve an explicit status/reason and keep the entity family out of canonical consumption until its producer contract is satisfied.

## 6. Closure blockers for issue #346

Issue #346 should remain open until the following evidence exists:

1. UnitInstance physical identity has an authoritative Engine/player scope, uniqueness/collision policy and complete ownership lifecycle proof.
2. The item-instance domain is either explicitly removed/redefined as catalog multiplicity or gains a real per-copy identity and owner lifecycle; no synthetic IDs.
3. Shop offer opportunity identity is bound to an exact shop snapshot/decision, independently of UnitInstance UUID and slot index.
4. Anvil option gameplay production is proven or the entity remains explicitly unavailable.
5. Strategic unit assessments and anchor candidates have stable identity/revision/completeness and exact owner/source sequence, or remain Shadow-only/unavailable.
6. Action opportunity candidate production exists with immutable exact parameters and truthful candidate-set status, or remains not-produced.
7. Position, traits and temporal entities preserve their distinct scopes/formulas and exact source references.
8. Anti-loop history has explicit record identity/scope/sequence and exact correlation if it is to cross the Python boundary; it must not replace action masks.
9. Native → pybind → wrapper → vector env → Trainer/RolloutBuffer → Actor/Critic delivery is proven field by field.
10. Integrated replay proves identity, stale/reset handling, empty-vs-missing, sequential matches, mask binding and all relevant entity lifecycle transitions.

These are evidence gates, not instructions to implement missing producers now.

## 7. Architecture reconstruction review

1. **Prior problem:** evidence was distributed across multiple audits and the 17 entity kinds could appear “complete” merely because each had a CSV row.
2. **Technical justification:** audit coverage, source availability, canonical identity and PPO delivery are different acceptance levels; conflating them creates false readiness.
3. **New responsibility:** this note owns the consolidated 17-kind coverage and issue-closure view; field-level source evidence remains in the linked audits and CSV.
4. **Contract and invariants:** no schema-only availability; no fabricated IDs/sequences; diagnostic/Shadow output is not PPO input; missing and empty remain distinct; native masks remain independent.
5. **Cross-component impacts:** all structured entity producers, Schema v2, source maps, Engine/pybind/wrapper, PPO rollout, Actor/Critic, replay and checkpoint lineage.
6. **Objective validation:** all 17 unique entity kinds and 31 field-family rows were read from the machine-readable coverage matrix; each family has an explicit evidence status and remaining acceptance gap; this note changes no runtime behavior.

## 8. Gate status

This is a coverage assessment, not issue closure. Issue #346 remains open. Gate 7 executable replay/evaluation remains pending. Gate 8 remains blocked until the integrated review of Gates 1–7 and explicit user authorization.

No runtime, test, schema implementation, tensor layout, PPO, reward, mask, training, checkpoint, Viewer or Overwolf behavior is changed.
