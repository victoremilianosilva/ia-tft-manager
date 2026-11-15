# Observation Producer-to-PPO Binding Audit v1 — Draft

**Status:** documentary audit; no runtime changes and no target tensor layout approved.  
**Base:** `new-arquiteture`, commit `ac93943a5dc6515e302071fb6ef419a0b46cd8b7`.  
**Related contracts:** Observation Schema v1, Observation Tensor Projection Requirements v1, Feature-to-Consumer Audit v1, Strategic Ownership & Integration v1, Action/Mask Contract v1, PPO Architecture/Checkpoint Contract v1.

## 1. Executive result

The repository contains two distinct information paths:

1. **Current PPO path:** native `TFTEngine::build_observations()` creates the numeric observation vector. The Python wrapper returns that vector to the trainer. The trainer obtains action masks separately and passes both to `TFTPolicy`.
2. **Shadow path:** the native engine builds strategic/economic evidence, runs the StrategicPlanner and related evaluators, optionally runs the Composition Intelligence runtime, adapts a `StrategicContextBridgeSnapshot`, and records diagnostic JSON snapshots. This path is isolated from PPO observations, rewards, masks, and action execution.

Therefore, the current runtime does **not** yet feed canonical Shadow strategic evidence into PPO. The current PPO observation still contains several fields sourced from the older `StrategyInfo` pipeline. This is an explicit migration boundary, not a reason to copy old encodings into the new projection.

The next projection must consume validated canonical evidence from its actual producers, not Shadow recommendations, evaluator scores, or old StrategyInfo defaults.

## 2. End-to-end current PPO delivery chain

| Stage | Current implementation | What is delivered |
|---|---|---|
| Native state | `cpp/src/lobby/TftEngine.cpp::Impl::build_observations()` | One flat float vector per player, row-major lobby output |
| Native reset/step result | `cpp/include/lobby/TftEngine.hpp`, `cpp/bindings/tft_engine_bindings.cpp` | Observations, action masks, episode/round metadata, and step result fields |
| Python wrapper | `cpp_lobby_env.py::reset/step` | Reset returns observations only; step returns observations/rewards/dones/info |
| Mask retrieval | `cpp_lobby_env.py::get_action_masks` called through trainer `env_method` | Native legality masks fetched separately from the current environment state |
| Trainer | `trainer.py` | Flattens observations and masks; calls policy with both |
| Policy | `policy.py::TFTPolicy` | Actor action heads use masks; shared encoder produces features for policy and value heads |
| Rollout | `rollout.py` | Stores observation, action, log-probability, value, reward, done/valid flags, and mask tensors |

### 2.1 Binding and wrapper facts

- Native `reset_to_dict` includes `observations`, `action_masks`, `episode_id`, and `observation_dim`.
- Native `step_to_dict` includes `observations`, `action_masks`, rewards, dones, episode ID, round, stage, players, and events.
- `CppTFTLobbyWrapper.reset()` returns only `result["observations"]`; reset masks are not returned to the trainer through this wrapper method.
- `CppTFTLobbyWrapper.step()` returns observations, rewards, done, and an info dictionary. It does not put the native step masks or a typed decision-sequence identity in that returned tuple.
- During each training step, `Trainer` calls `env_method("get_action_masks")` separately, validates/reshapes the masks, and passes them to the policy.
- The rollout stores masks alongside the transition, but there is no explicit observation-sequence token in the PPO observation tensor/rollout contract proving that the separately fetched mask and observation share the same native decision identity.

The current synchronous vector-environment loop may keep these reads aligned operationally, but the target contract requires explicit match/player/round/sequence correlation and stale rejection. Do not infer a typed sequence guarantee from call ordering alone.

### 2.2 Current Actor/Critic mask behavior

- Action heads apply masks during sampling.
- `evaluate_actions` applies masks while recomputing action log-probabilities.
- `TFTPolicy.get_value(obs, masks=None)` explicitly ignores masks and evaluates `value_head(encode(obs))`.
- The shared actor/value encoder consumes the flat observation. Exact masks are not currently a Critic side input.

This is a current implementation gap against the target Action/Mask contract: exact decision-correlated masks must be supplied independently to Actor and Critic (or through a provably lossless encoding); any additional Markov/history context is additive and cannot replace masks.

### 2.3 Current Actor/Critic item-compatibility split

The shared encoder does not consume every observation sub-block. `TFTPolicy.encode()` removes `item_compatibility_observation_dim` from the middle/global block before constructing `global_part` (`policy.py:271-304`). The semantic item-global block remains in the shared encoder: component features, nine inventory semantic rows, one hundred recipe semantic rows and thirty-seven unit target-profile rows.

The Actor separately extracts the full item state with `_item_state_features()`, including the 9×37 inventory-target fit matrix and 100×37 recipe-target fit matrix (`policy.py:389-446`). The inventory action head consumes per-item fit summaries, the item-target head consumes selected inventory fit scores, and the recipe path consumes selected recipe fit scores (`policy.py:448-500,882-979`). The value head uses only `value_head(encode(obs))` (`policy.py:528-530,1008`).

Therefore, the current Critic receives item semantics and target profiles but not the exact item/recipe compatibility matrices. These matrices are current Actor-only inputs. This is an implementation fact, not a decision that the future Critic must permanently exclude them; any future change is gated and requires explicit Actor/Critic projection review.

## 3. Current observation producers

### 3.1 Global player/economy fields

Produced from native `PlayerEnv` and economy state:
- lifecycle/alive;
- HP;
- gold, level, XP;
- win/loss streak;
- round/stage-derived values;
- XP-to-next and interest derived by the native economy engine.

These are genuine native state inputs, but the current flat vector normalizes or transforms them inline. The new manifest must preserve semantic units and separately define normalization, missingness, and validity.

### 3.2 Board, bench, shop, traits, and positioning

Produced by `build_observations()` from:
- physical native board and bench slots;
- current native shop offers;
- champion catalog definitions and traits;
- role classification and board evaluation;
- item state where applicable.

The existing observation is not a lossless entity representation. It includes slot-aligned fixed features and aggregate trait features. It does not, by itself, preserve all physical unit-instance identity, exact ownership/copy recipes, or all provenance required by the new unit contract.

Trait ordering is derived from the loaded catalog's observation trait list. Any future categorical vocabulary must be bound to a stable catalog identity/order fingerprint; never treat internal catalog IDs as continuous scalars.

### 3.3 Existing PPO candidate-slot features are not Shadow action candidates

The current native observation appends fixed slot-local feature records for:
- each bench slot;
- each shop slot.

The current `TFTPolicy._candidate_features()` decodes these records into bench/shop candidate tensors, and the BUY/SELL heads score them. They are produced by the observation builder from native unit/shop state and include derived fit/upgrade/affordability signals.

These are **PPO observation feature rows for fixed physical slots**. They are not instances of `StrategicActionCandidate`, do not prove that the Shadow action-candidate producer exists, and do not satisfy the strategic-action candidate contract's stable candidate identity, candidate-set state, full physical parameters, cost/benefit, provenance, and sequence requirements.

Do not rename or reinterpret the old bench/shop feature tail as the missing Shadow candidate set.

### 3.4 Existing item features

The native observation builder reads the ItemEngine and item/champion catalogs to encode component counts, inventory semantics, recipes, target roles/stats, compatibility, and anvil options. Some compatibility values are heuristic fits. The new projection must preserve item identity, unit-instance target identity, catalog binding, and formula provenance; it must not promote a heuristic fit score to an observed fact. The current Actor receives inventory/recipe compatibility matrices through item-specific heads, while the Critic's shared encoder strips those matrices and retains only the semantic item/recipe/target-profile block.

## 4. Legacy StrategyInfo still present in PPO observations

The observation builder currently reads the last `player_envs[i].strategy` entry and encodes legacy-owned fields including:

- legacy strategy enum one-hot;
- `composition_direction`;
- `core_traits`;
- `composition_focus_weights`;
- `composition_locked`;
- `composition_strength`;
- `planned_main_carry_id` indirectly through unit role classification;
- planned composition information indirectly through unit-composition fit and item-target role features.

The Python policy also derives target-level/reserve/spendable-gold context from the old strategy one-hot and hard-coded phase rules in `_economic_context_features()`.

These are not proof that PPO consumes the canonical Shadow direction, active composition, economic posture, or strategic evidence contracts. They are legacy observation producers/derivations that must be replaced or deliberately reconstructed from canonical evidence during the authorized migration.

Do not preserve the old ECON/STABILIZE/FAST8/SLOWROLL/ALL_IN encoding merely to keep the old tensor shape. The old `StrategyInfo` pipeline is evidence for audit and migration mapping, not target authority.

## 5. Shadow producer chain and its current delivery boundary

### 5.1 Native strategic evidence

Within the native engine's shadow-isolated evaluation, the engine constructs `StrategicSharedContext` from current native player/economy/board/shop/catalog state and candidate generation.

Observed source facts include native HP, gold, level, XP, streaks, owned board/bench units, and shop snapshot. Derived/estimated values include:
- stage mapping;
- board-power estimate and lobby-relative power;
- direction score and viability;
- candidate unit contribution/fit values;
- composition generator scores and transition costs.

The current builder also constructs candidate-unit fields such as board contribution using a cost/star heuristic, composition fit using a direction/trait match, and item fit using equipped-item count. Those are estimates/heuristics, not observed combat contribution or item compatibility. Their formula identity and uncertainty must remain explicit if ever projected.

The `NativeStrategicCompositionGenerator` produces composition/anchor candidates (`StrategicAnchorCandidate` downstream), not `StrategicActionCandidate` rows.

### 5.2 StrategicPlanner, EconomicController, and action evaluators

- `StrategicPlanner` evaluates the strategic evidence context and returns KEEP/ADAPT/PIVOT/ABANDON/initial/insufficient-evidence decisions.
- `EconomicController` returns economic posture/progression evidence.
- Baseline and contextual action evaluators compare action proposals.
- Positioning planner proposes a concrete board destination when its inputs permit it.
- The native action resolver validates/resolves a proposal read-only; it does not apply a game action.

These are Shadow outputs and must remain excluded from PPO features, labels, imitation targets, and rewards. PPO may eventually consume validated **input evidence** that the planners also read, but not their recommendations, scores, rankings, confidence values, baseline outputs, or executor resolutions.

### 5.3 Composition Intelligence runtime availability

The Composition Intelligence runtime is opt-in through `TFT_COMPOSITION_INTELLIGENCE_SHADOW` (accepted values: `1`, `true`, `yes`). Its default is disabled when the variable is absent.

When enabled, the runtime produces per-player diagnostic snapshots and exposes them through `get_composition_diagnostics_jsonl()`. The Python wrapper exposes a corresponding diagnostic getter, but the standard trainer observation path does not merge these JSON snapshots into the PPO observation tensor.

The strategic planner/economic/action Shadow evaluation block is separately isolated by the native `run_shadow_isolated` boundary. The existence of the diagnostic sidecar does not imply PPO delivery.

### 5.4 StrategicContextBridge semantics and provenance gaps

The bridge emits separate observed, derived, and recommended sections with match/player/round/sequence and composition identity metadata. This is useful as a diagnostic contract, but current assignments require correction before it can be a PPO projection source:

- `composition_locked` is set as Observed from `StrategicSharedContext`, while the audited Shadow context construction currently initializes `strategic_context.composition_locked = false` and does not source the canonical active-composition owner's lock state. The legacy `StrategyInfo` pipeline has its own lock heuristic, but that is not proof of an authoritative Shadow lock producer. For this bridge snapshot, lock is **unknown/unavailable**, not observed false.
- `observed_direction` is populated from `strategic_planner_commitments[i].composition_direction`; that is a canonical StrategicPlanner commitment, not a raw observed game fact. Its origin must identify the commitment owner/state semantics (a derived/committed strategic state).
- `observed_focus` and `core_traits` are derived from the selected native generated direction candidate's completed traits. They must be labelled Derived, with the generator/candidate identity as source, not raw observed composition facts.
- stage, board power, relative power, direction score, and viability are derived and require formula/source identity.
- recommended direction, composition decision, economic posture, and confidence are correctly marked Recommended and remain excluded from PPO input.

A valid bridge envelope is not proof that every field inside it has valid field-level provenance. Validate field origin, quality, and source independently.

### 5.5 Sequence namespaces

The current code has distinct counters/identities for:
- engine episode/match identity;
- per-player strategic context sequence;
- Composition Intelligence runtime player sequence;
- global diagnostic snapshot sequence;
- active composition ID/version;
- PPO rollout timestep/batch position.

These must remain typed and must not be collapsed into one generic sequence. The PPO observation and separately fetched masks currently lack a decision-correlated identity envelope. A future projection adapter must bind observation, masks, evidence snapshot, and catalog identity to one exact decision identity before publishing any tensor.

## 6. Strategic action candidate producer gap

The native engine constructs `StrategicSharedContext` and passes it to both action evaluators. In the audited `TftEngine.cpp` path, no `push_back`, `emplace_back`, or assignment populates `strategic_context.action_candidates` before the evaluator/comparison calls.

The engine later compares:
- `strategic_context.action_candidates.size()`;
- baseline evaluator candidate count;
- contextual evaluator candidate count.

The source candidate set therefore remains empty in this audited construction path. A comparison or serialized diagnostic must not be treated as a valid candidate evaluation merely because evaluator objects returned a result. Candidate-set status must explicitly distinguish `no_candidates`, `comparison_unavailable`, and `comparison_available` under the approved candidate contract.

This does **not** mean the existing fixed bench/shop PPO candidate feature tail is empty; those are separate mechanisms described in §3.3.

## 7. Executor contract reconciliation finding

The current native diagnostic serialization reports:
- `executor_connected = true`;
- `execution_enabled = false`;
- `native_action_applied = false`.

The engine invokes the read-only resolver's `resolve()` method and records its per-request result. The constant `executor_connected` flag means the call path is wired/invoked; it does not prove that a particular proposal was accepted. Per-request `accepted` and validation/resolution reasons carry that outcome. Execution remains disabled and no native game action is applied. These lifecycle states must remain distinct.

## 8. Producer-to-consumer disposition

| Feature family | Current producer | Current PPO delivery | Shadow delivery | Projection status |
|---|---|---|---|---|
| Player lifecycle/health/economy/streak | Native PlayerEnv/EconomyEngine | Yes, legacy flat observation | Yes, strategic context | Candidate after provenance/sequence/normalization manifest |
| Board/bench/shop | Native UnitInstance/ShopEngine | Yes, fixed slot/aggregate features | Yes, evidence context | Candidate; preserve physical identity and ownership domains |
| Traits/catalog | ChampionCatalog + owned units | Yes, ordered aggregate features | Yes, generator/planner inputs | Candidate; require catalog fingerprints and stable vocabulary |
| Unit upgrade/copy evidence | Native board/bench units | Partial/heuristic legacy features | Partial strategic copies aggregation | Withhold until lossless per-instance/star-tier producer mapping |
| Items | ItemEngine + item catalog | Yes, semantic/fit blocks | Yes, selected evidence/profile paths | Candidate with exact item/unit relations and heuristic provenance |
| Positioning | Native board evaluation | Aggregate/heuristic features | Position proposal/diagnostics | Candidate only after spatial contract and formula provenance |
| Legacy strategy/direction/focus/lock | StrategyInfo/update_strategy | Yes, directly or indirectly | Not canonical Shadow output | Migrate; do not treat as canonical strategic context |
| Canonical direction/active composition | StrategicPlanner commitment + CI ActiveCompositionManager/generator | No | Yes, Shadow snapshots/bridge | Eligible evidence only after owner/sequence/provenance contract |
| Economic posture/progression | EconomicController | No | Yes, recommendation/diagnostics | Recommendation excluded; raw input evidence may be eligible |
| Action candidates | No producer found in audited engine construction | Separate PPO fixed-slot features exist | Strategic action candidate vector empty | Blocked; implement producer only after Gate 8 |
| Action masks | Native ActionMaskEngine | Yes, separate side input to Actor | Included in resolver state | Actor path exists; Critic side-input integration pending |
| History/anti-loop | Native action history/AntiLoopEngine | Some temporal fields in observation | Diagnostic/context bridge paths | Candidate; explicit horizon, reset, and Critic/Actor allocation needed |
| Shadow recommendations/scores | StrategicPlanner/EconomicController/evaluators | No | Diagnostic only | Permanently exclude from PPO features/targets/reward |

## 9. Required work before the concrete tensor manifest

1. Create a source-to-runtime binding map for all 77 semantic source-map fields: exact producer callsite, owner, field-level provenance, quality/missingness, identity, and sequence namespace.
2. Separate current legacy observation fields from canonical Shadow evidence in the migration map. Mark each legacy feature as replace, reconstruct, exclude, or retain only if independently justified.
3. Resolve bridge provenance defects for lock, direction, focus, and core traits. Unknown must remain unknown; commitment/generator-derived values must not be marked raw observed facts.
4. Define and test explicit observation/mask/evidence decision identity correlation. No reliance on incidental synchronous call order.
5. Resolve the missing `StrategicActionCandidate` producer and candidate-set status; do not reuse the fixed bench/shop PPO feature tail as a substitute.
6. Reconcile executor connected/resolved/execution-disabled documentation with runtime evidence.
7. Trace every eligible field through native serialization, Python wrapper, trainer, rollout, Actor and Critic. Fields not delivered to a declared consumer remain unavailable for projection.
8. Only after these proofs, create the machine-readable tensor projection manifest with stable feature IDs, actor/critic consumer declarations, shape/order, encodings, normalization, missingness, catalog hashes, and checkpoint identity.

## 10. Architecture reconstruction review

1. **Prior problem:** semantic source-map availability and Shadow diagnostics could be mistaken for proof that canonical strategic evidence already reaches PPO; legacy StrategyInfo fields were not separated clearly enough from new Shadow evidence.
2. **Technical rationale:** a field is projection-eligible only when its actual producer, owner, provenance, identity, sequence, serialization, and target consumer are proven. Legacy encodings and diagnostic outputs cannot establish the target design.
3. **New responsibility:** this audit owns the current producer-to-binding-to-consumer evidence map and the explicit boundary between legacy PPO observations and canonical Shadow evidence.
4. **Contract/invariants:** no runtime mutation; no Shadow recommendations/scores/rankings/confidence as PPO features or targets; exact masks remain separate and decision-correlated; unknown is not false/zero; fixed bench/shop PPO candidate rows are not StrategicActionCandidate records; actor and critic consumers are declared independently.
5. **Cross-component impact:** TFTEngine observation builder, StrategicPlanner/commitments, CompositionIntelligence runtime, StrategicContextBridge, ActionMaskEngine, pybind bindings, Python environment wrapper, trainer, policy, rollout, checkpoint, replay, and evaluation.
6. **Objective validation:** inspected the canonical branch tree and exact source files for native observation construction, pybind reset/step/getters, Python wrapper, trainer mask/observation flow, policy Actor/Critic paths, rollout storage, Shadow context construction, bridge serialization, candidate evaluator callsites, and diagnostic sidecar exposure. Confirmed 77 semantic source-map entries. No runtime files changed.


## Appendix A — All 77 semantic source-map entries against the current PPO path

This table prevents the source-map `availability` value from being misread as “already delivered to PPO.” The `current_source` column is taken from the canonical source map; the final column is the audited current binding result. “Partially delivered” means a lossy/derived legacy encoding exists, not that the canonical typed field is present.

| Semantic field | Source-map availability | Nature | Declared current source | Current PPO binding result |
|---|---|---|---|---|
| `player.lifecycle` | available | observed | `player_envs[i].info.alive` | Delivered in current flat PPO observation; normalized legacy encoding |
| `player.health` | available | observed | `player_envs[i].info.hp` | Delivered in current flat PPO observation; normalized legacy encoding |
| `player.economy.gold` | available | observed | `player_envs[i].economy.gold` | Delivered in current flat PPO observation; normalized legacy encoding |
| `player.economy.level` | available | observed | `player_envs[i].economy.level` | Delivered in current flat PPO observation; normalized legacy encoding |
| `player.economy.xp` | available | observed | `player_envs[i].economy.xp` | Partially delivered: XP is divided by XP-to-next; raw XP and denominator are not separate tensor fields |
| `player.economy.xp_to_next` | available | derived | `economy_engine.get_xp_to_next(economy)` | Folded into normalized XP ratio; not separately delivered |
| `player.streaks.win_streak` | available | observed | `player_envs[i].economy.win_streak` | Delivered in current flat PPO observation; normalized legacy encoding |
| `player.streaks.loss_streak` | available | observed | `player_envs[i].economy.loss_streak` | Delivered in current flat PPO observation; normalized legacy encoding |
| `derived_context.economic_context.stage` | available | derived | `current_stage / stage_for_round` | Partially represented through round fraction; typed stage is not separately delivered |
| `derived_context.economic_context.interest_if_resolved_now` | available | derived | `economy_engine.get_interest(economy.gold)` | Not delivered as this typed field; only gold and legacy derived context reach PPO |
| `derived_context.economic_context.projected_next_round_income` | not_produced | estimated | `StrategicSharedContext.projected_next_round_income` | Not delivered as a distinct typed feature; source-map status remains authoritative |
| `derived_context.economic_context.board_power` | available | estimated | `power / board_power(i)` | Not delivered as these typed fields; other board/positioning heuristics are not equivalent |
| `derived_context.economic_context.lobby_average_board_power` | available | estimated | `average board_power(other) over alive opponents` | Not delivered as these typed fields; other board/positioning heuristics are not equivalent |
| `derived_context.economic_context.relative_board_power` | available | derived | `board_power / lobby_average_board_power` | Not delivered as these typed fields; other board/positioning heuristics are not equivalent |
| `derived_context.economic_context.estimated_incoming_damage` | not_produced | estimated | `StrategicSharedContext.estimated_incoming_damage` | Not delivered as a distinct typed feature; source-map status remains authoritative |
| `derived_context.economic_context.elimination_risk` | not_produced | estimated | `StrategicSharedContext.elimination_risk` | Not delivered as a distinct typed feature; source-map status remains authoritative |
| `entities.board` | available | observed | `player_envs[i].board + ChampionCatalog` | Partially delivered as fixed slot features/aggregates; not a lossless typed entity set |
| `entities.bench` | available | observed | `player_envs[i].bench + ChampionCatalog` | Partially delivered as fixed slot features/aggregates; not a lossless typed entity set |
| `entities.shop` | available | observed | `player_envs[i].shop + ChampionCatalog` | Partially delivered as fixed slot features/aggregates; not a lossless typed entity set |
| `entities.items` | available | observed | `ItemEngine + ItemCatalog + UnitInstance.items` | Partially delivered through item semantic blocks; exact item/unit-instance relation still needs lossless contract |
| `derived_context.positioning` | available | estimated | `BoardEvaluation + UnitCombatClassifier` | Partially delivered as aggregate positioning score, row ratios, and role features; not full typed positioning evidence |
| `strategic_evidence.commitment_context.direction_id` | available | derived | `strategic_planner_commitments[i].composition_direction` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `strategic_evidence.commitment_context.direction_identity` | available | derived | `direction:v2:<direction>` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `strategic_evidence.commitment_context.progression_plan` | not_produced | inferred | `StrategicSharedContext.progression_plan` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `strategic_evidence.owned_unit_assessments` | available_shadow_only | derived | per-slot `StrategicSharedContext.owned_units` plus champion-aggregated `UnitPrioritySnapshot` | Shadow-only; no UUID/per-instance identity, duplicate copies ambiguous, no structured PPO delivery |
| `strategic_evidence.anchor_candidates` | available_shadow_only | estimated | `NativeStrategicCompositionGenerator → StrategicSharedContext.anchor_candidates`; separate Unified direction/pivot records | Shadow-only; no stable candidate_id/revision or complete candidate-set envelope; not delivered to PPO |
| `strategic_evidence.candidate_generation` | available | observed | `strategic_native_generation diagnostics` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `strategic_evidence.completed_traits` | available | derived | `active_native_direction.completed_traits → StrategicEvidenceContextInput.focus_traits` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `strategic_evidence.commitment_context.core_unit_ids` | available | derived | `active_native_direction.unit_ids` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `strategic_evidence.commitment_context.composition_locked` | not_available | derived | `StrategicSharedContext.composition_locked` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `derived_context.action_opportunity.items` | not_produced | estimated | `StrategicSharedContext.action_candidates` | Not produced; strategic action-candidate set is empty in audited engine construction |
| `legal_state_context.anti_loop_state` | available_but_not_projected | observed | internal `AntiLoopHistory`; `get_state()` summary is not called/serialized by audited TftEngine path | Python exposes aggregate `get_anti_loop_metrics()` only; ordered history is not delivered to PPO |
| `legal_state_context.mask_reference` | not_correlated | observed | `Trainer observations + get_action_masks() separate calls` | Masks are fetched separately and stored in rollout; no typed decision-identity/hash correlation |
| `shadow_recommendations` | available_shadow_only | recommended | `StrategicPlanner/EconomicController/ActionEvaluator` | Shadow diagnostic only; excluded from PPO |
| `strategic_evidence.focus_weights` | not_produced | inferred | `No independent focus-weight source in new evidence callsite` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `strategic_evidence.commitment_context.composition_identity` | available | derived | `active_native_direction.identity / anchor.composition_identity` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `strategic_evidence.commitment_context.current_direction_score` | available | estimated | `active_native_direction.score` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `strategic_evidence.commitment_context.current_direction_viable` | available | derived | `active_native_direction candidate exists` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `strategic_evidence.commitment_context.direction_source` | available | derived | `literal per_player_strategic_commitment` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `derived_context.decision_history.actions_taken_this_round` | available | derived | `PlayerEnv::actions_taken_this_round → Impl::build_observations` | Normalized remaining-action horizon reaches PPO; no typed decision ID/event history or source sequence |
| `derived_context.decision_history.remaining_action_budget` | available | derived | configured action-memory horizon minus `actions_taken_this_round` | Normalized remaining-action horizon reaches PPO; horizon identity is implicit and no typed decision sequence is emitted |
| `derived_context.decision_history.board_move_age_by_slot` | available | derived | `PlayerEnv::board_move_age → Impl::build_observations` | Normalized 28-slot age values reach PPO; slot-scoped recency is not physical-unit history and has no typed decision sequence |
| `derived_context.recipe_target_fit` | available | estimated | `ItemFitCache.get(recipe_id, UnitProfile)` | Delivered in item recipe-target fit block; heuristic score, catalog/profile identity required |
| `entities.items.anvil_options` | available | derived | `ItemEngine.pending_anvil + ItemCatalog` | Delivered in item anvil option block; only current pending anvil snapshot |
| `derived_context.action_opportunity.items.sell_value` | available | derived | `UnitInstance sell value / sell rules` | Delivered in legacy bench candidate tail, normalized; tied to physical bench slot |
| `derived_context.action_opportunity.items.affordability` | available | derived | `player gold compared with candidate cost` | Delivered in legacy shop candidate tail, binary; tied to shop slot and same gold snapshot |
| `identity.decision_identity_hash` | derived | derived | `Canonical identity tuple in observation envelope` | Not delivered in observation/rollout envelope |
| `legal_state_context.anti_loop_state.position_history` | available_but_not_projected | observed | internal AntiLoopHistory; no ordered-history Python binding | Not delivered to PPO; only aggregate metrics are exposed; sequence identity is missing; exact masks remain separate |
| `legal_state_context.anti_loop_state.move_history` | available_but_not_projected | observed | internal AntiLoopHistory; no ordered-history Python binding | Not delivered to PPO; only aggregate metrics are exposed; sequence identity is missing; exact masks remain separate |
| `legal_state_context.anti_loop_state.blocked_move_records` | available_but_not_projected | derived | internal AntiLoopHistory; no ordered-history Python binding | Not delivered to PPO; only aggregate metrics are exposed; sequence identity is missing; exact masks remain separate |
| `legal_state_context.anti_loop_state.state_visits` | available_but_not_projected | derived | internal AntiLoopHistory; no ordered-history Python binding | Not delivered to PPO; only aggregate metrics are exposed; sequence identity is missing; exact masks remain separate |
| `legal_state_context.critic_context` | not_available | derived | `Action Contract mask side-input boundary` | Not delivered; current value path ignores masks |
| `derived_context.capacity` | derived | derived | `board occupancy + player level + bench slot count` | Delivered as two aggregate capacity features; not full capacity state |
| `derived_context.trait_counts` | available | derived | `trait_counts + observation_trait_names` | Delivered as catalog-ordered aggregate trait counts; requires catalog fingerprint |
| `derived_context.unit_roles` | available | derived | `UnitCombatClassifier.classify` | Partially delivered through board/bench/shop role features and item-target role encodings |
| `derived_context.item_target_fit` | available | estimated | `ItemFitCache.get(item_id, UnitProfile)` | Delivered in item compatibility block; heuristic score, item/target identity required |
| `player.economy.income` | not_produced | derived | `EconomyEngine income calculation` | Not delivered as a distinct typed feature; source-map status remains authoritative |
| `player.economy.interest` | not_produced | derived | `EconomyEngine interest calculation` | Not delivered as a distinct typed feature; source-map status remains authoritative |
| `player.economy.streak_bonus` | not_produced | derived | `EconomyEngine streak income calculation` | Not delivered as a distinct typed feature; source-map status remains authoritative |
| `player.economy.shop_cost` | not_produced | observed | `TFT rules/catalog reroll cost` | Not delivered as a distinct typed feature; source-map status remains authoritative |
| `derived_context.economic_context.board_pressure` | not_produced | estimated | `No populated source in current StrategicSharedContext callsite` | Not delivered as a distinct typed feature; source-map status remains authoritative |
| `derived_context.economic_context.economy_pressure` | not_produced | estimated | `No populated source in current StrategicSharedContext callsite` | Not delivered as a distinct typed feature; source-map status remains authoritative |
| `derived_context.economic_context.survival_pressure` | not_produced | estimated | `No populated source in current StrategicSharedContext callsite` | Not delivered as a distinct typed feature; source-map status remains authoritative |
| `strategic_evidence.priorities` | available_shadow_only | recommended | `Composition Intelligence UnitPriorityPlanner (feature-gated)` | Shadow diagnostic only; excluded from PPO |
| `strategic_evidence.progression` | not_produced | inferred | `StrategicSharedContext.current_economic_strategy / commitment progression` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `strategic_evidence.pressure` | not_produced | estimated | `No populated source in current StrategicSharedContext callsite` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `strategic_evidence.uncertainty` | not_produced | estimated | `No explicit uncertainty map in current evidence callsite` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `strategic_evidence.commitment_context.confidence` | available | estimated | `strategic_planner_commitments[i].confidence` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `strategic_evidence.commitment_context.consecutive_reviews` | available | derived | `strategic_planner_commitments[i].consecutive_reviews` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `strategic_evidence.commitment_context.last_review_round` | available | derived | `strategic_planner_commitments[i].last_review_round` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `strategic_evidence.commitment_context.selected_round` | available | derived | `strategic_planner_commitments[i].selected_round` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `strategic_evidence.commitment_context.selection_reason` | available | derived | `strategic_planner_commitments[i].selection_reason` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `strategic_evidence.commitment_context.revision_condition` | available | derived | `strategic_planner_commitments[i].revision_condition` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `strategic_evidence.commitment_context.flexible_unit_ids` | not_produced | inferred | `No independently populated flexible-unit list in current commitment bridge` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `strategic_evidence.owner_snapshots.planner_commitment` | available | derived | `strategic_planner_commitments[i]` | Not delivered as canonical Shadow evidence; legacy proxies, where present, are not equivalent |
| `strategic_evidence.owner_snapshots.composition_intelligence` | available_shadow_only | derived | `composition_intelligence_players[i].active` | Shadow diagnostic only; excluded from PPO |
| `strategic_evidence.owner_snapshots.unified_state_machine` | available_shadow_only | derived | `UnifiedStrategicShadowRuntime.machine()` | Shadow diagnostic only; excluded from PPO |



## Appendix B — Corrective provenance and resolver findings (source reconciliation)

### ContextBridge provenance

The current bridge adapter assigns `ContextValueOrigin::Observed` to all of
`composition_locked`, `observed_direction`, `observed_focus`, and
`core_traits`. The native Shadow context construction shows why this is not
valid field-level provenance:

- `composition_locked` is explicitly initialized to `false` in the Shadow
  context and is not populated from the active-composition owner's lock state.
  This is not evidence of an unlocked composition. The legacy `StrategyInfo`
  lock heuristic is a separate pipeline and cannot be silently substituted.
- `observed_direction` comes from the StrategicPlanner commitment.
- `observed_focus` and `core_traits` come from the selected native generated
  direction candidate's completed traits.

The current bridge representation should therefore be treated as diagnostic
only until a post-Gate-8 correction can preserve: lock = unavailable/unknown;
direction = canonical commitment with explicit owner/revision; focus and core
traits = derived from a named generator candidate with identity/provenance.
No runtime changes are made by this audit.

### Resolver integration

The current engine invokes `StrategicActionExecutor::resolve()`. The
comparison diagnostic serializes `executor_connected=true`,
`execution_enabled=false`, and `native_action_applied=false`. This corrects
the older `executor_connected=false` wording. Per-request acceptance remains
separate from resolver connectivity; the resolver is read-only and cannot
execute an action.

## Decision Identity v2 migration boundary (proposal; not runtime-approved)

The producer-binding audit remains the evidence for current behavior: native observations and masks are not delivered through one typed decision envelope, masks are fetched separately, and rollout does not retain an explicit observation-sequence token proving exact pairing. The proposed Observation Schema v2 changes the identity fields to typed `{namespace,value}` references, but the canonical Engine decision/snapshot namespaces are currently marked proposed-not-implemented in the registry. This proposal does not retroactively establish current producer availability. A future implementation must create and transport the identity atomically, bind exact mask content/hash, and preserve it through wrapper, trainer, Policy, rollout and replay. Until then, v2 identity is unavailable for runtime consumption.

## Projection consumer matrix boundary

The proposed [Observation Projection Consumer Matrix v1](observation-projection-consumer-matrix.v1.draft.md) classifies semantic eligibility and intended Actor/Critic/control/diagnostic consumers. It does not upgrade source availability: every entry remains subject to this producer-binding audit, and all fields marked candidate retain their producer, provenance, sequence-correlation and missingness blockers. In particular, an intended consumer is not proof that the current native→Python PPO path delivers the field.

## Structured entity producer requirements — draft

The proposed [Structured Entity and Temporal Evidence Contract v1](observation-structured-entity-temporal-contract.v1.draft.md) records the identity, ownership, completeness and source-sequence requirements that producers must satisfy. In particular, shop offer identity, physical item-instance identity, pool availability, board coordinates, and candidate collection completeness remain explicit gaps; this contract does not claim that current native or Python producers deliver them.
## Producer-backed identity correction — 2026-11-14

The previous draft described unit.instance_id as the canonical native identity. That claim was premature and is corrected here.

Source inspection of cpp/include/lobby/TftEngine.hpp finds UnitInstance::uuid, but the declaration's own comment states that effective UUID generation will be implemented later. The presence of a string member is therefore not evidence that a value is generated, non-empty, unique, stable across board/bench movement, or scoped to a match/player. cpp/src/lobby/TftEngine.cpp consumes unit.uuid in several paths and includes guards that skip some processing when it is empty; this still does not prove a valid identity lifecycle.

- Native physical-unit identity producer status is **unverified**.
- Schema v2's required instance_id is a semantic contract field, not a demonstrated alias for UnitInstance::uuid.
- Do not map instance_id = uuid until UUID generation, uniqueness, lifecycle, ownership transfer and reset semantics are proven.
- Champion ID and slot index remain invalid substitutes.
- Unit-instance projection remains blocked until the source audit establishes an authoritative identity or proposes a versioned producer/schema correction.

This correction does not alter runtime code or claim that UUID generation is implemented.


## 9. Strategic and temporal producer corrections — source-backed follow-up

The structured entity producer audit now distinguishes the actual new-architecture callsites:

- owned_unit_assessments is not a UUID-keyed physical-unit assessment. StrategicSharedContext::owned_units is appended per occupied slot but carries champion identity only; UnitPrioritySnapshot is aggregated by champion. Both are Shadow-derived records, not PPO structured entities.
- anchor_candidates is produced from NativeStrategicCompositionGenerator, while early direction hypotheses, active direction anchors and pivot candidates have separate owners/lifecycles. No stable candidate ID/revision or complete candidate-set envelope is emitted.
- action_candidates remains empty in the audited TftEngine construction path. The current diagnostic booleans can label two empty sets as equal and mark comparison available from non-stale evaluators; this does not satisfy the non-empty candidate comparison contract.
- The resolver is wired and invoked (executor_connected=true), but it is read-only (execution_enabled=false, native_action_applied=false). Connectivity is not per-request acceptance.
- PPO receives flat temporal action-memory scalars, not a typed decision history. Anti-loop history remains internal; Python exposes aggregate anti-loop metrics only. Exact action masks remain separate legality inputs.

These findings supersede any interpretation that champion-keyed assessments are physical-unit entities, that composition identity is a candidate-set identity, or that anti-loop metrics constitute delivery of ordered history.
## UnitInstance UUID producer correction — 2026-11-15

The earlier “Producer-backed identity correction — 2026-11-14” contains a statement that is now superseded by the later source audit. The header comment in TftEngine.hpp is stale: UnitInstanceFactory::create() calls generate_uuid(), and cpp/src/lobby/UnitInstanceFactory.cpp implements the UUID-shaped value generation. Successful factory creation therefore does produce a non-empty UUID in the audited path.

The corrected status is:

- **Raw UUID production:** native observed; the factory producer is implemented.
- **UUID scope/uniqueness:** unverified as canonical physical identity; deterministic same-seed reset and independent same-seed Engine instances can repeat the sequence; no match/player namespace or collision registry exists.
- **Object lifecycle:** moves/ownership transfers preserve the UUID in the audited paths; UnitInstance is implicitly copyable, so ordinary copies preserve UUID; complete ownership/copy/destruction acceptance remains open.
- **Python/diagnostic delivery:** audit snapshot exposes UUID to Python; this is diagnostic delivery, not typed PPO observation or RolloutBuffer delivery.
- **Schema v2 mapping:** do not treat raw UUID as a globally stable instance_id. A scoped identity is still required.

This addendum supersedes only the claim that generation was not implemented. It does not upgrade UUID to canonical cross-match identity or change any runtime behavior.
