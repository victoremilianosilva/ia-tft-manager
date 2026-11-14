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


## Current architecture reconciliation (2026-11-14)

The safety-boundary statements above describe the **audited runtime at the time
this document was written**: Composition Intelligence recommendations and
diagnostics are not currently projected into PPO observations. They must not
be read as a permanent prohibition against the canonical Shadow architecture
supplying strategic **context/evidence** to a future PPO observation contract.

The approved target keeps these concepts separate:

- A future PPO observation may consume versioned, provenance-bearing facts and
  canonical state/evidence published by the approved owners (StrategicPlanner
  direction commitment, accepted active composition, EconomicController
  posture/progression, and validated unit/lineup evidence), once the dedicated
  observation migration contract and implementation are approved.
- Shadow recommendations, candidate rankings, evaluator scores, confidence
  proxies, UnifiedStrategicStateMachine state, and executor resolutions are
  not PPO labels, imitation targets, reward targets, or substitutes for PPO
  action selection.
- UnifiedStrategicStateMachine / UnifiedStrategicShadowRuntime remains
  diagnostic-only and cannot publish its parallel state into canonical owners
  or PPO.
- Engine rules and native action masks remain final legality authority.
  Shadow remains read-only; no live action execution is authorized.

This reconciliation resolves the ambiguity in the older phrase “not fed into
PPO observations”: it records current implementation isolation, not the
approved future boundary for canonical context. It does not claim that such
projection exists today.

**Prior limitation:** this document described the existing runtime boundary
without distinguishing canonical strategic evidence from recommendations.
**Reason for clarification:** the approved Observation Schema and ownership
contracts require contextual inputs while explicitly prohibiting imitation
coupling.
**Ownership/contract:** source owners retain their approved authority; the PPO
observation projection is a separate versioned consumer and cannot mutate
source state.
**Cross-component impact:** #286/#293, #288, #294 and the ownership contract
must remain aligned; no change is made to current runtime behavior.
**Validation:** documentary consistency only now. Producer/consumer lineage,
provenance, identity/sequence, missingness and no-imitation tests are
executable acceptance after Gate 8 and explicit authorization.
