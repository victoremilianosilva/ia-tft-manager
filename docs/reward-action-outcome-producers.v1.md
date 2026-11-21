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
| Reroll | Per-slot offer revision and before/after offer identities | If round resolution also refreshes the shop, the revision delta is retained only as unattributed evidence; it is not assigned to the reroll |
| Sale | Removed physical unit UUIDs and copy-equivalent delta | Proceeds are not inferred from a mixed action-plus-income gold delta |
| Economy | Before/after gold and interest-if-resolved-now, realized EconomyEngine income and PvP gold-credit events, plus overlap markers | Native EconomyEngine::resolve_round events remain a separate income source |
| Positioning | Same-unit physical slot transitions plus total, positional, structural, exposed-carry, frontline, and unplayed-bench diagnostics | Scores are diagnostics only; no score delta becomes reward |

An event's causal_attribution is always not_established, reward is always null, and reward_eligible is always false under this telemetry contract. The producer never changes the scalar reward consumed by PPO.

## Invariants

1. Before/after snapshots must belong to the same Engine instance and episode.
2. The outcome snapshot and every player decision sequence must advance beyond the source decision.
3. Exactly eight player records and eight action traces are required; player IDs must match their array positions.
4. Owned-unit identity is UUID-based and scoped to the player snapshot. Occupied units without UUID/champion identity fail closed.
5. Shop revision arrays must contain exactly five native revisions.
6. When EconomyEngine::resolve_round overlaps the action, action-attributable gold/XP/level/interest deltas are null. A same-step PvP win/loss credit also makes action gold/interest deltas unavailable. These values are not reconstructed from a combined balance.
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


## Causal attribution candidate contract — PR #517 follow-up

`reward_signal_calibration.build_attribution_candidates` now evaluates action/outcome pairs without moving or creating reward. Policies define an explicit maximum player-decision gap per action family; the gap is a candidate-discovery bound, not a claim that the action's effect ends at that point.

Attribution is exclusive and fail-closed:
- only applied native action traces can be candidates;
- Engine instance, episode and player identity must match;
- only native PvP resolution and validated terminal placement outcomes are accepted;
- any intervening non-PASS action blocks attribution;
- multiple candidates are ambiguous; no candidate remains unattributed;
- every result has `reward=null`, `reward_moved=false`, and `causal_attribution` no stronger than `candidate_not_proven`.

This deliberately prevents delayed combat/placement reward from being duplicated as action reward while GAE already propagates it through the trajectory. It also does not claim causal proof from temporal proximity.

## Calibration evidence validator

`validate_calibration_manifest` rejects missing dataset/code/Engine/catalog identities, absent split manifests, overlapping train/validation/test episode IDs, and missing baseline/candidate/ablation report hashes. Passing this structural validator means only that the required evidence is present; it does not approve coefficients or activate reward.

## Remaining empirical acceptance

The repository does not contain an approved immutable replay dataset and completed baseline/candidate/ablation reports for these new signals. Consequently:
- action reward remains neutral under `tft.ppo.outcome-reward.v1`;
- no coefficients are fitted or promoted by runtime code;
- delayed benefits and reversals remain represented as factual evidence, not assigned scalar reward;
- calibration, statistical uncertainty, empirical anti-hacking evaluation and measured signal ablation remain unverified until the required replay artifacts exist.

The new unit tests cover exclusive candidates, intervening-action rejection, ambiguous multiple actions, failed handlers, missing calibration evidence and split leakage. These are contract tests, not empirical calibration results.


## Temporal lifecycle, reversals, pivots and adversarial audit — PR #517

`analyze_action_lifecycles` correlates native outcomes by Engine/episode/player identity and decision sequence, but emits only temporal candidates. It records a later sale of the same physical UUID as a reversal of the earlier acquisition, and a sale followed by acquisition of a different champion as an unproven pivot candidate. Neither is converted into positive or negative reward; the native PvP/placement outcome remains owned by its original producer.

`audit_reward_hacking_patterns` reports synthetic sequence patterns (repeated rerolls, repeated positioning, PASS streaks, and purchase/sale churn) as audit findings. These are adversarial diagnostics, not runtime penalties or reward coefficients. Duplicate event delivery and identity collisions fail closed.

The tests use constructed event sequences and validate bookkeeping and safety invariants only. They do not establish causal effects, optimal horizons, calibrated weights, or match-performance improvements. Replay/training data remains an empirical dependency, not a blocker for this implementation.
