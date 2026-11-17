# Strategic direction/pivot audit event contract

The offline Viewer audit consumes an optional session sidecar:

`strategic_direction_pivot.jsonl`

Each line is one immutable observation emitted by the shadow strategic-cycle producer. The audit never calls the planner, reconstructs a pivot from PPO actions, or edits the source event stream.

## Required envelope

- `schema_version`: integer, initially `1`.
- `sequence`: monotonically increasing sequence within the session/player stream.
- `player_id`, `round`, `phase`: event owner, round and unified state-machine phase.

## State and evidence

- `active_composition`: `{identity, version}`.
- `direction_anchor`: `{identity, composition_identity, composition_version, lifecycle, unit_ids}`.
- `pivot_candidate`: null or `{identity, target_composition_identity, source_direction_anchor_identity, source_composition_version}`.
- `unit_support`: array of unit evidence with `champion_id`, `relation` (core, trait completion, composition, temporary support), `copies_owned`, `highest_star`, `target_star`, and optional intent/reasons.
- `shop_evidence`: array of observed offers with champion ID, cost, copies and source sequence.
- `carry_gate`: eligibility plus champion ID, cost, star and explicit reason. Eligibility must reflect the rule carry 2-star OR carry cost 4/5; cost 4/5 alone is not pivot approval.
- `feasibility`: status, reason, blockers and missing data.
- `transition`: populated only for confirmed transitions, with source/destination identities and previous/new versions.

## Audit semantics

- `PIVOT_EVALUATION` must preserve active composition/direction and validate candidate source anchor/version.
- `PIVOT_CONFIRMED` must synchronize active composition and direction anchor to the same identity/version and clear the pending pivot.
- `NO_EVIDENCE` is distinct from rejection; missing shop/pool/ownership fields remain unavailable.
- `INVALIDATED` must not mutate the active composition.
- Repeated action snapshots are not counted as independent strategic reviews.
- Conflicts are evidence for investigation, not automatic proof of a strategic mistake.
- PPO actions/rewards are contextual only and never treated as strategic ground truth.

## Runtime integration

The live producer is connected in `cpp/src/lobby/TftEngine.cpp`, inside the existing per-player `update_strategy()` Shadow block and its `run_shadow_isolated` failure boundary. For each player, the engine adapts the normalized state already assembled for Composition Intelligence: active composition/version, owned board and bench units, shop offers, catalog traits, gold, and observed source candidates.

**Runtime scope:** this producer is the native `TFTEngine`/Viewer simulation session in this repository. It does not yet consume Overwolf GEP snapshots from an external live TFT client; that separate GEP-to-IA-ready-snapshot integration remains outside this PR.

The Viewer configures the sidecar after creating the match session directory. The native engine writes directly to:

`<session_dir>/strategic_direction_pivot.jsonl`

The path is exposed through `TFTEngine::set_strategic_direction_pivot_audit_path` and the Python lobby wrapper. The session metadata declares the sidecar and schema. Each player owns an independent `UnifiedStrategicShadowRuntime`; records share the session JSONL file but have player-local sequence numbers and state. A new match resets the machine and recorder state.

The producer deduplicates unchanged logical snapshots per player. Changes in observed gold, units, shop evidence, composition identity/version, pivot evidence, phase, or round remain recordable. Recorder I/O and serialization failures are contained and do not interrupt the existing snapshot producer.

## Evidence and remaining limits

The runtime uses only normalized values available in the engine. It does not reconstruct evidence from PPO actions, rewards, or legacy action logs. Missing values remain explicit.

The current live snapshot does not yet provide a configured protected-gold reserve floor or a complete transition opportunity-cost estimate. Those fields are deliberately left unavailable in `PivotFeasibilityInput`; therefore a pivot that depends on those missing economic inputs remains `INSUFFICIENT_EVIDENCE` and cannot be confirmed by fabricated defaults. This integration proves real event production and current-state direction synchronization, not full economic approval of pivots.

The producer tracks the last externally published Composition Intelligence identity/version separately from the unified machine state. It re-anchors only when that external snapshot itself advances; it does not reset the unified machine merely because a Shadow-confirmed pivot differs from the external source. After a Shadow pivot confirmation, subsequent evaluations use the unified machine's new internal composition/direction, without publishing that recommendation back to Composition Intelligence, PPO, or the executor. A later external identity/version change is treated as a new observed source snapshot and re-anchored explicitly.

The Viewer audit generator always writes `audit_direcao_pivot.md`. If the session sidecar is absent, the report explicitly marks producer data as unavailable. No autonomous action or PPO path is connected.


## Current architecture reconciliation (2026-11-14)

This audit describes the current isolated Unified direction/pivot observer.
Its statement that the observer does not publish recommendations to PPO
remains normative: the Unified diagnostic state and its pivot decisions are
not canonical PPO context, labels, rewards, or action authority.

That boundary does **not** prohibit a future PPO observation from consuming
validated facts and committed state from the approved canonical owners through
the separately versioned observation projection (#286/#293). In particular,
the future projection must not read the Unified machine's private parallel
state or infer canonical composition/direction from its diagnostic pivot.
The canonical StrategicPlanner commitment and CI active composition remain
separate owners, correlated through approved transition records. Engine rules
and masks remain final legality authority; Shadow remains read-only.

The Overwolf/GEP statement above is also a runtime-scope fact for this audit:
the producer described here consumes the normalized native engine snapshot
available in this repository. It does not establish that the separate
Overwolf live-snapshot adapter is already integrated, nor does it authorize
that integration.

**Prior limitation:** the original audit did not explicitly distinguish the
Unified diagnostic stream from canonical strategic evidence intended for a
future PPO projection, and its native-snapshot scope could be mistaken for
proof of Overwolf integration.
**Reason for clarification:** preserve the isolation of diagnostic hypotheses
while allowing the approved architecture to expose validated canonical
context, and prevent false claims about the live GEP path.
**Ownership/contract:** Unified Shadow owns only its diagnostic namespace;
StrategicPlanner and ActiveCompositionManager/TransitionManager own canonical
direction and active composition; the observation adapter is read-only.
**Cross-component impact:** #284/#286/#289/#293, the ownership and replay
contracts, and the separate Overwolf integration boundary.
**Validation:** documentary consistency now. Post-Gate-8 acceptance must
prove namespace isolation, canonical-source projection, identity/sequence
correlation, stale rejection, and explicit end-to-end GEP snapshot provenance
before claiming OW live integration.
