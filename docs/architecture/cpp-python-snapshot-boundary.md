# C++/Python snapshot boundary contract

Status: contract for the native lobby training path (binding v1 / native-state snapshot v6).

## Ownership and lifecycle

1. `TFTEngine::reset/step` creates a value-owned native result. The binding moves its `AuditSnapshot` into a `shared_ptr<const AuditSnapshot>` pinned to that exact engine/episode/decision sequence; no later Engine read is involved.
2. `reset_to_dict` / `step_to_dict` publish a `NativeAuditSnapshotHandle`, not an eagerly expanded tree. The handle owns the immutable native value and materializes the normal snapshot mapping only when Python consumers first read it.
3. Combat damage/attack/death event lists are separate lazy fields. Their sequence bounds are validated against the pinned parent `combat_sequence` in C++; Python dictionaries are allocated only if a consumer asks for those fields. The full `get_audit_snapshot()` API still returns the complete eager dictionary.
4. `CppTFTLobbyWrapper` validates the base snapshot contract and identity through a `Mapping` view. `deepcopy` creates an independent Python materialization cache over the same immutable native value, preserving public mutation isolation without copying native event vectors or materializing unused event rows.
4. The wrapper's current snapshot and masks belong to one observation/decision. At step entry, the previous snapshot is held in a local reference as the source decision; the current cache is invalidated before calling C++.
5. The new result is validated and published as the next decision snapshot. The prior source snapshot remains alive until reward audit and outcome attribution finish.
6. Public mask reads detach NumPy arrays. Public metadata reads remain defensive deep copies because callers are allowed to mutate their returned dictionaries.
7. `LobbyVectorEnv` preserves the step-result snapshot separately from a terminal auto-reset's next snapshot. Reward/done refer to the former; returned observations refer to the latter.

## Field → producer → consumer matrix

| Field/group | Producer | Consumer / contract |
|---|---|---|
| `observations` | `observations_to_array` in reset/step binding | Wrapper return; vector environment stacking; Trainer observation batch |
| `rewards`, `dones`, `lobby_done` | `step_to_dict` from `StepResult` | Wrapper return; vector environment; rollout reward/terminal alignment |
| `action_rewards`, `combat_rewards`, `placement_rewards` | `step_to_dict` from `StepResult` | `RewardAuditLedger`; component provenance must not be replaced by combined reward |
| `action_masks` | `masks_to_list` from the same ResetResult/StepResult | Wrapper cache; PPO action selection; public getter returns detached arrays |
| engine/episode/decision/player sequences | ResetResult/StepResult envelope | Wrapper identity validation; player identity envelopes; vector snapshot metadata; rollout alignment |
| `native_state_snapshot` envelope and player state | `audit_snapshot_to_dict` from the same native result | Wrapper schema/identity/integrity validation; semantic PPO projection; before/after outcome attribution; reward audit |
| strategic state, composition, direction, pivot, unit priorities, opportunity costs | `audit_snapshot_to_dict` | `semantic_observation.build_semantic_batch` and downstream PPO semantic state |
| board/bench/shop, units, items, traits, economy and pool | `audit_snapshot_to_dict` | Semantic PPO projection and factual before/after action outcome attribution |
| combat/economy/PvP event collections | `audit_snapshot_to_dict` | Snapshot contract validation and audit/replay provenance; must remain available until a consumer audit proves a narrower contract safe |
| `players` | `player_info_to_list` | Wrapper liveness compatibility; RewardAuditLedger |
| `action_traces` | `step_to_dict` from native action traces | RewardAuditLedger and `build_action_outcome_events` |
| `events`, round/stage/alive metadata | `step_to_dict` | Wrapper info and vector terminal handling / diagnostics |

## Copy and conversion decisions

- Removed: temporary `std::vector<PlayerInfo>` in `step_to_dict`; conversion iterates the native player container directly.
- Removed: deep copy immediately after native snapshot validation. The pybind converter already returns Python-owned containers.
- Removed: copying native mask arrays when normalizing into the wrapper's private cache. The binding creates owned arrays; the public getter still detaches them.
- Removed: deep-copying the previous decision snapshot at the start of a step. A local reference preserves its lifetime while the cache is replaced.
- Retained intentionally: `info["decision_snapshot"]` is a defensive snapshot copy, and `get_snapshot_metadata()` returns a defensive copy. Both cross a mutable public Python boundary; aliasing the wrapper's private snapshot would allow a caller to corrupt the next transition's source facts.
- Optimized: the exact full native snapshot remains available, but high-volume combat event rows are no longer eagerly converted on every reset/step. Strategic, board, unit, item, trait, economy, pool, economy-resolution and PvP-credit data remain in the normal mapping because PPO projection and reward/outcome attribution consume them. Combat event rows are converted on demand from the pinned immutable snapshot; no second Engine read can drift to another sequence.
- Retained intentionally: conversion of reward components, action traces, masks and player info; each has an active training/audit consumer.

## Safe separation of training and audit materialization

The binding now introduces the required immutable, sequence-bound native snapshot handle. It moves the `AuditSnapshot` value out of `ResetResult`/`StepResult` into shared immutable ownership. The Python mapping lazily converts combat damage/attack/death event collections, which are not consumed by the PPO semantic projection, action outcome attribution or reward ledger. Accessing any of those keys still returns the same list-of-dicts schema and exact events as before. The complete observer-facing `get_audit_snapshot()` remains eager and unchanged.

The strategic/player/economy portions remain materialized because they are semantically active. This is a safe first split: defer fields with no hot-path consumer while preserving the full snapshot contract and exact transition identity. A more aggressive field-level split must be based on measured consumer coverage and retain the same pinned-snapshot semantics.

## Required invariants

- A source snapshot is the exact snapshot paired with the action batch; the outcome snapshot is the exact result of that batch.
- Both snapshots share engine and episode identity; decision/player sequences advance according to the native contract.
- Observations, masks, rewards, done flags, traces and snapshots all come from the same native transition.
- No C++-owned mutable buffer escapes through a NumPy view.
- Wrapper-private cached masks/snapshots cannot be mutated through public getters.
- A terminal auto-reset never replaces the snapshot that produced terminal reward/done.
- Schema, identity, geometry, owner and sequence validations remain mandatory.

## Validation evidence

The PR tests cover Python-owned snapshot retention, internal mask-array reuse, and defensive public mask reads. Existing native/Python integration, PPO contract, training smoke and replay CI suites validate the end-to-end consumers. Future removal of the detailed snapshot conversion requires additional parity tests and a pinned-snapshot native API; it is explicitly not claimed by this change.


## Strategic diagnostics and training hot path (#542)

Strategic context production and diagnostic materialization are separate responsibilities. `TFT_COMPOSITION_INTELLIGENCE_ENABLED=1` continues to enable the native composition/planner pipeline, including `StrategicActionCandidateBuilder`, `ContextualActionEvaluator`, and validated `strategic_opportunity_costs` consumed by semantic PPO state.

Diagnostic work is controlled independently by `TFT_COMPOSITION_DIAGNOSTICS_MODE`:

| Value | Behavior |
|---|---|
| `off` (default) | Normal training. No baseline evaluator comparison, action-resolution audit, recorder capture, diagnostic JSON construction/serialization, fingerprints, or retained diagnostic snapshots. |
| `audit` | Produces detailed composition diagnostics and retains up to 4,096 snapshots per player for retrieval through `get_composition_diagnostics_jsonl()`. |
| `debug` | Same complete diagnostic payload as audit, plus per-stage execution trace. Intended for dedicated debugging runs, not normal training. |

The following remain active in `off`, because they produce decision context rather than diagnostic artifacts: native strategic composition generation, active-composition ownership, planner evidence, unit priorities, lineup planning, native action candidate generation, `ContextualActionEvaluator`, and opportunity-cost validation/projection. PPO still selects actions; Shadow recommendations remain non-authoritative.

The frozen baseline `CompositionActionEvaluator`, recommendation-vs-contextual comparison, position proposal serialization, native recommendation resolution, later-outcome correlation, `CompositionDiagnosticRecorder`, `StrategicContextBridge` JSON conversion, snapshot fingerprinting, and JSONL retention are diagnostic-only. They run only in `audit` or `debug`. The diagnostic snapshot buffer is bounded to 4,096 records per player; retrieval returns retained records in global sequence order. Stage trace construction is enabled only in `debug`, not in `audit`. Invalid mode values fail engine initialization rather than silently selecting a different execution mode.

`RewardAuditLedger`, reward decomposition, anti-duplication checks, semantic snapshot fields, masks, and factual action/outcome attribution are outside this switch and remain unchanged.
