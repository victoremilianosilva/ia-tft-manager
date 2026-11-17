# Native State Snapshot Contract v1 — Draft

**Status:** bounded runtime sidecar, pending PR review and CI.  
**Related:** #293, #294, #346, #288.  
**Implementation:** PR #455.  
**Base branch:** `new-arquiteture`.

## 1. Prior problem

The Engine already produced useful native audit records for board, bench, shop, economy and item inventory. They were available through a separate `get_audit_snapshot()` diagnostic call, so they were not guaranteed to describe the exact same publication as the observations and action masks selected for a PPO decision. The data could be read after the Engine advanced.

## 2. Technical rationale

A structured fact is useful for replay and future projection only when its producer and decision identity are bound to the same immutable publication as observations and masks. A separate read after the fact is not sufficient evidence of snapshot consistency.

The first producer slice deliberately reuses existing native state and does not synthesize identities or broaden the semantic contract beyond proven source data.

## 3. New responsibility and boundaries

- `TFTEngine::get_audit_snapshot()` remains the native source for this bounded sidecar.
- `ResetResult` and `StepResult` own the immutable copy `native_state_snapshot`, published alongside observations and masks.
- pybind serializes the envelope and records.
- `CppTFTLobbyWrapper` validates identity, version, player count and fixed slot cardinalities.
- `Trainer` expands the eight-player snapshot into the matching per-player rollout row.
- `RolloutBuffer` retains this payload as non-tensor metadata. It is not passed to Actor/Critic encoders.

## 4. Contract and invariants

The envelope contains:
- contract ID `tft.native-state-snapshot`, version 1;
- producer `TFTEngine::get_audit_snapshot`;
- source namespace `tft.engine.observation-snapshot`;
- `engine_instance_id`, `episode_id`, Engine-wide `snapshot_sequence`;
- the eight `player_decision_sequences`;
- round/stage/finished metadata and eight player records.

Each player record contains native economy facts, board (28 slots), bench (9 slots), shop (5 slots), unit champion/catalog identity, raw UnitInstance UUID, star/cost, equipped item catalog IDs, loose component catalog IDs/multiplicity, completed-item inventory catalog IDs, pending-anvil options and the existing audit diagnostics/masks.

Invariants:
1. Envelope identity must equal the enclosing ResetResult/StepResult identity.
2. The snapshot sequence must equal the enclosing Engine-wide decision sequence.
3. The eight per-player counters must match exactly.
4. Exactly eight player records must exist and their player IDs must match array order.
5. Board/bench/shop cardinalities are fixed at 28/9/5; occupied units require nonempty native champion ID and UUID.
6. Missing physical item/component IDs, shop-offer IDs, anvil IDs, pool snapshots, canonical hex coordinates, trait records, action-candidate sets, logical GEP match ID and typed temporal/anti-loop records remain unavailable. No synthetic values are created.
7. Unit UUID remains scoped evidence, not a globally unique or cross-episode canonical identity. Engine/episode/player/sequence envelope context is required, and lifecycle/collision proof remains open.
8. Strategic scores, diagnostics, recommendations, masks and action traces remain sidecar metadata. They do not become Actor/Critic features, PPO labels, rewards or executable commands.
9. Native masks remain the independent exact legality side input; this contract does not replace Action/Mask Contract v1.

## 5. Cross-component impact

The change crosses native result structs, native snapshot producer, pybind, Python wrapper, Trainer metadata expansion and RolloutBuffer metadata. Vector-env terminal auto-reset keeps the result snapshot separate from the next-episode snapshot through the existing metadata flow.

No changes are made to observation dimensions/order, action dimensions/catalog, mask generation/legality, reward formulas, PPO sampling, checkpoints, Viewer or Overwolf.

## 6. Validation criteria

- Native reset and step results carry the same Engine/episode/snapshot/per-player identity in the sidecar.
- Native API tests assert eight player records and 28/9/5 slot cardinalities.
- Wrapper rejects missing, mismatched or malformed structured snapshots and returns defensive deep copies.
- Trainer expands each lobby envelope into exactly the matching player record.
- Existing rollout metadata deep-copy and terminal auto-reset tests continue to pass.
- C++ build, native tests and Python tests pass in CI before merge.

## 7. Explicitly partial producer coverage

This sidecar proves transport for the fields already present in `AuditPlayerSnapshot`; it does not claim all 17 entity kinds in #346 are implemented. The following remain unresolved:
- canonical physical unit identity and collision/lifecycle guarantee;
- stable shop-offer identity/revision;
- physical item/component instance identity;
- authoritative anvil gameplay producer and stable choice identity;
- immutable pool availability snapshot;
- typed trait and canonical board geometry/position entities;
- stable strategic assessment/anchor candidate identities and complete candidate-set envelope;
- authoritative action-opportunity candidate producer;
- typed temporal and anti-loop history;
- real GEP logical match identity and Stage 7 capture validation.

## 8. Architecture reconstruction review

1. **Prior problem:** existing structured native state was only available through a separate diagnostic read, not atomically bound to the observation/mask publication.
2. **Technical justification:** replay and future projection require the same immutable decision identity across observations, masks and structured facts.
3. **New responsibility:** ResetResult/StepResult own the native sidecar; wrapper validates it; Trainer binds each player record; RolloutBuffer preserves it outside neural tensors.
4. **Contract/invariants:** versioned envelope, exact identity equality, strict cardinality, no synthetic fields, no promotion of diagnostics to PPO inputs.
5. **Cross-component impacts:** C++ result structs/producer, pybind, wrapper, vector env, Trainer and RolloutBuffer.
6. **Objective validation:** native/wrapper/Trainer tests plus CI; no tensor/action/reward/checkpoint behavior changes.
