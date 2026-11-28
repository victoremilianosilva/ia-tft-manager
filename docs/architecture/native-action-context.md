# Native ActionContext v1

The action boundary is published by the C++ Engine as part of the same
`NativeDecisionBatch` decision snapshot.

## Contracts

- `tft.engine.action-context` version 1 identifies the per-step action context.
- `tft.action-masks.packed` version 1 defines the canonical boolean mask layout.
- The packed mask buffer is contiguous with shape `[lobbies, 8, 1280]` and is
  exposed read-only by `NativeDecisionBatch.action_masks`.
- Layout order is: type, shop, bench source, board target, board source,
  board move target, bench move source, bench-to-board target, item inventory,
  item component first, item component pair, item target.
- `tft.engine.action-outcome-event` version 1 is emitted by the native step
  boundary for each player, carrying engine/episode/player identity,
  source/outcome decision sequences, requested/normalized/effective action,
  preflight mask permission, handler result/reason, candidate and actually
  affected physical unit UUIDs, catalog references, auto-merge facts and
  action-economy/XP/level deltas.
- Item actions additionally publish the native item handler kind, item ID and
  component IDs. Champion IDs remain catalog references, never copy identity.

## Authority and semantics

The Engine remains the only authority for legal masks. Eliminated players
receive a PASS-only mask from `refresh_masks`; the Trainer validates masks
and does not query player liveness or synthesize PASS.

PPO remains responsible for logits, sampling and selecting the action.
Action events are factual audit data and are not reward shaping, labels or
PPO targets. Delayed combat and terminal-placement rewards remain governed
by the reward contract.

The old Python snapshot-diff producer remains available as a test oracle only.
A directed end-to-end test compares its family, action type, handler result and
status against the native event. The production adapter consumes the native
event payload and fails closed if it is absent or its identity/sequence does
not match the published decision. RewardAudit validates and deduplicates the
native event ID; Rollout validates its action/identity parity and retains the
event beside the exact transition metadata.

## Boundaries

A malformed batch or action rejected by native preflight still raises before
any player action is executed. The wrapper attaches the eight native preflight
reports to the exception's `action_context`; rejected reports carry
`mask_permitted=false`, `decision_advanced=false`, a stable rejection code and
a diagnostic detail. They are never recorded as completed rollout transitions.
The event's `handler_applied` and `status_reason` describe handler execution,
not causal reward eligibility. Candidate references describe the entities
addressed by the selected action; affected references are emitted by the
handler only when an effect actually occurred. Champion IDs are catalog
references and are never used as copy IDs.
