# Economic Evidence and Progression Contract v1

**Status:** approved contract; partial runtime implementation and executable acceptance in PR 2  
**Contract ID:** `tft.economic-evidence.v1`  
**Target:** `new-arquiteture`  
**Related:** #282, #281, #283, #284, #289; Observation #293; Reward #287

> Runtime scope: this contract evolves the existing read-only economic evaluators and evidence adapters. It does not alter PPO, rewards, observations, Engine rules/masks, or Viewer behavior.

## 1. Purpose

The audit found that the integrated `StrategicSharedContext` path fills several observed economy fields (HP, gold, level, XP, XP-to-next, interest-if-resolved, streaks, and board-power signals), but does not populate `projected_next_round_income`, `estimated_incoming_damage`, `elimination_risk`, or `progression_plan`. Those fields retain defaults, while downstream posture scoring can consume them. The bridge can also mark a field Valid merely because it exists in the context, even when it is an unfilled default.

This contract distinguishes observed facts, derived values, estimates, unknowns, economic posture, progression hypotheses, and evaluator consumption.

## 2. Normative principles

1. **Observed values require a source.** A numeric field is not observed merely because its struct has a default.
2. **Missing is not zero.** Unknown income, damage, risk, board power, interest, or progression must remain explicitly unavailable/partial.
3. **Provenance is field-level.** A valid match/player envelope does not make every economic field valid.
4. **Estimates carry a horizon and uncertainty.** No projected value is meaningful without stating the interval/rounds it covers and its evidence quality.
5. **Posture is not an action.** Accumulate/stabilize/progress-like postures describe context; they do not force BUY, BUY_XP, REROLL, HOLD, or SELL.
6. **Progression is a separate hypothesis.** A Flexible/default plan is not evidence that a progression analysis occurred.
7. **No legacy strategy IDs.** Do not reintroduce fixed ECON/ALL_IN/FAST8/SLOWROLL policy selection.
8. **No double counting.** Costs and benefits must share a common baseline with explicit decomposition.
9. **Shadow/read-only.** Economic decisions are diagnostics/evidence for recommendations, never executed actions or PPO targets.

## 3. Evidence envelope

Every economic field or coherent evidence group must carry:
- value, when available;
- origin: observed, derived, estimated, inferred, or unknown;
- quality: valid, partial, missing, stale, invalid, unavailable;
- source component and source version;
- engine match/episode, player, round, and typed source-sequence reference(s);
- estimate horizon and method/version, when derived or estimated;
- reason and uncertainty bounds/range when the producer can support them.

A default numeric value without a corresponding availability/provenance declaration is unavailable, not observed. In particular, HP 100, gold 0, level 1, damage 0, risk 0, relative board power 0, and Flexible progression cannot be treated as observed evidence solely because they are defaults.

## 4. Evidence inventory and source policy

| Evidence | Contract origin | Source / policy | Missing-data behavior |
|---|---|---|---|
| HP, gold, level, XP, XP-to-next | Observed | Current validated Engine player snapshot | Unavailable if snapshot/field is absent or stale |
| Current interest / gold threshold | Observed or deterministically derived from observed gold and current rules version | Engine snapshot plus declared rule version | Unknown if gold or rule version is unavailable |
| Win/loss streak | Observed | Current player/match snapshot | Unknown if absent; do not infer from a partial history |
| Current board power | Derived | Declared board evaluator/version over current observed board | Partial if board or required unit evidence is incomplete |
| Relative board power | Derived | Current board and explicitly identified comparison baseline | Unknown if opponent/reference baseline is absent; zero is a valid value only with valid provenance |
| Projected next-round income | Estimated/derived | Dedicated projection producer using observed economy, streak, interest and round transition rules | Unavailable if inputs or rule version are insufficient |
| Estimated incoming damage | Estimated | Explicit combat/outcome estimator with declared horizon and calibration/version | Unavailable if no valid combat evidence; never default to zero |
| Elimination risk | Estimated | Explicit risk estimator using HP, incoming damage horizon, and available survival evidence | Unavailable if required inputs are missing; not a fixed heuristic label |
| Progression plan | Inferred hypothesis | EconomicController using validated economy, board, stage and risk evidence | Unknown/unavailable until sufficient evidence supports a plan |
| Economic posture | Derived decision | EconomicController over validated evidence | Indeterminate/insufficient-evidence when required inputs are missing |

This table defines source responsibilities, not permission to fabricate a producer. If a trustworthy source does not exist, the field remains unavailable until one is specified and validated.

## 5. EconomicController ownership and outputs

Per the approved Gate 5 ownership decision, `EconomicController` owns two distinct outputs:

### 5.1 Economic posture

A time-bounded contextual assessment of the player's economic situation. It must include:
- posture label and decision revision;
- evidence fields actually consumed;
- source-sequence references;
- horizon;
- evidence sufficiency/quality;
- reason and uncertainty;
- signals computed but not consumed, explicitly marked diagnostic-only.

Posture cannot mutate strategic direction, active composition, composition lock, or action candidates. It cannot force an action family.

### 5.2 Progression hypothesis

A separate, independently versioned hypothesis describing a possible development trajectory (for example, whether leveling or reroll-oriented development is supported by the evidence). It must include:
- hypothesis and revision;
- stage/round horizon;
- supporting and contradicting evidence;
- source/provenance/quality;
- explicit unknown/insufficient state.

Posture and progression may share input evidence but are not interchangeable and must not be collapsed into one strategy ID. Default Flexible is unknown unless the controller actually evaluated the evidence and explicitly selected a flexible hypothesis.

## 6. Economic signal consumption

The contract requires an explicit consumer map for each signal:
- `streak_strength`;
- `interest_if_resolved_now`;
- survival pressure;
- board pressure;
- economy pressure;
- relative board power;
- projected income;
- incoming damage;
- elimination risk;
- progression hypothesis.

For each signal, the implementation design must state whether it is consumed by:
1. EconomicController posture;
2. EconomicController progression;
3. baseline ActionEvaluator;
4. contextual candidate evaluator;
5. diagnostics only.

A signal not consumed by a component must not be described as influencing that component's score. In PR 2, the contextual candidate evaluator consumes only validated survival pressure, streak evidence, and exact same-snapshot gold/interest deltas. It does not consume nominal posture labels or unavailable future-income/damage/risk fields. The baseline CompositionActionEvaluator path still receives EconomicControlDecision, but unproduced action-family opportunity premiums are no longer added.

## 7. Marginal cost and opportunity-cost accounting

Each candidate's economic effect is measured against the same source snapshot and declared horizon.

Required decomposition:
- immediate gold spend/proceeds;
- gold after the candidate;
- interest delta under the declared rule version;
- projected income delta;
- reroll/XP/shop options preserved or consumed;
- board-strength and upgrade effects;
- survival/risk effects when supported;
- residual opportunity cost not already represented;
- uncertainty and unavailable inputs.

Do not sum direct spend, lost interest, and a generic opportunity-cost estimate when the latter already includes those terms. HOLD/PASS is the reference alternative, not a zero-cost assumption. The candidate contract in #281 owns the candidate-level envelope; this document defines the economic evidence carried into it.

## 8. Bridge and serialization requirements

A bridge must preserve field-level origin, quality, source, reason, horizon, and sequence. It must not mark all fields Valid because the enclosing match/player context is valid.

- A default value without an explicit source is missing/unavailable.
- Observed zero must be distinguishable from absent zero.
- Derived/estimated posture, progression, board power, damage, and risk must not be serialized as observed facts.
- Unknown lock remains unknown; economic evidence cannot infer lock state.
- Viewer/JSONL diagnostics must display unavailable/partial explicitly rather than showing defaults as facts.

## 9. Acceptance matrix — after Gate 8

| Scenario | Required result |
|---|---|
| Empty economic context | Insufficient evidence; no apparently confident posture |
| Real gold = 0 vs missing gold | Distinct observed-zero and unavailable states |
| Real HP = 100 vs default HP | Distinct observed value and unprovided default |
| Relative board power = 0 with valid baseline | Valid derived zero |
| Relative board baseline missing | Unknown, not zero |
| Projected income unavailable | No fabricated zero-income estimate |
| Damage/risk estimator unavailable | Unknown damage/risk, no false safety signal |
| Flexible default without evaluation | Unknown progression |
| Posture/progression disagreement | Both outputs and evidence preserved distinctly |
| Streak/interest computed but unused | Explicit diagnostic-only or justified consumer |
| Same candidates, changed HP/pressure | Score changes only where a documented marginal effect exists |
| Conflicting or stale sequences | Evidence rejected/marked stale |
| Missing economic evidence in bridge | Field-level partial/missing, not Valid |
| Candidate vs HOLD | Same baseline/horizon, no double counting |

Tests must also prove which evidence reaches each evaluator and which score components it affects. Confidence remains non-probabilistic.

## 10. Gate status and implementation boundary

This document specifies the economic evidence and ownership contract. #282 remains open until the source map is validated, field-level provenance is propagated, consumer decisions are documented, and executable evidence is produced after Gate 8.

No runtime files/tests, PPO, observations, rewards, checkpoints, masks, Engine rules, Viewer behavior, or game actions are changed. Gate 8 and explicit implementation authorization remain mandatory.

## 11. Runtime source audit and PR 2 implementation

### 11.1 Authoritative sources and unavailable projections

The runtime source audit found the following:

| Field | Authoritative source found | PR 2 disposition |
|---|---|---|
| Current gold / level / XP / streak | Native player economy snapshot | Observed when the native field is present |
| Current interest | `EconomyEngine::get_interest(gold)` | Deterministic derived value; cross-checked against observed gold |
| Immediate post-action gold | Candidate direct cost/proceeds + same native gold snapshot | Exact marginal cash delta |
| Post-action interest | `EconomyEngine::get_interest(gold_after)` | Exact marginal delta under the current Engine rules |
| Next-round total income | `EconomyEngine::resolve_round` produces realized income after round resolution; it includes round base income, interest, streak income and accumulated PvP win gold | No trustworthy pre-combat expected total. Remains unavailable; no expected win/streak outcome is fabricated |
| Incoming damage | `CombatEngine::simulate` returns damage for a fully specified actual simulation | No calibrated future-opponent/future-round predictor in the decision path. Actual combat result is not mislabeled as expected damage |
| Elimination risk | No calibrated risk producer found | Remains unavailable; HP alone is not converted into a probability |
| Progression plan | No authoritative native producer in the integrated callsite | `Flexible` default remains unavailable, not a confirmed hypothesis |
| Reroll/shop opportunity value | No validated producer for future shop outcomes | No fixed BUY/XP/REROLL premiums; opportunity cost remains unavailable |

### 11.2 Implemented marginal contract

The candidate builder now compares each candidate with HOLD using the same native gold snapshot. It records gold before/after, interest before/after, signed interest delta, source, one-round horizon and zero uncertainty for the deterministic cash/interest calculation itself. This uncertainty does **not** claim that future board, shop, combat or income outcomes are certain.

The contextual evaluator revalidates the source, horizon, current gold, post-action gold and both interest values against `EconomyEngine::get_interest` before consuming the marginal fields. Direct spend/credit and lost interest are counted once. The baseline action evaluator and composition evaluator no longer add fixed action-family opportunity premiums. An unproduced opportunity value has no score contribution.

### 11.3 Contradictory evidence

`EconomicController` rejects out-of-domain or contradictory fields before posture scoring, including negative observed quantities, non-finite/negative damage, risk outside [0,1], negative streaks, and simultaneous positive win/loss streaks. `PlannerEvidenceAdapters` additionally rejects interest that does not match the current gold under `EconomyEngine::get_interest`. Invalid evidence is surfaced separately from missing evidence; it is not clamped into a plausible value.

### 11.4 Executable evidence in PR 2

- Exact buy/sell/HOLD gold and interest deltas, including interest breakpoints.
- Marginal evidence source, horizon and uncertainty metadata.
- Contextual evaluator rejects stale/mismatched marginal values and ignores arbitrary unproduced opportunity-cost numbers.
- Controller tests for contradictory streaks, out-of-range elimination risk, real zero values and incomplete projections.
- Adapter tests for gold/interest inconsistency and propagation of invalid evidence.

### 11.5 Remaining boundary

This PR does not invent expected next-round income, incoming damage, elimination risk, progression hypotheses or shop opportunity value. Those fields remain explicitly unavailable until an authoritative producer and horizon/calibration contract exist. Therefore #282 remains open for those producers and for replay validation of contradictory/incomplete scenarios. The current implementation completes exact same-snapshot marginal cash/interest accounting and prevents unsupported values from influencing the evaluator; it does not claim the missing predictive models are solved.
