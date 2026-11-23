# Native strategic evidence calibration protocol

## Status

This protocol is active, but the current native composition and contextual-action scores remain **heuristic and uncalibrated** until a dataset of real match/replay observations with stable match, player, round, sequence, unit and combat identities is available.

No synthetic fixture, unit-test ordering, or generated candidate score is accepted as empirical calibration evidence.

## Evidence contracts

- Every evidence item must preserve match ID, player ID, round, decision sequence, producer, source snapshot, horizon, value basis and uncertainty.
- Owned copies, current shop offers and shared-pool availability are distinct acquisition states. A positive pool count means potentially acquirable in a future shop, not immediately purchasable.
- Unknown pool state is not exhausted pool state.
- Item fit is measured only from actual equipped item IDs, supported item-catalog definitions and the observed unit combat/profile snapshot. Missing or unsupported item data stays unavailable.
- Per-unit board contribution stays unavailable until combat outcomes can be attributed to a stable unit identity over a declared horizon. Purchase cost, star tier, role and trait overlap are not combat contribution.
- Opportunity cost currently compares alternatives on the same decision snapshot using `contextual_action_score.v1`. This is a contextual score basis, not a calibrated gold value or causal estimate of future value. It must remain labeled as heuristic.

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
