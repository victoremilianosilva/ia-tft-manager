# Reward Action Outcome Producers v1

**Status:** factual telemetry contract; not a reward-shaping approval.  
**Tracking:** #287, coordinated with #295.  
**Owner:** Python boundary producer over paired authoritative native Engine snapshots.

## Problem

Reward v1 intentionally keeps action reward neutral. That avoids promoting Shadow scores, composition fit, handler success, or heuristic board metrics into PPO targets. The remaining gap is that the Engine publishes rich state snapshots, but the Python transition did not bind the action that consumed the previous snapshot to factual changes in the next snapshot. As a result, purchase, upgrade, XP, reroll, sale, economy, and positioning consequences were not represented by one machine-checkable, decision-correlated event.

## Technical rationale

The producer must compare the exact native snapshot used for action selection with the next native snapshot returned by the Engine. It must preserve separate source-decision and outcome-snapshot identities, and it must mark ambiguous deltas unavailable rather than guessing. It must not use Shadow scores, candidate rankings, strategy labels, composition fit, or evaluator resolutions as outcomes.

## New responsibility

reward_outcome_producers.build_action_outcome_events emits one factual event per player decision from the paired native snapshots and native action execution trace. CppTFTLobbyWrapper.step retains the consumed pre-action snapshot locally, clears its public cache before invoking the Engine, and binds the resulting event to the post-step snapshot. A failed Engine step therefore cannot reuse stale state.

## Event contract

Each event includes:
- contract ID/version and explicit producer/source;
- Engine instance, episode, player, source decision sequence, and outcome snapshot sequence;
- the effective native action, handler application status, and machine-readable status reason;
- action family and facts available from the paired snapshots.

The current factual fields are:

| Family | Facts emitted | Important boundary |
|---|---|---|
| Purchase | Selected shop offer, newly owned physical unit UUIDs, owned copy-equivalent delta | No value is assigned to a purchase merely because it was accepted |
| Upgrade | Physical UUID changes, per-champion star-tier count deltas, and copy-equivalent changes | Physical tier change is evidence, not a calibrated utility score |
| XP | XP and level deltas, gold/interest changes | XP/gold deltas are unavailable when round-income resolution overlaps the action |
| Reroll | Per-slot offer revision and before/after offer identities | A changed shop is not automatically a successful or valuable reroll |
| Sale | Removed physical unit UUIDs and copy-equivalent delta | Proceeds are not inferred from a mixed action-plus-income gold delta |
| Economy | Before/after gold and interest-if-resolved-now, realized EconomyEngine resolution events, plus overlap marker | Native EconomyEngine::resolve_round events remain a separate income source |
| Positioning | Same-unit physical slot transitions plus total, positional, structural, exposed-carry, frontline, and unplayed-bench diagnostics | Scores are diagnostics only; no score delta becomes reward |

An event's causal_attribution is always not_established, reward is always null, and reward_eligible is always false under this telemetry contract. The producer never changes the scalar reward consumed by PPO.

## Invariants

1. Before/after snapshots must belong to the same Engine instance and episode.
2. The outcome snapshot and every player decision sequence must advance beyond the source decision.
3. Exactly eight player records and eight action traces are required; player IDs must match their array positions.
4. Owned-unit identity is UUID-based and scoped to the player snapshot. Occupied units without UUID/champion identity fail closed.
5. Shop revision arrays must contain exactly five native revisions.
6. When EconomyEngine::resolve_round overlaps the action, action-attributable gold and XP deltas are null; they are not reconstructed from the combined balance.
7. A positioning/deploy change is identified by the same unit UUID changing physical location or slot. Board-quality and positioning-score deltas remain descriptive diagnostics.
8. No event contains a reward coefficient, reward label, Shadow score, or evaluator score.

## Impact

The wrapper now exposes info["action_outcome_events"]. PPO reward, reward contract hash, GAE, action masks, Engine rules, and checkpoint semantics remain unchanged. This is an event-provenance foundation for later causal evaluation, not the completion of #287.

## Validation

Unit tests cover purchase/copy progress, reroll offer revisions, XP progress, sale identity, physical board movement, economy-resolution overlap, and snapshot/player-sequence mismatch. Wrapper integration tests exercise the event producer at the same boundary as the reward ledger.

## Calibration and ablation gate

No action-family signal is enabled as reward by this contract. Before a later Reward Contract version may use any event, #295 must provide:
- immutable train/validation/test episode and seed manifests;
- deterministic replay that binds observation, masks, action, event, combat and terminal placement to the same decision identity;
- a pre-registered hypothesis, outcome metric, horizon, attribution rule, non-overlap rule, normalization and reward-hacking checks for each family;
- paired baseline/candidate evaluation with seat rotation and uncertainty intervals;
- leave-one-family-out and combined ablations for purchase/upgrade, XP, reroll, sale, economy and positioning;
- raw per-episode artifacts and reproducible report hashes.

The current repository audit still identifies the integrated deterministic replay and rollout identity chain as incomplete. Therefore no empirical calibration result is claimed here, and no coefficient or reward shaping is introduced until that gate is satisfied.
