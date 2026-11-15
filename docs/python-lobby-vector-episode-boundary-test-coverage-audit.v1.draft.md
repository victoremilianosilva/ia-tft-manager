# Python Lobby Vector and Episode Boundary Test Coverage Audit v1 (Draft)

## Status and scope

Documentation-only inventory of existing regression coverage for the exception and episode-boundary behavior described in [the Python Lobby Vector Exception and Episode Boundary Audit](python-lobby-vector-exception-and-episode-boundary-audit.v1.draft.md).

This review maps existing tests to what they actually prove. It does not claim a reproduced runtime failure, and it does not add or modify runtime tests.

## 1. Prior problem

The source audit established sequential multi-lobby stepping, exception propagation, terminal auto-reset, positional player mapping and the absence of typed episode/player identity in RolloutBuffer. The remaining ambiguity was whether existing tests already covered those Python orchestration boundaries or only their native and PPO subcomponents.

## 2. Existing coverage

### 2.1 Native Engine reset and step contracts

**File:** `tests/test_tft_engine_api.py`

Relevant tests:
- `test_lobby_reset_contract` and `test_lobby_step_contract` (lines 14–72) validate the native pybind reset/step surface and basic lobby result shape.
- `test_observation_reward_done_and_mask_formats` (lines 226–287) validates native observations, rewards, dones and per-player masks.
- `test_reset_accepts_missing_seed` (lines 288–318) verifies that a successful reset advances native `episode_id`.
- Invalid action/seed cases assert that failed native operations do not advance the native round or episode state.

**Proves:** native API shape, basic reset/step behavior, masks, and native episode counter behavior.

**Does not prove:** Python wrapper preservation of episode identity, vector auto-reset pairing, multi-lobby isolation, Trainer recovery, or RolloutBuffer identity correlation.

### 2.2 Complete native terminal match

**File:** `tests/test_full_match_terminal_ranking.py`

`test_native_match_finishes_with_unique_ordered_placements_and_one_reward_each` drives one native Engine match through combat and elimination, then validates unique placements, winner and exactly-once placement rewards.

**Proves:** one native lobby can reach terminal state with a complete ranking and expected placement rewards.

**Does not prove:** `CppTFTLobbyWrapper` terminal return semantics, `LobbyVectorEnv` capture-and-reset behavior, terminal observation versus next-episode observation pairing, or multiple lobbies finishing independently.

### 2.3 Python wrapper smoke test

**File:** `tests/test_lobby_end_to_end.py`

`test_native_lobby_adapter_executes_a_step` (lines 7–28) constructs one `CppTFTLobbyWrapper`, resets it, submits one eight-player PASS batch and validates observation/reward shapes, player count, round and the `lobby_done` boolean.

**Proves:** one wrapper reset and one successful native step through the Python adapter.

**Does not prove:** exception translation/recovery, vector orchestration, terminal auto-reset, episode identity propagation, or multi-lobby partial progress.

### 2.4 RolloutBuffer and PPO mask preservation

**File:** `tests/test_ppo_mask_consistency.py`

Relevant tests:
- `test_full_ppo_update_with_conditional_masks` (lines 504–604) adds a batch to RolloutBuffer, computes GAE/returns and completes a PPO update.
- `test_item_masks_survive_rollout_and_ppo_minibatch_evaluation` (lines 670–734) verifies selected item masks survive RolloutBuffer storage and minibatch extraction, then validates policy log-probabilities against those masks.

**Proves:** numeric transition storage, GAE/update flow and preservation of the exact masks through RolloutBuffer minibatching.

**Does not prove:** native Engine/episode/player/round/decision identity storage, terminal/reset identity pairing, or recovery after a failed vector step.

## 3. Coverage matrix

| Behavior | Existing evidence | Coverage status |
|---|---|---|
| Native reset increments episode ID | `test_tft_engine_api.py::test_reset_accepts_missing_seed` | Covered at native API |
| Native step returns observation/reward/done/masks | `test_tft_engine_api.py::test_observation_reward_done_and_mask_formats` | Covered at native API |
| Full match reaches terminal ranking and grants placement rewards once | `test_full_match_terminal_ranking.py` | Covered at native Engine |
| Wrapper can reset and execute one successful step | `test_lobby_end_to_end.py` | Smoke coverage |
| Rollout stores observations/actions/rewards/dones/masks and supports PPO update | `test_ppo_mask_consistency.py` | Covered numerically |
| Rollout preserves masks through minibatches | `test_item_masks_survive_rollout_and_ppo_minibatch_evaluation` | Covered |
| Later-lobby exception after an earlier lobby advances | No dedicated vector failure-injection test identified | Missing |
| Vector call failure cannot leave reusable mixed lobby states | No vector fail-stop/recovery test identified | Missing |
| Failed vector step does not commit a rollout transition | No Trainer/vector failure-boundary test identified | Missing |
| Terminal reward/done/final state remain bound to old episode while returned observation belongs to new episode | Native and wrapper tests cover separate pieces, not the vector boundary | Missing |
| Different lobbies can auto-reset on different steps without identity mixing | No multi-lobby terminal replay test identified | Missing |
| Player seat order is checked across observations, masks, rewards, dones and player records at reset/terminal | Source order is now proven in #385; end-to-end regression assertion not identified | Missing |
| Rollout records durable Engine/episode/player/decision identity | Rollout tests validate tensor alignment/masks, not typed identity | Missing |

No dedicated `test_vector_lobby_env.py` file is present in the inspected test tree. The tests above cover native Engine, wrapper smoke behavior and RolloutBuffer/PPO separately; they do not compose those layers into the vector failure/reset boundary.

## 4. Required acceptance tests before runtime integration

1. **Cross-lobby failure injection:** use at least two deterministic fake/native lobby adapters; let the first step succeed and a later lobby throw. Assert the chosen vector policy (fail-stop/discard all affected instances or a genuinely transactional recovery) and prohibit silent reuse of mixed states.
2. **Trainer commit boundary:** assert that a failed vector step does not advance RolloutBuffer.ptr or append any partial transition; assert that Trainer cannot resume without an explicit reset/reconstruction policy.
3. **Terminal auto-reset binding:** assert that the old episode's reward, all-player done flags and final state remain associated with the terminal transition while the returned observation and masks are explicitly identified as belonging to the next episode.
4. **Independent lobby completion:** run multiple lobbies that finish on different vector steps; verify each lobby's reset and episode transition independently.
5. **Seat-order regression:** compare player_id and row index across observations, masks, rewards, dones and PlayerInfo for initial reset, ordinary step, terminal result and post-reset observation.
6. **Rollout identity correlation:** if the future approved contract transports identity, assert that Engine scope, episode, player, round and decision sequence remain attached to the exact observation/action/reward/done/mask transition through minibatch extraction.

These are acceptance requirements, not authorization to implement them now. Native masks remain separate final legality inputs.

## 5. Architecture reconstruction review

1. **Prior problem:** native API, wrapper smoke, terminal-match and RolloutBuffer tests existed, but their coverage boundaries were easy to conflate with end-to-end vector orchestration coverage.
2. **Technical justification:** a passing native test or PPO tensor test cannot establish multi-lobby exception isolation, reset correlation or Trainer recovery.
3. **New responsibility:** this document owns the regression-coverage map for the Python vector/episode boundary; the source audit owns implementation facts and the native Engine owns per-lobby game semantics.
4. **Contract and invariants:** distinguish native per-lobby atomicity from vector-wide failure semantics; preserve terminal reward/done/final-state identity; preserve next-episode observation identity; masks remain separate; do not infer durable identity from positional columns.
5. **Cross-component impacts:** native TFTEngine/pybind, CppTFTLobbyWrapper, LobbyVectorEnv, Trainer, RolloutBuffer, PPO update and replay acceptance.
6. **Objective validation:** each existing coverage claim is tied to a named test and bounded to what it asserts; every missing vector/reset/identity scenario has a deterministic acceptance description; documentation only.

No runtime, test, schema, tensor, PPO, reward, mask, training, checkpoint, Viewer or Overwolf changes are made by this audit. Issue #346 remains open; Gate 8 remains blocked.
