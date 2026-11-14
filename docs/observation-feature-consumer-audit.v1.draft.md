# Observation Feature-to-Consumer Audit v1 — Draft

**Status:** documentary audit; no tensor layout, dimensions, offsets, normalization constants, or encoder architecture approved.  
**Scope:** map current semantic source inventory to eligibility/consumer boundaries before creating the concrete tensor projection.  
**Base:** `new-arquiteture`; source-map commit `3575d21cc0f7dbb5544d75526bd96939b37f5c96`.  
**Depends on:** Observation Schema v1, Observation Tensor Projection Requirements v1, Action / Mask Contract v1, PPO Architecture and Checkpoint Contract v1.

## 1. Purpose

The source map and legacy feature map answer different questions. This audit joins them without treating historical tensor consumers as authority for the new projection:

- semantic source map: what each current semantic field is sourced from, its nature, availability, units, and intended semantic consumer;
- legacy feature map: which old tensor blocks/offsets fed existing policy components;
- this audit: whether a semantic field is eligible for model input, metadata/control only, diagnostic-only, or withheld pending a producer/contract.

This is a **consumer-boundary audit**, not the concrete tensor projection manifest required by the projection contract. It intentionally does not assign offsets, shapes, normalization, vocab indices, or encoder dimensions.

## 2. Reproducible inventory

The current source map contains **77 entries**:

- `available`: 50
- `not_produced`: 17
- `not_available`: 2
- `available_but_not_projected`: 1
- `not_correlated`: 1
- `available_shadow_only`: 4
- `derived`: 2

The legacy feature map contains **66 inventoried feature definitions across 18 blocks**. The migration crosswalk contains 66 mappings. These are three different inventories; their counts must not be added or conflated.

The source map records current native/strategic producers. It does **not** prove that Overwolf/GEP live snapshots have traversed the full adapter→Engine→PPO path. That integration requires its own end-to-end evidence.

## 3. Current versus target consumer boundary

### 3.1 What the historical PPO path proves

The audited legacy map records a shared encoded representation consumed by policy and value paths, with specialized consumers for board, item, and candidate features. The current `TFTPolicy.value_head` consumes the fused observation representation. The current `get_value` path ignores action masks.

These are facts about the historical/current implementation, not a target architecture decision. They do not prove that every new semantic field should be copied into both Actor and Critic.

### 3.2 Normative target constraints

- Actor and Critic feature consumers must be declared separately in the concrete projection manifest.
- Exact decision-correlated action masks remain a separate side input to Actor and Critic (or a provably lossless encoding), not ordinary observation features.
- Additional Markov/history context for the Critic is additive and cannot replace masks.
- Identity hashes, sequence references, catalog fingerprints, and mask references primarily validate/correlate inputs; they are not automatically neural features.
- Canonical strategic/composition/economic/unit evidence may be considered as PPO context only when source, owner, nature, provenance, status, and sequence are valid.
- Shadow recommendations, evaluator scores/rankings/confidence, baseline recommendations, executor resolutions, and diagnostic Unified Strategic State Machine outputs are excluded from PPO features and targets.
- Missing/unknown/unavailable values are never converted to zero/false or inferred from legacy defaults.

## 4. Field-level disposition

The disposition column is a conservative eligibility decision, not a tensor assignment. “Candidate” means eligible for a later projection proposal after its producer, provenance, and consumer are validated.

| Semantic field | Availability | Nature | Source-map intended consumer | Projection disposition |
|---|---|---|---|---|
| `player.lifecycle` | available | observed | player lifecycle field | global factual context candidate; preserve units, validity and missingness |
| `player.health` | available | observed | player/economy encoder | global factual context candidate; preserve units, validity and missingness |
| `player.economy.gold` | available | observed | player/economy encoder | global factual context candidate; preserve units, validity and missingness |
| `player.economy.level` | available | observed | player/economy encoder | global factual context candidate; preserve units, validity and missingness |
| `player.economy.xp` | available | observed | player/economy encoder | global factual context candidate; preserve units, validity and missingness |
| `player.economy.xp_to_next` | available | derived | player/economy encoder | global factual context candidate; preserve units, validity and missingness |
| `player.streaks.win_streak` | available | observed | player/economy encoder | global factual context candidate; preserve units, validity and missingness |
| `player.streaks.loss_streak` | available | observed | player/economy encoder | global factual context candidate; preserve units, validity and missingness |
| `derived_context.economic_context.stage` | available | derived | player/economy encoder | economic context candidate; estimated/unavailable fields retain nature and status |
| `derived_context.economic_context.interest_if_resolved_now` | available | derived | economic context encoder | economic context candidate; estimated/unavailable fields retain nature and status |
| `derived_context.economic_context.projected_next_round_income` | not_produced | estimated | economic context encoder | economic context candidate; estimated/unavailable fields retain nature and status |
| `derived_context.economic_context.board_power` | available | estimated | economic context encoder | economic context candidate; estimated/unavailable fields retain nature and status |
| `derived_context.economic_context.lobby_average_board_power` | available | estimated | economic context encoder | economic context candidate; estimated/unavailable fields retain nature and status |
| `derived_context.economic_context.relative_board_power` | available | derived | economic context encoder | economic context candidate; estimated/unavailable fields retain nature and status |
| `derived_context.economic_context.estimated_incoming_damage` | not_produced | estimated | economic/critic context encoder | economic context candidate; estimated/unavailable fields retain nature and status |
| `derived_context.economic_context.elimination_risk` | not_produced | estimated | economic/critic context encoder | economic context candidate; estimated/unavailable fields retain nature and status |
| `entities.board` | available | observed | entity-set encoder | typed entity/set candidate; preserve instance identity, ownership domain, slot and catalog binding |
| `entities.bench` | available | observed | entity-set encoder | typed entity/set candidate; preserve instance identity, ownership domain, slot and catalog binding |
| `entities.shop` | available | observed | entity-set encoder | typed entity/set candidate; preserve instance identity, ownership domain, slot and catalog binding |
| `entities.items` | available | observed | item/entity relation encoder | typed entity/set candidate; preserve instance identity, ownership domain, slot and catalog binding |
| `derived_context.positioning` | available | estimated | positioning/entity encoder | position/entity context candidate; preserve heuristic nature and formula provenance |
| `strategic_evidence.commitment_context.direction_id` | available | derived | strategic evidence encoder | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.commitment_context.direction_identity` | available | derived | strategic evidence encoder | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.commitment_context.progression_plan` | not_produced | inferred | strategic/economic context encoder | unavailable/unknown; do not project as a value |
| `strategic_evidence.owned_unit_assessments` | available | derived | strategic/entity encoder | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.anchor_candidates` | available | estimated | strategic evidence encoder | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.candidate_generation` | available | observed | strategic evidence encoder | diagnostic only; exclude from PPO input pending separate justification |
| `strategic_evidence.completed_traits` | available | derived | strategic evidence encoder | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.commitment_context.core_unit_ids` | available | derived | strategic evidence encoder | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.commitment_context.composition_locked` | not_available | derived | strategic evidence encoder | unavailable/unknown; do not project as a value |
| `derived_context.action_opportunity.items` | not_produced | estimated | action candidate context encoder | candidate/action-opportunity context; withhold until candidate producer and completeness contract are proven |
| `legal_state_context.anti_loop_state` | available_but_not_projected | observed | critic legal-context encoder | critic history/context candidate; exact masks remain a separate side input |
| `legal_state_context.mask_reference` | not_correlated | observed | actor and critic legal-context encoders | contract/control metadata; validate or bind vocabularies, not a learned scalar feature |
| `shadow_recommendations` | available_shadow_only | recommended | diagnostic channel only | diagnostic only; exclude from PPO input pending separate justification |
| `strategic_evidence.focus_weights` | not_produced | inferred | strategic evidence encoder | unavailable/unknown; do not project as a value |
| `strategic_evidence.commitment_context.composition_identity` | available | derived | strategic evidence encoder | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.commitment_context.current_direction_score` | available | estimated | strategic evidence encoder | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.commitment_context.current_direction_viable` | available | derived | strategic evidence encoder | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.commitment_context.direction_source` | available | derived | strategic evidence encoder | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `derived_context.decision_history.actions_taken_this_round` | available | derived | PPO contextual encoder / action-opportunity encoder | temporal context candidate; actor/critic allocation unresolved |
| `derived_context.decision_history.remaining_action_budget` | available | derived | PPO contextual encoder / action-opportunity encoder | temporal context candidate; actor/critic allocation unresolved |
| `derived_context.decision_history.board_move_age_by_slot` | available | derived | PPO contextual encoder / action-opportunity encoder | temporal context candidate; actor/critic allocation unresolved |
| `derived_context.recipe_target_fit` | available | estimated | PPO contextual encoder / action-opportunity encoder | unresolved; no tensor projection approved |
| `entities.items.anvil_options` | available | derived | PPO contextual encoder / action-opportunity encoder | typed entity/set candidate; preserve instance identity, ownership domain, slot and catalog binding |
| `derived_context.action_opportunity.items.sell_value` | available | derived | PPO contextual encoder / action-opportunity encoder | candidate/action-opportunity context; withhold until candidate producer and completeness contract are proven |
| `derived_context.action_opportunity.items.affordability` | available | derived | PPO contextual encoder / action-opportunity encoder | candidate/action-opportunity context; withhold until candidate producer and completeness contract are proven |
| `identity.decision_identity_hash` | derived | derived | observation/mask/transition correlation; rollout and replay | contract/control metadata; validate or bind vocabularies, not a learned scalar feature |
| `legal_state_context.anti_loop_state.position_history` | available | observed | critic state/context encoder and replay | critic history/context candidate; exact masks remain a separate side input |
| `legal_state_context.anti_loop_state.move_history` | available | observed | critic state/context encoder and replay | critic history/context candidate; exact masks remain a separate side input |
| `legal_state_context.anti_loop_state.blocked_move_records` | available | derived | critic state/context encoder and anti-loop diagnostics | critic history/context candidate; exact masks remain a separate side input |
| `legal_state_context.anti_loop_state.state_visits` | available | derived | critic state/context encoder and replay | critic history/context candidate; exact masks remain a separate side input |
| `legal_state_context.critic_context` | not_available | derived | PPO critic/value head | contract/control metadata; validate or bind vocabularies, not a learned scalar feature |
| `derived_context.capacity` | derived | derived | global/economic encoder | unresolved; no tensor projection approved |
| `derived_context.trait_counts` | available | derived | trait/entity encoder | unresolved; no tensor projection approved |
| `derived_context.unit_roles` | available | derived | unit/entity encoder | unresolved; no tensor projection approved |
| `derived_context.item_target_fit` | available | estimated | item/entity encoder | unresolved; no tensor projection approved |
| `player.economy.income` | not_produced | derived | economy encoder | global factual context candidate; preserve units, validity and missingness |
| `player.economy.interest` | not_produced | derived | economy encoder | global factual context candidate; preserve units, validity and missingness |
| `player.economy.streak_bonus` | not_produced | derived | economy encoder | global factual context candidate; preserve units, validity and missingness |
| `player.economy.shop_cost` | not_produced | observed | economy/action-opportunity encoder | global factual context candidate; preserve units, validity and missingness |
| `derived_context.economic_context.board_pressure` | not_produced | estimated | economic/context encoder | economic context candidate; estimated/unavailable fields retain nature and status |
| `derived_context.economic_context.economy_pressure` | not_produced | estimated | economic/context encoder | economic context candidate; estimated/unavailable fields retain nature and status |
| `derived_context.economic_context.survival_pressure` | not_produced | estimated | economic/context encoder | economic context candidate; estimated/unavailable fields retain nature and status |
| `strategic_evidence.priorities` | available_shadow_only | recommended | diagnostic strategic evidence encoder | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.progression` | not_produced | inferred | strategic/economic encoder | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.pressure` | not_produced | estimated | strategic/economic encoder | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.uncertainty` | not_produced | estimated | strategic evidence encoder | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.commitment_context.confidence` | available | estimated | strategic evidence encoder | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.commitment_context.consecutive_reviews` | available | derived | strategic evidence encoder | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.commitment_context.last_review_round` | available | derived | strategic evidence encoder | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.commitment_context.selected_round` | available | derived | strategic evidence encoder | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.commitment_context.selection_reason` | available | derived | strategic evidence encoder | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.commitment_context.revision_condition` | available | derived | strategic evidence encoder | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.commitment_context.flexible_unit_ids` | not_produced | inferred | strategic/entity encoder | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.owner_snapshots.planner_commitment` | available | derived | planner-local strategic evidence encoder and replay | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.owner_snapshots.composition_intelligence` | available_shadow_only | derived | diagnostic strategic evidence encoder/replay | canonical strategic evidence candidate; actor/critic allocation and formula-level provenance require review |
| `strategic_evidence.owner_snapshots.unified_state_machine` | available_shadow_only | derived | diagnostic strategic evidence encoder/replay | diagnostic only; exclude from PPO input pending separate justification |

## 5. Cross-cutting decisions and unresolved items

### 5.1 Global factual context

Player health, economy, streaks, lifecycle, and stage are candidate global context. Preserve physical units and raw semantic values before selecting normalization. XP and XP-to-next remain separate values; do not retain the legacy denominator-hidden ratio as the only representation.

### 5.2 Entity and spatial context

Board, bench, shop, and item domains remain distinct. A champion ID may group copies but cannot replace physical instance identity. Shop offers are temporary opportunities, not owned units. The target representation must preserve slot identity where meaningful, deterministic set ordering where not, and catalog fingerprints.

The legacy 4×7×5 board layout is historical only. Board axes/origin/orientation and slot-to-position mapping require explicit specification before any spatial tensor shape is selected.

### 5.3 Strategic evidence

The canonical direction/commitment owner and active composition owner may supply factual strategic context, but direction identity, composition identity, anchor identity, core unit membership, completed traits, focus weights, progression, and lock state remain distinct concepts.

- Missing progression/focus/lock values remain unavailable.
- Heuristic unit assessments and anchor scores retain estimated nature, formula identity, and uncertainty; they are not calibrated probabilities.
- Candidate-generation counters are diagnostic unless a concrete learning purpose and stable semantics are approved.
- Unified Strategic State Machine remains diagnostic-only and is not a second strategic authority.
- Shadow recommendations and evaluator outputs remain excluded.

### 5.4 Economic evidence

Observed gold/level/XP and derived interest/stage can be considered as context. Projected income, incoming damage, and elimination risk are not produced in the audited callsite and must remain unavailable. Board-power estimates and relative-power ratios retain their heuristic/estimated nature and require producer/version/sample-completeness evidence.

### 5.5 Temporal and anti-loop context

Decision history and anti-loop histories are sequence-bound. Anti-loop history is a Critic history/context candidate, not a replacement for masks and not a direct legality override. Decision-local action counts and board-move ages require a clear decision/round basis and reset policy; their Actor-versus-Critic allocation remains open.

### 5.6 Candidate/action opportunity context

The action-candidate collection is not populated in the audited callsite. Available sell-value/affordability subfields do not establish a complete candidate producer. Do not construct a fixed candidate tensor or infer candidate rows from empty/default vectors until candidate-set status, stable identity, physical parameters, costs, provenance, and sequence correlation are available.

### 5.7 Catalogs and metadata

Catalog IDs, content hashes, and order hashes bind categorical/entity vocabularies. They are checkpoint/projection compatibility metadata; do not normalize catalog IDs as continuous numeric values. Identity and mask hashes are correlation/validation metadata, not learned scalar inputs.

## 6. Required next evidence before concrete projection

1. Verify producer callsites and provenance for every source-map entry, including owner and exact sequence namespace.
2. Trace each candidate field through snapshot serialization and native/Python binding to confirm actual availability to PPO.
3. Trace legacy feature consumers in policy code to distinguish Actor heads, Critic/value path, and shared encoders; record only observed behavior.
4. Define target Actor/Critic consumer decisions for each semantic feature family, including exclusions and critic-only history.
5. Resolve candidate producer gaps and the action-opportunity parent/child availability inconsistency before projecting candidate rows.
6. Define exact spatial/entity ordering and catalog binding rules.
7. Only then author the machine-readable feature manifest with stable IDs, encodings, shapes, normalization, missingness, hashes, and consumer map.

## 7. Architecture reconstruction review

1. **Prior problem:** source-map intended consumers and legacy tensor consumers could be mistaken for an approved target Actor/Critic layout.
2. **Technical rationale:** legacy consumers describe the old implementation; target consumers must follow canonical ownership, provenance, masks, and semantic distinctions.
3. **New responsibility:** this audit classifies each semantic field's projection eligibility and identifies where Actor/Critic allocation remains undecided.
4. **Contract/invariants:** no offsets/shapes/normalization selected; masks remain independent side inputs; diagnostic recommendations and Unified Shadow outputs are excluded; unavailable values remain unavailable.
5. **Cross-component impact:** Observation Schema/source map, strategic/economic producers, Engine bindings, PPO Actor/Critic, Action/Mask, checkpoint lineage, replay, and evaluation.
6. **Objective validation:** parsed all 77 source-map entries; reconciled 66 legacy feature definitions across 18 blocks and the 66-entry migration crosswalk; checked the current projection and Action/Mask boundaries. No runtime files changed.

## Follow-up decision matrix

The proposed [Observation Projection Consumer Matrix v1](observation-projection-consumer-matrix.v1.draft.md) refines this audit into one primary disposition for each of the 77 semantic source-map fields and extends the 66-entry legacy crosswalk with target consumer intent. This follow-up remains a proposal: it does not approve tensor encoding, normalization, shape, offsets or architecture. The current audit remains the evidence inventory; the matrix is the proposed semantic consumer decision layer.
