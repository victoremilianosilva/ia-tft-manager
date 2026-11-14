# Integrated Shadow Audit Index

## Purpose

The existing `Executar auditoria` flow now produces one integrated, versioned
correlation index in addition to the existing per-domain reports. The index
does not replace or rewrite player JSON logs, legacy TFT text logs, or
`composition_diagnostics.jsonl`.

Output:
- `audit/audit_integrado.md` — integrated producer inventory, integrity
  diagnostics, normalized comparison and player/round timeline.
- The temporary `audit_report.json` includes `integrated_audit_index` and
  `integrated_audit_metrics` for the Viewer tab. It is not left in the session
  directory.

## Correlation envelope

New Viewer sessions write `correlation` schema v1 into each valid Composition
Intelligence JSONL record:
- `match_id`: Viewer session UUID, not the native engine episode ID;
- `player_id`: zero-based player seat;
- `round`: native global round ID;
- `timestamp_unix_ms`: source timestamp from the C++ snapshot;
- `sequence_id`: existing Composition Intelligence sequence;
- `composition_id` and `composition_version`;
- `identity_complete` and `timestamp_available`.

The record also retains `engine_match_id`, the original diagnostic fields,
and all existing schema fields. The C++ producer now exports `player_id` and
the source timestamp for successful snapshots. The Viewer adds the session
UUID when persisting the new session's JSONL.

Player log events retain their own per-player `sequence_id`, timestamp, round,
and match ID. The audit normalizes Viewer stage-round labels (for example
`2-1`) into the native global round number. Correlation is scoped by match,
player and round. Where a player event carries a composition ID/version, the
recommendation comparison requires the same identity/version.

## Data classification

The index keeps source payloads and classifications separate:
- observed PPO action and player state;
- Strategic Planner decisions/reasons;
- Economic Controller posture and validated Economy evidence;
- Composition Intelligence snapshots and transitions;
- Unit Priority, Lineup, Board and Item evidence in the original diagnostics;
- Action Evaluator baseline and independent contextual evaluator;
- later outcome observations.

The original Composition Intelligence record remains available in each
indexed snapshot, and index entries include source file/sequence references
for drill-down. Repeated player events are deduplicated by match/player/sequence.
Repeated Composition Intelligence sequence IDs are deduplicated by
match/sequence. Repeated strategic observations are summarized as one semantic
review with an observation count; changed decisions/reasons remain distinct.

## Strategic Planner KEEP confidence

The `audit_estrategia.md` report classifies each deduplicated KEEP review as
supported by current directional evidence, associated mainly with persistence
or investment proxies, or inconclusive. It separately reports alternative
evaluation outcomes and groups examples by player/round within the match
session. Board presence alone and the absence of a better alternative are not
treated as positive evidence. See
[Strategic Planner KEEP confidence audit](strategic-keep-confidence-audit.md)
for the classification rules and limitations.

## PPO comparison

PPO actions are normalized to categories:
- BUY → BUY_UNIT
- BUY_XP → BUY_XP
- REROLL → REROLL
- MOVE_BENCH / MOVE_BOARD → MOVE
- SELL → SELL
- PASS → HOLD

Evaluator action enums are normalized using the native
`StrategicActionKind` contract. Each PPO action is compared only with the
nearest timestamped evaluator snapshot for the same match/player/round, within
30 seconds. A known composition ID/version must match. Without the required
timestamp or identity, the comparison is `unavailable`, not guessed.

Agreement is not a quality score. PPO is not ground truth, and divergence
between baseline, contextual evaluator and PPO is retained as diagnostic
information rather than optimized away.

## Integrity and legacy compatibility

The report identifies:
- missing producers and missing correlation envelope fields;
- parse errors, duplicate event/sequence IDs, out-of-order sequences and
  sequence gaps;
- unversioned legacy records separately from unsupported future schema versions;
- missing/stale/partial/invalid evidence without converting it to numeric zero.

Legacy player logs and older Composition Intelligence JSONL remain readable
through the existing readers. Legacy records without an explicit match/player
envelope are preserved in their domain report and marked uncorrelatable in the
integrated index. No snapshot is synthesized from PPO logs.

## Safety boundaries

The integrated index is offline and read-only. It does not call planners,
create decisions, modify original logs, or connect to the executor. It does not
change PPO, training, observations, masks, legal actions, rewards, checkpoints,
game rules, or action execution. Correlation with later outcomes is explicitly
labelled correlation-only, never causal attribution.


## Current architecture reconciliation (2026-11-14)

This index is an **offline audit and correlation artifact**. Its “observed PPO
action and player state” classification and evaluator comparison do not mean
that the index is a live PPO input, that evaluator agreement is a quality
target, or that the PPO action is ground truth.

The future observation contract may project validated canonical state/evidence
from approved source owners into PPO, but this audit index is not that
projection. It must not synthesize observations from logs or promote Shadow
recommendations, scores, confidence, candidate rankings, or outcomes into PPO
labels/rewards. The action, baseline recommendation, contextual proposal and
executor resolution remain separate data sources; unavailable correlation
stays unavailable.

**Prior limitation:** the index described its current data classes but did not
explicitly state its non-role in the future PPO observation pipeline.
**Reason for clarification:** offline correlation and online model input have
different ownership, freshness, and validation contracts.
**Ownership/contract:** this index owns only audit presentation/correlation;
the versioned observation adapter is a separate future consumer of approved
source contracts.
**Cross-component impact:** #286/#289/#293/#294 and the approved candidate,
ownership, replay and evaluation contracts. No logs or runtime behavior change.
**Validation:** documentary consistency now; post-Gate-8 acceptance must prove
that audit artifacts cannot become training labels or runtime observations.
