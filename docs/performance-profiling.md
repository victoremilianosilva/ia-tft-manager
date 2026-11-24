# Performance profiling

The profiling suite is opt-in for training and native engine stages. It is designed
to answer four separate questions:

1. How much time is spent in native game/strategy work?
2. How much time is spent crossing the C++/Python boundary and materializing Python data?
3. How much time is spent in Python orchestration, semantic projection and PPO?
4. How much of the observed cost is serialization, memory pressure, GIL contention or
   vector-lobby orchestration?

Profiling does not change game decisions, rewards, masks, snapshots, or PPO updates.
It does add measurement overhead. Always compare profiled and unprofiled runs.

## 1. Rebuild and run the engine benchmark

Rebuild the native extension after pulling this branch because the binding and
`StepResult` contract now expose diagnostic timing fields:

```powershell
cmake --build build --config Release
```

Full controlled benchmark (native engine and Python wrapper, 1 and 4 independent lobbies):

```powershell
python scripts/benchmark_engine.py --mode both --lobbies 1 4 --warmup 10 --iterations 100 --memory-profile --parallel-check --json-out training_runs/full-engine-profile.json --csv-out training_runs/full-engine-profile.csv
```

The benchmark uses the same deterministic PASS workload in native and wrapper modes.
It steps independent engines sequentially for the serial baseline, matching the
current `LobbyVectorEnv` execution model. `--parallel-check` additionally submits
independent lobbies to a thread pool. This measures threaded scaling and dispatch
delay under the current GIL policy; it does not itself release the GIL.

The report contains per-lobby distributions (mean, median, P95/P99, min/max,
throughput), stage distributions, call counters, optional Python allocation tracing,
and process RSS before/after. RSS includes native allocations but is process-wide,
not an exact per-step C++ allocation counter. `tracemalloc` covers Python allocations
only and adds overhead, so memory profiling is enabled separately with
`--memory-profile`.

## 2. Native engine timings

Enable native and wrapper stage timings with:

```powershell
$env:TFT_PROFILE_STEPS = "1"
```

Native timing fields are emitted per engine/lobby:

- `native_engine_action_preflight_ms`: validation and mask preflight.
- `native_engine_action_execution_ms`: action execution loop (inclusive of action-time mask refresh).
- `native_engine_action_mask_refresh_ms`: mask refresh triggered after player actions.
- `native_engine_combat_resolution_ms`: PvP combat resolution when a PvP round resolves.
- `native_engine_pve_item_rewards_ms`: PvE item reward generation.
- `native_engine_economy_resolution_ms`: economy/XP resolution and shop refresh.
- `native_engine_economy_mask_refresh_ms`: masks refreshed after economy/shop changes.
- `native_engine_strategic_refresh_total_ms`: per-player strategic refresh work.
- `native_engine_observation_build_ms`: observation carrier construction.
- `native_engine_audit_snapshot_ms`: native structured snapshot capture.
- `native_engine_event_materialization_ms`: event construction and aggregation.
- `native_engine_step_total_ms`: complete native step.

Strategic refresh is decomposed further:

- `native_strategic_composition_candidates_ms`: native composition candidate/owned evidence refresh.
- `native_strategic_native_runtime_ms`: canonical native strategic runtime input and execution, including its nested sub-stages.
- `native_strategic_native_runtime_input_preparation_ms`: construction of the native strategic cycle input.
- `native_strategic_unified_runtime_refresh_ms`: `UnifiedStrategicRuntime.refresh` execution.
- `native_strategic_shadow_evaluation_ms`: isolated Shadow evaluation envelope, including nested stages.
- `native_strategic_direction_planner_ms`: strategic direction planner.
- `native_strategic_economic_controller_ms`: economic controller.
- `native_strategic_action_evaluator_ms`: contextual action evaluation before Composition Intelligence.
- `native_strategic_composition_transition_proposal_ms`: composition transition proposal.
- `native_strategic_planner_evidence_adapters_ms`: economy, board and item evidence adapters.
- `native_strategic_unit_priority_planner_ms`: unit priority resolution.
- `native_strategic_lineup_planner_ms`: lineup planning.
- `native_strategic_action_mask_population_ms`: strategic native action snapshot mask population.
- `native_strategic_action_candidate_generation_ms`: strategic action candidate generation.
- `native_strategic_composition_action_evaluator_ms`: baseline composition action evaluator.
- `native_strategic_contextual_action_evaluator_ms`: independent contextual action evaluator.
- `native_strategic_context_bridge_and_diagnostic_serialization_ms`: context bridge, diagnostic JSON construction and snapshot append.

Corresponding `native_count_*` values report call counts. Counts are exported
separately from elapsed-time distributions.

Some timings are intentionally inclusive: action execution includes its mask
refresh; strategic refresh totals include the detailed planner stages; the Shadow
envelope includes its sub-stages. Do not add inclusive and nested timings together.
Use the detailed stages to attribute the parent envelope, and calculate the
unattributed remainder rather than double-counting it.

The current instrumentation times the major native strategic producers and
evaluators individually. It does not yet provide per-line timings for every helper
inside those classes; that level of detail should be introduced only if these stage
measurements identify a specific remaining hotspot.

## 3. C++/Python binding timings

The binding reports:

- `binding_action_parse_ms`: conversion of the already pybind-converted action
  vectors into fixed native action structures.
- `native_engine_step_ms`: complete `TFTEngine::step`.
- `binding_observation_array_conversion_ms`: native observation vector to NumPy.
- `binding_reward_and_done_array_conversion_ms`: reward/done arrays.
- `binding_snapshot_handle_conversion_ms`: ownership transfer of the native snapshot handle.
- `binding_action_masks_conversion_ms`: native action masks to Python values.
- `binding_player_info_conversion_ms`: player structures to Python dictionaries.
- `binding_action_traces_and_events_conversion_ms`: action traces and event conversion.
- `binding_result_conversion_ms` / `binding_step_to_dict_total_ms`: aggregate result materialization.
- `binding_total_ms`: parse + native step + result conversion.
- `pybind_call_inclusive`: Python-visible wall-clock duration of the entire pybind call.
- `binding_gil_held_ms`: Python-visible call interval during which the GIL is held.
- `pybind_argument_conversion_overhead_ms`: residual between the Python-visible call
  and the timed C++ lambda regions; includes pybind argument conversion and boundary
  overhead, not pure interpreter time.

The GIL is still held during the pybind call. `--parallel-check` measures concurrent
thread dispatch delay and throughput across independent engine instances, allowing
us to see whether Python threads are serialized at the boundary. It is a contention
experiment, not proof that all dispatch delay is GIL wait.

## 4. Python wrapper and vector environment

The Python wrapper reports:

- action normalization;
- native snapshot handle wrapping;
- NumPy arrays and action-mask materialization;
- snapshot identity validation and projection;
- player-info materialization;
- reward arrays and action-trace materialization;
- action outcome event construction;
- reward audit ledger construction;
- info/deepcopy construction;
- total wrapper time and wrapper-exclusive time outside the binding.

`vector_lobby_env.py` separately reports per-lobby reward conversion, done/snapshot/reset
processing, wrapper-call inclusive time, plus batch stacking and total vector-step time.
Training logs per-lobby values independently; batch-level vector timings are logged
separately.

## 5. Training, semantic projection, policy and PPO

Enable detailed training timings:

```powershell
$env:TFT_PROFILE_STEPS = "1"
$env:TFT_PROFILE_GPU = "1"
$env:TFT_PROFILE_MEMORY = "1"
.\.venv\Scripts\python.exe train_native.py <argumentos habituais>
```

The Trainer records per rollout step:

- semantic projection, tensor construction and semantic contract validation;
- mask retrieval, flattening and audit preparation;
- policy inference host time;
- action materialization, host transfer, audit and lobby action formatting;
- vector environment step;
- next semantic projection;
- transition processing and rollout-buffer write.

It also records per-lobby wrapper/native/vector metrics, rollout collection, bootstrap
and GAE, PPO optimization, and total update time.

PPO internals report:

- advantage normalization;
- minibatch materialization from the rollout;
- loss/forward computation;
- backward;
- gradient clipping;
- optimizer step;
- metric extraction and device synchronization;
- minibatch counts and total PPO update time.

When `TFT_PROFILE_GPU=1` and the policy is on CUDA, CUDA events report GPU execution
time for rollout policy inference, PPO loss, and backward/clip/optimizer stages.
The event collection is synchronized at phase boundaries, not on every rollout step.
GPU event values and CPU wall-clock values are different measurements and must not be
added together.

## 6. Memory metrics

With `TFT_PROFILE_MEMORY=1` during training or `--memory-profile` in the benchmark:

- Python current and peak traced allocation bytes are reported by `tracemalloc`.
- Process RSS before/after is reported when `psutil` is installed; RSS includes native
  C++ heap and Python memory but is process-wide.
- CUDA peak allocated and reserved bytes are reported when using CUDA.

These metrics identify growth and memory pressure, but RSS deltas are not equivalent
to bytes allocated per step. Exact C++ allocation counts would require allocator-level
instrumentation and are intentionally not implemented with global `operator new`
hooks because those hooks would materially perturb the engine.

## 7. Interpretation and limits

- The native PASS benchmark is a controlled microbenchmark, not a representative
  distribution of all in-game actions. It does not execute PPO or semantic batch
  construction.
- Use the training instrumentation to capture real strategic refreshes, combat,
  economy and PPO workloads.
- Compare profiled and unprofiled runs to quantify profiler overhead before drawing
  performance conclusions.
- The current `LobbyVectorEnv` is serial. The thread-pool experiment tests GIL and
  independent-engine scaling without changing training execution.
- The Python-visible pybind interval includes argument conversion and return handling;
  the C++ lambda timings isolate only the regions measured inside the binding.
- Detailed stage timers are diagnostic. Keep the existing game/PPO outputs and
  correctness contracts as the authority when comparing runs.
