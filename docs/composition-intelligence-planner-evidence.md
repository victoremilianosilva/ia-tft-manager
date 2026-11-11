# Planner Evidence Consumption (Shadow)

## Snapshot identity and freshness

Every planner evidence snapshot is bound to the current episode/match, player,
active composition ID, active composition version, and round. Each source
(EconomicController, BoardEvaluation, ItemEngine) carries the same identity,
source round, expected round, and source version.

Consumers validate the snapshot envelope and each source independently.
A source is consumed only when its metadata is available, quality is `valid`,
and all identity/version/round fields match. A stale or invalid source does
not invalidate unrelated valid sources. Missing, stale, partial, and invalid
sources remain distinguishable in diagnostics; no absent source is converted
into a zero score or a negative signal.

Economic context also requires the StrategicSharedContext player ID to match
the player whose runtime is being evaluated, and the EconomicController
decision to be Shadow-only. Non-finite economic or board metrics are marked
invalid rather than silently normalized into usable evidence.

## Consumer mapping

| Consumer | Evidence consumed | Use |
| --- | --- | --- |
| UnitPriorityPlanner | BoardEvaluation | Adds a bounded role-priority adjustment when the observed board reports a missing frontline or backline/exposed carry. |
| UnitPriorityPlanner | ItemEngine | Uses the current per-unit equipped-item snapshot to restrict sale/substitution recommendations, including units outside the target composition. |
| LineupPlanner | BoardEvaluation | Adds a bounded priority adjustment to target frontline/carry roles that address observed structural gaps; emits the exact observed counts and evidence status. |
| CompositionActionEvaluator | EconomicController | Supplies action-specific opportunity-cost proxies for buy unit, buy XP, and reroll; reroll selects the with-target or without-target cost according to actual upgrade targets. Gold, interest, projected income, and posture are exposed in the diagnostic. |
| CompositionActionEvaluator | BoardEvaluation | Uses observed frontline/backline/exposed-carry gaps to enrich composition fit for matching target roles; it does not recalculate board scores. |
| CompositionActionEvaluator | ItemEngine | Rejects a sale candidate when the current validated item snapshot shows equipped items, in addition to existing transition/sale restrictions. |

The board role adjustments are bounded tie-breaker signals. They do not
override core-unit priority, create missing champion data, or mutate board
state. Economy opportunity costs are used only when the candidate does not
already carry a higher opportunity-cost value. Item evidence never causes an
equip, unequip, sale, purchase, or movement.

## Diagnostics

The JSONL snapshot exposes:

- Match/player/composition/version/round identity on the envelope and each
  source metadata record.
- Human-readable quality: `missing`, `stale`, `partial`, `invalid`, or
  `valid`, with source-specific reason.
- Evidence consumed/rejected by Unit Priority and Action Evaluation.
- Observed board counts and the board evidence availability/reason used by
  Lineup.
- Economic gold, interest, projected next-round income, and posture consumed
  by Action Evaluation.

## Isolation

All adapters and consumers are read-only. This work does not alter the
Economic Controller, Board Evaluation, ItemEngine, action execution, PPO,
training, observations, masks, legal actions, rewards, checkpoints, or game
rules. Composition Intelligence remains opt-in and Shadow-only.
