# Schema v2 Derived Context Exact-Path Source Proof v1 — Draft

**Status:** source-backed validation of 19 exact source-map matches; documentation only.  
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).  
**Base:** `new-arquiteture`.

## 1. Scope

This slice validates 19 exact source-map paths:
- positioning (2);
- trait counts (2);
- capacity (2);
- economic context (11);
- decision-history action count/budget (2).

An exact path match in the v1 source map is only an index into a possible producer. This audit checks the actual callsite, formula, serialization surface and PPO projection.

## 2. Positioning and trait counts

### 2.1 Positioning

`BoardEvaluationResult` contains positional, structural, synergy and total scores plus unit/frontline/carry/exposure/trait diagnostics (`BoardEvaluation.hpp:24-48`). TftEngine computes the board evaluation from the current board and emits:
- total positioning score;
- frontline ratio;
- backline ratio;
- unique-role diversity ratio

into four fixed PPO scalars (`TftEngine.cpp:1443-1448`). The audit snapshot separately exposes positioning/board-quality/positional/structural scores and selected board diagnostics (`TftEngine.cpp:6719-6728`).

No typed `derived_context.positioning` map is serialized. The schema's generic dynamic map cannot be treated as if every BoardEvaluationResult field were present. The board geometry remains the internal 4×7 rectangular slot mapping described in the trait/position producer audit; this does not prove canonical TFT hex geometry.

### 2.2 Trait counts

The observation builder's `count_traits` lambda iterates `ChampionDefinition::traits` for each occupied board and bench UnitInstance, preserving first-seen insertion order. It does not add item-granted traits in this PPO count path. The five-value SYNERGY block takes the first five accumulated traits and divides counts by five; the later fixed trait block uses catalog-derived `observation_trait_names`, also divides by five and clamps to one (`TftEngine.cpp:1292-1314,1436-1459`).

This is distinct from:
- board-only active traits, which union catalog traits with item-granted traits per physical UnitInstance;
- board+bench owned/core trait counts, which also include item-granted traits;
- champion-deduplicated reward helper counts.

The trait audit records these scope differences and the missing catalog-order fingerprint. Neither `trait_counts` nor its generic child is serialized as a typed map; PPO receives fixed numeric blocks.

## 3. Capacity

The observation builder emits exactly two normalized capacity features:
- remaining board capacity: `max(0, economy.level - board_count) / 9`;
- free bench slots: `(kBenchSlots - bench_count) / 9`.

The code writes these at the fixed CAPACITY block (`TftEngine.cpp:1301,1461-1464`). It does not serialize a named `capacity{}` map or dynamic key/value object. The values are lossy normalized features: the raw counts and semantic key names are not carried as typed fields.

## 4. Economic context

### 4.1 Produced current-state values

- **Stage:** `stage_for_round` maps rounds 1–4 to stage 1, then seven-round stage windows (`TftEngine.cpp:139-144`). The current stage is assigned to StrategicSharedContext. The Python policy also reconstructs stage from the normalized round feature in `_economic_context_features`; it is not a separate PPO field (`TftEngine.cpp:3195-3200`; `policy.py:306-324`).
- **Interest if resolved now:** `EconomyEngine::get_interest(gold)` is assigned to StrategicSharedContext and audit snapshot. It is diagnostic/context data, not a separate PPO observation feature (`TftEngine.cpp:3205-3206,6713`).
- **Board power:** the Engine sums `champion cost × star × 2` over occupied board units. It stores this in PlayerInfo/audit snapshot and passes it to the Shadow context (`TftEngine.cpp:2061-2072,3209,6714`).
- **Lobby average board power:** arithmetic mean of `board_power` over living players; if none are alive, the current player's power is used (`TftEngine.cpp:3237-3245`).
- **Relative board power:** current player's board power divided by the lobby mean when positive; otherwise 1.0 (`TftEngine.cpp:3244-3248`).

The lobby average and relative value are in the Shadow context and feed EconomicController. They are not emitted as typed PPO fields.

### 4.2 Pressure outputs and missing inputs

`EconomicController::evaluate` derives:
- `hp_pressure = clamp01((70 - hp)/70)`;
- `incoming_pressure = clamp01(estimated_incoming_damage/18)`;
- `elimination_pressure = clamp01(elimination_risk)`;
- `survival_pressure = clamp01(0.50*hp_pressure + 0.25*incoming_pressure + 0.25*elimination_pressure)`;
- `board_pressure = clamp01((1.05-relative_board_power)/0.75)`;
- `economy_pressure = clamp01((gold-30)/50)`.

These outputs are copied into PlayerInfo as economic survival, board and resource pressure diagnostic fields (`EconomicController.hpp:14-35`; `TftEngine.cpp:4192-4201`). They are Shadow-only diagnostic outputs and do not enter the PPO observation vector.

**Critical correction:** the audited TftEngine context builder does not assign `estimated_incoming_damage` or `elimination_risk`. Both fields retain the zero defaults declared in `StrategicSharedContext` (`StrategicPlanning.hpp:147-154`; `TftEngine.cpp:3195-3217`). Therefore the current survival-pressure value uses the HP term plus zero-valued incoming/elimination terms. Those zeros are defaults, not observed evidence that incoming damage or elimination risk is zero.

### 4.3 Unproduced projection

`projected_next_round_income` is declared in StrategicSharedContext with a zero default, but the audited TftEngine context construction does not assign it. No projected-income producer was found in this callsite. It must remain unavailable/unknown, not numeric zero.

## 5. Decision-history action count and budget

Each player has an internal `actions_taken_this_round` counter. It increments on each action and resets at round/episode boundaries (`TftEngine.cpp:428,1220,4844-4846`). The PPO observation does not emit the raw count. Instead, the temporal memory block emits:
`(10 - min(actions_taken_this_round, 10)) / 10`
using `kActionMemoryHorizon = 10`, followed by 28 normalized board-move-age values (`TftEngine.cpp:123-124,1510-1522`).

Thus:
- `actions_taken_this_round` exists internally, not as a raw Python/PPO field;
- `remaining_action_budget` is represented only by a normalized remaining-horizon scalar, not an exact integer;
- the feature is not a typed decision event sequence.

## 6. Field-level dispositions

| Schema path | Producer and formula | Python/PPO delivery | Disposition |
|---|---|---|---|
| `derived_context.positioning` | BoardEvaluationResult from current board | Audit snapshot diagnostics; four PPO scalars | `board_evaluation_and_flat_projection` |
| `derived_context.positioning{}` | Selected BoardEvaluation metrics | No typed map; selected flat metrics only | `selected_board_evaluation_fields` |
| `derived_context.trait_counts` | Board+bench catalog trait accumulation | Fixed catalog-order trait blocks | `board_bench_catalog_trait_counts` |
| `derived_context.trait_counts{}` | Individual trait count, normalized by five/clamped | Fixed numeric feature per catalog trait | `catalog_trait_count_entries_internal` |
| `derived_context.capacity` | Board level capacity and free bench slots | Two normalized PPO scalars | `two_flat_capacity_features` |
| `derived_context.capacity{}` | `max(0, level-board_count)/9`; `(9-bench_count)/9` | Two fixed positions, no named map | `derived_capacity_scalar_entries` |
| `derived_context.economic_context.stage` | `stage_for_round(round)` | Policy derives stage from round fraction | `stage_for_round_native_formula` |
| `derived_context.economic_context.interest_if_resolved_now` | EconomyEngine.get_interest(gold) | Audit snapshot only | `economy_engine_get_interest` |
| `derived_context.economic_context.projected_next_round_income` | Context field remains default zero | Not delivered | `default_zero_unpopulated_context_field` |
| `derived_context.economic_context.board_power` | Sum(cost×star×2) over board | PlayerInfo/audit snapshot | `board_power_cost_star_heuristic` |
| `derived_context.economic_context.lobby_average_board_power` | Mean power over living lobby | Shadow context only | `mean_alive_player_board_power` |
| `derived_context.economic_context.relative_board_power` | Own power / lobby mean, fallback 1.0 | Shadow context only | `board_power_divided_by_lobby_mean` |
| `derived_context.economic_context.estimated_incoming_damage` | Context default zero; no producer assignment | Not delivered | `default_zero_unpopulated_context_field` |
| `derived_context.economic_context.elimination_risk` | Context default zero; no producer assignment | Not delivered | `default_zero_unpopulated_context_field` |
| `derived_context.economic_context.survival_pressure` | EconomicController formula using HP + default-zero incoming/elimination | PlayerInfo/pybind step diagnostics | `economic_controller_derived_shadow_pressure` |
| `derived_context.economic_context.board_pressure` | Relative-power pressure formula | PlayerInfo/pybind step diagnostics | `economic_controller_relative_power_pressure` |
| `derived_context.economic_context.economy_pressure` | Gold pressure formula | PlayerInfo/pybind step diagnostics | `economic_controller_gold_pressure` |
| `derived_context.decision_history.actions_taken_this_round` | Internal per-round action counter | Not emitted raw | `internal_action_counter` |
| `derived_context.decision_history.remaining_action_budget` | Remaining horizon normalized by 10 | One flat PPO scalar | `normalized_remaining_action_horizon` |

## 7. Non-equivalences and invariants

1. BoardEvaluationResult is not a serialized `positioning{}` map.
2. Board+bench catalog trait counts are not board-only item-adjusted active traits.
3. Capacity scalars are not an exact named capacity object.
4. Default-zero incoming damage/elimination risk are not observed zero facts.
5. Economic pressure outputs are Shadow diagnostics, not PPO policy inputs.
6. Remaining action horizon is normalized scalar context, not an exact decision budget or event history.
7. Exact source-map path equality is not proof of consumer delivery.

## 8. Remaining proof

- Validate the remaining exact strategic-evidence paths, especially progression, pressure, uncertainty, commitment context and focus weights.
- Trace each PlayerInfo diagnostic through pybind and Python wrapper, then prove whether it reaches Trainer/rollout or is diagnostic-only.
- Complete Actor/Critic leaf allocation; this slice only establishes the fixed observation and diagnostic surfaces.
- Preserve unknown/default distinctions for projected income, incoming damage and elimination risk.

Issue #346 remains open. No runtime, schema, tensor, PPO, reward, mask, training, checkpoint or Viewer changes.

## 9. Architecture reconstruction review

1. **Prior problem:** exact source-map matches were treated as sufficient proof even where the object was only a flat vector, a Shadow diagnostic or an unpopulated default.
2. **Technical justification:** trait scope, capacity normalization, economic pressure inputs and temporal budgets differ across native state, diagnostic context and PPO features.
3. **New responsibility:** this audit owns the field-level source/formula/delivery proof for 19 derived-context paths.
4. **Contract and invariants:** no fabricated structured maps; no default-zero as observed fact; trait scopes remain distinct; pressure values remain heuristic Shadow diagnostics; masks remain separate.
5. **Cross-component impacts:** TftEngine, BoardEvaluation, ChampionCatalog, TraitMilestones, EconomyEngine, EconomicController, PlayerInfo, pybind, Python policy encoder, source map and Schema v2.
6. **Objective validation:** all 19 exact paths have source callsite/formula and consumer classification; no runtime or tensor-layout changes.

