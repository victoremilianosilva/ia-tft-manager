# Composition Intelligence Shadow Runtime

## Entry point and ownership

The runtime is entered from the per-player strategic evaluation block in
`cpp/src/lobby/TftEngine.cpp`, gated by
`TFT_COMPOSITION_INTELLIGENCE_SHADOW=1`.

Each lobby player owns one `CompositionIntelligencePlayerRuntime` instance in
the fixed-size `composition_intelligence_players` array. The instance owns
that player's active composition, transition hysteresis, diagnostic recorder,
snapshot history, player-local sequence, and duplicate-snapshot fingerprint.
The OP.GG catalog is immutable/shared input; Native candidates and diagnostics
are stored per player before being combined for that player's evaluation.

## Evaluation order

For each player update, the Shadow block executes the following order:

1. Collect validated Native and OP.GG candidates.
2. Build the current board/economy evidence used to score candidates.
3. Evaluate the candidate set and transition hysteresis.
4. Publish only an approved transition through `ActiveCompositionManager`.
5. Resolve unit priorities against the published composition identity/version.
6. Build a lineup against the same identity/version.
7. Attach economy, board, and item evidence to that version.
8. Evaluate eligible action candidates in Shadow mode.
9. Assemble the diagnostic snapshot and per-stage execution trace.
10. Feed the same normalized per-player state to `UnifiedStrategicShadowRuntime` and append direction/pivot events to the session sidecar when the Viewer has configured its path.
11. Append the Composition Intelligence diagnostic snapshot to the per-player history.

A stage can be marked completed, skipped, unavailable, or failed. Each trace
entry carries match/episode, player, round, stage sequence, and the active
composition identity/version at that point. The enclosing snapshot carries the
same player/match/round identity and a player-local sequence in addition to the
lobby-wide ordering sequence.

## Frequency and duplicate policy

The pipeline is evaluated at the player's update boundary, after the live state
for that update is available. This preserves action-level changes to board,
bench, shop, economy, and items. Before persistence, snapshots are compared
using a canonical representation that excludes only the lobby-wide sequence,
player-local sequence, and context-bridge wall-clock timestamp/sequence.
Identical logical snapshots are not appended. A changed diagnostic or stage
outcome is retained.

This policy deduplicates persisted records; it does not claim to skip all
upstream planner computation. The per-player runtime retains its last logical
snapshot fingerprint so a later change is not suppressed.

## Lifecycle and isolation

A new match/episode resets the entire per-player runtime array, Native
candidate buffers, diagnostics, and lobby-wide sequence. No active composition,
hysteresis streak, recorder sequence, snapshot history, or duplicate fingerprint
is shared between players. Unit/lineup/action planners also validate the active
composition ID and version before consuming derived snapshots; a pivot or
refinement therefore makes outputs from the previous version stale.

## Safety boundary

The runtime is opt-in, read-only, and Shadow-only. Its recommendations are
diagnostics and are not fed into PPO observations, action masks, legal actions,
rewards, training, checkpoints, rules, or the executor.


## Unified direction/pivot sidecar

When the Viewer creates a recorded session, it configures
`strategic_direction_pivot.jsonl` on the native engine. The same per-player
update boundary that produces Composition Intelligence snapshots feeds the
unified direction/pivot runtime. This is a read-only observer: it does not
publish recommendations back into the active-composition manager, PPO, masks,
rewards, or executor.

Unchanged logical events are deduplicated by the recorder. The unified machine
is re-anchored if the observed active composition identity/version changes.
Pivot feasibility preserves missing reserve-floor and full transition-cost
inputs as unavailable; it must not approve a pivot from assumed economic data.
See [Strategic direction/pivot audit](strategic-direction-pivot-audit.md) for
the event contract and current integration limits.
