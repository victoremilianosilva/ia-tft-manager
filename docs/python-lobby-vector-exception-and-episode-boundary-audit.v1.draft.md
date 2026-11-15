# Python Lobby Vector Exception and Episode Boundary Audit v1 (Draft)

## Status and scope

Documentation-only source audit on `new-arquiteture`. No runtime behavior is changed. This audit covers (1) exception propagation from the native lobby through `LobbyVectorEnv` and Trainer, and (2) lobby terminal/reset boundaries and the mapping of player experiences into PPO rollout storage.

Primary files inspected:
- `cpp_lobby_env.py`
- `vector_lobby_env.py`
- `trainer.py`
- `rollout.py`

This is a static source audit. It does not claim a reproduced runtime failure, stale-mask race, corrupted rollout, or incorrect native player ordering.

## 1. Exception propagation and partial vector progress

### Native wrapper boundary

`CppTFTLobbyWrapper.step()` validates that exactly eight player actions were supplied, normalizes each action, and calls the native `_engine.step(...)`. It does not catch native exceptions. It only constructs observations/rewards/player metadata after the native call returns successfully.

The native Engine audit documented separately establishes two-phase validation and atomic rejection for the eight-player batch within one lobby. That guarantee is scoped to one native `TFTEngine::step` invocation; it is not a transaction spanning multiple Python lobby instances.

### Vector adapter boundary

`LobbyVectorEnv.step()` iterates through `self.envs` sequentially. For each environment it calls `env.step()`, validates the reward shape, derives player dones, captures terminal state if needed, and appends the results. There is no exception isolation, rollback, or preflight across all lobbies.

Therefore, if lobby N raises after earlier lobbies have returned successfully, those earlier native lobbies may already have advanced while later lobbies have not. The vector call then raises before returning its aggregate tuple. This is a directly supported control-flow consequence, not proof that such a failure has occurred in training.

### Trainer and rollout boundary

Trainer calls `self.vec_env.step(lobby_actions)` before it processes returned infos, rewards, dones, and before `rollout.add(...)`. There is no local catch/recovery around this call in the inspected collection loop. A propagated exception therefore exits the current training call before that step is added to RolloutBuffer.

The existing code does not establish an automatic recovery protocol for continuing after such an exception. If a caller catches the exception externally and reuses the same Trainer/vector environment, the already-advanced earlier lobbies could be out of sync with the unadvanced lobbies and the pre-action observations/actions that were sampled. Do not describe this as a confirmed live bug; it is an unhandled failure boundary and a missing recovery contract.

### Required future acceptance cases

- Inject a failure in a later lobby after an earlier lobby has stepped; assert the documented vector-level policy (fail-stop with all environments discarded/reset, or a deliberately implemented recoverable transaction).
- Assert no partial transition is appended to PPO rollout when vector stepping fails.
- Assert Trainer cannot silently resume from a mixed set of lobby states after a failed vector step.
- Preserve the existing native per-lobby eight-player atomicity tests; do not conflate them with vector-wide atomicity.

## 2. Terminal lobby and reset boundary

For each successful vector step, `LobbyVectorEnv`:
1. Receives the terminal step observation, rewards, lobby_done, and info from the wrapper.
2. Derives per-player dones from the wrapper's current player-alive view.
3. Sets all eight dones to true when `lobby_done` is true, including the winner.
4. Captures `final_state` before reset (using `get_public_state()` when available).
5. Converts the terminal observation to an array.
6. Calls `env.reset()` immediately when the lobby is complete.
7. Returns the reset observation alongside the terminal rewards/dones and terminal info.

Thus the observation returned for a completed lobby belongs to the next episode, while the reward/dones/info describe the just-completed episode. The terminal observation is not returned in the vector observation tensor; the final public state is retained in `info.final_state` for outcome diagnostics.

Trainer processes terminal outcomes from `infos`, then stores the pre-action observation, sampled action, reward, done, value, and masks in RolloutBuffer. Since all eight dones are true at lobby completion, GAE is cut at that boundary; the reset observation becomes the next policy input. This is a conventional auto-reset pattern when the done signal is correctly retained.

## 3. Player-to-rollout mapping

Trainer uses a fixed positional flattening:
`agent_idx = lobby_idx * PLAYERS_PER_LOBBY + player_idx`.

The same ordering is used when:
- Flattening observations, rewards, and dones.
- Building per-lobby action batches from the flat policy output.
- Flattening masks by lobby then player.
- Updating per-agent activity and episode-return arrays.

`CppTFTLobbyWrapper` rebuilds its compatibility `players` list from the native `players` array in enumeration order, assigning each entry its reported `player_id`. `LobbyVectorEnv` derives dones by iterating that list's order. The native ordering contract is source-backed for the inspected reset/step path. TFTEngine::Impl::player_envs is a fixed std::array<PlayerEnv, 8> indexed by player seat; initialize_players() assigns PlayerInfo::player_id = i; build_observations() writes row i from player_envs[i]; TFTEngine::step() writes dones, masks, and StepResult::players[i] from that same index; get_action_masks() preserves the index; and pybind serializes the std::array in iteration order. CppTFTLobbyWrapper.step() enumerates the returned player list without sorting, and LobbyVectorEnv derives dones in that same order. Thus the current native→Python positional mapping is supported for the inspected path, including reset initialization and terminal step result construction. This proves stable seat ordering, not a durable player identity across episodes or Engine instances.

This positional mapping is adequate as an in-memory collection convention only while that ordering invariant holds. It is not a durable player identity and cannot independently correlate an experience to a native Engine instance, episode, round, or decision.

## 4. Rollout identity and episode separation

`RolloutBuffer` stores tensors for observations, actions, log probabilities, rewards, dones, values, advantages/returns, validity, and action masks. Its agent dimension is the flattened `num_lobbies * 8` position. The buffer pointer identifies a time row; the agent index identifies a storage column.

It does not store:
- Native Engine instance scope.
- Native `episode_id`.
- Lobby/match identity.
- Player identity beyond positional column.
- Round or decision sequence.
- A typed reference to the reset/terminal boundary.
- Submitted/effective/executed action resolution.

Prior audits established that native result dictionaries and pybind expose `episode_id`, but `CppTFTLobbyWrapper.reset()` and `step()` return only observations / Gym-style tuple and omit that identity from the Trainer-facing result. This audit confirms that `LobbyVectorEnv` and RolloutBuffer do not restore or add those identity fields.

A lobby reset is therefore represented in PPO by positional continuity plus done bits, not by an explicit old-episode/new-episode identity envelope. This is not proof that GAE currently crosses terminal boundaries: the inspected code marks all eight dones true at `lobby_done`.

## 5. Evidence classification

| Finding | Classification |
|---|---|
| Native exceptions propagate through wrapper | Direct source evidence |
| Vector stepping is sequential and has no cross-lobby rollback | Direct source evidence |
| Later-lobby failure can follow earlier-lobby advancement | Control-flow consequence; not reproduced runtime incident |
| Trainer does not append the failed vector step to rollout | Direct source evidence |
| No in-loop exception recovery/resynchronization | Direct source evidence in inspected collection path |
| Completed lobby captures final state then auto-resets before returning | Direct source evidence |
| Terminal reward/dones pair with reset observation in returned vector tuple | Direct source evidence |
| All eight done flags stop GAE at lobby completion | Direct source evidence from vector dones + Trainer GAE call |
| Player flattening is positional | Direct source evidence |
| Native player ordering across the inspected reset/step→pybind→wrapper path | Direct source evidence: fixed index i is used for observations, masks, dones and PlayerInfo::player_id; wrapper preserves list order |
| Rollout stores no typed Engine/episode/player/decision identity | Direct source evidence |
| Current terminal GAE necessarily crosses episodes | Not supported; code sets done=true |

## 6. Ownership and boundaries

- Native C++ Engine remains authoritative for game state, per-lobby action validation/execution, rewards, observations, masks, and native episode identity.
- `CppTFTLobbyWrapper` is an adapter; it should preserve native identity and failure semantics rather than inventing game state.
- `LobbyVectorEnv` owns vector orchestration and must define what happens when one member fails after others have advanced.
- Trainer owns policy sampling and collection ordering; it must not treat a failed vector call as a valid transition.
- RolloutBuffer owns training transition storage; positional indices are storage coordinates, not domain identity.

## 7. Contract requirements before runtime work

1. Define vector-step failure semantics explicitly: fail-stop/discard all affected lobby instances, or a verifiable transactional/recovery mechanism. Do not silently continue with partially advanced lobbies.
2. Preserve the distinction between terminal transition data and reset observation; include explicit episode identity on both sides of the boundary.
3. Bind each flattened agent slot to stable lobby/player identity for the lifetime of a collected transition.
4. Correlate observation, masks, sampled action, native result, reward components, done, and episode/decision identity in one transition envelope.
5. Keep native masks as separate final legality inputs; this audit does not authorize changing mask ownership.
6. Add deterministic failure-injection and terminal-reset replay tests before claiming acceptance.

## 8. Cross-component impacts

- **Native Engine / pybind:** identity fields already exist at the native result boundary; future work should expose them through the Python adapter without redefining their meaning.
- **Wrapper:** currently drops native episode identity from its Gym-facing return values.
- **Vector environment:** auto-reset changes the returned observation's episode while retaining the previous episode's done/reward/info.
- **Trainer:** uses positional agent columns and done bits; no explicit identity accompanies transitions.
- **Rollout / PPO:** tensors remain numerically aligned by position, but cannot independently audit cross-episode/player correlation.
- **Viewer/replay:** terminal public state is available in info for outcome logging, but this path is not a complete deterministic replay identity envelope.

## 9. Validation criteria

This documentation audit is complete when reviewers can trace the control flow above to the named files. Runtime acceptance remains pending until tests prove:
- Failure in lobby k does not permit silent continuation with mixed episode states.
- No rollout transition is committed for a failed vector step.
- A completed lobby's terminal reward/done and final state remain bound to the old episode.
- The next observation is explicitly bound to the new episode.
- Player identity/order is validated against native records rather than assumed solely from array position.
- Multiple lobbies completing on different steps do not mix their episode boundaries.
- Masks/action/observation remain correlated at each decision boundary.

No runtime code, PPO tensors, reward behavior, masks, checkpoints, or historical artifacts are changed by this audit.

## 10. Native player-order proof and remaining identity boundary

The earlier draft left native player ordering as unverified. A follow-up source trace closes that specific question:

- TFTEngine::Impl::player_envs is std::array<PlayerEnv, kPlayersPerLobby> and all relevant loops use the same index i.
- initialize_players() assigns player_envs[i].info.player_id = i before producing the initial observations and masks.
- build_observations() writes each player's observation into row i from player_envs[i].
- TFTEngine::step() writes dones[i], action_masks[i] and players[i] from player_envs[i]; get_action_masks() uses the same index.
- StepResult::players and action masks are fixed-size arrays. The pybind conversion iterates these arrays in order, and CppTFTLobbyWrapper.step() enumerates the returned player list without sorting or remapping it.
- LobbyVectorEnv derives each done flag by iterating env.players, preserving the wrapper's list order. Trainer flattening uses lobby_idx * 8 + player_idx consistently for observations, rewards, dones, masks and action batches.

**Disposition:** stable positional seat ordering is proven for the inspected native reset/step and Python adapter path. The remaining gap is not ordering; it is durable identity/correlation. player_id is a seat index in the lobby, while native Engine-instance scope, episode ID and decision sequence are not retained in RolloutBuffer. The proof also does not replace deterministic multi-lobby failure-injection tests.

## 11. Architecture reconstruction review

1. **Prior problem:** the initial audit correctly identified positional flattening but left the native ordering invariant unresolved, and did not explicitly separate stable seat order from durable player identity.
2. **Technical justification:** a stable array order supports correct in-memory flattening, but cannot by itself identify an experience across resets, separate Engine objects or replay sessions.
3. **New responsibility:** this addendum owns the source proof for seat-order preservation across native result arrays, pybind, wrapper and vector flattening; Engine/player identity contracts remain owned by their respective identity specifications.
4. **Contract and invariants:** index i must refer to the same seat across observations, masks, rewards, dones and player records within a lobby step; player seat index is not a cross-episode identity; no implicit sorting or reindexing is permitted.
5. **Cross-component impacts:** TFTEngine::Impl, ResetResult, StepResult, pybind conversion, CppTFTLobbyWrapper, LobbyVectorEnv, Trainer flattening and RolloutBuffer identity.
6. **Objective validation:** source trace confirms the same index through the inspected native reset/step and Python conversion path; runtime acceptance still requires tests that compare every player's returned identity/order across normal steps, terminal results, auto-reset and multiple independent lobbies.

No runtime code, tests, observations, masks, rewards, PPO tensors, checkpoints or historical artifacts are changed by this correction.