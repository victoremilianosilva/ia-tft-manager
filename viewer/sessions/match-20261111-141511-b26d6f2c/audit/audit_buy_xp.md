# BUY_XP coverage audit

> Shadow/read-only diagnostic. No action, score, PPO behavior, or gameplay is changed.

- BUY_XP candidates: **831**
- Selected BUY_XP candidates: **17**
- Final BUY_XP recommendations: **17**
- Candidates with positive total score: **204**
- Economic posture context matched: **831**
- Economic posture context missing: **0**

## Candidate classification

| Classification | Candidates |
|---|---:|
| Non-positive candidate score | 627 |
| Positive score, outscored by another action | 187 |
| Selected recommendation | 17 |

## Candidate score components

| Component | N | Mean | Min | Max |
|---|---:|---:|---:|---:|
| Δ ouro direto | 831 | 4.0 | 4.0 | 4.0 |
| Juros perdidos | 831 | 0.1613 | 0.0 | 1.0 |
| Oportunidade | 831 | 0.25 | 0.25 | 0.25 |
| Board | 831 | 0.1471 | 0.12 | 0.36 |
| Sobrevivência | 831 | 0.02 | 0.0 | 0.207 |
| Streak | 831 | 0.0115 | 0.0 | 0.068 |
| Composição | 831 | 0.0 | 0.0 | 0.0 |
| Upgrade | 831 | 0.0203 | 0.014 | 0.07 |
| Score custo direto | 831 | -0.22 | -0.22 | -0.22 |
| Score juros | 831 | -0.0161 | -0.1 | -0.0 |
| Score oportunidade | 831 | -0.025 | -0.025 | -0.025 |
| Total | 831 | -0.0284 | -0.211 | 0.7 |

## Selected recommendations by round

| Round | Selected BUY_XP |
|---|---:|
| 2-6 | 3 |
| 3-4 | 1 |
| 3-7 | 5 |
| 4-3 | 2 |
| 4-6 | 5 |
| 4-7 | 1 |

## Candidate coverage by round

| Round | Candidates | Positive score | Selected | Mean total |
|---|---:|---:|---:|---:|
| 2-1 | 25 | 0 | 0 | -0.111 |
| 2-2 | 16 | 5 | 0 | -0.0185 |
| 2-3 | 24 | 11 | 0 | 0.0407 |
| 2-4 | 18 | 2 | 0 | -0.079 |
| 2-5 | 42 | 9 | 0 | -0.0725 |
| 2-6 | 43 | 6 | 3 | -0.0983 |
| 2-7 | 16 | 4 | 0 | -0.0666 |
| 3-1 | 47 | 0 | 0 | -0.1389 |
| 3-2 | 15 | 0 | 0 | -0.1667 |
| 3-3 | 45 | 12 | 0 | -0.0613 |
| 3-4 | 16 | 4 | 1 | -0.0465 |
| 3-5 | 48 | 1 | 0 | -0.1288 |
| 3-6 | 16 | 0 | 0 | -0.1069 |
| 3-7 | 40 | 10 | 5 | -0.0309 |
| 4-1 | 24 | 6 | 0 | -0.0575 |
| 4-2 | 40 | 15 | 0 | 0.0244 |
| 4-3 | 24 | 11 | 2 | 0.0567 |
| 4-4 | 40 | 10 | 0 | -0.0126 |
| 4-5 | 24 | 7 | 0 | -0.0001 |
| 4-6 | 35 | 5 | 5 | 0.0274 |
| 4-7 | 21 | 3 | 1 | 0.034 |
| 5-1 | 35 | 5 | 0 | -0.0344 |
| 5-2 | 21 | 9 | 0 | 0.0373 |
| 5-3 | 24 | 10 | 0 | 0.0467 |
| 5-4 | 24 | 20 | 0 | 0.162 |
| 5-5 | 24 | 16 | 0 | 0.1005 |
| 5-6 | 16 | 4 | 0 | -0.0 |
| 5-7 | 12 | 4 | 0 | 0.026 |
| 6-1 | 12 | 7 | 0 | 0.081 |
| 6-2 | 12 | 4 | 0 | 0.0323 |
| 6-3 | 8 | 0 | 0 | -0.062 |
| 6-4 | 8 | 0 | 0 | -0.0615 |
| 6-5 | 8 | 0 | 0 | -0.0615 |
| 6-6 | 8 | 4 | 0 | 0.0785 |

## Limitations

- Positive score is evidence that the evaluator valued the candidate, not proof that buying XP was strategically optimal.
- Positive-but-outscored means another candidate had a higher score at the same decision; it is not a missed-opportunity label.
- The available candidate table does not expose raw current gold, level, XP-to-next-level, shop odds, or the counterfactual board after leveling.
- Economic posture is joined by player/round/step when the optional economic audit is supplied; it does not fill missing raw state.
- No target frequency is imposed. This report does not change scores, recommendations, PPO actions, training, or gameplay.
