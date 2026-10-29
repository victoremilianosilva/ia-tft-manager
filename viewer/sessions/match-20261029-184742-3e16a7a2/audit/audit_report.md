# Auditoria da partida TFT

- Arquivos lidos: **8**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Entradas JSON analisadas: **3769**
- Achados: **47**
- CRITICAL: 0 | HIGH: 16 | MEDIUM: 31 | LOW: 0

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 129 | 129 | 129 | 0 | 125 | 0 | 129 | 129 | 128 | 17/7 |
| Jogador 2 | 107 | 107 | 107 | 0 | 104 | 0 | 107 | 107 | 107 | 30/15 |
| Jogador 3 | 119 | 119 | 119 | 0 | 118 | 0 | 119 | 119 | 109 | 23/9 |
| Jogador 4 | 95 | 95 | 95 | 0 | 95 | 0 | 95 | 95 | 78 | 24/10 |
| Jogador 5 | 76 | 76 | 76 | 0 | 75 | 0 | 76 | 76 | 64 | 19/8 |
| Jogador 6 | 107 | 107 | 107 | 0 | 107 | 0 | 107 | 107 | 92 | 30/16 |
| Jogador 7 | 112 | 112 | 112 | 0 | 109 | 0 | 112 | 112 | 112 | 26/11 |
| Jogador 8 | 109 | 109 | 109 | 0 | 109 | 0 | 109 | 109 | 95 | 27/14 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0013076922623440623 | 0.0 | 0.0 | +— / -ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +a8111a04-3067-4ce6-9a4b-4f5bb205f413 / -— |
| Jogador 1 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.612060546875 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9794912934303284 | 0.0 | 0.0 | +cde2c30a-df2c-4275-86ef-e4a4a13a5be1 / -— |
| Jogador 1 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15270057320594788 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 13 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10814932733774185 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5613429546356201 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 15 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.22410883009433746 | 0.0 | 0.0 | +24247863-54d4-4674-86e9-9a45609a440e / -— |
| Jogador 1 | 1-3 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4899636209011078 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 23 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006554620806127787 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 24 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.049634214490652084 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3989794850349426 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 26 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9705076217651367 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 32 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7304418683052063 | 0.0 | 0.0 | +— / -cde2c30a-df2c-4275-86ef-e4a4a13a5be1 |
| Jogador 1 | 1-4 | 33 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0205076932907104 | 0.0 | 0.0 | +— / -c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 1-4 | 34 | PASS | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9717366099357605 | 0.0 | 0.0 | +2ffdabd7-c3ce-44f6-ba26-de66bd2c7216 / -— |
| Jogador 1 | 2-1 | 42 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3359365463256836 | 0.0 | 0.0 | +18082e05-51e8-4142-b541-c3d7d781b878 / -— |
| Jogador 1 | 2-1 | 43 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2971804141998291 | 0.0 | 0.0 | +e2e6d682-b207-4a6c-858b-9a3c5c11a38d / -— |
| Jogador 1 | 2-1 | 44 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15800000727176666 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 45 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5236830115318298 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 46 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34718042612075806 | 0.0 | 0.0 | +— / -e2e6d682-b207-4a6c-858b-9a3c5c11a38d |
| Jogador 1 | 2-1 | 47 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 51 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4668218493461609 | 0.0 | 0.0 | +7ca9b803-76eb-4283-9648-7f98bfd81149 / -— |
| Jogador 1 | 2-2 | 52 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06813739240169525 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 53 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04450000077486038 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 54 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6379247903823853 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 55 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0046905349008738995 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 56 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2952626049518585 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 57 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 61 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 62 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.046821143478155136 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 63 | PASS | STABILIZE | 100.0 | 5 | 7 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 71 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 14 | 1 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3065583407878876 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 72 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 14 | 1 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 73 | PASS | STABILIZE | 100.0 | 5 | 14 | 1 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 81 | BUY | STABILIZE | 100.0 | 5 | 21 | 2 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27735310792922974 | 0.0 | 0.0 | +35e1a0f6-207d-4df2-b096-fc07962d094a / -— |
| Jogador 1 | 2-5 | 82 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 18 | 1 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36936986446380615 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 83 | BUY_XP | STABILIZE | 100.0 | 5 | 18 | 1 | 22.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 84 | BUY_XP | STABILIZE | 100.0 | 5 | 14 | 1 | 22.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 85 | BUY_XP | STABILIZE | 100.0 | 5 | 10 | 1 | 22.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 86 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 22.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02449999935925007 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 87 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 2 | 0 | 22.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2360183596611023 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 88 | PASS | STABILIZE | 100.0 | 6 | 2 | 0 | 22.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 89 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 2 | 0 | 22.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4936164915561676 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 91 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 9 | 0 | 24.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2480742633342743 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 92 | BUY | STABILIZE | 100.0 | 6 | 9 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08625530451536179 | 0.0 | 0.0 | +837b2d09-a207-4830-b36d-29e493bbcc22 / -— |
| Jogador 1 | 2-6 | 93 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 6 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024458374828100204 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 94 | BUY_XP | STABILIZE | 100.0 | 6 | 6 | 0 | 24.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 95 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 2 | 0 | 24.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006830052472651005 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 96 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 2 | 0 | 24.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1509602665901184 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 97 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 2 | 0 | 24.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31764087080955505 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 98 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 2 | 0 | 24.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05740860849618912 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 99 | PASS | STABILIZE | 100.0 | 6 | 2 | 0 | 24.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 101 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 10 | 1 | 24.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31247198581695557 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 102 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 10 | 1 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06074532866477966 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 103 | PASS | STABILIZE | 100.0 | 6 | 10 | 1 | 24.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 111 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 18 | 1 | 24.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03186683729290962 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 112 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 18 | 1 | 24.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31072738766670227 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 113 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 18 | 1 | 20.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008046221919357777 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 114 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 18 | 1 | 24.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6308563947677612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 115 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 18 | 1 | 20.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27079781889915466 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 116 | PASS | STABILIZE | 100.0 | 6 | 18 | 1 | 20.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 121 | MOVE_BENCH | STABILIZE | 88.0 | 6 | 24 | 2 | 20.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013650464825332165 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 122 | MOVE_BENCH | STABILIZE | 88.0 | 6 | 24 | 2 | 24.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6304919719696045 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 123 | MOVE_BENCH | STABILIZE | 88.0 | 6 | 24 | 2 | 20.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2763637900352478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 124 | PASS | STABILIZE | 88.0 | 6 | 24 | 2 | 24.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 131 | BUY | SLOWROLL | 88.0 | 6 | 32 | 3 | 24.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.628175675868988 | 0.0 | 0.0 | +cf68219b-1d38-45a1-98db-495871c932ea / -— |
| Jogador 1 | 3-3 | 132 | BUY_XP | STABILIZE | 88.0 | 6 | 29 | 2 | 24.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 133 | BUY_XP | STABILIZE | 88.0 | 6 | 25 | 2 | 24.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 134 | BUY_XP | STABILIZE | 88.0 | 6 | 21 | 2 | 24.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 135 | BUY_XP | STABILIZE | 88.0 | 6 | 17 | 1 | 24.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 136 | BUY_XP | STABILIZE | 88.0 | 6 | 13 | 1 | 24.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.045499999076128006 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 137 | MOVE_BENCH | STABILIZE | 88.0 | 7 | 9 | 0 | 24.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5873540043830872 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 138 | BUY_XP | STABILIZE | 88.0 | 7 | 9 | 0 | 26.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 139 | BUY_XP | STABILIZE | 88.0 | 7 | 5 | 0 | 26.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 141 | MOVE_BENCH | STABILIZE | 88.0 | 7 | 8 | 0 | 26.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31987226009368896 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 142 | BUY_XP | STABILIZE | 88.0 | 7 | 8 | 0 | 30.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 143 | BUY_XP | STABILIZE | 88.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 144 | SELL | STABILIZE | 88.0 | 7 | 0 | 0 | 30.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7342392206192017 | 0.0 | 0.0 | +— / -a8111a04-3067-4ce6-9a4b-4f5bb205f413 |
| Jogador 1 | 3-4 | 145 | SELL | STABILIZE | 88.0 | 7 | 1 | 0 | 30.0 | Colosso/DA_18_Diana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.750076949596405 | 0.0 | 0.0 | +— / -cf68219b-1d38-45a1-98db-495871c932ea |
| Jogador 1 | 3-4 | 146 | BUY_XP | STABILIZE | 88.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 147 | PASS | STABILIZE | 88.0 | 7 | 0 | 0 | 30.0 | Colosso/DA_18_Diana | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 151 | BUY_XP | STABILIZE | 88.0 | 7 | 6 | 0 | 30.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 152 | PASS | STABILIZE | 88.0 | 7 | 2 | 0 | 30.0 | Colosso/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 161 | MOVE_BOARD | STABILIZE | 88.0 | 7 | 9 | 0 | 30.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10388842225074768 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 162 | PASS | STABILIZE | 88.0 | 7 | 9 | 0 | 30.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 171 | PASS | STABILIZE | 88.0 | 7 | 17 | 1 | 30.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 181 | BUY | STABILIZE | 88.0 | 7 | 24 | 2 | 30.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.7691758871078491 | 0.0 | 0.0 | +111acae7-a889-409f-a15e-419d250fccd0 / -— |
| Jogador 1 | 4-1 | 182 | CRAFT_AND_EQUIP | STABILIZE | 88.0 | 7 | 21 | 2 | 30.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18937622010707855 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 183 | BUY_XP | STABILIZE | 88.0 | 7 | 21 | 2 | 30.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 184 | BUY_XP | STABILIZE | 88.0 | 7 | 17 | 1 | 30.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 185 | BUY_XP | STABILIZE | 88.0 | 7 | 13 | 1 | 30.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 186 | BUY_XP | STABILIZE | 88.0 | 7 | 9 | 0 | 30.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 187 | BUY_XP | STABILIZE | 88.0 | 7 | 5 | 0 | 30.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 188 | SELL | STABILIZE | 88.0 | 7 | 1 | 0 | 30.0 | Colosso/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9300768971443176 | 0.0 | 0.0 | +— / -111acae7-a889-409f-a15e-419d250fccd0 |
| Jogador 1 | 4-1 | 189 | BUY_XP | STABILIZE | 88.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.05481249839067459 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 191 | BUY | ECON | 88.0 | 8 | 8 | 0 | 30.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08836566656827927 | 0.0 | 0.0 | +6e1d8af0-7f7c-4ec1-967c-e871072bc4e3 / -— |
| Jogador 1 | 4-2 | 192 | BUY | ECON | 88.0 | 8 | 4 | 0 | 30.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6695268750190735 | 0.0 | 0.0 | +815aab3d-cea8-4ca6-aea3-3c9d656e6edd / -— |
| Jogador 1 | 4-2 | 193 | MOVE_BENCH | ECON | 88.0 | 8 | 2 | 0 | 30.0 | Colosso/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1768496334552765 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 194 | MOVE_BENCH | ECON | 88.0 | 8 | 2 | 0 | 34.0 | Colosso/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21289458870887756 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 195 | PASS | WINSTREAK | 88.0 | 8 | 2 | 0 | 38.0 | Colosso/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 199 | MOVE_BENCH | WINSTREAK | 88.0 | 8 | 11 | 1 | 38.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9109521508216858 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 200 | PASS | WINSTREAK | 88.0 | 8 | 11 | 1 | 40.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 207 | PASS | WINSTREAK | 88.0 | 8 | 21 | 2 | 40.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 214 | PASS | WINSTREAK | 88.0 | 8 | 31 | 3 | 40.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 223 | PASS | WINSTREAK | 88.0 | 8 | 43 | 4 | 40.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 232 | PASS | WINSTREAK | 88.0 | 8 | 56 | 5 | 40.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11999999731779099 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 242 | EQUIP_FROM_INVENTORY | WINSTREAK | 88.0 | 8 | 69 | 5 | 40.0 | Colosso/DA_Brambleback18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 243 | BUY | WINSTREAK | 88.0 | 8 | 69 | 5 | 40.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1268010288476944 | 0.0 | 0.0 | +01c587bb-ca4f-4690-9e4b-d1e9c44fd33e / -— |
| Jogador 1 | 5-1 | 244 | PASS | WINSTREAK | 88.0 | 8 | 64 | 5 | 40.0 | Colosso/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18000000715255737 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 252 | PASS | ECON | 74.0 | 8 | 74 | 5 | 40.0 | Colosso/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 262 | PASS | ECON | 58.0 | 8 | 85 | 5 | 40.0 | Colosso/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18000000715255737 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 272 | PASS | ECON | 42.0 | 8 | 96 | 5 | 40.0 | Colosso/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18000000715255737 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 282 | PASS | ECON | 42.0 | 8 | 107 | 5 | 40.0 | Colosso/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 292 | PASS | STABILIZE | 26.0 | 8 | 118 | 5 | 40.0 | Colosso/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18000000715255737 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 302 | BUY | STABILIZE | 26.0 | 8 | 129 | 5 | 40.0 | Colosso/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9410750269889832 | 0.0 | 0.0 | +94e47e85-54f4-4546-af6a-3700e3c325a8 / -— |
| Jogador 1 | 5-7 | 303 | PASS | STABILIZE | 26.0 | 8 | 126 | 5 | 40.0 | Colosso/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18000000715255737 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 312 | EQUIP_FROM_INVENTORY | STABILIZE | 26.0 | 8 | 137 | 5 | 40.0 | Colosso/DA_18_Lux_Primal | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 313 | EQUIP_FROM_INVENTORY | STABILIZE | 26.0 | 8 | 137 | 5 | 40.0 | Colosso/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08136138319969177 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 314 | PASS | STABILIZE | 26.0 | 8 | 137 | 5 | 40.0 | Colosso/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23999999463558197 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 322 | PASS | STABILIZE | 26.0 | 8 | 148 | 5 | 40.0 | Colosso/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23999999463558197 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 332 | PASS | STABILIZE | 26.0 | 8 | 158 | 5 | 40.0 | Colosso/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23999999463558197 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-4 | 342 | PASS | ALL_IN | 8.0 | 8 | 168 | 5 | 40.0 | Colosso/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-5 | 352 | PASS | ALL_IN | 8.0 | 8 | 178 | 5 | 40.0 | Colosso/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-6 | 362 | PASS | ALL_IN | 0.0 | 8 | 178 | 5 | 0.0 | Colosso/DA_18_Lux_Primal | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.010384615510702133 | 0.0 | 0.0 | +— / -fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.22450661659240723 | 0.0 | 0.0 | +292ef825-d326-4dd8-9c42-c47cfc62116f / -— |
| Jogador 2 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.5911702513694763 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9709054827690125 | 0.0 | 0.0 | +94ede66e-59bc-4c41-aabf-f64372e20f9a / -— |
| Jogador 2 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08489282429218292 | 0.0 | 0.0 | +e0168c63-e704-4dde-8311-b514c6f4093b / -— |
| Jogador 2 | 1-2 | 13 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2563977837562561 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05337335169315338 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 15 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3861953020095825 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 16 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9389867186546326 | 0.0 | 0.0 | +046de242-84d0-4f44-a171-345f16a6e719 / -— |
| Jogador 2 | 1-3 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 23 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.63722825050354 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 24 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179251670837402 | 0.0 | 0.0 | +0023ba20-d605-41fb-8002-3b6920635c59 / -292ef825-d326-4dd8-9c42-c47cfc62116f,94ede66e-59bc-4c41-aabf-f64372e20f9a |
| Jogador 2 | 1-4 | 32 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02949407324194908 | 0.0 | 0.0 | +9a6f90da-bbac-4ba0-b2a3-729a1a2deab5 / -— |
| Jogador 2 | 1-4 | 33 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0628623440861702 | 0.0 | 0.0 | +9d9dd707-484b-47f6-ac7c-aff2e7e6f48d / -— |
| Jogador 2 | 1-4 | 34 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3868662416934967 | 0.0 | 0.0 | +— / -0023ba20-d605-41fb-8002-3b6920635c59 |
| Jogador 2 | 1-4 | 35 | REROLL | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 36 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yunara | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9101723432540894 | 0.0 | 0.0 | +57652644-f861-47bc-addd-90760a272b22 / -— |
| Jogador 2 | 1-4 | 37 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9601723551750183 | 0.0 | 0.0 | +— / -57652644-f861-47bc-addd-90760a272b22 |
| Jogador 2 | 1-4 | 38 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yunara | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31606799364089966 | 0.0 | 0.0 | +6770b090-e992-44c8-9223-f5cd6e92f19a / -— |
| Jogador 2 | 1-4 | 39 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3734915256500244 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1113569736480713 | 0.0 | 0.0 | +70d8224e-5996-4629-b4f6-761ef5f01525 / -046de242-84d0-4f44-a171-345f16a6e719,e0168c63-e704-4dde-8311-b514c6f4093b |
| Jogador 2 | 2-1 | 42 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 4.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010384615510702133 | 0.0 | 0.0 | +— / -9d9dd707-484b-47f6-ac7c-aff2e7e6f48d |
| Jogador 2 | 2-1 | 43 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 4.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11660544574260712 | 0.0 | 0.0 | +f19f9e7f-f189-47fe-b571-be5065c6eb39 / -— |
| Jogador 2 | 2-1 | 44 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 4.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3660679757595062 | 0.0 | 0.0 | +— / -6770b090-e992-44c8-9223-f5cd6e92f19a |
| Jogador 2 | 2-1 | 45 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 4.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40417221188545227 | 0.0 | 0.0 | +4274fbd9-759f-48e5-ae6b-c9e3ffed1bd1 / -— |
| Jogador 2 | 2-1 | 46 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 4.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45417219400405884 | 0.0 | 0.0 | +— / -4274fbd9-759f-48e5-ae6b-c9e3ffed1bd1 |
| Jogador 2 | 2-1 | 47 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 4.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44291383028030396 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 48 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37717297673225403 | 0.0 | 0.0 | +— / -70d8224e-5996-4629-b4f6-761ef5f01525 |
| Jogador 2 | 2-1 | 49 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.11935378611087799 | 0.0 | 0.0 | +c70251e8-af44-4466-808f-d49e9e5f57e9 / -— |
| Jogador 2 | 2-2 | 51 | BUY | STABILIZE | 94.0 | 4 | 10 | 1 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21904923021793365 | 0.0 | 0.0 | +8a68772c-3f02-4f2e-882b-4fa69fbb6750 / -— |
| Jogador 2 | 2-2 | 52 | BUY | STABILIZE | 94.0 | 4 | 7 | 0 | 8.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.036088116466999054 | 0.0 | 0.0 | +39cd170c-5fd5-4fa5-9466-e5595299dbe8 / -— |
| Jogador 2 | 2-2 | 53 | SELL | STABILIZE | 94.0 | 4 | 5 | 0 | 8.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1903846114873886 | 0.0 | 0.0 | +— / -c70251e8-af44-4466-808f-d49e9e5f57e9 |
| Jogador 2 | 2-2 | 54 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 6 | 0 | 8.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18958526849746704 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 55 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 6 | 0 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38683581352233887 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 56 | PASS | STABILIZE | 94.0 | 4 | 6 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 61 | BUY | STABILIZE | 90.0 | 4 | 12 | 1 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.279943585395813 | 0.0 | 0.0 | +29f10cb7-6575-47ca-b583-057992a08253 / -— |
| Jogador 2 | 2-3 | 62 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 10 | 1 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7472043037414551 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 63 | BUY | STABILIZE | 90.0 | 4 | 10 | 1 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030879875645041466 | 0.0 | 0.0 | +475e5206-4f54-4bbb-9db9-99d1895f0887 / -— |
| Jogador 2 | 2-3 | 64 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 8 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4381372332572937 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 65 | BUY_XP | STABILIZE | 90.0 | 4 | 8 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 66 | BUY_XP | STABILIZE | 90.0 | 4 | 4 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0494999997317791 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 67 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 0 | 0 | 16.0 | —/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35515543818473816 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 68 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 0 | 0 | 20.0 | —/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23657847940921783 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 69 | SELL | STABILIZE | 90.0 | 5 | 0 | 0 | 22.0 | —/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0017692308174446225 | 0.0 | 0.0 | +— / -475e5206-4f54-4bbb-9db9-99d1895f0887 |
| Jogador 2 | 2-4 | 71 | BUY | LOSS_STREAK | 85.0 | 5 | 8 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19779320061206818 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 2 | 2-4 | 72 | BUY | LOSS_STREAK | 85.0 | 5 | 5 | 0 | 22.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2165713906288147 | 0.0 | 0.0 | +27c9bbc9-ca0c-4ce7-bc7a-fcefe868e847 / -— |
| Jogador 2 | 2-4 | 73 | MOVE_BENCH | LOSS_STREAK | 85.0 | 5 | 2 | 0 | 22.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6156960725784302 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 74 | MOVE_BENCH | LOSS_STREAK | 85.0 | 5 | 2 | 0 | 22.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12027868628501892 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 75 | PASS | LOSS_STREAK | 85.0 | 5 | 2 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 81 | BUY | LOSS_STREAK | 85.0 | 5 | 8 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3768835663795471 | 0.0 | 0.0 | +b32c67a7-6903-403a-9ed6-519ac8487685 / -— |
| Jogador 2 | 2-5 | 82 | MOVE_BENCH | LOSS_STREAK | 85.0 | 5 | 5 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05378035083413124 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 83 | MOVE_BENCH | LOSS_STREAK | 85.0 | 5 | 5 | 0 | 22.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08278486132621765 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 84 | BUY_XP | LOSS_STREAK | 85.0 | 5 | 5 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 85 | MOVE_BOARD | LOSS_STREAK | 85.0 | 5 | 1 | 0 | 24.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2405618280172348 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 86 | PASS | LOSS_STREAK | 85.0 | 5 | 1 | 0 | 24.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 91 | BUY_XP | STABILIZE | 85.0 | 5 | 7 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 92 | PASS | STABILIZE | 85.0 | 5 | 3 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 101 | BUY_XP | STABILIZE | 85.0 | 5 | 10 | 1 | 24.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0754999965429306 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 102 | BUY | STABILIZE | 85.0 | 6 | 6 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09906601160764694 | 0.0 | 0.0 | +1e504283-c5d1-4eb3-915e-20533ec3a756 / -— |
| Jogador 2 | 2-7 | 103 | PASS | STABILIZE | 85.0 | 6 | 3 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 109 | MOVE_BENCH | STABILIZE | 85.0 | 6 | 3 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45299971103668213 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 111 | BUY_XP | ECON | 85.0 | 6 | 9 | 0 | 30.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09799999743700027 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 112 | BUY_XP | ECON | 85.0 | 6 | 5 | 0 | 30.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09799999743700027 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 113 | PASS | ECON | 85.0 | 6 | 1 | 0 | 30.0 | Solar/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 121 | BUY | STABILIZE | 85.0 | 6 | 8 | 0 | 30.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7366498112678528 | 0.0 | 0.0 | +65a6d68c-90ae-4e31-8bbc-82e8ec75b3de / -— |
| Jogador 2 | 3-2 | 122 | PASS | STABILIZE | 85.0 | 6 | 5 | 0 | 30.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 131 | BUY | STABILIZE | 85.0 | 6 | 12 | 1 | 30.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7426517605781555 | 0.0 | 0.0 | +1726bcae-3006-426c-a6c7-4e317e10b637 / -— |
| Jogador 2 | 3-3 | 132 | PASS | STABILIZE | 85.0 | 6 | 10 | 1 | 30.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 141 | PASS | STABILIZE | 85.0 | 6 | 19 | 1 | 30.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 151 | PASS | STABILIZE | 85.0 | 6 | 27 | 2 | 30.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 161 | PASS | SLOWROLL | 85.0 | 6 | 38 | 3 | 30.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 171 | PASS | SLOWROLL | 75.0 | 6 | 46 | 4 | 30.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04500000178813934 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 181 | PASS | SLOWROLL | 75.0 | 6 | 55 | 5 | 30.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11999999731779099 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 191 | PASS | SLOWROLL | 75.0 | 6 | 66 | 5 | 30.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11999999731779099 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 199 | PASS | SLOWROLL | 75.0 | 6 | 78 | 5 | 30.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11999999731779099 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 207 | PASS | SLOWROLL | 75.0 | 6 | 90 | 5 | 30.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11999999731779099 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 214 | PASS | SLOWROLL | 75.0 | 6 | 101 | 5 | 30.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11999999731779099 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 223 | BUY | FAST8 | 62.0 | 7 | 111 | 5 | 30.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7025042772293091 | 0.0 | 0.0 | +1512b230-15a6-405f-9b6b-4387a3091648 / -— |
| Jogador 2 | 4-6 | 224 | BUY | FAST8 | 62.0 | 7 | 108 | 5 | 30.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28226470947265625 | 0.0 | 0.0 | +7a419783-907e-47e2-bf69-29a54ee18a02 / -— |
| Jogador 2 | 4-6 | 225 | PASS | FAST8 | 62.0 | 7 | 106 | 5 | 30.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11999999731779099 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 232 | BUY | FAST8 | 62.0 | 7 | 117 | 5 | 36.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13646750152111053 | 0.0 | 0.0 | +edd2748e-d629-4a8a-8174-4c1ef3f5f852 / -— |
| Jogador 2 | 4-7 | 233 | PASS | FAST8 | 62.0 | 7 | 112 | 5 | 36.0 | Solar/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11999999731779099 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 242 | EQUIP_FROM_INVENTORY | FAST8 | 62.0 | 7 | 122 | 5 | 36.0 | Solar/DA_18_Lux_Elderwood | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 243 | BUY | FAST8 | 62.0 | 7 | 122 | 5 | 36.0 | Solar/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8051998615264893 | 0.0 | 0.0 | +2d5214b0-3e0c-4e71-8664-2459bf616650 / -— |
| Jogador 2 | 5-1 | 244 | BUY | FAST8 | 62.0 | 7 | 119 | 5 | 36.0 | Solar/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9486504793167114 | 0.0 | 0.0 | +d4c27edc-9b7e-4a31-a967-3aa80766b470 / -0b62545c-1de0-47d8-bb4c-119f7e1526b3,65a6d68c-90ae-4e31-8bbc-82e8ec75b3de |
| Jogador 2 | 5-1 | 245 | PASS | STABILIZE | 62.0 | 7 | 116 | 5 | 24.0 | Solar/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 250 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 116 | 5 | 24.0 | Solar/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.14256492257118225 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 252 | PASS | FAST8 | 62.0 | 7 | 128 | 5 | 34.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.18000000715255737 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 260 | MOVE_BENCH | FAST8 | 62.0 | 7 | 128 | 5 | 34.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5518127679824829 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 262 | PASS | FAST8 | 62.0 | 7 | 140 | 5 | 38.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.18000000715255737 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 272 | BUY | FAST8 | 62.0 | 7 | 152 | 5 | 38.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8009774088859558 | 0.0 | 0.0 | +2ac6d717-87f1-4421-929e-1934a9317e72 / -— |
| Jogador 2 | 5-4 | 273 | PASS | FAST8 | 62.0 | 7 | 150 | 5 | 38.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.18000000715255737 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 282 | PASS | FAST8 | 62.0 | 7 | 161 | 5 | 38.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 292 | PASS | FAST8 | 62.0 | 7 | 172 | 5 | 38.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.18000000715255737 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 302 | PASS | FAST8 | 47.0 | 7 | 182 | 5 | 38.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.18000000715255737 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 312 | EQUIP_FROM_INVENTORY | FAST8 | 47.0 | 7 | 192 | 5 | 38.0 | Solar/DA_18_Tristana | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 313 | EQUIP_FROM_INVENTORY | FAST8 | 47.0 | 7 | 192 | 5 | 38.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY, CRAFT_AND_EQUIP | True | — | 0.12254349887371063 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 314 | PASS | FAST8 | 47.0 | 7 | 192 | 5 | 38.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.23999999463558197 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 322 | PASS | STABILIZE | 29.0 | 7 | 203 | 5 | 38.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 332 | BUY | ALL_IN | 12.0 | 7 | 214 | 5 | 38.0 | Solar/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.09756240993738174 | 0.0 | 0.0 | +7904ab26-de3f-4144-b70f-ed620b41c907 / -— |
| Jogador 2 | 6-3 | 333 | PASS | ALL_IN | 12.0 | 7 | 211 | 5 | 38.0 | Solar/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 342 | PASS | ALL_IN | 12.0 | 7 | 222 | 5 | 38.0 | Solar/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 352 | PASS | ALL_IN | 12.0 | 7 | 233 | 5 | 38.0 | Solar/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 362 | PASS | ALL_IN | 12.0 | 7 | 244 | 5 | 38.0 | Solar/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.019615383818745613 | 0.0 | 0.0 | +— / -36f58657-5835-4389-95e9-a7d26464c2aa |
| Jogador 3 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.21530985832214355 | 0.0 | 0.0 | +2cf5ccdc-76f4-4fc8-b12c-7b3b68b1b2c8 / -— |
| Jogador 3 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_RekSai | MOVE_BENCH, SELL, PASS | True | True | 0.5971593260765076 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_RekSai | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_RekSai | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9699749946594238 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_RekSai | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0054244790226221085 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 13 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11883015930652618 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013037105090916157 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 15 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3174000084400177 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 17 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4711304306983948 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.0032916381023824215 | 0.0 | 0.0 | +405de1b8-45c1-4b7f-b044-f12b819507c3 / -— |
| Jogador 3 | 1-3 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Murkwolf18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35076743364334106 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 23 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_Murkwolf18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010184191167354584 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 24 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_Murkwolf18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28403541445732117 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Murkwolf18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35065075755119324 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 26 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_Murkwolf18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007723457645624876 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3143654465675354 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 34 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33563852310180664 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 3 | 2-1 | 42 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013125529512763023 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 43 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15800000727176666 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 44 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_Murkwolf18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.515301525592804 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 45 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_Murkwolf18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10814932733774185 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 46 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_Murkwolf18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 51 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 12.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9661731719970703 | 0.0 | 0.0 | +1c3f698b-ddeb-4552-af2c-2d8260874474 / -— |
| Jogador 3 | 2-2 | 52 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014501291327178478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 53 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04450000077486038 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 54 | PASS | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4164091944694519 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 61 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 8 | 0 | 16.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34620165824890137 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 62 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 8 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3470473885536194 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 63 | PASS | STABILIZE | 100.0 | 5 | 8 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 71 | BUY | STABILIZE | 100.0 | 5 | 15 | 1 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2750076353549957 | 0.0 | 0.0 | +4b3d3abb-8023-422a-b699-88050ea034e5 / -— |
| Jogador 3 | 2-4 | 72 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 12 | 1 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12336276471614838 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 73 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 12 | 1 | 18.0 | —/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6267129778862 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 74 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 12 | 1 | 16.0 | —/DA_18_Rengar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32958918809890747 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 75 | PASS | STABILIZE | 100.0 | 5 | 12 | 1 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 81 | BUY | STABILIZE | 100.0 | 5 | 19 | 1 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.115070104598999 | 0.0 | 0.0 | +752d9bcf-a330-4d9c-aedb-d009c9820888 / -0e9aa759-0538-4168-a523-02a5f8e09e0a,1c3f698b-ddeb-4552-af2c-2d8260874474 |
| Jogador 3 | 2-5 | 82 | BUY | STABILIZE | 100.0 | 5 | 17 | 1 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28467288613319397 | 0.0 | 0.0 | +032b5960-ec2a-4a26-ad67-862a20f30523 / -— |
| Jogador 3 | 2-5 | 83 | BUY | STABILIZE | 100.0 | 5 | 14 | 1 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9630900025367737 | 0.0 | 0.0 | +97fc5647-5995-4f21-aa03-13454546919a / -— |
| Jogador 3 | 2-5 | 84 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 13 | 1 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39617282152175903 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 85 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 13 | 1 | 16.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3069627285003662 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 86 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 13 | 1 | 16.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04654049873352051 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 87 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 13 | 1 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2655145227909088 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 88 | BUY_XP | STABILIZE | 100.0 | 5 | 13 | 1 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 89 | BUY_XP | STABILIZE | 100.0 | 5 | 9 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 91 | BUY | STABILIZE | 100.0 | 5 | 12 | 1 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48385393619537354 | 0.0 | 0.0 | +584991bb-37b3-4ac1-8e29-14e0d74c5e78 / -— |
| Jogador 3 | 2-6 | 92 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 10 | 1 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1883985698223114 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 93 | BUY_XP | STABILIZE | 100.0 | 5 | 10 | 1 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0729999989271164 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 94 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 6 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5043677687644958 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 95 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 6 | 0 | 16.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17261773347854614 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 96 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 6 | 0 | 20.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9171625971794128 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 97 | PASS | STABILIZE | 100.0 | 6 | 6 | 0 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 101 | BUY | STABILIZE | 95.0 | 6 | 11 | 1 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.888573944568634 | 0.0 | 0.0 | +f0f7bd0a-19e6-44d8-a0e2-e4e4dc2b9e68 / -— |
| Jogador 3 | 2-7 | 102 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 9 | 0 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09396984428167343 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 103 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 9 | 0 | 16.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20120464265346527 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 104 | PASS | STABILIZE | 95.0 | 6 | 9 | 0 | 20.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 111 | BUY | STABILIZE | 95.0 | 6 | 14 | 1 | 20.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21476998925209045 | 0.0 | 0.0 | +ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b / -— |
| Jogador 3 | 3-1 | 112 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 11 | 1 | 20.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9332675337791443 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 113 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 11 | 1 | 18.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2535335123538971 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 114 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 11 | 1 | 16.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 115 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 11 | 1 | 16.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10484588146209717 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 116 | BUY_XP | STABILIZE | 95.0 | 6 | 11 | 1 | 16.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 117 | BUY_XP | STABILIZE | 95.0 | 6 | 7 | 0 | 16.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 118 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 3 | 0 | 16.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 119 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 3 | 0 | 16.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 121 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 9 | 0 | 16.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8757058382034302 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 122 | BUY | STABILIZE | 95.0 | 6 | 9 | 0 | 18.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6947272419929504 | 0.0 | 0.0 | +805375b9-df52-4342-b581-4b92fcd12033 / -— |
| Jogador 3 | 3-2 | 123 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 18.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6539099812507629 | 0.0 | 0.0 | +fe6546c3-86ef-40e1-aa7e-ff7e400fe628 / -2cf5ccdc-76f4-4fc8-b12c-7b3b68b1b2c8,bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 3-2 | 124 | BUY | STABILIZE | 95.0 | 6 | 5 | 0 | 14.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11762641370296478 | 0.0 | 0.0 | +661b176a-5963-4715-b9dd-aca29f552fa9 / -— |
| Jogador 3 | 3-2 | 125 | BUY | STABILIZE | 95.0 | 6 | 3 | 0 | 14.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.289679616689682 | 0.0 | 0.0 | +40f2a32f-1ace-4700-8a79-e6b5d3212036 / -— |
| Jogador 3 | 3-2 | 126 | PASS | STABILIZE | 95.0 | 6 | 1 | 0 | 14.0 | Colosso/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 129 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 1 | 0 | 14.0 | Colosso/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38464927673339844 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 131 | BUY | STABILIZE | 85.0 | 6 | 6 | 0 | 20.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.74312424659729 | 0.0 | 0.0 | +23366968-ed3f-43d0-9f24-bb7691bf5d45 / -— |
| Jogador 3 | 3-3 | 132 | PASS | STABILIZE | 85.0 | 6 | 3 | 0 | 20.0 | Colosso/DA_Scuttlecrab18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 139 | MOVE_BENCH | STABILIZE | 85.0 | 6 | 3 | 0 | 20.0 | Colosso/DA_Scuttlecrab18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6132277846336365 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 141 | REROLL | STABILIZE | 85.0 | 6 | 9 | 0 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 142 | REROLL | STABILIZE | 85.0 | 6 | 7 | 0 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06704311072826385 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 143 | PASS | STABILIZE | 85.0 | 6 | 5 | 0 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 151 | REROLL | STABILIZE | 85.0 | 6 | 10 | 1 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 152 | REROLL | STABILIZE | 85.0 | 6 | 8 | 0 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06707116216421127 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 153 | REROLL | STABILIZE | 85.0 | 6 | 6 | 0 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08099989593029022 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 154 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 4 | 0 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24865101277828217 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 155 | PASS | STABILIZE | 85.0 | 6 | 4 | 0 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 161 | MOVE_BOARD | STABILIZE | 75.0 | 6 | 9 | 0 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21385490894317627 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 162 | MOVE_BOARD | STABILIZE | 75.0 | 6 | 9 | 0 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12835003435611725 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 163 | PASS | STABILIZE | 75.0 | 6 | 9 | 0 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 171 | PASS | STABILIZE | 75.0 | 6 | 16 | 1 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 181 | BUY | STABILIZE | 75.0 | 6 | 22 | 2 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8659475445747375 | 0.0 | 0.0 | +61362365-2cf7-40e4-95f9-98e28728fd39 / -584991bb-37b3-4ac1-8e29-14e0d74c5e78,f0f7bd0a-19e6-44d8-a0e2-e4e4dc2b9e68 |
| Jogador 3 | 4-1 | 182 | PASS | STABILIZE | 75.0 | 6 | 20 | 2 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 191 | BUY | STABILIZE | 65.0 | 6 | 27 | 2 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.863907516002655 | 0.0 | 0.0 | +023f01af-91d0-4e07-8229-2b7cded83151 / -032b5960-ec2a-4a26-ad67-862a20f30523,23366968-ed3f-43d0-9f24-bb7691bf5d45 |
| Jogador 3 | 4-2 | 192 | PASS | STABILIZE | 65.0 | 6 | 24 | 2 | 14.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 199 | PASS | SLOWROLL | 54.0 | 6 | 32 | 3 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05999999865889549 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 205 | MOVE_BENCH | SLOWROLL | 54.0 | 6 | 32 | 3 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5529212951660156 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 207 | BUY | SLOWROLL | 41.0 | 6 | 41 | 4 | 34.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.238590270280838 | 0.0 | 0.0 | +2949d735-3c16-4a45-835b-e11a9c12b16a / -— |
| Jogador 3 | 4-4 | 208 | PASS | SLOWROLL | 41.0 | 6 | 39 | 3 | 34.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05999999865889549 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 214 | PASS | SLOWROLL | 41.0 | 6 | 48 | 4 | 34.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 223 | BUY | STABILIZE | 28.0 | 7 | 58 | 5 | 34.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8699886798858643 | 0.0 | 0.0 | +0c96798c-ee23-488b-974f-74e8e3da6aa6 / -— |
| Jogador 3 | 4-6 | 224 | PASS | STABILIZE | 28.0 | 7 | 56 | 5 | 34.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11999999731779099 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 232 | PASS | STABILIZE | 16.0 | 7 | 68 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 242 | EQUIP_FROM_INVENTORY | STABILIZE | 16.0 | 7 | 80 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 243 | PASS | STABILIZE | 16.0 | 7 | 80 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.18000000715255737 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 252 | PASS | STABILIZE | 16.0 | 7 | 92 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.18000000715255737 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 262 | BUY | ALL_IN | 1.0 | 7 | 105 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.39848437905311584 | 0.0 | 0.0 | +9af00d66-f862-45b7-98d4-93fbd69fedba / -— |
| Jogador 3 | 5-3 | 263 | PASS | ALL_IN | 1.0 | 7 | 102 | 5 | 38.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.28519999980926514 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 272 | PASS | ALL_IN | 0.0 | 7 | 102 | 5 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 282 | PASS | ALL_IN | 0.0 | 7 | 102 | 5 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 292 | PASS | ALL_IN | 0.0 | 7 | 102 | 5 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 302 | PASS | ALL_IN | 0.0 | 7 | 102 | 5 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 312 | PASS | ALL_IN | 0.0 | 7 | 102 | 5 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-2 | 322 | PASS | ALL_IN | 0.0 | 7 | 102 | 5 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-3 | 332 | PASS | ALL_IN | 0.0 | 7 | 102 | 5 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-4 | 342 | PASS | ALL_IN | 0.0 | 7 | 102 | 5 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-5 | 352 | PASS | ALL_IN | 0.0 | 7 | 102 | 5 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-6 | 362 | PASS | ALL_IN | 0.0 | 7 | 102 | 5 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.019615383818745613 | 0.0 | 0.0 | +— / -9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +1903eae4-bd37-4ed8-bbae-28177e859592 / -— |
| Jogador 4 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.6058921217918396 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.25464189052581787 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00228595407679677 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 13 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1385176032781601 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30440935492515564 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 15 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.816641628742218 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 16 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.58186274766922 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3129260838031769 | 0.0 | 0.0 | +a19fc47b-fc81-49b2-bc25-d25d58b8deef / -— |
| Jogador 4 | 1-3 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7935476303100586 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 23 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08568045496940613 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 24 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.036051902920007706 | 0.0 | 0.0 | +— / -95829f2e-ad17-448d-a385-fdcf81872dc8 |
| Jogador 4 | 1-3 | 25 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, MOVE_BOARD, PASS | True | True | 0.044155314564704895 | 0.0 | 0.0 | +57f213f7-34b1-4a4a-8047-afa5e404e5c4 / -— |
| Jogador 4 | 1-3 | 26 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1983846127986908 | 0.0 | 0.0 | +— / -57f213f7-34b1-4a4a-8047-afa5e404e5c4 |
| Jogador 4 | 1-3 | 27 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9863340854644775 | 0.0 | 0.0 | +eddd35aa-7d38-4d71-8984-e4768f06379e / -— |
| Jogador 4 | 1-4 | 32 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179746389389038 | 0.0 | 0.0 | +cd27dcd8-0a45-4196-be66-fbe6eb4a0793 / -1903eae4-bd37-4ed8-bbae-28177e859592,eddd35aa-7d38-4d71-8984-e4768f06379e |
| Jogador 4 | 1-4 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9684662818908691 | 0.0 | 0.0 | +b29f76e2-456d-4abf-b9a2-a4a80b577187 / -— |
| Jogador 4 | 1-4 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7390545606613159 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 36 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17854541540145874 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 37 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3938461244106293 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 38 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.11736261844635 | 0.0 | 0.0 | +4a8986e4-45cf-42bc-866d-01c476dcb55b / -9e7d1da0-5190-4348-81b4-3a3f2129a8e5,b29f76e2-456d-4abf-b9a2-a4a80b577187 |
| Jogador 4 | 2-1 | 42 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9601584076881409 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 4 | 2-1 | 43 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1134697198867798 | 0.0 | 0.0 | +a5c3f6df-50ac-4f3b-aa9c-6476a055aa53 / -a19fc47b-fc81-49b2-bc25-d25d58b8deef,df330dae-9fc1-440f-896d-a733d052e5ba |
| Jogador 4 | 2-1 | 44 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 4.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7489213347434998 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 45 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 4.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3340178430080414 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 46 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.05112886428833 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 47 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4272199273109436 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 48 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 16.0 | —/DA_Gromp18_AP | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 51 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 16.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00941474735736847 | 0.0 | 0.0 | +341df1a1-a619-420a-926a-0fe048aa1456 / -— |
| Jogador 4 | 2-2 | 52 | BUY | STABILIZE | 95.0 | 4 | 2 | 0 | 16.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06592898815870285 | 0.0 | 0.0 | +0debca82-3a2a-44ba-af48-83211d5e5243 / -— |
| Jogador 4 | 2-2 | 53 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 0 | 0 | 16.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44724181294441223 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 54 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 0 | 0 | 16.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012586790136992931 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 55 | PASS | STABILIZE | 95.0 | 4 | 0 | 0 | 12.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 59 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 0 | 0 | 12.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36626553535461426 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 61 | BUY | STABILIZE | 90.0 | 4 | 6 | 0 | 18.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5445384979248047 | 0.0 | 0.0 | +0da2c93c-0c62-4fe0-94ff-688f086141e3 / -— |
| Jogador 4 | 2-3 | 62 | BUY_XP | STABILIZE | 90.0 | 4 | 5 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 63 | SELL | STABILIZE | 90.0 | 4 | 1 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6346586346626282 | 0.0 | 0.0 | +— / -0da2c93c-0c62-4fe0-94ff-688f086141e3 |
| Jogador 4 | 2-3 | 64 | MOVE_BOARD | STABILIZE | 90.0 | 4 | 2 | 0 | 18.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027898332104086876 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 65 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 2 | 0 | 18.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018744606524705887 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 66 | MOVE_BOARD | STABILIZE | 90.0 | 4 | 2 | 0 | 22.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3197319805622101 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 67 | PASS | STABILIZE | 90.0 | 4 | 2 | 0 | 22.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 71 | BUY | STABILIZE | 85.0 | 5 | 8 | 0 | 22.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5224719643592834 | 0.0 | 0.0 | +77d51a33-bfc7-4b8b-b460-8a4a45391474 / -— |
| Jogador 4 | 2-4 | 72 | BUY | STABILIZE | 85.0 | 5 | 6 | 0 | 22.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02428850345313549 | 0.0 | 0.0 | +53a17678-f853-4814-97c7-524b66ec199d / -— |
| Jogador 4 | 2-4 | 73 | BUY | STABILIZE | 85.0 | 5 | 2 | 0 | 22.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33315080404281616 | 0.0 | 0.0 | +18934be2-4988-4f62-9f62-07ba151231f2 / -— |
| Jogador 4 | 2-4 | 74 | MOVE_BOARD | STABILIZE | 85.0 | 5 | 1 | 0 | 22.0 | —/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01868247613310814 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 75 | BUY | STABILIZE | 85.0 | 5 | 1 | 0 | 22.0 | —/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015447127632796764 | 0.0 | 0.0 | +2c497125-ca06-46b1-a3b3-9a59d904705b / -— |
| Jogador 4 | 2-4 | 76 | PASS | STABILIZE | 85.0 | 5 | 0 | 0 | 22.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 79 | MOVE_BENCH | STABILIZE | 85.0 | 5 | 0 | 0 | 22.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5261403322219849 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 81 | BUY | STABILIZE | 85.0 | 5 | 6 | 0 | 26.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8134433627128601 | 0.0 | 0.0 | +0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb / -— |
| Jogador 4 | 2-5 | 82 | MOVE_BOARD | STABILIZE | 85.0 | 5 | 3 | 0 | 26.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 83 | MOVE_BOARD | STABILIZE | 85.0 | 5 | 3 | 0 | 26.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11629858613014221 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 84 | PASS | STABILIZE | 85.0 | 5 | 3 | 0 | 26.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 91 | REROLL | STABILIZE | 78.0 | 5 | 9 | 0 | 26.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06946005672216415 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 92 | BUY | STABILIZE | 78.0 | 5 | 7 | 0 | 26.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48010095953941345 | 0.0 | 0.0 | +a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 / -— |
| Jogador 4 | 2-6 | 93 | PASS | STABILIZE | 78.0 | 5 | 6 | 0 | 26.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 101 | BUY | STABILIZE | 71.0 | 5 | 13 | 1 | 26.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8360945582389832 | 0.0 | 0.0 | +2d1296a3-9aa4-42ab-8b86-34661e32a63d / -— |
| Jogador 4 | 2-7 | 102 | PASS | STABILIZE | 71.0 | 5 | 11 | 1 | 26.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 111 | BUY | STABILIZE | 71.0 | 5 | 19 | 1 | 26.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28675827383995056 | 0.0 | 0.0 | +2399a42a-332c-42ee-9bd8-5f52bb921ffa / -— |
| Jogador 4 | 3-1 | 112 | PASS | STABILIZE | 71.0 | 5 | 18 | 1 | 26.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 121 | PASS | STABILIZE | 61.0 | 5 | 27 | 2 | 26.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 131 | REROLL | SLOWROLL | 52.0 | 5 | 37 | 3 | 26.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 132 | PASS | SLOWROLL | 52.0 | 5 | 35 | 3 | 26.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 141 | PASS | SLOWROLL | 40.0 | 5 | 46 | 4 | 26.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04500000178813934 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 151 | PASS | SLOWROLL | 40.0 | 5 | 58 | 5 | 26.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 161 | PASS | STABILIZE | 29.0 | 5 | 71 | 5 | 26.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10080000013113022 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 171 | PASS | STABILIZE | 20.0 | 6 | 84 | 5 | 26.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14399999380111694 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 179 | MOVE_BENCH | STABILIZE | 20.0 | 6 | 84 | 5 | 26.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4393085539340973 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 181 | BUY | STABILIZE | 20.0 | 6 | 97 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.21150042116641998 | 0.0 | 0.0 | +31ea6d79-501d-4f2a-821d-7058334be82f / -— |
| Jogador 4 | 4-1 | 182 | PASS | STABILIZE | 20.0 | 6 | 94 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 191 | BUY | ALL_IN | 8.0 | 6 | 107 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.32836127281188965 | 0.0 | 0.0 | +673bda2e-1343-4894-8005-c3ee2c90f1b7 / -— |
| Jogador 4 | 4-2 | 192 | PASS | ALL_IN | 8.0 | 6 | 105 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 199 | PASS | ALL_IN | 8.0 | 6 | 116 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 207 | PASS | ALL_IN | 0.0 | 6 | 116 | 5 | 0.0 | Adaptador/DA_Gromp18_AP | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 214 | PASS | ALL_IN | 0.0 | 6 | 116 | 5 | 0.0 | Adaptador/DA_Gromp18_AP | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 223 | PASS | ALL_IN | 0.0 | 6 | 116 | 5 | 0.0 | Adaptador/DA_Gromp18_AP | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 232 | PASS | ALL_IN | 0.0 | 6 | 116 | 5 | 0.0 | Adaptador/DA_Gromp18_AP | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 242 | PASS | ALL_IN | 0.0 | 6 | 116 | 5 | 0.0 | Adaptador/DA_Gromp18_AP | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 252 | PASS | ALL_IN | 0.0 | 6 | 116 | 5 | 0.0 | Adaptador/DA_Gromp18_AP | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 262 | PASS | ALL_IN | 0.0 | 6 | 116 | 5 | 0.0 | Adaptador/DA_Gromp18_AP | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 272 | PASS | ALL_IN | 0.0 | 6 | 116 | 5 | 0.0 | Adaptador/DA_Gromp18_AP | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 282 | PASS | ALL_IN | 0.0 | 6 | 116 | 5 | 0.0 | Adaptador/DA_Gromp18_AP | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 292 | PASS | ALL_IN | 0.0 | 6 | 116 | 5 | 0.0 | Adaptador/DA_Gromp18_AP | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 302 | PASS | ALL_IN | 0.0 | 6 | 116 | 5 | 0.0 | Adaptador/DA_Gromp18_AP | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 312 | PASS | ALL_IN | 0.0 | 6 | 116 | 5 | 0.0 | Adaptador/DA_Gromp18_AP | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-2 | 322 | PASS | ALL_IN | 0.0 | 6 | 116 | 5 | 0.0 | Adaptador/DA_Gromp18_AP | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-3 | 332 | PASS | ALL_IN | 0.0 | 6 | 116 | 5 | 0.0 | Adaptador/DA_Gromp18_AP | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-4 | 342 | PASS | ALL_IN | 0.0 | 6 | 116 | 5 | 0.0 | Adaptador/DA_Gromp18_AP | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-5 | 352 | PASS | ALL_IN | 0.0 | 6 | 116 | 5 | 0.0 | Adaptador/DA_Gromp18_AP | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-6 | 362 | PASS | ALL_IN | 0.0 | 6 | 116 | 5 | 0.0 | Adaptador/DA_Gromp18_AP | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.010384615510702133 | 0.0 | 0.0 | +— / -f9c418e0-f8aa-4492-8b97-8855ce3af370 |
| Jogador 5 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +a05f4164-724c-4182-bafc-82ef354cea0b / -— |
| Jogador 5 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.6080599427223206 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.04858612269163132 | 0.0 | 0.0 | +df7d3860-9b2e-45ed-b564-281d95e64e82 / -— |
| Jogador 5 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3013538420200348 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 13 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.31294018030166626 | 0.0 | 0.0 | +4a7ac9c5-c110-4566-80e5-25d9e6033799 / -— |
| Jogador 5 | 1-3 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8164486885070801 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 23 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7033815979957581 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 24 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.018952207639813423 | 0.0 | 0.0 | +4c71fb0c-00db-4e1e-8563-2ca901248b7f / -— |
| Jogador 5 | 1-4 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Elise | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8110079169273376 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 33 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Kayle | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3345959186553955 | 0.0 | 0.0 | +9f7fed06-4220-46d5-a6c9-a7cda1f846d6 / -— |
| Jogador 5 | 1-4 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Kayle | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5062628388404846 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Kayle | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2510511577129364 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 36 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Kayle | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Kayle | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3543156683444977 | 0.0 | 0.0 | +646fc826-453b-479f-97d1-8aa2a9d86dc3 / -— |
| Jogador 5 | 2-1 | 42 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36308586597442627 | 0.0 | 0.0 | +c8b72b14-11a4-48e6-8135-41efdbc347cb / -— |
| Jogador 5 | 2-1 | 43 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12029819190502167 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 44 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41308584809303284 | 0.0 | 0.0 | +— / -c8b72b14-11a4-48e6-8135-41efdbc347cb |
| Jogador 5 | 2-1 | 45 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10305044800043106 | 0.0 | 0.0 | +185ee377-0917-4209-905b-9486d5be0193 / -— |
| Jogador 5 | 2-1 | 46 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20084615051746368 | 0.0 | 0.0 | +— / -185ee377-0917-4209-905b-9486d5be0193 |
| Jogador 5 | 2-1 | 47 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14676454663276672 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 48 | SELL | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0017692308174446225 | 0.0 | 0.0 | +— / -4c71fb0c-00db-4e1e-8563-2ca901248b7f |
| Jogador 5 | 2-1 | 49 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4919576048851013 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 51 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05983696132898331 | 0.0 | 0.0 | +f82eae62-dfe9-41bc-b346-71bf2c7cca02 / -— |
| Jogador 5 | 2-2 | 52 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27237752079963684 | 0.0 | 0.0 | +048e9074-b134-49ed-a105-88dca63d1aa3 / -— |
| Jogador 5 | 2-2 | 53 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0598648376762867 | 0.0 | 0.0 | +555d7565-0e53-4030-ac06-b8d749e88568 / -— |
| Jogador 5 | 2-2 | 54 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 16.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1111365407705307 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 55 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 16.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 61 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 5 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6172378659248352 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 62 | BUY | STABILIZE | 94.0 | 4 | 5 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9056427478790283 | 0.0 | 0.0 | +2ef60eed-d073-41a6-adec-4466c673b313 / -— |
| Jogador 5 | 2-3 | 63 | PASS | STABILIZE | 94.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 71 | PASS | STABILIZE | 87.0 | 4 | 10 | 1 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 81 | PASS | STABILIZE | 87.0 | 4 | 17 | 1 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 91 | BUY | LOSS_STREAK | 80.0 | 5 | 24 | 2 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8304895162582397 | 0.0 | 0.0 | +8980fd33-79c8-4825-95e9-9298680cbc6d / -— |
| Jogador 5 | 2-6 | 92 | BUY | LOSS_STREAK | 80.0 | 5 | 22 | 2 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8755929470062256 | 0.0 | 0.0 | +7c218f01-e884-46da-8a1a-2d2db27a5ff1 / -2ef60eed-d073-41a6-adec-4466c673b313,9f7fed06-4220-46d5-a6c9-a7cda1f846d6 |
| Jogador 5 | 2-6 | 93 | BUY | LOSS_STREAK | 80.0 | 5 | 21 | 2 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28253990411758423 | 0.0 | 0.0 | +d7649b2a-9868-4fa7-975d-3e4727c8554d / -— |
| Jogador 5 | 2-6 | 94 | BUY | STABILIZE | 80.0 | 5 | 20 | 2 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7471161484718323 | 0.0 | 0.0 | +dca8bf82-80ac-4054-9a77-3891a7de23e2 / -— |
| Jogador 5 | 2-6 | 95 | PASS | STABILIZE | 80.0 | 5 | 19 | 1 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 99 | MOVE_BENCH | STABILIZE | 80.0 | 5 | 19 | 1 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13374094665050507 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 101 | PASS | STABILIZE | 73.0 | 5 | 26 | 2 | 20.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 109 | MOVE_BENCH | STABILIZE | 73.0 | 5 | 26 | 2 | 20.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5223075151443481 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 111 | PASS | SLOWROLL | 73.0 | 5 | 34 | 3 | 26.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 121 | PASS | SLOWROLL | 73.0 | 5 | 43 | 4 | 26.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04500000178813934 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 131 | PASS | SLOWROLL | 73.0 | 5 | 54 | 5 | 26.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 141 | PASS | SLOWROLL | 62.0 | 5 | 64 | 5 | 26.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 151 | PASS | SLOWROLL | 62.0 | 5 | 74 | 5 | 26.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 161 | PASS | SLOWROLL | 53.0 | 5 | 85 | 5 | 26.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 171 | PASS | SLOWROLL | 41.0 | 5 | 96 | 5 | 26.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 181 | BUY | SLOWROLL | 41.0 | 5 | 107 | 5 | 26.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2989974021911621 | 0.0 | 0.0 | +ac547bcb-d285-480d-b50e-3cfba572db5a / -— |
| Jogador 5 | 4-1 | 182 | BUY | SLOWROLL | 41.0 | 5 | 104 | 5 | 26.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3399956226348877 | 0.0 | 0.0 | +715d5bfc-c8c3-4dec-a247-9e07ee2755e8 / -— |
| Jogador 5 | 4-1 | 183 | PASS | SLOWROLL | 41.0 | 5 | 103 | 5 | 26.0 | Congregação das Bruxas/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11999999731779099 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 191 | PASS | STABILIZE | 30.0 | 6 | 114 | 5 | 26.0 | Congregação das Bruxas/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 199 | PASS | STABILIZE | 20.0 | 6 | 126 | 5 | 32.0 | Congregação das Bruxas/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 207 | PASS | STABILIZE | 20.0 | 6 | 137 | 5 | 32.0 | Congregação das Bruxas/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 214 | PASS | STABILIZE | 20.0 | 6 | 147 | 5 | 32.0 | Congregação das Bruxas/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14399999380111694 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 223 | PASS | STABILIZE | 20.0 | 6 | 159 | 5 | 32.0 | Congregação das Bruxas/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14399999380111694 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 232 | BUY | ALL_IN | 7.0 | 6 | 169 | 5 | 32.0 | Congregação das Bruxas/DA_18_Camille | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.039381980895996 | 0.0 | 0.0 | +7de5aac5-85d7-4add-b5a7-1c89be9d7e40 / -8980fd33-79c8-4825-95e9-9298680cbc6d,df7d3860-9b2e-45ed-b564-281d95e64e82 |
| Jogador 5 | 4-7 | 233 | PASS | ALL_IN | 7.0 | 6 | 167 | 5 | 28.0 | Congregação das Bruxas/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2563999891281128 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 240 | MOVE_BENCH | ALL_IN | 7.0 | 6 | 167 | 5 | 28.0 | Congregação das Bruxas/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7137320637702942 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 242 | EQUIP_FROM_INVENTORY | ALL_IN | 7.0 | 6 | 177 | 5 | 36.0 | Congregação das Bruxas/DA_18_Elise | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 243 | PASS | ALL_IN | 7.0 | 6 | 177 | 5 | 36.0 | Congregação das Bruxas/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2563999891281128 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 252 | PASS | ALL_IN | 0.0 | 6 | 177 | 5 | 0.0 | Congregação das Bruxas/DA_18_Elise | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 262 | PASS | ALL_IN | 0.0 | 6 | 177 | 5 | 0.0 | Congregação das Bruxas/DA_18_Elise | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 272 | PASS | ALL_IN | 0.0 | 6 | 177 | 5 | 0.0 | Congregação das Bruxas/DA_18_Elise | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 282 | PASS | ALL_IN | 0.0 | 6 | 177 | 5 | 0.0 | Congregação das Bruxas/DA_18_Elise | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 292 | PASS | ALL_IN | 0.0 | 6 | 177 | 5 | 0.0 | Congregação das Bruxas/DA_18_Elise | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 302 | PASS | ALL_IN | 0.0 | 6 | 177 | 5 | 0.0 | Congregação das Bruxas/DA_18_Elise | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 312 | PASS | ALL_IN | 0.0 | 6 | 177 | 5 | 0.0 | Congregação das Bruxas/DA_18_Elise | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 322 | PASS | ALL_IN | 0.0 | 6 | 177 | 5 | 0.0 | Congregação das Bruxas/DA_18_Elise | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 332 | PASS | ALL_IN | 0.0 | 6 | 177 | 5 | 0.0 | Congregação das Bruxas/DA_18_Elise | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 342 | PASS | ALL_IN | 0.0 | 6 | 177 | 5 | 0.0 | Congregação das Bruxas/DA_18_Elise | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 352 | PASS | ALL_IN | 0.0 | 6 | 177 | 5 | 0.0 | Congregação das Bruxas/DA_18_Elise | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-6 | 362 | PASS | ALL_IN | 0.0 | 6 | 177 | 5 | 0.0 | Congregação das Bruxas/DA_18_Elise | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0013076922623440623 | 0.0 | 0.0 | +— / -698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +9002992e-4dcd-4fec-939c-87393464a41d / -— |
| Jogador 6 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.612060546875 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.04858612269163132 | 0.0 | 0.0 | +4d0bf502-ac30-4cdb-9da7-4f9a7ab054b1 / -— |
| Jogador 6 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0726608037948608 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 13 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5477675199508667 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 14 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.00015411031199619174 | 0.0 | 0.0 | +c3c53e80-c8e2-4774-afa2-9b0f4ab3b326 / -— |
| Jogador 6 | 1-3 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5723348259925842 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 23 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Teemo | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9878398180007935 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 24 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Teemo | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Teemo | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7275763750076294 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.019240504130721092 | 0.0 | 0.0 | +c19cf6a8-c66e-4670-b0fc-fb83453f22e7 / -— |
| Jogador 6 | 1-4 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Teemo | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6952731013298035 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 33 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Teemo | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34308648109436035 | 0.0 | 0.0 | +3ad41699-a484-4178-be10-d8f72dfd1f35 / -— |
| Jogador 6 | 1-4 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Teemo | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6236881017684937 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Teemo | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12006966024637222 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 36 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_Murkwolf18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9692961573600769 | 0.0 | 0.0 | +242805ca-f275-4e04-a2f5-81e0b6680dd1 / -— |
| Jogador 6 | 2-1 | 42 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002081192098557949 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 6 | 2-1 | 43 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0192961692810059 | 0.0 | 0.0 | +— / -242805ca-f275-4e04-a2f5-81e0b6680dd1 |
| Jogador 6 | 2-1 | 44 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04080982878804207 | 0.0 | 0.0 | +42f4384d-5499-4441-aa3b-d37e50926071 / -— |
| Jogador 6 | 2-1 | 45 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19295300543308258 | 0.0 | 0.0 | +— / -42f4384d-5499-4441-aa3b-d37e50926071 |
| Jogador 6 | 2-1 | 46 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36334386467933655 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 47 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31022030115127563 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 48 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 49 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 10.0 | —/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40069687366485596 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 51 | BUY | STABILIZE | 96.0 | 4 | 6 | 0 | 14.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44650381803512573 | 0.0 | 0.0 | +0d8b39fc-eb5c-4679-b615-50cdfdcf3eee / -— |
| Jogador 6 | 2-2 | 52 | BUY | STABILIZE | 96.0 | 4 | 3 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1207858994603157 | 0.0 | 0.0 | +98558a52-389f-46fc-b370-6345603f4103 / -— |
| Jogador 6 | 2-2 | 53 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 1 | 0 | 14.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7701587677001953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 54 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16973242163658142 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 55 | PASS | STABILIZE | 96.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 61 | BUY | STABILIZE | 96.0 | 4 | 7 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8597260117530823 | 0.0 | 0.0 | +3ffefe44-52ff-4118-83fb-ae8237b6caa0 / -— |
| Jogador 6 | 2-3 | 62 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40809503197669983 | 0.0 | 0.0 | +0547b747-1e37-49ba-a447-67c526a8cd50 / -— |
| Jogador 6 | 2-3 | 63 | BUY | STABILIZE | 96.0 | 4 | 3 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3066502809524536 | 0.0 | 0.0 | +dd5b4353-d201-4266-9fbe-72df320eb4f5 / -— |
| Jogador 6 | 2-3 | 64 | SELL | STABILIZE | 96.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007461538538336754 | 0.0 | 0.0 | +— / -98558a52-389f-46fc-b370-6345603f4103 |
| Jogador 6 | 2-3 | 65 | REROLL | STABILIZE | 96.0 | 4 | 3 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06954551488161087 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 66 | BUY | STABILIZE | 96.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.835345447063446 | 0.0 | 0.0 | +d44224c1-925d-42f9-ad60-ff4c36c665d6 / -— |
| Jogador 6 | 2-3 | 67 | SELL | STABILIZE | 96.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.885345458984375 | 0.0 | 0.0 | +— / -d44224c1-925d-42f9-ad60-ff4c36c665d6 |
| Jogador 6 | 2-3 | 68 | BUY | STABILIZE | 96.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8353691697120667 | 0.0 | 0.0 | +2ace989d-3e9e-483b-9b14-cd6b8f171f17 / -— |
| Jogador 6 | 2-3 | 69 | SELL | STABILIZE | 96.0 | 4 | 0 | 0 | 12.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8853691816329956 | 0.0 | 0.0 | +— / -2ace989d-3e9e-483b-9b14-cd6b8f171f17 |
| Jogador 6 | 2-4 | 71 | BUY | STABILIZE | 96.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7824690937995911 | 0.0 | 0.0 | +7915a339-3bda-4275-80ae-9941370ea609 / -— |
| Jogador 6 | 2-4 | 72 | REROLL | STABILIZE | 96.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07156690210103989 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 73 | BUY | STABILIZE | 96.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8002063632011414 | 0.0 | 0.0 | +d2a85061-235a-4ce6-816f-6fa27bf02754 / -— |
| Jogador 6 | 2-4 | 74 | SELL | STABILIZE | 96.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05551927536725998 | 0.0 | 0.0 | +— / -0547b747-1e37-49ba-a447-67c526a8cd50 |
| Jogador 6 | 2-4 | 75 | SELL | STABILIZE | 96.0 | 4 | 3 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.83246910572052 | 0.0 | 0.0 | +— / -7915a339-3bda-4275-80ae-9941370ea609 |
| Jogador 6 | 2-4 | 76 | REROLL | STABILIZE | 96.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 77 | REROLL | STABILIZE | 96.0 | 4 | 3 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07204311341047287 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 78 | SELL | STABILIZE | 96.0 | 4 | 1 | 0 | 12.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.033307693898677826 | 0.0 | 0.0 | +— / -dd5b4353-d201-4266-9fbe-72df320eb4f5 |
| Jogador 6 | 2-4 | 79 | BUY | STABILIZE | 96.0 | 4 | 3 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3796359598636627 | 0.0 | 0.0 | +caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e / -— |
| Jogador 6 | 2-5 | 81 | REROLL | STABILIZE | 96.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07479454576969147 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 82 | REROLL | STABILIZE | 96.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0772368386387825 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 83 | PASS | STABILIZE | 96.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 91 | BUY | STABILIZE | 88.0 | 5 | 7 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9285738468170166 | 0.0 | 0.0 | +bbdd0918-bfda-49bc-9ae0-8894eaf11a5c / -3ffefe44-52ff-4118-83fb-ae8237b6caa0,c3c53e80-c8e2-4774-afa2-9b0f4ab3b326 |
| Jogador 6 | 2-6 | 92 | BUY | STABILIZE | 88.0 | 5 | 5 | 0 | 12.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40738004446029663 | 0.0 | 0.0 | +e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 / -— |
| Jogador 6 | 2-6 | 93 | BUY | STABILIZE | 88.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2492649406194687 | 0.0 | 0.0 | +7115c5a0-d443-49d8-b8a4-e51e259572df / -— |
| Jogador 6 | 2-6 | 94 | BUY | STABILIZE | 88.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Teemo | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1213647797703743 | 0.0 | 0.0 | +4312fba1-1471-4fb3-af6f-257248fa1437 / -— |
| Jogador 6 | 2-6 | 95 | PASS | STABILIZE | 88.0 | 5 | 0 | 0 | 12.0 | —/DA_18_Teemo | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 99 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 0 | 0 | 12.0 | —/DA_18_Teemo | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7535244822502136 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 101 | REROLL | STABILIZE | 88.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07171857357025146 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 102 | REROLL | STABILIZE | 88.0 | 5 | 4 | 0 | 18.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07057327032089233 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 103 | REROLL | STABILIZE | 88.0 | 5 | 2 | 0 | 18.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 104 | SELL | STABILIZE | 88.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Teemo | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01838461495935917 | 0.0 | 0.0 | +— / -4312fba1-1471-4fb3-af6f-257248fa1437 |
| Jogador 6 | 2-7 | 105 | PASS | STABILIZE | 88.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Teemo | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 111 | REROLL | STABILIZE | 88.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06787161529064178 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 112 | BUY | STABILIZE | 88.0 | 5 | 4 | 0 | 18.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6843681931495667 | 0.0 | 0.0 | +7fd03119-ac82-49e1-b3bb-3a0caa31011f / -— |
| Jogador 6 | 3-1 | 113 | REROLL | STABILIZE | 88.0 | 5 | 2 | 0 | 18.0 | Vivaz/DA_18_Teemo | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 114 | SELL | STABILIZE | 88.0 | 5 | 0 | 0 | 18.0 | Vivaz/DA_18_Teemo | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0208059661090374 | 0.0 | 0.0 | +— / -7115c5a0-d443-49d8-b8a4-e51e259572df |
| Jogador 6 | 3-1 | 115 | REROLL | STABILIZE | 88.0 | 5 | 2 | 0 | 18.0 | Vivaz/DA_18_Teemo | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 116 | PASS | STABILIZE | 88.0 | 5 | 0 | 0 | 18.0 | Vivaz/DA_18_Teemo | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 121 | BUY | STABILIZE | 77.0 | 5 | 5 | 0 | 18.0 | Vivaz/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8332152366638184 | 0.0 | 0.0 | +f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e / -5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef,d2a85061-235a-4ce6-816f-6fa27bf02754 |
| Jogador 6 | 3-2 | 122 | REROLL | STABILIZE | 77.0 | 5 | 2 | 0 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 123 | SELL | STABILIZE | 77.0 | 5 | 0 | 0 | 18.0 | Vivaz/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03113824687898159 | 0.0 | 0.0 | +— / -e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 |
| Jogador 6 | 3-2 | 124 | REROLL | STABILIZE | 77.0 | 5 | 2 | 0 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 125 | PASS | STABILIZE | 77.0 | 5 | 0 | 0 | 18.0 | Vivaz/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 131 | BUY | STABILIZE | 65.0 | 5 | 6 | 0 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2758193016052246 | 0.0 | 0.0 | +bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed / -— |
| Jogador 6 | 3-3 | 132 | BUY | STABILIZE | 65.0 | 5 | 3 | 0 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21196945011615753 | 0.0 | 0.0 | +2822845b-56e7-4a10-8766-3f7aa579ffcb / -— |
| Jogador 6 | 3-3 | 133 | PASS | STABILIZE | 65.0 | 5 | 0 | 0 | 18.0 | Vivaz/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 141 | PASS | STABILIZE | 53.0 | 5 | 6 | 0 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 151 | PASS | STABILIZE | 53.0 | 5 | 12 | 1 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 161 | BUY | STABILIZE | 53.0 | 5 | 19 | 1 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28598999977111816 | 0.0 | 0.0 | +2357a4df-3c61-4957-83c3-572bbb99ac5a / -— |
| Jogador 6 | 3-6 | 162 | PASS | STABILIZE | 53.0 | 5 | 17 | 1 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 171 | PASS | STABILIZE | 41.0 | 5 | 23 | 2 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 181 | PASS | SLOWROLL | 41.0 | 5 | 30 | 3 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 191 | BUY | STABILIZE | 29.0 | 6 | 39 | 3 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17056560516357422 | 0.0 | 0.0 | +27146a6e-fcf0-46e2-b3fc-5e7b659a5d47 / -— |
| Jogador 6 | 4-2 | 192 | PASS | STABILIZE | 29.0 | 6 | 36 | 3 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 199 | BUY | STABILIZE | 18.0 | 6 | 45 | 4 | 22.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3490310609340668 | 0.0 | 0.0 | +5754c4b4-0a7d-49e5-93e4-b144c3090a41 / -— |
| Jogador 6 | 4-3 | 200 | PASS | STABILIZE | 18.0 | 6 | 42 | 4 | 22.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1151999980211258 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 207 | BUY | ALL_IN | 6.0 | 6 | 52 | 5 | 22.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8457333445549011 | 0.0 | 0.0 | +8d75ef64-e2c3-47b6-a336-c9e5867158e5 / -— |
| Jogador 6 | 4-4 | 208 | PASS | ALL_IN | 6.0 | 6 | 49 | 4 | 22.0 | Vivaz/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 214 | PASS | ALL_IN | 6.0 | 6 | 59 | 5 | 22.0 | Vivaz/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 223 | PASS | ALL_IN | 0.0 | 6 | 59 | 5 | 0.0 | Vivaz/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 232 | PASS | ALL_IN | 0.0 | 6 | 59 | 5 | 0.0 | Vivaz/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 242 | PASS | ALL_IN | 0.0 | 6 | 59 | 5 | 0.0 | Vivaz/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 252 | PASS | ALL_IN | 0.0 | 6 | 59 | 5 | 0.0 | Vivaz/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 262 | PASS | ALL_IN | 0.0 | 6 | 59 | 5 | 0.0 | Vivaz/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 272 | PASS | ALL_IN | 0.0 | 6 | 59 | 5 | 0.0 | Vivaz/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 282 | PASS | ALL_IN | 0.0 | 6 | 59 | 5 | 0.0 | Vivaz/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 292 | PASS | ALL_IN | 0.0 | 6 | 59 | 5 | 0.0 | Vivaz/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 302 | PASS | ALL_IN | 0.0 | 6 | 59 | 5 | 0.0 | Vivaz/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 312 | PASS | ALL_IN | 0.0 | 6 | 59 | 5 | 0.0 | Vivaz/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 322 | PASS | ALL_IN | 0.0 | 6 | 59 | 5 | 0.0 | Vivaz/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-3 | 332 | PASS | ALL_IN | 0.0 | 6 | 59 | 5 | 0.0 | Vivaz/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-4 | 342 | PASS | ALL_IN | 0.0 | 6 | 59 | 5 | 0.0 | Vivaz/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-5 | 352 | PASS | ALL_IN | 0.0 | 6 | 59 | 5 | 0.0 | Vivaz/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-6 | 362 | PASS | ALL_IN | 0.0 | 6 | 59 | 5 | 0.0 | Vivaz/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.019615383818745613 | 0.0 | 0.0 | +— / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987 |
| Jogador 7 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +c2a4318c-af60-41e2-8e14-c3ad967569a0 / -— |
| Jogador 7 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.612060546875 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9794912934303284 | 0.0 | 0.0 | +4e206e09-40e3-4699-81cb-8aaf01109dea / -— |
| Jogador 7 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06249129772186279 | 0.0 | 0.0 | +b21d3fc8-71ce-4669-b0ba-931c6e11cb69 / -— |
| Jogador 7 | 1-2 | 13 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10814932733774185 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3226932883262634 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 15 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5031378269195557 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.25657495856285095 | 0.0 | 0.0 | +734c75dd-d0f3-4b9f-abe8-a228e23557a2 / -— |
| Jogador 7 | 1-3 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3305455148220062 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 23 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3233529329299927 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 24 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02457413636147976 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3171919286251068 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 33 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9602869749069214 | 0.0 | 0.0 | +76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc / -— |
| Jogador 7 | 2-1 | 42 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32265087962150574 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 43 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6251571178436279 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 44 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011393295601010323 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 45 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 46 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 51 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37600183486938477 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 52 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24549610912799835 | 0.0 | 0.0 | +4b4cc4ba-04a0-4e04-88f2-e6913a342285 / -— |
| Jogador 7 | 2-2 | 53 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6048890352249146 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 54 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3115907907485962 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 55 | PASS | STABILIZE | 100.0 | 4 | 4 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 61 | MOVE_BENCH | STABILIZE | 93.0 | 4 | 9 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028618983924388885 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 62 | BUY | STABILIZE | 93.0 | 4 | 9 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0030705248937010765 | 0.0 | 0.0 | +491eb6b6-54f4-4de8-bc63-d96c6c1d9cce / -— |
| Jogador 7 | 2-3 | 63 | MOVE_BENCH | STABILIZE | 93.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04361065849661827 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 64 | MOVE_BENCH | STABILIZE | 93.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.022776471450924873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 65 | BUY_XP | STABILIZE | 93.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0494999997317791 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 66 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 2 | 0 | 12.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34427130222320557 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 67 | BUY | STABILIZE | 93.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2779120206832886 | 0.0 | 0.0 | +5de56114-806a-4f58-8241-b3b8434a2154 / -— |
| Jogador 7 | 2-3 | 68 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 0 | 0 | 10.0 | —/DA_18_Hecarim | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6299780011177063 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 69 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Hecarim | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3518066704273224 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 71 | BUY | STABILIZE | 87.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41630449891090393 | 0.0 | 0.0 | +0c9ac713-08bd-4fa7-a94a-2ab70d7815ff / -— |
| Jogador 7 | 2-4 | 72 | MOVE_BENCH | STABILIZE | 87.0 | 5 | 2 | 0 | 14.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15831147134304047 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 73 | MOVE_BOARD | STABILIZE | 87.0 | 5 | 2 | 0 | 20.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14082112908363342 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 74 | MOVE_BOARD | STABILIZE | 87.0 | 5 | 2 | 0 | 20.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 75 | PASS | STABILIZE | 87.0 | 5 | 2 | 0 | 20.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 81 | MOVE_BENCH | STABILIZE | 87.0 | 5 | 8 | 0 | 20.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030530918389558792 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 82 | MOVE_BENCH | STABILIZE | 87.0 | 5 | 8 | 0 | 18.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006677113473415375 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 83 | MOVE_BENCH | STABILIZE | 87.0 | 5 | 8 | 0 | 20.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04851919785141945 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 84 | BUY_XP | STABILIZE | 87.0 | 5 | 8 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 85 | BUY_XP | STABILIZE | 87.0 | 5 | 4 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 86 | SELL | STABILIZE | 87.0 | 5 | 0 | 0 | 24.0 | —/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028873521834611893 | 0.0 | 0.0 | +— / -b21d3fc8-71ce-4669-b0ba-931c6e11cb69 |
| Jogador 7 | 2-5 | 87 | PASS | STABILIZE | 87.0 | 5 | 1 | 0 | 24.0 | —/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 91 | PASS | STABILIZE | 87.0 | 5 | 7 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 101 | BUY_XP | STABILIZE | 87.0 | 5 | 14 | 1 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029500000178813934 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 102 | BUY | STABILIZE | 87.0 | 6 | 10 | 1 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06990166008472443 | 0.0 | 0.0 | +4278eb73-acda-419d-bf9e-53a29ff6900d / -— |
| Jogador 7 | 2-7 | 103 | MOVE_BENCH | STABILIZE | 87.0 | 6 | 7 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4862188398838043 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 104 | MOVE_BENCH | ECON | 87.0 | 6 | 7 | 0 | 26.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32944798469543457 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 105 | MOVE_BENCH | STABILIZE | 87.0 | 6 | 7 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04047728702425957 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 106 | PASS | ECON | 87.0 | 6 | 7 | 0 | 28.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 111 | BUY | ECON | 87.0 | 6 | 13 | 1 | 28.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15690800547599792 | 0.0 | 0.0 | +c02b6467-3a23-4da6-bca3-06ae415a9998 / -— |
| Jogador 7 | 3-1 | 112 | BUY_XP | ECON | 87.0 | 6 | 10 | 1 | 28.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17800000309944153 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 113 | PASS | ECON | 87.0 | 6 | 6 | 0 | 28.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 121 | BUY | STABILIZE | 87.0 | 6 | 13 | 1 | 28.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08256566524505615 | 0.0 | 0.0 | +fa5dc86b-f736-4083-b9df-5cc174b726f2 / -— |
| Jogador 7 | 3-2 | 122 | PASS | STABILIZE | 87.0 | 6 | 10 | 1 | 28.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 131 | PASS | STABILIZE | 87.0 | 6 | 18 | 1 | 28.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 141 | BUY | STABILIZE | 87.0 | 6 | 27 | 2 | 28.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2934015393257141 | 0.0 | 0.0 | +1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 / -— |
| Jogador 7 | 3-4 | 142 | BUY | STABILIZE | 87.0 | 6 | 24 | 2 | 28.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28540274500846863 | 0.0 | 0.0 | +6b05a3b6-1a7b-4d8a-b9a7-da29ba14c968 / -— |
| Jogador 7 | 3-4 | 143 | BUY | STABILIZE | 87.0 | 6 | 21 | 2 | 28.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7674855589866638 | 0.0 | 0.0 | +60255a84-4f78-49f0-a4f1-d598704c7ee7 / -734c75dd-d0f3-4b9f-abe8-a228e23557a2,76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc |
| Jogador 7 | 3-4 | 144 | BUY | STABILIZE | 87.0 | 6 | 19 | 1 | 20.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8379756212234497 | 0.0 | 0.0 | +0c07379e-5dd1-42e9-aa7a-a764f949deee / -4e206e09-40e3-4699-81cb-8aaf01109dea,c2a4318c-af60-41e2-8e14-c3ad967569a0 |
| Jogador 7 | 3-4 | 145 | PASS | STABILIZE | 87.0 | 6 | 18 | 1 | 18.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 149 | MOVE_BENCH | STABILIZE | 87.0 | 6 | 18 | 1 | 18.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06320744007825851 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 151 | BUY | STABILIZE | 87.0 | 6 | 26 | 2 | 24.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7475388646125793 | 0.0 | 0.0 | +00f38555-1887-4fe2-9930-934055269095 / -— |
| Jogador 7 | 3-5 | 152 | PASS | STABILIZE | 87.0 | 6 | 23 | 2 | 24.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 159 | MOVE_BENCH | STABILIZE | 87.0 | 6 | 23 | 2 | 24.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3448631167411804 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 161 | PASS | SLOWROLL | 87.0 | 6 | 34 | 3 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 169 | MOVE_BENCH | SLOWROLL | 87.0 | 6 | 34 | 3 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5283985733985901 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 171 | PASS | SLOWROLL | 87.0 | 6 | 46 | 4 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04500000178813934 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 181 | PASS | SLOWROLL | 87.0 | 6 | 58 | 5 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11999999731779099 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 191 | SELL | SLOWROLL | 87.0 | 6 | 72 | 5 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45115384459495544 | 0.0 | 0.0 | +— / -0c07379e-5dd1-42e9-aa7a-a764f949deee |
| Jogador 7 | 4-2 | 192 | PASS | SLOWROLL | 87.0 | 6 | 75 | 5 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 199 | PASS | SLOWROLL | 87.0 | 6 | 89 | 5 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11999999731779099 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 207 | BUY | SLOWROLL | 87.0 | 6 | 103 | 5 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.948200523853302 | 0.0 | 0.0 | +da6c9f59-1fc3-467d-8845-bf7b38b4232c / -00f38555-1887-4fe2-9930-934055269095,c02b6467-3a23-4da6-bca3-06ae415a9998 |
| Jogador 7 | 4-4 | 208 | BUY | SLOWROLL | 87.0 | 6 | 100 | 5 | 24.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1967177838087082 | 0.0 | 0.0 | +9414ca8e-930e-4a0e-8cbd-42d8997d8705 / -— |
| Jogador 7 | 4-4 | 209 | BUY | SLOWROLL | 87.0 | 6 | 98 | 5 | 24.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005406987387686968 | 0.0 | 0.0 | +986fbe1e-1826-4be7-a5d6-410a4c0a3f2f / -— |
| Jogador 7 | 4-4 | 210 | PASS | SLOWROLL | 87.0 | 6 | 96 | 5 | 24.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 212 | MOVE_BENCH | SLOWROLL | 87.0 | 6 | 96 | 5 | 24.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4080084562301636 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 214 | BUY | SLOWROLL | 87.0 | 6 | 109 | 5 | 36.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7590140700340271 | 0.0 | 0.0 | +2f2b455f-7035-4948-9429-612018ae7063 / -— |
| Jogador 7 | 4-5 | 215 | PASS | SLOWROLL | 87.0 | 6 | 106 | 5 | 36.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11999999731779099 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 221 | MOVE_BENCH | SLOWROLL | 87.0 | 6 | 106 | 5 | 36.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5213379859924316 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 223 | PASS | SLOWROLL | 87.0 | 6 | 120 | 5 | 42.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11999999731779099 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 232 | BUY | SLOWROLL | 87.0 | 6 | 134 | 5 | 42.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8897652626037598 | 0.0 | 0.0 | +e5f61076-ec13-419b-a4e8-d91b9975cfd6 / -2f2b455f-7035-4948-9429-612018ae7063,4b4cc4ba-04a0-4e04-88f2-e6913a342285 |
| Jogador 7 | 4-7 | 233 | BUY | SLOWROLL | 87.0 | 6 | 131 | 5 | 30.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26542168855667114 | 0.0 | 0.0 | +0c5adb43-b194-486e-b59c-c0f3b5479d40 / -— |
| Jogador 7 | 4-7 | 234 | PASS | SLOWROLL | 87.0 | 6 | 129 | 5 | 30.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 240 | MOVE_BENCH | SLOWROLL | 87.0 | 6 | 129 | 5 | 30.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4272245168685913 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 242 | EQUIP_FROM_INVENTORY | FAST8 | 87.0 | 7 | 142 | 5 | 42.0 | Vanguarda/DA_Fiddlesticks18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 243 | BUY | FAST8 | 87.0 | 7 | 142 | 5 | 42.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.15649700164794922 | 0.0 | 0.0 | +8faad4f9-9f15-49e8-94af-b4d28879cc0d / -— |
| Jogador 7 | 5-1 | 244 | PASS | FAST8 | 87.0 | 7 | 137 | 5 | 42.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 250 | MOVE_BENCH | FAST8 | 87.0 | 7 | 137 | 5 | 42.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.23724336922168732 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 252 | PASS | FAST8 | 87.0 | 7 | 151 | 5 | 52.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 260 | MOVE_BENCH | FAST8 | 87.0 | 7 | 151 | 5 | 52.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09400951117277145 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 262 | PASS | FAST8 | 87.0 | 7 | 165 | 5 | 56.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.18000000715255737 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 272 | BUY | FAST8 | 87.0 | 7 | 179 | 5 | 56.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1896544247865677 | 0.0 | 0.0 | +8025eaf5-b02b-4f94-b381-b94321bca206 / -— |
| Jogador 7 | 5-4 | 273 | BUY | FAST8 | 87.0 | 7 | 175 | 5 | 56.0 | Vanguarda/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7631509900093079 | 0.0 | 0.0 | +663beb45-28d7-42de-b6b8-a81e8676f55f / -— |
| Jogador 7 | 5-4 | 274 | PASS | FAST8 | 87.0 | 7 | 172 | 5 | 56.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 282 | PASS | FAST8 | 87.0 | 7 | 185 | 5 | 56.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 292 | PASS | FAST8 | 87.0 | 7 | 199 | 5 | 56.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 302 | PASS | FAST8 | 87.0 | 7 | 213 | 5 | 56.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 312 | EQUIP_FROM_INVENTORY | FAST8 | 87.0 | 7 | 226 | 5 | 56.0 | Vanguarda/DA_Fiddlesticks18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 313 | EQUIP_FROM_INVENTORY | FAST8 | 87.0 | 7 | 226 | 5 | 56.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY, CRAFT_AND_EQUIP | True | — | -0.028372975066304207 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 314 | PASS | FAST8 | 87.0 | 7 | 226 | 5 | 56.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 322 | PASS | FAST8 | 87.0 | 7 | 239 | 5 | 56.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 332 | PASS | FAST8 | 87.0 | 7 | 253 | 5 | 56.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 342 | PASS | FAST8 | 87.0 | 7 | 267 | 5 | 56.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 352 | PASS | FAST8 | 87.0 | 7 | 280 | 5 | 56.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-6 | 362 | PASS | FAST8 | 87.0 | 7 | 294 | 5 | 56.0 | Vanguarda/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.019615383818745613 | 0.0 | 0.0 | +— / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02 |
| Jogador 8 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +d40a14f6-4b32-4cf9-8eb7-2778414b099a / -— |
| Jogador 8 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.612060546875 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.014635218307375908 | 0.0 | 0.0 | +64afe66e-d5a9-466c-a4ff-9d32c9f153ce / -— |
| Jogador 8 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05395699292421341 | 0.0 | 0.0 | +47feb452-27a0-43f6-983f-ea1674f17ab8 / -— |
| Jogador 8 | 1-2 | 13 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.820525050163269 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2674914002418518 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 15 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33604341745376587 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 16 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.34342142939567566 | 0.0 | 0.0 | +f449cb2d-2ec7-4bf0-8f3a-80f82e1e7d26 / -— |
| Jogador 8 | 1-3 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8265775442123413 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2704628109931946 | 0.0 | 0.0 | +dfc76a7d-9a2b-4b35-b341-60eefe095b71 / -— |
| Jogador 8 | 1-3 | 24 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32046282291412354 | 0.0 | 0.0 | +— / -dfc76a7d-9a2b-4b35-b341-60eefe095b71 |
| Jogador 8 | 1-3 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10329122841358185 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 26 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01838461495935917 | 0.0 | 0.0 | +— / -47feb452-27a0-43f6-983f-ea1674f17ab8 |
| Jogador 8 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.052045270800590515 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 28 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9142209887504578 | 0.0 | 0.0 | +74c2d7f0-8d5d-460e-88fc-5407b717144a / -— |
| Jogador 8 | 1-3 | 29 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8343846201896667 | 0.0 | 0.0 | +— / -a349fd40-8d8c-4de8-9ff0-b3263fd120bc |
| Jogador 8 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32324540615081787 | 0.0 | 0.0 | +65a4f434-f421-47ab-ae23-86ad8971518d / -— |
| Jogador 8 | 1-4 | 32 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3732454180717468 | 0.0 | 0.0 | +— / -65a4f434-f421-47ab-ae23-86ad8971518d |
| Jogador 8 | 1-4 | 33 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2890514135360718 | 0.0 | 0.0 | +230d2dc1-4fa9-45ab-91f3-4db50a151f6e / -— |
| Jogador 8 | 1-4 | 34 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33905142545700073 | 0.0 | 0.0 | +— / -230d2dc1-4fa9-45ab-91f3-4db50a151f6e |
| Jogador 8 | 1-4 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01673945225775242 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 36 | BUY_XP | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04450000077486038 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 37 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04430828243494034 | 0.0 | 0.0 | +— / -f449cb2d-2ec7-4bf0-8f3a-80f82e1e7d26 |
| Jogador 8 | 1-4 | 38 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.04516586288809776 | 0.0 | 0.0 | +64f24363-3325-4538-972e-a6d8260b3787 / -— |
| Jogador 8 | 1-4 | 39 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3711366653442383 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9672965407371521 | 0.0 | 0.0 | +56a8c7e1-c6a6-47e0-9a00-6416cf6f068f / -— |
| Jogador 8 | 2-1 | 42 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 43 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6501463651657104 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 44 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 51 | BUY | STABILIZE | 95.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2500655949115753 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 8 | 2-2 | 52 | BUY_XP | STABILIZE | 95.0 | 4 | 5 | 0 | 8.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029500000178813934 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 53 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 8.0 | —/DA_Krug18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3524497151374817 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 54 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | —/DA_Krug18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.585929274559021 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 55 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_Krug18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22550229728221893 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 56 | BUY | STABILIZE | 95.0 | 5 | 1 | 0 | 10.0 | —/DA_Krug18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9685887098312378 | 0.0 | 0.0 | +6951a681-f5b9-4c22-9182-46b4d2c3cbb3 / -— |
| Jogador 8 | 2-2 | 57 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 0 | 0 | 10.0 | —/DA_Krug18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 58 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 0 | 0 | 10.0 | —/DA_Krug18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2819896638393402 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 59 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 10.0 | —/DA_Krug18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 61 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2677449882030487 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 8 | 2-3 | 62 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 3 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09878452122211456 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 63 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 3 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017940238118171692 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 64 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 3 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1666257083415985 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 65 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 3 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11629858613014221 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 66 | PASS | STABILIZE | 95.0 | 5 | 3 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 71 | BUY | STABILIZE | 95.0 | 5 | 10 | 1 | 10.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2856564223766327 | 0.0 | 0.0 | +eb214f08-2367-4b33-af94-8aa504781450 / -— |
| Jogador 8 | 2-4 | 72 | REROLL | STABILIZE | 95.0 | 5 | 7 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07744427025318146 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 73 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3510587215423584 | 0.0 | 0.0 | +c42b5c69-faa4-4147-bbb7-072c772c0f80 / -— |
| Jogador 8 | 2-4 | 74 | REROLL | STABILIZE | 95.0 | 5 | 2 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 75 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 10.0 | —/DA_Krug18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 81 | REROLL | STABILIZE | 95.0 | 5 | 6 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0785469338297844 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 82 | REROLL | STABILIZE | 95.0 | 5 | 4 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06945306807756424 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 83 | REROLL | STABILIZE | 95.0 | 5 | 2 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 84 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 10.0 | —/DA_Krug18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 91 | REROLL | STABILIZE | 89.0 | 5 | 5 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07365251332521439 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 92 | REROLL | STABILIZE | 89.0 | 5 | 3 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07023509591817856 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 93 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 1 | 0 | 10.0 | —/DA_Krug18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 94 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 1 | 0 | 10.0 | —/DA_Krug18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 95 | PASS | STABILIZE | 89.0 | 5 | 1 | 0 | 10.0 | —/DA_Krug18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 101 | REROLL | STABILIZE | 84.0 | 5 | 7 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.069545216858387 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 102 | BUY | STABILIZE | 84.0 | 5 | 5 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9092341065406799 | 0.0 | 0.0 | +e6ee6b15-d413-4678-8ffb-29272199a53d / -— |
| Jogador 8 | 2-7 | 103 | BUY | STABILIZE | 84.0 | 5 | 2 | 0 | 10.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8336760997772217 | 0.0 | 0.0 | +bb3be648-cee1-4b75-b472-59653324b9bd / -— |
| Jogador 8 | 2-7 | 104 | PASS | STABILIZE | 84.0 | 5 | 1 | 0 | 10.0 | —/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 111 | REROLL | STABILIZE | 84.0 | 5 | 7 | 0 | 10.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06702045351266861 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 112 | REROLL | STABILIZE | 84.0 | 5 | 5 | 0 | 10.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08092685043811798 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 113 | REROLL | STABILIZE | 84.0 | 5 | 3 | 0 | 10.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0670366883277893 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 114 | BUY | STABILIZE | 84.0 | 5 | 1 | 0 | 10.0 | Adaptador/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8375261425971985 | 0.0 | 0.0 | +82e109f9-54c8-492d-93e5-7e0dd0034b15 / -64afe66e-d5a9-466c-a4ff-9d32c9f153ce,bb3be648-cee1-4b75-b472-59653324b9bd |
| Jogador 8 | 3-1 | 115 | SELL | STABILIZE | 84.0 | 5 | 0 | 0 | 8.0 | Adaptador/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35346153378486633 | 0.0 | 0.0 | +— / -74c2d7f0-8d5d-460e-88fc-5407b717144a |
| Jogador 8 | 3-1 | 116 | PASS | STABILIZE | 84.0 | 5 | 1 | 0 | 8.0 | Adaptador/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 119 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 1 | 0 | 8.0 | Adaptador/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41235244274139404 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 121 | REROLL | STABILIZE | 75.0 | 5 | 7 | 0 | 14.0 | Adaptador/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06700003147125244 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 122 | BUY | STABILIZE | 75.0 | 5 | 5 | 0 | 14.0 | Adaptador/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8339773416519165 | 0.0 | 0.0 | +33a860e2-992f-4355-ab24-85b4a2576f90 / -e6ee6b15-d413-4678-8ffb-29272199a53d,eb214f08-2367-4b33-af94-8aa504781450 |
| Jogador 8 | 3-2 | 123 | REROLL | STABILIZE | 75.0 | 5 | 2 | 0 | 14.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 124 | PASS | STABILIZE | 75.0 | 5 | 0 | 0 | 14.0 | Adaptador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 131 | BUY | STABILIZE | 63.0 | 5 | 6 | 0 | 14.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28518790006637573 | 0.0 | 0.0 | +691cde76-cf1b-4a60-b818-65f790e312ec / -— |
| Jogador 8 | 3-3 | 132 | PASS | STABILIZE | 63.0 | 5 | 4 | 0 | 14.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 141 | PASS | STABILIZE | 52.0 | 5 | 11 | 1 | 14.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 151 | BUY | STABILIZE | 52.0 | 6 | 19 | 1 | 14.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0824950635433197 | 0.0 | 0.0 | +fb7e519a-8419-414a-8bdc-706c584ddeed / -— |
| Jogador 8 | 3-5 | 152 | BUY | STABILIZE | 52.0 | 6 | 16 | 1 | 14.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24821868538856506 | 0.0 | 0.0 | +dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 / -— |
| Jogador 8 | 3-5 | 153 | PASS | STABILIZE | 52.0 | 6 | 14 | 1 | 14.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 159 | MOVE_BENCH | STABILIZE | 52.0 | 6 | 14 | 1 | 14.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7621219158172607 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 161 | PASS | STABILIZE | 42.0 | 6 | 23 | 2 | 26.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 171 | BUY | SLOWROLL | 42.0 | 6 | 31 | 3 | 26.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24228547513484955 | 0.0 | 0.0 | +3a1de7b3-af72-4024-8105-588fa4ec946b / -— |
| Jogador 8 | 3-7 | 172 | PASS | SLOWROLL | 42.0 | 6 | 30 | 3 | 26.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 181 | BUY | SLOWROLL | 42.0 | 6 | 38 | 3 | 26.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7526397109031677 | 0.0 | 0.0 | +cba152f4-af54-4d82-a35d-67aa165174be / -d01cae02-d8ba-491e-841f-bf3120953933,fb7e519a-8419-414a-8bdc-706c584ddeed |
| Jogador 8 | 4-1 | 182 | PASS | SLOWROLL | 42.0 | 6 | 35 | 3 | 26.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.05999999865889549 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 191 | PASS | SLOWROLL | 42.0 | 6 | 45 | 4 | 26.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 199 | PASS | STABILIZE | 27.0 | 6 | 54 | 5 | 26.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.11999999731779099 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 207 | PASS | ALL_IN | 14.0 | 6 | 65 | 5 | 26.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.22280000150203705 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 214 | BUY | ALL_IN | 14.0 | 6 | 76 | 5 | 26.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8813216090202332 | 0.0 | 0.0 | +908d49c8-626c-44b5-9b03-6a85442f358b / -— |
| Jogador 8 | 4-5 | 215 | PASS | ALL_IN | 14.0 | 6 | 74 | 5 | 26.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.22280000150203705 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 223 | BUY | ALL_IN | 14.0 | 6 | 85 | 5 | 26.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4525688588619232 | 0.0 | 0.0 | +8756c125-e3d6-4f40-80d2-a6bf20e7b1c7 / -— |
| Jogador 8 | 4-6 | 224 | PASS | ALL_IN | 14.0 | 6 | 82 | 5 | 26.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.22280000150203705 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 232 | PASS | ALL_IN | 0.0 | 6 | 82 | 5 | 0.0 | Adaptador/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 242 | PASS | ALL_IN | 0.0 | 6 | 82 | 5 | 0.0 | Adaptador/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 252 | PASS | ALL_IN | 0.0 | 6 | 82 | 5 | 0.0 | Adaptador/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 262 | PASS | ALL_IN | 0.0 | 6 | 82 | 5 | 0.0 | Adaptador/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 272 | PASS | ALL_IN | 0.0 | 6 | 82 | 5 | 0.0 | Adaptador/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 282 | PASS | ALL_IN | 0.0 | 6 | 82 | 5 | 0.0 | Adaptador/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 292 | PASS | ALL_IN | 0.0 | 6 | 82 | 5 | 0.0 | Adaptador/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 302 | PASS | ALL_IN | 0.0 | 6 | 82 | 5 | 0.0 | Adaptador/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 312 | PASS | ALL_IN | 0.0 | 6 | 82 | 5 | 0.0 | Adaptador/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 322 | PASS | ALL_IN | 0.0 | 6 | 82 | 5 | 0.0 | Adaptador/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-3 | 332 | PASS | ALL_IN | 0.0 | 6 | 82 | 5 | 0.0 | Adaptador/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-4 | 342 | PASS | ALL_IN | 0.0 | 6 | 82 | 5 | 0.0 | Adaptador/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-5 | 352 | PASS | ALL_IN | 0.0 | 6 | 82 | 5 | 0.0 | Adaptador/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-6 | 362 | PASS | ALL_IN | 0.0 | 6 | 82 | 5 | 0.0 | Adaptador/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |

O audit_report.json mantém as máscaras brutas, distribuições da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Null indica campo ausente, não zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 129 | 135 | 11 | 7 | 20 | 2 | 0 | 0 | 178 | 0.0 |
- Jogador 1 — gasto por ação: BUY: 39g, BUY_XP: 96g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 6g, stage 2: 41g, stage 3: 47g, stage 4: 33g, stage 5: 8g, stage 6: 0g
| Jogador 2 | 107 | 92 | 14 | 3 | 5 | 1 | 1 | 0 | 244 | 38.0 |
- Jogador 2 — gasto por ação: BUY: 62g, BUY_XP: 28g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 12g, stage 2: 46g, stage 3: 13g, stage 4: 10g, stage 5: 8g, stage 6: 3g
| Jogador 3 | 119 | 86 | 1 | 6 | 5 | 1 | 5 | 1 | 102 | 0.0 |
- Jogador 3 — gasto por ação: BUY: 48g, BUY_XP: 28g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 10g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 5g, stage 2: 37g, stage 3: 32g, stage 4: 9g, stage 5: 3g, stage 6: 0g
| Jogador 4 | 95 | 48 | 4 | 0 | 1 | 0 | 2 | 1 | 116 | 0.0 |
- Jogador 4 — gasto por ação: BUY: 40g, BUY_XP: 4g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 4g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 9g, stage 2: 31g, stage 3: 3g, stage 4: 5g, stage 5: 0g, stage 6: 0g
| Jogador 5 | 76 | 34 | 5 | 1 | 0 | 0 | 0 | 0 | 177 | 0.0 |
- Jogador 5 — gasto por ação: BUY: 34g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 8g, stage 2: 20g, stage 3: 0g, stage 4: 6g, stage 5: 0g, stage 6: 0g
| Jogador 6 | 107 | 91 | 18 | 1 | 0 | 0 | 14 | 3 | 59 | 0.0 |
- Jogador 6 — gasto por ação: BUY: 63g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 28g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 8g, stage 2: 51g, stage 3: 23g, stage 4: 9g, stage 5: 0g, stage 6: 0g
| Jogador 7 | 112 | 91 | 5 | 3 | 4 | 0 | 0 | 0 | 294 | 56.0 |
- Jogador 7 — gasto por ação: BUY: 67g, BUY_XP: 24g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 5g, stage 2: 37g, stage 3: 22g, stage 4: 15g, stage 5: 12g, stage 6: 0g
| Jogador 8 | 109 | 82 | 8 | 1 | 0 | 0 | 13 | 3 | 82 | 0.0 |
- Jogador 8 — gasto por ação: BUY: 48g, BUY_XP: 8g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 26g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 14g, stage 2: 38g, stage 3: 22g, stage 4: 8g, stage 5: 0g, stage 6: 0g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 1 | 1 | 0 | 0.0% |
| Jogador 2 | 1 | 1 | 0 | 0.0% |
| Jogador 3 | 1 | 1 | 0 | 0.0% |
| Jogador 4 | 1 | 1 | 0 | 0.0% |
| Jogador 6 | 1 | 1 | 0 | 0.0% |
| Jogador 7 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 1 | 1 | 0 | 0.0% |

Os detalhes por transição ficam em audit_report.json. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ médio qualidade | Δ estrutural médio | Δ qualidade quando combate positivo | Δ qualidade quando combate negativo |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 129 | 0 | 0 | 129 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ 0.0000 (17 ações), BUY_XP: Δ 0.0000 (24 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0000 (35 ações), MOVE_BOARD: Δ 0.0000 (6 ações), PASS: Δ 0.0000 (36 ações), SELL: Δ 0.0000 (7 ações)
| Jogador 2 | 107 | 0 | 0 | 107 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ 0.0000 (30 ações), BUY_XP: Δ 0.0000 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0000 (21 ações), MOVE_BOARD: Δ 0.0000 (1 ações), PASS: Δ 0.0000 (35 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0000 (9 ações)
| Jogador 3 | 119 | 0 | 0 | 119 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ 0.0000 (23 ações), BUY_XP: Δ 0.0000 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (37 ações), MOVE_BOARD: Δ 0.0000 (9 ações), PASS: Δ 0.0000 (36 ações), REROLL: Δ 0.0000 (5 ações), SELL: Δ 0.0000 (1 ações)
| Jogador 4 | 95 | 0 | 0 | 95 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ 0.0000 (24 ações), BUY_XP: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (21 ações), MOVE_BOARD: Δ 0.0000 (5 ações), PASS: Δ 0.0000 (38 ações), REROLL: Δ 0.0000 (2 ações), SELL: Δ 0.0000 (4 ações)
| Jogador 5 | 76 | 0 | 0 | 76 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ 0.0000 (19 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (14 ações), MOVE_BOARD: Δ 0.0000 (1 ações), PASS: Δ 0.0000 (37 ações), SELL: Δ 0.0000 (4 ações)
| Jogador 6 | 107 | 0 | 0 | 107 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ 0.0000 (30 ações), MOVE_BENCH: Δ 0.0000 (14 ações), MOVE_BOARD: Δ 0.0000 (1 ações), PASS: Δ 0.0000 (36 ações), REROLL: Δ 0.0000 (14 ações), SELL: Δ 0.0000 (12 ações)
| Jogador 7 | 112 | 0 | 0 | 112 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ 0.0000 (26 ações), BUY_XP: Δ 0.0000 (6 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0000 (35 ações), MOVE_BOARD: Δ 0.0000 (2 ações), PASS: Δ 0.0000 (37 ações), SELL: Δ 0.0000 (3 ações)
| Jogador 8 | 109 | 0 | 0 | 109 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ 0.0000 (27 ações), BUY_XP: Δ 0.0000 (2 ações), MOVE_BENCH: Δ 0.0000 (17 ações), MOVE_BOARD: Δ 0.0000 (6 ações), PASS: Δ 0.0000 (36 ações), REROLL: Δ 0.0000 (13 ações), SELL: Δ 0.0000 (8 ações)

A pontuação é uma heurística para auditoria, não uma verdade absoluta. Compare-a com recompensas e resultados de combate; correlação não prova causalidade.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.076 | 0.000 |
| Jogador 1 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.010 | 0.000 |
| Jogador 1 | 1-3 | 7 | 2.000 | 2.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.016 | 0.000 |
| Jogador 1 | 1-4 | 5 | 0.000 | -2.000 | 0 → 0 | 1 → 0 | 11% → 11% | 3 → 8 | 1 | 3 → 4 | 0.000 | 0.000 |
| Jogador 1 | 2-1 | 8 | 4.000 | 2.000 | 0 → 0 | 0 → 1 | 11% → 14% | 8 → 7 | 8 | 4 → 4 | 0.001 | 0.327 |
| Jogador 1 | 2-2 | 8 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 7 → 7 | 7 | 4 → 5 | 0.017 | 0.297 |
| Jogador 1 | 2-3 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 7 → 14 | 0 | 5 → 5 | 0.000 | 0.628 |
| Jogador 1 | 2-4 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 14 → 21 | 0 | 5 → 5 | 0.000 | 0.000 |
| Jogador 1 | 2-5 | 10 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 21% | 21 → 9 | 19 | 5 → 6 | -0.024 | 0.291 |
| Jogador 1 | 2-6 | 10 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 21% → 21% | 9 → 10 | 7 | 6 → 6 | -0.022 | 0.275 |
| Jogador 1 | 2-7 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 10 → 18 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 3-1 | 7 | -4.000 | 4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 18 → 24 | 0 | 6 → 6 | 0.000 | -0.402 |
| Jogador 1 | 3-2 | 5 | 4.000 | -4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 24 → 32 | 0 | 6 → 6 | 0.000 | 0.562 |
| Jogador 1 | 3-3 | 10 | 2.000 | 4.000 | 0 → 0 | 1 → 2 | 21% → 25% | 32 → 8 | 31 | 6 → 7 | 0.000 | 0.298 |
| Jogador 1 | 3-4 | 8 | 4.000 | -12.000 | 0 → 0 | 2 → 0 | 25% → 25% | 8 → 6 | 12 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 3-5 | 3 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 6 → 9 | 4 | 7 → 7 | 0.000 | 0.983 |
| Jogador 1 | 3-6 | 3 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 9 → 17 | 0 | 7 → 7 | -0.001 | 0.995 |
| Jogador 1 | 3-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 17 → 24 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 4-1 | 10 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 24 → 8 | 27 | 7 → 8 | 0.000 | 0.298 |
| Jogador 1 | 4-2 | 6 | 8.000 | 4.000 | 0 → 0 | 0 → 1 | 25% → 29% | 8 → 11 | 6 | 8 → 8 | -0.003 | 0.509 |
| Jogador 1 | 4-3 | 3 | 2.000 | -2.000 | 0 → 0 | 1 → 1 | 29% → 29% | 11 → 21 | 0 | 8 → 8 | -0.069 | 1.028 |
| Jogador 1 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 21 → 31 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 4-5 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 31 → 43 | 0 | 8 → 8 | 0.000 | 1.531 |
| Jogador 1 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 43 → 56 | 0 | 8 → 8 | 0.000 | 1.553 |
| Jogador 1 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 56 → 69 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 5-1 | 4 | 0.000 | 10.000 | 0 → 0 | 1 → 1 | 29% → 29% | 69 → 74 | 5 | 8 → 8 | 0.000 | -0.683 |
| Jogador 1 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 74 → 85 | 0 | 8 → 8 | 0.000 | -1.425 |
| Jogador 1 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 85 → 96 | 0 | 8 → 8 | 0.000 | -1.425 |
| Jogador 1 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 96 → 107 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 107 → 118 | 0 | 8 → 8 | 0.000 | -1.400 |
| Jogador 1 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 118 → 129 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 5-7 | 3 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 29% → 29% | 129 → 137 | 3 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 6-1 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 137 → 148 | 0 | 8 → 8 | 0.000 | 0.774 |
| Jogador 1 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 148 → 158 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 158 → 168 | 0 | 8 → 8 | 0.000 | -1.425 |
| Jogador 1 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 168 → 178 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 6-5 | 2 | -40.000 | -18.000 | 0 → 0 | 2 → 0 | 29% → 0% | 178 → 178 | 0 | 8 → 8 | 0.169 | -1.425 |
| Jogador 1 | 6-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 178 → 178 | 0 | 8 → 8 | 0.000 | 0.000 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 1, COMPOSITION_COMPATIBILITY: 9, PAIR_POTENTIAL: 7; mudanças de composição: 0; posicionamento melhorou em 11 ações e piorou em 11.
- Jogador 1 — estado final: ouro 178, nível 8, vida 0.0, colocação 3.
| Jogador 2 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.064 | 0.000 |
| Jogador 2 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 2 | 1-3 | 5 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 2 → 4 | 1 | 3 → 3 | 0.000 | 0.000 |
| Jogador 2 | 1-4 | 10 | 2.000 | 2.000 | 0 → 0 | 2 → 1 | 11% → 11% | 4 → 4 | 8 | 3 → 4 | -0.031 | 0.000 |
| Jogador 2 | 2-1 | 10 | 0.000 | -2.000 | 0 → 0 | 1 → 0 | 11% → 7% | 4 → 10 | 5 | 4 → 4 | 0.018 | -0.258 |
| Jogador 2 | 2-2 | 7 | 10.000 | -2.000 | 0 → 0 | 0 → 0 | 7% → 14% | 10 → 12 | 5 | 4 → 4 | -0.028 | -0.323 |
| Jogador 2 | 2-3 | 10 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 18% | 12 → 8 | 12 | 4 → 5 | -0.047 | -0.237 |
| Jogador 2 | 2-4 | 6 | 2.000 | 10.000 | 0 → 0 | 0 → 0 | 18% → 18% | 8 → 8 | 6 | 5 → 5 | 0.037 | 0.000 |
| Jogador 2 | 2-5 | 7 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 18% → 18% | 8 → 7 | 7 | 5 → 5 | 0.028 | 0.408 |
| Jogador 2 | 2-6 | 3 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 7 → 10 | 4 | 5 → 5 | 0.000 | 0.837 |
| Jogador 2 | 2-7 | 5 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 21% | 10 → 9 | 7 | 5 → 6 | -0.027 | 0.000 |
| Jogador 2 | 3-1 | 4 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 9 → 8 | 8 | 6 → 6 | 0.000 | 0.763 |
| Jogador 2 | 3-2 | 3 | 0.000 | 6.000 | 0 → 0 | 0 → 1 | 21% → 21% | 8 → 12 | 3 | 6 → 6 | 0.000 | 1.011 |
| Jogador 2 | 3-3 | 3 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 21% → 21% | 12 → 19 | 2 | 6 → 6 | 0.000 | 1.028 |
| Jogador 2 | 3-4 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 19 → 27 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 3-5 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 27 → 38 | 0 | 6 → 6 | 0.000 | 1.431 |
| Jogador 2 | 3-6 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 38 → 46 | 0 | 6 → 6 | 0.000 | -1.316 |
| Jogador 2 | 3-7 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 46 → 55 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 4-1 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 55 → 66 | 0 | 6 → 6 | 0.000 | 1.431 |
| Jogador 2 | 4-2 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 66 → 78 | 0 | 6 → 6 | 0.000 | 1.381 |
| Jogador 2 | 4-3 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 78 → 90 | 0 | 6 → 6 | 0.000 | 1.542 |
| Jogador 2 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 90 → 101 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 4-5 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 101 → 111 | 0 | 6 → 7 | 0.000 | -1.450 |
| Jogador 2 | 4-6 | 4 | 6.000 | 4.000 | 0 → 0 | 2 → 3 | 21% → 25% | 111 → 117 | 5 | 7 → 7 | -0.032 | 0.733 |
| Jogador 2 | 4-7 | 3 | 0.000 | 10.000 | 0 → 0 | 3 → 3 | 25% → 25% | 117 → 122 | 5 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 5-1 | 6 | -2.000 | 8.000 | 0 → 0 | 3 → 3 | 25% → 21% | 122 → 128 | 6 | 7 → 7 | 0.011 | 0.489 |
| Jogador 2 | 5-2 | 3 | 4.000 | -4.000 | 0 → 0 | 3 → 3 | 21% → 25% | 128 → 140 | 0 | 7 → 7 | -0.042 | 0.985 |
| Jogador 2 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 25% → 25% | 140 → 152 | 0 | 7 → 7 | 0.000 | 1.478 |
| Jogador 2 | 5-4 | 3 | 0.000 | 4.000 | 0 → 0 | 3 → 4 | 25% → 25% | 152 → 161 | 2 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 161 → 172 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 172 → 182 | 0 | 7 → 7 | 0.000 | -1.450 |
| Jogador 2 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 182 → 192 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 6-1 | 4 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 192 → 203 | 0 | 7 → 7 | 0.000 | -0.725 |
| Jogador 2 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 203 → 214 | 0 | 7 → 7 | 0.000 | -1.450 |
| Jogador 2 | 6-3 | 3 | 0.000 | 6.000 | 0 → 0 | 4 → 4 | 25% → 25% | 214 → 222 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 222 → 233 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 233 → 244 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 6-6 | 2 | -38.000 | -54.000 | 0 → 0 | 4 → 0 | 25% → 0% | 244 → 244 | 0 | 7 → 7 | 0.193 | -1.450 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 4, COMPOSITION_COMPATIBILITY: 15, IMMEDIATE_UPGRADE: 3, PAIR_POTENTIAL: 8; mudanças de composição: 0; posicionamento melhorou em 12 ações e piorou em 18.
- Jogador 2 — estado final: ouro 244, nível 7, vida 0.0, colocação 2.
| Jogador 3 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.076 | 0.000 |
| Jogador 3 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.027 | 0.000 |
| Jogador 3 | 1-3 | 7 | 2.000 | 2.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 3 | 1-4 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 3 → 7 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 3 | 2-1 | 7 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 14% | 7 → 7 | 6 | 4 → 4 | 0.027 | 0.340 |
| Jogador 3 | 2-2 | 6 | 4.000 | 0.000 | 0 → 0 | 1 → 2 | 14% → 18% | 7 → 8 | 6 | 4 → 5 | -0.006 | 0.459 |
| Jogador 3 | 2-3 | 4 | -2.000 | 2.000 | 0 → 0 | 2 → 2 | 18% → 18% | 8 → 15 | 0 | 5 → 5 | -0.009 | 0.689 |
| Jogador 3 | 2-4 | 6 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 18% → 18% | 15 → 19 | 3 | 5 → 5 | 0.000 | 0.000 |
| Jogador 3 | 2-5 | 10 | -2.000 | 10.000 | 0 → 0 | 2 → 2 | 18% → 18% | 19 → 12 | 14 | 5 → 5 | -0.020 | 0.269 |
| Jogador 3 | 2-6 | 8 | 6.000 | -2.000 | 0 → 0 | 2 → 2 | 18% → 21% | 12 → 11 | 6 | 5 → 6 | -0.041 | -0.296 |
| Jogador 3 | 2-7 | 5 | 2.000 | 2.000 | 0 → 0 | 2 → 3 | 21% → 21% | 11 → 14 | 2 | 6 → 6 | -0.051 | 0.000 |
| Jogador 3 | 3-1 | 10 | -4.000 | 10.000 | 0 → 0 | 3 → 3 | 21% → 21% | 14 → 9 | 11 | 6 → 6 | 0.081 | 0.286 |
| Jogador 3 | 3-2 | 8 | 4.000 | 10.000 | 0 → 0 | 3 → 3 | 21% → 18% | 9 → 6 | 8 | 6 → 6 | -0.111 | -0.329 |
| Jogador 3 | 3-3 | 4 | 6.000 | 0.000 | 0 → 0 | 3 → 4 | 18% → 21% | 6 → 9 | 3 | 6 → 6 | 0.014 | 0.750 |
| Jogador 3 | 3-4 | 4 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 21% → 21% | 9 → 10 | 4 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 3-5 | 6 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 21% → 21% | 10 → 9 | 6 | 6 → 6 | -0.032 | -0.439 |
| Jogador 3 | 3-6 | 4 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 21% → 21% | 9 → 16 | 0 | 6 → 6 | 0.012 | 0.771 |
| Jogador 3 | 3-7 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 21% → 21% | 16 → 22 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 4-1 | 3 | 0.000 | 0.000 | 0 → 0 | 4 → 3 | 21% → 21% | 22 → 27 | 2 | 6 → 6 | -0.020 | -0.894 |
| Jogador 3 | 4-2 | 3 | -4.000 | 4.000 | 0 → 1 | 3 → 2 | 21% → 18% | 27 → 32 | 3 | 6 → 6 | 0.266 | -0.892 |
| Jogador 3 | 4-3 | 3 | 12.000 | -12.000 | 1 → 2 | 2 → 2 | 18% → 21% | 32 → 41 | 0 | 6 → 6 | 0.001 | -0.950 |
| Jogador 3 | 4-4 | 3 | 0.000 | 4.000 | 2 → 2 | 2 → 2 | 21% → 21% | 41 → 48 | 2 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 4-5 | 2 | 0.000 | 0.000 | 2 → 2 | 2 → 2 | 21% → 21% | 48 → 58 | 0 | 6 → 7 | 0.000 | -1.425 |
| Jogador 3 | 4-6 | 3 | 4.000 | 0.000 | 2 → 2 | 2 → 3 | 21% → 25% | 58 → 68 | 2 | 7 → 7 | 0.001 | -0.921 |
| Jogador 3 | 4-7 | 2 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 25% → 25% | 68 → 80 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 5-1 | 3 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 25% → 25% | 80 → 92 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 5-2 | 2 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 25% → 25% | 92 → 105 | 0 | 7 → 7 | 0.000 | -1.400 |
| Jogador 3 | 5-3 | 3 | -38.000 | -36.000 | 2 → 0 | 3 → 0 | 25% → 0% | 105 → 102 | 3 | 7 → 7 | -0.016 | -0.933 |
| Jogador 3 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 102 → 102 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 102 → 102 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 102 → 102 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 102 → 102 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 102 → 102 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 102 → 102 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 102 → 102 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 102 → 102 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 102 → 102 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 6-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 102 → 102 | 0 | 7 → 7 | 0.000 | 0.000 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 4, COMPOSITION_COMPATIBILITY: 8, IMMEDIATE_UPGRADE: 4, PAIR_POTENTIAL: 7; mudanças de composição: 0; posicionamento melhorou em 18 ações e piorou em 25.
- Jogador 3 — estado final: ouro 102, nível 7, vida 0.0, colocação 4.
| Jogador 4 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.064 | 0.000 |
| Jogador 4 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.019 | 0.000 |
| Jogador 4 | 1-3 | 8 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 4 | 3 | 3 → 3 | -0.033 | 0.000 |
| Jogador 4 | 1-4 | 9 | 2.000 | 2.000 | 0 → 1 | 0 → 1 | 11% → 11% | 4 → 5 | 3 | 3 → 4 | 0.034 | 0.000 |
| Jogador 4 | 2-1 | 9 | 6.000 | -2.000 | 1 → 3 | 1 → 0 | 11% → 11% | 5 → 5 | 5 | 4 → 4 | -0.089 | -0.275 |
| Jogador 4 | 2-2 | 7 | 2.000 | 8.000 | 3 → 2 | 0 → 0 | 11% → 14% | 5 → 6 | 5 | 4 → 4 | 0.101 | -0.346 |
| Jogador 4 | 2-3 | 8 | 4.000 | -4.000 | 2 → 3 | 0 → 0 | 14% → 14% | 6 → 8 | 5 | 4 → 5 | -0.106 | -0.303 |
| Jogador 4 | 2-4 | 8 | 4.000 | 12.000 | 3 → 3 | 0 → 0 | 14% → 18% | 8 → 6 | 8 | 5 → 5 | 0.003 | 0.000 |
| Jogador 4 | 2-5 | 5 | 0.000 | 6.000 | 3 → 3 | 0 → 1 | 18% → 18% | 6 → 9 | 3 | 5 → 5 | -0.003 | -0.507 |
| Jogador 4 | 2-6 | 4 | 0.000 | 2.000 | 3 → 3 | 1 → 1 | 18% → 18% | 9 → 13 | 3 | 5 → 5 | 0.000 | -0.646 |
| Jogador 4 | 2-7 | 3 | 0.000 | 4.000 | 3 → 3 | 1 → 2 | 18% → 18% | 13 → 19 | 2 | 5 → 5 | 0.000 | 0.000 |
| Jogador 4 | 3-1 | 3 | 0.000 | 2.000 | 3 → 3 | 2 → 2 | 18% → 18% | 19 → 27 | 1 | 5 → 5 | 0.000 | -0.894 |
| Jogador 4 | 3-2 | 2 | 0.000 | 0.000 | 3 → 3 | 2 → 2 | 18% → 18% | 27 → 37 | 0 | 5 → 5 | 0.000 | -1.294 |
| Jogador 4 | 3-3 | 3 | 0.000 | 0.000 | 3 → 3 | 2 → 2 | 18% → 18% | 37 → 46 | 2 | 5 → 5 | 0.000 | -0.971 |
| Jogador 4 | 3-4 | 2 | 0.000 | 0.000 | 3 → 3 | 2 → 2 | 18% → 18% | 46 → 58 | 0 | 5 → 5 | 0.000 | 0.000 |
| Jogador 4 | 3-5 | 2 | 0.000 | 0.000 | 3 → 3 | 2 → 2 | 18% → 18% | 58 → 71 | 0 | 5 → 5 | 0.000 | -1.388 |
| Jogador 4 | 3-6 | 2 | 0.000 | 0.000 | 3 → 3 | 2 → 2 | 18% → 18% | 71 → 84 | 0 | 5 → 6 | 0.000 | -1.269 |
| Jogador 4 | 3-7 | 3 | 6.000 | -6.000 | 3 → 3 | 2 → 2 | 18% → 21% | 84 → 97 | 0 | 6 → 6 | 0.015 | 0.000 |
| Jogador 4 | 4-1 | 3 | 0.000 | 6.000 | 3 → 3 | 2 → 2 | 21% → 21% | 97 → 107 | 3 | 6 → 6 | 0.000 | -0.921 |
| Jogador 4 | 4-2 | 3 | 0.000 | 4.000 | 3 → 3 | 2 → 2 | 21% → 21% | 107 → 116 | 2 | 6 → 6 | -0.020 | 0.950 |
| Jogador 4 | 4-3 | 2 | -32.000 | -34.000 | 3 → 0 | 2 → 0 | 21% → 0% | 116 → 116 | 0 | 6 → 6 | 0.373 | -1.466 |
| Jogador 4 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 116 → 116 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 4-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 116 → 116 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 116 → 116 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 116 → 116 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 116 → 116 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 116 → 116 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 116 → 116 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 116 → 116 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 116 → 116 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 116 → 116 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 116 → 116 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 116 → 116 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 116 → 116 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 116 → 116 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 116 → 116 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 116 → 116 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 116 → 116 | 0 | 6 → 6 | 0.000 | 0.000 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 6, COMPOSITION_COMPATIBILITY: 10, IMMEDIATE_UPGRADE: 3, PAIR_POTENTIAL: 5; mudanças de composição: 0; posicionamento melhorou em 14 ações e piorou em 13.
- Jogador 4 — estado final: ouro 116, nível 6, vida 0.0, colocação 8.
| Jogador 5 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.067 | 0.000 |
| Jogador 5 | 1-2 | 4 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.018 | 0.000 |
| Jogador 5 | 1-3 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | 0.007 | 0.000 |
| Jogador 5 | 1-4 | 7 | -2.000 | 8.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.131 | 0.000 |
| Jogador 5 | 2-1 | 10 | 8.000 | -6.000 | 0 → 0 | 0 → 0 | 11% → 14% | 4 → 9 | 5 | 4 → 4 | -0.005 | 0.274 |
| Jogador 5 | 2-2 | 6 | 0.000 | 18.000 | 0 → 0 | 0 → 0 | 14% → 14% | 9 → 5 | 9 | 4 → 4 | 0.024 | -0.422 |
| Jogador 5 | 2-3 | 4 | 0.000 | 2.000 | 0 → 0 | 0 → 1 | 14% → 14% | 5 → 10 | 1 | 4 → 4 | 0.000 | -0.646 |
| Jogador 5 | 2-4 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 10 → 17 | 0 | 4 → 4 | 0.000 | 0.000 |
| Jogador 5 | 2-5 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 17 → 24 | 0 | 4 → 5 | 0.000 | -1.343 |
| Jogador 5 | 2-6 | 7 | 4.000 | 4.000 | 0 → 0 | 1 → 2 | 14% → 14% | 24 → 26 | 5 | 5 → 5 | -0.037 | -0.369 |
| Jogador 5 | 2-7 | 3 | 6.000 | -6.000 | 0 → 0 | 2 → 2 | 14% → 18% | 26 → 34 | 0 | 5 → 5 | 0.011 | 0.000 |
| Jogador 5 | 3-1 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 34 → 43 | 0 | 5 → 5 | 0.000 | 1.383 |
| Jogador 5 | 3-2 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 43 → 54 | 0 | 5 → 5 | 0.000 | 1.383 |
| Jogador 5 | 3-3 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 54 → 64 | 0 | 5 → 5 | 0.000 | -1.413 |
| Jogador 5 | 3-4 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 64 → 74 | 0 | 5 → 5 | 0.000 | 0.000 |
| Jogador 5 | 3-5 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 74 → 85 | 0 | 5 → 5 | 0.000 | -1.294 |
| Jogador 5 | 3-6 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 85 → 96 | 0 | 5 → 5 | 0.000 | -1.407 |
| Jogador 5 | 3-7 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 96 → 107 | 0 | 5 → 5 | 0.000 | 0.000 |
| Jogador 5 | 4-1 | 4 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 18% → 18% | 107 → 114 | 4 | 5 → 6 | 0.000 | -0.669 |
| Jogador 5 | 4-2 | 2 | 6.000 | -6.000 | 0 → 0 | 2 → 2 | 18% → 21% | 114 → 126 | 0 | 6 → 6 | -0.005 | -1.291 |
| Jogador 5 | 4-3 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 126 → 137 | 0 | 6 → 6 | 0.000 | 1.506 |
| Jogador 5 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 137 → 147 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-5 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 147 → 159 | 0 | 6 → 6 | 0.000 | 1.506 |
| Jogador 5 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 159 → 169 | 0 | 6 → 6 | 0.000 | -1.400 |
| Jogador 5 | 4-7 | 4 | 4.000 | -4.000 | 0 → 1 | 2 → 1 | 21% → 21% | 169 → 177 | 2 | 6 → 6 | -0.078 | 0.000 |
| Jogador 5 | 5-1 | 3 | -36.000 | -18.000 | 1 → 0 | 1 → 0 | 21% → 0% | 177 → 177 | 0 | 6 → 6 | 0.236 | -0.927 |
| Jogador 5 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 177 → 177 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 177 → 177 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 177 → 177 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 177 → 177 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 177 → 177 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 177 → 177 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 177 → 177 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 177 → 177 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 177 → 177 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 177 → 177 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 177 → 177 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 177 → 177 | 0 | 6 → 6 | 0.000 | 0.000 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 3, COMPOSITION_COMPATIBILITY: 11, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 3; mudanças de composição: 0; posicionamento melhorou em 9 ações e piorou em 9.
- Jogador 5 — estado final: ouro 177, nível 6, vida 0.0, colocação 5.
| Jogador 6 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.076 | 0.000 |
| Jogador 6 | 1-2 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | -0.247 | 0.000 |
| Jogador 6 | 1-3 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | 0.016 | 0.000 |
| Jogador 6 | 1-4 | 7 | -2.000 | 8.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | 0.091 | 0.000 |
| Jogador 6 | 2-1 | 10 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 4 → 6 | 5 | 4 → 4 | -0.057 | -0.226 |
| Jogador 6 | 2-2 | 6 | -2.000 | 12.000 | 0 → 0 | 0 → 0 | 14% → 14% | 6 → 7 | 5 | 4 → 4 | -0.013 | 0.427 |
| Jogador 6 | 2-3 | 10 | 0.000 | 8.000 | 0 → 0 | 0 → 1 | 14% → 14% | 7 → 8 | 10 | 4 → 4 | 0.000 | 0.264 |
| Jogador 6 | 2-4 | 10 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 14% → 14% | 8 → 6 | 14 | 4 → 4 | 0.000 | 0.000 |
| Jogador 6 | 2-5 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 7 | 4 | 4 → 5 | 0.000 | -0.684 |
| Jogador 6 | 2-6 | 7 | 6.000 | 4.000 | 0 → 0 | 2 → 1 | 14% → 18% | 7 → 6 | 7 | 5 → 5 | -0.003 | 0.366 |
| Jogador 6 | 2-7 | 6 | 0.000 | -2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 6 → 6 | 6 | 5 → 5 | 0.000 | 0.000 |
| Jogador 6 | 3-1 | 7 | 0.000 | 0.000 | 0 → 0 | 1 → 2 | 18% → 18% | 6 → 5 | 8 | 5 → 5 | 0.009 | -0.411 |
| Jogador 6 | 3-2 | 6 | 0.000 | -4.000 | 0 → 0 | 2 → 1 | 18% → 18% | 5 → 6 | 7 | 5 → 5 | 0.020 | -0.477 |
| Jogador 6 | 3-3 | 4 | 0.000 | 12.000 | 0 → 0 | 1 → 1 | 18% → 18% | 6 → 6 | 6 | 5 → 5 | -0.015 | -0.704 |
| Jogador 6 | 3-4 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 6 → 12 | 0 | 5 → 5 | 0.000 | 0.000 |
| Jogador 6 | 3-5 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 12 → 19 | 0 | 5 → 5 | 0.000 | 1.383 |
| Jogador 6 | 3-6 | 3 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 18% → 18% | 19 → 23 | 2 | 5 → 5 | 0.000 | -0.971 |
| Jogador 6 | 3-7 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 23 → 30 | 0 | 5 → 5 | 0.000 | 0.000 |
| Jogador 6 | 4-1 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 30 → 39 | 0 | 5 → 6 | 0.000 | -1.407 |
| Jogador 6 | 4-2 | 3 | 4.000 | 2.000 | 0 → 0 | 1 → 1 | 18% → 21% | 39 → 45 | 3 | 6 → 6 | -0.046 | -0.892 |
| Jogador 6 | 4-3 | 3 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 21% → 21% | 45 → 52 | 3 | 6 → 6 | 0.000 | -0.971 |
| Jogador 6 | 4-4 | 3 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 21% → 21% | 52 → 59 | 3 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 4-5 | 2 | -22.000 | -60.000 | 0 → 0 | 2 → 0 | 21% → 0% | 59 → 59 | 0 | 6 → 6 | 0.411 | -1.338 |
| Jogador 6 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 59 → 59 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 59 → 59 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 5-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 59 → 59 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 59 → 59 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 59 → 59 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 59 → 59 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 59 → 59 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 59 → 59 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 59 → 59 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 59 → 59 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 59 → 59 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 59 → 59 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 59 → 59 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 59 → 59 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 6-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 59 → 59 | 0 | 6 → 6 | 0.000 | 0.000 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 8, COMPOSITION_COMPATIBILITY: 12, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 8; mudanças de composição: 0; posicionamento melhorou em 12 ações e piorou em 18.
- Jogador 6 — estado final: ouro 59, nível 6, vida 0.0, colocação 7.
| Jogador 7 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.076 | 0.000 |
| Jogador 7 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.035 | 0.000 |
| Jogador 7 | 1-3 | 5 | 2.000 | 2.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.006 | 0.000 |
| Jogador 7 | 1-4 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 3 → 7 | 0 | 3 → 4 | 0.004 | 0.000 |
| Jogador 7 | 2-1 | 7 | 4.000 | 0.000 | 0 → 0 | 1 → 2 | 11% → 14% | 7 → 7 | 6 | 4 → 4 | 0.010 | 0.366 |
| Jogador 7 | 2-2 | 6 | 2.000 | 4.000 | 0 → 0 | 2 → 2 | 14% → 14% | 7 → 9 | 3 | 4 → 4 | -0.003 | -0.431 |
| Jogador 7 | 2-3 | 10 | 0.000 | 10.000 | 0 → 0 | 2 → 2 | 14% → 18% | 9 → 6 | 9 | 4 → 5 | 0.007 | -0.248 |
| Jogador 7 | 2-4 | 6 | 6.000 | 2.000 | 0 → 0 | 2 → 2 | 18% → 18% | 6 → 8 | 4 | 5 → 5 | -0.004 | 0.000 |
| Jogador 7 | 2-5 | 8 | 4.000 | -6.000 | 0 → 0 | 2 → 2 | 18% → 18% | 8 → 7 | 8 | 5 → 5 | 0.007 | 0.338 |
| Jogador 7 | 2-6 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 7 → 14 | 0 | 5 → 5 | 0.000 | 1.377 |
| Jogador 7 | 2-7 | 7 | 4.000 | 2.000 | 0 → 0 | 2 → 2 | 18% → 21% | 14 → 13 | 7 | 5 → 6 | -0.011 | 0.000 |
| Jogador 7 | 3-1 | 4 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 21% → 21% | 13 → 13 | 7 | 6 → 6 | 0.000 | 0.746 |
| Jogador 7 | 3-2 | 3 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 21% → 21% | 13 → 18 | 3 | 6 → 6 | 0.000 | 1.011 |
| Jogador 7 | 3-3 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 18 → 27 | 0 | 6 → 6 | 0.000 | 1.500 |
| Jogador 7 | 3-4 | 7 | -4.000 | 16.000 | 0 → 0 | 2 → 0 | 21% → 14% | 27 → 26 | 9 | 6 → 6 | -0.034 | 0.000 |
| Jogador 7 | 3-5 | 4 | 6.000 | 0.000 | 0 → 0 | 0 → 1 | 14% → 18% | 26 → 34 | 3 | 6 → 6 | -0.026 | 0.703 |
| Jogador 7 | 3-6 | 3 | 6.000 | -6.000 | 0 → 0 | 1 → 1 | 18% → 21% | 34 → 46 | 0 | 6 → 6 | -0.020 | 0.937 |
| Jogador 7 | 3-7 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 46 → 58 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 4-1 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 58 → 72 | 0 | 6 → 6 | 0.000 | 1.467 |
| Jogador 7 | 4-2 | 3 | 0.000 | -4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 72 → 89 | 0 | 6 → 6 | 0.020 | 0.950 |
| Jogador 7 | 4-3 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 89 → 103 | 0 | 6 → 6 | 0.000 | 1.481 |
| Jogador 7 | 4-4 | 6 | 0.000 | 8.000 | 0 → 1 | 1 → 0 | 21% → 18% | 103 → 109 | 7 | 6 → 6 | 0.010 | 0.000 |
| Jogador 7 | 4-5 | 4 | 6.000 | 0.000 | 1 → 1 | 0 → 1 | 18% → 21% | 109 → 120 | 3 | 6 → 6 | -0.015 | 0.713 |
| Jogador 7 | 4-6 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 21% → 21% | 120 → 134 | 0 | 6 → 6 | 0.000 | 1.481 |
| Jogador 7 | 4-7 | 5 | 0.000 | 4.000 | 1 → 2 | 1 → 0 | 21% → 18% | 134 → 142 | 5 | 6 → 7 | 0.011 | 0.000 |
| Jogador 7 | 5-1 | 5 | 10.000 | 0.000 | 2 → 2 | 0 → 0 | 18% → 21% | 142 → 151 | 5 | 7 → 7 | -0.003 | 0.577 |
| Jogador 7 | 5-2 | 3 | 4.000 | -4.000 | 2 → 2 | 0 → 0 | 21% → 25% | 151 → 165 | 0 | 7 → 7 | -0.003 | 1.007 |
| Jogador 7 | 5-3 | 2 | 0.000 | 0.000 | 2 → 2 | 0 → 0 | 25% → 25% | 165 → 179 | 0 | 7 → 7 | 0.000 | 1.511 |
| Jogador 7 | 5-4 | 4 | 0.000 | 14.000 | 2 → 2 | 0 → 1 | 25% → 25% | 179 → 185 | 7 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 5-5 | 2 | 0.000 | 0.000 | 2 → 2 | 1 → 1 | 25% → 25% | 185 → 199 | 0 | 7 → 7 | 0.000 | 1.486 |
| Jogador 7 | 5-6 | 2 | 0.000 | 0.000 | 2 → 2 | 1 → 1 | 25% → 25% | 199 → 213 | 0 | 7 → 7 | 0.000 | 1.528 |
| Jogador 7 | 5-7 | 2 | 0.000 | 0.000 | 2 → 2 | 1 → 1 | 25% → 25% | 213 → 226 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 6-1 | 4 | 0.000 | 0.000 | 2 → 2 | 1 → 1 | 25% → 25% | 226 → 239 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 6-2 | 2 | 0.000 | 0.000 | 2 → 2 | 1 → 1 | 25% → 25% | 239 → 253 | 0 | 7 → 7 | 0.000 | 1.543 |
| Jogador 7 | 6-3 | 2 | 0.000 | 0.000 | 2 → 2 | 1 → 1 | 25% → 25% | 253 → 267 | 0 | 7 → 7 | 0.000 | 1.523 |
| Jogador 7 | 6-4 | 2 | 0.000 | 0.000 | 2 → 2 | 1 → 1 | 25% → 25% | 267 → 280 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 6-5 | 2 | 0.000 | 0.000 | 2 → 2 | 1 → 1 | 25% → 25% | 280 → 294 | 0 | 7 → 7 | 0.000 | 1.523 |
| Jogador 7 | 6-6 | 2 | 0.000 | 0.000 | 2 → 2 | 1 → 1 | 25% → 25% | 294 → 295 | 0 | 7 → 7 | 0.000 | 1.543 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 3, COMPOSITION_COMPATIBILITY: 14, IMMEDIATE_UPGRADE: 4, PAIR_POTENTIAL: 5; mudanças de composição: 0; posicionamento melhorou em 18 ações e piorou em 20.
- Jogador 7 — estado final: ouro 295, nível 7, vida 87.0, colocação 1.
| Jogador 8 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.076 | 0.000 |
| Jogador 8 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.140 | 0.000 |
| Jogador 8 | 1-3 | 10 | 0.000 | 2.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 4 | 4 | 3 → 3 | -0.008 | 0.000 |
| Jogador 8 | 1-4 | 10 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 11% → 14% | 4 → 4 | 7 | 3 → 4 | -0.005 | 0.000 |
| Jogador 8 | 2-1 | 5 | 0.000 | 2.000 | 0 → 0 | 0 → 1 | 14% → 14% | 4 → 8 | 1 | 4 → 4 | 0.000 | -0.484 |
| Jogador 8 | 2-2 | 10 | 2.000 | 6.000 | 0 → 0 | 1 → 2 | 14% → 18% | 8 → 6 | 8 | 4 → 5 | -0.001 | 0.269 |
| Jogador 8 | 2-3 | 7 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 18% → 18% | 6 → 10 | 3 | 5 → 5 | 0.008 | 0.366 |
| Jogador 8 | 2-4 | 6 | 0.000 | 12.000 | 0 → 0 | 2 → 2 | 18% → 18% | 10 → 6 | 10 | 5 → 5 | -0.020 | 0.000 |
| Jogador 8 | 2-5 | 5 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 6 → 5 | 6 | 5 → 5 | 0.000 | -0.506 |
| Jogador 8 | 2-6 | 6 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 5 → 7 | 4 | 5 → 5 | 0.000 | -0.404 |
| Jogador 8 | 2-7 | 5 | 0.000 | 8.000 | 0 → 0 | 2 → 4 | 18% → 18% | 7 → 7 | 6 | 5 → 5 | -0.012 | 0.000 |
| Jogador 8 | 3-1 | 8 | 4.000 | -6.000 | 0 → 0 | 4 → 2 | 18% → 18% | 7 → 7 | 7 | 5 → 5 | 0.076 | -0.323 |
| Jogador 8 | 3-2 | 5 | 0.000 | 0.000 | 0 → 0 | 2 → 1 | 18% → 18% | 7 → 6 | 7 | 5 → 5 | 0.012 | -0.573 |
| Jogador 8 | 3-3 | 3 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 18% → 18% | 6 → 11 | 2 | 5 → 5 | -0.020 | -0.942 |
| Jogador 8 | 3-4 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 11 → 19 | 0 | 5 → 6 | 0.000 | 0.000 |
| Jogador 8 | 3-5 | 5 | 12.000 | -2.000 | 0 → 1 | 1 → 2 | 18% → 21% | 19 → 23 | 5 | 6 → 6 | -0.003 | -0.537 |
| Jogador 8 | 3-6 | 2 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 21% → 21% | 23 → 31 | 0 | 6 → 6 | 0.000 | 1.358 |
| Jogador 8 | 3-7 | 3 | 0.000 | 2.000 | 1 → 1 | 2 → 2 | 21% → 21% | 31 → 38 | 1 | 6 → 6 | -0.020 | 0.000 |
| Jogador 8 | 4-1 | 3 | 0.000 | 0.000 | 1 → 1 | 2 → 1 | 21% → 21% | 38 → 45 | 3 | 6 → 6 | 0.020 | 0.950 |
| Jogador 8 | 4-2 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 21% → 21% | 45 → 54 | 0 | 6 → 6 | 0.000 | -1.450 |
| Jogador 8 | 4-3 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 21% → 21% | 54 → 65 | 0 | 6 → 6 | 0.000 | -1.400 |
| Jogador 8 | 4-4 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 21% → 21% | 65 → 76 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 4-5 | 3 | 0.000 | 4.000 | 1 → 1 | 1 → 2 | 21% → 21% | 76 → 85 | 2 | 6 → 6 | -0.020 | 0.000 |
| Jogador 8 | 4-6 | 3 | -26.000 | -36.000 | 1 → 0 | 2 → 0 | 21% → 0% | 85 → 82 | 3 | 6 → 6 | 0.110 | -0.983 |
| Jogador 8 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 82 → 82 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 82 → 82 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 82 → 82 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 82 → 82 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 82 → 82 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 82 → 82 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 82 → 82 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 82 → 82 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 82 → 82 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 82 → 82 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 82 → 82 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 82 → 82 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 82 → 82 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 6-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 82 → 82 | 0 | 6 → 6 | 0.000 | 0.000 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 4, COMPOSITION_COMPATIBILITY: 13, IMMEDIATE_UPGRADE: 3, PAIR_POTENTIAL: 7; mudanças de composição: 0; posicionamento melhorou em 10 ações e piorou em 18.
- Jogador 8 — estado final: ouro 82, nível 6, vida 0.0, colocação 6.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Revertidas ≤1 ação | ≤2 ações | ≤4 ações | Ouro perdido | Upgrades | Vendas core/par | Valor médio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 17 | 7 | 0 | 0 | 1 | 0 | 0 | 5 | 4.8212 |
| Jogador 2 | 30 | 9 | 2 | 2 | 3 | 0 | 3 | 3 | 3.5052 |
| Jogador 3 | 23 | 1 | 0 | 0 | 0 | 0 | 4 | 0 | 5.4086 |
| Jogador 4 | 24 | 4 | 1 | 1 | 1 | 0 | 3 | 1 | 5.3824 |
| Jogador 5 | 19 | 4 | 1 | 2 | 2 | 0 | 2 | 0 | 3.1062 |
| Jogador 6 | 30 | 12 | 1 | 1 | 2 | 0 | 2 | 4 | 3.0019 |
| Jogador 7 | 26 | 3 | 0 | 0 | 0 | 0 | 4 | 1 | 4.192 |
| Jogador 8 | 27 | 8 | 3 | 4 | 4 | 0 | 3 | 2 | 4.0012 |

As classificações detalhadas e cada sequência correlacionada ficam em audit_report.json.
Uma venda sem compra correspondente na janela é UNKNOWN; sequências ambíguas não são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| HIGH | Jogador 1 | 1-4 | 32 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 1 | 1-4 | 33 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 1 | 2-1 | 46 | PURCHASE_REVERSED | Compra de DA_18_Varus desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 1 | 3-4 | 144 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 1 | 3-4 | 145 | SOLD_CORE_UNIT | Venda de 'DA_Vi18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 1 | 4-1 | 188 | SOLD_CORE_UNIT | Venda de 'DA_Vi18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 1 | 6-6 | 371 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Lux_Primal' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 1 | 6-6 | 371 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Diana' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 1 | 6-6 | 371 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Brambleback18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 2 | 1-4 | 34 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 2 | 1-4 | 37 | SOLD_CORE_UNIT | Venda de 'DA_18_Veigar' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 2 | 1-4 | 37 | PURCHASE_REVERSED | Compra de DA_18_Veigar desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 2-1 | 46 | PURCHASE_REVERSED | Compra de DA_18_Yorick desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 2 | 2-1 | 48 | SOLD_CORE_UNIT | Venda de 'DA_18_Leona' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 2 | 2-2 | 53 | PURCHASE_REVERSED | Compra de DA_18_Veigar desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 3 | 5-4 | 281 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Scuttlecrab18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 3 | 5-4 | 281 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Tristana' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 3 | 5-4 | 281 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_CrimsonRaptor18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 4 | 1-3 | 26 | PURCHASE_REVERSED | Compra de DA_Karma18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 4 | 2-3 | 63 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 4 | 4-4 | 213 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Gromp18_AP' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 4 | 4-4 | 213 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Akali_AD' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 4 | 4-4 | 213 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Yorick' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 5 | 2-1 | 44 | PURCHASE_REVERSED | Compra de DA_18_Xayah desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-1 | 46 | PURCHASE_REVERSED | Compra de DA_18_Veigar desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 5-2 | 261 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Elise' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 5 | 5-2 | 261 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Camille' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 5 | 5-2 | 261 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Tristana' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 6 | 2-1 | 43 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 6 | 2-1 | 45 | PURCHASE_REVERSED | Compra de DA_Karma18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 6 | 2-3 | 67 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 6 | 2-3 | 69 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 6 | 2-4 | 75 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Gromp18_AP' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 6 | 2-4 | 75 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 6 | 4-6 | 231 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Rammus' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 6 | 4-6 | 231 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Teemo' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 6 | 4-6 | 231 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Tristana' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 7 | 4-2 | 191 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 8 | 1-3 | 24 | PURCHASE_REVERSED | Compra de DA_Karma18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 8 | 1-3 | 29 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 8 | 1-3 | 29 | PURCHASE_REVERSED | Compra de DA_18_Yorick desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 1-4 | 32 | PURCHASE_REVERSED | Compra de DA_18_RekSai desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 1-4 | 34 | PURCHASE_REVERSED | Compra de DA_18_Camille desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 8 | 3-1 | 115 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 8 | 4-7 | 241 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_MasterYi_AD' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 8 | 4-7 | 241 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Cassiopeia' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 8 | 4-7 | 241 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Veigar' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- O JSON estruturado é a fonte primária para estado de decisão, máscaras, política e recompensas; .tft é analisado apenas para jogadores sem sidecar JSON.- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
