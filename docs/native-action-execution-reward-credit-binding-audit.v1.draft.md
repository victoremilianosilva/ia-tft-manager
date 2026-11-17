# Native Action Execution and Reward-Credit Binding Audit v1 — Draft

**Status:** source-backed native execution/reward audit; documentation only.
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).
**Base:** `new-arquiteture`.

## 1. Prior ambiguity

Previous audits established the policy action shape, native masks, Python wrapper and RolloutBuffer storage. What remained unclear was whether the submitted action, the action actually applied by the Engine, execution/rejection outcomes and reward components remain distinguishable through the native result and PPO training record.

This audit traces the current `TFTEngine::step` → `PlayerEnv::step` → `StepResult` → wrapper → Trainer → RolloutBuffer path. It does not change action semantics, masks, rewards or training.

## 2. Lobby-level preflight and effective actions

`TFTEngine::step` first copies the submitted eight-player action batch into `effective_actions`. If a player has already finished the preparation phase and has no pending anvil, the Engine replaces that player's effective action with PASS (`{6,0,0,0,0,0}`). The submitted action and effective replacement are not both retained in `StepResult`.

Before executing any player, the Engine validates the bounds/shape of every effective action and validates each against the corresponding player's current native masks and semantic state. The source comment explicitly describes this as a side-effect-free two-phase preflight: if any action is impossible, the batch throws before the first player action is applied.

Consequences:
- A preflight rejection is an exception from native `step`, not a per-player rejected-action record in a successful `StepResult`.
- The all-player preflight prevents a partially applied batch when a later player's action fails validation.
- The successful result does not contain a canonical submitted-action batch, effective-action batch, per-player validation status or rejection reason.
- A policy action can be replaced with PASS by the Engine's round-finished rule; the result does not expose that substitution as a typed resolution record.

Special cases are intentional and must not be flattened into a generic invalid-action label: structurally valid anti-loop-blocked moves are allowed through preflight so the movement system can record the block; board-capacity deployment attempts can be admitted for a specific penalty; pending anvil type-7 selection is distinct from ordinary inventory equip.

## 3. Per-player execution and transition status

`PlayerEnv::step` returns a `PlayerTransition` containing `action_reward`, `acted`, capacity-violation flag, action cost/sale proceeds and before/after economy values. If the player is already dead, it refreshes masks and returns `{0.0f, false}`. For a living player, the normal path increments the player's `action_serial`, updates action-memory counters and processes the selected action. The method returns `acted=true` after producing its action-specific transition.

`TFTEngine::step` skips result aggregation when `transition.acted` is false. For acted players it copies action reward and economic deltas into local per-player arrays, refreshes masks and marks round completion as appropriate.

Important distinction: `acted` is an internal control flag. It is not exported as a per-player execution status in `StepResult`. A zero action reward is therefore not a universal failure signal: PASS may be a valid action with zero/negative shaping, and dead players are skipped.

## 4. Execution evidence that is exported

The successful `StepResult` exposes aggregate/per-player rewards, dones, observations, masks, player state, episode/round/stage and a vector of human-readable event strings. It does not expose the six-component action selected by PPO or a typed per-player `ActionExecutionResult`.

Some outcomes have partial diagnostic evidence:
- Economic action costs/proceeds and before/after gold, interest, level and XP are formatted into `ECONOMIC_ACTION` event strings for each player. These local arrays are not typed fields on `StepResult`.
- Capacity violations produce a `RULE_VIOLATION` event.
- Anti-loop execution attempts/blocks and movement counters are available through separate cumulative metrics, not correlated to a typed decision record.
- Item actions can emit `ITEM_ANVIL_CHOSEN` or `ITEM_ACTION_APPLIED` events with player, kind, item, target UUID, fit/reward and stage. These events do not include action sequence or native decision identity.
- A generic `ROUND_WAITING`/`ROUND_RESOLVED` event describes phase progression, not the execution resolution of an individual action.

These event strings are useful evidence for diagnostics, but they are not a stable typed action ledger. They may omit the exact submitted arguments, exact effective action, source state identity and explicit outcome status.

## 5. Reward composition and credit assignment

`PlayerEnv::step` computes an action-specific reward using action success, state changes and bounded shaping. It returns this as `PlayerTransition::action_reward`. The Engine copies this to `StepResult::action_rewards`.

`TFTEngine::step` separately accumulates combat rewards during PvP resolution and terminal placement rewards when placement becomes known. `StepResult::rewards` is the combined training reward for the step; `action_rewards`, `combat_rewards` and `placement_rewards` are exposed as separate arrays for audit/parity.

The Python wrapper places `action_rewards`, `combat_rewards` and `placement_rewards` in its `info` dictionary, while returning `rewards` as the Gym reward vector. Trainer consumes `rewards_raw` to create the PPO reward tensor and stores that combined value in RolloutBuffer. The component breakdown remains in `infos` for reporting and is not stored as separate PPO rollout tensors.

An important implementation comment in `PlayerEnv::step` says the broader `state_reward`/RewardManager components are not called by this Python environment; applying them here would change PPO targets. Therefore, do not assume `RewardState` or `state_reward()` is the actual PPO reward path.

Credit assignment limitation: the combined reward is temporally stored beside the sampled action, but the rollout does not retain typed action execution status, action-specific reward, combat reward and placement reward as separate fields. The separate component arrays are available in wrapper `info`, not preserved in the PPO rollout.

## 6. Action serial is not decision identity

`PlayerEnv::action_serial` increments inside the living player's `PlayerEnv::step` and resets to zero during episode initialization. It is used to bound recent-purchase reversal bookkeeping; `RecentPurchase` records refer to it. It is not emitted in `StepResult`, wrapper info or RolloutBuffer.

It is not a sufficient native decision identity by itself: it is player-local, reset per episode, and not namespaced by Engine instance, player ID or a snapshot/decision sequence in the training record. It also increments inside the execution routine rather than being a cross-layer envelope binding the exact observation, masks, submitted action and result.

## 7. Evidence-backed disposition

| Concern | Current disposition |
|---|---|
| Submitted policy action | Available in Trainer before `vec_env.step`; not returned by native `StepResult` |
| Engine effective action | Can replace submitted action with PASS for finished players; replacement not exported as typed resolution |
| Batch preflight | Two-phase, side-effect-free validation before any player mutation; invalid batch throws |
| Per-player `acted` | Internal `PlayerTransition` flag; not exported |
| Per-player action reward | `StepResult.action_rewards`, then wrapper `info`; not separately stored in RolloutBuffer |
| Combined PPO reward | `StepResult.rewards` → wrapper reward vector → Trainer → RolloutBuffer |
| Combat/placement reward | Separate native arrays and wrapper info; not separately stored in RolloutBuffer |
| Execution/rejection reason | Partial event strings and separate anti-loop metrics; no typed decision-bound resolution |
| Action serial | Player-local reward bookkeeping; not exported/correlated to rollout |
| Observation/action/mask identity | Temporal alignment by current synchronous call order and rollout pointer; no typed shared decision envelope |

## 8. Required future acceptance proof

1. Define a typed execution-resolution contract distinguishing submitted action, effective action, preflight rejection, accepted execution, intentional PASS/substitution, anti-loop block, capacity rejection and player-inactive skip.
2. Bind each resolution to the same native decision identity as its pre-action observation and masks, with Engine scope, episode, player and decision sequence represented as distinct typed namespaces.
3. Preserve action-specific, combat and placement reward components alongside the combined PPO reward in replay/audit data, without silently changing the reward consumed by PPO.
4. Verify atomic all-player preflight behavior with a batch where a later player is invalid; assert no earlier player's state was mutated.
5. Add cases for finished-player PASS substitution, dead-player skip, valid PASS, anti-loop block, capacity violation, item/anvil action and normal buy/sell/move execution.
6. Verify that event diagnostics and anti-loop metrics can be reconciled with typed outcomes, without treating free-form event strings or cumulative counters as the authoritative action ledger.
7. Replay the exact submitted action against the exact pre-action state/masks and verify the effective action, state delta, execution outcome and reward components.

## 9. Architecture reconstruction review

1. **Prior problem:** policy selection and combined reward were stored, but the submitted/effective/executed action distinction and component reward path were not traced through the native boundary.
2. **Technical justification:** PPO credit assignment and deterministic replay require knowing what the Engine actually accepted/applied and which reward components followed; reward magnitude alone cannot prove execution success.
3. **New responsibility:** this audit owns the evidence-backed mapping from Trainer-selected action through native preflight/execution to exported outcomes and PPO reward storage.
4. **Contract and invariants:** batch preflight precedes mutation; Engine may substitute PASS for finished players; internal `acted` is not exported; combined reward is PPO input; component rewards and diagnostic events are not typed execution identity.
5. **Cross-component impacts:** Trainer, LobbyVectorEnv, CppTFTLobbyWrapper, `TFTEngine::step`, `PlayerEnv::step`, `StepResult`, pybind dictionaries, reward model, anti-loop metrics, event diagnostics, RolloutBuffer and replay.
6. **Objective validation:** native preflight, per-player transition, event/result projection, wrapper info and rollout reward storage are traced; failure and acceptance scenarios are enumerated. Documentation only.

No runtime, schema, tensor-layout, PPO architecture, reward, mask, training, checkpoint, Viewer or Overwolf implementation is authorized by this audit. Issue #346 remains open; Gate 8 remains blocked.