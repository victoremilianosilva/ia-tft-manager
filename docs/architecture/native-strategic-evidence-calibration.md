# Native strategic evidence calibration protocol

## Status

This protocol is active, but the current native composition and contextual-action scores remain **heuristic and uncalibrated** until a dataset of real match/replay observations with stable match, player, round, sequence, unit and combat identities is available.

No synthetic fixture, unit-test ordering, or generated candidate score is accepted as empirical calibration evidence.

## Evidence contracts

- Every evidence item must preserve match ID, player ID, round, decision sequence, producer, source snapshot, horizon, value basis and uncertainty.
- Owned copies, current shop offers and shared-pool availability are distinct acquisition states. A positive pool count means potentially acquirable in a future shop, not immediately purchasable.
- Unknown pool state is not exhausted pool state.
- Item fit is measured only from actual equipped item IDs, supported item-catalog definitions and the observed unit combat/profile snapshot. Missing or unsupported item data stays unavailable.
- The native runtime now exposes a narrowly defined factual board-unit damage-share signal from completed combat results. It is joined through persistent board-unit UUIDs and aggregated by champion for the next decision. It is not a complete measure of strategic contribution and remains uncalibrated; cost, star tier, role and trait overlap are never substituted for combat outcomes.
- Opportunity cost currently compares alternatives on the same decision snapshot using `contextual_action_score.v1`. This is a contextual score basis, not a calibrated gold value or causal estimate of future value. It must remain labeled as heuristic.

## Current native board-contribution producer

The producer joins `CombatUnitResult` to the persistent board-unit UUID through
the combat input's source board position, then aggregates damage dealt by champion
for each player. It publishes each champion's share of damage dealt by the player's
mapped board units only after a completed, non-timeout combat with valid attribution
and positive team damage. The evidence is bound to match, round and combat sequence,
expires after the next decision window, and is cleared on episode reset.

This is factual simulator telemetry, not calibrated ground truth. It measures damage
share only; it does not yet capture all forms of frontline mitigation, crowd control,
trait utility, or counterfactual contribution. Missing or incomplete attribution
remains unavailable rather than becoming a zero measurement.

## Dataset requirements

Each row must contain:
- match/player/round/decision sequence and patch/set/catalog version;
- observed board, bench, shop, shared pool, gold, level, items and physical star-tier copies;
- candidate composition and lineup identity/version;
- candidate action, feasibility, acquisition cost, interest delta and forgone alternative;
- combat result and per-unit attribution where supported;
- evidence producer, availability, horizon, uncertainty and source identity.

Rows without complete identity or with mixed source sequences are excluded rather than repaired by inference.

## Split and leakage controls

- Split by complete match, never by individual observation row.
- Use chronological train/validation/test partitions by patch window.
- Keep all observations from a match in one partition.
- Fit normalization and calibration parameters on training data only.
- Report patch and stage/level strata separately; do not tune thresholds on the final test partition.
- Replays used for a calibration report must be immutable and identified by artifact hash.

## Required metrics

- Candidate ranking: NDCG@k, pairwise ranking accuracy and top-1 agreement against independently labeled outcomes.
- Direction quality: direction stability, time-to-commitment, false commitment rate and composition survival by stage.
- Pivot quality: pivot frequency, pivot regret, acquisition cost, time-to-feasibility and post-pivot outcomes.
- Economic quality: gold spent, interest forgone, liquidity trajectory, upgrade realization and opportunity-cost ranking agreement.
- Evidence quality: availability/coverage, stale-sequence rejection, calibration error and uncertainty by source.
- Report all metrics overall and stratified by patch, stage, level, gold band and candidate acquisition profile.

## Ablation and acceptance

Evaluate a frozen baseline and one-feature-at-a-time ablations for item fit, board contribution, pair/upgrade progress, pool reachability, direct acquisition cost, interest and opportunity cost. Define acceptance thresholds before examining the held-out test set. Publish confidence intervals and sample counts.

Weights and thresholds must not be adjusted merely to satisfy unit tests or improve synthetic ordering. Until the required real replay dataset exists, these fields remain explicitly heuristic/unavailable and the calibration gate remains open.
