# PR 8 — Opportunity cost and combat evidence

## Previous problem
The marginal envelope against HOLD already accounts for direct gold, liquidity and verified interest, but opportunity cost was limited to a BUY-only producer. That missed competing actions whose values are already evaluated by the native contextual evaluator. The CombatEngine is a deterministic simulator with incomplete champion/trait/buff/debuff/passive coverage; its output is not an empirically calibrated opponent prediction.

## Technical rationale
Opportunity cost is the net value of the strongest concrete alternative forgone on the same decision snapshot. The producer must compare alternatives in one explicit value basis and horizon. The contextual evaluator already computes each action's board, unit, upgrade, lineup and economy components, so its net score is the common basis: each alternative's direct gold, liquidity and interest costs are included once before opportunity cost is applied. The producer does not add those costs a second time.

Progression is valued only when a verified XP purchase immediately reaches the next level and unlocks an owned bench unit already selected by the lineup. Positioning uses the deterministic same-snapshot board-position score. Reroll remains unavailable as a positive alternative without a shop-outcome probability model.

Combat evidence must distinguish snapshot identity, actual opponent identity, mechanics coverage, observed replay outcomes and calibrated distributions.

## New responsibilities
- `strategy::OpportunityCostProducer`: select the strongest valid alternative and retain its candidate identity, common value basis, horizon and uncertainty.
- `StrategicActionCandidateBuilder`: emit factual progression value only when the exact XP threshold, full current board, selected lineup bench unit, physical bench UUID and UnitPriority evidence all agree. Positioning candidates carry a same-snapshot deterministic board score and one-round horizon.
- `ContextualActionEvaluator`: score candidates against HOLD first, then compare all eligible action families on `contextual_action_score.v1`. This includes BUY, XP level-up, deploy/move and sale when their evidence is valid. Sale subtracts the retained strategic value of the unit being sold. The evaluator applies the best alternative's net score once and reselects the action afterward. Candidate scores expose source sequence, opportunity value, value basis and forgone candidate.
- `combat_evidence::CombatSnapshotBuilder`: validate match/player/opponent/round/sequence, HP and unique roster identities. The real `TftEngine` pair emits a versioned `COMBAT_SNAPSHOT_V1` structured event in `StepResult.events`, including invalid snapshots and their rejection reason.
- `MatchupResolver`: accept only the opponent identity actually supplied by the lobby.
- `CombatCoverageValidator`: report partial mechanics coverage explicitly.
- `CombatPredictionCalibrator`: derive empirical quantiles only from observed, identity-bound outcomes.
- `derive_survival_risk` and `apply_to_economic_context`: publish survival evidence only when an observed-HP snapshot and calibrated damage distribution exist.

## Contracts and invariants
- Alternatives must share the exact match/player/round/snapshot sequence, horizon and value basis. HOLD is the zero-value baseline; alternatives with non-positive net score do not create an opportunity cost.
- The contextual score supplied to the producer is already net of direct gold, liquidity and interest. The producer never re-applies those costs.
- Unknown opportunity cost is unavailable, never a measured zero. Reroll is not assigned a fabricated expected shop value.
- Progression value is unavailable unless a level-up unlocks a verified selected bench unit; no generic XP prior is invented.
- No fabricated opponent, probability, damage or missing mechanic.
- Synthetic CombatEngine runs do not qualify as observed replay outcomes.
- Calibration requires a minimum sample count, matching match/player identity, non-duplicate outcome sequences strictly before the decision sequence, a prior round, and explicit versioned-replay provenance (artifact ID and dataset version). Simulator-only samples, missing provenance, or mixed artifact/version inputs are rejected. Fractional observed HP is preserved; invalid, overlapping or incomplete unit identities are rejected. Derived survival evidence retains match/player/round/sequence identity and cannot be applied to a different match, player, round or strategic-context sequence. The combat event carries both the engine-wide decision sequence and the per-player strategic-context sequence, so replay consumers do not conflate their domains. The emitted runtime snapshot explicitly marks mechanics coverage as unmeasured rather than implying roster completeness proves mechanics completeness.
- No PPO, reward, action-dimension or action-mask changes.

## Impacts
Adds a reusable net-opportunity producer/consumer contract and a native regression test. The contextual evaluator schema is version 4 and exposes the opportunity value and basis. Existing marginal economy scoring remains the sole owner of the selected action's direct costs; the competing alternative's net contextual score is subtracted once. The real matchup now emits structured, identity-bound snapshot evidence for replay/audit consumers. Combat risk remains unavailable until replay outcomes support calibration.

## Validation
Tests cover net cross-action opportunity comparison, BUY/positioning/sale evidence, XP level-up with a verified selected bench unit, explicit board-value evidence, snapshot identity, actual-opponent matching, partial coverage, empirical quantiles, fractional HP-bound risk, replay provenance and refusal to publish uncalibrated evidence.

Empirical calibration quality, champion-mechanics completeness, replay persistence and downstream consumption of calibrated risk remain pending real replay datasets and catalog coverage; they are non-blocking for merge of this infrastructure. Reroll opportunity remains unavailable until a factual shop-outcome probability producer exists. The emitted snapshot event is the collection boundary, not proof that replay storage or calibration has already run.
