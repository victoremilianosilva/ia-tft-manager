# Auditoria da partida TFT

- Arquivos lidos: **8**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **4625**
- Achados: **70**
- CRITICAL: 0 | HIGH: 11 | MEDIUM: 59 | LOW: 0

- Decisões analisadas enquanto os jogadores estavam vivos: **3895**
- Entradas posteriores à eliminação ignoradas: **730**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 123 | 123 | 123 | 0 | 122 | 0 | 123 | 123 | 123 | 39/25 |
| Jogador 2 | 223 | 223 | 223 | 0 | 219 | 0 | 223 | 223 | 223 | 66/52 |
| Jogador 3 | 160 | 160 | 160 | 0 | 159 | 0 | 160 | 160 | 160 | 44/29 |
| Jogador 4 | 205 | 205 | 205 | 0 | 199 | 0 | 205 | 205 | 205 | 59/43 |
| Jogador 5 | 194 | 194 | 194 | 0 | 193 | 0 | 194 | 194 | 194 | 63/48 |
| Jogador 6 | 148 | 148 | 148 | 0 | 146 | 0 | 148 | 148 | 148 | 53/40 |
| Jogador 7 | 146 | 146 | 146 | 0 | 145 | 0 | 146 | 146 | 146 | 37/24 |
| Jogador 8 | 187 | 187 | 187 | 0 | 183 | 0 | 187 | 187 | 187 | 52/39 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.0018307692371308804 | 0.0 | 0.0 | +— / -ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +a8111a04-3067-4ce6-9a4b-4f5bb205f413 / -— |
| Jogador 1 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.5990749597549438 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0420212745666504 | 0.0 | 0.0 | +cde2c30a-df2c-4275-86ef-e4a4a13a5be1 / -— |
| Jogador 1 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3530687689781189 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.1686171442270279 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30755534768104553 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 15 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 16 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 18 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4829709231853485 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 20 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1626153141260147 | 0.0 | 0.0 | +24247863-54d4-4674-86e9-9a45609a440e / -— |
| Jogador 1 | 1-3 | 21 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17975932359695435 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 22 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 30 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4006744921207428 | 0.0 | 0.0 | +— / -24247863-54d4-4674-86e9-9a45609a440e |
| Jogador 1 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0381423234939575 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -— |
| Jogador 1 | 1-4 | 32 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.13978111743927 | 0.0 | 0.0 | +— / -c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 1-4 | 33 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1182391345500946 | 0.0 | 0.0 | +9a936ebd-aacd-4366-a1c8-78534d5a253b / -— |
| Jogador 1 | 1-4 | 34 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6927846074104309 | 0.0 | 0.0 | +— / -9a936ebd-aacd-4366-a1c8-78534d5a253b |
| Jogador 1 | 1-4 | 35 | PASS | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 40 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1829160451889038 | 0.0 | 0.0 | +3a74be8d-bf7c-4449-9f1b-d76521e73e6f / -— |
| Jogador 1 | 2-1 | 41 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.380165696144104 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 42 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5684478878974915 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 43 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.21551617980003357 | 0.0 | 0.0 | +57652644-f861-47bc-addd-90760a272b22 / -— |
| Jogador 1 | 2-1 | 44 | BUY_XP | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 45 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 50 | SELL | STABILIZE | 96.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33136922121047974 | 0.0 | 0.0 | +— / -57652644-f861-47bc-addd-90760a272b22 |
| Jogador 1 | 2-2 | 51 | BUY | STABILIZE | 96.0 | 4 | 8 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0286104679107666 | 0.0 | 0.0 | +7aea963f-f0a4-4fa2-8da0-cc5eb260f665 / -— |
| Jogador 1 | 2-2 | 52 | BUY | STABILIZE | 96.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35835713148117065 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 53 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21587814390659332 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 54 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32909682393074036 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 55 | PASS | STABILIZE | 96.0 | 4 | 3 | 0 | 12.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 60 | SELL | STABILIZE | 89.0 | 4 | 9 | 0 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6969895362854004 | 0.0 | 0.0 | +— / -7aea963f-f0a4-4fa2-8da0-cc5eb260f665 |
| Jogador 1 | 2-3 | 61 | SELL | STABILIZE | 89.0 | 4 | 11 | 1 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40214627981185913 | 0.0 | 0.0 | +— / -3a74be8d-bf7c-4449-9f1b-d76521e73e6f |
| Jogador 1 | 2-3 | 62 | BUY | STABILIZE | 89.0 | 4 | 13 | 1 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2179591804742813 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 1 | 2-3 | 63 | SELL | STABILIZE | 89.0 | 4 | 11 | 1 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7081384658813477 | 0.0 | 0.0 | +— / -73185d11-22d3-4a1d-803a-b37e82272098 |
| Jogador 1 | 2-3 | 64 | BUY | STABILIZE | 89.0 | 4 | 13 | 1 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17879866063594818 | 0.0 | 0.0 | +ff10e482-7085-4e73-8a0c-fdd3f4938128 / -— |
| Jogador 1 | 2-3 | 65 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 11 | 1 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3986627757549286 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 66 | BUY_XP | STABILIZE | 89.0 | 4 | 11 | 1 | 10.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0533050000667572 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 67 | MOVE_BENCH | SLOWROLL | 89.0 | 5 | 7 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6694199442863464 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 68 | BUY | SLOWROLL | 89.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.10823601484298706 | 0.0 | 0.0 | +6951a681-f5b9-4c22-9182-46b4d2c3cbb3 / -— |
| Jogador 1 | 2-4 | 70 | SELL | SLOWROLL | 83.0 | 5 | 11 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32269880175590515 | 0.0 | 0.0 | +— / -6951a681-f5b9-4c22-9182-46b4d2c3cbb3 |
| Jogador 1 | 2-4 | 71 | BUY | SLOWROLL | 83.0 | 5 | 13 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.28511738777160645 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 72 | BUY | SLOWROLL | 83.0 | 5 | 10 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14313305914402008 | 0.0 | 0.0 | +8c5a0cda-86da-4f36-bee3-c2eae934e263 / -— |
| Jogador 1 | 2-4 | 73 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 8 | 0 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16991502046585083 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 74 | MOVE_BOARD | SLOWROLL | 83.0 | 5 | 8 | 0 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 75 | PASS | SLOWROLL | 83.0 | 5 | 8 | 0 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 79 | BUY | SLOWROLL | 83.0 | 5 | 14 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.263701856136322 | 0.0 | 0.0 | +0c9ac713-08bd-4fa7-a94a-2ab70d7815ff / -— |
| Jogador 1 | 2-5 | 80 | BUY | SLOWROLL | 83.0 | 5 | 11 | 1 | 16.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22445107996463776 | 0.0 | 0.0 | +760d5bee-7d64-4f03-abf0-6357c914a1ed / -— |
| Jogador 1 | 2-5 | 81 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 9 | 0 | 16.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8378760814666748 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 82 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 9 | 0 | 16.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22179296612739563 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 83 | PASS | SLOWROLL | 83.0 | 5 | 9 | 0 | 18.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 88 | BUY | SLOWROLL | 77.0 | 5 | 15 | 1 | 18.0 | Colosso/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.908027708530426 | 0.0 | 0.0 | +2fd4f2d8-6e40-439a-a96d-3e49e05779ad / -— |
| Jogador 1 | 2-6 | 89 | BUY | SLOWROLL | 77.0 | 5 | 12 | 1 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9077381491661072 | 0.0 | 0.0 | +af132466-c7bd-40ad-9848-b79d59a5915c / -— |
| Jogador 1 | 2-6 | 90 | MOVE_BENCH | SLOWROLL | 77.0 | 5 | 11 | 1 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2877718508243561 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 91 | MOVE_BENCH | SLOWROLL | 77.0 | 5 | 11 | 1 | 16.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8345738053321838 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 92 | MOVE_BENCH | SLOWROLL | 77.0 | 5 | 11 | 1 | 16.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2441367208957672 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 93 | PASS | SLOWROLL | 77.0 | 5 | 11 | 1 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 97 | BUY | SLOWROLL | 70.0 | 5 | 19 | 1 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17130930721759796 | 0.0 | 0.0 | +3fc2815d-c456-47c3-bb27-783336b3cdfa / -— |
| Jogador 1 | 2-7 | 98 | BUY | SLOWROLL | 70.0 | 5 | 17 | 1 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2275330275297165 | 0.0 | 0.0 | +acbbcd0d-6bd9-4b4b-ab3b-96ae01c553ce / -— |
| Jogador 1 | 2-7 | 99 | PASS | SLOWROLL | 70.0 | 5 | 16 | 1 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 106 | BUY | SLOWROLL | 70.0 | 5 | 24 | 2 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7469075918197632 | 0.0 | 0.0 | +8e819ba6-a356-4d9b-a8c9-7493332900fb / -— |
| Jogador 1 | 3-1 | 107 | PASS | SLOWROLL | 70.0 | 5 | 22 | 2 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 115 | SELL | SLOWROLL | 59.0 | 5 | 32 | 3 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020333237946033478 | 0.0 | 0.0 | +— / -3fc2815d-c456-47c3-bb27-783336b3cdfa |
| Jogador 1 | 3-2 | 116 | BUY | SLOWROLL | 59.0 | 5 | 34 | 3 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05386067554354668 | 0.0 | 0.0 | +9fe58106-e0c4-4ecc-b152-13c8c0eb564e / -— |
| Jogador 1 | 3-2 | 117 | SELL | SLOWROLL | 59.0 | 5 | 31 | 3 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025123076513409615 | 0.0 | 0.0 | +— / -ff10e482-7085-4e73-8a0c-fdd3f4938128 |
| Jogador 1 | 3-2 | 118 | BUY | SLOWROLL | 59.0 | 5 | 33 | 3 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3707936704158783 | 0.0 | 0.0 | +145f7470-8c0f-4957-b8d6-97939ddaeba1 / -— |
| Jogador 1 | 3-2 | 119 | PASS | SLOWROLL | 59.0 | 5 | 29 | 2 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 124 | SELL | SLOWROLL | 48.0 | 5 | 39 | 3 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10598461329936981 | 0.0 | 0.0 | +— / -9fe58106-e0c4-4ecc-b152-13c8c0eb564e |
| Jogador 1 | 3-3 | 125 | BUY | SLOWROLL | 48.0 | 5 | 42 | 4 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6806423664093018 | 0.0 | 0.0 | +c30e7bdb-41d6-423c-9d7d-2e146472e724 / -— |
| Jogador 1 | 3-3 | 126 | SELL | SLOWROLL | 48.0 | 5 | 39 | 3 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6869879364967346 | 0.0 | 0.0 | +— / -2718f555-b782-4fea-a68f-31395ad34232 |
| Jogador 1 | 3-3 | 127 | BUY | SLOWROLL | 48.0 | 5 | 40 | 4 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.675747811794281 | 0.0 | 0.0 | +e6ee6b15-d413-4678-8ffb-29272199a53d / -— |
| Jogador 1 | 3-3 | 128 | PASS | SLOWROLL | 48.0 | 5 | 38 | 3 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 133 | REROLL | STABILIZE | 38.0 | 5 | 49 | 4 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 134 | SELL | STABILIZE | 38.0 | 5 | 47 | 4 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39081910252571106 | 0.0 | 0.0 | +— / -af132466-c7bd-40ad-9848-b79d59a5915c |
| Jogador 1 | 3-4 | 135 | BUY | STABILIZE | 38.0 | 5 | 48 | 4 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7982701659202576 | 0.0 | 0.0 | +f6e6e08d-ecfe-4c84-acfa-6ad8292968ee / -— |
| Jogador 1 | 3-4 | 136 | REROLL | STABILIZE | 38.0 | 5 | 47 | 4 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 137 | REROLL | STABILIZE | 38.0 | 5 | 45 | 4 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 138 | SELL | STABILIZE | 38.0 | 5 | 43 | 4 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7346245646476746 | 0.0 | 0.0 | +— / -f6e6e08d-ecfe-4c84-acfa-6ad8292968ee |
| Jogador 1 | 3-4 | 139 | BUY | STABILIZE | 38.0 | 5 | 44 | 4 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2872644364833832 | 0.0 | 0.0 | +ccdd8153-af58-4fe7-994c-d49f0a7a17f8 / -— |
| Jogador 1 | 3-4 | 140 | REROLL | STABILIZE | 38.0 | 5 | 40 | 4 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17399999499320984 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 142 | SELL | STABILIZE | 38.0 | 6 | 49 | 4 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2783503830432892 | 0.0 | 0.0 | +— / -acbbcd0d-6bd9-4b4b-ab3b-96ae01c553ce |
| Jogador 1 | 3-5 | 143 | BUY | STABILIZE | 38.0 | 6 | 50 | 5 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24610848724842072 | 0.0 | 0.0 | +4af85188-f11e-4aca-8165-ba8e7f535670 / -— |
| Jogador 1 | 3-5 | 144 | MOVE_BENCH | STABILIZE | 38.0 | 6 | 48 | 4 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7431392669677734 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 145 | MOVE_BENCH | STABILIZE | 38.0 | 6 | 48 | 4 | 20.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2207861691713333 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 146 | MOVE_BENCH | STABILIZE | 38.0 | 6 | 48 | 4 | 20.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5168197154998779 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 147 | MOVE_BENCH | STABILIZE | 38.0 | 6 | 48 | 4 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7439250349998474 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 148 | PASS | STABILIZE | 38.0 | 6 | 48 | 4 | 20.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04271111264824867 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 150 | MOVE_BENCH | STABILIZE | 38.0 | 6 | 48 | 4 | 20.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8372431993484497 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 152 | BUY | STABILIZE | 27.0 | 6 | 60 | 5 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3157438337802887 | 0.0 | 0.0 | +bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 / -— |
| Jogador 1 | 3-6 | 153 | REROLL | STABILIZE | 27.0 | 6 | 59 | 5 | 26.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 154 | SELL | STABILIZE | 27.0 | 6 | 57 | 5 | 26.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3591538369655609 | 0.0 | 0.0 | +— / -bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 |
| Jogador 1 | 3-6 | 155 | BUY | STABILIZE | 27.0 | 6 | 58 | 5 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05052993819117546 | 0.0 | 0.0 | +691cde76-cf1b-4a60-b818-65f790e312ec / -— |
| Jogador 1 | 3-6 | 156 | REROLL | STABILIZE | 27.0 | 6 | 56 | 5 | 26.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 157 | SELL | STABILIZE | 27.0 | 6 | 54 | 5 | 26.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.045239612460136414 | 0.0 | 0.0 | +— / -691cde76-cf1b-4a60-b818-65f790e312ec |
| Jogador 1 | 3-6 | 158 | BUY | STABILIZE | 27.0 | 6 | 56 | 5 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15646660327911377 | 0.0 | 0.0 | +604a85af-ff68-41a7-8795-73fdc7723c0e / -— |
| Jogador 1 | 3-6 | 159 | MOVE_BENCH | STABILIZE | 27.0 | 6 | 52 | 5 | 26.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15318718552589417 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 160 | REROLL | STABILIZE | 27.0 | 6 | 52 | 5 | 24.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 162 | SELL | STABILIZE | 17.0 | 6 | 63 | 5 | 24.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.769289493560791 | 0.0 | 0.0 | +— / -e6ee6b15-d413-4678-8ffb-29272199a53d |
| Jogador 1 | 3-7 | 163 | BUY | STABILIZE | 17.0 | 6 | 65 | 5 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23941947519779205 | 0.0 | 0.0 | +a14e4b8f-77c5-4909-a9ee-0044b836a877 / -— |
| Jogador 1 | 3-7 | 164 | REROLL | STABILIZE | 17.0 | 6 | 62 | 5 | 24.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 165 | SELL | STABILIZE | 17.0 | 6 | 60 | 5 | 24.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060600001364946365 | 0.0 | 0.0 | +— / -a14e4b8f-77c5-4909-a9ee-0044b836a877 |
| Jogador 1 | 3-7 | 166 | BUY | STABILIZE | 17.0 | 6 | 63 | 5 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009839324280619621 | 0.0 | 0.0 | +b2a77bec-e150-4d98-847c-9f2cfb50cbe7 / -— |
| Jogador 1 | 3-7 | 167 | SELL | STABILIZE | 17.0 | 6 | 60 | 5 | 24.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04330839216709137 | 0.0 | 0.0 | +— / -b2a77bec-e150-4d98-847c-9f2cfb50cbe7 |
| Jogador 1 | 3-7 | 168 | BUY | STABILIZE | 17.0 | 6 | 63 | 5 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27716416120529175 | 0.0 | 0.0 | +1e81ac95-667f-494d-89eb-2bcdcf887a7e / -— |
| Jogador 1 | 3-7 | 169 | REROLL | STABILIZE | 17.0 | 6 | 59 | 5 | 24.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 170 | SELL | STABILIZE | 17.0 | 6 | 57 | 5 | 24.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07426153868436813 | 0.0 | 0.0 | +— / -1e81ac95-667f-494d-89eb-2bcdcf887a7e |
| Jogador 1 | 4-1 | 172 | BUY | STABILIZE | 17.0 | 6 | 74 | 5 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0054513216018677 | 0.0 | 0.0 | +23793b7b-2dab-48f0-a8ba-db85fc14c1c5 / -2fd4f2d8-6e40-439a-a96d-3e49e05779ad,d01cae02-d8ba-491e-841f-bf3120953933 |
| Jogador 1 | 4-1 | 173 | BUY | STABILIZE | 17.0 | 6 | 71 | 5 | 18.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2806181013584137 | 0.0 | 0.0 | +9cb61b5c-2c8a-43a2-a854-517f4377f6db / -— |
| Jogador 1 | 4-1 | 174 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 68 | 5 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.20841732621192932 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 175 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 68 | 5 | 20.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.5286775231361389 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 176 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 68 | 5 | 20.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.14991936087608337 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 177 | PASS | STABILIZE | 17.0 | 6 | 68 | 5 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.14115041494369507 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 180 | MOVE_BENCH | STABILIZE | 17.0 | 6 | 68 | 5 | 18.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4520382285118103 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 182 | BUY | ALL_IN | 6.0 | 6 | 81 | 5 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.17624254524707794 | 0.0 | 0.0 | +84886290-556f-45e9-805b-9ca86a80ba27 / -— |
| Jogador 1 | 4-2 | 183 | REROLL | ALL_IN | 6.0 | 6 | 79 | 5 | 26.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 184 | REROLL | ALL_IN | 6.0 | 6 | 77 | 5 | 26.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 185 | CRAFT_AND_EQUIP | ALL_IN | 6.0 | 6 | 75 | 5 | 26.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.11010857671499252 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 186 | REROLL | ALL_IN | 6.0 | 6 | 75 | 5 | 26.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 187 | REROLL | ALL_IN | 6.0 | 6 | 73 | 5 | 26.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 188 | SELL | ALL_IN | 6.0 | 6 | 71 | 5 | 26.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016254615038633347 | 0.0 | 0.0 | +— / -84886290-556f-45e9-805b-9ca86a80ba27 |
| Jogador 1 | 4-2 | 189 | BUY | ALL_IN | 6.0 | 6 | 73 | 5 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9202665090560913 | 0.0 | 0.0 | +b755a0c5-f515-4f95-8f58-1e05f40ad302 / -— |
| Jogador 1 | 4-2 | 190 | REROLL | ALL_IN | 6.0 | 6 | 71 | 5 | 26.0 | Colosso/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.01586153917014599 | 0.0 | 0.0 | +— / -fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3124316334724426 | 0.0 | 0.0 | +292ef825-d326-4dd8-9c42-c47cfc62116f / -— |
| Jogador 2 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.5844191908836365 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +94ede66e-59bc-4c41-aabf-f64372e20f9a / -— |
| Jogador 2 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3530687689781189 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.25811290740966797 | 0.0 | 0.0 | +5a1572b3-8b27-4d87-b885-f342b91c0854 / -— |
| Jogador 2 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3084859549999237 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 15 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 16 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 18 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4508800506591797 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 20 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2416125386953354 | 0.0 | 0.0 | +de00430a-8a57-423c-887c-317d53c2cdd3 / -— |
| Jogador 2 | 1-3 | 21 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35666486620903015 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 22 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 30 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4548526704311371 | 0.0 | 0.0 | +— / -5a1572b3-8b27-4d87-b885-f342b91c0854 |
| Jogador 2 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2815471887588501 | 0.0 | 0.0 | +9a6f90da-bbac-4ba0-b2a3-729a1a2deab5 / -— |
| Jogador 2 | 1-4 | 32 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7269346714019775 | 0.0 | 0.0 | +— / -9a6f90da-bbac-4ba0-b2a3-729a1a2deab5 |
| Jogador 2 | 1-4 | 33 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09304504096508026 | 0.0 | 0.0 | +0023ba20-d605-41fb-8002-3b6920635c59 / -— |
| Jogador 2 | 1-4 | 34 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 40 | SELL | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6961044073104858 | 0.0 | 0.0 | +— / -0023ba20-d605-41fb-8002-3b6920635c59 |
| Jogador 2 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3180779814720154 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 42 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3620184361934662 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 43 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.500612199306488 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 44 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.21587814390659332 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 45 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.11033560335636139 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 46 | PASS | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 50 | BUY | STABILIZE | 95.0 | 4 | 10 | 1 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.030463775619864464 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 51 | BUY_XP | STABILIZE | 95.0 | 4 | 8 | 0 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 52 | BUY_XP | STABILIZE | 95.0 | 4 | 4 | 0 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04550499841570854 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 53 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 0 | 0 | 14.0 | —/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44121962785720825 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 54 | PASS | SLOWROLL | 95.0 | 5 | 0 | 0 | 18.0 | —/DA_Vi18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 60 | BUY | SLOWROLL | 95.0 | 5 | 6 | 0 | 18.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2485928237438202 | 0.0 | 0.0 | +8c364966-f97c-4f54-b087-ddd182a9f8ea / -— |
| Jogador 2 | 2-3 | 61 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 3 | 0 | 18.0 | —/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27834683656692505 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 62 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 3 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03484884649515152 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 63 | PASS | STABILIZE | 95.0 | 5 | 3 | 0 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 70 | BUY | STABILIZE | 95.0 | 5 | 10 | 1 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2433420866727829 | 0.0 | 0.0 | +2ace989d-3e9e-483b-9b14-cd6b8f171f17 / -— |
| Jogador 2 | 2-4 | 71 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 7 | 0 | 20.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24143987894058228 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 72 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 7 | 0 | 20.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 73 | PASS | STABILIZE | 95.0 | 5 | 7 | 0 | 20.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 79 | BUY | STABILIZE | 95.0 | 5 | 13 | 1 | 20.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34116172790527344 | 0.0 | 0.0 | +081b684f-5d42-45c5-9a68-12127e5330a7 / -— |
| Jogador 2 | 2-5 | 80 | PASS | STABILIZE | 95.0 | 5 | 10 | 1 | 20.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 88 | SELL | SLOWROLL | 95.0 | 5 | 18 | 1 | 20.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07132399082183838 | 0.0 | 0.0 | +— / -561fb9a8-e987-4935-b11c-6c6104ced65d |
| Jogador 2 | 2-6 | 89 | SELL | SLOWROLL | 95.0 | 5 | 20 | 2 | 20.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02151300385594368 | 0.0 | 0.0 | +— / -8c364966-f97c-4f54-b087-ddd182a9f8ea |
| Jogador 2 | 2-6 | 90 | SELL | SLOWROLL | 95.0 | 5 | 23 | 2 | 20.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4695185720920563 | 0.0 | 0.0 | +— / -081b684f-5d42-45c5-9a68-12127e5330a7 |
| Jogador 2 | 2-6 | 91 | BUY | SLOWROLL | 95.0 | 5 | 26 | 2 | 20.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9743034839630127 | 0.0 | 0.0 | +6f3f86ec-6928-4032-a1ef-533a68865516 / -— |
| Jogador 2 | 2-6 | 92 | MOVE_BOARD | SLOWROLL | 95.0 | 5 | 24 | 2 | 20.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 93 | MOVE_BOARD | SLOWROLL | 95.0 | 5 | 24 | 2 | 20.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10707494616508484 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 94 | PASS | SLOWROLL | 95.0 | 5 | 24 | 2 | 20.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.021607141941785812 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 97 | SELL | SLOWROLL | 95.0 | 5 | 33 | 3 | 20.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.1636360883712769 | 0.0 | 0.0 | +— / -6f3f86ec-6928-4032-a1ef-533a68865516 |
| Jogador 2 | 2-7 | 98 | BUY | SLOWROLL | 95.0 | 5 | 35 | 3 | 20.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.1727232187986374 | 0.0 | 0.0 | +729ccd5b-adc5-4bca-9523-dcb532e93ecb / -— |
| Jogador 2 | 2-7 | 99 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 32 | 3 | 20.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27847006916999817 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 100 | BUY_XP | SLOWROLL | 95.0 | 5 | 32 | 3 | 22.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1379999965429306 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 101 | BUY_XP | SLOWROLL | 95.0 | 5 | 28 | 2 | 22.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 102 | BUY_XP | SLOWROLL | 95.0 | 5 | 24 | 2 | 22.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019509999081492424 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 103 | MOVE_BENCH | SLOWROLL | 95.0 | 6 | 20 | 2 | 22.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5440780520439148 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 104 | MOVE_BOARD | FAST8 | 95.0 | 6 | 20 | 2 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.032957449555397034 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 106 | BUY | FAST8 | 95.0 | 6 | 28 | 2 | 26.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8024701476097107 | 0.0 | 0.0 | +a0ebc646-2e71-4b07-9208-401aa0cda6bb / -292ef825-d326-4dd8-9c42-c47cfc62116f,94ede66e-59bc-4c41-aabf-f64372e20f9a |
| Jogador 2 | 3-1 | 107 | MOVE_BENCH | SLOWROLL | 95.0 | 6 | 27 | 2 | 22.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.136034294962883 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 108 | MOVE_BENCH | SLOWROLL | 95.0 | 6 | 27 | 2 | 22.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00870288722217083 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 109 | MOVE_BENCH | SLOWROLL | 95.0 | 6 | 27 | 2 | 20.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3452886641025543 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 110 | MOVE_BENCH | SLOWROLL | 95.0 | 6 | 27 | 2 | 22.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1390526443719864 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 111 | MOVE_BENCH | SLOWROLL | 95.0 | 6 | 27 | 2 | 22.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009235949255526066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 112 | MOVE_BENCH | SLOWROLL | 95.0 | 6 | 27 | 2 | 20.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2332158386707306 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 113 | BUY | FAST8 | 95.0 | 6 | 27 | 2 | 26.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.16566093266010284 | 0.0 | 0.0 | +e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 / -— |
| Jogador 2 | 3-2 | 115 | MOVE_BENCH | FAST8 | 85.0 | 6 | 31 | 3 | 26.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6470744013786316 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 116 | SELL | FAST8 | 85.0 | 6 | 31 | 3 | 28.0 | Colosso/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5590000152587891 | 0.0 | 0.0 | +— / -a0ebc646-2e71-4b07-9208-401aa0cda6bb |
| Jogador 2 | 3-2 | 117 | BUY | FAST8 | 85.0 | 6 | 34 | 3 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2534838020801544 | 0.0 | 0.0 | +584e7960-a541-4d45-8ea1-8a75e288c387 / -— |
| Jogador 2 | 3-2 | 118 | BUY_XP | FAST8 | 85.0 | 6 | 33 | 3 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1035500019788742 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 119 | BUY_XP | FAST8 | 85.0 | 6 | 29 | 2 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02355000004172325 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 120 | BUY_XP | FAST8 | 85.0 | 6 | 25 | 2 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02355000004172325 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 121 | BUY_XP | FAST8 | 85.0 | 6 | 21 | 2 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 122 | MOVE_BENCH | FAST8 | 85.0 | 6 | 17 | 1 | 28.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5625905394554138 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 124 | BUY | FAST8 | 85.0 | 6 | 24 | 2 | 30.0 | Colosso/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.056617371737957 | 0.0 | 0.0 | +4e116bc2-f686-4a17-adb1-a7b80865c159 / -— |
| Jogador 2 | 3-3 | 125 | MOVE_BENCH | FAST8 | 85.0 | 6 | 20 | 2 | 30.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5166208148002625 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 126 | MOVE_BENCH | FAST8 | 85.0 | 6 | 20 | 2 | 32.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3232147693634033 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 127 | PASS | FAST8 | 85.0 | 6 | 20 | 2 | 34.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05849999934434891 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 133 | BUY | FAST8 | 85.0 | 6 | 29 | 2 | 34.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027313657104969025 | 0.0 | 0.0 | +8edef2b0-f5b3-4c01-ba2b-851be248676e / -— |
| Jogador 2 | 3-4 | 134 | BUY_XP | FAST8 | 85.0 | 6 | 27 | 2 | 34.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001449999981559813 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 135 | BUY_XP | FAST8 | 85.0 | 6 | 23 | 2 | 34.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 136 | BUY_XP | FAST8 | 85.0 | 6 | 19 | 1 | 34.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07689999788999557 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 137 | MOVE_BENCH | FAST8 | 85.0 | 7 | 15 | 1 | 34.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6308958530426025 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 138 | MOVE_BENCH | FAST8 | 85.0 | 7 | 15 | 1 | 32.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35037294030189514 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 139 | PASS | FAST8 | 85.0 | 7 | 15 | 1 | 30.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0560000017285347 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 142 | BUY | FAST8 | 85.0 | 7 | 22 | 2 | 34.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.191989466547966 | 0.0 | 0.0 | +6db008fd-a1dd-40ad-b3d2-583a4bbff9d4 / -— |
| Jogador 2 | 3-5 | 143 | BUY_XP | FAST8 | 85.0 | 7 | 19 | 1 | 34.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 144 | BUY_XP | FAST8 | 85.0 | 7 | 15 | 1 | 34.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 145 | BUY_XP | FAST8 | 85.0 | 7 | 11 | 1 | 34.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 146 | BUY_XP | FAST8 | 85.0 | 7 | 7 | 0 | 34.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 147 | PASS | FAST8 | 85.0 | 7 | 3 | 0 | 34.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 152 | BUY | FAST8 | 85.0 | 7 | 10 | 1 | 34.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6550741791725159 | 0.0 | 0.0 | +cf68219b-1d38-45a1-98db-495871c932ea / -— |
| Jogador 2 | 3-6 | 153 | MOVE_BENCH | FAST8 | 85.0 | 7 | 8 | 0 | 34.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4980248510837555 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 154 | MOVE_BENCH | FAST8 | 85.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17894475162029266 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 155 | PASS | FAST8 | 85.0 | 7 | 8 | 0 | 38.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 162 | BUY | FAST8 | 85.0 | 7 | 15 | 1 | 38.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.043422818183898926 | 0.0 | 0.0 | +75d9034d-80ed-40d3-a330-44554cc2bb9e / -— |
| Jogador 2 | 3-7 | 163 | BUY_XP | FAST8 | 85.0 | 7 | 11 | 1 | 38.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 164 | BUY_XP | FAST8 | 85.0 | 7 | 7 | 0 | 38.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 165 | PASS | FAST8 | 85.0 | 7 | 3 | 0 | 38.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 172 | BUY | FAST8 | 85.0 | 7 | 9 | 0 | 38.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4442198872566223 | 0.0 | 0.0 | +9bd6852a-b7a4-468c-a8cc-5318f7906eae / -— |
| Jogador 2 | 4-1 | 173 | BUY_XP | FAST8 | 85.0 | 7 | 6 | 0 | 38.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 174 | PASS | FAST8 | 85.0 | 7 | 2 | 0 | 38.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 182 | BUY | FAST8 | 71.0 | 7 | 7 | 0 | 38.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21756914258003235 | 0.0 | 0.0 | +2001a193-3868-4a3f-8a71-3a9f95c04a02 / -— |
| Jogador 2 | 4-2 | 183 | BUY | FAST8 | 71.0 | 7 | 6 | 0 | 38.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1735454797744751 | 0.0 | 0.0 | +235510e3-df54-4de9-9bcf-bff6d47e364a / -— |
| Jogador 2 | 4-2 | 184 | BUY_XP | FAST8 | 71.0 | 7 | 4 | 0 | 38.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 185 | PASS | FAST8 | 71.0 | 7 | 0 | 0 | 38.0 | Colosso/DA_Nidalee18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 192 | BUY | FAST8 | 71.0 | 7 | 6 | 0 | 38.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7107187509536743 | 0.0 | 0.0 | +11b28280-bb53-4ca7-81b7-5ce8705303a5 / -— |
| Jogador 2 | 4-3 | 193 | PASS | FAST8 | 71.0 | 7 | 4 | 0 | 38.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 202 | BUY | FAST8 | 71.0 | 7 | 11 | 1 | 38.0 | Colosso/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5263725519180298 | 0.0 | 0.0 | +99182042-c4b9-4801-b66a-1f4432d301f3 / -6db008fd-a1dd-40ad-b3d2-583a4bbff9d4,9bd6852a-b7a4-468c-a8cc-5318f7906eae |
| Jogador 2 | 4-4 | 203 | BUY | FAST8 | 71.0 | 7 | 8 | 0 | 38.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20243948698043823 | 0.0 | 0.0 | +6e1d8af0-7f7c-4ec1-967c-e871072bc4e3 / -— |
| Jogador 2 | 4-4 | 204 | PASS | FAST8 | 71.0 | 7 | 5 | 0 | 38.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 212 | BUY | FAST8 | 71.0 | 7 | 11 | 1 | 38.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1270322948694229 | 0.0 | 0.0 | +362f7357-283e-4f88-bff3-ffa6314af821 / -— |
| Jogador 2 | 4-5 | 213 | PASS | FAST8 | 71.0 | 7 | 9 | 0 | 38.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 222 | SELL | FAST8 | 71.0 | 7 | 15 | 1 | 38.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32550209760665894 | 0.0 | 0.0 | +— / -235510e3-df54-4de9-9bcf-bff6d47e364a |
| Jogador 2 | 4-6 | 223 | BUY | FAST8 | 71.0 | 7 | 17 | 1 | 38.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7375787496566772 | 0.0 | 0.0 | +e270a6b1-23dd-49a0-8694-ba911eae4c71 / -— |
| Jogador 2 | 4-6 | 224 | PASS | FAST8 | 71.0 | 7 | 16 | 1 | 38.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025714285671710968 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 232 | PASS | FAST8 | 71.0 | 7 | 23 | 2 | 38.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030714286491274834 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 242 | EQUIP_FROM_INVENTORY | ECON | 71.0 | 8 | 31 | 3 | 38.0 | Colosso/DA_18_Rammus | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 243 | SELL | ECON | 71.0 | 8 | 31 | 3 | 38.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03805037960410118 | 0.0 | 0.0 | +— / -11b28280-bb53-4ca7-81b7-5ce8705303a5 |
| Jogador 2 | 5-1 | 244 | BUY | ECON | 71.0 | 8 | 33 | 3 | 38.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7693427801132202 | 0.0 | 0.0 | +9c3b3b78-e99c-4947-b958-cce156ecccb1 / -— |
| Jogador 2 | 5-1 | 245 | SELL | ECON | 71.0 | 8 | 30 | 3 | 38.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.039861537516117096 | 0.0 | 0.0 | +— / -8edef2b0-f5b3-4c01-ba2b-851be248676e |
| Jogador 2 | 5-1 | 246 | BUY | ECON | 71.0 | 8 | 32 | 3 | 38.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07092124223709106 | 0.0 | 0.0 | +a37d8478-8a98-4099-bb18-3602d68764f5 / -— |
| Jogador 2 | 5-1 | 247 | MOVE_BENCH | ECON | 71.0 | 8 | 27 | 2 | 38.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.14069923758506775 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 248 | MOVE_BENCH | ECON | 71.0 | 8 | 27 | 2 | 34.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.53466796875 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 249 | BUY | ECON | 71.0 | 8 | 27 | 2 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.33751609921455383 | 0.0 | 0.0 | +b311d350-7bab-48ee-9833-0883606b4a2f / -— |
| Jogador 2 | 5-1 | 250 | REROLL | ECON | 71.0 | 8 | 24 | 2 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 252 | SELL | WINSTREAK | 71.0 | 8 | 31 | 3 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.30960461497306824 | 0.0 | 0.0 | +— / -b311d350-7bab-48ee-9833-0883606b4a2f |
| Jogador 2 | 5-2 | 253 | BUY | WINSTREAK | 71.0 | 8 | 34 | 3 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9014837145805359 | 0.0 | 0.0 | +b0f8dc80-dd2b-4dde-87a9-b855a1c13da5 / -6e1d8af0-7f7c-4ec1-967c-e871072bc4e3,9c3b3b78-e99c-4947-b958-cce156ecccb1 |
| Jogador 2 | 5-2 | 254 | BUY | WINSTREAK | 71.0 | 8 | 31 | 3 | 40.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8251770734786987 | 0.0 | 0.0 | +54b8f150-85a6-4fad-9a4f-3b04897733cf / -cf68219b-1d38-45a1-98db-495871c932ea,de00430a-8a57-423c-887c-317d53c2cdd3 |
| Jogador 2 | 5-2 | 255 | BUY | WINSTREAK | 71.0 | 8 | 29 | 2 | 36.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.14622598886489868 | 0.0 | 0.0 | +ffd44f6f-388e-4792-ae4f-77f2faa3e95f / -— |
| Jogador 2 | 5-2 | 256 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 25 | 2 | 36.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07537882030010223 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 257 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 25 | 2 | 40.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.6399606466293335 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 258 | PASS | WINSTREAK | 71.0 | 8 | 25 | 2 | 46.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.1233571395277977 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 260 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 25 | 2 | 46.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6066949963569641 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 262 | BUY | WINSTREAK | 71.0 | 8 | 34 | 3 | 54.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.02761061303317547 | 0.0 | 0.0 | +23191bf1-a03a-47ab-aa04-1a5b6d86b445 / -— |
| Jogador 2 | 5-3 | 263 | BUY | WINSTREAK | 71.0 | 8 | 29 | 2 | 54.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6939749717712402 | 0.0 | 0.0 | +7904ab26-de3f-4144-b70f-ed620b41c907 / -— |
| Jogador 2 | 5-3 | 264 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 26 | 2 | 54.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1759796291589737 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 265 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 26 | 2 | 48.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2788848578929901 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 266 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 26 | 2 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.4449971318244934 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 267 | PASS | WINSTREAK | 71.0 | 8 | 26 | 2 | 54.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.03614285588264465 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 272 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 36 | 3 | 54.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.1339920610189438 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 273 | SELL | WINSTREAK | 71.0 | 8 | 36 | 3 | 56.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.10048247873783112 | 0.0 | 0.0 | +— / -4e116bc2-f686-4a17-adb1-a7b80865c159 |
| Jogador 2 | 5-4 | 274 | BUY | WINSTREAK | 71.0 | 8 | 40 | 4 | 56.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.30100125074386597 | 0.0 | 0.0 | +6d150146-2d96-4b53-a24b-05a486a348cf / -— |
| Jogador 2 | 5-4 | 275 | SELL | WINSTREAK | 71.0 | 8 | 37 | 3 | 56.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2732153832912445 | 0.0 | 0.0 | +— / -7904ab26-de3f-4144-b70f-ed620b41c907 |
| Jogador 2 | 5-4 | 276 | BUY | WINSTREAK | 71.0 | 8 | 40 | 4 | 56.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.09973547607660294 | 0.0 | 0.0 | +8ec344bd-ba9a-47e6-ba65-a4c832038b18 / -— |
| Jogador 2 | 5-4 | 277 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 36 | 3 | 56.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1066199243068695 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 278 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 36 | 3 | 52.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2524528503417969 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 279 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 36 | 3 | 48.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.9131275415420532 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 280 | PASS | WINSTREAK | 71.0 | 8 | 36 | 3 | 56.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.04399999976158142 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 282 | SELL | WINSTREAK | 71.0 | 8 | 46 | 4 | 56.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.09921444207429886 | 0.0 | 0.0 | +— / -8ec344bd-ba9a-47e6-ba65-a4c832038b18 |
| Jogador 2 | 5-5 | 283 | BUY | WINSTREAK | 71.0 | 8 | 50 | 5 | 56.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6072715520858765 | 0.0 | 0.0 | +61fe2c41-5cc2-4b6b-aa92-c83c3d900c07 / -— |
| Jogador 2 | 5-5 | 284 | SELL | WINSTREAK | 71.0 | 8 | 46 | 4 | 56.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2730615437030792 | 0.0 | 0.0 | +— / -ffd44f6f-388e-4792-ae4f-77f2faa3e95f |
| Jogador 2 | 5-5 | 285 | BUY | WINSTREAK | 71.0 | 8 | 50 | 5 | 56.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2130216509103775 | 0.0 | 0.0 | +d7ce3b58-1354-4970-94e8-17db783b9353 / -— |
| Jogador 2 | 5-5 | 286 | CRAFT_AND_EQUIP | WINSTREAK | 71.0 | 8 | 46 | 4 | 56.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.03895467519760132 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 287 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 46 | 4 | 56.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1433316320180893 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 288 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 46 | 4 | 52.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2631916105747223 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 289 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 46 | 4 | 48.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9170579314231873 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 290 | PASS | WINSTREAK | 71.0 | 8 | 46 | 4 | 56.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05185714364051819 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 292 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 59 | 5 | 56.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009437327273190022 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 293 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 59 | 5 | 52.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19453585147857666 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 294 | MOVE_BENCH | WINSTREAK | 71.0 | 8 | 59 | 5 | 56.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18468549847602844 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 295 | PASS | WINSTREAK | 71.0 | 8 | 59 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09383607655763626 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 302 | SELL | WINSTREAK | 71.0 | 8 | 73 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04472307860851288 | 0.0 | 0.0 | +— / -d7ce3b58-1354-4970-94e8-17db783b9353 |
| Jogador 2 | 5-7 | 303 | BUY | WINSTREAK | 71.0 | 8 | 77 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02839776873588562 | 0.0 | 0.0 | +91539d01-1b4f-442a-99b0-56b534ea8063 / -— |
| Jogador 2 | 5-7 | 304 | SELL | WINSTREAK | 71.0 | 8 | 73 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04472307860851288 | 0.0 | 0.0 | +— / -91539d01-1b4f-442a-99b0-56b534ea8063 |
| Jogador 2 | 5-7 | 305 | BUY | WINSTREAK | 71.0 | 8 | 77 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2574256360530853 | 0.0 | 0.0 | +d09be3d3-5a46-424a-94d9-4bcd4d2a6b30 / -— |
| Jogador 2 | 5-7 | 306 | SELL | WINSTREAK | 71.0 | 8 | 73 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07426153868436813 | 0.0 | 0.0 | +— / -d09be3d3-5a46-424a-94d9-4bcd4d2a6b30 |
| Jogador 2 | 5-7 | 307 | BUY | WINSTREAK | 71.0 | 8 | 77 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1143888309597969 | 0.0 | 0.0 | +2b9c96b0-47c3-4330-894e-c42471aef448 / -— |
| Jogador 2 | 5-7 | 308 | REROLL | WINSTREAK | 71.0 | 8 | 75 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 309 | SELL | WINSTREAK | 71.0 | 8 | 73 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0299538467079401 | 0.0 | 0.0 | +— / -2b9c96b0-47c3-4330-894e-c42471aef448 |
| Jogador 2 | 5-7 | 310 | BUY | WINSTREAK | 71.0 | 8 | 75 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10225452482700348 | 0.0 | 0.0 | +c8f70274-150a-4de3-8eb3-5a635e03ab3a / -— |
| Jogador 2 | 6-1 | 312 | EQUIP_FROM_INVENTORY | WINSTREAK | 71.0 | 8 | 84 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 313 | EQUIP_FROM_INVENTORY | WINSTREAK | 71.0 | 8 | 84 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.12210626900196075 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 314 | SELL | WINSTREAK | 71.0 | 8 | 84 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013707692734897137 | 0.0 | 0.0 | +— / -61fe2c41-5cc2-4b6b-aa92-c83c3d900c07 |
| Jogador 2 | 6-1 | 315 | BUY | WINSTREAK | 71.0 | 8 | 88 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9504823684692383 | 0.0 | 0.0 | +09e28e26-f7f0-4d8a-acca-f768d9205f14 / -— |
| Jogador 2 | 6-1 | 316 | SELL | WINSTREAK | 71.0 | 8 | 86 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03216923028230667 | 0.0 | 0.0 | +— / -c8f70274-150a-4de3-8eb3-5a635e03ab3a |
| Jogador 2 | 6-1 | 317 | BUY | WINSTREAK | 71.0 | 8 | 90 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13749834895133972 | 0.0 | 0.0 | +ffb8808b-40c6-4268-8a8f-9c90095a59b6 / -— |
| Jogador 2 | 6-1 | 318 | SELL | WINSTREAK | 71.0 | 8 | 86 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013707692734897137 | 0.0 | 0.0 | +— / -ffb8808b-40c6-4268-8a8f-9c90095a59b6 |
| Jogador 2 | 6-1 | 319 | BUY | WINSTREAK | 71.0 | 8 | 90 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1967226266860962 | 0.0 | 0.0 | +38b4cb27-ddc9-4488-9d22-eca4612a4bd8 / -— |
| Jogador 2 | 6-1 | 320 | REROLL | WINSTREAK | 71.0 | 8 | 86 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 322 | SELL | ECON | 55.0 | 8 | 94 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011244389228522778 | 0.0 | 0.0 | +— / -38b4cb27-ddc9-4488-9d22-eca4612a4bd8 |
| Jogador 2 | 6-2 | 323 | BUY | ECON | 55.0 | 8 | 98 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9160217642784119 | 0.0 | 0.0 | +e47e9d8e-e703-4b77-8266-2f90680eb62f / -— |
| Jogador 2 | 6-2 | 324 | SELL | ECON | 55.0 | 8 | 95 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.042876921594142914 | 0.0 | 0.0 | +— / -23191bf1-a03a-47ab-aa04-1a5b6d86b445 |
| Jogador 2 | 6-2 | 325 | BUY | ECON | 55.0 | 8 | 100 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36496806144714355 | 0.0 | 0.0 | +44497322-c916-4b15-8631-8f533aeada38 / -— |
| Jogador 2 | 6-2 | 326 | REROLL | ECON | 55.0 | 8 | 97 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 327 | SELL | ECON | 55.0 | 8 | 95 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31580740213394165 | 0.0 | 0.0 | +— / -44497322-c916-4b15-8631-8f533aeada38 |
| Jogador 2 | 6-2 | 328 | BUY | ECON | 55.0 | 8 | 98 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6106422543525696 | 0.0 | 0.0 | +53722e0c-9ca3-44b8-b593-c803870bce62 / -— |
| Jogador 2 | 6-2 | 329 | REROLL | ECON | 55.0 | 8 | 95 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 330 | SELL | ECON | 55.0 | 8 | 93 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3466615378856659 | 0.0 | 0.0 | +— / -53722e0c-9ca3-44b8-b593-c803870bce62 |
| Jogador 2 | 6-3 | 332 | BUY | STABILIZE | 39.0 | 8 | 107 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.613082766532898 | 0.0 | 0.0 | +ae36e82c-bcac-4ad8-b7b1-063966ecc411 / -— |
| Jogador 2 | 6-3 | 333 | SELL | STABILIZE | 39.0 | 8 | 103 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3425999879837036 | 0.0 | 0.0 | +— / -ae36e82c-bcac-4ad8-b7b1-063966ecc411 |
| Jogador 2 | 6-3 | 334 | BUY | STABILIZE | 39.0 | 8 | 107 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013963278383016586 | 0.0 | 0.0 | +8ef30c1a-60fd-4a11-bee3-08c3aa7baa32 / -— |
| Jogador 2 | 6-3 | 335 | REROLL | STABILIZE | 39.0 | 8 | 103 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 336 | SELL | STABILIZE | 39.0 | 8 | 101 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05063077062368393 | 0.0 | 0.0 | +— / -8ef30c1a-60fd-4a11-bee3-08c3aa7baa32 |
| Jogador 2 | 6-3 | 337 | BUY | STABILIZE | 39.0 | 8 | 105 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.079792857170105 | 0.0 | 0.0 | +81d97dc0-cc50-4303-acfe-e8273ef39d35 / -2001a193-3868-4a3f-8a71-3a9f95c04a02,e270a6b1-23dd-49a0-8694-ba911eae4c71 |
| Jogador 2 | 6-3 | 338 | BUY | STABILIZE | 39.0 | 8 | 104 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15349671244621277 | 0.0 | 0.0 | +a4b7d4f5-3823-499c-841c-70c78f286d69 / -— |
| Jogador 2 | 6-3 | 339 | BUY | STABILIZE | 39.0 | 8 | 100 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.020221471786499 | 0.0 | 0.0 | +646dafa4-69ff-4189-8342-afea213a6790 / -— |
| Jogador 2 | 6-3 | 340 | REROLL | STABILIZE | 39.0 | 8 | 99 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 342 | SELL | STABILIZE | 23.0 | 8 | 108 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4736153781414032 | 0.0 | 0.0 | +— / -81d97dc0-cc50-4303-acfe-e8273ef39d35 |
| Jogador 2 | 6-4 | 343 | BUY | STABILIZE | 23.0 | 8 | 111 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3942781686782837 | 0.0 | 0.0 | +426b9603-a128-446f-96c4-004287d79723 / -— |
| Jogador 2 | 6-4 | 344 | REROLL | STABILIZE | 23.0 | 8 | 108 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 345 | SELL | STABILIZE | 23.0 | 8 | 106 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31582027673721313 | 0.0 | 0.0 | +— / -426b9603-a128-446f-96c4-004287d79723 |
| Jogador 2 | 6-4 | 346 | BUY | STABILIZE | 23.0 | 8 | 109 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48636388778686523 | 0.0 | 0.0 | +c6cfacad-08af-4690-9ef3-7751f1aa7a30 / -— |
| Jogador 2 | 6-4 | 347 | REROLL | STABILIZE | 23.0 | 8 | 107 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 348 | SELL | STABILIZE | 23.0 | 8 | 105 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02626153826713562 | 0.0 | 0.0 | +— / -a4b7d4f5-3823-499c-841c-70c78f286d69 |
| Jogador 2 | 6-4 | 349 | BUY | STABILIZE | 23.0 | 8 | 109 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0211620330810547 | 0.0 | 0.0 | +d2cb6143-37d1-4d0b-9cf3-eff835d5fb8e / -— |
| Jogador 2 | 6-4 | 350 | SELL | STABILIZE | 23.0 | 8 | 106 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04472307860851288 | 0.0 | 0.0 | +— / -75d9034d-80ed-40d3-a330-44554cc2bb9e |
| Jogador 2 | 6-5 | 352 | BUY | STABILIZE | 23.0 | 8 | 121 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04621175676584244 | 0.0 | 0.0 | +83fa2298-3d6d-4785-bd01-7b40f6a69f1e / -— |
| Jogador 2 | 6-5 | 353 | SELL | STABILIZE | 23.0 | 8 | 117 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04472307860851288 | 0.0 | 0.0 | +— / -83fa2298-3d6d-4785-bd01-7b40f6a69f1e |
| Jogador 2 | 6-5 | 354 | BUY | STABILIZE | 23.0 | 8 | 121 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21476520597934723 | 0.0 | 0.0 | +54779dda-333a-4f96-a05f-350c5c303a9c / -— |
| Jogador 2 | 6-5 | 355 | REROLL | STABILIZE | 23.0 | 8 | 118 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 356 | SELL | STABILIZE | 23.0 | 8 | 116 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06207692250609398 | 0.0 | 0.0 | +— / -54779dda-333a-4f96-a05f-350c5c303a9c |
| Jogador 2 | 6-5 | 357 | BUY | STABILIZE | 23.0 | 8 | 119 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15252189338207245 | 0.0 | 0.0 | +4d7ec7ee-5678-4796-a6e4-43af72c50bc3 / -— |
| Jogador 2 | 6-5 | 358 | SELL | STABILIZE | 23.0 | 8 | 115 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02626153826713562 | 0.0 | 0.0 | +— / -4d7ec7ee-5678-4796-a6e4-43af72c50bc3 |
| Jogador 2 | 6-5 | 359 | BUY | STABILIZE | 23.0 | 8 | 119 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15252180397510529 | 0.0 | 0.0 | +88df713d-22d5-4b6e-b02d-4371b930f4fb / -— |
| Jogador 2 | 6-5 | 360 | REROLL | STABILIZE | 23.0 | 8 | 115 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 362 | SELL | ALL_IN | 6.0 | 8 | 124 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02626153826713562 | 0.0 | 0.0 | +— / -88df713d-22d5-4b6e-b02d-4371b930f4fb |
| Jogador 2 | 6-6 | 363 | BUY | ALL_IN | 6.0 | 8 | 128 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6289219260215759 | 0.0 | 0.0 | +12e4262b-f19f-4b25-b401-acf685f81d79 / -— |
| Jogador 2 | 6-6 | 364 | REROLL | ALL_IN | 6.0 | 8 | 125 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 365 | SELL | ALL_IN | 6.0 | 8 | 123 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3466615378856659 | 0.0 | 0.0 | +— / -12e4262b-f19f-4b25-b401-acf685f81d79 |
| Jogador 2 | 6-6 | 366 | BUY | ALL_IN | 6.0 | 8 | 126 | 5 | 50.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.069970965385437 | 0.0 | 0.0 | +09c6b187-ccc0-4525-9a38-7bde65ca178a / -6d150146-2d96-4b53-a24b-05a486a348cf,d2cb6143-37d1-4d0b-9cf3-eff835d5fb8e |
| Jogador 2 | 6-6 | 367 | BUY | ALL_IN | 6.0 | 8 | 123 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3963184058666229 | 0.0 | 0.0 | +29eeef02-9b0a-480b-aca7-9e423ecddd3a / -— |
| Jogador 2 | 6-6 | 368 | REROLL | ALL_IN | 6.0 | 8 | 119 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 369 | SELL | ALL_IN | 6.0 | 8 | 117 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3672769367694855 | 0.0 | 0.0 | +— / -99182042-c4b9-4801-b66a-1f4432d301f3 |
| Jogador 2 | 6-6 | 370 | MOVE_BENCH | ALL_IN | 6.0 | 8 | 125 | 5 | 44.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5787694454193115 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.026938460767269135 | 0.0 | 0.0 | +— / -36f58657-5835-4389-95e9-a7d26464c2aa |
| Jogador 3 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3026348650455475 | 0.0 | 0.0 | +2cf5ccdc-76f4-4fc8-b12c-7b3b68b1b2c8 / -— |
| Jogador 3 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_RekSai | MOVE_BENCH, SELL, PASS | True | True | 0.5842720866203308 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_RekSai | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_RekSai | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.038241982460022 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_RekSai | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 13 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_RekSai | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3530687689781189 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_RekSai | BUY, MOVE_BOARD, PASS | True | True | 0.1410975158214569 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 15 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3189476728439331 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 17 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 18 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46496832370758057 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 20 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.07861048728227615 | 0.0 | 0.0 | +405de1b8-45c1-4b7f-b044-f12b819507c3 / -— |
| Jogador 3 | 1-3 | 21 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Murkwolf18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 30 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 40 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3510284423828125 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.269167959690094 | 0.0 | 0.0 | +c70251e8-af44-4466-808f-d49e9e5f57e9 / -— |
| Jogador 3 | 2-1 | 42 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17975932359695435 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 43 | PASS | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 48 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44265875220298767 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 50 | BUY | STABILIZE | 100.0 | 4 | 11 | 1 | 10.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9543229341506958 | 0.0 | 0.0 | +e5a28bd6-35ef-4cb0-801c-68c64d65b8eb / -— |
| Jogador 3 | 2-2 | 51 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 9 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18218499422073364 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 52 | SELL | STABILIZE | 100.0 | 4 | 9 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3222307562828064 | 0.0 | 0.0 | +— / -405de1b8-45c1-4b7f-b044-f12b819507c3 |
| Jogador 3 | 2-2 | 53 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 11 | 1 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 54 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 11 | 1 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3724561333656311 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 55 | PASS | STABILIZE | 100.0 | 4 | 11 | 1 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 60 | SELL | STABILIZE | 94.0 | 4 | 17 | 1 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42015981674194336 | 0.0 | 0.0 | +— / -c83ad0c5-f046-4834-8d0e-6dac3e49cdef |
| Jogador 3 | 2-3 | 61 | BUY | STABILIZE | 94.0 | 4 | 18 | 1 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0970923975110054 | 0.0 | 0.0 | +29f10cb7-6575-47ca-b583-057992a08253 / -— |
| Jogador 3 | 2-3 | 62 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 15 | 1 | 12.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3507094979286194 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 63 | SELL | STABILIZE | 94.0 | 4 | 15 | 1 | 14.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8171108961105347 | 0.0 | 0.0 | +— / -e5a28bd6-35ef-4cb0-801c-68c64d65b8eb |
| Jogador 3 | 2-3 | 64 | BUY | STABILIZE | 94.0 | 4 | 17 | 1 | 14.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2665526866912842 | 0.0 | 0.0 | +41db1132-4e1c-48eb-8a9b-1b2c74cb22ce / -— |
| Jogador 3 | 2-3 | 65 | BUY_XP | STABILIZE | 94.0 | 4 | 15 | 1 | 14.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 66 | BUY_XP | STABILIZE | 94.0 | 4 | 11 | 1 | 14.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05587000027298927 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 67 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 7 | 0 | 14.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2781093120574951 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 68 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 7 | 0 | 12.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4275848865509033 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 70 | BUY | STABILIZE | 94.0 | 5 | 13 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1086442470550537 | 0.0 | 0.0 | +3e2ae0fa-f6ff-467f-99d8-331b49a6db63 / -2cf5ccdc-76f4-4fc8-b12c-7b3b68b1b2c8,bdef75b2-081b-43df-9efb-fc0bc5ee2935 |
| Jogador 3 | 2-4 | 71 | SELL | STABILIZE | 94.0 | 5 | 12 | 1 | 14.0 | —/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45727846026420593 | 0.0 | 0.0 | +— / -3e2ae0fa-f6ff-467f-99d8-331b49a6db63 |
| Jogador 3 | 2-4 | 72 | BUY | STABILIZE | 94.0 | 5 | 15 | 1 | 14.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2396010160446167 | 0.0 | 0.0 | +4c8a9a18-68d8-4672-a96d-bb09816257dc / -— |
| Jogador 3 | 2-4 | 73 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 12 | 1 | 14.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0953959971666336 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 74 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 12 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3598865270614624 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 75 | BUY | STABILIZE | 94.0 | 5 | 12 | 1 | 20.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08761516958475113 | 0.0 | 0.0 | +2a2066ee-841b-49d5-8b82-1d47feb36d8c / -— |
| Jogador 3 | 2-4 | 76 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 9 | 0 | 20.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49326714873313904 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 77 | BUY_XP | ECON | 94.0 | 5 | 9 | 0 | 26.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.05299999937415123 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 79 | BUY | ECON | 94.0 | 5 | 10 | 1 | 26.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8289262652397156 | 0.0 | 0.0 | +226a1062-8e9a-4652-9da7-a2f215fa46ae / -— |
| Jogador 3 | 2-5 | 80 | MOVE_BENCH | ECON | 94.0 | 5 | 8 | 0 | 26.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04829506576061249 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 81 | BUY | SLOWROLL | 94.0 | 5 | 8 | 0 | 26.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30532023310661316 | 0.0 | 0.0 | +cdb48eea-209d-4833-9a68-79df61990332 / -— |
| Jogador 3 | 2-5 | 82 | BUY_XP | SLOWROLL | 94.0 | 5 | 5 | 0 | 26.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 83 | PASS | SLOWROLL | 94.0 | 5 | 1 | 0 | 26.0 | Colosso/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 88 | BUY | SLOWROLL | 94.0 | 5 | 8 | 0 | 26.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0458288192749023 | 0.0 | 0.0 | +07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 / -226a1062-8e9a-4652-9da7-a2f215fa46ae,c70251e8-af44-4466-808f-d49e9e5f57e9 |
| Jogador 3 | 2-6 | 89 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 6 | 0 | 18.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03594653308391571 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 90 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 6 | 0 | 18.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37583214044570923 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 91 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 6 | 0 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2166452705860138 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 92 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 6 | 0 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.035785794258117676 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 93 | PASS | SLOWROLL | 94.0 | 5 | 6 | 0 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 95 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 6 | 0 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4261396825313568 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 97 | SELL | SLOWROLL | 88.0 | 5 | 11 | 1 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39161717891693115 | 0.0 | 0.0 | +— / -4c8a9a18-68d8-4672-a96d-bb09816257dc |
| Jogador 3 | 2-7 | 98 | BUY | SLOWROLL | 88.0 | 5 | 14 | 1 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.337068110704422 | 0.0 | 0.0 | +bca8862c-5e5b-4a51-9173-79218fbfea3d / -— |
| Jogador 3 | 2-7 | 99 | MOVE_BOARD | SLOWROLL | 88.0 | 5 | 12 | 1 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15115630626678467 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 100 | SELL | SLOWROLL | 88.0 | 5 | 12 | 1 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8320227861404419 | 0.0 | 0.0 | +— / -bca8862c-5e5b-4a51-9173-79218fbfea3d |
| Jogador 3 | 2-7 | 101 | BUY | SLOWROLL | 88.0 | 5 | 14 | 1 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19298696517944336 | 0.0 | 0.0 | +79786887-d318-4836-b2f0-c0f03e86cbe5 / -— |
| Jogador 3 | 2-7 | 102 | BUY_XP | SLOWROLL | 88.0 | 5 | 11 | 1 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08641000092029572 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 103 | MOVE_BENCH | FAST8 | 88.0 | 6 | 7 | 0 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4423089027404785 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 104 | MOVE_BENCH | FAST8 | 88.0 | 6 | 7 | 0 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6618350148200989 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 106 | BUY | FAST8 | 88.0 | 6 | 12 | 1 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.12027908116579056 | 0.0 | 0.0 | +c3f8419e-a450-4247-bb65-8de8dba1c8ee / -— |
| Jogador 3 | 3-1 | 107 | BUY_XP | FAST8 | 88.0 | 6 | 9 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 108 | BUY_XP | FAST8 | 88.0 | 6 | 5 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 109 | PASS | FAST8 | 88.0 | 6 | 1 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 115 | BUY_XP | FAST8 | 88.0 | 6 | 7 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 116 | PASS | FAST8 | 88.0 | 6 | 3 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 124 | SELL | FAST8 | 88.0 | 6 | 10 | 1 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07846605032682419 | 0.0 | 0.0 | +— / -c3f8419e-a450-4247-bb65-8de8dba1c8ee |
| Jogador 3 | 3-3 | 125 | BUY | FAST8 | 88.0 | 6 | 13 | 1 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7339646220207214 | 0.0 | 0.0 | +e8b0d22c-35bc-459e-a90c-7db13fcbe34f / -— |
| Jogador 3 | 3-3 | 126 | SELL | FAST8 | 88.0 | 6 | 10 | 1 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.2061229944229126 | 0.0 | 0.0 | +— / -e8b0d22c-35bc-459e-a90c-7db13fcbe34f |
| Jogador 3 | 3-3 | 127 | BUY | FAST8 | 88.0 | 6 | 13 | 1 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.21593445539474487 | 0.0 | 0.0 | +f0b6c16b-7610-454c-929d-7152f0a041d3 / -— |
| Jogador 3 | 3-3 | 128 | MOVE_BENCH | FAST8 | 88.0 | 6 | 11 | 1 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08366921544075012 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 129 | BUY_XP | FAST8 | 88.0 | 6 | 11 | 1 | 34.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 130 | BUY_XP | FAST8 | 88.0 | 6 | 7 | 0 | 34.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 131 | PASS | FAST8 | 88.0 | 6 | 3 | 0 | 34.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 133 | SELL | FAST8 | 88.0 | 6 | 10 | 1 | 34.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4128968417644501 | 0.0 | 0.0 | +— / -79786887-d318-4836-b2f0-c0f03e86cbe5 |
| Jogador 3 | 3-4 | 134 | BUY | FAST8 | 88.0 | 6 | 13 | 1 | 34.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.20576916635036469 | 0.0 | 0.0 | +d63ebe7f-9313-42c4-afa2-a6078130f235 / -— |
| Jogador 3 | 3-4 | 135 | BUY_XP | FAST8 | 88.0 | 6 | 10 | 1 | 34.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 136 | BUY_XP | FAST8 | 88.0 | 6 | 6 | 0 | 34.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07959999889135361 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 137 | MOVE_BENCH | FAST8 | 88.0 | 7 | 2 | 0 | 34.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42974305152893066 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 138 | MOVE_BENCH | FAST8 | 88.0 | 7 | 2 | 0 | 36.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13594678044319153 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 139 | MOVE_BENCH | FAST8 | 88.0 | 7 | 2 | 0 | 34.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026375340297818184 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 140 | MOVE_BENCH | FAST8 | 88.0 | 7 | 2 | 0 | 34.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43215158581733704 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 142 | BUY | FAST8 | 88.0 | 7 | 8 | 0 | 40.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7268218994140625 | 0.0 | 0.0 | +7c8b3027-1434-4346-95b3-5463e8a4aa9b / -— |
| Jogador 3 | 3-5 | 143 | MOVE_BOARD | FAST8 | 88.0 | 7 | 5 | 0 | 40.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012479945085942745 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 144 | BUY_XP | FAST8 | 88.0 | 7 | 5 | 0 | 40.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 145 | PASS | FAST8 | 88.0 | 7 | 1 | 0 | 40.0 | Colosso/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 152 | MOVE_BENCH | FAST8 | 88.0 | 7 | 8 | 0 | 40.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.70059734582901 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 153 | MOVE_BENCH | FAST8 | 88.0 | 7 | 8 | 0 | 42.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2429518699645996 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 154 | PASS | FAST8 | 88.0 | 7 | 8 | 0 | 40.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 162 | BUY | FAST8 | 88.0 | 7 | 16 | 1 | 40.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.763798177242279 | 0.0 | 0.0 | +a4188ec8-4188-4fdf-8d76-c559fc0c7daf / -7c8b3027-1434-4346-95b3-5463e8a4aa9b,d63ebe7f-9313-42c4-afa2-a6078130f235 |
| Jogador 3 | 3-7 | 163 | MOVE_BENCH | FAST8 | 88.0 | 7 | 13 | 1 | 28.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2950010597705841 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 164 | MOVE_BENCH | FAST8 | 88.0 | 7 | 13 | 1 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46831652522087097 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 165 | MOVE_BENCH | FAST8 | 88.0 | 7 | 13 | 1 | 40.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48986440896987915 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 166 | BUY_XP | FAST8 | 88.0 | 7 | 13 | 1 | 34.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 167 | BUY_XP | FAST8 | 88.0 | 7 | 9 | 0 | 34.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 168 | BUY_XP | FAST8 | 88.0 | 7 | 5 | 0 | 34.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 169 | PASS | FAST8 | 88.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 170 | MOVE_BENCH | FAST8 | 88.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6492412686347961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 172 | BUY | FAST8 | 88.0 | 7 | 8 | 0 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2137986719608307 | 0.0 | 0.0 | +4363594b-375b-45d4-9b1a-0c1ab96367a1 / -— |
| Jogador 3 | 4-1 | 173 | MOVE_BOARD | FAST8 | 88.0 | 7 | 5 | 0 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012479945085942745 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 174 | BUY_XP | FAST8 | 88.0 | 7 | 5 | 0 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 175 | PASS | FAST8 | 88.0 | 7 | 1 | 0 | 46.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 182 | BUY | FAST8 | 88.0 | 7 | 10 | 1 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6132427453994751 | 0.0 | 0.0 | +3bbd7105-b508-437d-ac84-11e01a499779 / -— |
| Jogador 3 | 4-2 | 183 | BUY_XP | FAST8 | 88.0 | 7 | 7 | 0 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 184 | PASS | FAST8 | 88.0 | 7 | 3 | 0 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 192 | BUY | FAST8 | 75.0 | 7 | 8 | 0 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10151223838329315 | 0.0 | 0.0 | +3a1de7b3-af72-4024-8105-588fa4ec946b / -— |
| Jogador 3 | 4-3 | 193 | BUY_XP | FAST8 | 75.0 | 7 | 5 | 0 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 194 | PASS | FAST8 | 75.0 | 7 | 1 | 0 | 46.0 | Colosso/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 202 | BUY_XP | FAST8 | 75.0 | 7 | 7 | 0 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 203 | PASS | FAST8 | 75.0 | 7 | 3 | 0 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 212 | BUY | FAST8 | 75.0 | 7 | 8 | 0 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7337983250617981 | 0.0 | 0.0 | +24b29fe6-466c-42d5-9f92-5d6114f0f98f / -— |
| Jogador 3 | 4-5 | 213 | PASS | FAST8 | 75.0 | 7 | 5 | 0 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 222 | BUY | FAST8 | 63.0 | 7 | 10 | 1 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06186414882540703 | 0.0 | 0.0 | +6594349f-ecaa-4212-b063-815acae6d0bb / -— |
| Jogador 3 | 4-6 | 223 | PASS | FAST8 | 63.0 | 7 | 7 | 0 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 232 | BUY | FAST8 | 50.0 | 7 | 13 | 1 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.793155312538147 | 0.0 | 0.0 | +7f9f3188-2482-4518-9fd2-34f0ea1527a9 / -24b29fe6-466c-42d5-9f92-5d6114f0f98f,4363594b-375b-45d4-9b1a-0c1ab96367a1 |
| Jogador 3 | 4-7 | 233 | BUY | FAST8 | 50.0 | 7 | 10 | 1 | 46.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6796237826347351 | 0.0 | 0.0 | +57ba484a-6228-4263-8171-00a8a5893bea / -2a2066ee-841b-49d5-8b82-1d47feb36d8c,3bbd7105-b508-437d-ac84-11e01a499779 |
| Jogador 3 | 4-7 | 234 | MOVE_BENCH | FAST8 | 50.0 | 7 | 7 | 0 | 40.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17347541451454163 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 235 | MOVE_BENCH | FAST8 | 50.0 | 7 | 7 | 0 | 40.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4890526533126831 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 236 | PASS | FAST8 | 50.0 | 7 | 7 | 0 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 240 | MOVE_BENCH | FAST8 | 50.0 | 7 | 7 | 0 | 42.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5649351477622986 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 242 | EQUIP_FROM_INVENTORY | ECON | 50.0 | 8 | 13 | 1 | 54.0 | Colosso/DA_Vi18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 243 | BUY | ECON | 50.0 | 8 | 13 | 1 | 54.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.08831184357404709 | 0.0 | 0.0 | +c5520bc4-3123-40f3-b275-83fa8cb06309 / -— |
| Jogador 3 | 5-1 | 244 | MOVE_BENCH | ECON | 50.0 | 8 | 10 | 1 | 54.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.003568874439224601 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 245 | MOVE_BENCH | ECON | 50.0 | 8 | 10 | 1 | 52.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.17359234392642975 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 246 | BUY | ECON | 50.0 | 8 | 10 | 1 | 52.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.23285451531410217 | 0.0 | 0.0 | +1f349179-be2a-4738-bda1-072f7fae2147 / -— |
| Jogador 3 | 5-1 | 247 | PASS | ECON | 50.0 | 8 | 8 | 0 | 52.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 250 | MOVE_BENCH | ECON | 50.0 | 8 | 8 | 0 | 52.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5103693008422852 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 252 | BUY | ECON | 50.0 | 8 | 14 | 1 | 58.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7659299969673157 | 0.0 | 0.0 | +e1be174a-f112-4e1b-8bf6-738af52f27e8 / -— |
| Jogador 3 | 5-2 | 253 | BUY | ECON | 50.0 | 8 | 11 | 1 | 58.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.25474610924720764 | 0.0 | 0.0 | +5184a53b-fca3-448c-b5ab-7daa37b0c259 / -— |
| Jogador 3 | 5-2 | 254 | BUY | ECON | 50.0 | 8 | 10 | 1 | 58.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3472212255001068 | 0.0 | 0.0 | +c71adf7d-8d74-439d-8863-dac0f4f20cd1 / -— |
| Jogador 3 | 5-2 | 255 | PASS | ECON | 50.0 | 8 | 6 | 0 | 58.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 262 | BUY | STABILIZE | 34.0 | 8 | 11 | 1 | 58.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.20323307812213898 | 0.0 | 0.0 | +3e1e33ef-4948-4ff2-bfb9-db16af507dd9 / -— |
| Jogador 3 | 5-3 | 263 | BUY | STABILIZE | 34.0 | 8 | 8 | 0 | 58.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.011442120186984539 | 0.0 | 0.0 | +6fe382fd-86c3-42ec-abb7-fb52c7a19c62 / -— |
| Jogador 3 | 5-3 | 264 | PASS | STABILIZE | 34.0 | 8 | 4 | 0 | 58.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 272 | SELL | STABILIZE | 18.0 | 8 | 10 | 1 | 58.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0524153858423233 | 0.0 | 0.0 | +— / -1f349179-be2a-4738-bda1-072f7fae2147 |
| Jogador 3 | 5-4 | 273 | BUY | STABILIZE | 18.0 | 8 | 12 | 1 | 58.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8059645295143127 | 0.0 | 0.0 | +c0e9ed28-9917-46be-b0c6-a8509aa1f600 / -— |
| Jogador 3 | 5-4 | 274 | MOVE_BOARD | STABILIZE | 18.0 | 8 | 10 | 1 | 58.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.12034890055656433 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 275 | MOVE_BOARD | STABILIZE | 18.0 | 8 | 10 | 1 | 58.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.25287696719169617 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 276 | PASS | STABILIZE | 18.0 | 8 | 10 | 1 | 58.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 282 | SELL | STABILIZE | 18.0 | 8 | 17 | 1 | 58.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.16226154565811157 | 0.0 | 0.0 | +— / -c71adf7d-8d74-439d-8863-dac0f4f20cd1 |
| Jogador 3 | 5-5 | 283 | BUY | STABILIZE | 18.0 | 8 | 21 | 2 | 58.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6387182474136353 | 0.0 | 0.0 | +36a593e6-6199-441a-907d-77b9ea835889 / -— |
| Jogador 3 | 5-5 | 284 | SELL | STABILIZE | 18.0 | 8 | 18 | 1 | 58.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2899044454097748 | 0.0 | 0.0 | +— / -36a593e6-6199-441a-907d-77b9ea835889 |
| Jogador 3 | 5-5 | 285 | BUY | STABILIZE | 18.0 | 8 | 21 | 2 | 58.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2044588178396225 | 0.0 | 0.0 | +7be7d9db-fa8f-421e-93d5-5910cc3e1bf2 / -— |
| Jogador 3 | 5-5 | 286 | MOVE_BOARD | STABILIZE | 18.0 | 8 | 16 | 1 | 58.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 287 | SELL | STABILIZE | 18.0 | 8 | 16 | 1 | 58.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.13695703446865082 | 0.0 | 0.0 | +— / -6fe382fd-86c3-42ec-abb7-fb52c7a19c62 |
| Jogador 3 | 5-5 | 288 | BUY | STABILIZE | 18.0 | 8 | 20 | 2 | 58.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.21320146322250366 | 0.0 | 0.0 | +99c9fbf5-b28f-4743-b04a-5299e9e116e5 / -— |
| Jogador 3 | 5-5 | 289 | REROLL | STABILIZE | 18.0 | 8 | 16 | 1 | 58.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 290 | SELL | STABILIZE | 18.0 | 8 | 14 | 1 | 58.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.052723076194524765 | 0.0 | 0.0 | +— / -99c9fbf5-b28f-4743-b04a-5299e9e116e5 |
| Jogador 3 | 5-6 | 292 | BUY | ALL_IN | 2.0 | 8 | 25 | 2 | 58.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.1333414912223816 | 0.0 | 0.0 | +b9b2c784-d8ee-4a31-978f-58a686f22af2 / -— |
| Jogador 3 | 5-6 | 293 | SELL | ALL_IN | 2.0 | 8 | 21 | 2 | 58.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.052723076194524765 | 0.0 | 0.0 | +— / -b9b2c784-d8ee-4a31-978f-58a686f22af2 |
| Jogador 3 | 5-6 | 294 | BUY | ALL_IN | 2.0 | 8 | 25 | 2 | 58.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.164821594953537 | 0.0 | 0.0 | +703b70a3-3aca-4ecd-86da-0a1b34e4bb3a / -— |
| Jogador 3 | 5-6 | 295 | REROLL | ALL_IN | 2.0 | 8 | 22 | 2 | 58.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 296 | SELL | ALL_IN | 2.0 | 8 | 20 | 2 | 58.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.025984615087509155 | 0.0 | 0.0 | +— / -703b70a3-3aca-4ecd-86da-0a1b34e4bb3a |
| Jogador 3 | 5-6 | 297 | BUY | ALL_IN | 2.0 | 8 | 23 | 2 | 58.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.017608774825930595 | 0.0 | 0.0 | +9b711f23-11ec-4049-b5e4-b0623b01204e / -— |
| Jogador 3 | 5-6 | 298 | SELL | ALL_IN | 2.0 | 8 | 19 | 1 | 58.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.14659999310970306 | 0.0 | 0.0 | +— / -6594349f-ecaa-4212-b063-815acae6d0bb |
| Jogador 3 | 5-6 | 299 | BUY | ALL_IN | 2.0 | 8 | 22 | 2 | 58.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.010025463066995144 | 0.0 | 0.0 | +a882c3ee-af7e-400d-911c-a25555e368a5 / -— |
| Jogador 3 | 5-6 | 300 | SELL | ALL_IN | 2.0 | 8 | 18 | 1 | 58.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.11915258318185806 | 0.0 | 0.0 | +— / -a882c3ee-af7e-400d-911c-a25555e368a5 |
| Jogador 4 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.026938460767269135 | 0.0 | 0.0 | +— / -9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +1903eae4-bd37-4ed8-bbae-28177e859592 / -— |
| Jogador 4 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.5990749597549438 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1957342028617859 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30133089423179626 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 13 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | -0.14705206453800201 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 14 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.1591830998659134 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 15 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 18 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36510446667671204 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 20 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2520820200443268 | 0.0 | 0.0 | +a19fc47b-fc81-49b2-bc25-d25d58b8deef / -— |
| Jogador 4 | 1-3 | 21 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 30 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4189223647117615 | 0.0 | 0.0 | +— / -a19fc47b-fc81-49b2-bc25-d25d58b8deef |
| Jogador 4 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.039581298828125 | 0.0 | 0.0 | +cd27dcd8-0a45-4196-be66-fbe6eb4a0793 / -— |
| Jogador 4 | 1-4 | 32 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.1852325201034546 | 0.0 | 0.0 | +— / -cd27dcd8-0a45-4196-be66-fbe6eb4a0793 |
| Jogador 4 | 1-4 | 33 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.039577841758728 | 0.0 | 0.0 | +eddd35aa-7d38-4d71-8984-e4768f06379e / -— |
| Jogador 4 | 1-4 | 34 | BUY_XP | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 35 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 38 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5330885052680969 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 40 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0331655740737915 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 4 | 2-1 | 41 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 50 | SELL | STABILIZE | 100.0 | 4 | 9 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.739515483379364 | 0.0 | 0.0 | +— / -0e9aa759-0538-4168-a523-02a5f8e09e0a |
| Jogador 4 | 2-2 | 51 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03695835918188095 | 0.0 | 0.0 | +4e00fb2f-75c1-4580-bd09-cb73c31af01f / -— |
| Jogador 4 | 2-2 | 52 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030969999730587006 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 53 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 3 | 0 | 8.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19964255392551422 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 54 | PASS | SLOWROLL | 100.0 | 5 | 3 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 58 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 3 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4171077609062195 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 60 | BUY | SLOWROLL | 100.0 | 5 | 10 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9679791331291199 | 0.0 | 0.0 | +ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 / -1903eae4-bd37-4ed8-bbae-28177e859592,eddd35aa-7d38-4d71-8984-e4768f06379e |
| Jogador 4 | 2-3 | 61 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 9 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22780993580818176 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 62 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 9 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33767127990722656 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 63 | BUY | SLOWROLL | 100.0 | 5 | 9 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3008972406387329 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 4 | 2-3 | 64 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5309566259384155 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 65 | MOVE_BOARD | SLOWROLL | 100.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29404476284980774 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 66 | PASS | SLOWROLL | 100.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 68 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7334550619125366 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 70 | BUY | SLOWROLL | 94.0 | 5 | 11 | 1 | 20.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03773941472172737 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 4 | 2-4 | 71 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8020634651184082 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 72 | MOVE_BENCH | SLOWROLL | 94.0 | 5 | 7 | 0 | 22.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36807307600975037 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 73 | SELL | SLOWROLL | 94.0 | 5 | 7 | 0 | 26.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.048981450498104095 | 0.0 | 0.0 | +— / -95829f2e-ad17-448d-a385-fdcf81872dc8 |
| Jogador 4 | 2-4 | 74 | BUY | SLOWROLL | 94.0 | 5 | 8 | 0 | 26.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.27422842383384705 | 0.0 | 0.0 | +a229cc5e-9f28-4ff3-b652-eab994251c92 / -— |
| Jogador 4 | 2-4 | 75 | BUY_XP | SLOWROLL | 94.0 | 5 | 6 | 0 | 26.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 76 | MOVE_BOARD | SLOWROLL | 94.0 | 5 | 2 | 0 | 26.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039354316890239716 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 77 | MOVE_BOARD | SLOWROLL | 94.0 | 5 | 2 | 0 | 26.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10718601942062378 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 79 | SELL | SLOWROLL | 94.0 | 5 | 7 | 0 | 26.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3702792227268219 | 0.0 | 0.0 | +— / -a229cc5e-9f28-4ff3-b652-eab994251c92 |
| Jogador 4 | 2-5 | 80 | BUY | SLOWROLL | 94.0 | 5 | 9 | 0 | 26.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.32091671228408813 | 0.0 | 0.0 | +a92eca5d-299f-4f4d-a16b-d23981ef719f / -— |
| Jogador 4 | 2-5 | 81 | MOVE_BOARD | SLOWROLL | 94.0 | 5 | 6 | 0 | 26.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1969456672668457 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 82 | MOVE_BOARD | SLOWROLL | 94.0 | 5 | 6 | 0 | 26.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 83 | PASS | SLOWROLL | 94.0 | 5 | 6 | 0 | 26.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 88 | MOVE_BOARD | SLOWROLL | 88.0 | 5 | 12 | 1 | 26.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17715884745121002 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 89 | MOVE_BOARD | SLOWROLL | 88.0 | 5 | 12 | 1 | 26.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007495662663131952 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 90 | MOVE_BOARD | SLOWROLL | 88.0 | 5 | 12 | 1 | 26.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31497427821159363 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 91 | MOVE_BOARD | SLOWROLL | 88.0 | 5 | 12 | 1 | 26.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1607125997543335 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 92 | BUY_XP | SLOWROLL | 88.0 | 5 | 12 | 1 | 26.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1379999965429306 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 93 | BUY_XP | SLOWROLL | 88.0 | 5 | 8 | 0 | 26.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01384000014513731 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 94 | MOVE_BENCH | FAST8 | 88.0 | 6 | 4 | 0 | 26.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6229805946350098 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 95 | PASS | FAST8 | 88.0 | 6 | 4 | 0 | 32.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 97 | BUY | FAST8 | 88.0 | 6 | 10 | 1 | 32.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.24475181102752686 | 0.0 | 0.0 | +5e247068-fe03-467e-9e7d-ab85ade7fdae / -— |
| Jogador 4 | 2-7 | 98 | MOVE_BENCH | FAST8 | 88.0 | 6 | 7 | 0 | 32.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3211950659751892 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 99 | BUY_XP | FAST8 | 88.0 | 6 | 7 | 0 | 32.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 100 | PASS | FAST8 | 88.0 | 6 | 3 | 0 | 32.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 106 | SELL | FAST8 | 88.0 | 6 | 8 | 0 | 32.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38337063789367676 | 0.0 | 0.0 | +— / -a92eca5d-299f-4f4d-a16b-d23981ef719f |
| Jogador 4 | 3-1 | 107 | BUY | FAST8 | 88.0 | 6 | 11 | 1 | 32.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.13477715849876404 | 0.0 | 0.0 | +74fe48c1-d955-4b0d-b832-39d4c86049dc / -— |
| Jogador 4 | 3-1 | 108 | BUY_XP | FAST8 | 88.0 | 6 | 9 | 0 | 32.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 109 | BUY_XP | FAST8 | 88.0 | 6 | 5 | 0 | 32.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 110 | PASS | FAST8 | 88.0 | 6 | 1 | 0 | 32.0 | Adaptador/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 115 | BUY_XP | FAST8 | 77.0 | 6 | 6 | 0 | 32.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 116 | PASS | FAST8 | 77.0 | 6 | 2 | 0 | 32.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 124 | SELL | FAST8 | 67.0 | 6 | 8 | 0 | 32.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4029465615749359 | 0.0 | 0.0 | +— / -74fe48c1-d955-4b0d-b832-39d4c86049dc |
| Jogador 4 | 3-3 | 125 | BUY | FAST8 | 67.0 | 6 | 10 | 1 | 32.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.13799871504306793 | 0.0 | 0.0 | +ac8f2a7d-1627-4aa4-a35b-805bce651b0e / -— |
| Jogador 4 | 3-3 | 126 | BUY_XP | FAST8 | 67.0 | 6 | 9 | 0 | 32.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 127 | BUY_XP | FAST8 | 67.0 | 6 | 5 | 0 | 32.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 128 | PASS | FAST8 | 67.0 | 6 | 1 | 0 | 32.0 | Adaptador/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 133 | SELL | FAST8 | 57.0 | 6 | 7 | 0 | 32.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8629999756813049 | 0.0 | 0.0 | +— / -ac8f2a7d-1627-4aa4-a35b-805bce651b0e |
| Jogador 4 | 3-4 | 134 | BUY | FAST8 | 57.0 | 6 | 8 | 0 | 32.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7337878346443176 | 0.0 | 0.0 | +2acd0734-f0c3-42b1-9791-5c48e1aa46bc / -— |
| Jogador 4 | 3-4 | 135 | BUY_XP | FAST8 | 57.0 | 6 | 5 | 0 | 32.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07959999889135361 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 136 | MOVE_BENCH | FAST8 | 57.0 | 7 | 1 | 0 | 32.0 | Adaptador/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 137 | MOVE_BENCH | FAST8 | 57.0 | 7 | 1 | 0 | 32.0 | Adaptador/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.677717387676239 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 138 | PASS | FAST8 | 57.0 | 7 | 1 | 0 | 38.0 | Adaptador/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 142 | BUY | FAST8 | 57.0 | 7 | 7 | 0 | 38.0 | Adaptador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7629095911979675 | 0.0 | 0.0 | +bd4236f8-c8ff-4536-934a-b12b71012724 / -2acd0734-f0c3-42b1-9791-5c48e1aa46bc,5e247068-fe03-467e-9e7d-ab85ade7fdae |
| Jogador 4 | 3-5 | 143 | MOVE_BENCH | FAST8 | 57.0 | 7 | 4 | 0 | 26.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5429810285568237 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 144 | BUY | FAST8 | 57.0 | 7 | 4 | 0 | 38.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.07792498171329498 | 0.0 | 0.0 | +fa5dc86b-f736-4083-b9df-5cc174b726f2 / -— |
| Jogador 4 | 3-5 | 145 | MOVE_BENCH | FAST8 | 57.0 | 7 | 1 | 0 | 38.0 | Adaptador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4451431334018707 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 146 | PASS | FAST8 | 57.0 | 7 | 1 | 0 | 44.0 | Adaptador/DA_18_MasterYi_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 152 | BUY | FAST8 | 57.0 | 7 | 7 | 0 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.21108916401863098 | 0.0 | 0.0 | +5f79a010-9e28-4a94-be40-973a17313186 / -— |
| Jogador 4 | 3-6 | 153 | BUY_XP | FAST8 | 57.0 | 7 | 4 | 0 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 154 | PASS | FAST8 | 57.0 | 7 | 0 | 0 | 44.0 | Adaptador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 162 | MOVE_BENCH | FAST8 | 57.0 | 7 | 7 | 0 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14576254785060883 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 163 | PASS | FAST8 | 57.0 | 7 | 7 | 0 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 172 | CRAFT_AND_EQUIP | FAST8 | 57.0 | 7 | 13 | 1 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08648793399333954 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 173 | PASS | FAST8 | 57.0 | 7 | 13 | 1 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 182 | BUY_XP | FAST8 | 57.0 | 7 | 21 | 2 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08192499727010727 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 183 | BUY_XP | FAST8 | 57.0 | 7 | 17 | 1 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0019249999895691872 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 184 | BUY_XP | FAST8 | 57.0 | 7 | 13 | 1 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 185 | BUY_XP | FAST8 | 57.0 | 7 | 9 | 0 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 186 | BUY_XP | FAST8 | 57.0 | 7 | 5 | 0 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 187 | PASS | FAST8 | 57.0 | 7 | 1 | 0 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 192 | PASS | FAST8 | 57.0 | 7 | 8 | 0 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 202 | PASS | FAST8 | 57.0 | 7 | 16 | 1 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10571428388357162 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 212 | PASS | FAST8 | 57.0 | 7 | 24 | 2 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11142857372760773 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 222 | PASS | FAST8 | 57.0 | 7 | 35 | 3 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17928571999073029 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 232 | BUY | FAST8 | 57.0 | 7 | 47 | 4 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8344574570655823 | 0.0 | 0.0 | +2cdf9a6a-5786-4a2b-8c4e-6fb9b151a92d / -— |
| Jogador 4 | 4-7 | 233 | BUY_XP | FAST8 | 57.0 | 7 | 44 | 4 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0019249999895691872 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 234 | BUY_XP | FAST8 | 57.0 | 7 | 40 | 4 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08192499727010727 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 235 | BUY_XP | FAST8 | 57.0 | 7 | 36 | 3 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11278750002384186 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 236 | PASS | WINSTREAK | 57.0 | 8 | 32 | 3 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15214285254478455 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 240 | MOVE_BENCH | WINSTREAK | 57.0 | 8 | 32 | 3 | 44.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44364041090011597 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 242 | EQUIP_FROM_INVENTORY | WINSTREAK | 57.0 | 8 | 43 | 4 | 50.0 | Adaptador/DA_18_MasterYi_AD | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 243 | BUY | WINSTREAK | 57.0 | 8 | 43 | 4 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4674990177154541 | 0.0 | 0.0 | +7d8564c6-8151-4e04-b028-2121cb064215 / -— |
| Jogador 4 | 5-1 | 244 | MOVE_BENCH | WINSTREAK | 57.0 | 8 | 40 | 4 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 245 | BUY | WINSTREAK | 57.0 | 8 | 40 | 4 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1278047412633896 | 0.0 | 0.0 | +1ad1f705-7e6b-4c1f-811c-2863dbf2db9e / -— |
| Jogador 4 | 5-1 | 246 | PASS | WINSTREAK | 57.0 | 8 | 37 | 3 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1987857073545456 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 252 | BUY | ECON | 41.0 | 8 | 45 | 4 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3424638509750366 | 0.0 | 0.0 | +497fbcb9-9d15-43f0-ad71-96eeceeee99d / -— |
| Jogador 4 | 5-2 | 253 | BUY | ECON | 41.0 | 8 | 41 | 4 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04090571030974388 | 0.0 | 0.0 | +a5247b50-831c-4600-bac0-e9bcdfa3ce1c / -— |
| Jogador 4 | 5-2 | 254 | PASS | ECON | 41.0 | 8 | 37 | 3 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20582571625709534 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 262 | BUY | ECON | 41.0 | 8 | 46 | 4 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14472879469394684 | 0.0 | 0.0 | +bdee88f4-e5b5-48fb-9ae5-1fd155982995 / -— |
| Jogador 4 | 5-3 | 263 | BUY | ECON | 41.0 | 8 | 42 | 4 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3526422381401062 | 0.0 | 0.0 | +db79d601-4b72-43c1-a8e3-4755c3442aa0 / -— |
| Jogador 4 | 5-3 | 264 | PASS | ECON | 41.0 | 8 | 38 | 3 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20687216520309448 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 272 | BUY | ECON | 41.0 | 8 | 48 | 4 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12645253539085388 | 0.0 | 0.0 | +405ddfe0-1547-4346-84c1-0affe79da8e5 / -— |
| Jogador 4 | 5-4 | 273 | BUY | ECON | 41.0 | 8 | 44 | 4 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6745257377624512 | 0.0 | 0.0 | +88249896-79bb-4f76-94a3-131d12f9fc3d / -— |
| Jogador 4 | 5-4 | 274 | REROLL | ECON | 41.0 | 8 | 41 | 4 | 50.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 275 | SELL | ECON | 41.0 | 8 | 39 | 3 | 50.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16226154565811157 | 0.0 | 0.0 | +— / -db79d601-4b72-43c1-a8e3-4755c3442aa0 |
| Jogador 4 | 5-4 | 276 | BUY | ECON | 41.0 | 8 | 43 | 4 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7132121324539185 | 0.0 | 0.0 | +09105a4a-c4d1-43c0-b1fb-08df25bcafd5 / -— |
| Jogador 4 | 5-4 | 277 | MOVE_BENCH | ECON | 41.0 | 8 | 39 | 3 | 50.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0756096839904785 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 278 | MOVE_BENCH | ECON | 41.0 | 8 | 39 | 3 | 46.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35266348719596863 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 279 | SELL | ECON | 41.0 | 8 | 39 | 3 | 50.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2889566719532013 | 0.0 | 0.0 | +— / -1ad1f705-7e6b-4c1f-811c-2863dbf2db9e |
| Jogador 4 | 5-4 | 280 | BUY | ECON | 41.0 | 8 | 42 | 4 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8168578147888184 | 0.0 | 0.0 | +2a8d50dc-11ec-4404-823c-6d8fa77c6c2b / -09105a4a-c4d1-43c0-b1fb-08df25bcafd5,0b62545c-1de0-47d8-bb4c-119f7e1526b3 |
| Jogador 4 | 5-5 | 282 | BUY | ECON | 41.0 | 8 | 47 | 4 | 42.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8689953088760376 | 0.0 | 0.0 | +e41f7d8d-7662-4445-a1b5-47ad14c9ecb9 / -— |
| Jogador 4 | 5-5 | 283 | MOVE_BENCH | ECON | 41.0 | 8 | 44 | 4 | 42.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7299318313598633 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 284 | BUY | ECON | 41.0 | 8 | 44 | 4 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8086888790130615 | 0.0 | 0.0 | +297d9911-9b62-421e-bb32-76d72c202f1a / -— |
| Jogador 4 | 5-5 | 285 | REROLL | ECON | 41.0 | 8 | 41 | 4 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24400000274181366 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 286 | MOVE_BENCH | ECON | 41.0 | 8 | 39 | 3 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.840687096118927 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 287 | MOVE_BENCH | ECON | 41.0 | 8 | 39 | 3 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5681386590003967 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 288 | PASS | ECON | 41.0 | 8 | 39 | 3 | 42.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05391862615942955 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 292 | MOVE_BENCH | ECON | 41.0 | 8 | 50 | 5 | 42.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27512112259864807 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 293 | SELL | ECON | 41.0 | 8 | 50 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00890769250690937 | 0.0 | 0.0 | +— / -88249896-79bb-4f76-94a3-131d12f9fc3d |
| Jogador 4 | 5-6 | 294 | BUY | ECON | 41.0 | 8 | 53 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7661891579627991 | 0.0 | 0.0 | +0af3def4-348c-47c9-aab3-11618b91e680 / -— |
| Jogador 4 | 5-6 | 295 | MOVE_BENCH | ECON | 41.0 | 8 | 49 | 4 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30390265583992004 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 296 | REROLL | ECON | 41.0 | 8 | 49 | 4 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 297 | SELL | ECON | 41.0 | 8 | 47 | 4 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31789231300354004 | 0.0 | 0.0 | +— / -497fbcb9-9d15-43f0-ad71-96eeceeee99d |
| Jogador 4 | 5-6 | 298 | BUY | ECON | 41.0 | 8 | 51 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2998286485671997 | 0.0 | 0.0 | +eb0046fd-392b-47c4-add2-fc669b031a3c / -— |
| Jogador 4 | 5-6 | 299 | REROLL | ECON | 41.0 | 8 | 47 | 4 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 300 | SELL | ECON | 41.0 | 8 | 45 | 4 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02112307772040367 | 0.0 | 0.0 | +— / -0af3def4-348c-47c9-aab3-11618b91e680 |
| Jogador 4 | 5-7 | 302 | BUY | ECON | 41.0 | 8 | 61 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25454580783843994 | 0.0 | 0.0 | +ee733f3d-35a8-4ea0-86ca-92d3bdae3cc9 / -— |
| Jogador 4 | 5-7 | 303 | REROLL | ECON | 41.0 | 8 | 57 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 304 | SELL | ECON | 41.0 | 8 | 55 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07426153868436813 | 0.0 | 0.0 | +— / -ee733f3d-35a8-4ea0-86ca-92d3bdae3cc9 |
| Jogador 4 | 5-7 | 305 | BUY | ECON | 41.0 | 8 | 59 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32896262407302856 | 0.0 | 0.0 | +15c32810-3029-4027-abcf-14005de787bf / -— |
| Jogador 4 | 5-7 | 306 | MOVE_BENCH | ECON | 41.0 | 8 | 55 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38856059312820435 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 307 | MOVE_BENCH | ECON | 41.0 | 8 | 55 | 5 | 42.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07660973817110062 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 308 | MOVE_BENCH | ECON | 41.0 | 8 | 55 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8948004245758057 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 309 | MOVE_BENCH | ECON | 41.0 | 8 | 55 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3647237718105316 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 310 | PASS | ECON | 41.0 | 8 | 55 | 5 | 42.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09887940436601639 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 312 | EQUIP_FROM_INVENTORY | ECON | 41.0 | 8 | 66 | 5 | 42.0 | Adaptador/DA_18_Aphelios | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 313 | EQUIP_FROM_INVENTORY | ECON | 41.0 | 8 | 66 | 5 | 42.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.006902201101183891 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 314 | MOVE_BENCH | ECON | 41.0 | 8 | 66 | 5 | 42.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27512112259864807 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 315 | SELL | ECON | 41.0 | 8 | 66 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029123077169060707 | 0.0 | 0.0 | +— / -15c32810-3029-4027-abcf-14005de787bf |
| Jogador 4 | 6-1 | 316 | BUY | ECON | 41.0 | 8 | 70 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14125072956085205 | 0.0 | 0.0 | +22f1ab5f-b752-49e7-b6f0-ed9b5e641d64 / -— |
| Jogador 4 | 6-1 | 317 | SELL | ECON | 41.0 | 8 | 65 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06318461894989014 | 0.0 | 0.0 | +— / -eb0046fd-392b-47c4-add2-fc669b031a3c |
| Jogador 4 | 6-1 | 318 | BUY | ECON | 41.0 | 8 | 69 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3552088439464569 | 0.0 | 0.0 | +4869a6d9-9cd7-4ee7-93ae-ae4b2a0c8233 / -— |
| Jogador 4 | 6-1 | 319 | MOVE_BENCH | ECON | 41.0 | 8 | 65 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3336503207683563 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 320 | SELL | ECON | 41.0 | 8 | 65 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029123077169060707 | 0.0 | 0.0 | +— / -4869a6d9-9cd7-4ee7-93ae-ae4b2a0c8233 |
| Jogador 4 | 6-2 | 322 | BUY | ECON | 41.0 | 8 | 82 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25979381799697876 | 0.0 | 0.0 | +e50e0ccc-eb5c-46e0-9049-d5c4d8ea471e / -— |
| Jogador 4 | 6-2 | 323 | REROLL | ECON | 41.0 | 8 | 79 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-2 | 324 | SELL | ECON | 41.0 | 8 | 77 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07500000298023224 | 0.0 | 0.0 | +— / -e50e0ccc-eb5c-46e0-9049-d5c4d8ea471e |
| Jogador 4 | 6-2 | 325 | BUY | ECON | 41.0 | 8 | 80 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41828784346580505 | 0.0 | 0.0 | +89cc418a-8b13-4a3c-8f62-de886873b56c / -— |
| Jogador 4 | 6-2 | 326 | SELL | ECON | 41.0 | 8 | 76 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04472307860851288 | 0.0 | 0.0 | +— / -bdee88f4-e5b5-48fb-9ae5-1fd155982995 |
| Jogador 4 | 6-2 | 327 | BUY | ECON | 41.0 | 8 | 80 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08938945084810257 | 0.0 | 0.0 | +61c7960c-fbf3-452f-9b2e-da0961761371 / -— |
| Jogador 4 | 6-2 | 328 | REROLL | ECON | 41.0 | 8 | 76 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-2 | 329 | SELL | ECON | 41.0 | 8 | 74 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03364615514874458 | 0.0 | 0.0 | +— / -61c7960c-fbf3-452f-9b2e-da0961761371 |
| Jogador 4 | 6-2 | 330 | BUY | ECON | 41.0 | 8 | 78 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13800916075706482 | 0.0 | 0.0 | +b3d39de6-2ee8-41d3-bd7d-fe6efb7067b1 / -— |
| Jogador 4 | 6-3 | 332 | SELL | ECON | 41.0 | 8 | 87 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030694670975208282 | 0.0 | 0.0 | +— / -a5247b50-831c-4600-bac0-e9bcdfa3ce1c |
| Jogador 4 | 6-3 | 333 | BUY | ECON | 41.0 | 8 | 91 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11514434963464737 | 0.0 | 0.0 | +d3dda9b6-13bb-47e1-af12-521aed1576d6 / -— |
| Jogador 4 | 6-3 | 334 | SELL | ECON | 41.0 | 8 | 86 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029318705201148987 | 0.0 | 0.0 | +— / -405ddfe0-1547-4346-84c1-0affe79da8e5 |
| Jogador 4 | 6-3 | 335 | BUY | ECON | 41.0 | 8 | 90 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47705408930778503 | 0.0 | 0.0 | +48f2cdff-3d7b-44b3-bfa7-13b22cfe5e87 / -— |
| Jogador 4 | 6-3 | 336 | REROLL | ECON | 41.0 | 8 | 87 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-3 | 337 | SELL | ECON | 41.0 | 8 | 85 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32820001244544983 | 0.0 | 0.0 | +— / -48f2cdff-3d7b-44b3-bfa7-13b22cfe5e87 |
| Jogador 4 | 6-3 | 338 | BUY | ECON | 41.0 | 8 | 88 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3550185561180115 | 0.0 | 0.0 | +233643ca-941f-4ffe-8d9a-f1ff0f64d1d2 / -— |
| Jogador 4 | 6-3 | 339 | SELL | ECON | 41.0 | 8 | 84 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029123077169060707 | 0.0 | 0.0 | +— / -233643ca-941f-4ffe-8d9a-f1ff0f64d1d2 |
| Jogador 4 | 6-3 | 340 | BUY | ECON | 41.0 | 8 | 88 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03185003250837326 | 0.0 | 0.0 | +d6d15e43-3f39-40c6-8a07-a05854ef835d / -— |
| Jogador 4 | 6-4 | 342 | SELL | ECON | 41.0 | 8 | 98 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04344303905963898 | 0.0 | 0.0 | +— / -d6d15e43-3f39-40c6-8a07-a05854ef835d |
| Jogador 4 | 6-4 | 343 | BUY | ECON | 41.0 | 8 | 102 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11570151895284653 | 0.0 | 0.0 | +d65c5164-c57f-4e67-a44e-19a48b97c4a4 / -— |
| Jogador 4 | 6-4 | 344 | SELL | ECON | 41.0 | 8 | 98 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04472307860851288 | 0.0 | 0.0 | +— / -d65c5164-c57f-4e67-a44e-19a48b97c4a4 |
| Jogador 4 | 6-4 | 345 | BUY | ECON | 41.0 | 8 | 102 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21361400187015533 | 0.0 | 0.0 | +8c28b034-ea67-4700-84c5-5dbd3059cbdb / -— |
| Jogador 4 | 6-4 | 346 | REROLL | ECON | 41.0 | 8 | 98 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-4 | 347 | SELL | ECON | 41.0 | 8 | 96 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06318461894989014 | 0.0 | 0.0 | +— / -8c28b034-ea67-4700-84c5-5dbd3059cbdb |
| Jogador 4 | 6-4 | 348 | BUY | ECON | 41.0 | 8 | 100 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6386250257492065 | 0.0 | 0.0 | +44758e57-e66f-4728-96d0-af1fd04cc221 / -— |
| Jogador 4 | 6-4 | 349 | SELL | ECON | 41.0 | 8 | 95 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030323076993227005 | 0.0 | 0.0 | +— / -22f1ab5f-b752-49e7-b6f0-ed9b5e641d64 |
| Jogador 4 | 6-4 | 350 | BUY | ECON | 41.0 | 8 | 100 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11234577745199203 | 0.0 | 0.0 | +958f6451-3c74-442e-a0a9-03d549dfd183 / -— |
| Jogador 4 | 6-5 | 352 | SELL | ECON | 41.0 | 8 | 109 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029321100562810898 | 0.0 | 0.0 | +— / -958f6451-3c74-442e-a0a9-03d549dfd183 |
| Jogador 4 | 6-5 | 353 | BUY | ECON | 41.0 | 8 | 113 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.048500657081604 | 0.0 | 0.0 | +0805d2e7-a19e-4760-b726-78436ad911b1 / -2cdf9a6a-5786-4a2b-8c4e-6fb9b151a92d,5f79a010-9e28-4a94-be40-973a17313186 |
| Jogador 4 | 6-5 | 354 | BUY | ECON | 41.0 | 8 | 110 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08719558268785477 | 0.0 | 0.0 | +3c1ce6b8-3dfe-4385-aeb3-dee588480540 / -— |
| Jogador 4 | 6-5 | 355 | BUY | ECON | 41.0 | 8 | 106 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.031978290528059006 | 0.0 | 0.0 | +2a9b1e8d-4aee-444b-811e-0be2249d114f / -— |
| Jogador 4 | 6-5 | 356 | REROLL | ECON | 41.0 | 8 | 102 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-5 | 357 | SELL | ECON | 41.0 | 8 | 100 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4618000090122223 | 0.0 | 0.0 | +— / -0805d2e7-a19e-4760-b726-78436ad911b1 |
| Jogador 4 | 6-5 | 358 | EQUIP_FROM_INVENTORY | ECON | 41.0 | 8 | 108 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.04983363673090935 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-5 | 359 | EQUIP_FROM_INVENTORY | ECON | 41.0 | 8 | 108 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.00830136053264141 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-5 | 360 | BUY | ECON | 41.0 | 8 | 108 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4774564504623413 | 0.0 | 0.0 | +786ad7ff-567c-4152-96b9-f05a1d09303d / -— |
| Jogador 4 | 6-6 | 362 | SELL | ECON | 41.0 | 8 | 121 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05452258512377739 | 0.0 | 0.0 | +— / -2a9b1e8d-4aee-444b-811e-0be2249d114f |
| Jogador 4 | 6-6 | 363 | BUY | ECON | 41.0 | 8 | 125 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04585079103708267 | 0.0 | 0.0 | +6773fbc8-b53d-4a82-a7f5-71d4237e5de7 / -— |
| Jogador 4 | 6-6 | 364 | SELL | ECON | 41.0 | 8 | 120 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03364615514874458 | 0.0 | 0.0 | +— / -3c1ce6b8-3dfe-4385-aeb3-dee588480540 |
| Jogador 4 | 6-6 | 365 | BUY | ECON | 41.0 | 8 | 124 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25563618540763855 | 0.0 | 0.0 | +fdc17360-8d79-44b4-8b7e-4fc1f86a76b7 / -— |
| Jogador 4 | 6-6 | 366 | REROLL | ECON | 41.0 | 8 | 120 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-6 | 367 | SELL | ECON | 41.0 | 8 | 118 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07426153868436813 | 0.0 | 0.0 | +— / -fdc17360-8d79-44b4-8b7e-4fc1f86a76b7 |
| Jogador 4 | 6-6 | 368 | BUY | ECON | 41.0 | 8 | 122 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11023854464292526 | 0.0 | 0.0 | +d7a1b629-d510-43ca-9135-5f487c38500d / -— |
| Jogador 4 | 6-6 | 369 | SELL | ECON | 41.0 | 8 | 118 | 5 | 48.0 | Adaptador/DA_18_Aphelios | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02935205213725567 | 0.0 | 0.0 | +— / -d7a1b629-d510-43ca-9135-5f487c38500d |
| Jogador 4 | 6-6 | 370 | BUY | ECON | 41.0 | 8 | 122 | 5 | 48.0 | Adaptador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.149881511926651 | 0.0 | 0.0 | +a4c663e8-5bdc-433d-93ae-5bf576160bd1 / -— |
| Jogador 5 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.01586153917014599 | 0.0 | 0.0 | +— / -f9c418e0-f8aa-4492-8b97-8855ce3af370 |
| Jogador 5 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +a05f4164-724c-4182-bafc-82ef354cea0b / -— |
| Jogador 5 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.5990749597549438 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.032908253371715546 | 0.0 | 0.0 | +df7d3860-9b2e-45ed-b564-281d95e64e82 / -— |
| Jogador 5 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36288121342658997 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 13 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 20 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2552894055843353 | 0.0 | 0.0 | +4a7ac9c5-c110-4566-80e5-25d9e6033799 / -— |
| Jogador 5 | 1-3 | 21 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18221034109592438 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 22 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 28 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3326510190963745 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 30 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1024957075715065 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Elise | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5770185589790344 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 32 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Sejuani | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 40 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6123588681221008 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.22462794184684753 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 42 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7062301635742188 | 0.0 | 0.0 | +— / -df330dae-9fc1-440f-896d-a733d052e5ba |
| Jogador 5 | 2-1 | 43 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.12542009353637695 | 0.0 | 0.0 | +a5c3f6df-50ac-4f3b-aa9c-6476a055aa53 / -— |
| Jogador 5 | 2-1 | 44 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 14.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 50 | SELL | STABILIZE | 100.0 | 4 | 9 | 0 | 14.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22167691588401794 | 0.0 | 0.0 | +— / -a5c3f6df-50ac-4f3b-aa9c-6476a055aa53 |
| Jogador 5 | 2-2 | 51 | BUY | STABILIZE | 100.0 | 4 | 11 | 1 | 14.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.19164136052131653 | 0.0 | 0.0 | +68cd8ae3-399f-461f-89a8-189d7b0a6b59 / -— |
| Jogador 5 | 2-2 | 52 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 8 | 0 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2748807370662689 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 53 | SELL | STABILIZE | 100.0 | 4 | 8 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07832307368516922 | 0.0 | 0.0 | +— / -1934c7ef-cc22-45b3-bed9-01aea61ffbdb |
| Jogador 5 | 2-2 | 54 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.12682415544986725 | 0.0 | 0.0 | +0debca82-3a2a-44ba-af48-83211d5e5243 / -— |
| Jogador 5 | 2-2 | 55 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 56 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 60 | SELL | STABILIZE | 95.0 | 4 | 8 | 0 | 16.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6124769449234009 | 0.0 | 0.0 | +— / -0debca82-3a2a-44ba-af48-83211d5e5243 |
| Jogador 5 | 2-3 | 61 | BUY | STABILIZE | 95.0 | 4 | 11 | 1 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.32278546690940857 | 0.0 | 0.0 | +0da2c93c-0c62-4fe0-94ff-688f086141e3 / -— |
| Jogador 5 | 2-3 | 62 | BUY_XP | STABILIZE | 95.0 | 4 | 10 | 1 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.058435000479221344 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 63 | SELL | STABILIZE | 95.0 | 5 | 6 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37278544902801514 | 0.0 | 0.0 | +— / -0da2c93c-0c62-4fe0-94ff-688f086141e3 |
| Jogador 5 | 2-3 | 64 | BUY | STABILIZE | 95.0 | 5 | 7 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3334686756134033 | 0.0 | 0.0 | +abde1e81-f452-47ad-9f1e-45efb138f86d / -— |
| Jogador 5 | 2-3 | 65 | BUY_XP | STABILIZE | 95.0 | 5 | 6 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 66 | PASS | STABILIZE | 95.0 | 5 | 2 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 68 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 2 | 0 | 16.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4409887194633484 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 70 | BUY | STABILIZE | 90.0 | 5 | 8 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2194368690252304 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 71 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 5 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33023467659950256 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 72 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 5 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.272696316242218 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 73 | PASS | STABILIZE | 90.0 | 5 | 5 | 0 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 79 | BUY | STABILIZE | 90.0 | 5 | 11 | 1 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0383907556533813 | 0.0 | 0.0 | +de78e1b7-ed58-42dd-8374-76b578543e94 / -— |
| Jogador 5 | 2-5 | 80 | SELL | STABILIZE | 90.0 | 5 | 10 | 1 | 20.0 | Devastador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017270030453801155 | 0.0 | 0.0 | +— / -df7d3860-9b2e-45ed-b564-281d95e64e82 |
| Jogador 5 | 2-5 | 81 | SELL | SLOWROLL | 90.0 | 5 | 12 | 1 | 20.0 | Devastador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.2230000495910645 | 0.0 | 0.0 | +— / -de78e1b7-ed58-42dd-8374-76b578543e94 |
| Jogador 5 | 2-5 | 82 | BUY | STABILIZE | 90.0 | 5 | 13 | 1 | 20.0 | Devastador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.05456497520208359 | 0.0 | 0.0 | +486e92ad-4dcf-4c0e-a470-e0b87777d380 / -— |
| Jogador 5 | 2-5 | 83 | BUY_XP | STABILIZE | 90.0 | 5 | 10 | 1 | 20.0 | Devastador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 84 | BUY_XP | STABILIZE | 90.0 | 5 | 6 | 0 | 20.0 | Devastador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 85 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 2 | 0 | 20.0 | Devastador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6188474893569946 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 86 | PASS | STABILIZE | 90.0 | 5 | 2 | 0 | 20.0 | Devastador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 88 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 8 | 0 | 20.0 | Devastador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3495495617389679 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 89 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 8 | 0 | 20.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08583671599626541 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 90 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 8 | 0 | 20.0 | Devastador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6186678409576416 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 91 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 8 | 0 | 20.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3494434952735901 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 92 | PASS | STABILIZE | 84.0 | 6 | 8 | 0 | 20.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 95 | MOVE_BENCH | STABILIZE | 84.0 | 6 | 8 | 0 | 20.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5102653503417969 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 97 | BUY | FAST8 | 79.0 | 6 | 14 | 1 | 26.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.031341686844825745 | 0.0 | 0.0 | +837b2d09-a207-4830-b36d-29e493bbcc22 / -— |
| Jogador 5 | 2-7 | 98 | BUY_XP | FAST8 | 79.0 | 6 | 12 | 1 | 26.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 99 | BUY_XP | FAST8 | 79.0 | 6 | 8 | 0 | 26.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 100 | BUY_XP | FAST8 | 79.0 | 6 | 4 | 0 | 26.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 101 | PASS | FAST8 | 79.0 | 6 | 0 | 0 | 26.0 | Devastador/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 106 | BUY | FAST8 | 79.0 | 6 | 6 | 0 | 26.0 | Devastador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12435714900493622 | 0.0 | 0.0 | +e8c36276-b932-45ba-b350-2d1cb339a019 / -— |
| Jogador 5 | 3-1 | 107 | MOVE_BOARD | FAST8 | 79.0 | 6 | 3 | 0 | 26.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25012993812561035 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 108 | MOVE_BOARD | FAST8 | 79.0 | 6 | 3 | 0 | 26.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11584769189357758 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 109 | PASS | FAST8 | 79.0 | 6 | 3 | 0 | 26.0 | Devastador/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 115 | SELL | FAST8 | 79.0 | 6 | 9 | 0 | 26.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0742974653840065 | 0.0 | 0.0 | +— / -837b2d09-a207-4830-b36d-29e493bbcc22 |
| Jogador 5 | 3-2 | 116 | BUY | FAST8 | 79.0 | 6 | 11 | 1 | 26.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6476626396179199 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -— |
| Jogador 5 | 3-2 | 117 | MOVE_BENCH | FAST8 | 79.0 | 6 | 8 | 0 | 26.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0341612808406353 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 118 | MOVE_BENCH | FAST8 | 79.0 | 6 | 8 | 0 | 26.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4294731020927429 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 119 | PASS | FAST8 | 79.0 | 6 | 8 | 0 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 124 | SELL | FAST8 | 79.0 | 6 | 15 | 1 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47716382145881653 | 0.0 | 0.0 | +— / -abde1e81-f452-47ad-9f1e-45efb138f86d |
| Jogador 5 | 3-3 | 125 | MOVE_BENCH | FAST8 | 79.0 | 6 | 16 | 1 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 126 | MOVE_BENCH | FAST8 | 79.0 | 6 | 16 | 1 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05678972974419594 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 127 | BUY | FAST8 | 79.0 | 6 | 16 | 1 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7318906784057617 | 0.0 | 0.0 | +a12781fd-4d61-4c7e-b439-a6e62bd48dfe / -— |
| Jogador 5 | 3-3 | 128 | MOVE_BENCH | FAST8 | 79.0 | 6 | 13 | 1 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21753649413585663 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 129 | MOVE_BENCH | FAST8 | 79.0 | 6 | 13 | 1 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 130 | PASS | FAST8 | 79.0 | 6 | 13 | 1 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 133 | MOVE_BENCH | FAST8 | 68.0 | 6 | 19 | 1 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08005346357822418 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 134 | MOVE_BENCH | FAST8 | 68.0 | 6 | 19 | 1 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0021017869003117085 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 135 | MOVE_BENCH | FAST8 | 68.0 | 6 | 19 | 1 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1740005910396576 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 136 | MOVE_BENCH | FAST8 | 68.0 | 6 | 19 | 1 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 137 | PASS | FAST8 | 68.0 | 6 | 19 | 1 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 142 | BUY | FAST8 | 68.0 | 6 | 25 | 2 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23476308584213257 | 0.0 | 0.0 | +4518ad1d-87e7-4110-830a-96183c533201 / -— |
| Jogador 5 | 3-5 | 143 | MOVE_BENCH | FAST8 | 68.0 | 6 | 22 | 2 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12582725286483765 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 144 | MOVE_BENCH | FAST8 | 68.0 | 6 | 22 | 2 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3867127001285553 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 145 | PASS | FAST8 | 68.0 | 6 | 22 | 2 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05950000137090683 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 152 | MOVE_BENCH | FAST8 | 57.0 | 6 | 30 | 3 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 153 | MOVE_BENCH | FAST8 | 57.0 | 6 | 30 | 3 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08666982501745224 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 154 | MOVE_BENCH | FAST8 | 57.0 | 6 | 30 | 3 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1742102950811386 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 155 | MOVE_BENCH | FAST8 | 57.0 | 6 | 30 | 3 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15635085105895996 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 156 | MOVE_BENCH | FAST8 | 57.0 | 6 | 30 | 3 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04352870583534241 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 157 | MOVE_BENCH | FAST8 | 57.0 | 6 | 30 | 3 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18132004141807556 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 158 | BUY | FAST8 | 57.0 | 6 | 30 | 3 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1180320605635643 | 0.0 | 0.0 | +68d2cec6-d29b-4173-a696-ac20ccb1f079 / -— |
| Jogador 5 | 3-6 | 159 | PASS | FAST8 | 57.0 | 6 | 28 | 2 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 162 | BUY | FAST8 | 57.0 | 6 | 36 | 3 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10867969691753387 | 0.0 | 0.0 | +9175d2a8-4736-402d-873b-cf4846b04d97 / -— |
| Jogador 5 | 3-7 | 163 | PASS | FAST8 | 57.0 | 6 | 33 | 3 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12449999898672104 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 172 | BUY | FAST8 | 57.0 | 6 | 41 | 4 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1788732409477234 | 0.0 | 0.0 | +7fd8b302-97aa-4373-94f4-adfcad477ed2 / -— |
| Jogador 5 | 4-1 | 173 | BUY | FAST8 | 57.0 | 6 | 38 | 3 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2571942210197449 | 0.0 | 0.0 | +86530a1f-5325-45fa-bf43-86419ccfda54 / -— |
| Jogador 5 | 4-1 | 174 | PASS | FAST8 | 57.0 | 6 | 35 | 3 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17928571999073029 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 182 | BUY | FAST8 | 43.0 | 6 | 43 | 4 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1865900754928589 | 0.0 | 0.0 | +badbffc5-dd49-4cd8-8b4d-941ae020e6e3 / -— |
| Jogador 5 | 4-2 | 183 | BUY | FAST8 | 43.0 | 6 | 39 | 3 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4368501901626587 | 0.0 | 0.0 | +a9588010-57fa-4baf-b226-a30f519342e7 / -— |
| Jogador 5 | 4-2 | 184 | REROLL | FAST8 | 43.0 | 6 | 37 | 3 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 185 | SELL | FAST8 | 43.0 | 6 | 35 | 3 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32297489047050476 | 0.0 | 0.0 | +— / -68d2cec6-d29b-4173-a696-ac20ccb1f079 |
| Jogador 5 | 4-2 | 186 | BUY | FAST8 | 43.0 | 6 | 37 | 3 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6847770810127258 | 0.0 | 0.0 | +fb551efa-6ad5-4f97-aa05-bc5eb70943d4 / -— |
| Jogador 5 | 4-2 | 187 | REROLL | FAST8 | 43.0 | 6 | 34 | 3 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 188 | SELL | FAST8 | 43.0 | 6 | 32 | 3 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05372411385178566 | 0.0 | 0.0 | +— / -a9588010-57fa-4baf-b226-a30f519342e7 |
| Jogador 5 | 4-2 | 189 | BUY | FAST8 | 43.0 | 6 | 34 | 3 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07778792083263397 | 0.0 | 0.0 | +2530bb2a-8b40-4f0b-a49c-f13fe67fbca4 / -— |
| Jogador 5 | 4-2 | 190 | REROLL | FAST8 | 43.0 | 6 | 32 | 3 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 192 | SELL | STABILIZE | 32.0 | 6 | 39 | 3 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11409885436296463 | 0.0 | 0.0 | +— / -2530bb2a-8b40-4f0b-a49c-f13fe67fbca4 |
| Jogador 5 | 4-3 | 193 | BUY | STABILIZE | 32.0 | 6 | 41 | 4 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.862385094165802 | 0.0 | 0.0 | +b1efce8c-0cb0-47fc-a361-c50a76c0f9de / -— |
| Jogador 5 | 4-3 | 194 | SELL | STABILIZE | 32.0 | 6 | 40 | 4 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08100000023841858 | 0.0 | 0.0 | +— / -86530a1f-5325-45fa-bf43-86419ccfda54 |
| Jogador 5 | 4-3 | 195 | BUY | STABILIZE | 32.0 | 6 | 43 | 4 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14184348285198212 | 0.0 | 0.0 | +477a3c7c-70fe-4f67-ab00-8c9c397365bf / -— |
| Jogador 5 | 4-3 | 196 | REROLL | STABILIZE | 32.0 | 6 | 40 | 4 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17399999499320984 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 197 | REROLL | STABILIZE | 32.0 | 6 | 38 | 3 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 198 | SELL | STABILIZE | 32.0 | 6 | 36 | 3 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.066600002348423 | 0.0 | 0.0 | +— / -9175d2a8-4736-402d-873b-cf4846b04d97 |
| Jogador 5 | 4-3 | 199 | BUY | STABILIZE | 32.0 | 6 | 39 | 3 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1452348232269287 | 0.0 | 0.0 | +7fb0217d-521c-42b5-995c-81e299b3b934 / -— |
| Jogador 5 | 4-3 | 200 | REROLL | STABILIZE | 32.0 | 6 | 36 | 3 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 202 | SELL | STABILIZE | 18.0 | 7 | 43 | 4 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05700000002980232 | 0.0 | 0.0 | +— / -7fb0217d-521c-42b5-995c-81e299b3b934 |
| Jogador 5 | 4-4 | 203 | BUY | STABILIZE | 18.0 | 7 | 46 | 4 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8911033868789673 | 0.0 | 0.0 | +673bda2e-1343-4894-8005-c3ee2c90f1b7 / -— |
| Jogador 5 | 4-4 | 204 | SELL | STABILIZE | 18.0 | 7 | 43 | 4 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3081692159175873 | 0.0 | 0.0 | +— / -0f1b15a2-9978-4691-a15e-483ccd03db7f |
| Jogador 5 | 4-4 | 205 | BUY | STABILIZE | 18.0 | 7 | 46 | 4 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8451768755912781 | 0.0 | 0.0 | +565ff610-fe51-470b-8452-a7eec5e31653 / -— |
| Jogador 5 | 4-4 | 206 | SELL | STABILIZE | 18.0 | 7 | 43 | 4 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.066600002348423 | 0.0 | 0.0 | +— / -fb551efa-6ad5-4f97-aa05-bc5eb70943d4 |
| Jogador 5 | 4-4 | 207 | BUY | STABILIZE | 18.0 | 7 | 46 | 4 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26938608288764954 | 0.0 | 0.0 | +db6b2dca-4de1-420e-aadb-943e19b6121a / -— |
| Jogador 5 | 4-4 | 208 | REROLL | STABILIZE | 18.0 | 7 | 44 | 4 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 209 | SELL | STABILIZE | 18.0 | 7 | 42 | 4 | 30.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.052723076194524765 | 0.0 | 0.0 | +— / -badbffc5-dd49-4cd8-8b4d-941ae020e6e3 |
| Jogador 5 | 4-4 | 210 | MOVE_BENCH | STABILIZE | 18.0 | 7 | 46 | 4 | 30.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6172614097595215 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 212 | BUY | STABILIZE | 18.0 | 7 | 56 | 5 | 36.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2221710979938507 | 0.0 | 0.0 | +2f2ff445-f60a-4a05-b37a-41b8a6d6c7f9 / -— |
| Jogador 5 | 4-5 | 213 | BUY | STABILIZE | 18.0 | 7 | 51 | 5 | 36.0 | Feérico/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.782345712184906 | 0.0 | 0.0 | +ee67f5c6-559f-492e-9cc0-6bc19a203d6a / -— |
| Jogador 5 | 4-5 | 214 | REROLL | STABILIZE | 18.0 | 7 | 48 | 4 | 36.0 | Feérico/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 215 | SELL | STABILIZE | 18.0 | 7 | 46 | 4 | 36.0 | Feérico/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0538967102766037 | 0.0 | 0.0 | +— / -db6b2dca-4de1-420e-aadb-943e19b6121a |
| Jogador 5 | 4-5 | 216 | BUY | STABILIZE | 18.0 | 7 | 48 | 4 | 36.0 | Feérico/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13671068847179413 | 0.0 | 0.0 | +f32e50e0-1430-4549-a1dd-a8473ffe0bd4 / -— |
| Jogador 5 | 4-5 | 217 | REROLL | STABILIZE | 18.0 | 7 | 46 | 4 | 36.0 | Feérico/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 218 | SELL | STABILIZE | 18.0 | 7 | 44 | 4 | 36.0 | Feérico/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03799446299672127 | 0.0 | 0.0 | +— / -f32e50e0-1430-4549-a1dd-a8473ffe0bd4 |
| Jogador 5 | 4-5 | 219 | BUY | STABILIZE | 18.0 | 7 | 46 | 4 | 36.0 | Feérico/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13198794424533844 | 0.0 | 0.0 | +2949d735-3c16-4a45-835b-e11a9c12b16a / -— |
| Jogador 5 | 4-5 | 220 | SELL | STABILIZE | 18.0 | 7 | 43 | 4 | 36.0 | Feérico/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05700000002980232 | 0.0 | 0.0 | +— / -2949d735-3c16-4a45-835b-e11a9c12b16a |
| Jogador 5 | 4-6 | 222 | BUY | STABILIZE | 18.0 | 7 | 56 | 5 | 36.0 | Feérico/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08128232508897781 | 0.0 | 0.0 | +217a3ebb-1953-4f1e-bfdd-a3c9438e791e / -— |
| Jogador 5 | 4-6 | 223 | SELL | STABILIZE | 18.0 | 7 | 52 | 5 | 36.0 | Feérico/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04472307860851288 | 0.0 | 0.0 | +— / -217a3ebb-1953-4f1e-bfdd-a3c9438e791e |
| Jogador 5 | 4-6 | 224 | BUY | STABILIZE | 18.0 | 7 | 56 | 5 | 36.0 | Feérico/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14354434609413147 | 0.0 | 0.0 | +3658b5d8-450f-451a-8487-5b3bdd7c385b / -— |
| Jogador 5 | 4-6 | 225 | REROLL | STABILIZE | 18.0 | 7 | 54 | 5 | 36.0 | Feérico/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 226 | SELL | STABILIZE | 18.0 | 7 | 52 | 5 | 36.0 | Feérico/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03375108912587166 | 0.0 | 0.0 | +— / -3658b5d8-450f-451a-8487-5b3bdd7c385b |
| Jogador 5 | 4-6 | 227 | BUY | STABILIZE | 18.0 | 7 | 54 | 5 | 36.0 | Feérico/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07956533133983612 | 0.0 | 0.0 | +e1055913-2340-4af0-8527-e175c8bc1ccb / -— |
| Jogador 5 | 4-6 | 228 | SELL | STABILIZE | 18.0 | 7 | 50 | 5 | 36.0 | Feérico/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04472307860851288 | 0.0 | 0.0 | +— / -e1055913-2340-4af0-8527-e175c8bc1ccb |
| Jogador 5 | 4-6 | 229 | BUY | STABILIZE | 18.0 | 7 | 54 | 5 | 36.0 | Feérico/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09043493866920471 | 0.0 | 0.0 | +4b1f1146-d580-41e9-987f-c32b1eb98b75 / -— |
| Jogador 5 | 4-6 | 230 | REROLL | STABILIZE | 18.0 | 7 | 50 | 5 | 36.0 | Feérico/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17399999499320984 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 232 | SELL | STABILIZE | 18.0 | 7 | 59 | 5 | 36.0 | Feérico/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04472307860851288 | 0.0 | 0.0 | +— / -4b1f1146-d580-41e9-987f-c32b1eb98b75 |
| Jogador 5 | 4-7 | 233 | BUY | STABILIZE | 18.0 | 7 | 63 | 5 | 36.0 | Feérico/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0014235973358154 | 0.0 | 0.0 | +aea521ef-8511-4b98-9c6d-e83b814777df / -565ff610-fe51-470b-8452-a7eec5e31653,7fd8b302-97aa-4373-94f4-adfcad477ed2 |
| Jogador 5 | 4-7 | 234 | BUY | STABILIZE | 18.0 | 7 | 60 | 5 | 30.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5476138591766357 | 0.0 | 0.0 | +d9097eba-c1b2-4df8-9e5d-a9134dbfe52f / -— |
| Jogador 5 | 4-7 | 235 | REROLL | STABILIZE | 18.0 | 7 | 58 | 5 | 30.0 | Feérico/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 236 | SELL | STABILIZE | 18.0 | 7 | 56 | 5 | 30.0 | Feérico/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3262799382209778 | 0.0 | 0.0 | +— / -d9097eba-c1b2-4df8-9e5d-a9134dbfe52f |
| Jogador 5 | 4-7 | 237 | BUY | STABILIZE | 18.0 | 7 | 58 | 5 | 30.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8933348059654236 | 0.0 | 0.0 | +e5f61076-ec13-419b-a4e8-d91b9975cfd6 / -486e92ad-4dcf-4c0e-a470-e0b87777d380,a12781fd-4d61-4c7e-b439-a6e62bd48dfe |
| Jogador 5 | 4-7 | 238 | MOVE_BENCH | STABILIZE | 18.0 | 7 | 55 | 5 | 18.0 | Feérico/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42306265234947205 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 239 | BUY | STABILIZE | 18.0 | 7 | 55 | 5 | 24.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07104922831058502 | 0.0 | 0.0 | +e978e901-0a52-4f01-ba52-a83fbcc3b439 / -— |
| Jogador 5 | 4-7 | 240 | MOVE_BENCH | STABILIZE | 18.0 | 7 | 52 | 5 | 24.0 | Feérico/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4645911753177643 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 242 | EQUIP_FROM_INVENTORY | STABILIZE | 18.0 | 7 | 63 | 5 | 34.0 | Feérico/DA_18_Diana | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 243 | BUY | STABILIZE | 18.0 | 7 | 63 | 5 | 34.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.421543687582016 | 0.0 | 0.0 | +8538e488-6f36-433a-b261-73626f24bb07 / -— |
| Jogador 5 | 5-1 | 244 | SELL | STABILIZE | 18.0 | 7 | 60 | 5 | 34.0 | Feérico/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3151243329048157 | 0.0 | 0.0 | +— / -8538e488-6f36-433a-b261-73626f24bb07 |
| Jogador 5 | 5-1 | 245 | BUY | STABILIZE | 18.0 | 7 | 63 | 5 | 34.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.18828390538692474 | 0.0 | 0.0 | +93581e04-3f00-4430-8e5b-c953196bc1de / -— |
| Jogador 5 | 5-1 | 246 | SELL | STABILIZE | 18.0 | 7 | 60 | 5 | 34.0 | Feérico/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0594613216817379 | 0.0 | 0.0 | +— / -e978e901-0a52-4f01-ba52-a83fbcc3b439 |
| Jogador 5 | 5-1 | 247 | BUY | STABILIZE | 18.0 | 7 | 63 | 5 | 34.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4011477828025818 | 0.0 | 0.0 | +d632ff66-a7c4-43d3-afb3-b83c174cda35 / -— |
| Jogador 5 | 5-1 | 248 | REROLL | STABILIZE | 18.0 | 7 | 60 | 5 | 34.0 | Feérico/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 249 | SELL | STABILIZE | 18.0 | 7 | 58 | 5 | 34.0 | Feérico/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3141692280769348 | 0.0 | 0.0 | +— / -93581e04-3f00-4430-8e5b-c953196bc1de |
| Jogador 5 | 5-1 | 250 | MOVE_BENCH | STABILIZE | 18.0 | 7 | 61 | 5 | 34.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6376209259033203 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 252 | BUY | STABILIZE | 18.0 | 7 | 72 | 5 | 40.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9148947596549988 | 0.0 | 0.0 | +94e47e85-54f4-4546-af6a-3700e3c325a8 / -— |
| Jogador 5 | 5-2 | 253 | BUY | STABILIZE | 18.0 | 7 | 67 | 5 | 40.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.25466036796569824 | 0.0 | 0.0 | +335c4988-791a-4579-a473-f387b986806c / -— |
| Jogador 5 | 5-2 | 254 | SELL | STABILIZE | 18.0 | 7 | 63 | 5 | 40.0 | Feérico/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.060600001364946365 | 0.0 | 0.0 | +— / -d632ff66-a7c4-43d3-afb3-b83c174cda35 |
| Jogador 5 | 5-2 | 255 | BUY | STABILIZE | 18.0 | 7 | 66 | 5 | 40.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.13945001363754272 | 0.0 | 0.0 | +158c7931-f8db-44bd-a279-53dd6e59b352 / -— |
| Jogador 5 | 5-2 | 256 | REROLL | STABILIZE | 18.0 | 7 | 64 | 5 | 40.0 | Feérico/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 257 | SELL | STABILIZE | 18.0 | 7 | 62 | 5 | 40.0 | Feérico/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0299538467079401 | 0.0 | 0.0 | +— / -158c7931-f8db-44bd-a279-53dd6e59b352 |
| Jogador 5 | 5-2 | 258 | BUY | STABILIZE | 18.0 | 7 | 64 | 5 | 40.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.42660456895828247 | 0.0 | 0.0 | +c3596d89-03d2-4fc7-afaf-591f10423252 / -— |
| Jogador 5 | 5-2 | 259 | SELL | STABILIZE | 18.0 | 7 | 61 | 5 | 40.0 | Feérico/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.07426153868436813 | 0.0 | 0.0 | +— / -335c4988-791a-4579-a473-f387b986806c |
| Jogador 5 | 5-2 | 260 | BUY | STABILIZE | 18.0 | 7 | 65 | 5 | 40.0 | Feérico/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.36941808462142944 | 0.0 | 0.0 | +7fd34ef6-a124-4d23-a166-9f7ad919c826 / -— |
| Jogador 5 | 5-3 | 262 | SELL | STABILIZE | 18.0 | 7 | 74 | 5 | 40.0 | Feérico/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.4645749628543854 | 0.0 | 0.0 | +— / -aea521ef-8511-4b98-9c6d-e83b814777df |
| Jogador 5 | 5-3 | 263 | BUY | STABILIZE | 18.0 | 7 | 82 | 5 | 40.0 | Feérico/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2586352527141571 | 0.0 | 0.0 | +1505b8ee-8c59-40ae-b774-fdce1230b8ef / -— |
| Jogador 5 | 5-3 | 264 | SELL | STABILIZE | 18.0 | 7 | 78 | 5 | 40.0 | Feérico/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.07426153868436813 | 0.0 | 0.0 | +— / -1505b8ee-8c59-40ae-b774-fdce1230b8ef |
| Jogador 5 | 5-3 | 265 | BUY | STABILIZE | 18.0 | 7 | 82 | 5 | 40.0 | Feérico/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.12407415360212326 | 0.0 | 0.0 | +b75d78d9-6080-40b3-ad63-30afae49e0a5 / -— |
| Jogador 5 | 5-3 | 266 | SELL | STABILIZE | 18.0 | 7 | 78 | 5 | 40.0 | Feérico/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04472307860851288 | 0.0 | 0.0 | +— / -b75d78d9-6080-40b3-ad63-30afae49e0a5 |
| Jogador 5 | 5-3 | 267 | BUY | STABILIZE | 18.0 | 7 | 82 | 5 | 40.0 | Feérico/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.13209643959999084 | 0.0 | 0.0 | +d14fd3f6-4cb4-4ffe-8f73-ba7946765a85 / -— |
| Jogador 5 | 5-3 | 268 | REROLL | STABILIZE | 18.0 | 7 | 80 | 5 | 40.0 | Feérico/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 269 | SELL | STABILIZE | 18.0 | 7 | 78 | 5 | 40.0 | Feérico/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -d14fd3f6-4cb4-4ffe-8f73-ba7946765a85 |
| Jogador 5 | 5-3 | 270 | BUY | STABILIZE | 18.0 | 7 | 80 | 5 | 40.0 | Feérico/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.21953098475933075 | 0.0 | 0.0 | +4f487e34-c67d-489d-a21e-78b5642aefd4 / -— |
| Jogador 5 | 5-4 | 272 | SELL | ALL_IN | 4.0 | 7 | 86 | 5 | 40.0 | Feérico/DA_18_Alune | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.06318461894989014 | 0.0 | 0.0 | +— / -4f487e34-c67d-489d-a21e-78b5642aefd4 |
| Jogador 5 | 5-4 | 273 | BUY | ALL_IN | 4.0 | 7 | 90 | 5 | 40.0 | Feérico/DA_18_Alune | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0524766445159912 | 0.0 | 0.0 | +6b0bead4-2978-41d5-a28d-a4c395f456a7 / -68b28241-1946-4304-8b10-ae24a13a8e60,e8c36276-b932-45ba-b350-2d1cb339a019 |
| Jogador 5 | 5-4 | 274 | MOVE_BENCH | ALL_IN | 4.0 | 7 | 87 | 5 | 28.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.7752348780632019 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 275 | MOVE_BENCH | ALL_IN | 4.0 | 7 | 87 | 5 | 28.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5593191385269165 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 276 | BUY | ALL_IN | 4.0 | 7 | 87 | 5 | 34.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6365245580673218 | 0.0 | 0.0 | +16ccc1d8-1393-41a2-9f14-000d94c78bca / -— |
| Jogador 5 | 5-4 | 277 | SELL | ALL_IN | 4.0 | 7 | 85 | 5 | 34.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3447584807872772 | 0.0 | 0.0 | +— / -16ccc1d8-1393-41a2-9f14-000d94c78bca |
| Jogador 5 | 5-4 | 278 | BUY | ALL_IN | 4.0 | 7 | 87 | 5 | 34.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.018439898267388344 | 0.0 | 0.0 | +a98c021a-415b-43eb-b741-97bdac39a598 / -— |
| Jogador 5 | 5-4 | 279 | REROLL | ALL_IN | 4.0 | 7 | 84 | 5 | 34.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 280 | MOVE_BENCH | ALL_IN | 4.0 | 7 | 82 | 5 | 34.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.609574556350708 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 282 | BUY | ALL_IN | 4.0 | 7 | 92 | 5 | 44.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4121928811073303 | 0.0 | 0.0 | +22c22c9e-03f7-4ff6-8880-fd8937bec7dc / -— |
| Jogador 5 | 5-5 | 283 | SELL | ALL_IN | 4.0 | 7 | 87 | 5 | 44.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05764615535736084 | 0.0 | 0.0 | +— / -a98c021a-415b-43eb-b741-97bdac39a598 |
| Jogador 5 | 5-5 | 284 | BUY | ALL_IN | 4.0 | 7 | 90 | 5 | 44.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2710864841938019 | 0.0 | 0.0 | +1477dd4d-8f90-4921-b6fd-ffaa744f0dce / -— |
| Jogador 5 | 5-5 | 285 | REROLL | ALL_IN | 4.0 | 7 | 88 | 5 | 44.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 286 | SELL | ALL_IN | 4.0 | 7 | 86 | 5 | 44.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.07500000298023224 | 0.0 | 0.0 | +— / -1477dd4d-8f90-4921-b6fd-ffaa744f0dce |
| Jogador 5 | 5-5 | 287 | BUY | ALL_IN | 4.0 | 7 | 88 | 5 | 44.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.062083255499601364 | 0.0 | 0.0 | +a14b4ce7-5af2-4930-9bda-7cadb7b4f8f4 / -— |
| Jogador 5 | 5-5 | 288 | SELL | ALL_IN | 4.0 | 7 | 85 | 5 | 44.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0397956520318985 | 0.0 | 0.0 | +— / -a14b4ce7-5af2-4930-9bda-7cadb7b4f8f4 |
| Jogador 5 | 5-5 | 289 | BUY | ALL_IN | 4.0 | 7 | 88 | 5 | 44.0 | Feérico/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2623802423477173 | 0.0 | 0.0 | +f8177556-bc54-4860-a7cf-90a94b0e6c96 / -— |
| Jogador 5 | 5-5 | 290 | REROLL | ALL_IN | 4.0 | 7 | 84 | 5 | 44.0 | Feérico/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.0018307692371308804 | 0.0 | 0.0 | +— / -698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +9002992e-4dcd-4fec-939c-87393464a41d / -— |
| Jogador 6 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.5990749597549438 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2717767059803009 | 0.0 | 0.0 | +908afab9-748c-4057-a2a9-d2686c5d52e0 / -— |
| Jogador 6 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33382871747016907 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 1.0362789630889893 | 0.0 | 0.0 | +425b1e77-5887-40b3-875e-c1f60dc6c513 / -— |
| Jogador 6 | 1-2 | 14 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 18 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4124380648136139 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 20 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.00680168904364109 | 0.0 | 0.0 | +c3c53e80-c8e2-4774-afa2-9b0f4ab3b326 / -— |
| Jogador 6 | 1-3 | 21 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 30 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37860000133514404 | 0.0 | 0.0 | +— / -c3c53e80-c8e2-4774-afa2-9b0f4ab3b326 |
| Jogador 6 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.24339362978935242 | 0.0 | 0.0 | +72aa8420-8dc2-4e9b-a10a-bd2a36f26656 / -— |
| Jogador 6 | 1-4 | 32 | BUY_XP | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 33 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17975932359695435 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 34 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 38 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3833625614643097 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 40 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.040618658065796 | 0.0 | 0.0 | +185ee377-0917-4209-905b-9486d5be0193 / -— |
| Jogador 6 | 2-1 | 41 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.1798723936080933 | 0.0 | 0.0 | +— / -185ee377-0917-4209-905b-9486d5be0193 |
| Jogador 6 | 2-1 | 42 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0402967929840088 | 0.0 | 0.0 | +646fc826-453b-479f-97d1-8aa2a9d86dc3 / -— |
| Jogador 6 | 2-1 | 43 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.179451584815979 | 0.0 | 0.0 | +— / -646fc826-453b-479f-97d1-8aa2a9d86dc3 |
| Jogador 6 | 2-1 | 44 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.025061845779419 | 0.0 | 0.0 | +97d28b21-b7a0-47f5-b9ee-78377ad4c7d8 / -— |
| Jogador 6 | 2-1 | 45 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 50 | SELL | STABILIZE | 96.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.1056586503982544 | 0.0 | 0.0 | +— / -97d28b21-b7a0-47f5-b9ee-78377ad4c7d8 |
| Jogador 6 | 2-2 | 51 | BUY | STABILIZE | 96.0 | 4 | 9 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2446407824754715 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 52 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21012116968631744 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 53 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5010378956794739 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 54 | PASS | STABILIZE | 96.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 60 | SELL | STABILIZE | 89.0 | 4 | 12 | 1 | 12.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.868829607963562 | 0.0 | 0.0 | +— / -908afab9-748c-4057-a2a9-d2686c5d52e0 |
| Jogador 6 | 2-3 | 61 | BUY | STABILIZE | 89.0 | 4 | 13 | 1 | 12.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2286713570356369 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 6 | 2-3 | 62 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 11 | 1 | 12.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2757025957107544 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 63 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 11 | 1 | 10.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05753965675830841 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 64 | SELL | STABILIZE | 89.0 | 4 | 11 | 1 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.033303093165159225 | 0.0 | 0.0 | +— / -72aa8420-8dc2-4e9b-a10a-bd2a36f26656 |
| Jogador 6 | 2-3 | 65 | BUY | STABILIZE | 89.0 | 4 | 12 | 1 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1485002338886261 | 0.0 | 0.0 | +2ef60eed-d073-41a6-adec-4466c673b313 / -— |
| Jogador 6 | 2-3 | 66 | BUY_XP | STABILIZE | 89.0 | 4 | 10 | 1 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07297000288963318 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 67 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47199174761772156 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 68 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 6 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5412683486938477 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 70 | BUY | STABILIZE | 89.0 | 5 | 12 | 1 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0377618074417114 | 0.0 | 0.0 | +18934be2-4988-4f62-9f62-07ba151231f2 / -— |
| Jogador 6 | 2-4 | 71 | SELL | STABILIZE | 89.0 | 5 | 11 | 1 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.179308533668518 | 0.0 | 0.0 | +— / -18934be2-4988-4f62-9f62-07ba151231f2 |
| Jogador 6 | 2-4 | 72 | BUY | STABILIZE | 89.0 | 5 | 12 | 1 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0378546714782715 | 0.0 | 0.0 | +53a17678-f853-4814-97c7-524b66ec199d / -— |
| Jogador 6 | 2-4 | 73 | BUY_XP | STABILIZE | 89.0 | 5 | 11 | 1 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 74 | BUY_XP | SLOWROLL | 89.0 | 5 | 7 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 75 | PASS | SLOWROLL | 89.0 | 5 | 3 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 79 | SELL | SLOWROLL | 89.0 | 5 | 8 | 0 | 18.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.1824650764465332 | 0.0 | 0.0 | +— / -53a17678-f853-4814-97c7-524b66ec199d |
| Jogador 6 | 2-5 | 80 | BUY | STABILIZE | 89.0 | 5 | 9 | 0 | 18.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0460737943649292 | 0.0 | 0.0 | +1b1964b4-7d5e-4cea-8e83-0692f326b599 / -— |
| Jogador 6 | 2-5 | 81 | BUY_XP | SLOWROLL | 89.0 | 5 | 8 | 0 | 18.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 82 | BUY_XP | SLOWROLL | 89.0 | 5 | 4 | 0 | 18.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008980000391602516 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 83 | PASS | SLOWROLL | 89.0 | 6 | 0 | 0 | 18.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 86 | MOVE_BENCH | SLOWROLL | 89.0 | 6 | 0 | 0 | 18.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6013466119766235 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 88 | BUY | SLOWROLL | 89.0 | 6 | 7 | 0 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2421695441007614 | 0.0 | 0.0 | +fee4e511-e40e-4114-a8b6-c2de73117e82 / -— |
| Jogador 6 | 2-6 | 89 | BUY | SLOWROLL | 89.0 | 6 | 4 | 0 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.172775998711586 | 0.0 | 0.0 | +2938180d-94e5-4bb7-832e-baa51f820ba2 / -— |
| Jogador 6 | 2-6 | 90 | MOVE_BENCH | SLOWROLL | 89.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22595669329166412 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 91 | MOVE_BOARD | SLOWROLL | 89.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17583663761615753 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 92 | MOVE_BOARD | SLOWROLL | 89.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3018093705177307 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 93 | MOVE_BOARD | SLOWROLL | 89.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10453628748655319 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 94 | PASS | SLOWROLL | 89.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 97 | SELL | SLOWROLL | 89.0 | 6 | 8 | 0 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.058004576712846756 | 0.0 | 0.0 | +— / -2ef60eed-d073-41a6-adec-4466c673b313 |
| Jogador 6 | 2-7 | 98 | BUY | SLOWROLL | 89.0 | 6 | 10 | 1 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8332839012145996 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 99 | MOVE_BENCH | SLOWROLL | 89.0 | 6 | 7 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40865734219551086 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 100 | MOVE_BENCH | SLOWROLL | 89.0 | 6 | 7 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9236778020858765 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 101 | PASS | SLOWROLL | 89.0 | 6 | 7 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 106 | MOVE_BENCH | SLOWROLL | 89.0 | 6 | 13 | 1 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03224129602313042 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 107 | BUY | SLOWROLL | 89.0 | 6 | 13 | 1 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14801377058029175 | 0.0 | 0.0 | +4eedd873-e4ec-41e5-9f5e-48e443e80f86 / -— |
| Jogador 6 | 3-1 | 108 | MOVE_BENCH | SLOWROLL | 89.0 | 6 | 9 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7472272515296936 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 109 | MOVE_BENCH | SLOWROLL | 89.0 | 6 | 9 | 0 | 24.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3003500699996948 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 110 | MOVE_BENCH | SLOWROLL | 89.0 | 6 | 9 | 0 | 24.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21972961723804474 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 111 | MOVE_BENCH | SLOWROLL | 89.0 | 6 | 9 | 0 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7470069527626038 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 112 | PASS | SLOWROLL | 89.0 | 6 | 9 | 0 | 24.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 115 | BUY | SLOWROLL | 89.0 | 6 | 17 | 1 | 24.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43288689851760864 | 0.0 | 0.0 | +6e096b30-0b49-4a98-8596-8b05089793ae / -— |
| Jogador 6 | 3-2 | 116 | MOVE_BENCH | SLOWROLL | 89.0 | 6 | 14 | 1 | 24.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 117 | MOVE_BENCH | SLOWROLL | 89.0 | 6 | 14 | 1 | 24.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8109037280082703 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 118 | PASS | SLOWROLL | 89.0 | 6 | 14 | 1 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 124 | MOVE_BENCH | SLOWROLL | 78.0 | 6 | 20 | 2 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0483885183930397 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 125 | MOVE_BENCH | SLOWROLL | 78.0 | 6 | 20 | 2 | 24.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 126 | PASS | SLOWROLL | 78.0 | 6 | 20 | 2 | 24.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05849999934434891 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 133 | BUY | SLOWROLL | 78.0 | 6 | 28 | 2 | 24.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1246030181646347 | 0.0 | 0.0 | +d056a271-6a74-4e71-bde6-087b97d2c527 / -— |
| Jogador 6 | 3-4 | 134 | MOVE_BENCH | SLOWROLL | 78.0 | 6 | 24 | 2 | 24.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2722124457359314 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 135 | BUY | SLOWROLL | 78.0 | 6 | 24 | 2 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22467944025993347 | 0.0 | 0.0 | +ea7e2f0c-7dec-42c0-86ac-e66997fb2e6c / -— |
| Jogador 6 | 3-4 | 136 | MOVE_BENCH | SLOWROLL | 78.0 | 6 | 21 | 2 | 22.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22050946950912476 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 137 | BUY | SLOWROLL | 78.0 | 6 | 21 | 2 | 24.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.127566859126091 | 0.0 | 0.0 | +2ed895f2-1e83-426c-88fc-b9fb6403835d / -— |
| Jogador 6 | 3-4 | 138 | PASS | SLOWROLL | 78.0 | 6 | 18 | 1 | 24.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057500001043081284 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 142 | BUY | SLOWROLL | 78.0 | 6 | 24 | 2 | 24.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7340108156204224 | 0.0 | 0.0 | +23157bd6-5e8f-4416-bb7f-2e5d71a06543 / -— |
| Jogador 6 | 3-5 | 143 | BUY | SLOWROLL | 78.0 | 6 | 21 | 2 | 24.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5434906482696533 | 0.0 | 0.0 | +8fb80cc8-4120-41a0-bc96-35f81a466ed9 / -2938180d-94e5-4bb7-832e-baa51f820ba2,6e096b30-0b49-4a98-8596-8b05089793ae |
| Jogador 6 | 3-5 | 144 | MOVE_BENCH | SLOWROLL | 78.0 | 6 | 18 | 1 | 18.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5567036867141724 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 145 | BUY | SLOWROLL | 78.0 | 6 | 18 | 1 | 24.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25774601101875305 | 0.0 | 0.0 | +63304cf5-4aa7-473e-9bfb-ec04cd68ebbd / -— |
| Jogador 6 | 3-5 | 146 | PASS | SLOWROLL | 78.0 | 6 | 16 | 1 | 24.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05649999901652336 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 152 | BUY | SLOWROLL | 78.0 | 6 | 24 | 2 | 24.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -4.7752520913491026e-05 | 0.0 | 0.0 | +ed0dab77-fd87-4677-8428-7505ccd34b86 / -— |
| Jogador 6 | 3-6 | 153 | SELL | SLOWROLL | 78.0 | 6 | 21 | 2 | 24.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05732979625463486 | 0.0 | 0.0 | +— / -63304cf5-4aa7-473e-9bfb-ec04cd68ebbd |
| Jogador 6 | 3-6 | 154 | BUY | SLOWROLL | 78.0 | 6 | 23 | 2 | 24.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2867560088634491 | 0.0 | 0.0 | +e0445166-70a5-4135-a45e-ff238a95b228 / -— |
| Jogador 6 | 3-6 | 155 | PASS | SLOWROLL | 78.0 | 6 | 21 | 2 | 24.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 162 | SELL | SLOWROLL | 65.0 | 6 | 28 | 2 | 24.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1589999943971634 | 0.0 | 0.0 | +— / -e0445166-70a5-4135-a45e-ff238a95b228 |
| Jogador 6 | 3-7 | 163 | BUY | SLOWROLL | 65.0 | 6 | 30 | 3 | 24.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13666333258152008 | 0.0 | 0.0 | +1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 / -— |
| Jogador 6 | 3-7 | 164 | SELL | SLOWROLL | 65.0 | 6 | 26 | 2 | 24.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038538459688425064 | 0.0 | 0.0 | +— / -ed0dab77-fd87-4677-8428-7505ccd34b86 |
| Jogador 6 | 3-7 | 165 | BUY | SLOWROLL | 65.0 | 6 | 29 | 2 | 24.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.704867422580719 | 0.0 | 0.0 | +f6de9b7d-1373-459e-b34a-7b878d1a1268 / -— |
| Jogador 6 | 3-7 | 166 | PASS | SLOWROLL | 65.0 | 6 | 26 | 2 | 24.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 172 | SELL | SLOWROLL | 65.0 | 6 | 33 | 3 | 24.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039126746356487274 | 0.0 | 0.0 | +— / -d056a271-6a74-4e71-bde6-087b97d2c527 |
| Jogador 6 | 4-1 | 173 | BUY | SLOWROLL | 65.0 | 6 | 37 | 3 | 24.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2566985785961151 | 0.0 | 0.0 | +7920bf77-c0ba-4906-a82d-6c18bc42f4d9 / -— |
| Jogador 6 | 4-1 | 174 | SELL | SLOWROLL | 65.0 | 6 | 34 | 3 | 24.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.056824691593647 | 0.0 | 0.0 | +— / -7920bf77-c0ba-4906-a82d-6c18bc42f4d9 |
| Jogador 6 | 4-1 | 175 | BUY | SLOWROLL | 65.0 | 6 | 37 | 3 | 24.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11579950153827667 | 0.0 | 0.0 | +0803068a-0141-4e75-ab81-12bb13986025 / -— |
| Jogador 6 | 4-1 | 176 | PASS | SLOWROLL | 65.0 | 6 | 35 | 3 | 24.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 182 | SELL | SLOWROLL | 65.0 | 6 | 44 | 4 | 24.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05730992555618286 | 0.0 | 0.0 | +— / -0803068a-0141-4e75-ab81-12bb13986025 |
| Jogador 6 | 4-2 | 183 | BUY | SLOWROLL | 65.0 | 6 | 46 | 4 | 24.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8389288783073425 | 0.0 | 0.0 | +80c51b33-0a85-4f21-a797-9551aa10760f / -43da0d73-facd-488b-b856-94e9496a97f9,f6de9b7d-1373-459e-b34a-7b878d1a1268 |
| Jogador 6 | 4-2 | 184 | BUY | SLOWROLL | 65.0 | 6 | 43 | 4 | 24.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25169214606285095 | 0.0 | 0.0 | +17d5d3f2-999d-4788-852b-bda84adb4350 / -— |
| Jogador 6 | 4-2 | 185 | BUY | SLOWROLL | 65.0 | 6 | 40 | 4 | 24.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2658863663673401 | 0.0 | 0.0 | +485dab1f-b3a1-4170-8ed6-c0035072ae9b / -— |
| Jogador 6 | 4-2 | 186 | PASS | SLOWROLL | 65.0 | 6 | 37 | 3 | 24.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 192 | SELL | SLOWROLL | 53.0 | 6 | 45 | 4 | 24.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3180138170719147 | 0.0 | 0.0 | +— / -17d5d3f2-999d-4788-852b-bda84adb4350 |
| Jogador 6 | 4-3 | 193 | BUY | SLOWROLL | 53.0 | 6 | 48 | 4 | 24.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24975717067718506 | 0.0 | 0.0 | +a72137b3-498b-40e1-938a-639f56745f08 / -— |
| Jogador 6 | 4-3 | 194 | PASS | SLOWROLL | 53.0 | 6 | 44 | 4 | 24.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 202 | SELL | SLOWROLL | 40.0 | 6 | 54 | 5 | 24.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05098814144730568 | 0.0 | 0.0 | +— / -485dab1f-b3a1-4170-8ed6-c0035072ae9b |
| Jogador 6 | 4-4 | 203 | BUY | SLOWROLL | 40.0 | 6 | 57 | 5 | 24.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8391624689102173 | 0.0 | 0.0 | +6ea982ab-292d-42fc-99e6-d67c89f9f4fe / -— |
| Jogador 6 | 4-4 | 204 | REROLL | SLOWROLL | 40.0 | 6 | 56 | 5 | 24.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26163581013679504 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 205 | SELL | SLOWROLL | 40.0 | 6 | 54 | 5 | 24.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3822989761829376 | 0.0 | 0.0 | +— / -80c51b33-0a85-4f21-a797-9551aa10760f |
| Jogador 6 | 4-4 | 206 | BUY | SLOWROLL | 40.0 | 6 | 62 | 5 | 24.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8202321529388428 | 0.0 | 0.0 | +e60f0b7f-8510-4c67-9ebd-0d8be1b0ff2b / -— |
| Jogador 6 | 4-4 | 207 | SELL | SLOWROLL | 40.0 | 6 | 60 | 5 | 24.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.348815381526947 | 0.0 | 0.0 | +— / -8fb80cc8-4120-41a0-bc96-35f81a466ed9 |
| Jogador 6 | 4-4 | 208 | BUY | SLOWROLL | 40.0 | 6 | 68 | 5 | 24.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2561062276363373 | 0.0 | 0.0 | +bae938fe-6a1c-4cd1-b700-508dd8adcca4 / -— |
| Jogador 6 | 4-4 | 209 | PASS | SLOWROLL | 40.0 | 6 | 66 | 5 | 24.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 212 | SELL | SLOWROLL | 40.0 | 6 | 77 | 5 | 24.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8382716178894043 | 0.0 | 0.0 | +— / -6ea982ab-292d-42fc-99e6-d67c89f9f4fe |
| Jogador 6 | 4-5 | 213 | BUY | SLOWROLL | 40.0 | 6 | 78 | 5 | 24.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.887907087802887 | 0.0 | 0.0 | +ecf369a7-649e-45fe-ad90-8f29e1714fe6 / -23157bd6-5e8f-4416-bb7f-2e5d71a06543,ea7e2f0c-7dec-42c0-86ac-e66997fb2e6c |
| Jogador 6 | 4-5 | 214 | BUY | SLOWROLL | 40.0 | 6 | 75 | 5 | 24.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24769046902656555 | 0.0 | 0.0 | +5416d773-cb2c-442a-8ee9-0d46d22c2087 / -— |
| Jogador 6 | 4-5 | 215 | BUY | SLOWROLL | 40.0 | 6 | 72 | 5 | 24.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1407468318939209 | 0.0 | 0.0 | +5754c4b4-0a7d-49e5-93e4-b144c3090a41 / -— |
| Jogador 6 | 4-5 | 216 | PASS | SLOWROLL | 40.0 | 6 | 70 | 5 | 24.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 222 | SELL | STABILIZE | 27.0 | 6 | 81 | 5 | 24.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.045988328754901886 | 0.0 | 0.0 | +— / -5754c4b4-0a7d-49e5-93e4-b144c3090a41 |
| Jogador 6 | 4-6 | 223 | BUY | STABILIZE | 27.0 | 6 | 83 | 5 | 24.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9523022770881653 | 0.0 | 0.0 | +b701c6c1-2e19-44b9-ad6e-e5d64e1d364c / -7c4fb31e-7de8-491a-bb02-ef0111cd9ede,fee4e511-e40e-4114-a8b6-c2de73117e82 |
| Jogador 6 | 4-6 | 224 | BUY | STABILIZE | 27.0 | 6 | 80 | 5 | 24.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9618698954582214 | 0.0 | 0.0 | +b2566e66-ba8b-4ec9-9875-e08ce45cd7a1 / -0fff7760-179f-4d7c-8267-08d70cb6c1bd,e60f0b7f-8510-4c67-9ebd-0d8be1b0ff2b |
| Jogador 6 | 4-6 | 225 | BUY | STABILIZE | 27.0 | 6 | 78 | 5 | 20.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8642569780349731 | 0.0 | 0.0 | +a5deb295-89d5-4573-8ace-e370a0718266 / -— |
| Jogador 6 | 4-6 | 226 | BUY | STABILIZE | 27.0 | 6 | 76 | 5 | 20.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02494288608431816 | 0.0 | 0.0 | +7a48aa2d-a43b-4e49-8230-77f4f2860cb2 / -— |
| Jogador 6 | 4-6 | 227 | REROLL | STABILIZE | 27.0 | 6 | 73 | 5 | 20.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 228 | SELL | STABILIZE | 27.0 | 6 | 71 | 5 | 20.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04270102456212044 | 0.0 | 0.0 | +— / -7a48aa2d-a43b-4e49-8230-77f4f2860cb2 |
| Jogador 6 | 4-6 | 229 | BUY | STABILIZE | 27.0 | 6 | 74 | 5 | 20.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23839496076107025 | 0.0 | 0.0 | +39b89fbe-9520-4eaa-80f9-81e03232c83c / -— |
| Jogador 6 | 4-6 | 230 | MOVE_BENCH | STABILIZE | 27.0 | 6 | 70 | 5 | 20.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8419157862663269 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 232 | BUY | STABILIZE | 16.0 | 6 | 81 | 5 | 28.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4509055018424988 | 0.0 | 0.0 | +f2dbe099-e518-4261-b120-9f327b112dcb / -— |
| Jogador 6 | 4-7 | 233 | REROLL | STABILIZE | 16.0 | 6 | 79 | 5 | 28.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 234 | SELL | STABILIZE | 16.0 | 6 | 77 | 5 | 28.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060600001364946365 | 0.0 | 0.0 | +— / -5416d773-cb2c-442a-8ee9-0d46d22c2087 |
| Jogador 6 | 4-7 | 235 | BUY | STABILIZE | 16.0 | 6 | 80 | 5 | 28.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42582932114601135 | 0.0 | 0.0 | +8486b8a9-20fe-4234-bbba-0efa031c3b76 / -— |
| Jogador 6 | 4-7 | 236 | SELL | STABILIZE | 16.0 | 6 | 77 | 5 | 28.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06318461894989014 | 0.0 | 0.0 | +— / -39b89fbe-9520-4eaa-80f9-81e03232c83c |
| Jogador 6 | 4-7 | 237 | BUY | STABILIZE | 16.0 | 6 | 81 | 5 | 28.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.008995771408081 | 0.0 | 0.0 | +150a2da3-f559-4a40-a058-005e9c74e11f / -a5deb295-89d5-4573-8ace-e370a0718266,bae938fe-6a1c-4cd1-b700-508dd8adcca4 |
| Jogador 6 | 4-7 | 238 | BUY | STABILIZE | 16.0 | 6 | 79 | 5 | 28.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1692136526107788 | 0.0 | 0.0 | +f087511a-d834-4f41-9b99-00bf0f6dc061 / -— |
| Jogador 6 | 4-7 | 239 | BUY | STABILIZE | 16.0 | 6 | 76 | 5 | 28.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2527599632740021 | 0.0 | 0.0 | +efa7f2f8-94f3-4bcc-9a4e-b5b9e72cc978 / -— |
| Jogador 6 | 4-7 | 240 | REROLL | STABILIZE | 16.0 | 6 | 73 | 5 | 28.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 242 | EQUIP_FROM_INVENTORY | STABILIZE | 16.0 | 7 | 82 | 5 | 28.0 | Colosso/DA_CrimsonRaptor18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 243 | SELL | STABILIZE | 16.0 | 7 | 82 | 5 | 28.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.050867024809122086 | 0.0 | 0.0 | +— / -efa7f2f8-94f3-4bcc-9a4e-b5b9e72cc978 |
| Jogador 6 | 5-1 | 244 | BUY | STABILIZE | 16.0 | 7 | 85 | 5 | 28.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.06719957292079926 | 0.0 | 0.0 | +920ec426-49cf-489f-aad8-3f5461b93be6 / -— |
| Jogador 6 | 5-1 | 245 | SELL | STABILIZE | 16.0 | 7 | 82 | 5 | 28.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05764615535736084 | 0.0 | 0.0 | +— / -920ec426-49cf-489f-aad8-3f5461b93be6 |
| Jogador 6 | 5-1 | 246 | BUY | STABILIZE | 16.0 | 7 | 85 | 5 | 28.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.042407095432281494 | 0.0 | 0.0 | +e89905aa-6564-4e15-bc3a-c281646446bc / -— |
| Jogador 6 | 5-1 | 247 | CRAFT_AND_EQUIP | STABILIZE | 16.0 | 7 | 82 | 5 | 28.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.18652354180812836 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 248 | REROLL | STABILIZE | 16.0 | 7 | 82 | 5 | 28.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 249 | SELL | STABILIZE | 16.0 | 7 | 80 | 5 | 28.0 | Colosso/DA_CrimsonRaptor18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05141563341021538 | 0.0 | 0.0 | +— / -e89905aa-6564-4e15-bc3a-c281646446bc |
| Jogador 6 | 5-1 | 250 | MOVE_BENCH | STABILIZE | 16.0 | 7 | 83 | 5 | 28.0 | Colosso/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5742188096046448 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.026938460767269135 | 0.0 | 0.0 | +— / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987 |
| Jogador 7 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +c2a4318c-af60-41e2-8e14-c3ad967569a0 / -— |
| Jogador 7 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.5990749597549438 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0808350220322609 | 0.0 | 0.0 | +b21d3fc8-71ce-4669-b0ba-931c6e11cb69 / -— |
| Jogador 7 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3300037980079651 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 1.029914379119873 | 0.0 | 0.0 | +a529e9b4-89c2-47e0-b821-7269b112f8ef / -— |
| Jogador 7 | 1-2 | 14 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 18 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12342328578233719 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 20 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.24486127495765686 | 0.0 | 0.0 | +42edb83f-b613-45e2-95e2-d603ddf9d104 / -— |
| Jogador 7 | 1-3 | 21 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21894723176956177 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 22 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 30 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41761514544487 | 0.0 | 0.0 | +— / -42edb83f-b613-45e2-95e2-d603ddf9d104 |
| Jogador 7 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.23228494822978973 | 0.0 | 0.0 | +a179e7d4-31e2-4a74-9905-0daede16517e / -— |
| Jogador 7 | 1-4 | 32 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7172755599021912 | 0.0 | 0.0 | +— / -a179e7d4-31e2-4a74-9905-0daede16517e |
| Jogador 7 | 1-4 | 33 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.27284231781959534 | 0.0 | 0.0 | +29aac672-b25c-44e5-af34-82fd8b0744f6 / -— |
| Jogador 7 | 1-4 | 34 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7149455547332764 | 0.0 | 0.0 | +— / -29aac672-b25c-44e5-af34-82fd8b0744f6 |
| Jogador 7 | 1-4 | 35 | PASS | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 40 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2147928774356842 | 0.0 | 0.0 | +de82e676-8d8b-4437-958e-a8398a3cfade / -— |
| Jogador 7 | 2-1 | 41 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2510315775871277 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 42 | SELL | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8307953476905823 | 0.0 | 0.0 | +— / -b21d3fc8-71ce-4669-b0ba-931c6e11cb69 |
| Jogador 7 | 2-1 | 43 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.16204668581485748 | 0.0 | 0.0 | +42f4384d-5499-4441-aa3b-d37e50926071 / -— |
| Jogador 7 | 2-1 | 44 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7844418883323669 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 45 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7723040580749512 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 46 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.16050855815410614 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 47 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.21499380469322205 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 48 | PASS | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 50 | BUY | STABILIZE | 95.0 | 4 | 11 | 1 | 12.0 | —/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2851749658584595 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 51 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22862887382507324 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 52 | SELL | STABILIZE | 95.0 | 4 | 8 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34069231152534485 | 0.0 | 0.0 | +— / -42f4384d-5499-4441-aa3b-d37e50926071 |
| Jogador 7 | 2-2 | 53 | BUY | STABILIZE | 95.0 | 4 | 10 | 1 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9338709115982056 | 0.0 | 0.0 | +98558a52-389f-46fc-b370-6345603f4103 / -— |
| Jogador 7 | 2-2 | 54 | BUY_XP | STABILIZE | 95.0 | 4 | 9 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 55 | BUY_XP | STABILIZE | 95.0 | 4 | 5 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 56 | PASS | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Hecarim | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 58 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Hecarim | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1192685216665268 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 60 | BUY | STABILIZE | 95.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0369709730148315 | 0.0 | 0.0 | +4367c039-e64e-4a3c-a49f-57cb2674a08f / -— |
| Jogador 7 | 2-3 | 61 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 8.122176950564608e-05 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 62 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3867223560810089 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 63 | SELL | SLOWROLL | 95.0 | 5 | 5 | 0 | 18.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44896891713142395 | 0.0 | 0.0 | +— / -c2a4318c-af60-41e2-8e14-c3ad967569a0 |
| Jogador 7 | 2-3 | 64 | BUY | SLOWROLL | 95.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0459895133972168 | 0.0 | 0.0 | +0547b747-1e37-49ba-a447-67c526a8cd50 / -98558a52-389f-46fc-b370-6345603f4103,a529e9b4-89c2-47e0-b821-7269b112f8ef |
| Jogador 7 | 2-3 | 65 | SELL | SLOWROLL | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_18_RekSai | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47021007537841797 | 0.0 | 0.0 | +— / -0547b747-1e37-49ba-a447-67c526a8cd50 |
| Jogador 7 | 2-3 | 66 | BUY | SLOWROLL | 95.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03722016140818596 | 0.0 | 0.0 | +3ffefe44-52ff-4118-83fb-ae8237b6caa0 / -— |
| Jogador 7 | 2-3 | 67 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5279752016067505 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 68 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19601181149482727 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 70 | BUY | SLOWROLL | 89.0 | 5 | 10 | 1 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17095039784908295 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 71 | MOVE_BENCH | SLOWROLL | 89.0 | 5 | 6 | 0 | 20.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28422781825065613 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 72 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 6 | 0 | 22.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2878808081150055 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 73 | BUY | ECON | 89.0 | 5 | 6 | 0 | 28.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.29579079151153564 | 0.0 | 0.0 | +2c7e844d-925a-43bb-8be8-65a71d11f964 / -— |
| Jogador 7 | 2-4 | 74 | MOVE_BENCH | ECON | 89.0 | 5 | 3 | 0 | 28.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4152223467826843 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 75 | MOVE_BENCH | ECON | 89.0 | 5 | 3 | 0 | 26.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32463276386260986 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 76 | PASS | ECON | 89.0 | 5 | 3 | 0 | 28.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 79 | SELL | ECON | 89.0 | 5 | 8 | 0 | 28.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0784769207239151 | 0.0 | 0.0 | +— / -3ffefe44-52ff-4118-83fb-ae8237b6caa0 |
| Jogador 7 | 2-5 | 80 | BUY | ECON | 89.0 | 5 | 11 | 1 | 28.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.022759249433875084 | 0.0 | 0.0 | +599caeca-96ef-4308-b6cd-f65b005879e2 / -— |
| Jogador 7 | 2-5 | 81 | MOVE_BENCH | SLOWROLL | 89.0 | 5 | 8 | 0 | 28.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8650350570678711 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 82 | MOVE_BENCH | SLOWROLL | 89.0 | 5 | 8 | 0 | 26.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2320071905851364 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 83 | BUY_XP | SLOWROLL | 89.0 | 5 | 8 | 0 | 28.0 | Lutador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 84 | BUY_XP | SLOWROLL | 89.0 | 5 | 4 | 0 | 28.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 85 | PASS | SLOWROLL | 89.0 | 5 | 0 | 0 | 28.0 | Sabugueiro/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 88 | SELL | SLOWROLL | 89.0 | 5 | 6 | 0 | 28.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4454822540283203 | 0.0 | 0.0 | +— / -2c7e844d-925a-43bb-8be8-65a71d11f964 |
| Jogador 7 | 2-6 | 89 | BUY | SLOWROLL | 89.0 | 5 | 9 | 0 | 28.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.28107938170433044 | 0.0 | 0.0 | +6c691ca5-c042-46de-8d64-493514f2d793 / -— |
| Jogador 7 | 2-6 | 90 | BUY_XP | SLOWROLL | 89.0 | 5 | 6 | 0 | 28.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01384000014513731 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 91 | MOVE_BENCH | FAST8 | 89.0 | 6 | 2 | 0 | 28.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5299044847488403 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 92 | MOVE_BENCH | FAST8 | 89.0 | 6 | 2 | 0 | 26.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2756773829460144 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 93 | MOVE_BENCH | FAST8 | 89.0 | 6 | 2 | 0 | 28.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6421398520469666 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 94 | MOVE_BENCH | FAST8 | 89.0 | 6 | 2 | 0 | 28.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.529664933681488 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 95 | MOVE_BENCH | FAST8 | 89.0 | 6 | 2 | 0 | 26.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6466169953346252 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 97 | BUY | FAST8 | 89.0 | 6 | 9 | 0 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.012622657231986523 | 0.0 | 0.0 | +584991bb-37b3-4ac1-8e29-14e0d74c5e78 / -— |
| Jogador 7 | 2-7 | 98 | MOVE_BENCH | FAST8 | 89.0 | 6 | 6 | 0 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30936744809150696 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 99 | MOVE_BENCH | FAST8 | 89.0 | 6 | 6 | 0 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30002206563949585 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 100 | PASS | FAST8 | 89.0 | 6 | 6 | 0 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 106 | MOVE_BENCH | FAST8 | 89.0 | 6 | 12 | 1 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04885123297572136 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 107 | MOVE_BENCH | FAST8 | 89.0 | 6 | 12 | 1 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30920401215553284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 108 | PASS | FAST8 | 89.0 | 6 | 12 | 1 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 115 | MOVE_BENCH | FAST8 | 89.0 | 6 | 20 | 2 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2989388108253479 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 116 | MOVE_BENCH | FAST8 | 89.0 | 6 | 20 | 2 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5275465846061707 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 117 | PASS | FAST8 | 89.0 | 6 | 20 | 2 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05849999934434891 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 124 | MOVE_BENCH | FAST8 | 89.0 | 6 | 29 | 2 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14604084193706512 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 125 | MOVE_BENCH | FAST8 | 89.0 | 6 | 29 | 2 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31438231468200684 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 126 | MOVE_BENCH | FAST8 | 89.0 | 6 | 29 | 2 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47174349427223206 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 127 | PASS | FAST8 | 89.0 | 6 | 29 | 2 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08049999922513962 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 133 | MOVE_BENCH | FAST8 | 80.0 | 6 | 36 | 3 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14604085683822632 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 134 | MOVE_BENCH | FAST8 | 80.0 | 6 | 36 | 3 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31401076912879944 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 135 | MOVE_BENCH | FAST8 | 80.0 | 6 | 36 | 3 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29752597212791443 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 136 | PASS | FAST8 | 80.0 | 6 | 36 | 3 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12600000202655792 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 142 | BUY | FAST8 | 80.0 | 6 | 44 | 4 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8341517448425293 | 0.0 | 0.0 | +27102740-ce4d-4bec-a9eb-ed936f6bc364 / -4367c039-e64e-4a3c-a49f-57cb2674a08f,de82e676-8d8b-4437-958e-a8398a3cfade |
| Jogador 7 | 3-5 | 143 | MOVE_BENCH | FAST8 | 80.0 | 6 | 42 | 4 | 26.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14798754453659058 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 144 | MOVE_BENCH | FAST8 | 80.0 | 6 | 42 | 4 | 28.0 | Sabugueiro/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1457589864730835 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 145 | MOVE_BENCH | FAST8 | 80.0 | 6 | 42 | 4 | 28.0 | Sabugueiro/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8081377148628235 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 146 | MOVE_BENCH | FAST8 | 80.0 | 6 | 42 | 4 | 26.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4418489336967468 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 147 | MOVE_BENCH | FAST8 | 80.0 | 6 | 42 | 4 | 34.0 | Sabugueiro/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13909004628658295 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 148 | MOVE_BENCH | FAST8 | 80.0 | 6 | 42 | 4 | 34.0 | Sabugueiro/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7506943941116333 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 149 | PASS | FAST8 | 80.0 | 6 | 42 | 4 | 34.0 | Sabugueiro/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1289999932050705 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 150 | MOVE_BENCH | FAST8 | 80.0 | 6 | 42 | 4 | 34.0 | Sabugueiro/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5806616544723511 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 152 | BUY | FAST8 | 70.0 | 6 | 52 | 5 | 40.0 | Sabugueiro/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.1091473400592804 | 0.0 | 0.0 | +bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed / -— |
| Jogador 7 | 3-6 | 153 | MOVE_BENCH | FAST8 | 70.0 | 6 | 48 | 4 | 40.0 | Sabugueiro/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05385652557015419 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 154 | MOVE_BENCH | FAST8 | 70.0 | 6 | 48 | 4 | 42.0 | Sabugueiro/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0045728557743132114 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 155 | MOVE_BENCH | FAST8 | 70.0 | 6 | 48 | 4 | 42.0 | Sabugueiro/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3362154960632324 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 156 | MOVE_BENCH | FAST8 | 70.0 | 6 | 48 | 4 | 40.0 | Sabugueiro/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0520097054541111 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 157 | PASS | FAST8 | 70.0 | 6 | 48 | 4 | 42.0 | Sabugueiro/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13199999928474426 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 162 | MOVE_BENCH | FAST8 | 58.0 | 6 | 58 | 5 | 42.0 | Sabugueiro/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2963782846927643 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 163 | MOVE_BENCH | FAST8 | 58.0 | 6 | 58 | 5 | 42.0 | Sabugueiro/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3787354528903961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 164 | PASS | FAST8 | 58.0 | 6 | 58 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15726256370544434 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 172 | MOVE_BENCH | FAST8 | 58.0 | 6 | 69 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2676056921482086 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 173 | MOVE_BENCH | FAST8 | 58.0 | 6 | 69 | 5 | 40.0 | Sabugueiro/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0337296724319458 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 174 | MOVE_BENCH | FAST8 | 58.0 | 6 | 69 | 5 | 42.0 | Sabugueiro/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8081380128860474 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 175 | PASS | FAST8 | 58.0 | 6 | 69 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23206952214241028 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 182 | PASS | FAST8 | 46.0 | 6 | 80 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23994778096675873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 192 | BUY | FAST8 | 46.0 | 6 | 91 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11671069264411926 | 0.0 | 0.0 | +d6a00f0c-4823-44d6-b326-67595876998d / -— |
| Jogador 7 | 4-3 | 193 | PASS | FAST8 | 46.0 | 6 | 87 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24512366950511932 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 202 | BUY | STABILIZE | 35.0 | 6 | 97 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21064673364162445 | 0.0 | 0.0 | +06332ba7-fc4e-431e-ab25-2fb284c08c33 / -— |
| Jogador 7 | 4-4 | 203 | PASS | STABILIZE | 35.0 | 6 | 94 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26817676424980164 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 212 | BUY | STABILIZE | 35.0 | 6 | 104 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0162103176116943 | 0.0 | 0.0 | +0a6546e5-8a3b-461e-ad5d-3dbd49f21e2c / -— |
| Jogador 7 | 4-5 | 213 | REROLL | STABILIZE | 35.0 | 6 | 101 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 214 | BUY | STABILIZE | 35.0 | 6 | 99 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1355276107788086 | 0.0 | 0.0 | +9c01b8f1-0dfb-4dc6-9a26-bb1ebde8cfd9 / -— |
| Jogador 7 | 4-5 | 215 | BUY | STABILIZE | 35.0 | 6 | 97 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20912301540374756 | 0.0 | 0.0 | +e5f38fbd-826a-4067-a33f-86cf7eb98f30 / -— |
| Jogador 7 | 4-5 | 216 | PASS | STABILIZE | 35.0 | 6 | 94 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26817676424980164 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 222 | BUY | STABILIZE | 24.0 | 6 | 105 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7716509699821472 | 0.0 | 0.0 | +4688e6f1-26c5-402d-8d27-0f9bce3a9681 / -— |
| Jogador 7 | 4-6 | 223 | BUY | STABILIZE | 24.0 | 6 | 102 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20769654214382172 | 0.0 | 0.0 | +b3905667-bcb5-4e23-94fa-25160b14a95e / -— |
| Jogador 7 | 4-6 | 224 | PASS | STABILIZE | 24.0 | 6 | 99 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2915530800819397 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 232 | BUY | STABILIZE | 24.0 | 6 | 110 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25816696882247925 | 0.0 | 0.0 | +91eb044c-6989-4b6a-a9fa-a59f75b56743 / -— |
| Jogador 7 | 4-7 | 233 | REROLL | STABILIZE | 24.0 | 6 | 106 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 234 | SELL | STABILIZE | 24.0 | 6 | 104 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017400000244379044 | 0.0 | 0.0 | +— / -9c01b8f1-0dfb-4dc6-9a26-bb1ebde8cfd9 |
| Jogador 7 | 4-7 | 235 | BUY | STABILIZE | 24.0 | 6 | 106 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3824876546859741 | 0.0 | 0.0 | +2b89bd83-8449-4c63-9da2-62a46c68bdf5 / -— |
| Jogador 7 | 4-7 | 236 | REROLL | STABILIZE | 24.0 | 6 | 103 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 237 | REROLL | STABILIZE | 24.0 | 6 | 101 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 238 | REROLL | STABILIZE | 24.0 | 6 | 99 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 239 | SELL | STABILIZE | 24.0 | 6 | 97 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060600001364946365 | 0.0 | 0.0 | +— / -e5f38fbd-826a-4067-a33f-86cf7eb98f30 |
| Jogador 7 | 4-7 | 240 | BUY | STABILIZE | 24.0 | 6 | 100 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32188427448272705 | 0.0 | 0.0 | +864f332a-0446-4995-b7fb-76d48d293501 / -— |
| Jogador 7 | 5-1 | 242 | EQUIP_FROM_INVENTORY | STABILIZE | 24.0 | 6 | 108 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 243 | SELL | STABILIZE | 24.0 | 6 | 108 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.029913626611232758 | 0.0 | 0.0 | +— / -864f332a-0446-4995-b7fb-76d48d293501 |
| Jogador 7 | 5-1 | 244 | BUY | STABILIZE | 24.0 | 6 | 110 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5999693274497986 | 0.0 | 0.0 | +bfe7ca8a-6e89-4673-b142-262e012398a9 / -— |
| Jogador 7 | 5-1 | 245 | REROLL | STABILIZE | 24.0 | 6 | 107 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 246 | SELL | STABILIZE | 24.0 | 6 | 105 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3141692280769348 | 0.0 | 0.0 | +— / -2b89bd83-8449-4c63-9da2-62a46c68bdf5 |
| Jogador 7 | 5-1 | 247 | BUY | STABILIZE | 24.0 | 6 | 108 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.11543505638837814 | 0.0 | 0.0 | +dc423197-9320-4651-b71d-a62086416f9d / -— |
| Jogador 7 | 5-1 | 248 | SELL | STABILIZE | 24.0 | 6 | 105 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.060600001364946365 | 0.0 | 0.0 | +— / -b3905667-bcb5-4e23-94fa-25160b14a95e |
| Jogador 7 | 5-1 | 249 | BUY | STABILIZE | 24.0 | 6 | 108 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.032867077738046646 | 0.0 | 0.0 | +2b10436d-ccfe-4329-aef8-2769899b3787 / -— |
| Jogador 7 | 5-1 | 250 | REROLL | STABILIZE | 24.0 | 6 | 105 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 252 | SELL | ALL_IN | 9.0 | 6 | 113 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03401538357138634 | 0.0 | 0.0 | +— / -2b10436d-ccfe-4329-aef8-2769899b3787 |
| Jogador 7 | 5-2 | 253 | BUY | ALL_IN | 9.0 | 6 | 116 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9248369932174683 | 0.0 | 0.0 | +d1f4a2a4-f3cb-413d-8ed8-b373fa56f1f2 / -— |
| Jogador 7 | 5-2 | 254 | REROLL | ALL_IN | 9.0 | 6 | 113 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 255 | SELL | ALL_IN | 9.0 | 6 | 111 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.032538462430238724 | 0.0 | 0.0 | +— / -dc423197-9320-4651-b71d-a62086416f9d |
| Jogador 7 | 5-2 | 256 | BUY | ALL_IN | 9.0 | 6 | 114 | 5 | 40.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0096006393432617 | 0.0 | 0.0 | +49eaab97-475e-4663-a2b7-61d755bf19ca / -06332ba7-fc4e-431e-ab25-2fb284c08c33,4688e6f1-26c5-402d-8d27-0f9bce3a9681 |
| Jogador 7 | 5-2 | 257 | BUY | ALL_IN | 9.0 | 6 | 111 | 5 | 40.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.09431660920381546 | 0.0 | 0.0 | +52799e57-7b54-4dc5-b7f8-c39c8f57e7fa / -— |
| Jogador 7 | 5-2 | 258 | BUY | ALL_IN | 9.0 | 6 | 109 | 5 | 40.0 | Sabugueiro/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1016542837023735 | 0.0 | 0.0 | +b5e5c8e4-7fb5-4b4b-b284-f0794e78eadc / -— |
| Jogador 7 | 5-2 | 259 | REROLL | ALL_IN | 9.0 | 6 | 107 | 5 | 40.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 260 | SELL | ALL_IN | 9.0 | 6 | 105 | 5 | 40.0 | Sabugueiro/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.019100116565823555 | 0.0 | 0.0 | +— / -52799e57-7b54-4dc5-b7f8-c39c8f57e7fa |
| Jogador 8 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.026938460767269135 | 0.0 | 0.0 | +— / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02 |
| Jogador 8 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +d40a14f6-4b32-4cf9-8eb7-2778414b099a / -— |
| Jogador 8 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.5990749597549438 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.011937879957258701 | 0.0 | 0.0 | +78019889-2624-4adb-917b-619681f23053 / -— |
| Jogador 8 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29970690608024597 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 1.0161010026931763 | 0.0 | 0.0 | +fddba3f3-87f3-4c97-a7b2-e5d1ef789709 / -— |
| Jogador 8 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 15 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8103029727935791 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 16 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 18 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4447084665298462 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 20 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2786955237388611 | 0.0 | 0.0 | +f449cb2d-2ec7-4bf0-8f3a-80f82e1e7d26 / -— |
| Jogador 8 | 1-3 | 21 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 30 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.429995596408844 | 0.0 | 0.0 | +— / -f449cb2d-2ec7-4bf0-8f3a-80f82e1e7d26 |
| Jogador 8 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1163243055343628 | 0.0 | 0.0 | +64f24363-3325-4538-972e-a6d8260b3787 / -78019889-2624-4adb-917b-619681f23053,fddba3f3-87f3-4c97-a7b2-e5d1ef789709 |
| Jogador 8 | 1-4 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 4 | 0 | 2.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39223045110702515 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 33 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.10612095892429352 | 0.0 | 0.0 | +65a4f434-f421-47ab-ae23-86ad8971518d / -— |
| Jogador 8 | 1-4 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4037308990955353 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 35 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 38 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5116502046585083 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 40 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.39312225580215454 | 0.0 | 0.0 | +630d9254-3856-4d88-b981-43a8270b4b3d / -— |
| Jogador 8 | 2-1 | 41 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012479945085942745 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 42 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5534167289733887 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 43 | PASS | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 50 | BUY | STABILIZE | 100.0 | 4 | 12 | 1 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0391709804534912 | 0.0 | 0.0 | +fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 / -— |
| Jogador 8 | 2-2 | 51 | BUY_XP | STABILIZE | 100.0 | 4 | 11 | 1 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 52 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 53 | MOVE_BOARD | SLOWROLL | 100.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03994898498058319 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 54 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05724026635289192 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 55 | MOVE_BOARD | SLOWROLL | 100.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 56 | MOVE_BOARD | SLOWROLL | 100.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18198171257972717 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 57 | PASS | SLOWROLL | 100.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 58 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 3 | 0 | 10.0 | —/DA_18_Leona | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10082154721021652 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 60 | BUY | SLOWROLL | 100.0 | 5 | 10 | 1 | 12.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.0888855829834938 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 61 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 7 | 0 | 12.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.400534987449646 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 62 | SELL | SLOWROLL | 100.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8688457608222961 | 0.0 | 0.0 | +— / -fa7ba406-b2bf-4dbb-8c80-7b56d69bb9b8 |
| Jogador 8 | 2-3 | 63 | BUY | SLOWROLL | 100.0 | 5 | 8 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08151858299970627 | 0.0 | 0.0 | +5de56114-806a-4f58-8241-b3b8434a2154 / -— |
| Jogador 8 | 2-3 | 64 | MOVE_BOARD | SLOWROLL | 100.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1695864498615265 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 65 | MOVE_BOARD | SLOWROLL | 100.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3285244405269623 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 66 | PASS | SLOWROLL | 100.0 | 5 | 6 | 0 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 70 | SELL | SLOWROLL | 100.0 | 5 | 13 | 1 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7022307515144348 | 0.0 | 0.0 | +— / -5de56114-806a-4f58-8241-b3b8434a2154 |
| Jogador 8 | 2-4 | 71 | BUY | SLOWROLL | 100.0 | 5 | 15 | 1 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1687069684267044 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 8 | 2-4 | 72 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 12 | 1 | 16.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33130282163619995 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 73 | BUY_XP | SLOWROLL | 100.0 | 5 | 12 | 1 | 18.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1379999965429306 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 74 | BUY_XP | SLOWROLL | 100.0 | 5 | 8 | 0 | 18.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 75 | BUY_XP | SLOWROLL | 100.0 | 5 | 4 | 0 | 18.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 76 | PASS | SLOWROLL | 100.0 | 5 | 0 | 0 | 18.0 | —/DA_18_Leona | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 79 | SELL | SLOWROLL | 100.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Leona | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4949338734149933 | 0.0 | 0.0 | +— / -64f24363-3325-4538-972e-a6d8260b3787 |
| Jogador 8 | 2-5 | 80 | BUY | STABILIZE | 100.0 | 5 | 9 | 0 | 18.0 | Adaptador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.394919753074646 | 0.0 | 0.0 | +cf4575c2-3622-4493-91f1-c5efbe1fbd8b / -— |
| Jogador 8 | 2-5 | 81 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 18.0 | Adaptador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16625721752643585 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 82 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 16.0 | Adaptador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32454296946525574 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 83 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 16.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7508281469345093 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 84 | SELL | STABILIZE | 100.0 | 5 | 7 | 0 | 18.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5063538551330566 | 0.0 | 0.0 | +— / -cf4575c2-3622-4493-91f1-c5efbe1fbd8b |
| Jogador 8 | 2-5 | 85 | BUY | STABILIZE | 100.0 | 5 | 9 | 0 | 18.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3854134976863861 | 0.0 | 0.0 | +35e1a0f6-207d-4df2-b096-fc07962d094a / -— |
| Jogador 8 | 2-5 | 86 | BUY_XP | STABILIZE | 100.0 | 5 | 7 | 0 | 18.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028404999524354935 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 88 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 8 | 0 | 18.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7142435908317566 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 89 | BUY | STABILIZE | 93.0 | 6 | 8 | 0 | 22.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.15660227835178375 | 0.0 | 0.0 | +87600495-fe90-4832-ab42-9a5cb0ebe3f4 / -— |
| Jogador 8 | 2-6 | 90 | MOVE_BENCH | STABILIZE | 93.0 | 6 | 4 | 0 | 22.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4904605746269226 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 91 | BUY_XP | FAST8 | 93.0 | 6 | 4 | 0 | 26.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 92 | PASS | FAST8 | 93.0 | 6 | 0 | 0 | 26.0 | Adaptador/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 97 | SELL | FAST8 | 87.0 | 6 | 6 | 0 | 26.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4502573311328888 | 0.0 | 0.0 | +— / -35e1a0f6-207d-4df2-b096-fc07962d094a |
| Jogador 8 | 2-7 | 98 | BUY | FAST8 | 87.0 | 6 | 8 | 0 | 26.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9977603554725647 | 0.0 | 0.0 | +f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 / -— |
| Jogador 8 | 2-7 | 99 | BUY_XP | FAST8 | 87.0 | 6 | 7 | 0 | 26.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 100 | PASS | FAST8 | 87.0 | 6 | 3 | 0 | 26.0 | Adaptador/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 106 | SELL | FAST8 | 87.0 | 6 | 9 | 0 | 26.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.1425498723983765 | 0.0 | 0.0 | +— / -f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 |
| Jogador 8 | 3-1 | 107 | BUY | FAST8 | 87.0 | 6 | 10 | 1 | 26.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.07549059391021729 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 108 | MOVE_BENCH | FAST8 | 87.0 | 6 | 6 | 0 | 26.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18415772914886475 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 109 | MOVE_BENCH | FAST8 | 87.0 | 6 | 6 | 0 | 26.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5030381083488464 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 110 | PASS | FAST8 | 87.0 | 6 | 6 | 0 | 28.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 115 | MOVE_BENCH | FAST8 | 77.0 | 6 | 12 | 1 | 28.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.045164793729782104 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 116 | MOVE_BENCH | FAST8 | 77.0 | 6 | 12 | 1 | 26.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10258432477712631 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 117 | SELL | FAST8 | 77.0 | 6 | 12 | 1 | 28.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020999999716877937 | 0.0 | 0.0 | +— / -b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 8 | 3-2 | 118 | BUY | FAST8 | 77.0 | 6 | 15 | 1 | 28.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06931766867637634 | 0.0 | 0.0 | +4ac49c80-f0c3-47ae-a031-96928d244e13 / -— |
| Jogador 8 | 3-2 | 119 | MOVE_BENCH | FAST8 | 77.0 | 6 | 11 | 1 | 28.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6291664838790894 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 120 | MOVE_BENCH | FAST8 | 77.0 | 6 | 11 | 1 | 30.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.192640021443367 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 121 | MOVE_BENCH | FAST8 | 77.0 | 6 | 11 | 1 | 28.0 | Adaptador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4183535873889923 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 122 | MOVE_BENCH | FAST8 | 77.0 | 6 | 11 | 1 | 28.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6283462047576904 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 124 | MOVE_BENCH | FAST8 | 67.0 | 6 | 18 | 1 | 30.0 | Adaptador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19276055693626404 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 125 | MOVE_BENCH | FAST8 | 67.0 | 6 | 18 | 1 | 28.0 | Adaptador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35877928137779236 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 126 | MOVE_BENCH | FAST8 | 67.0 | 6 | 18 | 1 | 28.0 | Adaptador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34936484694480896 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 127 | PASS | FAST8 | 67.0 | 6 | 18 | 1 | 30.0 | Adaptador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057500001043081284 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 133 | MOVE_BENCH | FAST8 | 67.0 | 6 | 25 | 2 | 30.0 | Adaptador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09445741027593613 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 134 | MOVE_BENCH | FAST8 | 67.0 | 6 | 25 | 2 | 28.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5137034058570862 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 135 | MOVE_BENCH | FAST8 | 67.0 | 6 | 25 | 2 | 28.0 | Adaptador/DA_Brambleback18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34936636686325073 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 136 | PASS | FAST8 | 67.0 | 6 | 25 | 2 | 30.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07850000262260437 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 142 | MOVE_BENCH | FAST8 | 67.0 | 6 | 32 | 3 | 30.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09445834904909134 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 143 | MOVE_BENCH | FAST8 | 67.0 | 6 | 32 | 3 | 28.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32193523645401 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 144 | MOVE_BENCH | FAST8 | 67.0 | 6 | 32 | 3 | 28.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5014572143554688 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 145 | PASS | FAST8 | 67.0 | 6 | 32 | 3 | 30.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12399999797344208 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 152 | MOVE_BENCH | FAST8 | 56.0 | 6 | 40 | 4 | 30.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.045522164553403854 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 153 | MOVE_BENCH | FAST8 | 56.0 | 6 | 40 | 4 | 28.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18257607519626617 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 154 | MOVE_BENCH | FAST8 | 56.0 | 6 | 40 | 4 | 28.0 | Adaptador/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5014442205429077 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 155 | PASS | FAST8 | 56.0 | 6 | 40 | 4 | 30.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12800000607967377 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 162 | MOVE_BENCH | FAST8 | 44.0 | 6 | 50 | 5 | 30.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04563170671463013 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 163 | MOVE_BENCH | FAST8 | 44.0 | 6 | 50 | 5 | 28.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3278159201145172 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 164 | BUY_XP | FAST8 | 44.0 | 6 | 50 | 5 | 34.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07855000346899033 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 165 | BUY_XP | FAST8 | 44.0 | 6 | 46 | 4 | 34.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11102499812841415 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 166 | MOVE_BENCH | FAST8 | 44.0 | 7 | 42 | 4 | 34.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4793608784675598 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 167 | BUY | FAST8 | 44.0 | 7 | 42 | 4 | 36.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08035583794116974 | 0.0 | 0.0 | +cc56fedc-f555-4075-af15-6b5fb93a156f / -— |
| Jogador 8 | 3-7 | 168 | BUY_XP | FAST8 | 44.0 | 7 | 39 | 3 | 36.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003275000024586916 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 169 | BUY_XP | FAST8 | 44.0 | 7 | 35 | 3 | 36.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003275000024586916 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 170 | BUY_XP | FAST8 | 44.0 | 7 | 31 | 3 | 36.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08327499777078629 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 172 | MOVE_BENCH | FAST8 | 44.0 | 7 | 35 | 3 | 36.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.49767184257507324 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 173 | MOVE_BENCH | FAST8 | 44.0 | 7 | 35 | 3 | 36.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0418890081346035 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 174 | BUY | FAST8 | 44.0 | 7 | 35 | 3 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.13626325130462646 | 0.0 | 0.0 | +cb30dcaa-bc26-4584-9b50-24e47e70fcb0 / -— |
| Jogador 8 | 4-1 | 175 | PASS | FAST8 | 44.0 | 7 | 32 | 3 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.17844656109809875 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 182 | BUY | FAST8 | 44.0 | 7 | 41 | 4 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2338014841079712 | 0.0 | 0.0 | +3c2cff2e-669c-4ef6-ad78-1fe93a7b2a58 / -— |
| Jogador 8 | 4-2 | 183 | PASS | FAST8 | 44.0 | 7 | 39 | 3 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.1838613748550415 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 192 | BUY | FAST8 | 44.0 | 7 | 50 | 5 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8207331895828247 | 0.0 | 0.0 | +262702a6-b710-4129-9dc6-0c1a04514ff9 / -— |
| Jogador 8 | 4-3 | 193 | PASS | FAST8 | 44.0 | 7 | 46 | 4 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.18892063200473785 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 202 | BUY | FAST8 | 44.0 | 7 | 56 | 5 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.02904598042368889 | 0.0 | 0.0 | +b9b38183-663e-43a4-9f9d-02f1bd4d2d24 / -— |
| Jogador 8 | 4-4 | 203 | PASS | FAST8 | 44.0 | 7 | 53 | 5 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2233622819185257 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 212 | BUY | FAST8 | 44.0 | 7 | 64 | 5 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.37803488969802856 | 0.0 | 0.0 | +18d25cfb-d559-4efa-b708-c9987987590b / -— |
| Jogador 8 | 4-5 | 213 | BUY | FAST8 | 44.0 | 7 | 61 | 5 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.012878970243036747 | 0.0 | 0.0 | +d381c462-a17f-4192-b694-66a7c3aaee4f / -— |
| Jogador 8 | 4-5 | 214 | PASS | FAST8 | 44.0 | 7 | 58 | 5 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.22643858194351196 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 222 | BUY | FAST8 | 44.0 | 7 | 70 | 5 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7717819809913635 | 0.0 | 0.0 | +5e843c10-0a8b-4781-983a-8e6e6f28253e / -— |
| Jogador 8 | 4-6 | 223 | BUY | FAST8 | 44.0 | 7 | 67 | 5 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.005465921014547348 | 0.0 | 0.0 | +9a96b07c-5b37-4be7-855e-dc2d942e7171 / -— |
| Jogador 8 | 4-6 | 224 | REROLL | FAST8 | 44.0 | 7 | 65 | 5 | 40.0 | Adaptador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 225 | SELL | FAST8 | 44.0 | 7 | 63 | 5 | 40.0 | Adaptador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05026153847575188 | 0.0 | 0.0 | +— / -65a4f434-f421-47ab-ae23-86ad8971518d |
| Jogador 8 | 4-6 | 226 | BUY | FAST8 | 44.0 | 7 | 64 | 5 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8144307732582092 | 0.0 | 0.0 | +d22aa2b7-7c7c-4d47-89be-0f1b8755971c / -— |
| Jogador 8 | 4-6 | 227 | SELL | FAST8 | 44.0 | 7 | 61 | 5 | 40.0 | Adaptador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04361538589000702 | 0.0 | 0.0 | +— / -d381c462-a17f-4192-b694-66a7c3aaee4f |
| Jogador 8 | 4-6 | 228 | BUY | FAST8 | 44.0 | 7 | 64 | 5 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.565248966217041 | 0.0 | 0.0 | +22f3c707-2635-41cb-a228-10d5ed1883b3 / -— |
| Jogador 8 | 4-6 | 229 | REROLL | FAST8 | 44.0 | 7 | 61 | 5 | 40.0 | Adaptador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 230 | SELL | FAST8 | 44.0 | 7 | 59 | 5 | 40.0 | Adaptador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.35478460788726807 | 0.0 | 0.0 | +— / -cb30dcaa-bc26-4584-9b50-24e47e70fcb0 |
| Jogador 8 | 4-7 | 232 | BUY | STABILIZE | 31.0 | 7 | 72 | 5 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9550144672393799 | 0.0 | 0.0 | +95a2e19e-619f-4497-ba52-e9bbf06b364f / -5e843c10-0a8b-4781-983a-8e6e6f28253e,b9b38183-663e-43a4-9f9d-02f1bd4d2d24 |
| Jogador 8 | 4-7 | 233 | BUY | STABILIZE | 31.0 | 7 | 69 | 5 | 40.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.24626578390598297 | 0.0 | 0.0 | +babdcded-7f64-4c88-a087-ff2e10b58b8d / -— |
| Jogador 8 | 4-7 | 234 | BUY | STABILIZE | 31.0 | 7 | 66 | 5 | 40.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.18056778609752655 | 0.0 | 0.0 | +0e5921d4-a056-4f42-951e-93de5f2834bb / -— |
| Jogador 8 | 4-7 | 235 | REROLL | STABILIZE | 31.0 | 7 | 63 | 5 | 40.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 236 | SELL | STABILIZE | 31.0 | 7 | 61 | 5 | 40.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.060600001364946365 | 0.0 | 0.0 | +— / -0e5921d4-a056-4f42-951e-93de5f2834bb |
| Jogador 8 | 4-7 | 237 | BUY | STABILIZE | 31.0 | 7 | 64 | 5 | 40.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.36969441175460815 | 0.0 | 0.0 | +01c587bb-ca4f-4690-9e4b-d1e9c44fd33e / -— |
| Jogador 8 | 4-7 | 238 | REROLL | STABILIZE | 31.0 | 7 | 61 | 5 | 40.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 239 | SELL | STABILIZE | 31.0 | 7 | 59 | 5 | 40.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.07500000298023224 | 0.0 | 0.0 | +— / -babdcded-7f64-4c88-a087-ff2e10b58b8d |
| Jogador 8 | 4-7 | 240 | BUY | STABILIZE | 31.0 | 7 | 62 | 5 | 40.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.16696913540363312 | 0.0 | 0.0 | +3c46b699-2b56-48d0-820c-b523c5153b9f / -— |
| Jogador 8 | 5-1 | 242 | EQUIP_FROM_INVENTORY | STABILIZE | 31.0 | 7 | 69 | 5 | 40.0 | Adaptador/DA_18_Diana | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 243 | SELL | STABILIZE | 31.0 | 7 | 69 | 5 | 40.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.032538462430238724 | 0.0 | 0.0 | +— / -22f3c707-2635-41cb-a228-10d5ed1883b3 |
| Jogador 8 | 5-1 | 244 | BUY | STABILIZE | 31.0 | 7 | 72 | 5 | 40.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0197237730026245 | 0.0 | 0.0 | +e7c18780-1d70-4a15-ad72-2eaa0f81df8d / -5f2c89f5-15c2-4a77-943e-4ba5492d925b,d22aa2b7-7c7c-4d47-89be-0f1b8755971c |
| Jogador 8 | 5-1 | 245 | BUY | STABILIZE | 31.0 | 7 | 69 | 5 | 34.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1698920726776123 | 0.0 | 0.0 | +63c47a3f-6712-4cfa-9376-6140da170089 / -— |
| Jogador 8 | 5-1 | 246 | REROLL | STABILIZE | 31.0 | 7 | 67 | 5 | 34.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 247 | SELL | STABILIZE | 31.0 | 7 | 65 | 5 | 34.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0298309363424778 | 0.0 | 0.0 | +— / -63c47a3f-6712-4cfa-9376-6140da170089 |
| Jogador 8 | 5-1 | 248 | BUY | STABILIZE | 31.0 | 7 | 67 | 5 | 34.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9223747849464417 | 0.0 | 0.0 | +ae9da355-52b7-402c-be6e-41fa1148a550 / -— |
| Jogador 8 | 5-1 | 249 | CRAFT_AND_EQUIP | STABILIZE | 31.0 | 7 | 64 | 5 | 34.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.14150597155094147 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 250 | MOVE_BENCH | STABILIZE | 31.0 | 7 | 64 | 5 | 34.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6641340255737305 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 252 | BUY | STABILIZE | 31.0 | 7 | 75 | 5 | 40.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.188410222530365 | 0.0 | 0.0 | +14c1ca8a-e057-4184-9c83-0b8846824932 / -— |
| Jogador 8 | 5-2 | 253 | REROLL | STABILIZE | 31.0 | 7 | 71 | 5 | 40.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 254 | SELL | STABILIZE | 31.0 | 7 | 69 | 5 | 40.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06318461894989014 | 0.0 | 0.0 | +— / -14c1ca8a-e057-4184-9c83-0b8846824932 |
| Jogador 8 | 5-2 | 255 | BUY | STABILIZE | 31.0 | 7 | 73 | 5 | 40.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09362367540597916 | 0.0 | 0.0 | +25029b69-ee52-4788-840e-006ff9e57d5d / -— |
| Jogador 8 | 5-2 | 256 | REROLL | STABILIZE | 31.0 | 7 | 70 | 5 | 40.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 257 | REROLL | STABILIZE | 31.0 | 7 | 68 | 5 | 40.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 258 | REROLL | STABILIZE | 31.0 | 7 | 66 | 5 | 40.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 259 | SELL | STABILIZE | 31.0 | 7 | 64 | 5 | 40.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04361538589000702 | 0.0 | 0.0 | +— / -25029b69-ee52-4788-840e-006ff9e57d5d |
| Jogador 8 | 5-2 | 260 | BUY | STABILIZE | 31.0 | 7 | 67 | 5 | 40.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7341803908348083 | 0.0 | 0.0 | +e99948bb-f38f-41e0-b1c4-1864c35ffe14 / -— |
| Jogador 8 | 5-3 | 262 | SELL | ALL_IN | 15.0 | 7 | 74 | 5 | 40.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44544416666030884 | 0.0 | 0.0 | +— / -95a2e19e-619f-4497-ba52-e9bbf06b364f |
| Jogador 8 | 5-3 | 263 | BUY | ALL_IN | 15.0 | 7 | 82 | 5 | 40.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42654141783714294 | 0.0 | 0.0 | +e15f057a-185e-4f99-8417-2c2b059912af / -— |
| Jogador 8 | 5-3 | 264 | REROLL | ALL_IN | 15.0 | 7 | 79 | 5 | 40.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 265 | SELL | ALL_IN | 15.0 | 7 | 77 | 5 | 40.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48061683773994446 | 0.0 | 0.0 | +— / -e7c18780-1d70-4a15-ad72-2eaa0f81df8d |
| Jogador 8 | 5-3 | 266 | BUY | ALL_IN | 15.0 | 7 | 85 | 5 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9054162502288818 | 0.0 | 0.0 | +84250843-db6c-4e91-9c6f-b12e36fc31cb / -— |
| Jogador 8 | 5-3 | 267 | REROLL | ALL_IN | 15.0 | 7 | 83 | 5 | 40.0 | Adaptador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 268 | SELL | ALL_IN | 15.0 | 7 | 81 | 5 | 40.0 | Adaptador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3588295876979828 | 0.0 | 0.0 | +— / -01c587bb-ca4f-4690-9e4b-d1e9c44fd33e |
| Jogador 8 | 5-3 | 269 | BUY | ALL_IN | 15.0 | 7 | 84 | 5 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0094220638275146 | 0.0 | 0.0 | +5594beb6-a447-4be2-a6e0-ae5c4f94fe70 / -3c46b699-2b56-48d0-820c-b523c5153b9f,e99948bb-f38f-41e0-b1c4-1864c35ffe14 |
| Jogador 8 | 5-3 | 270 | BUY | ALL_IN | 15.0 | 7 | 81 | 5 | 40.0 | Adaptador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2296553999185562 | 0.0 | 0.0 | +86aa0b8f-5eb2-483d-ab0f-033bebb928e3 / -— |
| Jogador 8 | 5-4 | 272 | BUY | ALL_IN | 15.0 | 7 | 88 | 5 | 40.0 | Adaptador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10044132173061371 | 0.0 | 0.0 | +8ac322bc-799c-4d78-a2d5-e76b64ce900f / -— |
| Jogador 8 | 5-4 | 273 | REROLL | ALL_IN | 15.0 | 7 | 85 | 5 | 40.0 | Adaptador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 274 | SELL | ALL_IN | 15.0 | 7 | 83 | 5 | 40.0 | Adaptador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07500000298023224 | 0.0 | 0.0 | +— / -86aa0b8f-5eb2-483d-ab0f-033bebb928e3 |
| Jogador 8 | 5-4 | 275 | BUY | ALL_IN | 15.0 | 7 | 86 | 5 | 40.0 | Adaptador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9332889914512634 | 0.0 | 0.0 | +0ba913e1-85ac-49ec-b800-33f13e98bc32 / -— |
| Jogador 8 | 5-4 | 276 | REROLL | ALL_IN | 15.0 | 7 | 83 | 5 | 40.0 | Adaptador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 277 | REROLL | ALL_IN | 15.0 | 7 | 81 | 5 | 40.0 | Adaptador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 278 | SELL | ALL_IN | 15.0 | 7 | 79 | 5 | 40.0 | Adaptador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48032063245773315 | 0.0 | 0.0 | +— / -5594beb6-a447-4be2-a6e0-ae5c4f94fe70 |
| Jogador 8 | 5-4 | 279 | EQUIP_FROM_INVENTORY | ALL_IN | 15.0 | 7 | 87 | 5 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.1100265383720398 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 280 | BUY | ALL_IN | 15.0 | 7 | 87 | 5 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8977946639060974 | 0.0 | 0.0 | +62214a63-ba6e-4230-8f21-741b36c6dae8 / -— |
| Jogador 8 | 5-5 | 282 | SELL | ALL_IN | 15.0 | 7 | 94 | 5 | 40.0 | Adaptador/DA_18_Soraka | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3588150143623352 | 0.0 | 0.0 | +— / -8ac322bc-799c-4d78-a2d5-e76b64ce900f |
| Jogador 8 | 5-5 | 283 | EQUIP_FROM_INVENTORY | ALL_IN | 15.0 | 7 | 97 | 5 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13693363964557648 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 284 | BUY | ALL_IN | 15.0 | 7 | 97 | 5 | 40.0 | Adaptador/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0097969770431519 | 0.0 | 0.0 | +fab5a72a-5696-4c10-941f-eb51daf0f5c9 / -3c2cff2e-669c-4ef6-ad78-1fe93a7b2a58,84250843-db6c-4e91-9c6f-b12e36fc31cb |
| Jogador 8 | 5-5 | 285 | BUY | ALL_IN | 15.0 | 7 | 95 | 5 | 40.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06737369298934937 | 0.0 | 0.0 | +b899f6f0-495e-490e-a4c5-3c81f7d7c739 / -— |
| Jogador 8 | 5-5 | 286 | BUY | ALL_IN | 15.0 | 7 | 92 | 5 | 40.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15289416909217834 | 0.0 | 0.0 | +74205da7-b8ab-42d1-8f02-e8b6ae31a33d / -— |
| Jogador 8 | 5-5 | 287 | REROLL | ALL_IN | 15.0 | 7 | 90 | 5 | 40.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 288 | REROLL | ALL_IN | 15.0 | 7 | 88 | 5 | 40.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 289 | REROLL | ALL_IN | 15.0 | 7 | 86 | 5 | 40.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 290 | REROLL | ALL_IN | 15.0 | 7 | 84 | 5 | 40.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 292 | REROLL | ALL_IN | 15.0 | 7 | 92 | 5 | 40.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 293 | SELL | ALL_IN | 15.0 | 7 | 90 | 5 | 40.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04134950786828995 | 0.0 | 0.0 | +— / -74205da7-b8ab-42d1-8f02-e8b6ae31a33d |
| Jogador 8 | 5-6 | 294 | BUY | ALL_IN | 15.0 | 7 | 92 | 5 | 40.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17066939175128937 | 0.0 | 0.0 | +0650ed76-f3bb-4dce-bd04-2ed294039e6d / -— |
| Jogador 8 | 5-6 | 295 | REROLL | ALL_IN | 15.0 | 7 | 87 | 5 | 40.0 | Adaptador/DA_18_Lux_Inferno | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 296 | SELL | ALL_IN | 15.0 | 7 | 85 | 5 | 40.0 | Adaptador/DA_18_Lux_Inferno | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04361538589000702 | 0.0 | 0.0 | +— / -b899f6f0-495e-490e-a4c5-3c81f7d7c739 |
| Jogador 8 | 5-6 | 297 | BUY | ALL_IN | 15.0 | 7 | 88 | 5 | 40.0 | Adaptador/DA_18_Lux_Inferno | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9412860870361328 | 0.0 | 0.0 | +a0ec2c92-3f53-42b7-b3ff-2f5018e3ae7e / -— |
| Jogador 8 | 5-6 | 298 | REROLL | ALL_IN | 15.0 | 7 | 87 | 5 | 40.0 | Adaptador/DA_18_Lux_Inferno | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09000000357627869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 299 | SELL | ALL_IN | 15.0 | 7 | 85 | 5 | 40.0 | Adaptador/DA_18_Lux_Inferno | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49507057666778564 | 0.0 | 0.0 | +— / -fab5a72a-5696-4c10-941f-eb51daf0f5c9 |
| Jogador 8 | 5-6 | 300 | BUY | ALL_IN | 15.0 | 7 | 90 | 5 | 40.0 | Adaptador/DA_18_Lux_Inferno | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0098837614059448 | 0.0 | 0.0 | +559d1b79-d4c7-470c-912e-fe30541195ec / -262702a6-b710-4129-9dc6-0c1a04514ff9,87600495-fe90-4832-ab42-9a5cb0ebe3f4 |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 123 | 122 | 42 | 8 | 1 | 0 | 14 | 0 | 69 | 26.0 |
- Jogador 1 — gasto por ação: BUY: 86g, BUY_XP: 8g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 28g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 7g, stage 2: 39g, stage 3: 56g, stage 4: 20g
| Jogador 2 | 223 | 293 | 131 | 19 | 17 | 1 | 13 | 0 | 125 | 48.0 |
- Jogador 2 — gasto por ação: BUY: 187g, BUY_XP: 80g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 26g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 8g, stage 2: 39g, stage 3: 72g, stage 4: 25g, stage 5: 61g, stage 6: 88g
| Jogador 3 | 160 | 204 | 54 | 20 | 17 | 0 | 2 | 0 | 22 | 58.0 |
- Jogador 3 — gasto por ação: BUY: 120g, BUY_XP: 80g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 4g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 5g, stage 2: 48g, stage 3: 61g, stage 4: 37g, stage 5: 53g
| Jogador 4 | 205 | 296 | 119 | 19 | 16 | 3 | 11 | 0 | 119 | 48.0 |
- Jogador 4 — gasto por ação: BUY: 190g, BUY_XP: 84g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 22g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 11g, stage 2: 40g, stage 3: 43g, stage 4: 35g, stage 5: 69g, stage 6: 98g
| Jogador 5 | 194 | 246 | 116 | 12 | 7 | 1 | 18 | 0 | 82 | 44.0 |
- Jogador 5 — gasto por ação: BUY: 178g, BUY_XP: 32g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 36g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 7g, stage 2: 54g, stage 3: 17g, stage 4: 94g, stage 5: 74g
| Jogador 6 | 148 | 163 | 72 | 8 | 3 | 2 | 5 | 0 | 83 | 32.0 |
- Jogador 6 — gasto por ação: BUY: 129g, BUY_XP: 24g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 10g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 10g, stage 2: 42g, stage 3: 37g, stage 4: 66g, stage 5: 8g
| Jogador 7 | 146 | 131 | 40 | 5 | 3 | 1 | 9 | 0 | 107 | 40.0 |
- Jogador 7 — gasto por ação: BUY: 93g, BUY_XP: 20g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 18g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 8g, stage 2: 50g, stage 3: 6g, stage 4: 40g, stage 5: 27g
| Jogador 8 | 187 | 229 | 84 | 9 | 10 | 2 | 21 | 0 | 86 | 32.0 |
- Jogador 8 — gasto por ação: BUY: 135g, BUY_XP: 52g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 42g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 6g, stage 2: 51g, stage 3: 31g, stage 4: 52g, stage 5: 89g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 1 | 1 | 0 | 0.0% |
| Jogador 2 | 1 | 1 | 0 | 0.0% |
| Jogador 3 | 1 | 1 | 0 | 0.0% |
| Jogador 4 | 1 | 1 | 0 | 0.0% |
| Jogador 5 | 2 | 2 | 0 | 0.0% |
| Jogador 6 | 1 | 1 | 0 | 0.0% |
| Jogador 7 | 2 | 2 | 0 | 0.0% |
| Jogador 8 | 1 | 1 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ médio qualidade | Estrutural médio | Δ estrutural médio | Posicional médio | Δ qualidade combate + | Δ qualidade combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 123 | 22 | 23 | 78 | -0.0034 | -0.3634 | -0.0057 | 0.3250 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ -0.0333 (39 ações), BUY_XP: Δ 0.0000 (2 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0238 (26 ações), MOVE_BOARD: Δ -0.0733 (3 ações), PASS: Δ 0.0000 (15 ações), REROLL: Δ 0.0000 (14 ações), SELL: Δ 0.0209 (23 ações)
| Jogador 2 | 223 | 27 | 36 | 160 | -0.0020 | -0.4417 | -0.0034 | 0.3334 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ -0.0044 (66 ações), BUY_XP: Δ 0.0000 (20 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ -0.0108 (47 ações), MOVE_BOARD: Δ -0.0191 (6 ações), PASS: Δ 0.0000 (27 ações), REROLL: Δ 0.0000 (13 ações), SELL: Δ 0.0120 (40 ações)
| Jogador 3 | 160 | 22 | 26 | 112 | -0.0007 | -0.4102 | -0.0027 | 0.3261 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ -0.0128 (44 ações), BUY_XP: Δ 0.0000 (20 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0174 (42 ações), MOVE_BOARD: Δ -0.0475 (7 ações), PASS: Δ 0.0000 (25 ações), REROLL: Δ 0.0000 (2 ações), SELL: Δ 0.0032 (19 ações)
| Jogador 4 | 205 | 24 | 24 | 157 | 0.0028 | -0.1570 | 0.0005 | 0.3605 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ -0.0130 (59 ações), BUY_XP: Δ 0.0000 (21 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (5 ações), MOVE_BENCH: Δ 0.0371 (34 ações), MOVE_BOARD: Δ -0.0038 (10 ações), PASS: Δ 0.0000 (29 ações), REROLL: Δ 0.0000 (11 ações), SELL: Δ 0.0034 (35 ações)
| Jogador 5 | 194 | 21 | 22 | 151 | 0.0033 | -0.0983 | 0.0006 | 0.4093 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ -0.0104 (63 ações), BUY_XP: Δ 0.0000 (8 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0322 (40 ações), MOVE_BOARD: Δ -0.0997 (3 ações), PASS: Δ 0.0000 (19 ações), REROLL: Δ 0.0000 (18 ações), SELL: Δ 0.0071 (42 ações)
| Jogador 6 | 148 | 16 | 24 | 108 | -0.0015 | -0.4592 | -0.0032 | 0.3098 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ -0.0201 (53 ações), BUY_XP: Δ 0.0000 (6 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0303 (27 ações), MOVE_BOARD: Δ -0.0312 (5 ações), PASS: Δ 0.0000 (22 ações), REROLL: Δ 0.0000 (5 ações), SELL: Δ 0.0064 (28 ações)
| Jogador 7 | 146 | 27 | 31 | 88 | -0.0046 | -0.7439 | -0.0063 | 0.2910 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ 0.0001 (37 ações), BUY_XP: Δ 0.0000 (5 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ -0.0125 (51 ações), MOVE_BOARD: Δ -0.1116 (3 ações), PASS: Δ 0.0000 (22 ações), REROLL: Δ 0.0000 (9 ações), SELL: Δ 0.0167 (18 ações)
| Jogador 8 | 187 | 25 | 25 | 137 | -0.0042 | -0.9086 | -0.0056 | 0.2416 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ -0.0139 (52 ações), BUY_XP: Δ 0.0000 (13 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0089 (44 ações), MOVE_BOARD: Δ -0.1355 (6 ações), PASS: Δ 0.0000 (20 ações), REROLL: Δ 0.0000 (21 ações), SELL: Δ 0.0133 (27 ações)

A pontuação é uma heurística para auditoria, não uma verdade absoluta. Compare-a com recompensas e resultados de combate; correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 142 | OK (142) | 0 | 1 | 0 | 0 | 1 | 0 |
- Jogador 1 — IDs equipados observados: TFT_Item_IonicSpark; eventos: COMPONENT_LOOT_GRANTED: 16.
| Jogador 2 | 260 | OK (260) | 0 | 2 | 0 | 1 | 2 | 1 |
- Jogador 2 — IDs equipados observados: TFT_Item_BlueBuff, TFT_Item_IonicSpark; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 2, COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
| Jogador 3 | 190 | OK (190) | 0 | 0 | 0 | 3 | 0 | 0 |
- Jogador 3 — IDs equipados observados: nenhum observado; eventos: COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
| Jogador 4 | 243 | OK (243) | 2 | 0 | 0 | 1 | 2 | 2 |
- Jogador 4 — IDs equipados observados: TFT_Item_Deathblade, TFT_Item_Redemption; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 2, COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
| Jogador 5 | 223 | OK (223) | 0 | 0 | 0 | 3 | 0 | 0 |
- Jogador 5 — IDs equipados observados: nenhum observado; eventos: COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
| Jogador 6 | 173 | OK (173) | 0 | 1 | 0 | 1 | 1 | 0 |
- Jogador 6 — IDs equipados observados: TFT_Item_Quicksilver; eventos: COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
| Jogador 7 | 172 | OK (172) | 0 | 0 | 0 | 3 | 0 | 0 |
- Jogador 7 — IDs equipados observados: nenhum observado; eventos: COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
| Jogador 8 | 217 | OK (217) | 1 | 0 | 0 | 1 | 1 | 1 |
- Jogador 8 — IDs equipados observados: TFT_Item_IonicSpark; eventos: COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.056 | 0.000 |
| Jogador 1 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.001 | 0.000 |
| Jogador 1 | 1-3 | 4 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.036 | 0.000 |
| Jogador 1 | 1-4 | 7 | 0.000 | -4.000 | 0 → 0 | 1 → 1 | 11% → 11% | 3 → 9 | 2 | 3 → 4 | 0.009 | 0.000 |
| Jogador 1 | 2-1 | 7 | 4.000 | 2.000 | 0 → 0 | 1 → 1 | 11% → 14% | 9 → 7 | 7 | 4 → 4 | 0.011 | -0.323 |
| Jogador 1 | 2-2 | 7 | 2.000 | 6.000 | 0 → 0 | 1 → 2 | 14% → 14% | 7 → 9 | 5 | 4 → 4 | -0.031 | -0.377 |
| Jogador 1 | 2-3 | 10 | 4.000 | -4.000 | 0 → 0 | 2 → 1 | 14% → 18% | 9 → 11 | 10 | 4 → 5 | 0.023 | -0.248 |
| Jogador 1 | 2-4 | 7 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 18% → 18% | 11 → 14 | 5 | 5 → 5 | 0.000 | 0.000 |
| Jogador 1 | 2-5 | 6 | 2.000 | 8.000 | 0 → 0 | 1 → 1 | 18% → 18% | 14 → 15 | 5 | 5 → 5 | -0.101 | -0.422 |
| Jogador 1 | 2-6 | 7 | 0.000 | 8.000 | 0 → 0 | 1 → 3 | 18% → 18% | 15 → 19 | 4 | 5 → 5 | 0.001 | -0.377 |
| Jogador 1 | 2-7 | 4 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 18% → 18% | 19 → 24 | 3 | 5 → 5 | 0.000 | 0.000 |
| Jogador 1 | 3-1 | 3 | 0.000 | 4.000 | 0 → 0 | 3 → 4 | 18% → 18% | 24 → 32 | 2 | 5 → 5 | 0.000 | -0.925 |
| Jogador 1 | 3-2 | 6 | 0.000 | 6.000 | 0 → 0 | 4 → 4 | 18% → 18% | 32 → 39 | 7 | 5 → 5 | 0.000 | -0.463 |
| Jogador 1 | 3-3 | 6 | 0.000 | 2.000 | 0 → 0 | 4 → 5 | 18% → 18% | 39 → 49 | 5 | 5 → 5 | 0.000 | -0.439 |
| Jogador 1 | 3-4 | 9 | 0.000 | 6.000 | 0 → 0 | 5 → 5 | 18% → 18% | 49 → 49 | 13 | 5 → 6 | 0.000 | 0.000 |
| Jogador 1 | 3-5 | 9 | 8.000 | -6.000 | 0 → 0 | 5 → 5 | 18% → 21% | 49 → 60 | 2 | 6 → 6 | 0.033 | -0.308 |
| Jogador 1 | 3-6 | 10 | -2.000 | 10.000 | 0 → 0 | 5 → 5 | 21% → 21% | 60 → 63 | 13 | 6 → 6 | 0.027 | -0.268 |
| Jogador 1 | 3-7 | 10 | 0.000 | -4.000 | 0 → 0 | 5 → 4 | 21% → 21% | 63 → 74 | 14 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 4-1 | 8 | 2.000 | 4.000 | 0 → 0 | 4 → 3 | 21% → 21% | 74 → 81 | 6 | 6 → 6 | -0.085 | -0.328 |
| Jogador 1 | 4-2 | 10 | -26.000 | -54.000 | 0 → 0 | 3 → 0 | 21% → 0% | 81 → 69 | 14 | 6 → 6 | 0.042 | -0.293 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 7, COMPOSITION_COMPATIBILITY: 21, IMMEDIATE_UPGRADE: 1, PAIR_POTENTIAL: 10; mudanças de composição: 0; posicionamento melhorou em 23 ações e piorou em 23.
- Jogador 1 — estado final: ouro 69, nível 6, vida 6.0, colocação None.
| Jogador 2 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.056 | 0.000 |
| Jogador 2 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.001 | 0.000 |
| Jogador 2 | 1-3 | 4 | 2.000 | 2.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.022 | 0.000 |
| Jogador 2 | 1-4 | 6 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 3 → 7 | 3 | 3 → 4 | -0.010 | 0.000 |
| Jogador 2 | 2-1 | 8 | 6.000 | -2.000 | 0 → 0 | 1 → 1 | 11% → 14% | 7 → 10 | 3 | 4 → 4 | -0.014 | -0.296 |
| Jogador 2 | 2-2 | 6 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 10 → 6 | 10 | 4 → 5 | -0.007 | 0.467 |
| Jogador 2 | 2-3 | 5 | 2.000 | 4.000 | 0 → 0 | 1 → 1 | 18% → 18% | 6 → 10 | 3 | 5 → 5 | 0.001 | 0.527 |
| Jogador 2 | 2-4 | 5 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 18% → 18% | 10 → 13 | 3 | 5 → 5 | 0.000 | 0.000 |
| Jogador 2 | 2-5 | 3 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 18% → 18% | 13 → 18 | 3 | 5 → 5 | -0.020 | 0.879 |
| Jogador 2 | 2-6 | 8 | 0.000 | -12.000 | 0 → 0 | 1 → 2 | 18% → 18% | 18 → 33 | 2 | 5 → 5 | 0.007 | 0.317 |
| Jogador 2 | 2-7 | 9 | 6.000 | -4.000 | 0 → 0 | 2 → 1 | 18% → 21% | 33 → 28 | 15 | 5 → 6 | 0.026 | 0.000 |
| Jogador 2 | 3-1 | 9 | 0.000 | 6.000 | 0 → 1 | 1 → 0 | 21% → 18% | 28 → 31 | 4 | 6 → 6 | 0.013 | -0.293 |
| Jogador 2 | 3-2 | 9 | 4.000 | -6.000 | 1 → 0 | 0 → 0 | 18% → 21% | 31 → 24 | 17 | 6 → 6 | -0.004 | 0.312 |
| Jogador 2 | 3-3 | 5 | 4.000 | 4.000 | 0 → 0 | 0 → 0 | 21% → 21% | 24 → 29 | 4 | 6 → 6 | -0.009 | 0.562 |
| Jogador 2 | 3-4 | 8 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 21% → 25% | 29 → 22 | 14 | 6 → 7 | -0.001 | 0.000 |
| Jogador 2 | 3-5 | 7 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 25% → 25% | 22 → 10 | 19 | 7 → 7 | 0.000 | 0.421 |
| Jogador 2 | 3-6 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 25% → 25% | 10 → 15 | 2 | 7 → 7 | -0.008 | 0.587 |
| Jogador 2 | 3-7 | 5 | 0.000 | 8.000 | 0 → 0 | 1 → 1 | 25% → 25% | 15 → 9 | 12 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 4-1 | 4 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 25% → 25% | 9 → 7 | 7 | 7 → 7 | 0.000 | -0.696 |
| Jogador 2 | 4-2 | 5 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 25% → 25% | 7 → 6 | 7 | 7 → 7 | -0.012 | 0.570 |
| Jogador 2 | 4-3 | 3 | 0.000 | 4.000 | 0 → 0 | 2 → 3 | 25% → 25% | 6 → 11 | 2 | 7 → 7 | -0.020 | 1.012 |
| Jogador 2 | 4-4 | 4 | 0.000 | 6.000 | 0 → 0 | 3 → 2 | 25% → 25% | 11 → 11 | 6 | 7 → 7 | -0.030 | 0.000 |
| Jogador 2 | 4-5 | 3 | 0.000 | 4.000 | 0 → 0 | 2 → 2 | 25% → 25% | 11 → 15 | 2 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 4-6 | 4 | 0.000 | -2.000 | 0 → 0 | 2 → 2 | 25% → 25% | 15 → 23 | 1 | 7 → 7 | 0.015 | 0.000 |
| Jogador 2 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 23 → 31 | 0 | 7 → 8 | 0.000 | 0.000 |
| Jogador 2 | 5-1 | 10 | 2.000 | 12.000 | 0 → 0 | 2 → 4 | 25% → 29% | 31 → 31 | 13 | 8 → 8 | -0.003 | 0.299 |
| Jogador 2 | 5-2 | 9 | 14.000 | -12.000 | 0 → 2 | 4 → 1 | 29% → 29% | 31 → 34 | 9 | 8 → 8 | -0.047 | 0.325 |
| Jogador 2 | 5-3 | 7 | 0.000 | 16.000 | 2 → 2 | 1 → 2 | 29% → 29% | 34 → 36 | 8 | 8 → 8 | -0.000 | 0.417 |
| Jogador 2 | 5-4 | 10 | 2.000 | -2.000 | 2 → 2 | 2 → 1 | 29% → 29% | 36 → 46 | 7 | 8 → 8 | -0.022 | 0.000 |
| Jogador 2 | 5-5 | 10 | 0.000 | 0.000 | 2 → 2 | 1 → 1 | 29% → 29% | 46 → 59 | 8 | 8 → 8 | -0.001 | 0.292 |
| Jogador 2 | 5-6 | 5 | -6.000 | 6.000 | 2 → 1 | 1 → 1 | 29% → 29% | 59 → 73 | 0 | 8 → 8 | -0.061 | 0.594 |
| Jogador 2 | 5-7 | 10 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 29% → 29% | 73 → 84 | 16 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 6-1 | 10 | 0.000 | -4.000 | 1 → 1 | 1 → 2 | 29% → 29% | 84 → 94 | 12 | 8 → 8 | 0.000 | -0.280 |
| Jogador 2 | 6-2 | 10 | 0.000 | -12.000 | 1 → 1 | 2 → 3 | 29% → 29% | 94 → 107 | 13 | 8 → 8 | 0.000 | -0.280 |
| Jogador 2 | 6-3 | 10 | 0.000 | 10.000 | 1 → 1 | 3 → 3 | 29% → 29% | 107 → 108 | 18 | 8 → 8 | -0.006 | -0.275 |
| Jogador 2 | 6-4 | 10 | 0.000 | -10.000 | 1 → 1 | 3 → 4 | 29% → 29% | 108 → 121 | 12 | 8 → 8 | 0.006 | 0.000 |
| Jogador 2 | 6-5 | 10 | 0.000 | 8.000 | 1 → 1 | 4 → 4 | 29% → 29% | 121 → 124 | 19 | 8 → 8 | 0.000 | -0.290 |
| Jogador 2 | 6-6 | 10 | -50.000 | -58.000 | 1 → 0 | 4 → 0 | 29% → 0% | 124 → 125 | 14 | 8 → 8 | 0.080 | -0.285 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 18, COMPOSITION_COMPATIBILITY: 23, IMMEDIATE_UPGRADE: 6, PAIR_POTENTIAL: 19; mudanças de composição: 0; posicionamento melhorou em 28 ações e piorou em 37.
- Jogador 2 — estado final: ouro 125, nível 8, vida 6.0, colocação None.
| Jogador 3 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.056 | 0.000 |
| Jogador 3 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.001 | 0.000 |
| Jogador 3 | 1-3 | 3 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 3 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 3 → 7 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 3 | 2-1 | 6 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 14% | 7 → 11 | 2 | 4 → 4 | -0.036 | 0.397 |
| Jogador 3 | 2-2 | 7 | 2.000 | -2.000 | 0 → 0 | 1 → 2 | 14% → 14% | 11 → 17 | 2 | 4 → 4 | 0.016 | -0.354 |
| Jogador 3 | 2-3 | 10 | 6.000 | -2.000 | 0 → 0 | 2 → 1 | 14% → 18% | 17 → 13 | 13 | 4 → 5 | -0.005 | 0.246 |
| Jogador 3 | 2-4 | 9 | 8.000 | 0.000 | 0 → 0 | 1 → 0 | 18% → 18% | 13 → 10 | 11 | 5 → 5 | 0.040 | 0.000 |
| Jogador 3 | 2-5 | 6 | 0.000 | 10.000 | 0 → 0 | 0 → 1 | 18% → 18% | 10 → 8 | 9 | 5 → 5 | -0.010 | 0.467 |
| Jogador 3 | 2-6 | 8 | 4.000 | -4.000 | 0 → 1 | 1 → 0 | 18% → 18% | 8 → 11 | 2 | 5 → 5 | -0.087 | -0.297 |
| Jogador 3 | 2-7 | 9 | 6.000 | -6.000 | 1 → 1 | 0 → 0 | 18% → 21% | 11 → 12 | 9 | 5 → 6 | -0.022 | 0.000 |
| Jogador 3 | 3-1 | 5 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 21% → 21% | 12 → 7 | 11 | 6 → 6 | 0.000 | 0.580 |
| Jogador 3 | 3-2 | 3 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 21% → 21% | 7 → 10 | 4 | 6 → 6 | 0.000 | 0.983 |
| Jogador 3 | 3-3 | 9 | -2.000 | 0.000 | 1 → 1 | 0 → 0 | 21% → 21% | 10 → 10 | 13 | 6 → 6 | 0.010 | 0.322 |
| Jogador 3 | 3-4 | 9 | 6.000 | -6.000 | 1 → 1 | 0 → 0 | 21% → 25% | 10 → 8 | 11 | 6 → 7 | -0.003 | 0.000 |
| Jogador 3 | 3-5 | 5 | 0.000 | 6.000 | 1 → 1 | 0 → 1 | 25% → 25% | 8 → 8 | 7 | 7 → 7 | 0.003 | 0.562 |
| Jogador 3 | 3-6 | 4 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 8 → 16 | 0 | 7 → 7 | 0.147 | 0.728 |
| Jogador 3 | 3-7 | 10 | 6.000 | -6.000 | 1 → 2 | 1 → 0 | 25% → 25% | 16 → 8 | 15 | 7 → 7 | -0.060 | 0.000 |
| Jogador 3 | 4-1 | 5 | 0.000 | 6.000 | 2 → 2 | 0 → 0 | 25% → 25% | 8 → 10 | 7 | 7 → 7 | 0.003 | 0.587 |
| Jogador 3 | 4-2 | 4 | 0.000 | 6.000 | 2 → 2 | 0 → 1 | 25% → 25% | 10 → 8 | 7 | 7 → 7 | 0.000 | -0.700 |
| Jogador 3 | 4-3 | 4 | 0.000 | 6.000 | 2 → 2 | 1 → 1 | 25% → 25% | 8 → 7 | 7 | 7 → 7 | 0.000 | 0.713 |
| Jogador 3 | 4-4 | 3 | 0.000 | 0.000 | 2 → 2 | 1 → 1 | 25% → 25% | 7 → 8 | 4 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 4-5 | 3 | 0.000 | 6.000 | 2 → 2 | 1 → 2 | 25% → 25% | 8 → 10 | 3 | 7 → 7 | 0.000 | -0.905 |
| Jogador 3 | 4-6 | 3 | 0.000 | 6.000 | 2 → 2 | 2 → 2 | 25% → 25% | 10 → 13 | 3 | 7 → 7 | 0.000 | -0.933 |
| Jogador 3 | 4-7 | 7 | 8.000 | -8.000 | 2 → 3 | 2 → 0 | 25% → 25% | 13 → 13 | 6 | 7 → 8 | -0.020 | 0.000 |
| Jogador 3 | 5-1 | 8 | 4.000 | 6.000 | 3 → 3 | 0 → 0 | 25% → 29% | 13 → 14 | 5 | 8 → 8 | 0.081 | 0.365 |
| Jogador 3 | 5-2 | 5 | 0.000 | 16.000 | 3 → 3 | 0 → 1 | 29% → 29% | 14 → 11 | 8 | 8 → 8 | 0.000 | -0.550 |
| Jogador 3 | 5-3 | 4 | 0.000 | 14.000 | 3 → 3 | 1 → 1 | 29% → 29% | 11 → 10 | 7 | 8 → 8 | 0.000 | -0.688 |
| Jogador 3 | 5-4 | 6 | 0.000 | 0.000 | 3 → 3 | 1 → 2 | 29% → 29% | 10 → 17 | 2 | 8 → 8 | -0.037 | 0.000 |
| Jogador 3 | 5-5 | 10 | 0.000 | -6.000 | 3 → 3 | 2 → 2 | 29% → 29% | 17 → 25 | 14 | 8 → 8 | 0.000 | -0.275 |
| Jogador 3 | 5-6 | 10 | -58.000 | -52.000 | 3 → 0 | 2 → 0 | 29% → 0% | 25 → 22 | 17 | 8 → 8 | 0.011 | -0.280 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 9, COMPOSITION_COMPATIBILITY: 20, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 10; mudanças de composição: 0; posicionamento melhorou em 23 ações e piorou em 26.
- Jogador 3 — estado final: ouro 22, nível 8, vida 2.0, colocação None.
| Jogador 4 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.056 | 0.000 |
| Jogador 4 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.011 | 0.000 |
| Jogador 4 | 1-3 | 3 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.020 | 0.000 |
| Jogador 4 | 1-4 | 8 | 2.000 | -4.000 | 0 → 0 | 0 → 1 | 11% → 14% | 3 → 4 | 6 | 3 → 4 | -0.001 | 0.000 |
| Jogador 4 | 2-1 | 3 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 14% → 14% | 4 → 9 | 1 | 4 → 4 | 0.000 | 0.793 |
| Jogador 4 | 2-2 | 7 | 6.000 | -2.000 | 0 → 0 | 2 → 1 | 14% → 18% | 9 → 10 | 7 | 4 → 5 | -0.005 | 0.401 |
| Jogador 4 | 2-3 | 9 | 6.000 | 0.000 | 0 → 1 | 1 → 0 | 18% → 18% | 10 → 11 | 4 | 5 → 5 | -0.111 | -0.270 |
| Jogador 4 | 2-4 | 9 | 6.000 | 4.000 | 1 → 1 | 0 → 0 | 18% → 18% | 11 → 7 | 10 | 5 → 5 | 0.093 | 0.000 |
| Jogador 4 | 2-5 | 6 | 0.000 | 2.000 | 1 → 1 | 0 → 0 | 18% → 18% | 7 → 12 | 3 | 5 → 5 | -0.018 | -0.422 |
| Jogador 4 | 2-6 | 9 | 6.000 | -6.000 | 1 → 1 | 0 → 0 | 18% → 21% | 12 → 10 | 8 | 5 → 6 | 0.038 | 0.312 |
| Jogador 4 | 2-7 | 5 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 21% → 21% | 10 → 8 | 7 | 6 → 6 | 0.001 | 0.000 |
| Jogador 4 | 3-1 | 6 | 0.000 | -2.000 | 1 → 1 | 0 → 0 | 21% → 21% | 8 → 6 | 10 | 6 → 6 | 0.000 | -0.454 |
| Jogador 4 | 3-2 | 3 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 21% → 21% | 6 → 8 | 4 | 6 → 6 | 0.000 | -0.878 |
| Jogador 4 | 3-3 | 6 | 0.000 | -2.000 | 1 → 1 | 0 → 0 | 21% → 21% | 8 → 7 | 9 | 6 → 6 | 0.000 | -0.439 |
| Jogador 4 | 3-4 | 7 | 6.000 | -2.000 | 1 → 1 | 0 → 1 | 21% → 25% | 7 → 7 | 7 | 6 → 7 | 0.019 | 0.000 |
| Jogador 4 | 3-5 | 6 | 6.000 | 0.000 | 1 → 2 | 1 → 0 | 25% → 25% | 7 → 7 | 6 | 7 → 7 | -0.028 | 0.492 |
| Jogador 4 | 3-6 | 4 | 0.000 | 6.000 | 2 → 2 | 0 → 0 | 25% → 25% | 7 → 7 | 7 | 7 → 7 | 0.000 | 0.746 |
| Jogador 4 | 3-7 | 3 | 0.000 | 0.000 | 2 → 2 | 0 → 0 | 25% → 25% | 7 → 13 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 4-1 | 3 | 0.000 | 0.000 | 2 → 2 | 0 → 0 | 25% → 25% | 13 → 21 | 0 | 7 → 7 | 0.000 | 0.978 |
| Jogador 4 | 4-2 | 7 | 0.000 | 0.000 | 2 → 2 | 0 → 0 | 25% → 25% | 21 → 8 | 20 | 7 → 7 | 0.000 | 0.423 |
| Jogador 4 | 4-3 | 2 | 0.000 | 0.000 | 2 → 2 | 0 → 0 | 25% → 25% | 8 → 16 | 0 | 7 → 7 | 0.000 | 1.506 |
| Jogador 4 | 4-4 | 2 | 0.000 | 0.000 | 2 → 2 | 0 → 0 | 25% → 25% | 16 → 24 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 4 | 4-5 | 2 | 0.000 | 0.000 | 2 → 2 | 0 → 0 | 25% → 25% | 24 → 35 | 0 | 7 → 7 | 0.000 | 1.506 |
| Jogador 4 | 4-6 | 2 | 0.000 | 0.000 | 2 → 2 | 0 → 0 | 25% → 25% | 35 → 47 | 0 | 7 → 7 | 0.000 | 1.481 |
| Jogador 4 | 4-7 | 7 | 6.000 | 0.000 | 2 → 2 | 0 → 1 | 25% → 29% | 47 → 43 | 15 | 7 → 8 | -0.005 | 0.000 |
| Jogador 4 | 5-1 | 6 | 0.000 | 12.000 | 2 → 2 | 1 → 1 | 29% → 29% | 43 → 45 | 6 | 8 → 8 | 0.000 | -0.458 |
| Jogador 4 | 5-2 | 4 | 0.000 | 16.000 | 2 → 2 | 1 → 1 | 29% → 29% | 45 → 46 | 8 | 8 → 8 | 0.000 | 0.755 |
| Jogador 4 | 5-3 | 4 | 0.000 | 16.000 | 2 → 2 | 1 → 1 | 29% → 29% | 46 → 48 | 8 | 8 → 8 | 0.000 | 0.721 |
| Jogador 4 | 5-4 | 10 | -8.000 | 16.000 | 2 → 2 | 1 → 1 | 29% → 25% | 48 → 47 | 17 | 8 → 8 | 0.021 | 0.000 |
| Jogador 4 | 5-5 | 8 | 0.000 | 12.000 | 2 → 1 | 1 → 3 | 25% → 29% | 47 → 50 | 8 | 8 → 8 | -0.094 | 0.371 |
| Jogador 4 | 5-6 | 10 | 6.000 | -12.000 | 1 → 2 | 3 → 3 | 29% → 29% | 50 → 61 | 12 | 8 → 8 | 0.102 | 0.305 |
| Jogador 4 | 5-7 | 10 | -6.000 | 14.000 | 2 → 1 | 3 → 3 | 29% → 29% | 61 → 66 | 10 | 8 → 8 | -0.102 | 0.000 |
| Jogador 4 | 6-1 | 10 | 6.000 | -12.000 | 1 → 2 | 3 → 3 | 29% → 29% | 66 → 82 | 9 | 8 → 8 | 0.102 | 0.297 |
| Jogador 4 | 6-2 | 10 | 0.000 | 10.000 | 2 → 2 | 3 → 3 | 29% → 29% | 82 → 87 | 20 | 8 → 8 | 0.000 | 0.297 |
| Jogador 4 | 6-3 | 10 | 0.000 | 2.000 | 2 → 2 | 3 → 3 | 29% → 29% | 87 → 98 | 18 | 8 → 8 | 0.000 | 0.292 |
| Jogador 4 | 6-4 | 10 | 0.000 | 0.000 | 2 → 2 | 3 → 4 | 29% → 29% | 98 → 109 | 19 | 8 → 8 | 0.000 | 0.000 |
| Jogador 4 | 6-5 | 10 | 0.000 | -2.000 | 2 → 2 | 4 → 3 | 29% → 29% | 109 → 121 | 14 | 8 → 8 | 0.000 | 0.309 |
| Jogador 4 | 6-6 | 10 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 29% → 29% | 121 → 120 | 18 | 8 → 8 | 0.000 | 0.305 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 19, COMPOSITION_COMPATIBILITY: 24, IMMEDIATE_UPGRADE: 4, PAIR_POTENTIAL: 12; mudanças de composição: 0; posicionamento melhorou em 24 ações e piorou em 24.
- Jogador 4 — estado final: ouro 120, nível 8, vida 41.0, colocação 1.
| Jogador 5 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.056 | 0.000 |
| Jogador 5 | 1-2 | 4 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.066 | 0.000 |
| Jogador 5 | 1-3 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.059 | 0.000 |
| Jogador 5 | 1-4 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.000 | 0.000 |
| Jogador 5 | 2-1 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 5 → 9 | 5 | 4 → 4 | 0.025 | 0.419 |
| Jogador 5 | 2-2 | 8 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 9 → 8 | 10 | 4 → 4 | 0.000 | -0.303 |
| Jogador 5 | 2-3 | 9 | 2.000 | -6.000 | 0 → 0 | 0 → 0 | 14% → 18% | 8 → 8 | 10 | 4 → 5 | -0.004 | -0.258 |
| Jogador 5 | 2-4 | 5 | 2.000 | 4.000 | 0 → 0 | 0 → 0 | 18% → 18% | 8 → 11 | 3 | 5 → 5 | 0.000 | 0.000 |
| Jogador 5 | 2-5 | 9 | 0.000 | 2.000 | 0 → 0 | 0 → 0 | 18% → 18% | 11 → 8 | 12 | 5 → 6 | 0.000 | -0.276 |
| Jogador 5 | 2-6 | 7 | 6.000 | -6.000 | 0 → 0 | 0 → 0 | 18% → 21% | 8 → 14 | 0 | 6 → 6 | -0.007 | -0.332 |
| Jogador 5 | 2-7 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 21% → 21% | 14 → 6 | 14 | 6 → 6 | -0.010 | 0.000 |
| Jogador 5 | 3-1 | 5 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 21% → 21% | 6 → 9 | 3 | 6 → 6 | -0.054 | 0.562 |
| Jogador 5 | 3-2 | 6 | 4.000 | -2.000 | 0 → 0 | 0 → 1 | 21% → 21% | 9 → 15 | 3 | 6 → 6 | -0.118 | 0.469 |
| Jogador 5 | 3-3 | 8 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 21% → 21% | 15 → 19 | 3 | 6 → 6 | 0.088 | -0.341 |
| Jogador 5 | 3-4 | 6 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 19 → 25 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 3-5 | 5 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 21% → 21% | 25 → 30 | 3 | 6 → 6 | -0.141 | -0.545 |
| Jogador 5 | 3-6 | 9 | 0.000 | 4.000 | 0 → 0 | 2 → 2 | 21% → 21% | 30 → 36 | 2 | 6 → 6 | 0.128 | 0.318 |
| Jogador 5 | 3-7 | 3 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 21% → 21% | 36 → 41 | 3 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-1 | 4 | 0.000 | 12.000 | 0 → 0 | 2 → 2 | 21% → 21% | 41 → 43 | 6 | 6 → 6 | 0.000 | -0.708 |
| Jogador 5 | 4-2 | 10 | 0.000 | 14.000 | 0 → 0 | 2 → 3 | 21% → 21% | 43 → 39 | 17 | 6 → 6 | 0.000 | -0.268 |
| Jogador 5 | 4-3 | 10 | 0.000 | -2.000 | 0 → 0 | 3 → 4 | 21% → 21% | 39 → 43 | 13 | 6 → 7 | 0.000 | -0.288 |
| Jogador 5 | 4-4 | 10 | 6.000 | -16.000 | 0 → 0 | 4 → 5 | 21% → 25% | 43 → 56 | 10 | 7 → 7 | -0.004 | 0.000 |
| Jogador 5 | 4-5 | 10 | 0.000 | 12.000 | 0 → 0 | 5 → 6 | 25% → 25% | 56 → 56 | 17 | 7 → 7 | 0.000 | 0.288 |
| Jogador 5 | 4-6 | 10 | 0.000 | 8.000 | 0 → 0 | 6 → 6 | 25% → 25% | 56 → 59 | 18 | 7 → 7 | 0.000 | 0.286 |
| Jogador 5 | 4-7 | 10 | -2.000 | 0.000 | 0 → 0 | 6 → 4 | 25% → 21% | 59 → 63 | 13 | 7 → 7 | 0.003 | 0.000 |
| Jogador 5 | 5-1 | 10 | 6.000 | -6.000 | 0 → 0 | 4 → 4 | 21% → 25% | 63 → 72 | 11 | 7 → 7 | 0.005 | 0.000 |
| Jogador 5 | 5-2 | 10 | 0.000 | 16.000 | 0 → 0 | 4 → 5 | 25% → 25% | 72 → 74 | 19 | 7 → 7 | 0.000 | 0.302 |
| Jogador 5 | 5-3 | 10 | 0.000 | -4.000 | 0 → 0 | 5 → 5 | 25% → 25% | 74 → 86 | 16 | 7 → 7 | 0.006 | -0.273 |
| Jogador 5 | 5-4 | 10 | 4.000 | -6.000 | 0 → 0 | 5 → 4 | 25% → 25% | 86 → 92 | 10 | 7 → 7 | 0.010 | 0.000 |
| Jogador 5 | 5-5 | 10 | -44.000 | -56.000 | 0 → 0 | 4 → 0 | 25% → 0% | 92 → 82 | 18 | 7 → 7 | -0.063 | -0.280 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 19, COMPOSITION_COMPATIBILITY: 27, IMMEDIATE_UPGRADE: 3, PAIR_POTENTIAL: 14; mudanças de composição: 1; posicionamento melhorou em 21 ações e piorou em 23.
- Jogador 5 — estado final: ouro 82, nível 7, vida 4.0, colocação None.
| Jogador 6 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.056 | 0.000 |
| Jogador 6 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.001 | 0.000 |
| Jogador 6 | 1-3 | 3 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.020 | 0.000 |
| Jogador 6 | 1-4 | 7 | 2.000 | -4.000 | 0 → 0 | 1 → 1 | 11% → 14% | 3 → 4 | 5 | 3 → 4 | -0.029 | 0.000 |
| Jogador 6 | 2-1 | 7 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 14% → 14% | 4 → 8 | 3 | 4 → 4 | 0.000 | -0.323 |
| Jogador 6 | 2-2 | 6 | 4.000 | 0.000 | 0 → 0 | 2 → 1 | 14% → 14% | 8 → 12 | 3 | 4 → 4 | -0.137 | -0.439 |
| Jogador 6 | 2-3 | 10 | 6.000 | -2.000 | 0 → 0 | 1 → 0 | 14% → 18% | 12 → 12 | 8 | 4 → 5 | 0.032 | 0.264 |
| Jogador 6 | 2-4 | 7 | 0.000 | 2.000 | 0 → 0 | 0 → 1 | 18% → 18% | 12 → 8 | 10 | 5 → 5 | 0.000 | 0.000 |
| Jogador 6 | 2-5 | 7 | 2.000 | -2.000 | 0 → 0 | 1 → 1 | 18% → 21% | 8 → 7 | 9 | 5 → 6 | 0.001 | 0.384 |
| Jogador 6 | 2-6 | 8 | 2.000 | 10.000 | 0 → 0 | 1 → 1 | 21% → 21% | 7 → 8 | 6 | 6 → 6 | 0.063 | 0.323 |
| Jogador 6 | 2-7 | 6 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 21% → 21% | 8 → 13 | 3 | 6 → 6 | -0.117 | 0.000 |
| Jogador 6 | 3-1 | 8 | 2.000 | 6.000 | 0 → 0 | 2 → 2 | 21% → 21% | 13 → 17 | 4 | 6 → 6 | 0.088 | 0.351 |
| Jogador 6 | 3-2 | 5 | -2.000 | 8.000 | 0 → 0 | 2 → 3 | 21% → 21% | 17 → 20 | 3 | 6 → 6 | -0.019 | -0.535 |
| Jogador 6 | 3-3 | 4 | 2.000 | -2.000 | 0 → 0 | 3 → 3 | 21% → 21% | 20 → 28 | 0 | 6 → 6 | -0.152 | 0.703 |
| Jogador 6 | 3-4 | 7 | 0.000 | 20.000 | 0 → 0 | 3 → 3 | 21% → 21% | 28 → 24 | 10 | 6 → 6 | 0.101 | 0.000 |
| Jogador 6 | 3-5 | 6 | 0.000 | 10.000 | 0 → 0 | 3 → 3 | 21% → 21% | 24 → 24 | 8 | 6 → 6 | -0.011 | 0.483 |
| Jogador 6 | 3-6 | 5 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 21% → 21% | 24 → 28 | 5 | 6 → 6 | 0.000 | -0.550 |
| Jogador 6 | 3-7 | 6 | 0.000 | 4.000 | 0 → 0 | 3 → 4 | 21% → 21% | 28 → 33 | 7 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 4-1 | 6 | 0.000 | -4.000 | 0 → 0 | 4 → 4 | 21% → 21% | 33 → 44 | 5 | 6 → 6 | 0.000 | 0.467 |
| Jogador 6 | 4-2 | 6 | 0.000 | 8.000 | 0 → 0 | 4 → 4 | 21% → 21% | 44 → 45 | 9 | 6 → 6 | -0.010 | -0.469 |
| Jogador 6 | 4-3 | 4 | 0.000 | 2.000 | 0 → 0 | 4 → 3 | 21% → 21% | 45 → 54 | 4 | 6 → 6 | 0.000 | -0.712 |
| Jogador 6 | 4-4 | 9 | 0.000 | -20.000 | 0 → 0 | 3 → 5 | 21% → 21% | 54 → 77 | 7 | 6 → 6 | 0.013 | 0.000 |
| Jogador 6 | 4-5 | 6 | 0.000 | 8.000 | 0 → 0 | 5 → 3 | 21% → 21% | 77 → 81 | 8 | 6 → 6 | -0.010 | -0.475 |
| Jogador 6 | 4-6 | 10 | 4.000 | 4.000 | 0 → 1 | 3 → 2 | 21% → 21% | 81 → 81 | 16 | 6 → 6 | -0.012 | -0.273 |
| Jogador 6 | 4-7 | 10 | 0.000 | 8.000 | 1 → 1 | 2 → 1 | 21% → 21% | 81 → 82 | 17 | 6 → 7 | -0.006 | 0.000 |
| Jogador 6 | 5-1 | 10 | -28.000 | -70.000 | 1 → 0 | 1 → 0 | 21% → 0% | 82 → 83 | 8 | 7 → 7 | 0.020 | -0.280 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 7, COMPOSITION_COMPATIBILITY: 25, IMMEDIATE_UPGRADE: 6, PAIR_POTENTIAL: 15; mudanças de composição: 0; posicionamento melhorou em 17 ações e piorou em 24.
- Jogador 6 — estado final: ouro 83, nível 7, vida 16.0, colocação None.
| Jogador 7 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.056 | 0.000 |
| Jogador 7 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.001 | 0.000 |
| Jogador 7 | 1-3 | 4 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.050 | 0.000 |
| Jogador 7 | 1-4 | 7 | 0.000 | -4.000 | 0 → 0 | 1 → 1 | 11% → 11% | 3 → 9 | 3 | 3 → 4 | 0.009 | 0.000 |
| Jogador 7 | 2-1 | 10 | 6.000 | 0.000 | 0 → 0 | 1 → 0 | 11% → 14% | 9 → 11 | 4 | 4 → 4 | -0.082 | -0.237 |
| Jogador 7 | 2-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 14% → 18% | 11 → 7 | 12 | 4 → 5 | 0.092 | 0.293 |
| Jogador 7 | 2-3 | 10 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 14% | 7 → 10 | 6 | 5 → 5 | -0.080 | -0.248 |
| Jogador 7 | 2-4 | 8 | 8.000 | 6.000 | 0 → 0 | 1 → 1 | 14% → 18% | 10 → 8 | 7 | 5 → 5 | 0.045 | 0.000 |
| Jogador 7 | 2-5 | 8 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 8 → 6 | 11 | 5 → 5 | 0.001 | 0.336 |
| Jogador 7 | 2-6 | 9 | 6.000 | -6.000 | 0 → 0 | 1 → 1 | 18% → 21% | 6 → 9 | 7 | 5 → 6 | -0.082 | 0.274 |
| Jogador 7 | 2-7 | 5 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 21% → 21% | 9 → 12 | 3 | 6 → 6 | 0.135 | 0.000 |
| Jogador 7 | 3-1 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 12 → 20 | 0 | 6 → 6 | 0.001 | 0.738 |
| Jogador 7 | 3-2 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 20 → 29 | 0 | 6 → 6 | -0.110 | 0.713 |
| Jogador 7 | 3-3 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 29 → 36 | 0 | 6 → 6 | -0.001 | -0.507 |
| Jogador 7 | 3-4 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 36 → 44 | 0 | 6 → 6 | 0.084 | 0.000 |
| Jogador 7 | 3-5 | 10 | 6.000 | -6.000 | 0 → 1 | 1 → 0 | 21% → 21% | 44 → 52 | 2 | 6 → 6 | -0.044 | -0.263 |
| Jogador 7 | 3-6 | 7 | 2.000 | 6.000 | 1 → 1 | 0 → 0 | 21% → 21% | 52 → 58 | 4 | 6 → 6 | -0.104 | -0.395 |
| Jogador 7 | 3-7 | 4 | -2.000 | 2.000 | 1 → 0 | 0 → 0 | 21% → 21% | 58 → 69 | 0 | 6 → 6 | 0.175 | 0.000 |
| Jogador 7 | 4-1 | 5 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 69 → 80 | 0 | 6 → 6 | -0.001 | -0.553 |
| Jogador 7 | 4-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 80 → 91 | 0 | 6 → 6 | 0.000 | 1.492 |
| Jogador 7 | 4-3 | 3 | 0.000 | 8.000 | 0 → 0 | 0 → 0 | 21% → 21% | 91 → 97 | 4 | 6 → 6 | 0.000 | -0.892 |
| Jogador 7 | 4-4 | 3 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 21% → 21% | 97 → 104 | 3 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 4-5 | 6 | 0.000 | 16.000 | 0 → 0 | 0 → 1 | 21% → 21% | 104 → 105 | 10 | 6 → 6 | 0.000 | -0.446 |
| Jogador 7 | 4-6 | 4 | 0.000 | 12.000 | 0 → 0 | 1 → 2 | 21% → 21% | 105 → 110 | 6 | 6 → 6 | 0.000 | 0.725 |
| Jogador 7 | 4-7 | 10 | 0.000 | 8.000 | 0 → 0 | 2 → 3 | 21% → 21% | 110 → 108 | 17 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 5-1 | 10 | 0.000 | 2.000 | 0 → 0 | 3 → 3 | 21% → 21% | 108 → 113 | 13 | 6 → 6 | 0.000 | -0.285 |
| Jogador 7 | 5-2 | 10 | -40.000 | -60.000 | 0 → 0 | 3 → 0 | 21% → 0% | 113 → 107 | 14 | 6 → 6 | 0.083 | -0.285 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 10, COMPOSITION_COMPATIBILITY: 16, IMMEDIATE_UPGRADE: 3, PAIR_POTENTIAL: 8; mudanças de composição: 1; posicionamento melhorou em 28 ações e piorou em 31.
- Jogador 7 — estado final: ouro 107, nível 6, vida 9.0, colocação None.
| Jogador 8 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.056 | 0.000 |
| Jogador 8 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.001 | 0.000 |
| Jogador 8 | 1-3 | 3 | 0.000 | 2.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 4 | 1 | 3 → 3 | -0.020 | 0.000 |
| Jogador 8 | 1-4 | 8 | 2.000 | -2.000 | 0 → 1 | 1 → 0 | 11% → 11% | 4 → 7 | 2 | 3 → 4 | -0.017 | 0.000 |
| Jogador 8 | 2-1 | 5 | 2.000 | 0.000 | 1 → 1 | 0 → 0 | 11% → 14% | 7 → 12 | 1 | 4 → 4 | 0.009 | 0.502 |
| Jogador 8 | 2-2 | 10 | 2.000 | 0.000 | 1 → 1 | 0 → 1 | 14% → 18% | 12 → 10 | 9 | 4 → 5 | -0.008 | 0.256 |
| Jogador 8 | 2-3 | 8 | 4.000 | 4.000 | 1 → 1 | 1 → 0 | 18% → 18% | 10 → 13 | 5 | 5 → 5 | -0.112 | 0.323 |
| Jogador 8 | 2-4 | 8 | 2.000 | 0.000 | 1 → 0 | 0 → 0 | 18% → 18% | 13 → 6 | 15 | 5 → 5 | -0.005 | 0.000 |
| Jogador 8 | 2-5 | 9 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 6 → 8 | 8 | 5 → 6 | 0.093 | -0.293 |
| Jogador 8 | 2-6 | 6 | 8.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 21% | 8 → 6 | 8 | 6 → 6 | -0.100 | -0.405 |
| Jogador 8 | 2-7 | 5 | 0.000 | -2.000 | 0 → 0 | 0 → 1 | 21% → 21% | 6 → 9 | 5 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 3-1 | 6 | 2.000 | 4.000 | 0 → 0 | 1 → 0 | 21% → 21% | 9 → 12 | 4 | 6 → 6 | 0.001 | -0.439 |
| Jogador 8 | 3-2 | 9 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 12 → 18 | 4 | 6 → 6 | -0.005 | -0.293 |
| Jogador 8 | 3-3 | 5 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 18 → 25 | 0 | 6 → 6 | 0.141 | 0.543 |
| Jogador 8 | 3-4 | 5 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 25 → 32 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 3-5 | 5 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 32 → 40 | 0 | 6 → 6 | -0.141 | -0.555 |
| Jogador 8 | 3-6 | 5 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 40 → 50 | 0 | 6 → 6 | 0.001 | -0.563 |
| Jogador 8 | 3-7 | 10 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 25% | 50 → 35 | 23 | 6 → 7 | -0.000 | 0.000 |
| Jogador 8 | 4-1 | 5 | 4.000 | 2.000 | 0 → 0 | 0 → 0 | 25% → 25% | 35 → 41 | 3 | 7 → 7 | -0.095 | 0.597 |
| Jogador 8 | 4-2 | 3 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 25% → 25% | 41 → 50 | 2 | 7 → 7 | 0.000 | 1.028 |
| Jogador 8 | 4-3 | 3 | 0.000 | 8.000 | 0 → 0 | 0 → 1 | 25% → 25% | 50 → 56 | 4 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 4-4 | 3 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 25% → 25% | 56 → 64 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 4-5 | 4 | 0.000 | 12.000 | 0 → 0 | 1 → 1 | 25% → 25% | 64 → 70 | 6 | 7 → 7 | 0.000 | 0.713 |
| Jogador 8 | 4-6 | 10 | 0.000 | 8.000 | 0 → 0 | 1 → 3 | 25% → 25% | 70 → 72 | 15 | 7 → 7 | 0.000 | -0.270 |
| Jogador 8 | 4-7 | 10 | 0.000 | 12.000 | 0 → 0 | 3 → 2 | 25% → 25% | 72 → 69 | 19 | 7 → 7 | -0.006 | 0.000 |
| Jogador 8 | 5-1 | 10 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 69 → 75 | 10 | 7 → 7 | 0.002 | 0.301 |
| Jogador 8 | 5-2 | 10 | 0.000 | 6.000 | 0 → 0 | 2 → 3 | 25% → 25% | 75 → 74 | 18 | 7 → 7 | 0.000 | -0.285 |
| Jogador 8 | 5-3 | 10 | 0.000 | -14.000 | 0 → 0 | 3 → 3 | 25% → 25% | 74 → 88 | 15 | 7 → 7 | 0.006 | 0.000 |
| Jogador 8 | 5-4 | 10 | 0.000 | 0.000 | 0 → 0 | 3 → 5 | 25% → 25% | 88 → 94 | 15 | 7 → 7 | 0.006 | 0.000 |
| Jogador 8 | 5-5 | 10 | 0.000 | 4.000 | 0 → 0 | 5 → 4 | 25% → 25% | 94 → 92 | 15 | 7 → 7 | -0.006 | 0.000 |
| Jogador 8 | 5-6 | 10 | -40.000 | -54.000 | 0 → 0 | 4 → 0 | 25% → 0% | 92 → 86 | 16 | 7 → 7 | 0.114 | -0.285 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 10, COMPOSITION_COMPATIBILITY: 23, IMMEDIATE_UPGRADE: 6, PAIR_POTENTIAL: 13; mudanças de composição: 0; posicionamento melhorou em 26 ações e piorou em 25.
- Jogador 8 — estado final: ouro 86, nível 7, vida 15.0, colocação None.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Revertidas ≤1 ação | ≤2 ações | ≤4 ações | Ouro perdido | Upgrades | Vendas core/par | Valor médio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 39 | 23 | 3 | 4 | 6 | 0 | 1 | 3 | 2.7245 |
| Jogador 2 | 66 | 40 | 1 | 1 | 2 | 0 | 6 | 13 | 3.0184 |
| Jogador 3 | 44 | 19 | 1 | 2 | 2 | 0 | 5 | 3 | 4.8739 |
| Jogador 4 | 59 | 35 | 1 | 1 | 3 | 0 | 4 | 4 | 4.1119 |
| Jogador 5 | 63 | 42 | 1 | 3 | 5 | 0 | 3 | 7 | 1.8524 |
| Jogador 6 | 53 | 28 | 3 | 3 | 5 | 0 | 6 | 5 | 3.6999 |
| Jogador 7 | 37 | 18 | 2 | 2 | 3 | 0 | 3 | 2 | 2.3566 |
| Jogador 8 | 52 | 27 | 0 | 0 | 2 | 0 | 6 | 5 | 3.5039 |

Vendas de core/pares ignoradas antes da decisão da composição: **34**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Uma venda sem compra correspondente na janela é UNKNOWN; sequências ambíguas não são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| MEDIUM | Jogador 1 | 1-4 | 30 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 1-4 | 32 | PURCHASE_REVERSED | Compra de DA_18_Akali_AD desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 1-4 | 34 | PURCHASE_REVERSED | Compra de DA_18_Veigar desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 2-2 | 50 | PURCHASE_REVERSED | Compra de DA_18_Varus desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 2-3 | 63 | PURCHASE_REVERSED | Compra de DA_18_Shen desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 2-4 | 70 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 3-3 | 126 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Akali_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 3-4 | 138 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sentry' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 1 | 3-7 | 162 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Gromp18_AP' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 1-4 | 32 | PURCHASE_REVERSED | Compra de DA_18_Yunara desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 2-1 | 40 | PURCHASE_REVERSED | Compra de DA_18_Xayah desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 2 | 2-6 | 90 | SOLD_CORE_UNIT | Venda de 'DA_18_Azir' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 2-7 | 97 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sejuani' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 2 | 3-2 | 116 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 4-6 | 222 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Gromp18_AP' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 5-2 | 252 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 5-4 | 275 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_MasterYi_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 5-5 | 284 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Ahri' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 6-2 | 327 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 6-2 | 330 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_MasterYi_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 6-3 | 333 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Lillia' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 6-4 | 345 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 6-6 | 365 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_MasterYi_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 2 | 6-6 | 369 | SOLD_CORE_UNIT | Venda de 'DA_18_Rammus' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 2-7 | 100 | PURCHASE_REVERSED | Compra de DA_Scuttlecrab18 desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 3 | 3-3 | 126 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Tristana' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 3-3 | 126 | PURCHASE_REVERSED | Compra de DA_18_Tristana desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 3 | 3-4 | 133 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 3 | 5-5 | 284 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Fiddlesticks18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 1-4 | 30 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 4 | 1-4 | 32 | PURCHASE_REVERSED | Compra de DA_18_Akali_AD desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 4 | 2-2 | 50 | PURCHASE_REVERSED | Compra de DA_18_Yorick desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 4 | 5-4 | 279 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_CrimsonRaptor18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 5-6 | 297 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Nidalee18_AP' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 4 | 6-3 | 337 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Krug18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 4 | 6-5 | 357 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 2-1 | 42 | PURCHASE_REVERSED | Compra de DA_18_Cassiopeia desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-2 | 50 | PURCHASE_REVERSED | Compra de DA_18_LeBlanc desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-3 | 60 | PURCHASE_REVERSED | Compra de DA_18_Tristana desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-3 | 63 | PURCHASE_REVERSED | Compra de DA_18_Camille desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-5 | 81 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Akali_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 2-5 | 81 | PURCHASE_REVERSED | Compra de DA_18_Akali_AD desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 4-2 | 185 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Teemo' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 4-4 | 204 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 4-7 | 236 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Murkwolf18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 5-1 | 244 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Cassiopeia' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 5-1 | 249 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 5-4 | 277 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Murkwolf18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 1-4 | 30 | PURCHASE_REVERSED | Compra de DA_18_Teemo desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 6 | 2-1 | 41 | PURCHASE_REVERSED | Compra de DA_18_Rakan desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 6 | 2-1 | 43 | PURCHASE_REVERSED | Compra de DA_18_Rakan desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 6 | 2-2 | 50 | PURCHASE_REVERSED | Compra de DA_Karma18 desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 6 | 2-4 | 71 | PURCHASE_REVERSED | Compra de DA_18_Rakan desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 6 | 2-5 | 79 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 4-3 | 192 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_MasterYi_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 4-4 | 205 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 6 | 4-4 | 207 | SOLD_CORE_UNIT | Venda de 'DA_18_Rammus' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 4-5 | 212 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 1-4 | 30 | PURCHASE_REVERSED | Compra de DA_18_Elise desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 7 | 1-4 | 32 | PURCHASE_REVERSED | Compra de DA_18_Elise desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 7 | 1-4 | 34 | PURCHASE_REVERSED | Compra de DA_18_Veigar desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 7 | 2-6 | 88 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 5-1 | 246 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 1-4 | 30 | PURCHASE_REVERSED | Compra de DA_18_Varus desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 8 | 2-5 | 84 | SOLD_CORE_UNIT | Venda de 'DA_Gromp18_AP' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 3-1 | 106 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Akali_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 3-1 | 106 | PURCHASE_REVERSED | Compra de DA_18_Akali_AD desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 4-6 | 230 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_CrimsonRaptor18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 5-4 | 278 | SOLD_CORE_UNIT | Venda de 'DA_Fiddlesticks18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 5-6 | 299 | SOLD_CORE_UNIT | Venda de 'DA_Gromp18_AP' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
