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
| CompositionActionEvaluator (baseline path) | EconomicController decision | Receives the decision/policy context for action-specific opportunity-cost evaluation of buy unit, buy XP and reroll. Only fields present, valid and actually consumed by this path may influence its score. Diagnostic serialization of a field is not proof that the field affects the score. |
| CompositionActionEvaluator (baseline path) | Economic diagnostics | Exposes gold, interest, projected-income availability and posture for audit. Projected next-round income is currently unavailable because no validated producer populates it; it must not be treated as zero or as a scoring input. |
| CompositionActionEvaluator | BoardEvaluation | Uses observed frontline/backline/exposed-carry gaps to enrich composition fit for matching target roles; it does not recalculate board scores. |
| CompositionActionEvaluator | ItemEngine | Rejects a sale candidate when the current validated item snapshot shows equipped items, in addition to existing transition/sale restrictions. |
| ContextualActionEvaluator | EconomicControlDecision | No direct consumption is established in the audited callsite. Do not infer a dependency from the baseline evaluator or shared diagnostics. |

The board role adjustments are bounded tie-breaker signals. They do not
override core-unit priority, create missing champion data, or mutate board
state. Economy opportunity costs are used only when the candidate does not
already carry a higher opportunity-cost value. Item evidence never causes an
equip, unequip, sale, purchase, or movement.

The baseline `CompositionActionEvaluator` and independent
`ContextualActionEvaluator` are not interchangeable. Their score semantics,
inputs and evidence consumption differ. Divergence is diagnostic; this
document does not establish a shared score scale or require agreement.

## Diagnostics

The JSONL snapshot exposes:

- Match/player/composition/version/round identity on the envelope and each
  source metadata record.
- Human-readable quality: `missing`, `stale`, `partial`, `invalid`, or
  `valid`, with source-specific reason.
- Evidence consumed/rejected by Unit Priority and Action Evaluation.
- Observed board counts and the board evidence availability/reason used by
  Lineup.
- Economic source values and their availability/provenance, including gold,
  interest, projected next-round income and posture. Projected income remains
  unavailable until a validated producer and horizon exist; diagnostic
  presence does not make it a consumed scoring feature.

## Isolation

All adapters and consumers are read-only. This work does not alter the
Economic Controller, Board Evaluation, ItemEngine, action execution, PPO,
training, observations, masks, legal actions, rewards, checkpoints, or game
rules. Composition Intelligence remains opt-in and Shadow-only.

## Current architecture reconciliation (2026-11-14)

This document describes the current Shadow planner evidence adapters and their
read-only consumers. Its statement that the current work does not alter PPO
observations is an implementation-scope fact, not a decision that canonical
strategic evidence must remain unavailable to PPO forever.

For the target architecture, any future PPO context projection must consume
only the approved, versioned source contracts and preserve field-level
provenance, quality, identity, source sequence, and unavailable/missing states.
The projection is downstream and read-only. It must not write back into
StrategicPlanner, ActiveCompositionManager / TransitionManager,
EconomicController, UnitPriorityPlanner, or LineupPlanner.

The evaluator outputs, bounded score adjustments, recommendations, and
confidence proxies remain diagnostics/proposals; they are not PPO labels,
reward targets, or action authority. Unified Shadow state remains diagnostic
and isolated. The Engine and native masks remain the final legality authority.

**Prior limitation:** the previous consumer map could be read as claiming that
projected next-round income was a validated input consumed by Action
Evaluation, and did not state the distinct baseline/contextual evaluator
boundary strongly enough.

**Reason for clarification:** the approved Economic Evidence Contract requires
field-level producer, availability, horizon and consumer mapping. An absent
projection must not be treated as zero or as a scoring input, and the baseline
evaluator's inputs must not be attributed to the independent contextual path.

**Ownership/contract:** EconomicController owns posture/progression outputs;
a future income projection requires its own validated producer and horizon.
Each evaluator owns only its declared input set. The diagnostic recorder
reports availability/consumption but does not create a dependency.

**Cross-component impact:** coordinate with #282/#284/#289/#290 and the
approved economic evidence, strategic ownership, action candidate and replay
contracts.

**Validation:** documentary reconciliation against the approved Economic
Evidence and Strategic Ownership contracts and the audited evaluator callsites.
Post-Gate-8 tests must prove per-field consumer attribution, unavailable
projected income, source freshness, read-only behavior, and independent
baseline/contextual evaluator semantics.
