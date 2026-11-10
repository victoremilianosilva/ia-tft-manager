# Outcome Evaluator — resultados observados

Esta auditoria mede mudanças observadas depois de cada ação e o estado final registrado. Não atribui causalidade exclusiva à ação ou à recomendação shadow.

> Recomendações em shadow mode são diagnósticos heurísticos. Elas não foram executadas nem alteraram a ação do PPO.

## Efeito imediato por decisão (sem repetir combate)

| Jogador | Round | Step | PPO executou | Action Evaluator recomendou | Campeão recomendado | Δ Ouro | Δ HP | Δ Board | Δ Nível | Δ XP | Δ pares | Δ 2★ board/bench | Δ 3★ board/bench | Δ win/loss streak | Composição antes → depois |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Jogador 1 | 1-1 | 1 | MOVE_BENCH | HOLD | -1 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 1-1 | 2 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 1-1 | 3 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 1-2 | 17 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 1-2 | 18 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 1-2 | 19 | MOVE_BENCH | HOLD | -1 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 1-2 | 20 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 1-2 | 21 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 1-2 | 22 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 1-2 | 25 | MOVE_BENCH | HOLD | -1 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 1-3 | 28 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 1-3 | 29 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 1-3 | 30 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 1-3 | 31 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 1-3 | 32 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 1-4 | 42 | BUY | BUY_UNIT | 6 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 1-4 | 43 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 1-4 | 44 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-1 | 55 | BUY | DEPLOY_OR_MOVE | 6 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-1 | 56 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-1 | 57 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-1 | 58 | BUY_XP | DEPLOY_OR_MOVE | 12 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-1 | 59 | PASS | DEPLOY_OR_MOVE | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-1 | 61 | MOVE_BENCH | DEPLOY_OR_MOVE | 12 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-2 | 64 | BUY | BUY_UNIT | 14 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-2 | 65 | SELL | BUY_UNIT | 25 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-2 | 66 | BUY_XP | BUY_UNIT | 25 | -4.000 | 0.000 | 0.000 | 1.000 | -6.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-2 | 67 | MOVE_BENCH | DEPLOY_OR_MOVE | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-2 | 68 | MOVE_BENCH | DEPLOY_OR_MOVE | 12 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-2 | 69 | MOVE_BOARD | SELL_UNIT | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-2 | 70 | SELL | SELL_UNIT | 29 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-3 | 72 | BUY | BUY_UNIT | 36 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-3 | 73 | BUY | BUY_UNIT | 10 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-3 | 74 | BUY_XP | SELL_UNIT | 23 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-3 | 75 | SELL | SELL_UNIT | 23 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-3 | 76 | BUY_XP | SELL_UNIT | 23 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-3 | 77 | MOVE_BOARD | SELL_UNIT | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-3 | 78 | MOVE_BOARD | SELL_UNIT | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-3 | 79 | PASS | SELL_UNIT | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-4 | 82 | BUY | BUY_UNIT | 6 | -1.000 | 0.000 | -2.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-4 | 83 | BUY_XP | DEPLOY_OR_MOVE | 6 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-4 | 84 | SELL | DEPLOY_OR_MOVE | 6 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-4 | 85 | BUY | DEPLOY_OR_MOVE | 23 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-4 | 86 | MOVE_BENCH | DEPLOY_OR_MOVE | 0 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-4 | 87 | MOVE_BOARD | SELL_UNIT | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-4 | 88 | PASS | SELL_UNIT | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 1 | 2-5 | 92 | BUY | BUY_UNIT | 23 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → Adaptador |
| Jogador 1 | 2-5 | 93 | BUY | BUY_UNIT | 18 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-5 | 94 | BUY_XP | BUY_XP | -1 | -4.000 | 0.000 | 0.000 | 1.000 | -16.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-5 | 95 | MOVE_BENCH | DEPLOY_OR_MOVE | 0 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-5 | 96 | SELL | DEPLOY_OR_MOVE | 0 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-5 | 97 | MOVE_BOARD | DEPLOY_OR_MOVE | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-5 | 98 | MOVE_BOARD | DEPLOY_OR_MOVE | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-5 | 99 | PASS | DEPLOY_OR_MOVE | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-6 | 102 | BUY | BUY_UNIT | 0 | -1.000 | 0.000 | -2.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-6 | 103 | BUY | DEPLOY_OR_MOVE | 0 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-6 | 104 | BUY | DEPLOY_OR_MOVE | 0 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-6 | 105 | MOVE_BENCH | DEPLOY_OR_MOVE | 0 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-6 | 106 | MOVE_BOARD | SELL_UNIT | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-6 | 107 | MOVE_BOARD | SELL_UNIT | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-6 | 108 | PASS | SELL_UNIT | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-7 | 112 | BUY | BUY_UNIT | 7 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-7 | 113 | BUY | BUY_UNIT | 7 | -1.000 | 0.000 | -4.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-7 | 114 | BUY | DEPLOY_OR_MOVE | 0 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-7 | 115 | MOVE_BENCH | DEPLOY_OR_MOVE | 0 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-7 | 116 | BUY | DEPLOY_OR_MOVE | 0 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-7 | 117 | SELL | DEPLOY_OR_MOVE | 0 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-7 | 118 | EQUIP_FROM_INVENTORY | DEPLOY_OR_MOVE | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-7 | 119 | EQUIP_FROM_INVENTORY | DEPLOY_OR_MOVE | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 2-7 | 120 | BUY_XP | DEPLOY_OR_MOVE | 0 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-1 | 122 | BUY | DEPLOY_OR_MOVE | 0 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-1 | 123 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-1 | 124 | BUY | DEPLOY_OR_MOVE | 0 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-1 | 125 | BUY_XP | DEPLOY_OR_MOVE | 0 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-1 | 126 | SELL | DEPLOY_OR_MOVE | 0 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-1 | 127 | BUY | DEPLOY_OR_MOVE | 18 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-1 | 128 | PASS | DEPLOY_OR_MOVE | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-2 | 132 | BUY | BUY_UNIT | 2 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-2 | 133 | BUY | BUY_UNIT | 35 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-2 | 134 | BUY_XP | SELL_UNIT | 28 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-2 | 135 | MOVE_BOARD | SELL_UNIT | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-2 | 136 | MOVE_BOARD | SELL_UNIT | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-2 | 137 | PASS | SELL_UNIT | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-3 | 142 | BUY | SELL_UNIT | 28 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-3 | 143 | BUY_XP | SELL_UNIT | 28 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-3 | 144 | BUY_XP | SELL_UNIT | 28 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-3 | 145 | MOVE_BOARD | SELL_UNIT | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-3 | 146 | MOVE_BOARD | SELL_UNIT | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-3 | 147 | SELL | SELL_UNIT | 28 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-3 | 148 | BUY | SELL_UNIT | 28 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-3 | 149 | MOVE_BOARD | SELL_UNIT | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-3 | 150 | MOVE_BOARD | SELL_UNIT | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-4 | 152 | SELL | BUY_UNIT | 9 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-4 | 153 | BUY | BUY_UNIT | 9 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-4 | 154 | BUY_XP | SELL_UNIT | 27 | -4.000 | 0.000 | 0.000 | 1.000 | -32.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-4 | 155 | BUY_XP | DEPLOY_OR_MOVE | 18 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-4 | 156 | SELL | DEPLOY_OR_MOVE | 18 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-4 | 157 | BUY | DEPLOY_OR_MOVE | 18 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-4 | 158 | SELL | DEPLOY_OR_MOVE | 18 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-4 | 159 | BUY_XP | DEPLOY_OR_MOVE | 18 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-4 | 160 | MOVE_BOARD | DEPLOY_OR_MOVE | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-5 | 162 | BUY | DEPLOY_OR_MOVE | 18 | -2.000 | 0.000 | -8.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-5 | 163 | MOVE_BENCH | DEPLOY_OR_MOVE | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-5 | 164 | MOVE_BENCH | DEPLOY_OR_MOVE | 18 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-5 | 165 | BUY_XP | DEPLOY_OR_MOVE | 18 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-5 | 166 | MOVE_BENCH | DEPLOY_OR_MOVE | 18 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-5 | 167 | MOVE_BOARD | DEPLOY_OR_MOVE | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-5 | 168 | BUY | DEPLOY_OR_MOVE | 18 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-5 | 169 | MOVE_BOARD | DEPLOY_OR_MOVE | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-5 | 170 | MOVE_BOARD | DEPLOY_OR_MOVE | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-6 | 172 | BUY | BUY_UNIT | 23 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-6 | 173 | BUY | BUY_UNIT | 23 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-6 | 174 | MOVE_BOARD | BUY_UNIT | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-6 | 175 | MOVE_BOARD | BUY_UNIT | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-6 | 176 | MOVE_BOARD | BUY_UNIT | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-6 | 177 | PASS | BUY_UNIT | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-7 | 182 | SELL | BUY_UNIT | 33 | 5.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-7 | 183 | BUY | BUY_UNIT | 33 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-7 | 184 | MOVE_BOARD | BUY_UNIT | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-7 | 185 | MOVE_BOARD | BUY_UNIT | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 3-7 | 186 | PASS | BUY_UNIT | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-1 | 192 | CRAFT_AND_EQUIP | SELL_UNIT | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-1 | 193 | CRAFT_AND_EQUIP | SELL_UNIT | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-1 | 194 | SELL | SELL_UNIT | 27 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-1 | 195 | BUY | BUY_UNIT | 27 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-1 | 196 | MOVE_BOARD | SELL_UNIT | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-1 | 197 | MOVE_BOARD | SELL_UNIT | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-1 | 198 | MOVE_BOARD | SELL_UNIT | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-1 | 199 | MOVE_BOARD | SELL_UNIT | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-1 | 200 | MOVE_BOARD | SELL_UNIT | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-2 | 202 | SELL | BUY_UNIT | 35 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-2 | 203 | BUY | BUY_UNIT | 35 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-2 | 204 | SELL | BUY_UNIT | 0 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-2 | 205 | BUY | BUY_UNIT | 0 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-2 | 206 | MOVE_BOARD | SELL_UNIT | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-2 | 207 | MOVE_BOARD | SELL_UNIT | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-2 | 208 | MOVE_BOARD | SELL_UNIT | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-2 | 209 | MOVE_BOARD | SELL_UNIT | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-2 | 210 | PASS | SELL_UNIT | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-3 | 212 | SELL | BUY_UNIT | 2 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-3 | 213 | BUY | BUY_UNIT | 2 | -1.000 | 0.000 | -2.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-3 | 214 | BUY | DEPLOY_OR_MOVE | 33 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-3 | 215 | SELL | DEPLOY_OR_MOVE | 36 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-3 | 216 | BUY | DEPLOY_OR_MOVE | 36 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-3 | 217 | SELL | DEPLOY_OR_MOVE | 36 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-3 | 218 | BUY_XP | DEPLOY_OR_MOVE | 36 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-3 | 219 | MOVE_BOARD | DEPLOY_OR_MOVE | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-3 | 220 | MOVE_BENCH | DEPLOY_OR_MOVE | 36 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-4 | 222 | BUY | SELL_UNIT | 51 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-4 | 223 | BUY | SELL_UNIT | 51 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-4 | 224 | MOVE_BOARD | SELL_UNIT | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-4 | 225 | MOVE_BOARD | SELL_UNIT | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-4 | 226 | MOVE_BOARD | SELL_UNIT | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-4 | 227 | PASS | SELL_UNIT | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-5 | 232 | SELL | SELL_UNIT | 51 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-5 | 233 | BUY | SELL_UNIT | 51 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-5 | 234 | SELL | SELL_UNIT | 51 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-5 | 235 | BUY | SELL_UNIT | 51 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-5 | 236 | MOVE_BOARD | SELL_UNIT | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-5 | 237 | MOVE_BOARD | SELL_UNIT | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-5 | 238 | MOVE_BOARD | SELL_UNIT | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-5 | 239 | MOVE_BOARD | SELL_UNIT | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-5 | 240 | PASS | SELL_UNIT | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-6 | 242 | SELL | BUY_UNIT | 18 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-6 | 243 | BUY | BUY_UNIT | 18 | -2.000 | 0.000 | -4.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-6 | 244 | BUY | DEPLOY_OR_MOVE | 18 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-6 | 245 | BUY | DEPLOY_OR_MOVE | 18 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-6 | 246 | BUY_XP | DEPLOY_OR_MOVE | 18 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-6 | 247 | BUY_XP | DEPLOY_OR_MOVE | 18 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-6 | 248 | BUY_XP | DEPLOY_OR_MOVE | 18 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-6 | 249 | BUY_XP | DEPLOY_OR_MOVE | 18 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-6 | 250 | BUY_XP | DEPLOY_OR_MOVE | 18 | -4.000 | 0.000 | 0.000 | 1.000 | -52.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-7 | 252 | BUY | DEPLOY_OR_MOVE | 18 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-7 | 253 | BUY_XP | DEPLOY_OR_MOVE | 18 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-7 | 254 | BUY_XP | DEPLOY_OR_MOVE | 18 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-7 | 255 | BUY_XP | DEPLOY_OR_MOVE | 18 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-7 | 256 | BUY_XP | DEPLOY_OR_MOVE | 18 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-7 | 257 | BUY_XP | DEPLOY_OR_MOVE | 18 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-7 | 258 | BUY_XP | DEPLOY_OR_MOVE | 18 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-7 | 259 | BUY_XP | DEPLOY_OR_MOVE | 18 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 4-7 | 260 | BUY_XP | DEPLOY_OR_MOVE | 18 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-1 | 262 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-1 | 263 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-1 | 264 | SELL | DEPLOY_OR_MOVE | 18 | 5.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-1 | 265 | BUY | BUY_UNIT | 33 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-1 | 266 | SELL | BUY_UNIT | 33 | 8.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-1 | 267 | BUY | DEPLOY_OR_MOVE | 51 | -3.000 | 0.000 | -6.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-1 | 268 | BUY | DEPLOY_OR_MOVE | 51 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-1 | 269 | MOVE_BENCH | DEPLOY_OR_MOVE | 34 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-1 | 270 | BUY_XP | DEPLOY_OR_MOVE | 34 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-2 | 272 | BUY | DEPLOY_OR_MOVE | 34 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-2 | 273 | MOVE_BENCH | DEPLOY_OR_MOVE | 34 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-2 | 274 | BUY | DEPLOY_OR_MOVE | 34 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-2 | 275 | MOVE_BOARD | DEPLOY_OR_MOVE | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-2 | 276 | MOVE_BOARD | DEPLOY_OR_MOVE | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-2 | 277 | PASS | DEPLOY_OR_MOVE | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-2 | 280 | MOVE_BENCH | DEPLOY_OR_MOVE | 51 | 0.000 | 0.000 | 8.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-3 | 282 | BUY | BUY_UNIT | 36 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-3 | 283 | SELL | BUY_UNIT | 36 | 8.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-3 | 284 | BUY | BUY_UNIT | 36 | -3.000 | 0.000 | -12.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-3 | 285 | MOVE_BENCH | DEPLOY_OR_MOVE | 34 | 0.000 | 0.000 | 8.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-3 | 286 | EQUIP_FROM_INVENTORY | DEPLOY_OR_MOVE | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-3 | 287 | EQUIP_FROM_INVENTORY | DEPLOY_OR_MOVE | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-3 | 288 | EQUIP_FROM_INVENTORY | DEPLOY_OR_MOVE | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-3 | 289 | BUY | DEPLOY_OR_MOVE | 34 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-3 | 290 | BUY_XP | DEPLOY_OR_MOVE | 34 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-4 | 292 | SELL | DEPLOY_OR_MOVE | 34 | 8.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-4 | 293 | BUY | DEPLOY_OR_MOVE | 34 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-4 | 294 | EQUIP_FROM_INVENTORY | DEPLOY_OR_MOVE | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-4 | 295 | EQUIP_FROM_INVENTORY | DEPLOY_OR_MOVE | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-4 | 296 | MOVE_BOARD | DEPLOY_OR_MOVE | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-4 | 297 | BUY_XP | DEPLOY_OR_MOVE | 34 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-4 | 298 | BUY_XP | DEPLOY_OR_MOVE | 34 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-4 | 299 | BUY_XP | DEPLOY_OR_MOVE | 34 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-4 | 300 | MOVE_BENCH | DEPLOY_OR_MOVE | 34 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-5 | 302 | BUY | SELL_UNIT | 42 | -5.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-5 | 303 | MOVE_BOARD | SELL_UNIT | 62 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-5 | 304 | MOVE_BOARD | SELL_UNIT | 62 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-5 | 305 | MOVE_BOARD | SELL_UNIT | 62 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-5 | 306 | PASS | SELL_UNIT | 62 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-6 | 312 | MOVE_BOARD | BUY_UNIT | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-6 | 313 | MOVE_BOARD | BUY_UNIT | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-6 | 314 | PASS | BUY_UNIT | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-7 | 322 | MOVE_BOARD | DEPLOY_OR_MOVE | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-7 | 323 | MOVE_BOARD | DEPLOY_OR_MOVE | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-7 | 324 | MOVE_BOARD | DEPLOY_OR_MOVE | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 5-7 | 325 | PASS | DEPLOY_OR_MOVE | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-1 | 332 | BUY | BUY_UNIT | 49 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-1 | 333 | BUY | BUY_UNIT | 14 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-1 | 334 | EQUIP_FROM_INVENTORY | BUY_UNIT | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-1 | 335 | BUY | BUY_UNIT | 50 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-1 | 336 | MOVE_BOARD | BUY_UNIT | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-1 | 337 | MOVE_BOARD | BUY_UNIT | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-1 | 338 | MOVE_BOARD | BUY_UNIT | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-1 | 339 | PASS | BUY_UNIT | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-2 | 342 | SELL | BUY_UNIT | 0 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-2 | 343 | BUY | BUY_UNIT | 0 | -1.000 | 0.000 | -4.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-2 | 344 | EQUIP_FROM_INVENTORY | DEPLOY_OR_MOVE | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-2 | 345 | BUY_XP | DEPLOY_OR_MOVE | 50 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-2 | 346 | BUY_XP | DEPLOY_OR_MOVE | 50 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-2 | 347 | BUY_XP | DEPLOY_OR_MOVE | 50 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-2 | 348 | BUY_XP | DEPLOY_OR_MOVE | 50 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-2 | 349 | BUY_XP | DEPLOY_OR_MOVE | 50 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-2 | 350 | BUY_XP | DEPLOY_OR_MOVE | 50 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-3 | 352 | BUY_XP | DEPLOY_OR_MOVE | 50 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-3 | 353 | BUY_XP | DEPLOY_OR_MOVE | 50 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-3 | 354 | BUY_XP | DEPLOY_OR_MOVE | 50 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-3 | 355 | BUY_XP | DEPLOY_OR_MOVE | 50 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-3 | 356 | BUY_XP | DEPLOY_OR_MOVE | 50 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-3 | 357 | BUY_XP | DEPLOY_OR_MOVE | 50 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-3 | 358 | BUY_XP | DEPLOY_OR_MOVE | 50 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-3 | 359 | BUY_XP | DEPLOY_OR_MOVE | 50 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-3 | 360 | BUY_XP | DEPLOY_OR_MOVE | 50 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-4 | 362 | PASS | DEPLOY_OR_MOVE | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-5 | 372 | BUY | DEPLOY_OR_MOVE | 50 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-5 | 373 | MOVE_BOARD | DEPLOY_OR_MOVE | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-5 | 374 | MOVE_BOARD | DEPLOY_OR_MOVE | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-5 | 375 | MOVE_BOARD | DEPLOY_OR_MOVE | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-5 | 376 | PASS | DEPLOY_OR_MOVE | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-5 | 380 | MOVE_BENCH | DEPLOY_OR_MOVE | 50 | 0.000 | 0.000 | 8.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-6 | 382 | BUY | DEPLOY_OR_MOVE | 50 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-6 | 383 | MOVE_BOARD | DEPLOY_OR_MOVE | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-6 | 384 | MOVE_BOARD | DEPLOY_OR_MOVE | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 1 | 6-6 | 385 | PASS | DEPLOY_OR_MOVE | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Adaptador → Adaptador |
| Jogador 2 | 1-1 | 1 | MOVE_BENCH | HOLD | -1 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 1-1 | 2 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 1-1 | 3 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 1-2 | 17 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 1-2 | 18 | BUY | DEPLOY_OR_MOVE | 11 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 1-2 | 19 | MOVE_BENCH | DEPLOY_OR_MOVE | 11 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 1-2 | 20 | PASS | DEPLOY_OR_MOVE | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 1-2 | 25 | MOVE_BENCH | DEPLOY_OR_MOVE | 11 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 1-3 | 28 | BUY | BUY_UNIT | 11 | -1.000 | 0.000 | -4.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 1-3 | 29 | BUY | DEPLOY_OR_MOVE | 11 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 1-3 | 30 | PASS | DEPLOY_OR_MOVE | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 1-3 | 39 | MOVE_BENCH | DEPLOY_OR_MOVE | 11 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 1.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 1-4 | 42 | BUY | BUY_UNIT | 11 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 1-4 | 43 | BUY | BUY_UNIT | 11 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 1-4 | 44 | BUY | DEPLOY_OR_MOVE | 11 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 1-4 | 45 | MOVE_BENCH | DEPLOY_OR_MOVE | 11 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 1-4 | 46 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 1-4 | 47 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 1-4 | 48 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-1 | 55 | BUY | DEPLOY_OR_MOVE | 11 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-1 | 56 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-1 | 57 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-1 | 58 | BUY | DEPLOY_OR_MOVE | 11 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-1 | 59 | SELL | DEPLOY_OR_MOVE | 11 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-1 | 60 | MOVE_BENCH | DEPLOY_OR_MOVE | 11 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-1 | 61 | BUY | SELL_UNIT | 40 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-1 | 62 | MOVE_BOARD | SELL_UNIT | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-2 | 64 | BUY | BUY_UNIT | 11 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-2 | 65 | BUY | SELL_UNIT | 40 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-2 | 66 | BUY | SELL_UNIT | 40 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-2 | 67 | MOVE_BOARD | SELL_UNIT | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-2 | 68 | SELL | SELL_UNIT | 40 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-2 | 69 | BUY_XP | SELL_UNIT | 40 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-2 | 70 | MOVE_BOARD | SELL_UNIT | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-3 | 72 | BUY | SELL_UNIT | 40 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-3 | 73 | BUY_XP | SELL_UNIT | 40 | -4.000 | 0.000 | 0.000 | 1.000 | -6.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-3 | 74 | PASS | DEPLOY_OR_MOVE | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-4 | 82 | BUY | BUY_UNIT | 12 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-4 | 83 | BUY | SELL_UNIT | 40 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-4 | 84 | MOVE_BOARD | SELL_UNIT | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-4 | 85 | SELL | SELL_UNIT | 40 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-4 | 86 | BUY | SELL_UNIT | 40 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-4 | 87 | SELL | SELL_UNIT | 32 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-4 | 88 | BUY | SELL_UNIT | 32 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-4 | 89 | MOVE_BENCH | SELL_UNIT | 32 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-4 | 90 | MOVE_BOARD | SELL_UNIT | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 2 | 2-5 | 92 | BUY | SELL_UNIT | 40 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → Feérico |
| Jogador 2 | 2-5 | 93 | BUY_XP | SELL_UNIT | 40 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-5 | 94 | SELL | SELL_UNIT | 40 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-5 | 95 | BUY | SELL_UNIT | 40 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-5 | 96 | SELL | SELL_UNIT | 40 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-5 | 97 | BUY | SELL_UNIT | 40 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-5 | 98 | SELL | SELL_UNIT | 40 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-5 | 99 | SELL | SELL_UNIT | 40 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-5 | 100 | BUY_XP | SELL_UNIT | 30 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-6 | 102 | BUY | SELL_UNIT | 30 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-6 | 103 | BUY_XP | SELL_UNIT | 33 | -4.000 | 0.000 | 0.000 | 1.000 | -16.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-6 | 104 | MOVE_BENCH | DEPLOY_OR_MOVE | 39 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-6 | 105 | MOVE_BOARD | SELL_UNIT | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-6 | 106 | MOVE_BOARD | SELL_UNIT | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-6 | 107 | PASS | SELL_UNIT | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-7 | 112 | BUY | SELL_UNIT | 33 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-7 | 113 | BUY | SELL_UNIT | 33 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-7 | 114 | SELL | SELL_UNIT | 33 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-7 | 115 | BUY | SELL_UNIT | 33 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-7 | 116 | SELL | SELL_UNIT | 33 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-7 | 117 | BUY | SELL_UNIT | 33 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-7 | 118 | SELL | SELL_UNIT | 33 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-7 | 119 | MOVE_BENCH | SELL_UNIT | 33 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 2-7 | 120 | MOVE_BOARD | SELL_UNIT | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-1 | 122 | BUY | SELL_UNIT | 33 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-1 | 123 | BUY | SELL_UNIT | 33 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-1 | 124 | CRAFT_AND_EQUIP | SELL_UNIT | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-1 | 125 | BUY_XP | SELL_UNIT | 33 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-1 | 126 | SELL | SELL_UNIT | 33 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-1 | 127 | BUY | SELL_UNIT | 33 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-1 | 128 | SELL | SELL_UNIT | 33 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-1 | 129 | SELL | SELL_UNIT | 33 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-1 | 130 | BUY_XP | SELL_UNIT | 37 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-2 | 132 | BUY | BUY_UNIT | 12 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-2 | 133 | BUY | BUY_UNIT | 13 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-2 | 134 | BUY_XP | SELL_UNIT | 37 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-2 | 135 | BUY_XP | SELL_UNIT | 37 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-2 | 136 | SELL | SELL_UNIT | 37 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-2 | 137 | BUY | SELL_UNIT | 37 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-2 | 138 | SELL | SELL_UNIT | 37 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-2 | 139 | BUY | SELL_UNIT | 37 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-2 | 140 | SELL | SELL_UNIT | 37 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-3 | 142 | BUY | BUY_UNIT | 39 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-3 | 143 | BUY | SELL_UNIT | 37 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-3 | 144 | SELL | SELL_UNIT | 49 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-3 | 145 | BUY | SELL_UNIT | 37 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-3 | 146 | SELL | SELL_UNIT | 28 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-3 | 147 | BUY_XP | SELL_UNIT | 37 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-3 | 148 | SELL | SELL_UNIT | 37 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-3 | 149 | SELL | SELL_UNIT | 30 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-3 | 150 | MOVE_BOARD | SELL_UNIT | 32 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-4 | 152 | BUY | SELL_UNIT | 32 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-4 | 153 | BUY | SELL_UNIT | 23 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-4 | 154 | MOVE_BOARD | BUY_UNIT | 25 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-4 | 155 | SELL | BUY_UNIT | 25 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-4 | 156 | BUY | BUY_UNIT | 25 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-4 | 157 | MOVE_BOARD | SELL_UNIT | 32 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-4 | 158 | MOVE_BOARD | SELL_UNIT | 32 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-4 | 159 | MOVE_BOARD | SELL_UNIT | 32 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-4 | 160 | PASS | SELL_UNIT | 32 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-5 | 162 | BUY | BUY_UNIT | 24 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-5 | 163 | BUY | BUY_UNIT | 24 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-5 | 164 | BUY | SELL_UNIT | 37 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-5 | 165 | MOVE_BOARD | SELL_UNIT | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-5 | 166 | MOVE_BOARD | SELL_UNIT | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-5 | 167 | PASS | SELL_UNIT | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-6 | 172 | SELL | BUY_UNIT | 11 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-6 | 173 | BUY | BUY_UNIT | 11 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-6 | 174 | SELL | BUY_UNIT | 22 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-6 | 175 | BUY | BUY_UNIT | 22 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-6 | 176 | MOVE_BOARD | BUY_UNIT | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-6 | 177 | SELL | BUY_UNIT | 22 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-6 | 178 | BUY | BUY_UNIT | 22 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-6 | 179 | MOVE_BOARD | BUY_UNIT | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-6 | 180 | MOVE_BOARD | BUY_UNIT | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-7 | 182 | SELL | BUY_UNIT | 39 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-7 | 183 | BUY | BUY_UNIT | 39 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-7 | 184 | SELL | BUY_UNIT | 39 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-7 | 185 | BUY | BUY_UNIT | 39 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-7 | 186 | BUY | DEPLOY_OR_MOVE | 39 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-7 | 187 | SELL | DEPLOY_OR_MOVE | 39 | 8.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-7 | 188 | SELL | DEPLOY_OR_MOVE | 46 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-7 | 189 | BUY | DEPLOY_OR_MOVE | 46 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 3-7 | 190 | BUY_XP | DEPLOY_OR_MOVE | 46 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-1 | 192 | BUY | DEPLOY_OR_MOVE | 46 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-1 | 193 | BUY | DEPLOY_OR_MOVE | 46 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-1 | 194 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-1 | 195 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-1 | 196 | SELL | DEPLOY_OR_MOVE | 46 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-1 | 197 | BUY | DEPLOY_OR_MOVE | 46 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-1 | 198 | BUY_XP | DEPLOY_OR_MOVE | 46 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-1 | 199 | BUY_XP | DEPLOY_OR_MOVE | 46 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-1 | 200 | MOVE_BENCH | DEPLOY_OR_MOVE | 46 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-2 | 202 | BUY | BUY_UNIT | 34 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-2 | 203 | BUY | SELL_UNIT | 45 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-2 | 204 | BUY | SELL_UNIT | 45 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-2 | 205 | MOVE_BOARD | SELL_UNIT | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-2 | 206 | MOVE_BOARD | SELL_UNIT | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-2 | 207 | PASS | SELL_UNIT | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-3 | 212 | SELL | SELL_UNIT | 45 | 8.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-3 | 213 | BUY | BUY_UNIT | 39 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-3 | 214 | SELL | SELL_UNIT | 45 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-3 | 215 | BUY | SELL_UNIT | 45 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-3 | 216 | MOVE_BOARD | SELL_UNIT | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-3 | 217 | SELL | SELL_UNIT | 45 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-3 | 218 | BUY | SELL_UNIT | 45 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-3 | 219 | MOVE_BOARD | SELL_UNIT | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-3 | 220 | MOVE_BOARD | SELL_UNIT | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-4 | 222 | SELL | SELL_UNIT | 45 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-4 | 223 | BUY | SELL_UNIT | 45 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-4 | 224 | SELL | SELL_UNIT | 45 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-4 | 225 | BUY | SELL_UNIT | 45 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-4 | 226 | SELL | SELL_UNIT | 45 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-4 | 227 | BUY | SELL_UNIT | 45 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-4 | 228 | SELL | SELL_UNIT | 45 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-4 | 229 | BUY | SELL_UNIT | 45 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-4 | 230 | MOVE_BOARD | SELL_UNIT | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-5 | 232 | SELL | BUY_UNIT | 39 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-5 | 233 | BUY | BUY_UNIT | 39 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-5 | 234 | SELL | SELL_UNIT | 45 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-5 | 235 | BUY | SELL_UNIT | 27 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-5 | 236 | SELL | SELL_UNIT | 37 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-5 | 237 | BUY | SELL_UNIT | 37 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-5 | 238 | MOVE_BOARD | SELL_UNIT | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-5 | 239 | MOVE_BOARD | SELL_UNIT | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-5 | 240 | PASS | SELL_UNIT | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-6 | 242 | SELL | BUY_UNIT | 7 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-6 | 243 | BUY | BUY_UNIT | 7 | -1.000 | 0.000 | -4.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-6 | 244 | SELL | BUY_UNIT | 11 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-6 | 245 | BUY | BUY_UNIT | 11 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-6 | 246 | MOVE_BENCH | DEPLOY_OR_MOVE | 39 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-6 | 247 | EQUIP_FROM_INVENTORY | DEPLOY_OR_MOVE | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-6 | 248 | EQUIP_FROM_INVENTORY | DEPLOY_OR_MOVE | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-6 | 249 | BUY | DEPLOY_OR_MOVE | 27 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-6 | 250 | MOVE_BOARD | DEPLOY_OR_MOVE | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-7 | 252 | SELL | DEPLOY_OR_MOVE | 39 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-7 | 253 | BUY | DEPLOY_OR_MOVE | 39 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-7 | 254 | SELL | DEPLOY_OR_MOVE | 39 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-7 | 255 | BUY | DEPLOY_OR_MOVE | 39 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-7 | 256 | SELL | DEPLOY_OR_MOVE | 39 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-7 | 257 | BUY | DEPLOY_OR_MOVE | 39 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-7 | 258 | SELL | DEPLOY_OR_MOVE | 46 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-7 | 259 | BUY | DEPLOY_OR_MOVE | 39 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 4-7 | 260 | BUY_XP | DEPLOY_OR_MOVE | 39 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-1 | 262 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-1 | 263 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-1 | 264 | SELL | DEPLOY_OR_MOVE | 39 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-1 | 265 | BUY | DEPLOY_OR_MOVE | 39 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-1 | 266 | MOVE_BENCH | DEPLOY_OR_MOVE | 39 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-1 | 267 | BUY | SELL_UNIT | 37 | -5.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-1 | 268 | SELL | SELL_UNIT | 71 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-1 | 269 | BUY | SELL_UNIT | 71 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-1 | 270 | SELL | SELL_UNIT | 71 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-2 | 272 | BUY | SELL_UNIT | 71 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-2 | 273 | SELL | SELL_UNIT | 71 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-2 | 274 | BUY | SELL_UNIT | 71 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-2 | 275 | SELL | SELL_UNIT | 71 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-2 | 276 | BUY | SELL_UNIT | 71 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-2 | 277 | SELL | SELL_UNIT | 71 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-2 | 278 | BUY | SELL_UNIT | 71 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-2 | 279 | SELL | SELL_UNIT | 71 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-2 | 280 | BUY | SELL_UNIT | 71 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-3 | 282 | SELL | BUY_UNIT | 27 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-3 | 283 | BUY | BUY_UNIT | 27 | -3.000 | 0.000 | -6.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-3 | 284 | BUY | DEPLOY_OR_MOVE | 46 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-3 | 285 | MOVE_BENCH | DEPLOY_OR_MOVE | 46 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-3 | 286 | SELL | DEPLOY_OR_MOVE | 46 | 8.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-3 | 287 | BUY | DEPLOY_OR_MOVE | 46 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-3 | 288 | BUY_XP | DEPLOY_OR_MOVE | 46 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-3 | 289 | BUY_XP | DEPLOY_OR_MOVE | 46 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-3 | 290 | BUY_XP | DEPLOY_OR_MOVE | 46 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-4 | 292 | SELL | DEPLOY_OR_MOVE | 46 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-4 | 293 | BUY | DEPLOY_OR_MOVE | 46 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-4 | 294 | SELL | DEPLOY_OR_MOVE | 46 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-4 | 295 | BUY | DEPLOY_OR_MOVE | 46 | -1.000 | 0.000 | -2.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-4 | 296 | MOVE_BENCH | DEPLOY_OR_MOVE | 46 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-4 | 297 | BUY | DEPLOY_OR_MOVE | 46 | -5.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-4 | 298 | MOVE_BOARD | DEPLOY_OR_MOVE | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-4 | 299 | BUY_XP | DEPLOY_OR_MOVE | 39 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-4 | 300 | MOVE_BENCH | DEPLOY_OR_MOVE | 39 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-5 | 302 | BUY | DEPLOY_OR_MOVE | 39 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-5 | 303 | BUY | DEPLOY_OR_MOVE | 39 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-5 | 304 | MOVE_BENCH | DEPLOY_OR_MOVE | 39 | 0.000 | 0.000 | 10.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-5 | 305 | BUY | SELL_UNIT | 54 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-5 | 306 | MOVE_BOARD | BUY_UNIT | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-5 | 307 | MOVE_BOARD | BUY_UNIT | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-5 | 308 | MOVE_BOARD | BUY_UNIT | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-5 | 309 | PASS | BUY_UNIT | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-6 | 312 | SELL | BUY_UNIT | 41 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-6 | 313 | BUY | BUY_UNIT | 41 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-6 | 314 | EQUIP_FROM_INVENTORY | BUY_UNIT | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-6 | 315 | EQUIP_FROM_INVENTORY | BUY_UNIT | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-6 | 316 | MOVE_BOARD | BUY_UNIT | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-6 | 317 | MOVE_BOARD | BUY_UNIT | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-6 | 318 | MOVE_BOARD | BUY_UNIT | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-6 | 319 | PASS | BUY_UNIT | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-7 | 322 | SELL | BUY_UNIT | 37 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-7 | 323 | BUY | BUY_UNIT | 37 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-7 | 324 | SELL | BUY_UNIT | 33 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-7 | 325 | BUY | SELL_UNIT | 47 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-7 | 326 | MOVE_BOARD | SELL_UNIT | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-7 | 327 | SELL | SELL_UNIT | 47 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-7 | 328 | BUY | SELL_UNIT | 47 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-7 | 329 | MOVE_BOARD | SELL_UNIT | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 5-7 | 330 | MOVE_BOARD | SELL_UNIT | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-1 | 332 | EQUIP_FROM_INVENTORY | SELL_UNIT | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-1 | 333 | SELL | SELL_UNIT | 47 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-1 | 334 | BUY | SELL_UNIT | 47 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-1 | 335 | SELL | SELL_UNIT | 47 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-1 | 336 | BUY | SELL_UNIT | 47 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-1 | 337 | SELL | SELL_UNIT | 47 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-1 | 338 | BUY | SELL_UNIT | 47 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-1 | 339 | MOVE_BOARD | SELL_UNIT | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-1 | 340 | MOVE_BOARD | SELL_UNIT | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-2 | 342 | SELL | BUY_UNIT | 25 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-2 | 343 | BUY | BUY_UNIT | 25 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-2 | 344 | SELL | BUY_UNIT | 20 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-2 | 345 | BUY | BUY_UNIT | 20 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-2 | 346 | SELL | BUY_UNIT | 20 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-2 | 347 | BUY | BUY_UNIT | 20 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-2 | 348 | SELL | SELL_UNIT | 47 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-2 | 349 | BUY | BUY_UNIT | 20 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-2 | 350 | SELL | BUY_UNIT | 20 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-3 | 352 | BUY | BUY_UNIT | 27 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-3 | 353 | SELL | BUY_UNIT | 41 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-3 | 354 | BUY | BUY_UNIT | 41 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-3 | 355 | SELL | BUY_UNIT | 41 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-3 | 356 | BUY | BUY_UNIT | 41 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-3 | 357 | SELL | SELL_UNIT | 41 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-3 | 358 | BUY | HOLD | -1 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-3 | 359 | SELL | SELL_UNIT | 15 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-3 | 360 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-4 | 362 | SELL | BUY_UNIT | 27 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-4 | 363 | BUY | BUY_UNIT | 27 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-4 | 364 | BUY | BUY_UNIT | 53 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-4 | 365 | BUY | BUY_UNIT | 53 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-4 | 366 | SELL | BUY_UNIT | 43 | 8.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-4 | 367 | BUY | BUY_UNIT | 43 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-4 | 368 | BUY_XP | SELL_UNIT | 43 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-4 | 369 | BUY_XP | SELL_UNIT | 43 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-4 | 370 | BUY_XP | SELL_UNIT | 43 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-5 | 372 | SELL | BUY_UNIT | 32 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-5 | 373 | BUY | BUY_UNIT | 32 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-5 | 374 | SELL | BUY_UNIT | 32 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-5 | 375 | BUY | BUY_UNIT | 32 | -3.000 | 0.000 | -12.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-5 | 376 | MOVE_BENCH | DEPLOY_OR_MOVE | 46 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-5 | 377 | BUY | DEPLOY_OR_MOVE | 46 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-5 | 378 | SELL | DEPLOY_OR_MOVE | 46 | 8.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-5 | 379 | BUY | DEPLOY_OR_MOVE | 46 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-5 | 380 | MOVE_BENCH | DEPLOY_OR_MOVE | 46 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-6 | 382 | BUY | BUY_UNIT | 53 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-6 | 383 | EQUIP_FROM_INVENTORY | BUY_UNIT | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-6 | 384 | EQUIP_FROM_INVENTORY | BUY_UNIT | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-6 | 385 | SELL | BUY_UNIT | 1 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-6 | 386 | BUY | BUY_UNIT | 1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-6 | 387 | SELL | BUY_UNIT | 1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-6 | 388 | BUY | BUY_UNIT | 1 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-6 | 389 | SELL | SELL_UNIT | 50 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 2 | 6-6 | 390 | BUY | BUY_UNIT | 1 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 3 | 1-1 | 1 | MOVE_BENCH | HOLD | -1 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 1-1 | 2 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 1-1 | 3 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 1-1 | 4 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 1-2 | 17 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 1-2 | 18 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 1-2 | 19 | MOVE_BENCH | HOLD | -1 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 1-2 | 20 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 1-2 | 21 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 1-2 | 25 | MOVE_BENCH | HOLD | -1 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 1-3 | 28 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 1-3 | 29 | BUY | BUY_UNIT | 0 | -1.000 | 0.000 | -2.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 1-3 | 30 | MOVE_BOARD | DEPLOY_OR_MOVE | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 1-3 | 31 | MOVE_BOARD | DEPLOY_OR_MOVE | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 1-3 | 32 | PASS | DEPLOY_OR_MOVE | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 1-3 | 39 | MOVE_BENCH | DEPLOY_OR_MOVE | 0 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 1.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 1-4 | 42 | BUY | HOLD | -1 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 1-4 | 43 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 1-4 | 44 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 1-4 | 45 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 1-4 | 46 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-1 | 55 | BUY | DEPLOY_OR_MOVE | 18 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-1 | 56 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-1 | 57 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-1 | 58 | MOVE_BENCH | DEPLOY_OR_MOVE | 18 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-1 | 59 | BUY | HOLD | -1 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-1 | 60 | MOVE_BENCH | HOLD | -1 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-1 | 61 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-2 | 64 | BUY | BUY_UNIT | 15 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-2 | 65 | BUY | BUY_UNIT | 29 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-2 | 66 | PASS | SELL_UNIT | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-3 | 72 | BUY | BUY_UNIT | 21 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-3 | 73 | BUY | BUY_UNIT | 2 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-3 | 74 | BUY_XP | BUY_UNIT | 2 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-3 | 75 | PASS | BUY_UNIT | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-4 | 82 | BUY | DEPLOY_OR_MOVE | 15 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-4 | 83 | MOVE_BENCH | DEPLOY_OR_MOVE | 15 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-4 | 84 | BUY | BUY_UNIT | 9 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-4 | 85 | MOVE_BENCH | BUY_UNIT | 9 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-4 | 86 | BUY_XP | BUY_UNIT | 9 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-4 | 87 | MOVE_BENCH | SELL_UNIT | 29 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-4 | 88 | MOVE_BOARD | SELL_UNIT | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-4 | 89 | PASS | SELL_UNIT | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 3 | 2-5 | 92 | BUY | BUY_UNIT | 15 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → Colosso |
| Jogador 3 | 2-5 | 93 | BUY_XP | BUY_UNIT | 15 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 2-5 | 94 | PASS | SELL_UNIT | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 2-6 | 102 | SELL | BUY_UNIT | 15 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 2-6 | 103 | BUY | BUY_UNIT | 15 | -2.000 | 0.000 | -4.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 2-6 | 104 | MOVE_BENCH | BUY_UNIT | 13 | 0.000 | 0.000 | 8.000 | 0.000 | 0.000 | 0.000 | 1.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 2-6 | 105 | BUY | BUY_UNIT | 13 | -1.000 | 0.000 | -2.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 2-6 | 106 | MOVE_BENCH | DEPLOY_OR_MOVE | 21 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 1.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 2-6 | 107 | BUY | SELL_UNIT | 29 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 2-6 | 108 | BUY_XP | SELL_UNIT | 29 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 2-6 | 109 | MOVE_BOARD | SELL_UNIT | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 2-6 | 110 | MOVE_BOARD | SELL_UNIT | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 2-7 | 112 | BUY | BUY_UNIT | 15 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 2-7 | 113 | BUY | BUY_UNIT | 15 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 2-7 | 114 | SELL | BUY_UNIT | 13 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 2-7 | 115 | BUY | BUY_UNIT | 13 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 2-7 | 116 | SELL | BUY_UNIT | 2 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 2-7 | 117 | SELL | BUY_UNIT | 2 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 2-7 | 118 | SELL | BUY_UNIT | 2 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 2-7 | 119 | BUY | BUY_UNIT | 2 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 2-7 | 120 | BUY_XP | SELL_UNIT | 18 | -4.000 | 0.000 | 0.000 | 1.000 | -16.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-1 | 122 | BUY | DEPLOY_OR_MOVE | 15 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-1 | 123 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-1 | 124 | MOVE_BENCH | DEPLOY_OR_MOVE | 15 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-1 | 125 | BUY | BUY_UNIT | 21 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-1 | 126 | MOVE_BOARD | BUY_UNIT | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-1 | 127 | MOVE_BOARD | BUY_UNIT | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-1 | 128 | MOVE_BOARD | BUY_UNIT | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-1 | 129 | PASS | BUY_UNIT | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-2 | 132 | BUY | BUY_UNIT | 2 | -1.000 | 0.000 | -2.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-2 | 133 | BUY | BUY_UNIT | 2 | -1.000 | 0.000 | -2.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-2 | 134 | MOVE_BENCH | DEPLOY_OR_MOVE | 15 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-2 | 135 | BUY | DEPLOY_OR_MOVE | 15 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-2 | 136 | MOVE_BOARD | DEPLOY_OR_MOVE | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-2 | 137 | MOVE_BOARD | DEPLOY_OR_MOVE | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-2 | 138 | PASS | DEPLOY_OR_MOVE | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-3 | 142 | BUY | BUY_UNIT | 15 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-3 | 143 | BUY | SELL_UNIT | 38 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-3 | 144 | MOVE_BOARD | SELL_UNIT | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-3 | 145 | MOVE_BOARD | SELL_UNIT | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-3 | 146 | MOVE_BOARD | SELL_UNIT | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-3 | 147 | PASS | SELL_UNIT | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-4 | 152 | SELL | BUY_UNIT | 40 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-4 | 153 | BUY | BUY_UNIT | 40 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-4 | 154 | MOVE_BENCH | SELL_UNIT | 52 | 0.000 | 0.000 | -2.000 | 0.000 | 0.000 | 0.000 | -1.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-4 | 155 | MOVE_BENCH | SELL_UNIT | 52 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 1.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-4 | 156 | MOVE_BENCH | SELL_UNIT | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-4 | 157 | MOVE_BENCH | SELL_UNIT | 52 | 0.000 | 0.000 | -2.000 | 0.000 | 0.000 | 0.000 | -1.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-4 | 158 | PASS | SELL_UNIT | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-5 | 162 | SELL | BUY_UNIT | 40 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-5 | 163 | BUY | BUY_UNIT | 40 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-5 | 164 | BUY | SELL_UNIT | 52 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-5 | 165 | BUY | SELL_UNIT | 52 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-5 | 166 | MOVE_BENCH | SELL_UNIT | 52 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 1.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-5 | 167 | MOVE_BENCH | SELL_UNIT | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-5 | 168 | MOVE_BENCH | SELL_UNIT | 49 | 0.000 | 0.000 | -2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-5 | 169 | PASS | SELL_UNIT | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-6 | 172 | SELL | BUY_UNIT | 15 | 5.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-6 | 173 | BUY | BUY_UNIT | 15 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-6 | 174 | BUY | BUY_UNIT | 33 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-6 | 175 | BUY | BUY_UNIT | 1 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-6 | 176 | BUY_XP | SELL_UNIT | 52 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-6 | 177 | SELL | SELL_UNIT | 52 | 5.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-6 | 178 | BUY | BUY_UNIT | 1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-6 | 179 | MOVE_BOARD | SELL_UNIT | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-6 | 180 | MOVE_BOARD | SELL_UNIT | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-7 | 182 | SELL | BUY_UNIT | 40 | 8.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-7 | 183 | BUY | SELL_UNIT | 52 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-7 | 184 | SELL | SELL_UNIT | 52 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-7 | 185 | BUY | SELL_UNIT | 52 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-7 | 186 | MOVE_BOARD | SELL_UNIT | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-7 | 187 | MOVE_BOARD | SELL_UNIT | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 3-7 | 188 | PASS | SELL_UNIT | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-1 | 192 | CRAFT_AND_EQUIP | BUY_UNIT | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-1 | 193 | CRAFT_AND_EQUIP | BUY_UNIT | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-1 | 194 | SELL | BUY_UNIT | 33 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-1 | 195 | BUY | BUY_UNIT | 33 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-1 | 196 | SELL | BUY_UNIT | 33 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-1 | 197 | BUY | BUY_UNIT | 33 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-1 | 198 | BUY | SELL_UNIT | 52 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-1 | 199 | BUY | SELL_UNIT | 53 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-1 | 200 | MOVE_BENCH | SELL_UNIT | 53 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-2 | 202 | SELL | SELL_UNIT | 53 | 8.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-2 | 203 | BUY | SELL_UNIT | 53 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-2 | 204 | SELL | SELL_UNIT | 53 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-2 | 205 | BUY | SELL_UNIT | 53 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-2 | 206 | SELL | SELL_UNIT | 53 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-2 | 207 | BUY | SELL_UNIT | 53 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-2 | 208 | MOVE_BOARD | SELL_UNIT | 53 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-2 | 209 | SELL | SELL_UNIT | 53 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-2 | 210 | BUY | SELL_UNIT | 53 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-3 | 212 | SELL | BUY_UNIT | 31 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-3 | 213 | BUY | SELL_UNIT | 53 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-3 | 214 | SELL | SELL_UNIT | 53 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-3 | 215 | BUY | SELL_UNIT | 53 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-3 | 216 | MOVE_BENCH | SELL_UNIT | 53 | 0.000 | 0.000 | -2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-3 | 217 | MOVE_BENCH | SELL_UNIT | 53 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-3 | 218 | MOVE_BENCH | SELL_UNIT | 53 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-3 | 219 | MOVE_BENCH | SELL_UNIT | 53 | 0.000 | 0.000 | -2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-3 | 220 | PASS | SELL_UNIT | 53 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-4 | 222 | SELL | SELL_UNIT | 53 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-4 | 223 | BUY | SELL_UNIT | 53 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-4 | 224 | SELL | SELL_UNIT | 53 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-4 | 225 | BUY | SELL_UNIT | 53 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-4 | 226 | SELL | SELL_UNIT | 53 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-4 | 227 | BUY | SELL_UNIT | 53 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-4 | 228 | SELL | SELL_UNIT | 53 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-4 | 229 | BUY | SELL_UNIT | 53 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-4 | 230 | SELL | BUY_UNIT | 4 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-5 | 232 | BUY | BUY_UNIT | 21 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-5 | 233 | SELL | SELL_UNIT | 53 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-5 | 234 | BUY | SELL_UNIT | 53 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-5 | 235 | SELL | SELL_UNIT | 53 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-5 | 236 | BUY | SELL_UNIT | 35 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-5 | 237 | SELL | SELL_UNIT | 35 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-5 | 238 | BUY | SELL_UNIT | 35 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-5 | 239 | SELL | BUY_UNIT | 26 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-5 | 240 | MOVE_BOARD | SELL_UNIT | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-6 | 242 | BUY | BUY_UNIT | 0 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-6 | 243 | SELL | BUY_UNIT | 15 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-6 | 244 | BUY | BUY_UNIT | 15 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-6 | 245 | SELL | BUY_UNIT | 22 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-6 | 246 | BUY | BUY_UNIT | 38 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-6 | 247 | SELL | BUY_UNIT | 38 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-6 | 248 | BUY | BUY_UNIT | 38 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-6 | 249 | SELL | BUY_UNIT | 22 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-6 | 250 | BUY | BUY_UNIT | 22 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-7 | 252 | SELL | BUY_UNIT | 40 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-7 | 253 | BUY | BUY_UNIT | 40 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-7 | 254 | BUY | SELL_UNIT | 35 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-7 | 255 | BUY | SELL_UNIT | 35 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-7 | 256 | SELL | SELL_UNIT | 35 | 8.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-7 | 257 | BUY | SELL_UNIT | 35 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-7 | 258 | SELL | SELL_UNIT | 35 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-7 | 259 | BUY | SELL_UNIT | 35 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 4-7 | 260 | SELL | SELL_UNIT | 35 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-1 | 262 | BUY | DEPLOY_OR_MOVE | 21 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-1 | 263 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-1 | 264 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-1 | 265 | SELL | DEPLOY_OR_MOVE | 15 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-1 | 266 | BUY | DEPLOY_OR_MOVE | 15 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-1 | 267 | SELL | DEPLOY_OR_MOVE | 15 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-1 | 268 | BUY | DEPLOY_OR_MOVE | 15 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-1 | 269 | MOVE_BENCH | DEPLOY_OR_MOVE | 15 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-1 | 270 | BUY | BUY_UNIT | 9 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-2 | 272 | SELL | BUY_UNIT | 7 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-2 | 273 | BUY | BUY_UNIT | 7 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-2 | 274 | SELL | BUY_XP | -1 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-2 | 275 | BUY | BUY_XP | -1 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-2 | 276 | SELL | SELL_UNIT | 25 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-2 | 277 | BUY | BUY_XP | -1 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-2 | 278 | MOVE_BOARD | SELL_UNIT | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-2 | 279 | MOVE_BOARD | SELL_UNIT | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-2 | 280 | MOVE_BOARD | SELL_UNIT | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-3 | 282 | SELL | BUY_UNIT | 18 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-3 | 283 | BUY | BUY_UNIT | 18 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-3 | 284 | SELL | BUY_UNIT | 18 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-3 | 285 | BUY | BUY_UNIT | 18 | -2.000 | 0.000 | -4.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-3 | 286 | BUY | DEPLOY_OR_MOVE | 35 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-3 | 287 | SELL | DEPLOY_OR_MOVE | 35 | 5.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-3 | 288 | BUY | DEPLOY_OR_MOVE | 7 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-3 | 289 | BUY_XP | DEPLOY_OR_MOVE | 7 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-3 | 290 | BUY_XP | DEPLOY_OR_MOVE | 7 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-4 | 292 | SELL | DEPLOY_OR_MOVE | 7 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-4 | 293 | BUY | DEPLOY_OR_MOVE | 7 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-4 | 294 | SELL | DEPLOY_OR_MOVE | 15 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-4 | 295 | BUY | DEPLOY_OR_MOVE | 35 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-4 | 296 | SELL | DEPLOY_OR_MOVE | 35 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-4 | 297 | BUY | DEPLOY_OR_MOVE | 35 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-4 | 298 | SELL | DEPLOY_OR_MOVE | 35 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-4 | 299 | BUY | DEPLOY_OR_MOVE | 35 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-4 | 300 | MOVE_BENCH | DEPLOY_OR_MOVE | 15 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-5 | 302 | BUY | SELL_UNIT | 21 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-5 | 303 | SELL | SELL_UNIT | 33 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-5 | 304 | BUY | SELL_UNIT | 33 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-5 | 305 | SELL | SELL_UNIT | 33 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-5 | 306 | BUY | SELL_UNIT | 33 | -5.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-5 | 307 | MOVE_BOARD | SELL_UNIT | 64 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-5 | 308 | SELL | SELL_UNIT | 64 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-5 | 309 | BUY | SELL_UNIT | 64 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-5 | 310 | MOVE_BOARD | SELL_UNIT | 64 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-6 | 312 | SELL | SELL_UNIT | 64 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-6 | 313 | BUY | SELL_UNIT | 64 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-6 | 314 | SELL | SELL_UNIT | 64 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-6 | 315 | BUY | SELL_UNIT | 64 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-6 | 316 | SELL | SELL_UNIT | 64 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-6 | 317 | BUY | SELL_UNIT | 64 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-6 | 318 | MOVE_BOARD | SELL_UNIT | 64 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-6 | 319 | MOVE_BOARD | SELL_UNIT | 64 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-6 | 320 | MOVE_BOARD | SELL_UNIT | 64 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-7 | 322 | SELL | BUY_UNIT | 13 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-7 | 323 | BUY | BUY_UNIT | 13 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-7 | 324 | SELL | SELL_UNIT | 64 | 5.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-7 | 325 | BUY | BUY_XP | -1 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-7 | 326 | SELL | SELL_UNIT | 33 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-7 | 327 | BUY | BUY_XP | -1 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-7 | 328 | SELL | SELL_UNIT | 30 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-7 | 329 | BUY | BUY_XP | -1 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 5-7 | 330 | MOVE_BOARD | SELL_UNIT | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-1 | 332 | EQUIP_FROM_INVENTORY | BUY_UNIT | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-1 | 333 | SELL | BUY_UNIT | 35 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-1 | 334 | BUY | BUY_UNIT | 35 | -3.000 | 0.000 | -6.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-1 | 335 | BUY | DEPLOY_OR_MOVE | 7 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-1 | 336 | SELL | DEPLOY_OR_MOVE | 7 | 8.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-1 | 337 | BUY | DEPLOY_OR_MOVE | 7 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-1 | 338 | SELL | DEPLOY_OR_MOVE | 7 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-1 | 339 | BUY | DEPLOY_OR_MOVE | 7 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-1 | 340 | MOVE_BENCH | DEPLOY_OR_MOVE | 7 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-2 | 342 | BUY | BUY_UNIT | 38 | -3.000 | 0.000 | -6.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-2 | 343 | BUY | DEPLOY_OR_MOVE | 7 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-2 | 344 | SELL | DEPLOY_OR_MOVE | 7 | 8.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-2 | 345 | BUY | DEPLOY_OR_MOVE | 7 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-2 | 346 | SELL | DEPLOY_OR_MOVE | 7 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-2 | 347 | BUY | DEPLOY_OR_MOVE | 7 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-2 | 348 | SELL | DEPLOY_OR_MOVE | 7 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-2 | 349 | BUY | DEPLOY_OR_MOVE | 7 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-2 | 350 | REROLL | DEPLOY_OR_MOVE | 7 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-3 | 352 | SELL | DEPLOY_OR_MOVE | 7 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-3 | 353 | BUY | DEPLOY_OR_MOVE | 7 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-3 | 354 | SELL | DEPLOY_OR_MOVE | 7 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-3 | 355 | BUY | DEPLOY_OR_MOVE | 7 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-3 | 356 | SELL | DEPLOY_OR_MOVE | 44 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-3 | 357 | BUY | DEPLOY_OR_MOVE | 7 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-3 | 358 | SELL | DEPLOY_OR_MOVE | 7 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-3 | 359 | BUY | DEPLOY_OR_MOVE | 7 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 3 | 6-3 | 360 | REROLL | DEPLOY_OR_MOVE | 7 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 4 | 1-1 | 1 | MOVE_BENCH | HOLD | -1 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 1-1 | 2 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 1-1 | 3 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 1-1 | 4 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 1-2 | 17 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 1-2 | 18 | BUY | DEPLOY_OR_MOVE | 13 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 1-2 | 19 | MOVE_BENCH | DEPLOY_OR_MOVE | 13 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 1-2 | 20 | MOVE_BOARD | DEPLOY_OR_MOVE | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 1-2 | 21 | PASS | DEPLOY_OR_MOVE | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 1-2 | 25 | MOVE_BENCH | DEPLOY_OR_MOVE | 13 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 1-3 | 28 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 1-3 | 29 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 1-3 | 30 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 1-3 | 31 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 1-3 | 32 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 1-4 | 42 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 1-4 | 43 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 1-4 | 44 | PASS | BUY_UNIT | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-1 | 55 | BUY | DEPLOY_OR_MOVE | 1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-1 | 56 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-1 | 57 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-1 | 58 | BUY_XP | DEPLOY_OR_MOVE | 13 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-1 | 59 | PASS | DEPLOY_OR_MOVE | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-1 | 61 | MOVE_BENCH | DEPLOY_OR_MOVE | 13 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-2 | 64 | BUY | BUY_UNIT | 3 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-2 | 65 | BUY_XP | HOLD | -1 | -4.000 | 0.000 | 0.000 | 1.000 | -6.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-2 | 66 | PASS | DEPLOY_OR_MOVE | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-3 | 72 | BUY | BUY_UNIT | 1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-3 | 73 | BUY | BUY_UNIT | 1 | -1.000 | 0.000 | -2.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-3 | 74 | BUY | DEPLOY_OR_MOVE | 13 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-3 | 75 | SELL | DEPLOY_OR_MOVE | 13 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-3 | 76 | BUY_XP | DEPLOY_OR_MOVE | 13 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-3 | 77 | SELL | DEPLOY_OR_MOVE | 13 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-3 | 78 | MOVE_BENCH | DEPLOY_OR_MOVE | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-3 | 79 | SELL | DEPLOY_OR_MOVE | 33 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-3 | 80 | PASS | DEPLOY_OR_MOVE | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-4 | 82 | BUY | BUY_UNIT | 18 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-4 | 83 | BUY | BUY_UNIT | 18 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-4 | 84 | SELL | SELL_UNIT | 43 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-4 | 85 | BUY_XP | SELL_UNIT | 43 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-4 | 86 | MOVE_BOARD | SELL_UNIT | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-4 | 87 | SELL | SELL_UNIT | 43 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-4 | 88 | SELL | SELL_UNIT | 43 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-4 | 89 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-4 | 90 | BUY | BUY_UNIT | 12 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 4 | 2-5 | 92 | BUY | BUY_UNIT | 12 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → Florescer |
| Jogador 4 | 2-5 | 93 | BUY | BUY_UNIT | 26 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-5 | 94 | BUY_XP | BUY_UNIT | 34 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-5 | 95 | SELL | BUY_UNIT | 34 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-5 | 96 | BUY | BUY_XP | -1 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-5 | 97 | MOVE_BENCH | SELL_UNIT | 29 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-5 | 98 | SELL | BUY_UNIT | 34 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-5 | 99 | BUY_XP | BUY_XP | -1 | -4.000 | 0.000 | 0.000 | 1.000 | -16.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-5 | 100 | MOVE_BENCH | DEPLOY_OR_MOVE | 3 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-6 | 102 | BUY | HOLD | -1 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-6 | 103 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-6 | 104 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-6 | 105 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-6 | 106 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-6 | 107 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-7 | 112 | BUY | BUY_UNIT | 7 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-7 | 113 | BUY | HOLD | -1 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-7 | 114 | BUY_XP | HOLD | -1 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-7 | 115 | SELL | HOLD | -1 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-7 | 116 | SELL | HOLD | -1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-7 | 117 | BUY | HOLD | -1 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-7 | 118 | SELL | HOLD | -1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-7 | 119 | MOVE_BENCH | HOLD | -1 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 2-7 | 120 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-1 | 122 | BUY | BUY_UNIT | 26 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-1 | 123 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-1 | 124 | CRAFT_AND_EQUIP | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-1 | 125 | BUY_XP | HOLD | -1 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-1 | 126 | SELL | HOLD | -1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-1 | 127 | SELL | HOLD | -1 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-1 | 128 | BUY | HOLD | -1 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-1 | 129 | MOVE_BENCH | SELL_UNIT | 32 | 0.000 | 0.000 | -2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-1 | 130 | MOVE_BENCH | SELL_UNIT | 32 | 0.000 | 0.000 | -2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-2 | 132 | BUY | BUY_UNIT | 13 | -1.000 | 0.000 | -4.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-2 | 133 | MOVE_BENCH | BUY_UNIT | 13 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-2 | 134 | BUY | BUY_UNIT | 13 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-2 | 135 | MOVE_BENCH | DEPLOY_OR_MOVE | 13 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-2 | 136 | BUY | SELL_UNIT | 32 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-2 | 137 | MOVE_BENCH | SELL_UNIT | 30 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 1.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-2 | 138 | MOVE_BOARD | SELL_UNIT | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-2 | 139 | MOVE_BOARD | SELL_UNIT | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-2 | 140 | PASS | SELL_UNIT | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-3 | 142 | BUY | BUY_UNIT | 26 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-3 | 143 | BUY | SELL_UNIT | 30 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-3 | 144 | BUY | SELL_UNIT | 30 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-3 | 145 | MOVE_BENCH | SELL_UNIT | 30 | 0.000 | 0.000 | -4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-3 | 146 | MOVE_BOARD | SELL_UNIT | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-3 | 147 | MOVE_BENCH | SELL_UNIT | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-3 | 148 | PASS | SELL_UNIT | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-4 | 152 | BUY | BUY_UNIT | 26 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-4 | 153 | BUY | BUY_UNIT | 36 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-4 | 154 | MOVE_BENCH | BUY_UNIT | 0 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-4 | 155 | BUY | BUY_UNIT | 0 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-4 | 156 | MOVE_BENCH | SELL_UNIT | 30 | 0.000 | 0.000 | -4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-4 | 157 | MOVE_BENCH | SELL_UNIT | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-4 | 158 | MOVE_BENCH | SELL_UNIT | 30 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-4 | 159 | PASS | SELL_UNIT | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-5 | 162 | SELL | BUY_UNIT | 26 | 5.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-5 | 163 | BUY | BUY_UNIT | 26 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-5 | 164 | MOVE_BENCH | SELL_UNIT | 30 | 0.000 | 0.000 | -4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-5 | 165 | MOVE_BENCH | BUY_UNIT | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-5 | 166 | MOVE_BENCH | BUY_UNIT | 22 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-5 | 167 | PASS | BUY_UNIT | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-6 | 172 | SELL | BUY_UNIT | 26 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-6 | 173 | BUY | BUY_UNIT | 26 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-6 | 174 | BUY | BUY_UNIT | 30 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-6 | 175 | MOVE_BENCH | BUY_UNIT | 28 | 0.000 | 0.000 | -4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-6 | 176 | SELL | BUY_UNIT | 28 | 5.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-6 | 177 | BUY | BUY_UNIT | 28 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-6 | 178 | MOVE_BENCH | SELL_UNIT | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-6 | 179 | MOVE_BENCH | SELL_UNIT | 28 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-6 | 180 | PASS | SELL_UNIT | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-7 | 182 | BUY | BUY_UNIT | 36 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-7 | 183 | MOVE_BENCH | SELL_UNIT | 28 | 0.000 | 0.000 | -4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-7 | 184 | MOVE_BENCH | SELL_UNIT | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-7 | 185 | MOVE_BENCH | SELL_UNIT | 28 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 3-7 | 186 | PASS | SELL_UNIT | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-1 | 192 | CRAFT_AND_EQUIP | SELL_UNIT | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-1 | 193 | CRAFT_AND_EQUIP | SELL_UNIT | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-1 | 194 | MOVE_BENCH | SELL_UNIT | 28 | 0.000 | 0.000 | -4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-1 | 195 | SELL | SELL_UNIT | 28 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-1 | 196 | BUY | BUY_UNIT | 38 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-1 | 197 | MOVE_BOARD | SELL_UNIT | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-1 | 198 | MOVE_BOARD | SELL_UNIT | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-1 | 199 | MOVE_BOARD | SELL_UNIT | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-1 | 200 | PASS | SELL_UNIT | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-2 | 202 | SELL | BUY_XP | -1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-2 | 203 | BUY | BUY_XP | -1 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-2 | 204 | SELL | BUY_XP | -1 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-2 | 205 | BUY | BUY_XP | -1 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-2 | 206 | MOVE_BENCH | BUY_XP | -1 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-2 | 207 | MOVE_BENCH | SELL_UNIT | 35 | 0.000 | 0.000 | -2.000 | 0.000 | 0.000 | 0.000 | -1.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-2 | 208 | PASS | BUY_XP | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-3 | 212 | SELL | BUY_XP | -1 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-3 | 213 | BUY | BUY_XP | -1 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-3 | 214 | EQUIP_FROM_INVENTORY | BUY_XP | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-3 | 215 | EQUIP_FROM_INVENTORY | BUY_XP | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-3 | 216 | EQUIP_FROM_INVENTORY | BUY_XP | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-3 | 217 | MOVE_BENCH | BUY_XP | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-3 | 218 | MOVE_BENCH | BUY_XP | -1 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-3 | 219 | PASS | BUY_XP | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-4 | 222 | MOVE_BENCH | DEPLOY_OR_MOVE | 36 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-4 | 223 | BUY | BUY_UNIT | 26 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-4 | 224 | MOVE_BOARD | BUY_UNIT | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-4 | 225 | SELL | BUY_UNIT | 38 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-4 | 226 | BUY | BUY_UNIT | 38 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-4 | 227 | REROLL | BUY_UNIT | 38 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-4 | 228 | SELL | BUY_UNIT | 53 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-4 | 229 | BUY | BUY_UNIT | 53 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-4 | 230 | MOVE_BENCH | BUY_UNIT | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-5 | 232 | SELL | BUY_UNIT | 33 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-5 | 233 | BUY | BUY_UNIT | 33 | -3.000 | 0.000 | -6.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-5 | 234 | MOVE_BENCH | DEPLOY_OR_MOVE | 36 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-5 | 235 | BUY | BUY_UNIT | 45 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-5 | 236 | MOVE_BOARD | BUY_UNIT | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-5 | 237 | MOVE_BOARD | BUY_UNIT | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 4 | 4-5 | 238 | PASS | BUY_UNIT | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Florescer → Florescer |
| Jogador 5 | 1-1 | 1 | MOVE_BENCH | HOLD | -1 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 1-1 | 2 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 1-1 | 3 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 1-2 | 17 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 1-2 | 18 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 1-2 | 19 | MOVE_BENCH | DEPLOY_OR_MOVE | 11 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 1-2 | 20 | MOVE_BOARD | DEPLOY_OR_MOVE | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 1-2 | 21 | MOVE_BOARD | DEPLOY_OR_MOVE | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 1-2 | 22 | PASS | DEPLOY_OR_MOVE | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 1-2 | 25 | MOVE_BENCH | DEPLOY_OR_MOVE | 11 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 1-3 | 28 | BUY | HOLD | -1 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 1-3 | 29 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 1-4 | 42 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 1-4 | 43 | BUY | HOLD | -1 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 1-4 | 44 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-1 | 55 | BUY | DEPLOY_OR_MOVE | 26 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-1 | 56 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-1 | 57 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-1 | 58 | MOVE_BENCH | DEPLOY_OR_MOVE | 8 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-1 | 59 | BUY | HOLD | -1 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-1 | 60 | PASS | SELL_UNIT | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-2 | 64 | BUY | BUY_UNIT | 7 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-2 | 65 | BUY_XP | SELL_UNIT | 28 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-2 | 66 | PASS | SELL_UNIT | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-3 | 72 | BUY | BUY_UNIT | 7 | -1.000 | 0.000 | -2.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-3 | 73 | BUY_XP | DEPLOY_OR_MOVE | 8 | -4.000 | 0.000 | 0.000 | 1.000 | -6.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-3 | 74 | MOVE_BENCH | DEPLOY_OR_MOVE | 8 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-3 | 75 | BUY | DEPLOY_OR_MOVE | 7 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-3 | 76 | MOVE_BENCH | DEPLOY_OR_MOVE | 8 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-3 | 77 | BUY | SELL_UNIT | 26 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-3 | 78 | MOVE_BOARD | SELL_UNIT | 26 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-3 | 79 | SELL | SELL_UNIT | 26 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-3 | 80 | BUY_XP | SELL_UNIT | 26 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-4 | 82 | BUY | HOLD | -1 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-4 | 83 | BUY | SELL_UNIT | 33 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-4 | 84 | SELL | SELL_UNIT | 33 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-4 | 85 | SELL | SELL_UNIT | 33 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-4 | 86 | BUY | SELL_UNIT | 33 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-4 | 87 | SELL | SELL_UNIT | 33 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-4 | 88 | SELL | SELL_UNIT | 33 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-4 | 89 | BUY_XP | SELL_UNIT | 33 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-4 | 90 | PASS | SELL_UNIT | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 5 | 2-5 | 92 | BUY | SELL_UNIT | 33 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → Espinhos Negros |
| Jogador 5 | 2-5 | 93 | BUY | SELL_UNIT | 37 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Espinhos Negros → Espinhos Negros |
| Jogador 5 | 2-5 | 94 | SELL | SELL_UNIT | 37 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Espinhos Negros → Espinhos Negros |
| Jogador 5 | 2-5 | 95 | SELL | SELL_UNIT | 33 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Espinhos Negros → Espinhos Negros |
| Jogador 5 | 2-5 | 96 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Espinhos Negros → Espinhos Negros |
| Jogador 5 | 2-5 | 97 | BUY_XP | HOLD | -1 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Espinhos Negros → Espinhos Negros |
| Jogador 5 | 2-5 | 98 | SELL | HOLD | -1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Espinhos Negros → Espinhos Negros |
| Jogador 5 | 2-5 | 99 | BUY_XP | HOLD | -1 | -4.000 | 0.000 | 0.000 | 1.000 | -16.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Espinhos Negros → Espinhos Negros |
| Jogador 5 | 2-5 | 100 | MOVE_BENCH | DEPLOY_OR_MOVE | 8 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Espinhos Negros → Espinhos Negros |
| Jogador 5 | 2-6 | 102 | BUY | BUY_UNIT | 20 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Espinhos Negros → Espinhos Negros |
| Jogador 5 | 2-6 | 103 | BUY | SELL_UNIT | 20 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Espinhos Negros → Enfeitiçador |
| Jogador 5 | 2-6 | 104 | MOVE_BOARD | SELL_UNIT | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 2-6 | 105 | BUY | SELL_UNIT | 17 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 2-6 | 106 | SELL | SELL_UNIT | 17 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 2-6 | 107 | SELL | SELL_UNIT | 17 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 2-6 | 108 | SELL | SELL_UNIT | 22 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 2-6 | 109 | BUY | SELL_UNIT | 20 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 2-6 | 110 | BUY | SELL_UNIT | 9 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 2-7 | 112 | BUY | HOLD | -1 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 2-7 | 113 | BUY | HOLD | -1 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 2-7 | 114 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 2-7 | 115 | SELL | HOLD | -1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 2-7 | 116 | SELL | HOLD | -1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 2-7 | 117 | BUY | HOLD | -1 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 2-7 | 118 | SELL | HOLD | -1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 2-7 | 119 | SELL | HOLD | -1 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 2-7 | 120 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-1 | 122 | BUY | BUY_UNIT | 26 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-1 | 123 | CRAFT_AND_EQUIP | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-1 | 124 | BUY | HOLD | -1 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-1 | 125 | BUY | SELL_UNIT | 39 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-1 | 126 | SELL | SELL_UNIT | 39 | 5.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-1 | 127 | BUY | SELL_UNIT | 39 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-1 | 128 | SELL | SELL_UNIT | 39 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-1 | 129 | SELL | SELL_UNIT | 39 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-1 | 130 | BUY | SELL_UNIT | 39 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-2 | 132 | BUY | BUY_UNIT | 39 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-2 | 133 | BUY | SELL_UNIT | 24 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-2 | 134 | SELL | SELL_UNIT | 24 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-2 | 135 | SELL | SELL_UNIT | 24 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-2 | 136 | SELL | SELL_UNIT | 26 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-2 | 137 | BUY | SELL_UNIT | 39 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-2 | 138 | SELL | SELL_UNIT | 39 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-2 | 139 | BUY | SELL_UNIT | 39 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-2 | 140 | SELL | SELL_UNIT | 39 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-3 | 142 | BUY | BUY_UNIT | 27 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-3 | 143 | BUY | BUY_UNIT | 41 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-3 | 144 | BUY | BUY_UNIT | 27 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-3 | 145 | SELL | SELL_UNIT | 39 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-3 | 146 | SELL | SELL_UNIT | 27 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-3 | 147 | BUY | SELL_UNIT | 27 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-3 | 148 | MOVE_BENCH | SELL_UNIT | 37 | 0.000 | 0.000 | -2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-3 | 149 | MOVE_BENCH | SELL_UNIT | 37 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-3 | 150 | PASS | SELL_UNIT | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-4 | 152 | BUY | BUY_UNIT | 3 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-4 | 153 | BUY | SELL_UNIT | 37 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-4 | 154 | SELL | SELL_UNIT | 37 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-4 | 155 | BUY | SELL_UNIT | 27 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-4 | 156 | SELL | SELL_UNIT | 27 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-4 | 157 | BUY | SELL_UNIT | 27 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-4 | 158 | SELL | SELL_UNIT | 27 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-4 | 159 | SELL | SELL_UNIT | 27 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-4 | 160 | SELL | SELL_UNIT | 27 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-5 | 162 | BUY | BUY_UNIT | 8 | -1.000 | 0.000 | -2.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-5 | 163 | BUY | DEPLOY_OR_MOVE | 26 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-5 | 164 | MOVE_BENCH | DEPLOY_OR_MOVE | 26 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-5 | 165 | BUY | SELL_UNIT | 35 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-5 | 166 | BUY | SELL_UNIT | 35 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-5 | 167 | BUY | SELL_UNIT | 35 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-5 | 168 | SELL | SELL_UNIT | 35 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-5 | 169 | SELL | SELL_UNIT | 34 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-5 | 170 | SELL | SELL_UNIT | 34 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-6 | 172 | BUY | SELL_UNIT | 34 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-6 | 173 | BUY | SELL_UNIT | 34 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-6 | 174 | BUY | SELL_UNIT | 34 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-6 | 175 | BUY | SELL_UNIT | 34 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-6 | 176 | SELL | SELL_UNIT | 34 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-6 | 177 | SELL | SELL_UNIT | 34 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-6 | 178 | SELL | SELL_UNIT | 34 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-6 | 179 | SELL | SELL_UNIT | 34 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-6 | 180 | SELL | SELL_UNIT | 34 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-7 | 182 | BUY | BUY_UNIT | 20 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-7 | 183 | BUY | SELL_UNIT | 27 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-7 | 184 | BUY | SELL_UNIT | 40 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-7 | 185 | BUY | SELL_UNIT | 40 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-7 | 186 | SELL | SELL_UNIT | 40 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-7 | 187 | BUY | SELL_UNIT | 40 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-7 | 188 | SELL | SELL_UNIT | 40 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-7 | 189 | REROLL | SELL_UNIT | 40 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 3-7 | 190 | BUY | BUY_UNIT | 20 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-1 | 192 | BUY | BUY_UNIT | 53 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-1 | 193 | CRAFT_AND_EQUIP | SELL_UNIT | 53 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-1 | 194 | CRAFT_AND_EQUIP | SELL_UNIT | 53 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-1 | 195 | SELL | SELL_UNIT | 53 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-1 | 196 | BUY | SELL_UNIT | 53 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-1 | 197 | SELL | SELL_UNIT | 53 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-1 | 198 | BUY | SELL_UNIT | 53 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-1 | 199 | SELL | BUY_UNIT | 23 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-1 | 200 | BUY | SELL_UNIT | 53 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-2 | 202 | SELL | BUY_UNIT | 27 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-2 | 203 | BUY | BUY_UNIT | 27 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-2 | 204 | SELL | SELL_UNIT | 53 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-2 | 205 | BUY | SELL_UNIT | 53 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-2 | 206 | SELL | SELL_UNIT | 53 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-2 | 207 | BUY | SELL_UNIT | 53 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-2 | 208 | SELL | SELL_UNIT | 53 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-2 | 209 | BUY | SELL_UNIT | 53 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-2 | 210 | MOVE_BOARD | SELL_UNIT | 53 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-3 | 212 | SELL | SELL_UNIT | 53 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-3 | 213 | BUY | SELL_UNIT | 53 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-3 | 214 | SELL | SELL_UNIT | 53 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-3 | 215 | BUY | SELL_UNIT | 53 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-3 | 216 | SELL | SELL_UNIT | 53 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-3 | 217 | BUY | SELL_UNIT | 53 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-3 | 218 | SELL | SELL_UNIT | 53 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-3 | 219 | BUY | SELL_UNIT | 53 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-3 | 220 | SELL | SELL_UNIT | 53 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-4 | 222 | BUY | BUY_UNIT | 3 | -1.000 | 0.000 | -2.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-4 | 223 | BUY | DEPLOY_OR_MOVE | 3 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-4 | 224 | MOVE_BENCH | DEPLOY_OR_MOVE | 3 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-4 | 225 | BUY | SELL_UNIT | 53 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-4 | 226 | SELL | BUY_UNIT | 5 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-4 | 227 | EQUIP_FROM_INVENTORY | BUY_UNIT | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-4 | 228 | BUY | BUY_UNIT | 5 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-4 | 229 | EQUIP_FROM_INVENTORY | SELL_UNIT | 53 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-4 | 230 | MOVE_BOARD | SELL_UNIT | 53 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-5 | 232 | SELL | BUY_UNIT | 35 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-5 | 233 | BUY | BUY_UNIT | 35 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-5 | 234 | SELL | BUY_UNIT | 30 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-5 | 235 | BUY | BUY_UNIT | 30 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-5 | 236 | SELL | SELL_UNIT | 30 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-5 | 237 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-5 | 238 | REROLL | SELL_UNIT | 0 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-5 | 239 | SELL | BUY_UNIT | 43 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-5 | 240 | BUY | BUY_UNIT | 43 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-6 | 242 | SELL | BUY_UNIT | 35 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-6 | 243 | BUY | BUY_UNIT | 35 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-6 | 244 | BUY | BUY_XP | -1 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-6 | 245 | BUY | BUY_XP | -1 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-6 | 246 | SELL | BUY_XP | -1 | 8.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-6 | 247 | BUY | BUY_XP | -1 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-6 | 248 | REROLL | BUY_XP | -1 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-6 | 249 | SELL | BUY_XP | -1 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 5 | 4-6 | 250 | BUY | BUY_XP | -1 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 6 | 1-1 | 1 | MOVE_BENCH | HOLD | -1 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 1-1 | 2 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 1-1 | 3 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 1-2 | 17 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 1-2 | 18 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 1-2 | 19 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 1-2 | 25 | MOVE_BENCH | DEPLOY_OR_MOVE | 12 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 1-3 | 28 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 1-3 | 29 | BUY | DEPLOY_OR_MOVE | 12 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 1-3 | 30 | MOVE_BOARD | DEPLOY_OR_MOVE | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 1-3 | 31 | MOVE_BOARD | DEPLOY_OR_MOVE | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 1-3 | 32 | PASS | DEPLOY_OR_MOVE | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 1-3 | 39 | MOVE_BENCH | DEPLOY_OR_MOVE | 12 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 1-4 | 42 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 1-4 | 43 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-1 | 55 | CRAFT_AND_EQUIP | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-1 | 56 | CRAFT_AND_EQUIP | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-1 | 57 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-1 | 58 | BUY_XP | DEPLOY_OR_MOVE | 7 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-1 | 59 | PASS | DEPLOY_OR_MOVE | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-1 | 61 | MOVE_BENCH | DEPLOY_OR_MOVE | 7 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-2 | 64 | BUY | HOLD | -1 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-2 | 65 | BUY | SELL_UNIT | 39 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-2 | 66 | SELL | SELL_UNIT | 39 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-2 | 67 | BUY | SELL_UNIT | 39 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-2 | 68 | PASS | SELL_UNIT | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-3 | 72 | BUY | SELL_UNIT | 39 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-3 | 73 | BUY | SELL_UNIT | 39 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-3 | 74 | BUY | SELL_UNIT | 39 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-3 | 75 | SELL | SELL_UNIT | 39 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-3 | 76 | SELL | SELL_UNIT | 39 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-3 | 77 | PASS | SELL_UNIT | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-4 | 82 | BUY | DEPLOY_OR_MOVE | 39 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-4 | 83 | BUY | DEPLOY_OR_MOVE | 39 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-4 | 84 | BUY | DEPLOY_OR_MOVE | 39 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-4 | 85 | BUY_XP | DEPLOY_OR_MOVE | 15 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-4 | 86 | SELL | DEPLOY_OR_MOVE | 15 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-4 | 87 | SELL | DEPLOY_OR_MOVE | 15 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-4 | 88 | BUY_XP | DEPLOY_OR_MOVE | 15 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-4 | 89 | SELL | DEPLOY_OR_MOVE | 15 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-4 | 90 | SELL | DEPLOY_OR_MOVE | 7 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 6 | 2-5 | 92 | BUY | DEPLOY_OR_MOVE | 7 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → Feérico |
| Jogador 6 | 2-5 | 93 | SELL | DEPLOY_OR_MOVE | 7 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-5 | 94 | BUY_XP | DEPLOY_OR_MOVE | 7 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-5 | 95 | BUY_XP | DEPLOY_OR_MOVE | 7 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-5 | 96 | BUY_XP | DEPLOY_OR_MOVE | 7 | -4.000 | 0.000 | 0.000 | 1.000 | -16.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-5 | 97 | MOVE_BENCH | DEPLOY_OR_MOVE | 7 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-5 | 98 | SELL | DEPLOY_OR_MOVE | 13 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-5 | 99 | BUY | DEPLOY_OR_MOVE | 13 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-5 | 100 | SELL | DEPLOY_OR_MOVE | 7 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-6 | 102 | BUY | DEPLOY_OR_MOVE | 13 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-6 | 103 | BUY | DEPLOY_OR_MOVE | 7 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-6 | 104 | BUY_XP | DEPLOY_OR_MOVE | 7 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-6 | 105 | SELL | DEPLOY_OR_MOVE | 7 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-6 | 106 | BUY_XP | DEPLOY_OR_MOVE | 7 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-6 | 107 | SELL | DEPLOY_OR_MOVE | 7 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-6 | 108 | SELL | DEPLOY_OR_MOVE | 13 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-6 | 109 | BUY | DEPLOY_OR_MOVE | 7 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-6 | 110 | MOVE_BOARD | DEPLOY_OR_MOVE | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-7 | 112 | BUY | DEPLOY_OR_MOVE | 7 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-7 | 113 | BUY | DEPLOY_OR_MOVE | 7 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-7 | 114 | MOVE_BENCH | DEPLOY_OR_MOVE | 7 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-7 | 115 | MOVE_BOARD | BUY_UNIT | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-7 | 116 | MOVE_BOARD | BUY_UNIT | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-7 | 117 | MOVE_BOARD | SELL_UNIT | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-7 | 118 | MOVE_BOARD | BUY_UNIT | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 2-7 | 119 | PASS | BUY_UNIT | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-1 | 122 | BUY | SELL_UNIT | 40 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-1 | 123 | CRAFT_AND_EQUIP | SELL_UNIT | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-1 | 124 | BUY | SELL_UNIT | 30 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-1 | 125 | MOVE_BENCH | SELL_UNIT | 30 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-1 | 126 | MOVE_BOARD | SELL_UNIT | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-1 | 127 | PASS | SELL_UNIT | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-2 | 132 | BUY | BUY_UNIT | 7 | -1.000 | 0.000 | -4.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-2 | 133 | BUY | BUY_UNIT | 7 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-2 | 134 | MOVE_BENCH | DEPLOY_OR_MOVE | 7 | 0.000 | 0.000 | -4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-2 | 135 | MOVE_BENCH | DEPLOY_OR_MOVE | 7 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-2 | 136 | BUY_XP | DEPLOY_OR_MOVE | 7 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-2 | 137 | MOVE_BOARD | DEPLOY_OR_MOVE | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-2 | 138 | SELL | DEPLOY_OR_MOVE | 7 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-2 | 139 | EQUIP_FROM_INVENTORY | DEPLOY_OR_MOVE | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-2 | 140 | EQUIP_FROM_INVENTORY | DEPLOY_OR_MOVE | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-3 | 142 | BUY | DEPLOY_OR_MOVE | 7 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-3 | 143 | EQUIP_FROM_INVENTORY | DEPLOY_OR_MOVE | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-3 | 144 | BUY_XP | DEPLOY_OR_MOVE | 7 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-3 | 145 | BUY_XP | DEPLOY_OR_MOVE | 7 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-3 | 146 | MOVE_BOARD | DEPLOY_OR_MOVE | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-3 | 147 | MOVE_BOARD | DEPLOY_OR_MOVE | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-3 | 148 | SELL | DEPLOY_OR_MOVE | 7 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-3 | 149 | BUY | DEPLOY_OR_MOVE | 39 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-3 | 150 | PASS | DEPLOY_OR_MOVE | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-4 | 152 | BUY | BUY_XP | -1 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-4 | 153 | BUY | SELL_UNIT | 40 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-4 | 154 | SELL | SELL_UNIT | 37 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-4 | 155 | BUY | SELL_UNIT | 37 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-4 | 156 | SELL | SELL_UNIT | 37 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-4 | 157 | SELL | SELL_UNIT | 37 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-4 | 158 | BUY_XP | BUY_XP | -1 | -4.000 | 0.000 | 0.000 | 1.000 | -32.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-4 | 159 | MOVE_BENCH | DEPLOY_OR_MOVE | 39 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-4 | 160 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-5 | 162 | BUY | HOLD | -1 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-5 | 163 | BUY | SELL_UNIT | 37 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-5 | 164 | MOVE_BOARD | SELL_UNIT | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-5 | 165 | MOVE_BOARD | SELL_UNIT | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-5 | 166 | MOVE_BOARD | SELL_UNIT | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-5 | 167 | PASS | SELL_UNIT | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-6 | 172 | BUY | SELL_UNIT | 37 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-6 | 173 | BUY | SELL_UNIT | 37 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-6 | 174 | BUY | SELL_UNIT | 37 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-6 | 175 | MOVE_BOARD | SELL_UNIT | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-6 | 176 | MOVE_BOARD | SELL_UNIT | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-6 | 177 | PASS | SELL_UNIT | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-7 | 182 | BUY | SELL_UNIT | 37 | -5.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-7 | 183 | MOVE_BOARD | BUY_UNIT | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-7 | 184 | SELL | BUY_UNIT | 24 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-7 | 185 | BUY | SELL_UNIT | 59 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-7 | 186 | MOVE_BOARD | SELL_UNIT | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-7 | 187 | MOVE_BOARD | SELL_UNIT | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 3-7 | 188 | PASS | SELL_UNIT | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-1 | 192 | CRAFT_AND_EQUIP | BUY_UNIT | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-1 | 193 | CRAFT_AND_EQUIP | BUY_UNIT | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-1 | 194 | SELL | BUY_UNIT | 37 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-1 | 195 | BUY | BUY_UNIT | 14 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-1 | 196 | SELL | BUY_UNIT | 14 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-1 | 197 | BUY | BUY_UNIT | 14 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-1 | 198 | BUY_XP | BUY_UNIT | 14 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-1 | 199 | BUY_XP | BUY_UNIT | 14 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-1 | 200 | MOVE_BOARD | SELL_UNIT | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-2 | 202 | SELL | BUY_UNIT | 37 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-2 | 203 | BUY | BUY_UNIT | 37 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-2 | 204 | SELL | BUY_UNIT | 37 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-2 | 205 | BUY | BUY_UNIT | 37 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-2 | 206 | BUY | SELL_UNIT | 59 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-2 | 207 | MOVE_BOARD | SELL_UNIT | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-2 | 208 | MOVE_BOARD | SELL_UNIT | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-2 | 209 | PASS | SELL_UNIT | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-3 | 212 | BUY | BUY_UNIT | 19 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-3 | 213 | MOVE_BOARD | BUY_UNIT | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-3 | 214 | MOVE_BOARD | BUY_UNIT | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-3 | 215 | SELL | BUY_UNIT | 14 | 8.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-3 | 216 | BUY | BUY_UNIT | 14 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-3 | 217 | MOVE_BOARD | SELL_UNIT | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-3 | 218 | MOVE_BOARD | SELL_UNIT | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-3 | 219 | PASS | SELL_UNIT | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-4 | 222 | SELL | BUY_UNIT | 40 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-4 | 223 | BUY | BUY_UNIT | 40 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-4 | 224 | SELL | BUY_UNIT | 40 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-4 | 225 | BUY | BUY_UNIT | 40 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-4 | 226 | BUY | SELL_UNIT | 59 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-4 | 227 | MOVE_BOARD | SELL_UNIT | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-4 | 228 | MOVE_BOARD | SELL_UNIT | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-4 | 229 | PASS | SELL_UNIT | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-5 | 232 | BUY | BUY_UNIT | 10 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-5 | 233 | SELL | SELL_UNIT | 59 | 8.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-5 | 234 | BUY | SELL_UNIT | 59 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-5 | 235 | SELL | SELL_UNIT | 59 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-5 | 236 | BUY | SELL_UNIT | 59 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-5 | 237 | MOVE_BOARD | SELL_UNIT | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-5 | 238 | SELL | SELL_UNIT | 59 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-5 | 239 | BUY | SELL_UNIT | 59 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-5 | 240 | MOVE_BOARD | SELL_UNIT | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-6 | 242 | SELL | BUY_UNIT | 46 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-6 | 243 | BUY | BUY_UNIT | 46 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-6 | 244 | SELL | SELL_UNIT | 59 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-6 | 245 | BUY | SELL_UNIT | 59 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-6 | 246 | SELL | SELL_UNIT | 59 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-6 | 247 | BUY | SELL_UNIT | 59 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-6 | 248 | SELL | SELL_UNIT | 59 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-6 | 249 | SELL | SELL_UNIT | 59 | 5.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-6 | 250 | SELL | SELL_UNIT | 2 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-7 | 252 | BUY | BUY_UNIT | 33 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-7 | 253 | BUY | BUY_UNIT | 33 | -3.000 | 0.000 | -6.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-7 | 254 | BUY | DEPLOY_OR_MOVE | 39 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-7 | 255 | SELL | DEPLOY_OR_MOVE | 30 | 8.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-7 | 256 | SELL | DEPLOY_OR_MOVE | 30 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-7 | 257 | SELL | DEPLOY_OR_MOVE | 39 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-7 | 258 | BUY | DEPLOY_OR_MOVE | 39 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-7 | 259 | MOVE_BENCH | DEPLOY_OR_MOVE | 39 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 4-7 | 260 | MOVE_BOARD | SELL_UNIT | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-1 | 262 | BUY | BUY_UNIT | 19 | -3.000 | 0.000 | -6.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-1 | 263 | BUY | BUY_UNIT | 19 | -2.000 | 0.000 | -4.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-1 | 264 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-1 | 265 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-1 | 266 | MOVE_BENCH | DEPLOY_OR_MOVE | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-1 | 267 | MOVE_BENCH | DEPLOY_OR_MOVE | 19 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-1 | 268 | BUY | DEPLOY_OR_MOVE | 19 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-1 | 269 | MOVE_BENCH | DEPLOY_OR_MOVE | 43 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-1 | 270 | BUY | DEPLOY_OR_MOVE | 19 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-2 | 272 | BUY | DEPLOY_OR_MOVE | 19 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-2 | 273 | BUY | DEPLOY_OR_MOVE | 19 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-2 | 274 | BUY | DEPLOY_OR_MOVE | 19 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-2 | 275 | SELL | DEPLOY_OR_MOVE | 19 | 5.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-2 | 276 | BUY | DEPLOY_OR_MOVE | 31 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-2 | 277 | MOVE_BOARD | DEPLOY_OR_MOVE | 31 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-2 | 278 | REROLL | DEPLOY_OR_MOVE | 31 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-2 | 279 | SELL | BUY_UNIT | 12 | 8.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-2 | 280 | MOVE_BENCH | BUY_UNIT | 12 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-3 | 282 | BUY | BUY_UNIT | 14 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-3 | 283 | BUY | BUY_UNIT | 54 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-3 | 284 | EQUIP_FROM_INVENTORY | BUY_UNIT | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-3 | 285 | EQUIP_FROM_INVENTORY | BUY_UNIT | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-3 | 286 | SELL | BUY_UNIT | 41 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-3 | 287 | BUY | BUY_UNIT | 41 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-3 | 288 | REROLL | BUY_UNIT | 41 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-3 | 289 | SELL | BUY_UNIT | 28 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 6 | 5-3 | 290 | BUY | BUY_UNIT | 28 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Feérico → Feérico |
| Jogador 7 | 1-1 | 1 | MOVE_BENCH | HOLD | -1 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 1-1 | 2 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 1-2 | 17 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 1-2 | 18 | BUY | DEPLOY_OR_MOVE | 10 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 1-2 | 19 | MOVE_BOARD | DEPLOY_OR_MOVE | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 1-2 | 20 | MOVE_BENCH | DEPLOY_OR_MOVE | 10 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 1-2 | 21 | MOVE_BOARD | DEPLOY_OR_MOVE | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 1-2 | 22 | MOVE_BOARD | DEPLOY_OR_MOVE | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 1-2 | 23 | PASS | DEPLOY_OR_MOVE | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 1-2 | 25 | MOVE_BENCH | DEPLOY_OR_MOVE | 10 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 1-3 | 28 | BUY | BUY_UNIT | 0 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 1-3 | 29 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 1-3 | 30 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 1-3 | 31 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 1-3 | 32 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 1-3 | 33 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 1-4 | 42 | BUY | BUY_UNIT | 10 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 1-4 | 43 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 1-4 | 44 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 1-4 | 45 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 1-4 | 46 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-1 | 55 | BUY | DEPLOY_OR_MOVE | 0 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-1 | 56 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-1 | 57 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-1 | 58 | BUY | DEPLOY_OR_MOVE | 0 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-1 | 59 | PASS | DEPLOY_OR_MOVE | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-1 | 61 | MOVE_BENCH | DEPLOY_OR_MOVE | 0 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-2 | 64 | BUY | BUY_UNIT | 0 | -1.000 | 0.000 | -4.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-2 | 65 | BUY_XP | DEPLOY_OR_MOVE | 10 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-2 | 66 | MOVE_BENCH | DEPLOY_OR_MOVE | 10 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-2 | 67 | BUY | DEPLOY_OR_MOVE | 10 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-2 | 68 | MOVE_BOARD | DEPLOY_OR_MOVE | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-2 | 69 | MOVE_BOARD | DEPLOY_OR_MOVE | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-2 | 70 | SELL | DEPLOY_OR_MOVE | 10 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-3 | 72 | BUY | BUY_UNIT | 10 | -1.000 | 0.000 | -2.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-3 | 73 | BUY | DEPLOY_OR_MOVE | 13 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-3 | 74 | EQUIP_FROM_INVENTORY | DEPLOY_OR_MOVE | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-3 | 75 | EQUIP_FROM_INVENTORY | DEPLOY_OR_MOVE | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-3 | 76 | BUY | DEPLOY_OR_MOVE | 13 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-3 | 77 | PASS | DEPLOY_OR_MOVE | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-4 | 82 | BUY | DEPLOY_OR_MOVE | 28 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-4 | 83 | BUY | DEPLOY_OR_MOVE | 28 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-4 | 84 | SELL | DEPLOY_OR_MOVE | 44 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-4 | 85 | BUY_XP | DEPLOY_OR_MOVE | 44 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-4 | 86 | MOVE_BOARD | DEPLOY_OR_MOVE | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-4 | 87 | SELL | DEPLOY_OR_MOVE | 44 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-4 | 88 | BUY | DEPLOY_OR_MOVE | 44 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-4 | 89 | SELL | DEPLOY_OR_MOVE | 44 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-4 | 90 | MOVE_BOARD | DEPLOY_OR_MOVE | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 7 | 2-5 | 92 | BUY | DEPLOY_OR_MOVE | 44 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → Colosso |
| Jogador 7 | 2-5 | 93 | BUY | DEPLOY_OR_MOVE | 44 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-5 | 94 | BUY_XP | DEPLOY_OR_MOVE | 44 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-5 | 95 | SELL | DEPLOY_OR_MOVE | 44 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-5 | 96 | SELL | DEPLOY_OR_MOVE | 44 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-5 | 97 | PASS | DEPLOY_OR_MOVE | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-6 | 102 | BUY | BUY_UNIT | 7 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-6 | 103 | BUY | BUY_UNIT | 33 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-6 | 104 | BUY_XP | SELL_UNIT | 44 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-6 | 105 | SELL | SELL_UNIT | 44 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-6 | 106 | SELL | SELL_UNIT | 44 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-6 | 107 | BUY_XP | BUY_UNIT | 24 | -4.000 | 0.000 | 0.000 | 1.000 | -16.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-6 | 108 | SELL | DEPLOY_OR_MOVE | 44 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-6 | 109 | BUY_XP | DEPLOY_OR_MOVE | 7 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-6 | 110 | MOVE_BOARD | DEPLOY_OR_MOVE | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-7 | 112 | BUY | DEPLOY_OR_MOVE | 7 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-7 | 113 | BUY_XP | DEPLOY_OR_MOVE | 7 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-7 | 114 | SELL | DEPLOY_OR_MOVE | 7 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-7 | 115 | BUY | DEPLOY_OR_MOVE | 7 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-7 | 116 | SELL | DEPLOY_OR_MOVE | 7 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-7 | 117 | BUY_XP | DEPLOY_OR_MOVE | 7 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-7 | 118 | SELL | DEPLOY_OR_MOVE | 7 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-7 | 119 | MOVE_BOARD | DEPLOY_OR_MOVE | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 2-7 | 120 | MOVE_BOARD | DEPLOY_OR_MOVE | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-1 | 122 | BUY | DEPLOY_OR_MOVE | 33 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-1 | 123 | CRAFT_AND_EQUIP | DEPLOY_OR_MOVE | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-1 | 124 | BUY_XP | DEPLOY_OR_MOVE | 33 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-1 | 125 | SELL | DEPLOY_OR_MOVE | 33 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-1 | 126 | BUY | DEPLOY_OR_MOVE | 33 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-1 | 127 | MOVE_BOARD | DEPLOY_OR_MOVE | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-1 | 128 | SELL | DEPLOY_OR_MOVE | 33 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-1 | 129 | BUY | DEPLOY_OR_MOVE | 33 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-1 | 130 | BUY | DEPLOY_OR_MOVE | 33 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-2 | 132 | BUY | DEPLOY_OR_MOVE | 13 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-2 | 133 | BUY | DEPLOY_OR_MOVE | 13 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-2 | 134 | SELL | DEPLOY_OR_MOVE | 13 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-2 | 135 | BUY | DEPLOY_OR_MOVE | 33 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-2 | 136 | SELL | DEPLOY_OR_MOVE | 33 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-2 | 137 | SELL | DEPLOY_OR_MOVE | 33 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-2 | 138 | BUY | DEPLOY_OR_MOVE | 33 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-2 | 139 | SELL | DEPLOY_OR_MOVE | 33 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-2 | 140 | BUY_XP | DEPLOY_OR_MOVE | 33 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-3 | 142 | BUY | DEPLOY_OR_MOVE | 33 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-3 | 143 | BUY | DEPLOY_OR_MOVE | 33 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-3 | 144 | BUY | DEPLOY_OR_MOVE | 12 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-3 | 145 | SELL | DEPLOY_OR_MOVE | 18 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-3 | 146 | SELL | DEPLOY_OR_MOVE | 18 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-3 | 147 | SELL | DEPLOY_OR_MOVE | 33 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-3 | 148 | BUY | DEPLOY_OR_MOVE | 33 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-3 | 149 | BUY_XP | DEPLOY_OR_MOVE | 33 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-3 | 150 | SELL | DEPLOY_OR_MOVE | 33 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-4 | 152 | BUY | BUY_UNIT | 33 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-4 | 153 | BUY | DEPLOY_OR_MOVE | 7 | -3.000 | 0.000 | -6.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-4 | 154 | SELL | DEPLOY_OR_MOVE | 7 | 8.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-4 | 155 | BUY_XP | DEPLOY_OR_MOVE | 7 | -4.000 | 0.000 | 0.000 | 1.000 | -32.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-4 | 156 | MOVE_BENCH | DEPLOY_OR_MOVE | 7 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-4 | 157 | BUY | DEPLOY_OR_MOVE | 7 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-4 | 158 | MOVE_BENCH | DEPLOY_OR_MOVE | 29 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-4 | 159 | BUY | DEPLOY_OR_MOVE | 7 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-4 | 160 | MOVE_BOARD | DEPLOY_OR_MOVE | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-5 | 162 | BUY | DEPLOY_OR_MOVE | 7 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-5 | 163 | BUY | DEPLOY_OR_MOVE | 7 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-5 | 164 | BUY | DEPLOY_OR_MOVE | 7 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-5 | 165 | MOVE_BOARD | DEPLOY_OR_MOVE | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-5 | 166 | MOVE_BOARD | DEPLOY_OR_MOVE | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-5 | 167 | MOVE_BOARD | DEPLOY_OR_MOVE | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-5 | 168 | PASS | DEPLOY_OR_MOVE | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-6 | 172 | BUY | SELL_UNIT | 30 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-6 | 173 | BUY | SELL_UNIT | 44 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-6 | 174 | MOVE_BOARD | SELL_UNIT | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-6 | 175 | MOVE_BOARD | SELL_UNIT | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-6 | 176 | PASS | SELL_UNIT | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-7 | 182 | BUY | BUY_UNIT | 44 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-7 | 183 | SELL | BUY_UNIT | 15 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-7 | 184 | BUY | BUY_UNIT | 15 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-7 | 185 | MOVE_BOARD | SELL_UNIT | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-7 | 186 | MOVE_BOARD | SELL_UNIT | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 3-7 | 187 | PASS | SELL_UNIT | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-1 | 192 | CRAFT_AND_EQUIP | SELL_UNIT | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-1 | 193 | CRAFT_AND_EQUIP | SELL_UNIT | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-1 | 194 | SELL | SELL_UNIT | 30 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-1 | 195 | BUY | SELL_UNIT | 30 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-1 | 196 | SELL | SELL_UNIT | 30 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-1 | 197 | BUY | HOLD | -1 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-1 | 198 | MOVE_BOARD | SELL_UNIT | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-1 | 199 | MOVE_BOARD | SELL_UNIT | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-1 | 200 | PASS | SELL_UNIT | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-2 | 202 | SELL | BUY_UNIT | 17 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-2 | 203 | BUY | BUY_UNIT | 17 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-2 | 204 | SELL | BUY_UNIT | 22 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-2 | 205 | BUY | BUY_UNIT | 22 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-2 | 206 | MOVE_BOARD | BUY_UNIT | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-2 | 207 | MOVE_BOARD | BUY_UNIT | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-2 | 208 | MOVE_BOARD | BUY_UNIT | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-2 | 209 | PASS | BUY_UNIT | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-3 | 212 | SELL | HOLD | -1 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-3 | 213 | BUY | SELL_UNIT | 38 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-3 | 214 | SELL | SELL_UNIT | 53 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-3 | 215 | BUY | SELL_UNIT | 53 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-3 | 216 | MOVE_BOARD | SELL_UNIT | 53 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-3 | 217 | MOVE_BOARD | SELL_UNIT | 53 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-3 | 218 | PASS | SELL_UNIT | 53 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-4 | 222 | SELL | BUY_UNIT | 31 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-4 | 223 | BUY | BUY_UNIT | 31 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-4 | 224 | SELL | BUY_UNIT | 17 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-4 | 225 | BUY | BUY_UNIT | 17 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-4 | 226 | MOVE_BOARD | BUY_UNIT | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-4 | 227 | MOVE_BOARD | BUY_UNIT | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-4 | 228 | MOVE_BOARD | BUY_UNIT | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-4 | 229 | PASS | BUY_UNIT | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-5 | 232 | SELL | BUY_UNIT | 29 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-5 | 233 | BUY | BUY_UNIT | 29 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-5 | 234 | SELL | SELL_UNIT | 35 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-5 | 235 | BUY | SELL_UNIT | 35 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-5 | 236 | SELL | SELL_UNIT | 45 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-5 | 237 | BUY | SELL_UNIT | 35 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-5 | 238 | MOVE_BOARD | SELL_UNIT | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-5 | 239 | MOVE_BOARD | SELL_UNIT | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-5 | 240 | PASS | SELL_UNIT | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-6 | 242 | SELL | BUY_UNIT | 7 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-6 | 243 | BUY | BUY_UNIT | 7 | -1.000 | 0.000 | -2.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-6 | 244 | BUY | DEPLOY_OR_MOVE | 44 | -3.000 | 0.000 | -6.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-6 | 245 | MOVE_BENCH | DEPLOY_OR_MOVE | 44 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 1.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-6 | 246 | BUY | DEPLOY_OR_MOVE | 44 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-6 | 247 | MOVE_BOARD | DEPLOY_OR_MOVE | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-6 | 248 | MOVE_BOARD | DEPLOY_OR_MOVE | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-6 | 249 | MOVE_BENCH | DEPLOY_OR_MOVE | 44 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-6 | 250 | MOVE_BOARD | SELL_UNIT | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-7 | 252 | BUY | BUY_UNIT | 15 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-7 | 253 | BUY | BUY_UNIT | 18 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-7 | 254 | MOVE_BOARD | BUY_UNIT | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-7 | 255 | MOVE_BOARD | BUY_UNIT | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 4-7 | 256 | PASS | BUY_UNIT | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-1 | 262 | CRAFT_AND_EQUIP | BUY_UNIT | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-1 | 263 | CRAFT_AND_EQUIP | BUY_UNIT | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-1 | 264 | SELL | BUY_UNIT | 18 | 8.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-1 | 265 | BUY | BUY_UNIT | 18 | -5.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-1 | 266 | MOVE_BOARD | BUY_UNIT | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-1 | 267 | SELL | BUY_UNIT | 18 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-1 | 268 | BUY | BUY_UNIT | 18 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-1 | 269 | MOVE_BOARD | SELL_UNIT | 56 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-1 | 270 | MOVE_BOARD | SELL_UNIT | 56 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-2 | 272 | SELL | BUY_UNIT | 18 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-2 | 273 | BUY | BUY_UNIT | 21 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-2 | 274 | SELL | BUY_UNIT | 18 | 5.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-2 | 275 | BUY | BUY_UNIT | 18 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-2 | 276 | SELL | BUY_UNIT | 18 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-2 | 277 | BUY | BUY_UNIT | 18 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-2 | 278 | MOVE_BOARD | SELL_UNIT | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-2 | 279 | MOVE_BOARD | SELL_UNIT | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-2 | 280 | MOVE_BOARD | SELL_UNIT | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-3 | 282 | SELL | BUY_UNIT | 5 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-3 | 283 | BUY | BUY_UNIT | 5 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-3 | 284 | SELL | BUY_UNIT | 23 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-3 | 285 | BUY | BUY_UNIT | 5 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-3 | 286 | MOVE_BOARD | BUY_UNIT | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-3 | 287 | SELL | BUY_UNIT | 5 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-3 | 288 | BUY | BUY_UNIT | 5 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-3 | 289 | MOVE_BOARD | BUY_UNIT | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-3 | 290 | MOVE_BOARD | BUY_UNIT | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-4 | 292 | SELL | BUY_UNIT | 15 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-4 | 293 | BUY | BUY_UNIT | 15 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-4 | 294 | BUY | BUY_UNIT | 18 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-4 | 295 | BUY | BUY_UNIT | 18 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-4 | 296 | SELL | BUY_UNIT | 18 | 5.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-4 | 297 | BUY | BUY_UNIT | 18 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-4 | 298 | MOVE_BOARD | SELL_UNIT | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-4 | 299 | SELL | SELL_UNIT | 51 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-4 | 300 | BUY | SELL_UNIT | 51 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-5 | 302 | SELL | BUY_UNIT | 40 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-5 | 303 | BUY | BUY_UNIT | 40 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-5 | 304 | SELL | SELL_UNIT | 51 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-5 | 305 | BUY | BUY_UNIT | 37 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-5 | 306 | SELL | BUY_UNIT | 37 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-5 | 307 | BUY | BUY_UNIT | 37 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-5 | 308 | SELL | BUY_UNIT | 37 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-5 | 309 | BUY | BUY_UNIT | 37 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 7 | 5-5 | 310 | MOVE_BOARD | BUY_UNIT | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Colosso → Colosso |
| Jogador 8 | 1-1 | 1 | MOVE_BENCH | HOLD | -1 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 1-1 | 2 | MOVE_BOARD | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 1-1 | 3 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 1-2 | 17 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 1-2 | 18 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 1-2 | 19 | MOVE_BENCH | DEPLOY_OR_MOVE | 11 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 1-2 | 20 | MOVE_BOARD | DEPLOY_OR_MOVE | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 1-2 | 21 | MOVE_BOARD | DEPLOY_OR_MOVE | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 1-2 | 22 | PASS | DEPLOY_OR_MOVE | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 1-2 | 25 | MOVE_BENCH | DEPLOY_OR_MOVE | 11 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 1-3 | 28 | BUY | BUY_UNIT | 3 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 1-3 | 29 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 1-3 | 30 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 1-4 | 42 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 1-4 | 43 | BUY | BUY_UNIT | 12 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 1-4 | 44 | SELL | HOLD | -1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 1-4 | 45 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 1-4 | 46 | SELL | HOLD | -1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 1-4 | 47 | PASS | HOLD | -1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-1 | 55 | BUY | BUY_UNIT | 3 | -1.000 | 0.000 | -2.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-1 | 56 | CRAFT_AND_EQUIP | BUY_UNIT | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-1 | 57 | CRAFT_AND_EQUIP | BUY_UNIT | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-1 | 58 | MOVE_BENCH | BUY_UNIT | 12 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 1.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-1 | 59 | BUY | BUY_UNIT | 12 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-1 | 60 | BUY | DEPLOY_OR_MOVE | 12 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-1 | 61 | MOVE_BENCH | DEPLOY_OR_MOVE | 12 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 1.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-1 | 62 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-2 | 64 | BUY | HOLD | -1 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-2 | 65 | BUY | HOLD | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-2 | 66 | BUY | HOLD | -1 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-2 | 67 | MOVE_BOARD | SELL_UNIT | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-2 | 68 | SELL | SELL_UNIT | 34 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-2 | 69 | MOVE_BENCH | SELL_UNIT | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-2 | 70 | MOVE_BENCH | SELL_UNIT | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-3 | 72 | BUY | BUY_UNIT | 3 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-3 | 73 | BUY | BUY_UNIT | 11 | -1.000 | 0.000 | -2.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-3 | 74 | BUY | BUY_UNIT | 3 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-3 | 75 | MOVE_BENCH | DEPLOY_OR_MOVE | 11 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 1.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-3 | 76 | BUY | SELL_UNIT | 34 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-3 | 77 | SELL | SELL_UNIT | 28 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-3 | 78 | BUY_XP | SELL_UNIT | 28 | -4.000 | 0.000 | 0.000 | 0.000 | 4.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-3 | 79 | MOVE_BOARD | SELL_UNIT | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-3 | 80 | MOVE_BOARD | SELL_UNIT | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-4 | 82 | BUY | DEPLOY_OR_MOVE | 3 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-4 | 83 | BUY | DEPLOY_OR_MOVE | 3 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-4 | 84 | MOVE_BENCH | DEPLOY_OR_MOVE | 3 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-4 | 85 | SELL | SELL_UNIT | 34 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-4 | 86 | BUY | SELL_UNIT | 34 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-4 | 87 | SELL | SELL_UNIT | 34 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-4 | 88 | BUY | SELL_UNIT | 34 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-4 | 89 | MOVE_BENCH | SELL_UNIT | 34 | 0.000 | 0.000 | -4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-4 | 90 | MOVE_BENCH | SELL_UNIT | 28 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → — |
| Jogador 8 | 2-5 | 92 | BUY | BUY_UNIT | 3 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | — → Enfeitiçador |
| Jogador 8 | 2-5 | 93 | BUY | SELL_UNIT | 34 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-5 | 94 | BUY | SELL_UNIT | 34 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-5 | 95 | SELL | SELL_UNIT | 34 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-5 | 96 | SELL | SELL_UNIT | 34 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-5 | 97 | SELL | SELL_UNIT | 36 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-5 | 98 | SELL | SELL_UNIT | 37 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-5 | 99 | SELL | SELL_UNIT | 37 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-5 | 100 | BUY | HOLD | -1 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-6 | 102 | BUY | HOLD | -1 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-6 | 103 | BUY | SELL_UNIT | 39 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-6 | 104 | BUY | SELL_UNIT | 39 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-6 | 105 | MOVE_BENCH | SELL_UNIT | 39 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-6 | 106 | SELL | SELL_UNIT | 29 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-6 | 107 | MOVE_BENCH | SELL_UNIT | 29 | 0.000 | 0.000 | -4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-6 | 108 | MOVE_BENCH | SELL_UNIT | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-6 | 109 | SELL | SELL_UNIT | 39 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-6 | 110 | SELL | SELL_UNIT | 39 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-7 | 112 | BUY | BUY_UNIT | 39 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-7 | 113 | BUY | BUY_UNIT | 40 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-7 | 114 | BUY | SELL_UNIT | 40 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-7 | 115 | SELL | SELL_UNIT | 40 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-7 | 116 | SELL | SELL_UNIT | 40 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-7 | 117 | BUY | SELL_UNIT | 4 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-7 | 118 | SELL | SELL_UNIT | 0 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-7 | 119 | SELL | SELL_UNIT | 4 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 2-7 | 120 | SELL | SELL_UNIT | 39 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-1 | 122 | BUY | BUY_UNIT | 46 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-1 | 123 | CRAFT_AND_EQUIP | SELL_UNIT | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-1 | 124 | BUY | SELL_UNIT | 46 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-1 | 125 | MOVE_BENCH | SELL_UNIT | 46 | 0.000 | 0.000 | -2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-1 | 126 | MOVE_BENCH | SELL_UNIT | 46 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-1 | 127 | PASS | SELL_UNIT | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-2 | 132 | BUY | SELL_UNIT | 46 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-2 | 133 | BUY | SELL_UNIT | 46 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-2 | 134 | MOVE_BENCH | SELL_UNIT | 46 | 0.000 | 0.000 | -2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-2 | 135 | MOVE_BENCH | SELL_UNIT | 46 | 0.000 | 0.000 | -2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-2 | 136 | MOVE_BENCH | SELL_UNIT | 46 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-2 | 137 | MOVE_BENCH | SELL_UNIT | 46 | 0.000 | 0.000 | -2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-2 | 138 | MOVE_BENCH | SELL_UNIT | 46 | 0.000 | 0.000 | -2.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-2 | 139 | MOVE_BENCH | SELL_UNIT | 46 | 0.000 | 0.000 | 2.000 | 0.000 | 0.000 | 0.000 | -1.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-2 | 140 | PASS | SELL_UNIT | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-3 | 142 | BUY | BUY_UNIT | 12 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-3 | 143 | SELL | BUY_UNIT | 0 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-3 | 144 | BUY | BUY_UNIT | 0 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-3 | 145 | EQUIP_FROM_INVENTORY | SELL_UNIT | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-3 | 146 | SELL | SELL_UNIT | 46 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-3 | 147 | SELL | SELL_UNIT | 46 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-3 | 148 | BUY | HOLD | -1 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-3 | 149 | SELL | HOLD | -1 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-3 | 150 | SELL | HOLD | -1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-4 | 152 | BUY | BUY_UNIT | 3 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-4 | 153 | BUY | BUY_UNIT | 4 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-4 | 154 | SELL | SELL_UNIT | 0 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-4 | 155 | BUY | SELL_UNIT | 0 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-4 | 156 | SELL | SELL_UNIT | 35 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-4 | 157 | SELL | SELL_UNIT | 35 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-4 | 158 | SELL | SELL_UNIT | 17 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-4 | 159 | SELL | SELL_UNIT | 17 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-4 | 160 | SELL | SELL_UNIT | 17 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-5 | 162 | BUY | BUY_UNIT | 28 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-5 | 163 | BUY | BUY_UNIT | 20 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-5 | 164 | BUY | BUY_UNIT | 20 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-5 | 165 | BUY | SELL_UNIT | 25 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-5 | 166 | SELL | SELL_UNIT | 26 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-5 | 167 | SELL | SELL_UNIT | 25 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-5 | 168 | SELL | BUY_XP | -1 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-5 | 169 | SELL | BUY_XP | -1 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-5 | 170 | BUY | BUY_XP | -1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-6 | 172 | BUY | BUY_UNIT | 17 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-6 | 173 | BUY | BUY_UNIT | 17 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-6 | 174 | BUY | BUY_XP | -1 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-6 | 175 | SELL | BUY_XP | -1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-6 | 176 | SELL | BUY_XP | -1 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-6 | 177 | BUY | BUY_XP | -1 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-6 | 178 | SELL | BUY_XP | -1 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-6 | 179 | SELL | BUY_XP | -1 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-6 | 180 | SELL | BUY_XP | -1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-7 | 182 | BUY | DEPLOY_OR_MOVE | 28 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-7 | 183 | BUY | DEPLOY_OR_MOVE | 28 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-7 | 184 | BUY | DEPLOY_OR_MOVE | 28 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-7 | 185 | BUY | DEPLOY_OR_MOVE | 28 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-7 | 186 | MOVE_BENCH | DEPLOY_OR_MOVE | 28 | 0.000 | 0.000 | 4.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-7 | 187 | BUY | BUY_UNIT | 6 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-7 | 188 | MOVE_BOARD | SELL_UNIT | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-7 | 189 | MOVE_BOARD | SELL_UNIT | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 3-7 | 190 | MOVE_BOARD | SELL_UNIT | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-1 | 192 | BUY | BUY_UNIT | 11 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-1 | 193 | BUY | BUY_UNIT | 16 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-1 | 194 | BUY | BUY_UNIT | 8 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-1 | 195 | BUY | SELL_UNIT | 27 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-1 | 196 | CRAFT_AND_EQUIP | SELL_UNIT | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-1 | 197 | CRAFT_AND_EQUIP | SELL_UNIT | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-1 | 198 | SELL | SELL_UNIT | 27 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-1 | 199 | BUY | SELL_UNIT | 27 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-1 | 200 | SELL | SELL_UNIT | 27 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-2 | 202 | BUY | BUY_UNIT | 17 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-2 | 203 | SELL | BUY_UNIT | 17 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-2 | 204 | BUY | BUY_UNIT | 17 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-2 | 205 | SELL | SELL_UNIT | 27 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-2 | 206 | BUY | SELL_UNIT | 27 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-2 | 207 | SELL | SELL_UNIT | 27 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-2 | 208 | BUY | SELL_UNIT | 27 | -4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-2 | 209 | SELL | SELL_UNIT | 52 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-2 | 210 | BUY | SELL_UNIT | 52 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-3 | 212 | SELL | BUY_UNIT | 20 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-3 | 213 | BUY | BUY_UNIT | 20 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-3 | 214 | SELL | BUY_UNIT | 29 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-3 | 215 | BUY | BUY_UNIT | 29 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-3 | 216 | SELL | SELL_UNIT | 52 | 4.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-3 | 217 | BUY | BUY_UNIT | 2 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-3 | 218 | SELL | BUY_UNIT | 24 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-3 | 219 | BUY | BUY_UNIT | 2 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-3 | 220 | SELL | BUY_UNIT | 2 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-4 | 222 | BUY | BUY_UNIT | 12 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-4 | 223 | SELL | BUY_UNIT | 12 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-4 | 224 | BUY | BUY_UNIT | 12 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-4 | 225 | SELL | BUY_UNIT | 30 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-4 | 226 | BUY | BUY_UNIT | 30 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-4 | 227 | SELL | BUY_UNIT | 1 | 2.000 | 0.000 | 0.000 | 0.000 | 0.000 | -1.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-4 | 228 | BUY | BUY_UNIT | 1 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-4 | 229 | SELL | BUY_UNIT | 6 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-4 | 230 | BUY | BUY_UNIT | 6 | -1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-5 | 232 | SELL | BUY_UNIT | 7 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-5 | 233 | BUY | BUY_UNIT | 7 | -1.000 | 0.000 | -2.000 | 0.000 | 0.000 | -1.000 | 0.0 / 1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-5 | 234 | BUY | DEPLOY_OR_MOVE | 28 | -3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-5 | 235 | MOVE_BENCH | DEPLOY_OR_MOVE | 28 | 0.000 | 0.000 | 6.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-5 | 236 | BUY | BUY_UNIT | 24 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-5 | 237 | SELL | BUY_UNIT | 19 | 3.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / -1.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-5 | 238 | EQUIP_FROM_INVENTORY | BUY_UNIT | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-5 | 239 | EQUIP_FROM_INVENTORY | BUY_UNIT | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |
| Jogador 8 | 4-5 | 240 | BUY | BUY_UNIT | 19 | -2.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | Enfeitiçador → Enfeitiçador |

## Resultado de combate (uma linha por jogador e round)

| Jogador | Round | HP fim round | Ouro | Board power | Nível | Win streak | Loss streak | Recompensa combate | Colocação | Vivo no snapshot |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Jogador 1 | 1-1 | 100.000 | 2 | 2.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 1 | 1-2 | 100.000 | 2 | 6.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 1 | 1-3 | 100.000 | 3 | 6.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 1 | 1-4 | 100.000 | 5 | 6.000 | 4 | 0 | 0 | 0.000 | — | True |
| Jogador 1 | 2-1 | 100.000 | 6 | 8.000 | 4 | 1 | 0 | 2.562 | — | True |
| Jogador 1 | 2-2 | 100.000 | 10 | 10.000 | 5 | 2 | 0 | 2.637 | — | True |
| Jogador 1 | 2-3 | 100.000 | 7 | 10.000 | 5 | 3 | 0 | 2.462 | — | True |
| Jogador 1 | 2-4 | 100.000 | 8 | 14.000 | 5 | 3 | 0 | 0.000 | — | True |
| Jogador 1 | 2-5 | 100.000 | 8 | 20.000 | 6 | 4 | 0 | 2.854 | — | True |
| Jogador 1 | 2-6 | 100.000 | 9 | 24.000 | 6 | 5 | 0 | 2.754 | — | True |
| Jogador 1 | 2-7 | 100.000 | 9 | 24.000 | 6 | 5 | 0 | 0.000 | — | True |
| Jogador 1 | 3-1 | 100.000 | 10 | 28.000 | 6 | 6 | 0 | 2.912 | — | True |
| Jogador 1 | 3-2 | 100.000 | 11 | 28.000 | 6 | 7 | 0 | 2.812 | — | True |
| Jogador 1 | 3-3 | 100.000 | 9 | 28.000 | 6 | 8 | 0 | 2.716 | — | True |
| Jogador 1 | 3-4 | 100.000 | 8 | 28.000 | 7 | 8 | 0 | 0.000 | — | True |
| Jogador 1 | 3-5 | 100.000 | 9 | 32.000 | 7 | 9 | 0 | 3.000 | — | True |
| Jogador 1 | 3-6 | 100.000 | 11 | 32.000 | 7 | 10 | 0 | 3.084 | — | True |
| Jogador 1 | 3-7 | 100.000 | 22 | 32.000 | 7 | 10 | 0 | 0.000 | — | True |
| Jogador 1 | 4-1 | 100.000 | 32 | 32.000 | 7 | 11 | 0 | 2.984 | — | True |
| Jogador 1 | 4-2 | 100.000 | 45 | 32.000 | 7 | 12 | 0 | 3.084 | — | True |
| Jogador 1 | 4-3 | 100.000 | 55 | 36.000 | 7 | 13 | 0 | 3.135 | — | True |
| Jogador 1 | 4-4 | 100.000 | 61 | 36.000 | 7 | 13 | 0 | 0.000 | — | True |
| Jogador 1 | 4-5 | 88.000 | 70 | 36.000 | 7 | 0 | 1 | -2.714 | — | True |
| Jogador 1 | 4-6 | 88.000 | 57 | 32.000 | 8 | 1 | 0 | 2.762 | — | True |
| Jogador 1 | 4-7 | 88.000 | 28 | 32.000 | 8 | 1 | 0 | 0.000 | — | True |
| Jogador 1 | 5-1 | 73.000 | 34 | 28.000 | 8 | 0 | 1 | -2.800 | — | True |
| Jogador 1 | 5-2 | 73.000 | 35 | 42.000 | 8 | 1 | 0 | 3.147 | — | True |
| Jogador 1 | 5-3 | 73.000 | 41 | 38.000 | 8 | 2 | 0 | 3.005 | — | True |
| Jogador 1 | 5-4 | 73.000 | 44 | 40.000 | 8 | 2 | 0 | 0.000 | — | True |
| Jogador 1 | 5-5 | 73.000 | 50 | 40.000 | 8 | 3 | 0 | 2.955 | — | True |
| Jogador 1 | 5-6 | 73.000 | 61 | 40.000 | 9 | 3 | 0 | 0.000 | — | True |
| Jogador 1 | 5-7 | 73.000 | 72 | 50.000 | 9 | 3 | 0 | 0.000 | — | True |
| Jogador 1 | 6-1 | 73.000 | 74 | 50.000 | 9 | 4 | 0 | 3.056 | — | True |
| Jogador 1 | 6-2 | 73.000 | 63 | 46.000 | 9 | 5 | 0 | 3.097 | — | True |
| Jogador 1 | 6-3 | 73.000 | 38 | 46.000 | 10 | 6 | 0 | 3.085 | — | True |
| Jogador 1 | 6-4 | 73.000 | 49 | 62.000 | 10 | 6 | 0 | 0.000 | — | True |
| Jogador 1 | 6-5 | 73.000 | 58 | 70.000 | 10 | 7 | 0 | 3.120 | — | True |
| Jogador 1 | 6-6 | 73.000 | 56 | 76.000 | 10 | 8 | 0 | 3.147 | 1 | True |
| Jogador 2 | 1-1 | 100.000 | 2 | 2.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 2 | 1-2 | 100.000 | 2 | 6.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 2 | 1-3 | 100.000 | 3 | 6.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 2 | 1-4 | 100.000 | 4 | 8.000 | 4 | 0 | 0 | 0.000 | — | True |
| Jogador 2 | 2-1 | 96.000 | 5 | 10.000 | 4 | 0 | 1 | -2.311 | — | True |
| Jogador 2 | 2-2 | 90.000 | 6 | 10.000 | 4 | 0 | 2 | -2.480 | — | True |
| Jogador 2 | 2-3 | 85.000 | 7 | 12.000 | 5 | 0 | 3 | -2.322 | — | True |
| Jogador 2 | 2-4 | 85.000 | 7 | 16.000 | 5 | 0 | 3 | 0.000 | — | True |
| Jogador 2 | 2-5 | 79.000 | 7 | 16.000 | 5 | 0 | 4 | -2.530 | — | True |
| Jogador 2 | 2-6 | 72.000 | 7 | 18.000 | 6 | 0 | 5 | -2.536 | — | True |
| Jogador 2 | 2-7 | 72.000 | 10 | 24.000 | 6 | 0 | 5 | 0.000 | — | True |
| Jogador 2 | 3-1 | 62.000 | 10 | 24.000 | 6 | 0 | 6 | -2.633 | — | True |
| Jogador 2 | 3-2 | 62.000 | 9 | 24.000 | 6 | 1 | 0 | 2.812 | — | True |
| Jogador 2 | 3-3 | 62.000 | 15 | 24.000 | 6 | 2 | 0 | 2.812 | — | True |
| Jogador 2 | 3-4 | 62.000 | 18 | 24.000 | 6 | 2 | 0 | 0.000 | — | True |
| Jogador 2 | 3-5 | 62.000 | 20 | 24.000 | 6 | 3 | 0 | 2.762 | — | True |
| Jogador 2 | 3-6 | 62.000 | 25 | 24.000 | 7 | 4 | 0 | 2.762 | — | True |
| Jogador 2 | 3-7 | 62.000 | 32 | 24.000 | 7 | 4 | 0 | 0.000 | — | True |
| Jogador 2 | 4-1 | 62.000 | 25 | 26.000 | 7 | 5 | 0 | 2.884 | — | True |
| Jogador 2 | 4-2 | 62.000 | 31 | 26.000 | 7 | 6 | 0 | 2.762 | — | True |
| Jogador 2 | 4-3 | 49.000 | 42 | 26.000 | 7 | 0 | 1 | -2.850 | — | True |
| Jogador 2 | 4-4 | 49.000 | 51 | 26.000 | 7 | 0 | 1 | 0.000 | — | True |
| Jogador 2 | 4-5 | 49.000 | 62 | 26.000 | 7 | 1 | 0 | 2.884 | — | True |
| Jogador 2 | 4-6 | 39.000 | 73 | 28.000 | 7 | 0 | 1 | -2.583 | — | True |
| Jogador 2 | 4-7 | 39.000 | 79 | 28.000 | 7 | 0 | 1 | 0.000 | — | True |
| Jogador 2 | 5-1 | 39.000 | 86 | 34.000 | 7 | 0 | 1 | 0.000 | — | True |
| Jogador 2 | 5-2 | 39.000 | 95 | 34.000 | 7 | 1 | 0 | 2.962 | — | True |
| Jogador 2 | 5-3 | 39.000 | 94 | 32.000 | 7 | 1 | 0 | 0.000 | — | True |
| Jogador 2 | 5-4 | 39.000 | 99 | 42.000 | 8 | 1 | 0 | 0.000 | — | True |
| Jogador 2 | 5-5 | 24.000 | 99 | 52.000 | 8 | 0 | 1 | -2.800 | — | True |
| Jogador 2 | 5-6 | 24.000 | 109 | 52.000 | 8 | 1 | 0 | 3.005 | — | True |
| Jogador 2 | 5-7 | 24.000 | 120 | 52.000 | 8 | 1 | 0 | 0.000 | — | True |
| Jogador 2 | 6-1 | 24.000 | 130 | 52.000 | 8 | 1 | 0 | 0.000 | — | True |
| Jogador 2 | 6-2 | 24.000 | 143 | 52.000 | 8 | 1 | 0 | 0.000 | — | True |
| Jogador 2 | 6-3 | 24.000 | 153 | 52.000 | 8 | 1 | 0 | 0.000 | — | True |
| Jogador 2 | 6-4 | 24.000 | 145 | 52.000 | 8 | 1 | 0 | 0.000 | — | True |
| Jogador 2 | 6-5 | 3.000 | 160 | 50.000 | 8 | 0 | 1 | -2.900 | — | True |
| Jogador 2 | 6-6 | 0.000 | 156 | 0.000 | 8 | 0 | 2 | -2.950 | 2 | False |
| Jogador 3 | 1-1 | 100.000 | 2 | 2.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 3 | 1-2 | 100.000 | 2 | 6.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 3 | 1-3 | 100.000 | 3 | 8.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 3 | 1-4 | 100.000 | 4 | 8.000 | 4 | 0 | 0 | 0.000 | — | True |
| Jogador 3 | 2-1 | 100.000 | 6 | 12.000 | 4 | 1 | 0 | 2.562 | — | True |
| Jogador 3 | 2-2 | 100.000 | 8 | 12.000 | 4 | 2 | 0 | 2.380 | — | True |
| Jogador 3 | 2-3 | 100.000 | 8 | 12.000 | 5 | 3 | 0 | 2.512 | — | True |
| Jogador 3 | 2-4 | 100.000 | 6 | 18.000 | 5 | 3 | 0 | 0.000 | — | True |
| Jogador 3 | 2-5 | 100.000 | 8 | 18.000 | 5 | 4 | 0 | 2.804 | — | True |
| Jogador 3 | 2-6 | 100.000 | 8 | 24.000 | 5 | 5 | 0 | 2.704 | — | True |
| Jogador 3 | 2-7 | 100.000 | 11 | 24.000 | 6 | 5 | 0 | 0.000 | — | True |
| Jogador 3 | 3-1 | 100.000 | 16 | 26.000 | 6 | 6 | 0 | 2.812 | — | True |
| Jogador 3 | 3-2 | 90.000 | 17 | 32.000 | 6 | 0 | 1 | -2.633 | — | True |
| Jogador 3 | 3-3 | 90.000 | 18 | 32.000 | 6 | 1 | 0 | 2.934 | — | True |
| Jogador 3 | 3-4 | 90.000 | 24 | 30.000 | 6 | 1 | 0 | 0.000 | — | True |
| Jogador 3 | 3-5 | 90.000 | 25 | 30.000 | 6 | 2 | 0 | 2.900 | — | True |
| Jogador 3 | 3-6 | 81.000 | 30 | 30.000 | 6 | 0 | 1 | -2.537 | — | True |
| Jogador 3 | 3-7 | 81.000 | 41 | 30.000 | 6 | 0 | 1 | 0.000 | — | True |
| Jogador 3 | 4-1 | 69.000 | 44 | 32.000 | 6 | 0 | 2 | -2.714 | — | True |
| Jogador 3 | 4-2 | 69.000 | 61 | 32.000 | 6 | 1 | 0 | 2.850 | — | True |
| Jogador 3 | 4-3 | 69.000 | 71 | 30.000 | 6 | 2 | 0 | 2.984 | — | True |
| Jogador 3 | 4-4 | 69.000 | 86 | 30.000 | 6 | 2 | 0 | 0.000 | — | True |
| Jogador 3 | 4-5 | 69.000 | 100 | 30.000 | 6 | 3 | 0 | 2.850 | — | True |
| Jogador 3 | 4-6 | 57.000 | 109 | 30.000 | 6 | 0 | 1 | -2.764 | — | True |
| Jogador 3 | 4-7 | 57.000 | 121 | 30.000 | 7 | 0 | 1 | 0.000 | — | True |
| Jogador 3 | 5-1 | 57.000 | 132 | 36.000 | 7 | 1 | 0 | 3.005 | — | True |
| Jogador 3 | 5-2 | 57.000 | 142 | 36.000 | 7 | 1 | 0 | 0.000 | — | True |
| Jogador 3 | 5-3 | 57.000 | 145 | 32.000 | 7 | 2 | 0 | 2.935 | — | True |
| Jogador 3 | 5-4 | 57.000 | 158 | 36.000 | 7 | 2 | 0 | 0.000 | — | True |
| Jogador 3 | 5-5 | 57.000 | 164 | 36.000 | 7 | 3 | 0 | 2.972 | — | True |
| Jogador 3 | 5-6 | 42.000 | 175 | 36.000 | 7 | 0 | 1 | -2.850 | — | True |
| Jogador 3 | 5-7 | 42.000 | 189 | 36.000 | 7 | 0 | 1 | 0.000 | — | True |
| Jogador 3 | 6-1 | 23.000 | 199 | 36.000 | 7 | 0 | 2 | -2.850 | — | True |
| Jogador 3 | 6-2 | 5.000 | 209 | 30.000 | 7 | 0 | 3 | -2.900 | — | True |
| Jogador 3 | 6-3 | 0.000 | 206 | 0.000 | 7 | 0 | 4 | -2.900 | 3 | False |
| Jogador 4 | 1-1 | 100.000 | 2 | 2.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 4 | 1-2 | 100.000 | 2 | 6.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 4 | 1-3 | 100.000 | 3 | 6.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 4 | 1-4 | 100.000 | 5 | 6.000 | 4 | 0 | 0 | 0.000 | — | True |
| Jogador 4 | 2-1 | 95.000 | 5 | 8.000 | 4 | 0 | 1 | -2.422 | — | True |
| Jogador 4 | 2-2 | 95.000 | 6 | 10.000 | 5 | 1 | 0 | 2.737 | — | True |
| Jogador 4 | 2-3 | 95.000 | 9 | 14.000 | 5 | 2 | 0 | 2.854 | — | True |
| Jogador 4 | 2-4 | 95.000 | 10 | 14.000 | 5 | 2 | 0 | 0.000 | — | True |
| Jogador 4 | 2-5 | 90.000 | 5 | 20.000 | 6 | 0 | 1 | -2.322 | — | True |
| Jogador 4 | 2-6 | 83.000 | 8 | 20.000 | 6 | 0 | 2 | -2.586 | — | True |
| Jogador 4 | 2-7 | 83.000 | 9 | 22.000 | 6 | 0 | 2 | 0.000 | — | True |
| Jogador 4 | 3-1 | 73.000 | 8 | 18.000 | 6 | 0 | 3 | -2.633 | — | True |
| Jogador 4 | 3-2 | 62.000 | 9 | 24.000 | 6 | 0 | 4 | -2.775 | — | True |
| Jogador 4 | 3-3 | 52.000 | 10 | 20.000 | 6 | 0 | 5 | -2.633 | — | True |
| Jogador 4 | 3-4 | 52.000 | 11 | 24.000 | 6 | 0 | 5 | 0.000 | — | True |
| Jogador 4 | 3-5 | 41.000 | 23 | 24.000 | 6 | 0 | 6 | -2.825 | — | True |
| Jogador 4 | 3-6 | 41.000 | 31 | 24.000 | 6 | 1 | 0 | 2.766 | — | True |
| Jogador 4 | 3-7 | 41.000 | 35 | 24.000 | 6 | 1 | 0 | 0.000 | — | True |
| Jogador 4 | 4-1 | 27.000 | 45 | 20.000 | 6 | 0 | 1 | -2.882 | — | True |
| Jogador 4 | 4-2 | 16.000 | 53 | 22.000 | 6 | 0 | 2 | -2.675 | — | True |
| Jogador 4 | 4-3 | 2.000 | 64 | 26.000 | 7 | 0 | 3 | -2.982 | — | True |
| Jogador 4 | 4-4 | 2.000 | 69 | 32.000 | 7 | 0 | 3 | 0.000 | — | True |
| Jogador 4 | 4-5 | 0.000 | 67 | 0.000 | 7 | 0 | 4 | -2.675 | 8 | False |
| Jogador 5 | 1-1 | 100.000 | 2 | 2.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 5 | 1-2 | 100.000 | 2 | 6.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 5 | 1-3 | 100.000 | 3 | 6.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 5 | 1-4 | 100.000 | 4 | 6.000 | 4 | 0 | 0 | 0.000 | — | True |
| Jogador 5 | 2-1 | 100.000 | 6 | 8.000 | 4 | 1 | 0 | 2.430 | — | True |
| Jogador 5 | 2-2 | 100.000 | 8 | 8.000 | 4 | 2 | 0 | 2.512 | — | True |
| Jogador 5 | 2-3 | 95.000 | 5 | 14.000 | 5 | 0 | 1 | -2.372 | — | True |
| Jogador 5 | 2-4 | 95.000 | 6 | 14.000 | 5 | 0 | 1 | 0.000 | — | True |
| Jogador 5 | 2-5 | 95.000 | 6 | 16.000 | 6 | 1 | 0 | 2.687 | — | True |
| Jogador 5 | 2-6 | 90.000 | 9 | 16.000 | 6 | 0 | 1 | -2.422 | — | True |
| Jogador 5 | 2-7 | 90.000 | 11 | 16.000 | 6 | 0 | 1 | 0.000 | — | True |
| Jogador 5 | 3-1 | 90.000 | 16 | 16.000 | 6 | 1 | 0 | 2.762 | — | True |
| Jogador 5 | 3-2 | 90.000 | 25 | 16.000 | 6 | 2 | 0 | 2.950 | — | True |
| Jogador 5 | 3-3 | 78.000 | 27 | 18.000 | 6 | 0 | 1 | -2.764 | — | True |
| Jogador 5 | 3-4 | 78.000 | 39 | 18.000 | 6 | 0 | 1 | 0.000 | — | True |
| Jogador 5 | 3-5 | 67.000 | 44 | 18.000 | 6 | 0 | 2 | -2.875 | — | True |
| Jogador 5 | 3-6 | 55.000 | 57 | 18.000 | 6 | 0 | 3 | -2.914 | — | True |
| Jogador 5 | 3-7 | 55.000 | 55 | 18.000 | 6 | 0 | 3 | 0.000 | — | True |
| Jogador 5 | 4-1 | 44.000 | 63 | 18.000 | 6 | 0 | 4 | -2.725 | — | True |
| Jogador 5 | 4-2 | 34.000 | 76 | 18.000 | 6 | 0 | 5 | -2.583 | — | True |
| Jogador 5 | 4-3 | 22.000 | 90 | 18.000 | 6 | 0 | 6 | -2.814 | — | True |
| Jogador 5 | 4-4 | 22.000 | 101 | 22.000 | 6 | 0 | 6 | 0.000 | — | True |
| Jogador 5 | 4-5 | 9.000 | 111 | 22.000 | 6 | 0 | 7 | -2.850 | — | True |
| Jogador 5 | 4-6 | 0.000 | 111 | 0.000 | 6 | 0 | 8 | -2.950 | 6 | False |
| Jogador 6 | 1-1 | 100.000 | 2 | 2.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 6 | 1-2 | 100.000 | 2 | 4.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 6 | 1-3 | 100.000 | 3 | 6.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 6 | 1-4 | 100.000 | 6 | 6.000 | 4 | 0 | 0 | 0.000 | — | True |
| Jogador 6 | 2-1 | 95.000 | 6 | 8.000 | 4 | 0 | 1 | -2.422 | — | True |
| Jogador 6 | 2-2 | 89.000 | 6 | 8.000 | 4 | 0 | 2 | -2.580 | — | True |
| Jogador 6 | 2-3 | 83.000 | 9 | 8.000 | 5 | 0 | 3 | -2.580 | — | True |
| Jogador 6 | 2-4 | 83.000 | 10 | 8.000 | 5 | 0 | 3 | 0.000 | — | True |
| Jogador 6 | 2-5 | 76.000 | 9 | 10.000 | 6 | 0 | 4 | -2.686 | — | True |
| Jogador 6 | 2-6 | 72.000 | 7 | 10.000 | 6 | 0 | 5 | -2.261 | — | True |
| Jogador 6 | 2-7 | 72.000 | 8 | 16.000 | 6 | 0 | 5 | 0.000 | — | True |
| Jogador 6 | 3-1 | 72.000 | 9 | 20.000 | 6 | 1 | 0 | 2.812 | — | True |
| Jogador 6 | 3-2 | 63.000 | 11 | 18.000 | 6 | 0 | 1 | -2.637 | — | True |
| Jogador 6 | 3-3 | 54.000 | 6 | 22.000 | 6 | 0 | 2 | -2.537 | — | True |
| Jogador 6 | 3-4 | 54.000 | 7 | 28.000 | 7 | 0 | 2 | 0.000 | — | True |
| Jogador 6 | 3-5 | 54.000 | 7 | 28.000 | 7 | 1 | 0 | 3.050 | — | True |
| Jogador 6 | 3-6 | 54.000 | 7 | 28.000 | 7 | 2 | 0 | 2.716 | — | True |
| Jogador 6 | 3-7 | 54.000 | 7 | 28.000 | 7 | 2 | 0 | 0.000 | — | True |
| Jogador 6 | 4-1 | 42.000 | 5 | 28.000 | 7 | 0 | 1 | -2.814 | — | True |
| Jogador 6 | 4-2 | 42.000 | 9 | 28.000 | 7 | 1 | 0 | 2.934 | — | True |
| Jogador 6 | 4-3 | 42.000 | 19 | 28.000 | 7 | 2 | 0 | 3.012 | — | True |
| Jogador 6 | 4-4 | 42.000 | 25 | 28.000 | 7 | 2 | 0 | 0.000 | — | True |
| Jogador 6 | 4-5 | 42.000 | 37 | 28.000 | 7 | 3 | 0 | 3.062 | — | True |
| Jogador 6 | 4-6 | 42.000 | 61 | 28.000 | 7 | 4 | 0 | 2.934 | — | True |
| Jogador 6 | 4-7 | 42.000 | 73 | 28.000 | 7 | 4 | 0 | 0.000 | — | True |
| Jogador 6 | 5-1 | 27.000 | 71 | 26.000 | 7 | 0 | 1 | -2.850 | — | True |
| Jogador 6 | 5-2 | 9.000 | 85 | 30.000 | 7 | 0 | 2 | -2.950 | — | True |
| Jogador 6 | 5-3 | 0.000 | 74 | 0.000 | 7 | 0 | 3 | -2.782 | 5 | False |
| Jogador 7 | 1-1 | 100.000 | 2 | 2.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 7 | 1-2 | 100.000 | 2 | 6.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 7 | 1-3 | 100.000 | 3 | 6.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 7 | 1-4 | 100.000 | 5 | 6.000 | 4 | 0 | 0 | 0.000 | — | True |
| Jogador 7 | 2-1 | 100.000 | 8 | 8.000 | 4 | 1 | 0 | 2.737 | — | True |
| Jogador 7 | 2-2 | 96.000 | 8 | 12.000 | 4 | 0 | 1 | -2.261 | — | True |
| Jogador 7 | 2-3 | 96.000 | 9 | 14.000 | 5 | 1 | 0 | 2.737 | — | True |
| Jogador 7 | 2-4 | 96.000 | 8 | 14.000 | 5 | 1 | 0 | 0.000 | — | True |
| Jogador 7 | 2-5 | 96.000 | 9 | 20.000 | 5 | 2 | 0 | 2.462 | — | True |
| Jogador 7 | 2-6 | 96.000 | 8 | 20.000 | 6 | 3 | 0 | 2.562 | — | True |
| Jogador 7 | 2-7 | 96.000 | 7 | 20.000 | 6 | 3 | 0 | 0.000 | — | True |
| Jogador 7 | 3-1 | 86.000 | 5 | 20.000 | 6 | 0 | 1 | -2.733 | — | True |
| Jogador 7 | 3-2 | 86.000 | 6 | 20.000 | 6 | 1 | 0 | 2.816 | — | True |
| Jogador 7 | 3-3 | 77.000 | 7 | 20.000 | 6 | 0 | 1 | -2.537 | — | True |
| Jogador 7 | 3-4 | 77.000 | 7 | 22.000 | 7 | 0 | 1 | 0.000 | — | True |
| Jogador 7 | 3-5 | 66.000 | 7 | 26.000 | 7 | 0 | 2 | -2.725 | — | True |
| Jogador 7 | 3-6 | 56.000 | 6 | 26.000 | 7 | 0 | 3 | -2.583 | — | True |
| Jogador 7 | 3-7 | 56.000 | 8 | 26.000 | 7 | 0 | 3 | 0.000 | — | True |
| Jogador 7 | 4-1 | 56.000 | 13 | 26.000 | 7 | 1 | 0 | 3.035 | — | True |
| Jogador 7 | 4-2 | 44.000 | 20 | 26.000 | 7 | 0 | 1 | -2.764 | — | True |
| Jogador 7 | 4-3 | 44.000 | 28 | 26.000 | 7 | 1 | 0 | 2.934 | — | True |
| Jogador 7 | 4-4 | 44.000 | 35 | 26.000 | 7 | 1 | 0 | 0.000 | — | True |
| Jogador 7 | 4-5 | 44.000 | 44 | 26.000 | 7 | 2 | 0 | 3.012 | — | True |
| Jogador 7 | 4-6 | 44.000 | 50 | 28.000 | 7 | 3 | 0 | 3.112 | — | True |
| Jogador 7 | 4-7 | 44.000 | 55 | 28.000 | 7 | 3 | 0 | 0.000 | — | True |
| Jogador 7 | 5-1 | 44.000 | 71 | 28.000 | 7 | 4 | 0 | 2.955 | — | True |
| Jogador 7 | 5-2 | 31.000 | 84 | 28.000 | 7 | 0 | 1 | -2.800 | — | True |
| Jogador 7 | 5-3 | 16.000 | 94 | 28.000 | 7 | 0 | 2 | -2.850 | — | True |
| Jogador 7 | 5-4 | 16.000 | 102 | 28.000 | 7 | 0 | 2 | 0.000 | — | True |
| Jogador 7 | 5-5 | 0.000 | 102 | 0.000 | 7 | 0 | 3 | -2.800 | 4 | False |
| Jogador 8 | 1-1 | 100.000 | 2 | 2.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 8 | 1-2 | 100.000 | 2 | 6.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 8 | 1-3 | 100.000 | 3 | 6.000 | 3 | 0 | 0 | 0.000 | — | True |
| Jogador 8 | 1-4 | 100.000 | 6 | 6.000 | 4 | 0 | 0 | 0.000 | — | True |
| Jogador 8 | 2-1 | 94.000 | 6 | 12.000 | 4 | 0 | 1 | -2.580 | — | True |
| Jogador 8 | 2-2 | 89.000 | 7 | 12.000 | 4 | 0 | 2 | -2.372 | — | True |
| Jogador 8 | 2-3 | 82.000 | 6 | 14.000 | 5 | 0 | 3 | -2.686 | — | True |
| Jogador 8 | 2-4 | 82.000 | 6 | 18.000 | 5 | 0 | 3 | 0.000 | — | True |
| Jogador 8 | 2-5 | 75.000 | 19 | 18.000 | 5 | 0 | 4 | -2.636 | — | True |
| Jogador 8 | 2-6 | 75.000 | 25 | 18.000 | 5 | 1 | 0 | 2.380 | — | True |
| Jogador 8 | 2-7 | 75.000 | 35 | 18.000 | 5 | 1 | 0 | 0.000 | — | True |
| Jogador 8 | 3-1 | 65.000 | 36 | 20.000 | 5 | 0 | 1 | -2.583 | — | True |
| Jogador 8 | 3-2 | 55.000 | 40 | 18.000 | 5 | 0 | 2 | -2.633 | — | True |
| Jogador 8 | 3-3 | 55.000 | 61 | 18.000 | 5 | 1 | 0 | 2.716 | — | True |
| Jogador 8 | 3-4 | 55.000 | 77 | 18.000 | 5 | 1 | 0 | 0.000 | — | True |
| Jogador 8 | 3-5 | 45.000 | 85 | 18.000 | 5 | 0 | 1 | -2.583 | — | True |
| Jogador 8 | 3-6 | 36.000 | 97 | 18.000 | 6 | 0 | 2 | -2.587 | — | True |
| Jogador 8 | 3-7 | 36.000 | 98 | 22.000 | 6 | 0 | 2 | 0.000 | — | True |
| Jogador 8 | 4-1 | 36.000 | 102 | 22.000 | 6 | 1 | 0 | 2.900 | — | True |
| Jogador 8 | 4-2 | 24.000 | 111 | 22.000 | 6 | 0 | 1 | -2.914 | — | True |
| Jogador 8 | 4-3 | 12.000 | 126 | 22.000 | 6 | 0 | 2 | -2.764 | — | True |
| Jogador 8 | 4-4 | 12.000 | 136 | 22.000 | 6 | 0 | 2 | 0.000 | — | True |
| Jogador 8 | 4-5 | 0.000 | 132 | 0.000 | 6 | 0 | 3 | -2.900 | 7 | False |

## Evolução posterior das recomendações por jogador/round

| Jogador | Round das recomendações | Contagem por recomendação | Ações PPO | Próximo round | Δ HP | Δ Ouro | Δ Board | Próximos 2 rounds Δ HP / Ouro / Board | Colocação final |
|---|---|---|---|---|---:|---:|---:|---|---:|
| Jogador 1 | 1-1 | HOLD=3 | DEPLOY_OR_MOVE=2; HOLD=1 | 1-2 | 0.000 | 0.000 | 4.000 | 0.0 / 1.0 / 4.0 | 1 |
| Jogador 2 | 1-1 | HOLD=3 | DEPLOY_OR_MOVE=2; HOLD=1 | 1-2 | 0.000 | 0.000 | 4.000 | 0.0 / 1.0 / 4.0 | 2 |
| Jogador 3 | 1-1 | HOLD=4 | DEPLOY_OR_MOVE=3; HOLD=1 | 1-2 | 0.000 | 0.000 | 4.000 | 0.0 / 1.0 / 6.0 | 3 |
| Jogador 4 | 1-1 | HOLD=4 | DEPLOY_OR_MOVE=3; HOLD=1 | 1-2 | 0.000 | 0.000 | 4.000 | 0.0 / 1.0 / 4.0 | 8 |
| Jogador 5 | 1-1 | HOLD=3 | DEPLOY_OR_MOVE=2; HOLD=1 | 1-2 | 0.000 | 0.000 | 4.000 | 0.0 / 1.0 / 4.0 | 6 |
| Jogador 6 | 1-1 | HOLD=3 | DEPLOY_OR_MOVE=2; HOLD=1 | 1-2 | 0.000 | 0.000 | 2.000 | 0.0 / 1.0 / 4.0 | 5 |
| Jogador 7 | 1-1 | HOLD=2 | DEPLOY_OR_MOVE=1; HOLD=1 | 1-2 | 0.000 | 0.000 | 4.000 | 0.0 / 1.0 / 4.0 | 4 |
| Jogador 8 | 1-1 | HOLD=3 | DEPLOY_OR_MOVE=2; HOLD=1 | 1-2 | 0.000 | 0.000 | 4.000 | 0.0 / 1.0 / 4.0 | 7 |
| Jogador 1 | 1-2 | HOLD=7 | BUY_UNIT=2; DEPLOY_OR_MOVE=4; HOLD=1 | 1-3 | 0.000 | 1.000 | 0.000 | 0.0 / 3.0 / 0.0 | 1 |
| Jogador 2 | 1-2 | HOLD=1; DEPLOY_OR_MOVE=4 | BUY_UNIT=2; DEPLOY_OR_MOVE=2; HOLD=1 | 1-3 | 0.000 | 1.000 | 0.000 | 0.0 / 2.0 / 2.0 | 2 |
| Jogador 3 | 1-2 | HOLD=6 | BUY_UNIT=2; DEPLOY_OR_MOVE=3; HOLD=1 | 1-3 | 0.000 | 1.000 | 2.000 | 0.0 / 2.0 / 2.0 | 3 |
| Jogador 4 | 1-2 | HOLD=1; DEPLOY_OR_MOVE=5 | BUY_UNIT=2; DEPLOY_OR_MOVE=3; HOLD=1 | 1-3 | 0.000 | 1.000 | 0.000 | 0.0 / 3.0 / 0.0 | 8 |
| Jogador 5 | 1-2 | HOLD=2; DEPLOY_OR_MOVE=5 | BUY_UNIT=2; DEPLOY_OR_MOVE=4; HOLD=1 | 1-3 | 0.000 | 1.000 | 0.000 | 0.0 / 2.0 / 0.0 | 6 |
| Jogador 6 | 1-2 | HOLD=3; DEPLOY_OR_MOVE=1 | BUY_UNIT=2; HOLD=1; DEPLOY_OR_MOVE=1 | 1-3 | 0.000 | 1.000 | 2.000 | 0.0 / 4.0 / 2.0 | 5 |
| Jogador 7 | 1-2 | HOLD=1; DEPLOY_OR_MOVE=7 | BUY_UNIT=2; DEPLOY_OR_MOVE=5; HOLD=1 | 1-3 | 0.000 | 1.000 | 0.000 | 0.0 / 3.0 / 0.0 | 4 |
| Jogador 8 | 1-2 | HOLD=2; DEPLOY_OR_MOVE=5 | BUY_UNIT=2; DEPLOY_OR_MOVE=4; HOLD=1 | 1-3 | 0.000 | 1.000 | 0.000 | 0.0 / 4.0 / 0.0 | 7 |
| Jogador 1 | 1-3 | HOLD=5 | BUY_UNIT=2; DEPLOY_OR_MOVE=2; HOLD=1 | 1-4 | 0.000 | 2.000 | 0.000 | 0.0 / 3.0 / 2.0 | 1 |
| Jogador 2 | 1-3 | BUY_UNIT=1; DEPLOY_OR_MOVE=3 | BUY_UNIT=2; HOLD=1; DEPLOY_OR_MOVE=1 | 1-4 | 0.000 | 1.000 | 2.000 | -4.0 / 2.0 / 4.0 | 2 |
| Jogador 3 | 1-3 | HOLD=1; BUY_UNIT=1; DEPLOY_OR_MOVE=4 | BUY_UNIT=2; DEPLOY_OR_MOVE=3; HOLD=1 | 1-4 | 0.000 | 1.000 | 0.000 | 0.0 / 3.0 / 4.0 | 3 |
| Jogador 4 | 1-3 | HOLD=5 | BUY_UNIT=2; DEPLOY_OR_MOVE=2; HOLD=1 | 1-4 | 0.000 | 2.000 | 0.000 | -5.0 / 2.0 / 2.0 | 8 |
| Jogador 5 | 1-3 | HOLD=2 | BUY_UNIT=1; HOLD=1 | 1-4 | 0.000 | 1.000 | 0.000 | 0.0 / 3.0 / 2.0 | 6 |
| Jogador 6 | 1-3 | HOLD=1; DEPLOY_OR_MOVE=5 | BUY_UNIT=2; DEPLOY_OR_MOVE=3; HOLD=1 | 1-4 | 0.000 | 3.000 | 0.000 | -5.0 / 3.0 / 2.0 | 5 |
| Jogador 7 | 1-3 | BUY_UNIT=1; HOLD=5 | BUY_UNIT=2; DEPLOY_OR_MOVE=3; HOLD=1 | 1-4 | 0.000 | 2.000 | 0.000 | 0.0 / 5.0 / 2.0 | 4 |
| Jogador 8 | 1-3 | BUY_UNIT=1; HOLD=2 | BUY_UNIT=2; HOLD=1 | 1-4 | 0.000 | 3.000 | 0.000 | -6.0 / 3.0 / 6.0 | 7 |
| Jogador 1 | 1-4 | BUY_UNIT=1; HOLD=2 | BUY_UNIT=2; HOLD=1 | 2-1 | 0.000 | 1.000 | 2.000 | 0.0 / 5.0 / 4.0 | 1 |
| Jogador 2 | 1-4 | BUY_UNIT=2; DEPLOY_OR_MOVE=2; HOLD=3 | BUY_UNIT=3; DEPLOY_OR_MOVE=3; HOLD=1 | 2-1 | -4.000 | 1.000 | 2.000 | -10.0 / 2.0 / 2.0 | 2 |
| Jogador 3 | 1-4 | HOLD=5 | BUY_UNIT=2; DEPLOY_OR_MOVE=2; HOLD=1 | 2-1 | 0.000 | 2.000 | 4.000 | 0.0 / 4.0 / 4.0 | 3 |
| Jogador 4 | 1-4 | HOLD=2; BUY_UNIT=1 | BUY_UNIT=2; HOLD=1 | 2-1 | -5.000 | 0.000 | 2.000 | -5.0 / 1.0 / 4.0 | 8 |
| Jogador 5 | 1-4 | HOLD=3 | BUY_UNIT=2; HOLD=1 | 2-1 | 0.000 | 2.000 | 2.000 | 0.0 / 4.0 / 2.0 | 6 |
| Jogador 6 | 1-4 | HOLD=2 | BUY_UNIT=1; HOLD=1 | 2-1 | -5.000 | 0.000 | 2.000 | -11.0 / 0.0 / 2.0 | 5 |
| Jogador 7 | 1-4 | BUY_UNIT=1; HOLD=4 | BUY_UNIT=2; DEPLOY_OR_MOVE=2; HOLD=1 | 2-1 | 0.000 | 3.000 | 2.000 | -4.0 / 3.0 / 6.0 | 4 |
| Jogador 8 | 1-4 | HOLD=5; BUY_UNIT=1 | BUY_UNIT=3; SELL_UNIT=2; HOLD=1 | 2-1 | -6.000 | 0.000 | 6.000 | -11.0 / 1.0 / 6.0 | 7 |
| Jogador 1 | 2-1 | DEPLOY_OR_MOVE=6 | BUY_UNIT=1; BUY_EXPERIENCE=1; HOLD=1; DEPLOY_OR_MOVE=1 | 2-2 | 0.000 | 4.000 | 2.000 | 0.0 / 1.0 / 2.0 | 1 |
| Jogador 2 | 2-1 | DEPLOY_OR_MOVE=6; SELL_UNIT=2 | BUY_UNIT=3; SELL_UNIT=1; DEPLOY_OR_MOVE=2 | 2-2 | -6.000 | 1.000 | 0.000 | -11.0 / 2.0 / 2.0 | 2 |
| Jogador 3 | 2-1 | DEPLOY_OR_MOVE=4; HOLD=3 | BUY_UNIT=2; DEPLOY_OR_MOVE=2; HOLD=1 | 2-2 | 0.000 | 2.000 | 0.000 | 0.0 / 2.0 / 0.0 | 3 |
| Jogador 4 | 2-1 | DEPLOY_OR_MOVE=6 | BUY_UNIT=1; BUY_EXPERIENCE=1; HOLD=1; DEPLOY_OR_MOVE=1 | 2-2 | 0.000 | 1.000 | 2.000 | 0.0 / 4.0 / 6.0 | 8 |
| Jogador 5 | 2-1 | DEPLOY_OR_MOVE=4; HOLD=1; SELL_UNIT=1 | BUY_UNIT=2; DEPLOY_OR_MOVE=1; HOLD=1 | 2-2 | 0.000 | 2.000 | 0.000 | -5.0 / -1.0 / 6.0 | 6 |
| Jogador 6 | 2-1 | HOLD=3; DEPLOY_OR_MOVE=3 | BUY_UNIT=1; BUY_EXPERIENCE=1; HOLD=1; DEPLOY_OR_MOVE=1 | 2-2 | -6.000 | 0.000 | 0.000 | -12.0 / 3.0 / 0.0 | 5 |
| Jogador 7 | 2-1 | DEPLOY_OR_MOVE=6 | BUY_UNIT=2; HOLD=1; DEPLOY_OR_MOVE=1 | 2-2 | -4.000 | 0.000 | 4.000 | -4.0 / 1.0 / 6.0 | 4 |
| Jogador 8 | 2-1 | BUY_UNIT=5; DEPLOY_OR_MOVE=2; HOLD=1 | BUY_UNIT=4; DEPLOY_OR_MOVE=2 | 2-2 | -5.000 | 1.000 | 0.000 | -12.0 / 0.0 / 2.0 | 7 |
| Jogador 1 | 2-2 | BUY_UNIT=3; DEPLOY_OR_MOVE=2; SELL_UNIT=2 | BUY_UNIT=1; SELL_UNIT=2; BUY_EXPERIENCE=1; DEPLOY_OR_MOVE=3 | 2-3 | 0.000 | -3.000 | 0.000 | 0.0 / -2.0 / 4.0 | 1 |
| Jogador 2 | 2-2 | BUY_UNIT=1; SELL_UNIT=6 | BUY_UNIT=3; DEPLOY_OR_MOVE=2; SELL_UNIT=1; BUY_EXPERIENCE=1 | 2-3 | -5.000 | 1.000 | 2.000 | -5.0 / 1.0 / 6.0 | 2 |
| Jogador 3 | 2-2 | BUY_UNIT=2; SELL_UNIT=1 | BUY_UNIT=2; HOLD=1 | 2-3 | 0.000 | 0.000 | 0.000 | 0.0 / -2.0 / 6.0 | 3 |
| Jogador 4 | 2-2 | BUY_UNIT=1; HOLD=1; DEPLOY_OR_MOVE=1 | BUY_UNIT=1; BUY_EXPERIENCE=1; HOLD=1 | 2-3 | 0.000 | 3.000 | 4.000 | 0.0 / 4.0 / 4.0 | 8 |
| Jogador 5 | 2-2 | BUY_UNIT=1; SELL_UNIT=2 | BUY_UNIT=1; BUY_EXPERIENCE=1; HOLD=1 | 2-3 | -5.000 | -3.000 | 6.000 | -5.0 / -2.0 / 6.0 | 6 |
| Jogador 6 | 2-2 | HOLD=1; SELL_UNIT=4 | BUY_UNIT=3; SELL_UNIT=1; HOLD=1 | 2-3 | -6.000 | 3.000 | 0.000 | -6.0 / 4.0 / 0.0 | 5 |
| Jogador 7 | 2-2 | BUY_UNIT=1; DEPLOY_OR_MOVE=6 | BUY_UNIT=2; BUY_EXPERIENCE=1; DEPLOY_OR_MOVE=3; SELL_UNIT=1 | 2-3 | 0.000 | 1.000 | 2.000 | 0.0 / 0.0 / 2.0 | 4 |
| Jogador 8 | 2-2 | HOLD=3; SELL_UNIT=4 | BUY_UNIT=3; DEPLOY_OR_MOVE=3; SELL_UNIT=1 | 2-3 | -7.000 | -1.000 | 2.000 | -7.0 / -1.0 / 6.0 | 7 |
| Jogador 1 | 2-3 | BUY_UNIT=2; SELL_UNIT=6 | BUY_UNIT=2; BUY_EXPERIENCE=2; SELL_UNIT=1; DEPLOY_OR_MOVE=2; HOLD=1 | 2-4 | 0.000 | 1.000 | 4.000 | 0.0 / 1.0 / 10.0 | 1 |
| Jogador 2 | 2-3 | SELL_UNIT=2; DEPLOY_OR_MOVE=1 | BUY_UNIT=1; BUY_EXPERIENCE=1; HOLD=1 | 2-4 | 0.000 | 0.000 | 4.000 | -6.0 / 0.0 / 4.0 | 2 |
| Jogador 3 | 2-3 | BUY_UNIT=4 | BUY_UNIT=2; BUY_EXPERIENCE=1; HOLD=1 | 2-4 | 0.000 | -2.000 | 6.000 | 0.0 / 0.0 / 6.0 | 3 |
| Jogador 4 | 2-3 | BUY_UNIT=2; DEPLOY_OR_MOVE=7 | BUY_UNIT=3; SELL_UNIT=3; BUY_EXPERIENCE=1; DEPLOY_OR_MOVE=1; HOLD=1 | 2-4 | 0.000 | 1.000 | 0.000 | -5.0 / -4.0 / 6.0 | 8 |
| Jogador 5 | 2-3 | BUY_UNIT=1; DEPLOY_OR_MOVE=4; SELL_UNIT=4 | BUY_UNIT=3; BUY_EXPERIENCE=2; DEPLOY_OR_MOVE=3; SELL_UNIT=1 | 2-4 | 0.000 | 1.000 | 0.000 | 0.0 / 1.0 / 2.0 | 6 |
| Jogador 6 | 2-3 | SELL_UNIT=6 | BUY_UNIT=3; SELL_UNIT=2; HOLD=1 | 2-4 | 0.000 | 1.000 | 0.000 | -7.0 / 0.0 / 2.0 | 5 |
| Jogador 7 | 2-3 | BUY_UNIT=1; DEPLOY_OR_MOVE=5 | BUY_UNIT=3; HOLD=1 | 2-4 | 0.000 | -1.000 | 0.000 | 0.0 / 0.0 / 6.0 | 4 |
| Jogador 8 | 2-3 | BUY_UNIT=3; DEPLOY_OR_MOVE=1; SELL_UNIT=5 | BUY_UNIT=4; DEPLOY_OR_MOVE=3; SELL_UNIT=1; BUY_EXPERIENCE=1 | 2-4 | 0.000 | 0.000 | 4.000 | -7.0 / 13.0 / 4.0 | 7 |
| Jogador 1 | 2-4 | BUY_UNIT=1; DEPLOY_OR_MOVE=4; SELL_UNIT=2 | BUY_UNIT=2; BUY_EXPERIENCE=1; SELL_UNIT=1; DEPLOY_OR_MOVE=2; HOLD=1 | 2-5 | 0.000 | 0.000 | 6.000 | 0.0 / 1.0 / 10.0 | 1 |
| Jogador 2 | 2-4 | BUY_UNIT=1; SELL_UNIT=8 | BUY_UNIT=4; DEPLOY_OR_MOVE=3; SELL_UNIT=2 | 2-5 | -6.000 | 0.000 | 0.000 | -13.0 / 0.0 / 2.0 | 2 |
| Jogador 3 | 2-4 | DEPLOY_OR_MOVE=2; BUY_UNIT=3; SELL_UNIT=3 | BUY_UNIT=2; DEPLOY_OR_MOVE=4; BUY_EXPERIENCE=1; HOLD=1 | 2-5 | 0.000 | 2.000 | 0.000 | 0.0 / 2.0 / 6.0 | 3 |
| Jogador 4 | 2-4 | BUY_UNIT=3; SELL_UNIT=5; HOLD=1 | BUY_UNIT=4; SELL_UNIT=3; BUY_EXPERIENCE=1; DEPLOY_OR_MOVE=1 | 2-5 | -5.000 | -5.000 | 6.000 | -12.0 / -2.0 / 6.0 | 8 |
| Jogador 5 | 2-4 | HOLD=1; SELL_UNIT=8 | BUY_UNIT=3; SELL_UNIT=4; BUY_EXPERIENCE=1; HOLD=1 | 2-5 | 0.000 | 0.000 | 2.000 | -5.0 / 3.0 / 2.0 | 6 |
| Jogador 6 | 2-4 | DEPLOY_OR_MOVE=9 | BUY_UNIT=3; BUY_EXPERIENCE=2; SELL_UNIT=4 | 2-5 | -7.000 | -1.000 | 2.000 | -11.0 / -3.0 / 2.0 | 5 |
| Jogador 7 | 2-4 | DEPLOY_OR_MOVE=9 | BUY_UNIT=3; SELL_UNIT=3; BUY_EXPERIENCE=1; DEPLOY_OR_MOVE=2 | 2-5 | 0.000 | 1.000 | 6.000 | 0.0 / 0.0 / 6.0 | 4 |
| Jogador 8 | 2-4 | DEPLOY_OR_MOVE=3; SELL_UNIT=6 | BUY_UNIT=4; DEPLOY_OR_MOVE=3; SELL_UNIT=2 | 2-5 | -7.000 | 13.000 | 0.000 | -7.0 / 19.0 / 0.0 | 7 |
| Jogador 1 | 2-5 | BUY_UNIT=2; BUY_XP=1; DEPLOY_OR_MOVE=5 | BUY_UNIT=2; BUY_EXPERIENCE=1; DEPLOY_OR_MOVE=3; SELL_UNIT=1; HOLD=1 | 2-6 | 0.000 | 1.000 | 4.000 | 0.0 / 1.0 / 4.0 | 1 |
| Jogador 2 | 2-5 | SELL_UNIT=9 | BUY_UNIT=3; BUY_EXPERIENCE=2; SELL_UNIT=4 | 2-6 | -7.000 | 0.000 | 2.000 | -7.0 / 3.0 / 8.0 | 2 |
| Jogador 3 | 2-5 | BUY_UNIT=2; SELL_UNIT=1 | BUY_UNIT=1; BUY_EXPERIENCE=1; HOLD=1 | 2-6 | 0.000 | 0.000 | 6.000 | 0.0 / 3.0 / 6.0 | 3 |
| Jogador 4 | 2-5 | BUY_UNIT=5; BUY_XP=2; SELL_UNIT=1; DEPLOY_OR_MOVE=1 | BUY_UNIT=3; BUY_EXPERIENCE=2; SELL_UNIT=2; DEPLOY_OR_MOVE=2 | 2-6 | -7.000 | 3.000 | 0.000 | -7.0 / 4.0 / 2.0 | 8 |
| Jogador 5 | 2-5 | SELL_UNIT=4; HOLD=4; DEPLOY_OR_MOVE=1 | BUY_UNIT=3; SELL_UNIT=3; BUY_EXPERIENCE=2; DEPLOY_OR_MOVE=1 | 2-6 | -5.000 | 3.000 | 0.000 | -5.0 / 5.0 / 0.0 | 6 |
| Jogador 6 | 2-5 | DEPLOY_OR_MOVE=9 | BUY_UNIT=2; SELL_UNIT=3; BUY_EXPERIENCE=3; DEPLOY_OR_MOVE=1 | 2-6 | -4.000 | -2.000 | 0.000 | -4.0 / -1.0 / 6.0 | 5 |
| Jogador 7 | 2-5 | DEPLOY_OR_MOVE=6 | BUY_UNIT=2; BUY_EXPERIENCE=1; SELL_UNIT=2; HOLD=1 | 2-6 | 0.000 | -1.000 | 0.000 | 0.0 / -2.0 / 0.0 | 4 |
| Jogador 8 | 2-5 | BUY_UNIT=1; SELL_UNIT=7; HOLD=1 | BUY_UNIT=4; SELL_UNIT=5 | 2-6 | 0.000 | 6.000 | 0.000 | 0.0 / 16.0 / 0.0 | 7 |
| Jogador 1 | 2-6 | BUY_UNIT=1; DEPLOY_OR_MOVE=3; SELL_UNIT=3 | BUY_UNIT=3; DEPLOY_OR_MOVE=3; HOLD=1 | 2-7 | 0.000 | 0.000 | 0.000 | 0.0 / 1.0 / 4.0 | 1 |
| Jogador 2 | 2-6 | SELL_UNIT=5; DEPLOY_OR_MOVE=1 | BUY_UNIT=1; BUY_EXPERIENCE=1; DEPLOY_OR_MOVE=3; HOLD=1 | 2-7 | 0.000 | 3.000 | 6.000 | -10.0 / 3.0 / 6.0 | 2 |
| Jogador 3 | 2-6 | BUY_UNIT=4; DEPLOY_OR_MOVE=1; SELL_UNIT=4 | SELL_UNIT=1; BUY_UNIT=3; DEPLOY_OR_MOVE=4; BUY_EXPERIENCE=1 | 2-7 | 0.000 | 3.000 | 0.000 | 0.0 / 8.0 / 2.0 | 3 |
| Jogador 4 | 2-6 | HOLD=6 | BUY_UNIT=2; DEPLOY_OR_MOVE=3; HOLD=1 | 2-7 | 0.000 | 1.000 | 2.000 | -10.0 / 0.0 / -2.0 | 8 |
| Jogador 5 | 2-6 | BUY_UNIT=1; SELL_UNIT=8 | BUY_UNIT=5; DEPLOY_OR_MOVE=1; SELL_UNIT=3 | 2-7 | 0.000 | 2.000 | 0.000 | 0.0 / 7.0 / 0.0 | 6 |
| Jogador 6 | 2-6 | DEPLOY_OR_MOVE=9 | BUY_UNIT=3; BUY_EXPERIENCE=2; SELL_UNIT=3; DEPLOY_OR_MOVE=1 | 2-7 | 0.000 | 1.000 | 6.000 | 0.0 / 2.0 / 10.0 | 5 |
| Jogador 7 | 2-6 | BUY_UNIT=3; SELL_UNIT=3; DEPLOY_OR_MOVE=3 | BUY_UNIT=2; BUY_EXPERIENCE=3; SELL_UNIT=3; DEPLOY_OR_MOVE=1 | 2-7 | 0.000 | -1.000 | 0.000 | -10.0 / -3.0 / 0.0 | 4 |
| Jogador 8 | 2-6 | HOLD=1; SELL_UNIT=8 | BUY_UNIT=3; DEPLOY_OR_MOVE=3; SELL_UNIT=3 | 2-7 | 0.000 | 10.000 | 0.000 | -10.0 / 11.0 / 2.0 | 7 |
| Jogador 1 | 2-7 | BUY_UNIT=2; DEPLOY_OR_MOVE=7 | BUY_UNIT=4; DEPLOY_OR_MOVE=1; SELL_UNIT=1; BUY_EXPERIENCE=1 | 3-1 | 0.000 | 1.000 | 4.000 | 0.0 / 2.0 / 4.0 | 1 |
| Jogador 2 | 2-7 | SELL_UNIT=9 | BUY_UNIT=4; SELL_UNIT=3; DEPLOY_OR_MOVE=2 | 3-1 | -10.000 | 0.000 | 0.000 | -10.0 / -1.0 / 0.0 | 2 |
| Jogador 3 | 2-7 | BUY_UNIT=8; SELL_UNIT=1 | BUY_UNIT=4; SELL_UNIT=4; BUY_EXPERIENCE=1 | 3-1 | 0.000 | 5.000 | 2.000 | -10.0 / 6.0 / 8.0 | 3 |
| Jogador 4 | 2-7 | BUY_UNIT=1; HOLD=8 | BUY_UNIT=3; BUY_EXPERIENCE=1; SELL_UNIT=3; DEPLOY_OR_MOVE=2 | 3-1 | -10.000 | -1.000 | -4.000 | -21.0 / 0.0 / 2.0 | 8 |
| Jogador 5 | 2-7 | HOLD=9 | BUY_UNIT=5; SELL_UNIT=4 | 3-1 | 0.000 | 5.000 | 0.000 | 0.0 / 14.0 / 0.0 | 6 |
| Jogador 6 | 2-7 | DEPLOY_OR_MOVE=3; BUY_UNIT=4; SELL_UNIT=1 | BUY_UNIT=2; DEPLOY_OR_MOVE=5; HOLD=1 | 3-1 | 0.000 | 1.000 | 4.000 | -9.0 / 3.0 / 2.0 | 5 |
| Jogador 7 | 2-7 | DEPLOY_OR_MOVE=9 | BUY_UNIT=2; BUY_EXPERIENCE=2; SELL_UNIT=3; DEPLOY_OR_MOVE=2 | 3-1 | -10.000 | -2.000 | 0.000 | -10.0 / -1.0 / 0.0 | 4 |
| Jogador 8 | 2-7 | BUY_UNIT=2; SELL_UNIT=7 | BUY_UNIT=4; SELL_UNIT=5 | 3-1 | -10.000 | 1.000 | 2.000 | -20.0 / 5.0 / 0.0 | 7 |
| Jogador 1 | 3-1 | DEPLOY_OR_MOVE=7 | BUY_UNIT=3; BUY_EXPERIENCE=1; SELL_UNIT=1; HOLD=1 | 3-2 | 0.000 | 1.000 | 0.000 | 0.0 / -1.0 / 0.0 | 1 |
| Jogador 2 | 3-1 | SELL_UNIT=9 | BUY_UNIT=3; BUY_EXPERIENCE=2; SELL_UNIT=3 | 3-2 | 0.000 | -1.000 | 0.000 | 0.0 / 5.0 / 0.0 | 2 |
| Jogador 3 | 3-1 | DEPLOY_OR_MOVE=3; BUY_UNIT=5 | BUY_UNIT=2; DEPLOY_OR_MOVE=4; HOLD=1 | 3-2 | -10.000 | 1.000 | 6.000 | -10.0 / 2.0 / 6.0 | 3 |
| Jogador 4 | 3-1 | BUY_UNIT=1; HOLD=6; SELL_UNIT=2 | BUY_UNIT=3; BUY_EXPERIENCE=1; SELL_UNIT=2; DEPLOY_OR_MOVE=2 | 3-2 | -11.000 | 1.000 | 6.000 | -21.0 / 2.0 / 2.0 | 8 |
| Jogador 5 | 3-1 | BUY_UNIT=1; HOLD=2; SELL_UNIT=6 | BUY_UNIT=5; SELL_UNIT=3 | 3-2 | 0.000 | 9.000 | 0.000 | -12.0 / 11.0 / 2.0 | 6 |
| Jogador 6 | 3-1 | SELL_UNIT=6 | BUY_UNIT=2; DEPLOY_OR_MOVE=2; HOLD=1 | 3-2 | -9.000 | 2.000 | -2.000 | -18.0 / -3.0 / 2.0 | 5 |
| Jogador 7 | 3-1 | DEPLOY_OR_MOVE=9 | BUY_UNIT=4; BUY_EXPERIENCE=1; SELL_UNIT=2; DEPLOY_OR_MOVE=1 | 3-2 | 0.000 | 1.000 | 0.000 | -9.0 / 2.0 / 0.0 | 4 |
| Jogador 8 | 3-1 | BUY_UNIT=1; SELL_UNIT=5 | BUY_UNIT=2; DEPLOY_OR_MOVE=2; HOLD=1 | 3-2 | -10.000 | 4.000 | -2.000 | -10.0 / 25.0 / -2.0 | 7 |
| Jogador 1 | 3-2 | BUY_UNIT=2; SELL_UNIT=4 | BUY_UNIT=2; BUY_EXPERIENCE=1; DEPLOY_OR_MOVE=2; HOLD=1 | 3-3 | 0.000 | -2.000 | 0.000 | 0.0 / -3.0 / 0.0 | 1 |
| Jogador 2 | 3-2 | BUY_UNIT=2; SELL_UNIT=7 | BUY_UNIT=4; BUY_EXPERIENCE=2; SELL_UNIT=3 | 3-3 | 0.000 | 6.000 | 0.000 | 0.0 / 9.0 / 0.0 | 2 |
| Jogador 3 | 3-2 | BUY_UNIT=2; DEPLOY_OR_MOVE=5 | BUY_UNIT=3; DEPLOY_OR_MOVE=3; HOLD=1 | 3-3 | 0.000 | 1.000 | 0.000 | 0.0 / 7.0 / -2.0 | 3 |
| Jogador 4 | 3-2 | BUY_UNIT=3; DEPLOY_OR_MOVE=1; SELL_UNIT=5 | BUY_UNIT=3; DEPLOY_OR_MOVE=5; HOLD=1 | 3-3 | -10.000 | 1.000 | -4.000 | -10.0 / 2.0 / 0.0 | 8 |
| Jogador 5 | 3-2 | BUY_UNIT=1; SELL_UNIT=8 | BUY_UNIT=4; SELL_UNIT=5 | 3-3 | -12.000 | 2.000 | 2.000 | -12.0 / 14.0 / 2.0 | 6 |
| Jogador 6 | 3-2 | BUY_UNIT=2; DEPLOY_OR_MOVE=7 | BUY_UNIT=2; DEPLOY_OR_MOVE=3; BUY_EXPERIENCE=1; SELL_UNIT=1 | 3-3 | -9.000 | -5.000 | 4.000 | -9.0 / -4.0 / 10.0 | 5 |
| Jogador 7 | 3-2 | DEPLOY_OR_MOVE=9 | BUY_UNIT=4; SELL_UNIT=4; BUY_EXPERIENCE=1 | 3-3 | -9.000 | 1.000 | 0.000 | -9.0 / 1.0 / 2.0 | 4 |
| Jogador 8 | 3-2 | SELL_UNIT=9 | BUY_UNIT=2; DEPLOY_OR_MOVE=6; HOLD=1 | 3-3 | 0.000 | 21.000 | 0.000 | 0.0 / 37.0 / 0.0 | 7 |
| Jogador 1 | 3-3 | SELL_UNIT=9 | BUY_UNIT=2; BUY_EXPERIENCE=2; DEPLOY_OR_MOVE=4; SELL_UNIT=1 | 3-4 | 0.000 | -1.000 | 0.000 | 0.0 / 0.0 / 4.0 | 1 |
| Jogador 2 | 3-3 | BUY_UNIT=1; SELL_UNIT=8 | BUY_UNIT=3; SELL_UNIT=4; BUY_EXPERIENCE=1; DEPLOY_OR_MOVE=1 | 3-4 | 0.000 | 3.000 | 0.000 | 0.0 / 5.0 / 0.0 | 2 |
| Jogador 3 | 3-3 | BUY_UNIT=1; SELL_UNIT=5 | BUY_UNIT=2; DEPLOY_OR_MOVE=3; HOLD=1 | 3-4 | 0.000 | 6.000 | -2.000 | 0.0 / 7.0 / -2.0 | 3 |
| Jogador 4 | 3-3 | BUY_UNIT=1; SELL_UNIT=6 | BUY_UNIT=3; DEPLOY_OR_MOVE=3; HOLD=1 | 3-4 | 0.000 | 1.000 | 4.000 | -11.0 / 13.0 / 4.0 | 8 |
| Jogador 5 | 3-3 | BUY_UNIT=3; SELL_UNIT=6 | BUY_UNIT=4; SELL_UNIT=2; DEPLOY_OR_MOVE=2; HOLD=1 | 3-4 | 0.000 | 12.000 | 0.000 | -11.0 / 17.0 / 0.0 | 6 |
| Jogador 6 | 3-3 | DEPLOY_OR_MOVE=9 | BUY_UNIT=2; BUY_EXPERIENCE=2; DEPLOY_OR_MOVE=2; SELL_UNIT=1; HOLD=1 | 3-4 | 0.000 | 1.000 | 6.000 | 0.0 / 1.0 / 6.0 | 5 |
| Jogador 7 | 3-3 | DEPLOY_OR_MOVE=9 | BUY_UNIT=4; SELL_UNIT=4; BUY_EXPERIENCE=1 | 3-4 | 0.000 | 0.000 | 2.000 | -11.0 / 0.0 / 6.0 | 4 |
| Jogador 8 | 3-3 | BUY_UNIT=3; SELL_UNIT=3; HOLD=3 | BUY_UNIT=3; SELL_UNIT=5 | 3-4 | 0.000 | 16.000 | 0.000 | -10.0 / 24.0 / 0.0 | 7 |
| Jogador 1 | 3-4 | BUY_UNIT=2; SELL_UNIT=1; DEPLOY_OR_MOVE=6 | SELL_UNIT=3; BUY_UNIT=2; BUY_EXPERIENCE=3; DEPLOY_OR_MOVE=1 | 3-5 | 0.000 | 1.000 | 4.000 | 0.0 / 3.0 / 4.0 | 1 |
| Jogador 2 | 3-4 | SELL_UNIT=6; BUY_UNIT=3 | BUY_UNIT=3; DEPLOY_OR_MOVE=4; SELL_UNIT=1; HOLD=1 | 3-5 | 0.000 | 2.000 | 0.000 | 0.0 / 7.0 / 0.0 | 2 |
| Jogador 3 | 3-4 | BUY_UNIT=2; SELL_UNIT=5 | SELL_UNIT=1; BUY_UNIT=1; DEPLOY_OR_MOVE=4; HOLD=1 | 3-5 | 0.000 | 1.000 | 0.000 | -9.0 / 6.0 / 0.0 | 3 |
| Jogador 4 | 3-4 | BUY_UNIT=4; SELL_UNIT=4 | BUY_UNIT=3; DEPLOY_OR_MOVE=4; HOLD=1 | 3-5 | -11.000 | 12.000 | 0.000 | -11.0 / 20.0 / 0.0 | 8 |
| Jogador 5 | 3-4 | BUY_UNIT=1; SELL_UNIT=8 | BUY_UNIT=4; SELL_UNIT=5 | 3-5 | -11.000 | 5.000 | 0.000 | -23.0 / 18.0 / 0.0 | 6 |
| Jogador 6 | 3-4 | BUY_XP=2; SELL_UNIT=5; DEPLOY_OR_MOVE=1; HOLD=1 | BUY_UNIT=3; SELL_UNIT=3; BUY_EXPERIENCE=1; DEPLOY_OR_MOVE=2 | 3-5 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 / 0.0 | 5 |
| Jogador 7 | 3-4 | BUY_UNIT=1; DEPLOY_OR_MOVE=8 | BUY_UNIT=4; SELL_UNIT=1; BUY_EXPERIENCE=1; DEPLOY_OR_MOVE=3 | 3-5 | -11.000 | 0.000 | 4.000 | -21.0 / -1.0 / 4.0 | 4 |
| Jogador 8 | 3-4 | BUY_UNIT=2; SELL_UNIT=7 | BUY_UNIT=3; SELL_UNIT=6 | 3-5 | -10.000 | 8.000 | 0.000 | -19.0 / 20.0 / 0.0 | 7 |
| Jogador 1 | 3-5 | DEPLOY_OR_MOVE=9 | BUY_UNIT=2; DEPLOY_OR_MOVE=6; BUY_EXPERIENCE=1 | 3-6 | 0.000 | 2.000 | 0.000 | 0.0 / 13.0 / 0.0 | 1 |
| Jogador 2 | 3-5 | BUY_UNIT=2; SELL_UNIT=4 | BUY_UNIT=3; DEPLOY_OR_MOVE=2; HOLD=1 | 3-6 | 0.000 | 5.000 | 0.000 | 0.0 / 12.0 / 0.0 | 2 |
| Jogador 3 | 3-5 | BUY_UNIT=2; SELL_UNIT=6 | SELL_UNIT=1; BUY_UNIT=3; DEPLOY_OR_MOVE=3; HOLD=1 | 3-6 | -9.000 | 5.000 | 0.000 | -9.0 / 16.0 / 0.0 | 3 |
| Jogador 4 | 3-5 | BUY_UNIT=5; SELL_UNIT=1 | SELL_UNIT=1; BUY_UNIT=1; DEPLOY_OR_MOVE=3; HOLD=1 | 3-6 | 0.000 | 8.000 | 0.000 | 0.0 / 12.0 / 0.0 | 8 |
| Jogador 5 | 3-5 | BUY_UNIT=1; DEPLOY_OR_MOVE=2; SELL_UNIT=6 | BUY_UNIT=5; DEPLOY_OR_MOVE=1; SELL_UNIT=3 | 3-6 | -12.000 | 13.000 | 0.000 | -12.0 / 11.0 / 0.0 | 6 |
| Jogador 6 | 3-5 | HOLD=1; SELL_UNIT=5 | BUY_UNIT=2; DEPLOY_OR_MOVE=3; HOLD=1 | 3-6 | 0.000 | 0.000 | 0.000 | 0.0 / 0.0 / 0.0 | 5 |
| Jogador 7 | 3-5 | DEPLOY_OR_MOVE=7 | BUY_UNIT=3; DEPLOY_OR_MOVE=3; HOLD=1 | 3-6 | -10.000 | -1.000 | 0.000 | -10.0 / 1.0 / 0.0 | 4 |
| Jogador 8 | 3-5 | BUY_UNIT=3; SELL_UNIT=3; BUY_XP=3 | BUY_UNIT=5; SELL_UNIT=4 | 3-6 | -9.000 | 12.000 | 0.000 | -9.0 / 13.0 / 4.0 | 7 |
| Jogador 1 | 3-6 | BUY_UNIT=6 | BUY_UNIT=2; DEPLOY_OR_MOVE=3; HOLD=1 | 3-7 | 0.000 | 11.000 | 0.000 | 0.0 / 21.0 / 0.0 | 1 |
| Jogador 2 | 3-6 | BUY_UNIT=9 | SELL_UNIT=3; BUY_UNIT=3; DEPLOY_OR_MOVE=3 | 3-7 | 0.000 | 7.000 | 0.000 | 0.0 / 0.0 / 2.0 | 2 |
| Jogador 3 | 3-6 | BUY_UNIT=5; SELL_UNIT=4 | SELL_UNIT=2; BUY_UNIT=4; BUY_EXPERIENCE=1; DEPLOY_OR_MOVE=2 | 3-7 | 0.000 | 11.000 | 0.000 | -12.0 / 14.0 / 2.0 | 3 |
| Jogador 4 | 3-6 | BUY_UNIT=6; SELL_UNIT=3 | SELL_UNIT=2; BUY_UNIT=3; DEPLOY_OR_MOVE=3; HOLD=1 | 3-7 | 0.000 | 4.000 | 0.000 | -14.0 / 14.0 / -4.0 | 8 |
| Jogador 5 | 3-6 | SELL_UNIT=9 | BUY_UNIT=4; SELL_UNIT=5 | 3-7 | 0.000 | -2.000 | 0.000 | -11.0 / 6.0 / 0.0 | 6 |
| Jogador 6 | 3-6 | SELL_UNIT=6 | BUY_UNIT=3; DEPLOY_OR_MOVE=2; HOLD=1 | 3-7 | 0.000 | 0.000 | 0.000 | -12.0 / -2.0 / 0.0 | 5 |
| Jogador 7 | 3-6 | SELL_UNIT=5 | BUY_UNIT=2; DEPLOY_OR_MOVE=2; HOLD=1 | 3-7 | 0.000 | 2.000 | 0.000 | 0.0 / 7.0 / 0.0 | 4 |
| Jogador 8 | 3-6 | BUY_UNIT=2; BUY_XP=7 | BUY_UNIT=4; SELL_UNIT=5 | 3-7 | 0.000 | 1.000 | 4.000 | 0.0 / 5.0 / 4.0 | 7 |
| Jogador 1 | 3-7 | BUY_UNIT=5 | SELL_UNIT=1; BUY_UNIT=1; DEPLOY_OR_MOVE=2; HOLD=1 | 4-1 | 0.000 | 10.000 | 0.000 | 0.0 / 23.0 / 0.0 | 1 |
| Jogador 2 | 3-7 | BUY_UNIT=4; DEPLOY_OR_MOVE=5 | SELL_UNIT=4; BUY_UNIT=4; BUY_EXPERIENCE=1 | 4-1 | 0.000 | -7.000 | 2.000 | 0.0 / -1.0 / 2.0 | 2 |
| Jogador 3 | 3-7 | BUY_UNIT=1; SELL_UNIT=6 | SELL_UNIT=2; BUY_UNIT=2; DEPLOY_OR_MOVE=2; HOLD=1 | 4-1 | -12.000 | 3.000 | 2.000 | -12.0 / 20.0 / 2.0 | 3 |
| Jogador 4 | 3-7 | BUY_UNIT=1; SELL_UNIT=4 | BUY_UNIT=1; DEPLOY_OR_MOVE=3; HOLD=1 | 4-1 | -14.000 | 10.000 | -4.000 | -25.0 / 18.0 / -2.0 | 8 |
| Jogador 5 | 3-7 | BUY_UNIT=2; SELL_UNIT=7 | BUY_UNIT=6; SELL_UNIT=2; REROLL_SHOP=1 | 4-1 | -11.000 | 8.000 | 0.000 | -21.0 / 21.0 / 0.0 | 6 |
| Jogador 6 | 3-7 | SELL_UNIT=5; BUY_UNIT=2 | BUY_UNIT=2; DEPLOY_OR_MOVE=3; SELL_UNIT=1; HOLD=1 | 4-1 | -12.000 | -2.000 | 0.000 | -12.0 / 2.0 / 0.0 | 5 |
| Jogador 7 | 3-7 | BUY_UNIT=3; SELL_UNIT=3 | BUY_UNIT=2; SELL_UNIT=1; DEPLOY_OR_MOVE=2; HOLD=1 | 4-1 | 0.000 | 5.000 | 0.000 | -12.0 / 12.0 / 0.0 | 4 |
| Jogador 8 | 3-7 | DEPLOY_OR_MOVE=5; BUY_UNIT=1; SELL_UNIT=3 | BUY_UNIT=5; DEPLOY_OR_MOVE=4 | 4-1 | 0.000 | 4.000 | 0.000 | -12.0 / 13.0 / 0.0 | 7 |
| Jogador 1 | 4-1 | SELL_UNIT=8; BUY_UNIT=1 | SELL_UNIT=1; BUY_UNIT=1; DEPLOY_OR_MOVE=5 | 4-2 | 0.000 | 13.000 | 0.000 | 0.0 / 23.0 / 4.0 | 1 |
| Jogador 2 | 4-1 | DEPLOY_OR_MOVE=9 | BUY_UNIT=3; SELL_UNIT=1; BUY_EXPERIENCE=2; DEPLOY_OR_MOVE=1 | 4-2 | 0.000 | 6.000 | 0.000 | -13.0 / 17.0 / 0.0 | 2 |
| Jogador 3 | 4-1 | BUY_UNIT=6; SELL_UNIT=3 | SELL_UNIT=2; BUY_UNIT=4; DEPLOY_OR_MOVE=1 | 4-2 | 0.000 | 17.000 | 0.000 | 0.0 / 27.0 / -2.0 | 3 |
| Jogador 4 | 4-1 | SELL_UNIT=8; BUY_UNIT=1 | DEPLOY_OR_MOVE=4; SELL_UNIT=1; BUY_UNIT=1; HOLD=1 | 4-2 | -11.000 | 8.000 | 2.000 | -25.0 / 19.0 / 6.0 | 8 |
| Jogador 5 | 4-1 | BUY_UNIT=2; SELL_UNIT=7 | BUY_UNIT=4; SELL_UNIT=3 | 4-2 | -10.000 | 13.000 | 0.000 | -22.0 / 27.0 / 0.0 | 6 |
| Jogador 6 | 4-1 | BUY_UNIT=8; SELL_UNIT=1 | SELL_UNIT=2; BUY_UNIT=2; BUY_EXPERIENCE=2; DEPLOY_OR_MOVE=1 | 4-2 | 0.000 | 4.000 | 0.000 | 0.0 / 14.0 / 0.0 | 5 |
| Jogador 7 | 4-1 | SELL_UNIT=8; HOLD=1 | SELL_UNIT=2; BUY_UNIT=2; DEPLOY_OR_MOVE=2; HOLD=1 | 4-2 | -12.000 | 7.000 | 0.000 | -12.0 / 15.0 / 0.0 | 4 |
| Jogador 8 | 4-1 | BUY_UNIT=3; SELL_UNIT=6 | BUY_UNIT=5; SELL_UNIT=2 | 4-2 | -12.000 | 9.000 | 0.000 | -24.0 / 24.0 / 0.0 | 7 |
| Jogador 1 | 4-2 | BUY_UNIT=4; SELL_UNIT=5 | SELL_UNIT=2; BUY_UNIT=2; DEPLOY_OR_MOVE=4; HOLD=1 | 4-3 | 0.000 | 10.000 | 4.000 | 0.0 / 16.0 / 4.0 | 1 |
| Jogador 2 | 4-2 | BUY_UNIT=1; SELL_UNIT=5 | BUY_UNIT=3; DEPLOY_OR_MOVE=2; HOLD=1 | 4-3 | -13.000 | 11.000 | 0.000 | -13.0 / 20.0 / 0.0 | 2 |
| Jogador 3 | 4-2 | SELL_UNIT=9 | SELL_UNIT=4; BUY_UNIT=4; DEPLOY_OR_MOVE=1 | 4-3 | 0.000 | 10.000 | -2.000 | 0.0 / 25.0 / -2.0 | 3 |
| Jogador 4 | 4-2 | BUY_XP=6; SELL_UNIT=1 | SELL_UNIT=2; BUY_UNIT=2; DEPLOY_OR_MOVE=2; HOLD=1 | 4-3 | -14.000 | 11.000 | 4.000 | -14.0 / 16.0 / 10.0 | 8 |
| Jogador 5 | 4-2 | BUY_UNIT=2; SELL_UNIT=7 | SELL_UNIT=4; BUY_UNIT=4; DEPLOY_OR_MOVE=1 | 4-3 | -12.000 | 14.000 | 0.000 | -12.0 / 25.0 / 4.0 | 6 |
| Jogador 6 | 4-2 | BUY_UNIT=4; SELL_UNIT=4 | SELL_UNIT=2; BUY_UNIT=3; DEPLOY_OR_MOVE=2; HOLD=1 | 4-3 | 0.000 | 10.000 | 0.000 | 0.0 / 16.0 / 0.0 | 5 |
| Jogador 7 | 4-2 | BUY_UNIT=8 | SELL_UNIT=2; BUY_UNIT=2; DEPLOY_OR_MOVE=3; HOLD=1 | 4-3 | 0.000 | 8.000 | 0.000 | 0.0 / 15.0 / 0.0 | 4 |
| Jogador 8 | 4-2 | BUY_UNIT=3; SELL_UNIT=6 | BUY_UNIT=5; SELL_UNIT=4 | 4-3 | -12.000 | 15.000 | 0.000 | -12.0 / 25.0 / 0.0 | 7 |
| Jogador 1 | 4-3 | BUY_UNIT=2; DEPLOY_OR_MOVE=7 | SELL_UNIT=3; BUY_UNIT=3; BUY_EXPERIENCE=1; DEPLOY_OR_MOVE=2 | 4-4 | 0.000 | 6.000 | 0.000 | -12.0 / 15.0 / 0.0 | 1 |
| Jogador 2 | 4-3 | SELL_UNIT=8; BUY_UNIT=1 | SELL_UNIT=3; BUY_UNIT=3; DEPLOY_OR_MOVE=3 | 4-4 | 0.000 | 9.000 | 0.000 | 0.0 / 20.0 / 0.0 | 2 |
| Jogador 3 | 4-3 | BUY_UNIT=1; SELL_UNIT=8 | SELL_UNIT=2; BUY_UNIT=2; DEPLOY_OR_MOVE=4; HOLD=1 | 4-4 | 0.000 | 15.000 | 0.000 | 0.0 / 29.0 / 0.0 | 3 |
| Jogador 4 | 4-3 | BUY_XP=8 | SELL_UNIT=1; BUY_UNIT=1; DEPLOY_OR_MOVE=2; HOLD=1 | 4-4 | 0.000 | 5.000 | 6.000 | -2.0 / 3.0 / -26.0 | 8 |
| Jogador 5 | 4-3 | SELL_UNIT=9 | SELL_UNIT=5; BUY_UNIT=4 | 4-4 | 0.000 | 11.000 | 4.000 | -13.0 / 21.0 / 4.0 | 6 |
| Jogador 6 | 4-3 | BUY_UNIT=5; SELL_UNIT=3 | BUY_UNIT=2; DEPLOY_OR_MOVE=4; SELL_UNIT=1; HOLD=1 | 4-4 | 0.000 | 6.000 | 0.000 | 0.0 / 18.0 / 0.0 | 5 |
| Jogador 7 | 4-3 | HOLD=1; SELL_UNIT=6 | SELL_UNIT=2; BUY_UNIT=2; DEPLOY_OR_MOVE=2; HOLD=1 | 4-4 | 0.000 | 7.000 | 0.000 | 0.0 / 16.0 / 0.0 | 4 |
| Jogador 8 | 4-3 | BUY_UNIT=8; SELL_UNIT=1 | SELL_UNIT=5; BUY_UNIT=4 | 4-4 | 0.000 | 10.000 | 0.000 | -12.0 / 6.0 / -22.0 | 7 |
| Jogador 1 | 4-4 | SELL_UNIT=6 | BUY_UNIT=2; DEPLOY_OR_MOVE=3; HOLD=1 | 4-5 | -12.000 | 9.000 | 0.000 | -12.0 / -4.0 / -4.0 | 1 |
| Jogador 2 | 4-4 | SELL_UNIT=9 | SELL_UNIT=4; BUY_UNIT=4; DEPLOY_OR_MOVE=1 | 4-5 | 0.000 | 11.000 | 0.000 | -10.0 / 22.0 / 2.0 | 2 |
| Jogador 3 | 4-4 | SELL_UNIT=8; BUY_UNIT=1 | SELL_UNIT=5; BUY_UNIT=4 | 4-5 | 0.000 | 14.000 | 0.000 | -12.0 / 23.0 / 0.0 | 3 |
| Jogador 4 | 4-4 | DEPLOY_OR_MOVE=1; BUY_UNIT=8 | DEPLOY_OR_MOVE=3; BUY_UNIT=3; SELL_UNIT=2; REROLL_SHOP=1 | 4-5 | -2.000 | -2.000 | -32.000 | None / None / None | 8 |
| Jogador 5 | 4-4 | BUY_UNIT=4; DEPLOY_OR_MOVE=2; SELL_UNIT=3 | BUY_UNIT=4; DEPLOY_OR_MOVE=2; SELL_UNIT=1 | 4-5 | -13.000 | 10.000 | 0.000 | -22.0 / 10.0 / -22.0 | 6 |
| Jogador 6 | 4-4 | BUY_UNIT=4; SELL_UNIT=4 | SELL_UNIT=2; BUY_UNIT=3; DEPLOY_OR_MOVE=2; HOLD=1 | 4-5 | 0.000 | 12.000 | 0.000 | 0.0 / 36.0 / 0.0 | 5 |
| Jogador 7 | 4-4 | BUY_UNIT=8 | SELL_UNIT=2; BUY_UNIT=2; DEPLOY_OR_MOVE=3; HOLD=1 | 4-5 | 0.000 | 9.000 | 0.000 | 0.0 / 15.0 / 2.0 | 4 |
| Jogador 8 | 4-4 | BUY_UNIT=9 | BUY_UNIT=5; SELL_UNIT=4 | 4-5 | -12.000 | -4.000 | -22.000 | None / None / None | 7 |
| Jogador 1 | 4-5 | SELL_UNIT=9 | SELL_UNIT=2; BUY_UNIT=2; DEPLOY_OR_MOVE=4; HOLD=1 | 4-6 | 0.000 | -13.000 | -4.000 | 0.0 / -42.0 / -4.0 | 1 |
| Jogador 2 | 4-5 | BUY_UNIT=2; SELL_UNIT=7 | SELL_UNIT=3; BUY_UNIT=3; DEPLOY_OR_MOVE=2; HOLD=1 | 4-6 | -10.000 | 11.000 | 2.000 | -10.0 / 17.0 / 2.0 | 2 |
| Jogador 3 | 4-5 | BUY_UNIT=2; SELL_UNIT=7 | BUY_UNIT=4; SELL_UNIT=4; DEPLOY_OR_MOVE=1 | 4-6 | -12.000 | 9.000 | 0.000 | -12.0 / 21.0 / 0.0 | 3 |
| Jogador 4 | 4-5 | BUY_UNIT=6; DEPLOY_OR_MOVE=1 | SELL_UNIT=1; BUY_UNIT=2; DEPLOY_OR_MOVE=3; HOLD=1 | — | — | — | — | None / None / None | 8 |
| Jogador 5 | 4-5 | BUY_UNIT=6; SELL_UNIT=2; HOLD=1 | SELL_UNIT=4; BUY_UNIT=4; REROLL_SHOP=1 | 4-6 | -9.000 | 0.000 | -22.000 | None / None / None | 6 |
| Jogador 6 | 4-5 | BUY_UNIT=1; SELL_UNIT=8 | BUY_UNIT=4; SELL_UNIT=3; DEPLOY_OR_MOVE=2 | 4-6 | 0.000 | 24.000 | 0.000 | 0.0 / 36.0 / 0.0 | 5 |
| Jogador 7 | 4-5 | BUY_UNIT=2; SELL_UNIT=7 | SELL_UNIT=3; BUY_UNIT=3; DEPLOY_OR_MOVE=2; HOLD=1 | 4-6 | 0.000 | 6.000 | 2.000 | 0.0 / 11.0 / 2.0 | 4 |
| Jogador 8 | 4-5 | BUY_UNIT=7; DEPLOY_OR_MOVE=2 | SELL_UNIT=2; BUY_UNIT=4; DEPLOY_OR_MOVE=1 | — | — | — | — | None / None / None | 7 |
| Jogador 1 | 4-6 | BUY_UNIT=2; DEPLOY_OR_MOVE=7 | SELL_UNIT=1; BUY_UNIT=3; BUY_EXPERIENCE=5 | 4-7 | 0.000 | -29.000 | 0.000 | -15.0 / -23.0 / -4.0 | 1 |
| Jogador 2 | 4-6 | BUY_UNIT=4; DEPLOY_OR_MOVE=5 | SELL_UNIT=2; BUY_UNIT=3; DEPLOY_OR_MOVE=2 | 4-7 | 0.000 | 6.000 | 0.000 | 0.0 / 13.0 / 6.0 | 2 |
| Jogador 3 | 4-6 | BUY_UNIT=9 | BUY_UNIT=5; SELL_UNIT=4 | 4-7 | 0.000 | 12.000 | 0.000 | 0.0 / 23.0 / 6.0 | 3 |
| Jogador 5 | 4-6 | BUY_UNIT=2; BUY_XP=7 | SELL_UNIT=3; BUY_UNIT=5; REROLL_SHOP=1 | — | — | — | — | None / None / None | 6 |
| Jogador 6 | 4-6 | BUY_UNIT=2; SELL_UNIT=7 | SELL_UNIT=6; BUY_UNIT=3 | 4-7 | 0.000 | 12.000 | 0.000 | -15.0 / 10.0 / -2.0 | 5 |
| Jogador 7 | 4-6 | BUY_UNIT=2; DEPLOY_OR_MOVE=6; SELL_UNIT=1 | SELL_UNIT=1; BUY_UNIT=3; DEPLOY_OR_MOVE=5 | 4-7 | 0.000 | 5.000 | 0.000 | 0.0 / 21.0 / 0.0 | 4 |
| Jogador 1 | 4-7 | DEPLOY_OR_MOVE=9 | BUY_UNIT=1; BUY_EXPERIENCE=8 | 5-1 | -15.000 | 6.000 | -4.000 | -15.0 / 7.0 / 10.0 | 1 |
| Jogador 2 | 4-7 | DEPLOY_OR_MOVE=9 | SELL_UNIT=4; BUY_UNIT=4; BUY_EXPERIENCE=1 | 5-1 | 0.000 | 7.000 | 6.000 | 0.0 / 16.0 / 6.0 | 2 |
| Jogador 3 | 4-7 | BUY_UNIT=2; SELL_UNIT=7 | SELL_UNIT=4; BUY_UNIT=5 | 5-1 | 0.000 | 11.000 | 6.000 | 0.0 / 21.0 / 6.0 | 3 |
| Jogador 6 | 4-7 | BUY_UNIT=2; DEPLOY_OR_MOVE=6; SELL_UNIT=1 | BUY_UNIT=4; SELL_UNIT=3; DEPLOY_OR_MOVE=2 | 5-1 | -15.000 | -2.000 | -2.000 | -33.0 / 12.0 / 2.0 | 5 |
| Jogador 7 | 4-7 | BUY_UNIT=5 | BUY_UNIT=2; DEPLOY_OR_MOVE=2; HOLD=1 | 5-1 | 0.000 | 16.000 | 0.000 | -13.0 / 29.0 / 0.0 | 4 |
| Jogador 1 | 5-1 | DEPLOY_OR_MOVE=7; BUY_UNIT=2 | SELL_UNIT=2; BUY_UNIT=3; DEPLOY_OR_MOVE=1; BUY_EXPERIENCE=1 | 5-2 | 0.000 | 1.000 | 14.000 | 0.0 / 7.0 / 10.0 | 1 |
| Jogador 2 | 5-1 | DEPLOY_OR_MOVE=5; SELL_UNIT=4 | SELL_UNIT=3; BUY_UNIT=3; DEPLOY_OR_MOVE=1 | 5-2 | 0.000 | 9.000 | 0.000 | 0.0 / 8.0 / -2.0 | 2 |
| Jogador 3 | 5-1 | DEPLOY_OR_MOVE=8; BUY_UNIT=1 | BUY_UNIT=4; SELL_UNIT=2; DEPLOY_OR_MOVE=1 | 5-2 | 0.000 | 10.000 | 0.000 | 0.0 / 13.0 / -4.0 | 3 |
| Jogador 6 | 5-1 | BUY_UNIT=2; DEPLOY_OR_MOVE=7 | BUY_UNIT=4; DEPLOY_OR_MOVE=3 | 5-2 | -18.000 | 14.000 | 4.000 | -27.0 / 3.0 / -26.0 | 5 |
| Jogador 7 | 5-1 | BUY_UNIT=7; SELL_UNIT=2 | SELL_UNIT=2; BUY_UNIT=2; DEPLOY_OR_MOVE=3 | 5-2 | -13.000 | 13.000 | 0.000 | -28.0 / 23.0 / 0.0 | 4 |
| Jogador 1 | 5-2 | DEPLOY_OR_MOVE=7 | BUY_UNIT=2; DEPLOY_OR_MOVE=4; HOLD=1 | 5-3 | 0.000 | 6.000 | -4.000 | 0.0 / 9.0 / -2.0 | 1 |
| Jogador 2 | 5-2 | SELL_UNIT=9 | BUY_UNIT=5; SELL_UNIT=4 | 5-3 | 0.000 | -1.000 | -2.000 | 0.0 / 4.0 / 8.0 | 2 |
| Jogador 3 | 5-2 | BUY_UNIT=2; BUY_XP=3; SELL_UNIT=4 | SELL_UNIT=3; BUY_UNIT=3; DEPLOY_OR_MOVE=3 | 5-3 | 0.000 | 3.000 | -4.000 | 0.0 / 16.0 / 0.0 | 3 |
| Jogador 6 | 5-2 | DEPLOY_OR_MOVE=7; BUY_UNIT=2 | BUY_UNIT=4; SELL_UNIT=2; DEPLOY_OR_MOVE=2; REROLL_SHOP=1 | 5-3 | -9.000 | -11.000 | -30.000 | None / None / None | 5 |
| Jogador 7 | 5-2 | BUY_UNIT=6; SELL_UNIT=3 | SELL_UNIT=3; BUY_UNIT=3; DEPLOY_OR_MOVE=3 | 5-3 | -15.000 | 10.000 | 0.000 | -15.0 / 18.0 / 0.0 | 4 |
| Jogador 1 | 5-3 | BUY_UNIT=3; DEPLOY_OR_MOVE=6 | BUY_UNIT=3; SELL_UNIT=1; DEPLOY_OR_MOVE=1; BUY_EXPERIENCE=1 | 5-4 | 0.000 | 3.000 | 2.000 | 0.0 / 9.0 / 2.0 | 1 |
| Jogador 2 | 5-3 | BUY_UNIT=2; DEPLOY_OR_MOVE=7 | SELL_UNIT=2; BUY_UNIT=3; DEPLOY_OR_MOVE=1; BUY_EXPERIENCE=3 | 5-4 | 0.000 | 5.000 | 10.000 | -15.0 / 5.0 / 20.0 | 2 |
| Jogador 3 | 5-3 | BUY_UNIT=4; DEPLOY_OR_MOVE=5 | SELL_UNIT=3; BUY_UNIT=4; BUY_EXPERIENCE=2 | 5-4 | 0.000 | 13.000 | 4.000 | 0.0 / 19.0 / 4.0 | 3 |
| Jogador 6 | 5-3 | BUY_UNIT=9 | BUY_UNIT=4; SELL_UNIT=2; REROLL_SHOP=1 | — | — | — | — | None / None / None | 5 |
| Jogador 7 | 5-3 | BUY_UNIT=9 | SELL_UNIT=3; BUY_UNIT=3; DEPLOY_OR_MOVE=3 | 5-4 | 0.000 | 8.000 | 0.000 | -16.0 / 8.0 / -28.0 | 4 |
| Jogador 1 | 5-4 | DEPLOY_OR_MOVE=9 | SELL_UNIT=1; BUY_UNIT=1; DEPLOY_OR_MOVE=2; BUY_EXPERIENCE=3 | 5-5 | 0.000 | 6.000 | 0.000 | 0.0 / 17.0 / 0.0 | 1 |
| Jogador 2 | 5-4 | DEPLOY_OR_MOVE=9 | SELL_UNIT=2; BUY_UNIT=3; DEPLOY_OR_MOVE=3; BUY_EXPERIENCE=1 | 5-5 | -15.000 | 0.000 | 10.000 | -15.0 / 10.0 / 10.0 | 2 |
| Jogador 3 | 5-4 | DEPLOY_OR_MOVE=9 | SELL_UNIT=4; BUY_UNIT=4; DEPLOY_OR_MOVE=1 | 5-5 | 0.000 | 6.000 | 0.000 | -15.0 / 17.0 / 0.0 | 3 |
| Jogador 7 | 5-4 | BUY_UNIT=6; SELL_UNIT=3 | SELL_UNIT=3; BUY_UNIT=5; DEPLOY_OR_MOVE=1 | 5-5 | -16.000 | 0.000 | -28.000 | None / None / None | 4 |
| Jogador 1 | 5-5 | SELL_UNIT=5 | BUY_UNIT=1; DEPLOY_OR_MOVE=3; HOLD=1 | 5-6 | 0.000 | 11.000 | 0.000 | 0.0 / 22.0 / 10.0 | 1 |
| Jogador 2 | 5-5 | DEPLOY_OR_MOVE=3; SELL_UNIT=1; BUY_UNIT=4 | BUY_UNIT=3; DEPLOY_OR_MOVE=4; HOLD=1 | 5-6 | 0.000 | 10.000 | 0.000 | 0.0 / 21.0 / 0.0 | 2 |
| Jogador 3 | 5-5 | SELL_UNIT=9 | BUY_UNIT=4; SELL_UNIT=3; DEPLOY_OR_MOVE=2 | 5-6 | -15.000 | 11.000 | 0.000 | -15.0 / 25.0 / 0.0 | 3 |
| Jogador 7 | 5-5 | BUY_UNIT=8; SELL_UNIT=1 | SELL_UNIT=4; BUY_UNIT=4; DEPLOY_OR_MOVE=1 | — | — | — | — | None / None / None | 4 |
| Jogador 1 | 5-6 | BUY_UNIT=3 | DEPLOY_OR_MOVE=2; HOLD=1 | 5-7 | 0.000 | 11.000 | 10.000 | 0.0 / 13.0 / 10.0 | 1 |
| Jogador 2 | 5-6 | BUY_UNIT=8 | SELL_UNIT=1; BUY_UNIT=1; DEPLOY_OR_MOVE=3; HOLD=1 | 5-7 | 0.000 | 11.000 | 0.000 | 0.0 / 21.0 / 0.0 | 2 |
| Jogador 3 | 5-6 | SELL_UNIT=9 | SELL_UNIT=3; BUY_UNIT=3; DEPLOY_OR_MOVE=3 | 5-7 | 0.000 | 14.000 | 0.000 | -19.0 / 24.0 / 0.0 | 3 |
| Jogador 1 | 5-7 | DEPLOY_OR_MOVE=4 | DEPLOY_OR_MOVE=3; HOLD=1 | 6-1 | 0.000 | 2.000 | 0.000 | 0.0 / -9.0 / -4.0 | 1 |
| Jogador 2 | 5-7 | BUY_UNIT=3; SELL_UNIT=6 | SELL_UNIT=3; BUY_UNIT=3; DEPLOY_OR_MOVE=3 | 6-1 | 0.000 | 10.000 | 0.000 | 0.0 / 23.0 / 0.0 | 2 |
| Jogador 3 | 5-7 | BUY_UNIT=2; SELL_UNIT=4; BUY_XP=3 | SELL_UNIT=4; BUY_UNIT=4; DEPLOY_OR_MOVE=1 | 6-1 | -19.000 | 10.000 | 0.000 | -37.0 / 20.0 / -6.0 | 3 |
| Jogador 1 | 6-1 | BUY_UNIT=8 | BUY_UNIT=3; DEPLOY_OR_MOVE=3; HOLD=1 | 6-2 | 0.000 | -11.000 | -4.000 | 0.0 / -36.0 / -4.0 | 1 |
| Jogador 2 | 6-1 | SELL_UNIT=9 | SELL_UNIT=3; BUY_UNIT=3; DEPLOY_OR_MOVE=2 | 6-2 | 0.000 | 13.000 | 0.000 | 0.0 / 23.0 / 0.0 | 2 |
| Jogador 3 | 6-1 | BUY_UNIT=3; DEPLOY_OR_MOVE=6 | SELL_UNIT=3; BUY_UNIT=4; DEPLOY_OR_MOVE=1 | 6-2 | -18.000 | 10.000 | -6.000 | -23.0 / 7.0 / -36.0 | 3 |
| Jogador 1 | 6-2 | BUY_UNIT=2; DEPLOY_OR_MOVE=7 | SELL_UNIT=1; BUY_UNIT=1; BUY_EXPERIENCE=6 | 6-3 | 0.000 | -25.000 | 0.000 | 0.0 / -14.0 / 16.0 | 1 |
| Jogador 2 | 6-2 | BUY_UNIT=8; SELL_UNIT=1 | SELL_UNIT=5; BUY_UNIT=4 | 6-3 | 0.000 | 10.000 | 0.000 | 0.0 / 2.0 / 0.0 | 2 |
| Jogador 3 | 6-2 | BUY_UNIT=1; DEPLOY_OR_MOVE=8 | BUY_UNIT=5; SELL_UNIT=3; REROLL_SHOP=1 | 6-3 | -5.000 | -3.000 | -30.000 | None / None / None | 3 |
| Jogador 1 | 6-3 | DEPLOY_OR_MOVE=9 | BUY_EXPERIENCE=9 | 6-4 | 0.000 | 11.000 | 16.000 | 0.0 / 20.0 / 24.0 | 1 |
| Jogador 2 | 6-3 | BUY_UNIT=5; SELL_UNIT=2; HOLD=2 | BUY_UNIT=5; SELL_UNIT=4 | 6-4 | 0.000 | -8.000 | 0.000 | -21.0 / 7.0 / -2.0 | 2 |
| Jogador 3 | 6-3 | DEPLOY_OR_MOVE=9 | SELL_UNIT=4; BUY_UNIT=4; REROLL_SHOP=1 | — | — | — | — | None / None / None | 3 |
| Jogador 1 | 6-4 | DEPLOY_OR_MOVE=1 | HOLD=1 | 6-5 | 0.000 | 9.000 | 8.000 | 0.0 / 7.0 / 14.0 | 1 |
| Jogador 2 | 6-4 | BUY_UNIT=6; SELL_UNIT=3 | SELL_UNIT=2; BUY_UNIT=4; BUY_EXPERIENCE=3 | 6-5 | -21.000 | 15.000 | -2.000 | -24.0 / 11.0 / -52.0 | 2 |
| Jogador 1 | 6-5 | DEPLOY_OR_MOVE=6 | BUY_UNIT=1; DEPLOY_OR_MOVE=4; HOLD=1 | 6-6 | 0.000 | -2.000 | 6.000 | None / None / None | 1 |
| Jogador 2 | 6-5 | BUY_UNIT=4; DEPLOY_OR_MOVE=5 | SELL_UNIT=3; BUY_UNIT=4; DEPLOY_OR_MOVE=2 | 6-6 | -3.000 | -4.000 | -50.000 | None / None / None | 2 |
| Jogador 1 | 6-6 | DEPLOY_OR_MOVE=4 | BUY_UNIT=1; DEPLOY_OR_MOVE=2; HOLD=1 | — | — | — | — | None / None / None | 1 |
| Jogador 2 | 6-6 | BUY_UNIT=8; SELL_UNIT=1 | BUY_UNIT=4; SELL_UNIT=3 | — | — | — | — | None / None / None | 2 |

## Último estado vivo preservado por jogador

| Jogador | HP último estado vivo | Ouro | Nível | Board power | Direção | Win streak | Loss streak | Colocação final | HP terminal |
|---|---:|---:|---:|---:|---|---:|---:|---:|---:|
| Jogador 5 | 9.000 | 111 | 6 | 22.000 | Enfeitiçador | 0 | 7 | 6 | 0.000 |
| Jogador 2 | 3.000 | 156 | 8 | 50.000 | Feérico | 0 | 1 | 2 | 0.000 |
| Jogador 7 | 16.000 | 102 | 7 | 28.000 | Colosso | 0 | 2 | 4 | 0.000 |
| Jogador 3 | 5.000 | 206 | 7 | 30.000 | Colosso | 0 | 3 | 3 | 0.000 |
| Jogador 8 | 12.000 | 132 | 6 | 26.000 | Enfeitiçador | 0 | 2 | 7 | 0.000 |
| Jogador 6 | 9.000 | 74 | 7 | 30.000 | Feérico | 0 | 2 | 5 | 0.000 |
| Jogador 1 | 73.000 | 56 | 10 | 76.000 | Adaptador | 8 | 0 | 1 | 73.000 |
| Jogador 4 | 2.000 | 67 | 7 | 28.000 | Florescer | 0 | 3 | 8 | 0.000 |

Os deltas imediatos medem apenas a transição registrada após a ação. O resultado de combate aparece uma única vez por jogador/round. A tabela de evolução liga o conjunto de recomendações daquele round aos próximos um e dois rounds; é associação temporal, não causalidade. O estado vivo é preservado separadamente do estado terminal de eliminação. Dados ausentes permanecem como —.
