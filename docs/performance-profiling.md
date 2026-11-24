# Performance profiling

This instrumentation is opt-in for per-step Python stage timing and always records
small C++ timing fields in the pybind result. It does not change game decisions,
rewards, masks, snapshots, or PPO updates.

## Engine and wrapper benchmark

Rebuild the native extension after pulling the branch (the binding source changed):

```powershell
cmake --build build --config Release
python scripts/benchmark_engine.py --mode both --lobbies 1 4 --warmup 10 --iterations 100 --json-out training_runs/engine-profile.json --csv-out training_runs/engine-profile.csv
```

The benchmark runs the same deterministic PASS workload in native and wrapper modes.
It steps lobbies sequentially, matching `LobbyVectorEnv`. It reports each lobby
separately and records per-stage distributions (mean, median, p95, p99, min, max).

C++/pybind timing fields:
- `binding_action_parse_ms`: conversion from the already Python-converted action
  vectors into the fixed native action array.
- `native_engine_step_ms`: time inside `TFTEngine::step`.
- `binding_result_conversion_ms`: conversion of the native StepResult into Python
  objects and arrays.
- `binding_total_ms`: the sum of the three measured C++ binding regions.

Python wrapper timing fields:
- `python_action_normalization`
- `pybind_call_inclusive`
- `python_arrays_and_action_masks`
- `python_snapshot_projection_and_validation`
- `python_action_outcome_events`
- `python_reward_audit`
- `python_info_and_deepcopy`
- `python_wrapper_total`

The Python wall-clock around the pybind call includes the native engine and binding
work. The C++ subfields let the report separate those parts from the Python-side
remainder. The Python action-to-`std::vector` argument conversion performed by
pybind before entering the lambda remains part of the inclusive call remainder.

## Training instrumentation

Set `TFT_PROFILE_STEPS=1` in the process environment to attach per-lobby wrapper
stage timings to each `info` result. During training, `trainer.py` aggregates
those samples per update and writes TensorBoard scalars under:

- `performance/wrapper_total_ms/*`
- `performance/wrapper_mean_ms/*`
- `performance/update/rollout_collection_ms`
- `performance/update/bootstrap_gae_ms`
- `performance/update/ppo_optimization_ms`
- `performance/update/total_through_ppo_ms`

PowerShell:

```powershell
$env:TFT_PROFILE_STEPS = "1"
..venv\Scripts\python.exe train_native.py <the usual training arguments>
```

Unset the variable after profiling:

```powershell
Remove-Item Env:TFT_PROFILE_STEPS
```

## Interpretation and current limits

- `native_engine_step_ms` is the complete C++ engine step for each lobby. It includes
  action validation/execution, round/combat/economy resolution when triggered,
  strategic state/mask refresh, reward calculation, and native snapshot production.
  Those internal C++ responsibilities are not yet timed independently.
- The current GIL is held across the pybind call. This benchmark measures its
  inclusive wall-clock cost but does not yet run a GIL-release variant.
- The native/wrapper PASS benchmark is a controlled microbenchmark, not a complete
  game workload. It does not run PPO or semantic-batch construction.
- Training TensorBoard timings separate rollout collection, bootstrap/GAE, and PPO
  optimization. The collection bucket still contains semantic projection, mask
  handling, policy inference, environment stepping, and rollout writes; use the
  per-lobby wrapper fields to isolate the adapter portion.
- Profiling is intended for diagnosis. Compare profiled runs with unprofiled runs
  to quantify instrumentation overhead before making performance claims.
