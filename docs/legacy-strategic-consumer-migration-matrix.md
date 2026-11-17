# Legacy strategic consumer and shutdown matrix

**Status:** approved documentary inventory and migration plan; no runtime shutdown authorized  
**Target branch:** `new-arquiteture`  
**Static source-audit baseline:** `3575d21cc0f7dbb5544d75526bd96939b37f5c96`  
**Consolidated from:** Audit F issue #301 and follow-up findings in #285–#292  
**Coordinates with:** Observation #286/#293, Reward #287, Checkpoint #288, Shadow replay #289, inventory #290, unit/item evidence #285/#291, Viewer #292, PPO evaluation #295

> This document is the single navigable reference for the static legacy-consumer inventory. It does not claim that the legacy producer or consumers have been migrated, dynamically tested, or removed. It does not authorize implementation before Gate 8 and explicit user approval.

## 1. Purpose and reconstruction rule

The audit found two simultaneous pipelines:

- **Legacy decision pipeline:** `update_strategy()` → `StrategyPolicy` / `CompositionDirectionPolicy` / `CompositionPlanner` → `StrategyInfo` → PPO observations, policy-derived economic features, active reward shaping, board/item evaluation, fine-tuning eligibility, Viewer and logs.
- **Canonical Shadow pipeline:** `NativeStrategicCompositionGenerator` → `StrategicPlanner` / `CompositionIntelligencePlayerRuntime` / `ActiveCompositionManager` → versioned strategic snapshots and diagnostics.

The Shadow fields copied into `StrategyInfo` (`strategic_*`, `economic_*`) are telemetry mirrors in the audited callsites. Their presence in that DTO does **not** mean PPO consumes Shadow context.

Apply the architecture reconstruction standard to every future migration:
1. State the previous problem or identify a genuinely new capability.
2. Explain the technical reason for the change.
3. Name the new owner, responsibility and limits.
4. Specify contracts and invariants.
5. Record cross-component impact.
6. Define objective validation evidence.

Legacy behavior is evidence, not authority. Classify each capability as preserve, improve, redesign, or discard; do not port a legacy implementation, default, enum, score or field merely because it exists.

## 2. Producer graph and ownership boundary

### 2.1 Audited legacy producer

The central producer is `TftEngine::Impl::update_strategy()`. In the audited path it is called after player actions and again at round resolution. It:

1. selects a nominal economic mode through `StrategyPolicy::select_economic_strategy(EconomicStrategyContext)`;
2. derives direction, focus weights and lock/hysteresis through `CompositionDirectionPolicy`;
3. builds core/planned units, traits, carry and composition score through `CompositionPlanner::build()`;
4. stores the result in the player's `StrategyInfo` history.

This is an active producer in the current runtime, not dead code.

### 2.2 Canonical Shadow owners

The approved documentary ownership split is:

| Concept | Canonical owner | Proposal/evidence | Important boundary |
|---|---|---|---|
| Direction commitment | `StrategicPlanner` | Native generator hypotheses and validated strategic evidence | Direction is a commitment, not a game fact or composition ID |
| Active composition and version | `CompositionIntelligencePlayerRuntime` through `ActiveCompositionManager` / `TransitionManager` | Native generator and CI evaluators | Only the active-composition transition path commits it |
| Pivot candidate | Candidate record in its own CI or diagnostic stream | Generator, pivot discovery and feasibility evidence | Candidate never mutates active composition |
| Confirmed active transition | Active-composition transition authority | Pivot coordinator and transition validation | Unified Shadow may confirm only its separate diagnostic state |
| Accepted focus | Active-composition owner | Generator and trait/evidence analysis | Ranked/weighted focus is not core-trait membership |
| Accepted core traits | Active-composition owner | Native generator computes candidate set | Must not be copied from focus or legacy `core_traits` |
| Composition lock | Active-composition owner, but unavailable until a valid producer/policy exists | Dedicated policy/evidence evaluator when defined | Unknown/unavailable is not false/unlocked |
| Economic posture | `EconomicController` | Engine facts plus validated estimates | Derived, time-bounded posture; not a strategy ID or action |
| Progression hypothesis | `EconomicController` under a distinct contract | Economy, HP, board strength, round and valid risk/projection evidence | Separate from posture and action; missing inputs stay unknown |

`UnifiedStrategicStateMachine` / `UnifiedStrategicShadowRuntime` remain diagnostic-only parallel state. They cannot publish canonical state into StrategicPlanner, active composition, PPO, Engine or Viewer. Divergence between those streams is diagnostic evidence, not last-writer-wins synchronization.

### 2.3 Required synchronization protocol

All future consumers and producers must follow this sequence:

1. Read one correlated input set with match/episode, player, round and typed source-sequence references.
2. Validate identity, freshness, provenance, quality and applicable composition/candidate version against the receiver's expected state.
3. Generate proposals without mutating canonical state.
4. Commit through exactly one declared owner after checking the expected prior identity/version.
5. Publish an immutable transition record with prior/next identity, reason, provenance and source sequences.
6. Keep downstream consumers read-only.
7. Represent disagreement, stale, rejected and unavailable states explicitly.
8. Reset all player-local state and sequence namespaces at the episode boundary.

Bare sequence integers from different namespaces are never comparable without an explicit correlation contract.

## 3. Field → consumer → destination matrix

| Legacy field / group | Producer / origin | Confirmed consumers and path | Classification | Target destination / issue |
|---|---|---|---|---|
| `strategy`, `strategy_id`, `strategy_name`, scores, reason, confidence, changed, previous strategy | `update_strategy()` → `StrategyInfo`; missing history may default to ECON/ID 0 | `build_observations()[10:17]`; `policy.py::_economic_context_features`; `PlayerEnv::step`; fine-tuning scenario filter; Trainer counts; Viewer/logs/scripts | Active decision input plus telemetry/history | Replace nominal IDs with versioned factual/contextual economic evidence in #286/#293; scenario eligibility in #295; preserve historical readers in #290/#292. Scores/confidence/reasons have no automatic PPO target equivalent |
| `composition_direction`, `composition_focus`, `composition_focus_weights`, `composition_locked`, `composition_strength` | `CompositionDirectionPolicy` through `update_strategy()` | PPO observations; `unit_composition_score()`; board/item fit; reward and `RecentPurchase`; Viewer, JSONL and audit scripts | Active legacy decision context plus presentation | Direction commitment and accepted active composition as separate versioned concepts; focus from accepted composition; lock unavailable until authoritative; strength has no automatic equivalent. #285/#286/#287/#290/#292 |
| `core_units/core_unit_ids/core_traits`, `active_traits`, unit/trait counts | `CompositionPlanner`, StrategyInfo and reconstructible board facts | Observation fit; board evaluation/cache; item profiles; sale/displacement reward; CI `collect_unit()`; Viewer/logs | Mixture of observed/reconstructible facts and legacy strategic preference | Recompute facts from current board/bench/catalog; core membership from accepted active composition; keep traits observed separate from preferred traits. #285/#291/#293; reward consumers #287 |
| `planned_units/planned_unit_ids/planned_traits/planned_main_carry_id/planned_composition_score` | `CompositionPlanner::build()` and plan hysteresis | PPO fit/role; board evaluation; item profiles; buy/sell reward; Viewer CompositionDialog; scripts | Active legacy plan and derived classification | Rebuild through canonical composition + lineup/role contracts. Distinguish owned, selected, deferred, target and deployable units. Planned carry must not override factual combat role. #285/#286/#291/#292 |
| `unit_composition_score()`, `preferred_traits`, item/board fit adapters | Adapter built from StrategyInfo | Board/bench/shop/candidate/item observation features; ItemFitCache; reward; RecentPurchase; CI item evidence | Shared transitive dependency | One shared, versioned evidence/profile adapter for PPO, board, item and reward consumers. Observed traits and composition-derived preferences require distinct provenance. #285/#291; #286/#287 |
| `board_evaluation()` and cache signature | StrategyInfo direction/focus/core/planned fields plus observed board | Unit role classification, board score/cache, observations, item fit and reward | Derived consumer contaminated by legacy context | Rebuild factual role from unit attributes/range/ability/items; composition may be a separate versioned context. Cache key must include exact source versions. #291/#285/#286/#287 |
| `RecentPurchase.comp_direction/comp_focus/fit_score` | Temporal purchase record | Later sale/reversal classification and reward | Temporal/transitive decision dependency | Store purchase-time provenance, source sequences and composition identity/version; evaluate later consequences without comparing legacy labels. #287 coordinated with #285/#291 |
| `strategic_*` / `economic_*` mirrored in StrategyInfo | StrategicPlanner, EconomicController and evaluator outputs | Binding, Viewer, JSONL and audits | Shadow telemetry mirror; not PPO authority in audited callsites | Separate typed Shadow/decision DTO and diagnostic records. Do not use as PPO imitation/reward labels. #290/#292; future observation projection only via #286/#293 |
| `get_strategies()` / `strategies_to_list()` | `TFTEngine::get_strategies()` and pybind | `cpp_lobby_env.get_strategy_snapshots()`, ViewerSession, logs; `get_strategies()` also feeds Trainer strategy counts | Compatibility/presentation/telemetry API | New-session projection independent of StrategyInfo; retain legacy parser/adapter only for historical records during transition. #290/#292 |
| `get_audit_snapshot()` | Factual native Engine state | Viewer/session | Factual source, separate from StrategyInfo | Preserve as factual input; compose with a separately versioned strategic projection. #292/#293 |
| `RewardManager::calculate_total_reward()`, `state_reward()` | Helper definitions | No active callsite found in the audited Python PPO training path | Not established as active | Do not migrate by assumption. Require a real callsite/callgraph before assigning ownership. #287 |
| JSONL, scripts, traces and fixtures reading old strategy/direction/focus/lock/planned fields | Historical snapshots and audit outputs | Viewer audit windows, integrated audit, strategic KEEP audit, scripts, fine-tuning audit/viewer and tests | Historical compatibility/diagnostics, except the fine-tuning eligibility path | Preserve historical readers; new logs use versioned schema, provenance and unavailable states. New scenario selection must not use nominal IDs. #290/#292/#295 |
| Tests asserting old offsets, IDs and StrategyInfo behavior | Legacy fixtures and runtime contracts | Policy/Engine/Viewer/Shadow/audit/fine-tuning tests | Legacy behavior contract or historical fixture | Replace decision assertions with new schema/owner tests; retain explicit historical-log parsing tests. #285–#288, #291–#293, #295 |

## 4. Critical consumer details

### 4.1 PPO observations and policy

The current observation producer reads the latest `StrategyInfo` directly. The legacy strategy one-hot is at `[10:17]`. Other strategic blocks include direction, core traits, composition fit, focus weights, lock, strength and planned-carry role. `unit_composition_score()` fans out into board, bench, shop, candidate-tail and item features.

`policy.py::_economic_context_features()` derives five active encoder inputs from facts plus the legacy one-hot: target level, level deficit, reserve, spendable gold and phase pressure. These features affect the shared actor/critic encoder; they are not merely Viewer labels.

**Required destination:** a new versioned projection from approved owners and evidence contracts. Preserve useful observed facts; rebuild derived features with explicit formulas, units, provenance, validity and uncertainty. Do not port ECON/FAST8/SLOWROLL/ALL_IN as classes or fixed rules. Checkpoint shape compatibility is not semantic compatibility; old checkpoints remain immutable historical baselines (#286/#288/#293).

### 4.2 Fine-tuning eligibility

`economy_finetuning/scenario_generator.py::decode_observation()` reads `obs[10:17]`, converts argmax into a legacy strategy ID/name, and `ScenarioSpec.matches()` uses that nominal mode to determine `valid`. `economy_finetuning/finetune.py` passes this value into `RolloutBuffer.add()`; valid transitions are then selected for minibatches and advantage normalization.

This is an active training-selection dependency, not telemetry. The new design must decide whether the economic fine-tuning curriculum remains at all. If retained, scenarios must be defined by versioned factual/contextual evidence and an explicit eligibility contract, never by legacy strategy IDs. If replaced by the PPO evaluation/retraining protocol, document that decision and preserve historical reports separately (#286/#295).

### 4.3 Reward and temporal consumers

The active path audited is `PlayerEnv::step → PlayerTransition.action_reward → TFTEngine::step/Lobby aggregation → wrapper → RolloutBuffer`. Legacy strategy IDs influence XP, reroll, PASS, ALL_IN and general action shaping. Composition fit and core/planned IDs influence purchase, sale, displacement and item-related reward. `RecentPurchase` stores direction/focus/fit at purchase time and is read by a later sale/reversal decision.

Combat, damage and placement are separate consequence channels and candidates to preserve under Reward Contract v1. GAE already propagates future rewards through per-player trajectories; do not duplicate the same combat/placement outcome as a second manual action reward. `RewardManager` and `state_reward()` were not found as active PPO reward callsites in the audited path.

### 4.4 Board, unit and item evidence

The legacy carry ID changes unit-role classification through `observation_role()` and `UnitCombatClassifier`. This can make a unit appear as a carry because the plan says so, not because its observed combat properties support it. Keep factual combat archetype separate from strategic suitability.

The same legacy source influences item profiles and ItemFitCache. A shared profile contract must distinguish:
- observed unit/item attributes;
- catalog-derived facts;
- formula-derived combat/role assessments;
- preferences derived from the accepted active composition;
- unavailable or stale inputs.

Do not fabricate `trait_completion`, `explicit_sell_candidate`, `completes_active_trait` or `core_potential` from defaults when their producers/evidence are absent (#285/#291).

### 4.5 Viewer and historical logs

The current ViewerSession combines factual `get_audit_snapshot()` with legacy `get_strategy_snapshots()`. PlayerCard and CompositionDialog read strategy name, direction, focus, lock, strength, planned units/carry/traits/score. PlayerJsonLogWriter persists legacy and Shadow fields. Composition Diagnostics and direction/pivot audit sidecars are separate diagnostic sources; they do not replace the PlayerCard contract.

Required split:
1. New sessions consume a versioned projection of canonical owners and preserve observed/derived/committed/recommended distinctions.
2. New logs persist typed source, provenance, match/player identity, round/timestamp and typed sequence references; unavailable is not ECON/false/zero.
3. Historical logs remain readable as historical data and must not become current decision authority.
4. Audit panels identify whether a value is legacy baseline, canonical context, or Shadow recommendation.

No UI change is implied by this documentary matrix (#292).

## 5. Defaults and fallback hazards

The audit found cases where absence is converted into a nominal value:

- Empty `StrategyInfo` and pybind snapshot fallback can emit ECON / strategy ID 0.
- Wrapper conversion of an invalid strategy ID can also fall back to ECON.
- `policy.py` argmax of an empty/default one-hot selects index 0 (ECON).
- Reward branches use strategy ID 0 when strategy history is absent.
- Viewer/log writer defaults can display ECON, unlocked/false, strength 0 and empty strings/lists when no source exists.
- The StrategicContextBridge provenance must not label Planner/generator-derived direction, focus or core traits as directly observed facts.
- Composition lock is unavailable until an authoritative producer/policy is defined; unavailable is not unlocked.
- Numeric defaults for economy/board/risk and missing candidate/evidence states must not be promoted into observations.

For new contracts, distinguish observed zero/false/empty from missing, unknown, unavailable, stale, partial and invalid. No fallback may invent an owner decision.

## 6. Migration and shutdown order

This order is normative for future implementation planning, not authorization to execute now.

1. **Owners and contracts:** Observation/context (#293), Action/Mask (#294), Reward (#287), Checkpoint/lineage (#288), unit/item evidence (#285/#291), and explicit provenance/identity/sequence.
2. **Remove leaks into canonical Shadow:** eliminate StrategyInfo/core_traits/direction dependencies in CI evidence and item profiles (#285). Prove operation with legacy fields absent.
3. **Unify shared evidence adapters:** rebuild unit role, composition fit, board evaluation/cache, ItemFitCache and purchase/reversal context from one versioned evidence/composition contract (#285/#291/#287).
4. **Migrate PPO and training selection:** project the new schema, redesign encoder/heads as justified, replace `obs[10:17]` and decide fine-tuning scenario eligibility (#286/#293/#295). Start a new semantic checkpoint lineage; do not adapt old weights for compatibility (#288).
5. **Migrate active reward:** remove nominal IDs and legacy composition dependencies from `PlayerEnv::step`; preserve combat/damage/placement only as specified and tested by Reward Contract v1 (#287).
6. **Migrate presentation and tooling:** Viewer card/dialog/session/log writer, audit scripts, exports and readers. New sessions do not require StrategyInfo; historical files remain readable (#290/#292).
7. **Remove old APIs and producers:** after all new consumers are proven independent, stop new-flow calls to `get_strategy_snapshots()`/pybind, then retire `update_strategy()`, `CompositionDirectionPolicy` and `CompositionPlanner` in small reversible steps. Remove DTO/enums/fields only after no active or historical reader depends on them.
8. **Evaluate and promote:** run integrated Shadow replay (#289) and PPO benchmark/ablations (#295) under approved contracts. Neither is replaced by the other.

## 7. Objective shutdown acceptance

A future shutdown PR must attach all of the following:

- Full branch scan of C++ headers/sources, bindings, Python, wrappers, training/fine-tuning, Viewer, scripts, replay/export/import and tests. Every remaining reference is classified; raw zero-match counts are insufficient.
- Callsite/callgraph evidence that no new runtime path reaches the legacy producer, getters or adapters, including indirect callbacks/adapters.
- Native and pybind build with retired symbols removed from new paths.
- Contract tests proving new snapshots/observations/rewards work without StrategyInfo and preserve unavailable/missingness rather than ECON, unlocked=false or fabricated zero.
- Integration tests proving PPO sampling, value estimation, replay, fine-tuning eligibility, rollout and Viewer new-session paths do not consult legacy APIs.
- Smoke-test instrumentation showing zero legacy producer/getter calls in new sessions.
- Regression tests proving Engine rules and native action masks remain final legality authority and are unchanged by strategic migration.
- Replay tests for identity, typed sequences, stale/rejected input, reset, match boundaries and incomplete evidence.
- Historical log/parser tests in the same CI, without requiring old checkpoints to load into the new semantic lineage.
- Rollback plan and immutable baseline references.

Static inventory completion is not dynamic acceptance. A green CI run on the pre-migration code is only a health baseline, not proof of successful shutdown.

## 8. Historical compatibility policy

- Old JSONL/session logs may retain `strategy_info` and old field names. Parsers may decode them for historical display and analysis only.
- New JSONL records use explicit schema version, provenance/source, match identity, engine match identity, player, round, timestamp, typed sequence references and composition identity/version when applicable.
- New-session Viewer tests must run without StrategyInfo; historical-log tests must continue to parse old records.
- Old PPO checkpoints remain immutable baselines. The new runtime must reject missing/incompatible semantic manifests; structural tensor shape alone is not compatibility.
- Historical fine-tuning reports may be read, but new scenario selection must not use old strategy IDs.
- Historical audit conclusions must label legacy heuristics as legacy evidence, not normative rules for the new architecture.

## 9. Audit status and boundaries

| Area | Documentary status | Runtime status |
|---|---|---|
| Static producer/consumer inventory | Consolidated in #301 and this matrix | No producer/consumer migration claimed |
| Strategic owner map | Approved in #311/#316 and ownership contract | Runtime conformance still requires post-Gate-8 proof |
| Observation schema/source/migration maps | Approved documentary contract | Producer/consumer migration pending |
| Action/mask and reward contracts | Approved documentary contracts | Runtime acceptance pending |
| Checkpoint lineage | Approved documentary contract; legacy checkpoints immutable | New loader acceptance pending |
| Shadow replay and PPO evaluation | Approved documentary protocols | Executable replay/benchmark pending |
| Legacy shutdown | Ordered migration plan defined | Not authorized before Gate 8 |

Audit F is complete as a static inventory and migration plan. It does **not** mean legacy code is removed, new consumers are migrated, historical compatibility is dynamically tested, or the legacy shutdown is approved.

Gate 8 remains blocked until Gates 1–7 are reviewed together and the user explicitly authorizes implementation. No code, PPO, Engine, observations, masks, rewards, training, Viewer, checkpoints or historical artifacts are changed by this document.
