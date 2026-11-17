# Schema v2 Strategic Evidence Exact-Path Source Proof v1 — Draft

**Status:** source-backed validation of the remaining 24 exact source-map matches; documentation only.  
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).  
**Base:** `new-arquiteture`.

## 1. Scope

This slice validates 24 exact source-map paths across:
- progression (2);
- pressure (2);
- uncertainty (2);
- commitment context (16);
- completed traits (1);
- focus weights (1).

The exact source-map entry was treated as a lead, not proof. The audit follows the actual StrategicSharedContext construction, StrategicEvidenceContextBuilder, StrategicPlanner mutation, PlayerInfo mirrors and PPO observation projection.

## 2. Progression, pressure and uncertainty maps

### 2.1 Progression is not populated by the current new-evidence callsite

`StrategicSharedContext.progression_plan` defaults to `ProgressionPlan::Flexible`. `StrategicCommitment.progression` also defaults to Flexible. The audited TftEngine builder does not assign either field, and the audited StrategicPlanner does not mutate either field. The planner's progression enum is therefore a default, not an observed plan. The legacy economic strategy is a different enum/decision and must not be silently aliased to the new progression plan (`StrategicPlanning.hpp:135-167,169-183`; `TftEngine.cpp:3195-3217`; `StrategicPlanner.hpp:46-205`).

The EconomicController consumes `StrategicSharedContext.progression_plan` to weight LevelToEight/LevelToNine/RerollForThreeStar plans. Since the current callsite leaves it Flexible, those progression-specific weights remain inactive. This is a concrete integration gap, not proof that Flexible is the intended plan.

No typed `strategic_evidence.progression{}` map is constructed.

### 2.2 Pressure outputs exist as separate diagnostics, not a pressure map

The EconomicController emits three scalar pressure values: survival, board and economy. TftEngine copies them to PlayerInfo fields and pybind exposes those fields as step diagnostics (`EconomicController.hpp:22-35`; `TftEngine.cpp:4192-4201`; `tft_engine_bindings.cpp:353-359`). These are not a `strategic_evidence.pressure{}` map and are not PPO observation fields.

The derived-context audit also established that incoming damage and elimination risk remain default-zero inputs. Thus survival pressure is currently an HP-driven heuristic plus zero-valued incoming/elimination terms, not a complete risk estimate.

### 2.3 Confidence is not an uncertainty map

The StrategicPlanner computes heuristic confidence from candidate/current direction scores and stores confidence on selected commitment branches. It does not construct a per-field or per-source uncertainty map. Confidence is a bounded heuristic score, not a calibrated probability, uncertainty interval or evidence-quality metric (`StrategicPlanner.hpp:62-66,73-77,285-287`; `StrategicPlanning.hpp:169-183`).

No typed `strategic_evidence.uncertainty{}` entries are produced.

## 3. Commitment context field-by-field

### 3.1 Direction and identity

TftEngine reads `strategic_planner_commitments[i].composition_direction` as the committed direction label. It separately constructs `direction_identity = "direction:v2:" + direction` and sets the literal source string `per_player_strategic_commitment` (`TftEngine.cpp:3363-3374`). These are internal StrategicEvidenceContext values, not Python/PPO inputs.

The active generated composition has its own `composition_identity` (native generated candidate identity). It is distinct from `direction:v2:<direction>` and from physical UnitInstance identity. Neither string is a stable candidate-set ID/revision.

### 3.2 Progression and unit lists

- `progression_plan`: remains default Flexible; neither context builder nor planner assigns it.
- `core_unit_ids`: copied from `active_native_direction.unit_ids`, which are champion/catalog IDs, not physical UnitInstance UUIDs. The builder stores them in `derived_core_unit_ids`; it does not create physical-unit references.
- `flexible_unit_ids`: the field exists in StrategicCommitment, but the audited TftEngine/StrategicPlanner path never assigns it.

### 3.3 Commitment lifecycle fields

- `selected_round`: set when the planner first selects a direction or synchronizes a changed current direction with the commitment.
- `last_review_round`: updated when an alternative candidate is reviewed.
- `selection_reason`: set on initial selection and selected pivot/abandon branches; it is not a complete reason for every KEEP/ADAPT cycle.
- `revision_condition`: declared on StrategicCommitment but never assigned in the audited path.
- `confidence`: commitment confidence is assigned on selected pivot branches, but not on initial selection/KEEP. PlayerInfo's `strategic_confidence` mirrors `shadow_decision.confidence`, which is a different decision-level field.
- `consecutive_reviews`: counts persistence of the current alternative candidate and is reset by `clear_candidate`; it is not a general commitment age or decision sequence.

TftEngine mirrors selected round, last review round and candidate streak into PlayerInfo step diagnostics, but does not serialize the complete StrategicCommitment object. The pybind output is diagnostic telemetry, not a PPO observation (`TftEngine.cpp:4290-4317`; `tft_engine_bindings.cpp:345-352`).

### 3.4 Composition identity, score, viability and lock

- `composition_identity`: copied from the active native generated direction candidate. It is not the direction identity string and does not carry a candidate revision.
- `current_direction_score`: copied from the active generated candidate's heuristic score; PlayerInfo mirrors this as a Shadow diagnostic.
- `current_direction_viable`: true when a generated candidate exists for the committed direction; this is a candidate-presence test.
- `composition_locked`: TftEngine explicitly assigns false to the new StrategicSharedContext, and StrategicEvidenceContextBuilder assigns false again (`TftEngine.cpp:3210-3217`; `StrategicEvidenceContext.hpp:103-110`). This does not read an authoritative lock producer. Per the strategic ownership contract, lock must be unknown/unavailable when no authoritative producer is wired; this false value must not be treated as observed unlocked state.

### 3.5 Completed traits and focus weights

TftEngine copies `active_native_direction.completed_traits` into `StrategicEvidenceContextInput.focus_traits`. The builder stores them as `derived_focus_traits`, `current_core_traits` and first-trait focus. They are generated candidate traits, not observed active board synergies or item-adjusted board trait counts (`TftEngine.cpp:3375-3382`; `StrategicEvidenceContext.hpp:69-110`).

No independent `focus_weights` map is populated in the new evidence callsite. A separate legacy `StrategyInfo.composition_focus_weights` map is still projected into the PPO observation in fixed catalog trait order and normalized from [0,10] to [0,1] (`TftEngine.cpp:1524-1540`). This legacy flat feature is not the new typed strategic-evidence focus-weight map.

## 4. Field-level dispositions

| Schema path | Native producer/evidence | Python/PPO surface | Disposition |
|---|---|---|---|
| `strategic_evidence.progression` | ProgressionPlan defaults Flexible; no assignment | No structured progression export | `no_progression_plan_producer_default_flexible` |
| `strategic_evidence.progression{}` | No typed progression map | No map delivery | `no_typed_progression_map` |
| `strategic_evidence.pressure` | EconomicController has separate pressure scalars | PlayerInfo/pybind diagnostics | `no_structured_pressure_map` |
| `strategic_evidence.pressure{}` | Scalar pressure values only | Not delivered as a map | `separate_scalar_pressures_only` |
| `strategic_evidence.uncertainty` | No uncertainty map producer | Heuristic confidence fields only | `no_uncertainty_map_producer` |
| `strategic_evidence.uncertainty{}` | No typed uncertainty entries | No map delivery | `no_uncertainty_map_entries` |
| `strategic_evidence.commitment_context.direction_id` | Committed direction string | PlayerInfo committed-direction diagnostic | `committed_direction_label` |
| `strategic_evidence.commitment_context.direction_identity` | `direction:v2:<direction>` | Internal evidence context only | `derived_direction_identity_string` |
| `strategic_evidence.commitment_context.progression_plan` | Default Flexible; no assignment | Not exported | `default_flexible_no_assignment` |
| `strategic_evidence.commitment_context.core_unit_ids` | Active native generated candidate champion IDs | Internal evidence context only | `active_native_candidate_champion_ids` |
| `strategic_evidence.commitment_context.flexible_unit_ids` | Declared but never populated | No export | `not_populated_commitment_field` |
| `strategic_evidence.commitment_context.selected_round` | StrategicPlanner sets on initial/changed direction | PlayerInfo step diagnostic | `planner_commitment_selection_round` |
| `strategic_evidence.commitment_context.last_review_round` | StrategicPlanner candidate review round | PlayerInfo step diagnostic | `planner_candidate_review_round` |
| `strategic_evidence.commitment_context.selection_reason` | Set on selected initial/pivot/abandon branches | Separate decision reason, not same field | `internal_commitment_selection_reason` |
| `strategic_evidence.commitment_context.revision_condition` | Declared but never assigned | No export | `never_assigned_commitment_default` |
| `strategic_evidence.commitment_context.confidence` | Partial commitment confidence on pivot branches | PlayerInfo confidence is decision-level confidence | `partial_commitment_confidence_only_on_pivot` |
| `strategic_evidence.commitment_context.consecutive_reviews` | Candidate persistence counter | PlayerInfo candidate streak diagnostic | `planner_candidate_persistence_counter` |
| `strategic_evidence.commitment_context.direction_source` | Literal provenance string | Internal evidence context only | `literal_per_player_strategic_commitment` |
| `strategic_evidence.commitment_context.composition_identity` | Active native generated composition identity | Partial candidate diagnostic only | `active_native_direction_composition_identity` |
| `strategic_evidence.commitment_context.current_direction_score` | Active native candidate heuristic score | PlayerInfo step diagnostic | `active_native_direction_heuristic_score` |
| `strategic_evidence.commitment_context.current_direction_viable` | Active generated candidate presence | PlayerInfo step diagnostic | `active_native_candidate_presence` |
| `strategic_evidence.commitment_context.composition_locked` | Hardcoded false in context and builder | No authoritative lock source | `hardcoded_false_not_authoritative_lock` |
| `strategic_evidence.completed_traits` | Active generated candidate completed traits | Internal derived-focus context | `active_generated_candidate_completed_traits` |
| `strategic_evidence.focus_weights` | No new evidence source; legacy StrategyInfo focus weights exist | Legacy flat PPO trait-weight block | `legacy_strategy_focus_weights_only` |

## 5. Non-equivalences and invariants

1. Legacy economic strategy is not the new ProgressionPlan.
2. A default Flexible enum is not evidence of an explicit flexible progression choice.
3. Scalar EconomicController pressure outputs are not a typed pressure map.
4. Heuristic confidence is not an uncertainty measure or calibrated probability.
5. Direction label, direction identity, composition identity, candidate ID and physical UnitInstance ID are distinct.
6. Champion-ID core lists are not physical unit-instance lists.
7. A false lock value hardcoded into a context is not authoritative unlocked state.
8. Generated completed traits are not observed active board traits.
9. Legacy focus-weight PPO scalars are not a new evidence-context focus-weight map.

## 6. Remaining proof

- Decide the correct future owner/producer for ProgressionPlan; do not map legacy strategy enums by name alone.
- Define pressure and uncertainty contracts only if they have real producers, explicit formulas, source sequence and quality.
- Resolve the hardcoded-false composition lock bridge before any runtime implementation; current contract requires unavailable/unknown without an authoritative producer.
- Decide whether commitment confidence and selection/revision reasons should be copied into immutable owner snapshots with explicit semantics.
- Trace PlayerInfo/pybind diagnostic mirrors through Python and confirm exclusion from Trainer/rollout/policy inputs; separately trace the legacy focus-weight feature through Actor/Critic.
- Complete the final Actor/Critic leaf-consumer proof and integrated replay.

Issue #346 remains open. No runtime, schema, tensor, PPO, reward, mask, training, checkpoint or Viewer changes.

## 7. Architecture reconstruction review

1. **Prior problem:** exact source-map matches obscured defaults, partially mutated commitment fields, generated versus observed traits, and legacy focus features versus new evidence.
2. **Technical justification:** the same names can refer to different owners, identity levels, score semantics and delivery channels; silent aliases would fabricate progression, pressure, uncertainty or lock facts.
3. **New responsibility:** this audit owns field-level source/formula/identity/delivery proof for the remaining strategic evidence paths.
4. **Contract and invariants:** no default as explicit choice; no confidence as uncertainty; no champion ID as physical ID; no hardcoded false as lock evidence; no legacy focus map as new evidence.
5. **Cross-component impacts:** StrategicSharedContext, StrategicCommitment, StrategicEvidenceContextInput/Builder, StrategicPlanner, NativeStrategicCompositionGenerator, EconomicController, StrategyInfo, PlayerInfo, pybind, PPO observation and replay.
6. **Objective validation:** all 24 remaining exact paths are individually classified against source construction, mutation and diagnostic export; no runtime or tensor-layout changes.

