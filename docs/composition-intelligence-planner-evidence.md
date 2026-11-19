# Planner Evidence Consumption (Shadow)

## Snapshot identity and freshness

Every planner evidence snapshot is bound to the current episode/match, player,
active composition ID, active composition version, and round. This
`PlannerEvidenceSnapshot` is the sole identity/version owner for its nested
EconomicController, BoardEvaluation and ItemEngine evidence.

Each source metadata carries only its source name, source round, expected
round, quality, availability and reason. Consumers validate the snapshot
identity once, then validate each source's freshness independently. A source
is consumed only when its metadata is available, quality is `valid`, and its
source/expected rounds match the current round. A stale or invalid source does
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

- Match/player/composition/version/round identity once on the
  PlannerEvidenceSnapshot/diagnostic envelope.
- Source-local provenance and freshness only in each nested source metadata.
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


## Envelope consolidation — PR #484

**Prior problem:** each evidence source repeated match/player/composition
identity and a `source_version` value that was populated from the enclosing
composition version. The diagnostic JSON therefore serialized the same
correlation identity several times.

**Technical rationale:** all three sources are constructed together and
consumed through one PlannerEvidenceSnapshot. Snapshot identity is validated
before individual source freshness. The source version was not independently
produced and therefore did not identify a distinct source revision.

**New responsibility:** PlannerEvidenceSnapshot owns match/player/composition/
version/round. EvidenceSourceMetadata owns source, source/expected round,
quality, availability and reason. CompositionDiagnosticSnapshot owns the
serialized diagnostic identity envelope; nested evidence contains source facts
only.

**Contract/invariants:** PlannerEvidenceSnapshot schema v2 removes repeated
identity and source_version fields from source metadata. Source and expected
round remain separate. A source remains unavailable/stale/partial/invalid as
appropriate; no missing value is synthesized.

**Cross-component impact:** PlannerEvidenceAdapters, UnitPriorityPlanner,
LineupPlanner, CompositionActionEvaluator, ContextualActionEvaluator,
CompositionDiagnosticRecorder and the native producer now share the single
identity boundary. The Viewer continues reading source quality from nested
metadata and correlation identity from the parent record.

**Validation:** native compilation covers every consumer; regression checks
assert that source metadata cannot reintroduce parent identity fields and that
snapshot identity is validated before source freshness. This consolidation
does not alter strategic scores, PPO inputs, reward, masks or action legality.

## Candidate identity, costs and unit-priority evidence — PR #495

**Prior problem:** candidate records were tied to match/player/sequence and a partial physical slot, but a move's target slot was not part of its stable identity. The contextual evaluator did not retain that identity, so the executor could only correlate a recommendation by candidate index and summary fields. Buy candidates also did not expose the source/horizon/uncertainty of their estimates; marginal interest loss was not attached consistently, and the contextual scorer discarded negative direct cost from an explicitly evidenced sale. Unit upgrade progress flattened physical star tiers and counted every shop copy as affordable once one copy was affordable. The producer also left trait-completion and explicit sell-candidate evidence under-populated.

**Technical rationale:** a candidate is a read-only alternative from one exact native snapshot. Correlation therefore requires all physical parameters, including source and destination slots, and the same identity must survive both evaluators and executor validation. Upgrade progress must reflect actual 1★/2★ instances and copies affordable with current gold; aggregate equivalent-copy counts cannot distinguish mixed tiers. Trait completion and sell candidacy must be derived from current board traits, active native composition, observed copies, and ItemEngine state.

**New responsibility:** StrategicActionCandidateBuilder now creates stable IDs from match/player/sequence/action/champion/shop/source/target/source-zone and attaches evidence source, horizon and uncertainty. It computes marginal interest loss only when interest evidence is available. UnitPriorityPlanner uses physical star-tier counts and caps shop progress by the number of offers the current gold can actually buy. The native producer supplies trait-completion and conservative sell-candidate evidence. Both action evaluators preserve candidate identity; StrategicActionExecutor rejects a recommendation whose ID differs from the source candidate. Contextual scoring preserves sale revenue as a negative direct cost rather than clamping it away.

**Contract/invariants:** candidate identity is immutable within its source sequence and includes every physical action parameter. Missing interest evidence remains unavailable, not a measured zero. Evidence uncertainty is an audit score, not a success probability. Shop copies contribute only when unit cost and available gold are known. A 3★ target counts complete additional 2★ instances; partial groups of 1★ copies do not become false 3★ progress. A sell candidate remains diagnostic and requires an exact legal bench instance plus explicit transition/priority evidence. No candidate is executed by this pipeline.

**Cross-component impact:** StrategicPlanning.hpp, StrategicActionCandidateBuilder, UnitPriorityPlanner, CompositionEvaluation, both action evaluators, StrategicActionExecutor, the TftEngine producer, and their native regression tests. PPO observations/rewards/checkpoints, action masks, game rules, and Viewer behavior are not changed by this contract.

**Validation:** native tests cover unique physical candidate IDs, target-slot identity, evidence provenance/horizon/uncertainty, marginal interest, stable identity through both evaluators, executor rejection of mismatched candidate IDs, sale-credit scoring, mixed physical star tiers, and shop affordability with insufficient versus sufficient gold. Runtime evidence tests verify the active composition/item path; the full PR CI must pass before merge.

**Known unavailable economic projections:** projected next-round income, estimated incoming damage, elimination risk and progression plan remain unavailable unless an authoritative producer supplies them for the current player/round. The controller and adapters must preserve that missingness; this PR does not synthesize projections from defaults or turn them into score inputs.

### Economic signal routing

EconomicController's evidence_used/evidence_missing lists now describe only
signals consumed by its posture score: HP, gold, level, XP-to-next, win/loss
streaks, relative board power, and any future validated damage/risk/progression
producers. Raw XP and absolute board power remain available to their other
consumers but do not independently affect posture. Current interest is not a
posture signal: StrategicActionCandidateBuilder consumes it to calculate
marginal interest lost by a known spend, and marks that cost unavailable when
the source flag is absent. Projected next-round income has no validated producer
in the current callsite and remains explicitly unavailable. Progression posture
can still be inferred contextually from observed stage, level, XP-to-next, gold,
board pressure and survival evidence; it does not require a legacy strategy ID
or an invented progression_plan.
