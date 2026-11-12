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

## Current integration boundary

The Viewer audit generator always writes `audit_direcao_pivot.md`. If the session sidecar is absent, the report explicitly marks the producer data as unavailable. This avoids fabricating state from legacy logs. The current unified state machine remains shadow/read-only; wiring a live event producer is a separate integration step and must preserve PPO, training, observations, masks, rewards, checkpoints, rules, Viewer behavior and action execution.
