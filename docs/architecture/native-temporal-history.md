# Native temporal history — contract v1

## Ownership and purpose

`TFTEngine::Impl` owns one bounded temporal stream per Engine instance and episode. It is separate from `AuditSnapshot`: snapshots remain point-in-time audit projections, while the temporal stream contains incremental facts emitted by their native producers. The stream is not a reward source, PPO target, prediction, or substitute for action masks.

The public contract is `tft.engine.temporal-history` v1. Individual records use `tft.engine.temporal-event` v1.

## Event envelope

Every event carries Engine/episode identity, a strictly increasing Engine-global sequence, an event ID, event type, scope, round/stage, producer, and optional player/unit/resource data. Player-scoped events also carry the player decision sequence. A delayed consequence may refer to the originating action event through `causal_event_id`, with separate source and observed player-decision sequences.

Current producers:
- `action_outcome`: the exact native `ActionOutcomeEvent` emitted by the action handler. Its event ID is reused, not reconstructed.
- `combat_damage` and `combat_death`: facts emitted by CombatEngine; health deltas are negative damage, not predicted damage.
- `economy_resolution` and `level_transition`: EconomyEngine resolution facts.
- `pvp_result_credit`: EconomyEngine credit fact.
- `player_elimination`: the transition to eliminated state.
- `round_transition`: lobby-scoped round boundary.

A consequence points to the latest same-round action event for the affected player where such a producer-owned relation exists. This is an explicit attribution anchor, not a claim that one action alone caused a multi-unit combat outcome. Events without a defensible source retain an empty causal reference. No damage/pressure forecasts or inferred future outcomes are emitted.

## Ordering, retention, and lifecycle

The stream is ordered by `global_sequence`; player sequence is inherited from the owning Engine's player decision counter. Records are retained up to 256 events and an eight-round window. Expiration/eviction sets `temporal_history_complete=false`; absence after eviction must not be interpreted as proof that an event never occurred.

A new episode clears the stream, sequence, causal anchors, and truncation flag. Elimination emits a factual event but does not erase the episode's audit trail. Lobby shutdown destroys the owning Engine and therefore its history. A new round emits a boundary event; the configured round window governs expiration.

`StepResult.temporal_events` contains only events newly emitted by that step. `AuditSnapshot.temporal_events` is the bounded retained window. This avoids copying the complete history through every vector-environment step.

## Anti-loop auxiliary history

Each player snapshot exposes a typed, bounded `anti_loop_history` projection: position signature hashes, ordered move records, blocked move records, and state visit counts/rounds. UUIDs are included only when the anti-loop identity contains a physical UUID. These records are diagnostics/context only and never alter or replace authoritative action masks.

## Temporal slot semantics

`board_move_age` remains indexed by board slot. A move resets the destination slot's age and expires the source slot; the age is not transferred as a property of a physical unit. UUID attribution is supplied separately by the current board projection and move/action events.

## Rollout ownership

Trainer attaches only player-owned events to each player row; the lobby boundary event is assigned once to player 0 to avoid eightfold duplication. Rollout validates event contract, identity, ordering, owner isolation, action-event linkage, and causal sequence ordering. The incremental event records are stored once in a compact sidecar, not repeated inside decision/result/next snapshot metadata. The result and next observation retain distinct identity, including terminal result versus post-auto-reset observation.

The numeric PPO tensors, GAE, action masks, rewards, and checkpoint formats are unchanged by this audit/context stream.
