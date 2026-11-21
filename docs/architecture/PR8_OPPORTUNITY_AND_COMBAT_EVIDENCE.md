# PR 8 — Opportunity cost and combat evidence

## Previous problem
The marginal envelope against HOLD already accounts for direct gold, liquidity and verified interest. Generic opportunity cost had no factual producer. The CombatEngine is a deterministic simulator with incomplete champion/trait/buff/debuff/passive coverage; its output is not an empirically calibrated opponent prediction.

## Technical rationale
Opportunity cost must describe a concrete alternative forgone on the same decision snapshot. Direct gold and interest stay exclusively in the marginal economy envelope to prevent double counting. Combat evidence must distinguish snapshot identity, actual opponent identity, mechanics coverage, observed replay outcomes and calibrated distributions.

## New responsibilities
- `strategy::OpportunityCostProducer`: select the strongest valid competing alternative and expose its identity, horizon and uncertainty. Missing or stale alternatives remain unavailable.
- `combat_evidence::CombatSnapshotBuilder`: validate match/player/opponent/round/sequence, HP and unique roster identities.
- `MatchupResolver`: accept only the opponent identity actually supplied by the lobby.
- `CombatCoverageValidator`: report partial mechanics coverage explicitly.
- `CombatPredictionCalibrator`: derive empirical quantiles only from observed, identity-bound outcomes.
- `derive_survival_risk` and `apply_to_economic_context`: publish survival evidence only when an observed-HP snapshot and calibrated damage distribution exist.

## Contracts and invariants
- No fabricated opponent, probability, damage or missing mechanic.
- Synthetic CombatEngine runs do not qualify as observed replay outcomes.
- Calibration requires a minimum sample count, matching match/player identity, non-duplicate outcome sequences and a non-stale snapshot sequence.
- Unknown opportunity cost is unavailable, never a measured zero.
- Direct gold and interest are not counted again in opportunity cost.
- No PPO, reward, action-dimension or action-mask changes.

## Impacts
Adds reusable evidence contracts and a native regression test. Existing economy scoring remains unchanged unless a validated producer supplies evidence. Combat risk remains unavailable until real replay outcomes support calibration.

## Validation
The new test covers alternative selection, invalid identity, snapshot validation, actual-opponent matching, partial coverage, empirical quantiles, HP-bound risk and refusal to publish uncalibrated evidence.

Empirical calibration quality and champion-mechanics completeness remain pending real replay datasets and catalog coverage; they are non-blocking for merge of this implementation.
