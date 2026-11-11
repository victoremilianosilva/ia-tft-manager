# HOLD baseline audit

> Shadow/read-only diagnostic. This report does not change the HOLD baseline or any gameplay behavior.

- HOLD candidates: **1085**
- Selected HOLD candidates: **151**
- Final HOLD recommendations: **159**
- Total score: **mean 0.106 / min 0.0 / max 0.24 / distinct values 2**
- Missing economic posture context: **0**

## Code-path review

- Baseline `strategy::ActionEvaluator`: HOLD receives a +0.24 posture component under `AccumulateResources`; the implementation does not add this bonus in the other posture branches.
- Independent `ContextualActionEvaluator`: HOLD total score is explicitly reset to 0.0 and retained as the fallback when no positive contextual candidate is selected.
- Therefore, the observed 0.240 is not a universal invariant across both evaluators. The report checks whether the reference session's constant value is explained by its observed economic-posture distribution.

## Score components

| Component | N | Mean | Min | Max | Distinct |
|---|---:|---:|---:|---:|---:|
| Score custo direto | 1085 | 0.0 | 0.0 | 0.0 | 1 |
| Score juros | 1085 | 0.0 | -0.0 | -0.0 | 1 |
| Score oportunidade | 1085 | 0.0 | -0.0 | -0.0 | 1 |
| Board | 1085 | 0.0 | 0.0 | 0.0 | 1 |
| Sobrevivência | 1085 | 0.0 | 0.0 | 0.0 | 1 |
| Streak | 1085 | 0.0 | 0.0 | 0.0 | 1 |
| Composição | 1085 | 0.0 | 0.0 | 0.0 | 1 |
| Upgrade | 1085 | 0.0 | 0.0 | 0.0 | 1 |
| Postura | 1085 | 0.106 | 0.0 | 0.24 | 2 |

## Economic posture

| Posture | Candidates | HOLD score mean | Min | Max | Distinct |
|---|---:|---:|---:|---:|---:|
| ACCUMULATE_RESOURCES | 479 | 0.24 | 0.24 | 0.24 | 1 |
| EMERGENCY_INVESTMENT | 87 | 0.0 | 0.0 | 0.0 | 1 |
| INVEST_EXPERIENCE | 13 | 0.0 | 0.0 | 0.0 | 1 |
| PRESERVE_LOSS_STREAK | 31 | 0.0 | 0.0 | 0.0 | 1 |
| PRESERVE_WIN_STREAK | 453 | 0.0 | 0.0 | 0.0 | 1 |
| STABILIZE_BOARD | 22 | 0.0 | 0.0 | 0.0 | 1 |

## Comparison against available alternatives

| Classification | Decisions |
|---|---:|
| HOLD score at or above best available alternative | 134 |
| HOLD score below best available alternative | 934 |
| No other available scored alternative | 17 |

Mean HOLD-minus-best-alternative margin when HOLD is lower: **-0.4602** (N=934).

## Interpretation boundaries

- The exported score is a heuristic ranking value, not a calibrated utility or probability.
- A candidate score of zero may still be selected as the explicit fallback when no positive alternative wins.
- The table does not establish whether holding was strategically optimal; that requires counterfactual state and outcome evidence.
- Economic posture is joined by player/round/step. Missing matches remain explicit and are not inferred.
- This audit does not modify HOLD scoring, recommendations, PPO, training, observations, masks, rewards, rules, or execution.
