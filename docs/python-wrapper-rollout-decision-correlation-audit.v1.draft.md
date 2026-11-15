# Python Wrapper-to-Rollout Decision Correlation Audit v1 — Draft

**Status:** source-backed Engine-to-training boundary audit; documentation only.
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).
**Base:** `new-arquiteture`.

## 1. Prior ambiguity

Earlier audits established that native reset/step results contain episode metadata and action masks, while the PPO rollout stores observations, actions and masks. The missing proof was whether the Python adapter preserves the native decision identity and whether the exact masks returned by the native step are the masks used for the next PPO decision.

This audit follows the actual synchronous training path. It does not claim a runtime race, and it does not change wrapper, trainer, rollout, PPO, masks or tensor layout.

## 2. Native and pybind boundary

The native result contracts expose more context than the current training-facing wrapper retains:

- `ResetResult` contains observations, observation dimension, action masks and episode_id (`cpp/include/lobby/TftEngine.hpp`).
- `StepResult` contains observations, action masks, episode_id, round/stage, rewards, dones, player information and events.
- `reset_to_dict()` exposes observations, action_masks, episode_id and observation_dim (`cpp/bindings/tft_engine_bindings.cpp`).
- `step_to_dict()` exposes observations, action_masks, episode_id, round, stage, rewards, dones, players and events.

The pybind boundary therefore does preserve episode_id and masks in both native result dictionaries. The loss described below occurs in the Python adapter, not in the native result structs or pybind conversion.

## 3. Python adapter drops identity and native returned masks

`CppTFTLobbyWrapper.reset()` calls native reset, then returns only `result["observations"]`. It does not return reset action_masks or episode_id.

`CppTFTLobbyWrapper.step()` calls native step and reads observations, rewards, dones, players, round, stage, events and reward breakdowns. Its returned info dictionary does not include native `action_masks` or `episode_id`.

`CppTFTLobbyWrapper.get_action_masks()` makes a separate native call to `get_action_masks()` and returns those masks (with the documented optional item-action ablation).

Therefore:
- Native post-step masks are produced and cross pybind, but are discarded by the normal wrapper step return.
- The trainer does not consume the masks bundled with the native step result.
- Reset episode identity is also discarded before the training loop.
- The wrapper's training-facing info includes round/stage but not a typed decision sequence or episode identifier.

## 4. Actual synchronous Trainer ordering

The source path in `trainer.py::Trainer.train()` is:

1. `LobbyVectorEnv.reset()` obtains each wrapper's observation; the trainer flattens it into `obs`.
2. At the start of each rollout step, `env_method("get_action_masks")` fetches masks from each current native environment.
3. The trainer flattens those masks and samples the policy action from the current `obs` plus those masks.
4. It converts the actions to per-lobby/per-player dictionaries and calls `LobbyVectorEnv.step()`.
5. Each wrapper calls native `step()`, returning the next observation/reward/done/info tuple; the wrapper discards the native step masks and episode_id.
6. The trainer adds the *pre-action* `obs`, sampled action, log probability, reward, done, value and the separately fetched pre-action masks to RolloutBuffer.
7. It advances `obs` to the returned next observation. On the next iteration, it separately fetches masks for that current state.

`LobbyVectorEnv` is a serial adapter: it iterates through each environment synchronously. After a terminal lobby step, it captures final state and resets the wrapper before returning the reset observation. This makes the next iteration's observation and separately fetched masks operationally correspond to the reset state in the current synchronous flow.

Between a normal step return and the next mask fetch, the audited trainer performs host-side result processing and read-only diagnostics; no second game action is submitted. This supports the intended temporal pairing in the current serial implementation. It is not a typed identity guarantee and must not be upgraded into one by assumption.

## 5. What RolloutBuffer preserves

`RolloutBuffer.add()` stores, at the same temporal pointer:
- observation tensor;
- six-component action tensor;
- log probability, reward, done and value;
- each supplied action-mask tensor;
- valid-agent flag.

Mask tensors are shape-checked and copied into the same rollout index as the observation/action. This preserves the masks actually used for sampling, by temporal array position.

The audited RolloutBuffer does not store native episode_id, Engine-instance identity, player identity, round, native decision sequence, observation sequence, mask source sequence, catalog fingerprint, or an explicit observation/mask/action correlation envelope. Its indexing (`ptr`, agent position) is storage order, not a native decision identity.

The trainer also fetches masks for bootstrap value evaluation, but the existing policy value path ignores masks; this is already documented in the producer-to-PPO audit and is not changed here.

## 6. Evidence-backed disposition

| Boundary / field | Current disposition |
|---|---|
| Native reset episode_id | `native_observed`, present in ResetResult and pybind dict |
| Native step episode_id | `native_observed`, present in StepResult and pybind dict |
| Native reset/step masks | `native_observed`, present in native results and pybind dicts |
| Wrapper reset episode_id/masks | `not_exposed_to_training_caller` |
| Wrapper step episode_id/masks | `not_exposed_to_training_caller` |
| Separately fetched masks | `native_observed_current_state`, returned through get_action_masks |
| Trainer pairing | `synchronous_temporal_pairing_by_call_order`; no typed identity proof |
| Rollout observation/action/masks | `stored_at_same_rollout_pointer` |
| Rollout native episode/player/round/decision identity | `not_stored` |
| Cross-process/global Engine identity | `not_produced` in the audited boundary |

## 7. Important non-findings

- This audit does not demonstrate that observation and mask are mismatched in the current serial training loop.
- It does not establish a concurrent mutation or stale-mask race.
- It does not imply that rollout masks are lost: they are stored alongside the observation/action at the same rollout pointer.
- It does not imply that episode_id is absent from C++ or pybind; it is present there and dropped by the Python adapter.
- It does not make the rollout array index a substitute for episode/player/decision identity.

## 8. Required future acceptance proof

1. Preserve or otherwise bind the native episode and decision identity through wrapper reset/step and mask retrieval; define the exact identity contract before implementation.
2. Prove that the observation, action masks and action submitted for a player share the same native pre-action decision identity.
3. Prove that post-step next observation and next-state masks share the same resulting state identity, including the terminal-lobby reset path.
4. Extend replay fixtures to verify that a stored transition can be reconstructed with its exact pre-action masks and native episode/player/round/decision context.
5. Verify agent ordering across lobby flattening, terminal reset, elimination and rollout storage; array index is not a durable player identity.
6. Keep Engine episode ID, Engine-instance scope, Viewer session ID, player ID, decision sequence and rollout pointer as distinct namespaces.

## 9. Architecture reconstruction review

1. **Prior problem:** native identity/masks were present, but the Python training adapter discarded them and RolloutBuffer retained only temporal storage alignment.
2. **Technical justification:** reproducible action replay and safe projection need explicit correlation of observation, masks, action, player and episode; positional call order alone is insufficient as a durable contract.
3. **New responsibility:** this audit owns the evidence-backed native→pybind→wrapper→Trainer→Rollout correlation boundary.
4. **Contract and invariants:** native result availability differs from training exposure; masks remain independent legality inputs; rollout pointer is not decision identity; no synthetic identity values.
5. **Cross-component impacts:** TFTEngine result structs, pybind dictionaries, CppTFTLobbyWrapper, LobbyVectorEnv, Trainer, RolloutBuffer, policy sampling/evaluation, replay and future decision envelope.
6. **Objective validation:** exact source paths and current call order are recorded; current serial pairing is distinguished from missing typed identity; terminal reset and replay acceptance cases are explicit. Documentation only.

No runtime, schema, tensor-layout, PPO architecture, reward, mask, training, checkpoint, Viewer or Overwolf implementation is authorized by this audit. Issue #346 remains open; Gate 8 remains blocked.