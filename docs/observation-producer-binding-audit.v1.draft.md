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

The native observation builder reads the ItemEngine and item/champion catalogs to encode component counts, inventory semantics, recipes, target roles/stats, compatibility, and anvil options. Some compatibility values are heuristic fits. The new projection must preserve item identity, unit-instance target identity, catalog binding, and formula provenance; it must not promote a heuristic fit score to an observed fact.

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

- `composition_locked` is set as Observed from `StrategicSharedContext`, while the audited engine construction currently initializes `strategic_context.composition_locked = false` rather than obtaining an authoritative lock producer. This is **unknown/unavailable**, not observed false.
- `observed_direction` is populated from `strategic_planner_commitments[i].composition_direction`; that is a canonical commitment state, not a raw observed game fact. Its origin must identify the commitment owner/state semantics.
- `observed_focus` and `core_traits` are derived from the selected native generated direction candidate's completed traits. They must not be labelled raw observed composition facts.
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

The engine also calls the read-only resolver's `resolve()` method and records its resolution result. This is stronger evidence of a wired resolver call than the older documentation statement that the executor was not connected. However, the boolean is serialized as a constant and does not itself prove that a particular proposal was accepted or resolved successfully.

Reconcile the older executor-boundary documentation with current runtime evidence. The correct distinction is:
- resolver code path invoked/connected;
- per-request resolution accepted or rejected;
- game-action execution disabled;
- native game action not applied.

Do not conflate these states.

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
