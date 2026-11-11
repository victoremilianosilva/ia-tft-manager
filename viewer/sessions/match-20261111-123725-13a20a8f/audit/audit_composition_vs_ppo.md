# Composition Intelligence × PPO — comparação descritiva

- Snapshots válidos da Composition Intelligence: **1743**
- Revisões estratégicas únicas: **328**
- Decisões PPO encontradas na auditoria: **1053** (timeline estruturada)

As recomendações são contadas por snapshot; snapshots repetidos não são decisões independentes. As distribuições não representam correspondência ação-a-ação.

## Ações executadas pelo PPO

- BUY: 436
- BUY_XP: 47
- CRAFT_AND_EQUIP: 52
- EQUIP_FROM_INVENTORY: 17
- MOVE_BENCH: 130
- MOVE_BOARD: 107
- PASS: 61
- REROLL: 3
- SELL: 200

## Recomendações da Composition Intelligence

- BUY_UNIT: 130
- BUY_XP: 156
- DEPLOY_OR_MOVE: 135
- HOLD: 614
- NONE: 708

## Interpretação

O PPO é a única fonte das ações executadas; recomendações shadow não são executadas.
Diferenças entre as distribuições não demonstram erro nem causalidade. Considere round, jogador, estado e evidência.

