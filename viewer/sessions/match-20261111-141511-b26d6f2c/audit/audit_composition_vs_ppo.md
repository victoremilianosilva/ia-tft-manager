# Composition Intelligence × PPO — comparação descritiva

- Snapshots válidos da Composition Intelligence: **1787**
- Revisões estratégicas únicas: **345**
- Decisões PPO encontradas na auditoria: **1093** (timeline estruturada)

As recomendações são contadas por snapshot; snapshots repetidos não são decisões independentes. As distribuições não representam correspondência ação-a-ação.

## Ações executadas pelo PPO

- BUY: 463
- BUY_XP: 43
- CRAFT_AND_EQUIP: 54
- EQUIP_FROM_INVENTORY: 28
- MOVE_BENCH: 119
- MOVE_BOARD: 102
- PASS: 49
- REROLL: 4
- SELL: 231

## Recomendações da Composition Intelligence

- BUY_UNIT: 127
- BUY_XP: 162
- DEPLOY_OR_MOVE: 185
- HOLD: 668
- NONE: 644
- SELL_UNIT: 1

## Interpretação

O PPO é a única fonte das ações executadas; recomendações shadow não são executadas.
Diferenças entre as distribuições não demonstram erro nem causalidade. Considere round, jogador, estado e evidência.

