# Combat prediction calibration gate

## Previous problem

The first combat-evidence implementation promoted a damage distribution to
`calibrated` as soon as it contained the configured minimum number of
versioned replay outcomes. A sample-count threshold proves only that samples
were collected; it does not prove predictive quality, interval coverage,
probability calibration, or independence between experimental splits.

That behavior could allow a replay-backed but unevaluated distribution to
publish elimination risk into the economic context.

## Technical rationale

Calibration is an empirical acceptance decision, not a property inferred from
sample count. The runtime may construct an experimental distribution from
observed replay outcomes, but promotion requires an explicit evaluation report
and an approved acceptance protocol.

The acceptance thresholds are supplied by the versioned evaluation protocol;
this change does not invent production thresholds or claim that any model has
passed them.

## New responsibility

- `CombatPredictionCalibrator` constructs an experimental replay-backed
  distribution and never marks it calibrated by itself.
- `approve_calibration` validates the evaluation report, protocol approval,
  sample minima, finite metric ranges, metric thresholds, SHA-256 manifest
  identities, and disjoint train/validation/test manifests.
- `derive_survival_risk` accepts only a distribution promoted through the
  explicit approval gate.

## Contract and invariants

- Sample count alone never changes `calibrated` to true.
- Synthetic CombatEngine output is not an observed replay outcome.
- Calibration requires a non-empty protocol ID and an explicit approved flag.
- Report and dataset manifest identifiers must be 64-character lowercase
  SHA-256 values.
- Train, validation, and test manifests must be distinct and episode splits
  must be declared disjoint.
- MAE, P90 coverage, and Brier score must be finite and satisfy the approved
  protocol's thresholds.
- A distribution without approval remains experimental and cannot derive
  elimination risk for economic consumption.

## Impacts

This is an additive guard around the existing combat-evidence contract. It
does not change CombatEngine mechanics, PPO, reward, action dimensions, masks,
Engine legality, or action execution. It does not claim that a calibrated
predictor or a replay dataset currently exists.

## Validation criteria

- A distribution with enough replay samples remains experimental before
  explicit approval.
- Valid report metadata and metrics under an approved protocol permit
  promotion.
- Unapproved protocols, overlapping manifests, insufficient samples, invalid
  hashes, and out-of-range or threshold-violating metrics reject promotion.
- Survival-risk derivation remains unavailable for experimental distributions.

## Remaining work in issue #514

This gate closes only the unsafe sample-count-to-calibrated transition. The
full issue still requires authoritative board snapshots, factual matchup
resolution, mechanics-level coverage measurement, scenario execution through
the existing CombatEngine, replay-backed quantitative evaluation, and
identity-safe integration into EconomicController and ContextualActionEvaluator.
Replay collection/calibration results depend on #518 and remain non-blocking
for merge under the project's agreed rule; no empirical quality is claimed by
this implementation.


## Cohort isolation

Only `experimental_replay_cohort_distribution.v1` can be promoted. It must
come from independent matches with exact engine version, composition
signature, mechanics signature, round and single-round horizon. The target
match is excluded, each match contributes at most one sample, and all
artifacts must belong to one dataset version. The legacy same-match summary
is diagnostic-only and is rejected by `approve_calibration`.

The acceptance protocol also requires minimum validation and test sample
counts, not only a training sample count. `derive_survival_risk` revalidates
the stored report hash, all three distinct manifest hashes, metrics, cohort
identity and replay artifact provenance before exposing a risk value.
