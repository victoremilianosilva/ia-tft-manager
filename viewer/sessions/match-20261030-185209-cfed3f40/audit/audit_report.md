# Auditoria da partida TFT

- Arquivos lidos: **8**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **3897**
- Achados: **77**
- CRITICAL: 0 | HIGH: 13 | MEDIUM: 64 | LOW: 0

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 184 | 184 | 184 | 0 | 181 | 0 | 184 | 184 | 180 | 38/25 |
| Jogador 2 | 131 | 131 | 131 | 0 | 128 | 0 | 131 | 131 | 131 | 24/8 |
| Jogador 3 | 144 | 144 | 144 | 0 | 143 | 0 | 144 | 144 | 134 | 29/15 |
| Jogador 4 | 115 | 115 | 115 | 0 | 115 | 0 | 115 | 115 | 98 | 25/11 |
| Jogador 5 | 111 | 111 | 111 | 0 | 111 | 0 | 111 | 111 | 98 | 25/12 |
| Jogador 6 | 110 | 110 | 110 | 0 | 110 | 0 | 110 | 110 | 93 | 21/7 |
| Jogador 7 | 137 | 137 | 137 | 0 | 134 | 0 | 137 | 137 | 137 | 24/8 |
| Jogador 8 | 146 | 146 | 146 | 0 | 145 | 0 | 146 | 146 | 139 | 37/22 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0013076922623440623 | 0.0 | 0.0 | +— / -ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +a8111a04-3067-4ce6-9a4b-4f5bb205f413 / -— |
| Jogador 1 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.3402393162250519 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9794912934303284 | 0.0 | 0.0 | +cde2c30a-df2c-4275-86ef-e4a4a13a5be1 / -— |
| Jogador 1 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 13 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29290837049484253 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 14 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.16431555151939392 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.23321442306041718 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 16 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16698694229125977 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 17 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5122578740119934 | 0.0 | 0.0 | +— / -2718f555-b782-4fea-a68f-31395ad34232 |
| Jogador 1 | 1-2 | 18 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.24870596826076508 | 0.0 | 0.0 | +679fe281-674a-438b-bdcf-57229a283d44 / -— |
| Jogador 1 | 1-2 | 19 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3669586181640625 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 20 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 21 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.22417572140693665 | 0.0 | 0.0 | +24247863-54d4-4674-86e9-9a45609a440e / -— |
| Jogador 1 | 1-3 | 25 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5058807134628296 | 0.0 | 0.0 | +— / -24247863-54d4-4674-86e9-9a45609a440e |
| Jogador 1 | 1-3 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.12280712276697159 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.31718239188194275 | 0.0 | 0.0 | +cfc9d52e-f119-4fc9-8ced-569ac7071cb6 / -— |
| Jogador 1 | 1-3 | 28 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5199753046035767 | 0.0 | 0.0 | +— / -cfc9d52e-f119-4fc9-8ced-569ac7071cb6 |
| Jogador 1 | 1-3 | 29 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 48 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9700698852539062 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 49 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0200698375701904 | 0.0 | 0.0 | +— / -c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 1-4 | 50 | BUY_XP | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.04450000077486038 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 51 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.03326775133609772 | 0.0 | 0.0 | +9a936ebd-aacd-4366-a1c8-78534d5a253b / -— |
| Jogador 1 | 1-4 | 52 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.501153826713562 | 0.0 | 0.0 | +— / -9a936ebd-aacd-4366-a1c8-78534d5a253b |
| Jogador 1 | 1-4 | 53 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | -0.04033435508608818 | 0.0 | 0.0 | +f712c9f5-96de-4ff5-93b8-5cad16b3cb05 / -— |
| Jogador 1 | 1-4 | 54 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4894615411758423 | 0.0 | 0.0 | +— / -f712c9f5-96de-4ff5-93b8-5cad16b3cb05 |
| Jogador 1 | 1-4 | 55 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | -0.04034249112010002 | 0.0 | 0.0 | +6465b229-8025-4e7d-94de-1cd49fa76167 / -— |
| Jogador 1 | 1-4 | 56 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4894615411758423 | 0.0 | 0.0 | +— / -6465b229-8025-4e7d-94de-1cd49fa76167 |
| Jogador 1 | 1-4 | 57 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 58 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 72 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.23910266160964966 | 0.0 | 0.0 | +3a74be8d-bf7c-4449-9f1b-d76521e73e6f / -— |
| Jogador 1 | 2-1 | 73 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4256007671356201 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 74 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.05448774993419647 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 75 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 76 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.051634397357702255 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 77 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.12371200323104858 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 78 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 92 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4389503300189972 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 93 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05647014081478119 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 94 | SELL | STABILIZE | 100.0 | 4 | 6 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04925163835287094 | 0.0 | 0.0 | +— / -679fe281-674a-438b-bdcf-57229a283d44 |
| Jogador 1 | 2-2 | 95 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9584171772003174 | 0.0 | 0.0 | +7aea963f-f0a4-4fa2-8da0-cc5eb260f665 / -— |
| Jogador 1 | 2-2 | 96 | SELL | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0084171295166016 | 0.0 | 0.0 | +— / -7aea963f-f0a4-4fa2-8da0-cc5eb260f665 |
| Jogador 1 | 2-2 | 97 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 7 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.01868247613310814 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 98 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 7 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.02176794223487377 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 99 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.026499999687075615 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 100 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3327846825122833 | 0.0 | 0.0 | +4fc25524-9d8f-46f0-a145-ba3de2642229 / -— |
| Jogador 1 | 2-2 | 101 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3827846646308899 | 0.0 | 0.0 | +— / -4fc25524-9d8f-46f0-a145-ba3de2642229 |
| Jogador 1 | 2-2 | 102 | PASS | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 112 | BUY | STABILIZE | 94.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.038433004170656204 | 0.0 | 0.0 | +ff10e482-7085-4e73-8a0c-fdd3f4938128 / -— |
| Jogador 1 | 2-3 | 113 | BUY | STABILIZE | 94.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.033316198736429214 | 0.0 | 0.0 | +6951a681-f5b9-4c22-9182-46b4d2c3cbb3 / -— |
| Jogador 1 | 2-3 | 114 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3783501386642456 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 115 | SELL | STABILIZE | 94.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19501690566539764 | 0.0 | 0.0 | +— / -6951a681-f5b9-4c22-9182-46b4d2c3cbb3 |
| Jogador 1 | 2-3 | 116 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 5 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.04408536106348038 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 117 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 5 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.14550241827964783 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 118 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 5 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06667235493659973 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 119 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 5 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10544315725564957 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 120 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 5 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0024998392909765244 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 121 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 5 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.012479945085942745 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 122 | PASS | STABILIZE | 94.0 | 5 | 5 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 136 | BUY | STABILIZE | 94.0 | 5 | 11 | 1 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.35678204894065857 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 137 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 8 | 0 | 20.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5129541754722595 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 138 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 8 | 0 | 20.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.037743207067251205 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 139 | SELL | STABILIZE | 94.0 | 5 | 8 | 0 | 24.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3916914463043213 | 0.0 | 0.0 | +— / -a8111a04-3067-4ce6-9a4b-4f5bb205f413 |
| Jogador 1 | 2-4 | 140 | BUY | STABILIZE | 94.0 | 5 | 9 | 0 | 24.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.30429738759994507 | 0.0 | 0.0 | +8c5a0cda-86da-4f36-bee3-c2eae934e263 / -— |
| Jogador 1 | 2-4 | 141 | SELL | STABILIZE | 94.0 | 5 | 7 | 0 | 24.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.354297399520874 | 0.0 | 0.0 | +— / -8c5a0cda-86da-4f36-bee3-c2eae934e263 |
| Jogador 1 | 2-4 | 142 | BUY_XP | STABILIZE | 94.0 | 5 | 9 | 0 | 24.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 143 | BUY_XP | STABILIZE | 94.0 | 5 | 5 | 0 | 24.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 144 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 1 | 0 | 24.0 | —/DA_KogMaw18_AD | BUY, MOVE_BOARD, PASS | True | True | -0.2255912870168686 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 145 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 1 | 0 | 24.0 | —/DA_KogMaw18_AD | BUY, MOVE_BOARD, PASS | True | True | 0.06809724122285843 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 146 | PASS | STABILIZE | 94.0 | 5 | 1 | 0 | 24.0 | —/DA_KogMaw18_AD | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 156 | BUY | STABILIZE | 94.0 | 5 | 6 | 0 | 24.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3641003668308258 | 0.0 | 0.0 | +0c9ac713-08bd-4fa7-a94a-2ab70d7815ff / -— |
| Jogador 1 | 2-5 | 157 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 3 | 0 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29054269194602966 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 158 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 3 | 0 | 24.0 | Colosso/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1297316998243332 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 159 | PASS | STABILIZE | 94.0 | 5 | 3 | 0 | 24.0 | Colosso/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 177 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 10 | 1 | 24.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45672622323036194 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 178 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 10 | 1 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33520781993865967 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 179 | PASS | STABILIZE | 94.0 | 5 | 10 | 1 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 198 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 18 | 1 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10090097039937973 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 199 | SELL | STABILIZE | 94.0 | 5 | 18 | 1 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27783581614494324 | 0.0 | 0.0 | +— / -3a74be8d-bf7c-4449-9f1b-d76521e73e6f |
| Jogador 1 | 2-7 | 200 | BUY | STABILIZE | 94.0 | 5 | 20 | 2 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9017502665519714 | 0.0 | 0.0 | +2a286030-5984-44b5-87ff-6c948d2e672e / -— |
| Jogador 1 | 2-7 | 201 | SELL | STABILIZE | 94.0 | 5 | 19 | 1 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9517502784729004 | 0.0 | 0.0 | +— / -2a286030-5984-44b5-87ff-6c948d2e672e |
| Jogador 1 | 2-7 | 202 | BUY_XP | STABILIZE | 94.0 | 5 | 20 | 2 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.06700000166893005 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 203 | BUY | STABILIZE | 94.0 | 6 | 16 | 1 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.04188863933086395 | 0.0 | 0.0 | +3fc2815d-c456-47c3-bb27-783336b3cdfa / -— |
| Jogador 1 | 2-7 | 204 | SELL | STABILIZE | 94.0 | 6 | 14 | 1 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1851431280374527 | 0.0 | 0.0 | +— / -3fc2815d-c456-47c3-bb27-783336b3cdfa |
| Jogador 1 | 2-7 | 205 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 16 | 1 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 206 | BUY | STABILIZE | 94.0 | 6 | 16 | 1 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10660452395677567 | 0.0 | 0.0 | +07130d94-c79f-4052-b3e9-7f867421f01b / -— |
| Jogador 1 | 2-7 | 207 | SELL | STABILIZE | 94.0 | 6 | 14 | 1 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16099999845027924 | 0.0 | 0.0 | +— / -07130d94-c79f-4052-b3e9-7f867421f01b |
| Jogador 1 | 2-7 | 208 | PASS | STABILIZE | 94.0 | 6 | 16 | 1 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 218 | BUY | STABILIZE | 94.0 | 6 | 23 | 2 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7019697427749634 | 0.0 | 0.0 | +7c218f01-e884-46da-8a1a-2d2db27a5ff1 / -— |
| Jogador 1 | 3-1 | 219 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 20 | 2 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12859918177127838 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 220 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 20 | 2 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.036966722458601 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 221 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 20 | 2 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 222 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 20 | 2 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.020740801468491554 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 223 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 20 | 2 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.127062126994133 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 224 | BUY | STABILIZE | 94.0 | 6 | 20 | 2 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.169617161154747 | 0.0 | 0.0 | +8e819ba6-a356-4d9b-a8c9-7493332900fb / -— |
| Jogador 1 | 3-1 | 225 | BUY_XP | STABILIZE | 94.0 | 6 | 18 | 1 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 226 | BUY_XP | STABILIZE | 94.0 | 6 | 14 | 1 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 227 | BUY_XP | STABILIZE | 94.0 | 6 | 10 | 1 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 228 | PASS | STABILIZE | 94.0 | 6 | 6 | 0 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 238 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 11 | 1 | 32.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31391021609306335 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 239 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 11 | 1 | 30.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.421885222196579 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 240 | PASS | STABILIZE | 84.0 | 6 | 11 | 1 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 256 | BUY | STABILIZE | 84.0 | 6 | 18 | 1 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7435451149940491 | 0.0 | 0.0 | +c30e7bdb-41d6-423c-9d7d-2e146472e724 / -— |
| Jogador 1 | 3-3 | 257 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 15 | 1 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.022793645039200783 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 258 | BUY_XP | STABILIZE | 84.0 | 6 | 15 | 1 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 259 | BUY_XP | STABILIZE | 84.0 | 6 | 11 | 1 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 260 | BUY_XP | STABILIZE | 84.0 | 6 | 7 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 261 | SELL | STABILIZE | 84.0 | 6 | 3 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3825877010822296 | 0.0 | 0.0 | +— / -3a43ff36-dccd-49a7-92d8-0b01e739ea89 |
| Jogador 1 | 3-3 | 262 | SELL | STABILIZE | 84.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9196153879165649 | 0.0 | 0.0 | +— / -c30e7bdb-41d6-423c-9d7d-2e146472e724 |
| Jogador 1 | 3-3 | 263 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 9 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.11359098553657532 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 264 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 9 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 265 | PASS | STABILIZE | 84.0 | 6 | 9 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 275 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 17 | 1 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.01040505338460207 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 276 | MOVE_BOARD | STABILIZE | 84.0 | 6 | 17 | 1 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.02891405299305916 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 277 | BUY_XP | STABILIZE | 84.0 | 6 | 17 | 1 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.05649999901652336 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 278 | BUY | STABILIZE | 84.0 | 7 | 13 | 1 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.2826005220413208 | 0.0 | 0.0 | +bddefab1-7dd7-4954-816c-45dbd44b947b / -— |
| Jogador 1 | 3-4 | 279 | SELL | STABILIZE | 84.0 | 7 | 11 | 1 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16099999845027924 | 0.0 | 0.0 | +— / -bddefab1-7dd7-4954-816c-45dbd44b947b |
| Jogador 1 | 3-4 | 280 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 13 | 1 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.14797915518283844 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 281 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 13 | 1 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03607180714607239 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 282 | BUY_XP | STABILIZE | 84.0 | 7 | 13 | 1 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.20800000429153442 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 283 | BUY_XP | STABILIZE | 84.0 | 7 | 9 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 284 | BUY_XP | STABILIZE | 84.0 | 7 | 5 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 285 | PASS | STABILIZE | 84.0 | 7 | 1 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 292 | BUY | STABILIZE | 84.0 | 7 | 7 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7439301013946533 | 0.0 | 0.0 | +727765c8-7f02-491e-a6da-12b0dab59f6d / -— |
| Jogador 1 | 3-5 | 293 | MOVE_BENCH | STABILIZE | 84.0 | 7 | 4 | 0 | 30.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5420548915863037 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 294 | BUY_XP | STABILIZE | 84.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 295 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_KogMaw18_AD | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 296 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_KogMaw18_AD | MOVE_BOARD, PASS | True | True | 0.017798790708184242 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 297 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_KogMaw18_AD | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 298 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_KogMaw18_AD | MOVE_BOARD, PASS | True | True | 0.1799345165491104 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 299 | PASS | STABILIZE | 84.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_KogMaw18_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 312 | BUY | STABILIZE | 84.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8305763602256775 | 0.0 | 0.0 | +d8c38b21-fc25-4c11-87b5-b5747d71bbc7 / -7c218f01-e884-46da-8a1a-2d2db27a5ff1,ff10e482-7085-4e73-8a0c-fdd3f4938128 |
| Jogador 1 | 3-6 | 313 | BUY | STABILIZE | 84.0 | 7 | 4 | 0 | 24.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15786564350128174 | 0.0 | 0.0 | +4518ad1d-87e7-4110-830a-96183c533201 / -— |
| Jogador 1 | 3-6 | 314 | MOVE_BENCH | STABILIZE | 84.0 | 7 | 0 | 0 | 24.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2250336855649948 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 315 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.034966591745615005 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 316 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 317 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12384627014398575 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 318 | PASS | STABILIZE | 84.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 329 | MOVE_BENCH | STABILIZE | 84.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4338514506816864 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 332 | BUY | STABILIZE | 84.0 | 7 | 7 | 0 | 44.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.13761021196842194 | 0.0 | 0.0 | +7306c9be-466e-498c-819e-274ff070c72b / -— |
| Jogador 1 | 3-7 | 333 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 2 | 0 | 44.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26720380783081055 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 334 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 2 | 0 | 44.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01956525258719921 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 335 | MOVE_BENCH | STABILIZE | 84.0 | 7 | 2 | 0 | 44.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7467291951179504 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 336 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 2 | 0 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18787872791290283 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 337 | PASS | STABILIZE | 84.0 | 7 | 2 | 0 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 352 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 8 | 0 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.31352606415748596 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 353 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 8 | 0 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.11304885894060135 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 354 | PASS | STABILIZE | 84.0 | 7 | 8 | 0 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 372 | BUY | STABILIZE | 84.0 | 7 | 16 | 1 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2773357629776001 | 0.0 | 0.0 | +5af104f2-7959-4ca5-91a9-7d44494532ea / -— |
| Jogador 1 | 4-2 | 373 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 13 | 1 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 374 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 13 | 1 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.15195749700069427 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 375 | PASS | STABILIZE | 84.0 | 7 | 13 | 1 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 392 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 19 | 1 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 393 | PASS | STABILIZE | 72.0 | 7 | 19 | 1 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 412 | PASS | STABILIZE | 72.0 | 7 | 27 | 2 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 432 | BUY | FAST8 | 72.0 | 7 | 34 | 3 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.11741878092288971 | 0.0 | 0.0 | +ed23d828-f4bc-4d6c-8cc1-c074047dac8a / -— |
| Jogador 1 | 4-5 | 433 | PASS | FAST8 | 72.0 | 7 | 30 | 3 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 452 | PASS | FAST8 | 57.0 | 7 | 38 | 3 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 472 | PASS | FAST8 | 44.0 | 7 | 47 | 4 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.04500000178813934 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 492 | EQUIP_FROM_INVENTORY | FAST8 | 44.0 | 7 | 57 | 5 | 48.0 | Colosso/DA_18_MasterYi_AD | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 493 | PASS | FAST8 | 44.0 | 7 | 57 | 5 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.002654589945450425 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 510 | PASS | FAST8 | 44.0 | 7 | 68 | 5 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.11355801671743393 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 522 | BUY | FAST8 | 44.0 | 7 | 79 | 5 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3892279863357544 | 0.0 | 0.0 | +2f2ff445-f60a-4a05-b37a-41b8a6d6c7f9 / -— |
| Jogador 1 | 5-3 | 523 | PASS | FAST8 | 44.0 | 7 | 75 | 5 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.12494135648012161 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 542 | PASS | STABILIZE | 30.0 | 7 | 85 | 5 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.1423230916261673 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 562 | PASS | STABILIZE | 30.0 | 7 | 95 | 5 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.024759097024798393 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 582 | BUY | ALL_IN | 12.0 | 7 | 106 | 5 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.1534100770950317 | 0.0 | 0.0 | +6c338d19-b3d3-49a7-b61e-4732249ee457 / -0c9ac713-08bd-4fa7-a94a-2ab70d7815ff,727765c8-7f02-491e-a6da-12b0dab59f6d |
| Jogador 1 | 5-6 | 583 | BUY | ALL_IN | 12.0 | 7 | 103 | 5 | 36.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.46321168541908264 | 0.0 | 0.0 | +7313188a-ce84-4a52-b2d0-a94b2c420cdb / -— |
| Jogador 1 | 5-6 | 584 | BUY | ALL_IN | 12.0 | 7 | 100 | 5 | 36.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.39998459815979004 | 0.0 | 0.0 | +4688e6f1-26c5-402d-8d27-0f9bce3a9681 / -— |
| Jogador 1 | 5-6 | 585 | PASS | ALL_IN | 12.0 | 7 | 98 | 5 | 36.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07675280421972275 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 600 | MOVE_BENCH | ALL_IN | 12.0 | 7 | 98 | 5 | 36.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3898926079273224 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 602 | BUY | ALL_IN | 12.0 | 7 | 109 | 5 | 42.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8944061994552612 | 0.0 | 0.0 | +8b8aaa92-8fe0-46ad-857e-af3bae9b26a4 / -— |
| Jogador 1 | 5-7 | 603 | PASS | ALL_IN | 12.0 | 7 | 106 | 5 | 42.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.08218884468078613 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 619 | MOVE_BENCH | ALL_IN | 12.0 | 7 | 106 | 5 | 42.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6808306574821472 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 622 | EQUIP_FROM_INVENTORY | ALL_IN | 12.0 | 7 | 117 | 5 | 48.0 | Colosso/DA_18_MasterYi_AD | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 623 | EQUIP_FROM_INVENTORY | ALL_IN | 12.0 | 7 | 117 | 5 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY, CRAFT_AND_EQUIP | True | — | 0.05426165089011192 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 624 | BUY | ALL_IN | 12.0 | 7 | 117 | 5 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.044387053698301315 | 0.0 | 0.0 | +d8392323-28e4-4e98-a466-5958bf400729 / -— |
| Jogador 1 | 6-1 | 625 | PASS | ALL_IN | 12.0 | 7 | 114 | 5 | 48.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.27795127034187317 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 632 | PASS | ALL_IN | 0.0 | 7 | 114 | 5 | 0.0 | Colosso/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 642 | PASS | ALL_IN | 0.0 | 7 | 114 | 5 | 0.0 | Colosso/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-4 | 652 | PASS | ALL_IN | 0.0 | 7 | 114 | 5 | 0.0 | Colosso/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-5 | 662 | PASS | ALL_IN | 0.0 | 7 | 114 | 5 | 0.0 | Colosso/DA_18_MasterYi_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.010384615510702133 | 0.0 | 0.0 | +— / -fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.22450661659240723 | 0.0 | 0.0 | +292ef825-d326-4dd8-9c42-c47cfc62116f / -— |
| Jogador 2 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 9 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.27265432476997375 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9709054827690125 | 0.0 | 0.0 | +94ede66e-59bc-4c41-aabf-f64372e20f9a / -— |
| Jogador 2 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30448776483535767 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 13 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.17199330031871796 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | -0.02973262593150139 | 0.0 | 0.0 | +f0d714b2-9165-4d27-97f5-04b552d02548 / -— |
| Jogador 2 | 1-2 | 15 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5027231574058533 | 0.0 | 0.0 | +— / -f0d714b2-9165-4d27-97f5-04b552d02548 |
| Jogador 2 | 1-2 | 16 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1847771406173706 | 0.0 | 0.0 | +de00430a-8a57-423c-887c-317d53c2cdd3 / -— |
| Jogador 2 | 1-3 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46916744112968445 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.03840096667408943 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 27 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Sejuani | BUY, MOVE_BOARD, PASS | True | True | 0.16031472384929657 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 28 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Sejuani | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 48 | BUY_XP | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.04450000077486038 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 49 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Sejuani | MOVE_BOARD, PASS | True | True | -0.18895575404167175 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 50 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 72 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3906307816505432 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 73 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 1 | 0 | 8.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40232640504837036 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 74 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 14.0 | —/DA_Vi18 | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 75 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 14.0 | —/DA_Vi18 | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 76 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 14.0 | —/DA_Vi18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 92 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.026499999687075615 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 93 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_Vi18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.06010375916957855 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 94 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_Vi18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.025268826633691788 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 95 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4418499767780304 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 96 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_Vi18 | BUY, MOVE_BOARD, PASS | True | True | 0.039354316890239716 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 97 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_Vi18 | BUY, MOVE_BOARD, PASS | True | True | 0.04875248298048973 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 98 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_Vi18 | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 99 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_Vi18 | BUY, MOVE_BOARD, PASS | True | True | -0.1243831217288971 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 100 | PASS | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_Vi18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 112 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 8 | 0 | 18.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.036966722458601 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 113 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 8 | 0 | 18.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08318109065294266 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 114 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 18.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3876167833805084 | 0.0 | 0.0 | +8c364966-f97c-4f54-b087-ddd182a9f8ea / -— |
| Jogador 2 | 2-3 | 115 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 5 | 0 | 18.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27389758825302124 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 116 | BUY_XP | STABILIZE | 100.0 | 5 | 5 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 117 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.43379834294319153 | 0.0 | 0.0 | +— / -292ef825-d326-4dd8-9c42-c47cfc62116f |
| Jogador 2 | 2-3 | 118 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 2 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 119 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 2 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.1297316998243332 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 120 | PASS | STABILIZE | 100.0 | 5 | 2 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 136 | BUY | STABILIZE | 95.0 | 5 | 7 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4382363557815552 | 0.0 | 0.0 | +2ace989d-3e9e-483b-9b14-cd6b8f171f17 / -— |
| Jogador 2 | 2-4 | 137 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 4 | 0 | 22.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08128055185079575 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 138 | BUY_XP | ECON | 95.0 | 5 | 4 | 0 | 26.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 139 | SELL | ECON | 95.0 | 5 | 0 | 0 | 26.0 | —/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06382633000612259 | 0.0 | 0.0 | +— / -94ede66e-59bc-4c41-aabf-f64372e20f9a |
| Jogador 2 | 2-4 | 140 | MOVE_BOARD | ECON | 95.0 | 5 | 1 | 0 | 26.0 | —/DA_Fiddlesticks18 | BUY, MOVE_BOARD, PASS | True | True | 0.029725274071097374 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 141 | PASS | ECON | 95.0 | 5 | 1 | 0 | 26.0 | —/DA_Fiddlesticks18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 156 | BUY | ECON | 95.0 | 5 | 6 | 0 | 26.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2848890423774719 | 0.0 | 0.0 | +081b684f-5d42-45c5-9a68-12127e5330a7 / -— |
| Jogador 2 | 2-5 | 157 | SELL | ECON | 95.0 | 5 | 3 | 0 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5489428043365479 | 0.0 | 0.0 | +— / -081b684f-5d42-45c5-9a68-12127e5330a7 |
| Jogador 2 | 2-5 | 158 | BUY_XP | STABILIZE | 95.0 | 5 | 6 | 0 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 159 | PASS | STABILIZE | 95.0 | 5 | 2 | 0 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 177 | BUY | STABILIZE | 95.0 | 6 | 8 | 0 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2804258465766907 | 0.0 | 0.0 | +97fc5647-5995-4f21-aa03-13454546919a / -— |
| Jogador 2 | 2-6 | 178 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 4 | 0 | 26.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4388050436973572 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 179 | BUY_XP | STABILIZE | 95.0 | 6 | 4 | 0 | 34.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 180 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 34.0 | Colosso/DA_18_Malphite | MOVE_BOARD, PASS | True | True | 0.032957449555397034 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 181 | MOVE_BOARD | STABILIZE | 95.0 | 6 | 0 | 0 | 34.0 | Colosso/DA_18_Malphite | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 182 | PASS | STABILIZE | 95.0 | 6 | 0 | 0 | 34.0 | Colosso/DA_18_Malphite | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 198 | BUY | STABILIZE | 95.0 | 6 | 7 | 0 | 34.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2840234935283661 | 0.0 | 0.0 | +729ccd5b-adc5-4bca-9523-dcb532e93ecb / -— |
| Jogador 2 | 2-7 | 199 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 3 | 0 | 34.0 | Colosso/DA_18_Malphite | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3474758267402649 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 200 | MOVE_BENCH | STABILIZE | 95.0 | 6 | 3 | 0 | 34.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1565542072057724 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 201 | PASS | STABILIZE | 95.0 | 6 | 3 | 0 | 36.0 | Colosso/DA_18_Malphite | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 218 | BUY_XP | STABILIZE | 95.0 | 6 | 9 | 0 | 36.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 219 | BUY_XP | STABILIZE | 95.0 | 6 | 5 | 0 | 36.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 220 | PASS | STABILIZE | 95.0 | 6 | 1 | 0 | 36.0 | Colosso/DA_18_Malphite | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 238 | BUY_XP | STABILIZE | 95.0 | 6 | 8 | 0 | 36.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 239 | BUY_XP | STABILIZE | 95.0 | 6 | 4 | 0 | 36.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 240 | SELL | STABILIZE | 95.0 | 6 | 0 | 0 | 36.0 | Colosso/DA_18_Malphite | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020999999716877937 | 0.0 | 0.0 | +— / -8c364966-f97c-4f54-b087-ddd182a9f8ea |
| Jogador 2 | 3-2 | 241 | PASS | STABILIZE | 95.0 | 6 | 3 | 0 | 36.0 | Colosso/DA_18_Malphite | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 256 | PASS | STABILIZE | 95.0 | 6 | 10 | 1 | 36.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 275 | PASS | STABILIZE | 95.0 | 6 | 19 | 1 | 36.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 292 | BUY_XP | STABILIZE | 95.0 | 6 | 27 | 2 | 36.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08349999785423279 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 293 | BUY | STABILIZE | 95.0 | 7 | 23 | 2 | 36.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.07509709894657135 | 0.0 | 0.0 | +cce8de69-f877-4e86-b720-6aea91e68f47 / -— |
| Jogador 2 | 3-5 | 294 | BUY_XP | STABILIZE | 95.0 | 7 | 20 | 2 | 36.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20800000429153442 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 295 | BUY_XP | STABILIZE | 95.0 | 7 | 16 | 1 | 36.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 296 | BUY_XP | STABILIZE | 95.0 | 7 | 12 | 1 | 36.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20800000429153442 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 297 | BUY_XP | STABILIZE | 95.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 298 | BUY_XP | STABILIZE | 95.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 299 | MOVE_BOARD | STABILIZE | 95.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_Malphite | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 300 | MOVE_BOARD | STABILIZE | 95.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_Malphite | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024840479716658592 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 301 | SELL | STABILIZE | 95.0 | 7 | 0 | 0 | 36.0 | Colosso/DA_18_Malphite | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18708595633506775 | 0.0 | 0.0 | +— / -cce8de69-f877-4e86-b720-6aea91e68f47 |
| Jogador 2 | 3-5 | 302 | PASS | STABILIZE | 95.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_18_Malphite | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 312 | BUY | STABILIZE | 84.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.12414298951625824 | 0.0 | 0.0 | +23157bd6-5e8f-4416-bb7f-2e5d71a06543 / -— |
| Jogador 2 | 3-6 | 313 | MOVE_BENCH | STABILIZE | 84.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35550349950790405 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 314 | BUY_XP | STABILIZE | 84.0 | 7 | 4 | 0 | 44.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 315 | MOVE_BOARD | STABILIZE | 84.0 | 7 | 0 | 0 | 44.0 | Colosso/DA_18_Malphite | MOVE_BOARD, PASS | True | True | 0.17825105786323547 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 316 | PASS | STABILIZE | 84.0 | 7 | 0 | 0 | 44.0 | Colosso/DA_18_Malphite | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 332 | BUY | STABILIZE | 72.0 | 7 | 6 | 0 | 44.0 | Colosso/DA_18_Malphite | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7333641648292542 | 0.0 | 0.0 | +e0445166-70a5-4135-a45e-ff238a95b228 / -— |
| Jogador 2 | 3-7 | 333 | MOVE_BOARD | STABILIZE | 72.0 | 7 | 2 | 0 | 44.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.282122939825058 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 334 | PASS | STABILIZE | 72.0 | 7 | 2 | 0 | 44.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 352 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 8 | 0 | 44.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 353 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 8 | 0 | 44.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3360576033592224 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 354 | PASS | STABILIZE | 72.0 | 7 | 8 | 0 | 48.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 372 | PASS | STABILIZE | 72.0 | 7 | 14 | 1 | 48.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 392 | BUY_XP | STABILIZE | 72.0 | 7 | 22 | 2 | 48.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 393 | BUY_XP | STABILIZE | 72.0 | 7 | 18 | 1 | 48.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 394 | BUY_XP | STABILIZE | 72.0 | 7 | 14 | 1 | 48.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 395 | BUY_XP | STABILIZE | 72.0 | 7 | 10 | 1 | 48.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 396 | BUY_XP | STABILIZE | 72.0 | 7 | 6 | 0 | 48.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 397 | SELL | STABILIZE | 72.0 | 7 | 2 | 0 | 48.0 | Colosso/DA_18_Lillia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35720232129096985 | 0.0 | 0.0 | +— / -de00430a-8a57-423c-887c-317d53c2cdd3 |
| Jogador 2 | 4-3 | 398 | BUY_XP | STABILIZE | 72.0 | 7 | 4 | 0 | 48.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.059593748301267624 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 399 | PASS | ECON | 72.0 | 8 | 0 | 0 | 48.0 | Colosso/DA_18_Lillia | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 412 | BUY | WINSTREAK | 72.0 | 8 | 7 | 0 | 48.0 | Defendente/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2611575424671173 | 0.0 | 0.0 | +8455b875-27e0-4172-9311-5cbb3e2242b9 / -— |
| Jogador 2 | 4-4 | 413 | MOVE_BENCH | WINSTREAK | 72.0 | 8 | 4 | 0 | 48.0 | Defendente/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4987216293811798 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 414 | PASS | WINSTREAK | 72.0 | 8 | 4 | 0 | 54.0 | Defendente/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 432 | BUY | WINSTREAK | 72.0 | 8 | 10 | 1 | 54.0 | Defendente/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.07644344866275787 | 0.0 | 0.0 | +e7c7b5ea-79ec-44e9-ae6c-6e881b84fe15 / -— |
| Jogador 2 | 4-5 | 433 | PASS | WINSTREAK | 72.0 | 8 | 6 | 0 | 54.0 | Defendente/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 452 | PASS | WINSTREAK | 72.0 | 8 | 13 | 1 | 54.0 | Defendente/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 472 | BUY | WINSTREAK | 72.0 | 8 | 22 | 2 | 54.0 | Defendente/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7458507418632507 | 0.0 | 0.0 | +ded275a3-9551-4816-8112-f0a25524412c / -— |
| Jogador 2 | 4-7 | 473 | PASS | WINSTREAK | 72.0 | 8 | 20 | 2 | 54.0 | Defendente/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 492 | EQUIP_FROM_INVENTORY | WINSTREAK | 72.0 | 8 | 29 | 2 | 54.0 | Defendente/DA_18_Lillia | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 493 | BUY | WINSTREAK | 72.0 | 8 | 29 | 2 | 54.0 | Defendente/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.20846466720104218 | 0.0 | 0.0 | +565ff610-fe51-470b-8452-a7eec5e31653 / -— |
| Jogador 2 | 5-1 | 494 | PASS | WINSTREAK | 72.0 | 8 | 24 | 2 | 54.0 | Defendente/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 510 | PASS | WINSTREAK | 72.0 | 8 | 35 | 3 | 54.0 | Defendente/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.04500000178813934 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 522 | PASS | WINSTREAK | 72.0 | 8 | 46 | 4 | 54.0 | Defendente/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 542 | PASS | WINSTREAK | 72.0 | 8 | 59 | 5 | 54.0 | Defendente/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10025422275066376 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 562 | BUY | WINSTREAK | 72.0 | 8 | 72 | 5 | 54.0 | Defendente/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.804061233997345 | 0.0 | 0.0 | +986fbe1e-1826-4be7-a5d6-410a4c0a3f2f / -— |
| Jogador 2 | 5-5 | 563 | PASS | WINSTREAK | 72.0 | 8 | 68 | 5 | 54.0 | Defendente/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.008245306089520454 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 582 | PASS | WINSTREAK | 72.0 | 8 | 82 | 5 | 54.0 | Defendente/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.13698852062225342 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 602 | BUY | WINSTREAK | 72.0 | 8 | 96 | 5 | 54.0 | Defendente/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.13562269508838654 | 0.0 | 0.0 | +af404167-469a-447e-b415-dcb52033ef9b / -— |
| Jogador 2 | 5-7 | 603 | BUY | WINSTREAK | 72.0 | 8 | 91 | 5 | 54.0 | Defendente/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9736145734786987 | 0.0 | 0.0 | +39b89fbe-9520-4eaa-80f9-81e03232c83c / -— |
| Jogador 2 | 5-7 | 604 | BUY | WINSTREAK | 72.0 | 8 | 88 | 5 | 54.0 | Defendente/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.26704859733581543 | 0.0 | 0.0 | +2f2b455f-7035-4948-9429-612018ae7063 / -— |
| Jogador 2 | 5-7 | 605 | PASS | WINSTREAK | 72.0 | 8 | 84 | 5 | 54.0 | Defendente/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.14053432643413544 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 622 | EQUIP_FROM_INVENTORY | WINSTREAK | 72.0 | 8 | 97 | 5 | 54.0 | Defendente/DA_18_Lux_Sunbeam | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 623 | EQUIP_FROM_INVENTORY | WINSTREAK | 72.0 | 8 | 97 | 5 | 54.0 | Defendente/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY, CRAFT_AND_EQUIP | True | — | 0.12545837461948395 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 624 | BUY | WINSTREAK | 72.0 | 8 | 97 | 5 | 54.0 | Defendente/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2670130133628845 | 0.0 | 0.0 | +64d87de4-68df-4a72-8b8d-f78039ae4ce5 / -— |
| Jogador 2 | 6-1 | 625 | PASS | WINSTREAK | 72.0 | 8 | 93 | 5 | 54.0 | Defendente/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.02344455197453499 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 632 | BUY | WINSTREAK | 72.0 | 8 | 107 | 5 | 54.0 | Defendente/DA_18_Lux_Sunbeam | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.26704785227775574 | 0.0 | 0.0 | +d2afd490-f89f-47c9-8279-a88acde5b1b6 / -— |
| Jogador 2 | 6-2 | 633 | PASS | WINSTREAK | 72.0 | 8 | 103 | 5 | 54.0 | Defendente/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.030130811035633087 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 642 | PASS | WINSTREAK | 72.0 | 8 | 117 | 5 | 54.0 | Defendente/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.039918072521686554 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 652 | PASS | WINSTREAK | 72.0 | 8 | 131 | 5 | 54.0 | Defendente/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0501258559525013 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 662 | PASS | WINSTREAK | 72.0 | 8 | 144 | 5 | 54.0 | Defendente/DA_18_Lux_Sunbeam | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.059928473085165024 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.019615383818745613 | 0.0 | 0.0 | +— / -36f58657-5835-4389-95e9-a7d26464c2aa |
| Jogador 3 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.21530985832214355 | 0.0 | 0.0 | +2cf5ccdc-76f4-4fc8-b12c-7b3b68b1b2c8 / -— |
| Jogador 3 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_RekSai | MOVE_BENCH, SELL, PASS | True | True | 0.32533809542655945 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_RekSai | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_RekSai | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9699749946594238 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_RekSai | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 13 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_RekSai | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29290837049484253 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_RekSai | BUY, MOVE_BOARD, PASS | True | True | 0.05865562707185745 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 15 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1701892912387848 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4150305688381195 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.154851496219635 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.0033023867290467024 | 0.0 | 0.0 | +405de1b8-45c1-4b7f-b044-f12b819507c3 / -— |
| Jogador 3 | 1-3 | 25 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Murkwolf18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48899999260902405 | 0.0 | 0.0 | +— / -405de1b8-45c1-4b7f-b044-f12b819507c3 |
| Jogador 3 | 1-3 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 27 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 48 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.26586347818374634 | 0.0 | 0.0 | +d15ca853-2585-49d0-9d7f-339dae104062 / -— |
| Jogador 3 | 1-4 | 49 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07784928381443024 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 50 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2186342030763626 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 51 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7037144899368286 | 0.0 | 0.0 | +— / -bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 1-4 | 52 | BUY_XP | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.04450000077486038 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 53 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_Scuttlecrab18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 72 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9552179574966431 | 0.0 | 0.0 | +c70251e8-af44-4466-808f-d49e9e5f57e9 / -— |
| Jogador 3 | 2-1 | 73 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09680510312318802 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 74 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 75 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 92 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1154931783676147 | 0.0 | 0.0 | +e5a28bd6-35ef-4cb0-801c-68c64d65b8eb / -c70251e8-af44-4466-808f-d49e9e5f57e9,d15ca853-2585-49d0-9d7f-339dae104062 |
| Jogador 3 | 2-2 | 93 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 4.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45604249835014343 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 94 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.29928159713745117 | 0.0 | 0.0 | +8a68772c-3f02-4f2e-882b-4fa69fbb6750 / -— |
| Jogador 3 | 2-2 | 95 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42014259099960327 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 96 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 97 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 98 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 112 | MOVE_BOARD | STABILIZE | 93.0 | 4 | 8 | 0 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06010375916957855 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 113 | BUY | STABILIZE | 93.0 | 4 | 8 | 0 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.013362291269004345 | 0.0 | 0.0 | +29f10cb7-6575-47ca-b583-057992a08253 / -— |
| Jogador 3 | 2-3 | 114 | MOVE_BENCH | STABILIZE | 93.0 | 4 | 5 | 0 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6930817365646362 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 115 | BUY_XP | STABILIZE | 93.0 | 4 | 5 | 0 | 16.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.037300001829862595 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 116 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 1 | 0 | 16.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6168332099914551 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 117 | MOVE_BOARD | STABILIZE | 93.0 | 5 | 1 | 0 | 24.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BOARD, PASS | True | True | 0.039354316890239716 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 118 | MOVE_BOARD | STABILIZE | 93.0 | 5 | 1 | 0 | 24.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BOARD, PASS | True | True | 0.029725274071097374 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 119 | MOVE_BOARD | STABILIZE | 93.0 | 5 | 1 | 0 | 24.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 120 | MOVE_BOARD | STABILIZE | 93.0 | 5 | 1 | 0 | 24.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BOARD, PASS | True | True | 0.017445070669054985 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 121 | MOVE_BOARD | STABILIZE | 93.0 | 5 | 1 | 0 | 24.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BOARD, PASS | True | True | -0.11900042742490768 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 122 | PASS | STABILIZE | 93.0 | 5 | 1 | 0 | 24.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 136 | BUY | STABILIZE | 93.0 | 5 | 7 | 0 | 24.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2878846824169159 | 0.0 | 0.0 | +2a2066ee-841b-49d5-8b82-1d47feb36d8c / -— |
| Jogador 3 | 2-4 | 137 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 4 | 0 | 24.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5786264538764954 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 138 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 4 | 0 | 24.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08394283056259155 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 139 | PASS | STABILIZE | 93.0 | 5 | 4 | 0 | 28.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 156 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 9 | 0 | 28.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3851032555103302 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 157 | BUY | STABILIZE | 93.0 | 5 | 9 | 0 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5338210463523865 | 0.0 | 0.0 | +226a1062-8e9a-4652-9da7-a2f215fa46ae / -— |
| Jogador 3 | 2-5 | 158 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 7 | 0 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07250635325908661 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 159 | BUY_XP | STABILIZE | 93.0 | 5 | 7 | 0 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 160 | SELL | STABILIZE | 93.0 | 5 | 3 | 0 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003006024518981576 | 0.0 | 0.0 | +— / -2cf5ccdc-76f4-4fc8-b12c-7b3b68b1b2c8 |
| Jogador 3 | 2-5 | 161 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 4 | 0 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35378360748291016 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 162 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 4 | 0 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0537598691880703 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 163 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 4 | 0 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6255270838737488 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 164 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 4 | 0 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3537833094596863 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 165 | PASS | STABILIZE | 93.0 | 5 | 4 | 0 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 177 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 11 | 1 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05357348173856735 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 178 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 11 | 1 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4273831248283386 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 179 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 11 | 1 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1199830025434494 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 180 | MOVE_BENCH | STABILIZE | 93.0 | 5 | 11 | 1 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3537832498550415 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 181 | SELL | STABILIZE | 93.0 | 5 | 11 | 1 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7334088087081909 | 0.0 | 0.0 | +— / -226a1062-8e9a-4652-9da7-a2f215fa46ae |
| Jogador 3 | 2-6 | 182 | BUY | STABILIZE | 93.0 | 5 | 13 | 1 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.535575807094574 | 0.0 | 0.0 | +07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 / -— |
| Jogador 3 | 2-6 | 183 | BUY_XP | STABILIZE | 93.0 | 5 | 11 | 1 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 184 | BUY_XP | STABILIZE | 93.0 | 5 | 7 | 0 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03189999982714653 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 185 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 3 | 0 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5317984223365784 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 186 | MOVE_BOARD | STABILIZE | 93.0 | 6 | 3 | 0 | 32.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.036966722458601 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 187 | PASS | STABILIZE | 93.0 | 6 | 3 | 0 | 32.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 198 | BUY | STABILIZE | 86.0 | 6 | 8 | 0 | 32.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9851731657981873 | 0.0 | 0.0 | +79786887-d318-4836-b2f0-c0f03e86cbe5 / -— |
| Jogador 3 | 2-7 | 199 | MOVE_BENCH | STABILIZE | 86.0 | 6 | 5 | 0 | 32.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 200 | MOVE_BENCH | STABILIZE | 86.0 | 6 | 5 | 0 | 32.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01257895864546299 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 201 | MOVE_BENCH | STABILIZE | 86.0 | 6 | 5 | 0 | 32.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3475167155265808 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 202 | MOVE_BENCH | STABILIZE | 86.0 | 6 | 5 | 0 | 32.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 203 | PASS | STABILIZE | 86.0 | 6 | 5 | 0 | 32.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 218 | MOVE_BENCH | STABILIZE | 86.0 | 6 | 10 | 1 | 32.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04752394184470177 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 219 | MOVE_BENCH | STABILIZE | 86.0 | 6 | 10 | 1 | 32.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41519829630851746 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 220 | MOVE_BOARD | STABILIZE | 86.0 | 6 | 10 | 1 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1381131112575531 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 221 | PASS | STABILIZE | 86.0 | 6 | 10 | 1 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 238 | MOVE_BOARD | STABILIZE | 86.0 | 6 | 17 | 1 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 239 | BUY_XP | STABILIZE | 86.0 | 6 | 17 | 1 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 240 | BUY_XP | STABILIZE | 86.0 | 6 | 13 | 1 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 241 | BUY_XP | STABILIZE | 86.0 | 6 | 9 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 242 | BUY_XP | STABILIZE | 86.0 | 6 | 5 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 243 | SELL | STABILIZE | 86.0 | 6 | 1 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36752739548683167 | 0.0 | 0.0 | +— / -c83ad0c5-f046-4834-8d0e-6dac3e49cdef |
| Jogador 3 | 3-2 | 244 | MOVE_BOARD | STABILIZE | 86.0 | 6 | 2 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.032957449555397034 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 245 | BUY | STABILIZE | 86.0 | 6 | 2 | 0 | 36.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.0536615364253521 | 0.0 | 0.0 | +fd3ab6e7-a3e5-4a03-8aa6-a80f6c0c1f47 / -— |
| Jogador 3 | 3-2 | 246 | SELL | STABILIZE | 86.0 | 6 | 0 | 0 | 36.0 | Vanguarda/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18007692694664001 | 0.0 | 0.0 | +— / -fd3ab6e7-a3e5-4a03-8aa6-a80f6c0c1f47 |
| Jogador 3 | 3-2 | 247 | MOVE_BOARD | STABILIZE | 86.0 | 6 | 2 | 0 | 36.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.022793645039200783 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 248 | PASS | STABILIZE | 86.0 | 6 | 2 | 0 | 36.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 256 | BUY | STABILIZE | 76.0 | 6 | 7 | 0 | 36.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.26500409841537476 | 0.0 | 0.0 | +527f78df-1e51-4731-9175-1c4812aa82ad / -— |
| Jogador 3 | 3-3 | 257 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 3 | 0 | 36.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5024519562721252 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 258 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 3 | 0 | 38.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.127062126994133 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 259 | PASS | STABILIZE | 76.0 | 6 | 3 | 0 | 38.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 275 | BUY | STABILIZE | 76.0 | 6 | 9 | 0 | 38.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19627435505390167 | 0.0 | 0.0 | +f5c14a50-b095-4a36-995f-2a8514e46f1c / -— |
| Jogador 3 | 3-4 | 276 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 6 | 0 | 38.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 277 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 6 | 0 | 38.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04875248298048973 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 278 | BUY_XP | STABILIZE | 76.0 | 6 | 6 | 0 | 38.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 279 | SELL | STABILIZE | 76.0 | 6 | 2 | 0 | 38.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24627435207366943 | 0.0 | 0.0 | +— / -f5c14a50-b095-4a36-995f-2a8514e46f1c |
| Jogador 3 | 3-4 | 280 | MOVE_BENCH | STABILIZE | 76.0 | 6 | 5 | 0 | 38.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 281 | SELL | STABILIZE | 76.0 | 6 | 5 | 0 | 38.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7590000033378601 | 0.0 | 0.0 | +— / -8a68772c-3f02-4f2e-882b-4fa69fbb6750 |
| Jogador 3 | 3-4 | 282 | PASS | STABILIZE | 76.0 | 6 | 8 | 0 | 38.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 292 | BUY | STABILIZE | 76.0 | 6 | 13 | 1 | 38.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.04458684101700783 | 0.0 | 0.0 | +ccdd8153-af58-4fe7-994c-d49f0a7a17f8 / -— |
| Jogador 3 | 3-5 | 293 | BUY | STABILIZE | 76.0 | 6 | 9 | 0 | 38.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17709305882453918 | 0.0 | 0.0 | +a9c52953-4532-455b-851f-04079adfd354 / -— |
| Jogador 3 | 3-5 | 294 | MOVE_BOARD | STABILIZE | 76.0 | 6 | 6 | 0 | 38.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 295 | BUY_XP | STABILIZE | 76.0 | 6 | 6 | 0 | 38.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06729999929666519 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 296 | MOVE_BENCH | STABILIZE | 76.0 | 7 | 2 | 0 | 38.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4325528144836426 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 297 | MOVE_BOARD | STABILIZE | 76.0 | 7 | 2 | 0 | 46.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017798790708184242 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 298 | MOVE_BOARD | STABILIZE | 76.0 | 7 | 2 | 0 | 46.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1213110089302063 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 299 | PASS | STABILIZE | 76.0 | 7 | 2 | 0 | 46.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 312 | BUY | STABILIZE | 64.0 | 7 | 7 | 0 | 46.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7458326816558838 | 0.0 | 0.0 | +0e31b1ec-3ead-480e-8577-f59bb5486d00 / -— |
| Jogador 3 | 3-6 | 313 | PASS | STABILIZE | 64.0 | 7 | 5 | 0 | 46.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 332 | BUY | STABILIZE | 64.0 | 7 | 11 | 1 | 46.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48684582114219666 | 0.0 | 0.0 | +bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed / -— |
| Jogador 3 | 3-7 | 333 | PASS | STABILIZE | 64.0 | 7 | 8 | 0 | 46.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 352 | PASS | STABILIZE | 64.0 | 7 | 13 | 1 | 46.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 372 | PASS | STABILIZE | 51.0 | 7 | 19 | 1 | 46.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 392 | BUY | STABILIZE | 51.0 | 7 | 27 | 2 | 46.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7567574977874756 | 0.0 | 0.0 | +3f488391-7117-4e28-b6cc-7416722351d4 / -— |
| Jogador 3 | 4-3 | 393 | PASS | STABILIZE | 51.0 | 7 | 24 | 2 | 46.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 412 | PASS | STABILIZE | 38.0 | 7 | 31 | 3 | 46.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 432 | BUY | STABILIZE | 38.0 | 7 | 39 | 3 | 46.0 | Vanguarda/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7997522950172424 | 0.0 | 0.0 | +84a3b0f5-c448-4fe1-b001-5ceff2ed306a / -a9c52953-4532-455b-851f-04079adfd354,bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed |
| Jogador 3 | 4-5 | 433 | BUY | STABILIZE | 38.0 | 7 | 36 | 3 | 46.0 | Vanguarda/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32184016704559326 | 0.0 | 0.0 | +bb51728e-fcc5-4950-ad03-c864c51c2371 / -— |
| Jogador 3 | 4-5 | 434 | BUY | STABILIZE | 38.0 | 7 | 33 | 3 | 46.0 | Vanguarda/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1202133521437645 | 0.0 | 0.0 | +17170204-1921-4cf1-b92b-cc73bb0701ea / -— |
| Jogador 3 | 4-5 | 435 | PASS | STABILIZE | 38.0 | 7 | 30 | 3 | 46.0 | Vanguarda/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 452 | BUY | STABILIZE | 26.0 | 7 | 39 | 3 | 46.0 | Vanguarda/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18793626129627228 | 0.0 | 0.0 | +f444bf9a-0e92-4a76-b4d0-9e1bac73cb77 / -— |
| Jogador 3 | 4-6 | 453 | BUY | STABILIZE | 26.0 | 7 | 36 | 3 | 46.0 | Vanguarda/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20569010078907013 | 0.0 | 0.0 | +8d6123c4-0ba0-4ff7-b01b-57c4f9e8780e / -— |
| Jogador 3 | 4-6 | 454 | PASS | STABILIZE | 26.0 | 7 | 33 | 3 | 46.0 | Vanguarda/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 472 | BUY | STABILIZE | 26.0 | 7 | 42 | 4 | 46.0 | Vanguarda/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8477711081504822 | 0.0 | 0.0 | +f3e882b5-333e-44e3-ae82-cacacc8b1137 / -2a2066ee-841b-49d5-8b82-1d47feb36d8c,3f488391-7117-4e28-b6cc-7416722351d4 |
| Jogador 3 | 4-7 | 473 | BUY | STABILIZE | 26.0 | 7 | 39 | 3 | 40.0 | Vanguarda/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3070218861103058 | 0.0 | 0.0 | +cba152f4-af54-4d82-a35d-67aa165174be / -— |
| Jogador 3 | 4-7 | 474 | PASS | STABILIZE | 26.0 | 7 | 36 | 3 | 40.0 | Vanguarda/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 488 | MOVE_BENCH | STABILIZE | 26.0 | 7 | 36 | 3 | 40.0 | Vanguarda/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.527041494846344 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 492 | EQUIP_FROM_INVENTORY | STABILIZE | 26.0 | 7 | 44 | 4 | 44.0 | Vanguarda/DA_Vi18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 493 | PASS | STABILIZE | 26.0 | 7 | 44 | 4 | 44.0 | Vanguarda/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 510 | BUY | ALL_IN | 11.0 | 7 | 53 | 5 | 44.0 | Vanguarda/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.11188583076000214 | 0.0 | 0.0 | +362f7357-283e-4f88-bff3-ffa6314af821 / -— |
| Jogador 3 | 5-2 | 511 | PASS | ALL_IN | 11.0 | 7 | 50 | 5 | 44.0 | Vanguarda/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.1436000019311905 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 522 | PASS | ALL_IN | 0.0 | 7 | 50 | 5 | 0.0 | Vanguarda/DA_Vi18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 542 | PASS | ALL_IN | 0.0 | 7 | 50 | 5 | 0.0 | Vanguarda/DA_Vi18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 562 | PASS | ALL_IN | 0.0 | 7 | 50 | 5 | 0.0 | Vanguarda/DA_Vi18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 582 | PASS | ALL_IN | 0.0 | 7 | 50 | 5 | 0.0 | Vanguarda/DA_Vi18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 602 | PASS | ALL_IN | 0.0 | 7 | 50 | 5 | 0.0 | Vanguarda/DA_Vi18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 622 | PASS | ALL_IN | 0.0 | 7 | 50 | 5 | 0.0 | Vanguarda/DA_Vi18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-2 | 632 | PASS | ALL_IN | 0.0 | 7 | 50 | 5 | 0.0 | Vanguarda/DA_Vi18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-3 | 642 | PASS | ALL_IN | 0.0 | 7 | 50 | 5 | 0.0 | Vanguarda/DA_Vi18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-4 | 652 | PASS | ALL_IN | 0.0 | 7 | 50 | 5 | 0.0 | Vanguarda/DA_Vi18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-5 | 662 | PASS | ALL_IN | 0.0 | 7 | 50 | 5 | 0.0 | Vanguarda/DA_Vi18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.019615383818745613 | 0.0 | 0.0 | +— / -9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +1903eae4-bd37-4ed8-bbae-28177e859592 / -— |
| Jogador 4 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 9 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.28737619519233704 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.25464189052581787 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2530312240123749 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 13 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.1701892912387848 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.07498838752508163 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 15 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44836655259132385 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 16 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.154851496219635 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.12280712276697159 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.306484580039978 | 0.0 | 0.0 | +a19fc47b-fc81-49b2-bc25-d25d58b8deef / -— |
| Jogador 4 | 1-3 | 25 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5214616656303406 | 0.0 | 0.0 | +— / -a19fc47b-fc81-49b2-bc25-d25d58b8deef |
| Jogador 4 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.004783479031175375 | 0.0 | 0.0 | +3224c4b3-14ed-42e7-a497-24e0be0a691c / -— |
| Jogador 4 | 1-3 | 27 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Alistar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1127055212855339 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 28 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Alistar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03817160427570343 | 0.0 | 0.0 | +— / -95829f2e-ad17-448d-a385-fdcf81872dc8 |
| Jogador 4 | 1-3 | 29 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Alistar | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 48 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9770524501800537 | 0.0 | 0.0 | +eddd35aa-7d38-4d71-8984-e4768f06379e / -— |
| Jogador 4 | 1-4 | 49 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.027052402496338 | 0.0 | 0.0 | +— / -eddd35aa-7d38-4d71-8984-e4768f06379e |
| Jogador 4 | 1-4 | 50 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.977044403553009 | 0.0 | 0.0 | +cd27dcd8-0a45-4196-be66-fbe6eb4a0793 / -— |
| Jogador 4 | 1-4 | 51 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.027044415473938 | 0.0 | 0.0 | +— / -cd27dcd8-0a45-4196-be66-fbe6eb4a0793 |
| Jogador 4 | 1-4 | 52 | BUY_XP | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.04450000077486038 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 53 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Alistar | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 72 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3069842457771301 | 0.0 | 0.0 | +c05579e6-aa73-434f-8a91-c58d68a81ced / -— |
| Jogador 4 | 2-1 | 73 | BUY | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9575209021568298 | 0.0 | 0.0 | +9819422b-1f51-47b5-89b7-9d6e906ddff2 / -— |
| Jogador 4 | 2-1 | 74 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43721482157707214 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 75 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 12.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0075209140777588 | 0.0 | 0.0 | +— / -9819422b-1f51-47b5-89b7-9d6e906ddff2 |
| Jogador 4 | 2-1 | 76 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Alistar | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.30979663133621216 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 77 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Alistar | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 78 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Alistar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 92 | BUY | STABILIZE | 96.0 | 4 | 7 | 0 | 12.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.34099283814430237 | 0.0 | 0.0 | +4e00fb2f-75c1-4580-bd09-cb73c31af01f / -— |
| Jogador 4 | 2-2 | 93 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 4 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030939772725105286 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 94 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 4 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17102721333503723 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 95 | SELL | STABILIZE | 96.0 | 4 | 4 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5340769290924072 | 0.0 | 0.0 | +— / -4e00fb2f-75c1-4580-bd09-cb73c31af01f |
| Jogador 4 | 2-2 | 96 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 7 | 0 | 12.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.310760498046875 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 97 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 7 | 0 | 12.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08777478337287903 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 98 | BUY_XP | STABILIZE | 96.0 | 4 | 7 | 0 | 12.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.026499999687075615 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 99 | BUY | STABILIZE | 96.0 | 5 | 3 | 0 | 12.0 | —/DA_18_Alistar | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.023211786523461342 | 0.0 | 0.0 | +e989a0cc-848a-4c45-b153-315877aee8f7 / -— |
| Jogador 4 | 2-2 | 100 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 1 | 0 | 12.0 | —/DA_18_Alistar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40846219658851624 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 101 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Alistar | BUY, MOVE_BOARD, PASS | True | True | 0.039354316890239716 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 102 | PASS | STABILIZE | 96.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Alistar | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 112 | BUY | STABILIZE | 96.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4762575924396515 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 4 | 2-3 | 113 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 4 | 0 | 16.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019473813474178314 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 114 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 4 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06809724122285843 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 115 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 4 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 116 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 4 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16319571435451508 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 117 | SELL | STABILIZE | 96.0 | 5 | 4 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0017692308174446225 | 0.0 | 0.0 | +— / -3224c4b3-14ed-42e7-a497-24e0be0a691c |
| Jogador 4 | 2-3 | 118 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 6 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.12289445847272873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 119 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 6 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.16236628592014313 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 120 | PASS | STABILIZE | 96.0 | 5 | 6 | 0 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 136 | BUY | STABILIZE | 91.0 | 5 | 11 | 1 | 18.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.02159690484404564 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 4 | 2-4 | 137 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 7 | 0 | 18.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3227403461933136 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 138 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09187524765729904 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 139 | PASS | STABILIZE | 91.0 | 5 | 7 | 0 | 24.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 156 | SELL | STABILIZE | 91.0 | 5 | 12 | 1 | 24.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06862760335206985 | 0.0 | 0.0 | +— / -1903eae4-bd37-4ed8-bbae-28177e859592 |
| Jogador 4 | 2-5 | 157 | BUY | STABILIZE | 91.0 | 5 | 13 | 1 | 24.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.48986753821372986 | 0.0 | 0.0 | +a92eca5d-299f-4f4d-a16b-d23981ef719f / -— |
| Jogador 4 | 2-5 | 158 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 10 | 1 | 24.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.270244836807251 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 159 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 10 | 1 | 22.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.799220621585846 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 160 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 10 | 1 | 24.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04432445764541626 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 161 | PASS | STABILIZE | 91.0 | 5 | 10 | 1 | 24.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 177 | BUY | STABILIZE | 85.0 | 5 | 17 | 1 | 24.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4400518536567688 | 0.0 | 0.0 | +b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a / -— |
| Jogador 4 | 2-6 | 178 | SELL | STABILIZE | 85.0 | 5 | 14 | 1 | 24.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49005183577537537 | 0.0 | 0.0 | +— / -b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a |
| Jogador 4 | 2-6 | 179 | MOVE_BENCH | STABILIZE | 85.0 | 5 | 17 | 1 | 24.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07207825034856796 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 180 | MOVE_BENCH | STABILIZE | 85.0 | 5 | 17 | 1 | 22.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7970163822174072 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 181 | PASS | STABILIZE | 85.0 | 5 | 17 | 1 | 24.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 198 | BUY | STABILIZE | 79.0 | 5 | 24 | 2 | 24.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.362099289894104 | 0.0 | 0.0 | +5e247068-fe03-467e-9e7d-ab85ade7fdae / -— |
| Jogador 4 | 2-7 | 199 | MOVE_BENCH | STABILIZE | 79.0 | 5 | 21 | 2 | 24.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49243688583374023 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 200 | MOVE_BENCH | STABILIZE | 79.0 | 5 | 21 | 2 | 24.0 | Lunar/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26898321509361267 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 201 | MOVE_BENCH | STABILIZE | 79.0 | 5 | 21 | 2 | 22.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7850618362426758 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 202 | MOVE_BENCH | STABILIZE | 79.0 | 5 | 21 | 2 | 24.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06880822777748108 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 203 | PASS | STABILIZE | 79.0 | 5 | 21 | 2 | 24.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 218 | BUY | STABILIZE | 79.0 | 5 | 29 | 2 | 24.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7539387941360474 | 0.0 | 0.0 | +74fe48c1-d955-4b0d-b832-39d4c86049dc / -— |
| Jogador 4 | 3-1 | 219 | MOVE_BENCH | STABILIZE | 79.0 | 5 | 27 | 2 | 24.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28724274039268494 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 220 | MOVE_BENCH | STABILIZE | 79.0 | 5 | 27 | 2 | 22.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.822136402130127 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 221 | MOVE_BENCH | STABILIZE | 79.0 | 5 | 27 | 2 | 24.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02513447031378746 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 222 | PASS | STABILIZE | 79.0 | 5 | 27 | 2 | 24.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007499999832361937 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 238 | BUY | SLOWROLL | 68.0 | 5 | 35 | 3 | 24.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05808952450752258 | 0.0 | 0.0 | +421bcbcb-ecb2-4af8-88d4-7be6cd284d27 / -— |
| Jogador 4 | 3-2 | 239 | MOVE_BENCH | SLOWROLL | 68.0 | 5 | 32 | 3 | 24.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30562400817871094 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 240 | BUY | SLOWROLL | 68.0 | 5 | 32 | 3 | 22.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6978307366371155 | 0.0 | 0.0 | +d71a866d-0c5a-41c2-9996-0e179f062aa2 / -— |
| Jogador 4 | 3-2 | 241 | MOVE_BENCH | SLOWROLL | 68.0 | 5 | 31 | 3 | 22.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7863746285438538 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 242 | SELL | SLOWROLL | 68.0 | 5 | 31 | 3 | 28.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6416632533073425 | 0.0 | 0.0 | +— / -9e7d1da0-5190-4348-81b4-3a3f2129a8e5 |
| Jogador 4 | 3-2 | 243 | PASS | SLOWROLL | 68.0 | 5 | 32 | 3 | 28.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 256 | BUY | SLOWROLL | 56.0 | 5 | 42 | 4 | 28.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3093762993812561 | 0.0 | 0.0 | +58c38a13-23c5-4ac1-8601-f0636aeb33ab / -— |
| Jogador 4 | 3-3 | 257 | BUY | SLOWROLL | 56.0 | 5 | 39 | 3 | 28.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10268938541412354 | 0.0 | 0.0 | +409b32b9-5280-4d79-b5b2-871ed597ba56 / -— |
| Jogador 4 | 3-3 | 258 | PASS | SLOWROLL | 56.0 | 5 | 37 | 3 | 28.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 275 | BUY | SLOWROLL | 44.0 | 5 | 48 | 4 | 28.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.270054429769516 | 0.0 | 0.0 | +2acd0734-f0c3-42b1-9791-5c48e1aa46bc / -— |
| Jogador 4 | 3-4 | 276 | PASS | SLOWROLL | 44.0 | 5 | 46 | 4 | 28.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02250000089406967 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 292 | BUY | SLOWROLL | 44.0 | 6 | 58 | 5 | 28.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12277170270681381 | 0.0 | 0.0 | +62b9f2fe-f0ec-474d-9b5d-1c589c8fa2b2 / -— |
| Jogador 4 | 3-5 | 293 | PASS | SLOWROLL | 44.0 | 6 | 55 | 5 | 28.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04706495627760887 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 307 | MOVE_BENCH | SLOWROLL | 44.0 | 6 | 55 | 5 | 28.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4210474193096161 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 312 | BUY | STABILIZE | 31.0 | 6 | 68 | 5 | 34.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5753118395805359 | 0.0 | 0.0 | +8e1a5a7a-d27d-47c9-a197-b383c1c3da3b / -— |
| Jogador 4 | 3-6 | 313 | BUY | STABILIZE | 31.0 | 6 | 65 | 5 | 34.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4362066984176636 | 0.0 | 0.0 | +f722cd46-0c4e-42e7-80ff-4b910c28d572 / -— |
| Jogador 4 | 3-6 | 314 | PASS | STABILIZE | 31.0 | 6 | 62 | 5 | 34.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005068708211183548 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 332 | PASS | STABILIZE | 18.0 | 6 | 75 | 5 | 34.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012229474261403084 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 352 | PASS | STABILIZE | 18.0 | 6 | 88 | 5 | 34.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.020212503150105476 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 372 | PASS | ALL_IN | 4.0 | 6 | 101 | 5 | 34.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07877159863710403 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 392 | PASS | ALL_IN | 0.0 | 6 | 101 | 5 | 0.0 | Adaptador/DA_18_Aphelios | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 412 | PASS | ALL_IN | 0.0 | 6 | 101 | 5 | 0.0 | Adaptador/DA_18_Aphelios | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 432 | PASS | ALL_IN | 0.0 | 6 | 101 | 5 | 0.0 | Adaptador/DA_18_Aphelios | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 452 | PASS | ALL_IN | 0.0 | 6 | 101 | 5 | 0.0 | Adaptador/DA_18_Aphelios | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 472 | PASS | ALL_IN | 0.0 | 6 | 101 | 5 | 0.0 | Adaptador/DA_18_Aphelios | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 492 | PASS | ALL_IN | 0.0 | 6 | 101 | 5 | 0.0 | Adaptador/DA_18_Aphelios | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 510 | PASS | ALL_IN | 0.0 | 6 | 101 | 5 | 0.0 | Adaptador/DA_18_Aphelios | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 522 | PASS | ALL_IN | 0.0 | 6 | 101 | 5 | 0.0 | Adaptador/DA_18_Aphelios | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 542 | PASS | ALL_IN | 0.0 | 6 | 101 | 5 | 0.0 | Adaptador/DA_18_Aphelios | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 562 | PASS | ALL_IN | 0.0 | 6 | 101 | 5 | 0.0 | Adaptador/DA_18_Aphelios | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 582 | PASS | ALL_IN | 0.0 | 6 | 101 | 5 | 0.0 | Adaptador/DA_18_Aphelios | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 602 | PASS | ALL_IN | 0.0 | 6 | 101 | 5 | 0.0 | Adaptador/DA_18_Aphelios | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 622 | PASS | ALL_IN | 0.0 | 6 | 101 | 5 | 0.0 | Adaptador/DA_18_Aphelios | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-2 | 632 | PASS | ALL_IN | 0.0 | 6 | 101 | 5 | 0.0 | Adaptador/DA_18_Aphelios | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-3 | 642 | PASS | ALL_IN | 0.0 | 6 | 101 | 5 | 0.0 | Adaptador/DA_18_Aphelios | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-4 | 652 | PASS | ALL_IN | 0.0 | 6 | 101 | 5 | 0.0 | Adaptador/DA_18_Aphelios | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-5 | 662 | PASS | ALL_IN | 0.0 | 6 | 101 | 5 | 0.0 | Adaptador/DA_18_Aphelios | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 9 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.27265432476997375 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.027269404381513596 | 0.0 | 0.0 | +df7d3860-9b2e-45ed-b564-281d95e64e82 / -— |
| Jogador 5 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3084299862384796 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 13 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.17653366923332214 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 14 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.28098976612091064 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 25 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5168516635894775 | 0.0 | 0.0 | +— / -7098795b-11bf-4b73-837a-87f5d8aece4c |
| Jogador 5 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.012894115410745144 | 0.0 | 0.0 | +4a7ac9c5-c110-4566-80e5-25d9e6033799 / -— |
| Jogador 5 | 1-3 | 27 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37192055583000183 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 28 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | -0.14186546206474304 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 29 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_Murkwolf18 | MOVE_BOARD, PASS | True | True | 0.16639362275600433 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 30 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_Murkwolf18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 48 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3293846845626831 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 49 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_Murkwolf18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19185180962085724 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 50 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Sejuani | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3089999854564667 | 0.0 | 0.0 | +— / -4a7ac9c5-c110-4566-80e5-25d9e6033799 |
| Jogador 5 | 1-4 | 51 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 72 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2662152349948883 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 73 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39309361577033997 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 74 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.32666483521461487 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 75 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 76 | PASS | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 92 | BUY | STABILIZE | 96.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.26719367504119873 | 0.0 | 0.0 | +68cd8ae3-399f-461f-89a8-189d7b0a6b59 / -— |
| Jogador 5 | 2-2 | 93 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 6 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10894233733415604 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 94 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 6 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04875248298048973 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 95 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 6 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2056483030319214 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 96 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 6 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17969462275505066 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 97 | SELL | STABILIZE | 96.0 | 4 | 6 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.036981817334890366 | 0.0 | 0.0 | +— / -1934c7ef-cc22-45b3-bed9-01aea61ffbdb |
| Jogador 5 | 2-2 | 98 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 8 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.036966722458601 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 99 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 8 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.16276787221431732 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 100 | BUY | STABILIZE | 96.0 | 4 | 8 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.23468877375125885 | 0.0 | 0.0 | +0debca82-3a2a-44ba-af48-83211d5e5243 / -— |
| Jogador 5 | 2-2 | 101 | SELL | STABILIZE | 96.0 | 4 | 5 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5002307891845703 | 0.0 | 0.0 | +— / -0debca82-3a2a-44ba-af48-83211d5e5243 |
| Jogador 5 | 2-2 | 102 | PASS | STABILIZE | 96.0 | 4 | 8 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 112 | BUY | STABILIZE | 96.0 | 4 | 14 | 1 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4598371386528015 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -— |
| Jogador 5 | 2-3 | 113 | SELL | STABILIZE | 96.0 | 4 | 13 | 1 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5098371505737305 | 0.0 | 0.0 | +— / -abde1e81-f452-47ad-9f1e-45efb138f86d |
| Jogador 5 | 2-3 | 114 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 14 | 1 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.13701719045639038 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 115 | BUY_XP | STABILIZE | 96.0 | 4 | 14 | 1 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 116 | BUY_XP | STABILIZE | 96.0 | 4 | 10 | 1 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 117 | BUY | STABILIZE | 96.0 | 5 | 6 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3964536488056183 | 0.0 | 0.0 | +0da2c93c-0c62-4fe0-94ff-688f086141e3 / -— |
| Jogador 5 | 2-3 | 118 | SELL | STABILIZE | 96.0 | 5 | 5 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44645363092422485 | 0.0 | 0.0 | +— / -0da2c93c-0c62-4fe0-94ff-688f086141e3 |
| Jogador 5 | 2-3 | 119 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 6 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.036966722458601 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 120 | PASS | STABILIZE | 96.0 | 5 | 6 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 136 | BUY | STABILIZE | 90.0 | 5 | 11 | 1 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.16263321042060852 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 137 | BUY | STABILIZE | 90.0 | 5 | 8 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4087090790271759 | 0.0 | 0.0 | +17cfefac-b43e-4a72-b6cb-1d559cc22ed1 / -— |
| Jogador 5 | 2-4 | 138 | SELL | STABILIZE | 90.0 | 5 | 6 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45870909094810486 | 0.0 | 0.0 | +— / -17cfefac-b43e-4a72-b6cb-1d559cc22ed1 |
| Jogador 5 | 2-4 | 139 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 8 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4208892285823822 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 140 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 8 | 0 | 24.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 141 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 8 | 0 | 24.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0417274534702301 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 142 | BUY_XP | STABILIZE | 90.0 | 5 | 8 | 0 | 24.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 143 | BUY_XP | STABILIZE | 90.0 | 5 | 4 | 0 | 24.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 144 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 0 | 0 | 24.0 | —/DA_18_MasterYi_AD | MOVE_BOARD, PASS | True | True | 0.024840479716658592 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 145 | PASS | STABILIZE | 90.0 | 5 | 0 | 0 | 24.0 | —/DA_18_MasterYi_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 156 | BUY | STABILIZE | 90.0 | 5 | 5 | 0 | 24.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03225110471248627 | 0.0 | 0.0 | +486e92ad-4dcf-4c0e-a470-e0b87777d380 / -— |
| Jogador 5 | 2-5 | 157 | SELL | STABILIZE | 90.0 | 5 | 2 | 0 | 24.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48115384578704834 | 0.0 | 0.0 | +— / -486e92ad-4dcf-4c0e-a470-e0b87777d380 |
| Jogador 5 | 2-5 | 158 | PASS | STABILIZE | 90.0 | 5 | 5 | 0 | 24.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 177 | BUY | STABILIZE | 85.0 | 5 | 11 | 1 | 24.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.04775262996554375 | 0.0 | 0.0 | +ae570779-3ae8-49b3-acdb-607fc512fcea / -— |
| Jogador 5 | 2-6 | 178 | SELL | STABILIZE | 85.0 | 5 | 9 | 0 | 24.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11837998032569885 | 0.0 | 0.0 | +— / -ae570779-3ae8-49b3-acdb-607fc512fcea |
| Jogador 5 | 2-6 | 179 | BUY | STABILIZE | 85.0 | 5 | 11 | 1 | 24.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.5019198656082153 | 0.0 | 0.0 | +fa0e266f-ef5b-48c5-b9a3-511450e97169 / -— |
| Jogador 5 | 2-6 | 180 | SELL | STABILIZE | 85.0 | 5 | 10 | 1 | 24.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5620769262313843 | 0.0 | 0.0 | +— / -fa0e266f-ef5b-48c5-b9a3-511450e97169 |
| Jogador 5 | 2-6 | 181 | BUY_XP | STABILIZE | 85.0 | 5 | 11 | 1 | 24.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.07599999755620956 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 182 | BUY | STABILIZE | 85.0 | 6 | 7 | 0 | 24.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4075160324573517 | 0.0 | 0.0 | +b6a21130-c9dc-45ad-8ddb-9223b0ec8751 / -— |
| Jogador 5 | 2-6 | 183 | SELL | STABILIZE | 85.0 | 6 | 6 | 0 | 24.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45751604437828064 | 0.0 | 0.0 | +— / -b6a21130-c9dc-45ad-8ddb-9223b0ec8751 |
| Jogador 5 | 2-6 | 184 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 7 | 0 | 24.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.13239096105098724 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 185 | MOVE_BOARD | STABILIZE | 85.0 | 6 | 7 | 0 | 24.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 186 | PASS | STABILIZE | 85.0 | 6 | 7 | 0 | 24.0 | Congregação das Bruxas/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 198 | BUY | STABILIZE | 80.0 | 6 | 13 | 1 | 24.0 | Congregação das Bruxas/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.5013148188591003 | 0.0 | 0.0 | +6eee9a92-4235-46af-ae42-c38acd6847ef / -— |
| Jogador 5 | 2-7 | 199 | BUY | STABILIZE | 80.0 | 6 | 11 | 1 | 24.0 | Congregação das Bruxas/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2555021345615387 | 0.0 | 0.0 | +837b2d09-a207-4830-b36d-29e493bbcc22 / -— |
| Jogador 5 | 2-7 | 200 | SELL | STABILIZE | 80.0 | 6 | 9 | 0 | 24.0 | Congregação das Bruxas/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30550214648246765 | 0.0 | 0.0 | +— / -837b2d09-a207-4830-b36d-29e493bbcc22 |
| Jogador 5 | 2-7 | 201 | MOVE_BENCH | STABILIZE | 80.0 | 6 | 11 | 1 | 24.0 | Congregação das Bruxas/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6264411807060242 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 202 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 11 | 1 | 28.0 | Congregação das Bruxas/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.14408981800079346 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 203 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 11 | 1 | 28.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.1656503975391388 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 204 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 11 | 1 | 28.0 | Congregação das Bruxas/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.036966722458601 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 205 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 11 | 1 | 28.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.1381131112575531 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 206 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 11 | 1 | 28.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.12670545279979706 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 207 | PASS | STABILIZE | 80.0 | 6 | 11 | 1 | 28.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 218 | BUY | STABILIZE | 80.0 | 6 | 18 | 1 | 28.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2613216042518616 | 0.0 | 0.0 | +e8c36276-b932-45ba-b350-2d1cb339a019 / -— |
| Jogador 5 | 3-1 | 219 | MOVE_BOARD | STABILIZE | 80.0 | 6 | 15 | 1 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3363801836967468 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 220 | MOVE_BENCH | STABILIZE | 80.0 | 6 | 15 | 1 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06701284646987915 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 221 | PASS | STABILIZE | 80.0 | 6 | 15 | 1 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 238 | BUY | STABILIZE | 80.0 | 6 | 22 | 2 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6741551756858826 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -— |
| Jogador 5 | 3-2 | 239 | BUY | STABILIZE | 80.0 | 6 | 19 | 1 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005396100226789713 | 0.0 | 0.0 | +4d8c374c-264c-47d9-8cfc-78cbf64ceda0 / -— |
| Jogador 5 | 3-2 | 240 | PASS | STABILIZE | 80.0 | 6 | 17 | 1 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 256 | BUY | STABILIZE | 80.0 | 6 | 25 | 2 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18832452595233917 | 0.0 | 0.0 | +8a4d0946-b80f-4fbb-ab7c-d43c2697c34e / -— |
| Jogador 5 | 3-3 | 257 | BUY | STABILIZE | 80.0 | 6 | 21 | 2 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0182114876806736 | 0.0 | 0.0 | +1d7b6420-388f-4cb1-b25c-2e5a3dfec742 / -— |
| Jogador 5 | 3-3 | 258 | PASS | STABILIZE | 80.0 | 6 | 18 | 1 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 275 | PASS | STABILIZE | 68.0 | 6 | 24 | 2 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 292 | PASS | SLOWROLL | 68.0 | 6 | 31 | 3 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 312 | BUY | SLOWROLL | 68.0 | 6 | 40 | 4 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19313545525074005 | 0.0 | 0.0 | +1457cd1e-c240-4ce5-9217-a91bddfc8807 / -— |
| Jogador 5 | 3-6 | 313 | PASS | SLOWROLL | 68.0 | 6 | 38 | 3 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 332 | BUY | SLOWROLL | 56.0 | 6 | 46 | 4 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.046309035271406174 | 0.0 | 0.0 | +8fec6a15-a0ef-42d0-b295-19ac5bd78aa5 / -— |
| Jogador 5 | 3-7 | 333 | PASS | SLOWROLL | 56.0 | 6 | 43 | 4 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 352 | BUY | SLOWROLL | 56.0 | 6 | 52 | 5 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18586163222789764 | 0.0 | 0.0 | +60255a84-4f78-49f0-a4f1-d598704c7ee7 / -— |
| Jogador 5 | 4-1 | 353 | PASS | SLOWROLL | 56.0 | 6 | 49 | 4 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04500000178813934 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 372 | PASS | SLOWROLL | 43.0 | 6 | 59 | 5 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0035889779683202505 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 392 | PASS | STABILIZE | 29.0 | 6 | 70 | 5 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08673300594091415 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 412 | PASS | ALL_IN | 15.0 | 6 | 81 | 5 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17923200130462646 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 432 | PASS | ALL_IN | 15.0 | 6 | 92 | 5 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1991194784641266 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 452 | PASS | ALL_IN | 1.0 | 6 | 104 | 5 | 28.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2556408643722534 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 472 | PASS | ALL_IN | 0.0 | 6 | 104 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 492 | PASS | ALL_IN | 0.0 | 6 | 104 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 510 | PASS | ALL_IN | 0.0 | 6 | 104 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 522 | PASS | ALL_IN | 0.0 | 6 | 104 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 542 | PASS | ALL_IN | 0.0 | 6 | 104 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 562 | PASS | ALL_IN | 0.0 | 6 | 104 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 582 | PASS | ALL_IN | 0.0 | 6 | 104 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 602 | PASS | ALL_IN | 0.0 | 6 | 104 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 622 | PASS | ALL_IN | 0.0 | 6 | 104 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 632 | PASS | ALL_IN | 0.0 | 6 | 104 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 642 | PASS | ALL_IN | 0.0 | 6 | 104 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 652 | PASS | ALL_IN | 0.0 | 6 | 104 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 662 | PASS | ALL_IN | 0.0 | 6 | 104 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0013076922623440623 | 0.0 | 0.0 | +— / -698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +9002992e-4dcd-4fec-939c-87393464a41d / -— |
| Jogador 6 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 9 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.28737619519233704 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.04858612269163132 | 0.0 | 0.0 | +4d0bf502-ac30-4cdb-9da7-4f9a7ab054b1 / -— |
| Jogador 6 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2912987470626831 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 13 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | -0.32645073533058167 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 14 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.00015411031199619174 | 0.0 | 0.0 | +f29b0444-8dd6-44a6-9a04-824febf737a0 / -— |
| Jogador 6 | 1-3 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49967682361602783 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 26 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | 0.14408981800079346 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 27 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Caitlyn | MOVE_BOARD, PASS | True | True | -0.3201245665550232 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 28 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Caitlyn | MOVE_BOARD, PASS | True | True | 0.179847851395607 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 29 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 48 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.019240504130721092 | 0.0 | 0.0 | +c19cf6a8-c66e-4670-b0fc-fb83453f22e7 / -— |
| Jogador 6 | 1-4 | 49 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Yunara | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48899999260902405 | 0.0 | 0.0 | +— / -c19cf6a8-c66e-4670-b0fc-fb83453f22e7 |
| Jogador 6 | 1-4 | 50 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 72 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.027847466990351677 | 0.0 | 0.0 | +75005e9c-56d1-48d6-815e-573e489e3dd7 / -— |
| Jogador 6 | 2-1 | 73 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9694250226020813 | 0.0 | 0.0 | +646fc826-453b-479f-97d1-8aa2a9d86dc3 / -— |
| Jogador 6 | 2-1 | 74 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4799444377422333 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 75 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 12.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2919284999370575 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 76 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17973603308200836 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 77 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7405862808227539 | 0.0 | 0.0 | +— / -646fc826-453b-479f-97d1-8aa2a9d86dc3 |
| Jogador 6 | 2-1 | 78 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.3224659860134125 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 79 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.14581196010112762 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 80 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.3177109360694885 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 81 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17935079336166382 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 82 | PASS | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 92 | BUY | STABILIZE | 95.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.45454248785972595 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 93 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 6 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.038481228053569794 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 94 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 6 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11622988432645798 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 95 | PASS | STABILIZE | 95.0 | 4 | 6 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 112 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 12 | 1 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33178484439849854 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 113 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 12 | 1 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03769022971391678 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 114 | PASS | STABILIZE | 90.0 | 4 | 12 | 1 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 136 | BUY | LOSS_STREAK | 83.0 | 4 | 19 | 1 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24516873061656952 | 0.0 | 0.0 | +a1c62c5f-385c-49ba-ac65-9dff28493faf / -— |
| Jogador 6 | 2-4 | 137 | MOVE_BENCH | LOSS_STREAK | 83.0 | 4 | 16 | 1 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22835946083068848 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 138 | SELL | LOSS_STREAK | 83.0 | 4 | 16 | 1 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024076923727989197 | 0.0 | 0.0 | +— / -f29b0444-8dd6-44a6-9a04-824febf737a0 |
| Jogador 6 | 2-4 | 139 | MOVE_BENCH | LOSS_STREAK | 83.0 | 4 | 18 | 1 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26832056045532227 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 140 | MOVE_BENCH | LOSS_STREAK | 83.0 | 4 | 18 | 1 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2914697825908661 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 141 | PASS | LOSS_STREAK | 83.0 | 4 | 18 | 1 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 156 | MOVE_BENCH | LOSS_STREAK | 83.0 | 4 | 25 | 2 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05387298762798309 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 157 | BUY | LOSS_STREAK | 83.0 | 4 | 25 | 2 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3086290657520294 | 0.0 | 0.0 | +c7d30607-e33e-4e6e-902a-3fd37223a8de / -— |
| Jogador 6 | 2-5 | 158 | MOVE_BENCH | STABILIZE | 83.0 | 4 | 23 | 2 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3409665524959564 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 159 | MOVE_BENCH | STABILIZE | 83.0 | 4 | 23 | 2 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29702675342559814 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 160 | PASS | STABILIZE | 83.0 | 4 | 23 | 2 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 177 | BUY | STABILIZE | 76.0 | 5 | 31 | 3 | 18.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8748182058334351 | 0.0 | 0.0 | +2938180d-94e5-4bb7-832e-baa51f820ba2 / -— |
| Jogador 6 | 2-6 | 178 | MOVE_BENCH | STABILIZE | 76.0 | 5 | 28 | 2 | 18.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.576775312423706 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 179 | MOVE_BOARD | STABILIZE | 76.0 | 5 | 28 | 2 | 24.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30979663133621216 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 180 | MOVE_BOARD | STABILIZE | 76.0 | 5 | 28 | 2 | 24.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 181 | PASS | STABILIZE | 76.0 | 5 | 28 | 2 | 24.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 198 | BUY | SLOWROLL | 76.0 | 5 | 36 | 3 | 24.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38565266132354736 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 199 | MOVE_BOARD | SLOWROLL | 76.0 | 5 | 33 | 3 | 24.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039354316890239716 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 200 | MOVE_BOARD | SLOWROLL | 76.0 | 5 | 33 | 3 | 24.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 201 | MOVE_BOARD | SLOWROLL | 76.0 | 5 | 33 | 3 | 24.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17992427945137024 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 202 | SELL | SLOWROLL | 76.0 | 5 | 33 | 3 | 24.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008288232609629631 | 0.0 | 0.0 | +— / -c7d30607-e33e-4e6e-902a-3fd37223a8de |
| Jogador 6 | 2-7 | 203 | MOVE_BOARD | SLOWROLL | 76.0 | 5 | 35 | 3 | 24.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25584542751312256 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 204 | MOVE_BOARD | SLOWROLL | 76.0 | 5 | 35 | 3 | 24.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13977457582950592 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 205 | PASS | SLOWROLL | 76.0 | 5 | 35 | 3 | 24.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 218 | BUY | SLOWROLL | 76.0 | 5 | 43 | 4 | 24.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2639719843864441 | 0.0 | 0.0 | +a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 / -— |
| Jogador 6 | 3-1 | 219 | MOVE_BOARD | SLOWROLL | 76.0 | 5 | 40 | 4 | 24.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27043604850769043 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 220 | MOVE_BOARD | SLOWROLL | 76.0 | 5 | 40 | 4 | 24.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 221 | PASS | SLOWROLL | 76.0 | 5 | 40 | 4 | 24.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02250000089406967 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 238 | BUY | SLOWROLL | 64.0 | 5 | 49 | 4 | 24.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8435772061347961 | 0.0 | 0.0 | +6e096b30-0b49-4a98-8596-8b05089793ae / -2938180d-94e5-4bb7-832e-baa51f820ba2,75005e9c-56d1-48d6-815e-573e489e3dd7 |
| Jogador 6 | 3-2 | 239 | MOVE_BENCH | SLOWROLL | 64.0 | 5 | 46 | 4 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6050195097923279 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 240 | MOVE_BOARD | SLOWROLL | 64.0 | 5 | 46 | 4 | 24.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2593608796596527 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 241 | BUY | SLOWROLL | 64.0 | 5 | 46 | 4 | 24.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7362948060035706 | 0.0 | 0.0 | +e29364db-c484-4e4d-954d-7f4940131ffc / -— |
| Jogador 6 | 3-2 | 242 | MOVE_BOARD | SLOWROLL | 64.0 | 5 | 45 | 4 | 24.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14466047286987305 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 243 | MOVE_BOARD | SLOWROLL | 64.0 | 5 | 45 | 4 | 24.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17997318506240845 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 244 | BUY_XP | SLOWROLL | 64.0 | 5 | 45 | 4 | 24.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 245 | BUY_XP | SLOWROLL | 64.0 | 5 | 41 | 4 | 24.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1080000028014183 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 246 | BUY_XP | SLOWROLL | 64.0 | 5 | 37 | 3 | 24.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 247 | BUY_XP | SLOWROLL | 64.0 | 5 | 33 | 3 | 24.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05420000106096268 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 248 | PASS | STABILIZE | 64.0 | 6 | 29 | 2 | 24.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007499999832361937 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 256 | BUY | SLOWROLL | 51.0 | 6 | 37 | 3 | 24.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24161173403263092 | 0.0 | 0.0 | +50f9a30c-27db-4ed0-804e-548f87950b17 / -— |
| Jogador 6 | 3-3 | 257 | BUY | SLOWROLL | 51.0 | 6 | 34 | 3 | 24.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.707788348197937 | 0.0 | 0.0 | +ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b / -— |
| Jogador 6 | 3-3 | 258 | MOVE_BOARD | SLOWROLL | 51.0 | 6 | 31 | 3 | 24.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23221850395202637 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 259 | MOVE_BOARD | SLOWROLL | 51.0 | 6 | 31 | 3 | 24.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26141127943992615 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 260 | PASS | SLOWROLL | 51.0 | 6 | 31 | 3 | 24.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 271 | MOVE_BENCH | SLOWROLL | 51.0 | 6 | 31 | 3 | 24.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5215966701507568 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 275 | BUY | SLOWROLL | 39.0 | 6 | 40 | 4 | 26.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17668937146663666 | 0.0 | 0.0 | +d056a271-6a74-4e71-bde6-087b97d2c527 / -— |
| Jogador 6 | 3-4 | 276 | MOVE_BOARD | SLOWROLL | 39.0 | 6 | 36 | 3 | 26.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17926807701587677 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 277 | MOVE_BOARD | SLOWROLL | 39.0 | 6 | 36 | 3 | 26.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 278 | PASS | SLOWROLL | 39.0 | 6 | 36 | 3 | 26.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 292 | BUY | SLOWROLL | 39.0 | 6 | 45 | 4 | 26.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7342720031738281 | 0.0 | 0.0 | +06db3a99-d008-406a-ac86-30884335d7c2 / -— |
| Jogador 6 | 3-5 | 293 | BUY | SLOWROLL | 39.0 | 6 | 42 | 4 | 26.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2949930429458618 | 0.0 | 0.0 | +6db008fd-a1dd-40ad-b3d2-583a4bbff9d4 / -— |
| Jogador 6 | 3-5 | 294 | PASS | SLOWROLL | 39.0 | 6 | 39 | 3 | 26.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 312 | BUY | STABILIZE | 28.0 | 6 | 48 | 4 | 26.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12767057120800018 | 0.0 | 0.0 | +cf68219b-1d38-45a1-98db-495871c932ea / -— |
| Jogador 6 | 3-6 | 313 | PASS | STABILIZE | 28.0 | 6 | 45 | 4 | 26.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 332 | BUY | ALL_IN | 15.0 | 6 | 56 | 5 | 26.0 | Feérico/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1707077920436859 | 0.0 | 0.0 | +891aea62-e06a-46d4-8250-a3d4a56e847d / -— |
| Jogador 6 | 3-7 | 333 | PASS | ALL_IN | 15.0 | 6 | 52 | 5 | 26.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050590358674526215 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 352 | PASS | ALL_IN | 15.0 | 6 | 64 | 5 | 26.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05609864741563797 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 372 | PASS | ALL_IN | 2.0 | 6 | 77 | 5 | 26.0 | Feérico/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06341270357370377 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 392 | PASS | ALL_IN | 0.0 | 6 | 77 | 5 | 0.0 | Feérico/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 412 | PASS | ALL_IN | 0.0 | 6 | 77 | 5 | 0.0 | Feérico/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 432 | PASS | ALL_IN | 0.0 | 6 | 77 | 5 | 0.0 | Feérico/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 452 | PASS | ALL_IN | 0.0 | 6 | 77 | 5 | 0.0 | Feérico/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 472 | PASS | ALL_IN | 0.0 | 6 | 77 | 5 | 0.0 | Feérico/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 492 | PASS | ALL_IN | 0.0 | 6 | 77 | 5 | 0.0 | Feérico/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 510 | PASS | ALL_IN | 0.0 | 6 | 77 | 5 | 0.0 | Feérico/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 522 | PASS | ALL_IN | 0.0 | 6 | 77 | 5 | 0.0 | Feérico/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 542 | PASS | ALL_IN | 0.0 | 6 | 77 | 5 | 0.0 | Feérico/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 562 | PASS | ALL_IN | 0.0 | 6 | 77 | 5 | 0.0 | Feérico/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 582 | PASS | ALL_IN | 0.0 | 6 | 77 | 5 | 0.0 | Feérico/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 602 | PASS | ALL_IN | 0.0 | 6 | 77 | 5 | 0.0 | Feérico/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 622 | PASS | ALL_IN | 0.0 | 6 | 77 | 5 | 0.0 | Feérico/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 632 | PASS | ALL_IN | 0.0 | 6 | 77 | 5 | 0.0 | Feérico/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-3 | 642 | PASS | ALL_IN | 0.0 | 6 | 77 | 5 | 0.0 | Feérico/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-4 | 652 | PASS | ALL_IN | 0.0 | 6 | 77 | 5 | 0.0 | Feérico/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-5 | 662 | PASS | ALL_IN | 0.0 | 6 | 77 | 5 | 0.0 | Feérico/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.019615383818745613 | 0.0 | 0.0 | +— / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987 |
| Jogador 7 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +c2a4318c-af60-41e2-8e14-c3ad967569a0 / -— |
| Jogador 7 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 9 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.28737619519233704 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.0015799786197021604 | 0.0 | 0.0 | +b21d3fc8-71ce-4669-b0ba-931c6e11cb69 / -— |
| Jogador 7 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2815883457660675 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 13 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.17468135058879852 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.9623193740844727 | 0.0 | 0.0 | +a529e9b4-89c2-47e0-b821-7269b112f8ef / -— |
| Jogador 7 | 1-2 | 15 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0123193264007568 | 0.0 | 0.0 | +— / -a529e9b4-89c2-47e0-b821-7269b112f8ef |
| Jogador 7 | 1-2 | 16 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.16698694229125977 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.24205608665943146 | 0.0 | 0.0 | +00a1ebb3-acfd-44df-9190-4f51a47d48c7 / -— |
| Jogador 7 | 1-2 | 18 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35220783948898315 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 20 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.09982795268297195 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 21 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3185639977455139 | 0.0 | 0.0 | +734c75dd-d0f3-4b9f-abe8-a228e23557a2 / -— |
| Jogador 7 | 1-3 | 25 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3573684096336365 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 26 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3767687976360321 | 0.0 | 0.0 | +— / -c2a4318c-af60-41e2-8e14-c3ad967569a0 |
| Jogador 7 | 1-3 | 27 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 48 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06592612713575363 | 0.0 | 0.0 | +a179e7d4-31e2-4a74-9905-0daede16517e / -— |
| Jogador 7 | 1-4 | 49 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49286553263664246 | 0.0 | 0.0 | +— / -a179e7d4-31e2-4a74-9905-0daede16517e |
| Jogador 7 | 1-4 | 50 | BUY_XP | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.04450000077486038 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 51 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_Scuttlecrab18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 72 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.35538917779922485 | 0.0 | 0.0 | +de82e676-8d8b-4437-958e-a8398a3cfade / -— |
| Jogador 7 | 2-1 | 73 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09607913345098495 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 74 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09084103256464005 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 75 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 92 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.11115534603595734 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 93 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2716406583786011 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 94 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03189999982714653 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 95 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Hecarim | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38238048553466797 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 96 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Hecarim | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 97 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Hecarim | BUY, MOVE_BOARD, PASS | True | True | 0.04408536106348038 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 98 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Hecarim | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 99 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Hecarim | BUY, MOVE_BOARD, PASS | True | True | 0.024840479716658592 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 100 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Hecarim | BUY, MOVE_BOARD, PASS | True | True | -0.13239096105098724 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 101 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Hecarim | BUY, MOVE_BOARD, PASS | True | True | 0.02728801965713501 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 102 | PASS | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Hecarim | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 112 | BUY | STABILIZE | 100.0 | 5 | 8 | 0 | 18.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9694114327430725 | 0.0 | 0.0 | +4367c039-e64e-4a3c-a49f-57cb2674a08f / -— |
| Jogador 7 | 2-3 | 113 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007239123806357384 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 114 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14294277131557465 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 115 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 116 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.054237235337495804 | 0.0 | 0.0 | +— / -b21d3fc8-71ce-4669-b0ba-931c6e11cb69 |
| Jogador 7 | 2-3 | 117 | BUY | STABILIZE | 100.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.02578849159181118 | 0.0 | 0.0 | +3ffefe44-52ff-4118-83fb-ae8237b6caa0 / -— |
| Jogador 7 | 2-3 | 118 | SELL | STABILIZE | 100.0 | 5 | 0 | 0 | 20.0 | —/DA_18_Hecarim | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4885384738445282 | 0.0 | 0.0 | +— / -3ffefe44-52ff-4118-83fb-ae8237b6caa0 |
| Jogador 7 | 2-3 | 119 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.017445070669054985 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 120 | PASS | STABILIZE | 100.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 136 | BUY | STABILIZE | 100.0 | 5 | 10 | 1 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3261948525905609 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 137 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 20.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2807047665119171 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 138 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0010158233344554901 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 139 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 22.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6495161056518555 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 140 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 20.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2788439691066742 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 141 | PASS | STABILIZE | 100.0 | 5 | 6 | 0 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 156 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 12 | 1 | 24.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029157958924770355 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 157 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 12 | 1 | 22.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31801003217697144 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 158 | PASS | STABILIZE | 100.0 | 5 | 12 | 1 | 24.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 177 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 20 | 2 | 24.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 178 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 20 | 2 | 24.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02723369002342224 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 179 | PASS | STABILIZE | 100.0 | 5 | 20 | 2 | 20.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 198 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 30 | 3 | 20.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2939576804637909 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 199 | SELL | SLOWROLL | 100.0 | 5 | 30 | 3 | 24.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7363510131835938 | 0.0 | 0.0 | +— / -de82e676-8d8b-4437-958e-a8398a3cfade |
| Jogador 7 | 2-7 | 200 | BUY | STABILIZE | 100.0 | 5 | 32 | 3 | 24.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.09796852618455887 | 0.0 | 0.0 | +584991bb-37b3-4ac1-8e29-14e0d74c5e78 / -— |
| Jogador 7 | 2-7 | 201 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 29 | 2 | 24.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7506112456321716 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 202 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 29 | 2 | 22.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27219629287719727 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 203 | PASS | STABILIZE | 100.0 | 5 | 29 | 2 | 26.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 218 | BUY_XP | STABILIZE | 100.0 | 5 | 38 | 3 | 26.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08889999985694885 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 219 | MOVE_BENCH | FAST8 | 100.0 | 6 | 34 | 3 | 26.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5442950129508972 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 220 | BUY | FAST8 | 100.0 | 6 | 34 | 3 | 30.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.11875107139348984 | 0.0 | 0.0 | +ad1693cd-1ab5-43a9-8164-25929b8bd68e / -— |
| Jogador 7 | 3-1 | 221 | BUY_XP | FAST8 | 100.0 | 6 | 32 | 3 | 30.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 222 | BUY_XP | STABILIZE | 100.0 | 6 | 28 | 2 | 30.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 223 | BUY_XP | STABILIZE | 100.0 | 6 | 24 | 2 | 30.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 224 | BUY_XP | STABILIZE | 100.0 | 6 | 20 | 2 | 30.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 225 | BUY_XP | STABILIZE | 100.0 | 6 | 16 | 1 | 30.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 226 | BUY_XP | STABILIZE | 100.0 | 6 | 12 | 1 | 30.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 227 | BUY_XP | STABILIZE | 100.0 | 6 | 8 | 0 | 30.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 228 | PASS | STABILIZE | 100.0 | 6 | 4 | 0 | 30.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 238 | BUY_XP | STABILIZE | 100.0 | 6 | 13 | 1 | 30.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 239 | BUY_XP | STABILIZE | 100.0 | 6 | 9 | 0 | 30.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.061900001019239426 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 240 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 5 | 0 | 30.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8224236965179443 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 241 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 5 | 0 | 30.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08540365099906921 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 242 | BUY | STABILIZE | 100.0 | 7 | 5 | 0 | 28.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13328298926353455 | 0.0 | 0.0 | +46320c4e-6bc0-49d6-b150-be378fa422cf / -— |
| Jogador 7 | 3-2 | 243 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 2 | 0 | 28.0 | Lutador/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 244 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 2 | 0 | 28.0 | Lutador/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.032957449555397034 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 245 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 2 | 0 | 28.0 | Lutador/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41994553804397583 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 246 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 2 | 0 | 34.0 | Lutador/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 247 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 2 | 0 | 34.0 | Lutador/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 248 | PASS | STABILIZE | 100.0 | 7 | 2 | 0 | 34.0 | Lutador/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 256 | BUY | STABILIZE | 100.0 | 7 | 11 | 1 | 34.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13493868708610535 | 0.0 | 0.0 | +f116ca4e-dbe8-457e-83a5-958525aa384a / -— |
| Jogador 7 | 3-3 | 257 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 8 | 0 | 34.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 258 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 8 | 0 | 34.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 259 | PASS | STABILIZE | 100.0 | 7 | 8 | 0 | 34.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 275 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 17 | 1 | 34.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13415248692035675 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 276 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 17 | 1 | 34.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6778324842453003 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 277 | PASS | STABILIZE | 100.0 | 7 | 17 | 1 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 292 | BUY | STABILIZE | 100.0 | 7 | 26 | 2 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22497624158859253 | 0.0 | 0.0 | +f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e / -— |
| Jogador 7 | 3-5 | 293 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 23 | 2 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2909073829650879 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 294 | MOVE_BOARD | STABILIZE | 100.0 | 7 | 23 | 2 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.042065247893333435 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 295 | SELL | STABILIZE | 100.0 | 7 | 23 | 2 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2749762535095215 | 0.0 | 0.0 | +— / -f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e |
| Jogador 7 | 3-5 | 296 | BUY | STABILIZE | 100.0 | 7 | 26 | 2 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7536977529525757 | 0.0 | 0.0 | +7c8b3027-1434-4346-95b3-5463e8a4aa9b / -— |
| Jogador 7 | 3-5 | 297 | BUY_XP | STABILIZE | 100.0 | 7 | 24 | 2 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 298 | BUY_XP | STABILIZE | 100.0 | 7 | 20 | 2 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 299 | BUY_XP | STABILIZE | 100.0 | 7 | 16 | 1 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 300 | BUY_XP | STABILIZE | 100.0 | 7 | 12 | 1 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 301 | BUY_XP | STABILIZE | 100.0 | 7 | 8 | 0 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 302 | PASS | STABILIZE | 100.0 | 7 | 4 | 0 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 312 | BUY | STABILIZE | 100.0 | 7 | 13 | 1 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1936269849538803 | 0.0 | 0.0 | +6caec849-54f8-4ec1-90a4-fc0587510013 / -— |
| Jogador 7 | 3-6 | 313 | PASS | STABILIZE | 100.0 | 7 | 9 | 0 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 332 | BUY | STABILIZE | 100.0 | 7 | 19 | 1 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7419376969337463 | 0.0 | 0.0 | +8a52858d-da47-4de9-8e91-8612788cb8fd / -— |
| Jogador 7 | 3-7 | 333 | PASS | STABILIZE | 100.0 | 7 | 15 | 1 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 352 | PASS | STABILIZE | 100.0 | 7 | 24 | 2 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 372 | PASS | FAST8 | 100.0 | 7 | 35 | 3 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 392 | BUY | FAST8 | 100.0 | 7 | 47 | 4 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09036365896463394 | 0.0 | 0.0 | +16acc555-c819-4f7c-b406-2f48f11ffc87 / -— |
| Jogador 7 | 4-3 | 393 | BUY | FAST8 | 100.0 | 7 | 43 | 4 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6129517555236816 | 0.0 | 0.0 | +72c247af-bdc3-410c-98dd-dd72b56f2818 / -— |
| Jogador 7 | 4-3 | 394 | PASS | FAST8 | 100.0 | 7 | 40 | 4 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04500000178813934 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 412 | BUY | FAST8 | 100.0 | 7 | 53 | 5 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6532924771308899 | 0.0 | 0.0 | +a2b57772-7a23-4ffd-ace1-d2a7a3f5a7cd / -— |
| Jogador 7 | 4-4 | 413 | PASS | FAST8 | 100.0 | 7 | 50 | 5 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05999999865889549 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 432 | BUY | FAST8 | 100.0 | 7 | 63 | 5 | 36.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12373332679271698 | 0.0 | 0.0 | +d175e09c-3ed6-4fb3-8c97-0c167862e29e / -— |
| Jogador 7 | 4-5 | 433 | PASS | FAST8 | 100.0 | 7 | 59 | 5 | 36.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0035889779683202505 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 452 | PASS | FAST8 | 100.0 | 7 | 73 | 5 | 36.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01106504537165165 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 472 | PASS | FAST8 | 100.0 | 7 | 87 | 5 | 36.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.019575905054807663 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 492 | EQUIP_FROM_INVENTORY | FAST8 | 100.0 | 7 | 100 | 5 | 36.0 | Lutador/DA_Sentinel18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 493 | PASS | FAST8 | 100.0 | 7 | 100 | 5 | 36.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.028095955029129982 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 510 | PASS | FAST8 | 84.0 | 7 | 110 | 5 | 36.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.03496723622083664 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 522 | PASS | FAST8 | 84.0 | 7 | 121 | 5 | 36.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.04279468208551407 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 542 | PASS | FAST8 | 68.0 | 7 | 131 | 5 | 36.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0501258559525013 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 562 | PASS | ECON | 68.0 | 8 | 141 | 5 | 36.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.05764072760939598 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 578 | MOVE_BENCH | ECON | 68.0 | 8 | 141 | 5 | 36.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4430637061595917 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 582 | BUY | ECON | 68.0 | 8 | 152 | 5 | 42.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8099929690361023 | 0.0 | 0.0 | +45b96060-6eda-4d0b-9012-e80db31b71d2 / -— |
| Jogador 7 | 5-6 | 583 | PASS | ECON | 68.0 | 8 | 148 | 5 | 42.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.06300152838230133 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 602 | PASS | ECON | 52.0 | 8 | 158 | 5 | 42.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07079266756772995 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 622 | EQUIP_FROM_INVENTORY | ECON | 52.0 | 8 | 168 | 5 | 42.0 | Lutador/DA_Sentinel18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 623 | EQUIP_FROM_INVENTORY | ECON | 52.0 | 8 | 168 | 5 | 42.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY, CRAFT_AND_EQUIP | True | — | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 624 | PASS | ECON | 52.0 | 8 | 168 | 5 | 42.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07872962951660156 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 632 | PASS | ECON | 52.0 | 8 | 178 | 5 | 42.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0868024006485939 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 642 | PASS | STABILIZE | 34.0 | 8 | 189 | 5 | 42.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09582912921905518 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 652 | PASS | STABILIZE | 16.0 | 8 | 200 | 5 | 42.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10499999672174454 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 662 | PASS | STABILIZE | 16.0 | 8 | 211 | 5 | 42.0 | Lutador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10499999672174454 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 9 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.28737619519233704 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.014635218307375908 | 0.0 | 0.0 | +64afe66e-d5a9-466c-a4ff-9d32c9f153ce / -— |
| Jogador 8 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2073448896408081 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 13 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Veigar | BUY, MOVE_BOARD, PASS | True | True | -0.31726083159446716 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Veigar | BUY, MOVE_BOARD, PASS | True | True | 0.22863437235355377 | 0.0 | 0.0 | +47feb452-27a0-43f6-983f-ea1674f17ab8 / -— |
| Jogador 8 | 1-2 | 15 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5022584795951843 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 16 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.14408981800079346 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.3201245665550232 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.179847851395607 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 24 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9485479593276978 | 0.0 | 0.0 | +dfc76a7d-9a2b-4b35-b341-60eefe095b71 / -— |
| Jogador 8 | 1-3 | 25 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9985479712486267 | 0.0 | 0.0 | +— / -dfc76a7d-9a2b-4b35-b341-60eefe095b71 |
| Jogador 8 | 1-3 | 26 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.40862175822257996 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 27 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5532451272010803 | 0.0 | 0.0 | +— / -a349fd40-8d8c-4de8-9ff0-b3263fd120bc |
| Jogador 8 | 1-3 | 28 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.14408981800079346 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 29 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 48 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3576620817184448 | 0.0 | 0.0 | +4ea4d9af-5729-414b-a102-b7fc80667118 / -— |
| Jogador 8 | 1-4 | 49 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5316286683082581 | 0.0 | 0.0 | +— / -4ea4d9af-5729-414b-a102-b7fc80667118 |
| Jogador 8 | 1-4 | 50 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3577617406845093 | 0.0 | 0.0 | +322e9047-623a-4fec-a0f9-d21d2fbcd88a / -— |
| Jogador 8 | 1-4 | 51 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5316608548164368 | 0.0 | 0.0 | +— / -322e9047-623a-4fec-a0f9-d21d2fbcd88a |
| Jogador 8 | 1-4 | 52 | BUY_XP | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.04450000077486038 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 53 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.33112895488739014 | 0.0 | 0.0 | +65a4f434-f421-47ab-ae23-86ad8971518d / -— |
| Jogador 8 | 1-4 | 54 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3811289370059967 | 0.0 | 0.0 | +— / -65a4f434-f421-47ab-ae23-86ad8971518d |
| Jogador 8 | 1-4 | 55 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | -0.3075500428676605 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 56 | BUY | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BOARD, PASS | True | True | -0.0036285296082496643 | 0.0 | 0.0 | +64f24363-3325-4538-972e-a6d8260b3787 / -— |
| Jogador 8 | 1-4 | 57 | SELL | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1786923110485077 | 0.0 | 0.0 | +— / -64f24363-3325-4538-972e-a6d8260b3787 |
| Jogador 8 | 1-4 | 58 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 72 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06775310635566711 | 0.0 | 0.0 | +a524fad3-c7d3-4fa7-9c62-1803c8e7c865 / -— |
| Jogador 8 | 2-1 | 73 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8883906006813049 | 0.0 | 0.0 | +76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc / -— |
| Jogador 8 | 2-1 | 74 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 6.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9383906126022339 | 0.0 | 0.0 | +— / -76695dc4-95ff-4aeb-b7ac-8b9a1fe3b9bc |
| Jogador 8 | 2-1 | 75 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3548371195793152 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 76 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 77 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.3287540674209595 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 78 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 92 | BUY | STABILIZE | 94.0 | 4 | 8 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.016137270256876945 | 0.0 | 0.0 | +4b4cc4ba-04a0-4e04-88f2-e6913a342285 / -— |
| Jogador 8 | 2-2 | 93 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 5 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4951702952384949 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 94 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 5 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17825740575790405 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 95 | SELL | STABILIZE | 94.0 | 4 | 5 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029709402471780777 | 0.0 | 0.0 | +— / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02 |
| Jogador 8 | 2-2 | 96 | BUY | STABILIZE | 94.0 | 4 | 6 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3577525019645691 | 0.0 | 0.0 | +a3df8a2b-03f3-406d-88a0-1df3c7efa789 / -— |
| Jogador 8 | 2-2 | 97 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 4 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05664046108722687 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 98 | SELL | STABILIZE | 94.0 | 4 | 4 | 0 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09999299794435501 | 0.0 | 0.0 | +— / -64afe66e-d5a9-466c-a4ff-9d32c9f153ce |
| Jogador 8 | 2-2 | 99 | BUY | STABILIZE | 94.0 | 4 | 5 | 0 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3551631271839142 | 0.0 | 0.0 | +3c6ac558-6b59-4a97-814e-bff0ff895232 / -— |
| Jogador 8 | 2-2 | 100 | SELL | STABILIZE | 94.0 | 4 | 4 | 0 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40516310930252075 | 0.0 | 0.0 | +— / -3c6ac558-6b59-4a97-814e-bff0ff895232 |
| Jogador 8 | 2-2 | 101 | BUY_XP | STABILIZE | 94.0 | 4 | 5 | 0 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.026499999687075615 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 102 | PASS | STABILIZE | 94.0 | 5 | 1 | 0 | 16.0 | —/DA_Krug18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 112 | BUY | STABILIZE | 89.0 | 5 | 7 | 0 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3900362551212311 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 113 | BUY | STABILIZE | 89.0 | 5 | 4 | 0 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0668332576751709 | 0.0 | 0.0 | +5de56114-806a-4f58-8241-b3b8434a2154 / -— |
| Jogador 8 | 2-3 | 114 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 2 | 0 | 16.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7335216403007507 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 115 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 2 | 0 | 22.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21120621263980865 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 116 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 2 | 0 | 22.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17535416781902313 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 117 | SELL | STABILIZE | 89.0 | 5 | 2 | 0 | 22.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19792307913303375 | 0.0 | 0.0 | +— / -5de56114-806a-4f58-8241-b3b8434a2154 |
| Jogador 8 | 2-3 | 118 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 4 | 0 | 22.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 119 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 4 | 0 | 22.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08387607336044312 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 120 | BUY | STABILIZE | 89.0 | 5 | 4 | 0 | 22.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.46783286333084106 | 0.0 | 0.0 | +f16ba193-452a-4c02-bfc0-b9757661a178 / -— |
| Jogador 8 | 2-3 | 121 | SELL | STABILIZE | 89.0 | 5 | 3 | 0 | 22.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.51783287525177 | 0.0 | 0.0 | +— / -f16ba193-452a-4c02-bfc0-b9757661a178 |
| Jogador 8 | 2-3 | 122 | PASS | STABILIZE | 89.0 | 5 | 4 | 0 | 22.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 136 | BUY | STABILIZE | 89.0 | 5 | 10 | 1 | 22.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.05669034644961357 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 8 | 2-4 | 137 | BUY | STABILIZE | 89.0 | 5 | 7 | 0 | 22.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3103225529193878 | 0.0 | 0.0 | +7915a339-3bda-4275-80ae-9941370ea609 / -— |
| Jogador 8 | 2-4 | 138 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 4 | 0 | 22.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1789892613887787 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 139 | SELL | STABILIZE | 89.0 | 5 | 4 | 0 | 24.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01169965136796236 | 0.0 | 0.0 | +— / -a3df8a2b-03f3-406d-88a0-1df3c7efa789 |
| Jogador 8 | 2-4 | 140 | SELL | STABILIZE | 89.0 | 5 | 6 | 0 | 24.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3603225648403168 | 0.0 | 0.0 | +— / -7915a339-3bda-4275-80ae-9941370ea609 |
| Jogador 8 | 2-4 | 141 | PASS | STABILIZE | 89.0 | 5 | 9 | 0 | 24.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 156 | BUY | STABILIZE | 89.0 | 5 | 14 | 1 | 24.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.12505578994750977 | 0.0 | 0.0 | +2e656a3d-eed0-40bb-a831-443d972d6588 / -— |
| Jogador 8 | 2-5 | 157 | BUY | STABILIZE | 89.0 | 5 | 11 | 1 | 24.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19572937488555908 | 0.0 | 0.0 | +cf4575c2-3622-4493-91f1-c5efbe1fbd8b / -— |
| Jogador 8 | 2-5 | 158 | SELL | STABILIZE | 89.0 | 5 | 9 | 0 | 24.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24572937190532684 | 0.0 | 0.0 | +— / -cf4575c2-3622-4493-91f1-c5efbe1fbd8b |
| Jogador 8 | 2-5 | 159 | BUY | STABILIZE | 89.0 | 5 | 11 | 1 | 24.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9723386168479919 | 0.0 | 0.0 | +b51e1745-5ed2-46f6-8ca5-fec9a0426afc / -— |
| Jogador 8 | 2-5 | 160 | SELL | STABILIZE | 89.0 | 5 | 10 | 1 | 24.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.022338628768921 | 0.0 | 0.0 | +— / -b51e1745-5ed2-46f6-8ca5-fec9a0426afc |
| Jogador 8 | 2-5 | 161 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 11 | 1 | 24.0 | Enfeitiçador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5614041090011597 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 162 | SELL | STABILIZE | 89.0 | 5 | 11 | 1 | 24.0 | Enfeitiçador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011454039253294468 | 0.0 | 0.0 | +— / -5f2c89f5-15c2-4a77-943e-4ba5492d925b |
| Jogador 8 | 2-5 | 163 | PASS | STABILIZE | 89.0 | 5 | 14 | 1 | 24.0 | Enfeitiçador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 177 | BUY | STABILIZE | 82.0 | 5 | 20 | 2 | 24.0 | Enfeitiçador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.32368549704551697 | 0.0 | 0.0 | +87600495-fe90-4832-ab42-9a5cb0ebe3f4 / -— |
| Jogador 8 | 2-6 | 178 | BUY | STABILIZE | 82.0 | 5 | 17 | 1 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25584936141967773 | 0.0 | 0.0 | +6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 / -— |
| Jogador 8 | 2-6 | 179 | SELL | STABILIZE | 82.0 | 5 | 14 | 1 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5020769238471985 | 0.0 | 0.0 | +— / -6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 |
| Jogador 8 | 2-6 | 180 | MOVE_BENCH | STABILIZE | 82.0 | 5 | 17 | 1 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5240496397018433 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 181 | MOVE_BENCH | STABILIZE | 82.0 | 5 | 17 | 1 | 24.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11011901497840881 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 182 | PASS | STABILIZE | 82.0 | 5 | 17 | 1 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 198 | BUY | STABILIZE | 78.0 | 5 | 24 | 2 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.008531093597412 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 8 | 2-7 | 199 | SELL | STABILIZE | 78.0 | 5 | 21 | 2 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01907600648701191 | 0.0 | 0.0 | +— / -47feb452-27a0-43f6-983f-ea1674f17ab8 |
| Jogador 8 | 2-7 | 200 | BUY | STABILIZE | 78.0 | 5 | 22 | 2 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08496711403131485 | 0.0 | 0.0 | +57903c42-49ca-43e1-8f86-42429c189fb5 / -— |
| Jogador 8 | 2-7 | 201 | SELL | STABILIZE | 78.0 | 5 | 19 | 1 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10035119950771332 | 0.0 | 0.0 | +— / -57903c42-49ca-43e1-8f86-42429c189fb5 |
| Jogador 8 | 2-7 | 202 | SELL | STABILIZE | 78.0 | 5 | 22 | 2 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0585310459136963 | 0.0 | 0.0 | +— / -d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 8 | 2-7 | 203 | PASS | STABILIZE | 78.0 | 5 | 25 | 2 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 218 | BUY | STABILIZE | 78.0 | 5 | 33 | 3 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.22323942184448242 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 219 | MOVE_BENCH | STABILIZE | 78.0 | 5 | 29 | 2 | 28.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2593424916267395 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 220 | SELL | STABILIZE | 78.0 | 5 | 29 | 2 | 30.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3713025450706482 | 0.0 | 0.0 | +— / -87600495-fe90-4832-ab42-9a5cb0ebe3f4 |
| Jogador 8 | 3-1 | 221 | PASS | STABILIZE | 78.0 | 5 | 32 | 3 | 30.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 238 | BUY | STABILIZE | 68.0 | 5 | 41 | 4 | 30.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08274387568235397 | 0.0 | 0.0 | +4ac49c80-f0c3-47ae-a031-96928d244e13 / -— |
| Jogador 8 | 3-2 | 239 | MOVE_BENCH | STABILIZE | 68.0 | 5 | 37 | 3 | 30.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7452058792114258 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 240 | MOVE_BENCH | STABILIZE | 68.0 | 5 | 37 | 3 | 30.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19572843611240387 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 241 | BUY_XP | STABILIZE | 68.0 | 5 | 37 | 3 | 32.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 242 | BUY_XP | STABILIZE | 68.0 | 5 | 33 | 3 | 32.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010900000110268593 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 243 | BUY_XP | STABILIZE | 68.0 | 6 | 29 | 2 | 32.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 244 | BUY_XP | STABILIZE | 68.0 | 6 | 25 | 2 | 32.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 245 | BUY_XP | STABILIZE | 68.0 | 6 | 21 | 2 | 32.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20800000429153442 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 246 | BUY_XP | STABILIZE | 68.0 | 6 | 17 | 1 | 32.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 247 | BUY_XP | STABILIZE | 68.0 | 6 | 13 | 1 | 32.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20800000429153442 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 248 | PASS | STABILIZE | 68.0 | 6 | 9 | 0 | 32.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 256 | BUY_XP | STABILIZE | 56.0 | 6 | 15 | 1 | 32.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 257 | BUY_XP | STABILIZE | 56.0 | 6 | 11 | 1 | 32.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20800000429153442 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 258 | BUY_XP | STABILIZE | 56.0 | 6 | 7 | 0 | 32.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06350000202655792 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 259 | MOVE_BENCH | STABILIZE | 56.0 | 7 | 3 | 0 | 32.0 | Vivaz/DA_18_Sett | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12478232383728027 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 260 | BUY | STABILIZE | 56.0 | 7 | 3 | 0 | 38.0 | Vivaz/DA_18_Sett | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.004296379629522562 | 0.0 | 0.0 | +e4605ac7-0b51-4f1c-a658-f7d25f9a9dae / -— |
| Jogador 8 | 3-3 | 261 | MOVE_BOARD | STABILIZE | 56.0 | 7 | 0 | 0 | 38.0 | Vivaz/DA_18_Sett | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020740801468491554 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 262 | MOVE_BENCH | STABILIZE | 56.0 | 7 | 0 | 0 | 38.0 | Vivaz/DA_18_Sett | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4263922870159149 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 263 | MOVE_BOARD | STABILIZE | 56.0 | 7 | 0 | 0 | 44.0 | Vivaz/DA_18_Sett | MOVE_BOARD, PASS | True | True | 0.010701649822294712 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 264 | MOVE_BOARD | STABILIZE | 56.0 | 7 | 0 | 0 | 44.0 | Vivaz/DA_18_Sett | MOVE_BOARD, PASS | True | True | -0.13466143608093262 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 265 | MOVE_BOARD | STABILIZE | 56.0 | 7 | 0 | 0 | 44.0 | Vivaz/DA_18_Sett | MOVE_BOARD, PASS | True | True | 0.1687082052230835 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 266 | PASS | STABILIZE | 56.0 | 7 | 0 | 0 | 44.0 | Vivaz/DA_18_Sett | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 275 | BUY | STABILIZE | 45.0 | 7 | 7 | 0 | 44.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06948781758546829 | 0.0 | 0.0 | +82e109f9-54c8-492d-93e5-7e0dd0034b15 / -— |
| Jogador 8 | 3-4 | 276 | BUY | STABILIZE | 45.0 | 7 | 4 | 0 | 44.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7132976055145264 | 0.0 | 0.0 | +d5848998-33f3-4632-94c0-60388a7cc6b8 / -— |
| Jogador 8 | 3-4 | 277 | MOVE_BOARD | STABILIZE | 45.0 | 7 | 1 | 0 | 44.0 | Vivaz/DA_18_Sett | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3388819098472595 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 278 | MOVE_BOARD | STABILIZE | 45.0 | 7 | 1 | 0 | 44.0 | Vivaz/DA_18_Sett | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09605743736028671 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 279 | MOVE_BOARD | STABILIZE | 45.0 | 7 | 1 | 0 | 44.0 | Vivaz/DA_18_Sett | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2950354218482971 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 280 | MOVE_BOARD | STABILIZE | 45.0 | 7 | 1 | 0 | 44.0 | Vivaz/DA_18_Lillia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06790129095315933 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 281 | PASS | STABILIZE | 45.0 | 7 | 1 | 0 | 44.0 | Vivaz/DA_18_Sett | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 292 | BUY | STABILIZE | 45.0 | 7 | 8 | 0 | 44.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5947239995002747 | 0.0 | 0.0 | +6e2d02c6-9aae-4ad9-92f3-05cf4a31dbc1 / -— |
| Jogador 8 | 3-5 | 293 | PASS | STABILIZE | 45.0 | 7 | 5 | 0 | 44.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 312 | BUY | STABILIZE | 45.0 | 7 | 11 | 1 | 44.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026028530672192574 | 0.0 | 0.0 | +a23ee552-279e-4c6c-aa05-6197043e8f1d / -— |
| Jogador 8 | 3-6 | 313 | PASS | STABILIZE | 45.0 | 7 | 7 | 0 | 44.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 332 | PASS | STABILIZE | 45.0 | 7 | 14 | 1 | 44.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 352 | PASS | STABILIZE | 45.0 | 7 | 21 | 2 | 44.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 372 | PASS | FAST8 | 45.0 | 7 | 30 | 3 | 44.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 392 | PASS | FAST8 | 45.0 | 7 | 40 | 4 | 44.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.04500000178813934 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 412 | PASS | STABILIZE | 32.0 | 7 | 49 | 4 | 44.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.04500000178813934 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 432 | BUY | STABILIZE | 32.0 | 7 | 58 | 5 | 44.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4481372535228729 | 0.0 | 0.0 | +e65701f6-4dac-4c89-8ac2-f38a1cf52fa8 / -— |
| Jogador 8 | 4-5 | 433 | PASS | STABILIZE | 32.0 | 7 | 55 | 5 | 44.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.06506495922803879 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 452 | PASS | STABILIZE | 32.0 | 7 | 66 | 5 | 44.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.08045294135808945 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 472 | PASS | STABILIZE | 18.0 | 7 | 76 | 5 | 44.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.012818812392652035 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 492 | EQUIP_FROM_INVENTORY | STABILIZE | 18.0 | 7 | 86 | 5 | 44.0 | Vivaz/DA_18_Sett | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 493 | BUY | STABILIZE | 18.0 | 7 | 86 | 5 | 44.0 | Vivaz/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10995283722877502 | 0.0 | 0.0 | +d1bc6c5b-74a5-46db-b00f-e91265546f5d / -— |
| Jogador 8 | 5-1 | 494 | BUY | STABILIZE | 18.0 | 7 | 81 | 5 | 44.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7691621780395508 | 0.0 | 0.0 | +f8a93323-530e-4f9c-99d7-a5ec83b78992 / -— |
| Jogador 8 | 5-1 | 495 | PASS | STABILIZE | 18.0 | 7 | 77 | 5 | 44.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.013412702828645706 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 510 | BUY | STABILIZE | 18.0 | 7 | 88 | 5 | 44.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3866521716117859 | 0.0 | 0.0 | +80130f72-2d7c-49db-8d6f-4c0a962260e8 / -— |
| Jogador 8 | 5-2 | 511 | PASS | STABILIZE | 18.0 | 7 | 85 | 5 | 44.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.018313081935048103 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 522 | PASS | ALL_IN | 4.0 | 7 | 95 | 5 | 44.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.23114027082920074 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 542 | BUY | ALL_IN | 4.0 | 7 | 106 | 5 | 44.0 | Vivaz/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.860853374004364 | 0.0 | 0.0 | +77489602-9456-4a97-aa7e-df7ef91d5e4a / -— |
| Jogador 8 | 5-4 | 543 | PASS | ALL_IN | 4.0 | 7 | 103 | 5 | 44.0 | Vivaz/DA_18_Lux_Elderwood | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.08013080805540085 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 562 | PASS | ALL_IN | 4.0 | 7 | 113 | 5 | 44.0 | Vivaz/DA_18_Lux_Elderwood | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0870756208896637 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 582 | PASS | ALL_IN | 0.0 | 7 | 113 | 5 | 0.0 | Vivaz/DA_18_Lux_Elderwood | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 602 | PASS | ALL_IN | 0.0 | 7 | 113 | 5 | 0.0 | Vivaz/DA_18_Lux_Elderwood | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 622 | PASS | ALL_IN | 0.0 | 7 | 113 | 5 | 0.0 | Vivaz/DA_18_Lux_Elderwood | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 632 | PASS | ALL_IN | 0.0 | 7 | 113 | 5 | 0.0 | Vivaz/DA_18_Lux_Elderwood | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-3 | 642 | PASS | ALL_IN | 0.0 | 7 | 113 | 5 | 0.0 | Vivaz/DA_18_Lux_Elderwood | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-4 | 652 | PASS | ALL_IN | 0.0 | 7 | 113 | 5 | 0.0 | Vivaz/DA_18_Lux_Elderwood | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-5 | 662 | PASS | ALL_IN | 0.0 | 7 | 113 | 5 | 0.0 | Vivaz/DA_18_Lux_Elderwood | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 184 | 152 | 34 | 7 | 12 | 4 | 0 | 0 | 114 | 0.0 |
- Jogador 1 — gasto por ação: BUY: 88g, BUY_XP: 64g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 15g, stage 2: 43g, stage 3: 69g, stage 4: 7g, stage 5: 15g, stage 6: 3g
| Jogador 2 | 131 | 168 | 15 | 5 | 19 | 3 | 0 | 0 | 144 | 54.0 |
- Jogador 2 — gasto por ação: BUY: 76g, BUY_XP: 92g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 9g, stage 2: 42g, stage 3: 55g, stage 4: 33g, stage 5: 21g, stage 6: 8g
| Jogador 3 | 144 | 119 | 16 | 5 | 7 | 1 | 0 | 0 | 50 | 0.0 |
- Jogador 3 — gasto por ação: BUY: 75g, BUY_XP: 44g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 11g, stage 2: 36g, stage 3: 45g, stage 4: 24g, stage 5: 3g, stage 6: 0g
| Jogador 4 | 115 | 64 | 18 | 2 | 0 | 1 | 0 | 0 | 101 | 0.0 |
- Jogador 4 — gasto por ação: BUY: 56g, BUY_XP: 8g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 13g, stage 2: 29g, stage 3: 22g, stage 4: 0g, stage 5: 0g, stage 6: 0g
| Jogador 5 | 111 | 78 | 22 | 9 | 3 | 2 | 0 | 0 | 104 | 0.0 |
- Jogador 5 — gasto por ação: BUY: 58g, BUY_XP: 20g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 8g, stage 2: 47g, stage 3: 20g, stage 4: 3g, stage 5: 0g, stage 6: 0g
| Jogador 6 | 110 | 71 | 8 | 5 | 3 | 1 | 0 | 0 | 77 | 0.0 |
- Jogador 6 — gasto por ação: BUY: 55g, BUY_XP: 16g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 7g, stage 2: 18g, stage 3: 46g, stage 4: 0g, stage 5: 0g, stage 6: 0g
| Jogador 7 | 137 | 136 | 14 | 10 | 14 | 1 | 0 | 0 | 211 | 42.0 |
- Jogador 7 — gasto por ação: BUY: 64g, BUY_XP: 72g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 12g, stage 2: 25g, stage 3: 81g, stage 4: 14g, stage 5: 4g, stage 6: 0g
| Jogador 8 | 146 | 137 | 37 | 11 | 8 | 3 | 0 | 0 | 113 | 0.0 |
- Jogador 8 — gasto por ação: BUY: 89g, BUY_XP: 48g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 12g, stage 2: 43g, stage 3: 64g, stage 4: 3g, stage 5: 15g, stage 6: 0g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 1 | 1 | 0 | 0.0% |
| Jogador 2 | 1 | 1 | 0 | 0.0% |
| Jogador 3 | 2 | 1 | 1 | 50.0% |
| Jogador 4 | 3 | 2 | 1 | 33.3% |
| Jogador 5 | 1 | 1 | 0 | 0.0% |
| Jogador 6 | 3 | 3 | 0 | 0.0% |
| Jogador 7 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 2 | 2 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ médio qualidade | Estrutural médio | Δ estrutural médio | Posicional médio | Δ qualidade combate + | Δ qualidade combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 184 | 0 | 0 | 184 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ 0.0000 (38 ações), BUY_XP: Δ 0.0000 (16 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0000 (21 ações), MOVE_BOARD: Δ 0.0000 (48 ações), PASS: Δ 0.0000 (37 ações), SELL: Δ 0.0000 (21 ações)
| Jogador 2 | 131 | 0 | 0 | 131 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ 0.0000 (24 ações), BUY_XP: Δ 0.0000 (23 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0000 (14 ações), MOVE_BOARD: Δ 0.0000 (22 ações), PASS: Δ 0.0000 (37 ações), SELL: Δ 0.0000 (8 ações)
| Jogador 3 | 144 | 0 | 0 | 144 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ 0.0000 (29 ações), BUY_XP: Δ 0.0000 (11 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (33 ações), MOVE_BOARD: Δ 0.0000 (24 ações), PASS: Δ 0.0000 (37 ações), SELL: Δ 0.0000 (9 ações)
| Jogador 4 | 115 | 0 | 0 | 115 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ 0.0000 (25 ações), BUY_XP: Δ 0.0000 (2 ações), MOVE_BENCH: Δ 0.0000 (24 ações), MOVE_BOARD: Δ 0.0000 (16 ações), PASS: Δ 0.0000 (37 ações), SELL: Δ 0.0000 (11 ações)
| Jogador 5 | 111 | 0 | 0 | 111 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ 0.0000 (25 ações), BUY_XP: Δ 0.0000 (5 ações), MOVE_BENCH: Δ 0.0000 (9 ações), MOVE_BOARD: Δ 0.0000 (23 ações), PASS: Δ 0.0000 (37 ações), SELL: Δ 0.0000 (12 ações)
| Jogador 6 | 110 | 0 | 0 | 110 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ 0.0000 (21 ações), BUY_XP: Δ 0.0000 (4 ações), MOVE_BENCH: Δ 0.0000 (18 ações), MOVE_BOARD: Δ 0.0000 (25 ações), PASS: Δ 0.0000 (37 ações), SELL: Δ 0.0000 (5 ações)
| Jogador 7 | 137 | 0 | 0 | 137 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ 0.0000 (24 ações), BUY_XP: Δ 0.0000 (18 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0000 (27 ações), MOVE_BOARD: Δ 0.0000 (20 ações), PASS: Δ 0.0000 (37 ações), SELL: Δ 0.0000 (8 ações)
| Jogador 8 | 146 | 0 | 0 | 146 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ 0.0000 (37 ações), BUY_XP: Δ 0.0000 (12 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (16 ações), MOVE_BOARD: Δ 0.0000 (21 ações), PASS: Δ 0.0000 (37 ações), SELL: Δ 0.0000 (22 ações)

A pontuação é uma heurística para auditoria, não uma verdade absoluta. Compare-a com recompensas e resultados de combate; correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 221 | OK (221) | 0 | 0 | 0 | 3 | 1 | 1 |
- Jogador 1 — IDs equipados observados: TFT_Item_UnstableConcoction; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 3, COMPONENT_ANVIL_GRANTED: 5, COMPONENT_LOOT_GRANTED: 16.
| Jogador 2 | 168 | OK (168) | 1 | 0 | 0 | 3 | 1 | 1 |
- Jogador 2 — IDs equipados observados: TFT_Item_IonicSpark; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 3, COMPONENT_ANVIL_GRANTED: 5, COMPONENT_LOOT_GRANTED: 16.
| Jogador 3 | 181 | OK (181) | 0 | 0 | 0 | 3 | 0 | 0 |
- Jogador 3 — IDs equipados observados: nenhum observado; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 3, COMPONENT_ANVIL_GRANTED: 5, COMPONENT_LOOT_GRANTED: 16.
| Jogador 4 | 152 | OK (152) | 0 | 0 | 0 | 2 | 0 | 0 |
- Jogador 4 — IDs equipados observados: nenhum observado; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 3, COMPONENT_ANVIL_GRANTED: 5, COMPONENT_LOOT_GRANTED: 16.
| Jogador 5 | 148 | OK (148) | 0 | 0 | 0 | 2 | 0 | 0 |
- Jogador 5 — IDs equipados observados: nenhum observado; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 3, COMPONENT_ANVIL_GRANTED: 5, COMPONENT_LOOT_GRANTED: 16.
| Jogador 6 | 147 | OK (147) | 0 | 0 | 0 | 2 | 0 | 0 |
- Jogador 6 — IDs equipados observados: nenhum observado; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 3, COMPONENT_ANVIL_GRANTED: 5, COMPONENT_LOOT_GRANTED: 16.
| Jogador 7 | 174 | OK (174) | 0 | 0 | 0 | 3 | 1 | 1 |
- Jogador 7 — IDs equipados observados: TFT_Item_TacticiansScepter; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 3, COMPONENT_ANVIL_GRANTED: 5, COMPONENT_LOOT_GRANTED: 16.
| Jogador 8 | 183 | OK (183) | 0 | 0 | 0 | 3 | 0 | 0 |
- Jogador 8 — IDs equipados observados: nenhum observado; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 3, COMPONENT_ANVIL_GRANTED: 5, COMPONENT_LOOT_GRANTED: 16.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | -0.025 | 0.000 |
| Jogador 1 | 1-2 | 12 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 3 | 3 → 3 | 0.043 | 0.000 |
| Jogador 1 | 1-3 | 7 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 5 | 3 | 3 → 3 | 0.024 | 0.000 |
| Jogador 1 | 1-4 | 12 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 5 → 5 | 8 | 3 → 4 | 0.000 | 0.000 |
| Jogador 1 | 2-1 | 8 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 14% | 5 → 9 | 2 | 4 → 4 | 0.001 | 0.297 |
| Jogador 1 | 2-2 | 12 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 9 → 8 | 11 | 4 → 5 | 0.004 | -0.211 |
| Jogador 1 | 2-3 | 12 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 8 → 11 | 5 | 5 → 5 | 0.001 | 0.209 |
| Jogador 1 | 2-4 | 12 | 4.000 | 0.000 | 0 → 0 | 1 → 0 | 18% → 18% | 11 → 6 | 13 | 5 → 5 | -0.058 | 0.000 |
| Jogador 1 | 2-5 | 5 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 18% → 18% | 6 → 10 | 3 | 5 → 5 | 0.114 | 0.561 |
| Jogador 1 | 2-6 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 18% → 18% | 10 → 18 | 0 | 5 → 5 | -0.177 | 0.659 |
| Jogador 1 | 2-7 | 12 | 0.000 | -4.000 | 0 → 0 | 0 → 0 | 18% → 18% | 18 → 23 | 9 | 5 → 6 | 0.011 | 0.000 |
| Jogador 1 | 3-1 | 12 | 6.000 | 4.000 | 0 → 0 | 0 → 1 | 18% → 21% | 23 → 11 | 17 | 6 → 6 | -0.001 | -0.224 |
| Jogador 1 | 3-2 | 4 | -2.000 | 2.000 | 0 → 0 | 1 → 1 | 21% → 21% | 11 → 18 | 0 | 6 → 6 | 0.013 | 0.703 |
| Jogador 1 | 3-3 | 11 | 0.000 | -6.000 | 0 → 0 | 1 → 1 | 21% → 21% | 18 → 17 | 15 | 6 → 6 | 0.001 | 0.276 |
| Jogador 1 | 3-4 | 12 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 17 → 7 | 18 | 6 → 7 | 0.003 | 0.000 |
| Jogador 1 | 3-5 | 9 | 6.000 | 0.000 | 0 → 0 | 1 → 2 | 21% → 25% | 7 → 7 | 7 | 7 → 7 | 0.091 | 0.340 |
| Jogador 1 | 3-6 | 9 | 8.000 | 0.000 | 0 → 1 | 2 → 1 | 25% → 25% | 7 → 7 | 7 | 7 → 7 | -0.021 | 0.337 |
| Jogador 1 | 3-7 | 7 | 4.000 | 6.000 | 1 → 1 | 1 → 1 | 25% → 25% | 7 → 8 | 5 | 7 → 7 | -0.044 | 0.000 |
| Jogador 1 | 4-1 | 4 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 8 → 16 | 0 | 7 → 7 | -0.125 | 0.765 |
| Jogador 1 | 4-2 | 5 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 25% → 25% | 16 → 19 | 3 | 7 → 7 | -0.011 | -0.543 |
| Jogador 1 | 4-3 | 3 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 19 → 27 | 0 | 7 → 7 | 0.000 | 1.045 |
| Jogador 1 | 4-4 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 27 → 34 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 4-5 | 3 | 0.000 | 8.000 | 1 → 1 | 1 → 1 | 25% → 25% | 34 → 38 | 4 | 7 → 7 | 0.000 | -0.917 |
| Jogador 1 | 4-6 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 38 → 47 | 0 | 7 → 7 | 0.000 | -1.400 |
| Jogador 1 | 4-7 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 47 → 57 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 5-1 | 3 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 57 → 68 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 5-2 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 68 → 79 | 0 | 7 → 7 | 0.000 | 1.443 |
| Jogador 1 | 5-3 | 3 | 0.000 | 8.000 | 1 → 1 | 1 → 1 | 25% → 25% | 79 → 85 | 4 | 7 → 7 | 0.000 | -0.927 |
| Jogador 1 | 5-4 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 85 → 95 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 5-5 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 95 → 106 | 0 | 7 → 7 | 0.000 | -1.375 |
| Jogador 1 | 5-6 | 6 | -6.000 | 16.000 | 1 → 1 | 1 → 0 | 25% → 21% | 106 → 109 | 8 | 7 → 7 | -0.008 | 0.000 |
| Jogador 1 | 5-7 | 4 | 6.000 | 0.000 | 1 → 1 | 0 → 1 | 21% → 25% | 109 → 117 | 3 | 7 → 7 | 0.010 | 0.000 |
| Jogador 1 | 6-1 | 5 | -48.000 | -44.000 | 1 → 0 | 1 → 0 | 25% → 0% | 117 → 114 | 3 | 7 → 7 | 0.047 | -0.570 |
| Jogador 1 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 114 → 114 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 114 → 114 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 114 → 114 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 114 → 114 | 0 | 7 → 7 | 0.000 | 0.000 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 3, COMPOSITION_COMPATIBILITY: 25, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 8; mudanças de composição: 0; posicionamento melhorou em 33 ações e piorou em 36.
- Jogador 1 — estado final: ouro 114, nível 7, vida 0.0, colocação 3.
| Jogador 2 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | -0.050 | 0.000 |
| Jogador 2 | 1-2 | 7 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 3 | 2 | 3 → 3 | 0.063 | 0.000 |
| Jogador 2 | 1-3 | 6 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 7% → 11% | 3 → 4 | 2 | 3 → 3 | 0.049 | 0.000 |
| Jogador 2 | 1-4 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 4 → 4 | 4 | 3 → 4 | -0.024 | 0.000 |
| Jogador 2 | 2-1 | 6 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 14% | 4 → 7 | 3 | 4 → 4 | -0.009 | 0.397 |
| Jogador 2 | 2-2 | 10 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 7 → 8 | 6 | 4 → 5 | 0.011 | 0.269 |
| Jogador 2 | 2-3 | 10 | 4.000 | 0.000 | 0 → 0 | 1 → 0 | 18% → 18% | 8 → 7 | 7 | 5 → 5 | 0.017 | -0.237 |
| Jogador 2 | 2-4 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 7 → 6 | 7 | 5 → 5 | 0.013 | 0.000 |
| Jogador 2 | 2-5 | 5 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 6 → 8 | 7 | 5 → 6 | 0.000 | 0.502 |
| Jogador 2 | 2-6 | 7 | 8.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 21% | 8 → 7 | 8 | 6 → 6 | -0.006 | 0.386 |
| Jogador 2 | 2-7 | 5 | 2.000 | 6.000 | 0 → 0 | 0 → 0 | 21% → 21% | 7 → 9 | 4 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 3-1 | 4 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 9 → 8 | 8 | 6 → 6 | 0.000 | 0.758 |
| Jogador 2 | 3-2 | 5 | 0.000 | -6.000 | 0 → 0 | 0 → 0 | 21% → 21% | 8 → 10 | 8 | 6 → 6 | 0.000 | 0.587 |
| Jogador 2 | 3-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 10 → 19 | 0 | 6 → 6 | 0.000 | 1.517 |
| Jogador 2 | 3-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 19 → 27 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 3-5 | 12 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 27 → 8 | 27 | 6 → 7 | 0.002 | -0.223 |
| Jogador 2 | 3-6 | 6 | 8.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 25% | 8 → 6 | 8 | 7 → 7 | 0.033 | -0.444 |
| Jogador 2 | 3-7 | 4 | 0.000 | 8.000 | 0 → 0 | 0 → 1 | 25% → 25% | 6 → 8 | 4 | 7 → 7 | -0.071 | 0.000 |
| Jogador 2 | 4-1 | 4 | 4.000 | -4.000 | 0 → 0 | 1 → 1 | 25% → 25% | 8 → 14 | 0 | 7 → 7 | 0.000 | 0.715 |
| Jogador 2 | 4-2 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 14 → 22 | 0 | 7 → 7 | 0.000 | 1.543 |
| Jogador 2 | 4-3 | 9 | 0.000 | -4.000 | 0 → 0 | 1 → 1 | 25% → 25% | 22 → 7 | 24 | 7 → 8 | 0.000 | 0.318 |
| Jogador 2 | 4-4 | 4 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 29% | 7 → 10 | 3 | 8 → 8 | -0.013 | 0.000 |
| Jogador 2 | 4-5 | 3 | 0.000 | 8.000 | 0 → 0 | 1 → 1 | 29% → 29% | 10 → 13 | 4 | 8 → 8 | 0.000 | 0.968 |
| Jogador 2 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 13 → 22 | 0 | 8 → 8 | 0.000 | 1.468 |
| Jogador 2 | 4-7 | 3 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 29% → 29% | 22 → 29 | 2 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 5-1 | 4 | 0.000 | 10.000 | 0 → 0 | 2 → 2 | 29% → 29% | 29 → 35 | 5 | 8 → 8 | 0.000 | 0.730 |
| Jogador 2 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 35 → 46 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 46 → 59 | 0 | 8 → 8 | 0.000 | 1.461 |
| Jogador 2 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 59 → 72 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 5-5 | 3 | 0.000 | 8.000 | 0 → 0 | 2 → 3 | 29% → 29% | 72 → 82 | 4 | 8 → 8 | 0.000 | 0.982 |
| Jogador 2 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 29% → 29% | 82 → 96 | 0 | 8 → 8 | 0.000 | 1.461 |
| Jogador 2 | 5-7 | 5 | 0.000 | 24.000 | 0 → 0 | 3 → 4 | 29% → 29% | 96 → 97 | 12 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 6-1 | 5 | 0.000 | 8.000 | 0 → 0 | 4 → 4 | 29% → 29% | 97 → 107 | 4 | 8 → 8 | 0.000 | 0.613 |
| Jogador 2 | 6-2 | 3 | 0.000 | 8.000 | 0 → 0 | 4 → 4 | 29% → 29% | 107 → 117 | 4 | 8 → 8 | 0.000 | 0.982 |
| Jogador 2 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 29% → 29% | 117 → 131 | 0 | 8 → 8 | 0.000 | 1.473 |
| Jogador 2 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 29% → 29% | 131 → 144 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 29% → 29% | 144 → 145 | 0 | 8 → 8 | 0.000 | 1.473 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 6, COMPOSITION_COMPATIBILITY: 13, PAIR_POTENTIAL: 5; mudanças de composição: 1; posicionamento melhorou em 18 ações e piorou em 14.
- Jogador 2 — estado final: ouro 145, nível 8, vida 72.0, colocação 1.
| Jogador 3 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | -0.025 | 0.000 |
| Jogador 3 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.065 | 0.000 |
| Jogador 3 | 1-3 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 5 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 3 | 1-4 | 7 | 2.000 | 0.000 | 0 → 0 | 1 → 0 | 11% → 11% | 5 → 4 | 6 | 3 → 4 | 0.026 | 0.000 |
| Jogador 3 | 2-1 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 11% → 14% | 4 → 8 | 2 | 4 → 4 | -0.022 | 0.512 |
| Jogador 3 | 2-2 | 8 | 6.000 | 0.000 | 0 → 1 | 1 → 0 | 14% → 14% | 8 → 8 | 5 | 4 → 4 | -0.001 | -0.336 |
| Jogador 3 | 2-3 | 12 | 6.000 | 0.000 | 1 → 1 | 0 → 0 | 14% → 18% | 8 → 7 | 7 | 4 → 5 | 0.006 | 0.224 |
| Jogador 3 | 2-4 | 5 | 4.000 | 2.000 | 1 → 1 | 0 → 0 | 18% → 18% | 7 → 9 | 3 | 5 → 5 | 0.012 | 0.000 |
| Jogador 3 | 2-5 | 11 | 0.000 | 2.000 | 1 → 1 | 0 → 0 | 18% → 18% | 9 → 11 | 6 | 5 → 5 | 0.000 | 0.250 |
| Jogador 3 | 2-6 | 12 | 4.000 | -4.000 | 1 → 1 | 0 → 0 | 18% → 21% | 11 → 8 | 10 | 5 → 6 | -0.003 | -0.211 |
| Jogador 3 | 2-7 | 7 | 0.000 | 6.000 | 1 → 1 | 0 → 1 | 21% → 21% | 8 → 10 | 3 | 6 → 6 | -0.006 | 0.000 |
| Jogador 3 | 3-1 | 5 | 4.000 | -4.000 | 1 → 1 | 1 → 1 | 21% → 21% | 10 → 17 | 0 | 6 → 6 | -0.002 | 0.600 |
| Jogador 3 | 3-2 | 12 | 0.000 | -2.000 | 1 → 1 | 1 → 1 | 21% → 21% | 17 → 7 | 18 | 6 → 6 | 0.005 | -0.219 |
| Jogador 3 | 3-3 | 5 | 2.000 | 6.000 | 1 → 1 | 1 → 1 | 21% → 21% | 7 → 9 | 4 | 6 → 6 | -0.129 | 0.607 |
| Jogador 3 | 3-4 | 9 | 0.000 | -6.000 | 1 → 1 | 1 → 0 | 21% → 21% | 9 → 13 | 7 | 6 → 6 | 0.006 | 0.000 |
| Jogador 3 | 3-5 | 9 | 8.000 | 6.000 | 1 → 1 | 0 → 0 | 21% → 25% | 13 → 7 | 11 | 6 → 7 | -0.007 | -0.302 |
| Jogador 3 | 3-6 | 3 | 0.000 | 4.000 | 1 → 1 | 0 → 1 | 25% → 25% | 7 → 11 | 2 | 7 → 7 | 0.000 | 1.004 |
| Jogador 3 | 3-7 | 3 | 0.000 | 6.000 | 1 → 1 | 1 → 2 | 25% → 25% | 11 → 13 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 4-1 | 2 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 13 → 19 | 0 | 7 → 7 | 0.000 | -1.350 |
| Jogador 3 | 4-2 | 2 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 19 → 27 | 0 | 7 → 7 | 0.000 | 1.518 |
| Jogador 3 | 4-3 | 3 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 25% → 25% | 27 → 31 | 3 | 7 → 7 | 0.000 | -0.917 |
| Jogador 3 | 4-4 | 2 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 25% → 25% | 31 → 39 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 4-5 | 5 | 0.000 | 12.000 | 1 → 1 | 3 → 2 | 25% → 25% | 39 → 39 | 9 | 7 → 7 | -0.012 | -0.543 |
| Jogador 3 | 4-6 | 4 | 0.000 | 12.000 | 1 → 1 | 2 → 2 | 25% → 25% | 39 → 42 | 6 | 7 → 7 | 0.000 | 0.771 |
| Jogador 3 | 4-7 | 5 | -2.000 | 8.000 | 1 → 1 | 2 → 1 | 25% → 25% | 42 → 44 | 6 | 7 → 7 | -0.023 | 0.000 |
| Jogador 3 | 5-1 | 3 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 44 → 53 | 0 | 7 → 7 | 0.000 | -0.950 |
| Jogador 3 | 5-2 | 3 | -44.000 | -54.000 | 1 → 0 | 1 → 0 | 25% → 0% | 53 → 50 | 3 | 7 → 7 | 0.066 | -0.950 |
| Jogador 3 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 50 → 50 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 50 → 50 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 50 → 50 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 50 → 50 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 50 → 50 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 50 → 50 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 50 → 50 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 50 → 50 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 50 → 50 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 50 → 50 | 0 | 7 → 7 | 0.000 | 0.000 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 8, COMPOSITION_COMPATIBILITY: 12, IMMEDIATE_UPGRADE: 3, PAIR_POTENTIAL: 6; mudanças de composição: 1; posicionamento melhorou em 21 ações e piorou em 23.
- Jogador 3 — estado final: ouro 50, nível 7, vida 0.0, colocação 5.
| Jogador 4 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | -0.050 | 0.000 |
| Jogador 4 | 1-2 | 10 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.080 | 0.000 |
| Jogador 4 | 1-3 | 7 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 4 | 4 | 3 → 3 | 0.013 | 0.000 |
| Jogador 4 | 1-4 | 7 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 4 → 4 | 6 | 3 → 4 | 0.000 | 0.000 |
| Jogador 4 | 2-1 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 4 → 7 | 4 | 4 → 4 | -0.094 | -0.283 |
| Jogador 4 | 2-2 | 12 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 18% | 7 → 7 | 9 | 4 → 5 | 0.003 | 0.209 |
| Jogador 4 | 2-3 | 10 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 7 → 11 | 3 | 5 → 5 | -0.007 | -0.242 |
| Jogador 4 | 2-4 | 5 | 6.000 | 2.000 | 0 → 0 | 0 → 0 | 18% → 18% | 11 → 12 | 4 | 5 → 5 | -0.045 | 0.000 |
| Jogador 4 | 2-5 | 7 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 18% → 18% | 12 → 17 | 3 | 5 → 5 | 0.000 | -0.361 |
| Jogador 4 | 2-6 | 6 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 17 → 24 | 3 | 5 → 5 | 0.038 | -0.413 |
| Jogador 4 | 2-7 | 7 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 18% → 18% | 24 → 29 | 3 | 5 → 5 | -0.032 | 0.000 |
| Jogador 4 | 3-1 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 18% → 18% | 29 → 35 | 2 | 5 → 5 | 0.000 | -0.471 |
| Jogador 4 | 3-2 | 7 | 4.000 | 2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 35 → 42 | 4 | 5 → 5 | 0.010 | -0.416 |
| Jogador 4 | 3-3 | 4 | 0.000 | 10.000 | 0 → 0 | 1 → 1 | 18% → 18% | 42 → 48 | 5 | 5 → 5 | 0.000 | -0.716 |
| Jogador 4 | 3-4 | 3 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 18% → 18% | 48 → 58 | 2 | 5 → 6 | 0.000 | 0.000 |
| Jogador 4 | 3-5 | 4 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 21% | 58 → 68 | 3 | 6 → 6 | -0.016 | -0.725 |
| Jogador 4 | 3-6 | 4 | 0.000 | 12.000 | 0 → 0 | 1 → 3 | 21% → 21% | 68 → 75 | 6 | 6 → 6 | 0.000 | -0.725 |
| Jogador 4 | 3-7 | 2 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 21% → 21% | 75 → 88 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 4-1 | 2 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 21% → 21% | 88 → 101 | 0 | 6 → 6 | 0.000 | -1.441 |
| Jogador 4 | 4-2 | 2 | -34.000 | -44.000 | 0 → 0 | 3 → 0 | 21% → 0% | 101 → 101 | 0 | 6 → 6 | 0.183 | -1.441 |
| Jogador 4 | 4-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 4-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 6 → 6 | 0.000 | 0.000 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 5, COMPOSITION_COMPATIBILITY: 13, PAIR_POTENTIAL: 7; mudanças de composição: 2; posicionamento melhorou em 19 ações e piorou em 20.
- Jogador 4 — estado final: ouro 101, nível 6, vida 0.0, colocação 8.
| Jogador 5 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 5 | 1-2 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.109 | 0.000 |
| Jogador 5 | 1-3 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 4 | 3 → 3 | 0.023 | 0.000 |
| Jogador 5 | 1-4 | 5 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 7 | 2 | 3 → 4 | 0.019 | 0.000 |
| Jogador 5 | 2-1 | 6 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 7 → 9 | 3 | 4 → 4 | -0.160 | -0.377 |
| Jogador 5 | 2-2 | 12 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 9 → 14 | 6 | 4 → 4 | 0.082 | 0.209 |
| Jogador 5 | 2-3 | 10 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 14 → 11 | 10 | 4 → 5 | 0.000 | -0.253 |
| Jogador 5 | 2-4 | 11 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 18% | 11 → 5 | 13 | 5 → 5 | -0.001 | 0.000 |
| Jogador 5 | 2-5 | 4 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 5 → 11 | 3 | 5 → 5 | 0.000 | -0.593 |
| Jogador 5 | 2-6 | 11 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 11 → 13 | 8 | 5 → 6 | -0.003 | -0.211 |
| Jogador 5 | 2-7 | 11 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 21% | 13 → 18 | 4 | 6 → 6 | 0.016 | 0.000 |
| Jogador 5 | 3-1 | 5 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 21% → 21% | 18 → 22 | 3 | 6 → 6 | -0.241 | 0.562 |
| Jogador 5 | 3-2 | 4 | 0.000 | 10.000 | 0 → 0 | 0 → 1 | 21% → 21% | 22 → 25 | 5 | 6 → 6 | 0.000 | 0.771 |
| Jogador 5 | 3-3 | 4 | 0.000 | 14.000 | 0 → 0 | 1 → 1 | 21% → 21% | 25 → 24 | 7 | 6 → 6 | -0.000 | -0.716 |
| Jogador 5 | 3-4 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 24 → 31 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 3-5 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 31 → 40 | 0 | 6 → 6 | 0.000 | 1.450 |
| Jogador 5 | 3-6 | 3 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 40 → 46 | 2 | 6 → 6 | 0.000 | -0.955 |
| Jogador 5 | 3-7 | 3 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 21% → 21% | 46 → 52 | 3 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-1 | 3 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 21% → 21% | 52 → 59 | 3 | 6 → 6 | 0.000 | -0.967 |
| Jogador 5 | 4-2 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 59 → 70 | 0 | 6 → 6 | 0.000 | -1.466 |
| Jogador 5 | 4-3 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 70 → 81 | 0 | 6 → 6 | 0.000 | -1.491 |
| Jogador 5 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 81 → 92 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-5 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 92 → 104 | 0 | 6 → 6 | 0.000 | -1.491 |
| Jogador 5 | 4-6 | 2 | -28.000 | -46.000 | 0 → 0 | 1 → 0 | 21% → 0% | 104 → 104 | 0 | 6 → 6 | 0.234 | -1.466 |
| Jogador 5 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 104 → 104 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 104 → 104 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 104 → 104 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 104 → 104 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 104 → 104 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 104 → 104 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 104 → 104 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 104 → 104 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 104 → 104 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 104 → 104 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 104 → 104 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 104 → 104 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 104 → 104 | 0 | 6 → 6 | 0.000 | 0.000 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 5, COMPOSITION_COMPATIBILITY: 19, PAIR_POTENTIAL: 1; mudanças de composição: 0; posicionamento melhorou em 16 ações e piorou em 17.
- Jogador 5 — estado final: ouro 104, nível 6, vida 0.0, colocação 6.
| Jogador 6 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | -0.050 | 0.000 |
| Jogador 6 | 1-2 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | -0.123 | 0.000 |
| Jogador 6 | 1-3 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | 0.069 | 0.000 |
| Jogador 6 | 1-4 | 4 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 7 | 2 | 3 → 4 | 0.000 | 0.000 |
| Jogador 6 | 2-1 | 12 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 7 → 9 | 4 | 4 → 4 | 0.024 | -0.202 |
| Jogador 6 | 2-2 | 5 | 2.000 | 4.000 | 0 → 0 | 0 → 0 | 14% → 14% | 9 → 12 | 3 | 4 → 4 | -0.019 | -0.474 |
| Jogador 6 | 2-3 | 4 | -2.000 | 2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 12 → 19 | 0 | 4 → 4 | -0.182 | -0.671 |
| Jogador 6 | 2-4 | 7 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 19 → 25 | 3 | 4 → 4 | 0.179 | 0.000 |
| Jogador 6 | 2-5 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 14% → 14% | 25 → 31 | 2 | 4 → 5 | 0.000 | -0.439 |
| Jogador 6 | 2-6 | 6 | 6.000 | 0.000 | 0 → 0 | 0 → 1 | 14% → 18% | 31 → 36 | 3 | 5 → 5 | -0.099 | 0.397 |
| Jogador 6 | 2-7 | 9 | 0.000 | 2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 36 → 43 | 3 | 5 → 5 | 0.071 | 0.000 |
| Jogador 6 | 3-1 | 5 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 18% → 18% | 43 → 49 | 3 | 5 → 5 | -0.049 | -0.573 |
| Jogador 6 | 3-2 | 12 | 0.000 | 2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 49 → 37 | 20 | 5 → 6 | -0.008 | -0.246 |
| Jogador 6 | 3-3 | 7 | 2.000 | 10.000 | 0 → 0 | 1 → 2 | 18% → 21% | 37 → 40 | 6 | 6 → 6 | -0.067 | -0.409 |
| Jogador 6 | 3-4 | 5 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 21% → 21% | 40 → 45 | 4 | 6 → 6 | -0.017 | 0.000 |
| Jogador 6 | 3-5 | 4 | 0.000 | 12.000 | 0 → 0 | 2 → 3 | 21% → 21% | 45 → 48 | 6 | 6 → 6 | 0.000 | -0.681 |
| Jogador 6 | 3-6 | 3 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 21% → 21% | 48 → 56 | 3 | 6 → 6 | 0.000 | -0.950 |
| Jogador 6 | 3-7 | 3 | 0.000 | 8.000 | 0 → 0 | 3 → 3 | 21% → 21% | 56 → 64 | 4 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 4-1 | 2 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 21% → 21% | 64 → 77 | 0 | 6 → 6 | 0.000 | -1.450 |
| Jogador 6 | 4-2 | 2 | -26.000 | -64.000 | 0 → 0 | 3 → 0 | 21% → 0% | 77 → 77 | 0 | 6 → 6 | 0.251 | -1.491 |
| Jogador 6 | 4-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 77 → 77 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 77 → 77 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 4-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 77 → 77 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 77 → 77 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 77 → 77 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 5-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 77 → 77 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 77 → 77 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 77 → 77 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 77 → 77 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 77 → 77 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 77 → 77 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 77 → 77 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 77 → 77 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 77 → 77 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 77 → 77 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 77 → 77 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 77 → 77 | 0 | 6 → 6 | 0.000 | 0.000 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 3, COMPOSITION_COMPATIBILITY: 12, IMMEDIATE_UPGRADE: 1, PAIR_POTENTIAL: 5; mudanças de composição: 2; posicionamento melhorou em 17 ações e piorou em 25.
- Jogador 6 — estado final: ouro 77, nível 6, vida 0.0, colocação 7.
| Jogador 7 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | -0.050 | 0.000 |
| Jogador 7 | 1-2 | 12 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 3 | 3 → 3 | 0.067 | 0.000 |
| Jogador 7 | 1-3 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 4 | 2 | 3 → 3 | 0.019 | 0.000 |
| Jogador 7 | 1-4 | 5 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 4 → 4 | 6 | 3 → 4 | 0.000 | 0.000 |
| Jogador 7 | 2-1 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 4 → 8 | 2 | 4 → 4 | 0.000 | 0.547 |
| Jogador 7 | 2-2 | 12 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 18% | 8 → 8 | 7 | 4 → 5 | -0.001 | 0.238 |
| Jogador 7 | 2-3 | 10 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 18% → 18% | 8 → 10 | 9 | 5 → 5 | 0.008 | 0.285 |
| Jogador 7 | 2-4 | 7 | 4.000 | 4.000 | 0 → 0 | 1 → 1 | 18% → 18% | 10 → 12 | 4 | 5 → 5 | 0.000 | 0.000 |
| Jogador 7 | 2-5 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 12 → 20 | 0 | 5 → 5 | 0.000 | 0.672 |
| Jogador 7 | 2-6 | 4 | -4.000 | 4.000 | 0 → 0 | 1 → 1 | 18% → 18% | 20 → 30 | 0 | 5 → 5 | 0.000 | 0.616 |
| Jogador 7 | 2-7 | 7 | 6.000 | -4.000 | 0 → 0 | 1 → 0 | 18% → 18% | 30 → 38 | 3 | 5 → 5 | 0.000 | 0.000 |
| Jogador 7 | 3-1 | 12 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 21% | 38 → 13 | 34 | 5 → 6 | -0.007 | 0.238 |
| Jogador 7 | 3-2 | 12 | 4.000 | 2.000 | 0 → 0 | 0 → 0 | 21% → 25% | 13 → 11 | 11 | 6 → 7 | -0.007 | 0.259 |
| Jogador 7 | 3-3 | 5 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 25% → 25% | 11 → 17 | 3 | 7 → 7 | 0.000 | 0.560 |
| Jogador 7 | 3-4 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 25% → 25% | 17 → 26 | 0 | 7 → 7 | 0.089 | 0.000 |
| Jogador 7 | 3-5 | 12 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 25% → 25% | 26 → 13 | 25 | 7 → 7 | -0.023 | 0.240 |
| Jogador 7 | 3-6 | 3 | 0.000 | 8.000 | 0 → 0 | 1 → 1 | 25% → 25% | 13 → 19 | 4 | 7 → 7 | 0.000 | 0.945 |
| Jogador 7 | 3-7 | 3 | 0.000 | 8.000 | 0 → 0 | 1 → 2 | 25% → 25% | 19 → 24 | 4 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 4-1 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 24 → 35 | 0 | 7 → 7 | 0.000 | 1.518 |
| Jogador 7 | 4-2 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 35 → 47 | 0 | 7 → 7 | 0.000 | 1.568 |
| Jogador 7 | 4-3 | 4 | 0.000 | 14.000 | 0 → 0 | 2 → 3 | 25% → 25% | 47 → 53 | 7 | 7 → 7 | 0.000 | 0.728 |
| Jogador 7 | 4-4 | 3 | 0.000 | 6.000 | 0 → 0 | 3 → 4 | 25% → 25% | 53 → 63 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 4-5 | 3 | 0.000 | 8.000 | 0 → 0 | 4 → 4 | 25% → 25% | 63 → 73 | 4 | 7 → 7 | 0.000 | 1.045 |
| Jogador 7 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 73 → 87 | 0 | 7 → 7 | 0.000 | 1.481 |
| Jogador 7 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 87 → 100 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 5-1 | 3 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 100 → 110 | 0 | 7 → 7 | 0.000 | -0.917 |
| Jogador 7 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 110 → 121 | 0 | 7 → 7 | 0.000 | 1.503 |
| Jogador 7 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 121 → 131 | 0 | 7 → 7 | 0.000 | -1.375 |
| Jogador 7 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 131 → 141 | 0 | 7 → 8 | 0.000 | 0.000 |
| Jogador 7 | 5-5 | 3 | 6.000 | -6.000 | 0 → 0 | 4 → 4 | 25% → 29% | 141 → 152 | 0 | 8 → 8 | -0.025 | 0.995 |
| Jogador 7 | 5-6 | 3 | 0.000 | 8.000 | 0 → 0 | 4 → 5 | 29% → 29% | 152 → 158 | 4 | 8 → 8 | 0.000 | -0.917 |
| Jogador 7 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 5 → 5 | 29% → 29% | 158 → 168 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 7 | 6-1 | 4 | 0.000 | 0.000 | 0 → 0 | 5 → 5 | 29% → 29% | 168 → 178 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 7 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 5 → 5 | 29% → 29% | 178 → 189 | 0 | 8 → 8 | 0.000 | -1.375 |
| Jogador 7 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 5 → 5 | 29% → 29% | 189 → 200 | 0 | 8 → 8 | 0.000 | -1.375 |
| Jogador 7 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 5 → 5 | 29% → 29% | 200 → 211 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 7 | 6-5 | 2 | -42.000 | -60.000 | 0 → 0 | 5 → 0 | 29% → 0% | 211 → 211 | 0 | 8 → 8 | -0.273 | -1.375 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 1, COMPOSITION_COMPATIBILITY: 16, PAIR_POTENTIAL: 7; mudanças de composição: 0; posicionamento melhorou em 15 ações e piorou em 13.
- Jogador 7 — estado final: ouro 211, nível 8, vida 0.0, colocação 2.
| Jogador 8 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 8 | 1-2 | 10 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.013 | 0.000 |
| Jogador 8 | 1-3 | 7 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 5 | 2 | 3 → 3 | 0.031 | 0.000 |
| Jogador 8 | 1-4 | 12 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 5 → 5 | 8 | 3 → 4 | -0.036 | 0.000 |
| Jogador 8 | 2-1 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 5 → 8 | 3 | 4 → 4 | -0.117 | -0.322 |
| Jogador 8 | 2-2 | 12 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 8 → 7 | 10 | 4 → 5 | 0.093 | -0.198 |
| Jogador 8 | 2-3 | 12 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 18% | 7 → 10 | 6 | 5 → 5 | 0.046 | 0.214 |
| Jogador 8 | 2-4 | 7 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 10 → 14 | 6 | 5 → 5 | 0.019 | 0.000 |
| Jogador 8 | 2-5 | 9 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 14 → 20 | 6 | 5 → 5 | 0.000 | -0.287 |
| Jogador 8 | 2-6 | 7 | 4.000 | 2.000 | 0 → 0 | 0 → 0 | 18% → 18% | 20 → 24 | 6 | 5 → 5 | -0.056 | -0.323 |
| Jogador 8 | 2-7 | 7 | 0.000 | -2.000 | 0 → 0 | 0 → 0 | 18% → 18% | 24 → 33 | 6 | 5 → 5 | 0.000 | 0.000 |
| Jogador 8 | 3-1 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 33 → 41 | 4 | 5 → 5 | 0.146 | -0.527 |
| Jogador 8 | 3-2 | 12 | 2.000 | 6.000 | 0 → 0 | 0 → 0 | 18% → 18% | 41 → 15 | 32 | 5 → 6 | 0.005 | -0.230 |
| Jogador 8 | 3-3 | 12 | 12.000 | -6.000 | 0 → 0 | 0 → 0 | 18% → 25% | 15 → 7 | 15 | 6 → 7 | 0.017 | -0.219 |
| Jogador 8 | 3-4 | 8 | 0.000 | 12.000 | 0 → 0 | 0 → 1 | 25% → 25% | 7 → 8 | 6 | 7 → 7 | -0.136 | 0.000 |
| Jogador 8 | 3-5 | 3 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 25% → 25% | 8 → 11 | 3 | 7 → 7 | 0.000 | 0.950 |
| Jogador 8 | 3-6 | 3 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 25% → 25% | 11 → 14 | 4 | 7 → 7 | 0.000 | 1.021 |
| Jogador 8 | 3-7 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 14 → 21 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 4-1 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 21 → 30 | 0 | 7 → 7 | 0.000 | 1.531 |
| Jogador 8 | 4-2 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 30 → 40 | 0 | 7 → 7 | 0.000 | 1.442 |
| Jogador 8 | 4-3 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 40 → 49 | 0 | 7 → 7 | 0.000 | -1.350 |
| Jogador 8 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 49 → 58 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 4-5 | 3 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 25% → 25% | 58 → 66 | 3 | 7 → 7 | 0.000 | 0.961 |
| Jogador 8 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 66 → 76 | 0 | 7 → 7 | 0.000 | -1.391 |
| Jogador 8 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 76 → 86 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 5-1 | 5 | 0.000 | 18.000 | 0 → 0 | 2 → 3 | 25% → 25% | 86 → 88 | 9 | 7 → 7 | 0.000 | 0.601 |
| Jogador 8 | 5-2 | 3 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 25% → 25% | 88 → 95 | 3 | 7 → 7 | 0.000 | -0.911 |
| Jogador 8 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 25% → 25% | 95 → 106 | 0 | 7 → 7 | 0.000 | 1.468 |
| Jogador 8 | 5-4 | 3 | 0.000 | 6.000 | 0 → 0 | 3 → 4 | 25% → 25% | 106 → 113 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 5-5 | 2 | -44.000 | -62.000 | 0 → 0 | 4 → 0 | 25% → 0% | 113 → 113 | 0 | 7 → 7 | 0.115 | -1.400 |
| Jogador 8 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 113 → 113 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 113 → 113 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 113 → 113 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 113 → 113 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 113 → 113 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 113 → 113 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 113 → 113 | 0 | 7 → 7 | 0.000 | 0.000 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 9, COMPOSITION_COMPATIBILITY: 20, PAIR_POTENTIAL: 8; mudanças de composição: 1; posicionamento melhorou em 20 ações e piorou em 18.
- Jogador 8 — estado final: ouro 113, nível 7, vida 0.0, colocação 4.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Revertidas ≤1 ação | ≤2 ações | ≤4 ações | Ouro perdido | Upgrades | Vendas core/par | Valor médio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 38 | 21 | 10 | 12 | 12 | 0 | 2 | 3 | 3.6588 |
| Jogador 2 | 24 | 8 | 2 | 2 | 2 | 0 | 0 | 1 | 2.729 |
| Jogador 3 | 29 | 9 | 2 | 2 | 3 | 0 | 3 | 2 | 3.9361 |
| Jogador 4 | 25 | 11 | 2 | 2 | 3 | 0 | 0 | 1 | 2.5923 |
| Jogador 5 | 25 | 12 | 10 | 10 | 10 | 0 | 0 | 1 | 1.6289 |
| Jogador 6 | 21 | 5 | 1 | 1 | 1 | 0 | 1 | 0 | 3.307 |
| Jogador 7 | 24 | 8 | 2 | 2 | 3 | 0 | 0 | 1 | 2.4953 |
| Jogador 8 | 37 | 22 | 10 | 10 | 12 | 0 | 0 | 4 | 2.3472 |

Vendas de core/pares ignoradas antes da decisão da composição: **32**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Uma venda sem compra correspondente na janela é UNKNOWN; sequências ambíguas não são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| MEDIUM | Jogador 1 | 1-2 | 17 | PURCHASE_REVERSED | Compra de DA_18_Akali_AD desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 1-3 | 25 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 1-3 | 28 | PURCHASE_REVERSED | Compra de DA_18_Xayah desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 1-4 | 52 | PURCHASE_REVERSED | Compra de DA_18_Veigar desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 1-4 | 54 | PURCHASE_REVERSED | Compra de DA_Karma18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 1-4 | 56 | PURCHASE_REVERSED | Compra de DA_18_Ornn desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 2-2 | 101 | PURCHASE_REVERSED | Compra de DA_18_Elise desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 2-3 | 115 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 2-4 | 141 | PURCHASE_REVERSED | Compra de DA_Scuttlecrab18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 1 | 2-7 | 201 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 1 | 2-7 | 204 | PURCHASE_REVERSED | Compra de DA_Murkwolf18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 2-7 | 207 | PURCHASE_REVERSED | Compra de DA_18_Caitlyn desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 1 | 3-3 | 261 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 1 | 3-3 | 262 | SOLD_CORE_UNIT | Venda de 'DA_Vi18' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 1 | 3-4 | 279 | PURCHASE_REVERSED | Compra de DA_18_Caitlyn desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 6-2 | 641 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_MasterYi_AD' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 1 | 6-2 | 641 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Vi18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 1 | 6-2 | 641 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Lux_Fae' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 2 | 1-2 | 15 | PURCHASE_REVERSED | Compra de DA_18_Veigar desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 2 | 2-5 | 157 | SOLD_CORE_UNIT | Venda de 'DA_18_Azir' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 2 | 2-5 | 157 | PURCHASE_REVERSED | Compra de DA_18_Azir desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 3 | 1-3 | 25 | PURCHASE_REVERSED | Compra de DA_Murkwolf18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 3 | 2-6 | 181 | SOLD_CORE_UNIT | Venda de 'DA_Scuttlecrab18' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 3 | 3-2 | 246 | PURCHASE_REVERSED | Compra de DA_18_Alistar desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 3 | 3-4 | 279 | PURCHASE_REVERSED | Compra de DA_Fiddlesticks18 desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 3 | 3-4 | 281 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 3 | 5-3 | 541 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Vi18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 3 | 5-3 | 541 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Hecarim' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 3 | 5-3 | 541 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Scuttlecrab18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 4 | 1-3 | 25 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 4 | 2-2 | 95 | PURCHASE_REVERSED | Compra de DA_Krug18 desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 4 | 2-6 | 178 | PURCHASE_REVERSED | Compra de DA_CrimsonRaptor18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 4 | 3-2 | 242 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 4 | 4-3 | 411 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Aphelios' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 4 | 4-3 | 411 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Fiddlesticks18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 4 | 4-3 | 411 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Diana' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 5 | 1-3 | 25 | PURCHASE_REVERSED | Compra de DA_18_Yunara desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-2 | 101 | PURCHASE_REVERSED | Compra de DA_18_Tristana desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-3 | 113 | PURCHASE_REVERSED | Compra de DA_18_Rakan desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-3 | 118 | PURCHASE_REVERSED | Compra de DA_18_Camille desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-4 | 138 | PURCHASE_REVERSED | Compra de DA_18_Caitlyn desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 5 | 2-5 | 157 | SOLD_CORE_UNIT | Venda de 'DA_18_Rammus' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 5 | 2-5 | 157 | PURCHASE_REVERSED | Compra de DA_18_Rammus desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-6 | 178 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-6 | 180 | PURCHASE_REVERSED | Compra de DA_18_Camille desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-6 | 183 | PURCHASE_REVERSED | Compra de DA_18_Rakan desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-7 | 200 | PURCHASE_REVERSED | Compra de DA_18_Yunara desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 4-7 | 491 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Tristana' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 5 | 4-7 | 491 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Ahri' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 5 | 4-7 | 491 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Azir' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 6 | 1-4 | 49 | PURCHASE_REVERSED | Compra de DA_Murkwolf18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 6 | 4-3 | 411 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Rammus' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 6 | 4-3 | 411 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Sentinel18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 6 | 4-3 | 411 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Tristana' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 7 | 1-4 | 49 | PURCHASE_REVERSED | Compra de DA_18_Elise desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 7 | 2-3 | 118 | PURCHASE_REVERSED | Compra de DA_18_Cassiopeia desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 7 | 2-7 | 199 | SOLD_CORE_UNIT | Venda de 'DA_18_Alistar' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 7 | 3-5 | 295 | PURCHASE_REVERSED | Compra de DA_18_Diana desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 1-3 | 27 | PURCHASE_REVERSED | Compra de DA_18_Yorick desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 1-4 | 49 | PURCHASE_REVERSED | Compra de DA_18_Xayah desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 1-4 | 51 | PURCHASE_REVERSED | Compra de DA_18_Xayah desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 1-4 | 54 | PURCHASE_REVERSED | Compra de DA_18_RekSai desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 1-4 | 57 | PURCHASE_REVERSED | Compra de DA_18_Leona desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 2-2 | 100 | PURCHASE_REVERSED | Compra de DA_18_Sentry desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 2-3 | 117 | PURCHASE_REVERSED | Compra de DA_18_Caitlyn desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 2-3 | 121 | PURCHASE_REVERSED | Compra de DA_18_Veigar desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 2-4 | 140 | PURCHASE_REVERSED | Compra de DA_18_KhaZix desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 2-5 | 158 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 8 | 2-5 | 160 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Karma18' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 8 | 2-6 | 179 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 8 | 2-6 | 179 | PURCHASE_REVERSED | Compra de DA_18_Diana desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 2-7 | 201 | PURCHASE_REVERSED | Compra de DA_Vi18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 8 | 2-7 | 202 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 8 | 3-1 | 220 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 8 | 5-6 | 601 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Lux_Elderwood' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 8 | 5-6 | 601 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Sett' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 8 | 5-6 | 601 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Lillia' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- O JSON estruturado é a fonte primária para estado de decisão, máscaras, política e recompensas; .tft é analisado apenas para jogadores sem sidecar JSON.- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
