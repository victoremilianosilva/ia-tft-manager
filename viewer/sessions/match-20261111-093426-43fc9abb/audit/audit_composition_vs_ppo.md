# Composition Intelligence × PPO — comparação descritiva

- Snapshots válidos da Composition Intelligence: **1968**
- Revisões estratégicas únicas: **339**
- Decisões PPO encontradas na auditoria: **1221** (timeline estruturada)

As recomendações são contadas por snapshot; snapshots repetidos não são decisões independentes. As distribuições não representam correspondência ação-a-ação.

## Ações executadas pelo PPO

- BUY: 491
- BUY_XP: 65
- CRAFT_AND_EQUIP: 52
- EQUIP_FROM_INVENTORY: 27
- MOVE_BENCH: 107
- MOVE_BOARD: 148
- PASS: 71
- REROLL: 7
- SELL: 253

## Recomendações da Composition Intelligence

- BUY_UNIT: 140
- BUY_XP: 209
- DEPLOY_OR_MOVE: 84
- HOLD: 480
- NONE: 1055

## Interpretação

O PPO é a única fonte das ações executadas; recomendações shadow não são executadas.
Diferenças entre as distribuições não demonstram erro nem causalidade. Considere round, jogador, estado e evidência.

