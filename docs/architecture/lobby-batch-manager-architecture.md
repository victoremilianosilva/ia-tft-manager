# LobbyBatchManager architecture and performance non-regression contract

Status: accepted architecture direction; implementation must follow the gates below.
Target branch: `new-arquiteture`.

## 1. Decision

Adopt the hybrid architecture:

- One `TFTEngine` owns and simulates exactly one complete TFT lobby (eight players).
- A native `LobbyBatchManager` owns and coordinates multiple independent `TFTEngine` instances.
- Python remains the PPO/training orchestrator. It supplies action batches and consumes compact transition batches; it does not coordinate per-lobby native calls in the hot path once the manager is integrated.

Important baseline correction: the current `TFTEngine` is already lobby-scoped. Its `step` contract accepts `std::array<PlayerAction, kPlayersPerLobby>`; reset/step results carry per-player observations, rewards, dones, masks and player records. The migration is therefore not a rewrite from player-engine to lobby-engine. It is an additive native batch orchestration layer around the existing lobby engine.

## 2. Problems this design must not reproduce

The existing path has several independently confirmed costs and sources of complexity:

1. `LobbyVectorEnv.reset/step` loops through Python lobby objects sequentially.
2. The pybind boundary creates nested Python dictionaries/lists for masks, player info, traces and snapshot content. The immutable native snapshot handle avoids eagerly expanding some event lists, but the normal snapshot still has a substantial Python representation.
3. `CppTFTLobbyWrapper._copy_native_state_snapshot` validates a large contract and nested player structures.
4. `semantic_observation.project_native_player_state` validates overlapping structures again, traverses board/bench/shop, rebuilds semantic features and serializes canonical content for hashes.
5. `Trainer._expand_lobby_snapshot_metadata` expands one lobby snapshot into eight player metadata objects and deep-copies each `native_player_state`.
6. `RolloutBuffer.add` deep-copies decision/result/next metadata groups; later metadata accessors deep-copy again for callers.
7. `build_action_outcome_events` reconstructs factual unit/shop/economy changes by diffing before/after snapshots even though the native engine executed the action and has the source facts.
8. The pybind step/reset calls have not yet established a safe GIL-release boundary. Threading the existing Python vector loop must not be treated as native parallel execution.
9. Existing benchmark coverage is incomplete: the engine/wrapper benchmark disables PPO and semantic-batch work and steps lobbies sequentially. It does not prove full training throughput or parallel speedup.

The earlier measured reference (from the separately instrumented benchmark branch, not a guarantee for every checkout) was approximately 4.8 ms per native lobby step versus 109.9 ms per wrapper lobby step. The wrapper's largest measured stage was snapshot validation/projection (~71 ms), followed by info/deepcopy (~18 ms) and action/outcome events (~4.8 ms). These numbers are a baseline signal, not acceptance criteria by themselves; the same benchmark configuration and environment must be rerun on the target branch before claiming a gain.

## 3. Component responsibilities

### TFTEngine (one lobby)

- Owns all eight player states and all lobby-shared state: shared unit pool, economy/round resolution, matchmaking/opponents, combat, ranking and terminal state.
- Accepts exactly eight player actions for one decision boundary.
- Produces one coherent transition revision: observations, masks, rewards, dones, traces, player records, immutable snapshot and identity sequences.
- Owns the authoritative factual action/outcome events where those facts are known at execution time.
- Does not know about other lobbies, PPO batches, Python rollout storage or optimizer state.

### LobbyBatchManager (many lobbies)

- Owns a collection of independent lobby engines and their lifecycle.
- Exposes batch reset/step APIs with explicit lobby dimensions and stable lobby indices.
- Validates outer batch dimensions once; delegates each inner eight-player action batch to its corresponding engine.
- Initially supports deterministic sequential execution through the same API, then parallel execution through a bounded native worker pool.
- Aggregates results into stable, contiguous batch buffers and per-lobby identity/result descriptors.
- Does not merge lobby state, share RNG streams, or introduce cross-lobby gameplay dependencies.
- Does not implement game rules, strategy selection, PPO policy inference, reward learning or optimizer operations.

### Python Trainer / PPO

- Remains the owner of policy inference, action sampling, rollout semantics, GAE, loss calculation and optimizer updates.
- Continues to consume the same logical per-player observations, masks, rewards, done flags and provenance.
- Calls the manager once per batch rather than issuing one Python-to-C++ call per lobby.
- Must not reconstruct native facts or expand full audit snapshots merely to prepare the ordinary PPO hot path.

## 4. Batch API and data contract

The public native API should be batch-oriented and versioned. Exact C++ type names can be finalized during implementation, but semantics must match:

- `reset(seeds[N]) -> BatchResetResult`
- `step(actions[N][8], timer_options[N]) -> BatchStepResult`
- `close()/reset_all()` with explicit lifecycle behavior.

Required invariants:

1. The outer dimension is the number of lobbies; the inner dimension is exactly eight players.
2. Every result row is paired with the same lobby index and the exact engine/episode/decision identity that produced it.
3. Observations, masks, rewards, dones, traces, factual events and snapshot handles in one result refer to the same transition.
4. Terminal reward/done provenance remains separate from any auto-reset observation.
5. Each lobby owns an independent RNG stream derived deterministically from the caller seed and stable lobby identity. Scheduling order must never change random sequences.
6. Result aggregation order is stable and independent of worker completion order.
7. A failed lobby step must have explicit failure semantics. The manager must not silently return a partially advanced batch as if it were atomic. The contract must identify failed lobby indices and require a full batch reset when state alignment cannot be recovered.
8. No pointer or view into mutable engine-owned memory may outlive its documented lease. Prefer immutable, sequence-bound snapshot handles or owned contiguous result buffers.
9. No Python object or Python callback may be accessed while a worker is executing native code without the GIL.
10. Batch capacity and worker count are bounded and configurable; no unbounded thread creation per step.

## 5. Performance rules: do not carry old bottlenecks forward

### 5.1 One authoritative validation boundary

- Keep strict schema, identity, geometry, owner and sequence validation.
- Separate integrity validation from semantic feature projection.
- Validate a native snapshot once at the trusted boundary, then pass a validated immutable view/typed handle to downstream consumers.
- Do not repeat full nested validation in wrapper, Trainer and semantic projection for the same immutable revision.
- Do not remove validation until parity and corruption tests prove the replacement contract is at least as strong.

### 5.2 Do not expand full snapshots into Python dictionaries on the PPO hot path

- The manager must not return `N * 8` independent nested dictionary trees as its primary training payload.
- Prefer contiguous typed arrays/buffers for observations, rewards, dones and masks.
- Semantic PPO inputs should be emitted as compact typed projections or built through a consumer-specific native projection API, not by repeatedly traversing a generic audit dictionary.
- Preserve the full immutable audit snapshot through a lazy/explicit audit interface for replay, debugging and provenance consumers.
- Large audit-only collections remain lazy and must not be materialized unless requested.

### 5.3 Eliminate repeated deep copies through ownership, not by weakening isolation

- Keep native snapshots immutable and identity-bound.
- Use shared immutable handles or compact immutable records across decision/result/next references when they represent the same revision.
- Rollout storage should own only the data it truly needs for training and the configured audit retention.
- Public mutable APIs must still return isolated values; do not expose mutable internal buffers to save time.
- Avoid expanding one lobby snapshot into eight deep-copied player dictionaries when a batch/player view can reference the immutable lobby snapshot plus player index.

### 5.4 Produce factual outcomes where they occur

- The engine should emit compact factual events for action execution: accepted/rejected action, selected offer identity/revision, unit UUID additions/removals/upgrades, shop revision changes, economy deltas and other facts already known during execution.
- Python may continue to derive policy-level labels, PPO reward shaping and training targets.
- Do not move PPO reward semantics or strategy decisions into the batch manager.
- Event parity must cover failed actions, simultaneous round/shop resolution, item actions, upgrades, sales, rerolls and terminal transitions before replacing snapshot-diff reconstruction.

### 5.5 GIL and worker execution

- First implement the manager with deterministic sequential execution and prove API parity.
- Parallelize only independent `TFTEngine` instances.
- Release the GIL only around pure native work, after proving the call path performs no Python API access, Python callbacks or Python object destruction requiring the GIL.
- Keep Python object conversion and result publication under the GIL, or redesign results as native buffers that can safely be copied/published afterward.
- Do not claim threads are parallel while the GIL is held.
- Do not parallelize the eight players of one lobby as independent tasks: they share pool, economy, combat, round and matchmaking state.

## 6. Migration sequence and gates

### Gate A — Baseline and ownership map

- Confirm all mutable state owned by one `TFTEngine`, including shared pool, player environments, RNG, combat and round coordinators.
- Capture target-branch baseline with fixed seed, lobbies, warmup, iterations and machine details.
- Profile native step, binding conversion, wrapper validation, semantic projection, outcome extraction, rollout storage, policy inference, GAE and optimizer separately.
- Record memory both for Python allocations and process/native allocations.

### Gate B — Batch manager, sequential parity

- Add manager ownership and batch API without changing `TFTEngine` rules.
- Run the same seeds/actions through old vector orchestration and new manager.
- Compare per-lobby observations, masks, rewards, dones, traces, events, player state, snapshot identities and terminal/reset behavior.
- Confirm exception and partial-failure semantics.

### Gate C — Compact data boundary

- Replace nested per-player dictionary materialization in the training path with typed contiguous batch buffers and immutable snapshot/player views.
- Move duplicate validation to one boundary while retaining all invariant checks.
- Preserve semantic feature values, champion IDs, missingness, normalization, identity envelopes and canonical hashes.
- Add parity tests for old and new projections; do not change PPO inputs or action decisions as part of this migration.

### Gate D — Factual event production

- Emit native factual action outcomes from the authoritative action execution point.
- Compare event-by-event against the existing Python snapshot-diff producer across the complete action matrix and edge cases.
- Keep the Python producer as a test oracle until parity is established; remove it from production hot path only after evidence is complete.

### Gate E — Native parallel execution

- Add a bounded worker pool over independent lobbies.
- Test determinism across worker counts, scheduling perturbations and repeated runs.
- Test no shared mutable state, no RNG coupling, no cross-lobby contamination and safe shutdown/error recovery.
- Verify actual overlap in native execution; do not infer it from thread count or wall-clock variance.

### Gate F — Full PPO throughput and memory acceptance

- Benchmark end-to-end training with PPO enabled, semantic batches enabled, rollout storage, GAE and optimizer included.
- Compare 1/2/4/8+ lobbies, sequential manager versus parallel manager, fixed hardware/software and equivalent seeds/work.
- Report lobby-steps/sec, player-decisions/sec, p50/p95/p99 latency, CPU utilization, memory (Python and process RSS), copy/materialization counts and per-stage timings.
- Verify learning inputs and action/mask/reward semantics are unchanged.
- Do not merge based solely on a faster native microbenchmark.

## 7. Required regression tests

- Eight-player lobby ownership and shared-pool correctness.
- Multi-lobby isolation for pool, RNG, economy, combat and episode identity.
- Batch ordering stable under out-of-order worker completion.
- Same seeds/actions produce identical results in sequential and parallel modes.
- Exact observation/mask/reward/done/snapshot revision correlation.
- Terminal auto-reset separation.
- Snapshot schema/identity/geometry/sequence corruption rejection.
- Semantic projection numeric/champion-ID/hash parity.
- Action outcome parity for every action family and failed/overlapped resolution.
- Buffer lifetime, immutable snapshot retention and no use-after-free.
- Worker exception, cancellation, shutdown and full-reset recovery.
- Full PPO smoke and checkpoint compatibility.

## 8. Explicit non-goals

- Moving PPO inference, GAE, loss or optimizer to C++.
- Changing policy architecture, reward semantics, strategic decision logic or action masks.
- Parallelizing players inside a lobby as if they were independent simulations.
- Replacing audit/replay provenance with a lossy training-only payload.
- Removing identity, sequence, ownership or schema validation to improve benchmark numbers.
- Claiming a speedup from native-only timing while Python projection/materialization remains unmeasured.

## 9. Acceptance principle

The new architecture is accepted only when it improves end-to-end training throughput and/or memory while preserving deterministic game behavior, PPO input semantics, reward/mask contracts, snapshot provenance and checkpoint compatibility. A bottleneck moved from Python into a native manager, or hidden behind a batch API without being removed, is not considered fixed.
