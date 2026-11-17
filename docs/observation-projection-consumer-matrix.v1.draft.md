# Observation Projection Consumer Matrix v1 — Draft

**Status:** proposed semantic-consumer decisions; not approved for runtime projection.  
**Scope:** semantic eligibility and intended Actor/Critic/control/diagnostic ownership only.  
**Source inventory:** 77 semantic source-map entries; 66 historical feature definitions across 18 blocks; 66 migration mappings.  
**Machine-readable matrix:** `spec/observation-projection-consumer-matrix.v1.draft.json`.

## 1. Purpose and boundary

The previous consumer audit correctly separated the semantic source map, historical PPO feature map and legacy migration map, but left several target consumer allocations broad or unresolved. This matrix makes a proposed primary disposition explicit for every semantic source-map entry and extends the legacy crosswalk with the resulting consumer intent.

It does **not** select tensor dimensions, offsets, shapes, axes, ordering, padding, normalization, categorical vocabularies, or encoder architecture. A candidate is not runtime-ready: all source, provenance, formula, validity, identity-correlation and missingness blockers must be satisfied first.

**Current implementation is separate from this proposed allocation.** See [Schema v2 Current Actor/Critic Delivery Audit](observation-schema-v2-actor-critic-current-delivery.v1.draft.md): the current Actor receives item/recipe compatibility matrices through specialized heads, while `encode()` removes those matrices from the value-head input; current masks are applied to Actor but ignored by `get_value()`. Any `shared_actor_critic_candidate` entry in this matrix is a future semantic-consumer proposal, not evidence that the current Critic receives that exact feature block.

## 2. Disposition vocabulary

| Disposition | Meaning |
|---|---|
| `shared_actor_critic_candidate` | Decision-relevant state/evidence proposed as available to both policy and value estimation |
| `critic_only_candidate` | Additional history/context proposed for value estimation; not a legality rule |
| `control_metadata_only` | Identity, provenance, correlation, contract or catalog metadata; not a learned scalar |
| `diagnostic_only` | Diagnostic/planner/evaluator output excluded from PPO inputs and targets |
| `unavailable` | No authoritative producer/value in the audited path; preserve missing/unknown |
| `unresolved` | Semantics or producer chain insufficiently proven; withhold |
| `excluded` | Explicitly not eligible for PPO input/target; used where a field is permanently out of scope |

## 3. Coverage summary

| Primary disposition | Fields |
|---|---:|
| shared_actor_critic_candidate | 34 |
| unavailable | 17 |
| control_metadata_only | 7 |
| diagnostic_only | 9 |
| unresolved | 5 |
| critic_only_candidate | 5 |

No semantic source-map field is currently classified as permanently excluded; diagnostic outputs and metadata have their own explicit dispositions. Candidate means proposed eligibility, not runtime approval.

Every source-map field has exactly one primary disposition in the machine-readable matrix. The legacy crosswalk separately classifies all 66 historical features; its counts are not additive to the 77 semantic fields.

## 4. Key consumer decisions

### Shared Actor/Critic candidates

- Player lifecycle, health, gold, level, XP, XP-to-next and streaks.
- Stage and current interest; estimated board power and relative lobby power only with formula provenance and sample completeness.
- Board, bench, shop offers and item entities, preserving physical identity, ownership domain, slot and catalog binding.
- Positioning, capacity, trait counts, unit roles, item/recipe fit, with estimated/derived provenance preserved.
- Canonical direction label and viability, owned-unit assessments and anchor candidate evidence, subject to their specific producer/formula blockers.
- Decision-local action counts, remaining action budget and per-slot board-move age.
- Anvil options and strategic commitment review timing.

These are candidate inputs because they describe the state or evidence on which buy, sell, reroll, XP, item, composition and positioning decisions depend. Their inclusion does not authorize legacy formulas or encodings.

### Critic-only history candidates

Anti-loop position history, move history, blocked-move records and state-visit history are proposed as additional value/history context. They do not suppress actions, redefine legal actions or replace exact masks. The Actor does not receive this history under this matrix until a separate justification is approved.

### Control metadata only

Decision identity hashes, mask references, opaque direction/composition identity keys, provenance source labels and raw owner snapshot envelopes are validated or retained for correlation/replay. They are not numeric policy features. Semantic direction and composition evidence may be represented by their own typed fields; identity tokens do not become neural scalars.

### Diagnostic-only outputs

Candidate-generation diagnostics, TFT Strategic Engine priorities, planner scores/confidence, selection rationale, revision rationale, raw Composition Intelligence diagnostic snapshots, Unified Strategic State Machine snapshots and TFT Strategic Engine recommendations remain outside PPO observations, labels, rewards and imitation targets. A future change requires a separate learning-purpose justification and reconstruction review.

### Unavailable and unresolved fields

Progression, focus weights, composition lock, flexible unit membership, projected income, incoming damage, elimination risk, economic/strategic pressure, income/interest/streak bonus and shop cost remain unavailable until authoritative producers exist.

Completed traits and core unit IDs remain unresolved because the current bridge conflates completed traits with core/focus concepts and the active direction's unit list is not yet proven to be a core-only set.

The action-opportunity parent collection is not populated. Sell-value and affordability child values do not establish a complete candidate set; those child fields remain unresolved and cannot be projected independently as candidate rows.

## 5. Strategic semantics preserved

- Direction label, direction identity and composition identity are separate.
- Active composition membership, core-unit membership and anchor candidates are not interchangeable.
- Completed traits are not focus weights or core traits by alias.
- Progression and economic posture are distinct outputs.
- Lock unavailable is not unlocked.
- Planner commitment, Composition Intelligence active composition and Unified Strategic State Machine snapshots remain separate owner streams.
- Candidate proposals are evidence, not commands or confirmed transitions.

## 6. Legacy crosswalk

The JSON matrix contains all 66 migration entries with their original migration decision and rationale plus the new projection crosswalk disposition, destination resolution and target consumers. Current crosswalk result: 45 rebuild from semantic destinations, 9 control/catalog/identity metadata, 6 excluded or deduplicated, 3 blocked by unavailable semantic sources, 1 diagnostic-only/excluded, and 2 unresolved semantic mappings. All destination paths are classified; none remains unmapped.

Historical positional features are not copied mechanically. Constants and duplicates are excluded/deduplicated; ratios and heuristic proxies are rebuilt from semantic facts; merged legacy features are split where they combined distinct concepts; unavailable destinations remain blocked; catalog-order encodings are replaced by stable IDs and catalog fingerprints.

## 7. Mask, identity and catalog boundary

Action masks remain independent, exact, decision-correlated side inputs for Actor and Critic. The Engine remains final legality authority. Anti-loop history is descriptive context only.

Decision identity hashes, observation/mask payload hashes, action/mask contract hashes and catalog fingerprints are control/compatibility metadata. They are not learned scalar features. A complete v2 identity and exact mask correlation are prerequisites for future projection consumption.

## 8. Remaining evidence before concrete tensor projection

1. Prove source/owner/sequence for every candidate field at native producer, serialization, binding, wrapper and PPO boundary.
2. Resolve completed-traits/core-unit semantic bridge and owner.
3. Resolve candidate producer and complete candidate-set lifecycle before exposing action-opportunity rows.
4. Define stable entity identity, ordering, catalog fingerprints and spatial coordinate semantics.
5. Define field-level formulas/quality for estimated board power, positioning, owned-unit assessments, anchor evidence, item fit and recipe fit.
6. Verify temporal reset and sequence correlation for action history and anti-loop history.
7. Review the v2 identity/mask correlation proposal and bind exact masks separately.
8. Only after those decisions, define per-feature encoding, normalization, shape and Actor/Critic block layout.

## 9. Architecture reconstruction review

1. **Prior problem:** the previous audit identified broad candidate families but left many Actor/Critic allocations unresolved and did not provide one explicit disposition for every semantic field.
2. **Technical rationale:** PPO must learn from canonical factual and strategic context without inheriting legacy positional assumptions or copying TFT Strategic Engine recommendations.
3. **New responsibility:** this matrix owns semantic eligibility and consumer intent; schema owns meaning/provenance; source owners own evidence; Action/Mask owns legality; PPO architecture owns eventual encoding.
4. **Contracts/invariants:** every field has one disposition; unavailable stays unavailable; no legacy offset inheritance; exact masks remain separate; TFT Strategic Engine recommendations/evaluator outputs are excluded; metadata hashes are not neural scalars.
5. **Cross-component impact:** schema/source/legacy/migration maps, strategic/economic owners, Engine bindings, Action/Mask, PPO Actor/Critic, checkpoint lineage, replay and evaluation.
6. **Objective validation:** 77/77 semantic fields accounted for; 66/66 historical mappings reconciled; disposition coverage checked; candidate producer, semantic bridge and provenance blockers explicitly retained. No runtime files changed.

**Gate status:** documentary proposal only. Gate 1 tensor projection and Gate 4 PPO architecture remain open. Gate 8 and explicit authorization are still required before runtime implementation.


## 10. Gate 8 initial consumer decision reconciliation — 2026-11-15

The initial PPO lineage decisions are:

- **Exact masks:** same decision-correlated native mask snapshot is mandatory as a separate Actor and Critic side input. The Engine remains final legality authority.
- **Item/recipe evidence:** factual inventory/component and unit target-profile inputs are shared semantic context. The precomputed 9×37 inventory-fit and 100×37 recipe-fit matrices are Actor-specific action-conditioning structures in the initial consumer design; they are not required raw Critic inputs. A Critic summary is permitted only as a separately versioned derivation from the same validated source evidence.
- **Temporal history:** AntiLoopEngine history and current untyped action-memory scalars are excluded as separate Critic history inputs in the initial projection. Reconsideration requires typed event producer/sequence, explicit reset semantics, deterministic replay and evaluation ablation.
- **No tensor layout:** these decisions establish semantic consumer eligibility only. They do not choose dimensions, offsets, normalization, padding, encoder family or sharing topology.

This section supersedes the unresolved wording in sections 4 and 8 that asked whether raw compatibility matrices or AntiLoop history should be included in the initial Critic input. The semantic consumer matrix remains a design input until Stage 0 projection review.
