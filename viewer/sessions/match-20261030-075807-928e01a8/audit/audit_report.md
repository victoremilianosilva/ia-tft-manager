# Auditoria da partida TFT

- Arquivos lidos: **8**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Entradas JSON analisadas: **3876**
- Achados: **53**
- CRITICAL: 0 | HIGH: 19 | MEDIUM: 34 | LOW: 0

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 166 | 166 | 166 | 0 | 164 | 0 | 166 | 166 | 162 | 28/14 |
| Jogador 2 | 133 | 133 | 133 | 0 | 133 | 0 | 133 | 133 | 120 | 33/20 |
| Jogador 3 | 124 | 124 | 124 | 0 | 123 | 0 | 124 | 124 | 117 | 16/2 |
| Jogador 4 | 150 | 150 | 150 | 0 | 146 | 0 | 150 | 150 | 150 | 14/5 |
| Jogador 5 | 113 | 113 | 113 | 0 | 113 | 0 | 113 | 113 | 100 | 24/10 |
| Jogador 6 | 169 | 169 | 169 | 0 | 165 | 0 | 169 | 169 | 169 | 33/21 |
| Jogador 7 | 101 | 101 | 101 | 0 | 100 | 0 | 101 | 101 | 98 | 21/6 |
| Jogador 8 | 135 | 135 | 135 | 0 | 131 | 0 | 135 | 135 | 134 | 17/6 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 8 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Ornn | MOVE_BENCH, SELL, PASS | True | True | 0.24171799421310425 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 10 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3013512194156647 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 11 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4440630376338959 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.9705569744110107 | 0.0 | 0.0 | +679fe281-674a-438b-bdcf-57229a283d44 / -— |
| Jogador 1 | 1-2 | 13 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5240298509597778 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 14 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.10086178034543991 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 16 | REROLL | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 17 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 25 | REROLL | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 26 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 34 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4455147087574005 | 0.0 | 0.0 | +70d8224e-5996-4629-b4f6-761ef5f01525 / -— |
| Jogador 1 | 2-1 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22905942797660828 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 36 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5241521596908569 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 37 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Shen | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 38 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Shen | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.12929771840572357 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 39 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Shen | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.041490811854600906 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 40 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 42 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4646205008029938 | 0.0 | 0.0 | +9bb3da58-fe6f-4298-8529-859cceb4857e / -— |
| Jogador 1 | 2-2 | 43 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07624980062246323 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 44 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45690590143203735 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 45 | SELL | STABILIZE | 100.0 | 4 | 6 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7408513426780701 | 0.0 | 0.0 | +— / -2718f555-b782-4fea-a68f-31395ad34232 |
| Jogador 1 | 2-2 | 46 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 47 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 52 | BUY_XP | STABILIZE | 100.0 | 4 | 10 | 1 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.05299999937415123 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 53 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9677067995071411 | 0.0 | 0.0 | +2ef60eed-d073-41a6-adec-4466c673b313 / -— |
| Jogador 1 | 2-3 | 54 | BUY | STABILIZE | 100.0 | 5 | 4 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07430631667375565 | 0.0 | 0.0 | +37192022-05ce-4f51-b5d3-353242887fe1 / -— |
| Jogador 1 | 2-3 | 55 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5085695385932922 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 56 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49776923656463623 | 0.0 | 0.0 | +— / -37192022-05ce-4f51-b5d3-353242887fe1 |
| Jogador 1 | 2-3 | 57 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 58 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_KogMaw18_AD | MOVE_BOARD, PASS | True | True | -0.12930524349212646 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 59 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_KogMaw18_AD | MOVE_BOARD, PASS | True | True | 0.1798628270626068 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 60 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_KogMaw18_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 62 | BUY | STABILIZE | 100.0 | 5 | 7 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9780924320220947 | 0.0 | 0.0 | +18934be2-4988-4f62-9f62-07ba151231f2 / -— |
| Jogador 1 | 2-4 | 63 | SELL | STABILIZE | 100.0 | 5 | 6 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.028092384338379 | 0.0 | 0.0 | +— / -18934be2-4988-4f62-9f62-07ba151231f2 |
| Jogador 1 | 2-4 | 64 | BUY_XP | STABILIZE | 100.0 | 5 | 7 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 65 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 3 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.15572163462638855 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 66 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 3 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 67 | PASS | STABILIZE | 100.0 | 5 | 3 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 72 | BUY_XP | STABILIZE | 100.0 | 5 | 9 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 73 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03200000151991844 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 74 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 1 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, MOVE_BOARD, PASS | True | True | 0.09808357805013657 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 75 | PASS | STABILIZE | 100.0 | 6 | 1 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 82 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3660585284233093 | 0.0 | 0.0 | +0067f61f-504d-440a-b071-de7f18886e3d / -— |
| Jogador 1 | 2-6 | 83 | BUY | STABILIZE | 95.0 | 6 | 3 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07989849150180817 | 0.0 | 0.0 | +c96b6357-8134-4e68-af0b-f5695a815597 / -— |
| Jogador 1 | 2-6 | 84 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 1 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43009093403816223 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 85 | SELL | STABILIZE | 95.0 | 6 | 1 | 0 | 24.0 | —/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1892419159412384 | 0.0 | 0.0 | +— / -c96b6357-8134-4e68-af0b-f5695a815597 |
| Jogador 1 | 2-6 | 86 | PASS | STABILIZE | 95.0 | 6 | 3 | 0 | 24.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 90 | BUY_XP | STABILIZE | 95.0 | 6 | 9 | 0 | 24.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 91 | BUY_XP | STABILIZE | 95.0 | 6 | 5 | 0 | 24.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 92 | PASS | STABILIZE | 95.0 | 6 | 1 | 0 | 24.0 | —/DA_KogMaw18_AD | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 94 | BUY_XP | STABILIZE | 95.0 | 6 | 6 | 0 | 24.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 95 | PASS | STABILIZE | 95.0 | 6 | 2 | 0 | 24.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 102 | BUY_XP | STABILIZE | 95.0 | 6 | 9 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 103 | BUY_XP | STABILIZE | 95.0 | 6 | 5 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 104 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 1 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, MOVE_BOARD, PASS | True | True | 0.041490811854600906 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 105 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 1 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, MOVE_BOARD, PASS | True | True | -0.3283054232597351 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 106 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 1 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, MOVE_BOARD, PASS | True | True | 0.05659887194633484 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 107 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 1 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, MOVE_BOARD, PASS | True | True | 0.06348513811826706 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 108 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 1 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 109 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 1 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, MOVE_BOARD, PASS | True | True | 0.01040505338460207 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 110 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 1 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, MOVE_BOARD, PASS | True | True | 0.17994467914104462 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 112 | BUY_XP | STABILIZE | 95.0 | 6 | 8 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06199999898672104 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 113 | MOVE_BOARD | STABILIZE | 95.0 | 7 | 4 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.28365546464920044 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 114 | MOVE_BOARD | STABILIZE | 95.0 | 7 | 4 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.022793645039200783 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 115 | MOVE_BOARD | STABILIZE | 95.0 | 7 | 4 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.02891405299305916 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 116 | MOVE_BOARD | STABILIZE | 95.0 | 7 | 4 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10453628748655319 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 117 | MOVE_BOARD | STABILIZE | 95.0 | 7 | 4 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.32547059655189514 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 118 | PASS | STABILIZE | 95.0 | 7 | 4 | 0 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 120 | BUY | STABILIZE | 95.0 | 7 | 11 | 1 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19488604366779327 | 0.0 | 0.0 | +c5a8f36d-74b1-4944-a3db-bfb601a89b59 / -— |
| Jogador 1 | 3-5 | 122 | BUY | STABILIZE | 95.0 | 7 | 13 | 1 | 32.0 | Adaptador/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7437052726745605 | 0.0 | 0.0 | +f1efd93e-603e-437a-a598-cafd605ddea8 / -— |
| Jogador 1 | 3-5 | 123 | MOVE_BOARD | STABILIZE | 95.0 | 7 | 10 | 1 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03721294552087784 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 124 | MOVE_BOARD | STABILIZE | 95.0 | 7 | 10 | 1 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008921255357563496 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 125 | MOVE_BOARD | STABILIZE | 95.0 | 7 | 10 | 1 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 127 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 16 | 1 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14587189257144928 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 128 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 16 | 1 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001785655738785863 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 129 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 16 | 1 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 130 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 16 | 1 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008921255357563496 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 132 | BUY | STABILIZE | 84.0 | 7 | 23 | 2 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7525511980056763 | 0.0 | 0.0 | +5af104f2-7959-4ca5-91a9-7d44494532ea / -— |
| Jogador 1 | 3-7 | 133 | MOVE_BENCH | STABILIZE | 84.0 | 7 | 20 | 2 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 134 | MOVE_BENCH | STABILIZE | 84.0 | 7 | 20 | 2 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07064858824014664 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 135 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 20 | 2 | 34.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.042065247893333435 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 136 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 20 | 2 | 34.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 137 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 20 | 2 | 34.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27581727504730225 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 138 | PASS | STABILIZE | 84.0 | 7 | 20 | 2 | 34.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007499999832361937 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 141 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 27 | 2 | 34.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0035709599032998085 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 142 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 27 | 2 | 34.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.16336657106876373 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 143 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 27 | 2 | 34.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.16057012975215912 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 144 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 27 | 2 | 34.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10971488058567047 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 145 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 27 | 2 | 34.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.14954893290996552 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 146 | PASS | STABILIZE | 84.0 | 7 | 27 | 2 | 34.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 151 | CRAFT_AND_EQUIP | FAST8 | 73.0 | 7 | 34 | 3 | 34.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.19030725955963135 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 152 | MOVE_BOARD | FAST8 | 73.0 | 7 | 34 | 3 | 34.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1756746470928192 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 153 | MOVE_BOARD | FAST8 | 73.0 | 7 | 34 | 3 | 34.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 154 | MOVE_BOARD | FAST8 | 73.0 | 7 | 34 | 3 | 34.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32172176241874695 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 155 | PASS | FAST8 | 73.0 | 7 | 34 | 3 | 34.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 161 | BUY | FAST8 | 61.0 | 7 | 43 | 4 | 34.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21877433359622955 | 0.0 | 0.0 | +c8706680-2712-4914-b6c0-59bf92a2796d / -— |
| Jogador 1 | 4-3 | 162 | REROLL | FAST8 | 61.0 | 7 | 39 | 3 | 34.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08900000154972076 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 163 | REROLL | FAST8 | 61.0 | 7 | 37 | 3 | 34.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 164 | BUY | FAST8 | 61.0 | 7 | 35 | 3 | 34.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8388761281967163 | 0.0 | 0.0 | +d30c92eb-1279-4532-b763-7c30826c8430 / -9bb3da58-fe6f-4298-8529-859cceb4857e,f1efd93e-603e-437a-a598-cafd605ddea8 |
| Jogador 1 | 4-3 | 165 | MOVE_BENCH | STABILIZE | 61.0 | 7 | 32 | 3 | 22.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05304485186934471 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 166 | MOVE_BOARD | FAST8 | 61.0 | 7 | 32 | 3 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.036966722458601 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 167 | MOVE_BOARD | FAST8 | 61.0 | 7 | 32 | 3 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11919979751110077 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 168 | MOVE_BOARD | FAST8 | 61.0 | 7 | 32 | 3 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07784928381443024 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 169 | MOVE_BENCH | FAST8 | 61.0 | 7 | 32 | 3 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5092079639434814 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 171 | BUY | FAST8 | 50.0 | 7 | 41 | 4 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24345539510250092 | 0.0 | 0.0 | +c2bf43be-e6e1-47ed-bcb4-606e37f26671 / -— |
| Jogador 1 | 4-4 | 172 | REROLL | FAST8 | 50.0 | 7 | 38 | 3 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 173 | MOVE_BOARD | FAST8 | 50.0 | 7 | 36 | 3 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 174 | MOVE_BOARD | FAST8 | 50.0 | 7 | 36 | 3 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 175 | PASS | FAST8 | 50.0 | 7 | 36 | 3 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 181 | BUY | FAST8 | 50.0 | 7 | 45 | 4 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.039922717958688736 | 0.0 | 0.0 | +de590b22-a48c-4c78-a2f3-6ef39ce948fe / -— |
| Jogador 1 | 4-5 | 182 | MOVE_BOARD | FAST8 | 50.0 | 7 | 41 | 4 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 183 | MOVE_BOARD | FAST8 | 50.0 | 7 | 41 | 4 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0230864305049181 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 184 | MOVE_BOARD | FAST8 | 50.0 | 7 | 41 | 4 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 185 | MOVE_BOARD | FAST8 | 50.0 | 7 | 41 | 4 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05690978839993477 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 186 | REROLL | FAST8 | 50.0 | 7 | 41 | 4 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16899999976158142 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 187 | REROLL | FAST8 | 50.0 | 7 | 39 | 3 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08900000154972076 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 188 | REROLL | FAST8 | 50.0 | 7 | 37 | 3 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 189 | REROLL | FAST8 | 50.0 | 7 | 35 | 3 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08900000154972076 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 191 | BUY | FAST8 | 50.0 | 7 | 42 | 4 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7967523336410522 | 0.0 | 0.0 | +6fe382fd-86c3-42ec-abb7-fb52c7a19c62 / -0067f61f-504d-440a-b071-de7f18886e3d,5af104f2-7959-4ca5-91a9-7d44494532ea |
| Jogador 1 | 4-6 | 192 | BUY | STABILIZE | 50.0 | 7 | 39 | 3 | 20.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.904384434223175 | 0.0 | 0.0 | +19e8f3ef-c3a6-459e-bf05-a53f742ba05d / -2ef60eed-d073-41a6-adec-4466c673b313,70d8224e-5996-4629-b4f6-761ef5f01525 |
| Jogador 1 | 4-6 | 193 | BUY | STABILIZE | 50.0 | 7 | 37 | 3 | 12.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16659922897815704 | 0.0 | 0.0 | +ac0e7aab-09c1-4762-8c74-09fedabcd769 / -— |
| Jogador 1 | 4-6 | 194 | BUY | STABILIZE | 50.0 | 7 | 34 | 3 | 12.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40351471304893494 | 0.0 | 0.0 | +699b59c7-1237-472b-a4d1-18a35e88b7c2 / -— |
| Jogador 1 | 4-6 | 195 | MOVE_BENCH | STABILIZE | 50.0 | 7 | 31 | 3 | 12.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.402023047208786 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 196 | MOVE_BENCH | STABILIZE | 50.0 | 7 | 31 | 3 | 18.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.281316876411438 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 198 | BUY | STABILIZE | 37.0 | 7 | 39 | 3 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8742273449897766 | 0.0 | 0.0 | +faad2b99-a44b-4552-909b-3805cb020272 / -699b59c7-1237-472b-a4d1-18a35e88b7c2,ac0e7aab-09c1-4762-8c74-09fedabcd769 |
| Jogador 1 | 4-7 | 199 | BUY | STABILIZE | 37.0 | 7 | 36 | 3 | 18.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4244707524776459 | 0.0 | 0.0 | +2adb37ce-c46e-4c3a-a715-443bdb688103 / -— |
| Jogador 1 | 4-7 | 200 | BUY | STABILIZE | 37.0 | 7 | 32 | 3 | 18.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27718955278396606 | 0.0 | 0.0 | +45bb5798-7b34-48ad-b40b-a871e20a4e62 / -— |
| Jogador 1 | 5-1 | 202 | EQUIP_FROM_INVENTORY | STABILIZE | 37.0 | 7 | 36 | 3 | 30.0 | Adaptador/DA_KogMaw18_AD | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 203 | BUY | STABILIZE | 37.0 | 7 | 36 | 3 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8041087985038757 | 0.0 | 0.0 | +f8177556-bc54-4860-a7cf-90a94b0e6c96 / -— |
| Jogador 1 | 5-1 | 204 | REROLL | STABILIZE | 37.0 | 7 | 32 | 3 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 205 | BUY | STABILIZE | 37.0 | 7 | 30 | 3 | 30.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7513619065284729 | 0.0 | 0.0 | +d63a72f0-dcab-454e-afad-17ddc66b5b3d / -— |
| Jogador 1 | 5-1 | 206 | REROLL | STABILIZE | 37.0 | 7 | 27 | 2 | 30.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 207 | REROLL | STABILIZE | 37.0 | 7 | 25 | 2 | 30.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 208 | REROLL | STABILIZE | 37.0 | 7 | 23 | 2 | 30.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 209 | REROLL | STABILIZE | 37.0 | 7 | 21 | 2 | 30.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 210 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 19 | 1 | 30.0 | Adaptador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2499537318944931 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 212 | REROLL | STABILIZE | 24.0 | 7 | 26 | 2 | 38.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 213 | REROLL | STABILIZE | 24.0 | 7 | 24 | 2 | 38.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 214 | REROLL | STABILIZE | 24.0 | 7 | 22 | 2 | 38.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 215 | REROLL | STABILIZE | 24.0 | 7 | 20 | 2 | 38.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 216 | REROLL | STABILIZE | 24.0 | 7 | 18 | 1 | 38.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 217 | REROLL | STABILIZE | 24.0 | 7 | 16 | 1 | 38.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 218 | REROLL | STABILIZE | 24.0 | 7 | 14 | 1 | 38.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 219 | REROLL | STABILIZE | 24.0 | 7 | 12 | 1 | 38.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 220 | MOVE_BENCH | STABILIZE | 24.0 | 7 | 10 | 1 | 38.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49615272879600525 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 222 | REROLL | STABILIZE | 24.0 | 7 | 17 | 1 | 46.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 223 | REROLL | STABILIZE | 24.0 | 7 | 15 | 1 | 46.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 224 | REROLL | STABILIZE | 24.0 | 7 | 13 | 1 | 46.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 225 | REROLL | STABILIZE | 24.0 | 7 | 11 | 1 | 46.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 226 | REROLL | STABILIZE | 24.0 | 7 | 9 | 0 | 46.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 227 | REROLL | STABILIZE | 24.0 | 7 | 7 | 0 | 46.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 228 | REROLL | STABILIZE | 24.0 | 7 | 5 | 0 | 46.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 229 | REROLL | STABILIZE | 24.0 | 7 | 3 | 0 | 46.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 230 | MOVE_BOARD | STABILIZE | 24.0 | 7 | 1 | 0 | 46.0 | Adaptador/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15499961376190186 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 232 | BUY | ALL_IN | 7.0 | 7 | 6 | 0 | 46.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8239747285842896 | 0.0 | 0.0 | +6b9809a4-494f-4f99-b10c-1675d1fabc17 / -c2bf43be-e6e1-47ed-bcb4-606e37f26671,d63a72f0-dcab-454e-afad-17ddc66b5b3d |
| Jogador 1 | 5-4 | 233 | BUY | ALL_IN | 7.0 | 7 | 3 | 0 | 40.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27399611473083496 | 0.0 | 0.0 | +459e41e4-1737-4721-af77-b028c5288f35 / -— |
| Jogador 1 | 5-4 | 234 | PASS | ALL_IN | 7.0 | 7 | 0 | 0 | 40.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 240 | MOVE_BENCH | ALL_IN | 7.0 | 7 | 0 | 0 | 40.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5427453517913818 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 242 | BUY | ALL_IN | 7.0 | 7 | 5 | 0 | 52.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7339709997177124 | 0.0 | 0.0 | +ba36a983-5b13-4f69-871b-e7eac4420b98 / -— |
| Jogador 1 | 5-5 | 243 | REROLL | ALL_IN | 7.0 | 7 | 2 | 0 | 52.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 244 | PASS | ALL_IN | 7.0 | 7 | 0 | 0 | 52.0 | Adaptador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 252 | PASS | ALL_IN | 0.0 | 7 | 0 | 0 | 0.0 | Adaptador/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 262 | PASS | ALL_IN | 0.0 | 7 | 0 | 0 | 0.0 | Adaptador/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 271 | PASS | ALL_IN | 0.0 | 7 | 0 | 0 | 0.0 | Adaptador/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 281 | PASS | ALL_IN | 0.0 | 7 | 0 | 0 | 0.0 | Adaptador/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.010384615510702133 | 0.0 | 0.0 | +— / -fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.22450661659240723 | 0.0 | 0.0 | +292ef825-d326-4dd8-9c42-c47cfc62116f / -— |
| Jogador 2 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.5933380722999573 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 10 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9709054827690125 | 0.0 | 0.0 | +94ede66e-59bc-4c41-aabf-f64372e20f9a / -— |
| Jogador 2 | 1-2 | 11 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11205994337797165 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 13 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 16 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.12844476103782654 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 17 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 25 | BUY | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1178797483444214 | 0.0 | 0.0 | +5ead8548-7453-4fa1-856e-674995576a48 / -292ef825-d326-4dd8-9c42-c47cfc62116f,94ede66e-59bc-4c41-aabf-f64372e20f9a |
| Jogador 2 | 1-4 | 26 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 5 | 0 | 0.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, SELL, PASS | True | True | 0.5940914154052734 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 27 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1537153720855713 | 0.0 | 0.0 | +ab6084b0-65df-4a70-8591-687b320d98b6 / -— |
| Jogador 2 | 1-4 | 28 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0026228427886963 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5990372896194458 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.17199330031871796 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.001247938722372055 | 0.0 | 0.0 | +e0d7b71a-2c4b-4907-b11d-4c25d39fe3d0 / -— |
| Jogador 2 | 1-4 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4148951768875122 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 34 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.35063663125038147 | 0.0 | 0.0 | +9819422b-1f51-47b5-89b7-9d6e906ddff2 / -— |
| Jogador 2 | 2-1 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3871501684188843 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 36 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 37 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1618809700012207 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 38 | REROLL | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 39 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 16.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 42 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 43 | REROLL | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 44 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 16.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 52 | BUY | STABILIZE | 94.0 | 4 | 6 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2927978038787842 | 0.0 | 0.0 | +0547b747-1e37-49ba-a447-67c526a8cd50 / -— |
| Jogador 2 | 2-3 | 53 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08069716393947601 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 54 | SELL | STABILIZE | 94.0 | 4 | 3 | 0 | 18.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0259399451315403 | 0.0 | 0.0 | +— / -ab6084b0-65df-4a70-8591-687b320d98b6 |
| Jogador 2 | 2-3 | 55 | BUY_XP | STABILIZE | 94.0 | 4 | 5 | 0 | 18.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.052000001072883606 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 56 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.03786883130669594 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 57 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 58 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.11892727017402649 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 59 | BUY | STABILIZE | 94.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | -0.026335537433624268 | 0.0 | 0.0 | +3ffefe44-52ff-4118-83fb-ae8237b6caa0 / -— |
| Jogador 2 | 2-3 | 60 | SELL | STABILIZE | 94.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1786923110485077 | 0.0 | 0.0 | +— / -3ffefe44-52ff-4118-83fb-ae8237b6caa0 |
| Jogador 2 | 2-4 | 62 | BUY | STABILIZE | 87.0 | 5 | 7 | 0 | 18.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3765932321548462 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 2 | 2-4 | 63 | MOVE_BENCH | STABILIZE | 87.0 | 5 | 4 | 0 | 18.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44361934065818787 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 64 | MOVE_BOARD | STABILIZE | 87.0 | 5 | 4 | 0 | 24.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.07262324541807175 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 65 | BUY_XP | STABILIZE | 87.0 | 5 | 4 | 0 | 24.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 66 | MOVE_BOARD | STABILIZE | 87.0 | 5 | 0 | 0 | 24.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.14408981800079346 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 67 | MOVE_BOARD | STABILIZE | 87.0 | 5 | 0 | 0 | 24.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.06839081645011902 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 68 | MOVE_BOARD | STABILIZE | 87.0 | 5 | 0 | 0 | 24.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | -0.3302437663078308 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 69 | MOVE_BOARD | STABILIZE | 87.0 | 5 | 0 | 0 | 24.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.08612926304340363 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 70 | MOVE_BOARD | STABILIZE | 87.0 | 5 | 0 | 0 | 24.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.17965929210186005 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 72 | REROLL | STABILIZE | 87.0 | 5 | 6 | 0 | 24.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 73 | BUY | STABILIZE | 87.0 | 5 | 4 | 0 | 24.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.5209535956382751 | 0.0 | 0.0 | +a9f7f52e-6619-4669-9b8a-390b99fd73d8 / -— |
| Jogador 2 | 2-5 | 74 | SELL | STABILIZE | 87.0 | 5 | 3 | 0 | 24.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6054986715316772 | 0.0 | 0.0 | +— / -a9f7f52e-6619-4669-9b8a-390b99fd73d8 |
| Jogador 2 | 2-5 | 75 | BUY | STABILIZE | 87.0 | 5 | 4 | 0 | 24.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.38212770223617554 | 0.0 | 0.0 | +19cba1be-95ae-4cf0-a600-0c5eb8d081b0 / -— |
| Jogador 2 | 2-5 | 76 | SELL | STABILIZE | 87.0 | 5 | 1 | 0 | 24.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4321277141571045 | 0.0 | 0.0 | +— / -19cba1be-95ae-4cf0-a600-0c5eb8d081b0 |
| Jogador 2 | 2-5 | 77 | BUY_XP | STABILIZE | 87.0 | 5 | 4 | 0 | 24.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 78 | PASS | STABILIZE | 87.0 | 5 | 0 | 0 | 24.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 82 | BUY_XP | STABILIZE | 87.0 | 5 | 6 | 0 | 24.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03200000151991844 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 83 | BUY | STABILIZE | 87.0 | 6 | 2 | 0 | 24.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.5210369825363159 | 0.0 | 0.0 | +60c8a84d-7243-462c-a452-5901135c78b8 / -— |
| Jogador 2 | 2-6 | 84 | SELL | STABILIZE | 87.0 | 6 | 1 | 0 | 24.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6055964827537537 | 0.0 | 0.0 | +— / -60c8a84d-7243-462c-a452-5901135c78b8 |
| Jogador 2 | 2-6 | 85 | BUY | STABILIZE | 87.0 | 6 | 2 | 0 | 24.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3775476813316345 | 0.0 | 0.0 | +79786887-d318-4836-b2f0-c0f03e86cbe5 / -— |
| Jogador 2 | 2-6 | 86 | SELL | STABILIZE | 87.0 | 6 | 1 | 0 | 24.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4275476932525635 | 0.0 | 0.0 | +— / -79786887-d318-4836-b2f0-c0f03e86cbe5 |
| Jogador 2 | 2-6 | 87 | MOVE_BOARD | STABILIZE | 87.0 | 6 | 2 | 0 | 24.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 88 | MOVE_BOARD | STABILIZE | 87.0 | 6 | 2 | 0 | 24.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.14408981800079346 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 90 | BUY | STABILIZE | 82.0 | 6 | 7 | 0 | 24.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9672713875770569 | 0.0 | 0.0 | +3acb90a6-bcf2-41d1-848f-f2aec19a2163 / -— |
| Jogador 2 | 2-7 | 91 | BUY | STABILIZE | 82.0 | 6 | 4 | 0 | 24.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.401954710483551 | 0.0 | 0.0 | +19cf270e-27a1-4d3c-bef7-0b1af400d07c / -— |
| Jogador 2 | 2-7 | 92 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 0 | 0 | 24.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4654599726200104 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 94 | SELL | STABILIZE | 82.0 | 6 | 5 | 0 | 30.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5385384559631348 | 0.0 | 0.0 | +— / -19cf270e-27a1-4d3c-bef7-0b1af400d07c |
| Jogador 2 | 3-1 | 95 | MOVE_BOARD | STABILIZE | 82.0 | 6 | 9 | 0 | 30.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.2920812964439392 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 96 | MOVE_BOARD | STABILIZE | 82.0 | 6 | 9 | 0 | 30.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.11919979751110077 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 97 | MOVE_BOARD | STABILIZE | 82.0 | 6 | 9 | 0 | 30.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 98 | MOVE_BOARD | STABILIZE | 82.0 | 6 | 9 | 0 | 30.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.26564493775367737 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 99 | PASS | STABILIZE | 82.0 | 6 | 9 | 0 | 30.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 102 | BUY | STABILIZE | 72.0 | 6 | 15 | 1 | 30.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2796606421470642 | 0.0 | 0.0 | +e8b0d22c-35bc-459e-a90c-7db13fcbe34f / -— |
| Jogador 2 | 3-2 | 103 | SELL | STABILIZE | 72.0 | 6 | 12 | 1 | 30.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.545769214630127 | 0.0 | 0.0 | +— / -e8b0d22c-35bc-459e-a90c-7db13fcbe34f |
| Jogador 2 | 3-2 | 104 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 15 | 1 | 30.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 105 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 15 | 1 | 30.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.2862316966056824 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 106 | PASS | STABILIZE | 72.0 | 6 | 15 | 1 | 30.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 112 | BUY | STABILIZE | 62.0 | 6 | 22 | 2 | 30.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.32406851649284363 | 0.0 | 0.0 | +d63ebe7f-9313-42c4-afa2-a6078130f235 / -— |
| Jogador 2 | 3-3 | 113 | SELL | STABILIZE | 62.0 | 6 | 19 | 1 | 30.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4267862141132355 | 0.0 | 0.0 | +— / -d63ebe7f-9313-42c4-afa2-a6078130f235 |
| Jogador 2 | 3-3 | 114 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 22 | 2 | 30.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17990650236606598 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 115 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 22 | 2 | 30.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.3413776457309723 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 116 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 22 | 2 | 30.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 117 | PASS | STABILIZE | 62.0 | 6 | 22 | 2 | 30.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.007499999832361937 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 120 | BUY | SLOWROLL | 50.0 | 6 | 30 | 3 | 30.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7229900360107422 | 0.0 | 0.0 | +65a6d68c-90ae-4e31-8bbc-82e8ec75b3de / -0547b747-1e37-49ba-a447-67c526a8cd50,3acb90a6-bcf2-41d1-848f-f2aec19a2163 |
| Jogador 2 | 3-5 | 122 | BUY | SLOWROLL | 50.0 | 6 | 35 | 3 | 30.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.2896031141281128 | 0.0 | 0.0 | +daad4576-7a5d-4154-9b81-963d092a7207 / -— |
| Jogador 2 | 3-5 | 123 | BUY | SLOWROLL | 50.0 | 6 | 31 | 3 | 30.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16533228754997253 | 0.0 | 0.0 | +b75c9bc5-9bc7-465a-a97c-59156e5c482d / -— |
| Jogador 2 | 3-5 | 124 | MOVE_BOARD | STABILIZE | 50.0 | 6 | 29 | 2 | 30.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15071353316307068 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 125 | MOVE_BENCH | STABILIZE | 50.0 | 6 | 29 | 2 | 30.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3571118414402008 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 127 | REROLL | STABILIZE | 37.0 | 6 | 38 | 3 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 128 | BUY | STABILIZE | 37.0 | 6 | 36 | 3 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33887070417404175 | 0.0 | 0.0 | +1be0cdcc-ee10-44dc-ad1b-de9b53b25164 / -— |
| Jogador 2 | 3-6 | 129 | REROLL | STABILIZE | 37.0 | 6 | 33 | 3 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 130 | REROLL | STABILIZE | 37.0 | 6 | 31 | 3 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 132 | REROLL | STABILIZE | 26.0 | 6 | 39 | 3 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 133 | REROLL | STABILIZE | 26.0 | 6 | 37 | 3 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 134 | REROLL | STABILIZE | 26.0 | 6 | 35 | 3 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 135 | BUY | STABILIZE | 26.0 | 6 | 33 | 3 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8360705971717834 | 0.0 | 0.0 | +235510e3-df54-4de9-9bcf-bff6d47e364a / -— |
| Jogador 2 | 3-7 | 136 | REROLL | STABILIZE | 26.0 | 6 | 30 | 3 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 137 | REROLL | STABILIZE | 26.0 | 6 | 28 | 2 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 138 | REROLL | STABILIZE | 26.0 | 6 | 26 | 2 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 139 | REROLL | STABILIZE | 26.0 | 6 | 24 | 2 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 141 | REROLL | STABILIZE | 26.0 | 6 | 32 | 3 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 142 | REROLL | STABILIZE | 26.0 | 6 | 30 | 3 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 143 | REROLL | STABILIZE | 26.0 | 6 | 28 | 2 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 144 | REROLL | STABILIZE | 26.0 | 6 | 26 | 2 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 145 | BUY | STABILIZE | 26.0 | 6 | 24 | 2 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8800358772277832 | 0.0 | 0.0 | +98b72340-a402-45bc-9493-71263e3168d6 / -1be0cdcc-ee10-44dc-ad1b-de9b53b25164,235510e3-df54-4de9-9bcf-bff6d47e364a |
| Jogador 2 | 4-1 | 146 | BUY | STABILIZE | 26.0 | 6 | 21 | 2 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25003525614738464 | 0.0 | 0.0 | +cba152f4-af54-4d82-a35d-67aa165174be / -— |
| Jogador 2 | 4-1 | 147 | REROLL | STABILIZE | 26.0 | 6 | 18 | 1 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 148 | REROLL | STABILIZE | 26.0 | 6 | 16 | 1 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 149 | BUY | STABILIZE | 26.0 | 6 | 14 | 1 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7439994812011719 | 0.0 | 0.0 | +b0c1aba5-b1bd-48df-abec-19efa8e49d6d / -— |
| Jogador 2 | 4-2 | 151 | BUY | ALL_IN | 14.0 | 6 | 20 | 2 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8049267530441284 | 0.0 | 0.0 | +6722b147-c2a7-4fd0-a943-5036adb3e3a1 / -65a6d68c-90ae-4e31-8bbc-82e8ec75b3de,98b72340-a402-45bc-9493-71263e3168d6,b0c1aba5-b1bd-48df-abec-19efa8e49d6d,cba152f4-af54-4d82-a35d-67aa165174be |
| Jogador 2 | 4-2 | 152 | BUY | ALL_IN | 14.0 | 6 | 17 | 1 | 26.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2571399509906769 | 0.0 | 0.0 | +04520fe5-4449-4632-b275-e5e28d642007 / -— |
| Jogador 2 | 4-2 | 153 | BUY | ALL_IN | 14.0 | 6 | 14 | 1 | 26.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06653756648302078 | 0.0 | 0.0 | +3b934078-806c-40f0-b102-e9131220f70e / -— |
| Jogador 2 | 4-2 | 154 | REROLL | ALL_IN | 14.0 | 6 | 13 | 1 | 26.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 155 | BUY | ALL_IN | 14.0 | 6 | 11 | 1 | 26.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6555307507514954 | 0.0 | 0.0 | +89ef75a2-6ac2-4c6c-b2b8-492aec985a01 / -— |
| Jogador 2 | 4-2 | 156 | BUY | ALL_IN | 14.0 | 6 | 9 | 0 | 26.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04462089389562607 | 0.0 | 0.0 | +9af900db-c181-448a-9736-30f08f062a00 / -— |
| Jogador 2 | 4-2 | 157 | BUY | ALL_IN | 14.0 | 6 | 6 | 0 | 26.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19357220828533173 | 0.0 | 0.0 | +77489602-9456-4a97-aa7e-df7ef91d5e4a / -— |
| Jogador 2 | 4-2 | 158 | REROLL | ALL_IN | 14.0 | 6 | 3 | 0 | 26.0 | Vivaz/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 159 | MOVE_BENCH | ALL_IN | 14.0 | 6 | 1 | 0 | 26.0 | Vivaz/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4689064621925354 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 161 | BUY | ALL_IN | 4.0 | 6 | 9 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05835681036114693 | 0.0 | 0.0 | +9f445115-49cc-4647-91a0-a80e347e9c62 / -— |
| Jogador 2 | 4-3 | 162 | REROLL | ALL_IN | 4.0 | 6 | 7 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 163 | BUY | ALL_IN | 4.0 | 6 | 5 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2778747081756592 | 0.0 | 0.0 | +2cdf9a6a-5786-4a2b-8c4e-6fb9b151a92d / -— |
| Jogador 2 | 4-3 | 164 | REROLL | ALL_IN | 4.0 | 6 | 4 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 165 | REROLL | ALL_IN | 4.0 | 6 | 2 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 166 | PASS | ALL_IN | 4.0 | 6 | 0 | 0 | 32.0 | Vivaz/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 171 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 181 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 191 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 198 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 202 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 212 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 222 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 232 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 242 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 252 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 262 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 271 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 281 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.019615383818745613 | 0.0 | 0.0 | +— / -36f58657-5835-4389-95e9-a7d26464c2aa |
| Jogador 3 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.21530985832214355 | 0.0 | 0.0 | +2cf5ccdc-76f4-4fc8-b12c-7b3b68b1b2c8 / -— |
| Jogador 3 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_RekSai | MOVE_BENCH, SELL, PASS | True | True | 0.5931587815284729 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_RekSai | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 10 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_RekSai | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9699749946594238 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 11 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_RekSai | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_RekSai | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035527557134628296 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 13 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_RekSai | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 16 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_RekSai | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 25 | PASS | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 34 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 4.0 | —/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.029922112822532654 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 3 | 2-1 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 8 | 0 | 4.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.381960391998291 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 36 | BUY_XP | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.15800000727176666 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 37 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.15800000727176666 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 38 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Shen | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 42 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 8.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.30496320128440857 | 0.0 | 0.0 | +98558a52-389f-46fc-b370-6345603f4103 / -— |
| Jogador 3 | 2-2 | 43 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42280489206314087 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 44 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34445253014564514 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 45 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09093416482210159 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 46 | PASS | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 52 | BUY | STABILIZE | 89.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2739450931549072 | 0.0 | 0.0 | +491eb6b6-54f4-4de8-bc63-d96c6c1d9cce / -— |
| Jogador 3 | 2-3 | 53 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4056094288825989 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 54 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4691050350666046 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 55 | BUY_XP | STABILIZE | 89.0 | 5 | 5 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 56 | PASS | STABILIZE | 89.0 | 5 | 1 | 0 | 20.0 | —/DA_18_Diana | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 62 | BUY_XP | STABILIZE | 89.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 63 | PASS | STABILIZE | 89.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 72 | BUY_XP | STABILIZE | 89.0 | 5 | 8 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 73 | BUY_XP | STABILIZE | 89.0 | 5 | 4 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.052000001072883606 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 74 | PASS | STABILIZE | 89.0 | 6 | 0 | 0 | 20.0 | —/DA_18_Diana | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 82 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 5 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06624050438404083 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 83 | BUY | STABILIZE | 83.0 | 6 | 5 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03317442908883095 | 0.0 | 0.0 | +764470bb-9820-4e49-98f9-5a5f0ce5ca8f / -— |
| Jogador 3 | 2-6 | 84 | PASS | STABILIZE | 83.0 | 6 | 3 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 88 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 3 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28635653853416443 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 90 | BUY | STABILIZE | 83.0 | 6 | 9 | 0 | 24.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9671397805213928 | 0.0 | 0.0 | +31aa0a5f-4d66-48c2-b6d4-b76ac220c752 / -— |
| Jogador 3 | 2-7 | 91 | BUY_XP | STABILIZE | 83.0 | 6 | 6 | 0 | 24.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 92 | SELL | STABILIZE | 83.0 | 6 | 2 | 0 | 24.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0171397924423218 | 0.0 | 0.0 | +— / -31aa0a5f-4d66-48c2-b6d4-b76ac220c752 |
| Jogador 3 | 3-1 | 94 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 10 | 1 | 24.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.00416592275723815 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 95 | BUY_XP | STABILIZE | 83.0 | 6 | 10 | 1 | 24.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 96 | BUY_XP | STABILIZE | 83.0 | 6 | 6 | 0 | 24.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 97 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 2 | 0 | 24.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.16880784928798676 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 98 | PASS | STABILIZE | 83.0 | 6 | 2 | 0 | 24.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 102 | BUY_XP | STABILIZE | 83.0 | 6 | 9 | 0 | 24.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 103 | BUY_XP | STABILIZE | 83.0 | 6 | 5 | 0 | 24.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 104 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 1 | 0 | 24.0 | Espinhos Negros/DA_18_Diana | BUY, MOVE_BOARD, PASS | True | True | -0.14524361491203308 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 105 | PASS | STABILIZE | 83.0 | 6 | 1 | 0 | 24.0 | Espinhos Negros/DA_18_Diana | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 112 | BUY_XP | STABILIZE | 72.0 | 6 | 6 | 0 | 24.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06199999898672104 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 113 | BUY | STABILIZE | 72.0 | 7 | 2 | 0 | 24.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.032821450382471085 | 0.0 | 0.0 | +7fd03119-ac82-49e1-b3bb-3a0caa31011f / -— |
| Jogador 3 | 3-3 | 114 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 0 | 0 | 24.0 | Espinhos Negros/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3949490487575531 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 115 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 0 | 0 | 28.0 | Espinhos Negros/DA_18_Diana | MOVE_BOARD, PASS | True | True | 0.031805504113435745 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 116 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 0 | 0 | 28.0 | Espinhos Negros/DA_18_Diana | MOVE_BOARD, PASS | True | True | 0.017798790708184242 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 117 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 0 | 0 | 28.0 | Espinhos Negros/DA_18_Diana | MOVE_BOARD, PASS | True | True | 0.03894601762294769 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 118 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 0 | 0 | 28.0 | Espinhos Negros/DA_18_Diana | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 120 | BUY | STABILIZE | 72.0 | 7 | 6 | 0 | 28.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.28360113501548767 | 0.0 | 0.0 | +661b176a-5963-4715-b9dd-aca29f552fa9 / -— |
| Jogador 3 | 3-5 | 122 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 8 | 0 | 28.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14431804418563843 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 123 | BUY | STABILIZE | 72.0 | 7 | 8 | 0 | 28.0 | Espinhos Negros/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07173363864421844 | 0.0 | 0.0 | +f722cd46-0c4e-42e7-80ff-4b910c28d572 / -— |
| Jogador 3 | 3-5 | 124 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 4 | 0 | 28.0 | Espinhos Negros/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08607418090105057 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 125 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 4 | 0 | 28.0 | Espinhos Negros/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001785655738785863 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 127 | MOVE_BOARD | STABILIZE | 61.0 | 7 | 9 | 0 | 28.0 | Espinhos Negros/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 128 | MOVE_BOARD | STABILIZE | 61.0 | 7 | 9 | 0 | 28.0 | Espinhos Negros/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 129 | PASS | STABILIZE | 61.0 | 7 | 9 | 0 | 28.0 | Espinhos Negros/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 132 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 15 | 1 | 28.0 | Espinhos Negros/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10971488058567047 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 133 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 15 | 1 | 28.0 | Espinhos Negros/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 134 | PASS | STABILIZE | 50.0 | 7 | 15 | 1 | 28.0 | Espinhos Negros/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 141 | BUY | STABILIZE | 50.0 | 7 | 22 | 2 | 28.0 | Espinhos Negros/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10161963850259781 | 0.0 | 0.0 | +bae633d7-8337-461a-9a84-9c9758392bb6 / -— |
| Jogador 3 | 4-1 | 142 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 18 | 1 | 28.0 | Espinhos Negros/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14954893290996552 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 143 | REROLL | STABILIZE | 50.0 | 7 | 18 | 1 | 28.0 | Espinhos Negros/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 144 | BUY | STABILIZE | 50.0 | 7 | 16 | 1 | 28.0 | Espinhos Negros/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7318097352981567 | 0.0 | 0.0 | +4c1dab77-0e6d-401b-a341-40117b445957 / -— |
| Jogador 3 | 4-1 | 145 | REROLL | STABILIZE | 50.0 | 7 | 12 | 1 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 146 | REROLL | STABILIZE | 50.0 | 7 | 10 | 1 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 147 | REROLL | STABILIZE | 50.0 | 7 | 8 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 148 | REROLL | STABILIZE | 50.0 | 7 | 6 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 149 | REROLL | STABILIZE | 50.0 | 7 | 4 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 151 | REROLL | STABILIZE | 50.0 | 7 | 8 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 152 | REROLL | STABILIZE | 50.0 | 7 | 6 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 153 | REROLL | STABILIZE | 50.0 | 7 | 4 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 154 | REROLL | STABILIZE | 50.0 | 7 | 2 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 155 | MOVE_BENCH | STABILIZE | 50.0 | 7 | 0 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2672063112258911 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 156 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 0 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 157 | MOVE_BOARD | STABILIZE | 50.0 | 7 | 0 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11552552878856659 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 158 | PASS | STABILIZE | 50.0 | 7 | 0 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 161 | REROLL | STABILIZE | 38.0 | 7 | 5 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 162 | REROLL | STABILIZE | 38.0 | 7 | 3 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 163 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 1 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 164 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 1 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31991010904312134 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 165 | PASS | STABILIZE | 38.0 | 7 | 1 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 171 | REROLL | STABILIZE | 38.0 | 7 | 7 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 172 | REROLL | STABILIZE | 38.0 | 7 | 5 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 173 | REROLL | STABILIZE | 38.0 | 7 | 3 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 174 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 1 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1610117256641388 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 175 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 1 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1467573344707489 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 176 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 1 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 177 | PASS | STABILIZE | 38.0 | 7 | 1 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 181 | REROLL | STABILIZE | 38.0 | 7 | 6 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 182 | REROLL | STABILIZE | 38.0 | 7 | 4 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 183 | REROLL | STABILIZE | 38.0 | 7 | 2 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 184 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 0 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026869148015975952 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 185 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 0 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 186 | MOVE_BOARD | STABILIZE | 38.0 | 7 | 0 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11969414353370667 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 187 | PASS | STABILIZE | 38.0 | 7 | 0 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 191 | REROLL | STABILIZE | 25.0 | 7 | 5 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 192 | REROLL | STABILIZE | 25.0 | 7 | 3 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 193 | MOVE_BOARD | STABILIZE | 25.0 | 7 | 1 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3262105882167816 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 194 | MOVE_BOARD | STABILIZE | 25.0 | 7 | 1 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17504683136940002 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 195 | MOVE_BOARD | STABILIZE | 25.0 | 7 | 1 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16028515994548798 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 196 | MOVE_BOARD | STABILIZE | 25.0 | 7 | 1 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 198 | REROLL | ALL_IN | 11.0 | 7 | 7 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 199 | BUY | ALL_IN | 11.0 | 7 | 5 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2716728150844574 | 0.0 | 0.0 | +48ed833b-ccf6-4e77-8dad-7a1dc65a34ad / -— |
| Jogador 3 | 4-7 | 200 | BUY | ALL_IN | 11.0 | 7 | 1 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27748146653175354 | 0.0 | 0.0 | +1477dd4d-8f90-4921-b6fd-ffaa744f0dce / -— |
| Jogador 3 | 5-1 | 202 | EQUIP_FROM_INVENTORY | ALL_IN | 11.0 | 7 | 6 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 203 | BUY | ALL_IN | 11.0 | 7 | 6 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2681084871292114 | 0.0 | 0.0 | +c184c7c4-0cf6-4101-ac4d-cea12a7b4607 / -— |
| Jogador 3 | 5-1 | 204 | BUY | ALL_IN | 11.0 | 7 | 3 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7008547782897949 | 0.0 | 0.0 | +63bfe693-fb71-48ad-a4b1-f350159175a9 / -— |
| Jogador 3 | 5-1 | 205 | PASS | ALL_IN | 11.0 | 7 | 0 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 212 | REROLL | ALL_IN | 11.0 | 7 | 6 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 213 | REROLL | ALL_IN | 11.0 | 7 | 4 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 214 | REROLL | ALL_IN | 11.0 | 7 | 2 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 215 | PASS | ALL_IN | 11.0 | 7 | 0 | 0 | 28.0 | Espinhos Negros/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 222 | PASS | ALL_IN | 0.0 | 7 | 0 | 0 | 0.0 | Espinhos Negros/DA_18_Soraka | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 232 | PASS | ALL_IN | 0.0 | 7 | 0 | 0 | 0.0 | Espinhos Negros/DA_18_Soraka | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 242 | PASS | ALL_IN | 0.0 | 7 | 0 | 0 | 0.0 | Espinhos Negros/DA_18_Soraka | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 252 | PASS | ALL_IN | 0.0 | 7 | 0 | 0 | 0.0 | Espinhos Negros/DA_18_Soraka | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 262 | PASS | ALL_IN | 0.0 | 7 | 0 | 0 | 0.0 | Espinhos Negros/DA_18_Soraka | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 271 | PASS | ALL_IN | 0.0 | 7 | 0 | 0 | 0.0 | Espinhos Negros/DA_18_Soraka | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-2 | 281 | PASS | ALL_IN | 0.0 | 7 | 0 | 0 | 0.0 | Espinhos Negros/DA_18_Soraka | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 8 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.28737619519233704 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 10 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3375903069972992 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 11 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40336331725120544 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 12 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 16 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 25 | PASS | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 34 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 4.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.889392077922821 | 0.0 | 0.0 | +185ee377-0917-4209-905b-9486d5be0193 / -— |
| Jogador 4 | 2-1 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 9 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 36 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 9 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24579323828220367 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 37 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0823926255106926 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 38 | BUY_XP | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.15800000727176666 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 39 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.15800000727176666 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 40 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 42 | BUY | STABILIZE | 94.0 | 5 | 6 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.074368417263031 | 0.0 | 0.0 | +3c6ac558-6b59-4a97-814e-bff0ff895232 / -— |
| Jogador 4 | 2-2 | 43 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 3 | 0 | 6.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15624593198299408 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 44 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 3 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 45 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 3 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.12929771840572357 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 46 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 3 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 47 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 3 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 48 | PASS | STABILIZE | 94.0 | 5 | 3 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 52 | BUY | STABILIZE | 94.0 | 5 | 9 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9320574402809143 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 4 | 2-3 | 53 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 6 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14012913405895233 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 54 | BUY_XP | STABILIZE | 94.0 | 5 | 6 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 55 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 2 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 56 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 2 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 57 | PASS | STABILIZE | 94.0 | 5 | 2 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 62 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 9 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.04875248298048973 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 63 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 9 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 64 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 9 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 65 | PASS | STABILIZE | 94.0 | 5 | 9 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 72 | BUY | STABILIZE | 94.0 | 5 | 15 | 1 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.110378623008728 | 0.0 | 0.0 | +6f3f86ec-6928-4032-a1ef-533a68865516 / -3c6ac558-6b59-4a97-814e-bff0ff895232,d01cae02-d8ba-491e-841f-bf3120953933 |
| Jogador 4 | 2-5 | 73 | BUY | STABILIZE | 94.0 | 5 | 12 | 1 | 6.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23808710277080536 | 0.0 | 0.0 | +032b5960-ec2a-4a26-ad67-862a20f30523 / -— |
| Jogador 4 | 2-5 | 74 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 9 | 0 | 6.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24776659905910492 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 75 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 9 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5499034523963928 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 76 | BUY_XP | STABILIZE | 94.0 | 5 | 9 | 0 | 24.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 77 | BUY_XP | STABILIZE | 94.0 | 5 | 5 | 0 | 24.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 78 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 1 | 0 | 24.0 | —/DA_Krug18 | BUY, MOVE_BOARD, PASS | True | True | 0.03215137496590614 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 79 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 1 | 0 | 24.0 | —/DA_Krug18 | BUY, MOVE_BOARD, PASS | True | True | 0.04875248298048973 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 80 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 1 | 0 | 24.0 | —/DA_Krug18 | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 82 | BUY | STABILIZE | 87.0 | 6 | 6 | 0 | 24.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.023155245929956436 | 0.0 | 0.0 | +21abffda-a6c9-4987-8350-4f6d8f540441 / -— |
| Jogador 4 | 2-6 | 83 | MOVE_BENCH | STABILIZE | 87.0 | 6 | 2 | 0 | 24.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44646355509757996 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 84 | MOVE_BOARD | STABILIZE | 87.0 | 6 | 2 | 0 | 32.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 85 | MOVE_BOARD | STABILIZE | 87.0 | 6 | 2 | 0 | 32.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.1292874664068222 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 86 | PASS | STABILIZE | 87.0 | 6 | 2 | 0 | 32.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 90 | MOVE_BOARD | STABILIZE | 81.0 | 6 | 8 | 0 | 32.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.11648605763912201 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 91 | MOVE_BOARD | STABILIZE | 81.0 | 6 | 8 | 0 | 32.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 92 | MOVE_BOARD | STABILIZE | 81.0 | 6 | 8 | 0 | 32.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 94 | BUY | STABILIZE | 81.0 | 6 | 14 | 1 | 32.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.07305185496807098 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -— |
| Jogador 4 | 3-1 | 95 | MOVE_BENCH | STABILIZE | 81.0 | 6 | 11 | 1 | 32.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35493528842926025 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 96 | MOVE_BENCH | STABILIZE | 81.0 | 6 | 11 | 1 | 30.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32359468936920166 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 97 | PASS | STABILIZE | 81.0 | 6 | 11 | 1 | 36.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 102 | BUY_XP | STABILIZE | 70.0 | 6 | 18 | 1 | 36.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 103 | BUY_XP | STABILIZE | 70.0 | 6 | 14 | 1 | 36.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 104 | BUY_XP | STABILIZE | 70.0 | 6 | 10 | 1 | 36.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 105 | BUY_XP | STABILIZE | 70.0 | 6 | 6 | 0 | 36.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 106 | SELL | STABILIZE | 70.0 | 6 | 2 | 0 | 36.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7286890745162964 | 0.0 | 0.0 | +— / -185ee377-0917-4209-905b-9486d5be0193 |
| Jogador 4 | 3-2 | 107 | PASS | STABILIZE | 70.0 | 6 | 3 | 0 | 36.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 112 | BUY_XP | STABILIZE | 70.0 | 6 | 9 | 0 | 36.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 113 | BUY_XP | STABILIZE | 70.0 | 6 | 5 | 0 | 36.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 114 | PASS | STABILIZE | 70.0 | 6 | 1 | 0 | 36.0 | Colosso/DA_Krug18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 120 | BUY_XP | STABILIZE | 70.0 | 6 | 8 | 0 | 36.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0820000022649765 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 122 | BUY | STABILIZE | 70.0 | 7 | 10 | 1 | 36.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2031114101409912 | 0.0 | 0.0 | +750eedbe-93d9-46de-b3b8-a88e41f395f0 / -— |
| Jogador 4 | 3-5 | 123 | BUY | STABILIZE | 70.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2768329679965973 | 0.0 | 0.0 | +1457cd1e-c240-4ce5-9217-a91bddfc8807 / -— |
| Jogador 4 | 3-5 | 124 | MOVE_BENCH | STABILIZE | 70.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5344192385673523 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 125 | BUY_XP | STABILIZE | 70.0 | 7 | 4 | 0 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 127 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 7 | 0 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 128 | BUY_XP | STABILIZE | 70.0 | 7 | 7 | 0 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 129 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 3 | 0 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 130 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 3 | 0 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05092886462807655 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 132 | MOVE_BENCH | STABILIZE | 70.0 | 7 | 10 | 1 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09878116846084595 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 133 | BUY_XP | STABILIZE | 70.0 | 7 | 10 | 1 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 134 | BUY_XP | STABILIZE | 70.0 | 7 | 6 | 0 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 135 | SELL | STABILIZE | 70.0 | 7 | 2 | 0 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00821650866419077 | 0.0 | 0.0 | +— / -68b28241-1946-4304-8b10-ae24a13a8e60 |
| Jogador 4 | 3-7 | 136 | BUY_XP | STABILIZE | 70.0 | 7 | 5 | 0 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 137 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 1 | 0 | 42.0 | Colosso/DA_Krug18 | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 138 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 1 | 0 | 42.0 | Colosso/DA_Krug18 | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 139 | PASS | STABILIZE | 70.0 | 7 | 1 | 0 | 42.0 | Colosso/DA_Krug18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 141 | CRAFT_AND_EQUIP | STABILIZE | 70.0 | 7 | 7 | 0 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | — | 0.09443093836307526 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 142 | BUY_XP | STABILIZE | 70.0 | 7 | 7 | 0 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 143 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 3 | 0 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.11359098553657532 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 144 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 3 | 0 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 145 | PASS | STABILIZE | 70.0 | 7 | 3 | 0 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 151 | BUY_XP | STABILIZE | 70.0 | 7 | 11 | 1 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 152 | BUY_XP | STABILIZE | 70.0 | 7 | 7 | 0 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 153 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 3 | 0 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 154 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 3 | 0 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.1213110089302063 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 155 | PASS | STABILIZE | 70.0 | 7 | 3 | 0 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 161 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 12 | 1 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.010701649822294712 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 162 | BUY_XP | STABILIZE | 70.0 | 7 | 12 | 1 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 163 | BUY_XP | STABILIZE | 70.0 | 7 | 8 | 0 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 164 | BUY_XP | STABILIZE | 70.0 | 7 | 4 | 0 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06543750315904617 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 165 | MOVE_BOARD | WINSTREAK | 70.0 | 8 | 0 | 0 | 42.0 | Colosso/DA_Krug18 | MOVE_BOARD, PASS | True | True | -0.1289699822664261 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 166 | MOVE_BOARD | WINSTREAK | 70.0 | 8 | 0 | 0 | 42.0 | Colosso/DA_Krug18 | MOVE_BOARD, PASS | True | True | 0.036966722458601 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 167 | MOVE_BOARD | WINSTREAK | 70.0 | 8 | 0 | 0 | 42.0 | Colosso/DA_Krug18 | MOVE_BOARD, PASS | True | True | -0.1384258270263672 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 168 | MOVE_BOARD | WINSTREAK | 70.0 | 8 | 0 | 0 | 42.0 | Colosso/DA_Krug18 | MOVE_BOARD, PASS | True | True | 0.0352528877556324 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 169 | MOVE_BOARD | WINSTREAK | 70.0 | 8 | 0 | 0 | 42.0 | Colosso/DA_Krug18 | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 171 | BUY | WINSTREAK | 70.0 | 8 | 9 | 0 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7227559089660645 | 0.0 | 0.0 | +5de51369-647a-45bd-95b7-c8efe44c5484 / -— |
| Jogador 4 | 4-4 | 172 | MOVE_BENCH | WINSTREAK | 70.0 | 8 | 6 | 0 | 42.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.543434202671051 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 173 | MOVE_BOARD | WINSTREAK | 70.0 | 8 | 6 | 0 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 174 | MOVE_BOARD | WINSTREAK | 70.0 | 8 | 6 | 0 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10340246558189392 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 175 | PASS | WINSTREAK | 70.0 | 8 | 6 | 0 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 181 | BUY | WINSTREAK | 70.0 | 8 | 14 | 1 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09514039754867554 | 0.0 | 0.0 | +87726d3e-4b0d-41ae-bf43-893d4092bd5b / -— |
| Jogador 4 | 4-5 | 182 | BUY | WINSTREAK | 70.0 | 8 | 10 | 1 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07909032702445984 | 0.0 | 0.0 | +f1ece814-0986-421f-b5df-0b457ebaa484 / -— |
| Jogador 4 | 4-5 | 183 | MOVE_BOARD | WINSTREAK | 70.0 | 8 | 6 | 0 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11697462201118469 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 184 | MOVE_BOARD | WINSTREAK | 70.0 | 8 | 6 | 0 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10170134902000427 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 185 | PASS | WINSTREAK | 70.0 | 8 | 6 | 0 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 191 | BUY | WINSTREAK | 70.0 | 8 | 15 | 1 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6871638894081116 | 0.0 | 0.0 | +fe772b41-d367-4385-b35f-eb5c07754a32 / -— |
| Jogador 4 | 4-6 | 192 | BUY_XP | WINSTREAK | 70.0 | 8 | 11 | 1 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 193 | BUY_XP | WINSTREAK | 70.0 | 8 | 7 | 0 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 194 | MOVE_BOARD | WINSTREAK | 70.0 | 8 | 3 | 0 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0015624607913196087 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 195 | MOVE_BOARD | WINSTREAK | 70.0 | 8 | 3 | 0 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11189623177051544 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 196 | MOVE_BOARD | WINSTREAK | 70.0 | 8 | 3 | 0 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 198 | MOVE_BENCH | WINSTREAK | 70.0 | 8 | 12 | 1 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3597928285598755 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 199 | BUY_XP | WINSTREAK | 70.0 | 8 | 12 | 1 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 200 | BUY_XP | WINSTREAK | 70.0 | 8 | 8 | 0 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 202 | EQUIP_FROM_INVENTORY | WINSTREAK | 70.0 | 8 | 12 | 1 | 48.0 | Colosso/DA_Krug18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 203 | BUY_XP | WINSTREAK | 70.0 | 8 | 12 | 1 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 204 | BUY_XP | WINSTREAK | 70.0 | 8 | 8 | 0 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 205 | BUY_XP | WINSTREAK | 70.0 | 8 | 4 | 0 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 206 | PASS | WINSTREAK | 70.0 | 8 | 0 | 0 | 48.0 | Colosso/DA_Krug18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 212 | BUY_XP | WINSTREAK | 70.0 | 8 | 9 | 0 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 213 | BUY_XP | WINSTREAK | 70.0 | 8 | 5 | 0 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 214 | PASS | WINSTREAK | 70.0 | 8 | 1 | 0 | 48.0 | Colosso/DA_Krug18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 222 | BUY_XP | WINSTREAK | 70.0 | 8 | 10 | 1 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 223 | BUY_XP | WINSTREAK | 70.0 | 8 | 6 | 0 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 224 | PASS | WINSTREAK | 70.0 | 8 | 2 | 0 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 232 | BUY_XP | WINSTREAK | 70.0 | 8 | 10 | 1 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 233 | BUY_XP | WINSTREAK | 70.0 | 8 | 6 | 0 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10587500035762787 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 234 | MOVE_BENCH | WINSTREAK | 70.0 | 9 | 2 | 0 | 48.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.510187029838562 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 235 | PASS | WINSTREAK | 70.0 | 9 | 2 | 0 | 56.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 242 | BUY_XP | WINSTREAK | 70.0 | 9 | 10 | 1 | 56.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 243 | BUY_XP | WINSTREAK | 70.0 | 9 | 6 | 0 | 56.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 244 | PASS | WINSTREAK | 70.0 | 9 | 2 | 0 | 56.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 252 | BUY_XP | WINSTREAK | 70.0 | 9 | 11 | 1 | 56.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 253 | BUY_XP | WINSTREAK | 70.0 | 9 | 7 | 0 | 56.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 254 | PASS | WINSTREAK | 70.0 | 9 | 3 | 0 | 56.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 262 | PASS | WINSTREAK | 70.0 | 9 | 12 | 1 | 56.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 271 | EQUIP_FROM_INVENTORY | WINSTREAK | 70.0 | 9 | 21 | 2 | 56.0 | Colosso/DA_Krug18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 272 | EQUIP_FROM_INVENTORY | WINSTREAK | 70.0 | 9 | 21 | 2 | 56.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.010413962416350842 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 273 | BUY_XP | WINSTREAK | 70.0 | 9 | 21 | 2 | 56.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 274 | BUY_XP | WINSTREAK | 70.0 | 9 | 17 | 1 | 56.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 275 | BUY_XP | WINSTREAK | 70.0 | 9 | 13 | 1 | 56.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 276 | BUY_XP | WINSTREAK | 70.0 | 9 | 9 | 0 | 56.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 277 | BUY_XP | WINSTREAK | 70.0 | 9 | 5 | 0 | 56.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 278 | SELL | WINSTREAK | 70.0 | 9 | 1 | 0 | 56.0 | Colosso/DA_Krug18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003317275084555149 | 0.0 | 0.0 | +— / -f1ece814-0986-421f-b5df-0b457ebaa484 |
| Jogador 4 | 6-1 | 279 | BUY_XP | WINSTREAK | 70.0 | 9 | 5 | 0 | 56.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-2 | 281 | BUY_XP | WINSTREAK | 70.0 | 9 | 10 | 1 | 56.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-2 | 282 | BUY_XP | WINSTREAK | 70.0 | 9 | 6 | 0 | 56.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-2 | 283 | PASS | WINSTREAK | 70.0 | 9 | 2 | 0 | 56.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 8 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.27265432476997375 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 10 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.027269404381513596 | 0.0 | 0.0 | +df7d3860-9b2e-45ed-b564-281d95e64e82 / -— |
| Jogador 5 | 1-2 | 11 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37584805488586426 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 12 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 16 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 25 | PASS | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 34 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.24848389625549316 | 0.0 | 0.0 | +242805ca-f275-4e04-a2f5-81e0b6680dd1 / -— |
| Jogador 5 | 2-1 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1427890807390213 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 36 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.32034075260162354 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 37 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2499295473098755 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 5 | 2-1 | 38 | SELL | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.51484614610672 | 0.0 | 0.0 | +— / -5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef |
| Jogador 5 | 2-1 | 39 | BUY_XP | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.15800000727176666 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 40 | REROLL | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 42 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4534066915512085 | 0.0 | 0.0 | +e6ac7c34-615e-4ccc-bc0f-8ba583bf5ca1 / -— |
| Jogador 5 | 2-2 | 43 | SELL | STABILIZE | 95.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5034067034721375 | 0.0 | 0.0 | +— / -e6ac7c34-615e-4ccc-bc0f-8ba583bf5ca1 |
| Jogador 5 | 2-2 | 44 | BUY_XP | STABILIZE | 95.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.06800000369548798 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 45 | BUY | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, MOVE_BOARD, PASS | True | True | 0.38790518045425415 | 0.0 | 0.0 | +257a34c3-5cf0-4a26-adb4-6635fda7a29b / -— |
| Jogador 5 | 2-2 | 46 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 12.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4379051923751831 | 0.0 | 0.0 | +— / -257a34c3-5cf0-4a26-adb4-6635fda7a29b |
| Jogador 5 | 2-2 | 47 | BUY | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, MOVE_BOARD, PASS | True | True | -0.011749920435249805 | 0.0 | 0.0 | +6951a681-f5b9-4c22-9182-46b4d2c3cbb3 / -— |
| Jogador 5 | 2-2 | 48 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 12.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1786923110485077 | 0.0 | 0.0 | +— / -6951a681-f5b9-4c22-9182-46b4d2c3cbb3 |
| Jogador 5 | 2-2 | 49 | BUY | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, MOVE_BOARD, PASS | True | True | -0.011844409629702568 | 0.0 | 0.0 | +ff10e482-7085-4e73-8a0c-fdd3f4938128 / -— |
| Jogador 5 | 2-2 | 50 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 0 | 0 | 12.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13451270759105682 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 52 | BUY | STABILIZE | 90.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.26933905482292175 | 0.0 | 0.0 | +d1840f93-35b0-4e88-b58e-eea7267beedc / -— |
| Jogador 5 | 2-3 | 53 | BUY | STABILIZE | 90.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4489268362522125 | 0.0 | 0.0 | +d44224c1-925d-42f9-ad60-ff4c36c665d6 / -— |
| Jogador 5 | 2-3 | 54 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48502326011657715 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 55 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14408981800079346 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 56 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2762066125869751 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 57 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2094142585992813 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 58 | PASS | STABILIZE | 90.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 62 | MOVE_BENCH | LOSS_STREAK | 84.0 | 5 | 7 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1352250725030899 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 63 | SELL | LOSS_STREAK | 84.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.044226277619600296 | 0.0 | 0.0 | +— / -df7d3860-9b2e-45ed-b564-281d95e64e82 |
| Jogador 5 | 2-4 | 64 | MOVE_BOARD | LOSS_STREAK | 84.0 | 5 | 9 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.14408981800079346 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 65 | MOVE_BOARD | LOSS_STREAK | 84.0 | 5 | 9 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.3410894274711609 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 66 | MOVE_BOARD | LOSS_STREAK | 84.0 | 5 | 9 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17878878116607666 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 67 | REROLL | LOSS_STREAK | 84.0 | 5 | 9 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 68 | BUY | LOSS_STREAK | 84.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3598998785018921 | 0.0 | 0.0 | +f957e607-dd51-492b-9186-252da4e0c12f / -— |
| Jogador 5 | 2-4 | 69 | SELL | LOSS_STREAK | 84.0 | 5 | 5 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40989986062049866 | 0.0 | 0.0 | +— / -f957e607-dd51-492b-9186-252da4e0c12f |
| Jogador 5 | 2-4 | 70 | BUY_XP | LOSS_STREAK | 84.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 72 | BUY | LOSS_STREAK | 84.0 | 5 | 9 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8935216665267944 | 0.0 | 0.0 | +d97b6383-1870-48d1-a9b8-6a8ce153c9ce / -— |
| Jogador 5 | 2-5 | 73 | SELL | LOSS_STREAK | 84.0 | 5 | 8 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9435216784477234 | 0.0 | 0.0 | +— / -d97b6383-1870-48d1-a9b8-6a8ce153c9ce |
| Jogador 5 | 2-5 | 74 | MOVE_BOARD | LOSS_STREAK | 84.0 | 5 | 9 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 75 | REROLL | LOSS_STREAK | 84.0 | 5 | 9 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 76 | REROLL | LOSS_STREAK | 84.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 77 | BUY | LOSS_STREAK | 84.0 | 5 | 5 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8936232924461365 | 0.0 | 0.0 | +3fc2815d-c456-47c3-bb27-783336b3cdfa / -— |
| Jogador 5 | 2-5 | 78 | SELL | LOSS_STREAK | 84.0 | 5 | 4 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9436232447624207 | 0.0 | 0.0 | +— / -3fc2815d-c456-47c3-bb27-783336b3cdfa |
| Jogador 5 | 2-5 | 79 | BUY_XP | LOSS_STREAK | 84.0 | 5 | 5 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 80 | MOVE_BOARD | LOSS_STREAK | 84.0 | 5 | 1 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, MOVE_BOARD, PASS | True | True | 0.17531836032867432 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 82 | BUY | LOSS_STREAK | 80.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3157503306865692 | 0.0 | 0.0 | +eafa585a-9474-415b-b46b-d3ce86f4a066 / -— |
| Jogador 5 | 2-6 | 83 | BUY | LOSS_STREAK | 80.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3530791997909546 | 0.0 | 0.0 | +a2f987f8-01d6-4463-9ab4-f96c9b6f067b / -— |
| Jogador 5 | 2-6 | 84 | MOVE_BENCH | LOSS_STREAK | 80.0 | 5 | 0 | 0 | 20.0 | —/DA_18_Ahri | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06330438703298569 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 85 | SELL | LOSS_STREAK | 80.0 | 5 | 0 | 0 | 22.0 | —/DA_18_Ahri | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04129337891936302 | 0.0 | 0.0 | +— / -d44224c1-925d-42f9-ad60-ff4c36c665d6 |
| Jogador 5 | 2-6 | 86 | MOVE_BENCH | LOSS_STREAK | 80.0 | 5 | 2 | 0 | 22.0 | —/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6939003467559814 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 87 | SELL | LOSS_STREAK | 80.0 | 5 | 2 | 0 | 24.0 | —/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3617304265499115 | 0.0 | 0.0 | +— / -a2f987f8-01d6-4463-9ab4-f96c9b6f067b |
| Jogador 5 | 2-6 | 88 | BUY_XP | LOSS_STREAK | 80.0 | 5 | 5 | 0 | 24.0 | —/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.017000000923871994 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 90 | BUY | LOSS_STREAK | 73.0 | 6 | 8 | 0 | 24.0 | —/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.04371820017695427 | 0.0 | 0.0 | +91f05e8c-f467-4f22-9cb0-c814ffa93198 / -— |
| Jogador 5 | 2-7 | 91 | MOVE_BENCH | LOSS_STREAK | 73.0 | 6 | 6 | 0 | 24.0 | —/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41304054856300354 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 92 | MOVE_BOARD | LOSS_STREAK | 73.0 | 6 | 6 | 0 | 28.0 | —/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.3250933289527893 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 94 | BUY | LOSS_STREAK | 73.0 | 6 | 13 | 1 | 28.0 | —/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.20838654041290283 | 0.0 | 0.0 | +6e096b30-0b49-4a98-8596-8b05089793ae / -— |
| Jogador 5 | 3-1 | 95 | MOVE_BENCH | LOSS_STREAK | 73.0 | 6 | 10 | 1 | 28.0 | —/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13749229907989502 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 96 | MOVE_BENCH | LOSS_STREAK | 73.0 | 6 | 10 | 1 | 28.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2178383767604828 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 97 | MOVE_BENCH | STABILIZE | 73.0 | 6 | 10 | 1 | 26.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7501276135444641 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 98 | PASS | STABILIZE | 73.0 | 6 | 10 | 1 | 28.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 102 | MOVE_BENCH | STABILIZE | 63.0 | 6 | 19 | 1 | 28.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03379211202263832 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 103 | MOVE_BENCH | STABILIZE | 63.0 | 6 | 19 | 1 | 28.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2486957609653473 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 104 | PASS | STABILIZE | 63.0 | 6 | 19 | 1 | 26.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 112 | BUY | STABILIZE | 51.0 | 6 | 28 | 2 | 26.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29409968852996826 | 0.0 | 0.0 | +ea7e2f0c-7dec-42c0-86ac-e66997fb2e6c / -— |
| Jogador 5 | 3-3 | 113 | BUY | STABILIZE | 51.0 | 6 | 26 | 2 | 26.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0465916246175766 | 0.0 | 0.0 | +333cdd27-0114-4d36-8ffa-e79b0f43b8e8 / -— |
| Jogador 5 | 3-3 | 114 | MOVE_BENCH | STABILIZE | 51.0 | 6 | 23 | 2 | 26.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7507396340370178 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 115 | MOVE_BENCH | STABILIZE | 51.0 | 6 | 23 | 2 | 28.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08655061572790146 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 116 | MOVE_BENCH | STABILIZE | 51.0 | 6 | 23 | 2 | 28.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21993008255958557 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 117 | MOVE_BOARD | STABILIZE | 51.0 | 6 | 23 | 2 | 30.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26141127943992615 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 118 | PASS | STABILIZE | 51.0 | 6 | 23 | 2 | 30.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007499999832361937 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 120 | MOVE_BOARD | FAST8 | 39.0 | 6 | 33 | 3 | 30.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3250933289527893 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 122 | MOVE_BENCH | FAST8 | 39.0 | 6 | 44 | 4 | 30.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.061130277812480927 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 123 | MOVE_BENCH | FAST8 | 39.0 | 6 | 44 | 4 | 28.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14500349760055542 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 124 | PASS | FAST8 | 39.0 | 6 | 44 | 4 | 28.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 127 | BUY | STABILIZE | 28.0 | 6 | 56 | 5 | 28.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4220682382583618 | 0.0 | 0.0 | +3a40e3a6-b3e3-4f35-8fa0-e81c89d72db6 / -— |
| Jogador 5 | 3-6 | 128 | REROLL | STABILIZE | 28.0 | 6 | 53 | 5 | 28.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009999999776482582 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 129 | REROLL | STABILIZE | 28.0 | 6 | 51 | 5 | 28.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09200000017881393 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 130 | REROLL | STABILIZE | 28.0 | 6 | 49 | 4 | 28.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 132 | BUY | STABILIZE | 16.0 | 6 | 59 | 5 | 28.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05634495988488197 | 0.0 | 0.0 | +d9fdb961-a3e3-4e39-9970-e46ffd59fc3b / -— |
| Jogador 5 | 3-7 | 133 | BUY | STABILIZE | 16.0 | 6 | 55 | 5 | 28.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9160887598991394 | 0.0 | 0.0 | +fff5cc22-5f1a-47a4-93e3-9772177b0910 / -— |
| Jogador 5 | 3-7 | 134 | BUY | STABILIZE | 16.0 | 6 | 54 | 5 | 28.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0279566440731287 | 0.0 | 0.0 | +dde5ed69-0fc4-4d15-b12c-a5252a239040 / -— |
| Jogador 5 | 3-7 | 135 | REROLL | STABILIZE | 16.0 | 6 | 52 | 5 | 28.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009999999776482582 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 136 | BUY | STABILIZE | 16.0 | 6 | 50 | 5 | 28.0 | Fera do Rift/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.826147198677063 | 0.0 | 0.0 | +7bcf9a7f-a7c9-44a7-9d12-e1ba998b23ed / -— |
| Jogador 5 | 3-7 | 137 | BUY | STABILIZE | 16.0 | 6 | 47 | 4 | 28.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14398548007011414 | 0.0 | 0.0 | +26462e09-ab6e-4b87-85a8-6bda974b0c45 / -— |
| Jogador 5 | 3-7 | 138 | REROLL | STABILIZE | 16.0 | 6 | 44 | 4 | 28.0 | Fera do Rift/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 139 | REROLL | STABILIZE | 16.0 | 6 | 42 | 4 | 28.0 | Fera do Rift/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 141 | PASS | STABILIZE | 16.0 | 6 | 52 | 5 | 28.0 | Fera do Rift/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0005903584533371031 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 151 | PASS | ALL_IN | 2.0 | 6 | 65 | 5 | 28.0 | Fera do Rift/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05662505328655243 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 161 | REROLL | ALL_IN | 2.0 | 6 | 76 | 5 | 28.0 | Fera do Rift/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009999999776482582 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 162 | REROLL | ALL_IN | 2.0 | 6 | 74 | 5 | 28.0 | Fera do Rift/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009999999776482582 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 163 | REROLL | ALL_IN | 2.0 | 6 | 72 | 5 | 28.0 | Fera do Rift/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009999999776482582 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 164 | REROLL | ALL_IN | 2.0 | 6 | 70 | 5 | 28.0 | Fera do Rift/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009999999776482582 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 165 | REROLL | ALL_IN | 2.0 | 6 | 68 | 5 | 28.0 | Fera do Rift/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009999999776482582 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 166 | REROLL | ALL_IN | 2.0 | 6 | 66 | 5 | 28.0 | Fera do Rift/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009999999776482582 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 167 | REROLL | ALL_IN | 2.0 | 6 | 64 | 5 | 28.0 | Fera do Rift/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009999999776482582 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 168 | REROLL | ALL_IN | 2.0 | 6 | 62 | 5 | 28.0 | Fera do Rift/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009999999776482582 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 169 | REROLL | ALL_IN | 2.0 | 6 | 60 | 5 | 28.0 | Fera do Rift/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009999999776482582 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 171 | PASS | ALL_IN | 0.0 | 6 | 58 | 5 | 0.0 | Fera do Rift/DA_CrimsonRaptor18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 181 | PASS | ALL_IN | 0.0 | 6 | 58 | 5 | 0.0 | Fera do Rift/DA_CrimsonRaptor18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 191 | PASS | ALL_IN | 0.0 | 6 | 58 | 5 | 0.0 | Fera do Rift/DA_CrimsonRaptor18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 198 | PASS | ALL_IN | 0.0 | 6 | 58 | 5 | 0.0 | Fera do Rift/DA_CrimsonRaptor18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 202 | PASS | ALL_IN | 0.0 | 6 | 58 | 5 | 0.0 | Fera do Rift/DA_CrimsonRaptor18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 212 | PASS | ALL_IN | 0.0 | 6 | 58 | 5 | 0.0 | Fera do Rift/DA_CrimsonRaptor18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 222 | PASS | ALL_IN | 0.0 | 6 | 58 | 5 | 0.0 | Fera do Rift/DA_CrimsonRaptor18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 232 | PASS | ALL_IN | 0.0 | 6 | 58 | 5 | 0.0 | Fera do Rift/DA_CrimsonRaptor18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 242 | PASS | ALL_IN | 0.0 | 6 | 58 | 5 | 0.0 | Fera do Rift/DA_CrimsonRaptor18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 252 | PASS | ALL_IN | 0.0 | 6 | 58 | 5 | 0.0 | Fera do Rift/DA_CrimsonRaptor18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 262 | PASS | ALL_IN | 0.0 | 6 | 58 | 5 | 0.0 | Fera do Rift/DA_CrimsonRaptor18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 271 | PASS | ALL_IN | 0.0 | 6 | 58 | 5 | 0.0 | Fera do Rift/DA_CrimsonRaptor18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 281 | PASS | ALL_IN | 0.0 | 6 | 58 | 5 | 0.0 | Fera do Rift/DA_CrimsonRaptor18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0013076922623440623 | 0.0 | 0.0 | +— / -698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +9002992e-4dcd-4fec-939c-87393464a41d / -— |
| Jogador 6 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.6080599427223206 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 10 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.04858612269163132 | 0.0 | 0.0 | +4d0bf502-ac30-4cdb-9da7-4f9a7ab054b1 / -— |
| Jogador 6 | 1-2 | 11 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.072932481765747 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5744122862815857 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 13 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 16 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.00015411031199619174 | 0.0 | 0.0 | +c3c53e80-c8e2-4774-afa2-9b0f4ab3b326 / -— |
| Jogador 6 | 1-3 | 17 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4659231901168823 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | -0.29711833596229553 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Teemo | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 25 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 34 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9766854643821716 | 0.0 | 0.0 | +630d9254-3856-4d88-b981-43a8270b4b3d / -— |
| Jogador 6 | 2-1 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5078945755958557 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 36 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.07743781059980392 | 0.0 | 0.0 | +a524fad3-c7d3-4fa7-9c62-1803c8e7c865 / -— |
| Jogador 6 | 2-1 | 37 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 12.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24940909445285797 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 38 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4218795895576477 | 0.0 | 0.0 | +— / -9002992e-4dcd-4fec-939c-87393464a41d |
| Jogador 6 | 2-1 | 39 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1607125997543335 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 40 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 42 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4681698679924011 | 0.0 | 0.0 | +f75a22a6-8a32-4581-8724-bdb7712c21ee / -— |
| Jogador 6 | 2-2 | 43 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17522434890270233 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 44 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00378961069509387 | 0.0 | 0.0 | +— / -4d0bf502-ac30-4cdb-9da7-4f9a7ab054b1 |
| Jogador 6 | 2-2 | 45 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.052000001072883606 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 46 | BUY | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Tristana | BUY, MOVE_BOARD, PASS | True | True | 0.2629634141921997 | 0.0 | 0.0 | +adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 / -— |
| Jogador 6 | 2-2 | 47 | SELL | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31296342611312866 | 0.0 | 0.0 | +— / -adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 |
| Jogador 6 | 2-2 | 48 | BUY | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Tristana | BUY, MOVE_BOARD, PASS | True | True | 0.3027745187282562 | 0.0 | 0.0 | +e9e61ad8-ae9d-4989-8061-94edb3a9bdd5 / -— |
| Jogador 6 | 2-2 | 49 | SELL | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3527745306491852 | 0.0 | 0.0 | +— / -e9e61ad8-ae9d-4989-8061-94edb3a9bdd5 |
| Jogador 6 | 2-2 | 50 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Tristana | MOVE_BOARD, PASS | True | True | 0.09761055558919907 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 52 | BUY | STABILIZE | 96.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9594144821166992 | 0.0 | 0.0 | +92450a29-eacd-4b5f-b3b5-cc8125e4918e / -— |
| Jogador 6 | 2-3 | 53 | BUY | STABILIZE | 96.0 | 5 | 4 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3150123953819275 | 0.0 | 0.0 | +669a8da1-dcc8-403b-a7af-7c96abdc464d / -— |
| Jogador 6 | 2-3 | 54 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7034227252006531 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 55 | SELL | STABILIZE | 96.0 | 5 | 1 | 0 | 20.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06886619329452515 | 0.0 | 0.0 | +— / -630d9254-3856-4d88-b981-43a8270b4b3d |
| Jogador 6 | 2-3 | 56 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 2 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14460977911949158 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 57 | SELL | STABILIZE | 96.0 | 5 | 2 | 0 | 22.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3560769259929657 | 0.0 | 0.0 | +— / -92450a29-eacd-4b5f-b3b5-cc8125e4918e |
| Jogador 6 | 2-3 | 58 | PASS | STABILIZE | 96.0 | 5 | 4 | 0 | 22.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 62 | BUY | STABILIZE | 89.0 | 5 | 10 | 1 | 22.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8776403665542603 | 0.0 | 0.0 | +03a4a455-ebf6-4587-8ab3-acd2b1038822 / -— |
| Jogador 6 | 2-4 | 63 | BUY | STABILIZE | 89.0 | 5 | 7 | 0 | 22.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48644185066223145 | 0.0 | 0.0 | +492fa74a-22b8-4f7d-a4f9-346fdcf565be / -— |
| Jogador 6 | 2-4 | 64 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 6 | 0 | 22.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 65 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 6 | 0 | 22.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4982548654079437 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 66 | BUY_XP | STABILIZE | 89.0 | 5 | 6 | 0 | 28.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 67 | SELL | STABILIZE | 89.0 | 5 | 2 | 0 | 28.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5364418625831604 | 0.0 | 0.0 | +— / -492fa74a-22b8-4f7d-a4f9-346fdcf565be |
| Jogador 6 | 2-4 | 68 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 3 | 0 | 28.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.17996996641159058 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 69 | PASS | STABILIZE | 89.0 | 5 | 3 | 0 | 28.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 72 | BUY_XP | STABILIZE | 89.0 | 5 | 9 | 0 | 28.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 73 | BUY_XP | STABILIZE | 89.0 | 5 | 5 | 0 | 28.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 74 | PASS | STABILIZE | 89.0 | 5 | 1 | 0 | 28.0 | —/DA_18_Tristana | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 82 | BUY | STABILIZE | 89.0 | 6 | 7 | 0 | 28.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9579947590827942 | 0.0 | 0.0 | +1e0a3ead-540d-4169-a1fc-3e79592564a0 / -— |
| Jogador 6 | 2-6 | 83 | MOVE_BENCH | STABILIZE | 89.0 | 6 | 4 | 0 | 28.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40925121307373047 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 84 | MOVE_BENCH | STABILIZE | 89.0 | 6 | 4 | 0 | 28.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6045956015586853 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 85 | BUY_XP | STABILIZE | 89.0 | 6 | 4 | 0 | 34.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 86 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 0 | 0 | 34.0 | —/DA_18_Tristana | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 87 | PASS | STABILIZE | 89.0 | 6 | 0 | 0 | 34.0 | —/DA_18_Tristana | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 90 | BUY_XP | STABILIZE | 89.0 | 6 | 7 | 0 | 34.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 91 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 3 | 0 | 34.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.06348513811826706 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 92 | PASS | STABILIZE | 89.0 | 6 | 3 | 0 | 34.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 94 | PASS | STABILIZE | 89.0 | 6 | 9 | 0 | 34.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 102 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 17 | 1 | 34.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.17367345094680786 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 103 | BUY_XP | STABILIZE | 89.0 | 6 | 17 | 1 | 34.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 104 | BUY_XP | STABILIZE | 89.0 | 6 | 13 | 1 | 34.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 105 | BUY_XP | STABILIZE | 89.0 | 6 | 9 | 0 | 34.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 106 | BUY_XP | STABILIZE | 89.0 | 6 | 5 | 0 | 34.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 107 | PASS | STABILIZE | 89.0 | 6 | 1 | 0 | 34.0 | Vivaz/DA_18_Tristana | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 112 | BUY | STABILIZE | 89.0 | 6 | 8 | 0 | 34.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8339408040046692 | 0.0 | 0.0 | +7e545d27-1847-4016-b42b-e7db1960ae89 / -1e0a3ead-540d-4169-a1fc-3e79592564a0,a524fad3-c7d3-4fa7-9c62-1803c8e7c865 |
| Jogador 6 | 3-3 | 113 | BUY | STABILIZE | 89.0 | 6 | 5 | 0 | 22.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7439841032028198 | 0.0 | 0.0 | +1ff50c59-5133-459e-8bf1-d449c26efabf / -— |
| Jogador 6 | 3-3 | 114 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 2 | 0 | 22.0 | Vivaz/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1795789748430252 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 115 | MOVE_BENCH | STABILIZE | 89.0 | 6 | 2 | 0 | 22.0 | Vivaz/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40081822872161865 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 116 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 2 | 0 | 28.0 | Vivaz/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 117 | MOVE_BENCH | STABILIZE | 89.0 | 6 | 2 | 0 | 28.0 | Vivaz/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6271976232528687 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 118 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 2 | 0 | 40.0 | Vivaz/DA_18_Rammus | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.3433819115161896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 120 | MOVE_BOARD | STABILIZE | 78.0 | 6 | 7 | 0 | 40.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17988646030426025 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 122 | BUY | STABILIZE | 78.0 | 7 | 12 | 1 | 40.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.20398637652397156 | 0.0 | 0.0 | +1726bcae-3006-426c-a6c7-4e317e10b637 / -— |
| Jogador 6 | 3-5 | 123 | BUY | STABILIZE | 78.0 | 7 | 9 | 0 | 40.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009699690155684948 | 0.0 | 0.0 | +a1aa0280-2379-4d0b-a475-143c1a2f6c25 / -— |
| Jogador 6 | 3-5 | 124 | MOVE_BOARD | STABILIZE | 78.0 | 7 | 6 | 0 | 40.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06778689473867416 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 125 | MOVE_BENCH | STABILIZE | 78.0 | 7 | 6 | 0 | 40.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5396533608436584 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 127 | MOVE_BOARD | STABILIZE | 78.0 | 7 | 12 | 1 | 46.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 128 | MOVE_BOARD | STABILIZE | 78.0 | 7 | 12 | 1 | 46.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17439277470111847 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 129 | SELL | STABILIZE | 78.0 | 7 | 12 | 1 | 46.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5014644861221313 | 0.0 | 0.0 | +— / -a1aa0280-2379-4d0b-a475-143c1a2f6c25 |
| Jogador 6 | 3-6 | 130 | BUY_XP | STABILIZE | 78.0 | 7 | 15 | 1 | 46.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 132 | PASS | STABILIZE | 78.0 | 7 | 19 | 1 | 46.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 141 | BUY | STABILIZE | 78.0 | 7 | 26 | 2 | 46.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7697955369949341 | 0.0 | 0.0 | +734c25e1-eddf-4452-a04a-1b39db3b94d0 / -— |
| Jogador 6 | 4-1 | 142 | MOVE_BOARD | STABILIZE | 78.0 | 7 | 23 | 2 | 46.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2859007716178894 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 143 | MOVE_BOARD | STABILIZE | 78.0 | 7 | 23 | 2 | 46.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014000236988067627 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 144 | MOVE_BOARD | STABILIZE | 78.0 | 7 | 23 | 2 | 46.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 145 | MOVE_BOARD | STABILIZE | 78.0 | 7 | 23 | 2 | 46.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3218093812465668 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 146 | PASS | STABILIZE | 78.0 | 7 | 23 | 2 | 46.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 151 | PASS | FAST8 | 78.0 | 7 | 32 | 3 | 46.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 161 | PASS | FAST8 | 66.0 | 7 | 40 | 4 | 46.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04500000178813934 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 171 | REROLL | FAST8 | 66.0 | 7 | 50 | 5 | 46.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 172 | REROLL | FAST8 | 66.0 | 7 | 48 | 4 | 46.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08900000154972076 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 173 | PASS | FAST8 | 66.0 | 7 | 46 | 4 | 46.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 181 | BUY | FAST8 | 66.0 | 7 | 55 | 5 | 46.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9779279232025146 | 0.0 | 0.0 | +a5247b50-831c-4600-bac0-e9bcdfa3ce1c / -1726bcae-3006-426c-a6c7-4e317e10b637,734c25e1-eddf-4452-a04a-1b39db3b94d0 |
| Jogador 6 | 4-5 | 182 | BUY | FAST8 | 66.0 | 7 | 52 | 5 | 40.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8079943060874939 | 0.0 | 0.0 | +bfff6629-3ccc-4136-82a4-319a2fc5350e / -1ff50c59-5133-459e-8bf1-d449c26efabf,f75a22a6-8a32-4581-8724-bdb7712c21ee |
| Jogador 6 | 4-5 | 183 | BUY | FAST8 | 66.0 | 7 | 49 | 4 | 28.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07281117141246796 | 0.0 | 0.0 | +ab6bd13e-9d3a-4a6e-8f99-cd46f301e1d4 / -— |
| Jogador 6 | 4-5 | 184 | BUY | FAST8 | 66.0 | 7 | 46 | 4 | 28.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2880128026008606 | 0.0 | 0.0 | +b053a0fd-0f0b-4343-a920-f0a36d36e771 / -— |
| Jogador 6 | 4-5 | 185 | BUY | FAST8 | 66.0 | 7 | 43 | 4 | 28.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023976851254701614 | 0.0 | 0.0 | +497fbcb9-9d15-43f0-ad71-96eeceeee99d / -— |
| Jogador 6 | 4-5 | 186 | MOVE_BENCH | FAST8 | 66.0 | 7 | 41 | 4 | 28.0 | Vivaz/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19417621195316315 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 187 | MOVE_BOARD | FAST8 | 66.0 | 7 | 41 | 4 | 32.0 | Vivaz/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 188 | MOVE_BOARD | FAST8 | 66.0 | 7 | 41 | 4 | 32.0 | Vivaz/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.179997056722641 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 189 | MOVE_BENCH | FAST8 | 66.0 | 7 | 41 | 4 | 32.0 | Vivaz/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27191486954689026 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 191 | BUY | FAST8 | 53.0 | 7 | 50 | 5 | 44.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.257721483707428 | 0.0 | 0.0 | +a74438d5-726a-4a58-a56d-cda374fddd16 / -— |
| Jogador 6 | 4-6 | 192 | REROLL | FAST8 | 53.0 | 7 | 47 | 4 | 44.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 193 | REROLL | FAST8 | 53.0 | 7 | 45 | 4 | 44.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 194 | BUY | FAST8 | 53.0 | 7 | 43 | 4 | 44.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7603515386581421 | 0.0 | 0.0 | +6b0bead4-2978-41d5-a28d-a4c395f456a7 / -— |
| Jogador 6 | 4-6 | 195 | REROLL | FAST8 | 53.0 | 7 | 40 | 4 | 44.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 196 | MOVE_BENCH | FAST8 | 53.0 | 7 | 38 | 3 | 44.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6393985748291016 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 198 | REROLL | FAST8 | 53.0 | 7 | 47 | 4 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 199 | BUY | FAST8 | 53.0 | 7 | 45 | 4 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3145313858985901 | 0.0 | 0.0 | +b1e222db-5292-4836-a0b4-2fe583bea359 / -— |
| Jogador 6 | 4-7 | 200 | REROLL | FAST8 | 53.0 | 7 | 42 | 4 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 202 | EQUIP_FROM_INVENTORY | FAST8 | 53.0 | 7 | 49 | 4 | 50.0 | Vivaz/DA_18_Rammus | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 203 | REROLL | FAST8 | 53.0 | 7 | 49 | 4 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 204 | REROLL | FAST8 | 53.0 | 7 | 47 | 4 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.08900000154972076 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 205 | REROLL | FAST8 | 53.0 | 7 | 45 | 4 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 206 | REROLL | FAST8 | 53.0 | 7 | 43 | 4 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.08900000154972076 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 207 | REROLL | FAST8 | 53.0 | 7 | 41 | 4 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.15399999916553497 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 208 | REROLL | FAST8 | 53.0 | 7 | 39 | 3 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 209 | REROLL | FAST8 | 53.0 | 7 | 37 | 3 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.08900000154972076 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 210 | REROLL | FAST8 | 53.0 | 7 | 35 | 3 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.08900000154972076 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 212 | REROLL | STABILIZE | 38.0 | 7 | 41 | 4 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 213 | REROLL | STABILIZE | 38.0 | 7 | 39 | 3 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 214 | REROLL | STABILIZE | 38.0 | 7 | 37 | 3 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 215 | REROLL | STABILIZE | 38.0 | 7 | 35 | 3 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 216 | REROLL | STABILIZE | 38.0 | 7 | 33 | 3 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 217 | REROLL | STABILIZE | 38.0 | 7 | 31 | 3 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 218 | REROLL | STABILIZE | 38.0 | 7 | 29 | 2 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 219 | REROLL | STABILIZE | 38.0 | 7 | 27 | 2 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 220 | REROLL | STABILIZE | 38.0 | 7 | 25 | 2 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 222 | REROLL | STABILIZE | 24.0 | 7 | 31 | 3 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 223 | REROLL | STABILIZE | 24.0 | 7 | 29 | 2 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 224 | REROLL | STABILIZE | 24.0 | 7 | 27 | 2 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 225 | REROLL | STABILIZE | 24.0 | 7 | 25 | 2 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 226 | REROLL | STABILIZE | 24.0 | 7 | 23 | 2 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 227 | REROLL | STABILIZE | 24.0 | 7 | 21 | 2 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 228 | REROLL | STABILIZE | 24.0 | 7 | 19 | 1 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 229 | BUY | STABILIZE | 24.0 | 7 | 17 | 1 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7439530491828918 | 0.0 | 0.0 | +bb616470-4b6d-4736-9b6a-8635fb5680b3 / -— |
| Jogador 6 | 5-3 | 230 | BUY | STABILIZE | 24.0 | 7 | 14 | 1 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7375547885894775 | 0.0 | 0.0 | +105550a2-b9bd-4b92-98d8-49d95050f3e1 / -— |
| Jogador 6 | 5-4 | 232 | BUY | STABILIZE | 24.0 | 7 | 18 | 1 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8240649700164795 | 0.0 | 0.0 | +9c09d322-6505-4a72-8964-c0cb94a401cc / -03a4a455-ebf6-4587-8ab3-acd2b1038822,669a8da1-dcc8-403b-a7af-7c96abdc464d |
| Jogador 6 | 5-4 | 233 | BUY | STABILIZE | 24.0 | 7 | 15 | 1 | 38.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.02794908545911312 | 0.0 | 0.0 | +c394b013-3260-4ba0-987e-a784fc42f5e7 / -— |
| Jogador 6 | 5-4 | 234 | REROLL | STABILIZE | 24.0 | 7 | 13 | 1 | 38.0 | Vivaz/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 235 | REROLL | STABILIZE | 24.0 | 7 | 11 | 1 | 38.0 | Vivaz/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 236 | REROLL | STABILIZE | 24.0 | 7 | 9 | 0 | 38.0 | Vivaz/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 237 | REROLL | STABILIZE | 24.0 | 7 | 7 | 0 | 38.0 | Vivaz/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 238 | REROLL | STABILIZE | 24.0 | 7 | 5 | 0 | 38.0 | Vivaz/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 239 | CRAFT_AND_EQUIP | STABILIZE | 24.0 | 7 | 3 | 0 | 38.0 | Vivaz/DA_18_Rammus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.195816308259964 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 240 | MOVE_BENCH | STABILIZE | 24.0 | 7 | 3 | 0 | 38.0 | Vivaz/DA_18_Rammus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30919456481933594 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 242 | REROLL | STABILIZE | 24.0 | 7 | 8 | 0 | 44.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 243 | BUY | STABILIZE | 24.0 | 7 | 6 | 0 | 44.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28399622440338135 | 0.0 | 0.0 | +6f0d0e0e-84ba-49c0-90fb-ac362001c761 / -— |
| Jogador 6 | 5-5 | 244 | REROLL | STABILIZE | 24.0 | 7 | 3 | 0 | 44.0 | Vivaz/DA_18_Rammus | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 245 | MOVE_BOARD | STABILIZE | 24.0 | 7 | 1 | 0 | 44.0 | Vivaz/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24676784873008728 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 246 | PASS | STABILIZE | 24.0 | 7 | 1 | 0 | 44.0 | Vivaz/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 250 | MOVE_BENCH | STABILIZE | 24.0 | 7 | 1 | 0 | 44.0 | Vivaz/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6590908169746399 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 252 | REROLL | STABILIZE | 24.0 | 7 | 6 | 0 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 253 | REROLL | STABILIZE | 24.0 | 7 | 4 | 0 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 254 | REROLL | STABILIZE | 24.0 | 7 | 2 | 0 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 255 | PASS | STABILIZE | 24.0 | 7 | 0 | 0 | 50.0 | Vivaz/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 262 | BUY | ALL_IN | 8.0 | 7 | 5 | 0 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8239773511886597 | 0.0 | 0.0 | +e1042a72-2627-4657-91b5-16187d528031 / -7e545d27-1847-4016-b42b-e7db1960ae89,a5247b50-831c-4600-bac0-e9bcdfa3ce1c,b1e222db-5292-4836-a0b4-2fe583bea359,bb616470-4b6d-4736-9b6a-8635fb5680b3 |
| Jogador 6 | 5-7 | 263 | BUY | ALL_IN | 8.0 | 7 | 2 | 0 | 32.0 | Vivaz/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4861411154270172 | 0.0 | 0.0 | +31e41b33-fbd1-4b09-a17b-c0f1edfa9894 / -— |
| Jogador 6 | 5-7 | 264 | PASS | ALL_IN | 8.0 | 7 | 0 | 0 | 32.0 | Vivaz/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 269 | MOVE_BENCH | ALL_IN | 8.0 | 7 | 0 | 0 | 32.0 | Vivaz/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4337748885154724 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 271 | EQUIP_FROM_INVENTORY | ALL_IN | 8.0 | 7 | 5 | 0 | 50.0 | Vivaz/DA_18_Rammus | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 272 | EQUIP_FROM_INVENTORY | ALL_IN | 8.0 | 7 | 5 | 0 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.005366666708141565 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 273 | REROLL | ALL_IN | 8.0 | 7 | 5 | 0 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 274 | REROLL | ALL_IN | 8.0 | 7 | 3 | 0 | 50.0 | Vivaz/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 275 | PASS | ALL_IN | 8.0 | 7 | 1 | 0 | 50.0 | Vivaz/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 279 | MOVE_BENCH | ALL_IN | 8.0 | 7 | 1 | 0 | 50.0 | Vivaz/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43700161576271057 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 281 | REROLL | ALL_IN | 8.0 | 7 | 6 | 0 | 54.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 282 | REROLL | ALL_IN | 8.0 | 7 | 4 | 0 | 54.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 283 | REROLL | ALL_IN | 8.0 | 7 | 2 | 0 | 54.0 | Vivaz/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 284 | PASS | ALL_IN | 8.0 | 7 | 0 | 0 | 54.0 | Vivaz/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.019615383818745613 | 0.0 | 0.0 | +— / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987 |
| Jogador 7 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +c2a4318c-af60-41e2-8e14-c3ad967569a0 / -— |
| Jogador 7 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.6080599427223206 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 10 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9794912934303284 | 0.0 | 0.0 | +4e206e09-40e3-4699-81cb-8aaf01109dea / -— |
| Jogador 7 | 1-2 | 11 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11205994337797165 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 13 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 16 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.23040270805358887 | 0.0 | 0.0 | +42edb83f-b613-45e2-95e2-d603ddf9d104 / -— |
| Jogador 7 | 1-3 | 17 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23999440670013428 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 18 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Elise | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.731069803237915 | 0.0 | 0.0 | +— / -4e206e09-40e3-4699-81cb-8aaf01109dea |
| Jogador 7 | 1-3 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.12844476103782654 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 20 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3135429620742798 | 0.0 | 0.0 | +734c75dd-d0f3-4b9f-abe8-a228e23557a2 / -— |
| Jogador 7 | 1-3 | 21 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2863163650035858 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3788042664527893 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 23 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_Scuttlecrab18 | MOVE_BOARD, PASS | True | True | 0.10621310770511627 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 25 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 34 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9562528133392334 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 7 | 2-1 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018751053139567375 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 36 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 37 | PASS | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 42 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 11 | 1 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.036966722458601 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 43 | BUY_XP | STABILIZE | 100.0 | 4 | 11 | 1 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 44 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.052000001072883606 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 45 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.27385205030441284 | 0.0 | 0.0 | +475e5206-4f54-4bbb-9db9-99d1895f0887 / -— |
| Jogador 7 | 2-2 | 46 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Hecarim | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17379489541053772 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 47 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 20.0 | —/DA_18_Hecarim | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 48 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 20.0 | —/DA_18_Hecarim | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 52 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.13516078889369965 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 53 | BUY_XP | STABILIZE | 100.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 54 | PASS | STABILIZE | 100.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 62 | BUY | STABILIZE | 100.0 | 5 | 10 | 1 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4039137363433838 | 0.0 | 0.0 | +4b07138d-44fd-4515-8b65-d7db84f4639c / -— |
| Jogador 7 | 2-4 | 63 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 20.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17439620196819305 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 64 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 65 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03610828518867493 | 0.0 | 0.0 | +— / -42edb83f-b613-45e2-95e2-d603ddf9d104 |
| Jogador 7 | 2-4 | 66 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 67 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 24.0 | —/DA_Sentinel18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 72 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03200000151991844 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 73 | PASS | STABILIZE | 100.0 | 6 | 2 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 82 | BUY | STABILIZE | 100.0 | 6 | 9 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4307492673397064 | 0.0 | 0.0 | +60b0249f-e02f-4aca-b90d-75e9bcc822b8 / -— |
| Jogador 7 | 2-6 | 83 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 6 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7258527278900146 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 84 | BUY_XP | ECON | 100.0 | 6 | 6 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 85 | MOVE_BOARD | ECON | 100.0 | 6 | 2 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.06348513811826706 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 86 | MOVE_BOARD | ECON | 100.0 | 6 | 2 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.3370322287082672 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 87 | MOVE_BOARD | ECON | 100.0 | 6 | 2 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 88 | PASS | ECON | 100.0 | 6 | 2 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 90 | BUY_XP | ECON | 100.0 | 6 | 10 | 1 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.20800000429153442 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 91 | BUY_XP | ECON | 100.0 | 6 | 6 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 92 | MOVE_BOARD | ECON | 100.0 | 6 | 2 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.032957449555397034 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 94 | PASS | ECON | 100.0 | 6 | 9 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 102 | PASS | STABILIZE | 91.0 | 6 | 14 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 112 | BUY | STABILIZE | 80.0 | 6 | 21 | 2 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19103747606277466 | 0.0 | 0.0 | +41782483-877e-4dce-bef9-4f1f3d5757bd / -— |
| Jogador 7 | 3-3 | 113 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 19 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1843842715024948 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 114 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 19 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1796598732471466 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 115 | SELL | STABILIZE | 80.0 | 6 | 19 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44309279322624207 | 0.0 | 0.0 | +— / -41782483-877e-4dce-bef9-4f1f3d5757bd |
| Jogador 7 | 3-3 | 116 | BUY_XP | STABILIZE | 80.0 | 6 | 21 | 2 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 117 | BUY_XP | STABILIZE | 80.0 | 6 | 17 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 118 | BUY_XP | STABILIZE | 80.0 | 6 | 13 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.0430000014603138 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 120 | BUY | STABILIZE | 80.0 | 7 | 16 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7419615983963013 | 0.0 | 0.0 | +fa5dc86b-f736-4083-b9df-5cc174b726f2 / -— |
| Jogador 7 | 3-5 | 122 | MOVE_BOARD | STABILIZE | 80.0 | 7 | 19 | 1 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.007139110006392002 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 123 | MOVE_BOARD | STABILIZE | 80.0 | 7 | 19 | 1 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1600322276353836 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 124 | MOVE_BOARD | STABILIZE | 80.0 | 7 | 19 | 1 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.33642056584358215 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 125 | BUY | STABILIZE | 80.0 | 7 | 19 | 1 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2630836069583893 | 0.0 | 0.0 | +a23ee552-279e-4c6c-aa05-6197043e8f1d / -— |
| Jogador 7 | 3-6 | 127 | BUY | STABILIZE | 80.0 | 7 | 24 | 2 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26150941848754883 | 0.0 | 0.0 | +3625f791-4c9f-4b95-bdf7-4a322dcd55d3 / -— |
| Jogador 7 | 3-6 | 128 | BUY | STABILIZE | 80.0 | 7 | 20 | 2 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1683819442987442 | 0.0 | 0.0 | +112206a4-c285-4f76-878a-056248cba468 / -— |
| Jogador 7 | 3-6 | 129 | REROLL | STABILIZE | 80.0 | 7 | 16 | 1 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 130 | BUY | STABILIZE | 80.0 | 7 | 14 | 1 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7419926524162292 | 0.0 | 0.0 | +a8a8381a-f3a8-45ec-9106-293d73fca0c8 / -— |
| Jogador 7 | 3-7 | 132 | BUY | STABILIZE | 80.0 | 7 | 18 | 1 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20681846141815186 | 0.0 | 0.0 | +bf0751f0-8094-4441-adb3-e5f8b4158426 / -— |
| Jogador 7 | 3-7 | 133 | BUY | STABILIZE | 80.0 | 7 | 15 | 1 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0647912323474884 | 0.0 | 0.0 | +0803068a-0141-4e75-ab81-12bb13986025 / -— |
| Jogador 7 | 3-7 | 134 | BUY | STABILIZE | 80.0 | 7 | 12 | 1 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3264021575450897 | 0.0 | 0.0 | +f384fea6-9b6f-4f9c-81ec-a8284d5ba140 / -— |
| Jogador 7 | 3-7 | 135 | REROLL | STABILIZE | 80.0 | 7 | 9 | 0 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 136 | BUY | STABILIZE | 80.0 | 7 | 7 | 0 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04991327226161957 | 0.0 | 0.0 | +d8ecc66e-097d-4caa-a657-90fcd1286c2b / -— |
| Jogador 7 | 3-7 | 137 | REROLL | STABILIZE | 80.0 | 7 | 4 | 0 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 138 | REROLL | STABILIZE | 80.0 | 7 | 2 | 0 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 139 | PASS | STABILIZE | 80.0 | 7 | 0 | 0 | 36.0 | Vanguarda/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 141 | BUY | STABILIZE | 80.0 | 7 | 6 | 0 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8336675763130188 | 0.0 | 0.0 | +9d2d95f2-c079-43eb-a4cd-37b224a473a8 / -60b0249f-e02f-4aca-b90d-75e9bcc822b8,fa5dc86b-f736-4083-b9df-5cc174b726f2 |
| Jogador 7 | 4-1 | 142 | MOVE_BENCH | STABILIZE | 80.0 | 7 | 3 | 0 | 24.0 | Vanguarda/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41958796977996826 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 143 | REROLL | STABILIZE | 80.0 | 7 | 3 | 0 | 30.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 144 | BUY | STABILIZE | 80.0 | 7 | 1 | 0 | 30.0 | Vanguarda/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7478761076927185 | 0.0 | 0.0 | +7fb0217d-521c-42b5-995c-81e299b3b934 / -— |
| Jogador 7 | 4-1 | 145 | MOVE_BOARD | STABILIZE | 80.0 | 7 | 0 | 0 | 30.0 | Vanguarda/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3355177640914917 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 146 | PASS | STABILIZE | 80.0 | 7 | 0 | 0 | 30.0 | Vanguarda/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 149 | MOVE_BENCH | STABILIZE | 80.0 | 7 | 0 | 0 | 30.0 | Vanguarda/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4332445561885834 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 151 | BUY | STABILIZE | 68.0 | 7 | 5 | 0 | 36.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7425491809844971 | 0.0 | 0.0 | +ecf369a7-649e-45fe-ad90-8f29e1714fe6 / -— |
| Jogador 7 | 4-2 | 152 | REROLL | STABILIZE | 68.0 | 7 | 2 | 0 | 36.0 | Vanguarda/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 153 | PASS | STABILIZE | 68.0 | 7 | 0 | 0 | 36.0 | Vanguarda/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 161 | PASS | STABILIZE | 68.0 | 7 | 6 | 0 | 36.0 | Vanguarda/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 171 | REROLL | STABILIZE | 68.0 | 7 | 13 | 1 | 36.0 | Vanguarda/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 172 | PASS | STABILIZE | 68.0 | 7 | 11 | 1 | 36.0 | Vanguarda/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 181 | PASS | STABILIZE | 68.0 | 7 | 18 | 1 | 36.0 | Vanguarda/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 191 | PASS | STABILIZE | 68.0 | 7 | 26 | 2 | 36.0 | Vanguarda/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 198 | PASS | FAST8 | 68.0 | 7 | 35 | 3 | 36.0 | Vanguarda/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 202 | EQUIP_FROM_INVENTORY | FAST8 | 68.0 | 7 | 44 | 4 | 36.0 | Vanguarda/DA_KogMaw18_AD | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 203 | PASS | FAST8 | 68.0 | 7 | 44 | 4 | 36.0 | Vanguarda/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 212 | PASS | FAST8 | 51.0 | 7 | 53 | 5 | 36.0 | Vanguarda/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0009603406069800258 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 222 | PASS | FAST8 | 51.0 | 7 | 64 | 5 | 36.0 | Vanguarda/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.006098646204918623 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 232 | PASS | STABILIZE | 36.0 | 7 | 74 | 5 | 36.0 | Vanguarda/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.011644833721220493 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 242 | PASS | STABILIZE | 36.0 | 7 | 84 | 5 | 36.0 | Vanguarda/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.017687013372778893 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 252 | PASS | STABILIZE | 19.0 | 7 | 95 | 5 | 36.0 | Vanguarda/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.024759097024798393 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 262 | PASS | STABILIZE | 0.0 | 7 | 95 | 5 | 0.0 | Vanguarda/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 271 | PASS | STABILIZE | 0.0 | 7 | 95 | 5 | 0.0 | Vanguarda/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 281 | PASS | STABILIZE | 0.0 | 7 | 95 | 5 | 0.0 | Vanguarda/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 8 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.28737619519233704 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 10 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.054392240941524506 | 0.0 | 0.0 | +fddba3f3-87f3-4c97-a7b2-e5d1ef789709 / -— |
| Jogador 8 | 1-2 | 11 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3687226474285126 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.948853611946106 | 0.0 | 0.0 | +78019889-2624-4adb-917b-619681f23053 / -— |
| Jogador 8 | 1-2 | 13 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0970795527100563 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 14 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 16 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 25 | BUY_XP | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.052000001072883606 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 26 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 34 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1164352893829346 | 0.0 | 0.0 | +23a7be1c-afbc-4200-98c5-f6752ea11e7f / -78019889-2624-4adb-917b-619681f23053,fddba3f3-87f3-4c97-a7b2-e5d1ef789709 |
| Jogador 8 | 2-1 | 35 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 2.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4601512849330902 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 8 | 2-1 | 36 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 2.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3791655898094177 | 0.0 | 0.0 | +— / -23a7be1c-afbc-4200-98c5-f6752ea11e7f |
| Jogador 8 | 2-1 | 37 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37042608857154846 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 38 | PASS | STABILIZE | 100.0 | 4 | 6 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 42 | BUY | STABILIZE | 94.0 | 4 | 11 | 1 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.07039880007505417 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 8 | 2-2 | 43 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 8 | 0 | 4.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.59308260679245 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 44 | BUY_XP | STABILIZE | 94.0 | 4 | 8 | 0 | 8.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 45 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 4 | 0 | 8.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24683719873428345 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 46 | BUY | STABILIZE | 94.0 | 5 | 4 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08447306603193283 | 0.0 | 0.0 | +89740fc1-ac0c-4a0b-9e85-1832d5c3acc4 / -— |
| Jogador 8 | 2-2 | 47 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 2 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.303840309381485 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 48 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 2 | 0 | 8.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1270747184753418 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 49 | PASS | STABILIZE | 94.0 | 5 | 2 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 50 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 2 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14405867457389832 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 52 | BUY | STABILIZE | 94.0 | 5 | 8 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.04466253146529198 | 0.0 | 0.0 | +b0190388-bc3b-43af-b782-94490de9d8b1 / -— |
| Jogador 8 | 2-3 | 53 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 5 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3244592249393463 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 54 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 5 | 0 | 20.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.022383540868759155 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 55 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 5 | 0 | 20.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 56 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 5 | 0 | 20.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.12517163157463074 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 57 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 5 | 0 | 20.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.3048655688762665 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 58 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 5 | 0 | 20.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 59 | PASS | STABILIZE | 94.0 | 5 | 5 | 0 | 20.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 62 | MOVE_BOARD | STABILIZE | 88.0 | 5 | 10 | 1 | 20.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09563779830932617 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 63 | BUY | STABILIZE | 88.0 | 5 | 10 | 1 | 20.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.21313078701496124 | 0.0 | 0.0 | +361c6f8a-301b-43b0-aace-dec56d04bbf1 / -— |
| Jogador 8 | 2-4 | 64 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 7 | 0 | 20.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22730475664138794 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 65 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1247539147734642 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 66 | PASS | STABILIZE | 88.0 | 5 | 7 | 0 | 24.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 72 | BUY_XP | STABILIZE | 88.0 | 5 | 12 | 1 | 24.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 73 | BUY_XP | STABILIZE | 88.0 | 5 | 8 | 0 | 24.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 74 | BUY_XP | STABILIZE | 88.0 | 5 | 4 | 0 | 24.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 75 | SELL | STABILIZE | 88.0 | 5 | 0 | 0 | 24.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011893286369740963 | 0.0 | 0.0 | +— / -561fb9a8-e987-4935-b11c-6c6104ced65d |
| Jogador 8 | 2-5 | 76 | PASS | STABILIZE | 88.0 | 5 | 1 | 0 | 24.0 | —/DA_18_Cassiopeia | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 82 | BUY | STABILIZE | 88.0 | 6 | 7 | 0 | 24.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3716721534729004 | 0.0 | 0.0 | +dca8bf82-80ac-4054-9a77-3891a7de23e2 / -— |
| Jogador 8 | 2-6 | 83 | BUY | STABILIZE | 88.0 | 6 | 3 | 0 | 24.0 | —/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45512858033180237 | 0.0 | 0.0 | +d7649b2a-9868-4fa7-975d-3e4727c8554d / -— |
| Jogador 8 | 2-6 | 84 | MOVE_BENCH | STABILIZE | 88.0 | 6 | 0 | 0 | 24.0 | —/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03862304240465164 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 85 | MOVE_BENCH | ECON | 88.0 | 6 | 0 | 0 | 26.0 | —/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5272735953330994 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 86 | MOVE_BOARD | ECON | 88.0 | 6 | 0 | 0 | 32.0 | —/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13247767090797424 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 87 | MOVE_BOARD | ECON | 88.0 | 6 | 0 | 0 | 32.0 | —/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08409585803747177 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 88 | SELL | ECON | 88.0 | 6 | 0 | 0 | 32.0 | —/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5672078728675842 | 0.0 | 0.0 | +— / -d7649b2a-9868-4fa7-975d-3e4727c8554d |
| Jogador 8 | 2-7 | 90 | BUY | ECON | 81.0 | 6 | 8 | 0 | 32.0 | —/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.32079043984413147 | 0.0 | 0.0 | +dc9a3df1-7032-4c92-a919-ca17ae7639ea / -— |
| Jogador 8 | 2-7 | 91 | MOVE_BENCH | ECON | 81.0 | 6 | 5 | 0 | 32.0 | —/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2985508441925049 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 92 | BUY_XP | ECON | 81.0 | 6 | 5 | 0 | 32.0 | —/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 94 | MOVE_BENCH | ECON | 81.0 | 6 | 6 | 0 | 32.0 | —/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29467663168907166 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 95 | BUY | ECON | 81.0 | 6 | 6 | 0 | 30.0 | —/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17966151237487793 | 0.0 | 0.0 | +bb3be648-cee1-4b75-b472-59653324b9bd / -— |
| Jogador 8 | 3-1 | 96 | MOVE_BENCH | ECON | 81.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5253120064735413 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 97 | MOVE_BENCH | STABILIZE | 81.0 | 6 | 2 | 0 | 32.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1406606286764145 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 98 | PASS | STABILIZE | 81.0 | 6 | 2 | 0 | 32.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 102 | BUY_XP | STABILIZE | 81.0 | 6 | 8 | 0 | 32.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 103 | BUY_XP | STABILIZE | 81.0 | 6 | 4 | 0 | 32.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 104 | PASS | STABILIZE | 81.0 | 6 | 0 | 0 | 32.0 | Colosso/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 112 | BUY_XP | STABILIZE | 81.0 | 6 | 7 | 0 | 32.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 113 | PASS | STABILIZE | 81.0 | 6 | 3 | 0 | 32.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 120 | BUY_XP | STABILIZE | 72.0 | 6 | 8 | 0 | 32.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 122 | BUY_XP | STABILIZE | 72.0 | 6 | 9 | 0 | 32.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 123 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 5 | 0 | 32.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38416963815689087 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 124 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 5 | 0 | 38.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14184674620628357 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 125 | BUY_XP | STABILIZE | 72.0 | 7 | 5 | 0 | 40.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 127 | BUY_XP | STABILIZE | 72.0 | 7 | 7 | 0 | 40.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 128 | PASS | STABILIZE | 72.0 | 7 | 3 | 0 | 40.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 132 | BUY_XP | STABILIZE | 59.0 | 7 | 8 | 0 | 40.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 133 | BUY_XP | STABILIZE | 59.0 | 7 | 4 | 0 | 40.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 134 | SELL | STABILIZE | 59.0 | 7 | 0 | 0 | 40.0 | Colosso/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020999999716877937 | 0.0 | 0.0 | +— / -9db562a0-c8a9-4291-8623-b7b6afbf2606 |
| Jogador 8 | 3-7 | 135 | MOVE_BOARD | STABILIZE | 59.0 | 7 | 3 | 0 | 40.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 136 | PASS | STABILIZE | 59.0 | 7 | 3 | 0 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 141 | CRAFT_AND_EQUIP | STABILIZE | 59.0 | 7 | 8 | 0 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | — | 0.10175666958093643 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 142 | PASS | STABILIZE | 59.0 | 7 | 8 | 0 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 151 | MOVE_BOARD | STABILIZE | 59.0 | 7 | 14 | 1 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06863513588905334 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 152 | PASS | STABILIZE | 59.0 | 7 | 14 | 1 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 161 | PASS | STABILIZE | 59.0 | 7 | 22 | 2 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 171 | PASS | STABILIZE | 47.0 | 7 | 29 | 2 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 181 | REROLL | FAST8 | 47.0 | 7 | 36 | 3 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08900000154972076 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 182 | BUY | FAST8 | 47.0 | 7 | 34 | 3 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2596031725406647 | 0.0 | 0.0 | +25029b69-ee52-4788-840e-006ff9e57d5d / -— |
| Jogador 8 | 4-5 | 183 | MOVE_BOARD | FAST8 | 47.0 | 7 | 31 | 3 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 184 | MOVE_BENCH | FAST8 | 47.0 | 7 | 31 | 3 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32469725608825684 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 185 | MOVE_BOARD | FAST8 | 47.0 | 7 | 31 | 3 | 38.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14246121048927307 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 186 | REROLL | FAST8 | 47.0 | 7 | 31 | 3 | 38.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16899999976158142 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 187 | PASS | STABILIZE | 47.0 | 7 | 29 | 2 | 38.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 191 | BUY | STABILIZE | 35.0 | 7 | 37 | 3 | 38.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7975026965141296 | 0.0 | 0.0 | +2ce6c216-8ffa-4f9b-b78a-aed96adfa47b / -— |
| Jogador 8 | 4-6 | 192 | REROLL | STABILIZE | 35.0 | 7 | 34 | 3 | 38.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 193 | REROLL | STABILIZE | 35.0 | 7 | 32 | 3 | 38.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 194 | REROLL | STABILIZE | 35.0 | 7 | 30 | 3 | 38.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 195 | BUY_XP | STABILIZE | 35.0 | 7 | 28 | 2 | 38.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 196 | BUY_XP | STABILIZE | 35.0 | 7 | 24 | 2 | 38.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 198 | BUY_XP | STABILIZE | 23.0 | 7 | 28 | 2 | 38.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 199 | BUY_XP | STABILIZE | 23.0 | 7 | 24 | 2 | 38.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 200 | BUY_XP | STABILIZE | 23.0 | 7 | 20 | 2 | 38.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 202 | EQUIP_FROM_INVENTORY | STABILIZE | 23.0 | 8 | 23 | 2 | 38.0 | Colosso/DA_18_Lillia | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 203 | BUY | STABILIZE | 23.0 | 8 | 23 | 2 | 38.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1447603553533554 | 0.0 | 0.0 | +4aad2eba-6da2-4e1f-8350-7a645cf03109 / -— |
| Jogador 8 | 5-1 | 204 | REROLL | STABILIZE | 23.0 | 8 | 19 | 1 | 38.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 205 | BUY | STABILIZE | 23.0 | 8 | 17 | 1 | 38.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27375268936157227 | 0.0 | 0.0 | +a920ed77-ca29-4616-afba-e4c7759b2d68 / -— |
| Jogador 8 | 5-1 | 206 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 13 | 1 | 38.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.645540177822113 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 207 | BUY_XP | STABILIZE | 23.0 | 8 | 13 | 1 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 208 | BUY_XP | STABILIZE | 23.0 | 8 | 9 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 209 | BUY_XP | STABILIZE | 23.0 | 8 | 5 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 210 | MOVE_BOARD | STABILIZE | 23.0 | 8 | 1 | 0 | 46.0 | Colosso/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0031246859580278397 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 212 | BUY_XP | STABILIZE | 23.0 | 8 | 7 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 213 | PASS | STABILIZE | 23.0 | 8 | 3 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 222 | REROLL | ALL_IN | 6.0 | 8 | 8 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 223 | REROLL | ALL_IN | 6.0 | 8 | 6 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 224 | BUY | ALL_IN | 6.0 | 8 | 4 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7246103286743164 | 0.0 | 0.0 | +c83e0903-8994-4014-b0d6-76d9c26e4b22 / -— |
| Jogador 8 | 5-3 | 225 | PASS | ALL_IN | 6.0 | 8 | 1 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 232 | REROLL | ALL_IN | 6.0 | 8 | 7 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 233 | REROLL | ALL_IN | 6.0 | 8 | 5 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 234 | REROLL | ALL_IN | 6.0 | 8 | 3 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 235 | PASS | ALL_IN | 6.0 | 8 | 1 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 242 | REROLL | ALL_IN | 6.0 | 8 | 6 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 243 | REROLL | ALL_IN | 6.0 | 8 | 4 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 244 | REROLL | ALL_IN | 6.0 | 8 | 2 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 245 | PASS | ALL_IN | 6.0 | 8 | 0 | 0 | 46.0 | Colosso/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 252 | REROLL | ALL_IN | 6.0 | 8 | 7 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 253 | REROLL | ALL_IN | 6.0 | 8 | 5 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 254 | REROLL | ALL_IN | 6.0 | 8 | 3 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 255 | PASS | ALL_IN | 6.0 | 8 | 1 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 262 | REROLL | ALL_IN | 6.0 | 8 | 8 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 263 | REROLL | ALL_IN | 6.0 | 8 | 6 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 264 | REROLL | ALL_IN | 6.0 | 8 | 4 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 265 | REROLL | ALL_IN | 6.0 | 8 | 2 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 266 | PASS | ALL_IN | 6.0 | 8 | 0 | 0 | 46.0 | Colosso/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 271 | EQUIP_FROM_INVENTORY | ALL_IN | 6.0 | 8 | 6 | 0 | 46.0 | Colosso/DA_18_Lillia | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 272 | EQUIP_FROM_INVENTORY | ALL_IN | 6.0 | 8 | 6 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12707078456878662 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 273 | REROLL | ALL_IN | 6.0 | 8 | 6 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 274 | REROLL | ALL_IN | 6.0 | 8 | 4 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 275 | REROLL | ALL_IN | 6.0 | 8 | 2 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 276 | PASS | ALL_IN | 6.0 | 8 | 0 | 0 | 46.0 | Colosso/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 281 | PASS | ALL_IN | 0.0 | 8 | 0 | 0 | 0.0 | Colosso/DA_18_Lillia | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |

O audit_report.json mantém as máscaras brutas, distribuições da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Null indica campo ausente, não zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 166 | 189 | 7 | 11 | 9 | 2 | 31 | 3 | 0 | 0.0 |
- Jogador 1 — gasto por ação: BUY: 79g, BUY_XP: 48g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 62g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 6g, stage 2: 48g, stage 3: 26g, stage 4: 49g, stage 5: 60g, stage 6: 0g
| Jogador 2 | 133 | 145 | 20 | 9 | 3 | 2 | 24 | 3 | 0 | 0.0 |
- Jogador 2 — gasto por ação: BUY: 77g, BUY_XP: 20g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 48g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 6g, stage 2: 49g, stage 3: 41g, stage 4: 49g, stage 5: 0g, stage 6: 0g
| Jogador 3 | 124 | 139 | 4 | 4 | 10 | 1 | 24 | 1 | 0 | 0.0 |
- Jogador 3 — gasto por ação: BUY: 43g, BUY_XP: 48g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 48g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 2g, stage 2: 41g, stage 3: 29g, stage 4: 55g, stage 5: 12g, stage 6: 0g
| Jogador 4 | 150 | 234 | 8 | 18 | 45 | 2 | 0 | 0 | 2 | 56.0 |
- Jogador 4 — gasto por ação: BUY: 42g, BUY_XP: 192g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 1g, stage 2: 37g, stage 3: 57g, stage 4: 55g, stage 5: 52g, stage 6: 32g
| Jogador 5 | 113 | 111 | 16 | 2 | 3 | 1 | 19 | 0 | 58 | 0.0 |
- Jogador 5 — gasto por ação: BUY: 53g, BUY_XP: 20g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 38g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 2g, stage 2: 55g, stage 3: 36g, stage 4: 18g, stage 5: 0g, stage 6: 0g
| Jogador 6 | 169 | 223 | 13 | 13 | 11 | 1 | 46 | 4 | 0 | 54.0 |
- Jogador 6 — gasto por ação: BUY: 83g, BUY_XP: 48g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 92g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 5g, stage 2: 49g, stage 3: 32g, stage 4: 40g, stage 5: 87g, stage 6: 10g
| Jogador 7 | 101 | 119 | 6 | 8 | 9 | 2 | 7 | 3 | 95 | 0.0 |
- Jogador 7 — gasto por ação: BUY: 57g, BUY_XP: 48g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 14g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 6g, stage 2: 48g, stage 3: 52g, stage 4: 13g, stage 5: 0g, stage 6: 0g
| Jogador 8 | 135 | 190 | 10 | 8 | 21 | 1 | 24 | 6 | 0 | 0.0 |
- Jogador 8 — gasto por ação: BUY: 46g, BUY_XP: 96g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 48g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 6g, stage 2: 43g, stage 3: 40g, stage 4: 36g, stage 5: 59g, stage 6: 6g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 1 | 1 | 0 | 0.0% |
| Jogador 2 | 2 | 2 | 0 | 0.0% |
| Jogador 3 | 1 | 1 | 0 | 0.0% |
| Jogador 4 | 1 | 1 | 0 | 0.0% |
| Jogador 5 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 1 | 1 | 0 | 0.0% |

Os detalhes por transição ficam em audit_report.json. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ médio qualidade | Δ estrutural médio | Δ qualidade quando combate positivo | Δ qualidade quando combate negativo |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 166 | 0 | 0 | 166 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ 0.0000 (28 ações), BUY_XP: Δ 0.0000 (12 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (17 ações), MOVE_BOARD: Δ 0.0000 (51 ações), PASS: Δ 0.0000 (21 ações), REROLL: Δ 0.0000 (31 ações), SELL: Δ 0.0000 (4 ações)
| Jogador 2 | 133 | 0 | 0 | 133 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ 0.0000 (33 ações), BUY_XP: Δ 0.0000 (5 ações), MOVE_BENCH: Δ 0.0000 (13 ações), MOVE_BOARD: Δ 0.0000 (25 ações), PASS: Δ 0.0000 (23 ações), REROLL: Δ 0.0000 (24 ações), SELL: Δ 0.0000 (10 ações)
| Jogador 3 | 124 | 0 | 0 | 124 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ 0.0000 (16 ações), BUY_XP: Δ 0.0000 (12 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (11 ações), MOVE_BOARD: Δ 0.0000 (31 ações), PASS: Δ 0.0000 (27 ações), REROLL: Δ 0.0000 (24 ações), SELL: Δ 0.0000 (2 ações)
| Jogador 4 | 150 | 0 | 0 | 150 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ 0.0000 (14 ações), BUY_XP: Δ 0.0000 (48 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0000 (16 ações), MOVE_BOARD: Δ 0.0000 (40 ações), PASS: Δ 0.0000 (25 ações), SELL: Δ 0.0000 (3 ações)
| Jogador 5 | 113 | 0 | 0 | 113 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ 0.0000 (24 ações), BUY_XP: Δ 0.0000 (5 ações), MOVE_BENCH: Δ 0.0000 (20 ações), MOVE_BOARD: Δ 0.0000 (11 ações), PASS: Δ 0.0000 (24 ações), REROLL: Δ 0.0000 (19 ações), SELL: Δ 0.0000 (10 ações)
| Jogador 6 | 169 | 0 | 0 | 169 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ 0.0000 (33 ações), BUY_XP: Δ 0.0000 (12 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0000 (23 ações), MOVE_BOARD: Δ 0.0000 (21 ações), PASS: Δ 0.0000 (21 ações), REROLL: Δ 0.0000 (46 ações), SELL: Δ 0.0000 (9 ações)
| Jogador 7 | 101 | 0 | 0 | 101 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ 0.0000 (21 ações), BUY_XP: Δ 0.0000 (12 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (12 ações), MOVE_BOARD: Δ 0.0000 (16 ações), PASS: Δ 0.0000 (28 ações), REROLL: Δ 0.0000 (7 ações), SELL: Δ 0.0000 (4 ações)
| Jogador 8 | 135 | 0 | 0 | 135 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ 0.0000 (17 ações), BUY_XP: Δ 0.0000 (24 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0000 (22 ações), MOVE_BOARD: Δ 0.0000 (13 ações), PASS: Δ 0.0000 (27 ações), REROLL: Δ 0.0000 (24 ações), SELL: Δ 0.0000 (4 ações)

A pontuação é uma heurística para auditoria, não uma verdade absoluta. Compare-a com recompensas e resultados de combate; correlação não prova causalidade.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 1 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.077 | 0.000 |
| Jogador 1 | 1-3 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 1 | 1-4 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.000 | 0.000 |
| Jogador 1 | 2-1 | 8 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 14% | 5 → 9 | 2 | 4 → 4 | 0.024 | 0.336 |
| Jogador 1 | 2-2 | 7 | 4.000 | 0.000 | 0 → 0 | 1 → 0 | 14% → 14% | 9 → 10 | 7 | 4 → 4 | -0.084 | 0.384 |
| Jogador 1 | 2-3 | 10 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 14% → 18% | 10 → 7 | 13 | 4 → 5 | 0.070 | 0.280 |
| Jogador 1 | 2-4 | 7 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 7 → 9 | 5 | 5 → 5 | -0.008 | 0.000 |
| Jogador 1 | 2-5 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 9 → 6 | 8 | 5 → 6 | 0.024 | -0.464 |
| Jogador 1 | 2-6 | 6 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 21% | 6 → 9 | 5 | 6 → 6 | -0.017 | 0.440 |
| Jogador 1 | 2-7 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 9 → 6 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 3-1 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 6 → 9 | 4 | 6 → 6 | 0.000 | 0.922 |
| Jogador 1 | 3-2 | 10 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 9 → 8 | 8 | 6 → 6 | 0.037 | 0.290 |
| Jogador 1 | 3-3 | 8 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 8 → 11 | 4 | 6 → 7 | -0.111 | 0.363 |
| Jogador 1 | 3-4 | 2 | 8.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 25% | 11 → 13 | 4 | 7 → 7 | -0.037 | 0.000 |
| Jogador 1 | 3-5 | 5 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 25% → 25% | 13 → 16 | 3 | 7 → 7 | 0.010 | -0.535 |
| Jogador 1 | 3-6 | 5 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 16 → 23 | 0 | 7 → 7 | -0.007 | 0.617 |
| Jogador 1 | 3-7 | 8 | 2.000 | 4.000 | 0 → 0 | 2 → 3 | 25% → 25% | 23 → 27 | 3 | 7 → 7 | -0.030 | 0.000 |
| Jogador 1 | 4-1 | 7 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 25% → 25% | 27 → 34 | 0 | 7 → 7 | 0.023 | -0.382 |
| Jogador 1 | 4-2 | 6 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 25% → 25% | 34 → 43 | 0 | 7 → 7 | -0.026 | -0.461 |
| Jogador 1 | 4-3 | 10 | -2.000 | 10.000 | 0 → 0 | 3 → 2 | 25% → 25% | 43 → 41 | 11 | 7 → 7 | 0.067 | -0.263 |
| Jogador 1 | 4-4 | 6 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 25% → 25% | 41 → 45 | 5 | 7 → 7 | -0.010 | 0.000 |
| Jogador 1 | 4-5 | 10 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 25% → 25% | 45 → 42 | 12 | 7 → 7 | 0.009 | 0.291 |
| Jogador 1 | 4-6 | 7 | -8.000 | 20.000 | 0 → 0 | 2 → 1 | 25% → 18% | 42 → 39 | 11 | 7 → 7 | -0.082 | -0.421 |
| Jogador 1 | 4-7 | 4 | 6.000 | 8.000 | 0 → 1 | 1 → 1 | 18% → 18% | 39 → 36 | 10 | 7 → 7 | -0.000 | 0.000 |
| Jogador 1 | 5-1 | 10 | 8.000 | 6.000 | 1 → 1 | 1 → 3 | 18% → 21% | 36 → 26 | 17 | 7 → 7 | -0.005 | -0.270 |
| Jogador 1 | 5-2 | 10 | 8.000 | -8.000 | 1 → 1 | 3 → 3 | 21% → 25% | 26 → 17 | 16 | 7 → 7 | 0.002 | 0.294 |
| Jogador 1 | 5-3 | 10 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 25% → 25% | 17 → 6 | 16 | 7 → 7 | 0.026 | -0.280 |
| Jogador 1 | 5-4 | 5 | 6.000 | 0.000 | 1 → 2 | 3 → 2 | 25% → 25% | 6 → 5 | 6 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 5-5 | 4 | -52.000 | -60.000 | 2 → 0 | 2 → 0 | 25% → 0% | 5 → 0 | 5 | 7 → 7 | -0.004 | -0.712 |
| Jogador 1 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 7 → 7 | 0.000 | 0.000 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 3, COMPOSITION_COMPATIBILITY: 10, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 10; mudanças de composição: 0; posicionamento melhorou em 34 ações e piorou em 34.
- Jogador 1 — estado final: ouro 0, nível 7, vida 0.0, colocação 5.
| Jogador 2 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.067 | 0.000 |
| Jogador 2 | 1-2 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | -0.029 | 0.000 |
| Jogador 2 | 1-3 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 7% → 7% | 3 → 6 | 0 | 3 → 3 | 0.060 | 0.000 |
| Jogador 2 | 1-4 | 9 | 6.000 | 0.000 | 0 → 1 | 1 → 0 | 7% → 11% | 6 → 6 | 4 | 3 → 4 | -0.109 | 0.000 |
| Jogador 2 | 2-1 | 7 | 6.000 | 0.000 | 1 → 1 | 0 → 0 | 11% → 14% | 6 → 7 | 5 | 4 → 4 | 0.021 | 0.366 |
| Jogador 2 | 2-2 | 4 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 14% → 14% | 7 → 6 | 6 | 4 → 4 | 0.000 | -0.632 |
| Jogador 2 | 2-3 | 10 | 2.000 | 0.000 | 1 → 1 | 0 → 0 | 14% → 14% | 6 → 7 | 8 | 4 → 5 | 0.020 | -0.264 |
| Jogador 2 | 2-4 | 10 | 6.000 | 0.000 | 1 → 1 | 0 → 0 | 14% → 18% | 7 → 6 | 7 | 5 → 5 | 0.034 | 0.000 |
| Jogador 2 | 2-5 | 8 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 18% → 18% | 6 → 6 | 10 | 5 → 5 | 0.000 | 0.297 |
| Jogador 2 | 2-6 | 8 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 18% → 18% | 6 → 7 | 6 | 5 → 6 | 0.027 | -0.290 |
| Jogador 2 | 2-7 | 4 | 6.000 | 8.000 | 1 → 1 | 0 → 1 | 18% → 21% | 7 → 5 | 7 | 6 → 6 | -0.037 | 0.000 |
| Jogador 2 | 3-1 | 7 | 0.000 | -8.000 | 1 → 1 | 1 → 1 | 21% → 21% | 5 → 15 | 0 | 6 → 6 | -0.057 | -0.383 |
| Jogador 2 | 3-2 | 6 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 21% → 21% | 15 → 22 | 3 | 6 → 6 | -0.050 | -0.447 |
| Jogador 2 | 3-3 | 7 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 21% → 21% | 22 → 30 | 3 | 6 → 6 | -0.027 | -0.402 |
| Jogador 2 | 3-4 | 2 | 0.000 | 0.000 | 1 → 2 | 1 → 0 | 21% → 18% | 30 → 35 | 3 | 6 → 6 | 0.218 | 0.000 |
| Jogador 2 | 3-5 | 5 | 8.000 | 4.000 | 2 → 2 | 0 → 0 | 18% → 21% | 35 → 38 | 6 | 6 → 6 | 0.027 | -0.570 |
| Jogador 2 | 3-6 | 5 | 0.000 | 6.000 | 2 → 2 | 0 → 0 | 21% → 21% | 38 → 39 | 9 | 6 → 6 | 0.000 | -0.555 |
| Jogador 2 | 3-7 | 9 | 0.000 | 6.000 | 2 → 2 | 0 → 1 | 21% → 21% | 39 → 32 | 17 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 4-1 | 10 | 0.000 | 12.000 | 2 → 2 | 1 → 1 | 21% → 21% | 32 → 20 | 21 | 6 → 6 | -0.006 | -0.276 |
| Jogador 2 | 4-2 | 10 | -6.000 | 12.000 | 2 → 1 | 1 → 1 | 21% → 21% | 20 → 9 | 19 | 6 → 6 | 0.003 | -0.263 |
| Jogador 2 | 4-3 | 7 | -32.000 | -40.000 | 1 → 0 | 1 → 0 | 21% → 0% | 9 → 0 | 9 | 6 → 6 | 0.028 | -0.402 |
| Jogador 2 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 4-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 5-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 8, COMPOSITION_COMPATIBILITY: 15, IMMEDIATE_UPGRADE: 3, NO_IDENTIFIED_STRATEGIC_GAIN: 1, PAIR_POTENTIAL: 6; mudanças de composição: 1; posicionamento melhorou em 25 ações e piorou em 20.
- Jogador 2 — estado final: ouro 0, nível 6, vida 0.0, colocação 8.
| Jogador 3 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.067 | 0.000 |
| Jogador 3 | 1-2 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | -0.008 | 0.000 |
| Jogador 3 | 1-3 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 7% → 7% | 3 → 6 | 0 | 3 → 3 | 0.000 | 0.000 |
| Jogador 3 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 7% → 7% | 6 → 10 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 3 | 2-1 | 6 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 7% → 11% | 10 → 5 | 10 | 4 → 5 | 0.030 | -0.395 |
| Jogador 3 | 2-2 | 6 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 14% | 5 → 8 | 3 | 5 → 5 | 0.018 | -0.405 |
| Jogador 3 | 2-3 | 6 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 8 → 7 | 7 | 5 → 5 | -0.009 | 0.431 |
| Jogador 3 | 2-4 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 7 → 8 | 4 | 5 → 5 | 0.000 | 0.000 |
| Jogador 3 | 2-5 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 8 → 5 | 8 | 5 → 6 | 0.000 | -0.620 |
| Jogador 3 | 2-6 | 5 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 21% | 5 → 9 | 2 | 6 → 6 | -0.055 | 0.492 |
| Jogador 3 | 2-7 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 9 → 10 | 7 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 3-1 | 6 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 10 → 9 | 8 | 6 → 6 | -0.011 | 0.475 |
| Jogador 3 | 3-2 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 9 → 6 | 8 | 6 → 6 | -0.009 | -0.545 |
| Jogador 3 | 3-3 | 8 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 25% | 6 → 6 | 6 | 6 → 7 | 0.005 | 0.379 |
| Jogador 3 | 3-4 | 2 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 25% → 25% | 6 → 8 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 3-5 | 5 | 0.000 | 8.000 | 0 → 0 | 1 → 1 | 25% → 25% | 8 → 9 | 4 | 7 → 7 | 0.012 | -0.545 |
| Jogador 3 | 3-6 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 9 → 15 | 0 | 7 → 7 | 0.000 | -0.669 |
| Jogador 3 | 3-7 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 15 → 22 | 0 | 7 → 7 | -0.002 | 0.000 |
| Jogador 3 | 4-1 | 10 | 0.000 | 16.000 | 0 → 0 | 1 → 2 | 25% → 25% | 22 → 8 | 20 | 7 → 7 | -0.005 | 0.293 |
| Jogador 3 | 4-2 | 9 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 8 → 5 | 8 | 7 → 7 | 0.046 | -0.307 |
| Jogador 3 | 4-3 | 6 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 5 → 7 | 4 | 7 → 7 | -0.095 | 0.497 |
| Jogador 3 | 4-4 | 8 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 7 → 6 | 6 | 7 → 7 | 0.030 | 0.000 |
| Jogador 3 | 4-5 | 8 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 6 → 5 | 6 | 7 → 7 | 0.001 | -0.344 |
| Jogador 3 | 4-6 | 7 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 5 → 7 | 4 | 7 → 7 | 0.006 | -0.412 |
| Jogador 3 | 4-7 | 4 | 0.000 | 10.000 | 0 → 0 | 2 → 2 | 25% → 25% | 7 → 6 | 7 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 5-1 | 5 | 0.000 | 12.000 | 0 → 0 | 2 → 3 | 25% → 25% | 6 → 6 | 6 | 7 → 7 | 0.000 | 0.572 |
| Jogador 3 | 5-2 | 5 | -28.000 | -52.000 | 0 → 0 | 3 → 0 | 25% → 0% | 6 → 0 | 6 | 7 → 7 | -0.065 | -0.570 |
| Jogador 3 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 7 → 7 | 0.000 | 0.000 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 1, COMPOSITION_COMPATIBILITY: 11, PAIR_POTENTIAL: 4; mudanças de composição: 0; posicionamento melhorou em 17 ações e piorou em 18.
- Jogador 3 — estado final: ouro 0, nível 7, vida 0.0, colocação 6.
| Jogador 4 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 4 | 1-2 | 4 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | 0.095 | 0.000 |
| Jogador 4 | 1-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 7% | 3 → 6 | 0 | 3 → 3 | 0.000 | 0.000 |
| Jogador 4 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 7% | 6 → 10 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 4 | 2-1 | 8 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 7% → 11% | 10 → 6 | 9 | 4 → 5 | 0.009 | -0.316 |
| Jogador 4 | 2-2 | 8 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 14% | 6 → 9 | 3 | 5 → 5 | 0.017 | 0.297 |
| Jogador 4 | 2-3 | 7 | 6.000 | 0.000 | 0 → 0 | 1 → 2 | 14% → 18% | 9 → 9 | 7 | 5 → 5 | -0.007 | 0.377 |
| Jogador 4 | 2-4 | 5 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 9 → 15 | 0 | 5 → 5 | 0.011 | 0.000 |
| Jogador 4 | 2-5 | 10 | 6.000 | 0.000 | 0 → 1 | 2 → 1 | 18% → 18% | 15 → 6 | 14 | 5 → 6 | 0.006 | -0.259 |
| Jogador 4 | 2-6 | 6 | 8.000 | 0.000 | 1 → 1 | 1 → 1 | 18% → 21% | 6 → 8 | 4 | 6 → 6 | -0.011 | -0.413 |
| Jogador 4 | 2-7 | 4 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 21% → 21% | 8 → 14 | 0 | 6 → 6 | 0.039 | 0.000 |
| Jogador 4 | 3-1 | 5 | 4.000 | 2.000 | 1 → 1 | 1 → 1 | 21% → 21% | 14 → 18 | 3 | 6 → 6 | 0.009 | -0.535 |
| Jogador 4 | 3-2 | 7 | 0.000 | -2.000 | 1 → 1 | 1 → 0 | 21% → 21% | 18 → 9 | 16 | 6 → 6 | 0.000 | 0.426 |
| Jogador 4 | 3-3 | 4 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 21% → 21% | 9 → 8 | 8 | 6 → 6 | 0.000 | 0.746 |
| Jogador 4 | 3-4 | 2 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 21% → 21% | 8 → 10 | 4 | 6 → 7 | 0.000 | 0.000 |
| Jogador 4 | 3-5 | 5 | 6.000 | 6.000 | 1 → 1 | 0 → 0 | 21% → 25% | 10 → 7 | 10 | 7 → 7 | -0.018 | 0.570 |
| Jogador 4 | 3-6 | 5 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 25% → 25% | 7 → 10 | 4 | 7 → 7 | 0.012 | 0.582 |
| Jogador 4 | 3-7 | 9 | 0.000 | -6.000 | 1 → 1 | 0 → 0 | 25% → 25% | 10 → 7 | 12 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 4-1 | 6 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 25% → 25% | 7 → 11 | 4 | 7 → 7 | -0.002 | 0.481 |
| Jogador 4 | 4-2 | 6 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 25% → 25% | 11 → 12 | 8 | 7 → 7 | -0.004 | 0.489 |
| Jogador 4 | 4-3 | 10 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 25% → 25% | 12 → 9 | 12 | 7 → 8 | 0.002 | 0.280 |
| Jogador 4 | 4-4 | 6 | 6.000 | 0.000 | 1 → 1 | 0 → 1 | 25% → 29% | 9 → 14 | 3 | 8 → 8 | -0.000 | 0.000 |
| Jogador 4 | 4-5 | 6 | 0.000 | 16.000 | 1 → 1 | 1 → 1 | 29% → 29% | 14 → 15 | 8 | 8 → 8 | -0.013 | 0.502 |
| Jogador 4 | 4-6 | 7 | 0.000 | 8.000 | 1 → 1 | 1 → 2 | 29% → 29% | 15 → 12 | 12 | 8 → 8 | -0.001 | 0.434 |
| Jogador 4 | 4-7 | 4 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 29% → 29% | 12 → 12 | 8 | 8 → 8 | 0.009 | 0.000 |
| Jogador 4 | 5-1 | 6 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 29% → 29% | 12 → 9 | 12 | 8 → 8 | 0.000 | 0.514 |
| Jogador 4 | 5-2 | 4 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 29% → 29% | 9 → 10 | 8 | 8 → 8 | 0.000 | 0.734 |
| Jogador 4 | 5-3 | 4 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 29% → 29% | 10 → 10 | 8 | 8 → 8 | 0.000 | 0.000 |
| Jogador 4 | 5-4 | 5 | 8.000 | -8.000 | 1 → 1 | 2 → 2 | 29% → 32% | 10 → 10 | 8 | 8 → 9 | -0.017 | 0.000 |
| Jogador 4 | 5-5 | 4 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 32% → 32% | 10 → 11 | 8 | 9 → 9 | 0.000 | 0.759 |
| Jogador 4 | 5-6 | 4 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 32% → 32% | 11 → 12 | 8 | 9 → 9 | 0.000 | 0.777 |
| Jogador 4 | 5-7 | 2 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 32% → 32% | 12 → 21 | 0 | 9 → 9 | 0.000 | 0.000 |
| Jogador 4 | 6-1 | 10 | 0.000 | -8.000 | 1 → 1 | 2 → 2 | 32% → 32% | 21 → 10 | 24 | 9 → 9 | 0.006 | 0.296 |
| Jogador 4 | 6-2 | 4 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 32% → 32% | 10 → 3 | 8 | 9 → 9 | 0.000 | 0.764 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 1, COMPOSITION_COMPATIBILITY: 8, IMMEDIATE_UPGRADE: 1, PAIR_POTENTIAL: 4; mudanças de composição: 0; posicionamento melhorou em 18 ações e piorou em 19.
- Jogador 4 — estado final: ouro 3, nível 9, vida 70.0, colocação 1.
| Jogador 5 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 5 | 1-2 | 4 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.116 | 0.000 |
| Jogador 5 | 1-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 7% | 2 → 5 | 0 | 3 → 3 | 0.000 | 0.000 |
| Jogador 5 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 7% | 5 → 9 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 5 | 2-1 | 8 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 9 → 5 | 11 | 4 → 4 | -0.096 | -0.303 |
| Jogador 5 | 2-2 | 10 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 5 → 6 | 8 | 4 → 5 | -0.007 | -0.232 |
| Jogador 5 | 2-3 | 8 | 4.000 | 6.000 | 0 → 0 | 0 → 0 | 14% → 18% | 6 → 7 | 5 | 5 → 5 | 0.043 | -0.304 |
| Jogador 5 | 2-4 | 10 | 2.000 | -6.000 | 0 → 0 | 0 → 0 | 18% → 18% | 7 → 9 | 8 | 5 → 5 | -0.068 | 0.000 |
| Jogador 5 | 2-5 | 10 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 9 → 7 | 10 | 5 → 5 | 0.043 | -0.226 |
| Jogador 5 | 2-6 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 7 → 8 | 11 | 5 → 6 | 0.000 | -0.336 |
| Jogador 5 | 2-7 | 4 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 21% | 8 → 13 | 2 | 6 → 6 | -0.184 | 0.000 |
| Jogador 5 | 3-1 | 6 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 21% → 21% | 13 → 19 | 3 | 6 → 6 | 0.185 | -0.447 |
| Jogador 5 | 3-2 | 4 | -2.000 | 2.000 | 0 → 0 | 0 → 0 | 21% → 21% | 19 → 28 | 0 | 6 → 6 | -0.278 | -0.704 |
| Jogador 5 | 3-3 | 8 | 4.000 | 6.000 | 0 → 0 | 0 → 0 | 21% → 21% | 28 → 33 | 5 | 6 → 6 | 0.081 | -0.358 |
| Jogador 5 | 3-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 33 → 44 | 0 | 6 → 6 | -0.324 | 0.000 |
| Jogador 5 | 3-5 | 4 | -2.000 | 2.000 | 0 → 0 | 0 → 0 | 21% → 21% | 44 → 56 | 0 | 6 → 6 | 0.162 | -0.694 |
| Jogador 5 | 3-6 | 5 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 21% → 21% | 56 → 59 | 9 | 6 → 6 | 0.000 | -0.583 |
| Jogador 5 | 3-7 | 9 | 0.000 | 26.000 | 0 → 0 | 0 → 2 | 21% → 21% | 59 → 52 | 19 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-1 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 52 → 65 | 0 | 6 → 6 | 0.000 | -1.466 |
| Jogador 5 | 4-2 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 65 → 76 | 0 | 6 → 6 | 0.000 | 1.406 |
| Jogador 5 | 4-3 | 10 | -28.000 | -48.000 | 0 → 0 | 2 → 0 | 21% → 0% | 76 → 58 | 18 | 6 → 6 | 0.063 | -0.281 |
| Jogador 5 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 58 → 58 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 58 → 58 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 58 → 58 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 58 → 58 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 58 → 58 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 58 → 58 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 58 → 58 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 58 → 58 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 58 → 58 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 58 → 58 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 58 → 58 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 58 → 58 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 58 → 58 | 0 | 6 → 6 | 0.000 | 0.000 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 8, COMPOSITION_COMPATIBILITY: 12, PAIR_POTENTIAL: 4; mudanças de composição: 0; posicionamento melhorou em 10 ações e piorou em 18.
- Jogador 5 — estado final: ouro 58, nível 6, vida 0.0, colocação 7.
| Jogador 6 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.067 | 0.000 |
| Jogador 6 | 1-2 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | -0.183 | 0.000 |
| Jogador 6 | 1-3 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.067 | 0.000 |
| Jogador 6 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 7 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 6 | 2-1 | 8 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 7 → 6 | 8 | 4 → 4 | 0.025 | 0.314 |
| Jogador 6 | 2-2 | 10 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 6 → 6 | 9 | 4 → 5 | 0.012 | -0.226 |
| Jogador 6 | 2-3 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 6 → 10 | 5 | 5 → 5 | 0.003 | -0.323 |
| Jogador 6 | 2-4 | 9 | 6.000 | 0.000 | 0 → 0 | 0 → 1 | 14% → 18% | 10 → 9 | 8 | 5 → 5 | 0.096 | 0.000 |
| Jogador 6 | 2-5 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 9 → 7 | 8 | 5 → 6 | 0.000 | 0.616 |
| Jogador 6 | 2-6 | 7 | 6.000 | 0.000 | 0 → 0 | 1 → 2 | 18% → 21% | 7 → 7 | 7 | 6 → 6 | 0.017 | 0.386 |
| Jogador 6 | 2-7 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 7 → 9 | 4 | 6 → 6 | 0.018 | 0.000 |
| Jogador 6 | 3-1 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 9 → 17 | 0 | 6 → 6 | 0.000 | 1.431 |
| Jogador 6 | 3-2 | 7 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 17 → 8 | 16 | 6 → 6 | -0.011 | 0.414 |
| Jogador 6 | 3-3 | 8 | 6.000 | 0.000 | 0 → 1 | 2 → 2 | 21% → 21% | 8 → 7 | 6 | 6 → 6 | -0.139 | -0.341 |
| Jogador 6 | 3-4 | 2 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 21% → 21% | 7 → 12 | 0 | 6 → 7 | 0.403 | 0.000 |
| Jogador 6 | 3-5 | 5 | 6.000 | 6.000 | 1 → 1 | 2 → 2 | 21% → 25% | 12 → 12 | 6 | 7 → 7 | 0.005 | 0.590 |
| Jogador 6 | 3-6 | 5 | 0.000 | -6.000 | 1 → 1 | 2 → 2 | 25% → 25% | 12 → 19 | 4 | 7 → 7 | 0.083 | 0.570 |
| Jogador 6 | 3-7 | 2 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 19 → 26 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 4-1 | 7 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 25% → 25% | 26 → 32 | 3 | 7 → 7 | -0.126 | 0.407 |
| Jogador 6 | 4-2 | 2 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 25% → 25% | 32 → 40 | 0 | 7 → 7 | 0.000 | -1.382 |
| Jogador 6 | 4-3 | 2 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 25% → 25% | 40 → 50 | 0 | 7 → 7 | 0.000 | 1.492 |
| Jogador 6 | 4-4 | 4 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 25% → 25% | 50 → 55 | 4 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 4-5 | 10 | -2.000 | 18.000 | 1 → 2 | 3 → 1 | 25% → 21% | 55 → 50 | 14 | 7 → 7 | 0.068 | -0.285 |
| Jogador 6 | 4-6 | 7 | 6.000 | 6.000 | 2 → 2 | 1 → 2 | 21% → 25% | 50 → 47 | 12 | 7 → 7 | -0.004 | 0.445 |
| Jogador 6 | 4-7 | 4 | 0.000 | 6.000 | 2 → 2 | 2 → 2 | 25% → 25% | 47 → 49 | 7 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 5-1 | 10 | 0.000 | 0.000 | 2 → 2 | 2 → 2 | 25% → 25% | 49 → 41 | 16 | 7 → 7 | 0.000 | -0.280 |
| Jogador 6 | 5-2 | 10 | 0.000 | 0.000 | 2 → 2 | 2 → 2 | 25% → 25% | 41 → 31 | 18 | 7 → 7 | 0.000 | -0.278 |
| Jogador 6 | 5-3 | 10 | 0.000 | 12.000 | 2 → 2 | 2 → 4 | 25% → 25% | 31 → 18 | 20 | 7 → 7 | 0.000 | 0.296 |
| Jogador 6 | 5-4 | 10 | -6.000 | 10.000 | 2 → 2 | 4 → 3 | 25% → 21% | 18 → 8 | 15 | 7 → 7 | -0.039 | 0.000 |
| Jogador 6 | 5-5 | 7 | 6.000 | 0.000 | 2 → 2 | 3 → 3 | 21% → 25% | 8 → 6 | 7 | 7 → 7 | -0.016 | 0.000 |
| Jogador 6 | 5-6 | 5 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 25% → 25% | 6 → 5 | 6 | 7 → 7 | 0.000 | -0.560 |
| Jogador 6 | 5-7 | 5 | 0.000 | -14.000 | 2 → 2 | 3 → 3 | 25% → 21% | 5 → 5 | 5 | 7 → 7 | 0.014 | 0.000 |
| Jogador 6 | 6-1 | 7 | 4.000 | -4.000 | 2 → 2 | 3 → 3 | 21% → 25% | 5 → 6 | 4 | 7 → 7 | -0.001 | 0.000 |
| Jogador 6 | 6-2 | 5 | -54.000 | -40.000 | 2 → 0 | 3 → 0 | 25% → 0% | 6 → 0 | 6 | 7 → 7 | 0.025 | -0.570 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 5, COMPOSITION_COMPATIBILITY: 13, IMMEDIATE_UPGRADE: 4, NO_IDENTIFIED_STRATEGIC_GAIN: 1, PAIR_POTENTIAL: 10; mudanças de composição: 0; posicionamento melhorou em 22 ações e piorou em 22.
- Jogador 6 — estado final: ouro 0, nível 7, vida 0.0, colocação 2.
| Jogador 7 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.067 | 0.000 |
| Jogador 7 | 1-2 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | -0.029 | 0.000 |
| Jogador 7 | 1-3 | 9 | 6.000 | 0.000 | 0 → 0 | 1 → 0 | 7% → 11% | 3 → 3 | 4 | 3 → 3 | 0.031 | 0.000 |
| Jogador 7 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 7 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 7 | 2-1 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 11% → 14% | 7 → 11 | 2 | 4 → 4 | -0.003 | 0.537 |
| Jogador 7 | 2-2 | 8 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 11 → 7 | 11 | 4 → 5 | -0.007 | 0.323 |
| Jogador 7 | 2-3 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 7 → 10 | 4 | 5 → 5 | 0.049 | 0.689 |
| Jogador 7 | 2-4 | 7 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 10 → 6 | 12 | 5 → 5 | 0.000 | 0.000 |
| Jogador 7 | 2-5 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 6 → 9 | 4 | 5 → 6 | 0.000 | 0.918 |
| Jogador 7 | 2-6 | 8 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 21% | 9 → 10 | 7 | 6 → 6 | -0.080 | 0.357 |
| Jogador 7 | 2-7 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 10 → 9 | 8 | 6 → 6 | 0.009 | 0.000 |
| Jogador 7 | 3-1 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 9 → 14 | 0 | 6 → 6 | 0.000 | -1.294 |
| Jogador 7 | 3-2 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 14 → 21 | 0 | 6 → 6 | 0.000 | -1.363 |
| Jogador 7 | 3-3 | 8 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 21 → 16 | 14 | 6 → 7 | 0.076 | 0.340 |
| Jogador 7 | 3-4 | 2 | 6.000 | 0.000 | 0 → 0 | 1 → 2 | 21% → 25% | 16 → 19 | 3 | 7 → 7 | -0.087 | 0.000 |
| Jogador 7 | 3-5 | 5 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 25% → 25% | 19 → 24 | 3 | 7 → 7 | -0.118 | 0.580 |
| Jogador 7 | 3-6 | 5 | 0.000 | 24.000 | 0 → 0 | 2 → 3 | 25% → 25% | 24 → 18 | 14 | 7 → 7 | 0.000 | 0.590 |
| Jogador 7 | 3-7 | 9 | 0.000 | 24.000 | 0 → 0 | 3 → 3 | 25% → 25% | 18 → 6 | 18 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 4-1 | 8 | 0.000 | 2.000 | 0 → 0 | 3 → 3 | 25% → 25% | 6 → 5 | 6 | 7 → 7 | 0.004 | -0.339 |
| Jogador 7 | 4-2 | 4 | 0.000 | 6.000 | 0 → 0 | 3 → 4 | 25% → 25% | 5 → 6 | 5 | 7 → 7 | 0.000 | 0.733 |
| Jogador 7 | 4-3 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 6 → 13 | 0 | 7 → 7 | 0.000 | 1.417 |
| Jogador 7 | 4-4 | 3 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 13 → 18 | 2 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 4-5 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 18 → 26 | 0 | 7 → 7 | 0.000 | 1.417 |
| Jogador 7 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 26 → 35 | 0 | 7 → 7 | 0.000 | 1.417 |
| Jogador 7 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 35 → 44 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 5-1 | 3 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 44 → 53 | 0 | 7 → 7 | 0.000 | -0.967 |
| Jogador 7 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 53 → 64 | 0 | 7 → 7 | 0.000 | 1.511 |
| Jogador 7 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 64 → 74 | 0 | 7 → 7 | 0.000 | -1.400 |
| Jogador 7 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 74 → 84 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 84 → 95 | 0 | 7 → 7 | 0.000 | -1.400 |
| Jogador 7 | 5-6 | 2 | -36.000 | -62.000 | 0 → 0 | 4 → 0 | 25% → 0% | 95 → 95 | 0 | 7 → 7 | 0.070 | -1.450 |
| Jogador 7 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 95 → 95 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 95 → 95 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 95 → 95 | 0 | 7 → 7 | 0.000 | 0.000 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 5, COMPOSITION_COMPATIBILITY: 9, IMMEDIATE_UPGRADE: 1, PAIR_POTENTIAL: 6; mudanças de composição: 0; posicionamento melhorou em 15 ações e piorou em 12.
- Jogador 7 — estado final: ouro 95, nível 7, vida 0.0, colocação 4.
| Jogador 8 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 8 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.054 | 0.000 |
| Jogador 8 | 1-3 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 5 | 0 | 3 → 3 | 0.000 | 0.000 |
| Jogador 8 | 1-4 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 5 → 5 | 4 | 3 → 4 | 0.000 | 0.000 |
| Jogador 8 | 2-1 | 6 | -2.000 | 0.000 | 0 → 0 | 1 → 0 | 11% → 7% | 5 → 11 | 2 | 4 → 4 | 0.009 | -0.422 |
| Jogador 8 | 2-2 | 10 | 10.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 14% | 11 → 8 | 9 | 4 → 5 | -0.002 | 0.246 |
| Jogador 8 | 2-3 | 9 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 18% | 8 → 10 | 3 | 5 → 5 | -0.056 | -0.276 |
| Jogador 8 | 2-4 | 6 | 4.000 | 2.000 | 0 → 0 | 0 → 0 | 18% → 18% | 10 → 12 | 3 | 5 → 5 | 0.022 | 0.000 |
| Jogador 8 | 2-5 | 6 | 0.000 | -2.000 | 0 → 0 | 0 → 0 | 18% → 18% | 12 → 7 | 12 | 5 → 6 | 0.000 | 0.440 |
| Jogador 8 | 2-6 | 8 | 8.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 21% | 7 → 8 | 7 | 6 → 6 | -0.009 | -0.317 |
| Jogador 8 | 2-7 | 4 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 21% → 21% | 8 → 6 | 7 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 3-1 | 6 | 0.000 | 8.000 | 0 → 0 | 0 → 0 | 21% → 21% | 6 → 8 | 4 | 6 → 6 | 0.018 | 0.477 |
| Jogador 8 | 3-2 | 4 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 8 → 7 | 8 | 6 → 6 | 0.000 | 0.715 |
| Jogador 8 | 3-3 | 3 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 7 → 8 | 4 | 6 → 6 | 0.000 | -0.846 |
| Jogador 8 | 3-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 8 → 9 | 4 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 3-5 | 5 | 8.000 | -8.000 | 0 → 0 | 0 → 0 | 21% → 25% | 9 → 7 | 8 | 6 → 7 | -0.016 | 0.602 |
| Jogador 8 | 3-6 | 3 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 7 → 8 | 4 | 7 → 7 | 0.000 | -0.917 |
| Jogador 8 | 3-7 | 6 | 0.000 | -6.000 | 0 → 0 | 0 → 0 | 25% → 25% | 8 → 8 | 8 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 4-1 | 3 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 8 → 14 | 0 | 7 → 7 | 0.000 | 1.028 |
| Jogador 8 | 4-2 | 3 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 14 → 22 | 0 | 7 → 7 | 0.027 | 0.978 |
| Jogador 8 | 4-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 22 → 29 | 0 | 7 → 7 | 0.000 | -1.332 |
| Jogador 8 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 29 → 36 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 4-5 | 8 | -2.000 | 8.000 | 0 → 0 | 0 → 0 | 25% → 25% | 36 → 37 | 7 | 7 → 7 | 0.073 | -0.333 |
| Jogador 8 | 4-6 | 7 | 0.000 | 6.000 | 0 → 0 | 0 → 1 | 25% → 25% | 37 → 28 | 17 | 7 → 7 | 0.000 | -0.381 |
| Jogador 8 | 4-7 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 28 → 23 | 12 | 7 → 8 | 0.000 | 0.000 |
| Jogador 8 | 5-1 | 10 | 8.000 | 8.000 | 0 → 0 | 1 → 1 | 25% → 29% | 23 → 7 | 22 | 8 → 8 | 0.016 | 0.296 |
| Jogador 8 | 5-2 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 7 → 8 | 4 | 8 → 8 | 0.000 | -0.917 |
| Jogador 8 | 5-3 | 5 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 29% → 29% | 8 → 7 | 7 | 8 → 8 | 0.000 | 0.597 |
| Jogador 8 | 5-4 | 5 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 7 → 6 | 6 | 8 → 8 | 0.000 | 0.000 |
| Jogador 8 | 5-5 | 5 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 6 → 7 | 6 | 8 → 8 | 0.000 | 0.597 |
| Jogador 8 | 5-6 | 5 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 7 → 8 | 6 | 8 → 8 | 0.000 | 0.594 |
| Jogador 8 | 5-7 | 6 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 8 → 6 | 8 | 8 → 8 | 0.000 | 0.000 |
| Jogador 8 | 6-1 | 7 | -46.000 | -28.000 | 0 → 0 | 2 → 0 | 29% → 0% | 6 → 0 | 6 | 8 → 8 | -0.073 | -0.393 |
| Jogador 8 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 8 → 8 | 0.000 | 0.000 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 3, COMPOSITION_COMPATIBILITY: 10, IMMEDIATE_UPGRADE: 1, PAIR_POTENTIAL: 3; mudanças de composição: 0; posicionamento melhorou em 16 ações e piorou em 14.
- Jogador 8 — estado final: ouro 0, nível 8, vida 0.0, colocação 3.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Revertidas ≤1 ação | ≤2 ações | ≤4 ações | Ouro perdido | Upgrades | Vendas core/par | Valor médio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 28 | 4 | 0 | 2 | 2 | 0 | 5 | 3 | 7.3865 |
| Jogador 2 | 33 | 10 | 4 | 4 | 5 | 0 | 3 | 4 | 6.4874 |
| Jogador 3 | 16 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 3.5329 |
| Jogador 4 | 14 | 3 | 0 | 0 | 0 | 0 | 1 | 1 | 3.8935 |
| Jogador 5 | 24 | 10 | 5 | 5 | 5 | 0 | 0 | 4 | 2.7843 |
| Jogador 6 | 33 | 9 | 2 | 2 | 3 | 0 | 4 | 3 | 6.6546 |
| Jogador 7 | 21 | 4 | 0 | 0 | 1 | 0 | 1 | 1 | 4.5744 |
| Jogador 8 | 17 | 4 | 0 | 0 | 0 | 0 | 1 | 2 | 3.3402 |

As classificações detalhadas e cada sequência correlacionada ficam em audit_report.json.
Uma venda sem compra correspondente na janela é UNKNOWN; sequências ambíguas não são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| HIGH | Jogador 1 | 2-2 | 45 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 1 | 2-3 | 56 | SOLD_CORE_UNIT | Venda de 'DA_Vi18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 1 | 2-3 | 56 | PURCHASE_REVERSED | Compra de DA_Vi18 desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 1 | 2-4 | 63 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 1 | 2-6 | 85 | PURCHASE_REVERSED | Compra de DA_18_Alistar desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 5-6 | 261 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_KogMaw18_AD' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 1 | 5-6 | 261 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_CrimsonRaptor18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 1 | 5-6 | 261 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_MasterYi_AD' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 2 | 2-3 | 60 | PURCHASE_REVERSED | Compra de DA_18_Camille desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 2 | 2-5 | 74 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 2 | 2-5 | 76 | PURCHASE_REVERSED | Compra de DA_18_Rammus desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 2 | 2-6 | 84 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 2 | 2-6 | 86 | PURCHASE_REVERSED | Compra de DA_18_Akali_AD desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 2 | 3-1 | 94 | SOLD_CORE_UNIT | Venda de 'DA_Nidalee18_AP' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 2 | 3-1 | 94 | PURCHASE_REVERSED | Compra de DA_Nidalee18_AP desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 3-2 | 103 | PURCHASE_REVERSED | Compra de DA_18_Rammus desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 2 | 3-3 | 113 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Vi18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 2 | 4-4 | 180 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Tristana' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 2 | 4-4 | 180 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Yorick' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 2 | 4-4 | 180 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Ezreal' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 3 | 2-7 | 92 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 3 | 5-3 | 231 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Soraka' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 3 | 5-3 | 231 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Zyra' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 3 | 5-3 | 231 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Malphite' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 4 | 3-2 | 106 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 5 | 2-1 | 38 | SOLD_CORE_UNIT | Venda de 'DA_18_LeBlanc' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 5 | 2-1 | 38 | PURCHASE_REVERSED | Compra de DA_18_LeBlanc desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-2 | 43 | PURCHASE_REVERSED | Compra de DA_18_Rakan desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-2 | 46 | PURCHASE_REVERSED | Compra de DA_18_Camille desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-2 | 48 | PURCHASE_REVERSED | Compra de DA_18_Kobuko desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-4 | 69 | PURCHASE_REVERSED | Compra de DA_18_Elise desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 5 | 2-5 | 73 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 5 | 2-5 | 78 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 5 | 2-6 | 87 | SOLD_CORE_UNIT | Venda de 'DA_18_Azir' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 5 | 4-4 | 180 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_CrimsonRaptor18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 5 | 4-4 | 180 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Ahri' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 5 | 4-4 | 180 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Aphelios' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 6 | 2-1 | 38 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 6 | 2-2 | 47 | PURCHASE_REVERSED | Compra de DA_18_Leona desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 6 | 2-2 | 49 | PURCHASE_REVERSED | Compra de DA_18_Akali_AD desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 6 | 2-3 | 57 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Teemo' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 6 | 2-4 | 67 | PURCHASE_REVERSED | Compra de DA_18_Rakan desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 6 | 3-6 | 129 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 7 | 1-3 | 18 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 7 | 3-3 | 115 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 7 | 5-7 | 270 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_KogMaw18_AD' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 7 | 5-7 | 270 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Sentinel18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 7 | 5-7 | 270 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Morgana' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 8 | 2-1 | 36 | SOLD_CORE_UNIT | Venda de 'DA_18_Leona' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 8 | 2-6 | 88 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 8 | 6-2 | 288 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Lillia' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 8 | 6-2 | 288 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Fiddlesticks18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 8 | 6-2 | 288 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Soraka' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- O JSON estruturado é a fonte primária para estado de decisão, máscaras, política e recompensas; .tft é analisado apenas para jogadores sem sidecar JSON.- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
