# Auditoria da partida TFT

- Arquivos lidos: **8**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Entradas JSON analisadas: **3867**
- Achados: **74**
- CRITICAL: 0 | HIGH: 33 | MEDIUM: 41 | LOW: 0

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 140 | 140 | 140 | 0 | 137 | 0 | 140 | 140 | 136 | 26/10 |
| Jogador 2 | 155 | 155 | 155 | 0 | 155 | 0 | 155 | 155 | 144 | 31/17 |
| Jogador 3 | 125 | 125 | 125 | 0 | 124 | 0 | 125 | 125 | 118 | 29/18 |
| Jogador 4 | 148 | 148 | 148 | 0 | 147 | 0 | 148 | 148 | 141 | 20/11 |
| Jogador 5 | 137 | 137 | 137 | 0 | 137 | 0 | 137 | 137 | 123 | 36/22 |
| Jogador 6 | 139 | 139 | 139 | 0 | 135 | 0 | 139 | 139 | 139 | 25/13 |
| Jogador 7 | 152 | 152 | 152 | 0 | 148 | 0 | 152 | 152 | 151 | 35/20 |
| Jogador 8 | 144 | 144 | 144 | 0 | 140 | 0 | 144 | 144 | 144 | 16/8 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 9 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Ornn | MOVE_BENCH, SELL, PASS | True | True | 0.24171799421310425 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3013512194156647 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4440630376338959 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.9705569744110107 | 0.0 | 0.0 | +679fe281-674a-438b-bdcf-57229a283d44 / -— |
| Jogador 1 | 1-2 | 14 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35434573888778687 | 0.0 | 0.0 | +— / -679fe281-674a-438b-bdcf-57229a283d44 |
| Jogador 1 | 1-2 | 15 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.045960210263729095 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 16 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.2868722975254059 | 0.0 | 0.0 | +cde2c30a-df2c-4275-86ef-e4a4a13a5be1 / -— |
| Jogador 1 | 1-2 | 17 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5337538719177246 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0696701928973198 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 20 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 29 | BUY_XP | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.44200000166893005 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 30 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.9708619713783264 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 31 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35677990317344666 | 0.0 | 0.0 | +— / -c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 1-4 | 32 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.9645202159881592 | 0.0 | 0.0 | +6465b229-8025-4e7d-94de-1cd49fa76167 / -— |
| Jogador 1 | 1-4 | 33 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33262479305267334 | 0.0 | 0.0 | +— / -6465b229-8025-4e7d-94de-1cd49fa76167 |
| Jogador 1 | 1-4 | 34 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 38 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9702284932136536 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -— |
| Jogador 1 | 2-1 | 39 | SELL | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3523384630680084 | 0.0 | 0.0 | +— / -c448b2c1-7854-4c8c-a51b-eca2791eb639 |
| Jogador 1 | 2-1 | 40 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2507373094558716 | 0.0 | 0.0 | +3a74be8d-bf7c-4449-9f1b-d76521e73e6f / -— |
| Jogador 1 | 2-1 | 41 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5330146551132202 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 42 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 45 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4477398693561554 | 0.0 | 0.0 | +7ca9b803-76eb-4283-9648-7f98bfd81149 / -— |
| Jogador 1 | 2-2 | 46 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10129771381616592 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 47 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06146416813135147 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 48 | SELL | STABILIZE | 100.0 | 4 | 6 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009015385061502457 | 0.0 | 0.0 | +— / -cde2c30a-df2c-4275-86ef-e4a4a13a5be1 |
| Jogador 1 | 2-2 | 49 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19200000166893005 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 50 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9508375525474548 | 0.0 | 0.0 | +55332573-18f4-4724-a314-6f978e772207 / -— |
| Jogador 1 | 2-3 | 52 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 8 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.14653614163398743 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 53 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 8 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.028264204040169716 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 54 | BUY_XP | STABILIZE | 100.0 | 5 | 8 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 55 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 56 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Diana | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 62 | BUY_XP | STABILIZE | 94.0 | 5 | 5 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 63 | PASS | STABILIZE | 94.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Diana | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 69 | BUY_XP | STABILIZE | 94.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19200000166893005 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 70 | BUY | STABILIZE | 94.0 | 6 | 2 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.42805665731430054 | 0.0 | 0.0 | +03a4a455-ebf6-4587-8ab3-acd2b1038822 / -— |
| Jogador 1 | 2-5 | 71 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 0 | 0 | 18.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03264440968632698 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 72 | SELL | STABILIZE | 94.0 | 6 | 0 | 0 | 20.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0012567176017910242 | 0.0 | 0.0 | +— / -2718f555-b782-4fea-a68f-31395ad34232 |
| Jogador 1 | 2-5 | 73 | PASS | STABILIZE | 94.0 | 6 | 1 | 0 | 20.0 | —/DA_18_Diana | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 75 | BUY | STABILIZE | 94.0 | 6 | 7 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.027407635003328323 | 0.0 | 0.0 | +f84bb43d-db12-46dd-a15c-28ef8fdb7fa2 / -— |
| Jogador 1 | 2-6 | 76 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 4 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31903594732284546 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 77 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 4 | 0 | 22.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5164386630058289 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 78 | BUY_XP | STABILIZE | 94.0 | 6 | 4 | 0 | 26.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 79 | PASS | STABILIZE | 94.0 | 6 | 0 | 0 | 26.0 | —/DA_18_Diana | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 82 | BUY_XP | STABILIZE | 94.0 | 6 | 7 | 0 | 26.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 83 | PASS | STABILIZE | 94.0 | 6 | 3 | 0 | 26.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 92 | BUY_XP | STABILIZE | 94.0 | 6 | 9 | 0 | 26.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 93 | BUY_XP | STABILIZE | 94.0 | 6 | 5 | 0 | 26.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 94 | PASS | STABILIZE | 94.0 | 6 | 1 | 0 | 26.0 | Defendente/DA_18_Diana | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 102 | BUY_XP | STABILIZE | 82.0 | 6 | 6 | 0 | 26.0 | Defendente/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 103 | PASS | STABILIZE | 82.0 | 6 | 2 | 0 | 26.0 | Defendente/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 112 | BUY_XP | STABILIZE | 82.0 | 6 | 8 | 0 | 26.0 | Defendente/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.421999990940094 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 113 | BUY | STABILIZE | 82.0 | 7 | 4 | 0 | 26.0 | Defendente/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.11903651058673859 | 0.0 | 0.0 | +ac8f2a7d-1627-4aa4-a35b-805bce651b0e / -— |
| Jogador 1 | 3-3 | 114 | MOVE_BENCH | STABILIZE | 82.0 | 7 | 1 | 0 | 26.0 | Defendente/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08913697302341461 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 115 | MOVE_BENCH | STABILIZE | 82.0 | 7 | 1 | 0 | 26.0 | Defendente/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4277469217777252 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 116 | MOVE_BOARD | STABILIZE | 82.0 | 7 | 1 | 0 | 32.0 | Defendente/DA_18_Diana | MOVE_BOARD, PASS | True | True | 0.06863513588905334 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 117 | MOVE_BOARD | STABILIZE | 82.0 | 7 | 1 | 0 | 32.0 | Defendente/DA_18_Diana | MOVE_BOARD, PASS | True | True | 0.016028856858611107 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 118 | MOVE_BOARD | STABILIZE | 82.0 | 7 | 1 | 0 | 32.0 | Defendente/DA_18_Diana | MOVE_BOARD, PASS | True | True | 0.00535556161776185 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 119 | MOVE_BOARD | STABILIZE | 82.0 | 7 | 1 | 0 | 32.0 | Defendente/DA_18_Diana | MOVE_BOARD, PASS | True | True | 0.042065247893333435 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 121 | MOVE_BOARD | STABILIZE | 82.0 | 7 | 8 | 0 | 32.0 | Defendente/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.1251494586467743 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 122 | BUY_XP | STABILIZE | 82.0 | 7 | 8 | 0 | 32.0 | Defendente/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 123 | BUY_XP | STABILIZE | 82.0 | 7 | 4 | 0 | 32.0 | Defendente/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 124 | PASS | STABILIZE | 82.0 | 7 | 0 | 0 | 32.0 | Defendente/DA_18_Diana | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 131 | BUY_XP | STABILIZE | 82.0 | 7 | 6 | 0 | 32.0 | Defendente/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 132 | PASS | STABILIZE | 82.0 | 7 | 2 | 0 | 32.0 | Defendente/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 140 | BUY | STABILIZE | 82.0 | 7 | 9 | 0 | 32.0 | Defendente/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.20403043925762177 | 0.0 | 0.0 | +eab06dbd-05d4-43b6-88f0-e6abb0e83d34 / -— |
| Jogador 1 | 3-7 | 142 | BUY | STABILIZE | 82.0 | 7 | 12 | 1 | 32.0 | Defendente/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006733808200806379 | 0.0 | 0.0 | +210d2415-663d-4768-bbc2-238766c2b863 / -— |
| Jogador 1 | 3-7 | 143 | MOVE_BENCH | STABILIZE | 82.0 | 7 | 7 | 0 | 32.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35267406702041626 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 144 | MOVE_BENCH | STABILIZE | 82.0 | 7 | 7 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09815693646669388 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 145 | MOVE_BENCH | STABILIZE | 82.0 | 7 | 7 | 0 | 34.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07590361684560776 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 146 | MOVE_BENCH | STABILIZE | 82.0 | 7 | 7 | 0 | 32.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37579241394996643 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 147 | PASS | STABILIZE | 82.0 | 7 | 7 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 152 | MOVE_BENCH | STABILIZE | 82.0 | 7 | 13 | 1 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.09907197952270508 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 153 | CRAFT_AND_EQUIP | STABILIZE | 82.0 | 7 | 13 | 1 | 34.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14393454790115356 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 154 | MOVE_BOARD | STABILIZE | 82.0 | 7 | 13 | 1 | 34.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 155 | MOVE_BENCH | STABILIZE | 82.0 | 7 | 13 | 1 | 34.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.041125502437353134 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 156 | MOVE_BOARD | STABILIZE | 82.0 | 7 | 13 | 1 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001785655738785863 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 157 | BUY_XP | STABILIZE | 82.0 | 7 | 13 | 1 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 158 | BUY_XP | STABILIZE | 82.0 | 7 | 9 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 159 | BUY_XP | STABILIZE | 82.0 | 7 | 5 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 160 | MOVE_BOARD | STABILIZE | 82.0 | 7 | 1 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0352528877556324 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 162 | BUY_XP | STABILIZE | 71.0 | 7 | 6 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 163 | MOVE_BOARD | STABILIZE | 71.0 | 7 | 2 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11552552878856659 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 164 | MOVE_BOARD | STABILIZE | 71.0 | 7 | 2 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08541153371334076 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 165 | MOVE_BOARD | STABILIZE | 71.0 | 7 | 2 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1251494586467743 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 166 | MOVE_BOARD | STABILIZE | 71.0 | 7 | 2 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001785655738785863 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 167 | MOVE_BOARD | STABILIZE | 71.0 | 7 | 2 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017798790708184242 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 168 | MOVE_BOARD | STABILIZE | 71.0 | 7 | 2 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02132791094481945 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 169 | SELL | STABILIZE | 71.0 | 7 | 2 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.170275017619133 | 0.0 | 0.0 | +— / -3a74be8d-bf7c-4449-9f1b-d76521e73e6f |
| Jogador 1 | 4-2 | 170 | EQUIP_FROM_INVENTORY | STABILIZE | 71.0 | 7 | 4 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12888529896736145 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 172 | BUY_XP | STABILIZE | 58.0 | 7 | 10 | 1 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 173 | BUY_XP | STABILIZE | 58.0 | 7 | 6 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 174 | SELL | STABILIZE | 58.0 | 7 | 2 | 0 | 36.0 | Defendente/DA_18_Lux_Fae | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.113826684653759 | 0.0 | 0.0 | +— / -210d2415-663d-4768-bbc2-238766c2b863 |
| Jogador 1 | 4-3 | 175 | BUY_XP | STABILIZE | 58.0 | 7 | 7 | 0 | 36.0 | Defendente/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 176 | PASS | STABILIZE | 58.0 | 7 | 3 | 0 | 36.0 | Defendente/DA_Nidalee18_AP | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 180 | BUY | ECON | 58.0 | 8 | 9 | 0 | 36.0 | Defendente/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.21367952227592468 | 0.0 | 0.0 | +e29db20a-6b71-4518-ac7d-1e5d9eb67582 / -— |
| Jogador 1 | 4-5 | 182 | BUY | ECON | 58.0 | 8 | 11 | 1 | 42.0 | Defendente/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08565792441368103 | 0.0 | 0.0 | +9a2edb0f-a3cd-455c-8406-2a7ca80e3bc6 / -— |
| Jogador 1 | 4-5 | 183 | MOVE_BENCH | ECON | 58.0 | 8 | 7 | 0 | 42.0 | Defendente/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2153530716896057 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 184 | MOVE_BENCH | ECON | 58.0 | 8 | 7 | 0 | 44.0 | Defendente/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09083347022533417 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 185 | MOVE_BOARD | ECON | 58.0 | 8 | 7 | 0 | 42.0 | Defendente/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 186 | MOVE_BOARD | ECON | 58.0 | 8 | 7 | 0 | 42.0 | Defendente/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 187 | PASS | ECON | 58.0 | 8 | 7 | 0 | 42.0 | Defendente/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 191 | MOVE_BENCH | ECON | 58.0 | 8 | 12 | 1 | 42.0 | Defendente/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11613821983337402 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 192 | MOVE_BENCH | ECON | 58.0 | 8 | 12 | 1 | 42.0 | Defendente/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08277828246355057 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 193 | MOVE_BENCH | ECON | 58.0 | 8 | 12 | 1 | 44.0 | Defendente/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17408007383346558 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 194 | MOVE_BOARD | ECON | 58.0 | 8 | 12 | 1 | 42.0 | Defendente/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02022671326994896 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 195 | MOVE_BOARD | ECON | 58.0 | 8 | 12 | 1 | 42.0 | Defendente/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 196 | MOVE_BOARD | ECON | 58.0 | 8 | 12 | 1 | 42.0 | Defendente/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13205914199352264 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 197 | PASS | ECON | 58.0 | 8 | 12 | 1 | 42.0 | Defendente/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 201 | BUY | ECON | 46.0 | 8 | 18 | 1 | 42.0 | Defendente/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10323244333267212 | 0.0 | 0.0 | +3b98edb7-348f-47b4-85fd-66ee3f1a7af5 / -— |
| Jogador 1 | 4-7 | 202 | MOVE_BOARD | ECON | 46.0 | 8 | 14 | 1 | 42.0 | Defendente/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22315895557403564 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 203 | MOVE_BENCH | ECON | 46.0 | 8 | 14 | 1 | 42.0 | Defendente/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4456649720668793 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 204 | PASS | ECON | 46.0 | 8 | 14 | 1 | 44.0 | Defendente/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 211 | EQUIP_FROM_INVENTORY | ECON | 46.0 | 8 | 20 | 2 | 44.0 | Defendente/DA_Nidalee18_AP | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 212 | BUY | ECON | 46.0 | 8 | 20 | 2 | 44.0 | Defendente/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03739284351468086 | 0.0 | 0.0 | +4cae9d83-6cc8-4a27-9c17-2e6f45091477 / -— |
| Jogador 1 | 5-1 | 213 | MOVE_BOARD | ECON | 46.0 | 8 | 15 | 1 | 44.0 | Defendente/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3094820976257324 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 214 | PASS | ECON | 46.0 | 8 | 15 | 1 | 44.0 | Defendente/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 220 | REROLL | ECON | 46.0 | 8 | 22 | 2 | 44.0 | Defendente/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19719457626342773 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 222 | REROLL | STABILIZE | 31.0 | 8 | 27 | 2 | 44.0 | Defendente/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1573108583688736 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 223 | REROLL | STABILIZE | 31.0 | 8 | 25 | 2 | 44.0 | Defendente/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16971617937088013 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 224 | REROLL | STABILIZE | 31.0 | 8 | 23 | 2 | 44.0 | Defendente/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17329995334148407 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 225 | REROLL | STABILIZE | 31.0 | 8 | 21 | 2 | 44.0 | Defendente/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0026081660762429237 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 226 | BUY | STABILIZE | 31.0 | 8 | 19 | 1 | 44.0 | Defendente/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.722450852394104 | 0.0 | 0.0 | +da4921b5-0ae7-4339-b38b-6ebce7412120 / -— |
| Jogador 1 | 5-3 | 227 | BUY | STABILIZE | 31.0 | 8 | 15 | 1 | 44.0 | Defendente/DA_18_Lux_Primal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8278942108154297 | 0.0 | 0.0 | +64b3ef70-cd08-48bc-95a8-e85929176d5c / -da4921b5-0ae7-4339-b38b-6ebce7412120,eab06dbd-05d4-43b6-88f0-e6abb0e83d34 |
| Jogador 1 | 5-3 | 228 | REROLL | STABILIZE | 31.0 | 8 | 11 | 1 | 36.0 | Defendente/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2459721714258194 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 229 | BUY | STABILIZE | 31.0 | 8 | 9 | 0 | 36.0 | Defendente/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2566070556640625 | 0.0 | 0.0 | +89e25847-d3e0-49a3-ba5b-4cd00ba7c8b6 / -— |
| Jogador 1 | 5-3 | 230 | MOVE_BENCH | STABILIZE | 31.0 | 8 | 5 | 0 | 36.0 | Defendente/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5711861848831177 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 232 | BUY | ALL_IN | 15.0 | 8 | 11 | 1 | 42.0 | Defendente/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22422271966934204 | 0.0 | 0.0 | +f88e593a-bc21-43b4-afac-fdfb5c3afb35 / -— |
| Jogador 1 | 5-4 | 233 | BUY | ALL_IN | 15.0 | 8 | 6 | 0 | 42.0 | Defendente/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48016807436943054 | 0.0 | 0.0 | +35f90973-e578-4be1-aaa5-9ee8073b0776 / -— |
| Jogador 1 | 5-4 | 234 | BUY | ALL_IN | 15.0 | 8 | 3 | 0 | 42.0 | Defendente/DA_Nidalee18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.058612897992134094 | 0.0 | 0.0 | +29eeef02-9b0a-480b-aca7-9e423ecddd3a / -— |
| Jogador 1 | 5-4 | 235 | BUY | ALL_IN | 15.0 | 8 | 1 | 0 | 42.0 | Defendente/DA_Nidalee18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04887602478265762 | 0.0 | 0.0 | +28a81cd3-1f8b-4a3f-93c1-9bbcd7487867 / -— |
| Jogador 1 | 5-4 | 236 | PASS | ALL_IN | 15.0 | 8 | 0 | 0 | 42.0 | Defendente/DA_Nidalee18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 242 | BUY | ALL_IN | 15.0 | 8 | 6 | 0 | 42.0 | Defendente/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2124631404876709 | 0.0 | 0.0 | +8866c8fb-a7fe-4299-b2fd-e967adcedb74 / -— |
| Jogador 1 | 5-5 | 243 | REROLL | ALL_IN | 15.0 | 8 | 2 | 0 | 42.0 | Defendente/DA_Nidalee18_AP | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 244 | PASS | ALL_IN | 15.0 | 8 | 0 | 0 | 42.0 | Defendente/DA_Nidalee18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 252 | PASS | ALL_IN | 0.0 | 8 | 0 | 0 | 0.0 | Defendente/DA_Nidalee18_AP | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 262 | PASS | ALL_IN | 0.0 | 8 | 0 | 0 | 0.0 | Defendente/DA_Nidalee18_AP | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 272 | PASS | ALL_IN | 0.0 | 8 | 0 | 0 | 0.0 | Defendente/DA_Nidalee18_AP | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 282 | PASS | ALL_IN | 0.0 | 8 | 0 | 0 | 0.0 | Defendente/DA_Nidalee18_AP | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.04556922987103462 | 0.0 | 0.0 | +— / -fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.22450661659240723 | 0.0 | 0.0 | +292ef825-d326-4dd8-9c42-c47cfc62116f / -— |
| Jogador 2 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.5933380722999573 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9709054827690125 | 0.0 | 0.0 | +94ede66e-59bc-4c41-aabf-f64372e20f9a / -— |
| Jogador 2 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 13 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11205994337797165 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 14 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 20 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.12844476103782654 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 21 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 29 | BUY | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1178797483444214 | 0.0 | 0.0 | +0023ba20-d605-41fb-8002-3b6920635c59 / -292ef825-d326-4dd8-9c42-c47cfc62116f,94ede66e-59bc-4c41-aabf-f64372e20f9a |
| Jogador 2 | 1-4 | 30 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 5 | 0 | 0.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, SELL, PASS | True | True | 0.5940914154052734 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.15138649940490723 | 0.0 | 0.0 | +9a6f90da-bbac-4ba0-b2a3-729a1a2deab5 / -— |
| Jogador 2 | 1-4 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7026370167732239 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 33 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5991480350494385 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 34 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.17199330031871796 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 35 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0014813457382842898 | 0.0 | 0.0 | +43759c90-bd65-4632-8aa4-56ab63ae84fe / -— |
| Jogador 2 | 1-4 | 36 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4149007499217987 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 38 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.35148903727531433 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 39 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3874405324459076 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 40 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 41 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1618809700012207 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 42 | REROLL | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.14551736414432526 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 43 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 16.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 45 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 46 | REROLL | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.13960744440555573 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 47 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 16.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 52 | BUY | STABILIZE | 94.0 | 4 | 6 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2929304838180542 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 2 | 2-3 | 53 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08038465678691864 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 54 | SELL | STABILIZE | 94.0 | 4 | 3 | 0 | 18.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.037092842161655426 | 0.0 | 0.0 | +— / -9a6f90da-bbac-4ba0-b2a3-729a1a2deab5 |
| Jogador 2 | 2-3 | 55 | BUY_XP | STABILIZE | 94.0 | 4 | 5 | 0 | 18.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.44200000166893005 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 56 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.03786883130669594 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 57 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 58 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.11892727017402649 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 59 | BUY | STABILIZE | 94.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | -0.026268232613801956 | 0.0 | 0.0 | +ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 / -— |
| Jogador 2 | 2-3 | 60 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4626002609729767 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 62 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 6 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.16541512310504913 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 63 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 6 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.3092462718486786 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 64 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 6 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09273318946361542 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 65 | BUY | STABILIZE | 94.0 | 5 | 6 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3906219005584717 | 0.0 | 0.0 | +86c535a4-a22b-4667-bc0f-46b4843d97cc / -— |
| Jogador 2 | 2-4 | 66 | SELL | STABILIZE | 94.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10550769418478012 | 0.0 | 0.0 | +— / -86c535a4-a22b-4667-bc0f-46b4843d97cc |
| Jogador 2 | 2-4 | 67 | BUY_XP | STABILIZE | 94.0 | 5 | 6 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 69 | BUY_XP | STABILIZE | 94.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 70 | REROLL | STABILIZE | 94.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1446780562400818 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 71 | PASS | STABILIZE | 94.0 | 5 | 1 | 0 | 20.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 75 | BUY_XP | STABILIZE | 94.0 | 5 | 8 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19200000166893005 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 76 | BUY | STABILIZE | 94.0 | 6 | 4 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.5210701823234558 | 0.0 | 0.0 | +ae570779-3ae8-49b3-acdb-607fc512fcea / -— |
| Jogador 2 | 2-6 | 77 | SELL | STABILIZE | 94.0 | 6 | 3 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14929378032684326 | 0.0 | 0.0 | +— / -ae570779-3ae8-49b3-acdb-607fc512fcea |
| Jogador 2 | 2-6 | 78 | BUY | STABILIZE | 94.0 | 6 | 4 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3810861110687256 | 0.0 | 0.0 | +53312511-4e10-4904-82c0-8a8e69c039cd / -— |
| Jogador 2 | 2-6 | 79 | SELL | STABILIZE | 94.0 | 6 | 3 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02452307753264904 | 0.0 | 0.0 | +— / -53312511-4e10-4904-82c0-8a8e69c039cd |
| Jogador 2 | 2-6 | 80 | BUY | STABILIZE | 94.0 | 6 | 4 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.31574538350105286 | 0.0 | 0.0 | +b6a21130-c9dc-45ad-8ddb-9223b0ec8751 / -— |
| Jogador 2 | 2-7 | 82 | BUY | STABILIZE | 94.0 | 6 | 10 | 1 | 22.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8874008655548096 | 0.0 | 0.0 | +46838f8d-8037-485c-8c34-9639f14ada19 / -— |
| Jogador 2 | 2-7 | 83 | BUY | STABILIZE | 94.0 | 6 | 7 | 0 | 22.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34916073083877563 | 0.0 | 0.0 | +c5593e47-f48a-4362-b230-dfa3d7d36ec9 / -— |
| Jogador 2 | 2-7 | 84 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 3 | 0 | 22.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14800184965133667 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 85 | SELL | STABILIZE | 94.0 | 6 | 3 | 0 | 22.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0311040747910738 | 0.0 | 0.0 | +— / -3eefd13b-5716-4917-a616-c3589f115098 |
| Jogador 2 | 2-7 | 86 | SELL | STABILIZE | 94.0 | 6 | 6 | 0 | 22.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3991607129573822 | 0.0 | 0.0 | +— / -c5593e47-f48a-4362-b230-dfa3d7d36ec9 |
| Jogador 2 | 2-7 | 87 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 10 | 1 | 22.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06491690129041672 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 88 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 10 | 1 | 22.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.006247489247471094 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 89 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 10 | 1 | 22.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.16336657106876373 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 90 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 10 | 1 | 22.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.15982767939567566 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 92 | BUY | STABILIZE | 94.0 | 6 | 17 | 1 | 22.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.10174001753330231 | 0.0 | 0.0 | +f7526b6b-8c94-4229-bd3f-1e538c769fec / -— |
| Jogador 2 | 3-1 | 93 | BUY | STABILIZE | 94.0 | 6 | 15 | 1 | 22.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7047673463821411 | 0.0 | 0.0 | +e8c36276-b932-45ba-b350-2d1cb339a019 / -— |
| Jogador 2 | 3-1 | 94 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 13 | 1 | 22.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 95 | SELL | STABILIZE | 94.0 | 6 | 13 | 1 | 22.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47319743037223816 | 0.0 | 0.0 | +— / -f7526b6b-8c94-4229-bd3f-1e538c769fec |
| Jogador 2 | 3-1 | 96 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 15 | 1 | 22.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1381131112575531 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 97 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 15 | 1 | 22.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17881269752979279 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 98 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 15 | 1 | 22.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 99 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 15 | 1 | 22.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32791614532470703 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 100 | PASS | STABILIZE | 94.0 | 6 | 15 | 1 | 22.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 102 | BUY | STABILIZE | 83.0 | 6 | 21 | 2 | 22.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20825403928756714 | 0.0 | 0.0 | +d218597b-b641-4a4c-867a-41227b83fcff / -— |
| Jogador 2 | 3-2 | 103 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 18 | 1 | 22.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 104 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 18 | 1 | 22.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11919979751110077 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 105 | SELL | STABILIZE | 83.0 | 6 | 18 | 1 | 22.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1331402063369751 | 0.0 | 0.0 | +— / -e8c36276-b932-45ba-b350-2d1cb339a019 |
| Jogador 2 | 3-2 | 106 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 20 | 2 | 22.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18302759528160095 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 107 | SELL | STABILIZE | 83.0 | 6 | 20 | 2 | 26.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1049748957157135 | 0.0 | 0.0 | +— / -b6a21130-c9dc-45ad-8ddb-9223b0ec8751 |
| Jogador 2 | 3-2 | 108 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 21 | 2 | 26.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.002083240309730172 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 109 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 21 | 2 | 26.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.2596094608306885 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 110 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 21 | 2 | 26.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 112 | BUY | STABILIZE | 72.0 | 6 | 29 | 2 | 26.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.040872178971767426 | 0.0 | 0.0 | +8a4e95ea-d35a-4690-9313-126b5d86773e / -— |
| Jogador 2 | 3-3 | 113 | SELL | STABILIZE | 72.0 | 6 | 26 | 2 | 26.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12911181151866913 | 0.0 | 0.0 | +— / -8a4e95ea-d35a-4690-9313-126b5d86773e |
| Jogador 2 | 3-3 | 114 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 29 | 2 | 26.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1448899805545807 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 115 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 29 | 2 | 26.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.1381131112575531 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 116 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 29 | 2 | 26.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.127062126994133 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 117 | PASS | STABILIZE | 72.0 | 6 | 29 | 2 | 26.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 121 | BUY | SLOWROLL | 61.0 | 6 | 37 | 3 | 26.0 | Vivaz/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8029951453208923 | 0.0 | 0.0 | +d056a271-6a74-4e71-bde6-087b97d2c527 / -46838f8d-8037-485c-8c34-9639f14ada19,9db562a0-c8a9-4291-8623-b7b6afbf2606 |
| Jogador 2 | 3-4 | 122 | BUY | SLOWROLL | 61.0 | 6 | 34 | 3 | 14.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7125524282455444 | 0.0 | 0.0 | +333cdd27-0114-4d36-8ffa-e79b0f43b8e8 / -— |
| Jogador 2 | 3-4 | 123 | BUY | SLOWROLL | 61.0 | 6 | 33 | 3 | 14.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28722742199897766 | 0.0 | 0.0 | +2ed895f2-1e83-426c-88fc-b9fb6403835d / -— |
| Jogador 2 | 3-4 | 124 | MOVE_BOARD | SLOWROLL | 61.0 | 6 | 30 | 3 | 14.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08120239526033401 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 125 | MOVE_BOARD | SLOWROLL | 61.0 | 6 | 30 | 3 | 14.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 126 | MOVE_BOARD | SLOWROLL | 61.0 | 6 | 30 | 3 | 14.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12034890055656433 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 127 | PASS | SLOWROLL | 61.0 | 6 | 30 | 3 | 14.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 129 | MOVE_BENCH | SLOWROLL | 61.0 | 6 | 30 | 3 | 14.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38043123483657837 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 131 | MOVE_BOARD | SLOWROLL | 61.0 | 6 | 39 | 3 | 26.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30833667516708374 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 132 | MOVE_BOARD | SLOWROLL | 61.0 | 6 | 39 | 3 | 26.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009149251505732536 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 133 | MOVE_BOARD | SLOWROLL | 61.0 | 6 | 39 | 3 | 26.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005840805824846029 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 134 | MOVE_BOARD | SLOWROLL | 61.0 | 6 | 39 | 3 | 26.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07924482971429825 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 135 | MOVE_BOARD | SLOWROLL | 61.0 | 6 | 39 | 3 | 26.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17909494042396545 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 136 | SELL | SLOWROLL | 61.0 | 6 | 39 | 3 | 26.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14570222795009613 | 0.0 | 0.0 | +— / -2ed895f2-1e83-426c-88fc-b9fb6403835d |
| Jogador 2 | 3-5 | 137 | SELL | SLOWROLL | 61.0 | 6 | 42 | 4 | 26.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3666348159313202 | 0.0 | 0.0 | +— / -333cdd27-0114-4d36-8ffa-e79b0f43b8e8 |
| Jogador 2 | 3-5 | 138 | MOVE_BOARD | SLOWROLL | 61.0 | 6 | 43 | 4 | 26.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.3235703110694885 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 140 | BUY | SLOWROLL | 48.0 | 6 | 53 | 5 | 26.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.0703008770942688 | 0.0 | 0.0 | +0d693604-37ed-4f64-9a87-ded68f8a2dea / -— |
| Jogador 2 | 3-7 | 142 | BUY | STABILIZE | 37.0 | 6 | 62 | 5 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.44654208421707153 | 0.0 | 0.0 | +60255a84-4f78-49f0-a4f1-d598704c7ee7 / -— |
| Jogador 2 | 3-7 | 143 | MOVE_BOARD | STABILIZE | 37.0 | 6 | 59 | 5 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16253557801246643 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 144 | REROLL | STABILIZE | 37.0 | 6 | 59 | 5 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18862198293209076 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 145 | BUY | STABILIZE | 37.0 | 6 | 57 | 5 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38850197196006775 | 0.0 | 0.0 | +93f7279f-b03b-407b-b623-c0a2bd88f877 / -— |
| Jogador 2 | 3-7 | 146 | REROLL | STABILIZE | 37.0 | 6 | 55 | 5 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22854436933994293 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 147 | REROLL | STABILIZE | 37.0 | 6 | 53 | 5 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1667744666337967 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 148 | REROLL | STABILIZE | 37.0 | 6 | 51 | 5 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2518492639064789 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 149 | REROLL | STABILIZE | 37.0 | 6 | 49 | 4 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1730615198612213 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 150 | REROLL | STABILIZE | 37.0 | 6 | 47 | 4 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2047852873802185 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 152 | BUY | STABILIZE | 37.0 | 6 | 56 | 5 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23097217082977295 | 0.0 | 0.0 | +e4764e13-e26d-4358-980a-c7c625e26726 / -— |
| Jogador 2 | 4-1 | 153 | REROLL | STABILIZE | 37.0 | 6 | 53 | 5 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24733547866344452 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 154 | REROLL | STABILIZE | 37.0 | 6 | 51 | 5 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2517465054988861 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 155 | REROLL | STABILIZE | 37.0 | 6 | 49 | 4 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19618290662765503 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 156 | REROLL | STABILIZE | 37.0 | 6 | 47 | 4 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17344698309898376 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 157 | REROLL | STABILIZE | 37.0 | 6 | 45 | 4 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2004888504743576 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 158 | REROLL | STABILIZE | 37.0 | 6 | 43 | 4 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 159 | REROLL | STABILIZE | 37.0 | 6 | 41 | 4 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10411924868822098 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 160 | REROLL | STABILIZE | 37.0 | 6 | 39 | 3 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2054060995578766 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 162 | REROLL | STABILIZE | 23.0 | 6 | 48 | 4 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25072625279426575 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 163 | REROLL | STABILIZE | 23.0 | 6 | 46 | 4 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 164 | BUY | STABILIZE | 23.0 | 6 | 44 | 4 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8973256945610046 | 0.0 | 0.0 | +a899fe97-90e4-4ae3-941c-af3dee48fed3 / -— |
| Jogador 2 | 4-2 | 165 | REROLL | STABILIZE | 23.0 | 6 | 41 | 4 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008138949051499367 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 166 | BUY | STABILIZE | 23.0 | 6 | 39 | 3 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8026362061500549 | 0.0 | 0.0 | +7a419783-907e-47e2-bf69-29a54ee18a02 / -— |
| Jogador 2 | 4-2 | 167 | BUY | STABILIZE | 23.0 | 6 | 37 | 3 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08404488861560822 | 0.0 | 0.0 | +64d87de4-68df-4a72-8b8d-f78039ae4ce5 / -— |
| Jogador 2 | 4-2 | 168 | BUY | STABILIZE | 23.0 | 6 | 34 | 3 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23849788308143616 | 0.0 | 0.0 | +b2517873-8317-401b-8461-1d86969edbd7 / -— |
| Jogador 2 | 4-2 | 169 | REROLL | STABILIZE | 23.0 | 6 | 31 | 3 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12255658954381943 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 170 | BUY | STABILIZE | 23.0 | 6 | 29 | 2 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.763298749923706 | 0.0 | 0.0 | +8486b8a9-20fe-4234-bbba-0efa031c3b76 / -— |
| Jogador 2 | 4-3 | 172 | REROLL | STABILIZE | 23.0 | 6 | 34 | 3 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20245105028152466 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 173 | BUY | STABILIZE | 23.0 | 6 | 32 | 3 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3446001708507538 | 0.0 | 0.0 | +194da7dc-39b4-40e3-869d-326ace65137b / -— |
| Jogador 2 | 4-3 | 174 | REROLL | STABILIZE | 23.0 | 6 | 31 | 3 | 32.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 175 | REROLL | STABILIZE | 23.0 | 6 | 29 | 2 | 32.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17389266192913055 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 176 | REROLL | STABILIZE | 23.0 | 6 | 27 | 2 | 32.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17250767350196838 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 177 | REROLL | STABILIZE | 23.0 | 6 | 25 | 2 | 32.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16711801290512085 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 178 | REROLL | STABILIZE | 23.0 | 6 | 23 | 2 | 32.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16736826300621033 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 180 | REROLL | ALL_IN | 9.0 | 6 | 28 | 2 | 32.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1743612140417099 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 182 | REROLL | ALL_IN | 9.0 | 6 | 33 | 3 | 32.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19998551905155182 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 183 | REROLL | ALL_IN | 9.0 | 6 | 31 | 3 | 32.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.023945029824972153 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 184 | REROLL | ALL_IN | 9.0 | 6 | 29 | 2 | 32.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1378723531961441 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 185 | REROLL | ALL_IN | 9.0 | 6 | 27 | 2 | 32.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17316192388534546 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 186 | REROLL | ALL_IN | 9.0 | 6 | 25 | 2 | 32.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17581415176391602 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 187 | REROLL | ALL_IN | 9.0 | 6 | 23 | 2 | 32.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17351962625980377 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 188 | REROLL | ALL_IN | 9.0 | 6 | 21 | 2 | 32.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0961691290140152 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 189 | REROLL | ALL_IN | 9.0 | 6 | 19 | 1 | 32.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17149542272090912 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 191 | PASS | ALL_IN | 0.0 | 6 | 17 | 1 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 201 | PASS | ALL_IN | 0.0 | 6 | 17 | 1 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 211 | PASS | ALL_IN | 0.0 | 6 | 17 | 1 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 220 | PASS | ALL_IN | 0.0 | 6 | 17 | 1 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 222 | PASS | ALL_IN | 0.0 | 6 | 17 | 1 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 232 | PASS | ALL_IN | 0.0 | 6 | 17 | 1 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 242 | PASS | ALL_IN | 0.0 | 6 | 17 | 1 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 252 | PASS | ALL_IN | 0.0 | 6 | 17 | 1 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 262 | PASS | ALL_IN | 0.0 | 6 | 17 | 1 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 272 | PASS | ALL_IN | 0.0 | 6 | 17 | 1 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 282 | PASS | ALL_IN | 0.0 | 6 | 17 | 1 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.040030770003795624 | 0.0 | 0.0 | +— / -36f58657-5835-4389-95e9-a7d26464c2aa |
| Jogador 3 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.21530985832214355 | 0.0 | 0.0 | +2cf5ccdc-76f4-4fc8-b12c-7b3b68b1b2c8 / -— |
| Jogador 3 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_RekSai | MOVE_BENCH, SELL, PASS | True | True | 0.5931587815284729 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_RekSai | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_RekSai | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9699749946594238 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_RekSai | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 13 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_RekSai | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035527557134628296 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 14 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_RekSai | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 20 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_RekSai | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 29 | PASS | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 38 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 4.0 | —/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.029922112822532654 | 0.0 | 0.0 | +f19f9e7f-f189-47fe-b571-be5065c6eb39 / -— |
| Jogador 3 | 2-1 | 39 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 8 | 0 | 4.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.381960391998291 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 40 | BUY_XP | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 41 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 42 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Shen | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 45 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 8.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3049129545688629 | 0.0 | 0.0 | +1acf3411-8f1a-4ee8-8a90-50013f260db3 / -— |
| Jogador 3 | 2-2 | 46 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12259109318256378 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 47 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 2 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34439894556999207 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 48 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09093416482210159 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 49 | PASS | STABILIZE | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 52 | BUY | STABILIZE | 89.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.27299150824546814 | 0.0 | 0.0 | +0da2c93c-0c62-4fe0-94ff-688f086141e3 / -— |
| Jogador 3 | 2-3 | 53 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10558653622865677 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 54 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4684777557849884 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 55 | BUY_XP | STABILIZE | 89.0 | 5 | 5 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 56 | PASS | STABILIZE | 89.0 | 5 | 1 | 0 | 20.0 | —/DA_18_Diana | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 62 | BUY_XP | STABILIZE | 89.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 63 | PASS | STABILIZE | 89.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 69 | BUY_XP | STABILIZE | 89.0 | 5 | 8 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 70 | BUY_XP | STABILIZE | 89.0 | 5 | 4 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.44200000166893005 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 71 | PASS | STABILIZE | 89.0 | 6 | 0 | 0 | 20.0 | —/DA_18_Diana | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 75 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 7 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06624050438404083 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 76 | BUY | STABILIZE | 89.0 | 6 | 7 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03315455839037895 | 0.0 | 0.0 | +fee4e511-e40e-4114-a8b6-c2de73117e82 / -— |
| Jogador 3 | 2-6 | 77 | BUY_XP | STABILIZE | 89.0 | 6 | 5 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 78 | SELL | STABILIZE | 89.0 | 6 | 1 | 0 | 20.0 | —/DA_18_Diana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12633846700191498 | 0.0 | 0.0 | +— / -fee4e511-e40e-4114-a8b6-c2de73117e82 |
| Jogador 3 | 2-6 | 79 | PASS | STABILIZE | 89.0 | 6 | 3 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 82 | BUY | STABILIZE | 83.0 | 6 | 8 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.967042088508606 | 0.0 | 0.0 | +a2f987f8-01d6-4463-9ab4-f96c9b6f067b / -— |
| Jogador 3 | 2-7 | 83 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 5 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.499625027179718 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 84 | BUY_XP | STABILIZE | 83.0 | 6 | 5 | 0 | 26.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 85 | PASS | STABILIZE | 83.0 | 6 | 1 | 0 | 26.0 | —/DA_18_Diana | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 92 | BUY_XP | STABILIZE | 83.0 | 6 | 6 | 0 | 26.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 93 | PASS | STABILIZE | 83.0 | 6 | 2 | 0 | 26.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 102 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 8 | 0 | 26.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 103 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 8 | 0 | 26.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 104 | PASS | STABILIZE | 72.0 | 6 | 8 | 0 | 26.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 112 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 14 | 1 | 26.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.07879506051540375 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 113 | BUY | STABILIZE | 62.0 | 6 | 14 | 1 | 26.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.13801132142543793 | 0.0 | 0.0 | +952adeb2-fe24-47af-9748-5131b91dcc06 / -— |
| Jogador 3 | 3-3 | 114 | BUY | STABILIZE | 62.0 | 6 | 10 | 1 | 26.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03450842201709747 | 0.0 | 0.0 | +25b16126-6e41-4649-a47f-42656ffc7a08 / -— |
| Jogador 3 | 3-3 | 115 | MOVE_BENCH | STABILIZE | 62.0 | 6 | 7 | 0 | 26.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2012300193309784 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 116 | MOVE_BENCH | STABILIZE | 62.0 | 6 | 7 | 0 | 28.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029373610392212868 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 117 | MOVE_BENCH | STABILIZE | 62.0 | 6 | 7 | 0 | 26.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6299376487731934 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 118 | MOVE_BOARD | STABILIZE | 62.0 | 6 | 7 | 0 | 28.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05045098066329956 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 119 | SELL | STABILIZE | 62.0 | 6 | 7 | 0 | 28.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.249417245388031 | 0.0 | 0.0 | +— / -1acf3411-8f1a-4ee8-8a90-50013f260db3 |
| Jogador 3 | 3-4 | 121 | BUY | STABILIZE | 62.0 | 6 | 17 | 1 | 28.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2675239145755768 | 0.0 | 0.0 | +94d1da64-f0c8-4fd8-a610-b7e86f10378e / -— |
| Jogador 3 | 3-4 | 122 | MOVE_BENCH | STABILIZE | 62.0 | 6 | 14 | 1 | 28.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.043041348457336426 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 123 | MOVE_BENCH | STABILIZE | 62.0 | 6 | 14 | 1 | 28.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01631835475564003 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 124 | BUY_XP | STABILIZE | 62.0 | 6 | 14 | 1 | 32.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 125 | BUY_XP | STABILIZE | 62.0 | 6 | 10 | 1 | 32.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 126 | BUY_XP | STABILIZE | 62.0 | 6 | 6 | 0 | 32.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.429500013589859 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 127 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 2 | 0 | 32.0 | Caçador/DA_18_Sivir | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13541053235530853 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 128 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 2 | 0 | 34.0 | Caçador/DA_18_Sivir | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17280325293540955 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 129 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 2 | 0 | 38.0 | Caçador/DA_18_Sivir | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13466143608093262 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 131 | BUY | STABILIZE | 62.0 | 7 | 7 | 0 | 38.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7323068976402283 | 0.0 | 0.0 | +27102740-ce4d-4bec-a9eb-ed936f6bc364 / -— |
| Jogador 3 | 3-5 | 132 | BUY_XP | STABILIZE | 62.0 | 7 | 4 | 0 | 38.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 133 | SELL | STABILIZE | 62.0 | 7 | 0 | 0 | 38.0 | Caçador/DA_18_Sivir | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.168022021651268 | 0.0 | 0.0 | +— / -2cf5ccdc-76f4-4fc8-b12c-7b3b68b1b2c8 |
| Jogador 3 | 3-5 | 134 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 1 | 0 | 38.0 | Caçador/DA_18_Sivir | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02132791094481945 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 135 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 1 | 0 | 38.0 | Caçador/DA_18_Sivir | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030072562396526337 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 136 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 1 | 0 | 38.0 | Caçador/DA_18_Sivir | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16540846228599548 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 137 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 1 | 0 | 38.0 | Caçador/DA_18_Sivir | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 138 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 1 | 0 | 38.0 | Caçador/DA_18_Sivir | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 140 | BUY | STABILIZE | 62.0 | 7 | 8 | 0 | 38.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2734692394733429 | 0.0 | 0.0 | +89cec488-9a0e-4838-b486-2504a0742476 / -— |
| Jogador 3 | 3-7 | 142 | BUY | STABILIZE | 51.0 | 7 | 10 | 1 | 38.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7518423795700073 | 0.0 | 0.0 | +f6b79583-b2fa-49a2-8adf-9b529a9eb3ae / -27102740-ce4d-4bec-a9eb-ed936f6bc364,94d1da64-f0c8-4fd8-a610-b7e86f10378e |
| Jogador 3 | 3-7 | 143 | REROLL | STABILIZE | 51.0 | 7 | 7 | 0 | 32.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14575177431106567 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 144 | BUY | STABILIZE | 51.0 | 7 | 5 | 0 | 32.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28383660316467285 | 0.0 | 0.0 | +4363594b-375b-45d4-9b1a-0c1ab96367a1 / -— |
| Jogador 3 | 3-7 | 145 | BUY | STABILIZE | 51.0 | 7 | 2 | 0 | 32.0 | Caçador/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2604065537452698 | 0.0 | 0.0 | +55944609-f4df-4e53-a1d1-31c79a148b22 / -— |
| Jogador 3 | 3-7 | 146 | MOVE_BOARD | STABILIZE | 51.0 | 7 | 0 | 0 | 32.0 | Caçador/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1837521344423294 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 147 | SELL | STABILIZE | 51.0 | 7 | 0 | 0 | 32.0 | Caçador/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11599999666213989 | 0.0 | 0.0 | +— / -55944609-f4df-4e53-a1d1-31c79a148b22 |
| Jogador 3 | 3-7 | 148 | REROLL | STABILIZE | 51.0 | 7 | 2 | 0 | 32.0 | Caçador/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 149 | MOVE_BOARD | STABILIZE | 51.0 | 7 | 0 | 0 | 32.0 | Caçador/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0945151075720787 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 150 | MOVE_BENCH | STABILIZE | 51.0 | 7 | 0 | 0 | 32.0 | Caçador/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42569008469581604 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 152 | REROLL | STABILIZE | 51.0 | 7 | 5 | 0 | 38.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02199334092438221 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 153 | SELL | STABILIZE | 51.0 | 7 | 3 | 0 | 38.0 | Caçador/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055961135774850845 | 0.0 | 0.0 | +— / -f6b79583-b2fa-49a2-8adf-9b529a9eb3ae |
| Jogador 3 | 4-1 | 154 | SELL | STABILIZE | 51.0 | 7 | 11 | 1 | 38.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1027129739522934 | 0.0 | 0.0 | +— / -4363594b-375b-45d4-9b1a-0c1ab96367a1 |
| Jogador 3 | 4-1 | 155 | REROLL | STABILIZE | 51.0 | 7 | 14 | 1 | 38.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.14319537580013275 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 156 | BUY | STABILIZE | 51.0 | 7 | 12 | 1 | 38.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6545704007148743 | 0.0 | 0.0 | +20821a31-3317-4f82-bbb2-b70cdebdd893 / -— |
| Jogador 3 | 4-1 | 157 | REROLL | STABILIZE | 51.0 | 7 | 9 | 0 | 38.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11291185766458511 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 158 | BUY | STABILIZE | 51.0 | 7 | 7 | 0 | 38.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7422431707382202 | 0.0 | 0.0 | +3b934078-806c-40f0-b102-e9131220f70e / -— |
| Jogador 3 | 4-1 | 159 | REROLL | STABILIZE | 51.0 | 7 | 4 | 0 | 38.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14537841081619263 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 160 | BUY | STABILIZE | 51.0 | 7 | 2 | 0 | 38.0 | Caçador/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2841281294822693 | 0.0 | 0.0 | +a64cf09b-42bf-494e-9603-d387b6740200 / -— |
| Jogador 3 | 4-2 | 162 | REROLL | STABILIZE | 51.0 | 7 | 6 | 0 | 38.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14598451554775238 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 163 | BUY | STABILIZE | 51.0 | 7 | 4 | 0 | 38.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7439827919006348 | 0.0 | 0.0 | +45b96060-6eda-4d0b-9012-e80db31b71d2 / -— |
| Jogador 3 | 4-2 | 164 | MOVE_BOARD | STABILIZE | 51.0 | 7 | 1 | 0 | 38.0 | Caçador/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 165 | SELL | STABILIZE | 51.0 | 7 | 1 | 0 | 38.0 | Caçador/DA_18_Diana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12283077090978622 | 0.0 | 0.0 | +— / -a64cf09b-42bf-494e-9603-d387b6740200 |
| Jogador 3 | 4-2 | 166 | REROLL | STABILIZE | 51.0 | 7 | 3 | 0 | 38.0 | Caçador/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1662440150976181 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 167 | MOVE_BOARD | STABILIZE | 51.0 | 7 | 1 | 0 | 38.0 | Caçador/DA_18_Diana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28980904817581177 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 168 | MOVE_BOARD | STABILIZE | 51.0 | 7 | 1 | 0 | 38.0 | Caçador/DA_18_Sivir | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16083969175815582 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 169 | MOVE_BOARD | STABILIZE | 51.0 | 7 | 1 | 0 | 38.0 | Caçador/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06863513588905334 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 170 | MOVE_BOARD | STABILIZE | 51.0 | 7 | 1 | 0 | 38.0 | Caçador/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11165398359298706 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 172 | BUY | STABILIZE | 40.0 | 7 | 6 | 0 | 38.0 | Caçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8301464319229126 | 0.0 | 0.0 | +85fb6db6-e1b0-4fa1-b99a-2f205305ef0b / -20821a31-3317-4f82-bbb2-b70cdebdd893,89cec488-9a0e-4838-b486-2504a0742476 |
| Jogador 3 | 4-3 | 173 | BUY | STABILIZE | 40.0 | 7 | 3 | 0 | 32.0 | Caçador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5687573552131653 | 0.0 | 0.0 | +1bf15a91-4832-4245-9b48-382a27410263 / -— |
| Jogador 3 | 4-3 | 174 | PASS | STABILIZE | 40.0 | 7 | 0 | 0 | 32.0 | Caçador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 178 | MOVE_BENCH | STABILIZE | 40.0 | 7 | 0 | 0 | 32.0 | Caçador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14786911010742188 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 180 | BUY | STABILIZE | 29.0 | 7 | 6 | 0 | 38.0 | Caçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2836977243423462 | 0.0 | 0.0 | +de590b22-a48c-4c78-a2f3-6ef39ce948fe / -— |
| Jogador 3 | 4-5 | 182 | BUY | STABILIZE | 29.0 | 7 | 9 | 0 | 38.0 | Caçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.743665337562561 | 0.0 | 0.0 | +52799e57-7b54-4dc5-b7f8-c39c8f57e7fa / -— |
| Jogador 3 | 4-5 | 183 | REROLL | STABILIZE | 29.0 | 7 | 6 | 0 | 38.0 | Caçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10306739807128906 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 184 | BUY | STABILIZE | 29.0 | 7 | 4 | 0 | 38.0 | Caçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8337005972862244 | 0.0 | 0.0 | +699b59c7-1237-472b-a4d1-18a35e88b7c2 / -52799e57-7b54-4dc5-b7f8-c39c8f57e7fa,de590b22-a48c-4c78-a2f3-6ef39ce948fe |
| Jogador 3 | 4-5 | 185 | PASS | STABILIZE | 29.0 | 7 | 1 | 0 | 38.0 | Caçador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 191 | BUY | STABILIZE | 18.0 | 7 | 7 | 0 | 38.0 | Caçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2569900155067444 | 0.0 | 0.0 | +77c36245-d5ea-4f94-bc0c-680d4a77794a / -— |
| Jogador 3 | 4-6 | 192 | BUY | STABILIZE | 18.0 | 7 | 3 | 0 | 38.0 | Caçador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26130738854408264 | 0.0 | 0.0 | +bf2246f7-4b73-4b2b-92ad-56849f783dfb / -— |
| Jogador 3 | 4-6 | 193 | PASS | STABILIZE | 18.0 | 7 | 0 | 0 | 38.0 | Caçador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 201 | BUY | STABILIZE | 18.0 | 7 | 6 | 0 | 38.0 | Caçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8339981436729431 | 0.0 | 0.0 | +c2de293a-fa44-4161-8593-47b3feca588d / -25b16126-6e41-4649-a47f-42656ffc7a08,45b96060-6eda-4d0b-9012-e80db31b71d2 |
| Jogador 3 | 4-7 | 202 | REROLL | STABILIZE | 18.0 | 7 | 3 | 0 | 32.0 | Caçador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11649028211832047 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 203 | PASS | STABILIZE | 18.0 | 7 | 1 | 0 | 32.0 | Caçador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 209 | MOVE_BENCH | STABILIZE | 18.0 | 7 | 1 | 0 | 32.0 | Caçador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4488166272640228 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 211 | EQUIP_FROM_INVENTORY | STABILIZE | 18.0 | 7 | 6 | 0 | 40.0 | Caçador/DA_KogMaw18_AD | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 212 | BUY | STABILIZE | 18.0 | 7 | 6 | 0 | 40.0 | Caçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2839992642402649 | 0.0 | 0.0 | +d4fd64a7-2945-4d09-ab2e-5bd475ff0f04 / -— |
| Jogador 3 | 5-1 | 213 | REROLL | STABILIZE | 18.0 | 7 | 3 | 0 | 40.0 | Caçador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.030916938558220863 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 214 | PASS | STABILIZE | 18.0 | 7 | 1 | 0 | 40.0 | Caçador/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 220 | BUY | ALL_IN | 1.0 | 7 | 6 | 0 | 40.0 | Caçador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8136081695556641 | 0.0 | 0.0 | +65213adf-9d1e-4f3a-95a2-7f9cfea817f3 / -0da2c93c-0c62-4fe0-94ff-688f086141e3,1bf15a91-4832-4245-9b48-382a27410263 |
| Jogador 3 | 5-3 | 222 | PASS | ALL_IN | 0.0 | 7 | 3 | 0 | 0.0 | Caçador/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 232 | PASS | ALL_IN | 0.0 | 7 | 3 | 0 | 0.0 | Caçador/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 242 | PASS | ALL_IN | 0.0 | 7 | 3 | 0 | 0.0 | Caçador/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 252 | PASS | ALL_IN | 0.0 | 7 | 3 | 0 | 0.0 | Caçador/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 262 | PASS | ALL_IN | 0.0 | 7 | 3 | 0 | 0.0 | Caçador/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 272 | PASS | ALL_IN | 0.0 | 7 | 3 | 0 | 0.0 | Caçador/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-2 | 282 | PASS | ALL_IN | 0.0 | 7 | 3 | 0 | 0.0 | Caçador/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 9 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.28737619519233704 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3375903069972992 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40336331725120544 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 13 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 20 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 29 | PASS | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 38 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 4.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8894625902175903 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 4 | 2-1 | 39 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 9 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 40 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 9 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24666821956634521 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 41 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0823926255106926 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 42 | BUY_XP | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 43 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 45 | BUY | STABILIZE | 94.0 | 5 | 6 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.07448136061429977 | 0.0 | 0.0 | +341df1a1-a619-420a-926a-0fe048aa1456 / -— |
| Jogador 4 | 2-2 | 46 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 3 | 0 | 6.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.053739070892333984 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 47 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 3 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28262749314308167 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 48 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 3 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 49 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 3 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.11402799189090729 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 50 | PASS | STABILIZE | 94.0 | 5 | 3 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 52 | BUY | STABILIZE | 90.0 | 5 | 9 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9320540428161621 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 4 | 2-3 | 53 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 6 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 54 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 6 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13421185314655304 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 55 | PASS | STABILIZE | 90.0 | 5 | 6 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 62 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 12 | 1 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 63 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 12 | 1 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 64 | PASS | STABILIZE | 90.0 | 5 | 12 | 1 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 69 | BUY | STABILIZE | 90.0 | 5 | 18 | 1 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1002213954925537 | 0.0 | 0.0 | +0023f061-5310-4e39-849a-22ad49993d8c / -0fff7760-179f-4d7c-8267-08d70cb6c1bd,341df1a1-a619-420a-926a-0fe048aa1456 |
| Jogador 4 | 2-5 | 70 | BUY | STABILIZE | 90.0 | 5 | 15 | 1 | 6.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31811392307281494 | 0.0 | 0.0 | +1b1964b4-7d5e-4cea-8e83-0692f326b599 / -— |
| Jogador 4 | 2-5 | 71 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 12 | 1 | 6.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3512972593307495 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 72 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 12 | 1 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5595578551292419 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 73 | BUY_XP | STABILIZE | 90.0 | 5 | 12 | 1 | 24.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 75 | MOVE_BOARD | STABILIZE | 83.0 | 5 | 13 | 1 | 24.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06450433284044266 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 76 | MOVE_BOARD | STABILIZE | 83.0 | 5 | 13 | 1 | 24.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03215137496590614 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 77 | MOVE_BOARD | STABILIZE | 83.0 | 5 | 13 | 1 | 24.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 78 | MOVE_BOARD | STABILIZE | 83.0 | 5 | 13 | 1 | 24.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 79 | PASS | STABILIZE | 83.0 | 5 | 13 | 1 | 24.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 82 | BUY_XP | STABILIZE | 76.0 | 5 | 20 | 2 | 24.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 83 | BUY_XP | STABILIZE | 76.0 | 5 | 16 | 1 | 24.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.44200000166893005 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 84 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 12 | 1 | 24.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03215137496590614 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 85 | BUY | STABILIZE | 76.0 | 6 | 12 | 1 | 24.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.28535589575767517 | 0.0 | 0.0 | +ac02c0c4-a10d-497d-b6c1-d458ad7ae58c / -— |
| Jogador 4 | 2-7 | 86 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 9 | 0 | 24.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5307639241218567 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 87 | BUY_XP | STABILIZE | 76.0 | 6 | 9 | 0 | 30.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 88 | BUY_XP | STABILIZE | 76.0 | 6 | 5 | 0 | 30.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 89 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 1 | 0 | 30.0 | —/DA_Krug18 | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 90 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 1 | 0 | 30.0 | —/DA_Krug18 | BUY, MOVE_BOARD, PASS | True | True | 0.002083240309730172 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 92 | BUY | STABILIZE | 76.0 | 6 | 7 | 0 | 30.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08267559111118317 | 0.0 | 0.0 | +ad1693cd-1ab5-43a9-8164-25929b8bd68e / -— |
| Jogador 4 | 3-1 | 93 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 4 | 0 | 30.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5208674669265747 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 94 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03724497929215431 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 95 | BUY_XP | STABILIZE | 76.0 | 6 | 4 | 0 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 96 | SELL | STABILIZE | 76.0 | 6 | 0 | 0 | 34.0 | Colosso/DA_Krug18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3684128224849701 | 0.0 | 0.0 | +— / -9e7d1da0-5190-4348-81b4-3a3f2129a8e5 |
| Jogador 4 | 3-1 | 97 | PASS | STABILIZE | 76.0 | 6 | 1 | 0 | 34.0 | Colosso/DA_Krug18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 102 | BUY | STABILIZE | 76.0 | 6 | 7 | 0 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7437528967857361 | 0.0 | 0.0 | +46320c4e-6bc0-49d6-b150-be378fa422cf / -— |
| Jogador 4 | 3-2 | 103 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 4 | 0 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 104 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 4 | 0 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.023838559165596962 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 105 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 4 | 0 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33983463048934937 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 106 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 4 | 0 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003007418941706419 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 107 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 4 | 0 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 108 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 4 | 0 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003424477530643344 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 109 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 4 | 0 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -4.832016566069797e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 110 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 4 | 0 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 112 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 11 | 1 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.023838713765144348 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 113 | BUY_XP | STABILIZE | 76.0 | 6 | 11 | 1 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 114 | BUY_XP | STABILIZE | 76.0 | 6 | 7 | 0 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 115 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 3 | 0 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 116 | SELL | STABILIZE | 76.0 | 6 | 3 | 0 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05832994356751442 | 0.0 | 0.0 | +— / -ad1693cd-1ab5-43a9-8164-25929b8bd68e |
| Jogador 4 | 3-3 | 117 | BUY_XP | STABILIZE | 76.0 | 6 | 6 | 0 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 118 | PASS | STABILIZE | 76.0 | 6 | 2 | 0 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 121 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 9 | 0 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10906810313463211 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 122 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 9 | 0 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10226842761039734 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 123 | PASS | STABILIZE | 76.0 | 6 | 9 | 0 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 131 | BUY | STABILIZE | 76.0 | 7 | 15 | 1 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7435142397880554 | 0.0 | 0.0 | +23f4d10f-2614-47b2-bfb2-4fb276764b5e / -— |
| Jogador 4 | 3-5 | 132 | MOVE_BENCH | STABILIZE | 76.0 | 7 | 12 | 1 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 133 | MOVE_BENCH | STABILIZE | 76.0 | 7 | 12 | 1 | 34.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06931429356336594 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 134 | PASS | STABILIZE | 76.0 | 7 | 12 | 1 | 38.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 138 | MOVE_BENCH | STABILIZE | 76.0 | 7 | 12 | 1 | 38.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5783743858337402 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 140 | BUY | STABILIZE | 64.0 | 7 | 18 | 1 | 40.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8320099115371704 | 0.0 | 0.0 | +8a52858d-da47-4de9-8e91-8612788cb8fd / -1b1964b4-7d5e-4cea-8e83-0692f326b599,46320c4e-6bc0-49d6-b150-be378fa422cf |
| Jogador 4 | 3-7 | 142 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 22 | 2 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08212891221046448 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 143 | BUY | STABILIZE | 52.0 | 7 | 22 | 2 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7684626579284668 | 0.0 | 0.0 | +cc56fedc-f555-4075-af15-6b5fb93a156f / -23f4d10f-2614-47b2-bfb2-4fb276764b5e,ac02c0c4-a10d-497d-b6c1-d458ad7ae58c |
| Jogador 4 | 3-7 | 144 | MOVE_BENCH | STABILIZE | 52.0 | 7 | 19 | 1 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4766685962677002 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 145 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 19 | 1 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.16292668879032135 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 146 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 19 | 1 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.04642727971076965 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 147 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 19 | 1 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.05562080815434456 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 148 | BUY | STABILIZE | 52.0 | 7 | 19 | 1 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.017741478979587555 | 0.0 | 0.0 | +97d52b06-365b-44ad-b4f9-63e0f9503c8a / -— |
| Jogador 4 | 3-7 | 149 | MOVE_BENCH | STABILIZE | 52.0 | 7 | 16 | 1 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0748792216181755 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 150 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 16 | 1 | 46.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.30499863624572754 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 152 | BUY | STABILIZE | 52.0 | 7 | 23 | 2 | 46.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.07697929441928864 | 0.0 | 0.0 | +2530bb2a-8b40-4f0b-a49c-f13fe67fbca4 / -— |
| Jogador 4 | 4-1 | 153 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 20 | 2 | 46.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.034966591745615005 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 154 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 20 | 2 | 46.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.034966591745615005 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 155 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 20 | 2 | 46.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10453628748655319 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 156 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 20 | 2 | 46.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 157 | PASS | STABILIZE | 52.0 | 7 | 20 | 2 | 46.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 160 | MOVE_BENCH | STABILIZE | 52.0 | 7 | 20 | 2 | 46.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.442931592464447 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 162 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 28 | 2 | 52.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | -0.1384258270263672 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 163 | BUY | STABILIZE | 52.0 | 7 | 28 | 2 | 52.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.0883287787437439 | 0.0 | 0.0 | +a492f78e-91f0-48cb-891a-6518551da328 / -— |
| Jogador 4 | 4-2 | 164 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 24 | 2 | 52.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0230864305049181 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 165 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 24 | 2 | 52.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.17539547383785248 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 166 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 24 | 2 | 52.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1763571798801422 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 167 | SELL | STABILIZE | 52.0 | 7 | 24 | 2 | 52.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.13832877576351166 | 0.0 | 0.0 | +— / -a492f78e-91f0-48cb-891a-6518551da328 |
| Jogador 4 | 4-2 | 168 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 28 | 2 | 52.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 169 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 28 | 2 | 52.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.001785655738785863 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 170 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 28 | 2 | 52.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 172 | BUY | FAST8 | 52.0 | 7 | 37 | 3 | 52.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | -0.03408635035157204 | 0.0 | 0.0 | +27079fe2-8808-47b7-8b10-9fb2834bb6ed / -— |
| Jogador 4 | 4-3 | 173 | MOVE_BOARD | FAST8 | 52.0 | 7 | 33 | 3 | 52.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 174 | MOVE_BOARD | FAST8 | 52.0 | 7 | 33 | 3 | 52.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3356841504573822 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 175 | PASS | FAST8 | 52.0 | 7 | 33 | 3 | 52.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.05999999865889549 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 180 | BUY | FAST8 | 40.0 | 7 | 41 | 4 | 52.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5010344386100769 | 0.0 | 0.0 | +ffd44f6f-388e-4792-ae4f-77f2faa3e95f / -— |
| Jogador 4 | 4-5 | 182 | BUY | FAST8 | 40.0 | 7 | 46 | 4 | 52.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8690459728240967 | 0.0 | 0.0 | +24d03668-5dc4-4b40-9439-a1d67522d0a3 / -97d52b06-365b-44ad-b4f9-63e0f9503c8a,ffd44f6f-388e-4792-ae4f-77f2faa3e95f |
| Jogador 4 | 4-5 | 183 | BUY | FAST8 | 40.0 | 7 | 43 | 4 | 46.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4080427885055542 | 0.0 | 0.0 | +7fd34ef6-a124-4d23-a166-9f7ad919c826 / -— |
| Jogador 4 | 4-5 | 184 | MOVE_BOARD | FAST8 | 40.0 | 7 | 39 | 3 | 46.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 185 | MOVE_BOARD | FAST8 | 40.0 | 7 | 39 | 3 | 46.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.012479945085942745 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 186 | MOVE_BOARD | FAST8 | 40.0 | 7 | 39 | 3 | 46.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 187 | MOVE_BOARD | FAST8 | 40.0 | 7 | 39 | 3 | 46.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.127062126994133 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 188 | PASS | FAST8 | 40.0 | 7 | 39 | 3 | 46.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 189 | MOVE_BENCH | FAST8 | 40.0 | 7 | 39 | 3 | 46.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.40416419506073 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 191 | REROLL | FAST8 | 40.0 | 7 | 49 | 4 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.12967219948768616 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 192 | REROLL | FAST8 | 40.0 | 7 | 47 | 4 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1029185801744461 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 193 | REROLL | FAST8 | 40.0 | 7 | 45 | 4 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.06400000303983688 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 194 | REROLL | FAST8 | 40.0 | 7 | 43 | 4 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.22380715608596802 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 195 | MOVE_BOARD | FAST8 | 40.0 | 7 | 41 | 4 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.11592227220535278 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 196 | REROLL | FAST8 | 40.0 | 7 | 41 | 4 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.08887020498514175 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 197 | REROLL | FAST8 | 40.0 | 7 | 39 | 3 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2235151082277298 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 198 | REROLL | FAST8 | 40.0 | 7 | 37 | 3 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.14422324299812317 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 199 | REROLL | FAST8 | 40.0 | 7 | 35 | 3 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.06400000303983688 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 201 | REROLL | STABILIZE | 28.0 | 7 | 41 | 4 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.25385528802871704 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 202 | REROLL | STABILIZE | 28.0 | 7 | 39 | 3 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.16050507128238678 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 203 | REROLL | STABILIZE | 28.0 | 7 | 37 | 3 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.16813777387142181 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 204 | REROLL | STABILIZE | 28.0 | 7 | 35 | 3 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.11108901351690292 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 205 | REROLL | STABILIZE | 28.0 | 7 | 33 | 3 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.045580051839351654 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 206 | REROLL | STABILIZE | 28.0 | 7 | 31 | 3 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.013134441338479519 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 207 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 29 | 2 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 208 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 29 | 2 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.20455847680568695 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 209 | PASS | STABILIZE | 28.0 | 7 | 29 | 2 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 211 | EQUIP_FROM_INVENTORY | STABILIZE | 28.0 | 7 | 36 | 3 | 54.0 | Colosso/DA_Fiddlesticks18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 212 | REROLL | STABILIZE | 28.0 | 7 | 36 | 3 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.16462008655071259 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 213 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 34 | 3 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 214 | REROLL | STABILIZE | 28.0 | 7 | 34 | 3 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.17547191679477692 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 215 | REROLL | STABILIZE | 28.0 | 7 | 32 | 3 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.10567594319581985 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 216 | REROLL | STABILIZE | 28.0 | 7 | 30 | 3 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.21585506200790405 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 217 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 28 | 2 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.024840479716658592 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 218 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 28 | 2 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.012479945085942745 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 220 | BUY | ALL_IN | 14.0 | 7 | 36 | 3 | 54.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.38266050815582275 | 0.0 | 0.0 | +81d97dc0-cc50-4303-acfe-e8273ef39d35 / -— |
| Jogador 4 | 5-3 | 222 | PASS | ALL_IN | 0.0 | 7 | 33 | 3 | 0.0 | Colosso/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 232 | PASS | ALL_IN | 0.0 | 7 | 33 | 3 | 0.0 | Colosso/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 242 | PASS | ALL_IN | 0.0 | 7 | 33 | 3 | 0.0 | Colosso/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 252 | PASS | ALL_IN | 0.0 | 7 | 33 | 3 | 0.0 | Colosso/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 262 | PASS | ALL_IN | 0.0 | 7 | 33 | 3 | 0.0 | Colosso/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 272 | PASS | ALL_IN | 0.0 | 7 | 33 | 3 | 0.0 | Colosso/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-2 | 282 | PASS | ALL_IN | 0.0 | 7 | 33 | 3 | 0.0 | Colosso/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 9 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.27265432476997375 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.027269404381513596 | 0.0 | 0.0 | +df7d3860-9b2e-45ed-b564-281d95e64e82 / -— |
| Jogador 5 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37584805488586426 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 13 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 20 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 29 | PASS | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 38 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.24964937567710876 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 39 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1429741531610489 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 40 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.32034075260162354 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.24984756112098694 | 0.0 | 0.0 | +a5c3f6df-50ac-4f3b-aa9c-6476a055aa53 / -— |
| Jogador 5 | 2-1 | 42 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41110432147979736 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 43 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 45 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2970731258392334 | 0.0 | 0.0 | +f82eae62-dfe9-41bc-b346-71bf2c7cca02 / -— |
| Jogador 5 | 2-2 | 46 | SELL | STABILIZE | 95.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34707313776016235 | 0.0 | 0.0 | +— / -f82eae62-dfe9-41bc-b346-71bf2c7cca02 |
| Jogador 5 | 2-2 | 47 | BUY_XP | STABILIZE | 95.0 | 4 | 5 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.44200000166893005 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 48 | BUY | STABILIZE | 95.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, MOVE_BOARD, PASS | True | True | 0.45763978362083435 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 5 | 2-2 | 49 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009230419993400574 | 0.0 | 0.0 | +— / -43da0d73-facd-488b-b856-94e9496a97f9 |
| Jogador 5 | 2-2 | 50 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, MOVE_BOARD, PASS | True | True | 0.14408981800079346 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 52 | BUY | STABILIZE | 95.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3269827365875244 | 0.0 | 0.0 | +dd5b4353-d201-4266-9fbe-72df320eb4f5 / -— |
| Jogador 5 | 2-3 | 53 | SELL | STABILIZE | 95.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37698274850845337 | 0.0 | 0.0 | +— / -dd5b4353-d201-4266-9fbe-72df320eb4f5 |
| Jogador 5 | 2-3 | 54 | BUY | STABILIZE | 95.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.028340982273221016 | 0.0 | 0.0 | +4367c039-e64e-4a3c-a49f-57cb2674a08f / -— |
| Jogador 5 | 2-3 | 55 | SELL | STABILIZE | 95.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12633846700191498 | 0.0 | 0.0 | +— / -4367c039-e64e-4a3c-a49f-57cb2674a08f |
| Jogador 5 | 2-3 | 56 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.3201592266559601 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 57 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.14362145960330963 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 58 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 59 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1799006164073944 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 60 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.32565149664878845 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 62 | BUY | STABILIZE | 88.0 | 5 | 12 | 1 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9443280696868896 | 0.0 | 0.0 | +3280b28e-bd8f-494b-a78d-111744e2178b / -— |
| Jogador 5 | 2-4 | 63 | BUY | STABILIZE | 88.0 | 5 | 10 | 1 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18308289349079132 | 0.0 | 0.0 | +2c7e844d-925a-43bb-8be8-65a71d11f964 / -— |
| Jogador 5 | 2-4 | 64 | BUY | STABILIZE | 88.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41245630383491516 | 0.0 | 0.0 | +22c1a0b0-5d27-406a-b3e1-9e0272a18947 / -— |
| Jogador 5 | 2-4 | 65 | SELL | STABILIZE | 88.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02927408181130886 | 0.0 | 0.0 | +— / -22c1a0b0-5d27-406a-b3e1-9e0272a18947 |
| Jogador 5 | 2-4 | 66 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45238035917282104 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 67 | MOVE_BOARD | STABILIZE | 88.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 69 | MOVE_BOARD | STABILIZE | 88.0 | 5 | 12 | 1 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3199225068092346 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 70 | BUY | STABILIZE | 88.0 | 5 | 12 | 1 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06732126325368881 | 0.0 | 0.0 | +599caeca-96ef-4308-b6cd-f65b005879e2 / -— |
| Jogador 5 | 2-5 | 71 | MOVE_BOARD | STABILIZE | 88.0 | 5 | 9 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17991268634796143 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 72 | SELL | STABILIZE | 88.0 | 5 | 9 | 0 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1269846111536026 | 0.0 | 0.0 | +— / -2c7e844d-925a-43bb-8be8-65a71d11f964 |
| Jogador 5 | 2-5 | 73 | SELL | STABILIZE | 88.0 | 5 | 12 | 1 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26372307538986206 | 0.0 | 0.0 | +— / -599caeca-96ef-4308-b6cd-f65b005879e2 |
| Jogador 5 | 2-6 | 75 | BUY | STABILIZE | 81.0 | 5 | 22 | 2 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9674902558326721 | 0.0 | 0.0 | +b482ecdd-cc1a-40fa-8c21-cd1cac92b594 / -— |
| Jogador 5 | 2-6 | 76 | SELL | STABILIZE | 81.0 | 5 | 20 | 2 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3287145495414734 | 0.0 | 0.0 | +— / -b482ecdd-cc1a-40fa-8c21-cd1cac92b594 |
| Jogador 5 | 2-6 | 77 | MOVE_BOARD | STABILIZE | 81.0 | 5 | 22 | 2 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09515496343374252 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 78 | BUY | STABILIZE | 81.0 | 5 | 22 | 2 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4529266059398651 | 0.0 | 0.0 | +6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 / -— |
| Jogador 5 | 2-6 | 79 | SELL | STABILIZE | 81.0 | 5 | 21 | 2 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015530240722000599 | 0.0 | 0.0 | +— / -6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 |
| Jogador 5 | 2-6 | 80 | MOVE_BOARD | STABILIZE | 81.0 | 5 | 22 | 2 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1721227467060089 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 82 | BUY | SLOWROLL | 73.0 | 5 | 30 | 3 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8099591135978699 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 5 | 2-7 | 83 | SELL | STABILIZE | 73.0 | 5 | 29 | 2 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11599826067686081 | 0.0 | 0.0 | +— / -d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 5 | 2-7 | 84 | BUY | SLOWROLL | 73.0 | 5 | 30 | 3 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09280841797590256 | 0.0 | 0.0 | +d731d71e-fc91-41ae-ab3f-75966dd2c428 / -— |
| Jogador 5 | 2-7 | 85 | SELL | STABILIZE | 73.0 | 5 | 28 | 2 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14280842244625092 | 0.0 | 0.0 | +— / -d731d71e-fc91-41ae-ab3f-75966dd2c428 |
| Jogador 5 | 2-7 | 86 | MOVE_BOARD | SLOWROLL | 73.0 | 5 | 30 | 3 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.324206680059433 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 87 | BUY | SLOWROLL | 73.0 | 5 | 30 | 3 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3029956519603729 | 0.0 | 0.0 | +f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 / -— |
| Jogador 5 | 2-7 | 88 | SELL | STABILIZE | 73.0 | 5 | 29 | 2 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09550545364618301 | 0.0 | 0.0 | +— / -f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 |
| Jogador 5 | 2-7 | 89 | MOVE_BOARD | SLOWROLL | 73.0 | 5 | 30 | 3 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10544315725564957 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 90 | MOVE_BOARD | SLOWROLL | 73.0 | 5 | 30 | 3 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.02665959857404232 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 92 | BUY | SLOWROLL | 73.0 | 5 | 39 | 3 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.026461267843842506 | 0.0 | 0.0 | +7b2af6c8-ec0f-4ab5-8913-9b88fc2e0e86 / -— |
| Jogador 5 | 3-1 | 93 | SELL | SLOWROLL | 73.0 | 5 | 37 | 3 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13524071872234344 | 0.0 | 0.0 | +— / -7b2af6c8-ec0f-4ab5-8913-9b88fc2e0e86 |
| Jogador 5 | 3-1 | 94 | BUY | SLOWROLL | 73.0 | 5 | 39 | 3 | 20.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.10664910078048706 | 0.0 | 0.0 | +a5c0595b-85f9-4c71-a156-675d22a7b3c2 / -— |
| Jogador 5 | 3-1 | 95 | SELL | SLOWROLL | 73.0 | 5 | 37 | 3 | 20.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09403076767921448 | 0.0 | 0.0 | +— / -a5c0595b-85f9-4c71-a156-675d22a7b3c2 |
| Jogador 5 | 3-1 | 96 | BUY | SLOWROLL | 73.0 | 5 | 39 | 3 | 20.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.24414613842964172 | 0.0 | 0.0 | +5cf46feb-77cd-4cb8-9211-ffb08d88391a / -— |
| Jogador 5 | 3-1 | 97 | SELL | SLOWROLL | 73.0 | 5 | 38 | 3 | 20.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.136461541056633 | 0.0 | 0.0 | +— / -5cf46feb-77cd-4cb8-9211-ffb08d88391a |
| Jogador 5 | 3-1 | 98 | MOVE_BOARD | SLOWROLL | 73.0 | 5 | 39 | 3 | 20.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 99 | MOVE_BOARD | SLOWROLL | 73.0 | 5 | 39 | 3 | 20.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.12904618680477142 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 100 | PASS | SLOWROLL | 73.0 | 5 | 39 | 3 | 20.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 102 | BUY | SLOWROLL | 62.0 | 5 | 48 | 4 | 20.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7151515483856201 | 0.0 | 0.0 | +2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c / -— |
| Jogador 5 | 3-2 | 103 | BUY | SLOWROLL | 62.0 | 5 | 46 | 4 | 20.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7273007035255432 | 0.0 | 0.0 | +5326031a-1b7e-4dbd-b58b-1e81029d42a1 / -— |
| Jogador 5 | 3-2 | 104 | SELL | SLOWROLL | 62.0 | 5 | 45 | 4 | 20.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32845038175582886 | 0.0 | 0.0 | +— / -5326031a-1b7e-4dbd-b58b-1e81029d42a1 |
| Jogador 5 | 3-2 | 105 | BUY | SLOWROLL | 62.0 | 5 | 46 | 4 | 20.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1453150063753128 | 0.0 | 0.0 | +655deca9-2d3f-4e88-827a-5f49da8f3451 / -— |
| Jogador 5 | 3-2 | 106 | MOVE_BOARD | SLOWROLL | 62.0 | 5 | 44 | 4 | 20.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 107 | SELL | SLOWROLL | 62.0 | 5 | 44 | 4 | 20.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0944598838686943 | 0.0 | 0.0 | +— / -655deca9-2d3f-4e88-827a-5f49da8f3451 |
| Jogador 5 | 3-2 | 108 | SELL | SLOWROLL | 62.0 | 5 | 46 | 4 | 20.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31174010038375854 | 0.0 | 0.0 | +— / -2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c |
| Jogador 5 | 3-2 | 109 | MOVE_BOARD | SLOWROLL | 62.0 | 5 | 48 | 4 | 20.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 110 | MOVE_BOARD | SLOWROLL | 62.0 | 5 | 48 | 4 | 20.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.02665959857404232 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 112 | BUY | SLOWROLL | 50.0 | 5 | 59 | 5 | 20.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3082432150840759 | 0.0 | 0.0 | +7c751800-5068-42ba-a253-3a49bfe52334 / -— |
| Jogador 5 | 3-3 | 113 | BUY | SLOWROLL | 50.0 | 5 | 55 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06172593683004379 | 0.0 | 0.0 | +1af578c1-57cf-4752-93e7-d0eebc6e8ae5 / -— |
| Jogador 5 | 3-3 | 114 | BUY | SLOWROLL | 50.0 | 5 | 52 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16734182834625244 | 0.0 | 0.0 | +8df39648-f588-452a-b234-32da76c43aff / -— |
| Jogador 5 | 3-3 | 115 | REROLL | SLOWROLL | 50.0 | 5 | 50 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22452272474765778 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 116 | BUY | SLOWROLL | 50.0 | 5 | 48 | 4 | 20.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.650352418422699 | 0.0 | 0.0 | +2acd0734-f0c3-42b1-9791-5c48e1aa46bc / -— |
| Jogador 5 | 3-3 | 117 | BUY | SLOWROLL | 50.0 | 5 | 46 | 4 | 20.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2661384344100952 | 0.0 | 0.0 | +4cf7dfe2-9d2c-4d45-803e-503eda810357 / -— |
| Jogador 5 | 3-3 | 118 | BUY | SLOWROLL | 50.0 | 5 | 45 | 4 | 20.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05762860178947449 | 0.0 | 0.0 | +7fd03119-ac82-49e1-b3bb-3a0caa31011f / -— |
| Jogador 5 | 3-3 | 119 | BUY | SLOWROLL | 50.0 | 5 | 43 | 4 | 20.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28090620040893555 | 0.0 | 0.0 | +e01be6cf-34fe-4057-aef3-c08c504794cf / -— |
| Jogador 5 | 3-4 | 121 | BUY | STABILIZE | 38.0 | 5 | 53 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2729203701019287 | 0.0 | 0.0 | +727765c8-7f02-491e-a6da-12b0dab59f6d / -— |
| Jogador 5 | 3-4 | 122 | REROLL | STABILIZE | 38.0 | 5 | 50 | 5 | 20.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10486705601215363 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 123 | REROLL | STABILIZE | 38.0 | 5 | 48 | 4 | 20.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13770559430122375 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 124 | BUY | STABILIZE | 38.0 | 5 | 46 | 4 | 20.0 | Enfeitiçador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8677878975868225 | 0.0 | 0.0 | +5b95b64a-b46a-4827-8613-307c8dadc072 / -2acd0734-f0c3-42b1-9791-5c48e1aa46bc,8df39648-f588-452a-b234-32da76c43aff |
| Jogador 5 | 3-4 | 125 | REROLL | STABILIZE | 38.0 | 5 | 44 | 4 | 20.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19022448360919952 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 126 | BUY | STABILIZE | 38.0 | 5 | 42 | 4 | 20.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24532181024551392 | 0.0 | 0.0 | +f546078f-fc3e-44a9-9b8f-25c46a043168 / -— |
| Jogador 5 | 3-4 | 127 | BUY | STABILIZE | 38.0 | 5 | 39 | 3 | 20.0 | Enfeitiçador/DA_18_Warwick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8729941844940186 | 0.0 | 0.0 | +7c8b3027-1434-4346-95b3-5463e8a4aa9b / -3280b28e-bd8f-494b-a78d-111744e2178b,a5c3f6df-50ac-4f3b-aa9c-6476a055aa53 |
| Jogador 5 | 3-4 | 128 | REROLL | STABILIZE | 38.0 | 5 | 37 | 3 | 12.0 | Enfeitiçador/DA_18_LeBlanc | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14091186225414276 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 129 | MOVE_BENCH | STABILIZE | 38.0 | 5 | 35 | 3 | 12.0 | Enfeitiçador/DA_18_LeBlanc | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5247616767883301 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 131 | BUY | STABILIZE | 38.0 | 6 | 46 | 4 | 20.0 | Enfeitiçador/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6247297525405884 | 0.0 | 0.0 | +750eedbe-93d9-46de-b3b8-a88e41f395f0 / -— |
| Jogador 5 | 3-5 | 132 | REROLL | STABILIZE | 38.0 | 6 | 43 | 4 | 20.0 | Enfeitiçador/DA_18_LeBlanc | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17634229362010956 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 133 | REROLL | STABILIZE | 38.0 | 6 | 41 | 4 | 20.0 | Enfeitiçador/DA_18_LeBlanc | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25346916913986206 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 134 | REROLL | STABILIZE | 38.0 | 6 | 39 | 3 | 20.0 | Enfeitiçador/DA_18_LeBlanc | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1706623136997223 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 135 | PASS | STABILIZE | 38.0 | 6 | 37 | 3 | 20.0 | Enfeitiçador/DA_18_LeBlanc | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 138 | MOVE_BENCH | STABILIZE | 38.0 | 6 | 37 | 3 | 20.0 | Enfeitiçador/DA_18_LeBlanc | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24802663922309875 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 140 | BUY | STABILIZE | 25.0 | 6 | 48 | 4 | 26.0 | Enfeitiçador/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23413366079330444 | 0.0 | 0.0 | +3625f791-4c9f-4b95-bdf7-4a322dcd55d3 / -— |
| Jogador 5 | 3-7 | 142 | BUY | ALL_IN | 14.0 | 6 | 56 | 5 | 34.0 | Enfeitiçador/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33382198214530945 | 0.0 | 0.0 | +b2a77bec-e150-4d98-847c-9f2cfb50cbe7 / -— |
| Jogador 5 | 3-7 | 143 | REROLL | ALL_IN | 14.0 | 6 | 54 | 5 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009999999776482582 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 144 | REROLL | ALL_IN | 14.0 | 6 | 52 | 5 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2117503136396408 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 145 | REROLL | ALL_IN | 14.0 | 6 | 50 | 5 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25353842973709106 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 146 | REROLL | ALL_IN | 14.0 | 6 | 48 | 4 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2571428120136261 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 147 | REROLL | ALL_IN | 14.0 | 6 | 46 | 4 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17383994162082672 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 148 | REROLL | ALL_IN | 14.0 | 6 | 44 | 4 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0030981635209172964 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 149 | REROLL | ALL_IN | 14.0 | 6 | 42 | 4 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23157881200313568 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 150 | REROLL | ALL_IN | 14.0 | 6 | 40 | 4 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25221845507621765 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 152 | REROLL | ALL_IN | 14.0 | 6 | 49 | 4 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24455009400844574 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 153 | REROLL | ALL_IN | 14.0 | 6 | 47 | 4 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1739143431186676 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 154 | REROLL | ALL_IN | 14.0 | 6 | 45 | 4 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0022137758787721395 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 155 | REROLL | ALL_IN | 14.0 | 6 | 43 | 4 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028264746069908142 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 156 | REROLL | ALL_IN | 14.0 | 6 | 41 | 4 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1772184520959854 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 157 | REROLL | ALL_IN | 14.0 | 6 | 39 | 3 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17383994162082672 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 158 | REROLL | ALL_IN | 14.0 | 6 | 37 | 3 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11504834145307541 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 159 | REROLL | ALL_IN | 14.0 | 6 | 35 | 3 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026395395398139954 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 160 | REROLL | ALL_IN | 14.0 | 6 | 33 | 3 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0076034110970795155 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 162 | REROLL | ALL_IN | 1.0 | 6 | 42 | 4 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1588074415922165 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 163 | REROLL | ALL_IN | 1.0 | 6 | 40 | 4 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25312328338623047 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 164 | REROLL | ALL_IN | 1.0 | 6 | 38 | 3 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11535241454839706 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 165 | REROLL | ALL_IN | 1.0 | 6 | 36 | 3 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19991160929203033 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 166 | REROLL | ALL_IN | 1.0 | 6 | 34 | 3 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1710834801197052 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 167 | REROLL | ALL_IN | 1.0 | 6 | 32 | 3 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09606262296438217 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 168 | REROLL | ALL_IN | 1.0 | 6 | 30 | 3 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25299593806266785 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 169 | REROLL | ALL_IN | 1.0 | 6 | 28 | 2 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11369045823812485 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 170 | REROLL | ALL_IN | 1.0 | 6 | 26 | 2 | 34.0 | Enfeitiçador/DA_18_Warwick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18923933804035187 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 172 | PASS | ALL_IN | 0.0 | 6 | 24 | 2 | 0.0 | Enfeitiçador/DA_18_Warwick | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 180 | PASS | ALL_IN | 0.0 | 6 | 24 | 2 | 0.0 | Enfeitiçador/DA_18_Warwick | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 182 | PASS | ALL_IN | 0.0 | 6 | 24 | 2 | 0.0 | Enfeitiçador/DA_18_Warwick | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 191 | PASS | ALL_IN | 0.0 | 6 | 24 | 2 | 0.0 | Enfeitiçador/DA_18_Warwick | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 201 | PASS | ALL_IN | 0.0 | 6 | 24 | 2 | 0.0 | Enfeitiçador/DA_18_Warwick | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 211 | PASS | ALL_IN | 0.0 | 6 | 24 | 2 | 0.0 | Enfeitiçador/DA_18_Warwick | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 220 | PASS | ALL_IN | 0.0 | 6 | 24 | 2 | 0.0 | Enfeitiçador/DA_18_Warwick | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 222 | PASS | ALL_IN | 0.0 | 6 | 24 | 2 | 0.0 | Enfeitiçador/DA_18_Warwick | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 232 | PASS | ALL_IN | 0.0 | 6 | 24 | 2 | 0.0 | Enfeitiçador/DA_18_Warwick | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 242 | PASS | ALL_IN | 0.0 | 6 | 24 | 2 | 0.0 | Enfeitiçador/DA_18_Warwick | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 252 | PASS | ALL_IN | 0.0 | 6 | 24 | 2 | 0.0 | Enfeitiçador/DA_18_Warwick | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 262 | PASS | ALL_IN | 0.0 | 6 | 24 | 2 | 0.0 | Enfeitiçador/DA_18_Warwick | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 272 | PASS | ALL_IN | 0.0 | 6 | 24 | 2 | 0.0 | Enfeitiçador/DA_18_Warwick | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 282 | PASS | ALL_IN | 0.0 | 6 | 24 | 2 | 0.0 | Enfeitiçador/DA_18_Warwick | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.05258461460471153 | 0.0 | 0.0 | +— / -698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +9002992e-4dcd-4fec-939c-87393464a41d / -— |
| Jogador 6 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.6080599427223206 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.04858612269163132 | 0.0 | 0.0 | +4d0bf502-ac30-4cdb-9da7-4f9a7ab054b1 / -— |
| Jogador 6 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7729324102401733 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 13 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5744122862815857 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 14 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 20 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.00015411031199619174 | 0.0 | 0.0 | +c3c53e80-c8e2-4774-afa2-9b0f4ab3b326 / -— |
| Jogador 6 | 1-3 | 21 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4659231901168823 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 22 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | -0.29711833596229553 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 23 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Teemo | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 29 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 38 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9764366745948792 | 0.0 | 0.0 | +646fc826-453b-479f-97d1-8aa2a9d86dc3 / -— |
| Jogador 6 | 2-1 | 39 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5078547596931458 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 40 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.07755864411592484 | 0.0 | 0.0 | +75005e9c-56d1-48d6-815e-573e489e3dd7 / -— |
| Jogador 6 | 2-1 | 41 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 12.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05061548203229904 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 42 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2211817353963852 | 0.0 | 0.0 | +— / -9002992e-4dcd-4fec-939c-87393464a41d |
| Jogador 6 | 2-1 | 43 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1607125997543335 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 45 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.38811734318733215 | 0.0 | 0.0 | +0d8b39fc-eb5c-4679-b615-50cdfdcf3eee / -— |
| Jogador 6 | 2-2 | 46 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3416791558265686 | 0.0 | 0.0 | +98558a52-389f-46fc-b370-6345603f4103 / -— |
| Jogador 6 | 2-2 | 47 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17521606385707855 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 48 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 49 | SELL | STABILIZE | 100.0 | 4 | 1 | 0 | 18.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05012368783354759 | 0.0 | 0.0 | +— / -4d0bf502-ac30-4cdb-9da7-4f9a7ab054b1 |
| Jogador 6 | 2-2 | 50 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39167913794517517 | 0.0 | 0.0 | +— / -98558a52-389f-46fc-b370-6345603f4103 |
| Jogador 6 | 2-3 | 52 | BUY | STABILIZE | 100.0 | 4 | 12 | 1 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9594868421554565 | 0.0 | 0.0 | +491eb6b6-54f4-4de8-bc63-d96c6c1d9cce / -— |
| Jogador 6 | 2-3 | 53 | SELL | STABILIZE | 100.0 | 4 | 10 | 1 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3195076882839203 | 0.0 | 0.0 | +— / -491eb6b6-54f4-4de8-bc63-d96c6c1d9cce |
| Jogador 6 | 2-3 | 54 | BUY_XP | STABILIZE | 100.0 | 4 | 12 | 1 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3370000123977661 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 55 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3155084550380707 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 6 | 2-3 | 56 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0015779262175783515 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 57 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.047616127878427505 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 58 | PASS | STABILIZE | 100.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 60 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.489174485206604 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 62 | BUY | STABILIZE | 94.0 | 5 | 11 | 1 | 22.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.250997394323349 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 6 | 2-4 | 63 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 8 | 0 | 22.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0018620288465172052 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 64 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 8 | 0 | 22.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0055463979952037334 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 65 | BUY_XP | STABILIZE | 94.0 | 5 | 8 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 66 | BUY_XP | STABILIZE | 94.0 | 5 | 4 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 67 | SELL | STABILIZE | 94.0 | 5 | 0 | 0 | 24.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039747174829244614 | 0.0 | 0.0 | +— / -b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 6 | 2-5 | 69 | BUY_XP | STABILIZE | 94.0 | 5 | 7 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 70 | PASS | STABILIZE | 94.0 | 5 | 3 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 75 | BUY | STABILIZE | 88.0 | 6 | 9 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.95969557762146 | 0.0 | 0.0 | +3fc2815d-c456-47c3-bb27-783336b3cdfa / -— |
| Jogador 6 | 2-6 | 76 | BUY | STABILIZE | 88.0 | 6 | 6 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44189783930778503 | 0.0 | 0.0 | +b3f8c1ae-0292-46d8-bb32-06b85a46353d / -— |
| Jogador 6 | 2-6 | 77 | MOVE_BENCH | STABILIZE | 88.0 | 6 | 3 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5598076581954956 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 78 | MOVE_BOARD | STABILIZE | 88.0 | 6 | 3 | 0 | 30.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 79 | MOVE_BOARD | STABILIZE | 88.0 | 6 | 3 | 0 | 30.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11549056321382523 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 80 | MOVE_BOARD | STABILIZE | 88.0 | 6 | 3 | 0 | 30.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17997249960899353 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 82 | BUY_XP | STABILIZE | 88.0 | 6 | 9 | 0 | 30.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 83 | BUY_XP | STABILIZE | 88.0 | 6 | 5 | 0 | 30.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 84 | SELL | STABILIZE | 88.0 | 6 | 1 | 0 | 30.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11473846435546875 | 0.0 | 0.0 | +— / -b3f8c1ae-0292-46d8-bb32-06b85a46353d |
| Jogador 6 | 2-7 | 85 | BUY_XP | STABILIZE | 88.0 | 6 | 4 | 0 | 30.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 86 | MOVE_BOARD | STABILIZE | 88.0 | 6 | 0 | 0 | 30.0 | —/DA_18_Tristana | MOVE_BOARD, PASS | True | True | -0.23917256295681 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 87 | PASS | STABILIZE | 88.0 | 6 | 0 | 0 | 30.0 | —/DA_18_Tristana | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 92 | BUY | STABILIZE | 88.0 | 6 | 5 | 0 | 30.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.13905896246433258 | 0.0 | 0.0 | +1e504283-c5d1-4eb3-915e-20533ec3a756 / -— |
| Jogador 6 | 3-1 | 93 | MOVE_BENCH | STABILIZE | 88.0 | 6 | 1 | 0 | 30.0 | —/DA_18_Ahri | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3651528060436249 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 94 | SELL | STABILIZE | 88.0 | 6 | 1 | 0 | 34.0 | Vivaz/DA_18_Ahri | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12158256769180298 | 0.0 | 0.0 | +— / -c3c53e80-c8e2-4774-afa2-9b0f4ab3b326 |
| Jogador 6 | 3-1 | 95 | MOVE_BOARD | STABILIZE | 88.0 | 6 | 3 | 0 | 34.0 | Vivaz/DA_18_Ahri | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 96 | MOVE_BOARD | STABILIZE | 88.0 | 6 | 3 | 0 | 34.0 | Vivaz/DA_18_Ahri | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.32658734917640686 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 97 | PASS | STABILIZE | 88.0 | 6 | 3 | 0 | 34.0 | Vivaz/DA_18_Ahri | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 102 | MOVE_BOARD | STABILIZE | 88.0 | 6 | 10 | 1 | 34.0 | Vivaz/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 103 | MOVE_BOARD | STABILIZE | 88.0 | 6 | 10 | 1 | 34.0 | Vivaz/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.16712558269500732 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 104 | BUY_XP | STABILIZE | 88.0 | 6 | 10 | 1 | 34.0 | Vivaz/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 105 | BUY_XP | STABILIZE | 88.0 | 6 | 6 | 0 | 34.0 | Vivaz/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 106 | MOVE_BOARD | STABILIZE | 88.0 | 6 | 2 | 0 | 34.0 | Vivaz/DA_18_Ahri | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.04204273596405983 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 107 | PASS | STABILIZE | 88.0 | 6 | 2 | 0 | 34.0 | Vivaz/DA_18_Ahri | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 112 | BUY | STABILIZE | 78.0 | 6 | 7 | 0 | 34.0 | Vivaz/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7439674735069275 | 0.0 | 0.0 | +c07fa6e1-195e-4a06-ba8f-b75213704c8a / -— |
| Jogador 6 | 3-3 | 113 | BUY_XP | STABILIZE | 78.0 | 6 | 4 | 0 | 34.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 114 | SELL | STABILIZE | 78.0 | 6 | 0 | 0 | 34.0 | Vivaz/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3678070306777954 | 0.0 | 0.0 | +— / -c07fa6e1-195e-4a06-ba8f-b75213704c8a |
| Jogador 6 | 3-3 | 115 | PASS | STABILIZE | 78.0 | 6 | 3 | 0 | 34.0 | Vivaz/DA_18_Ahri | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 121 | BUY | STABILIZE | 66.0 | 6 | 9 | 0 | 34.0 | Vivaz/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.01749824546277523 | 0.0 | 0.0 | +cce8de69-f877-4e86-b720-6aea91e68f47 / -— |
| Jogador 6 | 3-4 | 122 | MOVE_BENCH | STABILIZE | 66.0 | 6 | 5 | 0 | 34.0 | Vivaz/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0333319753408432 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 123 | BUY_XP | STABILIZE | 66.0 | 6 | 5 | 0 | 36.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7544999718666077 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 124 | MOVE_BENCH | STABILIZE | 66.0 | 7 | 1 | 0 | 36.0 | Vivaz/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49485358595848083 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 125 | PASS | STABILIZE | 66.0 | 7 | 1 | 0 | 42.0 | Vivaz/DA_18_Lillia | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 131 | PASS | STABILIZE | 66.0 | 7 | 7 | 0 | 42.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 140 | BUY_XP | STABILIZE | 66.0 | 7 | 13 | 1 | 42.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 142 | PASS | STABILIZE | 66.0 | 7 | 17 | 1 | 42.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 152 | BUY | STABILIZE | 66.0 | 7 | 24 | 2 | 42.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8637892603874207 | 0.0 | 0.0 | +42cf45df-f7dd-418d-a241-d89e69523352 / -3fc2815d-c456-47c3-bb27-783336b3cdfa,75005e9c-56d1-48d6-815e-573e489e3dd7 |
| Jogador 6 | 4-1 | 153 | BUY | STABILIZE | 66.0 | 7 | 21 | 2 | 30.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6343801021575928 | 0.0 | 0.0 | +ddae48a6-5360-4660-9fa1-143ac35635ee / -— |
| Jogador 6 | 4-1 | 154 | MOVE_BENCH | STABILIZE | 66.0 | 7 | 18 | 1 | 30.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4344606399536133 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 155 | MOVE_BOARD | STABILIZE | 66.0 | 7 | 18 | 1 | 42.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 156 | MOVE_BOARD | STABILIZE | 66.0 | 7 | 18 | 1 | 42.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05637349188327789 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 157 | MOVE_BOARD | STABILIZE | 66.0 | 7 | 18 | 1 | 42.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1795770227909088 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 158 | BUY_XP | STABILIZE | 66.0 | 7 | 18 | 1 | 42.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 159 | BUY_XP | STABILIZE | 66.0 | 7 | 14 | 1 | 42.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 160 | MOVE_BENCH | STABILIZE | 66.0 | 7 | 10 | 1 | 42.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15223512053489685 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 162 | PASS | STABILIZE | 66.0 | 7 | 18 | 1 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 172 | BUY_XP | STABILIZE | 55.0 | 7 | 24 | 2 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 173 | BUY_XP | STABILIZE | 55.0 | 7 | 20 | 2 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 174 | BUY_XP | STABILIZE | 55.0 | 7 | 16 | 1 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 175 | BUY_XP | STABILIZE | 55.0 | 7 | 12 | 1 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 176 | BUY_XP | STABILIZE | 55.0 | 7 | 8 | 0 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 177 | BUY_XP | STABILIZE | 55.0 | 7 | 4 | 0 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 178 | PASS | STABILIZE | 55.0 | 7 | 0 | 0 | 48.0 | Vivaz/DA_18_Rammus | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 180 | BUY_XP | STABILIZE | 55.0 | 7 | 6 | 0 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4248124957084656 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 182 | PASS | ECON | 55.0 | 8 | 7 | 0 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 191 | BUY | ECON | 55.0 | 8 | 14 | 1 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6553453207015991 | 0.0 | 0.0 | +2adb37ce-c46e-4c3a-a715-443bdb688103 / -— |
| Jogador 6 | 4-6 | 192 | MOVE_BENCH | ECON | 55.0 | 8 | 10 | 1 | 48.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10984427481889725 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 193 | BUY_XP | ECON | 55.0 | 8 | 10 | 1 | 56.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 194 | BUY_XP | ECON | 55.0 | 8 | 6 | 0 | 56.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 195 | MOVE_BOARD | ECON | 55.0 | 8 | 2 | 0 | 56.0 | Vivaz/DA_18_Rammus | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.009366531856358051 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 196 | PASS | ECON | 55.0 | 8 | 2 | 0 | 56.0 | Vivaz/DA_18_Rammus | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 201 | BUY | WINSTREAK | 55.0 | 8 | 9 | 0 | 56.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08360012620687485 | 0.0 | 0.0 | +8bd97bbd-01b6-4941-97db-510b7e2e6361 / -— |
| Jogador 6 | 4-7 | 202 | PASS | WINSTREAK | 55.0 | 8 | 5 | 0 | 56.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 211 | EQUIP_FROM_INVENTORY | WINSTREAK | 55.0 | 8 | 11 | 1 | 56.0 | Vivaz/DA_18_Rammus | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 212 | BUY | WINSTREAK | 55.0 | 8 | 11 | 1 | 56.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7270487546920776 | 0.0 | 0.0 | +cdd76540-e76c-41e9-ac02-253f5ba2e75e / -2adb37ce-c46e-4c3a-a715-443bdb688103,cce8de69-f877-4e86-b720-6aea91e68f47 |
| Jogador 6 | 5-1 | 213 | BUY | WINSTREAK | 55.0 | 8 | 7 | 0 | 40.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07340254634618759 | 0.0 | 0.0 | +22f1ab5f-b752-49e7-b6f0-ed9b5e641d64 / -— |
| Jogador 6 | 5-1 | 214 | MOVE_BENCH | WINSTREAK | 55.0 | 8 | 2 | 0 | 40.0 | Vivaz/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.21704868972301483 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 215 | CRAFT_AND_EQUIP | WINSTREAK | 55.0 | 8 | 2 | 0 | 48.0 | Vivaz/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.15405790507793427 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 216 | MOVE_BOARD | WINSTREAK | 55.0 | 8 | 2 | 0 | 48.0 | Vivaz/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07977375388145447 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 217 | MOVE_BOARD | WINSTREAK | 55.0 | 8 | 2 | 0 | 48.0 | Vivaz/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.127062126994133 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 218 | MOVE_BOARD | WINSTREAK | 55.0 | 8 | 2 | 0 | 48.0 | Vivaz/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3115563690662384 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 220 | PASS | STABILIZE | 38.0 | 8 | 7 | 0 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 222 | PASS | STABILIZE | 38.0 | 8 | 13 | 1 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 232 | BUY | STABILIZE | 38.0 | 8 | 21 | 2 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25860100984573364 | 0.0 | 0.0 | +31f86c34-a81d-4ba0-9136-c9106b0fbec5 / -— |
| Jogador 6 | 5-4 | 233 | BUY_XP | STABILIZE | 38.0 | 8 | 18 | 1 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 234 | BUY_XP | STABILIZE | 38.0 | 8 | 14 | 1 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 235 | BUY_XP | STABILIZE | 38.0 | 8 | 10 | 1 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 236 | BUY_XP | STABILIZE | 38.0 | 8 | 6 | 0 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 237 | MOVE_BOARD | STABILIZE | 38.0 | 8 | 2 | 0 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.275320440530777 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 238 | MOVE_BOARD | STABILIZE | 38.0 | 8 | 2 | 0 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2568742036819458 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 239 | PASS | STABILIZE | 38.0 | 8 | 2 | 0 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 242 | PASS | STABILIZE | 38.0 | 8 | 8 | 0 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 252 | BUY | STABILIZE | 38.0 | 8 | 15 | 1 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7439745664596558 | 0.0 | 0.0 | +eb200e13-0a0f-44e1-beae-7be91ae8fc7c / -— |
| Jogador 6 | 5-6 | 253 | BUY_XP | STABILIZE | 38.0 | 8 | 12 | 1 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 254 | BUY_XP | STABILIZE | 38.0 | 8 | 8 | 0 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 255 | BUY_XP | STABILIZE | 38.0 | 8 | 4 | 0 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 256 | PASS | STABILIZE | 38.0 | 8 | 0 | 0 | 64.0 | Vivaz/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 262 | BUY | STABILIZE | 20.0 | 8 | 5 | 0 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.743966281414032 | 0.0 | 0.0 | +817c7a79-054e-456a-a3d0-26c9f81ed3de / -— |
| Jogador 6 | 5-7 | 263 | REROLL | STABILIZE | 20.0 | 8 | 2 | 0 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17390967905521393 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 264 | PASS | STABILIZE | 20.0 | 8 | 0 | 0 | 64.0 | Vivaz/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 272 | EQUIP_FROM_INVENTORY | STABILIZE | 20.0 | 8 | 5 | 0 | 64.0 | Vivaz/DA_18_Lillia | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 273 | EQUIP_FROM_INVENTORY | STABILIZE | 20.0 | 8 | 5 | 0 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | -0.01176369283348322 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 274 | REROLL | STABILIZE | 20.0 | 8 | 5 | 0 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14645744860172272 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 275 | REROLL | STABILIZE | 20.0 | 8 | 3 | 0 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11283456534147263 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 276 | PASS | STABILIZE | 20.0 | 8 | 1 | 0 | 64.0 | Vivaz/DA_18_Lillia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 282 | BUY | STABILIZE | 20.0 | 8 | 7 | 0 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5820127725601196 | 0.0 | 0.0 | +a90199c3-c115-4554-b990-e29c331bafee / -— |
| Jogador 6 | 6-2 | 283 | REROLL | STABILIZE | 20.0 | 8 | 3 | 0 | 64.0 | Vivaz/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17351140081882477 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 284 | PASS | STABILIZE | 20.0 | 8 | 1 | 0 | 64.0 | Vivaz/DA_18_Lillia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.040030770003795624 | 0.0 | 0.0 | +— / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987 |
| Jogador 7 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +c2a4318c-af60-41e2-8e14-c3ad967569a0 / -— |
| Jogador 7 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.6080599427223206 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9794912934303284 | 0.0 | 0.0 | +4e206e09-40e3-4699-81cb-8aaf01109dea / -— |
| Jogador 7 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 13 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11205994337797165 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 14 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 20 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.23040270805358887 | 0.0 | 0.0 | +42edb83f-b613-45e2-95e2-d603ddf9d104 / -— |
| Jogador 7 | 1-3 | 21 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06000559404492378 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 22 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Elise | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3588418960571289 | 0.0 | 0.0 | +— / -4e206e09-40e3-4699-81cb-8aaf01109dea |
| Jogador 7 | 1-3 | 23 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.12844476103782654 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3135429620742798 | 0.0 | 0.0 | +734c75dd-d0f3-4b9f-abe8-a228e23557a2 / -— |
| Jogador 7 | 1-3 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013683632016181946 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 26 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3788042664527893 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 27 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_Scuttlecrab18 | MOVE_BOARD, PASS | True | True | 0.10621310770511627 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 29 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 38 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9562528133392334 | 0.0 | 0.0 | +de82e676-8d8b-4437-958e-a8398a3cfade / -— |
| Jogador 7 | 2-1 | 39 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018751053139567375 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 40 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 41 | PASS | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 45 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 11 | 1 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.036966722458601 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 46 | BUY_XP | STABILIZE | 100.0 | 4 | 11 | 1 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 47 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.44200000166893005 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 48 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.27402448654174805 | 0.0 | 0.0 | +4b4cc4ba-04a0-4e04-88f2-e6913a342285 / -— |
| Jogador 7 | 2-2 | 49 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Hecarim | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17376793920993805 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 50 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 20.0 | —/DA_18_Hecarim | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 52 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.13516078889369965 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 53 | BUY_XP | STABILIZE | 100.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 54 | PASS | STABILIZE | 100.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 62 | BUY | STABILIZE | 100.0 | 5 | 10 | 1 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4038276970386505 | 0.0 | 0.0 | +0c9ac713-08bd-4fa7-a94a-2ab70d7815ff / -— |
| Jogador 7 | 2-4 | 63 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 20.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17439033091068268 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 64 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 65 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030950147658586502 | 0.0 | 0.0 | +— / -42edb83f-b613-45e2-95e2-d603ddf9d104 |
| Jogador 7 | 2-4 | 66 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 67 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 24.0 | —/DA_Sentinel18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 69 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19200000166893005 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 70 | PASS | STABILIZE | 100.0 | 6 | 2 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 75 | BUY | STABILIZE | 100.0 | 6 | 9 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.430830717086792 | 0.0 | 0.0 | +729ccd5b-adc5-4bca-9523-dcb532e93ecb / -— |
| Jogador 7 | 2-6 | 76 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 6 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7263758182525635 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 77 | BUY_XP | ECON | 100.0 | 6 | 6 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 78 | MOVE_BOARD | ECON | 100.0 | 6 | 2 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.06348513811826706 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 79 | MOVE_BOARD | ECON | 100.0 | 6 | 2 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.3370322287082672 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 80 | MOVE_BOARD | ECON | 100.0 | 6 | 2 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 82 | BUY_XP | ECON | 100.0 | 6 | 10 | 1 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.15800000727176666 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 83 | BUY_XP | ECON | 100.0 | 6 | 6 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 84 | MOVE_BOARD | ECON | 100.0 | 6 | 2 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.032957449555397034 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 85 | PASS | ECON | 100.0 | 6 | 2 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 92 | PASS | ECON | 100.0 | 6 | 9 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 102 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 19 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.1843842715024948 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 103 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 19 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1796598732471466 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 104 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 19 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.008327384479343891 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 105 | BUY_XP | STABILIZE | 100.0 | 6 | 19 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 106 | BUY_XP | STABILIZE | 100.0 | 6 | 15 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 107 | BUY_XP | STABILIZE | 100.0 | 6 | 11 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 108 | BUY_XP | STABILIZE | 100.0 | 6 | 7 | 0 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.421999990940094 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 109 | PASS | STABILIZE | 100.0 | 7 | 3 | 0 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 112 | BUY | STABILIZE | 100.0 | 7 | 12 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8312461376190186 | 0.0 | 0.0 | +c4c0b136-020d-4c1e-9517-8e0bf4c5a628 / -734c75dd-d0f3-4b9f-abe8-a228e23557a2,de82e676-8d8b-4437-958e-a8398a3cfade |
| Jogador 7 | 3-3 | 113 | BUY | STABILIZE | 100.0 | 7 | 10 | 1 | 22.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.043097153306007385 | 0.0 | 0.0 | +ff0d9869-c346-4210-be85-1e802a25dd8b / -— |
| Jogador 7 | 3-3 | 114 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 7 | 0 | 22.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33946937322616577 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 115 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 7 | 0 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14187636971473694 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 116 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 7 | 0 | 30.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 117 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 7 | 0 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16431555151939392 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 118 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 7 | 0 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3384980857372284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 119 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 7 | 0 | 30.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1769431233406067 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 121 | BUY | STABILIZE | 89.0 | 7 | 12 | 1 | 36.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6629677414894104 | 0.0 | 0.0 | +a9c52953-4532-455b-851f-04079adfd354 / -— |
| Jogador 7 | 3-4 | 122 | BUY | STABILIZE | 89.0 | 7 | 9 | 0 | 36.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28564783930778503 | 0.0 | 0.0 | +ccdd8153-af58-4fe7-994c-d49f0a7a17f8 / -— |
| Jogador 7 | 3-4 | 123 | BUY | STABILIZE | 89.0 | 7 | 7 | 0 | 36.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0913093313574791 | 0.0 | 0.0 | +aaa84ce8-7919-4ec3-92eb-cc03a9decca9 / -— |
| Jogador 7 | 3-4 | 124 | MOVE_BOARD | STABILIZE | 89.0 | 7 | 3 | 0 | 36.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.032957449555397034 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 125 | MOVE_BENCH | STABILIZE | 89.0 | 7 | 3 | 0 | 36.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46669280529022217 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 126 | MOVE_BOARD | STABILIZE | 89.0 | 7 | 3 | 0 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 127 | MOVE_BOARD | STABILIZE | 89.0 | 7 | 3 | 0 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 128 | PASS | STABILIZE | 89.0 | 7 | 3 | 0 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 131 | MOVE_BOARD | STABILIZE | 89.0 | 7 | 8 | 0 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1723160594701767 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 132 | MOVE_BOARD | STABILIZE | 89.0 | 7 | 8 | 0 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17825105786323547 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 133 | SELL | STABILIZE | 89.0 | 7 | 8 | 0 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14209230244159698 | 0.0 | 0.0 | +— / -aaa84ce8-7919-4ec3-92eb-cc03a9decca9 |
| Jogador 7 | 3-5 | 134 | MOVE_BOARD | STABILIZE | 89.0 | 7 | 12 | 1 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.282122939825058 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 135 | MOVE_BOARD | STABILIZE | 89.0 | 7 | 12 | 1 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 136 | PASS | STABILIZE | 89.0 | 7 | 12 | 1 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 140 | BUY | STABILIZE | 78.0 | 7 | 19 | 1 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0008515400113537908 | 0.0 | 0.0 | +1d7ccf69-9aaa-4f0c-81ed-a94ef995d915 / -— |
| Jogador 7 | 3-7 | 142 | BUY | STABILIZE | 78.0 | 7 | 22 | 2 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6769916415214539 | 0.0 | 0.0 | +9cb61b5c-2c8a-43a2-a854-517f4377f6db / -— |
| Jogador 7 | 3-7 | 143 | BUY | STABILIZE | 78.0 | 7 | 18 | 1 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7453402280807495 | 0.0 | 0.0 | +c617e958-b482-40ce-ab24-acff4dc48bc0 / -— |
| Jogador 7 | 3-7 | 144 | MOVE_BOARD | STABILIZE | 78.0 | 7 | 16 | 1 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 145 | MOVE_BOARD | STABILIZE | 78.0 | 7 | 16 | 1 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008921255357563496 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 146 | MOVE_BOARD | STABILIZE | 78.0 | 7 | 16 | 1 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 147 | MOVE_BOARD | STABILIZE | 78.0 | 7 | 16 | 1 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 148 | PASS | STABILIZE | 78.0 | 7 | 16 | 1 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 152 | REROLL | STABILIZE | 78.0 | 7 | 22 | 2 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.047346219420433044 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 153 | REROLL | STABILIZE | 78.0 | 7 | 20 | 2 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24666593968868256 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 154 | REROLL | STABILIZE | 78.0 | 7 | 18 | 1 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13899798691272736 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 155 | BUY | STABILIZE | 78.0 | 7 | 16 | 1 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6856105327606201 | 0.0 | 0.0 | +815aab3d-cea8-4ca6-aea3-3c9d656e6edd / -— |
| Jogador 7 | 4-1 | 156 | REROLL | STABILIZE | 78.0 | 7 | 13 | 1 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13912011682987213 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 157 | BUY | STABILIZE | 78.0 | 7 | 11 | 1 | 40.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7535265684127808 | 0.0 | 0.0 | +d1bc6c5b-74a5-46db-b00f-e91265546f5d / -729ccd5b-adc5-4bca-9523-dcb532e93ecb,a9c52953-4532-455b-851f-04079adfd354 |
| Jogador 7 | 4-1 | 158 | BUY | STABILIZE | 78.0 | 7 | 8 | 0 | 34.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2830284535884857 | 0.0 | 0.0 | +68301141-c9f1-4303-9775-753520772836 / -— |
| Jogador 7 | 4-1 | 159 | MOVE_BENCH | STABILIZE | 78.0 | 7 | 5 | 0 | 34.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8175404667854309 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 160 | MOVE_BOARD | STABILIZE | 78.0 | 7 | 5 | 0 | 46.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33873501420021057 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 162 | BUY | STABILIZE | 65.0 | 7 | 10 | 1 | 46.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2037557065486908 | 0.0 | 0.0 | +9f445115-49cc-4647-91a0-a80e347e9c62 / -— |
| Jogador 7 | 4-2 | 163 | BUY | STABILIZE | 65.0 | 7 | 7 | 0 | 46.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7478527426719666 | 0.0 | 0.0 | +b701c6c1-2e19-44b9-ad6e-e5d64e1d364c / -— |
| Jogador 7 | 4-2 | 164 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 6 | 0 | 46.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02132791094481945 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 165 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 6 | 0 | 46.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13276995718479156 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 166 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 6 | 0 | 46.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04875248298048973 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 167 | REROLL | STABILIZE | 65.0 | 7 | 6 | 0 | 46.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1458871066570282 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 168 | BUY | STABILIZE | 65.0 | 7 | 4 | 0 | 46.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8356494903564453 | 0.0 | 0.0 | +ceaf1f61-1aa5-404e-ae3f-17db9137ceb7 / -c617e958-b482-40ce-ab24-acff4dc48bc0,ccdd8153-af58-4fe7-994c-d49f0a7a17f8 |
| Jogador 7 | 4-2 | 169 | REROLL | STABILIZE | 65.0 | 7 | 2 | 0 | 42.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17336972057819366 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 170 | MOVE_BENCH | STABILIZE | 65.0 | 7 | 0 | 0 | 42.0 | Vanguarda/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47297656536102295 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 172 | BUY | STABILIZE | 65.0 | 7 | 6 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27435094118118286 | 0.0 | 0.0 | +6eff87be-d18f-4f46-a9c6-9ae977c887e0 / -— |
| Jogador 7 | 4-3 | 173 | REROLL | STABILIZE | 65.0 | 7 | 4 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02994687855243683 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 174 | REROLL | STABILIZE | 65.0 | 7 | 2 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1156238317489624 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 175 | SELL | STABILIZE | 65.0 | 7 | 0 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3445592522621155 | 0.0 | 0.0 | +— / -b701c6c1-2e19-44b9-ad6e-e5d64e1d364c |
| Jogador 7 | 4-3 | 176 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 1 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1769106537103653 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 177 | SELL | STABILIZE | 65.0 | 7 | 1 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.181739941239357 | 0.0 | 0.0 | +— / -815aab3d-cea8-4ca6-aea3-3c9d656e6edd |
| Jogador 7 | 4-3 | 178 | BUY | STABILIZE | 65.0 | 7 | 4 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7437936663627625 | 0.0 | 0.0 | +85d35881-ba70-4310-8d5f-bae796309eed / -— |
| Jogador 7 | 4-4 | 180 | BUY | STABILIZE | 65.0 | 7 | 8 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0011738186003640294 | 0.0 | 0.0 | +497fbcb9-9d15-43f0-ad71-96eeceeee99d / -— |
| Jogador 7 | 4-5 | 182 | BUY | STABILIZE | 65.0 | 7 | 11 | 1 | 48.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.336128830909729 | 0.0 | 0.0 | +ff6d5b66-5b8f-49b1-bbad-4231b794c2f1 / -— |
| Jogador 7 | 4-5 | 183 | REROLL | STABILIZE | 65.0 | 7 | 8 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14558915793895721 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 184 | BUY | STABILIZE | 65.0 | 7 | 6 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28538239002227783 | 0.0 | 0.0 | +12d02679-e950-433b-ad9e-679a89cf86d8 / -— |
| Jogador 7 | 4-5 | 185 | REROLL | STABILIZE | 65.0 | 7 | 4 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002818257547914982 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 186 | REROLL | STABILIZE | 65.0 | 7 | 2 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17339500784873962 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 187 | SELL | STABILIZE | 65.0 | 7 | 0 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11707692593336105 | 0.0 | 0.0 | +— / -497fbcb9-9d15-43f0-ad71-96eeceeee99d |
| Jogador 7 | 4-5 | 188 | REROLL | STABILIZE | 65.0 | 7 | 3 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17391261458396912 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 189 | SELL | STABILIZE | 65.0 | 7 | 1 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38612884283065796 | 0.0 | 0.0 | +— / -ff6d5b66-5b8f-49b1-bbad-4231b794c2f1 |
| Jogador 7 | 4-6 | 191 | BUY | STABILIZE | 51.0 | 7 | 9 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8338016867637634 | 0.0 | 0.0 | +08479bff-e795-4e51-9f0b-2a84ec36f6a2 / -85d35881-ba70-4310-8d5f-bae796309eed,9f445115-49cc-4647-91a0-a80e347e9c62 |
| Jogador 7 | 4-6 | 192 | REROLL | STABILIZE | 51.0 | 7 | 6 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13356894254684448 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 193 | REROLL | STABILIZE | 51.0 | 7 | 4 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.173361673951149 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 194 | REROLL | STABILIZE | 51.0 | 7 | 2 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07063867151737213 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 195 | MOVE_BOARD | STABILIZE | 51.0 | 7 | 0 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.062415190041065216 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 196 | MOVE_BOARD | STABILIZE | 51.0 | 7 | 0 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31620216369628906 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 197 | MOVE_BOARD | STABILIZE | 51.0 | 7 | 0 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 198 | PASS | STABILIZE | 51.0 | 7 | 0 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 201 | BUY | STABILIZE | 38.0 | 7 | 6 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7394550442695618 | 0.0 | 0.0 | +23181987-d0b2-4e8c-a1a7-48a1e28179f7 / -— |
| Jogador 7 | 4-7 | 202 | REROLL | STABILIZE | 38.0 | 7 | 3 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08411189168691635 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 203 | PASS | STABILIZE | 38.0 | 7 | 1 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 211 | EQUIP_FROM_INVENTORY | STABILIZE | 38.0 | 7 | 7 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 212 | BUY | STABILIZE | 38.0 | 7 | 7 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2838110029697418 | 0.0 | 0.0 | +bed45cda-85fd-407c-a664-ef8acc55b3bf / -— |
| Jogador 7 | 5-1 | 213 | BUY | STABILIZE | 38.0 | 7 | 4 | 0 | 48.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8320284485816956 | 0.0 | 0.0 | +0474e055-4633-408f-837c-b93b86fa46be / -23181987-d0b2-4e8c-a1a7-48a1e28179f7,4b4cc4ba-04a0-4e04-88f2-e6913a342285 |
| Jogador 7 | 5-1 | 214 | BUY | STABILIZE | 38.0 | 7 | 1 | 0 | 42.0 | Vanguarda/DA_KogMaw18_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.08509846031665802 | 0.0 | 0.0 | +fe0cdc83-3953-4aad-86c0-cf907a803a8f / -— |
| Jogador 7 | 5-1 | 215 | CRAFT_AND_EQUIP | STABILIZE | 38.0 | 7 | 0 | 0 | 42.0 | Vanguarda/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18120351433753967 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 216 | SELL | STABILIZE | 38.0 | 7 | 0 | 0 | 42.0 | Vanguarda/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09516923129558563 | 0.0 | 0.0 | +— / -fe0cdc83-3953-4aad-86c0-cf907a803a8f |
| Jogador 7 | 5-1 | 217 | SELL | STABILIZE | 38.0 | 7 | 1 | 0 | 42.0 | Vanguarda/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11400666832923889 | 0.0 | 0.0 | +— / -6eff87be-d18f-4f46-a9c6-9ae977c887e0 |
| Jogador 7 | 5-1 | 218 | BUY | STABILIZE | 38.0 | 7 | 3 | 0 | 42.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08138024806976318 | 0.0 | 0.0 | +bb2609fb-c8cb-4e7a-b308-8cd512ff870d / -— |
| Jogador 7 | 5-2 | 220 | BUY | STABILIZE | 38.0 | 7 | 7 | 0 | 46.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2795025110244751 | 0.0 | 0.0 | +68251e71-5657-42da-9181-7351627204f6 / -— |
| Jogador 7 | 5-3 | 222 | BUY | STABILIZE | 38.0 | 7 | 12 | 1 | 46.0 | Vanguarda/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6638609170913696 | 0.0 | 0.0 | +d2cb6143-37d1-4d0b-9cf3-eff835d5fb8e / -— |
| Jogador 7 | 5-3 | 223 | REROLL | STABILIZE | 38.0 | 7 | 9 | 0 | 46.0 | Vanguarda/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14593224227428436 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 224 | PASS | STABILIZE | 38.0 | 7 | 7 | 0 | 46.0 | Vanguarda/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 232 | PASS | STABILIZE | 21.0 | 7 | 12 | 1 | 46.0 | Vanguarda/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 242 | PASS | STABILIZE | 21.0 | 7 | 18 | 1 | 46.0 | Vanguarda/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 252 | PASS | ALL_IN | 6.0 | 7 | 25 | 2 | 46.0 | Vanguarda/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 262 | PASS | ALL_IN | 6.0 | 7 | 33 | 3 | 46.0 | Vanguarda/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 272 | EQUIP_FROM_INVENTORY | ALL_IN | 6.0 | 7 | 42 | 4 | 46.0 | Vanguarda/DA_KogMaw18_AD | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 273 | EQUIP_FROM_INVENTORY | ALL_IN | 6.0 | 7 | 42 | 4 | 46.0 | Vanguarda/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | -0.00554510485380888 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 274 | PASS | ALL_IN | 6.0 | 7 | 42 | 4 | 46.0 | Vanguarda/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 282 | PASS | ALL_IN | 0.0 | 7 | 42 | 4 | 0.0 | Vanguarda/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 9 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.28737619519233704 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.054392240941524506 | 0.0 | 0.0 | +fddba3f3-87f3-4c97-a7b2-e5d1ef789709 / -— |
| Jogador 8 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3687226474285126 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.948853611946106 | 0.0 | 0.0 | +78019889-2624-4adb-917b-619681f23053 / -— |
| Jogador 8 | 1-2 | 14 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3219278156757355 | 0.0 | 0.0 | +— / -78019889-2624-4adb-917b-619681f23053 |
| Jogador 8 | 1-2 | 15 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 20 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 29 | PASS | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 38 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8736729621887207 | 0.0 | 0.0 | +f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 / -— |
| Jogador 8 | 2-1 | 39 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 9 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 40 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 9 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06262560933828354 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 41 | PASS | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 45 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 14 | 1 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0823926255106926 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 46 | BUY | STABILIZE | 94.0 | 4 | 14 | 1 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.012490112334489822 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 8 | 2-2 | 47 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 11 | 1 | 6.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05081021785736084 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 48 | SELL | STABILIZE | 94.0 | 4 | 11 | 1 | 10.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32656970620155334 | 0.0 | 0.0 | +— / -f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 |
| Jogador 8 | 2-2 | 49 | PASS | STABILIZE | 94.0 | 4 | 12 | 1 | 10.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 52 | BUY | STABILIZE | 89.0 | 4 | 19 | 1 | 10.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.027847466990351677 | 0.0 | 0.0 | +2ace989d-3e9e-483b-9b14-cd6b8f171f17 / -— |
| Jogador 8 | 2-3 | 53 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 16 | 1 | 10.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2843298017978668 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 54 | MOVE_BOARD | STABILIZE | 89.0 | 4 | 16 | 1 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 55 | BUY_XP | STABILIZE | 89.0 | 4 | 16 | 1 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 56 | BUY_XP | STABILIZE | 89.0 | 4 | 12 | 1 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3370000123977661 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 57 | BUY | STABILIZE | 89.0 | 5 | 8 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3855518102645874 | 0.0 | 0.0 | +ce928be1-b3ba-4640-b93c-d15c8a92833e / -— |
| Jogador 8 | 2-3 | 58 | SELL | STABILIZE | 89.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.43555182218551636 | 0.0 | 0.0 | +— / -ce928be1-b3ba-4640-b93c-d15c8a92833e |
| Jogador 8 | 2-3 | 59 | BUY | STABILIZE | 89.0 | 5 | 8 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.35793542861938477 | 0.0 | 0.0 | +d44224c1-925d-42f9-ad60-ff4c36c665d6 / -— |
| Jogador 8 | 2-3 | 60 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49763667583465576 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 62 | BUY | LOSS_STREAK | 83.0 | 5 | 13 | 1 | 18.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2230367213487625 | 0.0 | 0.0 | +6a071ec5-c3f4-41b3-a0d8-c1aee62cffee / -— |
| Jogador 8 | 2-4 | 63 | BUY | LOSS_STREAK | 83.0 | 5 | 10 | 1 | 18.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07929208129644394 | 0.0 | 0.0 | +eb214f08-2367-4b33-af94-8aa504781450 / -— |
| Jogador 8 | 2-4 | 64 | MOVE_BENCH | LOSS_STREAK | 83.0 | 5 | 7 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09457726776599884 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 65 | BUY_XP | LOSS_STREAK | 83.0 | 5 | 7 | 0 | 22.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 66 | SELL | LOSS_STREAK | 83.0 | 5 | 3 | 0 | 22.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04630121961236 | 0.0 | 0.0 | +— / -fddba3f3-87f3-4c97-a7b2-e5d1ef789709 |
| Jogador 8 | 2-4 | 67 | BUY_XP | LOSS_STREAK | 83.0 | 5 | 4 | 0 | 22.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 69 | MOVE_BENCH | LOSS_STREAK | 83.0 | 5 | 6 | 0 | 22.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12228263169527054 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 70 | MOVE_BENCH | LOSS_STREAK | 83.0 | 5 | 6 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13603118062019348 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 71 | MOVE_BENCH | LOSS_STREAK | 83.0 | 5 | 6 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02542947232723236 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 72 | PASS | LOSS_STREAK | 83.0 | 5 | 6 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 75 | MOVE_BENCH | LOSS_STREAK | 78.0 | 5 | 12 | 1 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12216150760650635 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 76 | MOVE_BENCH | LOSS_STREAK | 78.0 | 5 | 12 | 1 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.135880708694458 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 77 | MOVE_BENCH | LOSS_STREAK | 78.0 | 5 | 12 | 1 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03289090469479561 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 78 | PASS | LOSS_STREAK | 78.0 | 5 | 12 | 1 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 82 | SELL | LOSS_STREAK | 72.0 | 5 | 20 | 2 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08372307568788528 | 0.0 | 0.0 | +— / -73185d11-22d3-4a1d-803a-b37e82272098 |
| Jogador 8 | 2-7 | 83 | MOVE_BOARD | LOSS_STREAK | 72.0 | 5 | 23 | 2 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.14408981800079346 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 84 | MOVE_BOARD | LOSS_STREAK | 72.0 | 5 | 23 | 2 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.31834104657173157 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 85 | BUY | LOSS_STREAK | 72.0 | 5 | 23 | 2 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3578798770904541 | 0.0 | 0.0 | +3acb90a6-bcf2-41d1-848f-f2aec19a2163 / -— |
| Jogador 8 | 2-7 | 86 | MOVE_BOARD | LOSS_STREAK | 72.0 | 5 | 20 | 2 | 22.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14474132657051086 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 87 | SELL | LOSS_STREAK | 72.0 | 5 | 20 | 2 | 22.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1221134290099144 | 0.0 | 0.0 | +— / -3acb90a6-bcf2-41d1-848f-f2aec19a2163 |
| Jogador 8 | 2-7 | 88 | MOVE_BOARD | LOSS_STREAK | 72.0 | 5 | 23 | 2 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 89 | BUY_XP | LOSS_STREAK | 72.0 | 5 | 23 | 2 | 22.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.017000000923871994 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 90 | BUY | LOSS_STREAK | 72.0 | 6 | 19 | 1 | 22.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3226768672466278 | 0.0 | 0.0 | +dc90c323-d8b9-44ab-b714-ea0fcc860de9 / -— |
| Jogador 8 | 3-1 | 92 | BUY | LOSS_STREAK | 72.0 | 6 | 24 | 2 | 22.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17898914217948914 | 0.0 | 0.0 | +fd3ab6e7-a3e5-4a03-8aa6-a80f6c0c1f47 / -— |
| Jogador 8 | 3-1 | 93 | MOVE_BENCH | LOSS_STREAK | 72.0 | 6 | 20 | 2 | 22.0 | —/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16226372122764587 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 94 | MOVE_BENCH | LOSS_STREAK | 72.0 | 6 | 20 | 2 | 26.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42999032139778137 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 95 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 20 | 2 | 28.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14360803365707397 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 96 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 20 | 2 | 28.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2943667769432068 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 97 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 20 | 2 | 28.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14559587836265564 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 98 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 20 | 2 | 30.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 99 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 20 | 2 | 30.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008327384479343891 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 100 | BUY_XP | STABILIZE | 72.0 | 6 | 20 | 2 | 30.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 102 | MOVE_BOARD | STABILIZE | 72.0 | 6 | 23 | 2 | 30.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14892859756946564 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 103 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 23 | 2 | 30.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07471486181020737 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 104 | SELL | STABILIZE | 72.0 | 6 | 23 | 2 | 30.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04237861558794975 | 0.0 | 0.0 | +— / -2ace989d-3e9e-483b-9b14-cd6b8f171f17 |
| Jogador 8 | 3-2 | 105 | BUY | STABILIZE | 72.0 | 6 | 26 | 2 | 30.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.19402627646923065 | 0.0 | 0.0 | +527f78df-1e51-4731-9175-1c4812aa82ad / -— |
| Jogador 8 | 3-2 | 106 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 22 | 2 | 30.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4485786259174347 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 107 | MOVE_BENCH | STABILIZE | 72.0 | 6 | 22 | 2 | 30.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14593301713466644 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 108 | BUY_XP | STABILIZE | 72.0 | 6 | 22 | 2 | 32.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 109 | BUY_XP | STABILIZE | 72.0 | 6 | 18 | 1 | 32.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 110 | BUY_XP | STABILIZE | 72.0 | 6 | 14 | 1 | 32.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 112 | BUY_XP | STABILIZE | 72.0 | 6 | 18 | 1 | 32.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 113 | BUY_XP | STABILIZE | 72.0 | 6 | 14 | 1 | 32.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 114 | BUY_XP | STABILIZE | 72.0 | 6 | 10 | 1 | 32.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3244999945163727 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 115 | PASS | STABILIZE | 72.0 | 7 | 6 | 0 | 32.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 119 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 6 | 0 | 32.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3992098867893219 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 121 | PASS | STABILIZE | 72.0 | 7 | 13 | 1 | 38.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 131 | BUY | STABILIZE | 72.0 | 7 | 20 | 2 | 38.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6753684878349304 | 0.0 | 0.0 | +23366968-ed3f-43d0-9f24-bb7691bf5d45 / -— |
| Jogador 8 | 3-5 | 132 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 17 | 1 | 38.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020176485180854797 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 133 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 17 | 1 | 36.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.035912610590457916 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 134 | BUY_XP | STABILIZE | 72.0 | 7 | 17 | 1 | 42.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 135 | BUY_XP | STABILIZE | 72.0 | 7 | 13 | 1 | 42.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 136 | BUY_XP | STABILIZE | 72.0 | 7 | 9 | 0 | 42.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 137 | BUY_XP | STABILIZE | 72.0 | 7 | 5 | 0 | 42.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 138 | PASS | STABILIZE | 72.0 | 7 | 1 | 0 | 42.0 | Colosso/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 140 | BUY_XP | STABILIZE | 72.0 | 7 | 8 | 0 | 42.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 142 | BUY_XP | STABILIZE | 72.0 | 7 | 12 | 1 | 42.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 143 | BUY_XP | STABILIZE | 72.0 | 7 | 8 | 0 | 42.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 144 | BUY_XP | STABILIZE | 72.0 | 7 | 4 | 0 | 42.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 145 | SELL | STABILIZE | 72.0 | 7 | 0 | 0 | 42.0 | Colosso/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09147865325212479 | 0.0 | 0.0 | +— / -d44224c1-925d-42f9-ad60-ff4c36c665d6 |
| Jogador 8 | 3-7 | 146 | PASS | STABILIZE | 72.0 | 7 | 1 | 0 | 42.0 | Colosso/DA_Brambleback18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 152 | CRAFT_AND_EQUIP | STABILIZE | 72.0 | 7 | 8 | 0 | 42.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | — | 0.15237624943256378 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 153 | BUY_XP | STABILIZE | 72.0 | 7 | 8 | 0 | 42.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 154 | BUY_XP | STABILIZE | 72.0 | 7 | 4 | 0 | 42.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 155 | PASS | STABILIZE | 72.0 | 7 | 0 | 0 | 42.0 | Colosso/DA_Brambleback18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 162 | BUY_XP | STABILIZE | 72.0 | 7 | 9 | 0 | 42.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4248124957084656 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 163 | PASS | WINSTREAK | 72.0 | 8 | 5 | 0 | 42.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 172 | BUY | WINSTREAK | 72.0 | 8 | 14 | 1 | 42.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0360683910548687 | 0.0 | 0.0 | +bdee5671-864a-47c9-9576-9e0d8d2a7c6a / -— |
| Jogador 8 | 4-3 | 173 | BUY | WINSTREAK | 72.0 | 8 | 10 | 1 | 42.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2818204164505005 | 0.0 | 0.0 | +1f349179-be2a-4738-bda1-072f7fae2147 / -— |
| Jogador 8 | 4-3 | 174 | BUY_XP | WINSTREAK | 72.0 | 8 | 6 | 0 | 42.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 175 | PASS | WINSTREAK | 72.0 | 8 | 2 | 0 | 42.0 | Colosso/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 178 | MOVE_BENCH | WINSTREAK | 72.0 | 8 | 2 | 0 | 42.0 | Colosso/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6759731769561768 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 180 | BUY_XP | WINSTREAK | 72.0 | 8 | 10 | 1 | 50.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 182 | BUY_XP | WINSTREAK | 72.0 | 8 | 14 | 1 | 50.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 183 | BUY_XP | WINSTREAK | 72.0 | 8 | 10 | 1 | 50.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 184 | BUY_XP | WINSTREAK | 72.0 | 8 | 6 | 0 | 50.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 185 | PASS | WINSTREAK | 72.0 | 8 | 2 | 0 | 50.0 | Colosso/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 191 | BUY_XP | WINSTREAK | 72.0 | 8 | 11 | 1 | 50.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 192 | BUY_XP | WINSTREAK | 72.0 | 8 | 7 | 0 | 50.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 193 | MOVE_BOARD | WINSTREAK | 72.0 | 8 | 3 | 0 | 50.0 | Colosso/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33645081520080566 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 194 | PASS | WINSTREAK | 72.0 | 8 | 3 | 0 | 50.0 | Colosso/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 201 | BUY_XP | WINSTREAK | 72.0 | 8 | 12 | 1 | 50.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 202 | BUY_XP | WINSTREAK | 72.0 | 8 | 8 | 0 | 50.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 203 | BUY_XP | WINSTREAK | 72.0 | 8 | 4 | 0 | 50.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 204 | PASS | WINSTREAK | 72.0 | 8 | 0 | 0 | 50.0 | Colosso/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 211 | EQUIP_FROM_INVENTORY | WINSTREAK | 72.0 | 8 | 8 | 0 | 50.0 | Colosso/DA_Brambleback18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 212 | BUY_XP | WINSTREAK | 72.0 | 8 | 8 | 0 | 50.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 213 | BUY_XP | WINSTREAK | 72.0 | 8 | 4 | 0 | 50.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 214 | PASS | WINSTREAK | 72.0 | 8 | 0 | 0 | 50.0 | Colosso/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 220 | BUY_XP | WINSTREAK | 72.0 | 8 | 9 | 0 | 50.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 222 | MOVE_BENCH | WINSTREAK | 72.0 | 9 | 14 | 1 | 50.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46535465121269226 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 223 | PASS | WINSTREAK | 72.0 | 9 | 14 | 1 | 58.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 232 | BUY_XP | WINSTREAK | 72.0 | 9 | 24 | 2 | 58.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 233 | BUY_XP | WINSTREAK | 72.0 | 9 | 20 | 2 | 58.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 234 | BUY_XP | WINSTREAK | 72.0 | 9 | 16 | 1 | 58.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 235 | BUY_XP | WINSTREAK | 72.0 | 9 | 12 | 1 | 58.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 236 | BUY_XP | WINSTREAK | 72.0 | 9 | 8 | 0 | 58.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 237 | BUY_XP | WINSTREAK | 72.0 | 9 | 4 | 0 | 58.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 238 | PASS | WINSTREAK | 72.0 | 9 | 0 | 0 | 58.0 | Colosso/DA_Brambleback18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 242 | PASS | WINSTREAK | 72.0 | 9 | 8 | 0 | 58.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 252 | BUY_XP | WINSTREAK | 72.0 | 9 | 17 | 1 | 58.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 253 | BUY_XP | WINSTREAK | 72.0 | 9 | 13 | 1 | 58.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 254 | BUY_XP | WINSTREAK | 72.0 | 9 | 9 | 0 | 58.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 255 | BUY_XP | WINSTREAK | 72.0 | 9 | 5 | 0 | 58.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 256 | MOVE_BOARD | WINSTREAK | 72.0 | 9 | 1 | 0 | 58.0 | Colosso/DA_Brambleback18 | BUY, MOVE_BOARD, PASS | True | True | 0.1778765767812729 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 257 | MOVE_BOARD | WINSTREAK | 72.0 | 9 | 1 | 0 | 58.0 | Colosso/DA_Brambleback18 | BUY, MOVE_BOARD, PASS | True | True | -0.26731711626052856 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 258 | MOVE_BOARD | WINSTREAK | 72.0 | 9 | 1 | 0 | 58.0 | Colosso/DA_Brambleback18 | BUY, MOVE_BOARD, PASS | True | True | 0.1795438826084137 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 259 | PASS | WINSTREAK | 72.0 | 9 | 1 | 0 | 58.0 | Colosso/DA_Brambleback18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 262 | BUY_XP | WINSTREAK | 72.0 | 9 | 10 | 1 | 58.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 263 | BUY_XP | WINSTREAK | 72.0 | 9 | 6 | 0 | 58.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 264 | PASS | WINSTREAK | 72.0 | 9 | 2 | 0 | 58.0 | Colosso/DA_Brambleback18 | REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 272 | EQUIP_FROM_INVENTORY | WINSTREAK | 72.0 | 9 | 10 | 1 | 58.0 | Colosso/DA_Brambleback18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 273 | EQUIP_FROM_INVENTORY | WINSTREAK | 72.0 | 9 | 10 | 1 | 58.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08818848431110382 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 274 | BUY_XP | WINSTREAK | 72.0 | 9 | 10 | 1 | 58.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 275 | BUY_XP | WINSTREAK | 72.0 | 9 | 6 | 0 | 58.0 | Colosso/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 276 | PASS | WINSTREAK | 72.0 | 9 | 2 | 0 | 58.0 | Colosso/DA_Brambleback18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 282 | PASS | WINSTREAK | 72.0 | 10 | 10 | 1 | 58.0 | Colosso/DA_Brambleback18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |

O audit_report.json mantém as máscaras brutas, distribuições da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Null indica campo ausente, não zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 140 | 175 | 13 | 8 | 18 | 3 | 7 | 1 | 0 | 0.0 |
- Jogador 1 — gasto por ação: BUY: 73g, BUY_XP: 88g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 14g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 9g, stage 2: 41g, stage 3: 40g, stage 4: 39g, stage 5: 46g, stage 6: 0g
| Jogador 2 | 155 | 161 | 27 | 10 | 3 | 1 | 36 | 3 | 17 | 0.0 |
- Jogador 2 — gasto por ação: BUY: 69g, BUY_XP: 20g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 72g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 6g, stage 2: 46g, stage 3: 37g, stage 4: 72g, stage 5: 0g, stage 6: 0g
| Jogador 3 | 125 | 155 | 22 | 5 | 11 | 1 | 11 | 2 | 3 | 0.0 |
- Jogador 3 — gasto por ação: BUY: 81g, BUY_XP: 52g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 22g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 2g, stage 2: 45g, stage 3: 48g, stage 4: 52g, stage 5: 8g, stage 6: 0g
| Jogador 4 | 148 | 139 | 8 | 12 | 10 | 0 | 18 | 0 | 33 | 0.0 |
- Jogador 4 — gasto por ação: BUY: 59g, BUY_XP: 44g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 36g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 1g, stage 2: 44g, stage 3: 34g, stage 4: 49g, stage 5: 11g, stage 6: 0g
| Jogador 5 | 137 | 153 | 33 | 14 | 1 | 1 | 34 | 1 | 24 | 0.0 |
- Jogador 5 — gasto por ação: BUY: 77g, BUY_XP: 8g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 68g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 2g, stage 2: 38g, stage 3: 77g, stage 4: 36g, stage 5: 0g, stage 6: 0g
| Jogador 6 | 139 | 206 | 18 | 13 | 28 | 2 | 4 | 3 | 1 | 64.0 |
- Jogador 6 — gasto por ação: BUY: 74g, BUY_XP: 124g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 8g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 5g, stage 2: 54g, stage 3: 31g, stage 4: 58g, stage 5: 48g, stage 6: 10g
| Jogador 7 | 152 | 176 | 21 | 12 | 10 | 2 | 17 | 2 | 42 | 0.0 |
- Jogador 7 — gasto por ação: BUY: 90g, BUY_XP: 52g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 34g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 6g, stage 2: 48g, stage 3: 40g, stage 4: 66g, stage 5: 16g, stage 6: 0g
| Jogador 8 | 144 | 242 | 14 | 20 | 46 | 3 | 0 | 0 | 10 | 58.0 |
- Jogador 8 — gasto por ação: BUY: 42g, BUY_XP: 200g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 2g, stage 2: 41g, stage 3: 71g, stage 4: 60g, stage 5: 60g, stage 6: 8g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 1 | 1 | 0 | 0.0% |
| Jogador 2 | 1 | 1 | 0 | 0.0% |
| Jogador 3 | 2 | 2 | 0 | 0.0% |
| Jogador 4 | 1 | 1 | 0 | 0.0% |
| Jogador 5 | 1 | 1 | 0 | 0.0% |
| Jogador 6 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 1 | 1 | 0 | 0.0% |

Os detalhes por transição ficam em audit_report.json. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ médio qualidade | Δ estrutural médio | Δ qualidade quando combate positivo | Δ qualidade quando combate negativo |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 140 | 0 | 0 | 140 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ 0.0000 (26 ações), BUY_XP: Δ 0.0000 (22 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (2 ações), MOVE_BENCH: Δ 0.0000 (24 ações), MOVE_BOARD: Δ 0.0000 (25 ações), PASS: Δ 0.0000 (25 ações), REROLL: Δ 0.0000 (7 ações), SELL: Δ 0.0000 (8 ações)
| Jogador 2 | 155 | 0 | 0 | 155 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ 0.0000 (31 ações), BUY_XP: Δ 0.0000 (5 ações), MOVE_BENCH: Δ 0.0000 (13 ações), MOVE_BOARD: Δ 0.0000 (37 ações), PASS: Δ 0.0000 (20 ações), REROLL: Δ 0.0000 (36 ações), SELL: Δ 0.0000 (13 ações)
| Jogador 3 | 125 | 0 | 0 | 125 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ 0.0000 (29 ações), BUY_XP: Δ 0.0000 (13 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (19 ações), MOVE_BOARD: Δ 0.0000 (19 ações), PASS: Δ 0.0000 (25 ações), REROLL: Δ 0.0000 (11 ações), SELL: Δ 0.0000 (8 ações)
| Jogador 4 | 148 | 0 | 0 | 148 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ 0.0000 (20 ações), BUY_XP: Δ 0.0000 (11 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (29 ações), MOVE_BOARD: Δ 0.0000 (43 ações), PASS: Δ 0.0000 (23 ações), REROLL: Δ 0.0000 (18 ações), SELL: Δ 0.0000 (3 ações)
| Jogador 5 | 137 | 0 | 0 | 137 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ 0.0000 (36 ações), BUY_XP: Δ 0.0000 (2 ações), MOVE_BENCH: Δ 0.0000 (7 ações), MOVE_BOARD: Δ 0.0000 (20 ações), PASS: Δ 0.0000 (20 ações), REROLL: Δ 0.0000 (34 ações), SELL: Δ 0.0000 (18 ações)
| Jogador 6 | 139 | 0 | 0 | 139 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ 0.0000 (25 ações), BUY_XP: Δ 0.0000 (31 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0000 (20 ações), MOVE_BOARD: Δ 0.0000 (20 ações), PASS: Δ 0.0000 (26 ações), REROLL: Δ 0.0000 (4 ações), SELL: Δ 0.0000 (9 ações)
| Jogador 7 | 152 | 0 | 0 | 152 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ 0.0000 (35 ações), BUY_XP: Δ 0.0000 (13 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0000 (15 ações), MOVE_BOARD: Δ 0.0000 (36 ações), PASS: Δ 0.0000 (22 ações), REROLL: Δ 0.0000 (17 ações), SELL: Δ 0.0000 (10 ações)
| Jogador 8 | 144 | 0 | 0 | 144 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ 0.0000 (16 ações), BUY_XP: Δ 0.0000 (50 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0000 (25 ações), MOVE_BOARD: Δ 0.0000 (15 ações), PASS: Δ 0.0000 (26 ações), SELL: Δ 0.0000 (8 ações)

A pontuação é uma heurística para auditoria, não uma verdade absoluta. Compare-a com recompensas e resultados de combate; correlação não prova causalidade.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 1 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 3 | 3 → 3 | 0.063 | 0.000 |
| Jogador 1 | 1-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 5 | 0 | 3 → 3 | 0.000 | 0.000 |
| Jogador 1 | 1-4 | 7 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 5 → 5 | 6 | 3 → 4 | 0.000 | 0.000 |
| Jogador 1 | 2-1 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 5 → 9 | 3 | 4 → 4 | 0.001 | 0.448 |
| Jogador 1 | 2-2 | 7 | 8.000 | 0.000 | 0 → 0 | 0 → 1 | 14% → 18% | 9 → 8 | 9 | 4 → 5 | -0.003 | 0.384 |
| Jogador 1 | 2-3 | 6 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 8 → 5 | 8 | 5 → 5 | -0.003 | -0.413 |
| Jogador 1 | 2-4 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 5 → 6 | 4 | 5 → 5 | 0.000 | 0.000 |
| Jogador 1 | 2-5 | 6 | 2.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 6 → 7 | 6 | 5 → 6 | 0.002 | 0.440 |
| Jogador 1 | 2-6 | 6 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 21% | 7 → 7 | 7 | 6 → 6 | 0.002 | 0.451 |
| Jogador 1 | 2-7 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 7 → 9 | 4 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 3-1 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 9 → 6 | 8 | 6 → 6 | 0.000 | -0.691 |
| Jogador 1 | 3-2 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 6 → 8 | 4 | 6 → 6 | 0.000 | 0.921 |
| Jogador 1 | 3-3 | 9 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 25% | 8 → 8 | 7 | 6 → 7 | 0.014 | 0.320 |
| Jogador 1 | 3-4 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 8 → 6 | 8 | 7 → 7 | -0.005 | 0.000 |
| Jogador 1 | 3-5 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 6 → 9 | 4 | 7 → 7 | 0.000 | 0.961 |
| Jogador 1 | 3-6 | 2 | 0.000 | 8.000 | 0 → 0 | 1 → 1 | 25% → 25% | 9 → 12 | 4 | 7 → 7 | 0.000 | 1.450 |
| Jogador 1 | 3-7 | 7 | 4.000 | 6.000 | 0 → 0 | 1 → 1 | 25% → 25% | 12 → 13 | 5 | 7 → 7 | -0.014 | 0.000 |
| Jogador 1 | 4-1 | 10 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 13 → 6 | 12 | 7 → 7 | 0.004 | -0.263 |
| Jogador 1 | 4-2 | 10 | 0.000 | -4.000 | 0 → 0 | 1 → 0 | 25% → 25% | 6 → 10 | 4 | 7 → 7 | 0.011 | -0.275 |
| Jogador 1 | 4-3 | 6 | 0.000 | -10.000 | 0 → 0 | 0 → 0 | 25% → 25% | 10 → 9 | 12 | 7 → 8 | 0.010 | 0.472 |
| Jogador 1 | 4-4 | 2 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 29% | 9 → 11 | 3 | 8 → 8 | -0.026 | 0.000 |
| Jogador 1 | 4-5 | 7 | 0.000 | 8.000 | 0 → 0 | 0 → 0 | 29% → 29% | 11 → 12 | 4 | 8 → 8 | -0.086 | 0.000 |
| Jogador 1 | 4-6 | 8 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 29% → 29% | 12 → 18 | 0 | 8 → 8 | 0.073 | -0.333 |
| Jogador 1 | 4-7 | 5 | 2.000 | 6.000 | 0 → 0 | 0 → 0 | 29% → 29% | 18 → 20 | 4 | 8 → 8 | -0.029 | 0.000 |
| Jogador 1 | 5-1 | 5 | 0.000 | 10.000 | 0 → 0 | 0 → 0 | 29% → 29% | 20 → 22 | 5 | 8 → 8 | -0.089 | 0.607 |
| Jogador 1 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 29% → 29% | 22 → 27 | 2 | 8 → 8 | 0.000 | -1.375 |
| Jogador 1 | 5-3 | 10 | -2.000 | 18.000 | 0 → 0 | 0 → 0 | 29% → 29% | 27 → 11 | 22 | 8 → 8 | -0.011 | -0.275 |
| Jogador 1 | 5-4 | 6 | 0.000 | 22.000 | 0 → 0 | 0 → 1 | 29% → 29% | 11 → 6 | 11 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 5-5 | 4 | -42.000 | -64.000 | 0 → 0 | 1 → 0 | 29% → 0% | 6 → 0 | 6 | 8 → 8 | 0.064 | -0.688 |
| Jogador 1 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 8 → 8 | 0.000 | 0.000 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 3, COMPOSITION_COMPATIBILITY: 15, IMMEDIATE_UPGRADE: 1, PAIR_POTENTIAL: 7; mudanças de composição: 0; posicionamento melhorou em 28 ações e piorou em 21.
- Jogador 1 — estado final: ouro 0, nível 8, vida 0.0, colocação 4.
| Jogador 2 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.067 | 0.000 |
| Jogador 2 | 1-2 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | -0.029 | 0.000 |
| Jogador 2 | 1-3 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 7% → 7% | 3 → 6 | 0 | 3 → 3 | 0.060 | 0.000 |
| Jogador 2 | 1-4 | 9 | 6.000 | 0.000 | 0 → 1 | 1 → 0 | 7% → 11% | 6 → 6 | 4 | 3 → 4 | -0.109 | 0.000 |
| Jogador 2 | 2-1 | 7 | 6.000 | 0.000 | 1 → 1 | 0 → 0 | 11% → 14% | 6 → 7 | 5 | 4 → 4 | 0.021 | 0.359 |
| Jogador 2 | 2-2 | 4 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 14% → 14% | 7 → 6 | 6 | 4 → 4 | 0.000 | -0.632 |
| Jogador 2 | 2-3 | 10 | 4.000 | 0.000 | 1 → 1 | 0 → 0 | 14% → 18% | 6 → 6 | 8 | 4 → 5 | 0.022 | 0.264 |
| Jogador 2 | 2-4 | 7 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 18% → 18% | 6 → 7 | 7 | 5 → 5 | -0.002 | 0.000 |
| Jogador 2 | 2-5 | 4 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 18% → 18% | 7 → 8 | 6 | 5 → 5 | 0.000 | 0.701 |
| Jogador 2 | 2-6 | 7 | 2.000 | 0.000 | 1 → 1 | 0 → 0 | 18% → 21% | 8 → 10 | 7 | 5 → 6 | 0.004 | 0.377 |
| Jogador 2 | 2-7 | 10 | 0.000 | 0.000 | 1 → 1 | 0 → 1 | 21% → 21% | 10 → 17 | 7 | 6 → 6 | -0.004 | 0.000 |
| Jogador 2 | 3-1 | 10 | 0.000 | 4.000 | 1 → 1 | 1 → 1 | 21% → 21% | 17 → 21 | 4 | 6 → 6 | -0.017 | -0.283 |
| Jogador 2 | 3-2 | 10 | 4.000 | -4.000 | 1 → 1 | 1 → 1 | 21% → 21% | 21 → 29 | 3 | 6 → 6 | -0.001 | -0.283 |
| Jogador 2 | 3-3 | 7 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 21% → 21% | 29 → 37 | 3 | 6 → 6 | 0.022 | -0.396 |
| Jogador 2 | 3-4 | 9 | 0.000 | 8.000 | 1 → 2 | 1 → 1 | 21% → 18% | 37 → 39 | 7 | 6 → 6 | 0.043 | 0.000 |
| Jogador 2 | 3-5 | 9 | 0.000 | -8.000 | 2 → 2 | 1 → 0 | 18% → 18% | 39 → 53 | 0 | 6 → 6 | -0.039 | -0.322 |
| Jogador 2 | 3-6 | 2 | 6.000 | 0.000 | 2 → 2 | 0 → 0 | 18% → 21% | 53 → 62 | 3 | 6 → 6 | -0.057 | -1.388 |
| Jogador 2 | 3-7 | 10 | 0.000 | 10.000 | 2 → 2 | 0 → 0 | 21% → 21% | 62 → 56 | 17 | 6 → 6 | -0.007 | 0.000 |
| Jogador 2 | 4-1 | 10 | 0.000 | 6.000 | 2 → 2 | 0 → 0 | 21% → 21% | 56 → 48 | 19 | 6 → 6 | 0.000 | -0.298 |
| Jogador 2 | 4-2 | 10 | 0.000 | 28.000 | 2 → 2 | 0 → 3 | 21% → 21% | 48 → 34 | 22 | 6 → 6 | 0.000 | 0.281 |
| Jogador 2 | 4-3 | 8 | 0.000 | 2.000 | 2 → 2 | 3 → 3 | 21% → 21% | 34 → 28 | 13 | 6 → 6 | 0.000 | -0.367 |
| Jogador 2 | 4-4 | 2 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 21% → 21% | 28 → 33 | 2 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 4-5 | 9 | -32.000 | -46.000 | 2 → 0 | 3 → 0 | 21% → 0% | 33 → 17 | 16 | 6 → 6 | 0.047 | -0.318 |
| Jogador 2 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 17 → 17 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 17 → 17 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 5-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 17 → 17 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 17 → 17 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 17 → 17 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 17 → 17 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 17 → 17 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 17 → 17 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 17 → 17 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 17 → 17 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 17 → 17 | 0 | 6 → 6 | 0.000 | 0.000 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 7, COMPOSITION_COMPATIBILITY: 15, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 7; mudanças de composição: 0; posicionamento melhorou em 28 ações e piorou em 22.
- Jogador 2 — estado final: ouro 17, nível 6, vida 0.0, colocação 7.
| Jogador 3 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.067 | 0.000 |
| Jogador 3 | 1-2 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | -0.008 | 0.000 |
| Jogador 3 | 1-3 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 7% → 7% | 3 → 6 | 0 | 3 → 3 | 0.000 | 0.000 |
| Jogador 3 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 7% → 7% | 6 → 10 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 3 | 2-1 | 6 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 7% → 11% | 10 → 5 | 10 | 4 → 5 | 0.030 | -0.395 |
| Jogador 3 | 2-2 | 6 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 14% | 5 → 8 | 3 | 5 → 5 | 0.018 | -0.405 |
| Jogador 3 | 2-3 | 6 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 8 → 7 | 7 | 5 → 5 | -0.009 | 0.467 |
| Jogador 3 | 2-4 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 7 → 8 | 4 | 5 → 5 | 0.000 | 0.000 |
| Jogador 3 | 2-5 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 8 → 7 | 8 | 5 → 6 | 0.000 | 0.616 |
| Jogador 3 | 2-6 | 6 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 7 → 8 | 6 | 6 → 6 | 0.013 | -0.413 |
| Jogador 3 | 2-7 | 5 | 6.000 | 0.000 | 0 → 0 | 1 → 2 | 18% → 21% | 8 → 6 | 7 | 6 → 6 | -0.021 | 0.000 |
| Jogador 3 | 3-1 | 3 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 6 → 8 | 4 | 6 → 6 | 0.000 | -0.925 |
| Jogador 3 | 3-2 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 8 → 14 | 0 | 6 → 6 | 0.000 | -0.646 |
| Jogador 3 | 3-3 | 9 | 2.000 | 6.000 | 0 → 0 | 2 → 1 | 21% → 21% | 14 → 17 | 7 | 6 → 6 | -0.082 | 0.343 |
| Jogador 3 | 3-4 | 10 | 10.000 | -4.000 | 0 → 0 | 1 → 1 | 21% → 25% | 17 → 7 | 15 | 6 → 7 | -0.028 | 0.000 |
| Jogador 3 | 3-5 | 9 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 25% → 25% | 7 → 8 | 7 | 7 → 7 | 0.042 | 0.317 |
| Jogador 3 | 3-6 | 2 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 25% → 25% | 8 → 10 | 3 | 7 → 7 | 0.000 | -1.338 |
| Jogador 3 | 3-7 | 10 | 0.000 | 6.000 | 0 → 0 | 1 → 0 | 25% → 25% | 10 → 5 | 12 | 7 → 7 | -0.020 | 0.000 |
| Jogador 3 | 4-1 | 10 | 0.000 | -2.000 | 0 → 0 | 0 → 2 | 25% → 25% | 5 → 6 | 16 | 7 → 7 | 0.006 | 0.314 |
| Jogador 3 | 4-2 | 10 | 0.000 | 2.000 | 0 → 0 | 2 → 3 | 25% → 25% | 6 → 6 | 7 | 7 → 7 | 0.004 | -0.268 |
| Jogador 3 | 4-3 | 5 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 25% → 25% | 6 → 6 | 6 | 7 → 7 | 0.007 | -0.525 |
| Jogador 3 | 4-4 | 2 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 25% → 25% | 6 → 9 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 4-5 | 5 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 25% → 25% | 9 → 7 | 8 | 7 → 7 | -0.012 | -0.525 |
| Jogador 3 | 4-6 | 4 | 0.000 | 14.000 | 0 → 0 | 3 → 3 | 25% → 25% | 7 → 6 | 7 | 7 → 7 | 0.000 | 0.721 |
| Jogador 3 | 4-7 | 5 | 2.000 | -2.000 | 0 → 0 | 3 → 2 | 25% → 25% | 6 → 6 | 5 | 7 → 7 | 0.085 | 0.000 |
| Jogador 3 | 5-1 | 5 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 25% → 25% | 6 → 6 | 5 | 7 → 7 | 0.000 | -0.570 |
| Jogador 3 | 5-2 | 2 | -40.000 | -54.000 | 0 → 0 | 2 → 0 | 25% → 0% | 6 → 3 | 3 | 7 → 7 | -0.080 | -1.450 |
| Jogador 3 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 7 → 7 | 0.000 | 0.000 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 8, COMPOSITION_COMPATIBILITY: 8, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 8; mudanças de composição: 1; posicionamento melhorou em 20 ações e piorou em 22.
- Jogador 3 — estado final: ouro 3, nível 7, vida 0.0, colocação 6.
| Jogador 4 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 4 | 1-2 | 4 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | 0.095 | 0.000 |
| Jogador 4 | 1-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 7% | 3 → 6 | 0 | 3 → 3 | 0.000 | 0.000 |
| Jogador 4 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 7% | 6 → 10 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 4 | 2-1 | 7 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 7% → 11% | 10 → 6 | 9 | 4 → 5 | 0.010 | -0.361 |
| Jogador 4 | 2-2 | 7 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 14% | 6 → 9 | 3 | 5 → 5 | 0.014 | -0.323 |
| Jogador 4 | 2-3 | 5 | 6.000 | 0.000 | 0 → 0 | 1 → 2 | 14% → 18% | 9 → 12 | 3 | 5 → 5 | -0.009 | 0.527 |
| Jogador 4 | 2-4 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 12 → 18 | 0 | 5 → 5 | 0.000 | 0.000 |
| Jogador 4 | 2-5 | 6 | 6.000 | 0.000 | 0 → 1 | 2 → 1 | 18% → 18% | 18 → 13 | 10 | 5 → 5 | 0.014 | -0.431 |
| Jogador 4 | 2-6 | 6 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 18% → 18% | 13 → 20 | 0 | 5 → 5 | 0.019 | -0.423 |
| Jogador 4 | 2-7 | 10 | 6.000 | 0.000 | 1 → 1 | 1 → 1 | 18% → 21% | 20 → 7 | 19 | 5 → 6 | 0.008 | 0.000 |
| Jogador 4 | 3-1 | 7 | 4.000 | 0.000 | 1 → 1 | 1 → 0 | 21% → 21% | 7 → 7 | 7 | 6 → 6 | 0.006 | 0.421 |
| Jogador 4 | 3-2 | 10 | 0.000 | 6.000 | 1 → 1 | 0 → 1 | 21% → 21% | 7 → 11 | 3 | 6 → 6 | 0.000 | 0.308 |
| Jogador 4 | 3-3 | 8 | 0.000 | -6.000 | 1 → 1 | 1 → 1 | 21% → 21% | 11 → 9 | 12 | 6 → 6 | 0.000 | 0.369 |
| Jogador 4 | 3-4 | 4 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 21% → 21% | 9 → 15 | 0 | 6 → 7 | -0.003 | 0.000 |
| Jogador 4 | 3-5 | 6 | 6.000 | 0.000 | 1 → 1 | 1 → 2 | 21% → 25% | 15 → 18 | 3 | 7 → 7 | -0.005 | -0.452 |
| Jogador 4 | 3-6 | 2 | 0.000 | 0.000 | 1 → 2 | 2 → 1 | 25% → 21% | 18 → 22 | 3 | 7 → 7 | -0.110 | -1.382 |
| Jogador 4 | 3-7 | 10 | 6.000 | 0.000 | 2 → 3 | 1 → 0 | 21% → 21% | 22 → 23 | 6 | 7 → 7 | -0.049 | 0.000 |
| Jogador 4 | 4-1 | 8 | 6.000 | 0.000 | 3 → 3 | 0 → 0 | 21% → 25% | 23 → 28 | 3 | 7 → 7 | 0.002 | 0.370 |
| Jogador 4 | 4-2 | 10 | 0.000 | 0.000 | 3 → 3 | 0 → 0 | 25% → 25% | 28 → 37 | 4 | 7 → 7 | 0.088 | 0.285 |
| Jogador 4 | 4-3 | 5 | 0.000 | 8.000 | 3 → 3 | 0 → 0 | 25% → 25% | 37 → 41 | 4 | 7 → 7 | -0.172 | -0.533 |
| Jogador 4 | 4-4 | 2 | 0.000 | 6.000 | 3 → 3 | 0 → 1 | 25% → 25% | 41 → 46 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 4-5 | 9 | 2.000 | 6.000 | 3 → 3 | 1 → 1 | 25% → 25% | 46 → 49 | 7 | 7 → 7 | 0.033 | 0.337 |
| Jogador 4 | 4-6 | 10 | 0.000 | 0.000 | 3 → 3 | 1 → 1 | 25% → 25% | 49 → 41 | 16 | 7 → 7 | 0.015 | -0.271 |
| Jogador 4 | 4-7 | 10 | 0.000 | 0.000 | 3 → 3 | 1 → 1 | 25% → 25% | 41 → 36 | 12 | 7 → 7 | -0.012 | 0.000 |
| Jogador 4 | 5-1 | 9 | 0.000 | 0.000 | 3 → 3 | 1 → 1 | 25% → 25% | 36 → 36 | 8 | 7 → 7 | 0.005 | -0.304 |
| Jogador 4 | 5-2 | 2 | -54.000 | -20.000 | 3 → 0 | 1 → 0 | 25% → 0% | 36 → 33 | 3 | 7 → 7 | -0.122 | -1.425 |
| Jogador 4 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 33 → 33 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 33 → 33 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 33 → 33 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 33 → 33 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 33 → 33 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 33 → 33 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 33 → 33 | 0 | 7 → 7 | 0.000 | 0.000 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 2, COMPOSITION_COMPATIBILITY: 8, IMMEDIATE_UPGRADE: 4, PAIR_POTENTIAL: 6; mudanças de composição: 0; posicionamento melhorou em 29 ações e piorou em 23.
- Jogador 4 — estado final: ouro 33, nível 7, vida 0.0, colocação 5.
| Jogador 5 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 5 | 1-2 | 4 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.116 | 0.000 |
| Jogador 5 | 1-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 7% | 2 → 5 | 0 | 3 → 3 | 0.000 | 0.000 |
| Jogador 5 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 7% | 5 → 9 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 5 | 2-1 | 7 | 10.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 14% | 9 → 5 | 9 | 4 → 4 | -0.120 | -0.339 |
| Jogador 5 | 2-2 | 7 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 5 → 7 | 8 | 4 → 5 | 0.031 | 0.359 |
| Jogador 5 | 2-3 | 10 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 7 → 12 | 4 | 5 → 5 | -0.019 | -0.264 |
| Jogador 5 | 2-4 | 7 | 4.000 | 6.000 | 0 → 0 | 0 → 1 | 14% → 18% | 12 → 12 | 7 | 5 → 5 | -0.009 | 0.000 |
| Jogador 5 | 2-5 | 6 | 0.000 | -6.000 | 0 → 0 | 1 → 1 | 18% → 18% | 12 → 22 | 3 | 5 → 5 | 0.044 | -0.439 |
| Jogador 5 | 2-6 | 7 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 22 → 30 | 3 | 5 → 5 | 0.071 | -0.391 |
| Jogador 5 | 2-7 | 10 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 30 → 39 | 4 | 5 → 5 | -0.061 | 0.000 |
| Jogador 5 | 3-1 | 10 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 39 → 48 | 5 | 5 → 5 | -0.003 | -0.283 |
| Jogador 5 | 3-2 | 10 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 48 → 59 | 5 | 5 → 5 | 0.003 | -0.291 |
| Jogador 5 | 3-3 | 9 | 0.000 | 32.000 | 0 → 0 | 1 → 2 | 18% → 18% | 59 → 53 | 18 | 5 → 5 | 0.000 | -0.324 |
| Jogador 5 | 3-4 | 10 | 0.000 | 12.000 | 0 → 0 | 2 → 0 | 18% → 14% | 53 → 46 | 18 | 5 → 6 | 0.023 | 0.000 |
| Jogador 5 | 3-5 | 7 | 6.000 | 0.000 | 0 → 0 | 0 → 1 | 14% → 18% | 46 → 48 | 9 | 6 → 6 | -0.011 | -0.421 |
| Jogador 5 | 3-6 | 2 | 8.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 21% | 48 → 56 | 4 | 6 → 6 | -0.043 | -1.363 |
| Jogador 5 | 3-7 | 10 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 56 → 49 | 18 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-1 | 10 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 49 → 42 | 18 | 6 → 6 | 0.000 | -0.285 |
| Jogador 5 | 4-2 | 10 | -34.000 | -48.000 | 0 → 0 | 1 → 0 | 21% → 0% | 42 → 24 | 18 | 6 → 6 | 0.044 | -0.263 |
| Jogador 5 | 4-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 24 → 24 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 24 → 24 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 24 → 24 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 24 → 24 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 24 → 24 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 24 → 24 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 24 → 24 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 24 → 24 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 24 → 24 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 24 → 24 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 24 → 24 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 24 → 24 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 24 → 24 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 24 → 24 | 0 | 6 → 6 | 0.000 | 0.000 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 9, COMPOSITION_COMPATIBILITY: 18, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 7; mudanças de composição: 0; posicionamento melhorou em 12 ações e piorou em 16.
- Jogador 5 — estado final: ouro 24, nível 6, vida 0.0, colocação 8.
| Jogador 6 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.067 | 0.000 |
| Jogador 6 | 1-2 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | -0.183 | 0.000 |
| Jogador 6 | 1-3 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.067 | 0.000 |
| Jogador 6 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 7 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 6 | 2-1 | 7 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 7 → 10 | 4 | 4 → 4 | 0.029 | 0.359 |
| Jogador 6 | 2-2 | 7 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 10 → 12 | 9 | 4 → 4 | 0.000 | 0.340 |
| Jogador 6 | 2-3 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 18% | 12 → 11 | 8 | 4 → 5 | -0.008 | -0.270 |
| Jogador 6 | 2-4 | 7 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 11 → 7 | 11 | 5 → 5 | -0.000 | 0.000 |
| Jogador 6 | 2-5 | 3 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 7 → 9 | 4 | 5 → 6 | 0.000 | -0.827 |
| Jogador 6 | 2-6 | 7 | 6.000 | 6.000 | 0 → 0 | 0 → 1 | 18% → 21% | 9 → 9 | 6 | 6 → 6 | 0.158 | 0.370 |
| Jogador 6 | 2-7 | 7 | 0.000 | -6.000 | 0 → 0 | 1 → 1 | 21% → 21% | 9 → 5 | 12 | 6 → 6 | -0.025 | 0.000 |
| Jogador 6 | 3-1 | 7 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 5 → 10 | 4 | 6 → 6 | -0.096 | 0.429 |
| Jogador 6 | 3-2 | 7 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 10 → 7 | 8 | 6 → 6 | 0.054 | -0.376 |
| Jogador 6 | 3-3 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 7 → 9 | 7 | 6 → 6 | 0.000 | -0.543 |
| Jogador 6 | 3-4 | 6 | 8.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 25% | 9 → 7 | 8 | 6 → 7 | -0.024 | 0.000 |
| Jogador 6 | 3-5 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 7 → 13 | 0 | 7 → 7 | 0.000 | 1.556 |
| Jogador 6 | 3-6 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 13 → 17 | 4 | 7 → 7 | 0.000 | 1.425 |
| Jogador 6 | 3-7 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 17 → 24 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 4-1 | 10 | 6.000 | 0.000 | 0 → 1 | 1 → 1 | 25% → 25% | 24 → 18 | 14 | 7 → 7 | 0.066 | 0.280 |
| Jogador 6 | 4-2 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 18 → 24 | 0 | 7 → 7 | 0.000 | -1.338 |
| Jogador 6 | 4-3 | 8 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 24 → 6 | 24 | 7 → 7 | 0.000 | 0.350 |
| Jogador 6 | 4-4 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 6 → 7 | 4 | 7 → 8 | 0.000 | 0.000 |
| Jogador 6 | 4-5 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 7 → 14 | 0 | 8 → 8 | 0.000 | 1.400 |
| Jogador 6 | 4-6 | 7 | 8.000 | 0.000 | 1 → 1 | 1 → 2 | 25% → 29% | 14 → 9 | 12 | 8 → 8 | -0.004 | 0.405 |
| Jogador 6 | 4-7 | 3 | 0.000 | 8.000 | 1 → 1 | 2 → 2 | 29% → 29% | 9 → 11 | 4 | 8 → 8 | 0.000 | 0.000 |
| Jogador 6 | 5-1 | 9 | 8.000 | 2.000 | 1 → 2 | 2 → 1 | 29% → 29% | 11 → 7 | 9 | 8 → 8 | -0.054 | -0.311 |
| Jogador 6 | 5-2 | 2 | 0.000 | 0.000 | 2 → 2 | 1 → 1 | 29% → 29% | 7 → 13 | 0 | 8 → 8 | 0.000 | 1.453 |
| Jogador 6 | 5-3 | 2 | 0.000 | 0.000 | 2 → 2 | 1 → 1 | 29% → 29% | 13 → 21 | 0 | 8 → 8 | 0.000 | 1.461 |
| Jogador 6 | 5-4 | 9 | 0.000 | 6.000 | 2 → 2 | 1 → 1 | 29% → 29% | 21 → 8 | 19 | 8 → 8 | -0.052 | 0.000 |
| Jogador 6 | 5-5 | 2 | 0.000 | 0.000 | 2 → 2 | 1 → 1 | 29% → 29% | 8 → 15 | 0 | 8 → 8 | 0.000 | 1.453 |
| Jogador 6 | 5-6 | 6 | 0.000 | 6.000 | 2 → 2 | 1 → 2 | 29% → 29% | 15 → 5 | 15 | 8 → 8 | 0.000 | -0.475 |
| Jogador 6 | 5-7 | 4 | 0.000 | 6.000 | 2 → 2 | 2 → 3 | 29% → 29% | 5 → 5 | 5 | 8 → 8 | 0.000 | 0.000 |
| Jogador 6 | 6-1 | 6 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 29% → 29% | 5 → 7 | 4 | 8 → 8 | 0.000 | 0.489 |
| Jogador 6 | 6-2 | 4 | -64.000 | -28.000 | 2 → 0 | 3 → 0 | 29% → 0% | 7 → 1 | 6 | 8 → 8 | 0.152 | -0.725 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 4, COMPOSITION_COMPATIBILITY: 10, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 9; mudanças de composição: 0; posicionamento melhorou em 20 ações e piorou em 20.
- Jogador 6 — estado final: ouro 1, nível 8, vida 0.0, colocação 2.
| Jogador 7 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.067 | 0.000 |
| Jogador 7 | 1-2 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | -0.029 | 0.000 |
| Jogador 7 | 1-3 | 9 | 6.000 | 0.000 | 0 → 0 | 1 → 0 | 7% → 11% | 3 → 3 | 4 | 3 → 3 | 0.031 | 0.000 |
| Jogador 7 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 7 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 7 | 2-1 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 11% → 14% | 7 → 11 | 2 | 4 → 4 | -0.003 | 0.527 |
| Jogador 7 | 2-2 | 7 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 11 → 7 | 11 | 4 → 5 | -0.009 | 0.370 |
| Jogador 7 | 2-3 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 7 → 10 | 4 | 5 → 5 | 0.049 | 0.647 |
| Jogador 7 | 2-4 | 7 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 10 → 6 | 12 | 5 → 5 | 0.000 | 0.000 |
| Jogador 7 | 2-5 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 6 → 9 | 4 | 5 → 6 | 0.000 | 0.918 |
| Jogador 7 | 2-6 | 7 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 21% | 9 → 10 | 7 | 6 → 6 | -0.091 | 0.416 |
| Jogador 7 | 2-7 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 10 → 9 | 8 | 6 → 6 | 0.007 | 0.000 |
| Jogador 7 | 3-1 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 9 → 19 | 0 | 6 → 6 | 0.000 | 1.467 |
| Jogador 7 | 3-2 | 9 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 19 → 12 | 16 | 6 → 7 | 0.068 | 0.312 |
| Jogador 7 | 3-3 | 9 | 6.000 | 0.000 | 0 → 1 | 1 → 0 | 21% → 21% | 12 → 12 | 5 | 7 → 7 | -0.079 | -0.308 |
| Jogador 7 | 3-4 | 9 | 4.000 | 14.000 | 1 → 1 | 0 → 1 | 21% → 25% | 12 → 8 | 9 | 7 → 7 | -0.000 | 0.000 |
| Jogador 7 | 3-5 | 7 | 0.000 | -8.000 | 1 → 1 | 1 → 1 | 25% → 25% | 8 → 19 | 0 | 7 → 7 | 0.090 | -0.382 |
| Jogador 7 | 3-6 | 2 | 0.000 | 8.000 | 1 → 1 | 1 → 1 | 25% → 25% | 19 → 22 | 4 | 7 → 7 | 0.000 | 1.475 |
| Jogador 7 | 3-7 | 8 | 0.000 | 12.000 | 1 → 1 | 1 → 3 | 25% → 25% | 22 → 22 | 6 | 7 → 7 | 0.001 | 0.000 |
| Jogador 7 | 4-1 | 10 | 6.000 | 6.000 | 1 → 2 | 3 → 3 | 25% → 25% | 22 → 10 | 17 | 7 → 7 | -0.065 | -0.280 |
| Jogador 7 | 4-2 | 10 | 2.000 | 6.000 | 2 → 2 | 3 → 3 | 25% → 25% | 10 → 6 | 10 | 7 → 7 | -0.009 | 0.285 |
| Jogador 7 | 4-3 | 8 | 0.000 | 2.000 | 2 → 2 | 3 → 2 | 25% → 25% | 6 → 8 | 9 | 7 → 7 | 0.059 | 0.386 |
| Jogador 7 | 4-4 | 2 | 0.000 | 6.000 | 2 → 2 | 2 → 2 | 25% → 25% | 8 → 11 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 4-5 | 9 | 0.000 | -2.000 | 2 → 2 | 2 → 2 | 25% → 25% | 11 → 9 | 13 | 7 → 7 | 0.000 | -0.309 |
| Jogador 7 | 4-6 | 9 | 0.000 | 0.000 | 2 → 2 | 2 → 1 | 25% → 25% | 9 → 6 | 9 | 7 → 7 | -0.056 | -0.311 |
| Jogador 7 | 4-7 | 4 | 0.000 | 6.000 | 2 → 2 | 1 → 2 | 25% → 25% | 6 → 7 | 5 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 5-1 | 9 | -2.000 | 8.000 | 2 → 2 | 2 → 1 | 25% → 25% | 7 → 7 | 9 | 7 → 7 | -0.009 | 0.321 |
| Jogador 7 | 5-2 | 2 | 0.000 | 4.000 | 2 → 2 | 1 → 1 | 25% → 25% | 7 → 12 | 2 | 7 → 7 | 0.000 | 1.536 |
| Jogador 7 | 5-3 | 4 | 0.000 | 6.000 | 2 → 2 | 1 → 2 | 25% → 25% | 12 → 12 | 5 | 7 → 7 | 0.000 | -0.712 |
| Jogador 7 | 5-4 | 2 | 0.000 | 0.000 | 2 → 2 | 2 → 2 | 25% → 25% | 12 → 18 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 5-5 | 2 | 0.000 | 0.000 | 2 → 2 | 2 → 2 | 25% → 25% | 18 → 25 | 0 | 7 → 7 | 0.000 | -1.375 |
| Jogador 7 | 5-6 | 2 | 0.000 | 0.000 | 2 → 2 | 2 → 2 | 25% → 25% | 25 → 33 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 5-7 | 2 | 0.000 | 0.000 | 2 → 2 | 2 → 2 | 25% → 25% | 33 → 42 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 6-1 | 4 | -46.000 | -68.000 | 2 → 0 | 2 → 0 | 25% → 0% | 42 → 42 | 0 | 7 → 7 | 0.081 | -0.688 |
| Jogador 7 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 42 → 42 | 0 | 7 → 7 | 0.000 | 0.000 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 6, COMPOSITION_COMPATIBILITY: 13, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 11; mudanças de composição: 0; posicionamento melhorou em 24 ações e piorou em 22.
- Jogador 7 — estado final: ouro 42, nível 7, vida 0.0, colocação 3.
| Jogador 8 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 8 | 1-2 | 6 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 2 | 3 → 3 | 0.063 | 0.000 |
| Jogador 8 | 1-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 7% | 3 → 6 | 0 | 3 → 3 | 0.000 | 0.000 |
| Jogador 8 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 7% | 6 → 10 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 8 | 2-1 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 7% → 11% | 10 → 14 | 1 | 4 → 4 | -0.006 | -0.496 |
| Jogador 8 | 2-2 | 6 | 4.000 | 0.000 | 0 → 0 | 1 → 0 | 11% → 11% | 14 → 19 | 3 | 4 → 4 | 0.016 | -0.395 |
| Jogador 8 | 2-3 | 10 | 8.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 18% | 19 → 13 | 13 | 4 → 5 | -0.080 | -0.248 |
| Jogador 8 | 2-4 | 7 | 4.000 | 6.000 | 0 → 0 | 0 → 0 | 18% → 18% | 13 → 6 | 14 | 5 → 5 | 0.001 | 0.000 |
| Jogador 8 | 2-5 | 5 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 6 → 12 | 0 | 5 → 5 | 0.004 | -0.464 |
| Jogador 8 | 2-6 | 5 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 12 → 20 | 0 | 5 → 5 | 0.002 | -0.486 |
| Jogador 8 | 2-7 | 10 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 20 → 24 | 10 | 5 → 6 | -0.010 | 0.000 |
| Jogador 8 | 3-1 | 10 | 8.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 21% | 24 → 23 | 8 | 6 → 6 | 0.029 | 0.300 |
| Jogador 8 | 3-2 | 10 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 23 → 18 | 16 | 6 → 6 | 0.029 | 0.300 |
| Jogador 8 | 3-3 | 6 | 6.000 | -6.000 | 0 → 0 | 0 → 0 | 21% → 25% | 18 → 13 | 12 | 6 → 7 | -0.009 | 0.492 |
| Jogador 8 | 3-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 13 → 20 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 3-5 | 9 | 4.000 | 2.000 | 0 → 0 | 0 → 1 | 25% → 25% | 20 → 8 | 19 | 7 → 7 | 0.061 | 0.340 |
| Jogador 8 | 3-6 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 8 → 12 | 4 | 7 → 7 | 0.000 | 1.467 |
| Jogador 8 | 3-7 | 6 | 0.000 | -2.000 | 0 → 0 | 1 → 1 | 25% → 25% | 12 → 8 | 12 | 7 → 7 | 0.010 | 0.000 |
| Jogador 8 | 4-1 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 8 → 9 | 8 | 7 → 7 | 0.000 | 0.602 |
| Jogador 8 | 4-2 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 9 → 14 | 4 | 7 → 8 | 0.000 | 0.971 |
| Jogador 8 | 4-3 | 6 | 8.000 | 8.000 | 0 → 0 | 1 → 1 | 25% → 29% | 14 → 10 | 12 | 8 → 8 | 0.040 | 0.000 |
| Jogador 8 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 10 → 14 | 4 | 8 → 8 | 0.000 | 0.000 |
| Jogador 8 | 4-5 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 14 → 11 | 12 | 8 → 8 | 0.000 | 0.587 |
| Jogador 8 | 4-6 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 11 → 12 | 8 | 8 → 8 | -0.176 | 0.592 |
| Jogador 8 | 4-7 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 12 → 8 | 12 | 8 → 8 | 0.000 | 0.000 |
| Jogador 8 | 5-1 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 8 → 9 | 8 | 8 → 8 | 0.000 | 0.597 |
| Jogador 8 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 9 → 14 | 4 | 8 → 9 | 0.000 | 1.518 |
| Jogador 8 | 5-3 | 3 | 8.000 | -8.000 | 0 → 0 | 1 → 1 | 29% → 32% | 14 → 24 | 0 | 9 → 9 | -0.004 | 1.012 |
| Jogador 8 | 5-4 | 8 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 32% → 32% | 24 → 8 | 24 | 9 → 9 | 0.000 | 0.000 |
| Jogador 8 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 32% → 32% | 8 → 17 | 0 | 9 → 9 | 0.000 | 1.468 |
| Jogador 8 | 5-6 | 9 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 32% → 32% | 17 → 10 | 16 | 9 → 9 | 0.105 | 0.339 |
| Jogador 8 | 5-7 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 32% → 32% | 10 → 10 | 8 | 9 → 9 | 0.000 | 0.000 |
| Jogador 8 | 6-1 | 6 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 32% → 32% | 10 → 10 | 8 | 9 → 10 | 0.000 | 0.000 |
| Jogador 8 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 32% → 32% | 10 → 11 | 0 | 10 → 10 | 0.000 | 1.557 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 7, COMPOSITION_COMPATIBILITY: 6, PAIR_POTENTIAL: 3; mudanças de composição: 0; posicionamento melhorou em 18 ações e piorou em 20.
- Jogador 8 — estado final: ouro 11, nível 10, vida 72.0, colocação 1.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Revertidas ≤1 ação | ≤2 ações | ≤4 ações | Ouro perdido | Upgrades | Vendas core/par | Valor médio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 26 | 8 | 0 | 0 | 0 | 0 | 1 | 6 | 2.7967 |
| Jogador 2 | 31 | 13 | 3 | 3 | 4 | 0 | 2 | 5 | 5.2428 |
| Jogador 3 | 29 | 8 | 0 | 2 | 2 | 0 | 5 | 3 | 3.8912 |
| Jogador 4 | 20 | 3 | 0 | 0 | 1 | 0 | 4 | 1 | 3.6005 |
| Jogador 5 | 36 | 18 | 11 | 12 | 13 | 0 | 2 | 6 | 3.1086 |
| Jogador 6 | 25 | 9 | 0 | 0 | 1 | 0 | 2 | 4 | 4.8392 |
| Jogador 7 | 35 | 10 | 0 | 0 | 0 | 0 | 5 | 4 | 5.1486 |
| Jogador 8 | 16 | 8 | 1 | 2 | 2 | 0 | 0 | 4 | 2.5133 |

As classificações detalhadas e cada sequência correlacionada ficam em audit_report.json.
Uma venda sem compra correspondente na janela é UNKNOWN; sequências ambíguas não são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| HIGH | Jogador 1 | 1-2 | 14 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 1 | 1-4 | 31 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 1 | 1-4 | 33 | SOLD_CORE_UNIT | Venda de 'DA_18_Ornn' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 1 | 2-1 | 39 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 1 | 4-2 | 169 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sejuani' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 1 | 4-3 | 174 | SOLD_CORE_UNIT | Venda de 'DA_18_Lux_Fae' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 1 | 5-6 | 261 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Nidalee18_AP' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 1 | 5-6 | 261 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Lux18_Blossom' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 1 | 5-6 | 261 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Lux_Primal' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 2 | 2-4 | 66 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 2 | 2-4 | 66 | PURCHASE_REVERSED | Compra de DA_KogMaw18_AD desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 2 | 2-6 | 77 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 2 | 2-6 | 79 | PURCHASE_REVERSED | Compra de DA_18_Akali_AD desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 2 | 2-7 | 86 | SOLD_CORE_UNIT | Venda de 'DA_Nidalee18_AP' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 2 | 2-7 | 86 | PURCHASE_REVERSED | Compra de DA_Nidalee18_AP desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 2 | 3-1 | 95 | SOLD_CORE_UNIT | Venda de 'DA_18_Yunara' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 2 | 3-3 | 113 | PURCHASE_REVERSED | Compra de DA_18_Cassiopeia desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 2 | 3-5 | 137 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Veigar' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 2 | 4-6 | 200 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Tristana' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 2 | 4-6 | 200 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Yorick' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 2 | 4-6 | 200 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Azir' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 3 | 2-6 | 78 | PURCHASE_REVERSED | Compra de DA_18_Yunara desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 3 | 3-3 | 119 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 3 | 3-5 | 133 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_RekSai' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 3 | 3-7 | 147 | PURCHASE_REVERSED | Compra de DA_18_Kayle desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 3 | 4-1 | 153 | SOLD_CORE_UNIT | Venda de 'DA_Vi18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 3 | 5-3 | 231 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_KogMaw18_AD' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 3 | 5-3 | 231 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Tristana' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 3 | 5-3 | 231 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Rammus' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 4 | 3-1 | 96 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 4 | 4-2 | 167 | PURCHASE_REVERSED | Compra de DA_Nidalee18_AP desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 4 | 5-3 | 231 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Fiddlesticks18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 4 | 5-3 | 231 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Tristana' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 4 | 5-3 | 231 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_MasterYi_AD' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 5 | 2-2 | 46 | SOLD_CORE_UNIT | Venda de 'DA_18_MasterYi_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 5 | 2-2 | 46 | PURCHASE_REVERSED | Compra de DA_18_MasterYi_AD desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-2 | 49 | PURCHASE_REVERSED | Compra de DA_18_Rakan desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-3 | 53 | PURCHASE_REVERSED | Compra de DA_18_Sejuani desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-3 | 55 | PURCHASE_REVERSED | Compra de DA_Murkwolf18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-4 | 65 | PURCHASE_REVERSED | Compra de DA_18_Caitlyn desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 5 | 2-5 | 73 | SOLD_CORE_UNIT | Venda de 'DA_18_Rammus' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 5 | 2-5 | 73 | PURCHASE_REVERSED | Compra de DA_18_Rammus desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 5 | 2-6 | 76 | SOLD_CORE_UNIT | Venda de 'DA_18_Elise' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 5 | 2-6 | 79 | PURCHASE_REVERSED | Compra de DA_18_Rakan desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 5 | 2-7 | 83 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 5 | 2-7 | 85 | PURCHASE_REVERSED | Compra de DA_18_Yunara desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-7 | 88 | PURCHASE_REVERSED | Compra de DA_18_Rakan desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 3-1 | 93 | PURCHASE_REVERSED | Compra de DA_18_Yunara desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 3-1 | 95 | PURCHASE_REVERSED | Compra de DA_18_Warwick desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 3-1 | 97 | PURCHASE_REVERSED | Compra de DA_18_Veigar desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 5 | 3-2 | 104 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 5 | 3-2 | 107 | PURCHASE_REVERSED | Compra de DA_18_Warwick desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 5 | 3-2 | 108 | SOLD_CORE_UNIT | Venda de 'DA_18_Elise' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 5 | 4-3 | 179 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Warwick' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 5 | 4-3 | 179 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_LeBlanc' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 5 | 4-3 | 179 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Ahri' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 6 | 2-1 | 42 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 6 | 2-2 | 50 | PURCHASE_REVERSED | Compra de DA_18_Shen desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 6 | 2-3 | 53 | SOLD_CORE_UNIT | Venda de 'DA_18_Teemo' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 6 | 2-7 | 84 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 6 | 3-3 | 114 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 7 | 1-3 | 22 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 7 | 4-3 | 175 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 7 | 4-3 | 177 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Fiddlesticks18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 7 | 4-5 | 187 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Tristana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 7 | 6-2 | 286 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_KogMaw18_AD' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 7 | 6-2 | 286 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Scuttlecrab18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 7 | 6-2 | 286 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Hecarim' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 8 | 1-2 | 14 | SOLD_CORE_UNIT | Venda de 'DA_18_Leona' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 8 | 2-2 | 48 | SOLD_CORE_UNIT | Venda de 'DA_18_Leona' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 8 | 2-3 | 58 | PURCHASE_REVERSED | Compra de DA_18_Xayah desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 8 | 2-7 | 82 | SOLD_CORE_UNIT | Venda de 'DA_Krug18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 8 | 2-7 | 87 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 8 | 2-7 | 87 | PURCHASE_REVERSED | Compra de DA_18_Tristana desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- O JSON estruturado é a fonte primária para estado de decisão, máscaras, política e recompensas; .tft é analisado apenas para jogadores sem sidecar JSON.- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
