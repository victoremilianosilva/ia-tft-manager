# Stage 1 — Structured Entity Producer Audit Reconciliation v1

**Status:** consolidated source-audit result; documentary only; not runtime-approved.  
**Tracking:** #346 (producer audit), #293 (Observation Schema), #294 (Action/Mask correlation), #288 (checkpoint lineage).  
**Base:** `new-arquiteture`, after PR #451.

## 1. Prior problem

The structured-entity audit had several complementary artifacts: a 17-kind entity matrix, a 31-row field-family CSV, a 223-path Schema v2 crosswalk, per-family source proofs, and an Actor/Critic delivery audit. Without a single reconciliation point, it was easy to confuse:
- an entity kind being listed with its fields being produced;
- an inherited source-map availability with field-level proof;
- native or diagnostic visibility with Python exposure;
- Python exposure with PPO tensor delivery;
- a complete schema identity with a complete runtime decision identity.

PR #451 added executable Schema v2 validation and corrected the native sequence namespace. This reconciliation records what that validation proves—and what it does not.

## 2. Technical rationale

A structured entity is accepted only when its producer, identity, ownership, cardinality, completeness, provenance/formula, source sequence, lifecycle/reset behavior, Python exposure and PPO consumer delivery are independently established. A parent container or ancestor source-map match cannot prove a nested identity field.

The native Engine snapshot ordinal is shared by all eight player rows in one ResetResult/StepResult. It is not a per-player decision counter. Matching local integers, round values, array positions or timestamps cannot substitute for a typed identity join.

## 3. New responsibility and ownership

This document is the Stage 1 reconciliation index for item D:
- the 17-kind/31-family matrix owns entity-family coverage and unresolved gaps;
- the 223-path crosswalk owns Schema v2 field-path dispositions and current Actor/Critic delivery;
- the source audit and linked lifecycle/field proofs own concrete producer evidence;
- Schema v2 owns semantic field contracts, not runtime production;
- native Engine owns its Engine-instance snapshot publication sequence;
- Action/Mask Contract owns exact action/mask correlation and remains independent;
- PPO/rollout/checkpoint consumers must not upgrade partial identity or diagnostic fields into valid policy inputs.

It does not authorize runtime producers, schema serializers, tensor changes, or training changes.

## 4. Coverage and evidence inventory

| Artifact | Current audited scope | What the count establishes |
|---|---:|---|
| Structured entity temporal contract | 17 entity kinds | Entity-family inventory, not producer acceptance |
| Producer coverage matrix | 31 field-family rows × 15 columns | Source/status/delivery/gap dispositions at family granularity |
| Schema v2 field-source crosswalk | 223 data paths × 16 columns | Every enumerated path has a field-level classification and Actor/Critic delivery disposition |
| Source-map reconciliation | 77 source entries | Inventory of candidate source paths, not proof by itself |
| Schema v2 path classification | 43 exact + 164 ancestor/family + 16 no-source-map paths | All 223 enumerated paths have explicit dispositions; inherited matches are not field-level proof |
| Actor/Critic delivery audit | 223 paths classified | Current consumer boundary, not a proposed tensor layout |

The 223-path crosswalk and the separate 254 semantic-leaf count in the producer-correction proposal use different counting scopes. They must not be added together or treated as interchangeable. The 223-path crosswalk is the current auditable CSV inventory; the 254 count includes nested semantic leaf/wrapper paths and remains a reconciliation note until its counting rule is mechanically reproduced.

### Entity-family disposition

| Entity kind | Current disposition | Principal unresolved acceptance evidence |
|---|---|---|
| `unit_instance` | Native UUID exists; canonical physical identity remains unverified | UUID repeats after same-seed reset; no player/match namespace, collision registry or complete lifecycle acceptance |
| `champion_catalog_entry` | Native catalog metadata observed | Stable catalog fingerprint/order bound to the decision payload |
| `board_slot` | Native fixed 28-slot domain and occupancy observed | Canonical hex geometry/orientation, exact sequence and structured PPO delivery |
| `bench_slot` | Native fixed 9-slot domain and occupancy observed | Exact sequence and structured PPO delivery |
| `shop_offer` | Native five-slot offer content observed | Offer ID/revision/reroll generation and exact shop-snapshot binding |
| `pool_availability` | Native shared-lobby query exists | Immutable identity-correlated pool snapshot; no current PPO delivery |
| `item_instance` | Physical per-copy item identity not produced | Typed per-copy identity/owner relation/event sequence; elimination terminal disposition |
| `item_catalog_entry` | Catalog metadata observed | Catalog fingerprint/order in the decision payload |
| `component_inventory` | Catalog IDs and multiplicity observed | Per-copy identity/acquisition sequence; multiplicity is not physical identity |
| `anvil_option` | API capability exists; no gameplay producer found in audited path | Gameplay enqueue producer, stable anvil/option identity, pending-choice sequence |
| `trait` | Catalog membership and derived counts exist with distinct scopes | Typed membership, catalog/milestone version, item-granted trait semantics |
| `position` | Native 4×7 slot convention observed; Shadow proposals diagnostic | Canonical TFT hex geometry/orientation and physical-unit correlation |
| `unit_assessment` | Derived/Shadow assessment exists | Physical UUID/slot identity, formula/version and completeness |
| `anchor_candidate` | Shadow composition/direction/pivot candidates exist | Candidate ID/revision/set completeness and owner sequence |
| `action_opportunity_candidate` | Authoritative candidate vector is empty in audited construction path | Real producer and immutable snapshot-bound candidate set; empty is not HOLD |
| `temporal_decision_history` | Flat action-memory/slot-age features are delivered | Typed ordered events and authoritative per-player decision sequence |
| `anti_loop_history` | Internal native history exists | Record identity/sequence and approved Python exposure; it never replaces action masks |

## 5. Identity and delivery corrections carried forward from PR #451

1. Native `TFTEngine::Impl::decision_sequence` maps to `snapshot_sequence` in namespace `tft.engine.observation-snapshot`.
2. That sequence increments once per published ResetResult/StepResult, is shared by the eight player rows, and remains monotonic across episode resets within one Engine instance.
3. `tft.engine.decision` remains a future per-player decision counter. It must not be populated from the Engine-wide snapshot ordinal.
4. Authoritative logical `match_id` and per-player decision sequence remain unavailable in the audited native-to-PPO path. Decision identity therefore remains partial; the identity hash remains null.
5. A partial identity cannot authorize masks, Critic context, anti-loop history or strategic-owner snapshots.
6. The Action/Mask Contract remains independent. Native masks are exact side inputs; Engine remains the final legality authority.

## 6. Critical producer-to-PPO boundaries

- **Unit UUID:** available in diagnostic audit snapshots and decision-state copies; not present as a typed field in the flat PPO observation or RolloutBuffer.
- **Shop offer:** current offer content and a UnitInstance UUID are not a stable offer identity. Slot index and champion ID cannot substitute for offer revision.
- **Items/components:** catalog IDs and multiplicity are observed; physical item/component instance identity is not produced. Eliminated unit equipment mappings require explicit terminal cleanup/disposition evidence.
- **Traits/position:** native catalog/slot-derived and heuristic values have different scopes. The 4×7 internal mapping is not proven canonical TFT hex geometry.
- **Strategic evidence:** owned-unit assessments and anchors are Shadow/diagnostic; they lack physical unit or stable candidate-set identities. The action-candidate source vector is empty in the audited call path.
- **Temporal/anti-loop:** flat PPO action-memory scalars are not typed event history. Internal AntiLoopHistory records are not exported to Python and have no per-record decision sequence.
- **Actor/Critic:** the current audit records Actor-only item compatibility inputs and Actor mask side inputs; the value path currently ignores masks. This is a current-delivery finding, not an approval of a future Critic design.

## 7. Contract and invariants

1. Schema declaration is not evidence of production.
2. Raw `UnitInstance::uuid` is not accepted as a globally/cross-episode-safe `instance_id`.
3. Champion ID, slot index and array order are never physical instance identity.
4. Shop offer identity is distinct from offered UnitInstance identity and pool ownership.
5. Item catalog identity/multiplicity is distinct from physical item-instance identity.
6. Native, derived, Shadow-only, diagnostic-only, not-produced, not-correlated, not-exposed-to-Python and unverified remain distinct dispositions.
7. Empty, missing, unknown, partial, stale and incompatible remain distinct.
8. No synthetic IDs, sequences, candidate records, item copies, pool snapshots or spatial semantics.
9. Strategic recommendations, candidate scores, baselines and executor resolutions remain separate from PPO actions and never bypass native legality.
10. Exact action masks remain independent identity-correlated side inputs.

## 8. Remaining acceptance blockers

Issue #346 remains open until the following are proven or the corresponding schema fields are version-corrected to remain unavailable:
- safe physical UnitInstance identity scope, collision policy and complete ownership lifecycle (including elimination/item terminal cleanup);
- stable shop-offer identity/revision and exact snapshot binding;
- explicit item/component identity policy or schema representation as catalog multiplicity;
- anvil gameplay producer or explicit unavailable collection contract;
- canonical board geometry and typed position correlation;
- stable unit-assessment/anchor candidate identities and complete candidate-set envelopes, or explicit Shadow-only/unavailable status;
- real action-opportunity candidate producer, or explicit not-produced status;
- typed temporal/anti-loop record sequence and reset semantics, if these records are ever approved for Python/PPO;
- authoritative logical match identity and per-player decision sequence;
- integrated native → pybind → wrapper → vector env → Trainer/RolloutBuffer → Actor/Critic delivery and replay acceptance;
- reconciliation of the 223 versus 254 path-counting scopes with a reproducible enumeration rule.

These are acceptance blockers, not instructions to synthesize missing data. Real GEP match identity evidence remains deferred to Stage 7.

## 9. Cross-component impacts

The audit informs Observation Schema v2, Decision Identity v2, sequence registry, structured entity temporal contract, UnitInstance/ShopEngine/UnitPool/ItemEngine, trait and positioning producers, strategic evidence, pybind, Python wrapper, rollout, Actor/Critic, replay and checkpoint lineage. It does not alter any of those runtime components.

## 10. Objective validation criteria

- The 17-kind entity list matches the temporal contract.
- The 31-row producer matrix has 15 columns and 17 distinct entity kinds.
- The 223-path crosswalk has 16 columns and a field-level disposition for every path.
- All 223 paths have current Actor/Critic delivery classifications.
- Schema v2 v1/v2 validators continue to run in the Observation Schema workflow.
- Identity/hash fixtures preserve the PR #451 distinction between snapshot and per-player decision namespaces.
- No audit-only or diagnostic-only field is promoted to PPO delivery.
- No runtime, tensor, reward, mask, checkpoint, Viewer or Overwolf behavior is changed by this audit.

## 11. Architecture reconstruction review

1. **Prior problem:** multiple audits could be read as proving more than they do, and inherited source availability could be mistaken for field-level production.
2. **Technical rationale:** policy inputs and replay identity require producer-backed semantics at each field and boundary.
3. **New responsibility:** this reconciliation owns the consolidated Stage 1 item-D audit index; source-specific proofs remain authoritative for detailed evidence.
4. **Contract/invariants:** the 17-kind inventory, 31-family matrix and 223-path crosswalk remain separate counting scopes; no synthetic identity; diagnostic delivery is not PPO delivery; masks remain independent.
5. **Cross-component impact:** schema, entity producers, identity, Python boundary, rollout, Actor/Critic, replay and checkpoint lineage.
6. **Objective validation:** artifact counts and required fields are mechanically checked; unresolved producer capabilities remain explicitly blocked; documentation-only change.

## 12. Related evidence

- [Structured Entity Producer Evidence Audit](observation-structured-entity-producer-audit.v1.draft.md)
- [Structured Entity Producer Coverage Matrix](observation-structured-entity-producer-coverage.v1.draft.md)
- [Structured Entity Audit Coverage and Closure Status](observation-structured-entity-audit-coverage-status.v1.draft.md)
- [Schema v2 Field-to-Source Crosswalk](observation-schema-v2-field-source-crosswalk.v1.draft.md)
- [Schema v2 Unmapped Field Dispositions](observation-schema-v2-unmapped-field-dispositions.v1.draft.md)
- [Schema v2 Producer Reconciliation and Correction Proposal](observation-schema-v2-producer-correction-proposal.v1.draft.md)
- [Unit Instance, Shop Offer and Shared Pool Lifecycle Follow-up](unit-instance-shop-pool-lifecycle-followup.v1.draft.md)
- [Observation Schema v2 Identity Boundary](observation-schema-v2-identity-boundary.v1.draft.md)
- [Current Actor/Critic Delivery Audit](observation-schema-v2-actor-critic-current-delivery.v1.draft.md)
