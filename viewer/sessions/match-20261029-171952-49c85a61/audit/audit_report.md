# Auditoria da partida TFT

- Arquivos lidos: **8**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Entradas JSON analisadas: **4410**
- Achados: **161**
- CRITICAL: 0 | HIGH: 72 | MEDIUM: 89 | LOW: 0

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 215 | 215 | 215 | 0 | 211 | 0 | 215 | 215 | 212 | 41/31 |
| Jogador 2 | 178 | 178 | 178 | 0 | 176 | 0 | 178 | 178 | 170 | 40/32 |
| Jogador 3 | 217 | 217 | 217 | 0 | 213 | 0 | 217 | 217 | 216 | 27/15 |
| Jogador 4 | 157 | 157 | 157 | 0 | 156 | 0 | 157 | 157 | 146 | 22/11 |
| Jogador 5 | 182 | 182 | 182 | 0 | 180 | 0 | 182 | 182 | 175 | 40/29 |
| Jogador 6 | 211 | 211 | 211 | 0 | 209 | 0 | 211 | 211 | 207 | 51/42 |
| Jogador 7 | 256 | 256 | 256 | 0 | 252 | 0 | 256 | 256 | 256 | 55/46 |
| Jogador 8 | 249 | 249 | 249 | 0 | 242 | 0 | 249 | 249 | 249 | 56/47 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 9 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Ornn | MOVE_BENCH, SELL, PASS | True | True | 0.24171799421310425 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3013512194156647 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9475080370903015 | 0.0 | 0.0 | +679fe281-674a-438b-bdcf-57229a283d44 / -— |
| Jogador 1 | 1-2 | 13 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4258473813533783 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 21 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7530208826065063 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 22 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3134728670120239 | 0.0 | 0.0 | +24247863-54d4-4674-86e9-9a45609a440e / -— |
| Jogador 1 | 1-3 | 23 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1178767681121826 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -2718f555-b782-4fea-a68f-31395ad34232,679fe281-674a-438b-bdcf-57229a283d44 |
| Jogador 1 | 1-4 | 32 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 39 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3534727692604065 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.037005286663770676 | 0.0 | 0.0 | +3a74be8d-bf7c-4449-9f1b-d76521e73e6f / -— |
| Jogador 1 | 2-1 | 42 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3389334976673126 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -— |
| Jogador 1 | 2-1 | 43 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 49 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3202444911003113 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 51 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 9 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6853392720222473 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 52 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4275911748409271 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 53 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04230523109436035 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 54 | BUY_XP | STABILIZE | 100.0 | 4 | 6 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 55 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 61 | BUY_XP | STABILIZE | 100.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44699999690055847 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 62 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6768854856491089 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 63 | BUY | STABILIZE | 100.0 | 5 | 5 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9608235955238342 | 0.0 | 0.0 | +6951a681-f5b9-4c22-9182-46b4d2c3cbb3 / -— |
| Jogador 1 | 2-3 | 64 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 3 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14519578218460083 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 65 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 3 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07504034042358398 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 66 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3965875208377838 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 67 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 3 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14529743790626526 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 68 | PASS | STABILIZE | 100.0 | 5 | 3 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 71 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 8 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19759193062782288 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 72 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 8 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1955433189868927 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 73 | BUY_XP | STABILIZE | 95.0 | 5 | 8 | 0 | 20.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 74 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 20.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 75 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 20.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015292307361960411 | 0.0 | 0.0 | +— / -c448b2c1-7854-4c8c-a51b-eca2791eb639 |
| Jogador 1 | 2-4 | 76 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 20.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32591983675956726 | 0.0 | 0.0 | +— / -6951a681-f5b9-4c22-9182-46b4d2c3cbb3 |
| Jogador 1 | 2-4 | 77 | BUY | STABILIZE | 95.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.4718901515007019 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 78 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 20.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 81 | BUY | STABILIZE | 95.0 | 5 | 5 | 0 | 20.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34822356700897217 | 0.0 | 0.0 | +0c9ac713-08bd-4fa7-a94a-2ab70d7815ff / -— |
| Jogador 1 | 2-5 | 82 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 2 | 0 | 20.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44432884454727173 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 83 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 2 | 0 | 20.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3960810601711273 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 84 | PASS | STABILIZE | 95.0 | 5 | 2 | 0 | 22.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 91 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 8 | 0 | 22.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004331194330006838 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 92 | BUY_XP | STABILIZE | 95.0 | 5 | 8 | 0 | 22.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19949999451637268 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 93 | BUY | STABILIZE | 95.0 | 6 | 4 | 0 | 22.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5408682227134705 | 0.0 | 0.0 | +af132466-c7bd-40ad-9848-b79d59a5915c / -— |
| Jogador 1 | 2-6 | 94 | SELL | STABILIZE | 95.0 | 6 | 3 | 0 | 22.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1629454642534256 | 0.0 | 0.0 | +— / -c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 2-6 | 95 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 6 | 0 | 22.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13268457353115082 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 96 | BUY | STABILIZE | 95.0 | 6 | 6 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12280292063951492 | 0.0 | 0.0 | +2fd4f2d8-6e40-439a-a96d-3e49e05779ad / -— |
| Jogador 1 | 2-6 | 97 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 3 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46772322058677673 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 98 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 3 | 0 | 24.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09461166709661484 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 99 | SELL | ECON | 95.0 | 6 | 3 | 0 | 28.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004649774171411991 | 0.0 | 0.0 | +— / -af132466-c7bd-40ad-9848-b79d59a5915c |
| Jogador 1 | 2-7 | 101 | BUY | ECON | 95.0 | 6 | 11 | 1 | 28.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30238568782806396 | 0.0 | 0.0 | +3fc2815d-c456-47c3-bb27-783336b3cdfa / -— |
| Jogador 1 | 2-7 | 102 | BUY_XP | ECON | 95.0 | 6 | 9 | 0 | 28.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 103 | BUY_XP | ECON | 95.0 | 6 | 5 | 0 | 28.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 104 | SELL | ECON | 95.0 | 6 | 1 | 0 | 28.0 | —/DA_18_Diana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012783775106072426 | 0.0 | 0.0 | +— / -3fc2815d-c456-47c3-bb27-783336b3cdfa |
| Jogador 1 | 2-7 | 105 | MOVE_BENCH | ECON | 95.0 | 6 | 3 | 0 | 28.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006491185165941715 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 106 | MOVE_BENCH | ECON | 95.0 | 6 | 3 | 0 | 28.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13015244901180267 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 107 | MOVE_BENCH | ECON | 95.0 | 6 | 3 | 0 | 28.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.023309605196118355 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 108 | MOVE_BENCH | ECON | 95.0 | 6 | 3 | 0 | 28.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3172355890274048 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 109 | MOVE_BENCH | ECON | 95.0 | 6 | 3 | 0 | 28.0 | —/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44899019598960876 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 111 | BUY | ECON | 95.0 | 6 | 9 | 0 | 28.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18258655071258545 | 0.0 | 0.0 | +7c218f01-e884-46da-8a1a-2d2db27a5ff1 / -— |
| Jogador 1 | 3-1 | 112 | MOVE_BENCH | ECON | 95.0 | 6 | 6 | 0 | 28.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06080060824751854 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 113 | BUY_XP | ECON | 95.0 | 6 | 6 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 114 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 2 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12418631464242935 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 115 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 2 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21886856853961945 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 116 | PASS | STABILIZE | 95.0 | 6 | 2 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 121 | BUY | STABILIZE | 95.0 | 6 | 9 | 0 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.038869746029376984 | 0.0 | 0.0 | +145f7470-8c0f-4957-b8d6-97939ddaeba1 / -— |
| Jogador 1 | 3-2 | 122 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 5 | 0 | 28.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5518643856048584 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 123 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 5 | 0 | 30.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07232574373483658 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 124 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 5 | 0 | 30.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32914650440216064 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 125 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 5 | 0 | 30.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12794546782970428 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 126 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 5 | 0 | 28.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0046433089300990105 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 127 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 5 | 0 | 30.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02114531211555004 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 128 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 5 | 0 | 28.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5236574411392212 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 129 | BUY_XP | STABILIZE | 95.0 | 6 | 5 | 0 | 30.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 131 | BUY | STABILIZE | 84.0 | 6 | 6 | 0 | 30.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7323612570762634 | 0.0 | 0.0 | +c30e7bdb-41d6-423c-9d7d-2e146472e724 / -— |
| Jogador 1 | 3-3 | 132 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 3 | 0 | 30.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30642756819725037 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 133 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 3 | 0 | 30.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2633146345615387 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 134 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 3 | 0 | 28.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17940767109394073 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 135 | SELL | STABILIZE | 84.0 | 6 | 3 | 0 | 28.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3111032247543335 | 0.0 | 0.0 | +— / -0c9ac713-08bd-4fa7-a94a-2ab70d7815ff |
| Jogador 1 | 3-3 | 136 | BUY_XP | STABILIZE | 84.0 | 6 | 6 | 0 | 28.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 137 | SELL | STABILIZE | 84.0 | 6 | 2 | 0 | 28.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09418918937444687 | 0.0 | 0.0 | +— / -2fd4f2d8-6e40-439a-a96d-3e49e05779ad |
| Jogador 1 | 3-3 | 138 | BUY_XP | STABILIZE | 84.0 | 6 | 5 | 0 | 28.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 139 | SELL | STABILIZE | 84.0 | 6 | 1 | 0 | 28.0 | Adaptador/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08446153998374939 | 0.0 | 0.0 | +— / -3a43ff36-dccd-49a7-92d8-0b01e739ea89 |
| Jogador 1 | 3-4 | 141 | BUY | STABILIZE | 74.0 | 6 | 10 | 1 | 28.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20110833644866943 | 0.0 | 0.0 | +c07fa6e1-195e-4a06-ba8f-b75213704c8a / -— |
| Jogador 1 | 3-4 | 142 | BUY_XP | STABILIZE | 74.0 | 6 | 9 | 0 | 28.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4320000112056732 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 143 | BUY | STABILIZE | 74.0 | 7 | 5 | 0 | 28.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031560253351926804 | 0.0 | 0.0 | +bddefab1-7dd7-4954-816c-45dbd44b947b / -— |
| Jogador 1 | 3-4 | 144 | SELL | STABILIZE | 74.0 | 7 | 3 | 0 | 28.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11110563576221466 | 0.0 | 0.0 | +— / -c07fa6e1-195e-4a06-ba8f-b75213704c8a |
| Jogador 1 | 3-4 | 145 | BUY_XP | STABILIZE | 74.0 | 7 | 4 | 0 | 28.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 146 | SELL | STABILIZE | 74.0 | 7 | 0 | 0 | 28.0 | Adaptador/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1331278681755066 | 0.0 | 0.0 | +— / -bddefab1-7dd7-4954-816c-45dbd44b947b |
| Jogador 1 | 3-4 | 147 | MOVE_BENCH | STABILIZE | 74.0 | 7 | 2 | 0 | 28.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11913641542196274 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 148 | MOVE_BENCH | STABILIZE | 74.0 | 7 | 2 | 0 | 30.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4449707269668579 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 149 | MOVE_BOARD | STABILIZE | 74.0 | 7 | 2 | 0 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0423082634806633 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 151 | BUY | STABILIZE | 74.0 | 7 | 8 | 0 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.5821817517280579 | 0.0 | 0.0 | +727765c8-7f02-491e-a6da-12b0dab59f6d / -— |
| Jogador 1 | 3-5 | 152 | BUY | STABILIZE | 74.0 | 7 | 5 | 0 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05921978875994682 | 0.0 | 0.0 | +c5557e24-8174-4d79-9e22-c2cbbb8225a8 / -— |
| Jogador 1 | 3-5 | 153 | SELL | STABILIZE | 74.0 | 7 | 3 | 0 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1360221952199936 | 0.0 | 0.0 | +— / -c5557e24-8174-4d79-9e22-c2cbbb8225a8 |
| Jogador 1 | 3-5 | 154 | BUY_XP | STABILIZE | 74.0 | 7 | 5 | 0 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 155 | MOVE_BOARD | STABILIZE | 74.0 | 7 | 1 | 0 | 36.0 | Adaptador/DA_18_Ezreal | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12111096829175949 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 156 | MOVE_BOARD | STABILIZE | 74.0 | 7 | 1 | 0 | 36.0 | Adaptador/DA_18_Ezreal | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1394921988248825 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 157 | SELL | STABILIZE | 74.0 | 7 | 1 | 0 | 36.0 | Adaptador/DA_18_Ezreal | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6321817636489868 | 0.0 | 0.0 | +— / -727765c8-7f02-491e-a6da-12b0dab59f6d |
| Jogador 1 | 3-5 | 158 | BUY_XP | STABILIZE | 74.0 | 7 | 4 | 0 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 159 | MOVE_BOARD | STABILIZE | 74.0 | 7 | 0 | 0 | 36.0 | Adaptador/DA_18_Ezreal | MOVE_BOARD, PASS | True | True | -0.2862316966056824 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 161 | BUY | STABILIZE | 74.0 | 7 | 6 | 0 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.28059419989585876 | 0.0 | 0.0 | +4518ad1d-87e7-4110-830a-96183c533201 / -— |
| Jogador 1 | 3-6 | 162 | BUY | STABILIZE | 74.0 | 7 | 2 | 0 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4386007785797119 | 0.0 | 0.0 | +da5abe09-7f54-4361-8d82-84427a9da9e1 / -— |
| Jogador 1 | 3-6 | 163 | MOVE_BENCH | STABILIZE | 74.0 | 7 | 0 | 0 | 36.0 | Adaptador/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5626274943351746 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 164 | MOVE_BENCH | STABILIZE | 74.0 | 7 | 0 | 0 | 32.0 | Adaptador/DA_Nidalee18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24050243198871613 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 165 | PASS | STABILIZE | 74.0 | 7 | 0 | 0 | 34.0 | Adaptador/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 171 | BUY | STABILIZE | 63.0 | 7 | 5 | 0 | 34.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7439784407615662 | 0.0 | 0.0 | +227dbcdb-af5c-4318-94d1-f01a7847d100 / -— |
| Jogador 1 | 3-7 | 172 | MOVE_BENCH | STABILIZE | 63.0 | 7 | 2 | 0 | 34.0 | Adaptador/DA_18_Ezreal | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1840580552816391 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 173 | SELL | STABILIZE | 63.0 | 7 | 2 | 0 | 38.0 | Adaptador/DA_18_Ezreal | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16350248456001282 | 0.0 | 0.0 | +— / -da5abe09-7f54-4361-8d82-84427a9da9e1 |
| Jogador 1 | 3-7 | 174 | BUY_XP | STABILIZE | 63.0 | 7 | 4 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 175 | SELL | STABILIZE | 63.0 | 7 | 0 | 0 | 38.0 | Adaptador/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04164990782737732 | 0.0 | 0.0 | +— / -c30e7bdb-41d6-423c-9d7d-2e146472e724 |
| Jogador 1 | 3-7 | 176 | BUY | STABILIZE | 63.0 | 7 | 3 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22267229855060577 | 0.0 | 0.0 | +c8968d39-6c58-42c5-a3aa-a5643e7ec8d5 / -— |
| Jogador 1 | 3-7 | 177 | MOVE_BENCH | STABILIZE | 63.0 | 7 | 0 | 0 | 38.0 | Adaptador/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.042053189128637314 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 178 | MOVE_BENCH | STABILIZE | 63.0 | 7 | 0 | 0 | 36.0 | Adaptador/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13597697019577026 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 179 | MOVE_BENCH | STABILIZE | 63.0 | 7 | 0 | 0 | 36.0 | Adaptador/DA_Nidalee18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04941003397107124 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 181 | BUY | STABILIZE | 63.0 | 7 | 5 | 0 | 38.0 | Adaptador/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.17108066380023956 | 0.0 | 0.0 | +844f869e-0e0e-423a-8507-27efd66131f5 / -— |
| Jogador 1 | 4-1 | 182 | CRAFT_AND_EQUIP | STABILIZE | 63.0 | 7 | 2 | 0 | 38.0 | Adaptador/DA_Nidalee18_AP | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14626111090183258 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 183 | SELL | STABILIZE | 63.0 | 7 | 2 | 0 | 38.0 | Adaptador/DA_Nidalee18_AP | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22108066082000732 | 0.0 | 0.0 | +— / -844f869e-0e0e-423a-8507-27efd66131f5 |
| Jogador 1 | 4-1 | 184 | MOVE_BENCH | STABILIZE | 63.0 | 7 | 5 | 0 | 38.0 | Adaptador/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022568851709365845 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 185 | MOVE_BENCH | STABILIZE | 63.0 | 7 | 5 | 0 | 36.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06711000949144363 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 186 | BUY | STABILIZE | 63.0 | 7 | 5 | 0 | 36.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11288758367300034 | 0.0 | 0.0 | +e7c8751e-5d30-4953-9508-35488b6c45db / -— |
| Jogador 1 | 4-1 | 187 | SELL | STABILIZE | 63.0 | 7 | 2 | 0 | 36.0 | Adaptador/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12600000202655792 | 0.0 | 0.0 | +— / -e7c8751e-5d30-4953-9508-35488b6c45db |
| Jogador 1 | 4-1 | 188 | MOVE_BENCH | STABILIZE | 63.0 | 7 | 5 | 0 | 36.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49507150053977966 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 189 | BUY_XP | STABILIZE | 63.0 | 7 | 5 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 191 | BUY | STABILIZE | 49.0 | 7 | 7 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7424592971801758 | 0.0 | 0.0 | +5af104f2-7959-4ca5-91a9-7d44494532ea / -— |
| Jogador 1 | 4-2 | 192 | BUY | STABILIZE | 49.0 | 7 | 4 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2700323760509491 | 0.0 | 0.0 | +301afc05-ad23-4ed2-a835-108235c399e0 / -— |
| Jogador 1 | 4-2 | 193 | MOVE_BENCH | STABILIZE | 49.0 | 7 | 1 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028347907587885857 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 194 | MOVE_BENCH | STABILIZE | 49.0 | 7 | 1 | 0 | 36.0 | Adaptador/DA_18_Ezreal | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013184738345444202 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 195 | PASS | STABILIZE | 49.0 | 7 | 1 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 201 | BUY | STABILIZE | 37.0 | 7 | 7 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.049258001148700714 | 0.0 | 0.0 | +6388773b-0e99-40a9-8d68-895dcf16fce6 / -— |
| Jogador 1 | 4-3 | 202 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 3 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11609400063753128 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 203 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 3 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5406990051269531 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 204 | PASS | STABILIZE | 37.0 | 7 | 3 | 0 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 211 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 9 | 0 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04675581678748131 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 212 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 9 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12504827976226807 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 213 | BUY_XP | STABILIZE | 37.0 | 7 | 9 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 214 | BUY_XP | STABILIZE | 37.0 | 7 | 5 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 215 | SELL | STABILIZE | 37.0 | 7 | 1 | 0 | 38.0 | Adaptador/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3687237799167633 | 0.0 | 0.0 | +— / -227dbcdb-af5c-4318-94d1-f01a7847d100 |
| Jogador 1 | 4-4 | 216 | BUY_XP | STABILIZE | 37.0 | 7 | 4 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 217 | SELL | STABILIZE | 37.0 | 7 | 0 | 0 | 38.0 | Adaptador/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10041514039039612 | 0.0 | 0.0 | +— / -301afc05-ad23-4ed2-a835-108235c399e0 |
| Jogador 1 | 4-4 | 218 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 3 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07660790532827377 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 219 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 3 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011134089902043343 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 221 | BUY | STABILIZE | 37.0 | 7 | 8 | 0 | 40.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1813334971666336 | 0.0 | 0.0 | +42cf45df-f7dd-418d-a241-d89e69523352 / -— |
| Jogador 1 | 4-5 | 222 | BUY_XP | STABILIZE | 37.0 | 7 | 4 | 0 | 40.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 223 | SELL | STABILIZE | 37.0 | 7 | 0 | 0 | 40.0 | Adaptador/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03507189825177193 | 0.0 | 0.0 | +— / -c8968d39-6c58-42c5-a3aa-a5643e7ec8d5 |
| Jogador 1 | 4-5 | 224 | EQUIP_FROM_INVENTORY | STABILIZE | 37.0 | 7 | 3 | 0 | 40.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.10245753079652786 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 225 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 3 | 0 | 40.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03340361639857292 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 226 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 3 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6445139646530151 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 227 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 3 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06549765169620514 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 228 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 3 | 0 | 40.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2746867537498474 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 229 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 3 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0729684978723526 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 231 | BUY | STABILIZE | 25.0 | 8 | 8 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.736752986907959 | 0.0 | 0.0 | +4c1dab77-0e6d-401b-a341-40117b445957 / -— |
| Jogador 1 | 4-6 | 232 | MOVE_BENCH | STABILIZE | 25.0 | 8 | 4 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003171474440023303 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 233 | MOVE_BENCH | STABILIZE | 25.0 | 8 | 4 | 0 | 38.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4824233055114746 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 234 | MOVE_BENCH | STABILIZE | 25.0 | 8 | 4 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12447119504213333 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 235 | BUY | STABILIZE | 25.0 | 8 | 4 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.272709459066391 | 0.0 | 0.0 | +9717d30c-f073-470c-a6ce-7db8257de559 / -— |
| Jogador 1 | 4-6 | 236 | SELL | STABILIZE | 25.0 | 8 | 1 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09996923059225082 | 0.0 | 0.0 | +— / -9717d30c-f073-470c-a6ce-7db8257de559 |
| Jogador 1 | 4-6 | 237 | BUY_XP | STABILIZE | 25.0 | 8 | 4 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 238 | SELL | STABILIZE | 25.0 | 8 | 0 | 0 | 46.0 | Adaptador/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3180615305900574 | 0.0 | 0.0 | +— / -5af104f2-7959-4ca5-91a9-7d44494532ea |
| Jogador 1 | 4-6 | 239 | MOVE_BENCH | STABILIZE | 25.0 | 8 | 3 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01598612405359745 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 241 | BUY | STABILIZE | 25.0 | 8 | 9 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6962260007858276 | 0.0 | 0.0 | +b0c1aba5-b1bd-48df-abec-19efa8e49d6d / -— |
| Jogador 1 | 4-7 | 242 | BUY_XP | STABILIZE | 25.0 | 8 | 5 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 243 | SELL | STABILIZE | 25.0 | 8 | 1 | 0 | 46.0 | Adaptador/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03671645000576973 | 0.0 | 0.0 | +— / -42cf45df-f7dd-418d-a241-d89e69523352 |
| Jogador 1 | 4-7 | 244 | BUY | STABILIZE | 25.0 | 8 | 5 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0951039120554924 | 0.0 | 0.0 | +6ea982ab-292d-42fc-99e6-d67c89f9f4fe / -— |
| Jogador 1 | 4-7 | 245 | SELL | STABILIZE | 25.0 | 8 | 1 | 0 | 46.0 | Adaptador/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14510391652584076 | 0.0 | 0.0 | +— / -6ea982ab-292d-42fc-99e6-d67c89f9f4fe |
| Jogador 1 | 4-7 | 246 | MOVE_BENCH | STABILIZE | 25.0 | 8 | 5 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07780452072620392 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 247 | BUY_XP | STABILIZE | 25.0 | 8 | 5 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 248 | SELL | STABILIZE | 25.0 | 8 | 1 | 0 | 46.0 | Adaptador/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14406219124794006 | 0.0 | 0.0 | +— / -4518ad1d-87e7-4110-830a-96183c533201 |
| Jogador 1 | 4-7 | 249 | BUY_XP | STABILIZE | 25.0 | 8 | 5 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 251 | EQUIP_FROM_INVENTORY | STABILIZE | 25.0 | 8 | 6 | 0 | 46.0 | Adaptador/DA_18_Ezreal | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 252 | BUY | STABILIZE | 25.0 | 8 | 6 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7439781427383423 | 0.0 | 0.0 | +aaebedb3-18bf-4ae6-948e-7b326b573f1c / -— |
| Jogador 1 | 5-1 | 253 | MOVE_BENCH | STABILIZE | 25.0 | 8 | 3 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.023635659366846085 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 254 | BUY | STABILIZE | 25.0 | 8 | 3 | 0 | 44.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020088359713554382 | 0.0 | 0.0 | +3c59d736-011d-480c-a9af-1df7a3b4caab / -— |
| Jogador 1 | 5-1 | 255 | SELL | STABILIZE | 25.0 | 8 | 0 | 0 | 44.0 | Adaptador/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12452307343482971 | 0.0 | 0.0 | +— / -3c59d736-011d-480c-a9af-1df7a3b4caab |
| Jogador 1 | 5-1 | 256 | MOVE_BENCH | STABILIZE | 25.0 | 8 | 3 | 0 | 44.0 | Adaptador/DA_18_Ezreal | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008561530150473118 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 257 | MOVE_BENCH | STABILIZE | 25.0 | 8 | 3 | 0 | 44.0 | Adaptador/DA_18_Ezreal | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3286628723144531 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 258 | PASS | STABILIZE | 25.0 | 8 | 3 | 0 | 46.0 | Adaptador/DA_18_Ezreal | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 261 | BUY | STABILIZE | 25.0 | 8 | 8 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03189020976424217 | 0.0 | 0.0 | +ff181737-4995-4a67-add2-4f55cebabbee / -— |
| Jogador 1 | 5-2 | 262 | BUY_XP | STABILIZE | 25.0 | 8 | 4 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 263 | SELL | STABILIZE | 25.0 | 8 | 0 | 0 | 46.0 | Adaptador/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3686547875404358 | 0.0 | 0.0 | +— / -aaebedb3-18bf-4ae6-948e-7b326b573f1c |
| Jogador 1 | 5-2 | 264 | MOVE_BENCH | STABILIZE | 25.0 | 8 | 3 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15553322434425354 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 265 | MOVE_BENCH | STABILIZE | 25.0 | 8 | 3 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08368748426437378 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 266 | SELL | STABILIZE | 25.0 | 8 | 3 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3027506470680237 | 0.0 | 0.0 | +— / -6388773b-0e99-40a9-8d68-895dcf16fce6 |
| Jogador 1 | 5-2 | 267 | EQUIP_FROM_INVENTORY | STABILIZE | 25.0 | 8 | 7 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1080564558506012 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 268 | MOVE_BENCH | STABILIZE | 25.0 | 8 | 7 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2802780270576477 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 269 | MOVE_BENCH | STABILIZE | 25.0 | 8 | 7 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01677880622446537 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 271 | BUY | ALL_IN | 7.0 | 8 | 12 | 1 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6537217497825623 | 0.0 | 0.0 | +7313188a-ce84-4a52-b2d0-a94b2c420cdb / -— |
| Jogador 1 | 5-3 | 272 | BUY | ALL_IN | 7.0 | 8 | 9 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06314150243997574 | 0.0 | 0.0 | +6c338d19-b3d3-49a7-b61e-4732249ee457 / -— |
| Jogador 1 | 5-3 | 273 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 5 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03207315877079964 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 274 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 5 | 0 | 44.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13181419670581818 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 275 | PASS | ALL_IN | 7.0 | 8 | 5 | 0 | 44.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 281 | BUY | ALL_IN | 7.0 | 8 | 11 | 1 | 44.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16872724890708923 | 0.0 | 0.0 | +64215569-2a69-410d-a2f9-172544bef858 / -— |
| Jogador 1 | 5-4 | 282 | BUY_XP | ALL_IN | 7.0 | 8 | 9 | 0 | 44.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 283 | BUY_XP | ALL_IN | 7.0 | 8 | 5 | 0 | 44.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 284 | SELL | ALL_IN | 7.0 | 8 | 1 | 0 | 44.0 | Adaptador/DA_18_Ezreal | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09403076767921448 | 0.0 | 0.0 | +— / -64215569-2a69-410d-a2f9-172544bef858 |
| Jogador 1 | 5-4 | 285 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 3 | 0 | 44.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03213702514767647 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 286 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 3 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0008606823394075036 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 287 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 3 | 0 | 44.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13160493969917297 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 288 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 3 | 0 | 44.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1901450902223587 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 289 | PASS | ALL_IN | 7.0 | 8 | 3 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 291 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 8 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02783990651369095 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 292 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 8 | 0 | 44.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17824454605579376 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 293 | PASS | ALL_IN | 7.0 | 8 | 8 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 301 | BUY | ALL_IN | 7.0 | 8 | 15 | 1 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26034778356552124 | 0.0 | 0.0 | +bbfa514f-8d07-411b-aa19-4511ae5fb5cd / -— |
| Jogador 1 | 5-6 | 302 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 12 | 1 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04871615767478943 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 303 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 12 | 1 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3020811080932617 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 304 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 12 | 1 | 44.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4502588212490082 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 305 | BUY_XP | ALL_IN | 7.0 | 8 | 12 | 1 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 306 | BUY_XP | ALL_IN | 7.0 | 8 | 8 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 307 | BUY_XP | ALL_IN | 7.0 | 8 | 4 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 308 | SELL | ALL_IN | 7.0 | 8 | 0 | 0 | 46.0 | Adaptador/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09996923059225082 | 0.0 | 0.0 | +— / -bbfa514f-8d07-411b-aa19-4511ae5fb5cd |
| Jogador 1 | 5-6 | 309 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 3 | 0 | 46.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02783990651369095 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 311 | PASS | ALL_IN | 0.0 | 8 | 3 | 0 | 0.0 | Adaptador/DA_18_Ezreal | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 321 | PASS | ALL_IN | 0.0 | 8 | 3 | 0 | 0.0 | Adaptador/DA_18_Ezreal | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 331 | PASS | ALL_IN | 0.0 | 8 | 3 | 0 | 0.0 | Adaptador/DA_18_Ezreal | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.04556922987103462 | 0.0 | 0.0 | +— / -fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.22450661659240723 | 0.0 | 0.0 | +292ef825-d326-4dd8-9c42-c47cfc62116f / -— |
| Jogador 2 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 9 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.27265432476997375 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9709054827690125 | 0.0 | 0.0 | +94ede66e-59bc-4c41-aabf-f64372e20f9a / -— |
| Jogador 2 | 1-2 | 12 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26868247985839844 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1785006821155548 | 0.0 | 0.0 | +de00430a-8a57-423c-887c-317d53c2cdd3 / -— |
| Jogador 2 | 1-3 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6232665777206421 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 23 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Sejuani | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1179635524749756 | 0.0 | 0.0 | +0023ba20-d605-41fb-8002-3b6920635c59 / -292ef825-d326-4dd8-9c42-c47cfc62116f,94ede66e-59bc-4c41-aabf-f64372e20f9a |
| Jogador 2 | 1-4 | 32 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 39 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2872958779335022 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.34641340374946594 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 42 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019549621269106865 | 0.0 | 0.0 | +18082e05-51e8-4142-b541-c3d7d781b878 / -— |
| Jogador 2 | 2-1 | 43 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06651980429887772 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 44 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2690715491771698 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 45 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 14.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 49 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 14.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35111191868782043 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 51 | BUY | STABILIZE | 95.0 | 4 | 7 | 0 | 18.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.5336662530899048 | 0.0 | 0.0 | +7ca9b803-76eb-4283-9648-7f98bfd81149 / -— |
| Jogador 2 | 2-2 | 52 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 6 | 0 | 18.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05065076798200607 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 53 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 14.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9628644585609436 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 54 | BUY_XP | STABILIZE | 95.0 | 4 | 4 | 0 | 14.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 55 | PASS | STABILIZE | 95.0 | 4 | 0 | 0 | 14.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 61 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 6 | 0 | 14.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12545883655548096 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 62 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 6 | 0 | 16.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02261226624250412 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 63 | BUY_XP | STABILIZE | 90.0 | 4 | 6 | 0 | 18.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44699999690055847 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 64 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 2 | 0 | 18.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5455624461174011 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 65 | BUY | STABILIZE | 90.0 | 5 | 2 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.018599102273583412 | 0.0 | 0.0 | +95dad944-37ad-4a7a-ab57-8b92635fb4b2 / -— |
| Jogador 2 | 2-3 | 66 | PASS | STABILIZE | 90.0 | 5 | 0 | 0 | 20.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 71 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 6 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17074348032474518 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 72 | BUY | STABILIZE | 90.0 | 5 | 6 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.430963933467865 | 0.0 | 0.0 | +2ace989d-3e9e-483b-9b14-cd6b8f171f17 / -— |
| Jogador 2 | 2-4 | 73 | PASS | STABILIZE | 90.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 81 | BUY_XP | STABILIZE | 90.0 | 5 | 8 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 82 | BUY_XP | STABILIZE | 90.0 | 5 | 4 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 83 | SELL | STABILIZE | 90.0 | 5 | 0 | 0 | 20.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17864751815795898 | 0.0 | 0.0 | +— / -de00430a-8a57-423c-887c-317d53c2cdd3 |
| Jogador 2 | 2-5 | 84 | PASS | STABILIZE | 90.0 | 5 | 2 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 91 | BUY_XP | STABILIZE | 84.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19949999451637268 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 92 | BUY | STABILIZE | 84.0 | 6 | 3 | 0 | 20.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3765043020248413 | 0.0 | 0.0 | +97fc5647-5995-4f21-aa03-13454546919a / -— |
| Jogador 2 | 2-6 | 93 | PASS | STABILIZE | 84.0 | 6 | 0 | 0 | 20.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 99 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 0 | 0 | 20.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5454333424568176 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 101 | BUY | STABILIZE | 77.0 | 6 | 6 | 0 | 26.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07789697498083115 | 0.0 | 0.0 | +729ccd5b-adc5-4bca-9523-dcb532e93ecb / -— |
| Jogador 2 | 2-7 | 102 | MOVE_BENCH | STABILIZE | 77.0 | 6 | 2 | 0 | 26.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3043317496776581 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 103 | MOVE_BENCH | STABILIZE | 77.0 | 6 | 2 | 0 | 28.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48060792684555054 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 104 | SELL | STABILIZE | 77.0 | 6 | 2 | 0 | 30.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029134394600987434 | 0.0 | 0.0 | +— / -561fb9a8-e987-4935-b11c-6c6104ced65d |
| Jogador 2 | 2-7 | 105 | BUY_XP | STABILIZE | 77.0 | 6 | 4 | 0 | 30.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 106 | SELL | STABILIZE | 77.0 | 6 | 0 | 0 | 30.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.053661540150642395 | 0.0 | 0.0 | +— / -95dad944-37ad-4a7a-ab57-8b92635fb4b2 |
| Jogador 2 | 2-7 | 107 | MOVE_BENCH | STABILIZE | 77.0 | 6 | 2 | 0 | 30.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.043959829956293106 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 108 | SELL | STABILIZE | 77.0 | 6 | 2 | 0 | 34.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1489078849554062 | 0.0 | 0.0 | +— / -7ca9b803-76eb-4283-9648-7f98bfd81149 |
| Jogador 2 | 2-7 | 109 | BUY | STABILIZE | 77.0 | 6 | 3 | 0 | 34.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.10225152969360352 | 0.0 | 0.0 | +6340ebaf-bd41-4f47-bdce-50e06faa4044 / -— |
| Jogador 2 | 3-1 | 111 | BUY | STABILIZE | 77.0 | 6 | 7 | 0 | 34.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28781694173812866 | 0.0 | 0.0 | +a0ebc646-2e71-4b07-9208-401aa0cda6bb / -— |
| Jogador 2 | 3-1 | 112 | BUY_XP | STABILIZE | 77.0 | 6 | 6 | 0 | 34.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 113 | SELL | STABILIZE | 77.0 | 6 | 2 | 0 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17800000309944153 | 0.0 | 0.0 | +— / -a0ebc646-2e71-4b07-9208-401aa0cda6bb |
| Jogador 2 | 3-1 | 114 | MOVE_BENCH | STABILIZE | 77.0 | 6 | 3 | 0 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5731297135353088 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 115 | BUY | STABILIZE | 77.0 | 6 | 3 | 0 | 32.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04536806792020798 | 0.0 | 0.0 | +e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 / -— |
| Jogador 2 | 3-1 | 116 | PASS | STABILIZE | 77.0 | 6 | 0 | 0 | 32.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 121 | MOVE_BENCH | STABILIZE | 77.0 | 6 | 6 | 0 | 32.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09802059084177017 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 122 | BUY | STABILIZE | 77.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28798508644104004 | 0.0 | 0.0 | +584e7960-a541-4d45-8ea1-8a75e288c387 / -— |
| Jogador 2 | 3-2 | 123 | BUY_XP | STABILIZE | 77.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 124 | SELL | STABILIZE | 77.0 | 6 | 1 | 0 | 30.0 | Colosso/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16969230771064758 | 0.0 | 0.0 | +— / -584e7960-a541-4d45-8ea1-8a75e288c387 |
| Jogador 2 | 3-2 | 125 | MOVE_BENCH | STABILIZE | 77.0 | 6 | 2 | 0 | 30.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14549122750759125 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 126 | SELL | STABILIZE | 77.0 | 6 | 2 | 0 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0599384605884552 | 0.0 | 0.0 | +— / -6340ebaf-bd41-4f47-bdce-50e06faa4044 |
| Jogador 2 | 3-2 | 127 | BUY_XP | STABILIZE | 77.0 | 6 | 4 | 0 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 128 | SELL | STABILIZE | 77.0 | 6 | 0 | 0 | 34.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.059340570122003555 | 0.0 | 0.0 | +— / -e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 |
| Jogador 2 | 3-2 | 129 | MOVE_BOARD | STABILIZE | 77.0 | 6 | 3 | 0 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.16937078535556793 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 131 | BUY | STABILIZE | 77.0 | 6 | 10 | 1 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.05210873484611511 | 0.0 | 0.0 | +4e116bc2-f686-4a17-adb1-a7b80865c159 / -— |
| Jogador 2 | 3-3 | 132 | BUY | STABILIZE | 77.0 | 6 | 6 | 0 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04036112129688263 | 0.0 | 0.0 | +e658854d-c531-46fc-8978-067953930510 / -— |
| Jogador 2 | 3-3 | 133 | SELL | STABILIZE | 77.0 | 6 | 3 | 0 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12969230115413666 | 0.0 | 0.0 | +— / -e658854d-c531-46fc-8978-067953930510 |
| Jogador 2 | 3-3 | 134 | BUY_XP | STABILIZE | 77.0 | 6 | 6 | 0 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 135 | SELL | STABILIZE | 77.0 | 6 | 2 | 0 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28110769391059875 | 0.0 | 0.0 | +— / -4e116bc2-f686-4a17-adb1-a7b80865c159 |
| Jogador 2 | 3-3 | 136 | BUY_XP | STABILIZE | 77.0 | 6 | 6 | 0 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 137 | PASS | STABILIZE | 77.0 | 6 | 2 | 0 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 141 | BUY | STABILIZE | 77.0 | 6 | 9 | 0 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.01495619211345911 | 0.0 | 0.0 | +8edef2b0-f5b3-4c01-ba2b-851be248676e / -— |
| Jogador 2 | 3-4 | 142 | BUY_XP | STABILIZE | 77.0 | 6 | 7 | 0 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4269999861717224 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 143 | BUY | STABILIZE | 77.0 | 7 | 3 | 0 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07619286328554153 | 0.0 | 0.0 | +c4c0b136-020d-4c1e-9517-8e0bf4c5a628 / -— |
| Jogador 2 | 3-4 | 144 | SELL | STABILIZE | 77.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12006153911352158 | 0.0 | 0.0 | +— / -c4c0b136-020d-4c1e-9517-8e0bf4c5a628 |
| Jogador 2 | 3-4 | 145 | MOVE_BENCH | STABILIZE | 77.0 | 7 | 3 | 0 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33910244703292847 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 146 | BUY | STABILIZE | 77.0 | 7 | 3 | 0 | 30.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06126975268125534 | 0.0 | 0.0 | +c02b6467-3a23-4da6-bca3-06ae415a9998 / -— |
| Jogador 2 | 3-4 | 147 | SELL | STABILIZE | 77.0 | 7 | 1 | 0 | 30.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12006153911352158 | 0.0 | 0.0 | +— / -c02b6467-3a23-4da6-bca3-06ae415a9998 |
| Jogador 2 | 3-4 | 148 | BUY | STABILIZE | 77.0 | 7 | 3 | 0 | 30.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26776134967803955 | 0.0 | 0.0 | +ff0d9869-c346-4210-be85-1e802a25dd8b / -— |
| Jogador 2 | 3-4 | 149 | MOVE_BENCH | STABILIZE | 77.0 | 7 | 1 | 0 | 30.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4756135642528534 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 151 | MOVE_BENCH | STABILIZE | 77.0 | 7 | 7 | 0 | 38.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3242388367652893 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 152 | MOVE_BENCH | STABILIZE | 77.0 | 7 | 7 | 0 | 38.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33910244703292847 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 153 | PASS | STABILIZE | 77.0 | 7 | 7 | 0 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 161 | BUY | STABILIZE | 65.0 | 7 | 12 | 1 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09059476852416992 | 0.0 | 0.0 | +23157bd6-5e8f-4416-bb7f-2e5d71a06543 / -— |
| Jogador 2 | 3-6 | 162 | BUY | STABILIZE | 65.0 | 7 | 8 | 0 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04482857882976532 | 0.0 | 0.0 | +8fb80cc8-4120-41a0-bc96-35f81a466ed9 / -— |
| Jogador 2 | 3-6 | 163 | BUY_XP | STABILIZE | 65.0 | 7 | 5 | 0 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 164 | SELL | STABILIZE | 65.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1271163672208786 | 0.0 | 0.0 | +— / -8fb80cc8-4120-41a0-bc96-35f81a466ed9 |
| Jogador 2 | 3-6 | 165 | MOVE_BENCH | STABILIZE | 65.0 | 7 | 4 | 0 | 34.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09872998297214508 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 166 | BUY_XP | STABILIZE | 65.0 | 7 | 4 | 0 | 38.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 167 | SELL | STABILIZE | 65.0 | 7 | 0 | 0 | 38.0 | Colosso/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06400000303983688 | 0.0 | 0.0 | +— / -ff0d9869-c346-4210-be85-1e802a25dd8b |
| Jogador 2 | 3-6 | 168 | MOVE_BENCH | STABILIZE | 65.0 | 7 | 2 | 0 | 38.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0670967772603035 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 169 | MOVE_BENCH | STABILIZE | 65.0 | 7 | 2 | 0 | 38.0 | Colosso/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36369040608406067 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 171 | BUY | STABILIZE | 65.0 | 7 | 8 | 0 | 40.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7415425777435303 | 0.0 | 0.0 | +e0445166-70a5-4135-a45e-ff238a95b228 / -— |
| Jogador 2 | 3-7 | 172 | MOVE_BENCH | STABILIZE | 65.0 | 7 | 4 | 0 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05397601053118706 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 173 | BUY | STABILIZE | 65.0 | 7 | 4 | 0 | 38.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11828343570232391 | 0.0 | 0.0 | +392a7da1-290c-48d8-81c8-206aa6823d5b / -— |
| Jogador 2 | 3-7 | 174 | SELL | STABILIZE | 65.0 | 7 | 1 | 0 | 38.0 | Colosso/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16828343272209167 | 0.0 | 0.0 | +— / -392a7da1-290c-48d8-81c8-206aa6823d5b |
| Jogador 2 | 3-7 | 175 | MOVE_BENCH | STABILIZE | 65.0 | 7 | 4 | 0 | 38.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05101418495178223 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 176 | BUY_XP | STABILIZE | 65.0 | 7 | 4 | 0 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 177 | SELL | STABILIZE | 65.0 | 7 | 0 | 0 | 40.0 | Colosso/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1250571459531784 | 0.0 | 0.0 | +— / -3eefd13b-5716-4917-a616-c3589f115098 |
| Jogador 2 | 3-7 | 178 | MOVE_BENCH | STABILIZE | 65.0 | 7 | 3 | 0 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05170787498354912 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 179 | MOVE_BENCH | STABILIZE | 65.0 | 7 | 3 | 0 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05355670675635338 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 181 | BUY | STABILIZE | 65.0 | 7 | 8 | 0 | 44.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06232926622033119 | 0.0 | 0.0 | +59304448-26ee-4e38-a52e-014e22ece127 / -— |
| Jogador 2 | 4-1 | 182 | BUY_XP | STABILIZE | 65.0 | 7 | 4 | 0 | 44.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 183 | SELL | STABILIZE | 65.0 | 7 | 0 | 0 | 44.0 | Colosso/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04087424278259277 | 0.0 | 0.0 | +— / -8edef2b0-f5b3-4c01-ba2b-851be248676e |
| Jogador 2 | 4-1 | 184 | SELL | STABILIZE | 65.0 | 7 | 2 | 0 | 44.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11790769547224045 | 0.0 | 0.0 | +— / -59304448-26ee-4e38-a52e-014e22ece127 |
| Jogador 2 | 4-1 | 185 | BUY_XP | STABILIZE | 65.0 | 7 | 6 | 0 | 44.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 186 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 2 | 0 | 44.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1790105551481247 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 187 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 2 | 0 | 44.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.3262505829334259 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 188 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 2 | 0 | 44.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1427917331457138 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 189 | MOVE_BOARD | STABILIZE | 65.0 | 7 | 2 | 0 | 44.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.003927947953343391 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 191 | BUY | STABILIZE | 52.0 | 7 | 7 | 0 | 44.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7084878087043762 | 0.0 | 0.0 | +23793b7b-2dab-48f0-a8ba-db85fc14c1c5 / -— |
| Jogador 2 | 4-2 | 192 | MOVE_BENCH | STABILIZE | 52.0 | 7 | 5 | 0 | 44.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0014973036013543606 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 193 | BUY | STABILIZE | 52.0 | 7 | 5 | 0 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28676125407218933 | 0.0 | 0.0 | +b7e13ed2-571b-4245-ba21-401b1eef8660 / -— |
| Jogador 2 | 4-2 | 194 | BUY_XP | STABILIZE | 52.0 | 7 | 4 | 0 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 195 | SELL | STABILIZE | 52.0 | 7 | 0 | 0 | 40.0 | Colosso/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14058421552181244 | 0.0 | 0.0 | +— / -b7e13ed2-571b-4245-ba21-401b1eef8660 |
| Jogador 2 | 4-2 | 196 | MOVE_BENCH | STABILIZE | 52.0 | 7 | 1 | 0 | 40.0 | Colosso/DA_18_Lillia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6591129302978516 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 197 | SELL | STABILIZE | 52.0 | 7 | 1 | 0 | 42.0 | Colosso/DA_18_Lillia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12248267233371735 | 0.0 | 0.0 | +— / -2ace989d-3e9e-483b-9b14-cd6b8f171f17 |
| Jogador 2 | 4-2 | 198 | BUY_XP | STABILIZE | 52.0 | 7 | 4 | 0 | 42.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 199 | MOVE_BOARD | STABILIZE | 52.0 | 7 | 0 | 0 | 42.0 | Colosso/DA_18_Lillia | MOVE_BOARD, PASS | True | True | 0.17234109342098236 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 201 | BUY | STABILIZE | 40.0 | 7 | 6 | 0 | 42.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.13323462009429932 | 0.0 | 0.0 | +caf1c554-2223-4090-9f96-b551e5c579ce / -— |
| Jogador 2 | 4-3 | 202 | MOVE_BENCH | STABILIZE | 40.0 | 7 | 3 | 0 | 42.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006791628897190094 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 203 | MOVE_BENCH | STABILIZE | 40.0 | 7 | 3 | 0 | 44.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0021339128725230694 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 204 | BUY | STABILIZE | 40.0 | 7 | 3 | 0 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04733160883188248 | 0.0 | 0.0 | +104aaac3-252c-4c1b-9ad8-fc10a35c6cda / -— |
| Jogador 2 | 4-3 | 205 | SELL | STABILIZE | 40.0 | 7 | 0 | 0 | 40.0 | Colosso/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12771227955818176 | 0.0 | 0.0 | +— / -104aaac3-252c-4c1b-9ad8-fc10a35c6cda |
| Jogador 2 | 4-3 | 206 | MOVE_BENCH | STABILIZE | 40.0 | 7 | 3 | 0 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10470970720052719 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 207 | SELL | STABILIZE | 40.0 | 7 | 3 | 0 | 42.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.041141852736473083 | 0.0 | 0.0 | +— / -caf1c554-2223-4090-9f96-b551e5c579ce |
| Jogador 2 | 4-3 | 208 | BUY_XP | STABILIZE | 40.0 | 7 | 6 | 0 | 42.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 209 | MOVE_BOARD | STABILIZE | 40.0 | 7 | 2 | 0 | 42.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1710881143808365 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 211 | BUY | STABILIZE | 27.0 | 7 | 8 | 0 | 42.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.025959378108382225 | 0.0 | 0.0 | +696f53ae-1413-47cc-b491-9870b7bcba51 / -— |
| Jogador 2 | 4-4 | 212 | MOVE_BENCH | STABILIZE | 27.0 | 7 | 5 | 0 | 42.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4531155824661255 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 213 | BUY | STABILIZE | 27.0 | 7 | 5 | 0 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03722197934985161 | 0.0 | 0.0 | +fcd8f4bf-7e1f-42b3-a989-5b3683394c89 / -— |
| Jogador 2 | 4-4 | 214 | SELL | STABILIZE | 27.0 | 7 | 2 | 0 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12175463885068893 | 0.0 | 0.0 | +— / -fcd8f4bf-7e1f-42b3-a989-5b3683394c89 |
| Jogador 2 | 4-4 | 215 | MOVE_BENCH | STABILIZE | 27.0 | 7 | 5 | 0 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1723441779613495 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 216 | BUY | STABILIZE | 27.0 | 7 | 5 | 0 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05630968511104584 | 0.0 | 0.0 | +e1867f53-f97a-4c7a-bce3-24aa037ce27f / -— |
| Jogador 2 | 4-4 | 217 | SELL | STABILIZE | 27.0 | 7 | 2 | 0 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13063503801822662 | 0.0 | 0.0 | +— / -e1867f53-f97a-4c7a-bce3-24aa037ce27f |
| Jogador 2 | 4-4 | 218 | BUY_XP | STABILIZE | 27.0 | 7 | 5 | 0 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 219 | MOVE_BENCH | STABILIZE | 27.0 | 7 | 1 | 0 | 40.0 | Colosso/DA_18_Lillia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.023542581126093864 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 221 | BUY | STABILIZE | 27.0 | 7 | 7 | 0 | 42.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8331438302993774 | 0.0 | 0.0 | +e65701f6-4dac-4c89-8ac2-f38a1cf52fa8 / -18082e05-51e8-4142-b541-c3d7d781b878,23793b7b-2dab-48f0-a8ba-db85fc14c1c5 |
| Jogador 2 | 4-5 | 222 | MOVE_BENCH | STABILIZE | 27.0 | 7 | 5 | 0 | 34.0 | Colosso/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2505386471748352 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 223 | BUY_XP | STABILIZE | 27.0 | 7 | 5 | 0 | 40.0 | Colosso/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42649999260902405 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 224 | MOVE_BENCH | STABILIZE | 27.0 | 8 | 1 | 0 | 40.0 | Colosso/DA_18_LeBlanc | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17372485995292664 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 225 | MOVE_BENCH | STABILIZE | 27.0 | 8 | 1 | 0 | 40.0 | Colosso/DA_18_LeBlanc | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02371542528271675 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 226 | MOVE_BENCH | STABILIZE | 27.0 | 8 | 1 | 0 | 42.0 | Colosso/DA_18_LeBlanc | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17863649129867554 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 227 | SELL | STABILIZE | 27.0 | 8 | 1 | 0 | 40.0 | Colosso/DA_18_LeBlanc | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12495384365320206 | 0.0 | 0.0 | +— / -e65701f6-4dac-4c89-8ac2-f38a1cf52fa8 |
| Jogador 2 | 4-5 | 228 | BUY | STABILIZE | 27.0 | 8 | 6 | 0 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19890716671943665 | 0.0 | 0.0 | +5b96c8f7-bacb-47df-8666-30d30d49549d / -— |
| Jogador 2 | 4-5 | 229 | MOVE_BENCH | STABILIZE | 27.0 | 8 | 3 | 0 | 40.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2333165407180786 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 231 | BUY | STABILIZE | 27.0 | 8 | 9 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2874711751937866 | 0.0 | 0.0 | +a11208a9-96bf-468e-ab92-2ead6308be26 / -— |
| Jogador 2 | 4-6 | 232 | BUY_XP | STABILIZE | 27.0 | 8 | 8 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 233 | BUY_XP | STABILIZE | 27.0 | 8 | 4 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 234 | SELL | STABILIZE | 27.0 | 8 | 0 | 0 | 46.0 | Colosso/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13725624978542328 | 0.0 | 0.0 | +— / -a11208a9-96bf-468e-ab92-2ead6308be26 |
| Jogador 2 | 4-6 | 235 | PASS | STABILIZE | 27.0 | 8 | 1 | 0 | 46.0 | Colosso/DA_18_Lillia | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 241 | BUY | ALL_IN | 15.0 | 8 | 6 | 0 | 46.0 | Invocador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.05638619139790535 | 0.0 | 0.0 | +8b75555c-d84d-4b8a-8d6c-012585a05b99 / -— |
| Jogador 2 | 4-7 | 242 | MOVE_BENCH | ALL_IN | 15.0 | 8 | 3 | 0 | 46.0 | Invocador/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3380803167819977 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 243 | MOVE_BENCH | ALL_IN | 15.0 | 8 | 3 | 0 | 46.0 | Invocador/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09280974417924881 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 244 | MOVE_BENCH | ALL_IN | 15.0 | 8 | 3 | 0 | 44.0 | Invocador/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02341240830719471 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 245 | MOVE_BENCH | ALL_IN | 15.0 | 8 | 3 | 0 | 46.0 | Invocador/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3380652368068695 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 246 | MOVE_BENCH | ALL_IN | 15.0 | 8 | 3 | 0 | 46.0 | Invocador/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09249328821897507 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 247 | MOVE_BENCH | ALL_IN | 15.0 | 8 | 3 | 0 | 44.0 | Invocador/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04419013857841492 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 248 | MOVE_BOARD | ALL_IN | 15.0 | 8 | 3 | 0 | 52.0 | Invocador/DA_18_Lillia | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 249 | PASS | ALL_IN | 15.0 | 8 | 3 | 0 | 52.0 | Invocador/DA_18_Lillia | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 251 | EQUIP_FROM_INVENTORY | ALL_IN | 15.0 | 8 | 8 | 0 | 52.0 | Invocador/DA_18_Lillia | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 252 | BUY | ALL_IN | 15.0 | 8 | 8 | 0 | 52.0 | Invocador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | -0.16721023619174957 | 0.0 | 0.0 | +02d3d068-e592-4f9c-a574-914955401575 / -— |
| Jogador 2 | 5-1 | 253 | CRAFT_AND_EQUIP | ALL_IN | 15.0 | 8 | 3 | 0 | 52.0 | Invocador/DA_18_Lux_Elderwood | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.02191002294421196 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 254 | BUY | ALL_IN | 15.0 | 8 | 3 | 0 | 52.0 | Invocador/DA_18_Lux_Elderwood | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25083789229393005 | 0.0 | 0.0 | +d6a929d8-6d7c-4bcd-880d-d819daca2ae0 / -— |
| Jogador 2 | 5-1 | 255 | MOVE_BENCH | ALL_IN | 15.0 | 8 | 0 | 0 | 52.0 | Invocador/DA_18_Lux_Elderwood | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020884037017822266 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 256 | SELL | ALL_IN | 15.0 | 8 | 0 | 0 | 56.0 | Invocador/DA_18_Lux_Elderwood | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0244615375995636 | 0.0 | 0.0 | +— / -d6a929d8-6d7c-4bcd-880d-d819daca2ae0 |
| Jogador 2 | 5-1 | 257 | MOVE_BENCH | ALL_IN | 15.0 | 8 | 3 | 0 | 56.0 | Invocador/DA_18_Lux_Elderwood | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08935998380184174 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 258 | MOVE_BENCH | ALL_IN | 15.0 | 8 | 3 | 0 | 54.0 | Invocador/DA_18_Lux_Elderwood | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04855671525001526 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 259 | MOVE_BENCH | ALL_IN | 15.0 | 8 | 3 | 0 | 52.0 | Invocador/DA_18_Lux_Elderwood | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010733756236732006 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 261 | PASS | ALL_IN | 0.0 | 8 | 3 | 0 | 0.0 | Invocador/DA_18_Lux_Elderwood | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 271 | PASS | ALL_IN | 0.0 | 8 | 3 | 0 | 0.0 | Invocador/DA_18_Lux_Elderwood | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 281 | PASS | ALL_IN | 0.0 | 8 | 3 | 0 | 0.0 | Invocador/DA_18_Lux_Elderwood | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 291 | PASS | ALL_IN | 0.0 | 8 | 3 | 0 | 0.0 | Invocador/DA_18_Lux_Elderwood | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 301 | PASS | ALL_IN | 0.0 | 8 | 3 | 0 | 0.0 | Invocador/DA_18_Lux_Elderwood | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 311 | PASS | ALL_IN | 0.0 | 8 | 3 | 0 | 0.0 | Invocador/DA_18_Lux_Elderwood | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 321 | PASS | ALL_IN | 0.0 | 8 | 3 | 0 | 0.0 | Invocador/DA_18_Lux_Elderwood | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 331 | PASS | ALL_IN | 0.0 | 8 | 3 | 0 | 0.0 | Invocador/DA_18_Lux_Elderwood | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 9 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.28737619519233704 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.25464189052581787 | 0.0 | 0.0 | +268b29b3-1068-470f-9fe2-e319d1874787 / -— |
| Jogador 3 | 1-2 | 12 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21765097975730896 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9744700193405151 | 0.0 | 0.0 | +5f61fad0-e2c4-4bef-add4-0eab1d93b4df / -— |
| Jogador 3 | 1-3 | 22 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179372072219849 | 0.0 | 0.0 | +8a384047-bcc4-4d79-8896-30170e9313cd / -36f58657-5835-4389-95e9-a7d26464c2aa,5f61fad0-e2c4-4bef-add4-0eab1d93b4df |
| Jogador 3 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5220898389816284 | 0.0 | 0.0 | +477d3aa4-2130-4a0e-8254-2688ac860569 / -— |
| Jogador 3 | 1-3 | 24 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41969603300094604 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7712828516960144 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 32 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9576020836830139 | 0.0 | 0.0 | +5ead8548-7453-4fa1-856e-674995576a48 / -— |
| Jogador 3 | 1-4 | 33 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3428668975830078 | 0.0 | 0.0 | +f19f9e7f-f189-47fe-b571-be5065c6eb39 / -— |
| Jogador 3 | 2-1 | 42 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 43 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 49 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1720498949289322 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 51 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016399381682276726 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 52 | BUY_XP | STABILIZE | 96.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44699999690055847 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 53 | PASS | STABILIZE | 96.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 59 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 1 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6453942656517029 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 61 | BUY | STABILIZE | 96.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2371496707201004 | 0.0 | 0.0 | +29f10cb7-6575-47ca-b583-057992a08253 / -— |
| Jogador 3 | 2-3 | 62 | BUY | STABILIZE | 96.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27779775857925415 | 0.0 | 0.0 | +99511886-d1a7-4910-b099-5072e5385c63 / -— |
| Jogador 3 | 2-3 | 63 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3787960112094879 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 64 | PASS | STABILIZE | 96.0 | 5 | 2 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 71 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 9 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06615934520959854 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 72 | BUY_XP | STABILIZE | 96.0 | 5 | 9 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 73 | BUY_XP | STABILIZE | 96.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 74 | SELL | STABILIZE | 96.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17199113965034485 | 0.0 | 0.0 | +— / -8a384047-bcc4-4d79-8896-30170e9313cd |
| Jogador 3 | 2-4 | 75 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 4 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04355252534151077 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 76 | BUY | STABILIZE | 96.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2665864825248718 | 0.0 | 0.0 | +4c8a9a18-68d8-4672-a96d-bb09816257dc / -— |
| Jogador 3 | 2-4 | 77 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06090173497796059 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 78 | PASS | STABILIZE | 96.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 81 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5184705257415771 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 82 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002579611260443926 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 83 | BUY | STABILIZE | 96.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2701927423477173 | 0.0 | 0.0 | +cdb48eea-209d-4833-9a68-79df61990332 / -— |
| Jogador 3 | 2-5 | 84 | BUY_XP | STABILIZE | 96.0 | 5 | 4 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 85 | PASS | STABILIZE | 96.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 91 | BUY | STABILIZE | 90.0 | 6 | 5 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3657878339290619 | 0.0 | 0.0 | +14bbd76c-fca8-4017-89b5-e586bb1cae70 / -— |
| Jogador 3 | 2-6 | 92 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 3 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6422109007835388 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 93 | PASS | STABILIZE | 90.0 | 6 | 3 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 101 | BUY_XP | STABILIZE | 90.0 | 6 | 9 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 102 | BUY_XP | STABILIZE | 90.0 | 6 | 5 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 103 | SELL | STABILIZE | 90.0 | 6 | 1 | 0 | 20.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030371982604265213 | 0.0 | 0.0 | +— / -14bbd76c-fca8-4017-89b5-e586bb1cae70 |
| Jogador 3 | 2-7 | 104 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 3 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49605241417884827 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 105 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 3 | 0 | 22.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10177093744277954 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 106 | PASS | STABILIZE | 90.0 | 6 | 3 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 111 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 8 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09448104351758957 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 112 | BUY_XP | STABILIZE | 90.0 | 6 | 8 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 113 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 4 | 0 | 20.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5616965293884277 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 114 | BUY | STABILIZE | 90.0 | 6 | 4 | 0 | 22.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.744240939617157 | 0.0 | 0.0 | +2fa86b11-4e28-4652-890e-f00a79068223 / -— |
| Jogador 3 | 3-1 | 115 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 2 | 0 | 22.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11782166361808777 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 116 | BUY | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2705167531967163 | 0.0 | 0.0 | +19cf270e-27a1-4d3c-bef7-0b1af400d07c / -— |
| Jogador 3 | 3-1 | 117 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 1 | 0 | 20.0 | Devastador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1767522394657135 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 118 | SELL | STABILIZE | 90.0 | 6 | 1 | 0 | 20.0 | Devastador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11110645532608032 | 0.0 | 0.0 | +— / -19cf270e-27a1-4d3c-bef7-0b1af400d07c |
| Jogador 3 | 3-1 | 119 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 2 | 0 | 20.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10808348655700684 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 121 | BUY | STABILIZE | 80.0 | 6 | 7 | 0 | 22.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31200110912323 | 0.0 | 0.0 | +6a5bf4a0-0a6d-4ee6-9b76-3b4923ba1d97 / -— |
| Jogador 3 | 3-2 | 122 | BUY_XP | STABILIZE | 80.0 | 6 | 4 | 0 | 22.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 123 | SELL | STABILIZE | 80.0 | 6 | 0 | 0 | 22.0 | Devastador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10788071900606155 | 0.0 | 0.0 | +— / -f19f9e7f-f189-47fe-b571-be5065c6eb39 |
| Jogador 3 | 3-2 | 124 | MOVE_BENCH | STABILIZE | 80.0 | 6 | 2 | 0 | 22.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03360670804977417 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 125 | MOVE_BENCH | STABILIZE | 80.0 | 6 | 2 | 0 | 24.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011276250705122948 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 126 | MOVE_BENCH | STABILIZE | 80.0 | 6 | 2 | 0 | 22.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3325144350528717 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 127 | MOVE_BENCH | STABILIZE | 80.0 | 6 | 2 | 0 | 22.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01669350266456604 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 128 | MOVE_BENCH | STABILIZE | 80.0 | 6 | 2 | 0 | 24.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00935861561447382 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 129 | MOVE_BENCH | STABILIZE | 80.0 | 6 | 2 | 0 | 22.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06720353662967682 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 131 | BUY | STABILIZE | 80.0 | 6 | 8 | 0 | 22.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6916688680648804 | 0.0 | 0.0 | +e8b0d22c-35bc-459e-a90c-7db13fcbe34f / -— |
| Jogador 3 | 3-3 | 132 | BUY_XP | STABILIZE | 80.0 | 6 | 5 | 0 | 22.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 133 | SELL | STABILIZE | 80.0 | 6 | 1 | 0 | 22.0 | Devastador/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3332821726799011 | 0.0 | 0.0 | +— / -99511886-d1a7-4910-b099-5072e5385c63 |
| Jogador 3 | 3-3 | 134 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 3 | 0 | 22.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14799629151821136 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 135 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 3 | 0 | 22.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10063518583774567 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 136 | PASS | STABILIZE | 80.0 | 6 | 3 | 0 | 22.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 141 | MOVE_BENCH | STABILIZE | 69.0 | 6 | 8 | 0 | 22.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18039420247077942 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 142 | BUY_XP | STABILIZE | 69.0 | 6 | 8 | 0 | 24.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 143 | BUY_XP | STABILIZE | 69.0 | 6 | 4 | 0 | 24.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7544999718666077 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 144 | MOVE_BENCH | STABILIZE | 69.0 | 7 | 0 | 0 | 24.0 | Devastador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 145 | MOVE_BENCH | STABILIZE | 69.0 | 7 | 0 | 0 | 24.0 | Devastador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5257250666618347 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 146 | MOVE_BENCH | STABILIZE | 69.0 | 7 | 0 | 0 | 30.0 | Devastador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011575527489185333 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 147 | MOVE_BENCH | STABILIZE | 69.0 | 7 | 0 | 0 | 28.0 | Devastador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 148 | PASS | STABILIZE | 69.0 | 7 | 0 | 0 | 28.0 | Devastador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 151 | BUY | STABILIZE | 69.0 | 7 | 5 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2811352014541626 | 0.0 | 0.0 | +aaa84ce8-7919-4ec3-92eb-cc03a9decca9 / -— |
| Jogador 3 | 3-5 | 152 | BUY | STABILIZE | 69.0 | 7 | 2 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018346788361668587 | 0.0 | 0.0 | +65a6d68c-90ae-4e31-8bbc-82e8ec75b3de / -— |
| Jogador 3 | 3-5 | 153 | MOVE_BOARD | STABILIZE | 69.0 | 7 | 0 | 0 | 28.0 | Devastador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34590205550193787 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 154 | MOVE_BENCH | STABILIZE | 69.0 | 7 | 0 | 0 | 28.0 | Devastador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017511235550045967 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 155 | PASS | STABILIZE | 69.0 | 7 | 0 | 0 | 28.0 | Devastador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 161 | BUY | STABILIZE | 69.0 | 7 | 6 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7436072826385498 | 0.0 | 0.0 | +b75c9bc5-9bc7-465a-a97c-59156e5c482d / -— |
| Jogador 3 | 3-6 | 162 | MOVE_BENCH | STABILIZE | 69.0 | 7 | 3 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35425540804862976 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 163 | MOVE_BENCH | STABILIZE | 69.0 | 7 | 3 | 0 | 30.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08986454457044601 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 164 | MOVE_BENCH | STABILIZE | 69.0 | 7 | 3 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7504112720489502 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 165 | MOVE_BENCH | STABILIZE | 69.0 | 7 | 3 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3544401526451111 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 166 | MOVE_BENCH | STABILIZE | 69.0 | 7 | 3 | 0 | 30.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018069913610816002 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 167 | MOVE_BENCH | STABILIZE | 69.0 | 7 | 3 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0076470887288451195 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 168 | MOVE_BENCH | STABILIZE | 69.0 | 7 | 3 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3310842216014862 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 169 | PASS | STABILIZE | 69.0 | 7 | 3 | 0 | 30.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 171 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 8 | 0 | 30.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7421796321868896 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 172 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 8 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01773340068757534 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 173 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 8 | 0 | 26.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33503127098083496 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 174 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 8 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013548268936574459 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 175 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 8 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019515495747327805 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 176 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 8 | 0 | 26.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33501991629600525 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 177 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 8 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35576382279396057 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 178 | BUY_XP | STABILIZE | 57.0 | 7 | 8 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 179 | BUY_XP | STABILIZE | 57.0 | 7 | 4 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 181 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 5 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031153365969657898 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 182 | BUY_XP | STABILIZE | 57.0 | 7 | 5 | 0 | 28.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 183 | SELL | STABILIZE | 57.0 | 7 | 1 | 0 | 28.0 | Devastador/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10377024859189987 | 0.0 | 0.0 | +— / -65a6d68c-90ae-4e31-8bbc-82e8ec75b3de |
| Jogador 3 | 4-1 | 184 | MOVE_BOARD | STABILIZE | 57.0 | 7 | 3 | 0 | 28.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18628418445587158 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 185 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 3 | 0 | 28.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44523927569389343 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 186 | PASS | STABILIZE | 57.0 | 7 | 3 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 191 | BUY | STABILIZE | 57.0 | 7 | 9 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1366841048002243 | 0.0 | 0.0 | +0534477f-2ff8-47a7-b71b-1a1d5430589e / -— |
| Jogador 3 | 4-2 | 192 | BUY_XP | STABILIZE | 57.0 | 7 | 5 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 193 | MOVE_BOARD | STABILIZE | 57.0 | 7 | 1 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 194 | MOVE_BOARD | STABILIZE | 57.0 | 7 | 1 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13044486939907074 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 195 | MOVE_BOARD | STABILIZE | 57.0 | 7 | 1 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 196 | MOVE_BOARD | STABILIZE | 57.0 | 7 | 1 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13654682040214539 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 197 | PASS | STABILIZE | 57.0 | 7 | 1 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 201 | BUY_XP | STABILIZE | 57.0 | 7 | 8 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 202 | BUY_XP | STABILIZE | 57.0 | 7 | 4 | 0 | 28.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 203 | SELL | STABILIZE | 57.0 | 7 | 0 | 0 | 28.0 | Devastador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32679593563079834 | 0.0 | 0.0 | +— / -e8b0d22c-35bc-459e-a90c-7db13fcbe34f |
| Jogador 3 | 4-3 | 204 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 3 | 0 | 28.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14041873812675476 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 205 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 3 | 0 | 28.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44904088973999023 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 206 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 3 | 0 | 30.0 | Devastador/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24509553611278534 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 207 | PASS | STABILIZE | 57.0 | 7 | 3 | 0 | 28.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 211 | BUY_XP | STABILIZE | 57.0 | 7 | 10 | 1 | 28.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 212 | BUY_XP | STABILIZE | 57.0 | 7 | 6 | 0 | 28.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 213 | SELL | STABILIZE | 57.0 | 7 | 2 | 0 | 28.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.345519483089447 | 0.0 | 0.0 | +— / -aaa84ce8-7919-4ec3-92eb-cc03a9decca9 |
| Jogador 3 | 4-4 | 214 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 5 | 0 | 28.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13341623544692993 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 215 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 5 | 0 | 28.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05621830001473427 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 216 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 5 | 0 | 28.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.699589192867279 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 217 | PASS | STABILIZE | 57.0 | 7 | 5 | 0 | 28.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 221 | BUY | STABILIZE | 57.0 | 7 | 11 | 1 | 28.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.663646399974823 | 0.0 | 0.0 | +a58767a1-d7c1-48e9-94ae-df46a364ef92 / -— |
| Jogador 3 | 4-5 | 222 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 8 | 0 | 28.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0759667381644249 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 223 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 8 | 0 | 30.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02393532358109951 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 224 | BUY_XP | STABILIZE | 57.0 | 7 | 8 | 0 | 30.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 225 | BUY_XP | STABILIZE | 57.0 | 7 | 4 | 0 | 30.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4323124885559082 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 226 | MOVE_BOARD | ECON | 57.0 | 8 | 0 | 0 | 30.0 | Devastador/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08023229986429214 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 227 | MOVE_BOARD | ECON | 57.0 | 8 | 0 | 0 | 30.0 | Devastador/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1251494586467743 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 228 | MOVE_BOARD | ECON | 57.0 | 8 | 0 | 0 | 30.0 | Devastador/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03353238105773926 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 229 | MOVE_BENCH | ECON | 57.0 | 8 | 0 | 0 | 30.0 | Devastador/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08478565514087677 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 231 | MOVE_BENCH | WINSTREAK | 57.0 | 8 | 7 | 0 | 36.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14511828124523163 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 232 | MOVE_BENCH | ECON | 57.0 | 8 | 7 | 0 | 34.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4495774507522583 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 233 | BUY_XP | ECON | 57.0 | 8 | 7 | 0 | 34.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 234 | MOVE_BOARD | ECON | 57.0 | 8 | 3 | 0 | 34.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 235 | MOVE_BOARD | ECON | 57.0 | 8 | 3 | 0 | 34.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 236 | PASS | ECON | 57.0 | 8 | 3 | 0 | 34.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 241 | BUY | ECON | 57.0 | 8 | 11 | 1 | 34.0 | Devastador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5335788726806641 | 0.0 | 0.0 | +f8a93323-530e-4f9c-99d7-a5ec83b78992 / -— |
| Jogador 3 | 4-7 | 242 | BUY_XP | ECON | 57.0 | 8 | 7 | 0 | 34.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 243 | MOVE_BOARD | ECON | 57.0 | 8 | 3 | 0 | 34.0 | Devastador/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01868247613310814 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 244 | MOVE_BOARD | ECON | 57.0 | 8 | 3 | 0 | 34.0 | Devastador/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12290727347135544 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 245 | SELL | ECON | 57.0 | 8 | 3 | 0 | 34.0 | Devastador/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3454936742782593 | 0.0 | 0.0 | +— / -a58767a1-d7c1-48e9-94ae-df46a364ef92 |
| Jogador 3 | 4-7 | 246 | MOVE_BENCH | ECON | 57.0 | 8 | 6 | 0 | 34.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3064255714416504 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 247 | MOVE_BENCH | WINSTREAK | 57.0 | 8 | 6 | 0 | 36.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11796362698078156 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 248 | MOVE_BENCH | WINSTREAK | 57.0 | 8 | 6 | 0 | 36.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4826064705848694 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 249 | MOVE_BENCH | ECON | 57.0 | 8 | 6 | 0 | 34.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30472108721733093 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 251 | EQUIP_FROM_INVENTORY | WINSTREAK | 57.0 | 8 | 13 | 1 | 36.0 | Devastador/DA_18_Soraka | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 252 | CRAFT_AND_EQUIP | WINSTREAK | 57.0 | 8 | 13 | 1 | 36.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13184286653995514 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 253 | MOVE_BENCH | WINSTREAK | 57.0 | 8 | 13 | 1 | 36.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21044906973838806 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 254 | MOVE_BENCH | WINSTREAK | 57.0 | 8 | 13 | 1 | 36.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01356973871588707 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 255 | MOVE_BENCH | WINSTREAK | 57.0 | 8 | 13 | 1 | 36.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.524424135684967 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 256 | PASS | WINSTREAK | 57.0 | 8 | 13 | 1 | 36.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 261 | BUY | WINSTREAK | 57.0 | 8 | 23 | 2 | 36.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1893550157546997 | 0.0 | 0.0 | +e270a6b1-23dd-49a0-8694-ba911eae4c71 / -— |
| Jogador 3 | 5-2 | 262 | MOVE_BENCH | WINSTREAK | 57.0 | 8 | 19 | 1 | 36.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3326495885848999 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 263 | MOVE_BENCH | ECON | 57.0 | 8 | 19 | 1 | 34.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19126969575881958 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 264 | MOVE_BENCH | WINSTREAK | 57.0 | 8 | 19 | 1 | 36.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12274520099163055 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 265 | MOVE_BENCH | WINSTREAK | 57.0 | 8 | 19 | 1 | 36.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14047487080097198 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 266 | BUY_XP | ECON | 57.0 | 8 | 19 | 1 | 34.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 267 | BUY_XP | ECON | 57.0 | 8 | 15 | 1 | 34.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 268 | BUY_XP | ECON | 57.0 | 8 | 11 | 1 | 34.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 269 | BUY_XP | ECON | 57.0 | 8 | 7 | 0 | 34.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 271 | MOVE_BENCH | ECON | 57.0 | 8 | 12 | 1 | 34.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14396075904369354 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 272 | MOVE_BENCH | WINSTREAK | 57.0 | 8 | 12 | 1 | 36.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6839563846588135 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 273 | MOVE_BENCH | WINSTREAK | 57.0 | 8 | 12 | 1 | 36.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11208891868591309 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 274 | MOVE_BENCH | ECON | 57.0 | 8 | 12 | 1 | 34.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09968884289264679 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 275 | MOVE_BENCH | WINSTREAK | 57.0 | 8 | 12 | 1 | 36.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.031971242278814316 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 276 | MOVE_BENCH | WINSTREAK | 57.0 | 8 | 12 | 1 | 36.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11205890774726868 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 277 | BUY_XP | ECON | 57.0 | 8 | 12 | 1 | 34.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 278 | BUY_XP | ECON | 57.0 | 8 | 8 | 0 | 34.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 279 | BUY_XP | ECON | 57.0 | 8 | 4 | 0 | 34.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 281 | MOVE_BENCH | ECON | 42.0 | 8 | 5 | 0 | 34.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04578370228409767 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 282 | BUY | ECON | 42.0 | 8 | 5 | 0 | 36.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16869771480560303 | 0.0 | 0.0 | +d5c73756-6784-44e9-b521-5c61db813319 / -— |
| Jogador 3 | 5-4 | 283 | MOVE_BENCH | ECON | 42.0 | 8 | 1 | 0 | 36.0 | Devastador/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5988842248916626 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 284 | MOVE_BENCH | ECON | 42.0 | 8 | 1 | 0 | 36.0 | Devastador/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29759055376052856 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 285 | MOVE_BENCH | ECON | 42.0 | 8 | 1 | 0 | 36.0 | Devastador/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1052103266119957 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 286 | MOVE_BENCH | ECON | 42.0 | 8 | 1 | 0 | 36.0 | Devastador/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0344119668006897 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 287 | MOVE_BENCH | ECON | 42.0 | 8 | 1 | 0 | 36.0 | Devastador/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31372496485710144 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 288 | MOVE_BENCH | ECON | 42.0 | 8 | 1 | 0 | 36.0 | Devastador/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0798654556274414 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 289 | MOVE_BOARD | ECON | 42.0 | 8 | 1 | 0 | 34.0 | Devastador/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1500062346458435 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 291 | BUY | ECON | 42.0 | 8 | 6 | 0 | 34.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6090080142021179 | 0.0 | 0.0 | +3faf4ab2-44b3-4779-985b-658c64791c28 / -— |
| Jogador 3 | 5-5 | 292 | MOVE_BENCH | ECON | 42.0 | 8 | 2 | 0 | 34.0 | Devastador/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03184600546956062 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 293 | MOVE_BENCH | ECON | 42.0 | 8 | 2 | 0 | 36.0 | Devastador/DA_18_Malphite | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06341560930013657 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 294 | MOVE_BENCH | ECON | 42.0 | 8 | 2 | 0 | 36.0 | Devastador/DA_18_Malphite | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4140091836452484 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 295 | MOVE_BENCH | ECON | 42.0 | 8 | 2 | 0 | 34.0 | Devastador/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.034387800842523575 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 296 | MOVE_BENCH | ECON | 42.0 | 8 | 2 | 0 | 36.0 | Devastador/DA_18_Malphite | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0633464977145195 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 297 | MOVE_BENCH | ECON | 42.0 | 8 | 2 | 0 | 36.0 | Devastador/DA_18_Malphite | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014744633808732033 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 298 | MOVE_BOARD | ECON | 42.0 | 8 | 2 | 0 | 36.0 | Devastador/DA_18_Malphite | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 299 | MOVE_BOARD | ECON | 42.0 | 8 | 2 | 0 | 36.0 | Devastador/DA_18_Malphite | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 301 | BUY | STABILIZE | 26.0 | 8 | 8 | 0 | 36.0 | Devastador/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7394197583198547 | 0.0 | 0.0 | +9c07608c-00e1-40f1-9671-6d8bc584a6c9 / -— |
| Jogador 3 | 5-6 | 302 | BUY_XP | STABILIZE | 26.0 | 8 | 5 | 0 | 36.0 | Devastador/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 303 | SELL | STABILIZE | 26.0 | 8 | 1 | 0 | 36.0 | Devastador/DA_18_Malphite | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05400000140070915 | 0.0 | 0.0 | +— / -cdb48eea-209d-4833-9a68-79df61990332 |
| Jogador 3 | 5-6 | 304 | BUY_XP | STABILIZE | 26.0 | 8 | 4 | 0 | 36.0 | Devastador/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 305 | SELL | STABILIZE | 26.0 | 8 | 0 | 0 | 36.0 | Devastador/DA_18_Malphite | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33893832564353943 | 0.0 | 0.0 | +— / -9c07608c-00e1-40f1-9671-6d8bc584a6c9 |
| Jogador 3 | 5-6 | 306 | MOVE_BENCH | STABILIZE | 26.0 | 8 | 3 | 0 | 36.0 | Devastador/DA_18_Malphite | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04956774041056633 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 307 | MOVE_BENCH | STABILIZE | 26.0 | 8 | 3 | 0 | 36.0 | Devastador/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16572870314121246 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 308 | MOVE_BENCH | STABILIZE | 26.0 | 8 | 3 | 0 | 38.0 | Devastador/DA_18_Malphite | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5370745658874512 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 309 | MOVE_BENCH | STABILIZE | 26.0 | 8 | 3 | 0 | 36.0 | Devastador/DA_18_Malphite | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13832373917102814 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 311 | BUY | ALL_IN | 9.0 | 8 | 9 | 0 | 36.0 | Devastador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7954360842704773 | 0.0 | 0.0 | +0a6e3194-ed55-43ad-ac66-31e08ccda7aa / -3faf4ab2-44b3-4779-985b-658c64791c28,d5c73756-6784-44e9-b521-5c61db813319 |
| Jogador 3 | 5-7 | 312 | BUY | ALL_IN | 9.0 | 8 | 5 | 0 | 36.0 | Devastador/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7291865348815918 | 0.0 | 0.0 | +b250e22d-7193-4ea5-879d-5c7b41145719 / -— |
| Jogador 3 | 5-7 | 313 | MOVE_BENCH | ALL_IN | 9.0 | 8 | 2 | 0 | 36.0 | Devastador/DA_18_Malphite | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22679302096366882 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 314 | MOVE_BENCH | ALL_IN | 9.0 | 8 | 2 | 0 | 46.0 | Devastador/DA_18_Malphite | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0016061475034803152 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 315 | MOVE_BENCH | ALL_IN | 9.0 | 8 | 2 | 0 | 44.0 | Devastador/DA_18_Malphite | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2584499716758728 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 316 | PASS | ALL_IN | 9.0 | 8 | 2 | 0 | 36.0 | Devastador/DA_18_Malphite | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 321 | EQUIP_FROM_INVENTORY | ALL_IN | 9.0 | 8 | 8 | 0 | 36.0 | Devastador/DA_18_Malphite | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 322 | EQUIP_FROM_INVENTORY | ALL_IN | 9.0 | 8 | 8 | 0 | 36.0 | Devastador/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.0279674269258976 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 323 | MOVE_BENCH | ALL_IN | 9.0 | 8 | 8 | 0 | 36.0 | Devastador/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22679302096366882 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 324 | MOVE_BENCH | ALL_IN | 9.0 | 8 | 8 | 0 | 46.0 | Devastador/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5370810031890869 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 325 | MOVE_BENCH | ALL_IN | 9.0 | 8 | 8 | 0 | 44.0 | Devastador/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1478249430656433 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 326 | PASS | ALL_IN | 9.0 | 8 | 8 | 0 | 46.0 | Devastador/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-2 | 331 | PASS | ALL_IN | 0.0 | 8 | 8 | 0 | 0.0 | Devastador/DA_18_Malphite | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 9 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.28737619519233704 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3375903069972992 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06630194187164307 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 13 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2516838312149048 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019686980172991753 | 0.0 | 0.0 | +a19fc47b-fc81-49b2-bc25-d25d58b8deef / -— |
| Jogador 4 | 1-3 | 22 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48420730233192444 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 31 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9469206929206848 | 0.0 | 0.0 | +c05579e6-aa73-434f-8a91-c58d68a81ced / -— |
| Jogador 4 | 2-1 | 42 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1130337715148926 | 0.0 | 0.0 | +9819422b-1f51-47b5-89b7-9d6e906ddff2 / -a19fc47b-fc81-49b2-bc25-d25d58b8deef,c05579e6-aa73-434f-8a91-c58d68a81ced |
| Jogador 4 | 2-1 | 43 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 4.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 49 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 4.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21509887278079987 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 51 | BUY | STABILIZE | 95.0 | 4 | 8 | 0 | 6.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02944059669971466 | 0.0 | 0.0 | +4e00fb2f-75c1-4580-bd09-cb73c31af01f / -— |
| Jogador 4 | 2-2 | 52 | BUY | STABILIZE | 95.0 | 4 | 5 | 0 | 6.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3703615963459015 | 0.0 | 0.0 | +e989a0cc-848a-4c45-b153-315877aee8f7 / -— |
| Jogador 4 | 2-2 | 53 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 3 | 0 | 6.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6189660429954529 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 54 | PASS | STABILIZE | 95.0 | 4 | 3 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 61 | BUY_XP | STABILIZE | 95.0 | 4 | 9 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 62 | BUY_XP | STABILIZE | 95.0 | 4 | 5 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4519999921321869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 63 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11615848541259766 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 64 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6588684320449829 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 65 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 20.0 | —/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08723567426204681 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 66 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 16.0 | —/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11595360189676285 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 67 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 18.0 | —/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3689005374908447 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 68 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 20.0 | —/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 71 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 20.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5037814378738403 | 0.0 | 0.0 | +a229cc5e-9f28-4ff3-b652-eab994251c92 / -— |
| Jogador 4 | 2-4 | 72 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 20.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10444042086601257 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 4 | 2-4 | 73 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 2 | 0 | 20.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07958811521530151 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 74 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 2 | 0 | 16.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11466715484857559 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 75 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 2 | 0 | 18.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18654491007328033 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 76 | PASS | STABILIZE | 95.0 | 5 | 2 | 0 | 20.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 81 | BUY | STABILIZE | 95.0 | 5 | 8 | 0 | 20.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9645500183105469 | 0.0 | 0.0 | +3825a7ba-319f-48f8-ad2d-8c24eabbc1cc / -— |
| Jogador 4 | 2-5 | 82 | BUY_XP | STABILIZE | 95.0 | 5 | 5 | 0 | 20.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 83 | SELL | STABILIZE | 95.0 | 5 | 1 | 0 | 20.0 | —/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03492431342601776 | 0.0 | 0.0 | +— / -e989a0cc-848a-4c45-b153-315877aee8f7 |
| Jogador 4 | 2-5 | 84 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 3 | 0 | 20.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.032915689051151276 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 85 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1238461509346962 | 0.0 | 0.0 | +— / -9819422b-1f51-47b5-89b7-9d6e906ddff2 |
| Jogador 4 | 2-5 | 86 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 8 | 0 | 18.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16868150234222412 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 87 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 8 | 0 | 16.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 88 | PASS | STABILIZE | 95.0 | 5 | 8 | 0 | 16.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 91 | BUY | STABILIZE | 88.0 | 5 | 13 | 1 | 16.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4628787636756897 | 0.0 | 0.0 | +b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a / -— |
| Jogador 4 | 2-6 | 92 | MOVE_BENCH | STABILIZE | 88.0 | 5 | 10 | 1 | 16.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19659869372844696 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 93 | BUY_XP | STABILIZE | 88.0 | 5 | 10 | 1 | 18.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 94 | BUY_XP | STABILIZE | 88.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20200000703334808 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 95 | MOVE_BENCH | STABILIZE | 88.0 | 6 | 2 | 0 | 18.0 | —/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19665800034999847 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 96 | MOVE_BENCH | STABILIZE | 88.0 | 6 | 2 | 0 | 16.0 | —/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 97 | PASS | STABILIZE | 88.0 | 6 | 2 | 0 | 16.0 | —/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 99 | MOVE_BENCH | STABILIZE | 88.0 | 6 | 2 | 0 | 16.0 | —/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5852364897727966 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 101 | BUY | STABILIZE | 82.0 | 6 | 8 | 0 | 22.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37561145424842834 | 0.0 | 0.0 | +5e247068-fe03-467e-9e7d-ab85ade7fdae / -— |
| Jogador 4 | 2-7 | 102 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 5 | 0 | 22.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07039924710988998 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 103 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 5 | 0 | 22.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18245382606983185 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 104 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 5 | 0 | 24.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35755378007888794 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 105 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 5 | 0 | 22.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06896959245204926 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 106 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 5 | 0 | 22.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1824035793542862 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 107 | BUY_XP | STABILIZE | 82.0 | 6 | 5 | 0 | 24.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 108 | PASS | STABILIZE | 82.0 | 6 | 1 | 0 | 24.0 | —/DA_18_Aphelios | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 111 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 7 | 0 | 24.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05360064655542374 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 112 | BUY | STABILIZE | 82.0 | 6 | 7 | 0 | 22.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7339207530021667 | 0.0 | 0.0 | +74fe48c1-d955-4b0d-b832-39d4c86049dc / -— |
| Jogador 4 | 3-1 | 113 | BUY_XP | STABILIZE | 82.0 | 6 | 5 | 0 | 22.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 114 | MOVE_BOARD | STABILIZE | 82.0 | 6 | 1 | 0 | 22.0 | Fera do Rift/DA_18_Aphelios | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04875248298048973 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 115 | MOVE_BOARD | STABILIZE | 82.0 | 6 | 1 | 0 | 22.0 | Fera do Rift/DA_18_Aphelios | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11584769189357758 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 116 | SELL | STABILIZE | 82.0 | 6 | 1 | 0 | 22.0 | Fera do Rift/DA_18_Aphelios | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35272282361984253 | 0.0 | 0.0 | +— / -74fe48c1-d955-4b0d-b832-39d4c86049dc |
| Jogador 4 | 3-1 | 117 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 3 | 0 | 22.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3076687753200531 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 118 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 3 | 0 | 24.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14615249633789062 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 119 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 3 | 0 | 22.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33342188596725464 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 121 | BUY | STABILIZE | 82.0 | 6 | 9 | 0 | 26.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7438873052597046 | 0.0 | 0.0 | +d9b43609-2c36-4fea-b26b-ea5bea6609b5 / -— |
| Jogador 4 | 3-2 | 122 | BUY_XP | STABILIZE | 82.0 | 6 | 8 | 0 | 26.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 123 | BUY_XP | STABILIZE | 82.0 | 6 | 4 | 0 | 26.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 124 | SELL | STABILIZE | 82.0 | 6 | 0 | 0 | 26.0 | Fera do Rift/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3280300199985504 | 0.0 | 0.0 | +— / -d9b43609-2c36-4fea-b26b-ea5bea6609b5 |
| Jogador 4 | 3-2 | 125 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 1 | 0 | 26.0 | Fera do Rift/DA_18_Aphelios | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5240666270256042 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 126 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 1 | 0 | 24.0 | Fera do Rift/DA_18_Aphelios | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04325554519891739 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 127 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 1 | 0 | 26.0 | Fera do Rift/DA_18_Aphelios | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03909529373049736 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 128 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 1 | 0 | 26.0 | Fera do Rift/DA_18_Aphelios | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06902260333299637 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 129 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 1 | 0 | 24.0 | Fera do Rift/DA_18_Aphelios | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4508823752403259 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 131 | BUY | STABILIZE | 82.0 | 6 | 8 | 0 | 26.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2823876738548279 | 0.0 | 0.0 | +409b32b9-5280-4d79-b5b2-871ed597ba56 / -— |
| Jogador 4 | 3-3 | 132 | BUY_XP | STABILIZE | 82.0 | 6 | 5 | 0 | 26.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 133 | SELL | STABILIZE | 82.0 | 6 | 1 | 0 | 26.0 | Fera do Rift/DA_18_Aphelios | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13530951738357544 | 0.0 | 0.0 | +— / -a229cc5e-9f28-4ff3-b652-eab994251c92 |
| Jogador 4 | 3-3 | 134 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 3 | 0 | 26.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08495702594518661 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 135 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 3 | 0 | 26.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04790491238236427 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 136 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 3 | 0 | 24.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.521185040473938 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 137 | MOVE_BOARD | STABILIZE | 82.0 | 6 | 3 | 0 | 26.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014551508240401745 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 138 | MOVE_BOARD | STABILIZE | 82.0 | 6 | 3 | 0 | 26.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2011450082063675 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 139 | MOVE_BENCH | STABILIZE | 82.0 | 6 | 3 | 0 | 26.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17501522600650787 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 141 | BUY | STABILIZE | 70.0 | 6 | 8 | 0 | 24.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7034040689468384 | 0.0 | 0.0 | +2acd0734-f0c3-42b1-9791-5c48e1aa46bc / -— |
| Jogador 4 | 3-4 | 142 | BUY_XP | STABILIZE | 70.0 | 6 | 5 | 0 | 24.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 143 | SELL | STABILIZE | 70.0 | 6 | 1 | 0 | 24.0 | Fera do Rift/DA_18_Aphelios | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17897944152355194 | 0.0 | 0.0 | +— / -2acd0734-f0c3-42b1-9791-5c48e1aa46bc |
| Jogador 4 | 3-4 | 144 | BUY_XP | STABILIZE | 70.0 | 6 | 4 | 0 | 24.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4320000112056732 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 145 | MOVE_BENCH | STABILIZE | 70.0 | 7 | 0 | 0 | 24.0 | Fera do Rift/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4720410406589508 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 146 | MOVE_BENCH | STABILIZE | 70.0 | 7 | 0 | 0 | 32.0 | Fera do Rift/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.040817197412252426 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 147 | MOVE_BENCH | STABILIZE | 70.0 | 7 | 0 | 0 | 32.0 | Fera do Rift/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17505046725273132 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 148 | MOVE_BENCH | STABILIZE | 70.0 | 7 | 0 | 0 | 30.0 | Fera do Rift/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026664094999432564 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 149 | MOVE_BENCH | STABILIZE | 70.0 | 7 | 0 | 0 | 32.0 | Fera do Rift/DA_18_Aphelios | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04153645038604736 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 151 | BUY | STABILIZE | 70.0 | 7 | 5 | 0 | 32.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6981375813484192 | 0.0 | 0.0 | +40f2a32f-1ace-4700-8a79-e6b5d3212036 / -— |
| Jogador 4 | 3-5 | 152 | MOVE_BENCH | STABILIZE | 70.0 | 7 | 2 | 0 | 32.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1748064011335373 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 153 | MOVE_BENCH | STABILIZE | 70.0 | 7 | 2 | 0 | 30.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5830767750740051 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 154 | MOVE_BENCH | STABILIZE | 70.0 | 7 | 2 | 0 | 32.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04330326244235039 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 155 | MOVE_BENCH | STABILIZE | 70.0 | 7 | 2 | 0 | 32.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17484092712402344 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 156 | MOVE_BENCH | STABILIZE | 70.0 | 7 | 2 | 0 | 30.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02666398510336876 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 157 | MOVE_BENCH | STABILIZE | 70.0 | 7 | 2 | 0 | 32.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13774660229682922 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 158 | MOVE_BOARD | STABILIZE | 70.0 | 7 | 2 | 0 | 32.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3243946135044098 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 159 | MOVE_BENCH | STABILIZE | 70.0 | 7 | 2 | 0 | 32.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07285895943641663 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 161 | BUY | STABILIZE | 59.0 | 7 | 8 | 0 | 30.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7447754144668579 | 0.0 | 0.0 | +320038b5-88c4-48fe-a7fa-a30823d674c0 / -— |
| Jogador 4 | 3-6 | 162 | MOVE_BENCH | STABILIZE | 59.0 | 7 | 7 | 0 | 30.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.464655339717865 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 163 | MOVE_BENCH | STABILIZE | 59.0 | 7 | 7 | 0 | 26.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06096264719963074 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 164 | PASS | STABILIZE | 59.0 | 7 | 7 | 0 | 26.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 171 | BUY | STABILIZE | 46.0 | 7 | 13 | 1 | 26.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7231391072273254 | 0.0 | 0.0 | +05be69ba-41c7-4dee-9799-dabbd60f0dc9 / -40f2a32f-1ace-4700-8a79-e6b5d3212036,5e247068-fe03-467e-9e7d-ab85ade7fdae |
| Jogador 4 | 3-7 | 172 | BUY | STABILIZE | 46.0 | 7 | 10 | 1 | 26.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12235797196626663 | 0.0 | 0.0 | +eab06dbd-05d4-43b6-88f0-e6abb0e83d34 / -— |
| Jogador 4 | 3-7 | 173 | MOVE_BENCH | STABILIZE | 46.0 | 7 | 7 | 0 | 26.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0656135082244873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 174 | MOVE_BENCH | STABILIZE | 46.0 | 7 | 7 | 0 | 36.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016109490767121315 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 175 | MOVE_BENCH | STABILIZE | 46.0 | 7 | 7 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2367338240146637 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 176 | MOVE_BENCH | STABILIZE | 46.0 | 7 | 7 | 0 | 26.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08582806587219238 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 177 | BUY_XP | STABILIZE | 46.0 | 7 | 7 | 0 | 36.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 178 | MOVE_BOARD | STABILIZE | 46.0 | 7 | 3 | 0 | 36.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14355261623859406 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 179 | MOVE_BENCH | STABILIZE | 46.0 | 7 | 3 | 0 | 36.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7284420132637024 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 181 | BUY | STABILIZE | 46.0 | 7 | 9 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.12255233526229858 | 0.0 | 0.0 | +42733dbd-0bc3-461b-95ab-76daf5ad6296 / -— |
| Jogador 4 | 4-1 | 182 | CRAFT_AND_EQUIP | STABILIZE | 46.0 | 7 | 6 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08713789284229279 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 183 | BUY_XP | STABILIZE | 46.0 | 7 | 6 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 184 | MOVE_BOARD | STABILIZE | 46.0 | 7 | 2 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 185 | MOVE_BOARD | STABILIZE | 46.0 | 7 | 2 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17993684113025665 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 186 | MOVE_BOARD | STABILIZE | 46.0 | 7 | 2 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29512158036231995 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 187 | MOVE_BOARD | STABILIZE | 46.0 | 7 | 2 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15923942625522614 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 188 | SELL | STABILIZE | 46.0 | 7 | 2 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17255233228206635 | 0.0 | 0.0 | +— / -42733dbd-0bc3-461b-95ab-76daf5ad6296 |
| Jogador 4 | 4-1 | 189 | BUY_XP | STABILIZE | 46.0 | 7 | 5 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 191 | MOVE_BENCH | STABILIZE | 34.0 | 7 | 7 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21412540972232819 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 192 | MOVE_BENCH | STABILIZE | 34.0 | 7 | 7 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17933796346187592 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 193 | PASS | STABILIZE | 34.0 | 7 | 7 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 201 | BUY | STABILIZE | 22.0 | 7 | 14 | 1 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7438226342201233 | 0.0 | 0.0 | +60138930-82d5-4f1c-a5fe-a22ea4b70d36 / -— |
| Jogador 4 | 4-3 | 202 | BUY_XP | STABILIZE | 22.0 | 7 | 11 | 1 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 203 | BUY_XP | STABILIZE | 22.0 | 7 | 7 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 204 | MOVE_BOARD | STABILIZE | 22.0 | 7 | 3 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 205 | MOVE_BENCH | STABILIZE | 22.0 | 7 | 3 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 206 | PASS | STABILIZE | 22.0 | 7 | 3 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 211 | BUY_XP | ALL_IN | 9.0 | 7 | 11 | 1 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 212 | BUY_XP | ALL_IN | 9.0 | 7 | 7 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 213 | MOVE_BENCH | ALL_IN | 9.0 | 7 | 3 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1686304658651352 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 214 | MOVE_BENCH | ALL_IN | 9.0 | 7 | 3 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00316683785058558 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 215 | PASS | ALL_IN | 9.0 | 7 | 3 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 221 | BUY_XP | ALL_IN | 9.0 | 7 | 11 | 1 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 222 | BUY_XP | ALL_IN | 9.0 | 7 | 7 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 223 | MOVE_BENCH | ALL_IN | 9.0 | 7 | 3 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 224 | MOVE_BENCH | ALL_IN | 9.0 | 7 | 3 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003495350480079651 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 225 | MOVE_BENCH | ALL_IN | 9.0 | 7 | 3 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11171477288007736 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 226 | MOVE_BENCH | ALL_IN | 9.0 | 7 | 3 | 0 | 26.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15507090091705322 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 227 | MOVE_BENCH | ALL_IN | 9.0 | 7 | 3 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 228 | MOVE_BENCH | ALL_IN | 9.0 | 7 | 3 | 0 | 32.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15510563552379608 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 229 | PASS | ALL_IN | 9.0 | 7 | 3 | 0 | 26.0 | Fera do Rift/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 231 | PASS | ALL_IN | 0.0 | 7 | 3 | 0 | 0.0 | Fera do Rift/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 241 | PASS | ALL_IN | 0.0 | 7 | 3 | 0 | 0.0 | Fera do Rift/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 251 | PASS | ALL_IN | 0.0 | 7 | 3 | 0 | 0.0 | Fera do Rift/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 261 | PASS | ALL_IN | 0.0 | 7 | 3 | 0 | 0.0 | Fera do Rift/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 271 | PASS | ALL_IN | 0.0 | 7 | 3 | 0 | 0.0 | Fera do Rift/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 281 | PASS | ALL_IN | 0.0 | 7 | 3 | 0 | 0.0 | Fera do Rift/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 291 | PASS | ALL_IN | 0.0 | 7 | 3 | 0 | 0.0 | Fera do Rift/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 301 | PASS | ALL_IN | 0.0 | 7 | 3 | 0 | 0.0 | Fera do Rift/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 311 | PASS | ALL_IN | 0.0 | 7 | 3 | 0 | 0.0 | Fera do Rift/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 321 | PASS | ALL_IN | 0.0 | 7 | 3 | 0 | 0.0 | Fera do Rift/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-2 | 331 | PASS | ALL_IN | 0.0 | 7 | 3 | 0 | 0.0 | Fera do Rift/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 9 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.27265432476997375 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.027269404381513596 | 0.0 | 0.0 | +df7d3860-9b2e-45ed-b564-281d95e64e82 / -— |
| Jogador 5 | 1-2 | 12 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27256545424461365 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2792328894138336 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 22 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5755952000617981 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2996687889099121 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Elise | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49867820739746094 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 33 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 12.0 | —/DA_18_Sejuani | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27146995067596436 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 42 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 49 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6333560347557068 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 51 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4214632511138916 | 0.0 | 0.0 | +68cd8ae3-399f-461f-89a8-189d7b0a6b59 / -— |
| Jogador 5 | 2-2 | 52 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28077343106269836 | 0.0 | 0.0 | +0debca82-3a2a-44ba-af48-83211d5e5243 / -— |
| Jogador 5 | 2-2 | 53 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08733417093753815 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 54 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003409853670746088 | 0.0 | 0.0 | +— / -f9c418e0-f8aa-4492-8b97-8855ce3af370 |
| Jogador 5 | 2-2 | 55 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 61 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 10 | 1 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3353561758995056 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 62 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 10 | 1 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11772681772708893 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 63 | BUY_XP | STABILIZE | 100.0 | 4 | 10 | 1 | 20.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 64 | BUY_XP | STABILIZE | 100.0 | 4 | 6 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4494999945163727 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 65 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5821123123168945 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 66 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47855260968208313 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -— |
| Jogador 5 | 2-3 | 67 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 24.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00011049354361603037 | 0.0 | 0.0 | +— / -abde1e81-f452-47ad-9f1e-45efb138f86d |
| Jogador 5 | 2-3 | 68 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 2 | 0 | 24.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0569697804749012 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 69 | SELL | ECON | 100.0 | 5 | 2 | 0 | 26.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04938894882798195 | 0.0 | 0.0 | +— / -1934c7ef-cc22-45b3-bed9-01aea61ffbdb |
| Jogador 5 | 2-4 | 71 | BUY | ECON | 95.0 | 5 | 9 | 0 | 26.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19721397757530212 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 72 | BUY | ECON | 95.0 | 5 | 6 | 0 | 26.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3800264596939087 | 0.0 | 0.0 | +17cfefac-b43e-4a72-b6cb-1d559cc22ed1 / -— |
| Jogador 5 | 2-4 | 73 | MOVE_BENCH | ECON | 95.0 | 5 | 4 | 0 | 26.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4742327332496643 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 74 | MOVE_BENCH | ECON | 95.0 | 5 | 4 | 0 | 26.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2962343096733093 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 75 | PASS | ECON | 95.0 | 5 | 4 | 0 | 26.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 81 | BUY | ECON | 95.0 | 5 | 9 | 0 | 26.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.053158003836870193 | 0.0 | 0.0 | +486e92ad-4dcf-4c0e-a470-e0b87777d380 / -— |
| Jogador 5 | 2-5 | 82 | BUY_XP | ECON | 95.0 | 5 | 6 | 0 | 26.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 83 | PASS | ECON | 95.0 | 5 | 2 | 0 | 26.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 91 | MOVE_BENCH | ECON | 95.0 | 5 | 8 | 0 | 26.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04536784067749977 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 92 | MOVE_BENCH | ECON | 95.0 | 5 | 8 | 0 | 26.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07978671789169312 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 93 | BUY_XP | ECON | 95.0 | 5 | 8 | 0 | 26.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 94 | BUY_XP | ECON | 95.0 | 5 | 4 | 0 | 26.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08950000256299973 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 95 | SELL | ECON | 95.0 | 6 | 0 | 0 | 26.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020380165427923203 | 0.0 | 0.0 | +— / -17cfefac-b43e-4a72-b6cb-1d559cc22ed1 |
| Jogador 5 | 2-6 | 96 | BUY | ECON | 95.0 | 6 | 2 | 0 | 26.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8904485106468201 | 0.0 | 0.0 | +ae570779-3ae8-49b3-acdb-607fc512fcea / -— |
| Jogador 5 | 2-6 | 97 | SELL | ECON | 95.0 | 6 | 0 | 0 | 26.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1986246258020401 | 0.0 | 0.0 | +— / -ae570779-3ae8-49b3-acdb-607fc512fcea |
| Jogador 5 | 2-6 | 98 | MOVE_BENCH | ECON | 95.0 | 6 | 2 | 0 | 26.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40354421734809875 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 99 | MOVE_BENCH | ECON | 95.0 | 6 | 2 | 0 | 32.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0343630351126194 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 101 | BUY | ECON | 87.0 | 6 | 7 | 0 | 32.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8854554295539856 | 0.0 | 0.0 | +837b2d09-a207-4830-b36d-29e493bbcc22 / -— |
| Jogador 5 | 2-7 | 102 | BUY_XP | ECON | 87.0 | 6 | 5 | 0 | 32.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07800000160932541 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 103 | SELL | ECON | 87.0 | 6 | 1 | 0 | 32.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.188875213265419 | 0.0 | 0.0 | +— / -837b2d09-a207-4830-b36d-29e493bbcc22 |
| Jogador 5 | 2-7 | 104 | MOVE_BENCH | ECON | 87.0 | 6 | 3 | 0 | 32.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12236267328262329 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 105 | BUY | ECON | 87.0 | 6 | 3 | 0 | 32.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8835147619247437 | 0.0 | 0.0 | +46838f8d-8037-485c-8c34-9639f14ada19 / -— |
| Jogador 5 | 2-7 | 106 | SELL | ECON | 87.0 | 6 | 1 | 0 | 32.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18900075554847717 | 0.0 | 0.0 | +— / -46838f8d-8037-485c-8c34-9639f14ada19 |
| Jogador 5 | 2-7 | 107 | MOVE_BOARD | ECON | 87.0 | 6 | 3 | 0 | 32.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1760186403989792 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 108 | MOVE_BENCH | ECON | 87.0 | 6 | 3 | 0 | 32.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3015170097351074 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 109 | MOVE_BENCH | ECON | 87.0 | 6 | 3 | 0 | 32.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07451692968606949 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 111 | BUY | ECON | 87.0 | 6 | 8 | 0 | 32.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.673474907875061 | 0.0 | 0.0 | +e8c36276-b932-45ba-b350-2d1cb339a019 / -— |
| Jogador 5 | 3-1 | 112 | BUY | STABILIZE | 87.0 | 6 | 5 | 0 | 32.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7188693284988403 | 0.0 | 0.0 | +ae9f0b1e-4654-43eb-ae65-4f16dff93765 / -— |
| Jogador 5 | 3-1 | 113 | MOVE_BENCH | STABILIZE | 87.0 | 6 | 3 | 0 | 32.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10217123478651047 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 114 | MOVE_BENCH | STABILIZE | 87.0 | 6 | 3 | 0 | 32.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.235530823469162 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 115 | PASS | STABILIZE | 87.0 | 6 | 3 | 0 | 32.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 121 | BUY | STABILIZE | 76.0 | 6 | 9 | 0 | 32.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8335835933685303 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -0debca82-3a2a-44ba-af48-83211d5e5243,e8c36276-b932-45ba-b350-2d1cb339a019 |
| Jogador 5 | 3-2 | 122 | BUY | STABILIZE | 76.0 | 6 | 6 | 0 | 20.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8359169363975525 | 0.0 | 0.0 | +4d8c374c-264c-47d9-8cfc-78cbf64ceda0 / -7098795b-11bf-4b73-837a-87f5d8aece4c,ae9f0b1e-4654-43eb-ae65-4f16dff93765 |
| Jogador 5 | 3-2 | 123 | BUY_XP | STABILIZE | 76.0 | 6 | 4 | 0 | 16.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 124 | SELL | STABILIZE | 76.0 | 6 | 0 | 0 | 16.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16113846004009247 | 0.0 | 0.0 | +— / -4d8c374c-264c-47d9-8cfc-78cbf64ceda0 |
| Jogador 5 | 3-2 | 125 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 5 | 0 | 16.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29391348361968994 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 126 | BUY_XP | STABILIZE | 76.0 | 6 | 5 | 0 | 22.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 127 | SELL | STABILIZE | 76.0 | 6 | 1 | 0 | 22.0 | Florescer/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05473846197128296 | 0.0 | 0.0 | +— / -df330dae-9fc1-440f-896d-a733d052e5ba |
| Jogador 5 | 3-2 | 128 | BUY_XP | STABILIZE | 76.0 | 6 | 4 | 0 | 22.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 129 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 0 | 0 | 22.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36128008365631104 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 131 | BUY | STABILIZE | 64.0 | 6 | 6 | 0 | 34.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.27042660117149353 | 0.0 | 0.0 | +8a4d0946-b80f-4fbb-ab7c-d43c2697c34e / -— |
| Jogador 5 | 3-3 | 132 | BUY | STABILIZE | 64.0 | 6 | 2 | 0 | 34.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2849014699459076 | 0.0 | 0.0 | +8a4e95ea-d35a-4690-9313-126b5d86773e / -— |
| Jogador 5 | 3-3 | 133 | MOVE_BENCH | STABILIZE | 64.0 | 6 | 0 | 0 | 34.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5783092975616455 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 134 | MOVE_BOARD | STABILIZE | 64.0 | 6 | 0 | 0 | 42.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1754526048898697 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 135 | SELL | STABILIZE | 64.0 | 6 | 0 | 0 | 42.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13390769064426422 | 0.0 | 0.0 | +— / -8a4e95ea-d35a-4690-9313-126b5d86773e |
| Jogador 5 | 3-3 | 136 | BUY | STABILIZE | 64.0 | 6 | 2 | 0 | 42.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.2216571569442749 | 0.0 | 0.0 | +a29f1c5b-c2f0-48be-b39c-0aa0d57fb94a / -— |
| Jogador 5 | 3-3 | 137 | SELL | STABILIZE | 64.0 | 6 | 0 | 0 | 42.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12006153911352158 | 0.0 | 0.0 | +— / -a29f1c5b-c2f0-48be-b39c-0aa0d57fb94a |
| Jogador 5 | 3-3 | 138 | MOVE_BOARD | STABILIZE | 64.0 | 6 | 2 | 0 | 42.0 | Florescer/DA_18_Tristana | REROLL, MOVE_BOARD, PASS | True | True | -0.16937078535556793 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 139 | PASS | STABILIZE | 64.0 | 6 | 2 | 0 | 42.0 | Florescer/DA_18_Tristana | REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 141 | BUY | STABILIZE | 64.0 | 6 | 8 | 0 | 42.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.26274317502975464 | 0.0 | 0.0 | +3a11170d-1b8e-4316-ad59-9a7e60071f12 / -— |
| Jogador 5 | 3-4 | 142 | BUY_XP | STABILIZE | 64.0 | 6 | 6 | 0 | 42.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 143 | MOVE_BENCH | STABILIZE | 64.0 | 6 | 2 | 0 | 42.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44604578614234924 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 144 | MOVE_BENCH | STABILIZE | 64.0 | 6 | 2 | 0 | 38.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08478809893131256 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 145 | PASS | STABILIZE | 64.0 | 6 | 2 | 0 | 40.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 151 | BUY | STABILIZE | 64.0 | 6 | 7 | 0 | 40.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050896864384412766 | 0.0 | 0.0 | +9bbd1da9-6a26-472c-912e-165ea4031b90 / -— |
| Jogador 5 | 3-5 | 152 | BUY_XP | STABILIZE | 64.0 | 6 | 4 | 0 | 40.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.429500013589859 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 153 | PASS | STABILIZE | 64.0 | 7 | 0 | 0 | 40.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 159 | MOVE_BENCH | STABILIZE | 64.0 | 7 | 0 | 0 | 40.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4544205665588379 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 161 | BUY | STABILIZE | 53.0 | 7 | 5 | 0 | 46.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7318402528762817 | 0.0 | 0.0 | +750eedbe-93d9-46de-b3b8-a88e41f395f0 / -— |
| Jogador 5 | 3-6 | 162 | MOVE_BENCH | STABILIZE | 53.0 | 7 | 2 | 0 | 46.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42781636118888855 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 163 | MOVE_BENCH | STABILIZE | 53.0 | 7 | 2 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0580095611512661 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 164 | MOVE_BENCH | STABILIZE | 53.0 | 7 | 2 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44641268253326416 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 165 | BUY | STABILIZE | 53.0 | 7 | 2 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28762006759643555 | 0.0 | 0.0 | +82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 / -— |
| Jogador 5 | 3-6 | 166 | PASS | STABILIZE | 53.0 | 7 | 1 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 171 | BUY | STABILIZE | 53.0 | 7 | 7 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07297129184007645 | 0.0 | 0.0 | +bd0feb3d-9ff5-4678-862f-202b3bf74d5c / -— |
| Jogador 5 | 3-7 | 172 | BUY_XP | STABILIZE | 53.0 | 7 | 4 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 173 | SELL | STABILIZE | 53.0 | 7 | 0 | 0 | 48.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.136461541056633 | 0.0 | 0.0 | +— / -82ac67a6-7f48-40f4-a8ea-b49f7b4aba65 |
| Jogador 5 | 3-7 | 174 | MOVE_BENCH | STABILIZE | 53.0 | 7 | 1 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07787004858255386 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 175 | MOVE_BENCH | STABILIZE | 53.0 | 7 | 1 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05569921433925629 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 176 | MOVE_BENCH | STABILIZE | 53.0 | 7 | 1 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5037589073181152 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 177 | MOVE_BENCH | STABILIZE | 53.0 | 7 | 1 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07423821836709976 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 178 | SELL | STABILIZE | 53.0 | 7 | 1 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10385329276323318 | 0.0 | 0.0 | +— / -3a11170d-1b8e-4316-ad59-9a7e60071f12 |
| Jogador 5 | 3-7 | 179 | MOVE_BENCH | STABILIZE | 53.0 | 7 | 3 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05747571215033531 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 181 | BUY | STABILIZE | 53.0 | 7 | 8 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7015067338943481 | 0.0 | 0.0 | +1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 / -— |
| Jogador 5 | 4-1 | 182 | BUY | STABILIZE | 53.0 | 7 | 5 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2234620302915573 | 0.0 | 0.0 | +60255a84-4f78-49f0-a4f1-d598704c7ee7 / -— |
| Jogador 5 | 4-1 | 183 | SELL | STABILIZE | 53.0 | 7 | 2 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06599999964237213 | 0.0 | 0.0 | +— / -9bbd1da9-6a26-472c-912e-165ea4031b90 |
| Jogador 5 | 4-1 | 184 | BUY_XP | STABILIZE | 53.0 | 7 | 5 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 185 | SELL | STABILIZE | 53.0 | 7 | 1 | 0 | 48.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10967294871807098 | 0.0 | 0.0 | +— / -60255a84-4f78-49f0-a4f1-d598704c7ee7 |
| Jogador 5 | 4-1 | 186 | BUY | STABILIZE | 53.0 | 7 | 4 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2475976049900055 | 0.0 | 0.0 | +0c07379e-5dd1-42e9-aa7a-a764f949deee / -— |
| Jogador 5 | 4-1 | 187 | SELL | STABILIZE | 53.0 | 7 | 1 | 0 | 48.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11400000005960464 | 0.0 | 0.0 | +— / -0c07379e-5dd1-42e9-aa7a-a764f949deee |
| Jogador 5 | 4-1 | 188 | MOVE_BENCH | STABILIZE | 53.0 | 7 | 4 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08277608454227448 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 189 | BUY_XP | STABILIZE | 53.0 | 7 | 4 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 191 | BUY | STABILIZE | 41.0 | 7 | 5 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8299397826194763 | 0.0 | 0.0 | +dde5ed69-0fc4-4d15-b12c-a5252a239040 / -486e92ad-4dcf-4c0e-a470-e0b87777d380,750eedbe-93d9-46de-b3b8-a88e41f395f0 |
| Jogador 5 | 4-2 | 192 | BUY | STABILIZE | 41.0 | 7 | 2 | 0 | 42.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.041360192000865936 | 0.0 | 0.0 | +02c8aff1-803e-42bc-b7c2-f7cd6d986b4f / -— |
| Jogador 5 | 4-2 | 193 | MOVE_BENCH | STABILIZE | 41.0 | 7 | 0 | 0 | 42.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3333778977394104 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 194 | MOVE_BENCH | STABILIZE | 41.0 | 7 | 0 | 0 | 40.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.672164797782898 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 195 | MOVE_BENCH | STABILIZE | 41.0 | 7 | 0 | 0 | 52.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3518344759941101 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 196 | MOVE_BENCH | STABILIZE | 41.0 | 7 | 0 | 0 | 46.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1479475349187851 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 197 | MOVE_BENCH | STABILIZE | 41.0 | 7 | 0 | 0 | 54.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3307656943798065 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 198 | MOVE_BENCH | STABILIZE | 41.0 | 7 | 0 | 0 | 52.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35066187381744385 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 199 | PASS | STABILIZE | 41.0 | 7 | 0 | 0 | 46.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 201 | BUY | STABILIZE | 41.0 | 7 | 6 | 0 | 46.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7438501715660095 | 0.0 | 0.0 | +d8ecc66e-097d-4caa-a657-90fcd1286c2b / -— |
| Jogador 5 | 4-3 | 202 | BUY | STABILIZE | 41.0 | 7 | 3 | 0 | 46.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2822742462158203 | 0.0 | 0.0 | +27a4bd22-9c1f-4f9f-9192-06ea4933feb5 / -— |
| Jogador 5 | 4-3 | 203 | SELL | STABILIZE | 41.0 | 7 | 0 | 0 | 46.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10181612521409988 | 0.0 | 0.0 | +— / -dde5ed69-0fc4-4d15-b12c-a5252a239040 |
| Jogador 5 | 4-3 | 204 | BUY_XP | STABILIZE | 41.0 | 7 | 8 | 0 | 46.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 205 | BUY_XP | STABILIZE | 41.0 | 7 | 4 | 0 | 46.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 206 | SELL | STABILIZE | 41.0 | 7 | 0 | 0 | 46.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3506788909435272 | 0.0 | 0.0 | +— / -d8ecc66e-097d-4caa-a657-90fcd1286c2b |
| Jogador 5 | 4-3 | 207 | SELL | STABILIZE | 41.0 | 7 | 3 | 0 | 46.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13815566897392273 | 0.0 | 0.0 | +— / -27a4bd22-9c1f-4f9f-9192-06ea4933feb5 |
| Jogador 5 | 4-3 | 208 | BUY | STABILIZE | 41.0 | 7 | 6 | 0 | 46.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.270738810300827 | 0.0 | 0.0 | +72c247af-bdc3-410c-98dd-dd72b56f2818 / -— |
| Jogador 5 | 4-3 | 209 | MOVE_BENCH | STABILIZE | 41.0 | 7 | 3 | 0 | 46.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.062322307378053665 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 211 | BUY | STABILIZE | 28.0 | 7 | 8 | 0 | 46.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060589585453271866 | 0.0 | 0.0 | +ad19ac66-9f86-4c29-8ae7-7222164aece1 / -— |
| Jogador 5 | 4-4 | 212 | MOVE_BENCH | STABILIZE | 28.0 | 7 | 5 | 0 | 46.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06487147510051727 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 213 | BUY_XP | STABILIZE | 28.0 | 7 | 5 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 214 | SELL | STABILIZE | 28.0 | 7 | 1 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05941559001803398 | 0.0 | 0.0 | +— / -02c8aff1-803e-42bc-b7c2-f7cd6d986b4f |
| Jogador 5 | 4-4 | 215 | MOVE_BENCH | STABILIZE | 28.0 | 7 | 3 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6755428314208984 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 216 | MOVE_BENCH | STABILIZE | 28.0 | 7 | 3 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06531019508838654 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 217 | MOVE_BENCH | STABILIZE | 28.0 | 7 | 3 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3323909044265747 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 218 | MOVE_BENCH | STABILIZE | 28.0 | 7 | 3 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.507943868637085 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 219 | PASS | STABILIZE | 28.0 | 7 | 3 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 221 | BUY_XP | STABILIZE | 28.0 | 7 | 8 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 222 | BUY_XP | STABILIZE | 28.0 | 7 | 4 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 223 | SELL | STABILIZE | 28.0 | 7 | 0 | 0 | 48.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.304329514503479 | 0.0 | 0.0 | +— / -0f1b15a2-9978-4691-a15e-483ccd03db7f |
| Jogador 5 | 4-5 | 224 | MOVE_BENCH | STABILIZE | 28.0 | 7 | 3 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07950026541948318 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 225 | MOVE_BENCH | STABILIZE | 28.0 | 7 | 3 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32306647300720215 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 226 | SELL | STABILIZE | 28.0 | 7 | 3 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0904427319765091 | 0.0 | 0.0 | +— / -1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 |
| Jogador 5 | 4-5 | 227 | BUY_XP | STABILIZE | 28.0 | 7 | 6 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 228 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 2 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.17874549329280853 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 229 | MOVE_BOARD | STABILIZE | 28.0 | 7 | 2 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.30989962816238403 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 231 | BUY | STABILIZE | 16.0 | 7 | 8 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.07618661224842072 | 0.0 | 0.0 | +6e1d8af0-7f7c-4ec1-967c-e871072bc4e3 / -— |
| Jogador 5 | 4-6 | 232 | BUY | STABILIZE | 16.0 | 7 | 4 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07582701742649078 | 0.0 | 0.0 | +4a885bc0-41b4-43f1-94d3-8e755a10645c / -— |
| Jogador 5 | 4-6 | 233 | MOVE_BENCH | STABILIZE | 16.0 | 7 | 1 | 0 | 48.0 | Florescer/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5186622738838196 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 234 | SELL | STABILIZE | 16.0 | 7 | 1 | 0 | 50.0 | Florescer/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12600000202655792 | 0.0 | 0.0 | +— / -4a885bc0-41b4-43f1-94d3-8e755a10645c |
| Jogador 5 | 4-6 | 235 | BUY_XP | STABILIZE | 16.0 | 7 | 4 | 0 | 50.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43674999475479126 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 236 | MOVE_BENCH | STABILIZE | 16.0 | 8 | 0 | 0 | 50.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5448793172836304 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 237 | MOVE_BOARD | STABILIZE | 16.0 | 8 | 0 | 0 | 56.0 | Florescer/DA_18_Tristana | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 238 | MOVE_BOARD | STABILIZE | 16.0 | 8 | 0 | 0 | 56.0 | Florescer/DA_18_Tristana | MOVE_BOARD, PASS | True | True | -0.20006205141544342 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 239 | PASS | STABILIZE | 16.0 | 8 | 0 | 0 | 56.0 | Florescer/DA_18_Tristana | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 241 | BUY | ALL_IN | 2.0 | 8 | 6 | 0 | 56.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.19756191968917847 | 0.0 | 0.0 | +3a86599a-ebbe-4e57-8284-69fdd6e2d8a1 / -— |
| Jogador 5 | 4-7 | 242 | BUY | ALL_IN | 2.0 | 8 | 2 | 0 | 56.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20652785897254944 | 0.0 | 0.0 | +bae938fe-6a1c-4cd1-b700-508dd8adcca4 / -— |
| Jogador 5 | 4-7 | 243 | MOVE_BENCH | ALL_IN | 2.0 | 8 | 0 | 0 | 56.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03294242173433304 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 244 | MOVE_BENCH | ALL_IN | 2.0 | 8 | 0 | 0 | 56.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05688127875328064 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 245 | MOVE_BENCH | ALL_IN | 2.0 | 8 | 0 | 0 | 58.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35344213247299194 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 246 | MOVE_BENCH | ALL_IN | 2.0 | 8 | 0 | 0 | 56.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.044070541858673096 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 247 | PASS | ALL_IN | 2.0 | 8 | 0 | 0 | 56.0 | Florescer/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 251 | EQUIP_FROM_INVENTORY | ALL_IN | 2.0 | 8 | 6 | 0 | 56.0 | Florescer/DA_18_Tristana | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 252 | BUY | ALL_IN | 2.0 | 8 | 6 | 0 | 56.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2733294665813446 | 0.0 | 0.0 | +811fcf1f-2023-4c36-a961-d61cb0dd68d0 / -— |
| Jogador 5 | 5-1 | 253 | CRAFT_AND_EQUIP | ALL_IN | 2.0 | 8 | 3 | 0 | 56.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08114725351333618 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 254 | MOVE_BENCH | ALL_IN | 2.0 | 8 | 3 | 0 | 56.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.023478414863348007 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 255 | MOVE_BENCH | ALL_IN | 2.0 | 8 | 3 | 0 | 58.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29226961731910706 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 256 | MOVE_BENCH | ALL_IN | 2.0 | 8 | 3 | 0 | 56.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03248169645667076 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 257 | PASS | ALL_IN | 2.0 | 8 | 3 | 0 | 56.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 261 | BUY | ALL_IN | 2.0 | 8 | 9 | 0 | 56.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2721788287162781 | 0.0 | 0.0 | +2f75fcd7-1405-49fd-8a0c-649c1f8a9f09 / -— |
| Jogador 5 | 5-2 | 262 | BUY_XP | ALL_IN | 2.0 | 8 | 6 | 0 | 56.0 | Florescer/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 263 | MOVE_BENCH | ALL_IN | 2.0 | 8 | 2 | 0 | 56.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1735856682062149 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 264 | MOVE_BENCH | ALL_IN | 2.0 | 8 | 2 | 0 | 54.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5007039308547974 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 265 | MOVE_BENCH | ALL_IN | 2.0 | 8 | 2 | 0 | 56.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011290381662547588 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 266 | PASS | ALL_IN | 2.0 | 8 | 2 | 0 | 56.0 | Florescer/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 271 | PASS | ALL_IN | 0.0 | 8 | 2 | 0 | 0.0 | Florescer/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 281 | PASS | ALL_IN | 0.0 | 8 | 2 | 0 | 0.0 | Florescer/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 291 | PASS | ALL_IN | 0.0 | 8 | 2 | 0 | 0.0 | Florescer/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 301 | PASS | ALL_IN | 0.0 | 8 | 2 | 0 | 0.0 | Florescer/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 311 | PASS | ALL_IN | 0.0 | 8 | 2 | 0 | 0.0 | Florescer/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 321 | PASS | ALL_IN | 0.0 | 8 | 2 | 0 | 0.0 | Florescer/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 331 | PASS | ALL_IN | 0.0 | 8 | 2 | 0 | 0.0 | Florescer/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.05258461460471153 | 0.0 | 0.0 | +— / -698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +9002992e-4dcd-4fec-939c-87393464a41d / -— |
| Jogador 6 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 9 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.28737619519233704 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.04858612269163132 | 0.0 | 0.0 | +4d0bf502-ac30-4cdb-9da7-4f9a7ab054b1 / -— |
| Jogador 6 | 1-2 | 12 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3005092740058899 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.00015411031199619174 | 0.0 | 0.0 | +f29b0444-8dd6-44a6-9a04-824febf737a0 / -— |
| Jogador 6 | 1-3 | 22 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4412408769130707 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.019240504130721092 | 0.0 | 0.0 | +c19cf6a8-c66e-4670-b0fc-fb83453f22e7 / -— |
| Jogador 6 | 1-4 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Yunara | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5112704038619995 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 33 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 12.0 | —/DA_Murkwolf18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06491842865943909 | 0.0 | 0.0 | +75005e9c-56d1-48d6-815e-573e489e3dd7 / -— |
| Jogador 6 | 2-1 | 42 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6755994558334351 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 43 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 14.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9700382947921753 | 0.0 | 0.0 | +646fc826-453b-479f-97d1-8aa2a9d86dc3 / -— |
| Jogador 6 | 2-1 | 44 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 14.0 | —/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 51 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 14.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4570446014404297 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 52 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 53 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 14.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36547183990478516 | 0.0 | 0.0 | +— / -646fc826-453b-479f-97d1-8aa2a9d86dc3 |
| Jogador 6 | 2-2 | 54 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 14.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 61 | BUY | STABILIZE | 95.0 | 4 | 6 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3915741443634033 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 6 | 2-3 | 62 | BUY_XP | STABILIZE | 95.0 | 4 | 4 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4494999945163727 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 63 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 69 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7021920680999756 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 71 | BUY | STABILIZE | 95.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34721532464027405 | 0.0 | 0.0 | +a1c62c5f-385c-49ba-ac65-9dff28493faf / -— |
| Jogador 6 | 2-4 | 72 | BUY | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9713779091835022 | 0.0 | 0.0 | +18934be2-4988-4f62-9f62-07ba151231f2 / -— |
| Jogador 6 | 2-4 | 73 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 2 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 74 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 2 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1265406310558319 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 75 | PASS | STABILIZE | 95.0 | 5 | 2 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 81 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10588400065898895 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 82 | BUY_XP | STABILIZE | 95.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 83 | SELL | STABILIZE | 95.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21865950524806976 | 0.0 | 0.0 | +— / -18934be2-4988-4f62-9f62-07ba151231f2 |
| Jogador 6 | 2-5 | 84 | BUY_XP | STABILIZE | 95.0 | 5 | 4 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 85 | SELL | STABILIZE | 95.0 | 5 | 0 | 0 | 20.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027895549312233925 | 0.0 | 0.0 | +— / -0fff7760-179f-4d7c-8267-08d70cb6c1bd |
| Jogador 6 | 2-5 | 86 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 2 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04502463340759277 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 87 | BUY | STABILIZE | 95.0 | 5 | 2 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12284897267818451 | 0.0 | 0.0 | +c7d30607-e33e-4e6e-902a-3fd37223a8de / -— |
| Jogador 6 | 2-5 | 88 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 20.0 | —/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 91 | BUY | STABILIZE | 90.0 | 5 | 5 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9493534564971924 | 0.0 | 0.0 | +2938180d-94e5-4bb7-832e-baa51f820ba2 / -— |
| Jogador 6 | 2-6 | 92 | PASS | STABILIZE | 90.0 | 5 | 2 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 101 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 8 | 0 | 20.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04436703026294708 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 102 | BUY | STABILIZE | 83.0 | 5 | 8 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4030628502368927 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 103 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 5 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07909135520458221 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 104 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 5 | 0 | 22.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16815786063671112 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 105 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 5 | 0 | 20.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5012844800949097 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 106 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 5 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20071706175804138 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 107 | PASS | STABILIZE | 83.0 | 5 | 5 | 0 | 22.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 111 | BUY | STABILIZE | 83.0 | 6 | 11 | 1 | 22.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08413619548082352 | 0.0 | 0.0 | +4eedd873-e4ec-41e5-9f5e-48e443e80f86 / -— |
| Jogador 6 | 3-1 | 112 | BUY | STABILIZE | 83.0 | 6 | 7 | 0 | 22.0 | —/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.250404417514801 | 0.0 | 0.0 | +a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 / -— |
| Jogador 6 | 3-1 | 113 | BUY_XP | STABILIZE | 83.0 | 6 | 4 | 0 | 22.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 114 | SELL | STABILIZE | 83.0 | 6 | 0 | 0 | 22.0 | Adaptador/DA_18_Ahri | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03829142823815346 | 0.0 | 0.0 | +— / -9002992e-4dcd-4fec-939c-87393464a41d |
| Jogador 6 | 3-1 | 115 | SELL | STABILIZE | 83.0 | 6 | 1 | 0 | 22.0 | Adaptador/DA_18_Ahri | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15338461101055145 | 0.0 | 0.0 | +— / -75005e9c-56d1-48d6-815e-573e489e3dd7 |
| Jogador 6 | 3-1 | 116 | BUY | STABILIZE | 83.0 | 6 | 4 | 0 | 22.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7412853240966797 | 0.0 | 0.0 | +ab127012-83d7-46f0-a16c-b20582d1179b / -— |
| Jogador 6 | 3-1 | 117 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 2 | 0 | 22.0 | Adaptador/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16984343528747559 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 118 | SELL | STABILIZE | 83.0 | 6 | 2 | 0 | 22.0 | Adaptador/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32689231634140015 | 0.0 | 0.0 | +— / -ab127012-83d7-46f0-a16c-b20582d1179b |
| Jogador 6 | 3-1 | 119 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 4 | 0 | 22.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41674646735191345 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 121 | BUY | STABILIZE | 73.0 | 6 | 10 | 1 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24926400184631348 | 0.0 | 0.0 | +6e096b30-0b49-4a98-8596-8b05089793ae / -— |
| Jogador 6 | 3-2 | 122 | BUY_XP | STABILIZE | 73.0 | 6 | 7 | 0 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 123 | MOVE_BENCH | STABILIZE | 73.0 | 6 | 3 | 0 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33943498134613037 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 124 | SELL | STABILIZE | 73.0 | 6 | 3 | 0 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13390769064426422 | 0.0 | 0.0 | +— / -c7d30607-e33e-4e6e-902a-3fd37223a8de |
| Jogador 6 | 3-2 | 125 | BUY_XP | STABILIZE | 73.0 | 6 | 5 | 0 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 126 | SELL | STABILIZE | 73.0 | 6 | 1 | 0 | 32.0 | Adaptador/DA_18_Ahri | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3401167392730713 | 0.0 | 0.0 | +— / -6e096b30-0b49-4a98-8596-8b05089793ae |
| Jogador 6 | 3-2 | 127 | BUY_XP | STABILIZE | 73.0 | 6 | 4 | 0 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 128 | SELL | STABILIZE | 73.0 | 6 | 0 | 0 | 32.0 | Adaptador/DA_18_Ahri | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06018902361392975 | 0.0 | 0.0 | +— / -2938180d-94e5-4bb7-832e-baa51f820ba2 |
| Jogador 6 | 3-2 | 129 | MOVE_BENCH | STABILIZE | 73.0 | 6 | 3 | 0 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03355413302779198 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 131 | BUY | STABILIZE | 62.0 | 6 | 9 | 0 | 30.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7411952614784241 | 0.0 | 0.0 | +ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b / -— |
| Jogador 6 | 3-3 | 132 | BUY | STABILIZE | 62.0 | 6 | 6 | 0 | 30.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28563228249549866 | 0.0 | 0.0 | +25b16126-6e41-4649-a47f-42656ffc7a08 / -— |
| Jogador 6 | 3-3 | 133 | BUY_XP | STABILIZE | 62.0 | 6 | 4 | 0 | 30.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 134 | SELL | STABILIZE | 62.0 | 6 | 0 | 0 | 30.0 | Adaptador/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13464614748954773 | 0.0 | 0.0 | +— / -25b16126-6e41-4649-a47f-42656ffc7a08 |
| Jogador 6 | 3-3 | 135 | SELL | STABILIZE | 62.0 | 6 | 2 | 0 | 30.0 | Adaptador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3275652825832367 | 0.0 | 0.0 | +— / -ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b |
| Jogador 6 | 3-3 | 136 | BUY_XP | STABILIZE | 62.0 | 6 | 5 | 0 | 30.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 137 | SELL | STABILIZE | 62.0 | 6 | 1 | 0 | 30.0 | Adaptador/DA_18_Ahri | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10993846505880356 | 0.0 | 0.0 | +— / -a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 |
| Jogador 6 | 3-3 | 138 | MOVE_BENCH | STABILIZE | 62.0 | 6 | 4 | 0 | 30.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3178301453590393 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 139 | BUY_XP | STABILIZE | 62.0 | 6 | 4 | 0 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 141 | BUY | STABILIZE | 62.0 | 6 | 6 | 0 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28151246905326843 | 0.0 | 0.0 | +333cdd27-0114-4d36-8ffa-e79b0f43b8e8 / -— |
| Jogador 6 | 3-4 | 142 | BUY | STABILIZE | 62.0 | 6 | 3 | 0 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7354251742362976 | 0.0 | 0.0 | +4698e3b3-0833-4895-a1f1-26b372b2f965 / -— |
| Jogador 6 | 3-4 | 143 | SELL | STABILIZE | 62.0 | 6 | 1 | 0 | 32.0 | Adaptador/DA_18_Ahri | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3176615238189697 | 0.0 | 0.0 | +— / -4698e3b3-0833-4895-a1f1-26b372b2f965 |
| Jogador 6 | 3-4 | 144 | MOVE_BENCH | STABILIZE | 62.0 | 6 | 3 | 0 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1904064565896988 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 145 | SELL | STABILIZE | 62.0 | 6 | 3 | 0 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04315423220396042 | 0.0 | 0.0 | +— / -43da0d73-facd-488b-b856-94e9496a97f9 |
| Jogador 6 | 3-4 | 146 | MOVE_BENCH | STABILIZE | 62.0 | 6 | 6 | 0 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5238975286483765 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 147 | BUY | STABILIZE | 62.0 | 6 | 6 | 0 | 30.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09497804194688797 | 0.0 | 0.0 | +d056a271-6a74-4e71-bde6-087b97d2c527 / -— |
| Jogador 6 | 3-4 | 148 | SELL | STABILIZE | 62.0 | 6 | 2 | 0 | 30.0 | Adaptador/DA_18_Ahri | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09935533255338669 | 0.0 | 0.0 | +— / -4eedd873-e4ec-41e5-9f5e-48e443e80f86 |
| Jogador 6 | 3-4 | 149 | BUY_XP | STABILIZE | 62.0 | 6 | 6 | 0 | 30.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7570000290870667 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 151 | BUY | STABILIZE | 62.0 | 7 | 7 | 0 | 30.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2824901342391968 | 0.0 | 0.0 | +5b95b64a-b46a-4827-8613-307c8dadc072 / -— |
| Jogador 6 | 3-5 | 152 | BUY | STABILIZE | 62.0 | 7 | 4 | 0 | 30.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2833535969257355 | 0.0 | 0.0 | +6db008fd-a1dd-40ad-b3d2-583a4bbff9d4 / -— |
| Jogador 6 | 3-5 | 153 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 1 | 0 | 30.0 | Adaptador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5215010046958923 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 154 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 1 | 0 | 32.0 | Adaptador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.660111665725708 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 155 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 1 | 0 | 38.0 | Adaptador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13758485019207 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 156 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 1 | 0 | 38.0 | Adaptador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31986159086227417 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 157 | PASS | STABILIZE | 62.0 | 7 | 1 | 0 | 38.0 | Adaptador/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 161 | BUY | STABILIZE | 62.0 | 7 | 8 | 0 | 38.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7425414323806763 | 0.0 | 0.0 | +cf68219b-1d38-45a1-98db-495871c932ea / -— |
| Jogador 6 | 3-6 | 162 | BUY | STABILIZE | 62.0 | 7 | 5 | 0 | 38.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.833965539932251 | 0.0 | 0.0 | +ab472080-6e4b-4b75-b37d-cf10da9a5a0d / -5b95b64a-b46a-4827-8613-307c8dadc072,cf68219b-1d38-45a1-98db-495871c932ea |
| Jogador 6 | 3-6 | 163 | SELL | STABILIZE | 62.0 | 7 | 2 | 0 | 38.0 | Adaptador/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07222896069288254 | 0.0 | 0.0 | +— / -ab472080-6e4b-4b75-b37d-cf10da9a5a0d |
| Jogador 6 | 3-6 | 164 | BUY | STABILIZE | 62.0 | 7 | 10 | 1 | 38.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08983512967824936 | 0.0 | 0.0 | +604cc5dc-6c20-4d5a-b3a7-8862adfe1930 / -— |
| Jogador 6 | 3-6 | 165 | BUY_XP | STABILIZE | 62.0 | 7 | 7 | 0 | 38.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 166 | SELL | STABILIZE | 62.0 | 7 | 3 | 0 | 38.0 | Adaptador/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13983513414859772 | 0.0 | 0.0 | +— / -604cc5dc-6c20-4d5a-b3a7-8862adfe1930 |
| Jogador 6 | 3-6 | 167 | BUY_XP | STABILIZE | 62.0 | 7 | 6 | 0 | 38.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 168 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 2 | 0 | 38.0 | Adaptador/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09712766855955124 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 169 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 2 | 0 | 36.0 | Adaptador/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1354132741689682 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 171 | BUY | STABILIZE | 62.0 | 7 | 9 | 0 | 38.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06540782004594803 | 0.0 | 0.0 | +891aea62-e06a-46d4-8250-a3d4a56e847d / -— |
| Jogador 6 | 3-7 | 172 | BUY | STABILIZE | 62.0 | 7 | 4 | 0 | 38.0 | Adaptador/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07495234161615372 | 0.0 | 0.0 | +665661af-7240-4a65-bf3d-f4ecf3532a85 / -— |
| Jogador 6 | 3-7 | 173 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 0 | 0 | 38.0 | Adaptador/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02646191231906414 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 174 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 0 | 0 | 40.0 | Adaptador/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09706149995326996 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 175 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 0 | 0 | 38.0 | Adaptador/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06306923180818558 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 176 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 0 | 0 | 38.0 | Adaptador/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0236262995749712 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 177 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 0 | 0 | 40.0 | Adaptador/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09702647477388382 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 178 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 0 | 0 | 38.0 | Adaptador/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00494177034124732 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 179 | SELL | STABILIZE | 62.0 | 7 | 0 | 0 | 40.0 | Adaptador/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06599999964237213 | 0.0 | 0.0 | +— / -a1c62c5f-385c-49ba-ac65-9dff28493faf |
| Jogador 6 | 4-1 | 181 | BUY | STABILIZE | 62.0 | 7 | 9 | 0 | 40.0 | Adaptador/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011635961942374706 | 0.0 | 0.0 | +f6b79583-b2fa-49a2-8adf-9b529a9eb3ae / -— |
| Jogador 6 | 4-1 | 182 | MOVE_BENCH | STABILIZE | 62.0 | 7 | 6 | 0 | 40.0 | Adaptador/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06630562245845795 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 183 | BUY_XP | STABILIZE | 62.0 | 7 | 6 | 0 | 44.0 | Adaptador/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 184 | SELL | STABILIZE | 62.0 | 7 | 2 | 0 | 44.0 | Adaptador/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13492903113365173 | 0.0 | 0.0 | +— / -f6b79583-b2fa-49a2-8adf-9b529a9eb3ae |
| Jogador 6 | 4-1 | 185 | BUY_XP | STABILIZE | 62.0 | 7 | 5 | 0 | 44.0 | Adaptador/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 186 | SELL | STABILIZE | 62.0 | 7 | 1 | 0 | 44.0 | Adaptador/DA_18_GnarSmall | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1236795112490654 | 0.0 | 0.0 | +— / -6db008fd-a1dd-40ad-b3d2-583a4bbff9d4 |
| Jogador 6 | 4-1 | 187 | BUY_XP | STABILIZE | 62.0 | 7 | 4 | 0 | 44.0 | Adaptador/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 188 | SELL | STABILIZE | 62.0 | 7 | 0 | 0 | 44.0 | Adaptador/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13332919776439667 | 0.0 | 0.0 | +— / -7c4fb31e-7de8-491a-bb02-ef0111cd9ede |
| Jogador 6 | 4-1 | 189 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 3 | 0 | 44.0 | Adaptador/DA_18_GnarSmall | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.31992700695991516 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 191 | BUY | STABILIZE | 62.0 | 7 | 10 | 1 | 44.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.15225113928318024 | 0.0 | 0.0 | +86530a1f-5325-45fa-bf43-86419ccfda54 / -— |
| Jogador 6 | 4-2 | 192 | BUY | STABILIZE | 62.0 | 7 | 6 | 0 | 44.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27320072054862976 | 0.0 | 0.0 | +ef54ddfd-f436-4813-9585-cb652488ffa3 / -— |
| Jogador 6 | 4-2 | 193 | BUY_XP | STABILIZE | 62.0 | 7 | 4 | 0 | 44.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 194 | SELL | STABILIZE | 62.0 | 7 | 0 | 0 | 44.0 | Defendente/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11025940626859665 | 0.0 | 0.0 | +— / -ef54ddfd-f436-4813-9585-cb652488ffa3 |
| Jogador 6 | 4-2 | 195 | SELL | STABILIZE | 62.0 | 7 | 2 | 0 | 44.0 | Defendente/DA_18_GnarSmall | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020599571987986565 | 0.0 | 0.0 | +— / -86530a1f-5325-45fa-bf43-86419ccfda54 |
| Jogador 6 | 4-2 | 196 | BUY_XP | STABILIZE | 62.0 | 7 | 6 | 0 | 44.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 197 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 2 | 0 | 44.0 | Defendente/DA_18_GnarSmall | REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 198 | MOVE_BOARD | STABILIZE | 62.0 | 7 | 2 | 0 | 44.0 | Defendente/DA_18_GnarSmall | REROLL, MOVE_BOARD, PASS | True | True | 0.17192716896533966 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 199 | PASS | STABILIZE | 62.0 | 7 | 2 | 0 | 44.0 | Defendente/DA_18_GnarSmall | REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 201 | BUY | STABILIZE | 62.0 | 7 | 10 | 1 | 44.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.20185957849025726 | 0.0 | 0.0 | +03e5f6e4-e80d-49c1-b5bb-e5b158d96f51 / -— |
| Jogador 6 | 4-3 | 202 | BUY | STABILIZE | 62.0 | 7 | 6 | 0 | 44.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2796652019023895 | 0.0 | 0.0 | +a9588010-57fa-4baf-b226-a30f519342e7 / -— |
| Jogador 6 | 4-3 | 203 | BUY_XP | STABILIZE | 62.0 | 7 | 4 | 0 | 44.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 204 | SELL | STABILIZE | 62.0 | 7 | 0 | 0 | 44.0 | Defendente/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11226256191730499 | 0.0 | 0.0 | +— / -a9588010-57fa-4baf-b226-a30f519342e7 |
| Jogador 6 | 4-3 | 205 | SELL | STABILIZE | 62.0 | 7 | 2 | 0 | 44.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12529230117797852 | 0.0 | 0.0 | +— / -03e5f6e4-e80d-49c1-b5bb-e5b158d96f51 |
| Jogador 6 | 4-3 | 206 | BUY_XP | STABILIZE | 62.0 | 7 | 6 | 0 | 44.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 207 | PASS | STABILIZE | 62.0 | 7 | 2 | 0 | 44.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 211 | BUY | STABILIZE | 62.0 | 7 | 11 | 1 | 44.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.2112807184457779 | 0.0 | 0.0 | +677ea844-e1bf-4c68-a0b0-136abb86ba7b / -— |
| Jogador 6 | 4-4 | 212 | BUY_XP | STABILIZE | 62.0 | 7 | 8 | 0 | 44.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4323124885559082 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 213 | MOVE_BENCH | WINSTREAK | 62.0 | 8 | 4 | 0 | 44.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23336085677146912 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 214 | BUY | WINSTREAK | 62.0 | 8 | 4 | 0 | 40.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06725306808948517 | 0.0 | 0.0 | +b755a0c5-f515-4f95-8f58-1e05f40ad302 / -— |
| Jogador 6 | 4-4 | 215 | BUY | WINSTREAK | 62.0 | 8 | 1 | 0 | 40.0 | Defendente/DA_18_GnarSmall | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23547935485839844 | 0.0 | 0.0 | +e7c7b5ea-79ec-44e9-ae6c-6e881b84fe15 / -— |
| Jogador 6 | 4-4 | 216 | SELL | WINSTREAK | 62.0 | 8 | 0 | 0 | 40.0 | Defendente/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013446154072880745 | 0.0 | 0.0 | +— / -e7c7b5ea-79ec-44e9-ae6c-6e881b84fe15 |
| Jogador 6 | 4-4 | 217 | BUY | WINSTREAK | 62.0 | 8 | 1 | 0 | 40.0 | Defendente/DA_18_GnarSmall | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028377020731568336 | 0.0 | 0.0 | +15c93ffb-d63e-43e6-aa46-ba2beed9cb53 / -— |
| Jogador 6 | 4-4 | 218 | SELL | WINSTREAK | 62.0 | 8 | 0 | 0 | 40.0 | Defendente/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13603076338768005 | 0.0 | 0.0 | +— / -15c93ffb-d63e-43e6-aa46-ba2beed9cb53 |
| Jogador 6 | 4-4 | 219 | MOVE_BENCH | WINSTREAK | 62.0 | 8 | 1 | 0 | 40.0 | Defendente/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7807741165161133 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 221 | BUY | WINSTREAK | 62.0 | 8 | 9 | 0 | 50.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7029966115951538 | 0.0 | 0.0 | +61362365-2cf7-40e4-95f9-98e28728fd39 / -— |
| Jogador 6 | 4-5 | 222 | BUY_XP | WINSTREAK | 62.0 | 8 | 7 | 0 | 50.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 223 | MOVE_BENCH | WINSTREAK | 62.0 | 8 | 3 | 0 | 50.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09282542020082474 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 224 | SELL | WINSTREAK | 62.0 | 8 | 3 | 0 | 48.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0536307692527771 | 0.0 | 0.0 | +— / -677ea844-e1bf-4c68-a0b0-136abb86ba7b |
| Jogador 6 | 4-5 | 225 | BUY_XP | WINSTREAK | 62.0 | 8 | 6 | 0 | 48.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 226 | MOVE_BENCH | WINSTREAK | 62.0 | 8 | 2 | 0 | 48.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09445633739233017 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 227 | MOVE_BENCH | WINSTREAK | 62.0 | 8 | 2 | 0 | 50.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6093514561653137 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 228 | PASS | WINSTREAK | 62.0 | 8 | 2 | 0 | 44.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 231 | BUY | ECON | 49.0 | 8 | 7 | 0 | 44.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6718963980674744 | 0.0 | 0.0 | +c65dacb1-5745-49d1-b7d4-e45d8e24aa84 / -— |
| Jogador 6 | 4-6 | 232 | BUY | ECON | 49.0 | 8 | 3 | 0 | 44.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.673874020576477 | 0.0 | 0.0 | +50edcbf1-13cd-4f98-bf35-d5a474fbe20c / -— |
| Jogador 6 | 4-6 | 233 | MOVE_BENCH | ECON | 49.0 | 8 | 0 | 0 | 44.0 | Defendente/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.023832034319639206 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 234 | SELL | ECON | 49.0 | 8 | 0 | 0 | 46.0 | Defendente/DA_18_GnarSmall | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.058800000697374344 | 0.0 | 0.0 | +— / -b755a0c5-f515-4f95-8f58-1e05f40ad302 |
| Jogador 6 | 4-6 | 235 | SELL | ECON | 49.0 | 8 | 3 | 0 | 46.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3735212981700897 | 0.0 | 0.0 | +— / -50edcbf1-13cd-4f98-bf35-d5a474fbe20c |
| Jogador 6 | 4-6 | 236 | BUY_XP | ECON | 49.0 | 8 | 6 | 0 | 46.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 237 | SELL | ECON | 49.0 | 8 | 2 | 0 | 46.0 | Defendente/DA_18_GnarSmall | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11073846369981766 | 0.0 | 0.0 | +— / -891aea62-e06a-46d4-8250-a3d4a56e847d |
| Jogador 6 | 4-6 | 238 | BUY_XP | ECON | 49.0 | 8 | 7 | 0 | 46.0 | Defendente/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 239 | MOVE_BOARD | ECON | 49.0 | 8 | 3 | 0 | 46.0 | Defendente/DA_18_Lillia | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.1515425443649292 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 241 | BUY | STABILIZE | 37.0 | 8 | 9 | 0 | 46.0 | Defendente/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.21005934476852417 | 0.0 | 0.0 | +6722b147-c2a7-4fd0-a943-5036adb3e3a1 / -— |
| Jogador 6 | 4-7 | 242 | BUY | STABILIZE | 37.0 | 8 | 5 | 0 | 46.0 | Defendente/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11297047138214111 | 0.0 | 0.0 | +04520fe5-4449-4632-b275-e5e28d642007 / -— |
| Jogador 6 | 4-7 | 243 | MOVE_BENCH | STABILIZE | 37.0 | 8 | 1 | 0 | 46.0 | Defendente/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05298830568790436 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 244 | MOVE_BENCH | STABILIZE | 37.0 | 8 | 1 | 0 | 46.0 | Defendente/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 245 | PASS | STABILIZE | 37.0 | 8 | 1 | 0 | 46.0 | Defendente/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 251 | EQUIP_FROM_INVENTORY | STABILIZE | 37.0 | 8 | 7 | 0 | 46.0 | Defendente/DA_18_Lillia | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 252 | BUY | STABILIZE | 37.0 | 8 | 7 | 0 | 46.0 | Defendente/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8319640755653381 | 0.0 | 0.0 | +d381c462-a17f-4192-b694-66a7c3aaee4f / -c65dacb1-5745-49d1-b7d4-e45d8e24aa84,d056a271-6a74-4e71-bde6-087b97d2c527 |
| Jogador 6 | 5-1 | 253 | BUY | STABILIZE | 37.0 | 8 | 3 | 0 | 38.0 | Defendente/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.743853747844696 | 0.0 | 0.0 | +b0c8ce74-5ce1-4ed0-82ac-f95013475f3c / -— |
| Jogador 6 | 5-1 | 254 | CRAFT_AND_EQUIP | STABILIZE | 37.0 | 8 | 0 | 0 | 38.0 | Defendente/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.12616731226444244 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 255 | MOVE_BENCH | STABILIZE | 37.0 | 8 | 0 | 0 | 38.0 | Defendente/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1394863724708557 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 256 | MOVE_BENCH | STABILIZE | 37.0 | 8 | 0 | 0 | 36.0 | Defendente/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4987102150917053 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 257 | SELL | STABILIZE | 37.0 | 8 | 0 | 0 | 44.0 | Defendente/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.041046153753995895 | 0.0 | 0.0 | +— / -04520fe5-4449-4632-b275-e5e28d642007 |
| Jogador 6 | 5-1 | 258 | BUY_XP | STABILIZE | 37.0 | 8 | 4 | 0 | 44.0 | Defendente/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 259 | SELL | STABILIZE | 37.0 | 8 | 0 | 0 | 44.0 | Defendente/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06461430341005325 | 0.0 | 0.0 | +— / -d381c462-a17f-4192-b694-66a7c3aaee4f |
| Jogador 6 | 5-2 | 261 | BUY | STABILIZE | 22.0 | 8 | 18 | 1 | 44.0 | Defendente/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8339725732803345 | 0.0 | 0.0 | +45ae38c5-7e69-41bb-9a93-f14db3af3587 / -333cdd27-0114-4d36-8ffa-e79b0f43b8e8,b0c8ce74-5ce1-4ed0-82ac-f95013475f3c |
| Jogador 6 | 5-2 | 262 | BUY | STABILIZE | 22.0 | 8 | 15 | 1 | 32.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19503304362297058 | 0.0 | 0.0 | +79b461e3-2c4f-40a2-b967-e0b6d5248bf6 / -— |
| Jogador 6 | 5-2 | 263 | MOVE_BENCH | STABILIZE | 22.0 | 8 | 11 | 1 | 32.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6203650236129761 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 264 | MOVE_BENCH | STABILIZE | 22.0 | 8 | 11 | 1 | 44.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.73467618227005 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 265 | MOVE_BENCH | STABILIZE | 22.0 | 8 | 11 | 1 | 40.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26475656032562256 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 266 | MOVE_BENCH | STABILIZE | 22.0 | 8 | 11 | 1 | 44.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10609448701143265 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 267 | MOVE_BENCH | STABILIZE | 22.0 | 8 | 11 | 1 | 44.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.711767852306366 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 268 | PASS | STABILIZE | 22.0 | 8 | 11 | 1 | 40.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 269 | MOVE_BENCH | STABILIZE | 22.0 | 8 | 11 | 1 | 40.0 | Defendente/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8748008012771606 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 271 | BUY | ALL_IN | 6.0 | 8 | 18 | 1 | 52.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2684074938297272 | 0.0 | 0.0 | +45b96060-6eda-4d0b-9012-e80db31b71d2 / -— |
| Jogador 6 | 5-3 | 272 | BUY | ALL_IN | 6.0 | 8 | 15 | 1 | 52.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05381397530436516 | 0.0 | 0.0 | +b6883c6a-7149-4088-8506-20bd8dfed6a5 / -— |
| Jogador 6 | 5-3 | 273 | MOVE_BENCH | ALL_IN | 6.0 | 8 | 11 | 1 | 52.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014435065910220146 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 274 | MOVE_BENCH | ALL_IN | 6.0 | 8 | 11 | 1 | 50.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06003810465335846 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 275 | MOVE_BENCH | ALL_IN | 6.0 | 8 | 11 | 1 | 50.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35799461603164673 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 276 | MOVE_BENCH | ALL_IN | 6.0 | 8 | 11 | 1 | 52.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34625667333602905 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 277 | PASS | ALL_IN | 6.0 | 8 | 11 | 1 | 50.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 281 | BUY | ALL_IN | 6.0 | 8 | 18 | 1 | 50.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7280434370040894 | 0.0 | 0.0 | +1512b230-15a6-405f-9b6b-4387a3091648 / -— |
| Jogador 6 | 5-4 | 282 | MOVE_BENCH | ALL_IN | 6.0 | 8 | 14 | 1 | 50.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060127656906843185 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 283 | MOVE_BENCH | ALL_IN | 6.0 | 8 | 14 | 1 | 50.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3581240177154541 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 284 | BUY_XP | ALL_IN | 6.0 | 8 | 14 | 1 | 52.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 285 | BUY_XP | ALL_IN | 6.0 | 8 | 10 | 1 | 52.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 286 | BUY_XP | ALL_IN | 6.0 | 8 | 6 | 0 | 52.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 287 | MOVE_BENCH | ALL_IN | 6.0 | 8 | 2 | 0 | 52.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01177576370537281 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 288 | MOVE_BENCH | ALL_IN | 6.0 | 8 | 2 | 0 | 50.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06033474579453468 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 289 | MOVE_BENCH | ALL_IN | 6.0 | 8 | 2 | 0 | 50.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35789182782173157 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 291 | MOVE_BENCH | ALL_IN | 6.0 | 8 | 8 | 0 | 52.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6682426929473877 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 292 | BUY | ALL_IN | 6.0 | 8 | 8 | 0 | 46.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8250992298126221 | 0.0 | 0.0 | +8da82a9e-0746-43e1-81c3-fa22ec3bb863 / -4d0bf502-ac30-4cdb-9da7-4f9a7ab054b1,61362365-2cf7-40e4-95f9-98e28728fd39 |
| Jogador 6 | 5-5 | 293 | MOVE_BENCH | ALL_IN | 6.0 | 8 | 6 | 0 | 38.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35494840145111084 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 294 | MOVE_BENCH | ALL_IN | 6.0 | 8 | 6 | 0 | 42.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19481144845485687 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 295 | MOVE_BENCH | ALL_IN | 6.0 | 8 | 6 | 0 | 38.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2928633391857147 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 296 | BUY_XP | ALL_IN | 6.0 | 8 | 6 | 0 | 44.0 | Carrasco/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 297 | MOVE_BENCH | ALL_IN | 6.0 | 8 | 2 | 0 | 44.0 | Carrasco/DA_Fiddlesticks18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18243762850761414 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 298 | MOVE_BENCH | ALL_IN | 6.0 | 8 | 2 | 0 | 42.0 | Carrasco/DA_Fiddlesticks18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1990596204996109 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 299 | MOVE_BENCH | ALL_IN | 6.0 | 8 | 2 | 0 | 38.0 | Carrasco/DA_Fiddlesticks18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3114962875843048 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 301 | PASS | ALL_IN | 0.0 | 8 | 2 | 0 | 0.0 | Carrasco/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 311 | PASS | ALL_IN | 0.0 | 8 | 2 | 0 | 0.0 | Carrasco/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 321 | PASS | ALL_IN | 0.0 | 8 | 2 | 0 | 0.0 | Carrasco/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 331 | PASS | ALL_IN | 0.0 | 8 | 2 | 0 | 0.0 | Carrasco/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 9 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.28737619519233704 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.32177162170410156 | 0.0 | 0.0 | +47ec6577-cbf2-4275-b185-c19256223441 / -— |
| Jogador 7 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2104591727256775 | 0.0 | 0.0 | +4e206e09-40e3-4699-81cb-8aaf01109dea / -— |
| Jogador 7 | 1-2 | 13 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3348696231842041 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9858362674713135 | 0.0 | 0.0 | +96fb1ff5-06a8-439b-af2b-8700d7be8524 / -— |
| Jogador 7 | 1-3 | 22 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5808652639389038 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 31 | BUY_XP | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44449999928474426 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 32 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09999348968267441 | 0.0 | 0.0 | +— / -4e206e09-40e3-4699-81cb-8aaf01109dea |
| Jogador 7 | 1-4 | 33 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.21127668023109436 | 0.0 | 0.0 | +bb7ed7a4-035a-4798-a9b2-44893057ab84 / -— |
| Jogador 7 | 1-4 | 34 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 39 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42070528864860535 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3282388150691986 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 7 | 2-1 | 42 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022445622831583023 | 0.0 | 0.0 | +42f4384d-5499-4441-aa3b-d37e50926071 / -— |
| Jogador 7 | 2-1 | 43 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37823882699012756 | 0.0 | 0.0 | +— / -5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef |
| Jogador 7 | 2-1 | 44 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2648000121116638 | 0.0 | 0.0 | +— / -42f4384d-5499-4441-aa3b-d37e50926071 |
| Jogador 7 | 2-1 | 45 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 46 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 51 | BUY | STABILIZE | 100.0 | 5 | 6 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.019931601360440254 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 52 | BUY | STABILIZE | 100.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1179389953613281 | 0.0 | 0.0 | +0d8b39fc-eb5c-4679-b615-50cdfdcf3eee / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987,96fb1ff5-06a8-439b-af2b-8700d7be8524 |
| Jogador 7 | 2-2 | 53 | BUY | STABILIZE | 100.0 | 5 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030369509011507034 | 0.0 | 0.0 | +5db33b7c-1844-4f4f-8317-ac08f66d4c1e / -— |
| Jogador 7 | 2-2 | 54 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07333943992853165 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 55 | PASS | STABILIZE | 100.0 | 5 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4996865391731262 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 61 | BUY | STABILIZE | 94.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07957803457975388 | 0.0 | 0.0 | +3ffefe44-52ff-4118-83fb-ae8237b6caa0 / -— |
| Jogador 7 | 2-3 | 62 | BUY | STABILIZE | 94.0 | 5 | 2 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4236757755279541 | 0.0 | 0.0 | +3394d5fc-ee48-4a08-8669-05984c804b53 / -— |
| Jogador 7 | 2-3 | 63 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.217524453997612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 64 | PASS | STABILIZE | 94.0 | 5 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 69 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 0 | 0 | 12.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5572443008422852 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 71 | BUY | STABILIZE | 90.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2668112814426422 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 72 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 2 | 0 | 18.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6116878390312195 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 73 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 2 | 0 | 22.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.048057883977890015 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 74 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 2 | 0 | 16.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44232362508773804 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 75 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 2 | 0 | 22.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2136242538690567 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 76 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 2 | 0 | 18.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14308986067771912 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 77 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 2 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24431826174259186 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 78 | PASS | STABILIZE | 90.0 | 5 | 2 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 81 | BUY | STABILIZE | 90.0 | 5 | 8 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3711996078491211 | 0.0 | 0.0 | +599caeca-96ef-4308-b6cd-f65b005879e2 / -— |
| Jogador 7 | 2-5 | 82 | BUY_XP | STABILIZE | 90.0 | 5 | 5 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 83 | SELL | STABILIZE | 90.0 | 5 | 1 | 0 | 24.0 | —/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025772275403141975 | 0.0 | 0.0 | +— / -bb7ed7a4-035a-4798-a9b2-44893057ab84 |
| Jogador 7 | 2-5 | 84 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 2 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2081271857023239 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 85 | BUY | STABILIZE | 90.0 | 5 | 2 | 0 | 26.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43048742413520813 | 0.0 | 0.0 | +caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e / -— |
| Jogador 7 | 2-5 | 86 | SELL | STABILIZE | 90.0 | 5 | 1 | 0 | 26.0 | —/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.022569794207811356 | 0.0 | 0.0 | +— / -caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e |
| Jogador 7 | 2-5 | 87 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 2 | 0 | 26.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2245408147573471 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 88 | SELL | STABILIZE | 90.0 | 5 | 2 | 0 | 22.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04076923057436943 | 0.0 | 0.0 | +— / -5db33b7c-1844-4f4f-8317-ac08f66d4c1e |
| Jogador 7 | 2-5 | 89 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 3 | 0 | 22.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4257097542285919 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 91 | BUY | STABILIZE | 90.0 | 5 | 9 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4466319978237152 | 0.0 | 0.0 | +6c691ca5-c042-46de-8d64-493514f2d793 / -— |
| Jogador 7 | 2-6 | 92 | BUY_XP | STABILIZE | 90.0 | 5 | 6 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 93 | SELL | STABILIZE | 90.0 | 5 | 2 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02961769513785839 | 0.0 | 0.0 | +— / -599caeca-96ef-4308-b6cd-f65b005879e2 |
| Jogador 7 | 2-6 | 94 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 5 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15765945613384247 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 95 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 5 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05511276796460152 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 96 | BUY | STABILIZE | 90.0 | 5 | 5 | 0 | 22.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9433621764183044 | 0.0 | 0.0 | +a146f2d5-4da5-4c0e-bb09-de3177c72417 / -— |
| Jogador 7 | 2-6 | 97 | SELL | STABILIZE | 90.0 | 5 | 3 | 0 | 22.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18976476788520813 | 0.0 | 0.0 | +— / -a146f2d5-4da5-4c0e-bb09-de3177c72417 |
| Jogador 7 | 2-6 | 98 | BUY_XP | STABILIZE | 90.0 | 5 | 5 | 0 | 22.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3269999921321869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 99 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 1 | 0 | 22.0 | —/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36193525791168213 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 101 | BUY | STABILIZE | 90.0 | 6 | 8 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2955511510372162 | 0.0 | 0.0 | +584991bb-37b3-4ac1-8e29-14e0d74c5e78 / -— |
| Jogador 7 | 2-7 | 102 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 5 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10041967779397964 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 103 | BUY_XP | STABILIZE | 90.0 | 6 | 5 | 0 | 32.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 104 | SELL | STABILIZE | 90.0 | 6 | 1 | 0 | 32.0 | —/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005191342905163765 | 0.0 | 0.0 | +— / -6c691ca5-c042-46de-8d64-493514f2d793 |
| Jogador 7 | 2-7 | 105 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 4 | 0 | 32.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4401976764202118 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 106 | BUY | STABILIZE | 90.0 | 6 | 4 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31986120343208313 | 0.0 | 0.0 | +ac02c0c4-a10d-497d-b6c1-d458ad7ae58c / -— |
| Jogador 7 | 2-7 | 107 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 2 | 0 | 30.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05900115892291069 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 108 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 2 | 0 | 28.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3073887526988983 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 109 | PASS | STABILIZE | 90.0 | 6 | 2 | 0 | 26.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 111 | BUY | STABILIZE | 90.0 | 6 | 8 | 0 | 26.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2769327759742737 | 0.0 | 0.0 | +ad1693cd-1ab5-43a9-8164-25929b8bd68e / -— |
| Jogador 7 | 3-1 | 112 | BUY_XP | STABILIZE | 90.0 | 6 | 5 | 0 | 26.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 113 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 1 | 0 | 26.0 | Inferno/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 114 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 1 | 0 | 26.0 | Inferno/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13479605317115784 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 115 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 1 | 0 | 26.0 | Inferno/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006237977184355259 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 116 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 1 | 0 | 26.0 | Inferno/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09447509795427322 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 117 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 1 | 0 | 28.0 | Inferno/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10420360416173935 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 118 | SELL | STABILIZE | 90.0 | 6 | 1 | 0 | 28.0 | Inferno/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05052334442734718 | 0.0 | 0.0 | +— / -584991bb-37b3-4ac1-8e29-14e0d74c5e78 |
| Jogador 7 | 3-1 | 119 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 4 | 0 | 28.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026153486222028732 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 121 | BUY | STABILIZE | 81.0 | 6 | 9 | 0 | 30.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7286807894706726 | 0.0 | 0.0 | +fa331d8d-1e0c-49b4-848e-8ad58859331c / -— |
| Jogador 7 | 3-2 | 122 | BUY | STABILIZE | 81.0 | 6 | 7 | 0 | 30.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8288125395774841 | 0.0 | 0.0 | +96bf8f0a-9fe1-4182-95dc-903c1e623983 / -ac02c0c4-a10d-497d-b6c1-d458ad7ae58c,fa331d8d-1e0c-49b4-848e-8ad58859331c |
| Jogador 7 | 3-2 | 123 | BUY_XP | STABILIZE | 81.0 | 6 | 5 | 0 | 26.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 124 | SELL | STABILIZE | 81.0 | 6 | 1 | 0 | 26.0 | Inferno/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1403251737356186 | 0.0 | 0.0 | +— / -96bf8f0a-9fe1-4182-95dc-903c1e623983 |
| Jogador 7 | 3-2 | 125 | BUY | STABILIZE | 81.0 | 6 | 6 | 0 | 26.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06392357498407364 | 0.0 | 0.0 | +daa7f698-2fa2-43d7-ae73-ec616b006db4 / -— |
| Jogador 7 | 3-2 | 126 | SELL | STABILIZE | 81.0 | 6 | 3 | 0 | 26.0 | Inferno/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1444147229194641 | 0.0 | 0.0 | +— / -3394d5fc-ee48-4a08-8669-05984c804b53 |
| Jogador 7 | 3-2 | 127 | BUY_XP | STABILIZE | 81.0 | 6 | 5 | 0 | 26.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 128 | SELL | STABILIZE | 81.0 | 6 | 1 | 0 | 26.0 | Inferno/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11941510438919067 | 0.0 | 0.0 | +— / -daa7f698-2fa2-43d7-ae73-ec616b006db4 |
| Jogador 7 | 3-2 | 129 | MOVE_BENCH | STABILIZE | 81.0 | 6 | 4 | 0 | 26.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6098509430885315 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 131 | BUY | STABILIZE | 81.0 | 6 | 10 | 1 | 34.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6617006659507751 | 0.0 | 0.0 | +f116ca4e-dbe8-457e-83a5-958525aa384a / -— |
| Jogador 7 | 3-3 | 132 | MOVE_BENCH | STABILIZE | 81.0 | 6 | 7 | 0 | 34.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006654964294284582 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 133 | BUY | STABILIZE | 81.0 | 6 | 7 | 0 | 32.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006242046132683754 | 0.0 | 0.0 | +4d03897d-0113-4a29-a864-75305c142d97 / -— |
| Jogador 7 | 3-3 | 134 | BUY_XP | STABILIZE | 81.0 | 6 | 5 | 0 | 32.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 135 | SELL | STABILIZE | 81.0 | 6 | 1 | 0 | 32.0 | Inferno/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28371864557266235 | 0.0 | 0.0 | +— / -4d03897d-0113-4a29-a864-75305c142d97 |
| Jogador 7 | 3-3 | 136 | SELL | STABILIZE | 81.0 | 6 | 3 | 0 | 32.0 | Inferno/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11181538552045822 | 0.0 | 0.0 | +— / -fb7c0635-9f86-4c1e-b354-37372f84d656 |
| Jogador 7 | 3-3 | 137 | BUY_XP | STABILIZE | 81.0 | 6 | 7 | 0 | 32.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 138 | MOVE_BOARD | STABILIZE | 81.0 | 6 | 3 | 0 | 32.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1721227467060089 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 139 | MOVE_BOARD | STABILIZE | 81.0 | 6 | 3 | 0 | 32.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.332162469625473 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 141 | BUY | STABILIZE | 71.0 | 6 | 8 | 0 | 32.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.28104037046432495 | 0.0 | 0.0 | +cfe17b3a-c9b6-4e09-9ba1-23e762a72569 / -— |
| Jogador 7 | 3-4 | 142 | MOVE_BENCH | STABILIZE | 71.0 | 6 | 5 | 0 | 32.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09207834303379059 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 143 | BUY | STABILIZE | 71.0 | 6 | 5 | 0 | 32.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10509537905454636 | 0.0 | 0.0 | +86c1ac55-598e-426a-86ea-64249f82b085 / -— |
| Jogador 7 | 3-4 | 144 | SELL | STABILIZE | 71.0 | 6 | 2 | 0 | 32.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15509538352489471 | 0.0 | 0.0 | +— / -86c1ac55-598e-426a-86ea-64249f82b085 |
| Jogador 7 | 3-4 | 145 | MOVE_BENCH | STABILIZE | 71.0 | 6 | 5 | 0 | 32.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23342181742191315 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 146 | BUY_XP | STABILIZE | 71.0 | 6 | 5 | 0 | 30.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4320000112056732 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 147 | MOVE_BENCH | STABILIZE | 71.0 | 7 | 1 | 0 | 30.0 | Inferno/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5507880449295044 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 148 | MOVE_BENCH | STABILIZE | 71.0 | 7 | 1 | 0 | 32.0 | Inferno/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5384351015090942 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 149 | MOVE_BOARD | STABILIZE | 71.0 | 7 | 1 | 0 | 38.0 | Inferno/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 151 | BUY | STABILIZE | 71.0 | 7 | 6 | 0 | 38.0 | Inferno/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8338422179222107 | 0.0 | 0.0 | +f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e / -ad1693cd-1ab5-43a9-8164-25929b8bd68e,f116ca4e-dbe8-457e-83a5-958525aa384a |
| Jogador 7 | 3-5 | 152 | BUY | STABILIZE | 71.0 | 7 | 3 | 0 | 26.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06221163645386696 | 0.0 | 0.0 | +2074e6ec-81e7-41c9-be7e-a0d9310fbafa / -— |
| Jogador 7 | 3-5 | 153 | MOVE_BENCH | STABILIZE | 71.0 | 7 | 0 | 0 | 26.0 | Inferno/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.365779310464859 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 154 | MOVE_BENCH | STABILIZE | 71.0 | 7 | 0 | 0 | 30.0 | Inferno/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45031800866127014 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 155 | SELL | STABILIZE | 71.0 | 7 | 0 | 0 | 36.0 | Inferno/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1294461488723755 | 0.0 | 0.0 | +— / -47ec6577-cbf2-4275-b185-c19256223441 |
| Jogador 7 | 3-5 | 156 | SELL | STABILIZE | 71.0 | 7 | 1 | 0 | 36.0 | Inferno/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11898461729288101 | 0.0 | 0.0 | +— / -2074e6ec-81e7-41c9-be7e-a0d9310fbafa |
| Jogador 7 | 3-5 | 157 | BUY | STABILIZE | 71.0 | 7 | 4 | 0 | 36.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.0761650800704956 | 0.0 | 0.0 | +7c8b3027-1434-4346-95b3-5463e8a4aa9b / -— |
| Jogador 7 | 3-5 | 158 | MOVE_BENCH | STABILIZE | 71.0 | 7 | 2 | 0 | 36.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5800033211708069 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 159 | MOVE_BENCH | STABILIZE | 71.0 | 7 | 2 | 0 | 28.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4652564823627472 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 161 | BUY | STABILIZE | 58.0 | 7 | 8 | 0 | 40.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7274379134178162 | 0.0 | 0.0 | +d69fa0dc-74b6-4ee7-90f7-aaca5405c59c / -— |
| Jogador 7 | 3-6 | 162 | BUY | STABILIZE | 58.0 | 7 | 4 | 0 | 40.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03769470751285553 | 0.0 | 0.0 | +6caec849-54f8-4ec1-90a4-fc0587510013 / -— |
| Jogador 7 | 3-6 | 163 | MOVE_BENCH | STABILIZE | 58.0 | 7 | 0 | 0 | 40.0 | Inferno/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 164 | MOVE_BENCH | STABILIZE | 58.0 | 7 | 0 | 0 | 40.0 | Inferno/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11085309833288193 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 165 | PASS | STABILIZE | 58.0 | 7 | 0 | 0 | 44.0 | Inferno/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 169 | MOVE_BENCH | STABILIZE | 58.0 | 7 | 0 | 0 | 44.0 | Inferno/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6491402387619019 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 171 | BUY | STABILIZE | 48.0 | 7 | 6 | 0 | 48.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2768630087375641 | 0.0 | 0.0 | +8a52858d-da47-4de9-8e91-8612788cb8fd / -— |
| Jogador 7 | 3-7 | 172 | BUY | STABILIZE | 48.0 | 7 | 2 | 0 | 48.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2761008143424988 | 0.0 | 0.0 | +1cba4955-961e-4efd-a291-e0a70bf72841 / -— |
| Jogador 7 | 3-7 | 173 | MOVE_BENCH | STABILIZE | 48.0 | 7 | 0 | 0 | 48.0 | Inferno/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09585545212030411 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 174 | SELL | STABILIZE | 48.0 | 7 | 0 | 0 | 48.0 | Inferno/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11220154166221619 | 0.0 | 0.0 | +— / -1cba4955-961e-4efd-a291-e0a70bf72841 |
| Jogador 7 | 3-7 | 175 | MOVE_BENCH | STABILIZE | 48.0 | 7 | 2 | 0 | 48.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 176 | MOVE_BENCH | STABILIZE | 48.0 | 7 | 2 | 0 | 48.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1020832508802414 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 177 | PASS | STABILIZE | 48.0 | 7 | 2 | 0 | 48.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 181 | BUY | STABILIZE | 48.0 | 7 | 8 | 0 | 48.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13396263122558594 | 0.0 | 0.0 | +97d52b06-365b-44ad-b4f9-63e0f9503c8a / -— |
| Jogador 7 | 4-1 | 182 | MOVE_BENCH | STABILIZE | 48.0 | 7 | 5 | 0 | 48.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15695808827877045 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 183 | BUY_XP | STABILIZE | 48.0 | 7 | 5 | 0 | 48.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 184 | SELL | STABILIZE | 48.0 | 7 | 1 | 0 | 48.0 | Inferno/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1839626282453537 | 0.0 | 0.0 | +— / -97d52b06-365b-44ad-b4f9-63e0f9503c8a |
| Jogador 7 | 4-1 | 185 | MOVE_BENCH | STABILIZE | 48.0 | 7 | 4 | 0 | 48.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 186 | MOVE_BENCH | STABILIZE | 48.0 | 7 | 4 | 0 | 48.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15237198770046234 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 187 | PASS | STABILIZE | 48.0 | 7 | 4 | 0 | 52.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 191 | BUY | STABILIZE | 48.0 | 7 | 10 | 1 | 52.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18438807129859924 | 0.0 | 0.0 | +0803068a-0141-4e75-ab81-12bb13986025 / -— |
| Jogador 7 | 4-2 | 192 | BUY_XP | STABILIZE | 48.0 | 7 | 7 | 0 | 52.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 193 | SELL | STABILIZE | 48.0 | 7 | 3 | 0 | 52.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0432199127972126 | 0.0 | 0.0 | +— / -7c8b3027-1434-4346-95b3-5463e8a4aa9b |
| Jogador 7 | 4-2 | 194 | BUY_XP | STABILIZE | 48.0 | 7 | 5 | 0 | 52.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 195 | SELL | STABILIZE | 48.0 | 7 | 1 | 0 | 52.0 | Inferno/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10070769488811493 | 0.0 | 0.0 | +— / -0803068a-0141-4e75-ab81-12bb13986025 |
| Jogador 7 | 4-2 | 196 | BUY_XP | STABILIZE | 48.0 | 7 | 4 | 0 | 52.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 197 | SELL | STABILIZE | 48.0 | 7 | 0 | 0 | 52.0 | Inferno/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.042929425835609436 | 0.0 | 0.0 | +— / -6caec849-54f8-4ec1-90a4-fc0587510013 |
| Jogador 7 | 4-2 | 198 | BUY_XP | STABILIZE | 48.0 | 7 | 4 | 0 | 52.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 199 | MOVE_BOARD | STABILIZE | 48.0 | 7 | 0 | 0 | 52.0 | Inferno/DA_Fiddlesticks18 | MOVE_BOARD, PASS | True | True | 0.0832260251045227 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 201 | BUY | STABILIZE | 35.0 | 7 | 5 | 0 | 52.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.15514487028121948 | 0.0 | 0.0 | +80c51b33-0a85-4f21-a797-9551aa10760f / -— |
| Jogador 7 | 4-3 | 202 | MOVE_BENCH | STABILIZE | 35.0 | 7 | 1 | 0 | 52.0 | Inferno/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05251992866396904 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 203 | SELL | STABILIZE | 35.0 | 7 | 1 | 0 | 52.0 | Inferno/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16267995536327362 | 0.0 | 0.0 | +— / -0cf5c315-d2f3-4854-a95b-07912b83ea81 |
| Jogador 7 | 4-3 | 204 | BUY_XP | STABILIZE | 35.0 | 7 | 5 | 0 | 52.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 205 | MOVE_BOARD | STABILIZE | 35.0 | 7 | 1 | 0 | 52.0 | Inferno/DA_Fiddlesticks18 | MOVE_BOARD, PASS | True | True | -0.19681254029273987 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 206 | MOVE_BOARD | STABILIZE | 35.0 | 7 | 1 | 0 | 52.0 | Inferno/DA_Fiddlesticks18 | MOVE_BOARD, PASS | True | True | -0.2502897381782532 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 207 | PASS | STABILIZE | 35.0 | 7 | 1 | 0 | 52.0 | Inferno/DA_Fiddlesticks18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 211 | BUY | STABILIZE | 23.0 | 7 | 7 | 0 | 52.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.28379058837890625 | 0.0 | 0.0 | +17170204-1921-4cf1-b92b-cc73bb0701ea / -— |
| Jogador 7 | 4-4 | 212 | MOVE_BENCH | STABILIZE | 23.0 | 7 | 4 | 0 | 52.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06276058405637741 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 213 | MOVE_BENCH | STABILIZE | 23.0 | 7 | 4 | 0 | 50.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007650860585272312 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 214 | BUY | STABILIZE | 23.0 | 7 | 4 | 0 | 50.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04204319417476654 | 0.0 | 0.0 | +bb51728e-fcc5-4950-ad03-c864c51c2371 / -— |
| Jogador 7 | 4-4 | 215 | SELL | STABILIZE | 23.0 | 7 | 1 | 0 | 50.0 | Inferno/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12895384430885315 | 0.0 | 0.0 | +— / -bb51728e-fcc5-4950-ad03-c864c51c2371 |
| Jogador 7 | 4-4 | 216 | MOVE_BENCH | STABILIZE | 23.0 | 7 | 4 | 0 | 50.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01593203656375408 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 217 | BUY_XP | STABILIZE | 23.0 | 7 | 4 | 0 | 52.0 | Inferno/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 218 | SELL | STABILIZE | 23.0 | 7 | 0 | 0 | 52.0 | Inferno/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15304531157016754 | 0.0 | 0.0 | +— / -17170204-1921-4cf1-b92b-cc73bb0701ea |
| Jogador 7 | 4-4 | 219 | MOVE_BOARD | STABILIZE | 23.0 | 7 | 3 | 0 | 52.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.26141127943992615 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 221 | BUY | STABILIZE | 23.0 | 7 | 9 | 0 | 52.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.726523756980896 | 0.0 | 0.0 | +bc0aa086-b5e5-4809-833f-193c5c0da181 / -— |
| Jogador 7 | 4-5 | 222 | BUY | STABILIZE | 23.0 | 7 | 5 | 0 | 52.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7317430973052979 | 0.0 | 0.0 | +b82f90f3-6914-4db5-bc7c-74543cf91aef / -— |
| Jogador 7 | 4-5 | 223 | SELL | STABILIZE | 23.0 | 7 | 2 | 0 | 52.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3268386423587799 | 0.0 | 0.0 | +— / -b82f90f3-6914-4db5-bc7c-74543cf91aef |
| Jogador 7 | 4-5 | 224 | BUY_XP | STABILIZE | 23.0 | 7 | 5 | 0 | 52.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 225 | SELL | STABILIZE | 23.0 | 7 | 1 | 0 | 52.0 | Flora Fatalis/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33500412106513977 | 0.0 | 0.0 | +— / -bc0aa086-b5e5-4809-833f-193c5c0da181 |
| Jogador 7 | 4-5 | 226 | BUY_XP | STABILIZE | 23.0 | 7 | 5 | 0 | 52.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 227 | MOVE_BOARD | STABILIZE | 23.0 | 7 | 1 | 0 | 52.0 | Flora Fatalis/DA_Fiddlesticks18 | MOVE_BOARD, PASS | True | True | -0.3007032871246338 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 228 | MOVE_BOARD | STABILIZE | 23.0 | 7 | 1 | 0 | 52.0 | Flora Fatalis/DA_Fiddlesticks18 | MOVE_BOARD, PASS | True | True | 0.09566855430603027 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 229 | MOVE_BOARD | STABILIZE | 23.0 | 7 | 1 | 0 | 52.0 | Flora Fatalis/DA_Fiddlesticks18 | MOVE_BOARD, PASS | True | True | 0.14408981800079346 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 231 | BUY | STABILIZE | 23.0 | 8 | 7 | 0 | 52.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.013482467271387577 | 0.0 | 0.0 | +023f01af-91d0-4e07-8229-2b7cded83151 / -— |
| Jogador 7 | 4-6 | 232 | BUY | STABILIZE | 23.0 | 8 | 3 | 0 | 52.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25519245862960815 | 0.0 | 0.0 | +ec9662c5-0734-41a3-9999-224d7716228b / -— |
| Jogador 7 | 4-6 | 233 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 1 | 0 | 52.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.053688183426856995 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 234 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 1 | 0 | 52.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6089675426483154 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 235 | SELL | STABILIZE | 23.0 | 8 | 1 | 0 | 60.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10002510249614716 | 0.0 | 0.0 | +— / -ec9662c5-0734-41a3-9999-224d7716228b |
| Jogador 7 | 4-6 | 236 | MOVE_BOARD | STABILIZE | 23.0 | 8 | 3 | 0 | 60.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 237 | MOVE_BOARD | STABILIZE | 23.0 | 8 | 3 | 0 | 60.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.16915513575077057 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 238 | MOVE_BOARD | STABILIZE | 23.0 | 8 | 3 | 0 | 60.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 239 | MOVE_BOARD | STABILIZE | 23.0 | 8 | 3 | 0 | 60.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.3023725748062134 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 241 | BUY | STABILIZE | 23.0 | 8 | 8 | 0 | 60.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7293643951416016 | 0.0 | 0.0 | +d80c845d-24bc-4053-a60d-5d0122839b0c / -— |
| Jogador 7 | 4-7 | 242 | BUY | STABILIZE | 23.0 | 8 | 4 | 0 | 60.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6755377054214478 | 0.0 | 0.0 | +362f7357-283e-4f88-bff3-ffa6314af821 / -— |
| Jogador 7 | 4-7 | 243 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 1 | 0 | 60.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08031228929758072 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 244 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 1 | 0 | 60.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5081339478492737 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 245 | SELL | STABILIZE | 23.0 | 8 | 1 | 0 | 56.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e |
| Jogador 7 | 4-7 | 246 | BUY_XP | STABILIZE | 23.0 | 8 | 9 | 0 | 56.0 | Flora Fatalis/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 247 | BUY_XP | STABILIZE | 23.0 | 8 | 5 | 0 | 56.0 | Flora Fatalis/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 248 | SELL | STABILIZE | 23.0 | 8 | 1 | 0 | 56.0 | Flora Fatalis/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30403077602386475 | 0.0 | 0.0 | +— / -362f7357-283e-4f88-bff3-ffa6314af821 |
| Jogador 7 | 4-7 | 249 | BUY_XP | STABILIZE | 23.0 | 8 | 4 | 0 | 56.0 | Flora Fatalis/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 251 | EQUIP_FROM_INVENTORY | STABILIZE | 23.0 | 8 | 5 | 0 | 56.0 | Flora Fatalis/DA_Sentinel18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 252 | CRAFT_AND_EQUIP | STABILIZE | 23.0 | 8 | 5 | 0 | 56.0 | Flora Fatalis/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | — | 0.216617614030838 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 253 | BUY | STABILIZE | 23.0 | 8 | 5 | 0 | 56.0 | Flora Fatalis/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10018034279346466 | 0.0 | 0.0 | +c7a7408a-e7bd-428d-9935-4d5a002d8d9f / -— |
| Jogador 7 | 5-1 | 254 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 0 | 0 | 56.0 | Flora Fatalis/DA_18_Ashe | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0536515936255455 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 255 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 0 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1593698412179947 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 256 | PASS | STABILIZE | 23.0 | 8 | 0 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 261 | BUY | STABILIZE | 23.0 | 8 | 7 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.022188426926732063 | 0.0 | 0.0 | +3658b5d8-450f-451a-8487-5b3bdd7c385b / -— |
| Jogador 7 | 5-2 | 262 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 3 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07296255975961685 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 263 | BUY | STABILIZE | 23.0 | 8 | 3 | 0 | 56.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0016311758663505316 | 0.0 | 0.0 | +4432f76a-94cc-4a96-b72b-1cf35b310dca / -— |
| Jogador 7 | 5-2 | 264 | SELL | STABILIZE | 23.0 | 8 | 0 | 0 | 56.0 | Flora Fatalis/DA_18_Ashe | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13227692246437073 | 0.0 | 0.0 | +— / -4432f76a-94cc-4a96-b72b-1cf35b310dca |
| Jogador 7 | 5-2 | 265 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 3 | 0 | 56.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05365157127380371 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 266 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 3 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08032690733671188 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 267 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 3 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16673418879508972 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 268 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 3 | 0 | 56.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05366550013422966 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 269 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 3 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 271 | BUY | STABILIZE | 23.0 | 8 | 10 | 1 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28152838349342346 | 0.0 | 0.0 | +8b8aaa92-8fe0-46ad-857e-af3bae9b26a4 / -— |
| Jogador 7 | 5-3 | 272 | BUY_XP | STABILIZE | 23.0 | 8 | 7 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 273 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 3 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05193467065691948 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 274 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 3 | 0 | 56.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18774783611297607 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 275 | MOVE_BENCH | STABILIZE | 23.0 | 8 | 3 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08035151660442352 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 276 | PASS | STABILIZE | 23.0 | 8 | 3 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 281 | BUY | ALL_IN | 7.0 | 8 | 8 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7321253418922424 | 0.0 | 0.0 | +95eba9e8-10f5-48d5-86de-3d9a446b2e65 / -— |
| Jogador 7 | 5-4 | 282 | BUY_XP | ALL_IN | 7.0 | 8 | 5 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 283 | SELL | ALL_IN | 7.0 | 8 | 1 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.058800000697374344 | 0.0 | 0.0 | +— / -8b8aaa92-8fe0-46ad-857e-af3bae9b26a4 |
| Jogador 7 | 5-4 | 284 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 4 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05191785842180252 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 285 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 4 | 0 | 56.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.051948923617601395 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 286 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 4 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05149807035923004 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 287 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 4 | 0 | 54.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05364829674363136 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 288 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 4 | 0 | 56.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00035217899130657315 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 289 | BUY_XP | ALL_IN | 7.0 | 8 | 4 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 291 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 5 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16673418879508972 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 292 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 5 | 0 | 56.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05365011468529701 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 293 | BUY_XP | ALL_IN | 7.0 | 8 | 5 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 294 | SELL | ALL_IN | 7.0 | 8 | 1 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32878971099853516 | 0.0 | 0.0 | +— / -95eba9e8-10f5-48d5-86de-3d9a446b2e65 |
| Jogador 7 | 5-5 | 295 | BUY | ALL_IN | 7.0 | 8 | 4 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2199908047914505 | 0.0 | 0.0 | +0b38218d-9c50-41ac-b761-115c054bf314 / -— |
| Jogador 7 | 5-5 | 296 | SELL | ALL_IN | 7.0 | 8 | 0 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.052861537784338 | 0.0 | 0.0 | +— / -3658b5d8-450f-451a-8487-5b3bdd7c385b |
| Jogador 7 | 5-5 | 297 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 4 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1593731939792633 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 298 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 4 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07296255975961685 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 299 | PASS | ALL_IN | 7.0 | 8 | 4 | 0 | 56.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 301 | BUY | ALL_IN | 7.0 | 8 | 10 | 1 | 56.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028295734897255898 | 0.0 | 0.0 | +551e9535-d584-4055-a544-ed78d65ecacb / -— |
| Jogador 7 | 5-6 | 302 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 6 | 0 | 56.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05366770178079605 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 303 | BUY_XP | ALL_IN | 7.0 | 8 | 6 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 304 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 2 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08032585680484772 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 305 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 2 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16673418879508972 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 306 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 2 | 0 | 56.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05366458743810654 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 307 | SELL | ALL_IN | 7.0 | 8 | 2 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1346844732761383 | 0.0 | 0.0 | +— / -551e9535-d584-4055-a544-ed78d65ecacb |
| Jogador 7 | 5-6 | 308 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 6 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 309 | BUY_XP | ALL_IN | 7.0 | 8 | 6 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 311 | BUY | ALL_IN | 7.0 | 8 | 9 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13424542546272278 | 0.0 | 0.0 | +1bf15a91-4832-4245-9b48-382a27410263 / -— |
| Jogador 7 | 5-7 | 312 | BUY_XP | ALL_IN | 7.0 | 8 | 5 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 313 | SELL | ALL_IN | 7.0 | 8 | 1 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18424542248249054 | 0.0 | 0.0 | +— / -1bf15a91-4832-4245-9b48-382a27410263 |
| Jogador 7 | 5-7 | 314 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 5 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05180538818240166 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 315 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 5 | 0 | 56.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18774783611297607 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 316 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 5 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08034206926822662 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 317 | PASS | ALL_IN | 7.0 | 8 | 5 | 0 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 321 | EQUIP_FROM_INVENTORY | ALL_IN | 7.0 | 8 | 11 | 1 | 58.0 | Flora Fatalis/DA_18_Ashe | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 322 | EQUIP_FROM_INVENTORY | ALL_IN | 7.0 | 8 | 11 | 1 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.06254623085260391 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 323 | BUY | ALL_IN | 7.0 | 8 | 11 | 1 | 58.0 | Flora Fatalis/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.741479754447937 | 0.0 | 0.0 | +b311d350-7bab-48ee-9833-0883606b4a2f / -d69fa0dc-74b6-4ee7-90f7-aaca5405c59c,d80c845d-24bc-4053-a60d-5d0122839b0c |
| Jogador 7 | 6-1 | 324 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 7 | 0 | 50.0 | Flora Fatalis/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04315805807709694 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 325 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 7 | 0 | 50.0 | Flora Fatalis/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5162668228149414 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 326 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 7 | 0 | 58.0 | Flora Fatalis/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15988308191299438 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 327 | BUY_XP | ALL_IN | 7.0 | 8 | 7 | 0 | 66.0 | Flora Fatalis/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 328 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 3 | 0 | 66.0 | Flora Fatalis/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04315805807709694 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 329 | MOVE_BENCH | ALL_IN | 7.0 | 8 | 3 | 0 | 66.0 | Flora Fatalis/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.201888307929039 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 331 | BUY | ALL_IN | 7.0 | 8 | 9 | 0 | 58.0 | Flora Fatalis/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2705824673175812 | 0.0 | 0.0 | +c93990ff-0a6f-46bc-8fc1-12623d55abc1 / -— |
| Jogador 7 | 6-2 | 332 | BUY_XP | ALL_IN | 7.0 | 8 | 6 | 0 | 58.0 | Flora Fatalis/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7064999938011169 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 333 | MOVE_BENCH | ALL_IN | 7.0 | 9 | 2 | 0 | 58.0 | Flora Fatalis/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09489015489816666 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 334 | BUY | ALL_IN | 7.0 | 9 | 2 | 0 | 56.0 | Flora Fatalis/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1410226821899414 | 0.0 | 0.0 | +194da7dc-39b4-40e3-869d-326ace65137b / -— |
| Jogador 7 | 6-2 | 335 | MOVE_BENCH | ALL_IN | 7.0 | 9 | 0 | 0 | 56.0 | Flora Fatalis/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4707551598548889 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 336 | SELL | ALL_IN | 7.0 | 9 | 0 | 0 | 64.0 | Flora Fatalis/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2869538366794586 | 0.0 | 0.0 | +— / -194da7dc-39b4-40e3-869d-326ace65137b |
| Jogador 7 | 6-2 | 337 | MOVE_BENCH | ALL_IN | 7.0 | 9 | 2 | 0 | 64.0 | Flora Fatalis/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11768639087677002 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 338 | MOVE_BENCH | ALL_IN | 7.0 | 9 | 2 | 0 | 74.0 | Flora Fatalis/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09685210883617401 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 339 | MOVE_BENCH | ALL_IN | 7.0 | 9 | 2 | 0 | 72.0 | Flora Fatalis/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20166561007499695 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 9 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.28737619519233704 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.054392240941524506 | 0.0 | 0.0 | +fddba3f3-87f3-4c97-a7b2-e5d1ef789709 / -— |
| Jogador 8 | 1-2 | 12 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8287736773490906 | 0.0 | 0.0 | +78019889-2624-4adb-917b-619681f23053 / -— |
| Jogador 8 | 1-2 | 13 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22103363275527954 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3514671325683594 | 0.0 | 0.0 | +74c2d7f0-8d5d-460e-88fc-5407b717144a / -— |
| Jogador 8 | 1-3 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.662534773349762 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 23 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 31 | BUY_XP | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44449999928474426 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 32 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 39 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07852748036384583 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1163219213485718 | 0.0 | 0.0 | +f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 / -78019889-2624-4adb-917b-619681f23053,fddba3f3-87f3-4c97-a7b2-e5d1ef789709 |
| Jogador 8 | 2-1 | 42 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 4.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45856958627700806 | 0.0 | 0.0 | +630d9254-3856-4d88-b981-43a8270b4b3d / -— |
| Jogador 8 | 2-1 | 43 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 4.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 49 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 4.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32252466678619385 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 51 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012891371734440327 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 52 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5559768676757812 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 53 | BUY | STABILIZE | 95.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.02041030488908291 | 0.0 | 0.0 | +4b4cc4ba-04a0-4e04-88f2-e6913a342285 / -— |
| Jogador 8 | 2-2 | 54 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.052536483854055405 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 55 | BUY_XP | STABILIZE | 95.0 | 4 | 4 | 0 | 14.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19449999928474426 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 56 | PASS | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 59 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5511317849159241 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 61 | BUY | STABILIZE | 89.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.005328469909727573 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 62 | BUY | STABILIZE | 89.0 | 5 | 3 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0073005021549761295 | 0.0 | 0.0 | +5de56114-806a-4f58-8241-b3b8434a2154 / -— |
| Jogador 8 | 2-3 | 63 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Leona | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4806644916534424 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 64 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Leona | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36491334438323975 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 65 | PASS | STABILIZE | 89.0 | 5 | 1 | 0 | 20.0 | —/DA_18_Leona | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 71 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1634853333234787 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 72 | BUY | STABILIZE | 83.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08067145943641663 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 8 | 2-4 | 73 | BUY_XP | STABILIZE | 83.0 | 5 | 4 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 74 | PASS | STABILIZE | 83.0 | 5 | 0 | 0 | 16.0 | —/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 81 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4808889925479889 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 82 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.055024079978466034 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 83 | PASS | STABILIZE | 83.0 | 5 | 6 | 0 | 20.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 91 | BUY_XP | STABILIZE | 83.0 | 5 | 12 | 1 | 20.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 92 | BUY_XP | STABILIZE | 83.0 | 5 | 8 | 0 | 20.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19949999451637268 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 93 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 4 | 0 | 20.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5044065117835999 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 94 | BUY | STABILIZE | 83.0 | 6 | 4 | 0 | 24.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4029689133167267 | 0.0 | 0.0 | +6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 / -— |
| Jogador 8 | 2-6 | 95 | SELL | STABILIZE | 83.0 | 6 | 1 | 0 | 24.0 | —/DA_18_Leona | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01344677247107029 | 0.0 | 0.0 | +— / -74c2d7f0-8d5d-460e-88fc-5407b717144a |
| Jogador 8 | 2-6 | 96 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 2 | 0 | 24.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09491176903247833 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 97 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 2 | 0 | 24.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03405407443642616 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 98 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 2 | 0 | 24.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16756293177604675 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 99 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 2 | 0 | 24.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20125576853752136 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 101 | BUY | STABILIZE | 83.0 | 6 | 9 | 0 | 26.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36879709362983704 | 0.0 | 0.0 | +57903c42-49ca-43e1-8f86-42429c189fb5 / -— |
| Jogador 8 | 2-7 | 102 | BUY_XP | STABILIZE | 83.0 | 6 | 6 | 0 | 26.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 103 | SELL | STABILIZE | 83.0 | 6 | 2 | 0 | 26.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0481230765581131 | 0.0 | 0.0 | +— / -5de56114-806a-4f58-8241-b3b8434a2154 |
| Jogador 8 | 2-7 | 104 | BUY_XP | STABILIZE | 83.0 | 6 | 4 | 0 | 26.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 105 | SELL | STABILIZE | 83.0 | 6 | 0 | 0 | 26.0 | —/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03021572157740593 | 0.0 | 0.0 | +— / -57903c42-49ca-43e1-8f86-42429c189fb5 |
| Jogador 8 | 2-7 | 106 | BUY | STABILIZE | 83.0 | 6 | 3 | 0 | 26.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3613998293876648 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 8 | 2-7 | 107 | SELL | STABILIZE | 83.0 | 6 | 0 | 0 | 26.0 | —/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05473846197128296 | 0.0 | 0.0 | +— / -4b4cc4ba-04a0-4e04-88f2-e6913a342285 |
| Jogador 8 | 2-7 | 108 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 3 | 0 | 26.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14799629151821136 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 109 | SELL | STABILIZE | 83.0 | 6 | 3 | 0 | 26.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41139981150627136 | 0.0 | 0.0 | +— / -d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 8 | 3-1 | 111 | BUY | STABILIZE | 83.0 | 6 | 12 | 1 | 26.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17625544965267181 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 112 | BUY | STABILIZE | 83.0 | 6 | 8 | 0 | 26.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12961196899414062 | 0.0 | 0.0 | +7b2af6c8-ec0f-4ab5-8913-9b88fc2e0e86 / -— |
| Jogador 8 | 3-1 | 113 | BUY_XP | STABILIZE | 83.0 | 6 | 6 | 0 | 26.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 114 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 2 | 0 | 26.0 | Defendente/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5201614499092102 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 115 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 2 | 0 | 24.0 | Defendente/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.755665123462677 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 116 | PASS | STABILIZE | 83.0 | 6 | 2 | 0 | 24.0 | Defendente/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 121 | BUY | STABILIZE | 83.0 | 6 | 9 | 0 | 24.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06472501158714294 | 0.0 | 0.0 | +4ac49c80-f0c3-47ae-a031-96928d244e13 / -— |
| Jogador 8 | 3-2 | 122 | BUY | STABILIZE | 83.0 | 6 | 5 | 0 | 24.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28564292192459106 | 0.0 | 0.0 | +2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c / -— |
| Jogador 8 | 3-2 | 123 | BUY_XP | STABILIZE | 83.0 | 6 | 4 | 0 | 24.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 124 | SELL | STABILIZE | 83.0 | 6 | 0 | 0 | 24.0 | Defendente/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12817725539207458 | 0.0 | 0.0 | +— / -2c9e300a-5b3d-46c6-a67d-1c7ddd2dd84c |
| Jogador 8 | 3-2 | 125 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 1 | 0 | 24.0 | Defendente/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17541909217834473 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 126 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 1 | 0 | 26.0 | Defendente/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08904644846916199 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 127 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 1 | 0 | 24.0 | Defendente/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00022468309907708317 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 128 | MOVE_BOARD | STABILIZE | 83.0 | 6 | 1 | 0 | 24.0 | Defendente/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3356137275695801 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 129 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 1 | 0 | 24.0 | Defendente/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17470937967300415 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 131 | BUY | STABILIZE | 71.0 | 6 | 6 | 0 | 26.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2852034866809845 | 0.0 | 0.0 | +3bf8af53-85e7-4e5b-8cf8-b7198a955e8d / -— |
| Jogador 8 | 3-3 | 132 | BUY_XP | STABILIZE | 71.0 | 6 | 5 | 0 | 26.0 | Defendente/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 133 | SELL | STABILIZE | 71.0 | 6 | 1 | 0 | 26.0 | Defendente/DA_18_Leona | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12189671397209167 | 0.0 | 0.0 | +— / -3bf8af53-85e7-4e5b-8cf8-b7198a955e8d |
| Jogador 8 | 3-3 | 134 | MOVE_BENCH | STABILIZE | 71.0 | 6 | 2 | 0 | 26.0 | Defendente/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08890864998102188 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 135 | MOVE_BENCH | STABILIZE | 71.0 | 6 | 2 | 0 | 24.0 | Defendente/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7434554696083069 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 136 | MOVE_BENCH | STABILIZE | 71.0 | 6 | 2 | 0 | 24.0 | Defendente/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24805279076099396 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 137 | MOVE_BENCH | STABILIZE | 71.0 | 6 | 2 | 0 | 26.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07503002136945724 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 138 | MOVE_BENCH | STABILIZE | 71.0 | 6 | 2 | 0 | 24.0 | Defendente/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12295825779438019 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 139 | SELL | STABILIZE | 71.0 | 6 | 2 | 0 | 28.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04646836966276169 | 0.0 | 0.0 | +— / -7b2af6c8-ec0f-4ab5-8913-9b88fc2e0e86 |
| Jogador 8 | 3-4 | 141 | BUY | STABILIZE | 71.0 | 6 | 10 | 1 | 28.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06741317361593246 | 0.0 | 0.0 | +82e109f9-54c8-492d-93e5-7e0dd0034b15 / -— |
| Jogador 8 | 3-4 | 142 | BUY_XP | STABILIZE | 71.0 | 6 | 7 | 0 | 28.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 143 | MOVE_BENCH | STABILIZE | 71.0 | 6 | 3 | 0 | 28.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5615339875221252 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 144 | MOVE_BENCH | STABILIZE | 71.0 | 6 | 3 | 0 | 28.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23226338624954224 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 145 | SELL | STABILIZE | 71.0 | 6 | 3 | 0 | 30.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04772307723760605 | 0.0 | 0.0 | +— / -82e109f9-54c8-492d-93e5-7e0dd0034b15 |
| Jogador 8 | 3-4 | 146 | BUY_XP | STABILIZE | 71.0 | 6 | 6 | 0 | 30.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.429500013589859 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 147 | SELL | STABILIZE | 71.0 | 7 | 2 | 0 | 30.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12021155655384064 | 0.0 | 0.0 | +— / -6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 |
| Jogador 8 | 3-4 | 148 | MOVE_BENCH | STABILIZE | 71.0 | 7 | 5 | 0 | 30.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6140709519386292 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 149 | BUY_XP | STABILIZE | 71.0 | 7 | 5 | 0 | 36.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 151 | BUY | STABILIZE | 71.0 | 7 | 6 | 0 | 36.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2811863422393799 | 0.0 | 0.0 | +9b5e9e71-6772-49bc-979f-11f446f27b11 / -— |
| Jogador 8 | 3-5 | 152 | BUY | STABILIZE | 71.0 | 7 | 3 | 0 | 36.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7132324576377869 | 0.0 | 0.0 | +9af097e2-729d-474a-9a7e-b266c665c606 / -— |
| Jogador 8 | 3-5 | 153 | SELL | STABILIZE | 71.0 | 7 | 0 | 0 | 36.0 | Defendente/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3045044541358948 | 0.0 | 0.0 | +— / -9af097e2-729d-474a-9a7e-b266c665c606 |
| Jogador 8 | 3-5 | 154 | BUY | STABILIZE | 71.0 | 7 | 3 | 0 | 36.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28480657935142517 | 0.0 | 0.0 | +fa5dc86b-f736-4083-b9df-5cc174b726f2 / -— |
| Jogador 8 | 3-5 | 155 | SELL | STABILIZE | 71.0 | 7 | 1 | 0 | 36.0 | Defendente/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12836922705173492 | 0.0 | 0.0 | +— / -fa5dc86b-f736-4083-b9df-5cc174b726f2 |
| Jogador 8 | 3-5 | 156 | SELL | STABILIZE | 71.0 | 7 | 3 | 0 | 36.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1201075091958046 | 0.0 | 0.0 | +— / -9b5e9e71-6772-49bc-979f-11f446f27b11 |
| Jogador 8 | 3-5 | 157 | BUY_XP | STABILIZE | 71.0 | 7 | 6 | 0 | 36.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 158 | PASS | STABILIZE | 71.0 | 7 | 2 | 0 | 36.0 | Defendente/DA_Brambleback18 | REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 161 | BUY | STABILIZE | 71.0 | 7 | 9 | 0 | 36.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2839283049106598 | 0.0 | 0.0 | +23366968-ed3f-43d0-9f24-bb7691bf5d45 / -— |
| Jogador 8 | 3-6 | 162 | BUY | STABILIZE | 71.0 | 7 | 6 | 0 | 36.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7135183811187744 | 0.0 | 0.0 | +b55260cd-3c6a-4cb8-99d0-b7c6471103ad / -— |
| Jogador 8 | 3-6 | 163 | MOVE_BENCH | STABILIZE | 71.0 | 7 | 3 | 0 | 36.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0006709432927891612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 164 | MOVE_BENCH | STABILIZE | 71.0 | 7 | 3 | 0 | 36.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5603313446044922 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 165 | BUY | STABILIZE | 71.0 | 7 | 3 | 0 | 34.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06701988726854324 | 0.0 | 0.0 | +b71cd729-4b0b-4276-8a58-aaf1f0c2e4c0 / -— |
| Jogador 8 | 3-6 | 166 | MOVE_BENCH | STABILIZE | 71.0 | 7 | 1 | 0 | 34.0 | Defendente/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027768122032284737 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 167 | SELL | STABILIZE | 71.0 | 7 | 1 | 0 | 36.0 | Defendente/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13100136816501617 | 0.0 | 0.0 | +— / -b71cd729-4b0b-4276-8a58-aaf1f0c2e4c0 |
| Jogador 8 | 3-6 | 168 | MOVE_BENCH | STABILIZE | 71.0 | 7 | 3 | 0 | 36.0 | Defendente/DA_Brambleback18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3538854122161865 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 169 | SELL | STABILIZE | 71.0 | 7 | 3 | 0 | 36.0 | Defendente/DA_Brambleback18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3053317964076996 | 0.0 | 0.0 | +— / -b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 8 | 3-7 | 171 | MOVE_BENCH | STABILIZE | 71.0 | 7 | 13 | 1 | 36.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07125300168991089 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 172 | BUY | STABILIZE | 71.0 | 7 | 13 | 1 | 34.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06907361000776291 | 0.0 | 0.0 | +3625f791-4c9f-4b95-bdf7-4a322dcd55d3 / -— |
| Jogador 8 | 3-7 | 173 | BUY_XP | STABILIZE | 71.0 | 7 | 10 | 1 | 34.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 174 | BUY_XP | STABILIZE | 71.0 | 7 | 6 | 0 | 34.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 175 | SELL | STABILIZE | 71.0 | 7 | 2 | 0 | 34.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12526154518127441 | 0.0 | 0.0 | +— / -3625f791-4c9f-4b95-bdf7-4a322dcd55d3 |
| Jogador 8 | 3-7 | 176 | BUY_XP | STABILIZE | 71.0 | 7 | 5 | 0 | 34.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 177 | SELL | STABILIZE | 71.0 | 7 | 1 | 0 | 34.0 | Defendente/DA_Brambleback18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16071097552776337 | 0.0 | 0.0 | +— / -4d995451-2e5c-43c2-93f0-22e074e35ab2 |
| Jogador 8 | 3-7 | 178 | BUY_XP | STABILIZE | 71.0 | 7 | 5 | 0 | 34.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 179 | MOVE_BOARD | STABILIZE | 71.0 | 7 | 1 | 0 | 34.0 | Defendente/DA_Brambleback18 | BUY, MOVE_BOARD, PASS | True | True | -0.18787872791290283 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 181 | BUY | STABILIZE | 71.0 | 7 | 7 | 0 | 34.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.18525971472263336 | 0.0 | 0.0 | +2c153083-6c43-425e-90d5-23f7f2058592 / -— |
| Jogador 8 | 4-1 | 182 | CRAFT_AND_EQUIP | STABILIZE | 71.0 | 7 | 4 | 0 | 34.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08596033602952957 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 183 | MOVE_BENCH | STABILIZE | 71.0 | 7 | 4 | 0 | 34.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10080467909574509 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 184 | BUY | STABILIZE | 71.0 | 7 | 4 | 0 | 34.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5148497223854065 | 0.0 | 0.0 | +88035b70-61e0-4279-9d55-e451f412f0d3 / -— |
| Jogador 8 | 4-1 | 185 | SELL | STABILIZE | 71.0 | 7 | 1 | 0 | 34.0 | Defendente/DA_Brambleback18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5648497343063354 | 0.0 | 0.0 | +— / -88035b70-61e0-4279-9d55-e451f412f0d3 |
| Jogador 8 | 4-1 | 186 | MOVE_BENCH | STABILIZE | 71.0 | 7 | 4 | 0 | 34.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7874386310577393 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 187 | BUY | STABILIZE | 71.0 | 7 | 4 | 0 | 34.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1317434310913086 | 0.0 | 0.0 | +1e81ac95-667f-494d-89eb-2bcdcf887a7e / -— |
| Jogador 8 | 4-1 | 188 | SELL | STABILIZE | 71.0 | 7 | 1 | 0 | 34.0 | Defendente/DA_Brambleback18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18174342811107635 | 0.0 | 0.0 | +— / -1e81ac95-667f-494d-89eb-2bcdcf887a7e |
| Jogador 8 | 4-1 | 189 | MOVE_BENCH | STABILIZE | 71.0 | 7 | 4 | 0 | 34.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15061548352241516 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 191 | BUY | STABILIZE | 71.0 | 7 | 11 | 1 | 34.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3206222653388977 | 0.0 | 0.0 | +08a36d54-bb5c-48a6-afb1-e0f9943bf069 / -— |
| Jogador 8 | 4-2 | 192 | BUY_XP | STABILIZE | 71.0 | 7 | 7 | 0 | 34.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 193 | MOVE_BENCH | STABILIZE | 71.0 | 7 | 3 | 0 | 34.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2409936636686325 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 194 | MOVE_BENCH | STABILIZE | 71.0 | 7 | 3 | 0 | 34.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022456469014286995 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 195 | MOVE_BENCH | STABILIZE | 71.0 | 7 | 3 | 0 | 34.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03087017685174942 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 196 | PASS | STABILIZE | 71.0 | 7 | 3 | 0 | 36.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 201 | BUY | STABILIZE | 71.0 | 7 | 11 | 1 | 36.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6144455671310425 | 0.0 | 0.0 | +1fa69553-5270-4459-986b-600f748711b7 / -— |
| Jogador 8 | 4-3 | 202 | BUY_XP | STABILIZE | 71.0 | 7 | 8 | 0 | 36.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 203 | BUY_XP | STABILIZE | 71.0 | 7 | 4 | 0 | 36.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 204 | SELL | STABILIZE | 71.0 | 7 | 0 | 0 | 36.0 | Defendente/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31599298119544983 | 0.0 | 0.0 | +— / -1fa69553-5270-4459-986b-600f748711b7 |
| Jogador 8 | 4-3 | 205 | SELL | STABILIZE | 71.0 | 7 | 3 | 0 | 36.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13476721942424774 | 0.0 | 0.0 | +— / -23366968-ed3f-43d0-9f24-bb7691bf5d45 |
| Jogador 8 | 4-3 | 206 | BUY_XP | STABILIZE | 71.0 | 7 | 6 | 0 | 36.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 207 | SELL | STABILIZE | 71.0 | 7 | 2 | 0 | 36.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08233251422643661 | 0.0 | 0.0 | +— / -b55260cd-3c6a-4cb8-99d0-b7c6471103ad |
| Jogador 8 | 4-3 | 208 | EQUIP_FROM_INVENTORY | STABILIZE | 71.0 | 7 | 5 | 0 | 36.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.06298024207353592 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 209 | MOVE_BOARD | STABILIZE | 71.0 | 7 | 5 | 0 | 36.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.29594194889068604 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 211 | BUY | WINSTREAK | 71.0 | 8 | 14 | 1 | 36.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09707539528608322 | 0.0 | 0.0 | +167110eb-b0d0-4873-9ffe-38286dcc5ca2 / -— |
| Jogador 8 | 4-4 | 212 | BUY | WINSTREAK | 71.0 | 8 | 10 | 1 | 36.0 | Defendente/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03711622208356857 | 0.0 | 0.0 | +8995f621-b355-44ec-816e-797184bdc266 / -— |
| Jogador 8 | 4-4 | 213 | BUY | WINSTREAK | 71.0 | 8 | 8 | 0 | 36.0 | Defendente/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2536891996860504 | 0.0 | 0.0 | +bae633d7-8337-461a-9a84-9c9758392bb6 / -— |
| Jogador 8 | 4-4 | 214 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 6 | 0 | 36.0 | Defendente/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07127463072538376 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 215 | BUY_XP | WINSTREAK | 71.0 | 8 | 6 | 0 | 36.0 | Defendente/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 216 | SELL | WINSTREAK | 71.0 | 8 | 2 | 0 | 36.0 | Defendente/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14870768785476685 | 0.0 | 0.0 | +— / -f92b86ad-e2f2-4a04-b87f-8bcfa2788e53 |
| Jogador 8 | 4-4 | 217 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 5 | 0 | 36.0 | Defendente/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09596548229455948 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 218 | BUY_XP | WINSTREAK | 71.0 | 8 | 5 | 0 | 40.0 | Defendente/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 219 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 1 | 0 | 40.0 | Defendente/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4652605354785919 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 221 | BUY | WINSTREAK | 71.0 | 8 | 9 | 0 | 44.0 | Defendente/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26347148418426514 | 0.0 | 0.0 | +8aa832ec-4c09-43bd-ae21-baf7268e468d / -— |
| Jogador 8 | 4-5 | 222 | BUY | WINSTREAK | 71.0 | 8 | 6 | 0 | 44.0 | Defendente/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06748849153518677 | 0.0 | 0.0 | +715d5bfc-c8c3-4dec-a247-9e07ee2755e8 / -— |
| Jogador 8 | 4-5 | 223 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 2 | 0 | 44.0 | Defendente/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1813793033361435 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 224 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 2 | 0 | 42.0 | Defendente/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09855508804321289 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 225 | SELL | WINSTREAK | 71.0 | 8 | 2 | 0 | 46.0 | Defendente/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03326193615794182 | 0.0 | 0.0 | +— / -8995f621-b355-44ec-816e-797184bdc266 |
| Jogador 8 | 4-5 | 226 | BUY_XP | WINSTREAK | 71.0 | 8 | 4 | 0 | 46.0 | Defendente/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 227 | SELL | WINSTREAK | 71.0 | 8 | 0 | 0 | 46.0 | Defendente/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06400000303983688 | 0.0 | 0.0 | +— / -bae633d7-8337-461a-9a84-9c9758392bb6 |
| Jogador 8 | 4-5 | 228 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 2 | 0 | 46.0 | Defendente/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4469520151615143 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 229 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 2 | 0 | 48.0 | Defendente/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05535149201750755 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 231 | BUY | WINSTREAK | 71.0 | 8 | 11 | 1 | 46.0 | Defendente/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18385478854179382 | 0.0 | 0.0 | +db6b2dca-4de1-420e-aadb-943e19b6121a / -— |
| Jogador 8 | 4-6 | 232 | BUY | WINSTREAK | 71.0 | 8 | 8 | 0 | 46.0 | Defendente/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08569048345088959 | 0.0 | 0.0 | +5c931416-3aeb-40d4-9e6f-612b0d387226 / -— |
| Jogador 8 | 4-6 | 233 | BUY_XP | WINSTREAK | 71.0 | 8 | 4 | 0 | 46.0 | Defendente/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 234 | SELL | WINSTREAK | 71.0 | 8 | 0 | 0 | 46.0 | Defendente/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14287811517715454 | 0.0 | 0.0 | +— / -db6b2dca-4de1-420e-aadb-943e19b6121a |
| Jogador 8 | 4-6 | 235 | SELL | WINSTREAK | 71.0 | 8 | 3 | 0 | 46.0 | Defendente/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13569048047065735 | 0.0 | 0.0 | +— / -5c931416-3aeb-40d4-9e6f-612b0d387226 |
| Jogador 8 | 4-6 | 236 | BUY_XP | WINSTREAK | 71.0 | 8 | 7 | 0 | 46.0 | Defendente/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 237 | SELL | WINSTREAK | 71.0 | 8 | 3 | 0 | 46.0 | Defendente/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10880889743566513 | 0.0 | 0.0 | +— / -167110eb-b0d0-4873-9ffe-38286dcc5ca2 |
| Jogador 8 | 4-6 | 238 | BUY_XP | WINSTREAK | 71.0 | 8 | 7 | 0 | 46.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 239 | MOVE_BOARD | WINSTREAK | 71.0 | 8 | 3 | 0 | 46.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 241 | BUY | WINSTREAK | 71.0 | 8 | 12 | 1 | 46.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.5896151661872864 | 0.0 | 0.0 | +d633d2d8-1b5e-49cf-ac47-114c6ad29cf8 / -— |
| Jogador 8 | 4-7 | 242 | BUY | WINSTREAK | 71.0 | 8 | 8 | 0 | 46.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010296505875885487 | 0.0 | 0.0 | +b70671f9-0d78-4ae8-bd13-0267c96e7207 / -— |
| Jogador 8 | 4-7 | 243 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 4 | 0 | 46.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0366072952747345 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 244 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 4 | 0 | 46.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0027649779804050922 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 245 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 4 | 0 | 46.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13466250896453857 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 246 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 4 | 0 | 46.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05441568046808243 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 247 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 4 | 0 | 46.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002770080929622054 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 248 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 4 | 0 | 46.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6173850893974304 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 249 | BUY_XP | WINSTREAK | 71.0 | 8 | 4 | 0 | 48.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 251 | EQUIP_FROM_INVENTORY | WINSTREAK | 71.0 | 8 | 8 | 0 | 48.0 | Defendente/DA_Brambleback18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 252 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 8 | 0 | 48.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4301009476184845 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 253 | BUY | WINSTREAK | 71.0 | 8 | 8 | 0 | 46.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14517159759998322 | 0.0 | 0.0 | +f32e50e0-1430-4549-a1dd-a8473ffe0bd4 / -— |
| Jogador 8 | 5-1 | 254 | SELL | WINSTREAK | 71.0 | 8 | 3 | 0 | 46.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06763076782226562 | 0.0 | 0.0 | +— / -b70671f9-0d78-4ae8-bd13-0267c96e7207 |
| Jogador 8 | 5-1 | 255 | BUY | WINSTREAK | 71.0 | 8 | 7 | 0 | 46.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2122342735528946 | 0.0 | 0.0 | +af98a89b-ee97-45ce-972a-3f41e280b6b2 / -— |
| Jogador 8 | 5-1 | 256 | SELL | WINSTREAK | 71.0 | 8 | 3 | 0 | 46.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03583471477031708 | 0.0 | 0.0 | +— / -af98a89b-ee97-45ce-972a-3f41e280b6b2 |
| Jogador 8 | 5-1 | 257 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 7 | 0 | 46.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0029687988571822643 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 258 | BUY | WINSTREAK | 71.0 | 8 | 7 | 0 | 46.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.062997967004776 | 0.0 | 0.0 | +5a6985d6-5377-425c-b4a3-c53dc138b288 / -— |
| Jogador 8 | 5-1 | 259 | SELL | WINSTREAK | 71.0 | 8 | 3 | 0 | 46.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12713846564292908 | 0.0 | 0.0 | +— / -5a6985d6-5377-425c-b4a3-c53dc138b288 |
| Jogador 8 | 5-2 | 261 | BUY | ECON | 55.0 | 8 | 12 | 1 | 46.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5913574695587158 | 0.0 | 0.0 | +a5deb295-89d5-4573-8ace-e370a0718266 / -— |
| Jogador 8 | 5-2 | 262 | MOVE_BENCH | ECON | 55.0 | 8 | 9 | 0 | 46.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024023113772273064 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 263 | BUY_XP | ECON | 55.0 | 8 | 9 | 0 | 48.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 264 | BUY_XP | ECON | 55.0 | 8 | 5 | 0 | 48.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 265 | SELL | ECON | 55.0 | 8 | 1 | 0 | 48.0 | Defendente/DA_18_Lux_Elderwood | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.034763041883707047 | 0.0 | 0.0 | +— / -2c153083-6c43-425e-90d5-23f7f2058592 |
| Jogador 8 | 5-2 | 266 | BUY_XP | ECON | 55.0 | 8 | 4 | 0 | 48.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 267 | SELL | ECON | 55.0 | 8 | 0 | 0 | 48.0 | Defendente/DA_18_Lux_Elderwood | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3234530985355377 | 0.0 | 0.0 | +— / -a5deb295-89d5-4573-8ace-e370a0718266 |
| Jogador 8 | 5-2 | 268 | MOVE_BENCH | ECON | 55.0 | 8 | 3 | 0 | 48.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1275494247674942 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 269 | MOVE_BENCH | ECON | 55.0 | 8 | 3 | 0 | 50.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12768159806728363 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 271 | MOVE_BENCH | ECON | 55.0 | 8 | 9 | 0 | 50.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02755848504602909 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 272 | MOVE_BENCH | ECON | 55.0 | 8 | 9 | 0 | 48.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13791531324386597 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 273 | MOVE_BENCH | ECON | 55.0 | 8 | 9 | 0 | 50.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11597780138254166 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 274 | MOVE_BENCH | ECON | 55.0 | 8 | 9 | 0 | 50.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09978671371936798 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 275 | BUY_XP | ECON | 55.0 | 8 | 9 | 0 | 50.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 276 | BUY_XP | ECON | 55.0 | 8 | 5 | 0 | 50.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 277 | SELL | ECON | 55.0 | 8 | 1 | 0 | 50.0 | Defendente/DA_18_Lux_Elderwood | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06209230795502663 | 0.0 | 0.0 | +— / -08a36d54-bb5c-48a6-afb1-e0f9943bf069 |
| Jogador 8 | 5-3 | 278 | EQUIP_FROM_INVENTORY | ECON | 55.0 | 8 | 5 | 0 | 50.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, EQUIP_FROM_INVENTORY | True | — | 0.08960529416799545 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 279 | BUY | ECON | 55.0 | 8 | 5 | 0 | 50.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1575453281402588 | 0.0 | 0.0 | +af404167-469a-447e-b415-dcb52033ef9b / -— |
| Jogador 8 | 5-4 | 281 | BUY | ECON | 55.0 | 8 | 9 | 0 | 50.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2138708531856537 | 0.0 | 0.0 | +76fcc4d0-4988-4e99-8ac0-c251f0b99dcd / -— |
| Jogador 8 | 5-4 | 282 | BUY_XP | ECON | 55.0 | 8 | 6 | 0 | 50.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 283 | SELL | ECON | 55.0 | 8 | 2 | 0 | 50.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03642700985074043 | 0.0 | 0.0 | +— / -af404167-469a-447e-b415-dcb52033ef9b |
| Jogador 8 | 5-4 | 284 | BUY_XP | ECON | 55.0 | 8 | 5 | 0 | 50.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6501250267028809 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 285 | MOVE_BENCH | ECON | 55.0 | 9 | 1 | 0 | 50.0 | Defendente/DA_18_Lux_Elderwood | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19398920238018036 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 286 | MOVE_BENCH | ECON | 55.0 | 9 | 1 | 0 | 48.0 | Defendente/DA_18_Lux_Elderwood | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5364502668380737 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 287 | MOVE_BOARD | ECON | 55.0 | 9 | 1 | 0 | 56.0 | Defendente/DA_18_Lux_Elderwood | BUY, MOVE_BOARD, PASS | True | True | -0.2382698804140091 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 288 | MOVE_BOARD | ECON | 55.0 | 9 | 1 | 0 | 56.0 | Defendente/DA_18_Lux_Elderwood | BUY, MOVE_BOARD, PASS | True | True | 0.12328065186738968 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 289 | MOVE_BOARD | ECON | 55.0 | 9 | 1 | 0 | 56.0 | Defendente/DA_18_Lux_Elderwood | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 291 | BUY | ECON | 55.0 | 9 | 7 | 0 | 56.0 | Defendente/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7572479248046875 | 0.0 | 0.0 | +f087511a-d834-4f41-9b99-00bf0f6dc061 / -4ac49c80-f0c3-47ae-a031-96928d244e13,d633d2d8-1b5e-49cf-ac47-114c6ad29cf8 |
| Jogador 8 | 5-5 | 292 | BUY | ECON | 55.0 | 9 | 3 | 0 | 40.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015468857251107693 | 0.0 | 0.0 | +c07a17cf-e9e7-42be-b925-cb4f699593de / -— |
| Jogador 8 | 5-5 | 293 | SELL | ECON | 55.0 | 9 | 0 | 0 | 40.0 | Defendente/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13449230790138245 | 0.0 | 0.0 | +— / -c07a17cf-e9e7-42be-b925-cb4f699593de |
| Jogador 8 | 5-5 | 294 | BUY | ECON | 55.0 | 9 | 3 | 0 | 40.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28416571021080017 | 0.0 | 0.0 | +150a2da3-f559-4a40-a058-005e9c74e11f / -— |
| Jogador 8 | 5-5 | 295 | SELL | ECON | 55.0 | 9 | 1 | 0 | 40.0 | Defendente/DA_Brambleback18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11599999666213989 | 0.0 | 0.0 | +— / -150a2da3-f559-4a40-a058-005e9c74e11f |
| Jogador 8 | 5-5 | 296 | BUY | ECON | 55.0 | 9 | 3 | 0 | 40.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23742695152759552 | 0.0 | 0.0 | +8486b8a9-20fe-4234-bbba-0efa031c3b76 / -— |
| Jogador 8 | 5-5 | 297 | SELL | ECON | 55.0 | 9 | 1 | 0 | 40.0 | Defendente/DA_Brambleback18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12006153911352158 | 0.0 | 0.0 | +— / -8486b8a9-20fe-4234-bbba-0efa031c3b76 |
| Jogador 8 | 5-5 | 298 | MOVE_BENCH | ECON | 55.0 | 9 | 3 | 0 | 40.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1348697990179062 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 299 | MOVE_BENCH | ECON | 55.0 | 9 | 3 | 0 | 50.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45848098397254944 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 301 | BUY | ECON | 55.0 | 9 | 9 | 0 | 56.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6707342267036438 | 0.0 | 0.0 | +2d5214b0-3e0c-4e71-8664-2459bf616650 / -— |
| Jogador 8 | 5-6 | 302 | BUY | ECON | 55.0 | 9 | 6 | 0 | 56.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017461508512496948 | 0.0 | 0.0 | +f078e755-d142-4dad-99d0-7e7599e3016d / -— |
| Jogador 8 | 5-6 | 303 | MOVE_BOARD | ECON | 55.0 | 9 | 2 | 0 | 56.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001385686919093132 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 304 | MOVE_BENCH | ECON | 55.0 | 9 | 2 | 0 | 56.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.053044818341732025 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 305 | MOVE_BENCH | ECON | 55.0 | 9 | 2 | 0 | 46.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6292758584022522 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 306 | SELL | ECON | 55.0 | 9 | 2 | 0 | 62.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12713846564292908 | 0.0 | 0.0 | +— / -f078e755-d142-4dad-99d0-7e7599e3016d |
| Jogador 8 | 5-6 | 307 | BUY_XP | ECON | 55.0 | 9 | 6 | 0 | 62.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.04800000041723251 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 308 | MOVE_BOARD | ECON | 55.0 | 9 | 2 | 0 | 62.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.17341938614845276 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 309 | MOVE_BOARD | ECON | 55.0 | 9 | 2 | 0 | 62.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 311 | BUY | WINSTREAK | 55.0 | 9 | 9 | 0 | 62.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0671389251947403 | 0.0 | 0.0 | +3c46b699-2b56-48d0-820c-b523c5153b9f / -— |
| Jogador 8 | 5-7 | 312 | BUY | WINSTREAK | 55.0 | 9 | 4 | 0 | 62.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03906526416540146 | 0.0 | 0.0 | +3365b4aa-125c-4f72-bcc5-01c5a205b9b0 / -— |
| Jogador 8 | 5-7 | 313 | MOVE_BENCH | WINSTREAK | 55.0 | 9 | 0 | 0 | 62.0 | Defendente/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020338356494903564 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 314 | MOVE_BENCH | WINSTREAK | 55.0 | 9 | 0 | 0 | 66.0 | Defendente/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 315 | PASS | WINSTREAK | 55.0 | 9 | 0 | 0 | 66.0 | Defendente/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 321 | EQUIP_FROM_INVENTORY | WINSTREAK | 55.0 | 9 | 6 | 0 | 66.0 | Defendente/DA_Brambleback18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 322 | EQUIP_FROM_INVENTORY | WINSTREAK | 55.0 | 9 | 6 | 0 | 66.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.061984095722436905 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 323 | BUY | WINSTREAK | 55.0 | 9 | 6 | 0 | 66.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4964295029640198 | 0.0 | 0.0 | +1f349179-be2a-4738-bda1-072f7fae2147 / -— |
| Jogador 8 | 6-1 | 324 | SELL | WINSTREAK | 55.0 | 9 | 2 | 0 | 66.0 | Defendente/DA_Brambleback18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3223547041416168 | 0.0 | 0.0 | +— / -2d5214b0-3e0c-4e71-8664-2459bf616650 |
| Jogador 8 | 6-1 | 325 | BUY_XP | WINSTREAK | 55.0 | 9 | 5 | 0 | 66.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 326 | SELL | WINSTREAK | 55.0 | 9 | 1 | 0 | 66.0 | Defendente/DA_Brambleback18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5464295148849487 | 0.0 | 0.0 | +— / -1f349179-be2a-4738-bda1-072f7fae2147 |
| Jogador 8 | 6-1 | 327 | MOVE_BENCH | WINSTREAK | 55.0 | 9 | 5 | 0 | 66.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5268164873123169 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 328 | MOVE_BENCH | WINSTREAK | 55.0 | 9 | 5 | 0 | 68.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15974947810173035 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 329 | MOVE_BENCH | WINSTREAK | 55.0 | 9 | 5 | 0 | 64.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11735109239816666 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 331 | BUY | WINSTREAK | 55.0 | 9 | 12 | 1 | 66.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06425192952156067 | 0.0 | 0.0 | +8538e488-6f36-433a-b261-73626f24bb07 / -— |
| Jogador 8 | 6-2 | 332 | MOVE_BENCH | WINSTREAK | 55.0 | 9 | 9 | 0 | 66.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09755563735961914 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 333 | BUY | WINSTREAK | 55.0 | 9 | 9 | 0 | 62.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7256196737289429 | 0.0 | 0.0 | +d632ff66-a7c4-43d3-afb3-b83c174cda35 / -— |
| Jogador 8 | 6-2 | 334 | BUY_XP | WINSTREAK | 55.0 | 9 | 8 | 0 | 62.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 335 | BUY_XP | WINSTREAK | 55.0 | 9 | 4 | 0 | 62.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 336 | SELL | WINSTREAK | 55.0 | 9 | 0 | 0 | 62.0 | Defendente/DA_Brambleback18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32760000228881836 | 0.0 | 0.0 | +— / -d632ff66-a7c4-43d3-afb3-b83c174cda35 |
| Jogador 8 | 6-2 | 337 | MOVE_BENCH | WINSTREAK | 55.0 | 9 | 1 | 0 | 62.0 | Defendente/DA_Brambleback18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41498780250549316 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 338 | SELL | WINSTREAK | 55.0 | 9 | 1 | 0 | 66.0 | Defendente/DA_Brambleback18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11905210465192795 | 0.0 | 0.0 | +— / -8aa832ec-4c09-43bd-ae21-baf7268e468d |
| Jogador 8 | 6-2 | 339 | EQUIP_FROM_INVENTORY | WINSTREAK | 55.0 | 9 | 4 | 0 | 66.0 | Defendente/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.04608887434005737 | 0.0 | 0.0 | +— / -— |

O audit_report.json mantém as máscaras brutas, distribuições da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Null indica campo ausente, não zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 215 | 236 | 79 | 5 | 28 | 0 | 0 | 0 | 3 | 0.0 |
- Jogador 1 — gasto por ação: BUY: 112g, BUY_XP: 124g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 5g, stage 2: 48g, stage 3: 66g, stage 4: 71g, stage 5: 46g, stage 6: 0g
| Jogador 2 | 178 | 196 | 68 | 2 | 20 | 1 | 0 | 0 | 3 | 0.0 |
- Jogador 2 — gasto por ação: BUY: 100g, BUY_XP: 96g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 5g, stage 2: 46g, stage 3: 70g, stage 4: 67g, stage 5: 8g, stage 6: 0g
| Jogador 3 | 217 | 202 | 27 | 6 | 30 | 1 | 0 | 0 | 8 | 0.0 |
- Jogador 3 — gasto por ação: BUY: 70g, BUY_XP: 132g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 5g, stage 2: 43g, stage 3: 45g, stage 4: 51g, stage 5: 58g, stage 6: 0g
| Jogador 4 | 157 | 137 | 18 | 5 | 18 | 1 | 0 | 0 | 3 | 0.0 |
- Jogador 4 — gasto por ação: BUY: 53g, BUY_XP: 84g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 4g, stage 2: 48g, stage 3: 47g, stage 4: 38g, stage 5: 0g, stage 6: 0g
| Jogador 5 | 182 | 193 | 61 | 1 | 18 | 1 | 0 | 0 | 2 | 0.0 |
- Jogador 5 — gasto por ação: BUY: 105g, BUY_XP: 88g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 6g, stage 2: 48g, stage 3: 54g, stage 4: 75g, stage 5: 10g, stage 6: 0g
| Jogador 6 | 211 | 269 | 102 | 7 | 28 | 2 | 0 | 0 | 2 | 0.0 |
- Jogador 6 — gasto por ação: BUY: 145g, BUY_XP: 124g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 7g, stage 2: 37g, stage 3: 90g, stage 4: 88g, stage 5: 47g, stage 6: 0g
| Jogador 7 | 256 | 287 | 109 | 5 | 29 | 1 | 0 | 0 | 2 | 64.0 |
- Jogador 7 — gasto por ação: BUY: 155g, BUY_XP: 132g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 8g, stage 2: 53g, stage 3: 67g, stage 4: 84g, stage 5: 58g, stage 6: 17g
| Jogador 8 | 249 | 322 | 122 | 11 | 35 | 2 | 0 | 0 | 4 | 66.0 |
- Jogador 8 — gasto por ação: BUY: 162g, BUY_XP: 160g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 7g, stage 2: 46g, stage 3: 78g, stage 4: 90g, stage 5: 81g, stage 6: 20g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 1 | 1 | 0 | 0.0% |
| Jogador 2 | 1 | 1 | 0 | 0.0% |
| Jogador 3 | 1 | 1 | 0 | 0.0% |
| Jogador 4 | 1 | 1 | 0 | 0.0% |
| Jogador 5 | 1 | 1 | 0 | 0.0% |
| Jogador 6 | 3 | 2 | 1 | 33.3% |
| Jogador 7 | 2 | 2 | 0 | 0.0% |
| Jogador 8 | 1 | 1 | 0 | 0.0% |

Os detalhes por transição ficam em audit_report.json. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ médio qualidade | Δ estrutural médio | Δ qualidade quando combate positivo | Δ qualidade quando combate negativo |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 215 | 0 | 0 | 215 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ 0.0000 (41 ações), BUY_XP: Δ 0.0000 (31 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0000 (84 ações), MOVE_BOARD: Δ 0.0000 (6 ações), PASS: Δ 0.0000 (20 ações), SELL: Δ 0.0000 (29 ações)
| Jogador 2 | 178 | 0 | 0 | 178 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ 0.0000 (40 ações), BUY_XP: Δ 0.0000 (24 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (53 ações), MOVE_BOARD: Δ 0.0000 (8 ações), PASS: Δ 0.0000 (23 ações), SELL: Δ 0.0000 (28 ações)
| Jogador 3 | 217 | 0 | 0 | 217 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ 0.0000 (27 ações), BUY_XP: Δ 0.0000 (33 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0000 (99 ações), MOVE_BOARD: Δ 0.0000 (19 ações), PASS: Δ 0.0000 (24 ações), SELL: Δ 0.0000 (11 ações)
| Jogador 4 | 157 | 0 | 0 | 157 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ 0.0000 (22 ações), BUY_XP: Δ 0.0000 (21 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (68 ações), MOVE_BOARD: Δ 0.0000 (11 ações), PASS: Δ 0.0000 (27 ações), SELL: Δ 0.0000 (7 ações)
| Jogador 5 | 182 | 0 | 0 | 182 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ 0.0000 (40 ações), BUY_XP: Δ 0.0000 (22 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (62 ações), MOVE_BOARD: Δ 0.0000 (7 ações), PASS: Δ 0.0000 (26 ações), SELL: Δ 0.0000 (23 ações)
| Jogador 6 | 211 | 0 | 0 | 211 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ 0.0000 (51 ações), BUY_XP: Δ 0.0000 (31 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (64 ações), MOVE_BOARD: Δ 0.0000 (7 ações), PASS: Δ 0.0000 (22 ações), SELL: Δ 0.0000 (34 ações)
| Jogador 7 | 256 | 0 | 0 | 256 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ 0.0000 (55 ações), BUY_XP: Δ 0.0000 (33 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0000 (90 ações), MOVE_BOARD: Δ 0.0000 (19 ações), PASS: Δ 0.0000 (17 ações), SELL: Δ 0.0000 (38 ações)
| Jogador 8 | 249 | 0 | 0 | 249 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ 0.0000 (56 ações), BUY_XP: Δ 0.0000 (40 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (6 ações), MOVE_BENCH: Δ 0.0000 (78 ações), MOVE_BOARD: Δ 0.0000 (12 ações), PASS: Δ 0.0000 (13 ações), SELL: Δ 0.0000 (43 ações)

A pontuação é uma heurística para auditoria, não uma verdade absoluta. Compare-a com recompensas e resultados de combate; correlação não prova causalidade.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 1 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.004 | 0.000 |
| Jogador 1 | 1-3 | 4 | 2.000 | 2.000 | 0 → 0 | 1 → 1 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | 0.072 | 0.000 |
| Jogador 1 | 1-4 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 0 | 11% → 7% | 3 → 6 | 1 | 3 → 4 | -0.075 | 0.000 |
| Jogador 1 | 2-1 | 5 | 4.000 | 2.000 | 0 → 0 | 0 → 0 | 7% → 11% | 6 → 9 | 3 | 4 → 4 | 0.002 | 0.502 |
| Jogador 1 | 2-2 | 6 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 9 → 9 | 7 | 4 → 4 | 0.031 | 0.419 |
| Jogador 1 | 2-3 | 9 | 0.000 | 4.000 | 0 → 1 | 0 → 1 | 14% → 18% | 9 → 8 | 6 | 4 → 5 | 0.020 | -0.258 |
| Jogador 1 | 2-4 | 9 | 4.000 | -4.000 | 1 → 1 | 1 → 0 | 18% → 18% | 8 → 5 | 11 | 5 → 5 | 0.000 | 0.000 |
| Jogador 1 | 2-5 | 5 | 2.000 | 4.000 | 1 → 0 | 0 → 0 | 18% → 18% | 5 → 8 | 3 | 5 → 5 | -0.012 | 0.492 |
| Jogador 1 | 2-6 | 10 | 6.000 | -4.000 | 0 → 0 | 0 → 0 | 18% → 21% | 8 → 11 | 8 | 5 → 6 | -0.049 | 0.259 |
| Jogador 1 | 2-7 | 10 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 11 → 9 | 10 | 6 → 6 | -0.000 | 0.000 |
| Jogador 1 | 3-1 | 7 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 21% → 21% | 9 → 9 | 7 | 6 → 6 | 0.001 | 0.388 |
| Jogador 1 | 3-2 | 10 | 2.000 | 6.000 | 0 → 0 | 0 → 0 | 21% → 21% | 9 → 6 | 8 | 6 → 6 | -0.049 | -0.273 |
| Jogador 1 | 3-3 | 10 | -2.000 | -10.000 | 0 → 0 | 0 → 0 | 21% → 21% | 6 → 10 | 11 | 6 → 6 | 0.113 | -0.268 |
| Jogador 1 | 3-4 | 10 | 8.000 | -8.000 | 0 → 0 | 0 → 0 | 21% → 25% | 10 → 8 | 11 | 6 → 7 | 0.009 | 0.000 |
| Jogador 1 | 3-5 | 10 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 8 → 6 | 13 | 7 → 7 | -0.012 | 0.290 |
| Jogador 1 | 3-6 | 6 | -2.000 | 14.000 | 0 → 0 | 0 → 1 | 25% → 25% | 6 → 5 | 6 | 7 → 7 | -0.012 | -0.438 |
| Jogador 1 | 3-7 | 10 | 4.000 | -2.000 | 0 → 0 | 1 → 1 | 25% → 25% | 5 → 5 | 10 | 7 → 7 | 0.007 | 0.000 |
| Jogador 1 | 4-1 | 10 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 5 → 7 | 10 | 7 → 7 | -0.034 | -0.293 |
| Jogador 1 | 4-2 | 6 | 0.000 | 12.000 | 0 → 0 | 1 → 2 | 25% → 25% | 7 → 7 | 6 | 7 → 7 | 0.001 | -0.452 |
| Jogador 1 | 4-3 | 5 | -2.000 | 10.000 | 0 → 0 | 2 → 2 | 25% → 25% | 7 → 9 | 4 | 7 → 7 | -0.095 | 0.602 |
| Jogador 1 | 4-4 | 10 | 4.000 | -16.000 | 0 → 0 | 2 → 1 | 25% → 25% | 9 → 8 | 12 | 7 → 7 | 0.048 | 0.000 |
| Jogador 1 | 4-5 | 10 | -2.000 | 4.000 | 0 → 0 | 1 → 1 | 25% → 25% | 8 → 8 | 8 | 7 → 8 | 0.007 | -0.266 |
| Jogador 1 | 4-6 | 10 | 8.000 | -6.000 | 0 → 0 | 1 → 1 | 25% → 29% | 8 → 9 | 11 | 8 → 8 | -0.006 | 0.288 |
| Jogador 1 | 4-7 | 10 | 0.000 | -8.000 | 0 → 0 | 1 → 2 | 29% → 29% | 9 → 6 | 20 | 8 → 8 | 0.007 | 0.000 |
| Jogador 1 | 5-1 | 9 | 0.000 | 6.000 | 0 → 0 | 2 → 3 | 29% → 29% | 6 → 8 | 6 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 5-2 | 10 | 0.000 | -6.000 | 0 → 0 | 3 → 1 | 29% → 29% | 8 → 12 | 8 | 8 → 8 | 0.000 | -0.300 |
| Jogador 1 | 5-3 | 6 | -2.000 | 16.000 | 0 → 0 | 1 → 2 | 29% → 29% | 12 → 11 | 7 | 8 → 8 | -0.010 | 0.501 |
| Jogador 1 | 5-4 | 10 | 2.000 | -2.000 | 0 → 0 | 2 → 2 | 29% → 29% | 11 → 8 | 10 | 8 → 8 | -0.029 | 0.000 |
| Jogador 1 | 5-5 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 8 → 15 | 0 | 8 → 8 | -0.082 | 0.780 |
| Jogador 1 | 5-6 | 10 | -46.000 | -22.000 | 0 → 0 | 2 → 0 | 29% → 0% | 15 → 3 | 15 | 8 → 8 | 0.073 | -0.290 |
| Jogador 1 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 8 → 8 | 0.000 | 0.000 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 15, COMPOSITION_COMPATIBILITY: 14, IMMEDIATE_UPGRADE: 1, PAIR_POTENTIAL: 11; mudanças de composição: 0; posicionamento melhorou em 35 ações e piorou em 39.
- Jogador 1 — estado final: ouro 3, nível 8, vida 0.0, colocação 4.
| Jogador 2 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | -0.050 | 0.000 |
| Jogador 2 | 1-2 | 4 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | 0.005 | 0.000 |
| Jogador 2 | 1-3 | 4 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 7% → 11% | 3 → 4 | 2 | 3 → 3 | 0.102 | 0.000 |
| Jogador 2 | 1-4 | 4 | 0.000 | 0.000 | 0 → 1 | 1 → 0 | 11% → 7% | 4 → 7 | 1 | 3 → 4 | 0.017 | 0.000 |
| Jogador 2 | 2-1 | 7 | 10.000 | 0.000 | 1 → 1 | 0 → 0 | 7% → 14% | 7 → 7 | 5 | 4 → 4 | -0.026 | -0.332 |
| Jogador 2 | 2-2 | 6 | -4.000 | 10.000 | 1 → 1 | 0 → 1 | 14% → 14% | 7 → 6 | 7 | 4 → 4 | 0.000 | -0.395 |
| Jogador 2 | 2-3 | 7 | 6.000 | -2.000 | 1 → 1 | 1 → 1 | 14% → 18% | 6 → 6 | 6 | 4 → 5 | -0.005 | 0.352 |
| Jogador 2 | 2-4 | 4 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 18% → 18% | 6 → 8 | 3 | 5 → 5 | -0.054 | 0.000 |
| Jogador 2 | 2-5 | 5 | 0.000 | -4.000 | 1 → 1 | 1 → 0 | 18% → 18% | 8 → 7 | 8 | 5 → 5 | 0.012 | -0.496 |
| Jogador 2 | 2-6 | 5 | 6.000 | 0.000 | 1 → 1 | 0 → 0 | 18% → 21% | 7 → 6 | 7 | 5 → 6 | 0.005 | -0.507 |
| Jogador 2 | 2-7 | 10 | 8.000 | -6.000 | 1 → 1 | 0 → 0 | 21% → 21% | 6 → 7 | 10 | 6 → 6 | 0.020 | 0.000 |
| Jogador 2 | 3-1 | 7 | -2.000 | 8.000 | 1 → 1 | 0 → 0 | 21% → 21% | 7 → 6 | 8 | 6 → 6 | -0.008 | 0.402 |
| Jogador 2 | 3-2 | 10 | 2.000 | -12.000 | 1 → 1 | 0 → 0 | 21% → 21% | 6 → 10 | 9 | 6 → 6 | -0.002 | 0.293 |
| Jogador 2 | 3-3 | 8 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 21% → 21% | 10 → 9 | 15 | 6 → 6 | 0.000 | 0.367 |
| Jogador 2 | 3-4 | 10 | 4.000 | 4.000 | 1 → 1 | 0 → 0 | 21% → 25% | 9 → 7 | 12 | 6 → 7 | -0.005 | 0.000 |
| Jogador 2 | 3-5 | 4 | -4.000 | 4.000 | 1 → 1 | 0 → 0 | 25% → 25% | 7 → 12 | 0 | 7 → 7 | 0.000 | -0.679 |
| Jogador 2 | 3-6 | 10 | 6.000 | -2.000 | 1 → 1 | 0 → 0 | 25% → 25% | 12 → 8 | 15 | 7 → 7 | -0.006 | 0.281 |
| Jogador 2 | 3-7 | 10 | 4.000 | -2.000 | 1 → 1 | 0 → 1 | 25% → 25% | 8 → 8 | 11 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 4-1 | 10 | 0.000 | -4.000 | 1 → 1 | 1 → 1 | 25% → 25% | 8 → 7 | 12 | 7 → 7 | 0.014 | -0.270 |
| Jogador 2 | 4-2 | 10 | -2.000 | 0.000 | 1 → 1 | 1 → 2 | 25% → 25% | 7 → 6 | 11 | 7 → 7 | -0.010 | -0.276 |
| Jogador 2 | 4-3 | 10 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 6 → 8 | 10 | 7 → 7 | 0.037 | -0.285 |
| Jogador 2 | 4-4 | 10 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 25% → 25% | 8 → 7 | 13 | 7 → 7 | -0.044 | 0.000 |
| Jogador 2 | 4-5 | 10 | 4.000 | -6.000 | 1 → 1 | 2 → 1 | 25% → 25% | 7 → 9 | 9 | 7 → 8 | 0.036 | 0.283 |
| Jogador 2 | 4-6 | 6 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 9 → 6 | 9 | 8 → 8 | 0.000 | -0.452 |
| Jogador 2 | 4-7 | 10 | 6.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 29% | 6 → 8 | 3 | 8 → 8 | -0.003 | 0.000 |
| Jogador 2 | 5-1 | 10 | -52.000 | 0.000 | 1 → 0 | 1 → 0 | 29% → 0% | 8 → 3 | 8 | 8 → 8 | 0.016 | -0.275 |
| Jogador 2 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 8 → 8 | 0.000 | 0.000 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 12, COMPOSITION_COMPATIBILITY: 22, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 4; mudanças de composição: 1; posicionamento melhorou em 23 ações e piorou em 26.
- Jogador 2 — estado final: ouro 3, nível 8, vida 0.0, colocação 7.
| Jogador 3 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 3 | 1-2 | 4 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | 0.005 | 0.000 |
| Jogador 3 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 7% → 7% | 3 → 3 | 3 | 3 → 3 | -0.010 | 0.000 |
| Jogador 3 | 1-4 | 4 | 4.000 | -2.000 | 0 → 1 | 0 → 1 | 7% → 11% | 3 → 6 | 1 | 3 → 4 | 0.102 | 0.000 |
| Jogador 3 | 2-1 | 5 | 2.000 | 2.000 | 1 → 1 | 1 → 1 | 11% → 14% | 6 → 5 | 6 | 4 → 4 | -0.030 | -0.462 |
| Jogador 3 | 2-2 | 5 | 4.000 | -4.000 | 1 → 1 | 1 → 1 | 14% → 18% | 5 → 7 | 4 | 4 → 5 | 0.020 | 0.537 |
| Jogador 3 | 2-3 | 5 | 2.000 | 8.000 | 1 → 1 | 1 → 1 | 18% → 18% | 7 → 9 | 5 | 5 → 5 | 0.000 | 0.502 |
| Jogador 3 | 2-4 | 9 | 0.000 | 2.000 | 1 → 0 | 1 → 1 | 18% → 18% | 9 → 7 | 11 | 5 → 5 | 0.001 | 0.000 |
| Jogador 3 | 2-5 | 6 | -2.000 | 8.000 | 0 → 0 | 1 → 1 | 18% → 18% | 7 → 5 | 7 | 5 → 6 | -0.011 | -0.413 |
| Jogador 3 | 2-6 | 4 | 6.000 | -2.000 | 0 → 0 | 1 → 1 | 18% → 21% | 5 → 9 | 2 | 6 → 6 | 0.027 | 0.676 |
| Jogador 3 | 2-7 | 7 | 0.000 | -4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 9 → 8 | 8 | 6 → 6 | -0.088 | 0.000 |
| Jogador 3 | 3-1 | 10 | 2.000 | 2.000 | 0 → 0 | 1 → 2 | 21% → 21% | 8 → 7 | 7 | 6 → 6 | 0.045 | -0.263 |
| Jogador 3 | 3-2 | 10 | 0.000 | 2.000 | 0 → 0 | 2 → 3 | 21% → 21% | 7 → 8 | 7 | 6 → 6 | 0.008 | 0.290 |
| Jogador 3 | 3-3 | 7 | 0.000 | 2.000 | 0 → 0 | 3 → 3 | 21% → 21% | 8 → 8 | 7 | 6 → 6 | -0.016 | -0.382 |
| Jogador 3 | 3-4 | 9 | 6.000 | -6.000 | 0 → 0 | 3 → 3 | 21% → 25% | 8 → 5 | 8 | 6 → 7 | 0.044 | 0.000 |
| Jogador 3 | 3-5 | 6 | 0.000 | 10.000 | 0 → 0 | 3 → 3 | 25% → 25% | 5 → 6 | 5 | 7 → 7 | -0.194 | 0.502 |
| Jogador 3 | 3-6 | 10 | 2.000 | 4.000 | 0 → 0 | 3 → 4 | 25% → 25% | 6 → 8 | 3 | 7 → 7 | 0.069 | -0.281 |
| Jogador 3 | 3-7 | 10 | -2.000 | 2.000 | 0 → 0 | 4 → 4 | 25% → 25% | 8 → 5 | 8 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 4-1 | 7 | 0.000 | -4.000 | 0 → 0 | 4 → 4 | 25% → 25% | 5 → 9 | 4 | 7 → 7 | 0.055 | 0.409 |
| Jogador 3 | 4-2 | 8 | 0.000 | 8.000 | 0 → 0 | 4 → 4 | 25% → 25% | 9 → 8 | 8 | 7 → 7 | 0.018 | 0.367 |
| Jogador 3 | 4-3 | 8 | 0.000 | -6.000 | 0 → 0 | 4 → 3 | 25% → 25% | 8 → 10 | 8 | 7 → 7 | 0.000 | 0.376 |
| Jogador 3 | 4-4 | 8 | 0.000 | -6.000 | 0 → 0 | 3 → 2 | 25% → 25% | 10 → 11 | 8 | 7 → 7 | -0.043 | 0.000 |
| Jogador 3 | 4-5 | 10 | 8.000 | -2.000 | 0 → 0 | 2 → 3 | 25% → 29% | 11 → 7 | 11 | 7 → 8 | 0.042 | 0.304 |
| Jogador 3 | 4-6 | 7 | -2.000 | 2.000 | 0 → 0 | 3 → 3 | 29% → 29% | 7 → 11 | 4 | 8 → 8 | 0.000 | 0.405 |
| Jogador 3 | 4-7 | 10 | 2.000 | 0.000 | 0 → 0 | 3 → 3 | 29% → 29% | 11 → 13 | 8 | 8 → 8 | -0.014 | 0.000 |
| Jogador 3 | 5-1 | 7 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 29% → 29% | 13 → 23 | 0 | 8 → 8 | 0.000 | 0.422 |
| Jogador 3 | 5-2 | 10 | -2.000 | 10.000 | 0 → 0 | 3 → 3 | 29% → 29% | 23 → 12 | 20 | 8 → 8 | 0.033 | 0.296 |
| Jogador 3 | 5-3 | 10 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 29% → 29% | 12 → 5 | 12 | 8 → 8 | -0.002 | -0.285 |
| Jogador 3 | 5-4 | 10 | 0.000 | 8.000 | 0 → 0 | 3 → 3 | 29% → 29% | 5 → 6 | 4 | 8 → 8 | -0.026 | 0.000 |
| Jogador 3 | 5-5 | 10 | 2.000 | 6.000 | 0 → 0 | 3 → 4 | 29% → 29% | 6 → 8 | 4 | 8 → 8 | 0.024 | -0.280 |
| Jogador 3 | 5-6 | 10 | 0.000 | -6.000 | 0 → 0 | 4 → 4 | 29% → 29% | 8 → 9 | 11 | 8 → 8 | -0.040 | -0.285 |
| Jogador 3 | 5-7 | 7 | 0.000 | 6.000 | 0 → 0 | 4 → 4 | 29% → 29% | 9 → 8 | 7 | 8 → 8 | 0.052 | 0.000 |
| Jogador 3 | 6-1 | 7 | -36.000 | -44.000 | 0 → 0 | 4 → 0 | 29% → 0% | 8 → 8 | 0 | 8 → 8 | -0.077 | -0.414 |
| Jogador 3 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 8 → 8 | 0 | 8 → 8 | 0.000 | 0.000 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 2, COMPOSITION_COMPATIBILITY: 12, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 11; mudanças de composição: 0; posicionamento melhorou em 42 ações e piorou em 47.
- Jogador 3 — estado final: ouro 8, nível 8, vida 0.0, colocação 3.
| Jogador 4 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 4 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.004 | 0.000 |
| Jogador 4 | 1-3 | 4 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.005 | 0.000 |
| Jogador 4 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 7 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 4 | 2-1 | 5 | -2.000 | 6.000 | 0 → 0 | 0 → 0 | 11% → 11% | 7 → 8 | 4 | 4 → 4 | -0.004 | -0.474 |
| Jogador 4 | 2-2 | 5 | 6.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 14% | 8 → 9 | 5 | 4 → 4 | 0.036 | 0.512 |
| Jogador 4 | 2-3 | 9 | 8.000 | -8.000 | 0 → 1 | 0 → 0 | 14% → 18% | 9 → 8 | 8 | 4 → 5 | -0.055 | 0.287 |
| Jogador 4 | 2-4 | 7 | 0.000 | 12.000 | 1 → 1 | 0 → 0 | 18% → 18% | 8 → 8 | 6 | 5 → 5 | 0.000 | 0.000 |
| Jogador 4 | 2-5 | 9 | -4.000 | -2.000 | 1 → 0 | 0 → 1 | 18% → 18% | 8 → 13 | 7 | 5 → 5 | 0.007 | -0.287 |
| Jogador 4 | 2-6 | 9 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 21% | 13 → 8 | 11 | 5 → 6 | -0.001 | -0.270 |
| Jogador 4 | 2-7 | 9 | 2.000 | 4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 8 → 7 | 7 | 6 → 6 | 0.062 | 0.000 |
| Jogador 4 | 3-1 | 10 | 2.000 | -2.000 | 0 → 0 | 1 → 1 | 21% → 21% | 7 → 9 | 6 | 6 → 6 | -0.006 | 0.281 |
| Jogador 4 | 3-2 | 10 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 9 → 8 | 9 | 6 → 6 | 0.003 | 0.298 |
| Jogador 4 | 3-3 | 10 | -2.000 | 4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 8 → 8 | 7 | 6 → 6 | 0.001 | -0.276 |
| Jogador 4 | 3-4 | 10 | 8.000 | -8.000 | 0 → 0 | 1 → 1 | 21% → 25% | 8 → 5 | 11 | 6 → 7 | 0.015 | 0.000 |
| Jogador 4 | 3-5 | 10 | -2.000 | 8.000 | 0 → 0 | 1 → 2 | 25% → 25% | 5 → 8 | 3 | 7 → 7 | -0.066 | -0.273 |
| Jogador 4 | 3-6 | 5 | -4.000 | 6.000 | 0 → 0 | 2 → 3 | 25% → 25% | 8 → 13 | 1 | 7 → 7 | -0.048 | -0.560 |
| Jogador 4 | 3-7 | 10 | 6.000 | 0.000 | 0 → 1 | 3 → 2 | 25% → 25% | 13 → 9 | 10 | 7 → 7 | 0.024 | 0.000 |
| Jogador 4 | 4-1 | 10 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 9 → 7 | 11 | 7 → 7 | 0.080 | -0.271 |
| Jogador 4 | 4-2 | 4 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 7 → 14 | 0 | 7 → 7 | -0.087 | -0.691 |
| Jogador 4 | 4-3 | 7 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 25% → 25% | 14 → 11 | 11 | 7 → 7 | 0.000 | -0.407 |
| Jogador 4 | 4-4 | 6 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 25% → 25% | 11 → 11 | 8 | 7 → 7 | -0.063 | 0.000 |
| Jogador 4 | 4-5 | 10 | -32.000 | -32.000 | 1 → 0 | 3 → 0 | 25% → 0% | 11 → 3 | 8 | 7 → 7 | 0.043 | -0.288 |
| Jogador 4 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 5-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 3 → 3 | 0 | 7 → 7 | 0.000 | 0.000 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 3, COMPOSITION_COMPATIBILITY: 9, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 8; mudanças de composição: 0; posicionamento melhorou em 33 ações e piorou em 31.
- Jogador 4 — estado final: ouro 3, nível 7, vida 0.0, colocação 8.
| Jogador 5 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 5 | 1-2 | 4 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.007 | 0.000 |
| Jogador 5 | 1-3 | 4 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | 0.006 | 0.000 |
| Jogador 5 | 1-4 | 4 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.000 | 0.000 |
| Jogador 5 | 2-1 | 4 | 2.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 14% | 5 → 8 | 3 | 4 → 4 | 0.000 | 0.616 |
| Jogador 5 | 2-2 | 6 | 4.000 | 6.000 | 0 → 0 | 0 → 0 | 14% → 14% | 8 → 10 | 6 | 4 → 4 | 0.002 | 0.440 |
| Jogador 5 | 2-3 | 10 | 8.000 | -12.000 | 0 → 0 | 0 → 0 | 14% → 18% | 10 → 9 | 9 | 4 → 5 | -0.044 | -0.237 |
| Jogador 5 | 2-4 | 6 | 0.000 | 10.000 | 0 → 0 | 0 → 0 | 18% → 18% | 9 → 9 | 5 | 5 → 5 | 0.009 | 0.000 |
| Jogador 5 | 2-5 | 4 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 18% → 18% | 9 → 8 | 7 | 5 → 5 | 0.000 | 0.659 |
| Jogador 5 | 2-6 | 10 | 6.000 | -10.000 | 0 → 0 | 0 → 0 | 18% → 21% | 8 → 7 | 10 | 5 → 6 | 0.020 | -0.264 |
| Jogador 5 | 2-7 | 10 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 7 → 8 | 8 | 6 → 6 | 0.045 | 0.000 |
| Jogador 5 | 3-1 | 6 | 0.000 | 10.000 | 0 → 0 | 0 → 2 | 21% → 21% | 8 → 9 | 5 | 6 → 6 | -0.029 | -0.463 |
| Jogador 5 | 3-2 | 10 | 2.000 | -16.000 | 0 → 1 | 2 → 0 | 21% → 18% | 9 → 6 | 17 | 6 → 6 | 0.027 | -0.281 |
| Jogador 5 | 3-3 | 10 | 8.000 | 0.000 | 1 → 1 | 0 → 0 | 18% → 21% | 6 → 8 | 8 | 6 → 6 | 0.029 | 0.285 |
| Jogador 5 | 3-4 | 6 | -2.000 | 6.000 | 1 → 1 | 0 → 0 | 21% → 21% | 8 → 7 | 6 | 6 → 6 | -0.082 | 0.000 |
| Jogador 5 | 3-5 | 5 | 6.000 | 0.000 | 1 → 1 | 0 → 0 | 21% → 25% | 7 → 5 | 7 | 6 → 7 | -0.007 | -0.535 |
| Jogador 5 | 3-6 | 7 | 2.000 | 6.000 | 1 → 1 | 0 → 1 | 25% → 25% | 5 → 7 | 4 | 7 → 7 | -0.100 | 0.400 |
| Jogador 5 | 3-7 | 10 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 7 → 8 | 7 | 7 → 7 | 0.010 | 0.000 |
| Jogador 5 | 4-1 | 10 | 0.000 | 0.000 | 1 → 1 | 1 → 2 | 25% → 25% | 8 → 5 | 17 | 7 → 7 | 0.060 | -0.271 |
| Jogador 5 | 4-2 | 10 | -2.000 | 6.000 | 1 → 1 | 2 → 1 | 25% → 25% | 5 → 6 | 5 | 7 → 7 | -0.068 | 0.293 |
| Jogador 5 | 4-3 | 10 | 0.000 | -6.000 | 1 → 1 | 1 → 1 | 25% → 25% | 6 → 8 | 17 | 7 → 7 | 0.021 | -0.285 |
| Jogador 5 | 4-4 | 10 | 2.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 8 → 8 | 7 | 7 → 7 | -0.015 | 0.000 |
| Jogador 5 | 4-5 | 10 | 0.000 | -12.000 | 1 → 1 | 1 → 0 | 25% → 25% | 8 → 8 | 12 | 7 → 7 | 0.026 | -0.266 |
| Jogador 5 | 4-6 | 10 | 8.000 | 0.000 | 1 → 1 | 0 → 0 | 25% → 29% | 8 → 6 | 11 | 7 → 8 | -0.042 | -0.283 |
| Jogador 5 | 4-7 | 8 | 0.000 | 12.000 | 1 → 1 | 0 → 0 | 29% → 29% | 6 → 6 | 6 | 8 → 8 | 0.007 | 0.000 |
| Jogador 5 | 5-1 | 8 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 29% → 29% | 6 → 9 | 3 | 8 → 8 | 0.029 | 0.363 |
| Jogador 5 | 5-2 | 7 | -56.000 | -18.000 | 1 → 0 | 0 → 0 | 29% → 0% | 9 → 2 | 7 | 8 → 8 | 0.078 | -0.400 |
| Jogador 5 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 2 → 2 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 5 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 2 → 2 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 5 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 2 → 2 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 5 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 2 → 2 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 5 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 2 → 2 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 5 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 2 → 2 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 5 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 2 → 2 | 0 | 8 → 8 | 0.000 | 0.000 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 9, COMPOSITION_COMPATIBILITY: 20, IMMEDIATE_UPGRADE: 3, PAIR_POTENTIAL: 8; mudanças de composição: 0; posicionamento melhorou em 33 ações e piorou em 35.
- Jogador 5 — estado final: ouro 2, nível 8, vida 0.0, colocação 6.
| Jogador 6 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | -0.050 | 0.000 |
| Jogador 6 | 1-2 | 4 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.018 | 0.000 |
| Jogador 6 | 1-3 | 4 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.003 | 0.000 |
| Jogador 6 | 1-4 | 4 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.000 | 0.000 |
| Jogador 6 | 2-1 | 5 | 2.000 | 6.000 | 0 → 0 | 0 → 1 | 11% → 14% | 5 → 7 | 4 | 4 → 4 | 0.014 | 0.486 |
| Jogador 6 | 2-2 | 5 | 0.000 | 4.000 | 0 → 0 | 1 → 0 | 14% → 14% | 7 → 6 | 7 | 4 → 4 | 0.000 | -0.484 |
| Jogador 6 | 2-3 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 18% | 6 → 6 | 6 | 4 → 5 | 0.030 | 0.476 |
| Jogador 6 | 2-4 | 6 | -2.000 | 10.000 | 0 → 0 | 0 → 1 | 18% → 18% | 6 → 7 | 4 | 5 → 5 | -0.039 | 0.000 |
| Jogador 6 | 2-5 | 9 | 4.000 | -6.000 | 0 → 0 | 1 → 0 | 18% → 18% | 7 → 5 | 10 | 5 → 5 | -0.058 | -0.258 |
| Jogador 6 | 2-6 | 3 | 0.000 | 6.000 | 0 → 0 | 0 → 1 | 18% → 18% | 5 → 8 | 3 | 5 → 5 | -0.020 | -0.879 |
| Jogador 6 | 2-7 | 8 | 2.000 | 4.000 | 0 → 0 | 1 → 1 | 18% → 18% | 8 → 11 | 3 | 5 → 6 | -0.026 | 0.000 |
| Jogador 6 | 3-1 | 10 | 6.000 | 0.000 | 0 → 0 | 1 → 0 | 18% → 21% | 11 → 10 | 13 | 6 → 6 | 0.026 | -0.263 |
| Jogador 6 | 3-2 | 10 | 2.000 | -12.000 | 0 → 0 | 0 → 0 | 21% → 21% | 10 → 9 | 15 | 6 → 6 | 0.069 | -0.273 |
| Jogador 6 | 3-3 | 10 | 2.000 | -8.000 | 0 → 0 | 0 → 0 | 21% → 21% | 9 → 6 | 17 | 6 → 6 | 0.000 | 0.286 |
| Jogador 6 | 3-4 | 10 | -2.000 | 2.000 | 0 → 0 | 0 → 0 | 21% → 21% | 6 → 7 | 13 | 6 → 7 | -0.008 | 0.000 |
| Jogador 6 | 3-5 | 8 | 8.000 | 4.000 | 0 → 0 | 0 → 0 | 21% → 25% | 7 → 8 | 6 | 7 → 7 | -0.078 | 0.356 |
| Jogador 6 | 3-6 | 10 | 0.000 | -6.000 | 0 → 0 | 0 → 0 | 25% → 25% | 8 → 9 | 17 | 7 → 7 | 0.000 | 0.298 |
| Jogador 6 | 3-7 | 10 | 2.000 | 10.000 | 0 → 0 | 0 → 0 | 25% → 25% | 9 → 9 | 9 | 7 → 7 | 0.117 | 0.000 |
| Jogador 6 | 4-1 | 10 | 4.000 | -16.000 | 0 → 0 | 0 → 0 | 25% → 25% | 9 → 10 | 15 | 7 → 7 | -0.047 | 0.309 |
| Jogador 6 | 4-2 | 10 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 10 → 10 | 14 | 7 → 7 | 0.038 | 0.301 |
| Jogador 6 | 4-3 | 8 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 10 → 11 | 14 | 7 → 7 | 0.000 | 0.376 |
| Jogador 6 | 4-4 | 10 | 6.000 | 6.000 | 0 → 0 | 0 → 0 | 25% → 29% | 11 → 9 | 12 | 7 → 8 | -0.005 | 0.000 |
| Jogador 6 | 4-5 | 9 | -6.000 | 4.000 | 0 → 0 | 0 → 1 | 29% → 29% | 9 → 7 | 10 | 8 → 8 | -0.066 | -0.300 |
| Jogador 6 | 4-6 | 10 | 2.000 | -10.000 | 0 → 0 | 1 → 2 | 29% → 29% | 7 → 9 | 15 | 8 → 8 | -0.005 | -0.266 |
| Jogador 6 | 4-7 | 6 | 0.000 | 16.000 | 0 → 0 | 2 → 2 | 29% → 29% | 9 → 7 | 8 | 8 → 8 | -0.008 | 0.000 |
| Jogador 6 | 5-1 | 10 | -2.000 | -16.000 | 0 → 0 | 2 → 2 | 29% → 29% | 7 → 18 | 11 | 8 → 8 | 0.010 | -0.280 |
| Jogador 6 | 5-2 | 10 | 8.000 | 0.000 | 0 → 1 | 2 → 1 | 29% → 29% | 18 → 18 | 7 | 8 → 8 | -0.024 | -0.285 |
| Jogador 6 | 5-3 | 8 | -2.000 | 16.000 | 1 → 1 | 1 → 1 | 29% → 29% | 18 → 18 | 7 | 8 → 8 | 0.000 | 0.000 |
| Jogador 6 | 5-4 | 10 | 2.000 | 6.000 | 1 → 1 | 1 → 2 | 29% → 29% | 18 → 8 | 16 | 8 → 8 | 0.000 | 0.000 |
| Jogador 6 | 5-5 | 10 | -52.000 | -22.000 | 1 → 0 | 2 → 0 | 29% → 0% | 8 → 2 | 6 | 8 → 8 | 0.056 | -0.295 |
| Jogador 6 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 2 → 2 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 6 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 2 → 2 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 6 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 2 → 2 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 6 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 2 → 2 | 0 | 8 → 8 | 0.000 | 0.000 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 14, COMPOSITION_COMPATIBILITY: 20, IMMEDIATE_UPGRADE: 4, PAIR_POTENTIAL: 13; mudanças de composição: 2; posicionamento melhorou em 28 ações e piorou em 35.
- Jogador 6 — estado final: ouro 2, nível 8, vida 0.0, colocação 5.
| Jogador 7 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 7 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.014 | 0.000 |
| Jogador 7 | 1-3 | 4 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 7% → 11% | 2 → 4 | 1 | 3 → 3 | -0.000 | 0.000 |
| Jogador 7 | 1-4 | 6 | 2.000 | -2.000 | 0 → 0 | 1 → 1 | 11% → 14% | 4 → 4 | 5 | 3 → 4 | -0.005 | 0.000 |
| Jogador 7 | 2-1 | 7 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 4 → 6 | 8 | 4 → 5 | 0.000 | 0.373 |
| Jogador 7 | 2-2 | 7 | 8.000 | 2.000 | 0 → 1 | 1 → 0 | 14% → 14% | 6 → 5 | 6 | 5 → 5 | -0.031 | -0.361 |
| Jogador 7 | 2-3 | 6 | 2.000 | 8.000 | 1 → 1 | 0 → 0 | 14% → 18% | 5 → 6 | 5 | 5 → 5 | 0.073 | -0.377 |
| Jogador 7 | 2-4 | 9 | 6.000 | 2.000 | 1 → 1 | 0 → 0 | 18% → 18% | 6 → 8 | 4 | 5 → 5 | -0.082 | 0.000 |
| Jogador 7 | 2-5 | 10 | 0.000 | 2.000 | 1 → 1 | 0 → 0 | 18% → 18% | 8 → 9 | 8 | 5 → 5 | 0.057 | 0.275 |
| Jogador 7 | 2-6 | 10 | 6.000 | -6.000 | 1 → 1 | 0 → 0 | 18% → 21% | 9 → 8 | 13 | 5 → 6 | -0.013 | 0.281 |
| Jogador 7 | 2-7 | 10 | -4.000 | 8.000 | 1 → 1 | 0 → 0 | 21% → 21% | 8 → 8 | 9 | 6 → 6 | 0.017 | 0.000 |
| Jogador 7 | 3-1 | 10 | 4.000 | -4.000 | 1 → 1 | 0 → 0 | 21% → 21% | 8 → 9 | 7 | 6 → 6 | 0.015 | -0.254 |
| Jogador 7 | 3-2 | 10 | 4.000 | -12.000 | 1 → 1 | 0 → 0 | 21% → 21% | 9 → 10 | 15 | 6 → 6 | 0.009 | 0.290 |
| Jogador 7 | 3-3 | 10 | -2.000 | 0.000 | 1 → 1 | 0 → 1 | 21% → 21% | 10 → 8 | 13 | 6 → 6 | -0.040 | -0.263 |
| Jogador 7 | 3-4 | 10 | 6.000 | 0.000 | 1 → 1 | 1 → 1 | 21% → 25% | 8 → 6 | 10 | 6 → 7 | 0.071 | 0.000 |
| Jogador 7 | 3-5 | 10 | 2.000 | 0.000 | 1 → 2 | 1 → 0 | 25% → 21% | 6 → 8 | 8 | 7 → 7 | -0.072 | -0.285 |
| Jogador 7 | 3-6 | 7 | 8.000 | 8.000 | 2 → 2 | 0 → 1 | 21% → 25% | 8 → 6 | 8 | 7 → 7 | 0.030 | -0.376 |
| Jogador 7 | 3-7 | 8 | 0.000 | 8.000 | 2 → 2 | 1 → 1 | 25% → 25% | 6 → 8 | 6 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 4-1 | 8 | 4.000 | -4.000 | 2 → 2 | 1 → 1 | 25% → 25% | 8 → 10 | 7 | 7 → 7 | -0.020 | 0.360 |
| Jogador 7 | 4-2 | 10 | 0.000 | -12.000 | 2 → 2 | 1 → 1 | 25% → 25% | 10 → 5 | 19 | 7 → 7 | 0.010 | -0.285 |
| Jogador 7 | 4-3 | 8 | 0.000 | 0.000 | 2 → 2 | 1 → 0 | 25% → 25% | 5 → 7 | 8 | 7 → 7 | -0.038 | -0.339 |
| Jogador 7 | 4-4 | 10 | 0.000 | 0.000 | 2 → 2 | 0 → 0 | 25% → 25% | 7 → 9 | 10 | 7 → 7 | -0.001 | 0.000 |
| Jogador 7 | 4-5 | 10 | 0.000 | 0.000 | 2 → 2 | 0 → 0 | 25% → 25% | 9 → 7 | 15 | 7 → 8 | -0.004 | 0.283 |
| Jogador 7 | 4-6 | 10 | 8.000 | 0.000 | 2 → 2 | 0 → 0 | 25% → 29% | 7 → 8 | 6 | 8 → 8 | -0.003 | 0.000 |
| Jogador 7 | 4-7 | 10 | -4.000 | 0.000 | 2 → 1 | 0 → 1 | 29% → 29% | 8 → 5 | 19 | 8 → 8 | 0.008 | 0.000 |
| Jogador 7 | 5-1 | 7 | 2.000 | 8.000 | 1 → 1 | 1 → 1 | 29% → 29% | 5 → 7 | 5 | 8 → 8 | -0.049 | 0.417 |
| Jogador 7 | 5-2 | 10 | 0.000 | 8.000 | 1 → 1 | 1 → 1 | 29% → 29% | 7 → 10 | 7 | 8 → 8 | 0.034 | 0.302 |
| Jogador 7 | 5-3 | 7 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 29% → 29% | 10 → 8 | 7 | 8 → 8 | -0.061 | -0.393 |
| Jogador 7 | 5-4 | 10 | 0.000 | 0.000 | 1 → 1 | 1 → 2 | 29% → 29% | 8 → 5 | 11 | 8 → 8 | 0.008 | 0.000 |
| Jogador 7 | 5-5 | 10 | -2.000 | -4.000 | 1 → 1 | 2 → 1 | 29% → 29% | 5 → 10 | 8 | 8 → 8 | -0.008 | 0.297 |
| Jogador 7 | 5-6 | 10 | 2.000 | -2.000 | 1 → 1 | 1 → 1 | 29% → 29% | 10 → 9 | 12 | 8 → 8 | 0.043 | 0.304 |
| Jogador 7 | 5-7 | 8 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 29% → 29% | 9 → 11 | 8 | 8 → 8 | -0.053 | 0.000 |
| Jogador 7 | 6-1 | 10 | 0.000 | 0.000 | 1 → 1 | 1 → 0 | 29% → 29% | 11 → 9 | 8 | 8 → 8 | 0.030 | 0.000 |
| Jogador 7 | 6-2 | 10 | -58.000 | -16.000 | 1 → 0 | 0 → 0 | 29% → 0% | 9 → 2 | 9 | 8 → 9 | 0.056 | -0.275 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 17, COMPOSITION_COMPATIBILITY: 24, IMMEDIATE_UPGRADE: 4, PAIR_POTENTIAL: 10; mudanças de composição: 1; posicionamento melhorou em 44 ações e piorou em 48.
- Jogador 7 — estado final: ouro 2, nível 9, vida 0.0, colocação 2.
| Jogador 8 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 8 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.004 | 0.000 |
| Jogador 8 | 1-3 | 4 | 2.000 | 0.000 | 0 → 0 | 1 → 1 | 7% → 11% | 2 → 4 | 1 | 3 → 3 | 0.087 | 0.000 |
| Jogador 8 | 1-4 | 4 | 2.000 | -2.000 | 0 → 0 | 1 → 1 | 11% → 14% | 4 → 4 | 4 | 3 → 4 | -0.022 | 0.000 |
| Jogador 8 | 2-1 | 5 | 0.000 | 2.000 | 0 → 1 | 1 → 0 | 14% → 11% | 4 → 7 | 2 | 4 → 4 | 0.018 | -0.494 |
| Jogador 8 | 2-2 | 8 | 8.000 | -2.000 | 1 → 1 | 0 → 0 | 11% → 18% | 7 → 6 | 7 | 4 → 5 | 0.008 | -0.310 |
| Jogador 8 | 2-3 | 6 | 4.000 | 6.000 | 1 → 1 | 0 → 0 | 18% → 18% | 6 → 7 | 5 | 5 → 5 | -0.118 | -0.405 |
| Jogador 8 | 2-4 | 5 | -4.000 | 10.000 | 1 → 1 | 0 → 0 | 18% → 18% | 7 → 6 | 7 | 5 → 5 | 0.106 | 0.000 |
| Jogador 8 | 2-5 | 4 | 4.000 | -4.000 | 1 → 1 | 0 → 0 | 18% → 18% | 6 → 12 | 0 | 5 → 5 | -0.124 | 0.659 |
| Jogador 8 | 2-6 | 10 | 6.000 | -2.000 | 1 → 1 | 0 → 0 | 18% → 21% | 12 → 9 | 11 | 5 → 6 | 0.089 | 0.280 |
| Jogador 8 | 2-7 | 10 | 0.000 | -10.000 | 1 → 1 | 0 → 0 | 21% → 21% | 9 → 12 | 14 | 6 → 6 | -0.005 | 0.000 |
| Jogador 8 | 3-1 | 7 | -2.000 | 14.000 | 1 → 1 | 0 → 0 | 21% → 21% | 12 → 9 | 10 | 6 → 6 | -0.172 | 0.421 |
| Jogador 8 | 3-2 | 10 | 2.000 | 6.000 | 1 → 1 | 0 → 0 | 21% → 21% | 9 → 6 | 9 | 6 → 6 | 0.034 | -0.276 |
| Jogador 8 | 3-3 | 10 | 2.000 | -6.000 | 1 → 1 | 0 → 0 | 21% → 21% | 6 → 10 | 5 | 6 → 6 | 0.080 | 0.281 |
| Jogador 8 | 3-4 | 10 | 8.000 | -14.000 | 1 → 1 | 0 → 0 | 21% → 25% | 10 → 6 | 15 | 6 → 7 | 0.037 | 0.000 |
| Jogador 8 | 3-5 | 9 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 25% → 25% | 6 → 9 | 12 | 7 → 7 | 0.000 | 0.320 |
| Jogador 8 | 3-6 | 10 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 25% → 25% | 9 → 13 | 8 | 7 → 7 | -0.036 | 0.296 |
| Jogador 8 | 3-7 | 10 | -2.000 | -6.000 | 1 → 1 | 0 → 0 | 25% → 25% | 13 → 7 | 19 | 7 → 7 | 0.026 | 0.000 |
| Jogador 8 | 4-1 | 10 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 25% → 25% | 7 → 11 | 9 | 7 → 7 | -0.102 | 0.288 |
| Jogador 8 | 4-2 | 7 | 2.000 | 6.000 | 1 → 1 | 0 → 0 | 25% → 25% | 11 → 11 | 8 | 7 → 7 | 0.140 | 0.412 |
| Jogador 8 | 4-3 | 10 | 0.000 | -12.000 | 1 → 1 | 0 → 0 | 25% → 25% | 11 → 14 | 15 | 7 → 8 | -0.035 | 0.288 |
| Jogador 8 | 4-4 | 10 | 8.000 | 4.000 | 1 → 0 | 0 → 0 | 25% → 29% | 14 → 9 | 16 | 8 → 8 | -0.002 | 0.000 |
| Jogador 8 | 4-5 | 10 | 2.000 | 4.000 | 0 → 0 | 0 → 0 | 29% → 29% | 9 → 11 | 11 | 8 → 8 | -0.009 | 0.286 |
| Jogador 8 | 4-6 | 10 | 0.000 | -8.000 | 0 → 0 | 0 → 0 | 29% → 29% | 11 → 12 | 19 | 8 → 8 | 0.000 | 0.299 |
| Jogador 8 | 4-7 | 10 | 2.000 | 14.000 | 0 → 0 | 0 → 1 | 29% → 29% | 12 → 8 | 12 | 8 → 8 | -0.019 | 0.000 |
| Jogador 8 | 5-1 | 10 | -2.000 | 4.000 | 0 → 0 | 1 → 1 | 29% → 29% | 8 → 12 | 13 | 8 → 8 | -0.030 | -0.275 |
| Jogador 8 | 5-2 | 10 | 4.000 | -10.000 | 0 → 0 | 1 → 1 | 29% → 29% | 12 → 9 | 15 | 8 → 8 | 0.008 | 0.320 |
| Jogador 8 | 5-3 | 10 | 0.000 | -2.000 | 0 → 0 | 1 → 1 | 29% → 29% | 9 → 9 | 11 | 8 → 8 | -0.002 | 0.292 |
| Jogador 8 | 5-4 | 10 | 6.000 | -6.000 | 0 → 0 | 1 → 1 | 29% → 32% | 9 → 7 | 11 | 8 → 9 | 0.001 | 0.000 |
| Jogador 8 | 5-5 | 10 | 0.000 | 0.000 | 0 → 1 | 1 → 0 | 32% → 29% | 7 → 9 | 11 | 9 → 9 | -0.059 | 0.000 |
| Jogador 8 | 5-6 | 10 | 6.000 | 0.000 | 1 → 1 | 0 → 1 | 29% → 32% | 9 → 9 | 11 | 9 → 9 | 0.051 | 0.309 |
| Jogador 8 | 5-7 | 6 | 4.000 | 14.000 | 1 → 1 | 1 → 1 | 32% → 32% | 9 → 6 | 9 | 9 → 9 | 0.096 | 0.000 |
| Jogador 8 | 6-1 | 10 | 0.000 | -6.000 | 1 → 1 | 1 → 0 | 32% → 32% | 6 → 12 | 8 | 9 → 9 | 0.001 | 0.312 |
| Jogador 8 | 6-2 | 10 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 32% → 32% | 12 → 5 | 12 | 9 → 9 | -0.001 | 0.295 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 24, COMPOSITION_COMPATIBILITY: 20, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 10; mudanças de composição: 0; posicionamento melhorou em 42 ações e piorou em 37.
- Jogador 8 — estado final: ouro 5, nível 9, vida 55.0, colocação 1.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Revertidas ≤1 ação | ≤2 ações | ≤4 ações | Ouro perdido | Upgrades | Vendas core/par | Valor médio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 41 | 29 | 5 | 6 | 10 | 0 | 1 | 11 | 3.2733 |
| Jogador 2 | 40 | 28 | 7 | 10 | 13 | 0 | 2 | 6 | 3.2803 |
| Jogador 3 | 27 | 11 | 0 | 1 | 1 | 0 | 2 | 6 | 4.7408 |
| Jogador 4 | 22 | 7 | 0 | 0 | 0 | 0 | 2 | 4 | 2.1796 |
| Jogador 5 | 40 | 23 | 3 | 4 | 6 | 0 | 3 | 9 | 2.9286 |
| Jogador 6 | 51 | 34 | 2 | 6 | 9 | 0 | 4 | 12 | 3.0795 |
| Jogador 7 | 55 | 38 | 4 | 10 | 15 | 0 | 4 | 13 | 2.0139 |
| Jogador 8 | 56 | 43 | 7 | 10 | 17 | 0 | 2 | 11 | 1.8376 |

As classificações detalhadas e cada sequência correlacionada ficam em audit_report.json.
Uma venda sem compra correspondente na janela é UNKNOWN; sequências ambíguas não são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| HIGH | Jogador 1 | 2-4 | 76 | SOLD_CORE_UNIT | Venda de 'DA_Gromp18_AP' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 1 | 2-6 | 94 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 1 | 2-7 | 104 | PURCHASE_REVERSED | Compra de DA_Murkwolf18 desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 1 | 3-3 | 135 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Vi18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 1 | 3-3 | 139 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 1 | 3-4 | 144 | PURCHASE_REVERSED | Compra de DA_18_Sentry desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 3-4 | 146 | PURCHASE_REVERSED | Compra de DA_Scuttlecrab18 desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 3-5 | 153 | PURCHASE_REVERSED | Compra de DA_18_Yunara desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 1 | 3-5 | 157 | SOLD_CORE_UNIT | Venda de 'DA_Vi18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 1 | 3-7 | 173 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sejuani' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 1 | 4-1 | 183 | PURCHASE_REVERSED | Compra de DA_Vi18 desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 4-1 | 187 | PURCHASE_REVERSED | Compra de DA_18_Azir desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 1 | 4-4 | 215 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 1 | 4-6 | 236 | PURCHASE_REVERSED | Compra de DA_CrimsonRaptor18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 1 | 4-6 | 238 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_MasterYi_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 1 | 4-7 | 245 | PURCHASE_REVERSED | Compra de DA_Amumu18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 1 | 4-7 | 248 | SOLD_CORE_UNIT | Venda de 'DA_Nidalee18_AP' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 1 | 5-1 | 255 | PURCHASE_REVERSED | Compra de DA_Krug18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 1 | 5-2 | 263 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 1 | 5-2 | 266 | SOLD_CORE_UNIT | Venda de 'DA_18_Sivir' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 1 | 5-4 | 284 | PURCHASE_REVERSED | Compra de DA_Murkwolf18 desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 5-7 | 320 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Ezreal' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 1 | 5-7 | 320 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Sivir' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 1 | 5-7 | 320 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Ahri' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 2 | 2-5 | 83 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sejuani' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 2 | 2-7 | 108 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 2 | 3-1 | 113 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 2 | 3-2 | 124 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 2 | 3-3 | 133 | PURCHASE_REVERSED | Compra de DA_18_Tristana desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 2 | 3-3 | 135 | SOLD_CORE_UNIT | Venda de 'DA_Nidalee18_AP' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 2 | 3-3 | 135 | PURCHASE_REVERSED | Compra de DA_Nidalee18_AP desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 3-4 | 144 | PURCHASE_REVERSED | Compra de DA_18_Yunara desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 3-4 | 147 | PURCHASE_REVERSED | Compra de DA_18_Yunara desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 3-6 | 164 | PURCHASE_REVERSED | Compra de DA_18_Cassiopeia desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 3-7 | 174 | PURCHASE_REVERSED | Compra de DA_18_Tristana desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 4-1 | 184 | PURCHASE_REVERSED | Compra de DA_18_Ezreal desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 4-2 | 195 | PURCHASE_REVERSED | Compra de DA_18_Rakan desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 4-3 | 205 | PURCHASE_REVERSED | Compra de DA_18_Tristana desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 4-4 | 214 | PURCHASE_REVERSED | Compra de DA_18_Cassiopeia desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 4-4 | 217 | PURCHASE_REVERSED | Compra de DA_18_Rammus desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 2 | 4-5 | 227 | SOLD_CORE_UNIT | Venda de 'DA_18_LeBlanc' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 2 | 4-6 | 234 | PURCHASE_REVERSED | Compra de DA_18_Rakan desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 5-1 | 256 | PURCHASE_REVERSED | Compra de DA_CrimsonRaptor18 desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 5-2 | 270 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Lux_Elderwood' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 2 | 5-2 | 270 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Yorick' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 2 | 5-2 | 270 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Lillia' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 3 | 2-4 | 74 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 3 | 3-1 | 118 | PURCHASE_REVERSED | Compra de DA_18_Sentry desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 3 | 3-3 | 133 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Murkwolf18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 3 | 4-3 | 203 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 3 | 4-4 | 213 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 3 | 4-7 | 245 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 3 | 5-6 | 305 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 3 | 6-2 | 340 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Malphite' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 3 | 6-2 | 340 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Soraka' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 3 | 6-2 | 340 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_KogMaw18_AD' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 4 | 2-5 | 85 | SOLD_CORE_UNIT | Venda de 'DA_Gromp18_AP' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 4 | 3-1 | 116 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Gromp18_AP' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 4 | 3-2 | 124 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 4 | 3-4 | 143 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_MasterYi_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 4 | 4-6 | 240 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_MasterYi_AD' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 4 | 4-6 | 240 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_CrimsonRaptor18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 4 | 4-6 | 240 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Aphelios' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 5 | 2-3 | 67 | PURCHASE_REVERSED | Compra de DA_18_Rakan desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 5 | 2-6 | 97 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Elise' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 5 | 2-7 | 103 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yunara' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 5 | 2-7 | 106 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yunara' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 5 | 3-2 | 124 | SOLD_CORE_UNIT | Venda de 'DA_18_Yunara' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 5 | 3-3 | 135 | PURCHASE_REVERSED | Compra de DA_18_Yunara desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 3-3 | 137 | PURCHASE_REVERSED | Compra de DA_18_Warwick desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 5 | 4-1 | 185 | SOLD_CORE_UNIT | Venda de 'DA_Fiddlesticks18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 5 | 4-1 | 185 | PURCHASE_REVERSED | Compra de DA_Fiddlesticks18 desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 4-1 | 187 | PURCHASE_REVERSED | Compra de DA_Krug18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 5 | 4-3 | 203 | SOLD_CORE_UNIT | Venda de 'DA_18_Rammus' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 5 | 4-3 | 206 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_MasterYi_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 5 | 4-3 | 207 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 5 | 4-5 | 223 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 5 | 4-6 | 234 | PURCHASE_REVERSED | Compra de DA_CrimsonRaptor18 desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 5-3 | 280 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Tristana' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 5 | 5-3 | 280 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Sentinel18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 5 | 5-3 | 280 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Ahri' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 6 | 2-2 | 53 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 6 | 2-5 | 83 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 6 | 3-1 | 115 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rammus' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 6 | 3-1 | 118 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Murkwolf18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 6 | 3-2 | 126 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rammus' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 6 | 3-3 | 134 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 6 | 3-3 | 135 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 6 | 3-4 | 143 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Murkwolf18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 6 | 3-4 | 148 | SOLD_CORE_UNIT | Venda de 'DA_18_Ahri' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 6 | 3-6 | 163 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 6 | 3-6 | 166 | PURCHASE_REVERSED | Compra de DA_18_Azir desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 6 | 4-1 | 184 | PURCHASE_REVERSED | Compra de DA_18_Rammus desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 6 | 4-2 | 194 | PURCHASE_REVERSED | Compra de DA_18_LeBlanc desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 6 | 4-2 | 195 | PURCHASE_REVERSED | Compra de DA_18_Soraka desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 6 | 4-3 | 204 | PURCHASE_REVERSED | Compra de DA_18_Alistar desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 6 | 4-3 | 205 | PURCHASE_REVERSED | Compra de DA_18_Aphelios desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 6 | 4-4 | 216 | PURCHASE_REVERSED | Compra de DA_18_Rakan desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 6 | 4-4 | 218 | PURCHASE_REVERSED | Compra de DA_18_Kobuko desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 6 | 4-6 | 235 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Fiddlesticks18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 6 | 4-6 | 237 | SOLD_CORE_UNIT | Venda de 'DA_18_GnarSmall' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 6 | 5-1 | 259 | SOLD_CORE_UNIT | Venda de 'DA_18_Lillia' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 6 | 5-6 | 310 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Fiddlesticks18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 6 | 5-6 | 310 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Yunara' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 6 | 5-6 | 310 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Zyra' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 7 | 1-4 | 32 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 7 | 2-1 | 43 | SOLD_CORE_UNIT | Venda de 'DA_18_Shen' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 7 | 2-1 | 43 | PURCHASE_REVERSED | Compra de DA_18_Shen desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 7 | 2-1 | 44 | SOLD_CORE_UNIT | Venda de 'DA_18_LeBlanc' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 7 | 2-1 | 44 | PURCHASE_REVERSED | Compra de DA_18_LeBlanc desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 7 | 2-5 | 86 | PURCHASE_REVERSED | Compra de DA_18_Xayah desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 7 | 2-6 | 97 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Shen' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 7 | 3-2 | 124 | SOLD_CORE_UNIT | Venda de 'DA_Murkwolf18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 7 | 3-2 | 128 | PURCHASE_REVERSED | Compra de DA_Vi18 desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 7 | 3-3 | 135 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 7 | 3-3 | 136 | SOLD_CORE_UNIT | Venda de 'DA_Sentinel18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 7 | 3-4 | 144 | PURCHASE_REVERSED | Compra de DA_18_Diana desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 7 | 3-5 | 156 | PURCHASE_REVERSED | Compra de DA_Krug18 desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 7 | 3-7 | 174 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 7 | 4-1 | 184 | PURCHASE_REVERSED | Compra de DA_18_Azir desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 7 | 4-2 | 195 | PURCHASE_REVERSED | Compra de DA_CrimsonRaptor18 desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 7 | 4-3 | 203 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Ezreal' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 7 | 4-4 | 215 | PURCHASE_REVERSED | Compra de DA_18_MasterYi_AD desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 7 | 4-4 | 218 | SOLD_CORE_UNIT | Venda de 'DA_Fiddlesticks18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 7 | 4-5 | 223 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_KogMaw18_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 7 | 4-5 | 225 | SOLD_CORE_UNIT | Venda de 'DA_18_Ezreal' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 7 | 4-6 | 235 | PURCHASE_REVERSED | Compra de DA_18_Yunara desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 7 | 4-7 | 245 | SOLD_CORE_UNIT | Venda de 'DA_Fiddlesticks18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 7 | 4-7 | 248 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Cassiopeia' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 7 | 5-2 | 264 | PURCHASE_REVERSED | Compra de DA_CrimsonRaptor18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 7 | 5-5 | 294 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_KogMaw18_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 7 | 5-7 | 313 | PURCHASE_REVERSED | Compra de DA_Nidalee18_AP desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 7 | 6-2 | 336 | PURCHASE_REVERSED | Compra de DA_18_Shen desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 2-7 | 105 | PURCHASE_REVERSED | Compra de DA_Vi18 desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 8 | 2-7 | 109 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 8 | 2-7 | 109 | PURCHASE_REVERSED | Compra de DA_18_Tristana desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 3-2 | 124 | PURCHASE_REVERSED | Compra de DA_18_Akali_AD desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 3-3 | 133 | PURCHASE_REVERSED | Compra de DA_18_Akali_AD desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 8 | 3-5 | 153 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Cassiopeia' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 8 | 3-5 | 155 | PURCHASE_REVERSED | Compra de DA_18_Shen desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 3-6 | 167 | PURCHASE_REVERSED | Compra de DA_18_LeBlanc desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 8 | 3-6 | 169 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Cassiopeia' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 8 | 3-7 | 175 | PURCHASE_REVERSED | Compra de DA_Krug18 desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 8 | 3-7 | 177 | SOLD_CORE_UNIT | Venda de 'DA_18_Lillia' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 8 | 4-1 | 185 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_MasterYi_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 8 | 4-1 | 188 | PURCHASE_REVERSED | Compra de DA_18_Tristana desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 8 | 4-3 | 204 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 8 | 4-6 | 234 | PURCHASE_REVERSED | Compra de DA_Fiddlesticks18 desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 4-6 | 235 | PURCHASE_REVERSED | Compra de DA_Amumu18 desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 8 | 4-6 | 237 | SOLD_CORE_UNIT | Venda de 'DA_Sentinel18' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 8 | 5-1 | 256 | PURCHASE_REVERSED | Compra de DA_Nidalee18_AP desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 5-1 | 259 | PURCHASE_REVERSED | Compra de DA_18_Zyra desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 8 | 5-2 | 267 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_KogMaw18_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| MEDIUM | Jogador 8 | 5-4 | 283 | PURCHASE_REVERSED | Compra de DA_18_Diana desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 5-5 | 293 | PURCHASE_REVERSED | Compra de DA_Vi18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 5-5 | 295 | PURCHASE_REVERSED | Compra de DA_Murkwolf18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 5-5 | 297 | PURCHASE_REVERSED | Compra de DA_18_Warwick desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 5-6 | 306 | PURCHASE_REVERSED | Compra de DA_18_Ahri desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 8 | 6-1 | 324 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_KogMaw18_AD' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 8 | 6-1 | 326 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Soraka' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |
| HIGH | Jogador 8 | 6-2 | 336 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Leona' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- O JSON estruturado é a fonte primária para estado de decisão, máscaras, política e recompensas; .tft é analisado apenas para jogadores sem sidecar JSON.- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
