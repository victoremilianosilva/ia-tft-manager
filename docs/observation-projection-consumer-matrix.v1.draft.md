# Observation Projection Consumer Matrix v1 — Draft

**Status:** proposed semantic-consumer decisions; not approved for runtime projection.  
**Scope:** semantic eligibility and intended Actor/Critic/control/diagnostic ownership only.  
**Source inventory:** 77 semantic source-map entries; 66 historical feature definitions across 18 blocks; 66 migration mappings.  
**Machine-readable matrix:** `spec/observation-projection-consumer-matrix.v1.draft.json`.

## 1. Purpose and boundary

The previous consumer audit correctly separated the semantic source map, historical PPO feature map and legacy migration map, but left several target consumer allocations broad or unresolved. This matrix makes a proposed primary disposition explicit for every semantic source-map entry and extends the legacy crosswalk with the resulting consumer intent.

It does **not** select tensor dimensions, offsets, shapes, axes, ordering, padding, normalization, categorical vocabularies, or encoder architecture. A candidate is not runtime-ready: all source, provenance, formula, validity, identity-correlation and missingness blockers must be satisfied first.

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

Candidate-generation diagnostics, Shadow priorities, planner scores/confidence, selection rationale, revision rationale, raw Composition Intelligence diagnostic snapshots, Unified Strategic State Machine snapshots and Shadow recommendations remain outside PPO observations, labels, rewards and imitation targets. A future change requires a separate learning-purpose justification and reconstruction review.

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
- Planner commitment, Composition Intelligence active composition and Unified Shadow snapshots remain separate owner streams.
- Candidate proposals are evidence, not commands or confirmed transitions.

## 6. Legacy crosswalk

The JSON matrix contains all 66 migration entries with their original migration decision and rationale plus the new projection crosswalk disposition and target consumers.

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
2. **Technical rationale:** PPO must learn from canonical factual and strategic context without inheriting legacy positional assumptions or copying Shadow recommendations.
3. **New responsibility:** this matrix owns semantic eligibility and consumer intent; schema owns meaning/provenance; source owners own evidence; Action/Mask owns legality; PPO architecture owns eventual encoding.
4. **Contracts/invariants:** every field has one disposition; unavailable stays unavailable; no legacy offset inheritance; exact masks remain separate; Shadow recommendations/evaluator outputs are excluded; metadata hashes are not neural scalars.
5. **Cross-component impact:** schema/source/legacy/migration maps, strategic/economic owners, Engine bindings, Action/Mask, PPO Actor/Critic, checkpoint lineage, replay and evaluation.
6. **Objective validation:** 77/77 semantic fields accounted for; 66/66 historical mappings reconciled; disposition coverage checked; candidate producer, semantic bridge and provenance blockers explicitly retained. No runtime files changed.

**Gate status:** documentary proposal only. Gate 1 tensor projection and Gate 4 PPO architecture remain open. Gate 8 and explicit authorization are still required before runtime implementation.
