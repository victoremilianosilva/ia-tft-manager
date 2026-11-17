# Current Replay, Correlation and Evaluation Gap Audit v1 — Draft

**Status:** static source audit; documentation only, no runtime changes.  
**Tracking:** Gate 7 issues #289/#295; integrated review `docs/gates-1-7-integrated-readiness-review.v1.draft.md`.  
**Base:** `new-arquiteture`.

## 1. Executive finding

The repository has useful diagnostic and replay-adjacent capabilities:
- per-player Composition Intelligence snapshots and stage traces;
- a separate UnifiedStrategicShadowRuntime JSONL sidecar;
- Viewer session logs with monotonic event sequence IDs;
- Viewer log playback;
- a narrow deterministic C++/Python round-barrier and BUY_XP fixture;
- legacy head-to-head checkpoint evaluation with seed/seat rotation.

These do **not** yet form the deterministic multi-round replay and PPO evaluation chain required by Gate 7. Multiple sequence namespaces exist, but the PPO rollout stores no match/player/round/decision identity. Native masks are fetched separately from observations. Viewer log playback does not re-execute the Engine or policy.

## 2. Current identity and sequence namespaces

| Namespace | Current producer | Scope/meaning | Correlation limitation |
|---|---|---|---|
| Engine `episode_id` | TFTEngine | Numeric native match/episode identity used by strategic and diagnostic records | Distinct from ViewerSession UUID; not returned in wrapper reset/step observation tuple |
| `strategic_context_sequences[player]` | TftEngine strategic context builder | Per-player sequence incremented for strategic evidence evaluation | Separate from Composition Intelligence player sequence; not stored in RolloutBuffer |
| Composition Intelligence `player_sequence` | CompositionIntelligencePlayerRuntime | Per-player snapshot/evaluation sequence; ContextBridge uses `next_player_sequence()` | Diagnostic sequence, not a universal source decision sequence |
| Composition Diagnostic `sequence` | CompositionDiagnosticRecorder | Recorder-local snapshot sequence | Separate from outer/global append sequence and player_sequence |
| TftEngine `composition_intelligence_sequence` | TftEngine | Global append sequence across the lobby's Composition Intelligence snapshots | Not the per-player sequence; reset on Engine episode reset |
| Unified sidecar `sequence` | StrategicDirectionPivotAuditRecorder | Per-player emitted-record sequence; unchanged records are deduplicated | Emission sequence, not a decision sequence |
| Unified sidecar `evaluation_sequence` | ContextBridge/Composition Intelligence runtime | References the per-player Composition Intelligence evaluation sequence | Correlates the sidecar to that diagnostic evaluation, not to PPO rollout step |
| Viewer `match_id` | ViewerSession UUID | Session-level ID in metadata and player event logs | Not the numeric Engine episode ID |
| Viewer `sequence_id` | ViewerSession `_sequence` | Monotonic event order within the Viewer session | Not any native or PPO decision sequence |
| PPO rollout pointer/environment index | RolloutBuffer | Tensor time index and flattened agent slot | No native match/player/round/decision ID or source sequence stored |

The namespaces must not be compared directly. The current code does establish some explicit diagnostic correlation, but no single immutable decision identity envelope spans native observation, masks, Shadow diagnostics, Viewer event and PPO rollout.

## 3. Existing diagnostic correlation

### 3.1 Composition Intelligence and ContextBridge

TftEngine supplies numeric Engine episode ID, player ID, round, timestamp and `runtime.next_player_sequence()` to `StrategicContextBridge::adapt`. The resulting metadata includes match/player/round/timestamp/sequence and composition identity/version. The runtime's `append_snapshot` adds match/player/round and a per-player `player_sequence`, then deduplicates unchanged snapshots after removing emission/timestamp fields.

This is a useful diagnostic envelope, but its sequence identifies a Composition Intelligence evaluation/emission. It is not a canonical decision sequence shared with strategic context, action masks, PPO action and rollout.

### 3.2 Unified strategic sidecar

`StrategicDirectionPivotAuditRecorder` emits a per-player sequence and records Engine match ID, player ID, round, machine phase, active composition, pivot candidate, optional confirmed transition, reason and `evaluation_sequence`. The recorder explicitly excludes emission/evaluation sequence values from its deduplication fingerprint so repeated evaluation of unchanged evidence does not advance pivot hysteresis.

This sidecar can be joined to the Composition Intelligence evaluation through `evaluation_sequence` plus match/player/round context. It does not carry ViewerSession UUID or PPO rollout identity directly.

### 3.3 Viewer-to-Engine correlation and a completeness defect

ViewerSession creates a UUID `match_id` and records it in `metadata.json`, player logs and Viewer events. It also records checkpoint SHA-256, seed, deterministic mode, observation dimension and action dimensions.

When persisting Composition Intelligence diagnostics, ViewerSession rewrites the session `match_id` and adds a correlation envelope containing:
- Viewer `match_id` and its source;
- numeric `engine_match_id`;
- player ID, round, timestamp;
- diagnostic sequence;
- composition ID/version.

This provides an explicit Viewer-session ↔ Engine-match mapping for those diagnostic records.

**Current defect:** the code sets `identity_complete` when `player_id`, `round` and `sequence` are integers, but does not require `engine_match_id` to be present/valid. A record can therefore be labeled identity-complete without a proven Engine episode identity. The replay contract requires Engine episode identity for a complete Engine↔session correlation.

The Unified sidecar file is written directly by the native recorder and carries Engine match ID, not Viewer UUID. It can be joined through the Engine ID exposed in Composition Intelligence correlation records, but there is no single shared sequence across the two files.

## 4. Current Python and PPO transition path

- `CppTFTLobbyWrapper.reset()` returns the float32 observation array only.
- `CppTFTLobbyWrapper.step()` returns observation, rewards, done and diagnostic info (players, round, stage, events and reward components). It does not return an observation/mask identity envelope.
- `get_action_masks()` is a separate wrapper call.
- Trainer calls `env_method("get_action_masks")` before policy action selection, then steps the environment. It fetches masks again for value bootstrap.
- `RolloutBuffer` stores observation, action, log probability, reward, done, value, validity and masks in separate tensors. It stores no match ID, Engine episode ID, player ID, round, decision ID or typed source sequence.
- `TFTPolicy.get_value()` ignores masks in the current implementation.

Consequently, the current training path cannot prove from stored rollout data that a particular mask snapshot belongs to the exact observation/action decision. It also cannot join a PPO transition to the Viewer/Shadow sidecars by stable identity.

## 5. Existing replay is not the Gate 7 integrated replay

### 5.1 Viewer replay

Viewer `load_replay()` imports recorded JSON player logs or legacy JSONL, validates schema version and monotonic unique `sequence_id`, and exposes the stored events for navigation. It does not execute the policy, reset/replay the native Engine, regenerate masks, or recompute Shadow state. The repository's `sessions-logs-replay.md` correctly distinguishes this log playback from the Strategic Shadow Integrated Replay Contract.

### 5.2 Cross-language fixture

`tests/fixtures/cross_language_replay.json` covers deterministic round barriers and BUY_XP across Python/C++ actions, comparing state, rewards and stable observation features. Its own description states that board-move reward parity is tested separately because starting-unit RNG is not shared yet.

This is useful cross-language parity evidence, but it does not exercise the full required chain:
observed evidence → candidates → canonical commitment → active composition → unit priorities → lineup → progression/economy → baseline/contextual evaluators → positioning → executor resolution → diagnostics → later outcome.

### 5.3 Current evaluation tooling

The existing `scripts/evaluate_checkpoints.py` and tests cover action serialization, mask plumbing, deterministic head-to-head helpers, paired seeds/seat rotation and rejection of incomplete rankings. Some helper tests use a fake lobby. `docs/evaluation-tooling.md` explicitly says these utilities are not the normative new-lineage promotion protocol.

The approved PPO Evaluation Protocol v1 additionally requires immutable semantic manifests, contract hashes, independent RNG streams, train/validation/test splits, uncertainty/ablations, and promotion/rollback evidence. Those are not integrated into the current Trainer checkpoint payload or legacy evaluator.

## 6. Checkpoint and evaluation identity

The current Trainer saves:
- policy state dict;
- optimizer state;
- scheduler state;
- update number;
- training config;
- scheduler type.

It does not save Observation Schema ID/version/hash, projection identity, Action/Mask contract ID/version/hash, Reward Contract ID/version/hash, catalog/rules fingerprint, encoder/head identity, RNG states, dataset split IDs or evaluation manifest.

Viewer metadata does compute the loaded checkpoint's SHA-256 and records seed, deterministic mode, observation dimension and action dimensions. That is useful artifact identity, but dimension/shape and checkpoint hash do not establish semantic contract compatibility.

## 7. Required post-Gate-8 acceptance

1. Define one immutable decision identity envelope with Engine episode, player, round, decision ID and typed per-producer source-sequence references.
2. Carry that identity through observation, masks, candidate set, action, reward, rollout and diagnostic records.
3. Bind observation and mask snapshots to the same decision; reject stale/mismatched masks before policy evaluation.
4. Fix Viewer correlation completeness so Engine match ID is mandatory for a complete Engine↔session identity.
5. Preserve separate sequence namespaces and explicit correlation records; never equate emission sequence with source decision sequence.
6. Add rollout identity fields so each stored transition can be joined to its observation/mask/action/reward and source diagnostics.
7. Extend deterministic fixtures to the full multi-round strategic chain, including negative cases for missing IDs, stale masks, duplicate snapshots, empty candidates, episode reset and cross-session collisions.
8. Record deterministic seed/config/code/catalog/rules identity and all relevant RNG states.
9. Implement evaluation manifests and paired-seed/seat-rotation/train-validation-test protocol; fail closed on missing semantic hashes.
10. Produce reproducible replay/evaluation artifacts before Gate 7 acceptance.

Issue #289 remains open for integrated multi-round replay. Issue #295 remains open for new-lineage PPO evaluation. Gate 8 remains blocked.

## 8. Architecture reconstruction review

1. **Prior problem:** the repository had several valid local sequence counters and replay-like tools, but no proof that they referred to one decision or could reconstruct the full strategic/PPO transition.
2. **Technical justification:** emission order, per-player evaluation sequence, Engine episode identity, Viewer session order and PPO rollout time have different scopes and reset rules.
3. **New responsibility:** this audit owns the current correlation/replay/evaluation gap inventory; it does not implement a new ID or replay mechanism.
4. **Contract and invariants:** preserve namespace separation; require Engine identity for complete session correlation; no observation/mask/action correlation inferred from adjacency; Viewer log playback is not Engine replay; no checkpoint semantic compatibility inferred from dimensions.
5. **Cross-component impacts:** TFTEngine, CompositionIntelligencePlayerRuntime, StrategicContextBridge, UnifiedStrategicStateMachine/Recorder, ViewerSession, CppTFTLobbyWrapper, Trainer, RolloutBuffer, policy, checkpoint and evaluation tooling.
6. **Objective validation:** each existing sequence, reset, persistence and replay mechanism is mapped to source; missing cross-boundary identities and the Viewer completeness predicate are explicitly identified; no runtime changes.




## Viewer/Engine identity scope clarification — 2026-11-15

The Viewer-to-Engine mapping described in section 3.3 is an explicit **diagnostic correlation** between a Viewer session UUID and the native numeric episode counter for those records. It is not a globally unique Engine episode identity: independent Engine objects can share the same episode_id, and no Engine-instance scope token is currently produced.

Accordingly:
- ViewerSession.match_id is session identity and maps to v2 session_match_id.
- The copied numeric engine_match_id is legacy diagnostic metadata sourced from episode_id; it does not satisfy canonical v2 engine_match_id.
- The current identity_complete predicate remains too weak for canonical identity and does not prove Engine scope or a typed decision sequence.
- A v2 adapter must preserve the legacy values as session/episode metadata and leave canonical identity incomplete until authoritative match_id and scoped engine_match_id producers exist.

See [Observation Schema v2 Identity Field Semantics Reconciliation](observation-schema-v2-identity-field-semantics-reconciliation.v1.draft.md). No runtime changes are made.
