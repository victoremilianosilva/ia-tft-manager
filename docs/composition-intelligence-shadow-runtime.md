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
entry carries its stage sequence and the active composition identity/version
at that point; the active composition may change between stages. The enclosing
snapshot owns match/episode, player, round, timestamp, player-local sequence
and lobby-wide ordering sequence.

## Frequency and duplicate policy

The pipeline is evaluated at the player's update boundary, after the live state
for that update is available. This preserves action-level changes to board,
bench, shop, economy, and items. Before persistence, snapshots are compared
using a canonical representation that excludes the lobby-wide sequence,
player-local sequence and top-level wall-clock timestamp. Context Bridge is a
nested semantic projection and no longer carries a second identity, timestamp
or sequence envelope. Identical logical snapshots are not appended. A changed diagnostic or stage
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


## Envelope consolidation — PR #484

**Prior problem:** runtime_execution and each stage repeated match/player/
round already present on the parent snapshot. Context Bridge metadata also
repeated match/player/round, timestamp, sequence and active composition
identity, even though Context Bridge is serialized only inside this runtime
snapshot.

**Technical rationale:** Context Bridge validates expected player/round while
adapting strategic values; it is not an independent transport. The runtime
snapshot is the common transport envelope. Stage-local composition identity
is retained because a transition may change the active composition during a
single evaluation cycle.

**New responsibility:** CompositionDiagnosticSnapshot owns match/player/
round/composition identity. CompositionIntelligencePlayerRuntime adds the
player-local sequence and timestamp at the outer snapshot. Context Bridge
metadata owns schema/quality/reason and each value retains its own
observed/derived/recommended origin, quality and source. Stage records own
stage_sequence and stage-specific composition identity/version only.

**Contract/invariants:** diagnostic snapshot schema v2 and Context Bridge
metadata schema v2. Nested Context Bridge and runtime stage records do not
repeat the parent identity envelope. The duplicate-snapshot fingerprint
ignores timestamp and sequence fields but retains semantic stage outcomes and
stage-specific composition identity.

**Cross-component impact:** CompositionIntelligenceRuntime,
CompositionDiagnosticRecorder, StrategicContextBridge and TftEngine producer
are updated together. UnifiedStrategicShadowRuntime still receives its
independent evaluation sequence; that sequence is sourced from the runtime
before append and is not stored in ContextBridgeInput.

**Validation:** native build and strategic architecture regression checks
validate the updated DTOs, producers and consumers. Diagnostic schema changes
are isolated from PPO, rewards, masks, action execution and Engine legality.


## Core-trait provenance boundary (Stage 1 PR 2)

Composition Intelligence derives unit synergy and item affinity from the
native `StrategicSharedContext::current_core_traits` built from the current
per-player native strategic commitment and Native candidate generation.

The runtime must not read `StrategyInfo::core_traits` for either:
- `UnitPriorityEvidence::synergy_contribution`;
- `ItemUnitBinding::profile.preferred_traits`.

Those legacy fields may remain available to the old PPO/Viewer compatibility
path, but they are not inputs to Composition Intelligence. When the native
strategic context has no core traits, the value remains an empty/unknown
evidence set; it is not filled from legacy fields.

The architecture regression check extracts the Composition Intelligence
pipeline from `TftEngine.cpp` and rejects any `info.core_traits` reference
inside that boundary while requiring the native strategic-context source.

This change does not migrate the PPO anvil observation helper
`item_unit_profiles()`, which remains part of the legacy PPO projection and
must move only with the approved observation contract (#286). It also does not
change reward shaping (#287) or Viewer compatibility (#292).

## Six-point architecture review

1. **Prior problem:** Composition Intelligence calculated owned-unit synergy and item preferred traits from legacy `StrategyInfo::core_traits`, despite its new native strategic evidence context.
2. **Technical rationale:** the same update already constructs `StrategicSharedContext::current_core_traits` from the per-player native commitment and Native candidate generation. The legacy field is not needed for this runtime.
3. **New responsibility:** native strategic context owns the trait evidence consumed by Composition Intelligence; `StrategyInfo` remains only for legacy consumers.
4. **Contracts/invariants:** no fallback from missing native traits to legacy traits; preserve missingness and provenance; recommendations remain Shadow-only.
5. **Cross-component impact:** `TftEngine.cpp`, the strategic architecture regression test and this runtime contract. PPO observation, reward, Viewer UI and Engine legality are unchanged.
6. **Objective validation:** source-level architecture guard proves the Composition Intelligence block contains no legacy core-trait reads and uses the native strategic context instead.

## Native semantic unit/item projection and legacy isolation — PR #495

**Prior problem:** the item-unit profile used by PPO item features and item-action validation was assembled from legacy StrategyInfo fields (core/planned traits, direction, focus weights and legacy composition scoring). The shared combat classifier also accepted planned_main_carry, allowing a legacy planning label to promote an otherwise ambiguous ranged unit into a carry. The existing Python boundary guard proved only that the Shadow block did not directly read legacy fields; it did not exercise the native active-composition/item-evidence path at runtime.

**Technical rationale:** item affinity and combat role should derive from observable champion/item facts and the canonical active composition, not from a parallel legacy strategy projection. The active composition owner identifies core units; their catalog traits provide the preferred-trait set. Combat classification should use base role, attack range, stats, ability semantics and equipped item stats. A planned carry label is a strategic recommendation, not a combat fact.

**New responsibility:** semantic_item_unit_profiles builds one shared ItemEngine profile from champion definitions, observed unit stats/items, and the core-unit traits of CompositionIntelligencePlayerRuntime::active. The same profile path is used by item observation scoring and item-action validation. UnitCombatClassifier no longer accepts or consumes a planned-main-carry override. Composition Intelligence continues to derive core/synergy evidence from native generation and active board traits.

**Contract/invariants:** no StrategyInfo, legacy direction/focus, planned carry, or legacy item-profile projection may feed the semantic item-profile builder. Without an active composition, preferred traits are empty and item fit falls back to observed role/stats/effects; no legacy fallback is permitted. ItemEngine remains the only item-fit implementation. Classification never treats a planned carry as observed role evidence. This path remains read-only and does not execute item or board actions.

**Cross-component impact:** TftEngine item-profile construction, PPO item-option feature derivation, ItemEngine action validation, UnitCombatClassifier, PlannerEvidenceAdapters, and Composition Intelligence runtime tests. Observation dimensions/order and PPO training/reward contracts are unchanged.

**Validation:** a runtime Composition Intelligence test publishes a native active composition, derives preferred traits from its core unit, measures ItemEngine inventory fit, and completes an initial Shadow publication without constructing legacy strategy state. A static boundary guard asserts that the semantic profile builder reads the active composition and catalog traits but contains no legacy strategy fields. Classifier regressions prove an ambiguous ranged unit remains flexible without factual combat evidence, even when the former planned-carry signal would have promoted it.
