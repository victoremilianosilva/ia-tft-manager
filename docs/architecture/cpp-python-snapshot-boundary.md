# C++/Python snapshot boundary contract

Status: contract for the native lobby training path (binding v1 / native-state snapshot v6).

## Ownership and lifecycle

1. `TFTEngine::reset/step` creates a value-owned native result. The binding converts that result into Python-owned objects; no NumPy view points into a C++ buffer.
2. `reset_to_dict` / `step_to_dict` are the sole producers of the Python result envelope. Each NumPy array and each nested dict/list is newly materialized for that result.
3. `CppTFTLobbyWrapper` validates the native snapshot envelope and its identity before retaining it. After validation, it retains the Python-owned snapshot by reference; it does not deep-copy it.
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
- Retained intentionally: C++ → Python conversion of the full native-state snapshot. This payload is not merely diagnostic: semantic PPO consumes strategic, board, unit, item, trait, economy and pool state; outcome attribution compares pre/post player and inventory facts; reward audit requires paired snapshot identity. Omitting it from the normal path would break training semantics or require a separately synchronized second native read.
- Retained intentionally: conversion of reward components, action traces, masks and player info; each has an active training/audit consumer.

## Why detailed snapshot materialization is not yet optional

A split into a minimal training payload and an optional audit payload is not safe merely by classifying the entire snapshot as “audit”. The same v6 payload currently feeds semantic PPO projection and factual action-outcome/reward auditing. A lazy second read from the engine would also be incorrect unless the native API pins the exact result snapshot: after another step it could return a different decision sequence. Any future split must introduce an immutable, sequence-bound native snapshot handle (or equivalent value) and prove exact parity for semantic tensors, action outcomes, rewards and rollout identity before changing the default path.

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
