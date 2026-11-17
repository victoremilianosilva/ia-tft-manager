# Schema v2 Action Opportunity and Temporal Field Proof v1 — Draft

**Status:** source-backed field-level audit; documentation only, not runtime-approved.  
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).  
**Base:** `new-arquiteture`.

## 1. Scope

This slice audits 17 paths:
- 16 fields nested under `derived_context.action_opportunity.items[]`;
- `derived_context.decision_history.board_move_age_by_slot[]`.

It reconciles the approved Strategic Action Candidate Contract with the current native producer path and distinguishes legacy slot-local PPO features from a real candidate collection.

## 2. Action opportunity: DTO capability is not a populated producer

`StrategicSharedContext` declares `action_candidates`, and `StrategicActionCandidate` has candidate kind, champion ID, gold cost, direct spend, lost interest, opportunity cost, expected economy/board effects, composition fit, upgrade value and availability (`StrategicPlanning.hpp:88-100,135-167`). However, the audited `TftEngine.cpp` construction block initializes `StrategicSharedContext` and builds owned-unit/anchor/candidate-generation evidence without appending any `action_candidates` rows. The later comparison reads `strategic_context.action_candidates.size()`; the audited path therefore passes an empty source vector to baseline and contextual evaluators (`TftEngine.cpp:3195-3217,3250-3360,3816-3865`).

The Strategic Action Candidate Contract explicitly requires a non-empty, correlated, snapshot-bound candidate set and distinguishes `no_candidates` from valid comparison/HOLD. It also requires exact physical parameters and per-candidate cost/benefit/provenance. Those conditions are not met by the current empty source vector.

### Legacy slot features are separate data

The current PPO candidate tail emits eight slot-aligned values for each bench/shop slot. They include composition fit, cost, star, role, core flag, owned-copy count, upgrade signal, and either sell value (bench) or affordability (shop). Sell value is calculated by `EconomyEngine::get_sell_value` and normalized by 50; shop affordability is a boolean comparison of gold against champion cost (`TftEngine.cpp:1783-1827`).

These features are not `StrategicActionCandidate` rows:
- no candidate ID/revision/set identity;
- no action kind or exact source/target parameters;
- no per-candidate source sequence;
- no candidate-bound direct/lost-interest/opportunity-cost decomposition;
- no per-candidate evaluation horizon;
- no typed physical unit UUID reference.

Likewise, aggregate `ActionEvaluation` diagnostics written into PlayerInfo are separate from candidate records. They cannot be expanded into per-candidate values when the source candidate vector is empty.

## 3. Decision history: board move age is a scalar temporal feature

Each PlayerEnv stores `board_move_age[28]` and `actions_taken_this_round`. At the start of an action, the action counter increments (capped at the configured horizon), each occupied board slot's age increments, and empty slots are set to the horizon. A successful deploy/move resets the destination slot age to zero; a move/swap also updates the source slot age appropriately (`TftEngine.cpp:424-429,4844-4853,5246-5248,5331-5337`).

The observation builder emits normalized remaining action horizon and one normalized age per board slot (`TftEngine.cpp:1510-1522`). The Python wrapper returns the native reset/step observation array to the trainer (`cpp_lobby_env.py:120-145`).

This is a real 28-slot temporal feature, but it is not a typed ordered decision history:
- no per-event decision ID or action record;
- no source decision sequence namespace;
- no action outcome or reason per event;
- slot age is not physical-unit identity;
- it does not serialize the internal AntiLoopHistory.

Episode reset initializes board ages to the horizon and resets the action counter (`TftEngine.cpp:1219-1221`). The feature's semantics are slot-local age since the last placement/move, capped by the configured action-memory horizon; it must not be reinterpreted as a general event ledger.

## 4. Field-level dispositions

| Schema path | Evidence | Python/PPO boundary | Disposition |
|---|---|---|---|
| `derived_context.action_opportunity.items[].candidate_id` | No populated source candidate rows or stable IDs | No candidate record | `not_produced_empty_candidate_collection` |
| `derived_context.action_opportunity.items[].action_kind` | Enum exists; no candidate rows | No candidate record | `not_produced_empty_candidate_collection` |
| `derived_context.action_opportunity.items[].champion_id` | Champion IDs exist in slots, not action-candidate rows | Legacy slot features only | `not_produced_as_action_candidate` |
| `derived_context.action_opportunity.items[].unit_instance_id` | No UUID-bound action candidate | No candidate UUID | `not_produced_physical_candidate_reference` |
| `derived_context.action_opportunity.items[].gold_cost` | Candidate DTO field only; source vector empty | No per-candidate cost | `not_produced_per_candidate` |
| `derived_context.action_opportunity.items[].direct_gold_cost` | Aggregate action diagnostics are separate | No per-candidate breakdown | `not_produced_per_candidate` |
| `derived_context.action_opportunity.items[].lost_interest_cost` | Aggregate action diagnostics are separate | No per-candidate breakdown | `not_produced_per_candidate` |
| `derived_context.action_opportunity.items[].opportunity_cost` | Aggregate action diagnostics are separate | No per-candidate breakdown | `not_produced_per_candidate` |
| `derived_context.action_opportunity.items[].expected_economy_cost` | Aggregate action diagnostics are separate | No per-candidate breakdown | `not_produced_per_candidate` |
| `derived_context.action_opportunity.items[].expected_board_delta` | Aggregate action diagnostics are separate | No per-candidate breakdown | `not_produced_per_candidate` |
| `derived_context.action_opportunity.items[].composition_fit` | Legacy slot-tail fit scalar exists | Not candidate-bound | `legacy_slot_composition_fit_scalar` |
| `derived_context.action_opportunity.items[].upgrade_value` | Legacy slot-tail upgrade signal exists | Not candidate-bound | `legacy_slot_upgrade_signal_scalar` |
| `derived_context.action_opportunity.items[].available` | Candidate DTO field only; no rows | Native masks remain separate | `not_produced_per_candidate` |
| `derived_context.action_opportunity.items[].evaluation_horizon` | No per-candidate horizon producer | Not delivered | `not_produced` |
| `derived_context.action_opportunity.items[].sell_value` | Legacy bench-slot sell value | Numeric slot feature, not candidate record | `legacy_slot_sell_value_only` |
| `derived_context.action_opportunity.items[].affordability` | Legacy shop-slot gold-vs-cost boolean | Numeric slot feature, not candidate record | `legacy_shop_slot_affordability_only` |
| `derived_context.decision_history.board_move_age_by_slot[]` | Native 28-slot age array | Normalized flat PPO features via reset/step | `observed_slot_age_flat_temporal_feature` |

## 5. Non-equivalences and invariants

1. A candidate DTO definition is not a populated candidate producer.
2. An empty candidate set is not a valid comparison, HOLD, or zero-cost opportunity.
3. Legacy slot features do not become action candidates by semantic similarity.
4. Aggregate ActionEvaluation values are not per-candidate cost/benefit records.
5. Native masks remain independent final legality inputs.
6. Board move age is slot-local temporal context, not a typed decision timeline.
7. Board slot index/age is not physical UnitInstance identity.

## 6. Remaining proof

- Keep action opportunity unavailable until a real producer creates non-empty, immutable, sequence-bound candidate sets with exact parameters.
- Trace the legacy slot-tail features through policy/Actor consumers separately; do not alias them to Schema v2 action-candidate fields.
- Define a typed temporal history producer only if the target contract still requires event-level history; do not inflate board ages into synthetic events.
- Complete anti-loop history and mask-reference field audit separately.
- Complete exact 43 source-map callsite checks and Actor/Critic leaf allocation.

Issue #346 remains open. No runtime, schema, tensor, PPO, reward, mask, training, checkpoint or Viewer changes.

## 7. Architecture reconstruction review

1. **Prior problem:** action-opportunity schema fields inherited availability from a parent despite an empty candidate source; the decision-history path risked conflating slot ages with event history.
2. **Technical justification:** legacy slot features and aggregate evaluator outputs do not provide candidate identity, exact physical parameters, source sequence or per-candidate cost/benefit; slot age does not preserve ordered decisions.
3. **New responsibility:** this audit owns the field-level boundary for action-opportunity candidates and the current board-move-age feature.
4. **Contract and invariants:** no fabricated candidates or horizons; no zero-default substitution; masks remain separate; temporal age remains slot-scoped.
5. **Cross-component impacts:** StrategicSharedContext, ActionCandidate contract, baseline/contextual evaluators, TftEngine observation builder, EconomyEngine sell-value helper, pybind, Python wrapper, policy candidate tail, PPO rollout and replay.
6. **Objective validation:** all 17 paths are mapped to source callsites or explicit absence/legacy-only status; source vector is empty; 28 age features are emitted; no runtime or tensor-layout change.

