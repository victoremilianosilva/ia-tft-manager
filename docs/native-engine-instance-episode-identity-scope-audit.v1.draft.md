# Native Engine Instance and Episode Identity Scope Audit v1 — Draft

**Status:** source-backed static audit; documentation only.  
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).  
**Base:** `new-arquiteture`.  
**Related:** [Viewer–Engine Session Correlation Source Audit v1](viewer-engine-session-correlation-audit.v1.draft.md); [Engine Episode Identity Reset Reconciliation](engine-episode-identity-reset-reconciliation.v1.draft.md).

## 1. Purpose

Determine whether the native `TFTEngine` exposes an identity for the Engine object itself, establish the actual scope and lifecycle of `episode_id`, trace its pybind and Python-wrapper propagation, and reconcile the earlier Viewer↔Engine audit with the source.

This is an audit only. It does not modify the Engine, bindings, wrapper, PPO, masks, Viewer, schema or runtime.

## 2. Native object and episode identity

### 2.1 Object construction and ownership

`TFTEngine` owns a private `std::unique_ptr<Impl>`. Its constructor creates a new `Impl` from the supplied seed and catalog paths. The public type deletes copy construction/assignment and supports defaulted move construction/assignment.

The audited constructor and `Impl` fields expose no Engine-instance UUID, globally unique token, process/session namespace, or externally supplied instance identity. The `Impl` contains:
- `seed`;
- `episode_id`, initialized to zero;
- matchmaking RNG and other mutable match state.

Therefore the source proves an episode counter scoped to an `Impl` lifetime, but does **not** prove a unique identity for that `Impl` or its owning `TFTEngine`.

Defaulted move operations transfer the `unique_ptr` and therefore transfer the existing `Impl` state with it. They do not mint or publish an Engine identity. Move assignment replaces the destination's owned implementation state; no generation/token is emitted to identify that replacement.

### 2.2 Episode lifecycle

`TFTEngine::reset()` increments `impl_->episode_id` before rebuilding match state. The counter is not reset to zero inside that method. Reset results publish the resulting episode ID; step results publish the current episode ID. The `episode_id()` accessor returns the counter when `impl_` exists and zero for a moved-from/null implementation.

Consequences:
- The first successful reset on a newly constructed object produces episode ID 1.
- Repeated resets on the same `Impl` increment the counter.
- Two independently constructed Engines begin with independent counters and can both produce episode ID 1, 2, etc.
- The numeric episode ID is not globally unique and is not sufficient by itself to join records across Engine objects, processes, or Viewer sessions.
- No overflow policy for the uint64 counter was identified in the audited reset path.

### 2.3 Seed and UnitInstance UUID interaction

On reset, `UnitInstanceFactory` is reconstructed from `impl_->seed`, not from a seed mixed with `episode_id`. The factory uses a deterministic `std::mt19937_64` seeded by that value to generate UUID-shaped strings.

Thus same-seed Engine objects, or repeated resets of the same Engine using the same base seed, can regenerate the same initial UnitInstance UUID sequence. The episode counter does not currently namespace those UUIDs. This confirms the prior audit: UnitInstance UUID is useful as an in-episode physical-instance handle under the observed ownership lifecycle, but is not a globally unique cross-episode identity.

## 3. Native result and pybind propagation

The C++ result contracts include `episode_id`:
- `ResetResult` has an `episode_id` field.
- `StepResult` has an `episode_id` field.
- `TFTEngine::reset()` assigns the incremented ID to `ResetResult`.
- `TFTEngine::step()` assigns the current ID to `StepResult`.

The pybind conversion functions preserve that field:
- `reset_to_dict()` emits `result["episode_id"] = reset.episode_id`.
- `step_to_dict()` emits `result["episode_id"] = step.episode_id`.
- The binding also exposes a read-only `episode_id` property mapped to `TFTEngine::episode_id()`.

**Correction to any broad reading of the prior Viewer audit:** native C++ and pybind do not drop the episode ID from reset/step results. They expose it correctly at that boundary. The loss occurs in the higher-level Python adapter described below.

## 4. Python wrapper propagation

The root-level `cpp_lobby_env.py` constructs one native `TFTLobby` and stores it as `self._engine`.

- `CppTFTLobbyWrapper.reset()` calls `self._engine.reset(seed)`, but returns only `result["observations"]`. The native `episode_id` and reset masks are not included in the wrapper return value.
- `CppTFTLobbyWrapper.step()` receives the native result, but its returned `info` contains players, round, stage, completion flags, events and reward components. It omits `result["episode_id"]`.
- `get_action_masks()` invokes a separate native method and returns masks without attaching an episode or decision identity.
- The wrapper does not expose a public episode identity property or a session-to-Engine scope mapping.

This establishes the precise boundary: **native Engine → pybind preserves episode ID; pybind → `CppTFTLobbyWrapper` discards it from the training-facing reset/step contract.**

The wrapper retains the native object in `self._engine`, so code with direct private access could query its property, but no such access is part of the wrapper's public reset/step/mask contract. Private reachability is not an identity propagation guarantee.

## 5. Identity namespace matrix

| Identity | Producer / owner | Actual scope | Cross-object uniqueness |
|---|---|---|---|
| Engine object identity | No producer found | Not represented | Not established |
| `episode_id` | `TFTEngine::Impl` counter | One Impl lifetime | No |
| Viewer `match_id` | Python `ViewerSession` UUID | One Viewer session | UUID-shaped, but no explicit Engine binding by itself |
| UnitInstance `uuid` | `UnitInstanceFactory` seeded RNG | Generated instance sequence within seeded factory | No; repeatable across same-seed resets/objects |
| Viewer `sequence_id` | Viewer event emitter | One Viewer event stream | No; separate namespace |
| Composition Intelligence sequence | Native diagnostic/runtime counters | Its own reset/cycle scope | Not interchangeable with episode ID |
| PPO rollout index | Rollout storage position | Buffer/collection scope | Not a source identity |

## 6. Contract implications

A valid future cross-component identity must distinguish at least:
1. Engine instance/scope identity;
2. episode ID within that Engine scope;
3. player identity within the episode;
4. decision identity within the player/episode;
5. producer-specific sequence namespaces.

A proposed composite scope such as `(engine_instance_id, episode_id)` is a semantic requirement, **not** an approved field name, wire format, or implementation choice. The exact Engine-instance identity source, persistence, process boundaries, serialization and lifecycle must be designed and reviewed after Gate 8.

Do not:
- treat `episode_id` alone as globally unique;
- use the seed as Engine identity;
- use UnitInstance UUID as cross-episode identity;
- use Viewer UUID as a substitute for Engine scope;
- infer identity from timestamps, pointer addresses, object allocation order, equal numeric counters or array positions;
- claim masks are bound to an observation because they were fetched from the same wrapper object.

## 7. Required post-Gate-8 acceptance

1. Construct two Engines with the same seed and prove their Engine scopes are distinct while their local episode counters may match.
2. Reset one Engine repeatedly and prove episode IDs advance within its stable Engine scope.
3. Move-construct and move-assign Engines; prove the intended scope identity lifecycle and replacement semantics.
4. Recreate an Engine object and prove no stale records can join to its new episodes.
5. Preserve Engine scope + episode identity through pybind reset/step, Python wrapper, vectorized environments, Viewer events/diagnostics, masks and PPO rollout storage.
6. Reject masks, observations, actions, rewards and transitions whose Engine scope or episode differs.
7. Verify same-seed UnitInstance UUID repetition is harmless only when correctly scoped, and prove no cross-episode ownership joins occur.
8. Test terminal lobby reset and multiple simultaneous Engine objects.
9. Keep all sequence namespaces typed and independently validated.

These are acceptance requirements, not runtime work authorized by this audit.

## 8. Architecture reconstruction review

1. **Prior problem:** episode identity had been traced, but the global Engine-object scope and exact native→pybind→wrapper propagation boundary remained unresolved.
2. **Technical justification:** `episode_id` is a per-`Impl` counter, while independently constructed Engines can share the same numeric values; using it alone permits cross-Engine collisions.
3. **New responsibility:** this note owns the source-backed Engine-object scope, episode counter lifecycle, UnitInstance UUID interaction and native-to-Python identity propagation findings.
4. **Contract and invariants:** Engine scope and episode are separate; pybind preserves episode ID; the Python wrapper currently drops it from training-facing results; seeds and UUIDs are not global identity; all downstream joins require explicit scope.
5. **Cross-component impacts:** `TFTEngine::Impl`, `ResetResult`, `StepResult`, pybind bindings, `cpp_lobby_env.py`, `LobbyVectorEnv`, Viewer session/diagnostics, masks and PPO RolloutBuffer.
6. **Objective validation:** constructor/Impl fields, reset/step/accessor, move semantics, pybind result dictionaries and Python wrapper returns are source-traced; duplicate episode scopes and repeated UnitInstance UUID sequences are explicitly identified; no runtime or tensor changes are made.

Issue #346 remains open. Gate 7 executable acceptance remains pending. Gate 8 remains blocked.
