# Auditoria da partida TFT

- Arquivos lidos: **8**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **3794**
- Achados: **71**
- CRITICAL: 0 | HIGH: 31 | MEDIUM: 40 | LOW: 0

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 159 | 159 | 159 | 0 | 157 | 0 | 159 | 159 | 151 | 33/18 |
| Jogador 2 | 118 | 118 | 118 | 0 | 116 | 0 | 118 | 118 | 112 | 12/3 |
| Jogador 3 | 142 | 142 | 142 | 0 | 138 | 0 | 142 | 142 | 142 | 19/9 |
| Jogador 4 | 149 | 149 | 149 | 0 | 147 | 0 | 149 | 149 | 145 | 20/12 |
| Jogador 5 | 144 | 144 | 144 | 0 | 143 | 0 | 144 | 144 | 136 | 31/16 |
| Jogador 6 | 156 | 156 | 156 | 0 | 152 | 0 | 156 | 156 | 156 | 22/11 |
| Jogador 7 | 143 | 143 | 143 | 0 | 142 | 0 | 143 | 143 | 136 | 27/12 |
| Jogador 8 | 125 | 125 | 125 | 0 | 123 | 0 | 125 | 125 | 122 | 24/11 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 17 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Ornn | MOVE_BENCH, SELL, PASS | True | True | 0.24171799421310425 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3013512194156647 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4440630376338959 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 26 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.9705569744110107 | 0.0 | 0.0 | +679fe281-674a-438b-bdcf-57229a283d44 / -— |
| Jogador 1 | 1-2 | 27 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.020556926727295 | 0.0 | 0.0 | +— / -679fe281-674a-438b-bdcf-57229a283d44 |
| Jogador 1 | 1-2 | 28 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.1504369080066681 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 29 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.2868722975254059 | 0.0 | 0.0 | +cde2c30a-df2c-4275-86ef-e4a4a13a5be1 / -— |
| Jogador 1 | 1-2 | 30 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43348413705825806 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 31 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.09773150831460953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 32 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 49 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.27007853984832764 | 0.0 | 0.0 | +24247863-54d4-4674-86e9-9a45609a440e / -— |
| Jogador 1 | 1-3 | 50 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5175982713699341 | 0.0 | 0.0 | +— / -24247863-54d4-4674-86e9-9a45609a440e |
| Jogador 1 | 1-3 | 51 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 77 | BUY_XP | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.052000001072883606 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 78 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.9711475372314453 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 79 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0211474895477295 | 0.0 | 0.0 | +— / -c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 1-4 | 80 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.9622067213058472 | 0.0 | 0.0 | +6465b229-8025-4e7d-94de-1cd49fa76167 / -— |
| Jogador 1 | 1-4 | 81 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0122066736221313 | 0.0 | 0.0 | +— / -6465b229-8025-4e7d-94de-1cd49fa76167 |
| Jogador 1 | 1-4 | 82 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | -0.010358829982578754 | 0.0 | 0.0 | +50fd90d6-9c1c-467f-bb3c-e88ca8815ef7 / -— |
| Jogador 1 | 1-4 | 83 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1786923110485077 | 0.0 | 0.0 | +— / -50fd90d6-9c1c-467f-bb3c-e88ca8815ef7 |
| Jogador 1 | 1-4 | 84 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 85 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 86 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 104 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9611726403236389 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -— |
| Jogador 1 | 2-1 | 105 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07570988684892654 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 106 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 107 | PASS | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 127 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.35905271768569946 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 128 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15648013353347778 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 129 | SELL | STABILIZE | 100.0 | 4 | 7 | 0 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37360498309135437 | 0.0 | 0.0 | +— / -ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 2-2 | 130 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 131 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.07869397848844528 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 132 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 133 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 134 | PASS | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 147 | BUY | STABILIZE | 100.0 | 4 | 15 | 1 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.43394824862480164 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 1 | 2-3 | 148 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 13 | 1 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14975683391094208 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 149 | SELL | STABILIZE | 100.0 | 4 | 13 | 1 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03500000014901161 | 0.0 | 0.0 | +— / -cde2c30a-df2c-4275-86ef-e4a4a13a5be1 |
| Jogador 1 | 2-3 | 150 | BUY_XP | STABILIZE | 100.0 | 4 | 14 | 1 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03200000151991844 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 151 | BUY | STABILIZE | 100.0 | 5 | 10 | 1 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.20315146446228027 | 0.0 | 0.0 | +6951a681-f5b9-4c22-9182-46b4d2c3cbb3 / -— |
| Jogador 1 | 2-3 | 152 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29407626390457153 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 153 | BUY_XP | STABILIZE | 100.0 | 5 | 8 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 154 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 155 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Diana | MOVE_BOARD, PASS | True | True | 0.09666892141103745 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 156 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Diana | MOVE_BOARD, PASS | True | True | -0.1439472734928131 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 157 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Diana | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 170 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 7 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.14480186998844147 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 171 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 7 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 172 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 7 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10272206366062164 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 173 | PASS | STABILIZE | 100.0 | 5 | 7 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 190 | BUY | STABILIZE | 100.0 | 5 | 13 | 1 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9678398370742798 | 0.0 | 0.0 | +a72d427f-f2f7-46dd-97bf-d28999772db0 / -— |
| Jogador 1 | 2-5 | 191 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 11 | 1 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 192 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 11 | 1 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33829477429389954 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 193 | PASS | STABILIZE | 100.0 | 5 | 11 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 212 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 17 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3350262939929962 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 213 | BUY | STABILIZE | 94.0 | 5 | 17 | 1 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45154035091400146 | 0.0 | 0.0 | +ae570779-3ae8-49b3-acdb-607fc512fcea / -— |
| Jogador 1 | 2-6 | 214 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 14 | 1 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0017167552141472697 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 215 | SELL | STABILIZE | 94.0 | 5 | 14 | 1 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10599883645772934 | 0.0 | 0.0 | +— / -2718f555-b782-4fea-a68f-31395ad34232 |
| Jogador 1 | 2-6 | 216 | SELL | STABILIZE | 94.0 | 5 | 15 | 1 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5565354228019714 | 0.0 | 0.0 | +— / -ae570779-3ae8-49b3-acdb-607fc512fcea |
| Jogador 1 | 2-6 | 217 | BUY_XP | STABILIZE | 94.0 | 5 | 18 | 1 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03200000151991844 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 218 | BUY | STABILIZE | 94.0 | 6 | 14 | 1 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.008244642056524754 | 0.0 | 0.0 | +fa0e266f-ef5b-48c5-b9a3-511450e97169 / -— |
| Jogador 1 | 2-6 | 219 | BUY | STABILIZE | 94.0 | 6 | 11 | 1 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49562856554985046 | 0.0 | 0.0 | +53312511-4e10-4904-82c0-8a8e69c039cd / -— |
| Jogador 1 | 2-6 | 220 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 10 | 1 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5281538367271423 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 221 | BUY_XP | STABILIZE | 94.0 | 6 | 10 | 1 | 26.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 222 | PASS | STABILIZE | 94.0 | 6 | 6 | 0 | 26.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 233 | BUY_XP | STABILIZE | 88.0 | 6 | 12 | 1 | 26.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 234 | BUY_XP | STABILIZE | 88.0 | 6 | 8 | 0 | 26.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 235 | BUY_XP | STABILIZE | 88.0 | 6 | 4 | 0 | 26.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 236 | SELL | STABILIZE | 88.0 | 6 | 0 | 0 | 26.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10442455112934113 | 0.0 | 0.0 | +— / -53312511-4e10-4904-82c0-8a8e69c039cd |
| Jogador 1 | 2-7 | 237 | MOVE_BOARD | STABILIZE | 88.0 | 6 | 1 | 0 | 26.0 | —/DA_18_Diana | BUY, MOVE_BOARD, PASS | True | True | -0.26141127943992615 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 238 | PASS | STABILIZE | 88.0 | 6 | 1 | 0 | 26.0 | —/DA_18_Diana | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 252 | BUY | STABILIZE | 88.0 | 6 | 7 | 0 | 26.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.15014374256134033 | 0.0 | 0.0 | +a22733bf-aedc-4ee7-8fcb-2fdbd51df2b9 / -— |
| Jogador 1 | 3-1 | 253 | MOVE_BENCH | STABILIZE | 88.0 | 6 | 4 | 0 | 26.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42412450909614563 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 254 | BUY_XP | ECON | 88.0 | 6 | 4 | 0 | 26.0 | Defendente/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09799999743700027 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 255 | SELL | STABILIZE | 88.0 | 6 | 0 | 0 | 26.0 | Defendente/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3582598567008972 | 0.0 | 0.0 | +— / -3a43ff36-dccd-49a7-92d8-0b01e739ea89 |
| Jogador 1 | 3-1 | 256 | PASS | STABILIZE | 88.0 | 6 | 3 | 0 | 26.0 | Defendente/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 273 | MOVE_BOARD | STABILIZE | 77.0 | 6 | 9 | 0 | 26.0 | Defendente/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.059659093618392944 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 274 | MOVE_BOARD | STABILIZE | 77.0 | 6 | 9 | 0 | 26.0 | Defendente/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.1381131112575531 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 275 | MOVE_BOARD | STABILIZE | 77.0 | 6 | 9 | 0 | 26.0 | Defendente/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 276 | PASS | STABILIZE | 77.0 | 6 | 9 | 0 | 26.0 | Defendente/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 296 | MOVE_BOARD | STABILIZE | 77.0 | 6 | 16 | 1 | 26.0 | Defendente/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.05637349188327789 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 297 | MOVE_BOARD | STABILIZE | 77.0 | 6 | 16 | 1 | 26.0 | Defendente/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.1843842715024948 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 298 | MOVE_BOARD | STABILIZE | 77.0 | 6 | 16 | 1 | 26.0 | Defendente/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1721227467060089 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 299 | BUY_XP | STABILIZE | 77.0 | 6 | 16 | 1 | 26.0 | Defendente/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 300 | BUY_XP | STABILIZE | 77.0 | 6 | 12 | 1 | 26.0 | Defendente/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.0430000014603138 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 301 | BUY | STABILIZE | 77.0 | 7 | 8 | 0 | 26.0 | Defendente/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.22934623062610626 | 0.0 | 0.0 | +e4605ac7-0b51-4f1c-a658-f7d25f9a9dae / -— |
| Jogador 1 | 3-3 | 302 | MOVE_BENCH | STABILIZE | 77.0 | 7 | 5 | 0 | 26.0 | Defendente/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28443989157676697 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 303 | BUY_XP | STABILIZE | 77.0 | 7 | 5 | 0 | 28.0 | Defendente/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 304 | SELL | STABILIZE | 77.0 | 7 | 1 | 0 | 28.0 | Defendente/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0061081768944859505 | 0.0 | 0.0 | +— / -6951a681-f5b9-4c22-9182-46b4d2c3cbb3 |
| Jogador 1 | 3-3 | 305 | PASS | STABILIZE | 77.0 | 7 | 3 | 0 | 28.0 | Defendente/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 312 | BUY | STABILIZE | 77.0 | 7 | 10 | 1 | 28.0 | Defendente/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6599671840667725 | 0.0 | 0.0 | +d5848998-33f3-4632-94c0-60388a7cc6b8 / -— |
| Jogador 1 | 3-4 | 313 | BUY | STABILIZE | 77.0 | 7 | 7 | 0 | 28.0 | Defendente/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8359093070030212 | 0.0 | 0.0 | +41782483-877e-4dce-bef9-4f1f3d5757bd / -73185d11-22d3-4a1d-803a-b37e82272098,a72d427f-f2f7-46dd-97bf-d28999772db0 |
| Jogador 1 | 3-4 | 314 | BUY | STABILIZE | 77.0 | 7 | 5 | 0 | 20.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04139462485909462 | 0.0 | 0.0 | +eb7e36f0-cef9-4a2e-979a-f8a357da73e8 / -— |
| Jogador 1 | 3-4 | 315 | MOVE_BENCH | STABILIZE | 77.0 | 7 | 3 | 0 | 20.0 | Defendente/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2220706343650818 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 316 | SELL | STABILIZE | 77.0 | 7 | 3 | 0 | 26.0 | Defendente/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17823076248168945 | 0.0 | 0.0 | +— / -eb7e36f0-cef9-4a2e-979a-f8a357da73e8 |
| Jogador 1 | 3-4 | 317 | MOVE_BENCH | STABILIZE | 77.0 | 7 | 5 | 0 | 26.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26053693890571594 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 318 | MOVE_BOARD | STABILIZE | 77.0 | 7 | 5 | 0 | 28.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 319 | MOVE_BOARD | STABILIZE | 77.0 | 7 | 5 | 0 | 28.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09808357805013657 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 320 | MOVE_BENCH | STABILIZE | 77.0 | 7 | 5 | 0 | 28.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20363016426563263 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 321 | MOVE_BOARD | STABILIZE | 77.0 | 7 | 5 | 0 | 34.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08409585803747177 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 322 | PASS | STABILIZE | 77.0 | 7 | 5 | 0 | 34.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 330 | BUY | STABILIZE | 77.0 | 7 | 11 | 1 | 34.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.20596890151500702 | 0.0 | 0.0 | +8fb80cc8-4120-41a0-bc96-35f81a466ed9 / -— |
| Jogador 1 | 3-5 | 331 | MOVE_BENCH | STABILIZE | 77.0 | 7 | 9 | 0 | 34.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5435391664505005 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 332 | MOVE_BOARD | STABILIZE | 77.0 | 7 | 9 | 0 | 38.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.158089742064476 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 333 | MOVE_BOARD | STABILIZE | 77.0 | 7 | 9 | 0 | 38.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.31801438331604004 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 334 | PASS | STABILIZE | 77.0 | 7 | 9 | 0 | 38.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 342 | BUY | STABILIZE | 68.0 | 7 | 14 | 1 | 38.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7459926605224609 | 0.0 | 0.0 | +74b1cd6f-12f4-4287-a5f6-9d016663ccf5 / -— |
| Jogador 1 | 3-6 | 343 | MOVE_BENCH | STABILIZE | 68.0 | 7 | 12 | 1 | 38.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05329079553484917 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 344 | MOVE_BENCH | STABILIZE | 68.0 | 7 | 12 | 1 | 36.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31554484367370605 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 345 | BUY_XP | STABILIZE | 68.0 | 7 | 12 | 1 | 40.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 346 | BUY_XP | STABILIZE | 68.0 | 7 | 8 | 0 | 40.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 347 | BUY_XP | STABILIZE | 68.0 | 7 | 4 | 0 | 40.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 348 | MOVE_BOARD | STABILIZE | 68.0 | 7 | 0 | 0 | 40.0 | Defendente/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 349 | MOVE_BOARD | STABILIZE | 68.0 | 7 | 0 | 0 | 40.0 | Defendente/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028333866968750954 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 350 | SELL | STABILIZE | 68.0 | 7 | 0 | 0 | 40.0 | Defendente/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37284615635871887 | 0.0 | 0.0 | +— / -c448b2c1-7854-4c8c-a51b-eca2791eb639 |
| Jogador 1 | 3-6 | 351 | PASS | STABILIZE | 68.0 | 7 | 1 | 0 | 40.0 | Defendente/DA_18_Shen | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 362 | BUY | STABILIZE | 59.0 | 7 | 7 | 0 | 40.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0059379031881690025 | 0.0 | 0.0 | +1be0cdcc-ee10-44dc-ad1b-de9b53b25164 / -— |
| Jogador 1 | 3-7 | 363 | MOVE_BENCH | STABILIZE | 59.0 | 7 | 2 | 0 | 40.0 | Defendente/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025092799216508865 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 364 | PASS | STABILIZE | 59.0 | 7 | 2 | 0 | 44.0 | Defendente/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 382 | BUY | STABILIZE | 59.0 | 7 | 8 | 0 | 44.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2813456058502197 | 0.0 | 0.0 | +b7e13ed2-571b-4245-ba21-401b1eef8660 / -— |
| Jogador 1 | 4-1 | 383 | CRAFT_AND_EQUIP | STABILIZE | 59.0 | 7 | 5 | 0 | 44.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.22125332057476044 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 384 | PASS | STABILIZE | 59.0 | 7 | 5 | 0 | 44.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 402 | BUY | STABILIZE | 47.0 | 7 | 11 | 1 | 44.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6411275267601013 | 0.0 | 0.0 | +d8ecc66e-097d-4caa-a657-90fcd1286c2b / -— |
| Jogador 1 | 4-2 | 403 | PASS | STABILIZE | 47.0 | 7 | 8 | 0 | 44.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 420 | PASS | STABILIZE | 35.0 | 7 | 14 | 1 | 44.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 432 | BUY | STABILIZE | 35.0 | 7 | 21 | 2 | 44.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23434804379940033 | 0.0 | 0.0 | +652568b9-7093-4e77-8b9c-7ed286cf7f4c / -— |
| Jogador 1 | 4-4 | 433 | PASS | STABILIZE | 35.0 | 7 | 18 | 1 | 44.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 446 | BUY | STABILIZE | 35.0 | 7 | 24 | 2 | 44.0 | Defendente/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8636794090270996 | 0.0 | 0.0 | +ec9662c5-0734-41a3-9999-224d7716228b / -d5848998-33f3-4632-94c0-60388a7cc6b8,fa0e266f-ef5b-48c5-b9a3-511450e97169 |
| Jogador 1 | 4-5 | 447 | BUY | STABILIZE | 35.0 | 7 | 21 | 2 | 32.0 | Defendente/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6844017505645752 | 0.0 | 0.0 | +6fb9f857-4ee1-4b52-8825-57f514dc2d0f / -— |
| Jogador 1 | 4-5 | 448 | BUY | STABILIZE | 35.0 | 7 | 18 | 1 | 32.0 | Defendente/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015678659081459045 | 0.0 | 0.0 | +3bfc4626-3226-44b6-a401-ff9c18761448 / -— |
| Jogador 1 | 4-5 | 449 | BUY | STABILIZE | 35.0 | 7 | 14 | 1 | 32.0 | Defendente/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.187395378947258 | 0.0 | 0.0 | +023f01af-91d0-4e07-8229-2b7cded83151 / -— |
| Jogador 1 | 4-5 | 450 | BUY | STABILIZE | 35.0 | 7 | 10 | 1 | 32.0 | Defendente/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3718470335006714 | 0.0 | 0.0 | +20821a31-3317-4f82-bbb2-b70cdebdd893 / -— |
| Jogador 1 | 4-5 | 451 | REROLL | STABILIZE | 35.0 | 7 | 8 | 0 | 32.0 | Defendente/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 452 | PASS | STABILIZE | 35.0 | 7 | 6 | 0 | 32.0 | Defendente/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 453 | MOVE_BENCH | STABILIZE | 35.0 | 7 | 6 | 0 | 32.0 | Defendente/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15038904547691345 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 457 | BUY | STABILIZE | 23.0 | 7 | 11 | 1 | 38.0 | Defendente/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.199747234582901 | 0.0 | 0.0 | +685fc2a9-6a67-445e-ab34-59ec1f986f8e / -— |
| Jogador 1 | 4-6 | 458 | PASS | STABILIZE | 23.0 | 7 | 8 | 0 | 38.0 | Defendente/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 465 | MOVE_BENCH | STABILIZE | 23.0 | 7 | 8 | 0 | 38.0 | Defendente/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6567378044128418 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 470 | BUY | ALL_IN | 11.0 | 7 | 14 | 1 | 44.0 | Defendente/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2710799276828766 | 0.0 | 0.0 | +af404167-469a-447e-b415-dcb52033ef9b / -— |
| Jogador 1 | 4-7 | 471 | REROLL | ALL_IN | 11.0 | 7 | 11 | 1 | 44.0 | Defendente/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09222623705863953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 472 | REROLL | ALL_IN | 11.0 | 7 | 9 | 0 | 44.0 | Defendente/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010171356610953808 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 473 | REROLL | ALL_IN | 11.0 | 7 | 7 | 0 | 44.0 | Defendente/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010169677436351776 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 474 | REROLL | ALL_IN | 11.0 | 7 | 5 | 0 | 44.0 | Defendente/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017835598438978195 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 475 | REROLL | ALL_IN | 11.0 | 7 | 3 | 0 | 44.0 | Defendente/DA_18_Cassiopeia | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017832253128290176 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 476 | PASS | ALL_IN | 11.0 | 7 | 1 | 0 | 44.0 | Defendente/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 481 | EQUIP_FROM_INVENTORY | ALL_IN | 11.0 | 7 | 7 | 0 | 44.0 | Defendente/DA_18_Cassiopeia | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 482 | REROLL | ALL_IN | 11.0 | 7 | 7 | 0 | 44.0 | Defendente/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010164141654968262 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 483 | REROLL | ALL_IN | 11.0 | 7 | 5 | 0 | 44.0 | Defendente/DA_18_Cassiopeia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0178382471203804 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 484 | REROLL | ALL_IN | 11.0 | 7 | 3 | 0 | 44.0 | Defendente/DA_18_Cassiopeia | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01759861409664154 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 485 | PASS | ALL_IN | 11.0 | 7 | 1 | 0 | 44.0 | Defendente/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 492 | PASS | ALL_IN | 0.0 | 7 | 1 | 0 | 0.0 | Defendente/DA_18_Cassiopeia | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 502 | PASS | ALL_IN | 0.0 | 7 | 1 | 0 | 0.0 | Defendente/DA_18_Cassiopeia | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 512 | PASS | ALL_IN | 0.0 | 7 | 1 | 0 | 0.0 | Defendente/DA_18_Cassiopeia | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 522 | PASS | ALL_IN | 0.0 | 7 | 1 | 0 | 0.0 | Defendente/DA_18_Cassiopeia | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 532 | PASS | ALL_IN | 0.0 | 7 | 1 | 0 | 0.0 | Defendente/DA_18_Cassiopeia | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 542 | PASS | ALL_IN | 0.0 | 7 | 1 | 0 | 0.0 | Defendente/DA_18_Cassiopeia | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 552 | PASS | ALL_IN | 0.0 | 7 | 1 | 0 | 0.0 | Defendente/DA_18_Cassiopeia | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 568 | PASS | ALL_IN | 0.0 | 7 | 1 | 0 | 0.0 | Defendente/DA_18_Cassiopeia | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.010384615510702133 | 0.0 | 0.0 | +— / -fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.22450661659240723 | 0.0 | 0.0 | +292ef825-d326-4dd8-9c42-c47cfc62116f / -— |
| Jogador 2 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.5933380722999573 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9709054827690125 | 0.0 | 0.0 | +94ede66e-59bc-4c41-aabf-f64372e20f9a / -— |
| Jogador 2 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 26 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11205994337797165 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 27 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 49 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.12844476103782654 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 50 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.18950986862182617 | 0.0 | 0.0 | +de00430a-8a57-423c-887c-317d53c2cdd3 / -— |
| Jogador 2 | 1-3 | 51 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2418525367975235 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 52 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Sejuani | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7156829237937927 | 0.0 | 0.0 | +— / -94ede66e-59bc-4c41-aabf-f64372e20f9a |
| Jogador 2 | 1-3 | 53 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 77 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9708172678947449 | 0.0 | 0.0 | +0023ba20-d605-41fb-8002-3b6920635c59 / -— |
| Jogador 2 | 1-4 | 78 | BUY_XP | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06800000369548798 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 79 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06034808233380318 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 80 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23584432899951935 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 81 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Sejuani | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 104 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3938586413860321 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 105 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3529687225818634 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 106 | SELL | STABILIZE | 100.0 | 4 | 1 | 0 | 12.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.729604959487915 | 0.0 | 0.0 | +— / -0023ba20-d605-41fb-8002-3b6920635c59 |
| Jogador 2 | 2-1 | 107 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_Vi18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 127 | PASS | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 147 | PASS | STABILIZE | 96.0 | 4 | 13 | 1 | 12.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 170 | BUY | STABILIZE | 90.0 | 5 | 20 | 2 | 12.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.298534631729126 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 2 | 2-4 | 171 | BUY | STABILIZE | 90.0 | 5 | 17 | 1 | 12.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24421319365501404 | 0.0 | 0.0 | +8aecef4c-747d-4f03-a858-85fe309988ab / -— |
| Jogador 2 | 2-4 | 172 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 14 | 1 | 12.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14025267958641052 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 173 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 14 | 1 | 14.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4029315710067749 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 174 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 14 | 1 | 12.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8378371000289917 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 175 | PASS | STABILIZE | 90.0 | 5 | 14 | 1 | 12.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 184 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 14 | 1 | 12.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2106650322675705 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 190 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 21 | 2 | 18.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3256666362285614 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 191 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 21 | 2 | 18.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10429682582616806 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 192 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 21 | 2 | 20.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6943549513816833 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 193 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 21 | 2 | 18.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6270171403884888 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 194 | BUY_XP | STABILIZE | 90.0 | 5 | 21 | 2 | 24.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 195 | BUY_XP | STABILIZE | 90.0 | 5 | 17 | 1 | 24.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 196 | BUY_XP | STABILIZE | 90.0 | 5 | 13 | 1 | 24.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 197 | BUY_XP | STABILIZE | 90.0 | 5 | 9 | 0 | 24.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 198 | BUY_XP | STABILIZE | 90.0 | 5 | 5 | 0 | 24.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.041999999433755875 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 199 | PASS | STABILIZE | 90.0 | 6 | 1 | 0 | 24.0 | —/DA_Fiddlesticks18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 212 | BUY | STABILIZE | 90.0 | 6 | 7 | 0 | 24.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3503589332103729 | 0.0 | 0.0 | +2938180d-94e5-4bb7-832e-baa51f820ba2 / -— |
| Jogador 2 | 2-6 | 213 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 3 | 0 | 24.0 | —/DA_18_Malphite | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10351759195327759 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 214 | PASS | ECON | 90.0 | 6 | 3 | 0 | 28.0 | —/DA_18_Malphite | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 231 | MOVE_BENCH | ECON | 90.0 | 6 | 3 | 0 | 28.0 | —/DA_18_Malphite | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13692231476306915 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 233 | BUY_XP | ECON | 90.0 | 6 | 10 | 1 | 32.0 | —/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.20800000429153442 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 234 | BUY_XP | ECON | 90.0 | 6 | 6 | 0 | 32.0 | —/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 235 | PASS | ECON | 90.0 | 6 | 2 | 0 | 32.0 | —/DA_18_Malphite | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 252 | BUY_XP | ECON | 90.0 | 6 | 8 | 0 | 32.0 | —/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.09799999743700027 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 253 | BUY_XP | ECON | 90.0 | 6 | 4 | 0 | 32.0 | —/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.09799999743700027 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 254 | PASS | ECON | 90.0 | 6 | 0 | 0 | 32.0 | Colosso/DA_18_Malphite | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 273 | BUY_XP | STABILIZE | 80.0 | 6 | 5 | 0 | 32.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 274 | PASS | STABILIZE | 80.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_18_Malphite | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 296 | BUY_XP | STABILIZE | 70.0 | 6 | 7 | 0 | 32.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06199999898672104 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 297 | PASS | STABILIZE | 70.0 | 7 | 3 | 0 | 32.0 | Colosso/DA_18_Malphite | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 312 | BUY | STABILIZE | 59.0 | 7 | 9 | 0 | 32.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.743762731552124 | 0.0 | 0.0 | +727765c8-7f02-491e-a6da-12b0dab59f6d / -— |
| Jogador 2 | 3-4 | 313 | MOVE_BENCH | STABILIZE | 59.0 | 7 | 6 | 0 | 32.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009453711099922657 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 314 | MOVE_BENCH | STABILIZE | 59.0 | 7 | 6 | 0 | 30.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5722610354423523 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 315 | BUY_XP | STABILIZE | 59.0 | 7 | 6 | 0 | 38.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 316 | MOVE_BOARD | STABILIZE | 59.0 | 7 | 2 | 0 | 38.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.016028856858611107 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 317 | PASS | STABILIZE | 59.0 | 7 | 2 | 0 | 38.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 330 | BUY_XP | STABILIZE | 59.0 | 7 | 8 | 0 | 38.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 331 | BUY_XP | STABILIZE | 59.0 | 7 | 4 | 0 | 38.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 332 | PASS | STABILIZE | 59.0 | 7 | 0 | 0 | 38.0 | Colosso/DA_Fiddlesticks18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 342 | BUY | STABILIZE | 59.0 | 7 | 6 | 0 | 38.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19456720352172852 | 0.0 | 0.0 | +cbcde5b6-8f03-4d96-ade5-1ef113ab25bc / -— |
| Jogador 2 | 3-6 | 343 | MOVE_BENCH | STABILIZE | 59.0 | 7 | 2 | 0 | 38.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4773499667644501 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 344 | MOVE_BENCH | STABILIZE | 59.0 | 7 | 2 | 0 | 40.0 | Colosso/DA_18_Zyra | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00943298265337944 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 345 | MOVE_BENCH | STABILIZE | 59.0 | 7 | 2 | 0 | 38.0 | Colosso/DA_18_Zyra | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11468527466058731 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 346 | MOVE_BENCH | STABILIZE | 59.0 | 7 | 2 | 0 | 38.0 | Colosso/DA_18_Malphite | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4642989933490753 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 347 | PASS | STABILIZE | 59.0 | 7 | 2 | 0 | 40.0 | Colosso/DA_18_Malphite | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 362 | MOVE_BENCH | STABILIZE | 47.0 | 7 | 7 | 0 | 40.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00942525640130043 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 363 | MOVE_BENCH | STABILIZE | 47.0 | 7 | 7 | 0 | 38.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2684377431869507 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 364 | MOVE_BENCH | STABILIZE | 47.0 | 7 | 7 | 0 | 40.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3204774558544159 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 365 | PASS | STABILIZE | 47.0 | 7 | 7 | 0 | 40.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 382 | MOVE_BENCH | STABILIZE | 47.0 | 7 | 12 | 1 | 40.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18790556490421295 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 383 | MOVE_BENCH | STABILIZE | 47.0 | 7 | 12 | 1 | 38.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06866546720266342 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 384 | MOVE_BENCH | STABILIZE | 47.0 | 7 | 12 | 1 | 40.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3172398805618286 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 385 | PASS | STABILIZE | 47.0 | 7 | 12 | 1 | 40.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 402 | MOVE_BOARD | STABILIZE | 35.0 | 7 | 19 | 1 | 40.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0035709599032998085 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 403 | BUY_XP | STABILIZE | 35.0 | 7 | 19 | 1 | 40.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 404 | BUY_XP | STABILIZE | 35.0 | 7 | 15 | 1 | 40.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 405 | BUY_XP | STABILIZE | 35.0 | 7 | 11 | 1 | 40.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 406 | BUY_XP | STABILIZE | 35.0 | 7 | 7 | 0 | 40.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 407 | MOVE_BOARD | STABILIZE | 35.0 | 7 | 3 | 0 | 40.0 | Colosso/DA_18_Zyra | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0352528877556324 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 408 | MOVE_BOARD | STABILIZE | 35.0 | 7 | 3 | 0 | 40.0 | Colosso/DA_18_Zyra | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028333866968750954 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 409 | PASS | STABILIZE | 35.0 | 7 | 3 | 0 | 40.0 | Colosso/DA_18_Zyra | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 420 | BUY_XP | STABILIZE | 24.0 | 7 | 9 | 0 | 40.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 421 | BUY_XP | STABILIZE | 24.0 | 7 | 5 | 0 | 40.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 422 | PASS | STABILIZE | 24.0 | 7 | 1 | 0 | 40.0 | Colosso/DA_18_Zyra | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 432 | BUY_XP | STABILIZE | 24.0 | 7 | 7 | 0 | 40.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44741666316986084 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 433 | MOVE_BENCH | STABILIZE | 24.0 | 8 | 3 | 0 | 40.0 | Colosso/DA_18_Zyra | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5875647068023682 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 434 | PASS | STABILIZE | 24.0 | 8 | 3 | 0 | 46.0 | Colosso/DA_18_Zyra | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 446 | BUY_XP | STABILIZE | 24.0 | 8 | 8 | 0 | 46.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 447 | BUY_XP | STABILIZE | 24.0 | 8 | 4 | 0 | 46.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 448 | PASS | STABILIZE | 24.0 | 8 | 0 | 0 | 46.0 | Colosso/DA_18_Zyra | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 457 | BUY_XP | STABILIZE | 24.0 | 8 | 7 | 0 | 46.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 458 | PASS | STABILIZE | 24.0 | 8 | 3 | 0 | 46.0 | Colosso/DA_18_Zyra | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 470 | BUY_XP | ALL_IN | 12.0 | 8 | 8 | 0 | 46.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 471 | BUY_XP | ALL_IN | 12.0 | 8 | 4 | 0 | 46.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 472 | PASS | ALL_IN | 12.0 | 8 | 0 | 0 | 46.0 | Colosso/DA_18_Zyra | MOVE_BOARD, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 481 | EQUIP_FROM_INVENTORY | ALL_IN | 12.0 | 8 | 5 | 0 | 46.0 | Colosso/DA_18_Zyra | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 482 | CRAFT_AND_EQUIP | ALL_IN | 12.0 | 8 | 5 | 0 | 46.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | — | 0.004760212730616331 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 483 | PASS | ALL_IN | 12.0 | 8 | 5 | 0 | 46.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 492 | REROLL | ALL_IN | 12.0 | 8 | 11 | 1 | 46.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.09063787758350372 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 493 | BUY | ALL_IN | 12.0 | 8 | 9 | 0 | 46.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2677009403705597 | 0.0 | 0.0 | +3e1e33ef-4948-4ff2-bfb9-db16af507dd9 / -— |
| Jogador 2 | 5-2 | 494 | PASS | ALL_IN | 12.0 | 8 | 5 | 0 | 46.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 502 | REROLL | ALL_IN | 12.0 | 8 | 12 | 1 | 46.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017777159810066223 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 503 | BUY | ALL_IN | 12.0 | 8 | 10 | 1 | 46.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5948416590690613 | 0.0 | 0.0 | +da85aa35-e317-4d7e-9d1b-b7c69505b4d0 / -— |
| Jogador 2 | 5-3 | 504 | REROLL | ALL_IN | 12.0 | 8 | 6 | 0 | 46.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016333522275090218 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 505 | REROLL | ALL_IN | 12.0 | 8 | 4 | 0 | 46.0 | Colosso/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 506 | REROLL | ALL_IN | 12.0 | 8 | 2 | 0 | 46.0 | Colosso/DA_18_Zyra | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 507 | PASS | ALL_IN | 12.0 | 8 | 0 | 0 | 46.0 | Colosso/DA_18_Zyra | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 512 | PASS | ALL_IN | 0.0 | 8 | 0 | 0 | 0.0 | Colosso/DA_18_Zyra | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 522 | PASS | ALL_IN | 0.0 | 8 | 0 | 0 | 0.0 | Colosso/DA_18_Zyra | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 532 | PASS | ALL_IN | 0.0 | 8 | 0 | 0 | 0.0 | Colosso/DA_18_Zyra | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 542 | PASS | ALL_IN | 0.0 | 8 | 0 | 0 | 0.0 | Colosso/DA_18_Zyra | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 552 | PASS | ALL_IN | 0.0 | 8 | 0 | 0 | 0.0 | Colosso/DA_18_Zyra | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 568 | PASS | ALL_IN | 0.0 | 8 | 0 | 0 | 0.0 | Colosso/DA_18_Zyra | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.019615383818745613 | 0.0 | 0.0 | +— / -36f58657-5835-4389-95e9-a7d26464c2aa |
| Jogador 3 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.21530985832214355 | 0.0 | 0.0 | +2cf5ccdc-76f4-4fc8-b12c-7b3b68b1b2c8 / -— |
| Jogador 3 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_RekSai | MOVE_BENCH, SELL, PASS | True | True | 0.5931587815284729 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_RekSai | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_RekSai | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9699749946594238 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_RekSai | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 26 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_RekSai | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035527557134628296 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 27 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_RekSai | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 49 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_RekSai | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 77 | PASS | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 104 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 4.0 | —/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.029922112822532654 | 0.0 | 0.0 | +f19f9e7f-f189-47fe-b571-be5065c6eb39 / -— |
| Jogador 3 | 2-1 | 105 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 8 | 0 | 4.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.381960391998291 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 106 | BUY_XP | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.15800000727176666 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 107 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.15800000727176666 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 108 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Shen | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 127 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 8.0 | —/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.30548015236854553 | 0.0 | 0.0 | +8a68772c-3f02-4f2e-882b-4fa69fbb6750 / -— |
| Jogador 3 | 2-2 | 128 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 3 | 0 | 8.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42496412992477417 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 129 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34503400325775146 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 130 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09093416482210159 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 131 | PASS | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 147 | BUY | STABILIZE | 94.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.27695244550704956 | 0.0 | 0.0 | +29f10cb7-6575-47ca-b583-057992a08253 / -— |
| Jogador 3 | 2-3 | 148 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4055953323841095 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 149 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4706707298755646 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 150 | BUY_XP | STABILIZE | 94.0 | 5 | 5 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 151 | PASS | STABILIZE | 94.0 | 5 | 1 | 0 | 20.0 | —/DA_18_Diana | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 170 | BUY_XP | STABILIZE | 94.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 171 | PASS | STABILIZE | 94.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 190 | BUY_XP | STABILIZE | 94.0 | 5 | 8 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 191 | BUY_XP | STABILIZE | 94.0 | 5 | 4 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.052000001072883606 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 192 | PASS | STABILIZE | 94.0 | 6 | 0 | 0 | 20.0 | —/DA_18_Diana | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 212 | MOVE_BOARD | STABILIZE | 88.0 | 6 | 5 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06624050438404083 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 213 | BUY | STABILIZE | 88.0 | 6 | 5 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.033186174929142 | 0.0 | 0.0 | +19cba1be-95ae-4cf0-a600-0c5eb8d081b0 / -— |
| Jogador 3 | 2-6 | 214 | SELL | STABILIZE | 88.0 | 6 | 3 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17823076248168945 | 0.0 | 0.0 | +— / -19cba1be-95ae-4cf0-a600-0c5eb8d081b0 |
| Jogador 3 | 2-6 | 215 | PASS | STABILIZE | 88.0 | 6 | 5 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 233 | BUY | STABILIZE | 81.0 | 6 | 11 | 1 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8870447278022766 | 0.0 | 0.0 | +584991bb-37b3-4ac1-8e29-14e0d74c5e78 / -— |
| Jogador 3 | 2-7 | 234 | MOVE_BENCH | STABILIZE | 81.0 | 6 | 8 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4996623396873474 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 235 | BUY_XP | STABILIZE | 81.0 | 6 | 8 | 0 | 26.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 236 | BUY_XP | STABILIZE | 81.0 | 6 | 4 | 0 | 26.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 237 | PASS | STABILIZE | 81.0 | 6 | 0 | 0 | 26.0 | —/DA_18_Diana | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 252 | BUY_XP | STABILIZE | 81.0 | 6 | 6 | 0 | 26.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 253 | PASS | STABILIZE | 81.0 | 6 | 2 | 0 | 26.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 273 | MOVE_BOARD | STABILIZE | 69.0 | 6 | 8 | 0 | 26.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 274 | MOVE_BOARD | STABILIZE | 69.0 | 6 | 8 | 0 | 26.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 275 | PASS | STABILIZE | 69.0 | 6 | 8 | 0 | 26.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 296 | MOVE_BOARD | STABILIZE | 59.0 | 6 | 14 | 1 | 26.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.07879506051540375 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 297 | BUY | STABILIZE | 59.0 | 6 | 14 | 1 | 26.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.13801132142543793 | 0.0 | 0.0 | +ff0d9869-c346-4210-be85-1e802a25dd8b / -— |
| Jogador 3 | 3-3 | 298 | BUY | STABILIZE | 59.0 | 6 | 10 | 1 | 26.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03450842201709747 | 0.0 | 0.0 | +a15ff9dc-bf8a-49e0-9893-f92a212263d8 / -— |
| Jogador 3 | 3-3 | 299 | MOVE_BENCH | STABILIZE | 59.0 | 6 | 7 | 0 | 26.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5012946128845215 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 300 | MOVE_BENCH | STABILIZE | 59.0 | 6 | 7 | 0 | 28.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12108214199542999 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 301 | MOVE_BENCH | STABILIZE | 59.0 | 6 | 7 | 0 | 26.0 | Devastador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9308396577835083 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 302 | MOVE_BOARD | STABILIZE | 59.0 | 6 | 7 | 0 | 28.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05045098066329956 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 303 | SELL | STABILIZE | 59.0 | 6 | 7 | 0 | 28.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6046954393386841 | 0.0 | 0.0 | +— / -8a68772c-3f02-4f2e-882b-4fa69fbb6750 |
| Jogador 3 | 3-3 | 304 | BUY_XP | STABILIZE | 59.0 | 6 | 10 | 1 | 28.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 305 | BUY_XP | STABILIZE | 59.0 | 6 | 6 | 0 | 28.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 306 | PASS | STABILIZE | 59.0 | 6 | 2 | 0 | 28.0 | Caçador/DA_18_Sivir | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 312 | BUY | STABILIZE | 59.0 | 6 | 8 | 0 | 28.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7406362295150757 | 0.0 | 0.0 | +b5cec20a-0619-4060-9f1b-e72942ac34dd / -— |
| Jogador 3 | 3-4 | 313 | MOVE_BOARD | STABILIZE | 59.0 | 6 | 5 | 0 | 28.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 314 | MOVE_BOARD | STABILIZE | 59.0 | 6 | 5 | 0 | 28.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17773666977882385 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 315 | SELL | STABILIZE | 59.0 | 6 | 5 | 0 | 28.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.850276529788971 | 0.0 | 0.0 | +— / -b5cec20a-0619-4060-9f1b-e72942ac34dd |
| Jogador 3 | 3-4 | 316 | SELL | STABILIZE | 59.0 | 6 | 8 | 0 | 28.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27792081236839294 | 0.0 | 0.0 | +— / -584991bb-37b3-4ac1-8e29-14e0d74c5e78 |
| Jogador 3 | 3-4 | 317 | BUY | STABILIZE | 59.0 | 6 | 11 | 1 | 28.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17948557436466217 | 0.0 | 0.0 | +cce8de69-f877-4e86-b720-6aea91e68f47 / -— |
| Jogador 3 | 3-4 | 318 | BUY_XP | STABILIZE | 59.0 | 6 | 8 | 0 | 28.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07100000232458115 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 319 | MOVE_BENCH | STABILIZE | 59.0 | 7 | 4 | 0 | 28.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4563734233379364 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 320 | MOVE_BOARD | STABILIZE | 59.0 | 7 | 4 | 0 | 34.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.1956586241722107 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 321 | MOVE_BOARD | STABILIZE | 59.0 | 7 | 4 | 0 | 34.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.012479945085942745 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 322 | PASS | STABILIZE | 59.0 | 7 | 4 | 0 | 34.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 330 | BUY | STABILIZE | 59.0 | 7 | 9 | 0 | 34.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7422679662704468 | 0.0 | 0.0 | +320038b5-88c4-48fe-a7fa-a30823d674c0 / -— |
| Jogador 3 | 3-5 | 331 | MOVE_BENCH | STABILIZE | 59.0 | 7 | 6 | 0 | 34.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08396459370851517 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 332 | MOVE_BOARD | STABILIZE | 59.0 | 7 | 6 | 0 | 38.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00535556161776185 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 333 | PASS | STABILIZE | 59.0 | 7 | 6 | 0 | 38.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 342 | SELL | STABILIZE | 59.0 | 7 | 13 | 1 | 38.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6804715991020203 | 0.0 | 0.0 | +— / -bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 3-6 | 343 | PASS | STABILIZE | 59.0 | 7 | 14 | 1 | 38.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 362 | BUY | STABILIZE | 48.0 | 7 | 20 | 2 | 38.0 | Caçador/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7698661684989929 | 0.0 | 0.0 | +9175d2a8-4736-402d-873b-cf4846b04d97 / -320038b5-88c4-48fe-a7fa-a30823d674c0,cce8de69-f877-4e86-b720-6aea91e68f47 |
| Jogador 3 | 3-7 | 363 | BUY | STABILIZE | 48.0 | 7 | 17 | 1 | 26.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0358441025018692 | 0.0 | 0.0 | +210d2415-663d-4768-bbc2-238766c2b863 / -— |
| Jogador 3 | 3-7 | 364 | MOVE_BENCH | STABILIZE | 48.0 | 7 | 14 | 1 | 26.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45221853256225586 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 365 | MOVE_BOARD | STABILIZE | 48.0 | 7 | 14 | 1 | 38.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1716316044330597 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 366 | MOVE_BENCH | STABILIZE | 48.0 | 7 | 14 | 1 | 38.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4369087815284729 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 367 | MOVE_BOARD | STABILIZE | 48.0 | 7 | 14 | 1 | 44.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 368 | MOVE_BOARD | STABILIZE | 48.0 | 7 | 14 | 1 | 44.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09389273822307587 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 369 | BUY_XP | STABILIZE | 48.0 | 7 | 14 | 1 | 44.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 370 | BUY_XP | STABILIZE | 48.0 | 7 | 10 | 1 | 44.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 371 | BUY_XP | STABILIZE | 48.0 | 7 | 6 | 0 | 44.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 372 | PASS | STABILIZE | 48.0 | 7 | 2 | 0 | 44.0 | Caçador/DA_Vi18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 382 | BUY | STABILIZE | 48.0 | 7 | 7 | 0 | 44.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.28371351957321167 | 0.0 | 0.0 | +4363594b-375b-45d4-9b1a-0c1ab96367a1 / -— |
| Jogador 3 | 4-1 | 383 | MOVE_BENCH | STABILIZE | 48.0 | 7 | 4 | 0 | 44.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5681386590003967 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 384 | MOVE_BENCH | STABILIZE | 48.0 | 7 | 4 | 0 | 38.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07272947579622269 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 385 | BUY_XP | STABILIZE | 48.0 | 7 | 4 | 0 | 48.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 386 | PASS | STABILIZE | 48.0 | 7 | 0 | 0 | 48.0 | Caçador/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 402 | BUY_XP | STABILIZE | 48.0 | 7 | 6 | 0 | 48.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 403 | PASS | STABILIZE | 48.0 | 7 | 2 | 0 | 48.0 | Caçador/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 420 | BUY_XP | STABILIZE | 36.0 | 7 | 7 | 0 | 48.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 421 | PASS | STABILIZE | 36.0 | 7 | 3 | 0 | 48.0 | Caçador/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 432 | BUY_XP | STABILIZE | 36.0 | 7 | 9 | 0 | 48.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 433 | BUY_XP | STABILIZE | 36.0 | 7 | 5 | 0 | 48.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 434 | SELL | STABILIZE | 36.0 | 7 | 1 | 0 | 48.0 | Caçador/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32484614849090576 | 0.0 | 0.0 | +— / -2cf5ccdc-76f4-4fc8-b12c-7b3b68b1b2c8 |
| Jogador 3 | 4-4 | 435 | PASS | STABILIZE | 36.0 | 7 | 2 | 0 | 48.0 | Caçador/DA_Vi18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 446 | PASS | STABILIZE | 36.0 | 7 | 7 | 0 | 48.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 457 | PASS | STABILIZE | 36.0 | 7 | 14 | 1 | 48.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 470 | BUY | STABILIZE | 36.0 | 7 | 22 | 2 | 48.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6948531866073608 | 0.0 | 0.0 | +987e61e4-0d34-49cf-b1ef-a95a7a5dfb21 / -— |
| Jogador 3 | 4-7 | 471 | REROLL | STABILIZE | 36.0 | 7 | 19 | 1 | 48.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 472 | BUY_XP | STABILIZE | 36.0 | 7 | 17 | 1 | 48.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07443749904632568 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 473 | REROLL | STABILIZE | 36.0 | 8 | 13 | 1 | 48.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 474 | BUY | STABILIZE | 36.0 | 8 | 11 | 1 | 48.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34360089898109436 | 0.0 | 0.0 | +864f332a-0446-4995-b7fb-76d48d293501 / -— |
| Jogador 3 | 4-7 | 475 | MOVE_BENCH | STABILIZE | 36.0 | 8 | 7 | 0 | 48.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5631617903709412 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 476 | BUY_XP | STABILIZE | 36.0 | 8 | 7 | 0 | 54.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 477 | MOVE_BOARD | STABILIZE | 36.0 | 8 | 3 | 0 | 54.0 | Caçador/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01558587234467268 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 478 | MOVE_BOARD | STABILIZE | 36.0 | 8 | 3 | 0 | 54.0 | Caçador/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 479 | MOVE_BOARD | STABILIZE | 36.0 | 8 | 3 | 0 | 54.0 | Caçador/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1931658238172531 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 481 | EQUIP_FROM_INVENTORY | STABILIZE | 36.0 | 8 | 9 | 0 | 54.0 | Caçador/DA_Vi18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 482 | BUY | STABILIZE | 36.0 | 8 | 9 | 0 | 54.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5251843333244324 | 0.0 | 0.0 | +93581e04-3f00-4430-8e5b-c953196bc1de / -— |
| Jogador 3 | 5-1 | 483 | CRAFT_AND_EQUIP | STABILIZE | 36.0 | 8 | 5 | 0 | 54.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11709195375442505 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 484 | MOVE_BENCH | STABILIZE | 36.0 | 8 | 5 | 0 | 54.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01981431618332863 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 485 | BUY_XP | STABILIZE | 36.0 | 8 | 5 | 0 | 56.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 486 | MOVE_BOARD | STABILIZE | 36.0 | 8 | 1 | 0 | 56.0 | Caçador/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 487 | PASS | STABILIZE | 36.0 | 8 | 1 | 0 | 56.0 | Caçador/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 492 | BUY | STABILIZE | 36.0 | 8 | 8 | 0 | 56.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5524293184280396 | 0.0 | 0.0 | +389bcf7d-1a3c-4360-8bcf-a98cacecbaea / -— |
| Jogador 3 | 5-2 | 493 | BUY_XP | STABILIZE | 36.0 | 8 | 5 | 0 | 56.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 494 | PASS | STABILIZE | 36.0 | 8 | 1 | 0 | 56.0 | Caçador/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 502 | MOVE_BENCH | STABILIZE | 36.0 | 8 | 9 | 0 | 56.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08043667674064636 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 503 | PASS | STABILIZE | 36.0 | 8 | 9 | 0 | 56.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 512 | BUY_XP | STABILIZE | 36.0 | 8 | 19 | 1 | 56.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 513 | BUY_XP | STABILIZE | 36.0 | 8 | 15 | 1 | 56.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 514 | BUY_XP | STABILIZE | 36.0 | 8 | 11 | 1 | 56.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 515 | BUY_XP | STABILIZE | 36.0 | 8 | 7 | 0 | 56.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 516 | PASS | STABILIZE | 36.0 | 8 | 3 | 0 | 56.0 | Caçador/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 522 | BUY_XP | STABILIZE | 36.0 | 8 | 11 | 1 | 56.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 523 | BUY_XP | STABILIZE | 36.0 | 8 | 7 | 0 | 56.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 524 | PASS | STABILIZE | 36.0 | 8 | 3 | 0 | 56.0 | Caçador/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 532 | BUY_XP | STABILIZE | 36.0 | 8 | 12 | 1 | 56.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 533 | BUY_XP | STABILIZE | 36.0 | 8 | 8 | 0 | 56.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 534 | BUY_XP | STABILIZE | 36.0 | 8 | 4 | 0 | 56.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 535 | PASS | STABILIZE | 36.0 | 8 | 0 | 0 | 56.0 | Caçador/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 542 | BUY_XP | STABILIZE | 36.0 | 8 | 9 | 0 | 56.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08087500184774399 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 543 | MOVE_BENCH | STABILIZE | 36.0 | 9 | 5 | 0 | 56.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.397447794675827 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 544 | PASS | STABILIZE | 36.0 | 9 | 5 | 0 | 62.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 552 | EQUIP_FROM_INVENTORY | STABILIZE | 36.0 | 9 | 13 | 1 | 62.0 | Caçador/DA_Vi18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 553 | EQUIP_FROM_INVENTORY | STABILIZE | 36.0 | 9 | 13 | 1 | 62.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.003753878176212311 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 554 | BUY_XP | STABILIZE | 36.0 | 9 | 13 | 1 | 62.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 555 | BUY_XP | STABILIZE | 36.0 | 9 | 9 | 0 | 62.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 556 | BUY_XP | STABILIZE | 36.0 | 9 | 5 | 0 | 62.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 557 | PASS | STABILIZE | 36.0 | 9 | 1 | 0 | 62.0 | Caçador/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-2 | 568 | PASS | STABILIZE | 36.0 | 9 | 10 | 1 | 62.0 | Caçador/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 17 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.28737619519233704 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3375903069972992 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40336331725120544 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 26 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 49 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 77 | BUY_XP | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.06800000369548798 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 78 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.02368042804300785 | 0.0 | 0.0 | +df71e10d-846b-4b12-8eb4-53633834303f / -— |
| Jogador 4 | 1-4 | 79 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 4.0 | —/DA_18_Teemo | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.986575722694397 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 80 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Teemo | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34288489818573 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 81 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Teemo | MOVE_BOARD, PASS | True | True | 0.16431555151939392 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 82 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Teemo | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 104 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9703867435455322 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 4 | 2-1 | 105 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23212121427059174 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 106 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32118919491767883 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 107 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.32635581493377686 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 108 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.16469737887382507 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 109 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.14128389954566956 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 110 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.028817784041166306 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 111 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.11346163600683212 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 112 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 113 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.17543157935142517 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 114 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 127 | BUY_XP | STABILIZE | 95.0 | 4 | 8 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03200000151991844 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 128 | BUY | STABILIZE | 95.0 | 5 | 4 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.04703228548169136 | 0.0 | 0.0 | +4e00fb2f-75c1-4580-bd09-cb73c31af01f / -— |
| Jogador 4 | 2-2 | 129 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 10.0 | —/DA_Krug18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36574307084083557 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 130 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 16.0 | —/DA_Krug18 | BUY, MOVE_BOARD, PASS | True | True | 0.08080365508794785 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 131 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 1 | 0 | 16.0 | —/DA_Krug18 | BUY, MOVE_BOARD, PASS | True | True | 0.14635807275772095 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 132 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 16.0 | —/DA_Krug18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 147 | BUY | STABILIZE | 95.0 | 5 | 7 | 0 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4292357265949249 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 4 | 2-3 | 148 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 4 | 0 | 16.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48061978816986084 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 149 | SELL | STABILIZE | 95.0 | 5 | 4 | 0 | 20.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39178818464279175 | 0.0 | 0.0 | +— / -0e9aa759-0538-4168-a523-02a5f8e09e0a |
| Jogador 4 | 2-3 | 150 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 20.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 151 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 20.0 | —/DA_KogMaw18_AD | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 170 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 20.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.11539900302886963 | 0.0 | 0.0 | +53a17678-f853-4814-97c7-524b66ec199d / -— |
| Jogador 4 | 2-4 | 171 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 4 | 0 | 20.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45782020688056946 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 172 | SELL | STABILIZE | 95.0 | 5 | 4 | 0 | 22.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3085384666919708 | 0.0 | 0.0 | +— / -4e00fb2f-75c1-4580-bd09-cb73c31af01f |
| Jogador 4 | 2-4 | 173 | BUY_XP | STABILIZE | 95.0 | 5 | 7 | 0 | 22.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 174 | REROLL | STABILIZE | 95.0 | 5 | 3 | 0 | 22.0 | —/DA_18_Aphelios | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 175 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 22.0 | —/DA_18_Aphelios | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 190 | BUY | STABILIZE | 95.0 | 5 | 7 | 0 | 22.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4305298626422882 | 0.0 | 0.0 | +caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e / -— |
| Jogador 4 | 2-5 | 191 | SELL | STABILIZE | 95.0 | 5 | 4 | 0 | 22.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5458217263221741 | 0.0 | 0.0 | +— / -caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e |
| Jogador 4 | 2-5 | 192 | BUY_XP | STABILIZE | 95.0 | 5 | 7 | 0 | 22.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 193 | REROLL | STABILIZE | 95.0 | 5 | 3 | 0 | 22.0 | —/DA_18_Aphelios | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 194 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 22.0 | —/DA_18_Aphelios | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 212 | BUY | STABILIZE | 89.0 | 6 | 6 | 0 | 22.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2709255516529083 | 0.0 | 0.0 | +c9a1ea77-662a-469a-ba7f-eac0713c0c52 / -— |
| Jogador 4 | 2-6 | 213 | BUY | STABILIZE | 89.0 | 6 | 3 | 0 | 22.0 | —/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.968740701675415 | 0.0 | 0.0 | +b482ecdd-cc1a-40fa-8c21-cd1cac92b594 / -— |
| Jogador 4 | 2-6 | 214 | MOVE_BENCH | STABILIZE | 89.0 | 6 | 2 | 0 | 22.0 | —/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5370436310768127 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 215 | SELL | ECON | 89.0 | 6 | 2 | 0 | 28.0 | —/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0187406539916992 | 0.0 | 0.0 | +— / -b482ecdd-cc1a-40fa-8c21-cd1cac92b594 |
| Jogador 4 | 2-6 | 216 | MOVE_BOARD | ECON | 89.0 | 6 | 3 | 0 | 28.0 | —/DA_18_Aphelios | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.07442047446966171 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 217 | MOVE_BOARD | ECON | 89.0 | 6 | 3 | 0 | 28.0 | —/DA_18_Aphelios | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.14652138948440552 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 218 | MOVE_BOARD | ECON | 89.0 | 6 | 3 | 0 | 28.0 | —/DA_18_Aphelios | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.14408981800079346 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 219 | MOVE_BOARD | ECON | 89.0 | 6 | 3 | 0 | 28.0 | —/DA_18_Aphelios | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.08455117046833038 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 220 | MOVE_BOARD | ECON | 89.0 | 6 | 3 | 0 | 28.0 | —/DA_18_Aphelios | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.020740801468491554 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 221 | MOVE_BOARD | ECON | 89.0 | 6 | 3 | 0 | 28.0 | —/DA_18_Aphelios | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.19717535376548767 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 222 | PASS | ECON | 89.0 | 6 | 3 | 0 | 28.0 | —/DA_18_Aphelios | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 233 | BUY | ECON | 89.0 | 6 | 9 | 0 | 28.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3363494575023651 | 0.0 | 0.0 | +d731d71e-fc91-41ae-ab3f-75966dd2c428 / -— |
| Jogador 4 | 2-7 | 234 | BUY | ECON | 89.0 | 6 | 6 | 0 | 28.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.894477367401123 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 4 | 2-7 | 235 | MOVE_BENCH | ECON | 89.0 | 6 | 5 | 0 | 28.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3519456684589386 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 236 | BUY_XP | ECON | 89.0 | 6 | 5 | 0 | 30.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 237 | SELL | ECON | 89.0 | 6 | 1 | 0 | 30.0 | —/DA_18_Aphelios | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.944477379322052 | 0.0 | 0.0 | +— / -d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 4 | 2-7 | 238 | SELL | ECON | 89.0 | 6 | 2 | 0 | 30.0 | —/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024076923727989197 | 0.0 | 0.0 | +— / -df71e10d-846b-4b12-8eb4-53633834303f |
| Jogador 4 | 2-7 | 239 | BUY_XP | ECON | 89.0 | 6 | 4 | 0 | 30.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 240 | PASS | ECON | 89.0 | 6 | 0 | 0 | 30.0 | —/DA_18_Aphelios | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 252 | PASS | ECON | 89.0 | 6 | 5 | 0 | 30.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 273 | PASS | STABILIZE | 89.0 | 6 | 12 | 1 | 30.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 296 | BUY | STABILIZE | 89.0 | 6 | 20 | 2 | 30.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.09774180501699448 | 0.0 | 0.0 | +c2c83d3a-8db0-4a0f-a896-4227c10a8d6a / -— |
| Jogador 4 | 3-3 | 297 | MOVE_BOARD | STABILIZE | 89.0 | 6 | 17 | 1 | 30.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1619366556406021 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 298 | BUY_XP | STABILIZE | 89.0 | 6 | 17 | 1 | 30.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 299 | BUY_XP | STABILIZE | 89.0 | 6 | 13 | 1 | 30.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 300 | BUY_XP | STABILIZE | 89.0 | 6 | 9 | 0 | 30.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 301 | BUY_XP | STABILIZE | 89.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 302 | SELL | STABILIZE | 89.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18484027683734894 | 0.0 | 0.0 | +— / -c2c83d3a-8db0-4a0f-a896-4227c10a8d6a |
| Jogador 4 | 3-3 | 303 | BUY_XP | STABILIZE | 89.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.07199999690055847 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 304 | PASS | STABILIZE | 89.0 | 7 | 0 | 0 | 30.0 | Colosso/DA_18_Aphelios | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 312 | BUY | STABILIZE | 89.0 | 7 | 7 | 0 | 30.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7437868714332581 | 0.0 | 0.0 | +ccdd8153-af58-4fe7-994c-d49f0a7a17f8 / -— |
| Jogador 4 | 3-4 | 313 | MOVE_BENCH | STABILIZE | 89.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6242635250091553 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 314 | BUY_XP | STABILIZE | 89.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 315 | PASS | STABILIZE | 89.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_Fiddlesticks18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 330 | PASS | STABILIZE | 89.0 | 7 | 6 | 0 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 342 | BUY_XP | STABILIZE | 89.0 | 7 | 14 | 1 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 343 | BUY_XP | STABILIZE | 89.0 | 7 | 10 | 1 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 344 | BUY_XP | STABILIZE | 89.0 | 7 | 6 | 0 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 345 | PASS | STABILIZE | 89.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 362 | BUY_XP | STABILIZE | 89.0 | 7 | 11 | 1 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 363 | BUY_XP | STABILIZE | 89.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 364 | PASS | STABILIZE | 89.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 382 | BUY | STABILIZE | 89.0 | 7 | 11 | 1 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | -0.06689947098493576 | 0.0 | 0.0 | +d9fdb961-a3e3-4e39-9970-e46ffd59fc3b / -— |
| Jogador 4 | 4-1 | 383 | BUY | STABILIZE | 89.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2780669629573822 | 0.0 | 0.0 | +fff5cc22-5f1a-47a4-93e3-9772177b0910 / -— |
| Jogador 4 | 4-1 | 384 | CRAFT_AND_EQUIP | STABILIZE | 89.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.10078420490026474 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 385 | MOVE_BOARD | STABILIZE | 89.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0035709599032998085 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 386 | BUY_XP | STABILIZE | 89.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 387 | MOVE_BOARD | STABILIZE | 89.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008921255357563496 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 388 | MOVE_BOARD | STABILIZE | 89.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 389 | SELL | STABILIZE | 89.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.531000018119812 | 0.0 | 0.0 | +— / -fff5cc22-5f1a-47a4-93e3-9772177b0910 |
| Jogador 4 | 4-1 | 390 | MOVE_BOARD | STABILIZE | 89.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3099592328071594 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 391 | MOVE_BOARD | STABILIZE | 89.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17243216931819916 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 392 | PASS | STABILIZE | 89.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 402 | MOVE_BOARD | STABILIZE | 89.0 | 7 | 12 | 1 | 36.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1816743165254593 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 403 | MOVE_BENCH | STABILIZE | 89.0 | 7 | 12 | 1 | 36.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02101786434650421 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 404 | PASS | STABILIZE | 89.0 | 7 | 12 | 1 | 38.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 420 | MOVE_BOARD | STABILIZE | 89.0 | 7 | 22 | 2 | 38.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03448290750384331 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 421 | MOVE_BOARD | STABILIZE | 89.0 | 7 | 22 | 2 | 38.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1673896759748459 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 422 | PASS | STABILIZE | 89.0 | 7 | 22 | 2 | 38.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 432 | PASS | STABILIZE | 75.0 | 7 | 29 | 2 | 38.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 446 | BUY | FAST8 | 75.0 | 7 | 36 | 3 | 38.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2554032504558563 | 0.0 | 0.0 | +06332ba7-fc4e-431e-ab25-2fb284c08c33 / -— |
| Jogador 4 | 4-5 | 447 | BUY_XP | FAST8 | 75.0 | 7 | 33 | 3 | 38.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 448 | BUY_XP | STABILIZE | 75.0 | 7 | 29 | 2 | 38.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 449 | BUY_XP | STABILIZE | 75.0 | 7 | 25 | 2 | 38.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08443749696016312 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 450 | BUY_XP | ECON | 75.0 | 8 | 21 | 2 | 38.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2980000078678131 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 451 | BUY_XP | ECON | 75.0 | 8 | 17 | 1 | 38.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21799999475479126 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 452 | BUY_XP | ECON | 75.0 | 8 | 13 | 1 | 38.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2980000078678131 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 453 | MOVE_BENCH | ECON | 75.0 | 8 | 9 | 0 | 38.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.439554899930954 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 454 | BUY_XP | ECON | 75.0 | 8 | 9 | 0 | 44.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09799999743700027 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 455 | BUY_XP | ECON | 75.0 | 8 | 5 | 0 | 44.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09799999743700027 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 457 | BUY_XP | ECON | 63.0 | 8 | 7 | 0 | 44.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09799999743700027 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 458 | MOVE_BOARD | ECON | 63.0 | 8 | 3 | 0 | 44.0 | Colosso/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 459 | PASS | ECON | 63.0 | 8 | 3 | 0 | 44.0 | Colosso/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 470 | BUY_XP | ECON | 63.0 | 8 | 9 | 0 | 44.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09799999743700027 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 471 | BUY_XP | ECON | 63.0 | 8 | 5 | 0 | 44.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09799999743700027 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 472 | SELL | ECON | 63.0 | 8 | 1 | 0 | 44.0 | Colosso/DA_18_Aphelios | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36576923727989197 | 0.0 | 0.0 | +— / -06332ba7-fc4e-431e-ab25-2fb284c08c33 |
| Jogador 4 | 4-7 | 473 | BUY_XP | ECON | 63.0 | 8 | 4 | 0 | 44.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.09799999743700027 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 474 | PASS | ECON | 63.0 | 8 | 0 | 0 | 44.0 | Colosso/DA_18_Aphelios | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 481 | EQUIP_FROM_INVENTORY | ECON | 63.0 | 8 | 5 | 0 | 44.0 | Colosso/DA_18_Aphelios | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 482 | BUY_XP | ECON | 63.0 | 8 | 5 | 0 | 44.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.09799999743700027 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 483 | PASS | ECON | 63.0 | 8 | 1 | 0 | 44.0 | Colosso/DA_18_Aphelios | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 492 | REROLL | ECON | 46.0 | 8 | 6 | 0 | 44.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 493 | REROLL | ECON | 46.0 | 8 | 4 | 0 | 44.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 494 | PASS | ECON | 46.0 | 8 | 2 | 0 | 44.0 | Colosso/DA_18_Aphelios | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 502 | BUY | STABILIZE | 30.0 | 8 | 8 | 0 | 44.0 | Colosso/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8334593772888184 | 0.0 | 0.0 | +c56b25d1-5d1b-4a79-9368-41f6efef6af0 / -ccdd8153-af58-4fe7-994c-d49f0a7a17f8,d731d71e-fc91-41ae-ab3f-75966dd2c428 |
| Jogador 4 | 5-3 | 503 | BUY | STABILIZE | 30.0 | 8 | 5 | 0 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07825496047735214 | 0.0 | 0.0 | +586ccfc6-ee5a-4ca1-98c2-31dec4273deb / -— |
| Jogador 4 | 5-3 | 504 | MOVE_BOARD | STABILIZE | 30.0 | 8 | 1 | 0 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26049119234085083 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 505 | MOVE_BOARD | STABILIZE | 30.0 | 8 | 1 | 0 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17985932528972626 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 506 | SELL | STABILIZE | 30.0 | 8 | 1 | 0 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19269230961799622 | 0.0 | 0.0 | +— / -586ccfc6-ee5a-4ca1-98c2-31dec4273deb |
| Jogador 4 | 5-3 | 507 | BUY | STABILIZE | 30.0 | 8 | 5 | 0 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03441229835152626 | 0.0 | 0.0 | +4f487e34-c67d-489d-a21e-78b5642aefd4 / -— |
| Jogador 4 | 5-3 | 508 | MOVE_BOARD | STABILIZE | 30.0 | 8 | 1 | 0 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16945569217205048 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 509 | MOVE_BOARD | STABILIZE | 30.0 | 8 | 1 | 0 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 510 | PASS | STABILIZE | 30.0 | 8 | 1 | 0 | 32.0 | Colosso/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 512 | BUY | ALL_IN | 12.0 | 8 | 7 | 0 | 44.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05478363111615181 | 0.0 | 0.0 | +9315c427-7094-4e56-adb5-70be515fddaa / -— |
| Jogador 4 | 5-4 | 513 | REROLL | ALL_IN | 12.0 | 8 | 3 | 0 | 44.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017796732485294342 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 514 | PASS | ALL_IN | 12.0 | 8 | 1 | 0 | 44.0 | Colosso/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 522 | REROLL | ALL_IN | 12.0 | 8 | 7 | 0 | 52.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017721915617585182 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 523 | REROLL | ALL_IN | 12.0 | 8 | 5 | 0 | 52.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010204178281128407 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 524 | REROLL | ALL_IN | 12.0 | 8 | 3 | 0 | 52.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 525 | PASS | ALL_IN | 12.0 | 8 | 1 | 0 | 52.0 | Colosso/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 532 | PASS | ALL_IN | 0.0 | 8 | 1 | 0 | 0.0 | Colosso/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 542 | PASS | ALL_IN | 0.0 | 8 | 1 | 0 | 0.0 | Colosso/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 552 | PASS | ALL_IN | 0.0 | 8 | 1 | 0 | 0.0 | Colosso/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-2 | 568 | PASS | ALL_IN | 0.0 | 8 | 1 | 0 | 0.0 | Colosso/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 17 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.27265432476997375 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.027269404381513596 | 0.0 | 0.0 | +df7d3860-9b2e-45ed-b564-281d95e64e82 / -— |
| Jogador 5 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37584805488586426 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 26 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 49 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 77 | PASS | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 104 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.26276248693466187 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 105 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004183540586382151 | 0.0 | 0.0 | +a5c3f6df-50ac-4f3b-aa9c-6476a055aa53 / -— |
| Jogador 5 | 2-1 | 106 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15707001090049744 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 107 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32034075260162354 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 108 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.693448543548584 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 109 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.26141127943992615 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 110 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 111 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 16.0 | —/DA_18_Cassiopeia | MOVE_BOARD, PASS | True | True | -0.18081526458263397 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 112 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 16.0 | —/DA_18_Cassiopeia | MOVE_BOARD, PASS | True | True | 0.153819739818573 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 113 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 16.0 | —/DA_18_Cassiopeia | MOVE_BOARD, PASS | True | True | 0.13510000705718994 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 114 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 16.0 | —/DA_18_Cassiopeia | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 127 | BUY | STABILIZE | 96.0 | 4 | 5 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2863383889198303 | 0.0 | 0.0 | +68cd8ae3-399f-461f-89a8-189d7b0a6b59 / -— |
| Jogador 5 | 2-2 | 128 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1895359307527542 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 129 | SELL | STABILIZE | 96.0 | 4 | 2 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3604661226272583 | 0.0 | 0.0 | +— / -df330dae-9fc1-440f-896d-a733d052e5ba |
| Jogador 5 | 2-2 | 130 | BUY_XP | STABILIZE | 96.0 | 4 | 5 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.052000001072883606 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 131 | PASS | STABILIZE | 96.0 | 5 | 1 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 147 | BUY | STABILIZE | 91.0 | 5 | 7 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9503758549690247 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -— |
| Jogador 5 | 2-3 | 148 | SELL | STABILIZE | 91.0 | 5 | 5 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0003758668899536 | 0.0 | 0.0 | +— / -abde1e81-f452-47ad-9f1e-45efb138f86d |
| Jogador 5 | 2-3 | 149 | BUY | STABILIZE | 91.0 | 5 | 7 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2766529321670532 | 0.0 | 0.0 | +5627d898-cff3-4664-87d1-40a8f3656ab3 / -— |
| Jogador 5 | 2-3 | 150 | SELL | STABILIZE | 91.0 | 5 | 5 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3266529440879822 | 0.0 | 0.0 | +— / -5627d898-cff3-4664-87d1-40a8f3656ab3 |
| Jogador 5 | 2-3 | 151 | BUY_XP | STABILIZE | 91.0 | 5 | 7 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.15800000727176666 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 152 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 3 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.16868707537651062 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 153 | REROLL | STABILIZE | 91.0 | 5 | 3 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 154 | BUY | STABILIZE | 91.0 | 5 | 1 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, MOVE_BOARD, PASS | True | True | 0.34528329968452454 | 0.0 | 0.0 | +7d8f4f6b-4eba-4c31-9834-bd81a3765520 / -— |
| Jogador 5 | 2-3 | 155 | SELL | STABILIZE | 91.0 | 5 | 0 | 0 | 16.0 | —/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3952833116054535 | 0.0 | 0.0 | +— / -7d8f4f6b-4eba-4c31-9834-bd81a3765520 |
| Jogador 5 | 2-3 | 156 | PASS | STABILIZE | 91.0 | 5 | 1 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 170 | BUY | LOSS_STREAK | 85.0 | 5 | 7 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.038560401648283005 | 0.0 | 0.0 | +2c7e844d-925a-43bb-8be8-65a71d11f964 / -— |
| Jogador 5 | 2-4 | 171 | MOVE_BENCH | LOSS_STREAK | 85.0 | 5 | 4 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4024730324745178 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 172 | BUY_XP | LOSS_STREAK | 85.0 | 5 | 4 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 173 | PASS | LOSS_STREAK | 85.0 | 5 | 0 | 0 | 22.0 | —/DA_18_MasterYi_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 190 | BUY_XP | LOSS_STREAK | 85.0 | 5 | 6 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 191 | PASS | LOSS_STREAK | 85.0 | 5 | 2 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 212 | BUY | LOSS_STREAK | 80.0 | 6 | 8 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.35354167222976685 | 0.0 | 0.0 | +2a286030-5984-44b5-87ff-6c948d2e672e / -— |
| Jogador 5 | 2-6 | 213 | SELL | LOSS_STREAK | 80.0 | 6 | 6 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4035416543483734 | 0.0 | 0.0 | +— / -2a286030-5984-44b5-87ff-6c948d2e672e |
| Jogador 5 | 2-6 | 214 | BUY | LOSS_STREAK | 80.0 | 6 | 8 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.35389846563339233 | 0.0 | 0.0 | +b3f8c1ae-0292-46d8-bb32-06b85a46353d / -— |
| Jogador 5 | 2-6 | 215 | SELL | LOSS_STREAK | 80.0 | 6 | 6 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4038984775543213 | 0.0 | 0.0 | +— / -b3f8c1ae-0292-46d8-bb32-06b85a46353d |
| Jogador 5 | 2-6 | 216 | BUY | LOSS_STREAK | 80.0 | 6 | 8 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2537631690502167 | 0.0 | 0.0 | +07130d94-c79f-4052-b3e9-7f867421f01b / -— |
| Jogador 5 | 2-6 | 217 | BUY_XP | LOSS_STREAK | 80.0 | 6 | 6 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15800000727176666 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 218 | MOVE_BOARD | LOSS_STREAK | 80.0 | 6 | 2 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 219 | SELL | LOSS_STREAK | 80.0 | 6 | 2 | 0 | 22.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30376315116882324 | 0.0 | 0.0 | +— / -07130d94-c79f-4052-b3e9-7f867421f01b |
| Jogador 5 | 2-6 | 220 | BUY_XP | LOSS_STREAK | 80.0 | 6 | 4 | 0 | 22.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.15800000727176666 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 221 | MOVE_BOARD | LOSS_STREAK | 80.0 | 6 | 0 | 0 | 22.0 | —/DA_18_Rammus | MOVE_BOARD, PASS | True | True | -0.32744553685188293 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 222 | PASS | LOSS_STREAK | 80.0 | 6 | 0 | 0 | 22.0 | —/DA_18_Rammus | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 233 | BUY | LOSS_STREAK | 73.0 | 6 | 7 | 0 | 22.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.26556169986724854 | 0.0 | 0.0 | +8e819ba6-a356-4d9b-a8c9-7493332900fb / -— |
| Jogador 5 | 2-7 | 234 | BUY | LOSS_STREAK | 73.0 | 6 | 4 | 0 | 22.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35595595836639404 | 0.0 | 0.0 | +dca8bf82-80ac-4054-9a77-3891a7de23e2 / -— |
| Jogador 5 | 2-7 | 235 | MOVE_BENCH | LOSS_STREAK | 73.0 | 6 | 2 | 0 | 22.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.615893542766571 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 236 | MOVE_BOARD | LOSS_STREAK | 73.0 | 6 | 2 | 0 | 26.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3133748769760132 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 237 | MOVE_BENCH | LOSS_STREAK | 73.0 | 6 | 2 | 0 | 26.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07184554636478424 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 238 | SELL | LOSS_STREAK | 73.0 | 6 | 2 | 0 | 30.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06421984732151031 | 0.0 | 0.0 | +— / -f9c418e0-f8aa-4492-8b97-8855ce3af370 |
| Jogador 5 | 2-7 | 239 | MOVE_BOARD | LOSS_STREAK | 73.0 | 6 | 3 | 0 | 30.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1271149069070816 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 240 | MOVE_BOARD | LOSS_STREAK | 73.0 | 6 | 3 | 0 | 30.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 241 | MOVE_BOARD | LOSS_STREAK | 73.0 | 6 | 3 | 0 | 30.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.032957449555397034 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 242 | MOVE_BOARD | LOSS_STREAK | 73.0 | 6 | 3 | 0 | 30.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 243 | PASS | LOSS_STREAK | 73.0 | 6 | 3 | 0 | 30.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 252 | BUY | LOSS_STREAK | 73.0 | 6 | 10 | 1 | 30.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.5934773683547974 | 0.0 | 0.0 | +dc9a3df1-7032-4c92-a919-ca17ae7639ea / -— |
| Jogador 5 | 3-1 | 253 | MOVE_BENCH | STABILIZE | 73.0 | 6 | 7 | 0 | 30.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15010547637939453 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 254 | BUY_XP | STABILIZE | 73.0 | 6 | 7 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 255 | SELL | STABILIZE | 73.0 | 6 | 3 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015729306265711784 | 0.0 | 0.0 | +— / -dca8bf82-80ac-4054-9a77-3891a7de23e2 |
| Jogador 5 | 3-1 | 256 | BUY_XP | STABILIZE | 73.0 | 6 | 5 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 257 | MOVE_BOARD | STABILIZE | 73.0 | 6 | 1 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 258 | MOVE_BOARD | STABILIZE | 73.0 | 6 | 1 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, MOVE_BOARD, PASS | True | True | 0.17968499660491943 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 259 | MOVE_BOARD | STABILIZE | 73.0 | 6 | 1 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 260 | MOVE_BOARD | STABILIZE | 73.0 | 6 | 1 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, MOVE_BOARD, PASS | True | True | 0.16224460303783417 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 261 | PASS | STABILIZE | 73.0 | 6 | 1 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 273 | REROLL | STABILIZE | 73.0 | 6 | 7 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 274 | REROLL | STABILIZE | 73.0 | 6 | 5 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 275 | REROLL | STABILIZE | 73.0 | 6 | 3 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 276 | MOVE_BOARD | STABILIZE | 73.0 | 6 | 1 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 277 | MOVE_BOARD | STABILIZE | 73.0 | 6 | 1 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, MOVE_BOARD, PASS | True | True | -0.30113935470581055 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 278 | PASS | STABILIZE | 73.0 | 6 | 1 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 296 | BUY | STABILIZE | 64.0 | 6 | 6 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.23435980081558228 | 0.0 | 0.0 | +d754fcfc-6d22-4bc0-8643-8f4bef9afda5 / -— |
| Jogador 5 | 3-3 | 297 | MOVE_BOARD | STABILIZE | 64.0 | 6 | 3 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3080379366874695 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 298 | MOVE_BOARD | STABILIZE | 64.0 | 6 | 3 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 299 | PASS | STABILIZE | 64.0 | 6 | 3 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 312 | REROLL | STABILIZE | 54.0 | 6 | 9 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 313 | BUY | STABILIZE | 54.0 | 6 | 7 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04489108920097351 | 0.0 | 0.0 | +9b5e9e71-6772-49bc-979f-11f446f27b11 / -— |
| Jogador 5 | 3-4 | 314 | REROLL | STABILIZE | 54.0 | 6 | 3 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 315 | BUY | STABILIZE | 54.0 | 6 | 1 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22057148814201355 | 0.0 | 0.0 | +da5abe09-7f54-4361-8d82-84427a9da9e1 / -— |
| Jogador 5 | 3-4 | 316 | MOVE_BOARD | STABILIZE | 54.0 | 6 | 0 | 0 | 32.0 | Vivaz/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13100743293762207 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 317 | SELL | STABILIZE | 54.0 | 6 | 0 | 0 | 32.0 | Vivaz/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4963274896144867 | 0.0 | 0.0 | +— / -da5abe09-7f54-4361-8d82-84427a9da9e1 |
| Jogador 5 | 3-4 | 318 | BUY | STABILIZE | 54.0 | 6 | 1 | 0 | 32.0 | Vivaz/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04548688977956772 | 0.0 | 0.0 | +4518ad1d-87e7-4110-830a-96183c533201 / -— |
| Jogador 5 | 3-4 | 319 | SELL | STABILIZE | 54.0 | 6 | 0 | 0 | 32.0 | Vivaz/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18709473311901093 | 0.0 | 0.0 | +— / -4518ad1d-87e7-4110-830a-96183c533201 |
| Jogador 5 | 3-4 | 320 | MOVE_BENCH | STABILIZE | 54.0 | 6 | 1 | 0 | 32.0 | Vivaz/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14818593859672546 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 321 | SELL | STABILIZE | 54.0 | 6 | 1 | 0 | 34.0 | Vivaz/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0122307687997818 | 0.0 | 0.0 | +— / -a5c3f6df-50ac-4f3b-aa9c-6476a055aa53 |
| Jogador 5 | 3-4 | 322 | PASS | STABILIZE | 54.0 | 6 | 3 | 0 | 34.0 | Vivaz/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 330 | BUY | STABILIZE | 54.0 | 6 | 9 | 0 | 34.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.284643292427063 | 0.0 | 0.0 | +ab472080-6e4b-4b75-b37d-cf10da9a5a0d / -— |
| Jogador 5 | 3-5 | 331 | PASS | STABILIZE | 54.0 | 6 | 7 | 0 | 34.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 342 | BUY_XP | STABILIZE | 42.0 | 6 | 13 | 1 | 34.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 343 | BUY_XP | STABILIZE | 42.0 | 6 | 9 | 0 | 34.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08491666615009308 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 344 | PASS | STABILIZE | 42.0 | 7 | 5 | 0 | 34.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 355 | MOVE_BENCH | STABILIZE | 42.0 | 7 | 5 | 0 | 34.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6078866124153137 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 362 | BUY | STABILIZE | 42.0 | 7 | 11 | 1 | 38.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12383285164833069 | 0.0 | 0.0 | +a8a8381a-f3a8-45ec-9106-293d73fca0c8 / -— |
| Jogador 5 | 3-7 | 363 | MOVE_BENCH | STABILIZE | 42.0 | 7 | 7 | 0 | 38.0 | Vivaz/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01994626596570015 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 364 | PASS | STABILIZE | 42.0 | 7 | 7 | 0 | 40.0 | Vivaz/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 382 | BUY | STABILIZE | 42.0 | 7 | 12 | 1 | 40.0 | Vivaz/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31335851550102234 | 0.0 | 0.0 | +86530a1f-5325-45fa-bf43-86419ccfda54 / -— |
| Jogador 5 | 4-1 | 383 | PASS | STABILIZE | 42.0 | 7 | 8 | 0 | 40.0 | Vivaz/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 402 | BUY | STABILIZE | 29.0 | 7 | 13 | 1 | 40.0 | Vivaz/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8339975476264954 | 0.0 | 0.0 | +6d07e1f3-82d2-45a3-8dd8-56ec5760a4a9 / -8e819ba6-a356-4d9b-a8c9-7493332900fb,dc9a3df1-7032-4c92-a919-ca17ae7639ea |
| Jogador 5 | 4-2 | 403 | BUY | STABILIZE | 29.0 | 7 | 10 | 1 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014225296676158905 | 0.0 | 0.0 | +94e3fa7e-029d-4de6-a1e4-9e67ce1b699e / -— |
| Jogador 5 | 4-2 | 404 | BUY | STABILIZE | 29.0 | 7 | 6 | 0 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2364266961812973 | 0.0 | 0.0 | +a7893c5d-2faa-4292-9240-f3cc5813151e / -— |
| Jogador 5 | 4-2 | 405 | BUY | STABILIZE | 29.0 | 7 | 2 | 0 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2878056466579437 | 0.0 | 0.0 | +2357a4df-3c61-4957-83c3-572bbb99ac5a / -— |
| Jogador 5 | 4-2 | 406 | MOVE_BENCH | STABILIZE | 29.0 | 7 | 1 | 0 | 28.0 | Vivaz/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18043403327465057 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 407 | MOVE_BOARD | STABILIZE | 29.0 | 7 | 1 | 0 | 36.0 | Vivaz/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29497402906417847 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 408 | MOVE_BOARD | STABILIZE | 29.0 | 7 | 1 | 0 | 36.0 | Vivaz/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16497652232646942 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 409 | MOVE_BOARD | STABILIZE | 29.0 | 7 | 1 | 0 | 36.0 | Vivaz/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1223064735531807 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 410 | PASS | STABILIZE | 29.0 | 7 | 1 | 0 | 36.0 | Vivaz/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 414 | MOVE_BENCH | STABILIZE | 29.0 | 7 | 1 | 0 | 36.0 | Vivaz/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.634912371635437 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 420 | BUY | STABILIZE | 29.0 | 7 | 7 | 0 | 44.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7458512187004089 | 0.0 | 0.0 | +11b28280-bb53-4ca7-81b7-5ce8705303a5 / -— |
| Jogador 5 | 4-3 | 421 | PASS | STABILIZE | 29.0 | 7 | 5 | 0 | 44.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 432 | BUY | STABILIZE | 18.0 | 7 | 10 | 1 | 44.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20375026762485504 | 0.0 | 0.0 | +a5c83255-d413-4d36-92a8-3552e6785108 / -— |
| Jogador 5 | 4-4 | 433 | BUY | STABILIZE | 18.0 | 7 | 7 | 0 | 44.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8359479308128357 | 0.0 | 0.0 | +ded275a3-9551-4816-8112-f0a25524412c / -11b28280-bb53-4ca7-81b7-5ce8705303a5,ab472080-6e4b-4b75-b37d-cf10da9a5a0d |
| Jogador 5 | 4-4 | 434 | BUY | STABILIZE | 18.0 | 7 | 5 | 0 | 40.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19354987144470215 | 0.0 | 0.0 | +7fb0217d-521c-42b5-995c-81e299b3b934 / -— |
| Jogador 5 | 4-4 | 435 | PASS | STABILIZE | 18.0 | 7 | 2 | 0 | 40.0 | Vivaz/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 442 | MOVE_BENCH | STABILIZE | 18.0 | 7 | 2 | 0 | 40.0 | Vivaz/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47613683342933655 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 446 | BUY | STABILIZE | 18.0 | 7 | 7 | 0 | 46.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28398293256759644 | 0.0 | 0.0 | +d366508d-f33b-485a-8ff3-e5d0a248ae3e / -— |
| Jogador 5 | 4-5 | 447 | REROLL | STABILIZE | 18.0 | 7 | 4 | 0 | 46.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017179783433675766 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 448 | PASS | STABILIZE | 18.0 | 7 | 2 | 0 | 46.0 | Vivaz/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 457 | BUY | STABILIZE | 18.0 | 7 | 8 | 0 | 46.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2325005829334259 | 0.0 | 0.0 | +ff181737-4995-4a67-add2-4f55cebabbee / -— |
| Jogador 5 | 4-6 | 458 | REROLL | STABILIZE | 18.0 | 7 | 6 | 0 | 46.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01590786874294281 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 459 | REROLL | STABILIZE | 18.0 | 7 | 4 | 0 | 46.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01261995080858469 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 460 | REROLL | STABILIZE | 18.0 | 7 | 2 | 0 | 46.0 | Vivaz/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 461 | PASS | STABILIZE | 18.0 | 7 | 0 | 0 | 46.0 | Vivaz/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 470 | PASS | ALL_IN | 5.0 | 7 | 5 | 0 | 46.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 481 | EQUIP_FROM_INVENTORY | ALL_IN | 5.0 | 7 | 10 | 1 | 46.0 | Vivaz/DA_18_Tristana | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 482 | REROLL | ALL_IN | 5.0 | 7 | 10 | 1 | 46.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0963631421327591 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 483 | REROLL | ALL_IN | 5.0 | 7 | 8 | 0 | 46.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.017325524240732193 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 484 | REROLL | ALL_IN | 5.0 | 7 | 6 | 0 | 46.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.011964183300733566 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 485 | REROLL | ALL_IN | 5.0 | 7 | 4 | 0 | 46.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.015518813394010067 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 486 | REROLL | ALL_IN | 5.0 | 7 | 2 | 0 | 46.0 | Vivaz/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 487 | PASS | ALL_IN | 5.0 | 7 | 0 | 0 | 46.0 | Vivaz/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 492 | PASS | ALL_IN | 0.0 | 7 | 0 | 0 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 502 | PASS | ALL_IN | 0.0 | 7 | 0 | 0 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 512 | PASS | ALL_IN | 0.0 | 7 | 0 | 0 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 522 | PASS | ALL_IN | 0.0 | 7 | 0 | 0 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 532 | PASS | ALL_IN | 0.0 | 7 | 0 | 0 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 542 | PASS | ALL_IN | 0.0 | 7 | 0 | 0 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 552 | PASS | ALL_IN | 0.0 | 7 | 0 | 0 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 568 | PASS | ALL_IN | 0.0 | 7 | 0 | 0 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0013076922623440623 | 0.0 | 0.0 | +— / -698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +9002992e-4dcd-4fec-939c-87393464a41d / -— |
| Jogador 6 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.6080599427223206 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.04858612269163132 | 0.0 | 0.0 | +4d0bf502-ac30-4cdb-9da7-4f9a7ab054b1 / -— |
| Jogador 6 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.072932481765747 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 26 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5744122862815857 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 27 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 49 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.00015411031199619174 | 0.0 | 0.0 | +f29b0444-8dd6-44a6-9a04-824febf737a0 / -— |
| Jogador 6 | 1-3 | 50 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48899999260902405 | 0.0 | 0.0 | +— / -f29b0444-8dd6-44a6-9a04-824febf737a0 |
| Jogador 6 | 1-3 | 51 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.00015411031199619174 | 0.0 | 0.0 | +c3c53e80-c8e2-4774-afa2-9b0f4ab3b326 / -— |
| Jogador 6 | 1-3 | 52 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4659231901168823 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 53 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | -0.29711833596229553 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 54 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Teemo | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 77 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 104 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.973596453666687 | 0.0 | 0.0 | +185ee377-0917-4209-905b-9486d5be0193 / -— |
| Jogador 6 | 2-1 | 105 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179723739624023 | 0.0 | 0.0 | +646fc826-453b-479f-97d1-8aa2a9d86dc3 / -185ee377-0917-4209-905b-9486d5be0193,9002992e-4dcd-4fec-939c-87393464a41d |
| Jogador 6 | 2-1 | 106 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12511856853961945 | 0.0 | 0.0 | +75005e9c-56d1-48d6-815e-573e489e3dd7 / -— |
| Jogador 6 | 2-1 | 107 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5132974982261658 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 108 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3521210253238678 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 109 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37254416942596436 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 110 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 18.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.14408981800079346 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 111 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 18.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.28522995114326477 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 112 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 18.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09785233438014984 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 113 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 18.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 114 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 18.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 127 | BUY | STABILIZE | 95.0 | 4 | 7 | 0 | 18.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4652961492538452 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 128 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 4 | 0 | 18.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06055152416229248 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 129 | BUY | STABILIZE | 95.0 | 4 | 4 | 0 | 18.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06993073970079422 | 0.0 | 0.0 | +f1876a44-285c-4a57-8129-205768cd6ee6 / -— |
| Jogador 6 | 2-2 | 130 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 2 | 0 | 18.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2508719265460968 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 131 | SELL | STABILIZE | 95.0 | 4 | 2 | 0 | 20.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.033307693898677826 | 0.0 | 0.0 | +— / -c3c53e80-c8e2-4774-afa2-9b0f4ab3b326 |
| Jogador 6 | 2-2 | 132 | BUY_XP | STABILIZE | 95.0 | 4 | 4 | 0 | 20.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 133 | SELL | STABILIZE | 95.0 | 4 | 0 | 0 | 20.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2133076936006546 | 0.0 | 0.0 | +— / -f1876a44-285c-4a57-8129-205768cd6ee6 |
| Jogador 6 | 2-2 | 134 | MOVE_BOARD | STABILIZE | 95.0 | 4 | 2 | 0 | 20.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.12647919356822968 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 135 | PASS | STABILIZE | 95.0 | 4 | 2 | 0 | 20.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 147 | BUY | STABILIZE | 88.0 | 4 | 8 | 0 | 20.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3718286156654358 | 0.0 | 0.0 | +2ef60eed-d073-41a6-adec-4466c673b313 / -— |
| Jogador 6 | 2-3 | 148 | SELL | STABILIZE | 88.0 | 4 | 6 | 0 | 20.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42182859778404236 | 0.0 | 0.0 | +— / -2ef60eed-d073-41a6-adec-4466c673b313 |
| Jogador 6 | 2-3 | 149 | BUY | STABILIZE | 88.0 | 4 | 8 | 0 | 20.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.27674487233161926 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 6 | 2-3 | 150 | BUY_XP | STABILIZE | 88.0 | 4 | 6 | 0 | 20.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 151 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 2 | 0 | 20.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3033169209957123 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 152 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 2 | 0 | 18.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.577346682548523 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 153 | PASS | STABILIZE | 88.0 | 5 | 2 | 0 | 24.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 170 | BUY | STABILIZE | 83.0 | 5 | 8 | 0 | 24.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.5283918976783752 | 0.0 | 0.0 | +7915a339-3bda-4275-80ae-9941370ea609 / -— |
| Jogador 6 | 2-4 | 171 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 7 | 0 | 24.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007146743126213551 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 172 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 7 | 0 | 22.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3160921633243561 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 173 | BUY | STABILIZE | 83.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9971569180488586 | 0.0 | 0.0 | +82e3ae1b-a015-4fac-8624-f3b73ec1d90c / -— |
| Jogador 6 | 2-4 | 174 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 6 | 0 | 20.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16574729979038239 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 175 | SELL | STABILIZE | 83.0 | 5 | 6 | 0 | 22.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0029485318809747696 | 0.0 | 0.0 | +— / -4d0bf502-ac30-4cdb-9da7-4f9a7ab054b1 |
| Jogador 6 | 2-4 | 176 | SELL | STABILIZE | 83.0 | 5 | 8 | 0 | 22.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0471569299697876 | 0.0 | 0.0 | +— / -82e3ae1b-a015-4fac-8624-f3b73ec1d90c |
| Jogador 6 | 2-4 | 177 | MOVE_BOARD | STABILIZE | 83.0 | 5 | 9 | 0 | 22.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 178 | MOVE_BOARD | STABILIZE | 83.0 | 5 | 9 | 0 | 22.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.11087857931852341 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 179 | PASS | STABILIZE | 83.0 | 5 | 9 | 0 | 22.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 190 | BUY | STABILIZE | 83.0 | 5 | 15 | 1 | 22.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2804402709007263 | 0.0 | 0.0 | +f095cd70-c807-4086-a3f1-ddda4f6aa574 / -— |
| Jogador 6 | 2-5 | 191 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 13 | 1 | 22.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2665010690689087 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 192 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 13 | 1 | 20.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029328448697924614 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 193 | PASS | STABILIZE | 83.0 | 5 | 13 | 1 | 22.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 212 | BUY | STABILIZE | 83.0 | 5 | 20 | 2 | 22.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.878514289855957 | 0.0 | 0.0 | +c96b6357-8134-4e68-af0b-f5695a815597 / -— |
| Jogador 6 | 2-6 | 213 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 17 | 1 | 22.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2873031497001648 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 214 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 17 | 1 | 22.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27268216013908386 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 215 | PASS | STABILIZE | 83.0 | 5 | 17 | 1 | 24.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 233 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 25 | 2 | 24.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004756048321723938 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 234 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 25 | 2 | 22.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2967827320098877 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 235 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 25 | 2 | 20.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4839679002761841 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 236 | PASS | STABILIZE | 83.0 | 5 | 25 | 2 | 24.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 252 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 33 | 3 | 24.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.004752591717988253 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 253 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 33 | 3 | 22.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29652759432792664 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 254 | BUY | SLOWROLL | 83.0 | 5 | 33 | 3 | 20.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22955948114395142 | 0.0 | 0.0 | +5489a8f6-2466-4171-b91e-64c367875d3c / -— |
| Jogador 6 | 3-1 | 255 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 30 | 3 | 20.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4775547385215759 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 256 | BUY_XP | SLOWROLL | 83.0 | 5 | 30 | 3 | 24.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1080000028014183 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 257 | BUY_XP | STABILIZE | 83.0 | 5 | 26 | 2 | 24.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08100000023841858 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 258 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 22 | 2 | 24.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08956800401210785 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 259 | BUY_XP | STABILIZE | 83.0 | 6 | 22 | 2 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 260 | BUY_XP | STABILIZE | 83.0 | 6 | 18 | 1 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 261 | BUY_XP | STABILIZE | 83.0 | 6 | 14 | 1 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 262 | PASS | STABILIZE | 83.0 | 6 | 10 | 1 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 273 | BUY_XP | STABILIZE | 83.0 | 6 | 18 | 1 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 274 | BUY_XP | STABILIZE | 83.0 | 6 | 14 | 1 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 275 | BUY_XP | STABILIZE | 83.0 | 6 | 10 | 1 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 276 | BUY_XP | STABILIZE | 83.0 | 6 | 6 | 0 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 277 | SELL | STABILIZE | 83.0 | 6 | 2 | 0 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7514423727989197 | 0.0 | 0.0 | +— / -7915a339-3bda-4275-80ae-9941370ea609 |
| Jogador 6 | 3-2 | 278 | SELL | STABILIZE | 83.0 | 6 | 3 | 0 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4006653130054474 | 0.0 | 0.0 | +— / -5489a8f6-2466-4171-b91e-64c367875d3c |
| Jogador 6 | 3-2 | 279 | BUY_XP | STABILIZE | 83.0 | 6 | 6 | 0 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 280 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 2 | 0 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 281 | PASS | STABILIZE | 83.0 | 6 | 2 | 0 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 296 | BUY | STABILIZE | 72.0 | 7 | 7 | 0 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2812846004962921 | 0.0 | 0.0 | +46fc5f36-cf3e-422e-89f3-9501ec9d7d12 / -— |
| Jogador 6 | 3-3 | 297 | BUY | STABILIZE | 72.0 | 7 | 4 | 0 | 30.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03416426107287407 | 0.0 | 0.0 | +6084e8d8-82f2-47e3-b8e1-4077ad70efe5 / -— |
| Jogador 6 | 3-3 | 298 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 1 | 0 | 30.0 | Feérico/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5775518417358398 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 299 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 1 | 0 | 36.0 | Feérico/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 300 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 1 | 0 | 36.0 | Feérico/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06863513588905334 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 301 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 1 | 0 | 36.0 | Feérico/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 302 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 1 | 0 | 36.0 | Feérico/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 303 | PASS | STABILIZE | 72.0 | 7 | 1 | 0 | 36.0 | Feérico/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 312 | BUY | STABILIZE | 62.0 | 7 | 7 | 0 | 36.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2759949564933777 | 0.0 | 0.0 | +6e4f7b89-c6fa-4963-83e1-8fc0f1a13dc5 / -— |
| Jogador 6 | 3-4 | 313 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 3 | 0 | 36.0 | Feérico/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14415687322616577 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 314 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 3 | 0 | 40.0 | Feérico/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02132791094481945 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 315 | PASS | STABILIZE | 62.0 | 7 | 3 | 0 | 40.0 | Feérico/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 330 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 9 | 0 | 40.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7499474883079529 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 331 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 9 | 0 | 36.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2142535299062729 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 332 | PASS | STABILIZE | 62.0 | 7 | 9 | 0 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 342 | BUY_XP | STABILIZE | 62.0 | 7 | 16 | 1 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 343 | BUY_XP | STABILIZE | 62.0 | 7 | 12 | 1 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 344 | BUY_XP | STABILIZE | 62.0 | 7 | 8 | 0 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 345 | BUY_XP | STABILIZE | 62.0 | 7 | 4 | 0 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 346 | PASS | STABILIZE | 62.0 | 7 | 0 | 0 | 38.0 | Feérico/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 362 | BUY_XP | STABILIZE | 62.0 | 7 | 7 | 0 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 363 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 3 | 0 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1213110089302063 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 364 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 3 | 0 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04875248298048973 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 365 | PASS | STABILIZE | 62.0 | 7 | 3 | 0 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 382 | BUY_XP | STABILIZE | 62.0 | 7 | 9 | 0 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 383 | BUY_XP | STABILIZE | 62.0 | 7 | 5 | 0 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 384 | PASS | STABILIZE | 62.0 | 7 | 1 | 0 | 38.0 | Feérico/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 402 | BUY_XP | STABILIZE | 62.0 | 7 | 8 | 0 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 403 | BUY_XP | STABILIZE | 62.0 | 7 | 4 | 0 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 404 | PASS | STABILIZE | 62.0 | 7 | 0 | 0 | 38.0 | Feérico/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 420 | BUY_XP | STABILIZE | 62.0 | 7 | 7 | 0 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 421 | PASS | STABILIZE | 62.0 | 7 | 3 | 0 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 432 | PASS | ECON | 50.0 | 8 | 8 | 0 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 442 | MOVE_BENCH | ECON | 50.0 | 8 | 8 | 0 | 38.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4709305465221405 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 446 | BUY_XP | ECON | 50.0 | 8 | 13 | 1 | 44.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17800000309944153 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 447 | BUY_XP | ECON | 50.0 | 8 | 9 | 0 | 44.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09799999743700027 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 448 | BUY_XP | ECON | 50.0 | 8 | 5 | 0 | 44.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09799999743700027 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 449 | PASS | ECON | 50.0 | 8 | 1 | 0 | 44.0 | Feérico/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 457 | BUY_XP | ECON | 50.0 | 8 | 7 | 0 | 44.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09799999743700027 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 458 | PASS | ECON | 50.0 | 8 | 3 | 0 | 44.0 | Feérico/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 470 | PASS | ECON | 50.0 | 8 | 10 | 1 | 44.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 481 | EQUIP_FROM_INVENTORY | ECON | 50.0 | 8 | 17 | 1 | 44.0 | Feérico/DA_18_Rakan | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 482 | CRAFT_AND_EQUIP | ECON | 50.0 | 8 | 17 | 1 | 44.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.1899586319923401 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 483 | PASS | ECON | 50.0 | 8 | 17 | 1 | 44.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 492 | BUY_XP | ECON | 50.0 | 8 | 25 | 2 | 44.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09799999743700027 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 493 | BUY_XP | ECON | 50.0 | 8 | 21 | 2 | 44.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17800000309944153 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 494 | BUY_XP | ECON | 50.0 | 8 | 17 | 1 | 44.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09799999743700027 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 495 | BUY_XP | ECON | 50.0 | 8 | 13 | 1 | 44.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17800000309944153 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 496 | BUY_XP | ECON | 50.0 | 8 | 9 | 0 | 44.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09799999743700027 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 497 | BUY_XP | ECON | 50.0 | 8 | 5 | 0 | 44.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09799999743700027 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 498 | PASS | ECON | 50.0 | 8 | 1 | 0 | 44.0 | Feérico/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 502 | BUY_XP | STABILIZE | 33.0 | 8 | 6 | 0 | 44.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 503 | PASS | STABILIZE | 33.0 | 8 | 2 | 0 | 44.0 | Feérico/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 512 | BUY_XP | STABILIZE | 33.0 | 8 | 8 | 0 | 44.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 513 | BUY_XP | STABILIZE | 33.0 | 8 | 4 | 0 | 44.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 514 | PASS | STABILIZE | 33.0 | 8 | 0 | 0 | 44.0 | Feérico/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 522 | BUY | STABILIZE | 33.0 | 9 | 5 | 0 | 44.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005582420155405998 | 0.0 | 0.0 | +266ee11d-6e5b-4c48-8f89-769fb12dfd1a / -— |
| Jogador 6 | 5-5 | 523 | MOVE_BENCH | STABILIZE | 33.0 | 9 | 1 | 0 | 44.0 | Feérico/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.419789582490921 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 524 | PASS | STABILIZE | 33.0 | 9 | 1 | 0 | 52.0 | Feérico/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 532 | PASS | STABILIZE | 33.0 | 9 | 8 | 0 | 52.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 542 | PASS | STABILIZE | 33.0 | 9 | 14 | 1 | 52.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 552 | EQUIP_FROM_INVENTORY | STABILIZE | 33.0 | 9 | 21 | 2 | 52.0 | Feérico/DA_18_Rakan | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 553 | EQUIP_FROM_INVENTORY | STABILIZE | 33.0 | 9 | 21 | 2 | 52.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | -0.010933353565633297 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 554 | PASS | STABILIZE | 33.0 | 9 | 21 | 2 | 52.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 568 | BUY | ALL_IN | 14.0 | 9 | 28 | 2 | 52.0 | Feérico/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8100383877754211 | 0.0 | 0.0 | +559d1b79-d4c7-470c-912e-fe30541195ec / -— |
| Jogador 6 | 6-2 | 569 | BUY | ALL_IN | 14.0 | 9 | 24 | 2 | 52.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7431748509407043 | 0.0 | 0.0 | +e16e453d-d380-4b02-aaae-65f563be25e7 / -— |
| Jogador 6 | 6-2 | 570 | BUY_XP | ALL_IN | 14.0 | 9 | 20 | 2 | 52.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 571 | BUY_XP | ALL_IN | 14.0 | 9 | 16 | 1 | 52.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 572 | BUY_XP | ALL_IN | 14.0 | 9 | 12 | 1 | 52.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 573 | BUY_XP | ALL_IN | 14.0 | 9 | 8 | 0 | 52.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 574 | BUY_XP | ALL_IN | 14.0 | 9 | 4 | 0 | 52.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 575 | PASS | ALL_IN | 14.0 | 9 | 0 | 0 | 52.0 | Feérico/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.019615383818745613 | 0.0 | 0.0 | +— / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987 |
| Jogador 7 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +c2a4318c-af60-41e2-8e14-c3ad967569a0 / -— |
| Jogador 7 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.6080599427223206 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.0015799786197021604 | 0.0 | 0.0 | +b21d3fc8-71ce-4669-b0ba-931c6e11cb69 / -— |
| Jogador 7 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7486492991447449 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 26 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33987870812416077 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 27 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.9623157978057861 | 0.0 | 0.0 | +a529e9b4-89c2-47e0-b821-7269b112f8ef / -— |
| Jogador 7 | 1-2 | 28 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0123158693313599 | 0.0 | 0.0 | +— / -a529e9b4-89c2-47e0-b821-7269b112f8ef |
| Jogador 7 | 1-2 | 29 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 49 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2979022264480591 | 0.0 | 0.0 | +42edb83f-b613-45e2-95e2-d603ddf9d104 / -— |
| Jogador 7 | 1-3 | 50 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Elise | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2664298713207245 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 51 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Elise | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3240300714969635 | 0.0 | 0.0 | +— / -b21d3fc8-71ce-4669-b0ba-931c6e11cb69 |
| Jogador 7 | 1-3 | 52 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.07757808268070221 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 53 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.30986878275871277 | 0.0 | 0.0 | +734c75dd-d0f3-4b9f-abe8-a228e23557a2 / -— |
| Jogador 7 | 1-3 | 54 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40848100185394287 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 55 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_Scuttlecrab18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 77 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 104 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08322905004024506 | 0.0 | 0.0 | +42f4384d-5499-4441-aa3b-d37e50926071 / -— |
| Jogador 7 | 2-1 | 105 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5854786038398743 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 106 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0295570008456707 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 107 | PASS | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 121 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4972017705440521 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 127 | BUY_XP | STABILIZE | 100.0 | 4 | 11 | 1 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 128 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.052000001072883606 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 129 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09093416482210159 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 130 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3159113824367523 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 131 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Hecarim | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12151893973350525 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 132 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 20.0 | —/DA_18_Hecarim | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 147 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.04267248511314392 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 148 | BUY_XP | STABILIZE | 100.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 149 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.08080365508794785 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 150 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 151 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.10357164591550827 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 152 | PASS | STABILIZE | 100.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 170 | BUY | STABILIZE | 100.0 | 5 | 10 | 1 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4056612551212311 | 0.0 | 0.0 | +0c9ac713-08bd-4fa7-a94a-2ab70d7815ff / -— |
| Jogador 7 | 2-4 | 171 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 20.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2220061719417572 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 172 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 173 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03897899389266968 | 0.0 | 0.0 | +— / -42f4384d-5499-4441-aa3b-d37e50926071 |
| Jogador 7 | 2-4 | 174 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 175 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 24.0 | —/DA_Sentinel18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 190 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03200000151991844 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 191 | PASS | STABILIZE | 100.0 | 6 | 2 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 212 | BUY | STABILIZE | 100.0 | 6 | 9 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.43999508023262024 | 0.0 | 0.0 | +e2f28d51-690c-476e-b097-e5c69258f933 / -— |
| Jogador 7 | 2-6 | 213 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 6 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7885279655456543 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 214 | BUY_XP | ECON | 100.0 | 6 | 6 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 215 | MOVE_BOARD | ECON | 100.0 | 6 | 2 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.3370322287082672 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 216 | MOVE_BOARD | ECON | 100.0 | 6 | 2 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.032957449555397034 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 217 | PASS | ECON | 100.0 | 6 | 2 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 233 | BUY_XP | ECON | 100.0 | 6 | 10 | 1 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.20800000429153442 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 234 | BUY_XP | ECON | 100.0 | 6 | 6 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 235 | PASS | ECON | 100.0 | 6 | 2 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 252 | PASS | ECON | 100.0 | 6 | 9 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 273 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 19 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10453628748655319 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 274 | BUY | STABILIZE | 100.0 | 6 | 19 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.15131805837154388 | 0.0 | 0.0 | +527f78df-1e51-4731-9175-1c4812aa82ad / -— |
| Jogador 7 | 3-2 | 275 | SELL | STABILIZE | 100.0 | 6 | 16 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5164765119552612 | 0.0 | 0.0 | +— / -527f78df-1e51-4731-9175-1c4812aa82ad |
| Jogador 7 | 3-2 | 276 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 19 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17918989062309265 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 277 | BUY_XP | STABILIZE | 100.0 | 6 | 19 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 278 | BUY_XP | STABILIZE | 100.0 | 6 | 15 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 279 | BUY_XP | STABILIZE | 100.0 | 6 | 11 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 280 | BUY_XP | STABILIZE | 100.0 | 6 | 7 | 0 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06199999898672104 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 281 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 3 | 0 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 282 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 3 | 0 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 283 | PASS | STABILIZE | 100.0 | 7 | 3 | 0 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 296 | BUY | STABILIZE | 100.0 | 7 | 12 | 1 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6634483337402344 | 0.0 | 0.0 | +d056a271-6a74-4e71-bde6-087b97d2c527 / -— |
| Jogador 7 | 3-3 | 297 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 9 | 0 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5124959349632263 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 298 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 9 | 0 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.2601943612098694 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 299 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 9 | 0 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.3009292185306549 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 300 | PASS | STABILIZE | 100.0 | 7 | 9 | 0 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 312 | BUY | STABILIZE | 100.0 | 7 | 19 | 1 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7427738308906555 | 0.0 | 0.0 | +06db3a99-d008-406a-ac86-30884335d7c2 / -— |
| Jogador 7 | 3-4 | 313 | BUY | STABILIZE | 100.0 | 7 | 16 | 1 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26917046308517456 | 0.0 | 0.0 | +9443e3b5-f0a2-4ab7-8378-907a3d2bccaa / -— |
| Jogador 7 | 3-4 | 314 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 12 | 1 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 315 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 12 | 1 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 316 | PASS | STABILIZE | 100.0 | 7 | 12 | 1 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 330 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 21 | 2 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028333866968750954 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 331 | SELL | STABILIZE | 100.0 | 7 | 21 | 2 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7110646367073059 | 0.0 | 0.0 | +— / -06db3a99-d008-406a-ac86-30884335d7c2 |
| Jogador 7 | 3-5 | 332 | BUY | STABILIZE | 100.0 | 7 | 24 | 2 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2932626008987427 | 0.0 | 0.0 | +a23ee552-279e-4c6c-aa05-6197043e8f1d / -— |
| Jogador 7 | 3-5 | 333 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 21 | 2 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 334 | SELL | STABILIZE | 100.0 | 7 | 21 | 2 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5728461742401123 | 0.0 | 0.0 | +— / -a23ee552-279e-4c6c-aa05-6197043e8f1d |
| Jogador 7 | 3-5 | 335 | SELL | STABILIZE | 100.0 | 7 | 24 | 2 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2976153790950775 | 0.0 | 0.0 | +— / -9443e3b5-f0a2-4ab7-8378-907a3d2bccaa |
| Jogador 7 | 3-5 | 336 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 28 | 2 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 337 | PASS | STABILIZE | 100.0 | 7 | 28 | 2 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 342 | BUY | FAST8 | 88.0 | 7 | 35 | 3 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.710996150970459 | 0.0 | 0.0 | +112206a4-c285-4f76-878a-056248cba468 / -— |
| Jogador 7 | 3-6 | 343 | BUY | FAST8 | 88.0 | 7 | 31 | 3 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.098208487033844 | 0.0 | 0.0 | +3625f791-4c9f-4b95-bdf7-4a322dcd55d3 / -— |
| Jogador 7 | 3-6 | 344 | BUY | STABILIZE | 88.0 | 7 | 27 | 2 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26037925481796265 | 0.0 | 0.0 | +a14e4b8f-77c5-4909-a9ee-0044b836a877 / -— |
| Jogador 7 | 3-6 | 345 | MOVE_BENCH | STABILIZE | 88.0 | 7 | 23 | 2 | 36.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3085315227508545 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 346 | BUY | STABILIZE | 88.0 | 7 | 23 | 2 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6570584774017334 | 0.0 | 0.0 | +014c92c3-e588-4e8b-b4bd-93cee45d74af / -— |
| Jogador 7 | 3-6 | 347 | MOVE_BOARD | STABILIZE | 88.0 | 7 | 19 | 1 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 348 | MOVE_BOARD | STABILIZE | 88.0 | 7 | 19 | 1 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1799452304840088 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 349 | BUY_XP | STABILIZE | 88.0 | 7 | 19 | 1 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 350 | BUY_XP | STABILIZE | 88.0 | 7 | 15 | 1 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 351 | BUY_XP | STABILIZE | 88.0 | 7 | 11 | 1 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 352 | PASS | STABILIZE | 88.0 | 7 | 7 | 0 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 362 | BUY | STABILIZE | 88.0 | 7 | 13 | 1 | 38.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7519978284835815 | 0.0 | 0.0 | +1e81ac95-667f-494d-89eb-2bcdcf887a7e / -0c9ac713-08bd-4fa7-a94a-2ab70d7815ff,112206a4-c285-4f76-878a-056248cba468 |
| Jogador 7 | 3-7 | 363 | BUY | STABILIZE | 88.0 | 7 | 9 | 0 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.261684387922287 | 0.0 | 0.0 | +b2a77bec-e150-4d98-847c-9f2cfb50cbe7 / -— |
| Jogador 7 | 3-7 | 364 | BUY | STABILIZE | 88.0 | 7 | 6 | 0 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7055158019065857 | 0.0 | 0.0 | +88035b70-61e0-4279-9d55-e451f412f0d3 / -— |
| Jogador 7 | 3-7 | 365 | BUY | STABILIZE | 88.0 | 7 | 4 | 0 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10518646240234375 | 0.0 | 0.0 | +2faa526c-d29e-47a9-9eb3-5030750cb483 / -— |
| Jogador 7 | 3-7 | 366 | MOVE_BENCH | STABILIZE | 88.0 | 7 | 2 | 0 | 30.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11620543897151947 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 367 | MOVE_BOARD | STABILIZE | 88.0 | 7 | 2 | 0 | 34.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 368 | PASS | STABILIZE | 88.0 | 7 | 2 | 0 | 34.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 382 | REROLL | STABILIZE | 88.0 | 7 | 7 | 0 | 34.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 383 | REROLL | STABILIZE | 88.0 | 7 | 5 | 0 | 34.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 384 | REROLL | STABILIZE | 88.0 | 7 | 3 | 0 | 34.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 385 | MOVE_BOARD | STABILIZE | 88.0 | 7 | 1 | 0 | 34.0 | Vanguarda/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04875248298048973 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 386 | MOVE_BOARD | STABILIZE | 88.0 | 7 | 1 | 0 | 34.0 | Vanguarda/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 387 | MOVE_BOARD | STABILIZE | 88.0 | 7 | 1 | 0 | 34.0 | Vanguarda/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 388 | PASS | STABILIZE | 88.0 | 7 | 1 | 0 | 34.0 | Vanguarda/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 402 | BUY | STABILIZE | 75.0 | 7 | 6 | 0 | 34.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06400240957736969 | 0.0 | 0.0 | +a2b57772-7a23-4ffd-ace1-d2a7a3f5a7cd / -— |
| Jogador 7 | 4-2 | 403 | REROLL | STABILIZE | 75.0 | 7 | 2 | 0 | 34.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 404 | PASS | STABILIZE | 75.0 | 7 | 0 | 0 | 34.0 | Vanguarda/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 420 | BUY | STABILIZE | 61.0 | 7 | 6 | 0 | 34.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8347761034965515 | 0.0 | 0.0 | +fcc4f620-7b85-40ed-a42c-2eadd37a82fd / -734c75dd-d0f3-4b9f-abe8-a228e23557a2,88035b70-61e0-4279-9d55-e451f412f0d3 |
| Jogador 7 | 4-3 | 421 | BUY | STABILIZE | 61.0 | 7 | 4 | 0 | 26.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22645631432533264 | 0.0 | 0.0 | +111acae7-a889-409f-a15e-419d250fccd0 / -— |
| Jogador 7 | 4-3 | 422 | PASS | STABILIZE | 61.0 | 7 | 0 | 0 | 26.0 | Vanguarda/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 432 | BUY | STABILIZE | 48.0 | 7 | 6 | 0 | 32.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0770954117178917 | 0.0 | 0.0 | +6e1d8af0-7f7c-4ec1-967c-e871072bc4e3 / -— |
| Jogador 7 | 4-4 | 433 | PASS | STABILIZE | 48.0 | 7 | 1 | 0 | 32.0 | Vanguarda/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 442 | MOVE_BENCH | STABILIZE | 48.0 | 7 | 1 | 0 | 32.0 | Vanguarda/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2789232134819031 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 446 | BUY | STABILIZE | 48.0 | 7 | 7 | 0 | 42.0 | Vanguarda/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22136180102825165 | 0.0 | 0.0 | +04520fe5-4449-4632-b275-e5e28d642007 / -— |
| Jogador 7 | 4-5 | 447 | REROLL | STABILIZE | 48.0 | 7 | 4 | 0 | 42.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 448 | REROLL | STABILIZE | 48.0 | 7 | 2 | 0 | 42.0 | Vanguarda/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 449 | PASS | STABILIZE | 48.0 | 7 | 0 | 0 | 42.0 | Vanguarda/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 457 | REROLL | STABILIZE | 37.0 | 7 | 6 | 0 | 42.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 458 | REROLL | STABILIZE | 37.0 | 7 | 4 | 0 | 42.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 459 | REROLL | STABILIZE | 37.0 | 7 | 2 | 0 | 42.0 | Vanguarda/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 460 | PASS | STABILIZE | 37.0 | 7 | 0 | 0 | 42.0 | Vanguarda/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 470 | REROLL | STABILIZE | 25.0 | 7 | 7 | 0 | 42.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017219500616192818 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 471 | REROLL | STABILIZE | 25.0 | 7 | 5 | 0 | 42.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010817804373800755 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 472 | REROLL | STABILIZE | 25.0 | 7 | 3 | 0 | 42.0 | Vanguarda/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01709691993892193 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 473 | PASS | STABILIZE | 25.0 | 7 | 1 | 0 | 42.0 | Vanguarda/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 481 | EQUIP_FROM_INVENTORY | STABILIZE | 25.0 | 7 | 8 | 0 | 42.0 | Vanguarda/DA_Sentinel18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 482 | REROLL | STABILIZE | 25.0 | 7 | 8 | 0 | 42.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.010742723010480404 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 483 | REROLL | STABILIZE | 25.0 | 7 | 6 | 0 | 42.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.010921156965196133 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 484 | REROLL | STABILIZE | 25.0 | 7 | 4 | 0 | 42.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.011446098797023296 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 485 | REROLL | STABILIZE | 25.0 | 7 | 2 | 0 | 42.0 | Vanguarda/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 486 | PASS | STABILIZE | 25.0 | 7 | 0 | 0 | 42.0 | Vanguarda/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 492 | REROLL | ALL_IN | 10.0 | 7 | 8 | 0 | 42.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.01013689860701561 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 493 | PASS | ALL_IN | 10.0 | 7 | 6 | 0 | 42.0 | Vanguarda/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 502 | PASS | ALL_IN | 0.0 | 7 | 6 | 0 | 0.0 | Vanguarda/DA_Sentinel18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 512 | PASS | ALL_IN | 0.0 | 7 | 6 | 0 | 0.0 | Vanguarda/DA_Sentinel18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 522 | PASS | ALL_IN | 0.0 | 7 | 6 | 0 | 0.0 | Vanguarda/DA_Sentinel18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 532 | PASS | ALL_IN | 0.0 | 7 | 6 | 0 | 0.0 | Vanguarda/DA_Sentinel18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 542 | PASS | ALL_IN | 0.0 | 7 | 6 | 0 | 0.0 | Vanguarda/DA_Sentinel18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 552 | PASS | ALL_IN | 0.0 | 7 | 6 | 0 | 0.0 | Vanguarda/DA_Sentinel18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 568 | PASS | ALL_IN | 0.0 | 7 | 6 | 0 | 0.0 | Vanguarda/DA_Sentinel18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 17 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.28737619519233704 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.054392240941524506 | 0.0 | 0.0 | +fddba3f3-87f3-4c97-a7b2-e5d1ef789709 / -— |
| Jogador 8 | 1-2 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37020111083984375 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 26 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.948853611946106 | 0.0 | 0.0 | +78019889-2624-4adb-917b-619681f23053 / -— |
| Jogador 8 | 1-2 | 27 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47183793783187866 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 28 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 49 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 77 | BUY_XP | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.052000001072883606 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 78 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.036966722458601 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 79 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 104 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.116906762123108 | 0.0 | 0.0 | +630d9254-3856-4d88-b981-43a8270b4b3d / -78019889-2624-4adb-917b-619681f23053,fddba3f3-87f3-4c97-a7b2-e5d1ef789709 |
| Jogador 8 | 2-1 | 105 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 2.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41998085379600525 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 106 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.029513126239180565 | 0.0 | 0.0 | +a524fad3-c7d3-4fa7-9c62-1803c8e7c865 / -— |
| Jogador 8 | 2-1 | 107 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8817939758300781 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 108 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39971181750297546 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 109 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.16431555151939392 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 110 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.14565446972846985 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 111 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 127 | BUY | STABILIZE | 94.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.006002536043524742 | 0.0 | 0.0 | +4b4cc4ba-04a0-4e04-88f2-e6913a342285 / -— |
| Jogador 8 | 2-2 | 128 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4590277373790741 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 129 | BUY_XP | STABILIZE | 94.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03200000151991844 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 130 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Leona | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 131 | PASS | STABILIZE | 94.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Leona | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 147 | BUY | STABILIZE | 94.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.033804286271333694 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 148 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 3 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30873557925224304 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 149 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 3 | 0 | 22.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.12860406935214996 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 150 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 3 | 0 | 22.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1756042242050171 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 151 | BUY | STABILIZE | 94.0 | 5 | 3 | 0 | 22.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.10751637071371078 | 0.0 | 0.0 | +5de56114-806a-4f58-8241-b3b8434a2154 / -— |
| Jogador 8 | 2-3 | 152 | SELL | STABILIZE | 94.0 | 5 | 1 | 0 | 22.0 | —/DA_18_Leona | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19792307913303375 | 0.0 | 0.0 | +— / -5de56114-806a-4f58-8241-b3b8434a2154 |
| Jogador 8 | 2-3 | 153 | REROLL | STABILIZE | 94.0 | 5 | 3 | 0 | 22.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.07400000095367432 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 154 | BUY | STABILIZE | 94.0 | 5 | 1 | 0 | 22.0 | —/DA_18_Leona | BUY, MOVE_BOARD, PASS | True | True | 0.344673752784729 | 0.0 | 0.0 | +ce928be1-b3ba-4640-b93c-d15c8a92833e / -— |
| Jogador 8 | 2-3 | 155 | SELL | STABILIZE | 94.0 | 5 | 0 | 0 | 22.0 | —/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39467376470565796 | 0.0 | 0.0 | +— / -ce928be1-b3ba-4640-b93c-d15c8a92833e |
| Jogador 8 | 2-3 | 156 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 1 | 0 | 22.0 | —/DA_18_Leona | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 157 | PASS | STABILIZE | 94.0 | 5 | 1 | 0 | 22.0 | —/DA_18_Leona | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 170 | BUY | STABILIZE | 88.0 | 5 | 6 | 0 | 22.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.39329373836517334 | 0.0 | 0.0 | +6a071ec5-c3f4-41b3-a0d8-c1aee62cffee / -— |
| Jogador 8 | 2-4 | 171 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 3 | 0 | 22.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07919561117887497 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 172 | SELL | STABILIZE | 88.0 | 5 | 3 | 0 | 22.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002230769256129861 | 0.0 | 0.0 | +— / -b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 8 | 2-4 | 173 | BUY_XP | STABILIZE | 88.0 | 5 | 6 | 0 | 22.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 174 | PASS | STABILIZE | 88.0 | 5 | 2 | 0 | 22.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 190 | BUY | STABILIZE | 88.0 | 5 | 7 | 0 | 22.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.46385955810546875 | 0.0 | 0.0 | +14bbd76c-fca8-4017-89b5-e586bb1cae70 / -— |
| Jogador 8 | 2-5 | 191 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 4 | 0 | 22.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39139193296432495 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 192 | SELL | STABILIZE | 88.0 | 5 | 4 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38723769783973694 | 0.0 | 0.0 | +— / -630d9254-3856-4d88-b981-43a8270b4b3d |
| Jogador 8 | 2-5 | 193 | PASS | STABILIZE | 88.0 | 5 | 7 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 212 | BUY | STABILIZE | 88.0 | 5 | 13 | 1 | 24.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.967004120349884 | 0.0 | 0.0 | +764470bb-9820-4e49-98f9-5a5f0ce5ca8f / -— |
| Jogador 8 | 2-6 | 213 | SELL | STABILIZE | 88.0 | 5 | 10 | 1 | 24.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.017004132270813 | 0.0 | 0.0 | +— / -764470bb-9820-4e49-98f9-5a5f0ce5ca8f |
| Jogador 8 | 2-6 | 214 | BUY_XP | STABILIZE | 88.0 | 5 | 13 | 1 | 24.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 215 | BUY_XP | STABILIZE | 88.0 | 5 | 9 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03200000151991844 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 216 | BUY | STABILIZE | 88.0 | 6 | 5 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.369687020778656 | 0.0 | 0.0 | +3d4fca52-8f58-4464-8cec-752fa99dbb3c / -— |
| Jogador 8 | 2-6 | 217 | PASS | STABILIZE | 88.0 | 6 | 2 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 231 | MOVE_BENCH | STABILIZE | 88.0 | 6 | 2 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4506770074367523 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 233 | BUY | ECON | 82.0 | 6 | 7 | 0 | 30.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.37602269649505615 | 0.0 | 0.0 | +cf421cf5-8e22-4dd1-8aa5-5cb3bda86c88 / -— |
| Jogador 8 | 2-7 | 234 | BUY | ECON | 82.0 | 6 | 3 | 0 | 30.0 | —/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23543453216552734 | 0.0 | 0.0 | +31aa0a5f-4d66-48c2-b6d4-b76ac220c752 / -— |
| Jogador 8 | 2-7 | 235 | MOVE_BENCH | ECON | 82.0 | 6 | 1 | 0 | 30.0 | —/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21406346559524536 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 236 | PASS | ECON | 82.0 | 6 | 1 | 0 | 32.0 | —/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 252 | MOVE_BENCH | ECON | 82.0 | 6 | 6 | 0 | 32.0 | —/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10864600539207458 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 253 | BUY_XP | ECON | 82.0 | 6 | 6 | 0 | 36.0 | —/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09799999743700027 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 254 | PASS | ECON | 82.0 | 6 | 2 | 0 | 36.0 | Feérico/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 273 | BUY_XP | STABILIZE | 72.0 | 6 | 8 | 0 | 36.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 274 | BUY_XP | STABILIZE | 72.0 | 6 | 4 | 0 | 36.0 | Feérico/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 275 | SELL | STABILIZE | 72.0 | 6 | 0 | 0 | 36.0 | Feérico/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02777967043220997 | 0.0 | 0.0 | +— / -31aa0a5f-4d66-48c2-b6d4-b76ac220c752 |
| Jogador 8 | 3-2 | 276 | SELL | STABILIZE | 72.0 | 6 | 2 | 0 | 36.0 | Feérico/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3959014117717743 | 0.0 | 0.0 | +— / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02 |
| Jogador 8 | 3-2 | 277 | PASS | STABILIZE | 72.0 | 6 | 3 | 0 | 36.0 | Vivaz/DA_18_Lillia | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 296 | PASS | STABILIZE | 72.0 | 6 | 9 | 0 | 36.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 312 | PASS | STABILIZE | 59.0 | 6 | 14 | 1 | 36.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 330 | BUY | STABILIZE | 59.0 | 6 | 20 | 2 | 36.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.02581390179693699 | 0.0 | 0.0 | +68d2cec6-d29b-4173-a696-ac20ccb1f079 / -— |
| Jogador 8 | 3-5 | 331 | BUY | STABILIZE | 59.0 | 6 | 16 | 1 | 36.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19955097138881683 | 0.0 | 0.0 | +7306c9be-466e-498c-819e-274ff070c72b / -— |
| Jogador 8 | 3-5 | 332 | MOVE_BENCH | STABILIZE | 59.0 | 6 | 13 | 1 | 36.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3484026789665222 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 333 | MOVE_BENCH | STABILIZE | 59.0 | 6 | 13 | 1 | 36.0 | Vivaz/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2741503119468689 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 334 | PASS | STABILIZE | 59.0 | 6 | 13 | 1 | 38.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 342 | MOVE_BENCH | STABILIZE | 47.0 | 6 | 20 | 2 | 38.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05355466157197952 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 343 | MOVE_BENCH | STABILIZE | 47.0 | 6 | 20 | 2 | 36.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22052952647209167 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 344 | BUY_XP | STABILIZE | 47.0 | 6 | 20 | 2 | 38.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 345 | BUY_XP | STABILIZE | 47.0 | 6 | 16 | 1 | 38.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 346 | BUY_XP | STABILIZE | 47.0 | 6 | 12 | 1 | 38.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03400000184774399 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 347 | MOVE_BENCH | STABILIZE | 47.0 | 7 | 8 | 0 | 38.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5104473829269409 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 348 | BUY_XP | STABILIZE | 47.0 | 7 | 8 | 0 | 44.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 349 | BUY_XP | STABILIZE | 47.0 | 7 | 4 | 0 | 44.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 350 | PASS | STABILIZE | 47.0 | 7 | 0 | 0 | 44.0 | Vivaz/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 362 | BUY_XP | STABILIZE | 35.0 | 7 | 6 | 0 | 44.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 363 | PASS | STABILIZE | 35.0 | 7 | 2 | 0 | 44.0 | Vivaz/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 382 | CRAFT_AND_EQUIP | STABILIZE | 35.0 | 7 | 8 | 0 | 44.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12226126343011856 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 383 | BUY_XP | STABILIZE | 35.0 | 7 | 8 | 0 | 44.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 384 | BUY_XP | STABILIZE | 35.0 | 7 | 4 | 0 | 44.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 385 | PASS | STABILIZE | 35.0 | 7 | 0 | 0 | 44.0 | Vivaz/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 402 | BUY_XP | STABILIZE | 35.0 | 7 | 6 | 0 | 44.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 403 | PASS | STABILIZE | 35.0 | 7 | 2 | 0 | 44.0 | Vivaz/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 420 | BUY_XP | STABILIZE | 35.0 | 7 | 9 | 0 | 44.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 421 | BUY_XP | STABILIZE | 35.0 | 7 | 5 | 0 | 44.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 422 | PASS | STABILIZE | 35.0 | 7 | 1 | 0 | 44.0 | Vivaz/DA_18_Lillia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 432 | PASS | STABILIZE | 35.0 | 7 | 8 | 0 | 44.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 446 | BUY_XP | STABILIZE | 35.0 | 7 | 14 | 1 | 44.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 447 | BUY_XP | STABILIZE | 35.0 | 7 | 10 | 1 | 44.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 448 | BUY_XP | STABILIZE | 35.0 | 7 | 6 | 0 | 44.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07443749904632568 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 449 | PASS | STABILIZE | 35.0 | 8 | 2 | 0 | 44.0 | Vivaz/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 453 | MOVE_BENCH | STABILIZE | 35.0 | 8 | 2 | 0 | 44.0 | Vivaz/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46764856576919556 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 457 | PASS | STABILIZE | 22.0 | 8 | 7 | 0 | 50.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 470 | BUY | STABILIZE | 22.0 | 8 | 13 | 1 | 50.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.23248286545276642 | 0.0 | 0.0 | +dcb61be2-9a58-49bc-9f11-2f5fce42e7ea / -— |
| Jogador 8 | 4-7 | 471 | BUY | STABILIZE | 22.0 | 8 | 8 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08059524744749069 | 0.0 | 0.0 | +8756c125-e3d6-4f40-80d2-a6bf20e7b1c7 / -— |
| Jogador 8 | 4-7 | 472 | REROLL | STABILIZE | 22.0 | 8 | 4 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012908756732940674 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 473 | REROLL | STABILIZE | 22.0 | 8 | 2 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 474 | PASS | STABILIZE | 22.0 | 8 | 0 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 481 | EQUIP_FROM_INVENTORY | STABILIZE | 22.0 | 8 | 5 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 482 | BUY | STABILIZE | 22.0 | 8 | 5 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7316752672195435 | 0.0 | 0.0 | +ae9da355-52b7-402c-be6e-41fa1148a550 / -— |
| Jogador 8 | 5-1 | 483 | PASS | STABILIZE | 22.0 | 8 | 2 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 492 | BUY_XP | STABILIZE | 22.0 | 8 | 9 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 493 | BUY_XP | STABILIZE | 22.0 | 8 | 5 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 494 | PASS | STABILIZE | 22.0 | 8 | 1 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 502 | BUY | STABILIZE | 22.0 | 8 | 8 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006222694180905819 | 0.0 | 0.0 | +6559ddb9-ba21-4084-9a25-7c9179a347dd / -— |
| Jogador 8 | 5-3 | 503 | REROLL | STABILIZE | 22.0 | 8 | 4 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017388910055160522 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 504 | REROLL | STABILIZE | 22.0 | 8 | 2 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 505 | PASS | STABILIZE | 22.0 | 8 | 0 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 512 | REROLL | STABILIZE | 22.0 | 8 | 6 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010614673607051373 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 513 | REROLL | STABILIZE | 22.0 | 8 | 4 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01737617328763008 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 514 | BUY | STABILIZE | 22.0 | 8 | 2 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17736327648162842 | 0.0 | 0.0 | +b1e222db-5292-4836-a0b4-2fe583bea359 / -— |
| Jogador 8 | 5-4 | 515 | PASS | STABILIZE | 22.0 | 8 | 1 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 522 | BUY | STABILIZE | 22.0 | 8 | 7 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7355079054832458 | 0.0 | 0.0 | +77742642-57e8-4594-8bb9-5b2e80a86ba1 / -— |
| Jogador 8 | 5-5 | 523 | REROLL | STABILIZE | 22.0 | 8 | 3 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017275076359510422 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 524 | PASS | STABILIZE | 22.0 | 8 | 1 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 532 | BUY | ALL_IN | 3.0 | 8 | 6 | 0 | 50.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.823727548122406 | 0.0 | 0.0 | +0af3def4-348c-47c9-aab3-11618b91e680 / -7306c9be-466e-498c-819e-274ff070c72b,ae9da355-52b7-402c-be6e-41fa1148a550 |
| Jogador 8 | 5-6 | 533 | BUY | ALL_IN | 3.0 | 8 | 3 | 0 | 44.0 | Vivaz/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04853413999080658 | 0.0 | 0.0 | +a1fb8708-db9f-4fa9-96ad-39fe485a9dc5 / -— |
| Jogador 8 | 5-6 | 534 | PASS | ALL_IN | 3.0 | 8 | 1 | 0 | 44.0 | Vivaz/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 542 | PASS | ALL_IN | 0.0 | 8 | 1 | 0 | 0.0 | Vivaz/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 552 | PASS | ALL_IN | 0.0 | 8 | 1 | 0 | 0.0 | Vivaz/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 568 | PASS | ALL_IN | 0.0 | 8 | 1 | 0 | 0.0 | Vivaz/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 159 | 160 | 21 | 14 | 12 | 2 | 9 | 3 | 1 | 0.0 |
- Jogador 1 — gasto por ação: BUY: 78g, BUY_XP: 64g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 18g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 12g, stage 2: 49g, stage 3: 50g, stage 4: 43g, stage 5: 6g, stage 6: 0g
| Jogador 2 | 118 | 151 | 3 | 7 | 23 | 2 | 5 | 1 | 0 | 0.0 |
- Jogador 2 — gasto por ação: BUY: 33g, BUY_XP: 108g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 10g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 9g, stage 2: 41g, stage 3: 35g, stage 4: 48g, stage 5: 18g, stage 6: 0g
| Jogador 3 | 142 | 206 | 14 | 13 | 33 | 1 | 2 | 0 | 10 | 62.0 |
- Jogador 3 — gasto por ação: BUY: 54g, BUY_XP: 148g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 4g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 2g, stage 2: 45g, stage 3: 50g, stage 4: 42g, stage 5: 55g, stage 6: 12g
| Jogador 4 | 149 | 200 | 24 | 8 | 28 | 1 | 8 | 5 | 1 | 0.0 |
- Jogador 4 — gasto por ação: BUY: 56g, BUY_XP: 128g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 16g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 7g, stage 2: 50g, stage 3: 50g, stage 4: 62g, stage 5: 31g, stage 6: 0g
| Jogador 5 | 144 | 152 | 21 | 7 | 9 | 2 | 15 | 3 | 0 | 0.0 |
- Jogador 5 — gasto por ação: BUY: 78g, BUY_XP: 44g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 30g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 2g, stage 2: 57g, stage 3: 44g, stage 4: 39g, stage 5: 10g, stage 6: 0g
| Jogador 6 | 156 | 213 | 16 | 10 | 38 | 0 | 0 | 0 | 0 | 52.0 |
- Jogador 6 — gasto por ação: BUY: 53g, BUY_XP: 160g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 7g, stage 2: 29g, stage 3: 73g, stage 4: 36g, stage 5: 40g, stage 6: 28g
| Jogador 7 | 143 | 178 | 18 | 9 | 13 | 2 | 17 | 6 | 6 | 0.0 |
- Jogador 7 — gasto por ação: BUY: 80g, BUY_XP: 64g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 34g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 7g, stage 2: 48g, stage 3: 71g, stage 4: 42g, stage 5: 10g, stage 6: 0g
| Jogador 8 | 125 | 177 | 15 | 6 | 19 | 4 | 8 | 3 | 1 | 0.0 |
- Jogador 8 — gasto por ação: BUY: 65g, BUY_XP: 96g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 16g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 6g, stage 2: 48g, stage 3: 43g, stage 4: 45g, stage 5: 35g, stage 6: 0g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 1 | 1 | 0 | 0.0% |
| Jogador 2 | 1 | 1 | 0 | 0.0% |
| Jogador 3 | 2 | 2 | 0 | 0.0% |
| Jogador 5 | 1 | 1 | 0 | 0.0% |
| Jogador 6 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 2 | 1 | 1 | 50.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ médio qualidade | Δ estrutural médio | Δ qualidade quando combate positivo | Δ qualidade quando combate negativo |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 159 | 0 | 0 | 159 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ 0.0000 (33 ações), BUY_XP: Δ 0.0000 (16 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (23 ações), MOVE_BOARD: Δ 0.0000 (28 ações), PASS: Δ 0.0000 (34 ações), REROLL: Δ 0.0000 (9 ações), SELL: Δ 0.0000 (14 ações)
| Jogador 2 | 118 | 0 | 0 | 118 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ 0.0000 (12 ações), BUY_XP: Δ 0.0000 (27 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (30 ações), MOVE_BOARD: Δ 0.0000 (5 ações), PASS: Δ 0.0000 (34 ações), REROLL: Δ 0.0000 (5 ações), SELL: Δ 0.0000 (3 ações)
| Jogador 3 | 142 | 0 | 0 | 142 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ 0.0000 (19 ações), BUY_XP: Δ 0.0000 (37 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0000 (22 ações), MOVE_BOARD: Δ 0.0000 (18 ações), PASS: Δ 0.0000 (33 ações), REROLL: Δ 0.0000 (2 ações), SELL: Δ 0.0000 (7 ações)
| Jogador 4 | 149 | 0 | 0 | 149 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ 0.0000 (20 ações), BUY_XP: Δ 0.0000 (32 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (14 ações), MOVE_BOARD: Δ 0.0000 (30 ações), PASS: Δ 0.0000 (33 ações), REROLL: Δ 0.0000 (8 ações), SELL: Δ 0.0000 (10 ações)
| Jogador 5 | 144 | 0 | 0 | 144 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ 0.0000 (31 ações), BUY_XP: Δ 0.0000 (11 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (15 ações), MOVE_BOARD: Δ 0.0000 (25 ações), PASS: Δ 0.0000 (34 ações), REROLL: Δ 0.0000 (15 ações), SELL: Δ 0.0000 (12 ações)
| Jogador 6 | 156 | 0 | 0 | 156 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ 0.0000 (22 ações), BUY_XP: Δ 0.0000 (40 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0000 (31 ações), MOVE_BOARD: Δ 0.0000 (16 ações), PASS: Δ 0.0000 (34 ações), SELL: Δ 0.0000 (9 ações)
| Jogador 7 | 143 | 0 | 0 | 143 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ 0.0000 (27 ações), BUY_XP: Δ 0.0000 (16 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (15 ações), MOVE_BOARD: Δ 0.0000 (25 ações), PASS: Δ 0.0000 (34 ações), REROLL: Δ 0.0000 (17 ações), SELL: Δ 0.0000 (8 ações)
| Jogador 8 | 125 | 0 | 0 | 125 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ 0.0000 (24 ações), BUY_XP: Δ 0.0000 (24 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (19 ações), MOVE_BOARD: Δ 0.0000 (7 ações), PASS: Δ 0.0000 (34 ações), REROLL: Δ 0.0000 (8 ações), SELL: Δ 0.0000 (7 ações)

A pontuação é uma heurística para auditoria, não uma verdade absoluta. Compare-a com recompensas e resultados de combate; correlação não prova causalidade.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 1 | 1-2 | 10 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 3 | 3 → 3 | 0.068 | 0.000 |
| Jogador 1 | 1-3 | 4 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 5 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 1 | 1-4 | 11 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 5 → 5 | 7 | 3 → 4 | 0.000 | 0.000 |
| Jogador 1 | 2-1 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 11% → 14% | 5 → 10 | 1 | 4 → 4 | -0.017 | 0.502 |
| Jogador 1 | 2-2 | 9 | 4.000 | 0.000 | 0 → 0 | 1 → 0 | 14% → 14% | 10 → 15 | 3 | 4 → 4 | 0.010 | 0.264 |
| Jogador 1 | 2-3 | 12 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 18% | 15 → 7 | 16 | 4 → 5 | -0.058 | 0.224 |
| Jogador 1 | 2-4 | 5 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 7 → 13 | 0 | 5 → 5 | 0.044 | 0.000 |
| Jogador 1 | 2-5 | 5 | -2.000 | 6.000 | 0 → 0 | 0 → 1 | 18% → 18% | 13 → 17 | 2 | 5 → 5 | 0.011 | -0.496 |
| Jogador 1 | 2-6 | 12 | 10.000 | -4.000 | 0 → 0 | 1 → 1 | 18% → 21% | 17 → 12 | 15 | 5 → 6 | 0.008 | -0.207 |
| Jogador 1 | 2-7 | 7 | 0.000 | -2.000 | 0 → 0 | 1 → 1 | 21% → 21% | 12 → 7 | 12 | 6 → 6 | -0.031 | 0.000 |
| Jogador 1 | 3-1 | 6 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 7 → 9 | 7 | 6 → 6 | 0.007 | -0.454 |
| Jogador 1 | 3-2 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 9 → 16 | 0 | 6 → 6 | 0.006 | 0.562 |
| Jogador 1 | 3-3 | 11 | 2.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 16 → 10 | 15 | 6 → 7 | 0.064 | 0.256 |
| Jogador 1 | 3-4 | 12 | 6.000 | 0.000 | 0 → 1 | 1 → 1 | 21% → 21% | 10 → 11 | 7 | 7 → 7 | -0.003 | 0.000 |
| Jogador 1 | 3-5 | 6 | 4.000 | 0.000 | 1 → 1 | 1 → 1 | 21% → 25% | 11 → 14 | 2 | 7 → 7 | -0.111 | -0.423 |
| Jogador 1 | 3-6 | 11 | 2.000 | 0.000 | 1 → 1 | 1 → 2 | 25% → 25% | 14 → 7 | 14 | 7 → 7 | 0.006 | -0.231 |
| Jogador 1 | 3-7 | 4 | 4.000 | 6.000 | 1 → 1 | 2 → 2 | 25% → 25% | 7 → 8 | 5 | 7 → 7 | -0.072 | 0.000 |
| Jogador 1 | 4-1 | 4 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 25% → 25% | 8 → 11 | 3 | 7 → 7 | 0.000 | -0.666 |
| Jogador 1 | 4-2 | 3 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 25% → 25% | 11 → 14 | 3 | 7 → 7 | 0.000 | -0.888 |
| Jogador 1 | 4-3 | 2 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 25% → 25% | 14 → 21 | 0 | 7 → 7 | 0.000 | 1.468 |
| Jogador 1 | 4-4 | 3 | 0.000 | 6.000 | 1 → 1 | 3 → 3 | 25% → 25% | 21 → 24 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 4-5 | 9 | -6.000 | 32.000 | 1 → 1 | 3 → 3 | 25% → 21% | 24 → 11 | 18 | 7 → 7 | 0.010 | -0.307 |
| Jogador 1 | 4-6 | 4 | 6.000 | 0.000 | 1 → 1 | 3 → 3 | 21% → 25% | 11 → 14 | 3 | 7 → 7 | 0.054 | -0.679 |
| Jogador 1 | 4-7 | 8 | 0.000 | 6.000 | 1 → 1 | 3 → 3 | 25% → 25% | 14 → 7 | 13 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 5-1 | 6 | -44.000 | -62.000 | 1 → 0 | 3 → 0 | 25% → 0% | 7 → 1 | 6 | 7 → 7 | -0.008 | -0.475 |
| Jogador 1 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 1 → 1 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 1 → 1 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 1 → 1 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 1 → 1 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 1 → 1 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 1 → 1 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 1 → 1 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 1 → 1 | 0 | 7 → 7 | 0.000 | 0.000 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 7, COMPOSITION_COMPATIBILITY: 15, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 9; mudanças de composição: 0; posicionamento melhorou em 23 ações e piorou em 22.
- Jogador 1 — estado final: ouro 1, nível 7, vida 0.0, colocação 8.
| Jogador 2 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.067 | 0.000 |
| Jogador 2 | 1-2 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | -0.029 | 0.000 |
| Jogador 2 | 1-3 | 6 | 2.000 | 0.000 | 0 → 0 | 1 → 0 | 7% → 7% | 3 → 5 | 2 | 3 → 3 | 0.044 | 0.000 |
| Jogador 2 | 1-4 | 6 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 7% → 11% | 5 → 4 | 5 | 3 → 4 | -0.017 | 0.000 |
| Jogador 2 | 2-1 | 5 | 4.000 | 0.000 | 0 → 0 | 1 → 0 | 11% → 11% | 4 → 8 | 3 | 4 → 4 | 0.000 | 0.476 |
| Jogador 2 | 2-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 8 → 13 | 0 | 4 → 4 | 0.000 | -1.130 |
| Jogador 2 | 2-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 13 → 20 | 0 | 4 → 5 | 0.000 | -1.265 |
| Jogador 2 | 2-4 | 8 | 6.000 | 6.000 | 0 → 0 | 0 → 0 | 11% → 14% | 20 → 21 | 6 | 5 → 5 | -0.016 | 0.000 |
| Jogador 2 | 2-5 | 11 | 6.000 | -6.000 | 0 → 0 | 0 → 0 | 14% → 18% | 21 → 7 | 20 | 5 → 6 | 0.018 | 0.224 |
| Jogador 2 | 2-6 | 5 | 8.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 21% | 7 → 10 | 4 | 6 → 6 | -0.014 | 0.551 |
| Jogador 2 | 2-7 | 4 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 10 → 8 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 3-1 | 4 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 8 → 5 | 8 | 6 → 6 | 0.000 | -0.646 |
| Jogador 2 | 3-2 | 3 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 5 → 7 | 4 | 6 → 6 | 0.000 | -0.878 |
| Jogador 2 | 3-3 | 3 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 7 → 9 | 4 | 6 → 7 | 0.000 | -0.892 |
| Jogador 2 | 3-4 | 7 | 6.000 | 0.000 | 0 → 0 | 0 → 1 | 21% → 25% | 9 → 8 | 7 | 7 → 7 | 0.016 | 0.000 |
| Jogador 2 | 3-5 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 8 → 6 | 8 | 7 → 7 | 0.000 | 0.733 |
| Jogador 2 | 3-6 | 7 | 2.000 | 6.000 | 0 → 0 | 1 → 1 | 25% → 25% | 6 → 7 | 4 | 7 → 7 | -0.087 | -0.395 |
| Jogador 2 | 3-7 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 7 → 12 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 4-1 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 12 → 19 | 0 | 7 → 7 | -0.015 | -0.543 |
| Jogador 2 | 4-2 | 9 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 19 → 9 | 16 | 7 → 7 | 0.008 | -0.292 |
| Jogador 2 | 4-3 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 9 → 7 | 8 | 7 → 7 | 0.000 | 0.708 |
| Jogador 2 | 4-4 | 4 | 6.000 | -6.000 | 0 → 0 | 1 → 1 | 25% → 29% | 7 → 8 | 4 | 7 → 8 | -0.002 | 0.000 |
| Jogador 2 | 4-5 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 8 → 7 | 8 | 8 → 8 | 0.000 | 0.733 |
| Jogador 2 | 4-6 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 7 → 8 | 4 | 8 → 8 | 0.000 | -0.888 |
| Jogador 2 | 4-7 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 8 → 5 | 8 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 5-1 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 5 → 11 | 0 | 8 → 8 | 0.000 | 0.746 |
| Jogador 2 | 5-2 | 4 | 0.000 | 8.000 | 0 → 0 | 1 → 1 | 29% → 29% | 11 → 12 | 6 | 8 → 8 | 0.000 | 0.768 |
| Jogador 2 | 5-3 | 7 | -46.000 | -8.000 | 0 → 0 | 1 → 0 | 29% → 0% | 12 → 0 | 12 | 8 → 8 | 0.022 | -0.407 |
| Jogador 2 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 8 → 8 | 0.000 | 0.000 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 1, COMPOSITION_COMPATIBILITY: 7, PAIR_POTENTIAL: 4; mudanças de composição: 0; posicionamento melhorou em 15 ações e piorou em 12.
- Jogador 2 — estado final: ouro 0, nível 8, vida 0.0, colocação 5.
| Jogador 3 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.067 | 0.000 |
| Jogador 3 | 1-2 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | -0.008 | 0.000 |
| Jogador 3 | 1-3 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 7% → 7% | 3 → 6 | 0 | 3 → 3 | 0.000 | 0.000 |
| Jogador 3 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 7% → 7% | 6 → 10 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 3 | 2-1 | 6 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 7% → 11% | 10 → 6 | 10 | 4 → 5 | 0.030 | 0.419 |
| Jogador 3 | 2-2 | 6 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 14% | 6 → 8 | 3 | 5 → 5 | 0.018 | -0.413 |
| Jogador 3 | 2-3 | 6 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 8 → 7 | 7 | 5 → 5 | -0.009 | 0.448 |
| Jogador 3 | 2-4 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 7 → 8 | 4 | 5 → 5 | 0.000 | 0.000 |
| Jogador 3 | 2-5 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 8 → 5 | 8 | 5 → 6 | 0.000 | -0.620 |
| Jogador 3 | 2-6 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 5 → 11 | 2 | 6 → 6 | 0.015 | -0.517 |
| Jogador 3 | 2-7 | 6 | 6.000 | 0.000 | 0 → 0 | 1 → 2 | 18% → 21% | 11 → 6 | 11 | 6 → 6 | -0.018 | 0.000 |
| Jogador 3 | 3-1 | 3 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 6 → 8 | 4 | 6 → 6 | 0.000 | -0.921 |
| Jogador 3 | 3-2 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 8 → 14 | 0 | 6 → 6 | 0.000 | -0.658 |
| Jogador 3 | 3-3 | 12 | 2.000 | 6.000 | 0 → 0 | 2 → 1 | 21% → 21% | 14 → 8 | 15 | 6 → 6 | -0.062 | 0.238 |
| Jogador 3 | 3-4 | 12 | 6.000 | -6.000 | 0 → 0 | 1 → 1 | 21% → 25% | 8 → 9 | 10 | 6 → 7 | 0.031 | 0.000 |
| Jogador 3 | 3-5 | 5 | 4.000 | 2.000 | 0 → 0 | 1 → 2 | 25% → 25% | 9 → 13 | 3 | 7 → 7 | 0.001 | 0.587 |
| Jogador 3 | 3-6 | 3 | 0.000 | -2.000 | 0 → 0 | 2 → 1 | 25% → 25% | 13 → 20 | 0 | 7 → 7 | 0.000 | -0.875 |
| Jogador 3 | 3-7 | 12 | 6.000 | 0.000 | 0 → 1 | 1 → 0 | 25% → 25% | 20 → 7 | 18 | 7 → 7 | 0.008 | 0.000 |
| Jogador 3 | 4-1 | 6 | 4.000 | 2.000 | 1 → 1 | 0 → 0 | 25% → 25% | 7 → 6 | 7 | 7 → 7 | 0.000 | 0.481 |
| Jogador 3 | 4-2 | 3 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 25% → 25% | 6 → 7 | 4 | 7 → 7 | 0.000 | -0.921 |
| Jogador 3 | 4-3 | 3 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 25% → 25% | 7 → 9 | 4 | 7 → 7 | 0.000 | 0.950 |
| Jogador 3 | 4-4 | 5 | 0.000 | -2.000 | 1 → 1 | 0 → 0 | 25% → 25% | 9 → 7 | 8 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 4-5 | 2 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 25% → 25% | 7 → 14 | 0 | 7 → 7 | 0.000 | 1.442 |
| Jogador 3 | 4-6 | 2 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 25% → 25% | 14 → 22 | 0 | 7 → 7 | 0.000 | 1.456 |
| Jogador 3 | 4-7 | 11 | 6.000 | 8.000 | 1 → 1 | 0 → 1 | 25% → 29% | 22 → 9 | 19 | 7 → 8 | -0.011 | 0.000 |
| Jogador 3 | 5-1 | 8 | 2.000 | 6.000 | 1 → 1 | 1 → 2 | 29% → 29% | 9 → 8 | 8 | 8 → 8 | -0.037 | 0.378 |
| Jogador 3 | 5-2 | 4 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 29% → 29% | 8 → 9 | 7 | 8 → 8 | 0.000 | 0.759 |
| Jogador 3 | 5-3 | 3 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 29% → 29% | 9 → 19 | 0 | 8 → 8 | 0.100 | 1.007 |
| Jogador 3 | 5-4 | 6 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 29% → 29% | 19 → 11 | 16 | 8 → 8 | 0.000 | 0.000 |
| Jogador 3 | 5-5 | 4 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 29% → 29% | 11 → 12 | 8 | 8 → 8 | 0.000 | 0.771 |
| Jogador 3 | 5-6 | 5 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 29% → 29% | 12 → 9 | 12 | 8 → 8 | 0.000 | 0.597 |
| Jogador 3 | 5-7 | 4 | 6.000 | -6.000 | 1 → 1 | 3 → 3 | 29% → 32% | 9 → 13 | 4 | 8 → 9 | -0.024 | 0.000 |
| Jogador 3 | 6-1 | 7 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 32% → 32% | 13 → 10 | 12 | 9 → 9 | 0.000 | 0.429 |
| Jogador 3 | 6-2 | 2 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 32% → 32% | 10 → 11 | 0 | 9 → 9 | 0.000 | 1.503 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 5, COMPOSITION_COMPATIBILITY: 6, IMMEDIATE_UPGRADE: 1, PAIR_POTENTIAL: 7; mudanças de composição: 1; posicionamento melhorou em 19 ações e piorou em 19.
- Jogador 3 — estado final: ouro 11, nível 9, vida 36.0, colocação 1.
| Jogador 4 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 4 | 1-2 | 4 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | 0.095 | 0.000 |
| Jogador 4 | 1-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 7% | 3 → 6 | 0 | 3 → 3 | 0.000 | 0.000 |
| Jogador 4 | 1-4 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 6 → 4 | 6 | 3 → 4 | -0.108 | 0.000 |
| Jogador 4 | 2-1 | 12 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 11% → 14% | 4 → 8 | 1 | 4 → 4 | 0.068 | -0.198 |
| Jogador 4 | 2-2 | 7 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 8 → 7 | 7 | 4 → 5 | 0.032 | 0.401 |
| Jogador 4 | 2-3 | 6 | 4.000 | 0.000 | 0 → 0 | 1 → 0 | 18% → 18% | 7 → 8 | 7 | 5 → 5 | -0.088 | 0.448 |
| Jogador 4 | 2-4 | 7 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 8 → 7 | 10 | 5 → 5 | -0.042 | 0.000 |
| Jogador 4 | 2-5 | 6 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 7 → 6 | 9 | 5 → 6 | 0.000 | -0.413 |
| Jogador 4 | 2-6 | 12 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 21% | 6 → 9 | 4 | 6 → 6 | 0.021 | 0.220 |
| Jogador 4 | 2-7 | 9 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 9 → 5 | 12 | 6 → 6 | 0.009 | 0.000 |
| Jogador 4 | 3-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 5 → 12 | 0 | 6 → 6 | 0.000 | 1.467 |
| Jogador 4 | 3-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 12 → 20 | 0 | 6 → 6 | 0.000 | 1.358 |
| Jogador 4 | 3-3 | 10 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 20 → 7 | 23 | 6 → 7 | 0.029 | 0.285 |
| Jogador 4 | 3-4 | 5 | 6.000 | 0.000 | 0 → 0 | 0 → 1 | 21% → 25% | 7 → 6 | 7 | 7 → 7 | 0.006 | 0.000 |
| Jogador 4 | 3-5 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 6 → 14 | 0 | 7 → 7 | 0.000 | 1.358 |
| Jogador 4 | 3-6 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 14 → 11 | 12 | 7 → 7 | 0.000 | 0.587 |
| Jogador 4 | 3-7 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 11 → 11 | 8 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 4-1 | 12 | 0.000 | 8.000 | 0 → 0 | 1 → 1 | 25% → 25% | 11 → 12 | 11 | 7 → 7 | -0.054 | 0.243 |
| Jogador 4 | 4-2 | 4 | 2.000 | -2.000 | 0 → 0 | 1 → 1 | 25% → 25% | 12 → 22 | 0 | 7 → 7 | -0.084 | 0.733 |
| Jogador 4 | 4-3 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 22 → 29 | 0 | 7 → 7 | -0.008 | -0.696 |
| Jogador 4 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 29 → 36 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 4-5 | 11 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 29% | 36 → 7 | 35 | 7 → 8 | -0.004 | -0.247 |
| Jogador 4 | 4-6 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 7 → 9 | 4 | 8 → 8 | 0.000 | 0.746 |
| Jogador 4 | 4-7 | 6 | 0.000 | -6.000 | 0 → 0 | 1 → 1 | 29% → 29% | 9 → 5 | 12 | 8 → 8 | 0.000 | 0.000 |
| Jogador 4 | 5-1 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 5 → 6 | 4 | 8 → 8 | 0.000 | -0.700 |
| Jogador 4 | 5-2 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 6 → 8 | 4 | 8 → 8 | 0.000 | -0.688 |
| Jogador 4 | 5-3 | 10 | 0.000 | 8.000 | 0 → 1 | 1 → 0 | 29% → 25% | 8 → 7 | 11 | 8 → 8 | 0.045 | -0.290 |
| Jogador 4 | 5-4 | 4 | 8.000 | 0.000 | 1 → 1 | 0 → 0 | 25% → 29% | 7 → 7 | 6 | 8 → 8 | -0.007 | 0.000 |
| Jogador 4 | 5-5 | 5 | -52.000 | -8.000 | 1 → 0 | 0 → 0 | 29% → 0% | 7 → 1 | 6 | 8 → 8 | 0.004 | -0.580 |
| Jogador 4 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 1 → 1 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 4 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 1 → 1 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 4 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 1 → 1 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 4 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 1 → 1 | 0 | 8 → 8 | 0.000 | 0.000 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 8, COMPOSITION_COMPATIBILITY: 7, IMMEDIATE_UPGRADE: 1, PAIR_POTENTIAL: 4; mudanças de composição: 0; posicionamento melhorou em 26 ações e piorou em 24.
- Jogador 4 — estado final: ouro 1, nível 8, vida 0.0, colocação 4.
| Jogador 5 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 5 | 1-2 | 4 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.116 | 0.000 |
| Jogador 5 | 1-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 7% | 2 → 5 | 0 | 3 → 3 | 0.000 | 0.000 |
| Jogador 5 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 7% | 5 → 9 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 5 | 2-1 | 12 | 10.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 14% | 9 → 5 | 9 | 4 → 4 | -0.044 | -0.188 |
| Jogador 5 | 2-2 | 6 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 5 → 7 | 7 | 4 → 5 | 0.139 | -0.404 |
| Jogador 5 | 2-3 | 11 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 7 → 7 | 11 | 5 → 5 | -0.007 | -0.230 |
| Jogador 5 | 2-4 | 5 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 18% | 7 → 6 | 7 | 5 → 5 | -0.014 | 0.000 |
| Jogador 5 | 2-5 | 3 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 6 → 8 | 4 | 5 → 6 | 0.000 | -0.774 |
| Jogador 5 | 2-6 | 12 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 8 → 7 | 14 | 6 → 6 | -0.057 | -0.211 |
| Jogador 5 | 2-7 | 12 | 8.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 21% | 7 → 10 | 5 | 6 → 6 | -0.000 | 0.000 |
| Jogador 5 | 3-1 | 11 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 21% → 21% | 10 → 7 | 11 | 6 → 6 | 0.056 | 0.256 |
| Jogador 5 | 3-2 | 7 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 7 → 6 | 6 | 6 → 6 | -0.054 | -0.362 |
| Jogador 5 | 3-3 | 5 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 21% → 21% | 6 → 9 | 3 | 6 → 6 | -0.087 | -0.537 |
| Jogador 5 | 3-4 | 12 | 2.000 | 2.000 | 0 → 0 | 1 → 1 | 21% → 21% | 9 → 9 | 10 | 6 → 6 | 0.038 | 0.000 |
| Jogador 5 | 3-5 | 3 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 9 → 13 | 2 | 6 → 6 | 0.000 | -0.921 |
| Jogador 5 | 3-6 | 5 | 4.000 | -4.000 | 0 → 0 | 1 → 1 | 21% → 25% | 13 → 11 | 8 | 6 → 7 | -0.001 | 0.543 |
| Jogador 5 | 3-7 | 4 | 2.000 | 6.000 | 0 → 0 | 1 → 1 | 25% → 25% | 11 → 12 | 4 | 7 → 7 | -0.064 | 0.000 |
| Jogador 5 | 4-1 | 3 | 0.000 | 8.000 | 0 → 0 | 1 → 1 | 25% → 25% | 12 → 13 | 4 | 7 → 7 | 0.000 | -0.900 |
| Jogador 5 | 4-2 | 11 | 4.000 | 14.000 | 0 → 0 | 1 → 0 | 25% → 25% | 13 → 7 | 12 | 7 → 7 | 0.015 | 0.255 |
| Jogador 5 | 4-3 | 3 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 25% → 25% | 7 → 10 | 2 | 7 → 7 | 0.000 | -0.892 |
| Jogador 5 | 4-4 | 6 | 2.000 | 10.000 | 0 → 0 | 1 → 0 | 25% → 25% | 10 → 7 | 8 | 7 → 7 | -0.021 | 0.000 |
| Jogador 5 | 4-5 | 4 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 25% → 25% | 7 → 8 | 5 | 7 → 7 | 0.000 | 0.700 |
| Jogador 5 | 4-6 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 25% → 25% | 8 → 5 | 8 | 7 → 7 | 0.000 | -0.458 |
| Jogador 5 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 5 → 10 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 5-1 | 8 | -46.000 | -60.000 | 0 → 0 | 0 → 0 | 25% → 0% | 10 → 0 | 10 | 7 → 7 | 0.035 | -0.350 |
| Jogador 5 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 7 → 7 | 0.000 | 0.000 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 11, COMPOSITION_COMPATIBILITY: 15, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 3; mudanças de composição: 0; posicionamento melhorou em 17 ações e piorou em 22.
- Jogador 5 — estado final: ouro 0, nível 7, vida 0.0, colocação 7.
| Jogador 6 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.067 | 0.000 |
| Jogador 6 | 1-2 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | -0.183 | 0.000 |
| Jogador 6 | 1-3 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 4 | 3 → 3 | -0.048 | 0.000 |
| Jogador 6 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 7 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 6 | 2-1 | 12 | 8.000 | 0.000 | 0 → 1 | 0 → 0 | 11% → 14% | 7 → 7 | 5 | 4 → 4 | 0.018 | -0.198 |
| Jogador 6 | 2-2 | 10 | 2.000 | 0.000 | 1 → 1 | 0 → 0 | 14% → 14% | 7 → 8 | 9 | 4 → 4 | 0.018 | -0.264 |
| Jogador 6 | 2-3 | 8 | 4.000 | 0.000 | 1 → 1 | 0 → 0 | 14% → 18% | 8 → 8 | 8 | 4 → 5 | 0.034 | -0.290 |
| Jogador 6 | 2-4 | 11 | -2.000 | 0.000 | 1 → 1 | 0 → 0 | 18% → 18% | 8 → 15 | 2 | 5 → 5 | 0.020 | 0.000 |
| Jogador 6 | 2-5 | 5 | 0.000 | 4.000 | 1 → 1 | 0 → 0 | 18% → 18% | 15 → 20 | 2 | 5 → 5 | 0.000 | 0.527 |
| Jogador 6 | 2-6 | 5 | 2.000 | 4.000 | 1 → 1 | 0 → 1 | 18% → 18% | 20 → 25 | 3 | 5 → 5 | 0.012 | 0.527 |
| Jogador 6 | 2-7 | 5 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 18% → 18% | 25 → 33 | 0 | 5 → 5 | 0.000 | 0.000 |
| Jogador 6 | 3-1 | 12 | 6.000 | 0.000 | 1 → 1 | 1 → 1 | 18% → 21% | 33 → 18 | 23 | 5 → 6 | -0.005 | 0.230 |
| Jogador 6 | 3-2 | 10 | 0.000 | -8.000 | 1 → 1 | 1 → 1 | 21% → 21% | 18 → 7 | 20 | 6 → 7 | 0.000 | -0.273 |
| Jogador 6 | 3-3 | 9 | 6.000 | 6.000 | 1 → 1 | 1 → 1 | 21% → 25% | 7 → 7 | 6 | 7 → 7 | -0.002 | -0.293 |
| Jogador 6 | 3-4 | 5 | 4.000 | 4.000 | 1 → 1 | 1 → 1 | 25% → 25% | 7 → 9 | 4 | 7 → 7 | 0.005 | 0.000 |
| Jogador 6 | 3-5 | 4 | -2.000 | 2.000 | 1 → 1 | 1 → 1 | 25% → 25% | 9 → 16 | 0 | 7 → 7 | 0.147 | 0.733 |
| Jogador 6 | 3-6 | 6 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 16 → 7 | 16 | 7 → 7 | 0.000 | 0.467 |
| Jogador 6 | 3-7 | 5 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 7 → 9 | 4 | 7 → 7 | 0.007 | 0.000 |
| Jogador 6 | 4-1 | 4 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 9 → 8 | 8 | 7 → 7 | 0.000 | 0.708 |
| Jogador 6 | 4-2 | 4 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 8 → 7 | 8 | 7 → 7 | 0.000 | 0.734 |
| Jogador 6 | 4-3 | 3 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 7 → 8 | 4 | 7 → 8 | 0.000 | -0.888 |
| Jogador 6 | 4-4 | 3 | 6.000 | -6.000 | 1 → 1 | 1 → 1 | 25% → 29% | 8 → 13 | 0 | 8 → 8 | -0.100 | 0.000 |
| Jogador 6 | 4-5 | 5 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 29% → 29% | 13 → 7 | 12 | 8 → 8 | 0.000 | 0.572 |
| Jogador 6 | 4-6 | 3 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 29% → 29% | 7 → 10 | 4 | 8 → 8 | 0.000 | 0.961 |
| Jogador 6 | 4-7 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 29% → 29% | 10 → 17 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 6 | 5-1 | 4 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 29% → 29% | 17 → 25 | 0 | 8 → 8 | 0.000 | 0.739 |
| Jogador 6 | 5-2 | 8 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 29% → 29% | 25 → 6 | 24 | 8 → 8 | 0.000 | -0.356 |
| Jogador 6 | 5-3 | 3 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 29% → 29% | 6 → 8 | 4 | 8 → 8 | 0.000 | 1.032 |
| Jogador 6 | 5-4 | 4 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 29% → 29% | 8 → 5 | 8 | 8 → 9 | 0.000 | 0.000 |
| Jogador 6 | 5-5 | 4 | 8.000 | 0.000 | 1 → 1 | 1 → 1 | 29% → 32% | 5 → 8 | 4 | 9 → 9 | -0.008 | 0.739 |
| Jogador 6 | 5-6 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 32% → 32% | 8 → 14 | 0 | 9 → 9 | 0.000 | 0.000 |
| Jogador 6 | 5-7 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 32% → 32% | 14 → 21 | 0 | 9 → 9 | 0.000 | 0.000 |
| Jogador 6 | 6-1 | 4 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 32% → 32% | 21 → 28 | 0 | 9 → 9 | 0.000 | -0.700 |
| Jogador 6 | 6-2 | 9 | -52.000 | -6.000 | 1 → 0 | 1 → 0 | 32% → 0% | 28 → 0 | 28 | 9 → 9 | -0.029 | -0.311 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 3, COMPOSITION_COMPATIBILITY: 13, IMMEDIATE_UPGRADE: 1, PAIR_POTENTIAL: 5; mudanças de composição: 0; posicionamento melhorou em 18 ações e piorou em 23.
- Jogador 6 — estado final: ouro 0, nível 9, vida 0.0, colocação 2.
| Jogador 7 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.067 | 0.000 |
| Jogador 7 | 1-2 | 7 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 2 | 3 → 3 | -0.003 | 0.000 |
| Jogador 7 | 1-3 | 8 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 3 → 3 | 4 | 3 → 3 | 0.013 | 0.000 |
| Jogador 7 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 7 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 7 | 2-1 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 7 → 11 | 2 | 4 → 4 | -0.024 | 0.448 |
| Jogador 7 | 2-2 | 7 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 18% | 11 → 7 | 11 | 4 → 5 | 0.004 | 0.377 |
| Jogador 7 | 2-3 | 7 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 7 → 10 | 4 | 5 → 5 | 0.039 | 0.352 |
| Jogador 7 | 2-4 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 10 → 6 | 12 | 5 → 5 | 0.008 | 0.000 |
| Jogador 7 | 2-5 | 3 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 6 → 9 | 4 | 5 → 6 | 0.000 | 0.879 |
| Jogador 7 | 2-6 | 7 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 21% | 9 → 10 | 7 | 6 → 6 | -0.095 | 0.386 |
| Jogador 7 | 2-7 | 4 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 10 → 9 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 3-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 9 → 19 | 0 | 6 → 6 | 0.000 | 1.450 |
| Jogador 7 | 3-2 | 12 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 19 → 12 | 19 | 6 → 7 | 0.050 | 0.242 |
| Jogador 7 | 3-3 | 6 | 6.000 | 0.000 | 0 → 0 | 0 → 1 | 21% → 25% | 12 → 19 | 3 | 7 → 7 | -0.109 | 0.494 |
| Jogador 7 | 3-4 | 6 | 0.000 | 14.000 | 0 → 0 | 1 → 2 | 25% → 25% | 19 → 21 | 7 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 3-5 | 9 | 0.000 | -14.000 | 0 → 0 | 2 → 1 | 25% → 25% | 21 → 35 | 3 | 7 → 7 | 0.004 | -0.307 |
| Jogador 7 | 3-6 | 12 | 2.000 | 30.000 | 0 → 0 | 1 → 3 | 25% → 25% | 35 → 13 | 28 | 7 → 7 | 0.073 | 0.244 |
| Jogador 7 | 3-7 | 8 | -4.000 | 18.000 | 0 → 0 | 3 → 3 | 25% → 25% | 13 → 7 | 11 | 7 → 7 | -0.014 | 0.000 |
| Jogador 7 | 4-1 | 8 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 25% → 25% | 7 → 6 | 6 | 7 → 7 | 0.007 | -0.344 |
| Jogador 7 | 4-2 | 4 | 0.000 | 8.000 | 0 → 0 | 3 → 3 | 25% → 25% | 6 → 6 | 6 | 7 → 7 | 0.000 | -0.696 |
| Jogador 7 | 4-3 | 4 | -2.000 | 10.000 | 0 → 0 | 3 → 2 | 25% → 21% | 6 → 6 | 6 | 7 → 7 | -0.055 | -0.687 |
| Jogador 7 | 4-4 | 4 | 10.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 25% | 6 → 7 | 5 | 7 → 7 | -0.089 | 0.000 |
| Jogador 7 | 4-5 | 5 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 25% → 25% | 7 → 6 | 7 | 7 → 7 | 0.000 | -0.525 |
| Jogador 7 | 4-6 | 5 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 6 → 7 | 6 | 7 → 7 | 0.000 | -0.563 |
| Jogador 7 | 4-7 | 5 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 7 → 8 | 6 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 5-1 | 7 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 8 → 8 | 8 | 7 → 7 | 0.000 | -0.400 |
| Jogador 7 | 5-2 | 3 | -42.000 | -72.000 | 0 → 0 | 2 → 0 | 25% → 0% | 8 → 6 | 2 | 7 → 7 | -0.068 | -0.967 |
| Jogador 7 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 6 → 6 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 6 → 6 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 6 → 6 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 6 → 6 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 6 → 6 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 6 → 6 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 6 → 6 | 0 | 7 → 7 | 0.000 | 0.000 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 5, COMPOSITION_COMPATIBILITY: 14, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 6; mudanças de composição: 0; posicionamento melhorou em 15 ações e piorou em 18.
- Jogador 7 — estado final: ouro 6, nível 7, vida 0.0, colocação 6.
| Jogador 8 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 8 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.070 | 0.000 |
| Jogador 8 | 1-3 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 5 | 0 | 3 → 3 | 0.000 | 0.000 |
| Jogador 8 | 1-4 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 5 → 5 | 4 | 3 → 4 | 0.010 | 0.000 |
| Jogador 8 | 2-1 | 9 | 4.000 | 0.000 | 0 → 1 | 1 → 0 | 11% → 11% | 5 → 7 | 3 | 4 → 4 | -0.069 | -0.281 |
| Jogador 8 | 2-2 | 6 | 6.000 | 0.000 | 1 → 1 | 0 → 0 | 11% → 14% | 7 → 6 | 7 | 4 → 5 | 0.001 | 0.427 |
| Jogador 8 | 2-3 | 12 | 6.000 | 0.000 | 1 → 1 | 0 → 0 | 14% → 18% | 6 → 6 | 8 | 5 → 5 | 0.012 | -0.211 |
| Jogador 8 | 2-4 | 6 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 18% → 18% | 6 → 7 | 7 | 5 → 5 | 0.122 | 0.000 |
| Jogador 8 | 2-5 | 5 | 2.000 | 0.000 | 1 → 0 | 0 → 0 | 18% → 18% | 7 → 13 | 3 | 5 → 5 | -0.135 | 0.527 |
| Jogador 8 | 2-6 | 8 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 21% | 13 → 7 | 14 | 5 → 6 | -0.007 | -0.310 |
| Jogador 8 | 2-7 | 5 | 2.000 | 10.000 | 0 → 0 | 0 → 0 | 21% → 21% | 7 → 6 | 6 | 6 → 6 | 0.142 | 0.000 |
| Jogador 8 | 3-1 | 4 | 4.000 | -4.000 | 0 → 0 | 0 → 0 | 21% → 21% | 6 → 8 | 4 | 6 → 6 | -0.147 | -0.658 |
| Jogador 8 | 3-2 | 6 | 0.000 | -6.000 | 0 → 0 | 0 → 0 | 21% → 21% | 8 → 9 | 8 | 6 → 6 | 0.000 | 0.469 |
| Jogador 8 | 3-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 9 → 14 | 0 | 6 → 6 | 0.000 | -1.400 |
| Jogador 8 | 3-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 14 → 20 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 3-5 | 6 | 2.000 | 12.000 | 0 → 0 | 0 → 0 | 21% → 21% | 20 → 20 | 7 | 6 → 6 | 0.000 | -0.461 |
| Jogador 8 | 3-6 | 10 | 6.000 | -6.000 | 0 → 0 | 0 → 0 | 21% → 25% | 20 → 6 | 20 | 6 → 7 | -0.015 | -0.276 |
| Jogador 8 | 3-7 | 3 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 6 → 8 | 4 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 4-1 | 5 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 8 → 6 | 8 | 7 → 7 | 0.000 | 0.572 |
| Jogador 8 | 4-2 | 3 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 6 → 9 | 4 | 7 → 7 | 0.000 | 0.945 |
| Jogador 8 | 4-3 | 4 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 9 → 8 | 8 | 7 → 7 | 0.000 | 0.728 |
| Jogador 8 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 8 → 14 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 4-5 | 6 | 6.000 | -6.000 | 0 → 0 | 0 → 0 | 25% → 29% | 14 → 7 | 12 | 7 → 8 | -0.006 | -0.450 |
| Jogador 8 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 29% → 29% | 7 → 13 | 0 | 8 → 8 | 0.000 | 1.417 |
| Jogador 8 | 4-7 | 6 | 0.000 | 18.000 | 0 → 0 | 0 → 0 | 29% → 29% | 13 → 5 | 13 | 8 → 8 | 0.000 | 0.000 |
| Jogador 8 | 5-1 | 4 | 0.000 | 6.000 | 0 → 0 | 0 → 1 | 29% → 29% | 5 → 9 | 3 | 8 → 8 | 0.000 | 0.739 |
| Jogador 8 | 5-2 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 9 → 8 | 8 | 8 → 8 | 0.000 | 0.730 |
| Jogador 8 | 5-3 | 5 | 0.000 | 8.000 | 0 → 0 | 1 → 1 | 29% → 29% | 8 → 6 | 8 | 8 → 8 | 0.000 | 0.000 |
| Jogador 8 | 5-4 | 5 | 0.000 | 2.000 | 0 → 0 | 1 → 1 | 29% → 29% | 6 → 7 | 5 | 8 → 8 | 0.000 | 0.000 |
| Jogador 8 | 5-5 | 4 | 0.000 | 8.000 | 0 → 0 | 1 → 2 | 29% → 29% | 7 → 6 | 6 | 8 → 8 | 0.000 | -0.688 |
| Jogador 8 | 5-6 | 4 | -50.000 | -42.000 | 0 → 0 | 2 → 0 | 29% → 0% | 6 → 1 | 5 | 8 → 8 | 0.081 | -0.700 |
| Jogador 8 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 1 → 1 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 8 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 1 → 1 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 8 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 1 → 1 | 0 | 8 → 8 | 0.000 | 0.000 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 9, COMPOSITION_COMPATIBILITY: 9, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 4; mudanças de composição: 1; posicionamento melhorou em 14 ações e piorou em 13.
- Jogador 8 — estado final: ouro 1, nível 8, vida 0.0, colocação 3.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Revertidas ≤1 ação | ≤2 ações | ≤4 ações | Ouro perdido | Upgrades | Vendas core/par | Valor médio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 33 | 14 | 2 | 3 | 4 | 0 | 2 | 7 | 4.5387 |
| Jogador 2 | 12 | 3 | 0 | 0 | 0 | 0 | 0 | 2 | 5.1212 |
| Jogador 3 | 19 | 7 | 1 | 1 | 2 | 0 | 1 | 4 | 3.401 |
| Jogador 4 | 20 | 10 | 1 | 1 | 2 | 0 | 1 | 5 | 3.1431 |
| Jogador 5 | 31 | 12 | 5 | 6 | 7 | 0 | 2 | 2 | 3.2179 |
| Jogador 6 | 22 | 9 | 2 | 2 | 3 | 0 | 1 | 4 | 4.5292 |
| Jogador 7 | 27 | 8 | 1 | 2 | 2 | 0 | 2 | 5 | 3.5956 |
| Jogador 8 | 24 | 7 | 2 | 2 | 2 | 0 | 2 | 2 | 2.3952 |

As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Uma venda sem compra correspondente na janela é UNKNOWN; sequências ambíguas não são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| HIGH | Jogador 1 | 1-2 | 27 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 1 | 1-3 | 50 | SOLD_CORE_UNIT | Venda de 'DA_Gromp18_AP' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 1 | 1-3 | 50 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 1 | 1-4 | 79 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 1 | 1-4 | 81 | SOLD_CORE_UNIT | Venda de 'DA_18_Ornn' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 1 | 1-4 | 83 | PURCHASE_REVERSED | Compra de DA_18_Kobuko desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 1 | 2-2 | 129 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Ornn' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 1 | 2-6 | 216 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 1 | 2-6 | 216 | PURCHASE_REVERSED | Compra de DA_KogMaw18_AD desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 1 | 3-1 | 255 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 1 | 3-4 | 316 | PURCHASE_REVERSED | Compra de DA_18_Yunara desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 5-2 | 501 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Cassiopeia' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 1 | 5-2 | 501 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Shen' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 1 | 5-2 | 501 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Lux_Fae' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 2 | 1-3 | 52 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 2 | 2-1 | 106 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 2 | 5-4 | 521 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Zyra' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 2 | 5-4 | 521 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Malphite' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 2 | 5-4 | 521 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Fiddlesticks18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 3 | 2-6 | 214 | PURCHASE_REVERSED | Compra de DA_18_Caitlyn desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 3 | 3-3 | 303 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 3 | 3-4 | 315 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 3 | 3-4 | 315 | PURCHASE_REVERSED | Compra de DA_18_Diana desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 3 | 3-4 | 316 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 3 | 3-6 | 342 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_RekSai' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 4 | 2-3 | 149 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 4 | 2-4 | 172 | SOLD_CORE_UNIT | Venda de 'DA_Krug18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 4 | 2-5 | 191 | SOLD_CORE_UNIT | Venda de 'DA_CrimsonRaptor18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 4 | 2-5 | 191 | PURCHASE_REVERSED | Compra de DA_CrimsonRaptor18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 4 | 2-6 | 215 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 4 | 2-7 | 237 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 4 | 5-3 | 506 | PURCHASE_REVERSED | Compra de DA_Nidalee18_AP desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 4 | 5-6 | 541 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Fiddlesticks18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 4 | 5-6 | 541 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Aphelios' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 4 | 5-6 | 541 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Soraka' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 5 | 2-2 | 129 | SOLD_CORE_UNIT | Venda de 'DA_18_Cassiopeia' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 5 | 2-3 | 148 | SOLD_CORE_UNIT | Venda de 'DA_18_LeBlanc' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 5 | 2-3 | 150 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-3 | 155 | PURCHASE_REVERSED | Compra de DA_18_Veigar desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-6 | 213 | PURCHASE_REVERSED | Compra de DA_18_Yunara desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-6 | 215 | PURCHASE_REVERSED | Compra de DA_18_Yunara desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-6 | 219 | PURCHASE_REVERSED | Compra de DA_Scuttlecrab18 desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 3-4 | 317 | PURCHASE_REVERSED | Compra de DA_18_RekSai desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 3-4 | 319 | PURCHASE_REVERSED | Compra de DA_Cinderling18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 5-2 | 501 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Tristana' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 5 | 5-2 | 501 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Sentinel18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 5 | 5-2 | 501 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Teemo' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 6 | 1-3 | 50 | SOLD_CORE_UNIT | Venda de 'DA_18_Caitlyn' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 6 | 1-3 | 50 | PURCHASE_REVERSED | Compra de DA_18_Caitlyn desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 6 | 2-2 | 133 | PURCHASE_REVERSED | Compra de DA_18_Shen desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 6 | 2-3 | 148 | PURCHASE_REVERSED | Compra de DA_18_Teemo desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 6 | 2-4 | 176 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 6 | 3-2 | 277 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 6 | 3-2 | 278 | SOLD_CORE_UNIT | Venda de 'DA_Fiddlesticks18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 7 | 1-2 | 28 | SOLD_CORE_UNIT | Venda de 'DA_18_RekSai' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 7 | 1-3 | 51 | SOLD_CORE_UNIT | Venda de 'DA_18_RekSai' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 7 | 3-2 | 275 | SOLD_CORE_UNIT | Venda de 'DA_CrimsonRaptor18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 7 | 3-2 | 275 | PURCHASE_REVERSED | Compra de DA_CrimsonRaptor18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 7 | 3-5 | 331 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 7 | 3-5 | 334 | PURCHASE_REVERSED | Compra de DA_18_Diana desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 7 | 3-5 | 335 | SOLD_CORE_UNIT | Venda de 'DA_18_Aphelios' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 7 | 5-3 | 511 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Sentinel18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 7 | 5-3 | 511 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Ashe' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 7 | 5-3 | 511 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Scuttlecrab18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 8 | 2-3 | 152 | PURCHASE_REVERSED | Compra de DA_18_Caitlyn desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 2-3 | 155 | PURCHASE_REVERSED | Compra de DA_18_Kobuko desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 8 | 2-5 | 192 | SOLD_CORE_UNIT | Venda de 'DA_18_Leona' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 8 | 2-6 | 213 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 8 | 5-7 | 551 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Fiddlesticks18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 8 | 5-7 | 551 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Lux_Elderwood' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 8 | 5-7 | 551 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Malphite' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- O JSON estruturado é a fonte primária para estado de decisão, máscaras, política e recompensas; .tft é analisado apenas para jogadores sem sidecar JSON.- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
\n\n---\n\n## Evidências resumidas dos achados\n\nO relatório apresenta métricas agregadas e a timeline em tabelas. Esta seção complementa apenas os achados com o contexto mínimo da decisão; snapshots, máscaras brutas e diagnósticos completos não são duplicados em Markdown.\n\n### HIGH · SOLD_CORE_UNIT · Jogador 1 · 1-2 · step 27\n\nVenda de 'DA_18_Akali_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 3, ouro 0, força 4.0\n- Composição: — / DA_18_Akali_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -1.020556926727295, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Akali_AD, core_sale=True, pair_lost=True, pair_count_before=1, pair_count_after=0, gold_before=0, gold_after=1\n\n### HIGH · SOLD_CORE_UNIT · Jogador 1 · 1-3 · step 50\n\nVenda de 'DA_Gromp18_AP' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 3, ouro 0, força 6.0\n- Composição: — / DA_Gromp18_AP\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.5175982713699341, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_Gromp18_AP, core_sale=True, pair_lost=False, pair_count_before=0, pair_count_after=0, gold_before=0, gold_after=2\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 1 · 1-3 · step 50\n\nCompra de DA_Gromp18_AP desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 3, ouro 0, força 6.0\n- Composição: — / DA_Gromp18_AP\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.5175982713699341, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=49, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=0.7818\n\n### HIGH · SOLD_CORE_UNIT · Jogador 1 · 1-4 · step 79\n\nVenda de 'DA_18_Akali_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 4, ouro 0, força 6.0\n- Composição: — / DA_18_Akali_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -1.0211474895477295, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Akali_AD, core_sale=True, pair_lost=True, pair_count_before=1, pair_count_after=0, gold_before=0, gold_after=1\n\n### HIGH · SOLD_CORE_UNIT · Jogador 1 · 1-4 · step 81\n\nVenda de 'DA_18_Ornn' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 4, ouro 0, força 6.0\n- Composição: — / DA_18_Akali_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -1.0122066736221313, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Ornn, core_sale=True, pair_lost=True, pair_count_before=1, pair_count_after=0, gold_before=0, gold_after=1\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 1 · 1-4 · step 83\n\nCompra de DA_18_Kobuko desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 4, ouro 0, força 6.0\n- Composição: — / DA_18_Akali_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.1786923110485077, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=82, cost=1, sale_gold_delta=1, net_gold_lost=0, fit_score=0.0\n\n### HIGH · SOLD_UPGRADE_PAIR_COPY · Jogador 1 · 2-2 · step 129\n\nVenda de 'DA_18_Ornn' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 4, ouro 7, força 12.0\n- Composição: — / DA_18_Diana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.37360498309135437, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Ornn, core_sale=False, pair_lost=True, pair_count_before=1, pair_count_after=0, gold_before=7, gold_after=8\n\n### HIGH · SOLD_CORE_UNIT · Jogador 1 · 2-6 · step 216\n\nVenda de 'DA_KogMaw18_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 94.0, nível 5, ouro 15, força 20.0\n- Composição: — / DA_18_Diana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.5565354228019714, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_KogMaw18_AD, core_sale=True, pair_lost=False, pair_count_before=1, pair_count_after=1, gold_before=15, gold_after=18\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 1 · 2-6 · step 216\n\nCompra de DA_KogMaw18_AD desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 94.0, nível 5, ouro 15, força 20.0\n- Composição: — / DA_18_Diana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.5565354228019714, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=213, cost=3, sale_gold_delta=3, net_gold_lost=0, fit_score=2.1663\n\n### HIGH · SOLD_CORE_UNIT · Jogador 1 · 3-1 · step 255\n\nVenda de 'DA_18_Diana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 88.0, nível 6, ouro 0, força 26.0\n- Composição: Defendente / DA_18_Diana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3582598567008972, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Diana, core_sale=True, pair_lost=False, pair_count_before=1, pair_count_after=1, gold_before=0, gold_after=3\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 1 · 3-4 · step 316\n\nCompra de DA_18_Yunara desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 77.0, nível 7, ouro 3, força 26.0\n- Composição: Defendente / DA_18_Shen\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.17823076248168945, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=314, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=0.0\n\n### MEDIUM · CORE_UNIT_MISSING_REPEATEDLY · Jogador 1 · 5-2 · step 501\n\nUnidade core 'DA_18_Cassiopeia' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos.\n- Evidência adicional: core_unit=DA_18_Cassiopeia, missing_snapshots=3, comp_direction=Defendente, comp_focus=DA_18_Cassiopeia\n\n### MEDIUM · CORE_UNIT_MISSING_REPEATEDLY · Jogador 1 · 5-2 · step 501\n\nUnidade core 'DA_18_Shen' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos.\n- Evidência adicional: core_unit=DA_18_Shen, missing_snapshots=3, comp_direction=Defendente, comp_focus=DA_18_Cassiopeia\n\n### MEDIUM · CORE_UNIT_MISSING_REPEATEDLY · Jogador 1 · 5-2 · step 501\n\nUnidade core 'DA_18_Lux_Fae' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos.\n- Evidência adicional: core_unit=DA_18_Lux_Fae, missing_snapshots=3, comp_direction=Defendente, comp_focus=DA_18_Cassiopeia\n\n### HIGH · SOLD_CORE_UNIT · Jogador 2 · 1-3 · step 52\n\nVenda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 3, ouro 1, força 6.0\n- Composição: — / DA_18_Sejuani\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.7156829237937927, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Yorick, core_sale=True, pair_lost=True, pair_count_before=1, pair_count_after=0, gold_before=1, gold_after=2\n\n### HIGH · SOLD_CORE_UNIT · Jogador 2 · 2-1 · step 106\n\nVenda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 4, ouro 1, força 12.0\n- Composição: — / DA_Vi18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.729604959487915, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Yorick, core_sale=True, pair_lost=True, pair_count_before=1, pair_count_after=0, gold_before=1, gold_after=2\n\n### MEDIUM · CORE_UNIT_MISSING_REPEATEDLY · Jogador 2 · 5-4 · step 521\n\nUnidade core 'DA_18_Zyra' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos.\n- Evidência adicional: core_unit=DA_18_Zyra, missing_snapshots=3, comp_direction=Colosso, comp_focus=DA_18_Zyra\n\n### MEDIUM · CORE_UNIT_MISSING_REPEATEDLY · Jogador 2 · 5-4 · step 521\n\nUnidade core 'DA_18_Malphite' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos.\n- Evidência adicional: core_unit=DA_18_Malphite, missing_snapshots=3, comp_direction=Colosso, comp_focus=DA_18_Zyra\n\n### MEDIUM · CORE_UNIT_MISSING_REPEATEDLY · Jogador 2 · 5-4 · step 521\n\nUnidade core 'DA_Fiddlesticks18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos.\n- Evidência adicional: core_unit=DA_Fiddlesticks18, missing_snapshots=3, comp_direction=Colosso, comp_focus=DA_18_Zyra\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 3 · 2-6 · step 214\n\nCompra de DA_18_Caitlyn desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 88.0, nível 6, ouro 3, força 20.0\n- Composição: — / DA_18_Diana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.17823076248168945, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=213, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=0.0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 3 · 3-3 · step 303\n\nVenda de 'DA_18_Diana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 59.0, nível 6, ouro 7, força 28.0\n- Composição: Caçador / DA_18_Sivir\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.6046954393386841, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Diana, core_sale=True, pair_lost=True, pair_count_before=2, pair_count_after=1, gold_before=7, gold_after=10\n\n### HIGH · SOLD_CORE_UNIT · Jogador 3 · 3-4 · step 315\n\nVenda de 'DA_18_Diana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 59.0, nível 6, ouro 5, força 28.0\n- Composição: Caçador / DA_18_Sivir\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.850276529788971, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Diana, core_sale=True, pair_lost=True, pair_count_before=2, pair_count_after=1, gold_before=5, gold_after=8\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 3 · 3-4 · step 315\n\nCompra de DA_18_Diana desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 59.0, nível 6, ouro 5, força 28.0\n- Composição: Caçador / DA_18_Sivir\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.850276529788971, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=312, cost=3, sale_gold_delta=3, net_gold_lost=0, fit_score=5.0576\n\n### HIGH · SOLD_CORE_UNIT · Jogador 3 · 3-4 · step 316\n\nVenda de 'DA_18_Diana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 59.0, nível 6, ouro 8, força 28.0\n- Composição: Caçador / DA_18_Sivir\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.27792081236839294, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Diana, core_sale=True, pair_lost=False, pair_count_before=1, pair_count_after=1, gold_before=8, gold_after=11\n\n### HIGH · SOLD_UPGRADE_PAIR_COPY · Jogador 3 · 3-6 · step 342\n\nVenda de 'DA_18_RekSai' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 59.0, nível 7, ouro 13, força 38.0\n- Composição: Caçador / DA_18_Sivir\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.6804715991020203, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_RekSai, core_sale=False, pair_lost=True, pair_count_before=2, pair_count_after=1, gold_before=13, gold_after=14\n\n### HIGH · SOLD_UPGRADE_PAIR_COPY · Jogador 4 · 2-3 · step 149\n\nVenda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 95.0, nível 5, ouro 4, força 20.0\n- Composição: — / DA_KogMaw18_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.39178818464279175, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Yorick, core_sale=False, pair_lost=True, pair_count_before=1, pair_count_after=0, gold_before=4, gold_after=5\n\n### HIGH · SOLD_CORE_UNIT · Jogador 4 · 2-4 · step 172\n\nVenda de 'DA_Krug18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 95.0, nível 5, ouro 4, força 22.0\n- Composição: — / DA_18_Aphelios\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3085384666919708, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_Krug18, core_sale=True, pair_lost=False, pair_count_before=0, pair_count_after=0, gold_before=4, gold_after=7\n\n### HIGH · SOLD_CORE_UNIT · Jogador 4 · 2-5 · step 191\n\nVenda de 'DA_CrimsonRaptor18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 95.0, nível 5, ouro 4, força 22.0\n- Composição: — / DA_18_Aphelios\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.5458217263221741, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_CrimsonRaptor18, core_sale=True, pair_lost=False, pair_count_before=0, pair_count_after=0, gold_before=4, gold_after=7\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 4 · 2-5 · step 191\n\nCompra de DA_CrimsonRaptor18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 95.0, nível 5, ouro 4, força 22.0\n- Composição: — / DA_18_Aphelios\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.5458217263221741, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=190, cost=3, sale_gold_delta=3, net_gold_lost=0, fit_score=1.4796\n\n### HIGH · SOLD_UPGRADE_PAIR_COPY · Jogador 4 · 2-6 · step 215\n\nVenda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia ECON · motivo ECON: acumular até o limite de juros de 50\n- Estado: HP 89.0, nível 6, ouro 2, força 28.0\n- Composição: — / DA_18_Aphelios\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -1.0187406539916992, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Rakan, core_sale=False, pair_lost=True, pair_count_before=1, pair_count_after=0, gold_before=2, gold_after=3\n\n### HIGH · SOLD_UPGRADE_PAIR_COPY · Jogador 4 · 2-7 · step 237\n\nVenda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia ECON · motivo ECON: acumular até o limite de juros de 50\n- Estado: HP 89.0, nível 6, ouro 1, força 30.0\n- Composição: — / DA_18_Aphelios\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.944477379322052, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Yorick, core_sale=False, pair_lost=True, pair_count_before=1, pair_count_after=0, gold_before=1, gold_after=2\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 4 · 5-3 · step 506\n\nCompra de DA_Nidalee18_AP desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: pressão de vida\n- Estado: HP 30.0, nível 8, ouro 1, força 32.0\n- Composição: Colosso / DA_Fiddlesticks18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.19269230961799622, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=503, cost=4, sale_gold_delta=4, net_gold_lost=0, fit_score=0.0\n\n### MEDIUM · CORE_UNIT_MISSING_REPEATEDLY · Jogador 4 · 5-6 · step 541\n\nUnidade core 'DA_Fiddlesticks18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos.\n- Evidência adicional: core_unit=DA_Fiddlesticks18, missing_snapshots=3, comp_direction=Colosso, comp_focus=DA_Fiddlesticks18\n\n### MEDIUM · CORE_UNIT_MISSING_REPEATEDLY · Jogador 4 · 5-6 · step 541\n\nUnidade core 'DA_18_Aphelios' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos.\n- Evidência adicional: core_unit=DA_18_Aphelios, missing_snapshots=3, comp_direction=Colosso, comp_focus=DA_Fiddlesticks18\n\n### MEDIUM · CORE_UNIT_MISSING_REPEATEDLY · Jogador 4 · 5-6 · step 541\n\nUnidade core 'DA_18_Soraka' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos.\n- Evidência adicional: core_unit=DA_18_Soraka, missing_snapshots=3, comp_direction=Colosso, comp_focus=DA_Fiddlesticks18\n\n### HIGH · SOLD_CORE_UNIT · Jogador 5 · 2-2 · step 129\n\nVenda de 'DA_18_Cassiopeia' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 96.0, nível 4, ouro 2, força 16.0\n- Composição: — / DA_18_MasterYi_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3604661226272583, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Cassiopeia, core_sale=True, pair_lost=False, pair_count_before=0, pair_count_after=0, gold_before=2, gold_after=5\n\n### HIGH · SOLD_CORE_UNIT · Jogador 5 · 2-3 · step 148\n\nVenda de 'DA_18_LeBlanc' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 91.0, nível 5, ouro 5, força 16.0\n- Composição: — / DA_18_MasterYi_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -1.0003758668899536, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_LeBlanc, core_sale=True, pair_lost=True, pair_count_before=1, pair_count_after=0, gold_before=5, gold_after=7\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 5 · 2-3 · step 150\n\nCompra de DA_Gromp18_AP desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 91.0, nível 5, ouro 5, força 16.0\n- Composição: — / DA_18_MasterYi_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3266529440879822, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=149, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=0.0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 5 · 2-3 · step 155\n\nCompra de DA_18_Veigar desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 91.0, nível 5, ouro 0, força 16.0\n- Composição: — / DA_18_MasterYi_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3952833116054535, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=154, cost=1, sale_gold_delta=1, net_gold_lost=0, fit_score=0.0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 5 · 2-6 · step 213\n\nCompra de DA_18_Yunara desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia LOSS_STREAK · motivo LOSS_STREAK: converter derrota em economia sem risco crítico\n- Estado: HP 80.0, nível 6, ouro 6, força 22.0\n- Composição: — / DA_18_MasterYi_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.4035416543483734, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=212, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=3.1225\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 5 · 2-6 · step 215\n\nCompra de DA_18_Yunara desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia LOSS_STREAK · motivo LOSS_STREAK: converter derrota em economia sem risco crítico\n- Estado: HP 80.0, nível 6, ouro 6, força 22.0\n- Composição: — / DA_18_MasterYi_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.4038984775543213, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=214, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=3.1789\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 5 · 2-6 · step 219\n\nCompra de DA_Scuttlecrab18 desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia LOSS_STREAK · motivo LOSS_STREAK: converter derrota em economia sem risco crítico\n- Estado: HP 80.0, nível 6, ouro 2, força 22.0\n- Composição: — / DA_18_Rammus\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.30376315116882324, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=216, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=1.6965\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 5 · 3-4 · step 317\n\nCompra de DA_18_RekSai desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 54.0, nível 6, ouro 0, força 32.0\n- Composição: Vivaz / DA_18_Tristana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.4963274896144867, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=315, cost=1, sale_gold_delta=1, net_gold_lost=0, fit_score=0.0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 5 · 3-4 · step 319\n\nCompra de DA_Cinderling18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 54.0, nível 6, ouro 0, força 32.0\n- Composição: Vivaz / DA_18_Tristana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.18709473311901093, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=318, cost=1, sale_gold_delta=1, net_gold_lost=0, fit_score=0.2721\n\n### MEDIUM · CORE_UNIT_MISSING_REPEATEDLY · Jogador 5 · 5-2 · step 501\n\nUnidade core 'DA_18_Tristana' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos.\n- Evidência adicional: core_unit=DA_18_Tristana, missing_snapshots=3, comp_direction=Vivaz, comp_focus=DA_18_Tristana\n\n### MEDIUM · CORE_UNIT_MISSING_REPEATEDLY · Jogador 5 · 5-2 · step 501\n\nUnidade core 'DA_Sentinel18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos.\n- Evidência adicional: core_unit=DA_Sentinel18, missing_snapshots=3, comp_direction=Vivaz, comp_focus=DA_18_Tristana\n\n### MEDIUM · CORE_UNIT_MISSING_REPEATEDLY · Jogador 5 · 5-2 · step 501\n\nUnidade core 'DA_18_Teemo' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos.\n- Evidência adicional: core_unit=DA_18_Teemo, missing_snapshots=3, comp_direction=Vivaz, comp_focus=DA_18_Tristana\n\n### HIGH · SOLD_CORE_UNIT · Jogador 6 · 1-3 · step 50\n\nVenda de 'DA_18_Caitlyn' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 3, ouro 0, força 6.0\n- Composição: — / DA_18_Yunara\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.48899999260902405, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Caitlyn, core_sale=True, pair_lost=False, pair_count_before=0, pair_count_after=0, gold_before=0, gold_after=2\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 6 · 1-3 · step 50\n\nCompra de DA_18_Caitlyn desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 3, ouro 0, força 6.0\n- Composição: — / DA_18_Yunara\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.48899999260902405, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=49, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=0.0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 6 · 2-2 · step 133\n\nCompra de DA_18_Shen desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 95.0, nível 4, ouro 0, força 20.0\n- Composição: — / DA_18_Rakan\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.2133076936006546, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=129, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=0.0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 6 · 2-3 · step 148\n\nCompra de DA_18_Teemo desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 88.0, nível 4, ouro 6, força 20.0\n- Composição: — / DA_18_Rakan\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.42182859778404236, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=147, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=0.0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 6 · 2-4 · step 176\n\nVenda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 83.0, nível 5, ouro 8, força 22.0\n- Composição: — / DA_18_Rakan\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -1.0471569299697876, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Rakan, core_sale=True, pair_lost=True, pair_count_before=1, pair_count_after=0, gold_before=8, gold_after=9\n\n### HIGH · SOLD_CORE_UNIT · Jogador 6 · 3-2 · step 277\n\nVenda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 83.0, nível 6, ouro 2, força 30.0\n- Composição: Feérico / DA_18_Rakan\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.7514423727989197, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Rakan, core_sale=True, pair_lost=False, pair_count_before=1, pair_count_after=1, gold_before=2, gold_after=3\n\n### HIGH · SOLD_CORE_UNIT · Jogador 6 · 3-2 · step 278\n\nVenda de 'DA_Fiddlesticks18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 83.0, nível 6, ouro 3, força 30.0\n- Composição: Feérico / DA_18_Rakan\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.4006653130054474, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_Fiddlesticks18, core_sale=True, pair_lost=False, pair_count_before=1, pair_count_after=1, gold_before=3, gold_after=6\n\n### HIGH · SOLD_CORE_UNIT · Jogador 7 · 1-2 · step 28\n\nVenda de 'DA_18_RekSai' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 3, ouro 0, força 4.0\n- Composição: — / DA_18_Rakan\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -1.0123158693313599, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_RekSai, core_sale=True, pair_lost=True, pair_count_before=1, pair_count_after=0, gold_before=0, gold_after=1\n\n### HIGH · SOLD_CORE_UNIT · Jogador 7 · 1-3 · step 51\n\nVenda de 'DA_18_RekSai' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 3, ouro 1, força 6.0\n- Composição: — / DA_18_Elise\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3240300714969635, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_RekSai, core_sale=True, pair_lost=False, pair_count_before=0, pair_count_after=0, gold_before=1, gold_after=2\n\n### HIGH · SOLD_CORE_UNIT · Jogador 7 · 3-2 · step 275\n\nVenda de 'DA_CrimsonRaptor18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 6, ouro 16, força 30.0\n- Composição: Vanguarda / DA_Sentinel18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.5164765119552612, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_CrimsonRaptor18, core_sale=True, pair_lost=False, pair_count_before=0, pair_count_after=0, gold_before=16, gold_after=19\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 7 · 3-2 · step 275\n\nCompra de DA_CrimsonRaptor18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 6, ouro 16, força 30.0\n- Composição: Vanguarda / DA_Sentinel18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.5164765119552612, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=274, cost=3, sale_gold_delta=3, net_gold_lost=0, fit_score=0.0583\n\n### HIGH · SOLD_CORE_UNIT · Jogador 7 · 3-5 · step 331\n\nVenda de 'DA_KogMaw18_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 7, ouro 21, força 36.0\n- Composição: Vanguarda / DA_Sentinel18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.7110646367073059, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_KogMaw18_AD, core_sale=True, pair_lost=True, pair_count_before=2, pair_count_after=1, gold_before=21, gold_after=24\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 7 · 3-5 · step 334\n\nCompra de DA_18_Diana desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 7, ouro 21, força 36.0\n- Composição: Vanguarda / DA_Sentinel18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.5728461742401123, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=332, cost=3, sale_gold_delta=3, net_gold_lost=0, fit_score=9.2977\n\n### HIGH · SOLD_CORE_UNIT · Jogador 7 · 3-5 · step 335\n\nVenda de 'DA_18_Aphelios' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 7, ouro 24, força 36.0\n- Composição: Vanguarda / DA_Sentinel18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.2976153790950775, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Aphelios, core_sale=True, pair_lost=False, pair_count_before=1, pair_count_after=1, gold_before=24, gold_after=28\n\n### MEDIUM · CORE_UNIT_MISSING_REPEATEDLY · Jogador 7 · 5-3 · step 511\n\nUnidade core 'DA_Sentinel18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos.\n- Evidência adicional: core_unit=DA_Sentinel18, missing_snapshots=3, comp_direction=Vanguarda, comp_focus=DA_Sentinel18\n\n### MEDIUM · CORE_UNIT_MISSING_REPEATEDLY · Jogador 7 · 5-3 · step 511\n\nUnidade core 'DA_18_Ashe' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos.\n- Evidência adicional: core_unit=DA_18_Ashe, missing_snapshots=3, comp_direction=Vanguarda, comp_focus=DA_Sentinel18\n\n### MEDIUM · CORE_UNIT_MISSING_REPEATEDLY · Jogador 7 · 5-3 · step 511\n\nUnidade core 'DA_Scuttlecrab18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos.\n- Evidência adicional: core_unit=DA_Scuttlecrab18, missing_snapshots=3, comp_direction=Vanguarda, comp_focus=DA_Sentinel18\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 8 · 2-3 · step 152\n\nCompra de DA_18_Caitlyn desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 94.0, nível 5, ouro 1, força 22.0\n- Composição: — / DA_18_Leona\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.19792307913303375, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=151, cost=2, sale_gold_delta=2, net_gold_lost=0, fit_score=0.0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 8 · 2-3 · step 155\n\nCompra de DA_18_Kobuko desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 94.0, nível 5, ouro 0, força 22.0\n- Composição: — / DA_18_Leona\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.39467376470565796, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=154, cost=1, sale_gold_delta=1, net_gold_lost=0, fit_score=0.0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 8 · 2-5 · step 192\n\nVenda de 'DA_18_Leona' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 88.0, nível 5, ouro 4, força 24.0\n- Composição: — / DA_18_Tristana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.38723769783973694, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Leona, core_sale=True, pair_lost=False, pair_count_before=0, pair_count_after=0, gold_before=4, gold_after=7\n\n### HIGH · SOLD_CORE_UNIT · Jogador 8 · 2-6 · step 213\n\nVenda de 'DA_18_Tristana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 88.0, nível 5, ouro 10, força 24.0\n- Composição: — / DA_18_Tristana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -1.017004132270813, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Tristana, core_sale=True, pair_lost=True, pair_count_before=1, pair_count_after=0, gold_before=10, gold_after=13\n\n### MEDIUM · CORE_UNIT_MISSING_REPEATEDLY · Jogador 8 · 5-7 · step 551\n\nUnidade core 'DA_Fiddlesticks18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos.\n- Evidência adicional: core_unit=DA_Fiddlesticks18, missing_snapshots=3, comp_direction=Vivaz, comp_focus=DA_Fiddlesticks18\n\n### MEDIUM · CORE_UNIT_MISSING_REPEATEDLY · Jogador 8 · 5-7 · step 551\n\nUnidade core 'DA_18_Lux_Elderwood' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos.\n- Evidência adicional: core_unit=DA_18_Lux_Elderwood, missing_snapshots=3, comp_direction=Vivaz, comp_focus=DA_Fiddlesticks18\n\n### MEDIUM · CORE_UNIT_MISSING_REPEATEDLY · Jogador 8 · 5-7 · step 551\n\nUnidade core 'DA_18_Malphite' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos.\n- Evidência adicional: core_unit=DA_18_Malphite, missing_snapshots=3, comp_direction=Vivaz, comp_focus=DA_Fiddlesticks18\n\n## Arquivos e rastreabilidade\n\n- Jogadores analisados: 8\n- Entradas analisadas: 3794\n- Decisões com timeline: 1136\n- Achados: 71\n- Os arquivos estruturados de origem permanecem separados deste relatório.\n- Campos ausentes são exibidos como “—”; não são inferidos como zero.\n