# Phase C — Integrated audit for #574–#578

## Scope and implementation boundary

This audit treats #574, #575, #576, #577 and #578 as one coordinated Decision Context migration on the existing #583 branch. The work must preserve the current PPO policy input and behavior until an explicitly versioned neural expansion is approved. Native context is metadata/audit input first; it must not become an implicit planner execution path.

The Engine remains authoritative for game state, action legality, action execution, and factual outcomes. Changes in this tranche may add read-only projections and event transport, but must not alter simulation rules, lifecycle, ordering, RNG, determinism, rewards, masks, action sampling, PPO updates, or checkpoint compatibility.

## Current architecture found on the #583 head

| Area | Existing owner/source | Existing transport/consumer | Audit finding |
|---|---|---|---|
| Entity identity | #573 native board/bench/shop snapshots; UUID and champion internal ID | `AuditUnitSnapshot`, binding dictionaries, semantic v8 projection | Stable physical identity is available and must remain the only entity key. |
| Strategic context (#574) | `ActiveCompositionManager`, `UnitPriorityPlanner`, `LineupPlanner`, direction/pivot anchors, `UnitCopyProgress`, opportunity-cost evidence | `AuditStrategicOwnerSnapshot` v4; Python structured `strategic_context`; semantic v8 remains separate | Most owner outputs are now transported. Python still validates/project features; no planner output may be treated as an action. |
| Positioning (#575) | `BoardEvaluation`, `PositioningEngine`, board roles and unit profiles | Aggregate scores/counts on `AuditPlayerSnapshot`; board slots and unit profiles | Aggregate diagnostics exist, but no explicit per-entity position/neighbor/protection/exposure/relation rows are transported. Do not infer tactical metrics that the native evaluator does not expose. |
| Action masks (#576) | Native `ActionMaskEngine` / `PlayerActionMasks` | Packed 1,280-wide boolean mask plus compatibility mapping | Masks already originate in C++ and must be byte-for-byte/shape-identical. Candidate semantics and source/destination association need a typed, versioned view, not a second legality implementation. |
| Executed action (#576) | `TFTEngine::step`, `PlayerEnv::step`, `ActionExecutionTrace` | requested/effective action, handler_applied, status_reason; Python wrapper | Engine already knows normalized/applied action, but factual outcome events are reconstructed in Python by diffing pre/post native snapshots in `build_action_outcome_events`. |
| Temporal facts (#577) | Engine/episode/round/player sequence counters; player action counters and board move age; combat/economy/PvP event producers | Native audit snapshot and decision identity envelopes | Basic temporal identity and selected counters exist. A bounded, causal event/history contract is not yet explicit. Existing latest-event collections are not a substitute for a cross-decision history. |
| PPO integration (#578) | Python wrapper, semantic projection/batch, trainer and rollout | semantic v8 numeric tensor + champion IDs/hash; structured strategic context in snapshot metadata | Current semantic v8 input is the compatibility baseline. The rich Decision Context needs a separate envelope and consumer map; do not silently change tensor dimensions or checkpoint lineage. |

## Important implementation observations

### #574 — strategic context

The native v4 strategic owner contract already contains composition identity/version, direction and pivot anchors, priorities, pair/upgrade evidence, lineup membership and opportunity-cost provenance. It is bound to player/episode/round/decision sequence and has a separate strategic context sequence. Keep the v8 tensor/hash contract unchanged while exposing the complete structured context. Unavailable owner output must remain unavailable, not become a measured zero.

### #575 — positioning

`AuditPlayerSnapshot` currently exposes aggregate board scores and counts. `AuditUnitSnapshot` exposes role and combat attributes, while the board array gives slot identity. The missing layer is a compact per-entity/per-board-slot relation projection with explicit provenance and geometry version. The implementation must reuse the existing 4x7 geometry and evaluator semantics; it must not introduce a second tactical evaluator or alter placement/movement rules. Bench entities should be represented as bench facts, not assigned invented board coordinates.

### #576 — Action Context and factual events

The Engine already validates the whole action batch before executing it, validates against current masks, and records requested/effective action plus handler result. The versioned native execution event now also carries transition availability, board-capacity outcome, native gold/interest/level/XP/cost/proceeds facts, before/after shop-offer revisions, and native item-action result metadata, bound to source/outcome snapshot and per-player sequences. Python then calls `build_action_outcome_events(before_snapshot, after_snapshot, action_traces)`, which rebuilds unit/copy/shop/item/economy deltas. The target is to emit a compact native factual event at the execution boundary, retaining the Python diff producer as a temporary oracle in parity tests. The event must distinguish requested, normalized/effective and actually applied action; identify the player decision and source snapshot; and represent unavailable deltas explicitly. Rewards remain independently produced and must not be copied into factual event labels.

### #577 — temporal and delayed consequences

Native identity already has engine instance, episode, snapshot sequence and per-player decision sequence. Round/stage, combat sequence, economy resolution and PvP credit events are also available. Player state has `actions_taken_this_round` and `board_move_age`. Missing is a bounded per-player event history with explicit causal references from later outcomes to originating decisions. History must be isolated by engine instance, episode and player; reset/auto-reset must clear it; retention must be bounded by a documented policy. Do not manufacture timestamps or future predictions where the Engine has no factual producer.

### #578 — Decision Context adapter and PPO

The adapter should create one lobby envelope containing shared snapshot identity and shared-pool/catalog facts, plus eight player views keyed by stable player identity and sequence. It should forward structured entity, strategy, positioning, action and temporal blocks without reconstructing semantics or duplicating lobby-wide data eight times. The existing semantic v8 projection remains the compatibility path and oracle. PPO tensors, action masks, rewards, dones, GAE, rollout transitions and checkpoints remain unchanged in this migration. Any new neural encoder/input dimension is a separate versioned experiment.

## Coordinated implementation order

1. Stabilize a common envelope and sequence/identity validation across snapshot, strategic, positioning, action and temporal blocks.
2. Add compact positioning rows from existing native facts/evaluator outputs; preserve aggregate legacy fields.
3. Add native factual action outcome events at the action boundary and compare them against the existing Python diff oracle.
4. Add bounded causal history keyed by engine/episode/player/decision identity, including existing combat/economy events where their provenance supports attribution.
5. Build the lobby-level and player-level Decision Context adapter; map every field to audit-only, semantic compatibility, or future policy consumers.
6. Run all native/Python contract, reset, auto-reset, multi-lobby, parity and checkpoint-compatibility tests.
7. Benchmark the complete path with PPO active. Compare the integrated result with #573-1 and the immediately preceding profile using the same workload. Investigate any material regression before considering acceptance.

## Performance hypotheses to measure

- Avoid reserializing/revalidating the same lobby-wide data once per player.
- Avoid materializing full Python dictionaries for native blocks that can be exposed as owner-backed read-only views with a lifetime tied to the native result.
- Avoid rebuilding entity maps, UUID sets, item counts and generic snapshot diffs in the hot path when the native producer can emit compact deltas.
- Avoid repeated board scans by sharing a single immutable per-snapshot board projection among board evaluation, relation projection and semantic compatibility where the contracts permit it.
- Avoid full-snapshot copies for temporal history; retain compact events/deltas and stable references.
- Do not introduce caches without complete identity/version keys and explicit lifetime/invalidation rules.

These are hypotheses, not claimed wins. The benchmark decides.

## Required validation and acceptance gates

- Exact parity for existing semantic v8 numeric values, champion IDs, hash, action masks, rewards, dones, rollout identities and checkpoint lineage.
- Native/Python event parity across all action families, including overridden, rejected/not-applied, no-op, item/anvil, round resolution, elimination and reset cases.
- Positioning coverage for empty/partial/full boards, swaps/moves, invalid/absent entities and board/bench identity.
- Temporal coverage for multiple actions, round/stage transition, combat/economy delayed outcomes, elimination, independent episodes, auto-reset and multiple lobbies; no cross-player/lobby/episode attribution.
- Audit snapshots and replay remain complete.
- End-to-end PPO-active benchmark includes native binding, adapter, batching, rollout, GAE and optimizer; do not rely on microbenchmarks or hide work in binding/C++.
- No issue is closed and no performance gate is declared passed until evidence exists.


## Implementation progress on the integrated PR

The following pieces have now been added to this branch; they are implementation increments, not completion claims for the five issues:

- **#575 partial:** native `board_relations` rows expose occupied slot, 4x7 row/column, role, adjacent occupied slots, frontline slots in front, and tank/fighter counts. Physical UUID remains owned once by the corresponding `AuditUnitSnapshot` board slot; relation rows reference that stable slot. Fixed-size neighbor arrays avoid per-relation heap allocations. The projection uses the existing board geometry and raw role facts; it does not create a second board evaluator. Neighbor storage is fixed-size and the projection avoids temporary neighbor vectors.
- **#576 partial:** `ActionExecutionTrace` is now a versioned `tft.action-execution-event` v1 with static producer/source metadata and source/outcome snapshot plus per-player sequence, round and stage. The Python oracle checks that this causal envelope matches the paired snapshots. Native economic transition facts and pre-action shop revisions are checked against the paired snapshots; post-action shop parity is checked when no round auto-refresh overlaps. Native item-action metadata and unit add/remove/move/upgrade deltas are emitted at the execution boundary. The Python snapshot-diff producer remains an oracle and rejects any native unit-delta mismatch; its richer legacy facts remain available during migration.
- **#578 partial:** the trainer now creates one shared lobby context reused by its eight player rows, plus a player view referencing the frozen native player subtree. Strategic and positioning blocks are exposed as direct views; temporal counters and shared economy/PvP facts are carried separately. Native action execution is attached only to the matching outcome row. The existing semantic v8 tensor remains unchanged.
- **#577 partial:** current action traces are explicitly linked to their source/outcome decision identities; existing round counters, board-move ages, combat sequence and economy/PvP events are preserved in the context. A bounded cross-decision history that links delayed combat outcomes to originating decisions is still outstanding; current action traces identify the source/outcome boundary but do not claim an unproven one-action cause for later combat results. No artificial retention window or causal attribution is being invented.
- **#574:** the existing strategic-owner v4 implementation remains intact and is consumed by the new player context.

### Remaining before the integrated performance gate

1. Extend native Action Context beyond execution identity: emit action-family-specific factual deltas at the execution boundary, and keep the current Python diff producer as a parity oracle until all families match.
2. Complete the positioning field/consumer matrix and validate relation rows against existing board evaluator outputs without changing evaluator behavior.
3. Define and implement delayed-outcome causal references only where native producer evidence can establish them; specify bounded retention and reset/auto-reset semantics before adding history storage.
4. Complete field-to-consumer routing for trainer, rollout, masks, rewards and audit. Keep the current Policy/checkpoint interface as compatibility mode.
5. Run CI, inspect failures, then run the PPO-active integrated benchmark. The baseline comparison remains #573-1; no gain is claimed until measured.
