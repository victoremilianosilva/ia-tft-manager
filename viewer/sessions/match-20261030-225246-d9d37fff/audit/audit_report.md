# Auditoria da partida TFT

- Arquivos lidos: **8**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **5123**
- Achados: **93**
- CRITICAL: 0 | HIGH: 44 | MEDIUM: 49 | LOW: 0

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 276 | 276 | 276 | 0 | 270 | 0 | 276 | 276 | 276 | 73/57 |
| Jogador 2 | 227 | 227 | 227 | 0 | 224 | 0 | 227 | 227 | 221 | 63/48 |
| Jogador 3 | 146 | 146 | 146 | 0 | 146 | 0 | 146 | 146 | 129 | 26/12 |
| Jogador 4 | 225 | 225 | 225 | 0 | 223 | 0 | 225 | 225 | 210 | 76/62 |
| Jogador 5 | 191 | 191 | 191 | 0 | 189 | 0 | 191 | 191 | 177 | 56/41 |
| Jogador 6 | 186 | 186 | 186 | 0 | 186 | 0 | 186 | 186 | 166 | 54/40 |
| Jogador 7 | 344 | 344 | 344 | 0 | 338 | 0 | 344 | 344 | 344 | 117/103 |
| Jogador 8 | 185 | 185 | 185 | 0 | 184 | 0 | 185 | 185 | 165 | 50/36 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0013076922623440623 | 0.0 | 0.0 | +— / -ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.22450661659240723 | 0.0 | 0.0 | +4a842f64-d6fc-4bc6-8312-a6299595aaa8 / -— |
| Jogador 1 | 1-1 | 3 | SELL | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Veigar | MOVE_BENCH, SELL, PASS | True | True | -0.5276153683662415 | 0.0 | 0.0 | +— / -4a842f64-d6fc-4bc6-8312-a6299595aaa8 |
| Jogador 1 | 1-1 | 4 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.21367721259593964 | 0.0 | 0.0 | +7b7f211c-1c4a-4e0b-b818-3f9b0f67829a / -— |
| Jogador 1 | 1-1 | 5 | SELL | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_Karma18 | MOVE_BENCH, SELL, PASS | True | True | -0.49913451075553894 | 0.0 | 0.0 | +— / -7b7f211c-1c4a-4e0b-b818-3f9b0f67829a |
| Jogador 1 | 1-1 | 6 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +a8111a04-3067-4ce6-9a4b-4f5bb205f413 / -— |
| Jogador 1 | 1-1 | 7 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.5972075462341309 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 8 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.970565140247345 | 0.0 | 0.0 | +cde2c30a-df2c-4275-86ef-e4a4a13a5be1 / -— |
| Jogador 1 | 1-2 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06559108197689056 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 35 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.10718601942062378 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 36 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.009241865947842598 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 37 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.2646143436431885 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 38 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4223015308380127 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 39 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.11149677634239197 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 40 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 41 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.06377681344747543 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 42 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 43 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 57 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2227867692708969 | 0.0 | 0.0 | +24247863-54d4-4674-86e9-9a45609a440e / -— |
| Jogador 1 | 1-3 | 58 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0228151082992554 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3008958697319031 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 60 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 83 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2319662868976593 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 84 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5313377976417542 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 85 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 86 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 109 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5447356700897217 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 110 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1171423196792603 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -a8111a04-3067-4ce6-9a4b-4f5bb205f413,cde2c30a-df2c-4275-86ef-e4a4a13a5be1 |
| Jogador 1 | 2-1 | 111 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39749523997306824 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 112 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.30655789375305176 | 0.0 | 0.0 | +3a74be8d-bf7c-4449-9f1b-d76521e73e6f / -— |
| Jogador 1 | 2-1 | 113 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.46341627836227417 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 114 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6546896696090698 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 115 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.16042961180210114 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 116 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17102721333503723 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 117 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1137281209230423 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 118 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03994898498058319 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 119 | PASS | STABILIZE | 100.0 | 4 | 4 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 133 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 14.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.35520505905151367 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 134 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 14.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03739011287689209 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 135 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 7 | 0 | 18.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030939772725105286 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 136 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 18.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 137 | SELL | STABILIZE | 100.0 | 4 | 3 | 0 | 18.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06793897598981857 | 0.0 | 0.0 | +— / -2718f555-b782-4fea-a68f-31395ad34232 |
| Jogador 1 | 2-2 | 138 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 18.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9562321305274963 | 0.0 | 0.0 | +7aea963f-f0a4-4fa2-8da0-cc5eb260f665 / -— |
| Jogador 1 | 2-2 | 139 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 18.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41142556071281433 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 140 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 18.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42373764514923096 | 0.0 | 0.0 | +— / -c448b2c1-7854-4c8c-a51b-eca2791eb639 |
| Jogador 1 | 2-2 | 141 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.04450000077486038 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 142 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Diana | MOVE_BOARD, PASS | True | True | -0.32442647218704224 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 143 | PASS | STABILIZE | 100.0 | 5 | 1 | 0 | 18.0 | —/DA_18_Diana | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 157 | BUY | STABILIZE | 96.0 | 5 | 6 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.29174473881721497 | 0.0 | 0.0 | +ff10e482-7085-4e73-8a0c-fdd3f4938128 / -— |
| Jogador 1 | 2-3 | 158 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 3 | 0 | 18.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42710214853286743 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 159 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 3 | 0 | 24.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.01991809904575348 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 160 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 3 | 0 | 24.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.05787229165434837 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 161 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 3 | 0 | 24.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.17925453186035156 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 162 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 3 | 0 | 24.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.322867214679718 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 163 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 3 | 0 | 24.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 164 | PASS | STABILIZE | 96.0 | 5 | 3 | 0 | 24.0 | —/DA_18_Diana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 182 | BUY | STABILIZE | 96.0 | 5 | 9 | 0 | 24.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4697507321834564 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 183 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 6 | 0 | 24.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.001365384552627802 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 184 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 6 | 0 | 24.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06990031898021698 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 185 | MOVE_BENCH | ECON | 96.0 | 5 | 6 | 0 | 26.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 186 | MOVE_BENCH | ECON | 96.0 | 5 | 6 | 0 | 26.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6503801941871643 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 187 | PASS | STABILIZE | 96.0 | 5 | 6 | 0 | 24.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 205 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 11 | 1 | 24.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30381497740745544 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 206 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 11 | 1 | 24.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36629602313041687 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 207 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 11 | 1 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30944064259529114 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 208 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 11 | 1 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8469429016113281 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 209 | PASS | STABILIZE | 96.0 | 5 | 11 | 1 | 24.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 227 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 17 | 1 | 24.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015819162130355835 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 228 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 17 | 1 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1544836312532425 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 229 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 17 | 1 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8471853733062744 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 230 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 17 | 1 | 24.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.073702372610569 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 231 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 17 | 1 | 24.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17427249252796173 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 232 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 17 | 1 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.407380074262619 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 233 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 17 | 1 | 24.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18691745400428772 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 234 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 17 | 1 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07172378152608871 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 235 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 17 | 1 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 236 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 17 | 1 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37803179025650024 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 237 | PASS | STABILIZE | 90.0 | 5 | 17 | 1 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 250 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 24 | 2 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00383011088706553 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 251 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 24 | 2 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 252 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 24 | 2 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33854931592941284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 253 | PASS | STABILIZE | 90.0 | 5 | 24 | 2 | 24.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 270 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 31 | 3 | 24.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3663739264011383 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 271 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 31 | 3 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31414371728897095 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 272 | SELL | STABILIZE | 90.0 | 5 | 31 | 3 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37238460779190063 | 0.0 | 0.0 | +— / -24247863-54d4-4674-86e9-9a45609a440e |
| Jogador 1 | 3-1 | 273 | BUY | STABILIZE | 90.0 | 5 | 33 | 3 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7766798734664917 | 0.0 | 0.0 | +7c218f01-e884-46da-8a1a-2d2db27a5ff1 / -— |
| Jogador 1 | 3-1 | 274 | BUY_XP | SLOWROLL | 90.0 | 5 | 30 | 3 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1080000028014183 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 275 | BUY_XP | STABILIZE | 90.0 | 5 | 26 | 2 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07360000163316727 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 276 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 22 | 2 | 26.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5314178466796875 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 277 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 22 | 2 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.24907290935516357 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 278 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 22 | 2 | 32.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.14471355080604553 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 279 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 22 | 2 | 32.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.14029812812805176 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 280 | PASS | STABILIZE | 90.0 | 6 | 22 | 2 | 32.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 289 | BUY | SLOWROLL | 90.0 | 6 | 31 | 3 | 32.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.3610772490501404 | 0.0 | 0.0 | +145f7470-8c0f-4957-b8d6-97939ddaeba1 / -— |
| Jogador 1 | 3-2 | 290 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 27 | 2 | 32.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08232700079679489 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 291 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 27 | 2 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11302431672811508 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 292 | BUY_XP | STABILIZE | 90.0 | 6 | 27 | 2 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 293 | BUY_XP | STABILIZE | 90.0 | 6 | 23 | 2 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 294 | BUY_XP | STABILIZE | 90.0 | 6 | 19 | 1 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 295 | BUY_XP | STABILIZE | 90.0 | 6 | 15 | 1 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 296 | BUY_XP | STABILIZE | 90.0 | 6 | 11 | 1 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 297 | BUY_XP | STABILIZE | 90.0 | 6 | 7 | 0 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 298 | SELL | STABILIZE | 90.0 | 6 | 3 | 0 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3380490243434906 | 0.0 | 0.0 | +— / -7aea963f-f0a4-4fa2-8da0-cc5eb260f665 |
| Jogador 1 | 3-2 | 299 | PASS | STABILIZE | 90.0 | 6 | 5 | 0 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 306 | BUY | STABILIZE | 90.0 | 6 | 12 | 1 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.06160743907094002 | 0.0 | 0.0 | +e6ee6b15-d413-4678-8ffb-29272199a53d / -— |
| Jogador 1 | 3-3 | 307 | MOVE_BOARD | STABILIZE | 90.0 | 6 | 9 | 0 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10453628748655319 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 308 | BUY_XP | STABILIZE | 90.0 | 6 | 9 | 0 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 309 | BUY_XP | STABILIZE | 90.0 | 6 | 5 | 0 | 36.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06459999829530716 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 310 | MOVE_BENCH | STABILIZE | 90.0 | 7 | 1 | 0 | 36.0 | Adaptador/DA_18_Ezreal | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42674216628074646 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 311 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 1 | 0 | 42.0 | Adaptador/DA_18_Ezreal | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 312 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 1 | 0 | 42.0 | Adaptador/DA_18_Ezreal | MOVE_BOARD, PASS | True | True | 0.052043795585632324 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 313 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 1 | 0 | 42.0 | Adaptador/DA_18_Ezreal | MOVE_BOARD, PASS | True | True | 0.14408981800079346 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 314 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 1 | 0 | 42.0 | Adaptador/DA_18_Ezreal | MOVE_BOARD, PASS | True | True | -0.33962926268577576 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 315 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 1 | 0 | 42.0 | Adaptador/DA_18_Ezreal | MOVE_BOARD, PASS | True | True | 0.08313614130020142 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 316 | PASS | STABILIZE | 90.0 | 7 | 1 | 0 | 42.0 | Adaptador/DA_18_Ezreal | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 323 | BUY | STABILIZE | 90.0 | 7 | 8 | 0 | 42.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7436851263046265 | 0.0 | 0.0 | +bddefab1-7dd7-4954-816c-45dbd44b947b / -— |
| Jogador 1 | 3-4 | 324 | BUY_XP | STABILIZE | 90.0 | 7 | 5 | 0 | 42.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 325 | SELL | STABILIZE | 90.0 | 7 | 1 | 0 | 42.0 | Adaptador/DA_18_Diana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9023512601852417 | 0.0 | 0.0 | +— / -bddefab1-7dd7-4954-816c-45dbd44b947b |
| Jogador 1 | 3-4 | 326 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 4 | 0 | 42.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0035709599032998085 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 327 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 4 | 0 | 42.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 328 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 4 | 0 | 42.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.014255795627832413 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 329 | BUY_XP | STABILIZE | 90.0 | 7 | 4 | 0 | 42.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 330 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 0 | 0 | 42.0 | Adaptador/DA_18_Ezreal | MOVE_BOARD, PASS | True | True | -0.10388842225074768 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 331 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 0 | 0 | 42.0 | Adaptador/DA_18_Ezreal | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 332 | PASS | STABILIZE | 90.0 | 7 | 0 | 0 | 42.0 | Adaptador/DA_18_Ezreal | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 342 | BUY | STABILIZE | 90.0 | 7 | 6 | 0 | 42.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03667299076914787 | 0.0 | 0.0 | +727765c8-7f02-491e-a6da-12b0dab59f6d / -— |
| Jogador 1 | 3-5 | 343 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 3 | 0 | 42.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0352528877556324 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 344 | SELL | STABILIZE | 90.0 | 7 | 3 | 0 | 42.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18269230425357819 | 0.0 | 0.0 | +— / -727765c8-7f02-491e-a6da-12b0dab59f6d |
| Jogador 1 | 3-5 | 345 | BUY_XP | STABILIZE | 90.0 | 7 | 6 | 0 | 42.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 346 | PASS | STABILIZE | 90.0 | 7 | 2 | 0 | 42.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 362 | BUY | STABILIZE | 90.0 | 7 | 10 | 1 | 42.0 | Adaptador/DA_18_Ezreal | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7538526654243469 | 0.0 | 0.0 | +d8c38b21-fc25-4c11-87b5-b5747d71bbc7 / -7c218f01-e884-46da-8a1a-2d2db27a5ff1,ff10e482-7085-4e73-8a0c-fdd3f4938128 |
| Jogador 1 | 3-6 | 363 | BUY | STABILIZE | 90.0 | 7 | 7 | 0 | 30.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27844732999801636 | 0.0 | 0.0 | +4518ad1d-87e7-4110-830a-96183c533201 / -— |
| Jogador 1 | 3-6 | 364 | MOVE_BENCH | STABILIZE | 90.0 | 7 | 3 | 0 | 30.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3631952702999115 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 365 | MOVE_BENCH | STABILIZE | 90.0 | 7 | 3 | 0 | 38.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09987351298332214 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 366 | MOVE_BENCH | STABILIZE | 90.0 | 7 | 3 | 0 | 42.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6225292682647705 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 367 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 3 | 0 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.042065247893333435 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 368 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 3 | 0 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.11552552878856659 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 369 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 3 | 0 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0230864305049181 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 370 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 3 | 0 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.007139110006392002 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 371 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 3 | 0 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10388842225074768 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 372 | PASS | STABILIZE | 90.0 | 7 | 3 | 0 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 381 | BUY | STABILIZE | 90.0 | 7 | 12 | 1 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.018666988238692284 | 0.0 | 0.0 | +7306c9be-466e-498c-819e-274ff070c72b / -— |
| Jogador 1 | 3-7 | 382 | BUY | STABILIZE | 90.0 | 7 | 7 | 0 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7438192963600159 | 0.0 | 0.0 | +227dbcdb-af5c-4318-94d1-f01a7847d100 / -— |
| Jogador 1 | 3-7 | 383 | BUY | STABILIZE | 90.0 | 7 | 4 | 0 | 50.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7418991327285767 | 0.0 | 0.0 | +0d8cf876-2884-4724-ab79-246f8e0406f0 / -— |
| Jogador 1 | 3-7 | 384 | MOVE_BENCH | STABILIZE | 90.0 | 7 | 1 | 0 | 50.0 | Adaptador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06453734636306763 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 385 | SELL | STABILIZE | 90.0 | 7 | 1 | 0 | 52.0 | Adaptador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0018909353530034423 | 0.0 | 0.0 | +— / -145f7470-8c0f-4957-b8d6-97939ddaeba1 |
| Jogador 1 | 3-7 | 386 | SELL | STABILIZE | 90.0 | 7 | 5 | 0 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8610828518867493 | 0.0 | 0.0 | +— / -0d8cf876-2884-4724-ab79-246f8e0406f0 |
| Jogador 1 | 3-7 | 387 | SELL | STABILIZE | 90.0 | 7 | 8 | 0 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.859000027179718 | 0.0 | 0.0 | +— / -227dbcdb-af5c-4318-94d1-f01a7847d100 |
| Jogador 1 | 3-7 | 388 | BUY_XP | STABILIZE | 90.0 | 7 | 11 | 1 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 389 | BUY_XP | STABILIZE | 90.0 | 7 | 7 | 0 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 390 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 3 | 0 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.23449817299842834 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 391 | PASS | STABILIZE | 90.0 | 7 | 3 | 0 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 402 | BUY | STABILIZE | 90.0 | 7 | 11 | 1 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | True | 0.08586011826992035 | 0.0 | 0.0 | +844f869e-0e0e-423a-8507-27efd66131f5 / -— |
| Jogador 1 | 4-1 | 403 | CRAFT_AND_EQUIP | STABILIZE | 90.0 | 7 | 8 | 0 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17408716678619385 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 404 | BUY_XP | STABILIZE | 90.0 | 7 | 8 | 0 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 405 | BUY_XP | STABILIZE | 90.0 | 7 | 4 | 0 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 406 | PASS | STABILIZE | 90.0 | 7 | 0 | 0 | 52.0 | Adaptador/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 422 | BUY | STABILIZE | 90.0 | 7 | 9 | 0 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.283978670835495 | 0.0 | 0.0 | +5af104f2-7959-4ca5-91a9-7d44494532ea / -— |
| Jogador 1 | 4-2 | 423 | BUY | STABILIZE | 90.0 | 7 | 6 | 0 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19202080368995667 | 0.0 | 0.0 | +b750b244-a898-479e-9a8e-f30a3f4b0005 / -— |
| Jogador 1 | 4-2 | 424 | PASS | STABILIZE | 90.0 | 7 | 3 | 0 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 441 | BUY | STABILIZE | 90.0 | 7 | 12 | 1 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6639759540557861 | 0.0 | 0.0 | +5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1 / -— |
| Jogador 1 | 4-3 | 442 | PASS | STABILIZE | 90.0 | 7 | 9 | 0 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 461 | BUY | STABILIZE | 90.0 | 7 | 19 | 1 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27412644028663635 | 0.0 | 0.0 | +3c2cff2e-669c-4ef6-ad78-1fe93a7b2a58 / -— |
| Jogador 1 | 4-4 | 462 | PASS | STABILIZE | 90.0 | 7 | 16 | 1 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 481 | BUY | STABILIZE | 90.0 | 7 | 25 | 2 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1041426807641983 | 0.0 | 0.0 | +17170204-1921-4cf1-b92b-cc73bb0701ea / -— |
| Jogador 1 | 4-5 | 482 | BUY | STABILIZE | 90.0 | 7 | 21 | 2 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18423615396022797 | 0.0 | 0.0 | +2530bb2a-8b40-4f0b-a49c-f13fe67fbca4 / -— |
| Jogador 1 | 4-5 | 483 | BUY | STABILIZE | 90.0 | 7 | 17 | 1 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3500664234161377 | 0.0 | 0.0 | +84a3b0f5-c448-4fe1-b001-5ceff2ed306a / -— |
| Jogador 1 | 4-5 | 484 | PASS | STABILIZE | 90.0 | 7 | 14 | 1 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 500 | BUY | STABILIZE | 78.0 | 7 | 20 | 2 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3490760922431946 | 0.0 | 0.0 | +7643f027-a90f-4f3a-8b4c-7be4cba17f95 / -— |
| Jogador 1 | 4-6 | 501 | PASS | STABILIZE | 78.0 | 7 | 17 | 1 | 52.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 512 | SELL | STABILIZE | 78.0 | 7 | 24 | 2 | 52.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016118640080094337 | 0.0 | 0.0 | +— / -844f869e-0e0e-423a-8507-27efd66131f5 |
| Jogador 1 | 4-7 | 513 | BUY | STABILIZE | 78.0 | 7 | 27 | 2 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7658945322036743 | 0.0 | 0.0 | +20a4e507-09d3-42d7-b748-4dde14e82ddf / -— |
| Jogador 1 | 4-7 | 514 | SELL | STABILIZE | 78.0 | 7 | 24 | 2 | 52.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2683076858520508 | 0.0 | 0.0 | +— / -b750b244-a898-479e-9a8e-f30a3f4b0005 |
| Jogador 1 | 4-7 | 515 | BUY | STABILIZE | 78.0 | 7 | 27 | 2 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34475409984588623 | 0.0 | 0.0 | +98b72340-a402-45bc-9493-71263e3168d6 / -— |
| Jogador 1 | 4-7 | 516 | PASS | STABILIZE | 78.0 | 7 | 24 | 2 | 52.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 531 | EQUIP_FROM_INVENTORY | FAST8 | 78.0 | 7 | 31 | 3 | 52.0 | Adaptador/DA_18_MasterYi_AD | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 532 | SELL | FAST8 | 78.0 | 7 | 31 | 3 | 52.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2683076858520508 | 0.0 | 0.0 | +— / -98b72340-a402-45bc-9493-71263e3168d6 |
| Jogador 1 | 5-1 | 533 | BUY | FAST8 | 78.0 | 7 | 34 | 3 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8539901971817017 | 0.0 | 0.0 | +6ea982ab-292d-42fc-99e6-d67c89f9f4fe / -20a4e507-09d3-42d7-b748-4dde14e82ddf,d01cae02-d8ba-491e-841f-bf3120953933 |
| Jogador 1 | 5-1 | 534 | BUY | FAST8 | 78.0 | 7 | 31 | 3 | 46.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6256452798843384 | 0.0 | 0.0 | +4aa5d560-d9d3-45f9-802a-bdbe95788762 / -7643f027-a90f-4f3a-8b4c-7be4cba17f95,e6ee6b15-d413-4678-8ffb-29272199a53d |
| Jogador 1 | 5-1 | 535 | BUY | STABILIZE | 78.0 | 7 | 28 | 2 | 40.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04256745055317879 | 0.0 | 0.0 | +84e865bc-366e-45cd-85e4-fa7314688368 / -— |
| Jogador 1 | 5-1 | 536 | MOVE_BENCH | STABILIZE | 78.0 | 7 | 24 | 2 | 40.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18529798090457916 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 537 | BUY | STABILIZE | 78.0 | 7 | 24 | 2 | 46.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2383435070514679 | 0.0 | 0.0 | +0435182d-aea5-44fe-ba36-601627982b66 / -— |
| Jogador 1 | 5-1 | 538 | MOVE_BOARD | STABILIZE | 78.0 | 7 | 21 | 2 | 46.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04875248298048973 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 539 | MOVE_BENCH | STABILIZE | 78.0 | 7 | 21 | 2 | 46.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40505775809288025 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 540 | BUY | STABILIZE | 78.0 | 7 | 21 | 2 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43207812309265137 | 0.0 | 0.0 | +b0c1aba5-b1bd-48df-abec-19efa8e49d6d / -— |
| Jogador 1 | 5-1 | 541 | PASS | STABILIZE | 78.0 | 7 | 18 | 1 | 52.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 549 | SELL | STABILIZE | 78.0 | 7 | 24 | 2 | 52.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29046154022216797 | 0.0 | 0.0 | +— / -b0c1aba5-b1bd-48df-abec-19efa8e49d6d |
| Jogador 1 | 5-2 | 550 | BUY | STABILIZE | 78.0 | 7 | 27 | 2 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7715815305709839 | 0.0 | 0.0 | +d80c845d-24bc-4053-a60d-5d0122839b0c / -— |
| Jogador 1 | 5-2 | 551 | SELL | STABILIZE | 78.0 | 7 | 24 | 2 | 52.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.032769229263067245 | 0.0 | 0.0 | +— / -17170204-1921-4cf1-b92b-cc73bb0701ea |
| Jogador 1 | 5-2 | 552 | BUY | STABILIZE | 78.0 | 7 | 28 | 2 | 52.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8787996172904968 | 0.0 | 0.0 | +943437ce-e190-4790-986b-4e66e49637a7 / -3a43ff36-dccd-49a7-92d8-0b01e739ea89,d80c845d-24bc-4053-a60d-5d0122839b0c |
| Jogador 1 | 5-2 | 553 | BUY | STABILIZE | 78.0 | 7 | 25 | 2 | 46.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09388703107833862 | 0.0 | 0.0 | +a3def045-2a10-4672-a6d6-255c40fd1c90 / -— |
| Jogador 1 | 5-2 | 554 | MOVE_BOARD | STABILIZE | 78.0 | 7 | 21 | 2 | 46.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10906810313463211 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 555 | MOVE_BOARD | STABILIZE | 78.0 | 7 | 21 | 2 | 46.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012479945085942745 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 556 | MOVE_BOARD | STABILIZE | 78.0 | 7 | 21 | 2 | 46.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02891405299305916 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 557 | PASS | STABILIZE | 78.0 | 7 | 21 | 2 | 46.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 562 | BUY | ECON | 78.0 | 8 | 30 | 3 | 58.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03014860674738884 | 0.0 | 0.0 | +ecf369a7-649e-45fe-ad90-8f29e1714fe6 / -— |
| Jogador 1 | 5-3 | 563 | MOVE_BENCH | ECON | 78.0 | 8 | 26 | 2 | 58.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6648463010787964 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 564 | BUY | ECON | 78.0 | 8 | 26 | 2 | 66.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21780461072921753 | 0.0 | 0.0 | +5754c4b4-0a7d-49e5-93e4-b144c3090a41 / -— |
| Jogador 1 | 5-3 | 565 | SELL | ECON | 78.0 | 8 | 22 | 2 | 66.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.048153847455978394 | 0.0 | 0.0 | +— / -5754c4b4-0a7d-49e5-93e4-b144c3090a41 |
| Jogador 1 | 5-3 | 566 | BUY | ECON | 78.0 | 8 | 26 | 2 | 66.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2810552716255188 | 0.0 | 0.0 | +5416d773-cb2c-442a-8ee9-0d46d22c2087 / -— |
| Jogador 1 | 5-3 | 567 | MOVE_BOARD | ECON | 78.0 | 8 | 23 | 2 | 66.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16880784928798676 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 568 | MOVE_BOARD | ECON | 78.0 | 8 | 23 | 2 | 66.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0031246859580278397 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 569 | PASS | ECON | 78.0 | 8 | 23 | 2 | 66.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 579 | SELL | ECON | 78.0 | 8 | 31 | 3 | 66.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0560000017285347 | 0.0 | 0.0 | +— / -5416d773-cb2c-442a-8ee9-0d46d22c2087 |
| Jogador 1 | 5-4 | 580 | BUY | ECON | 78.0 | 8 | 34 | 3 | 66.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02000996842980385 | 0.0 | 0.0 | +e5f38fbd-826a-4067-a33f-86cf7eb98f30 / -— |
| Jogador 1 | 5-4 | 581 | SELL | ECON | 78.0 | 8 | 32 | 3 | 66.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.032769229263067245 | 0.0 | 0.0 | +— / -2530bb2a-8b40-4f0b-a49c-f13fe67fbca4 |
| Jogador 1 | 5-4 | 582 | BUY | ECON | 78.0 | 8 | 36 | 3 | 66.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09923339635133743 | 0.0 | 0.0 | +98b600a1-736b-437d-a69e-8a7f7235d9c3 / -— |
| Jogador 1 | 5-4 | 583 | PASS | ECON | 78.0 | 8 | 34 | 3 | 66.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 592 | SELL | ECON | 78.0 | 8 | 43 | 4 | 66.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02138461545109749 | 0.0 | 0.0 | +— / -98b600a1-736b-437d-a69e-8a7f7235d9c3 |
| Jogador 1 | 5-5 | 593 | BUY | ECON | 78.0 | 8 | 45 | 4 | 66.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16970621049404144 | 0.0 | 0.0 | +89ef75a2-6ac2-4c6c-b2b8-492aec985a01 / -— |
| Jogador 1 | 5-5 | 594 | SELL | ECON | 78.0 | 8 | 40 | 4 | 66.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.032769229263067245 | 0.0 | 0.0 | +— / -ecf369a7-649e-45fe-ad90-8f29e1714fe6 |
| Jogador 1 | 5-5 | 595 | BUY | ECON | 78.0 | 8 | 44 | 4 | 66.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05788537487387657 | 0.0 | 0.0 | +9af900db-c181-448a-9736-30f08f062a00 / -— |
| Jogador 1 | 5-5 | 596 | PASS | ECON | 78.0 | 8 | 41 | 4 | 66.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 609 | SELL | ECON | 78.0 | 8 | 51 | 5 | 66.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013384615071117878 | 0.0 | 0.0 | +— / -9af900db-c181-448a-9736-30f08f062a00 |
| Jogador 1 | 5-6 | 610 | BUY | ECON | 78.0 | 8 | 54 | 5 | 66.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14994187653064728 | 0.0 | 0.0 | +3658b5d8-450f-451a-8487-5b3bdd7c385b / -— |
| Jogador 1 | 5-6 | 611 | SELL | ECON | 78.0 | 8 | 50 | 5 | 66.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04015384614467621 | 0.0 | 0.0 | +— / -3658b5d8-450f-451a-8487-5b3bdd7c385b |
| Jogador 1 | 5-6 | 612 | BUY | ECON | 78.0 | 8 | 54 | 5 | 66.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04221409931778908 | 0.0 | 0.0 | +99857cfa-b422-4167-bb01-d9fd94a55d88 / -— |
| Jogador 1 | 5-6 | 613 | SELL | ECON | 78.0 | 8 | 50 | 5 | 66.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02476923167705536 | 0.0 | 0.0 | +— / -99857cfa-b422-4167-bb01-d9fd94a55d88 |
| Jogador 1 | 5-6 | 614 | BUY | ECON | 78.0 | 8 | 54 | 5 | 66.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07829810678958893 | 0.0 | 0.0 | +217a3ebb-1953-4f1e-bfdd-a3c9438e791e / -— |
| Jogador 1 | 5-6 | 615 | PASS | ECON | 78.0 | 8 | 51 | 5 | 66.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00025696842931210995 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 622 | SELL | ECON | 63.0 | 8 | 61 | 5 | 66.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029999999329447746 | 0.0 | 0.0 | +— / -217a3ebb-1953-4f1e-bfdd-a3c9438e791e |
| Jogador 1 | 5-7 | 623 | BUY | ECON | 63.0 | 8 | 64 | 5 | 66.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38335171341896057 | 0.0 | 0.0 | +9a96b07c-5b37-4be7-855e-dc2d942e7171 / -— |
| Jogador 1 | 5-7 | 624 | SELL | ECON | 63.0 | 8 | 61 | 5 | 66.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002047809073701501 | 0.0 | 0.0 | +— / -84e865bc-366e-45cd-85e4-fa7314688368 |
| Jogador 1 | 5-7 | 625 | BUY | ECON | 63.0 | 8 | 65 | 5 | 66.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8444710373878479 | 0.0 | 0.0 | +aee0c45d-0178-4238-987f-5ee83dae7bce / -— |
| Jogador 1 | 5-7 | 626 | PASS | ECON | 63.0 | 8 | 62 | 5 | 66.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005068708211183548 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 638 | EQUIP_FROM_INVENTORY | ECON | 63.0 | 8 | 72 | 5 | 66.0 | Adaptador/DA_18_Diana | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 639 | EQUIP_FROM_INVENTORY | ECON | 63.0 | 8 | 72 | 5 | 66.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.031112564727663994 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 640 | SELL | ECON | 63.0 | 8 | 72 | 5 | 66.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28415384888648987 | 0.0 | 0.0 | +— / -e5f38fbd-826a-4067-a33f-86cf7eb98f30 |
| Jogador 1 | 6-1 | 641 | BUY | ECON | 63.0 | 8 | 74 | 5 | 66.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8425312042236328 | 0.0 | 0.0 | +a1357716-abf4-4d4f-abb8-34f2681f16dd / -— |
| Jogador 1 | 6-1 | 642 | SELL | ECON | 63.0 | 8 | 70 | 5 | 66.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -89ef75a2-6ac2-4c6c-b2b8-492aec985a01 |
| Jogador 1 | 6-1 | 643 | BUY | ECON | 63.0 | 8 | 75 | 5 | 66.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1504749059677124 | 0.0 | 0.0 | +39b89fbe-9520-4eaa-80f9-81e03232c83c / -— |
| Jogador 1 | 6-1 | 644 | PASS | ECON | 63.0 | 8 | 71 | 5 | 66.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009920714423060417 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 652 | SELL | ECON | 63.0 | 8 | 81 | 5 | 66.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04015384614467621 | 0.0 | 0.0 | +— / -39b89fbe-9520-4eaa-80f9-81e03232c83c |
| Jogador 1 | 6-2 | 653 | BUY | ECON | 63.0 | 8 | 85 | 5 | 66.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.039570927619934 | 0.0 | 0.0 | +1512b230-15a6-405f-9b6b-4387a3091648 / -4518ad1d-87e7-4110-830a-96183c533201,a1357716-abf4-4d4f-abb8-34f2681f16dd |
| Jogador 1 | 6-2 | 654 | BUY | ECON | 63.0 | 8 | 81 | 5 | 58.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02983715757727623 | 0.0 | 0.0 | +b2517873-8317-401b-8461-1d86969edbd7 / -— |
| Jogador 1 | 6-2 | 655 | SELL | ECON | 63.0 | 8 | 77 | 5 | 58.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02476923167705536 | 0.0 | 0.0 | +— / -b2517873-8317-401b-8461-1d86969edbd7 |
| Jogador 1 | 6-2 | 656 | BUY | ECON | 63.0 | 8 | 81 | 5 | 58.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06513337790966034 | 0.0 | 0.0 | +64d87de4-68df-4a72-8b8d-f78039ae4ce5 / -— |
| Jogador 1 | 6-2 | 657 | PASS | ECON | 63.0 | 8 | 78 | 5 | 58.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014011009596288204 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 661 | MOVE_BENCH | ECON | 63.0 | 8 | 78 | 5 | 58.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6440697312355042 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 667 | BUY | ECON | 63.0 | 8 | 89 | 5 | 64.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09497234970331192 | 0.0 | 0.0 | +d9097eba-c1b2-4df8-9e5d-a9134dbfe52f / -— |
| Jogador 1 | 6-3 | 668 | SELL | ECON | 63.0 | 8 | 84 | 5 | 64.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029999999329447746 | 0.0 | 0.0 | +— / -64d87de4-68df-4a72-8b8d-f78039ae4ce5 |
| Jogador 1 | 6-3 | 669 | BUY | ECON | 63.0 | 8 | 87 | 5 | 64.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.480386346578598 | 0.0 | 0.0 | +aea521ef-8511-4b98-9c6d-e83b814777df / -— |
| Jogador 1 | 6-3 | 670 | PASS | ECON | 63.0 | 8 | 84 | 5 | 64.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.017687013372778893 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-4 | 681 | SELL | ECON | 63.0 | 8 | 94 | 5 | 64.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28600001335144043 | 0.0 | 0.0 | +— / -aea521ef-8511-4b98-9c6d-e83b814777df |
| Jogador 1 | 6-4 | 682 | BUY | ECON | 63.0 | 8 | 97 | 5 | 64.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04971139132976532 | 0.0 | 0.0 | +95a2e19e-619f-4497-ba52-e9bbf06b364f / -— |
| Jogador 1 | 6-4 | 683 | SELL | ECON | 63.0 | 8 | 93 | 5 | 64.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02476923167705536 | 0.0 | 0.0 | +— / -95a2e19e-619f-4497-ba52-e9bbf06b364f |
| Jogador 1 | 6-4 | 684 | BUY | ECON | 63.0 | 8 | 97 | 5 | 64.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1574452817440033 | 0.0 | 0.0 | +0e5921d4-a056-4f42-951e-93de5f2834bb / -— |
| Jogador 1 | 6-4 | 685 | SELL | ECON | 63.0 | 8 | 93 | 5 | 64.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04015384614467621 | 0.0 | 0.0 | +— / -0e5921d4-a056-4f42-951e-93de5f2834bb |
| Jogador 1 | 6-4 | 686 | BUY | ECON | 63.0 | 8 | 97 | 5 | 64.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1574452668428421 | 0.0 | 0.0 | +0b38218d-9c50-41ac-b761-115c054bf314 / -— |
| Jogador 1 | 6-4 | 687 | PASS | ECON | 63.0 | 8 | 93 | 5 | 64.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02344455197453499 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-5 | 695 | SELL | ECON | 63.0 | 8 | 103 | 5 | 64.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04015384614467621 | 0.0 | 0.0 | +— / -0b38218d-9c50-41ac-b761-115c054bf314 |
| Jogador 1 | 6-5 | 696 | BUY | ECON | 63.0 | 8 | 107 | 5 | 64.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0399974584579468 | 0.0 | 0.0 | +674bcfdb-fddd-498c-ba65-ef3a3b989f07 / -5920dc34-fc7a-4b87-88cd-2fa9ea29f4d1,5af104f2-7959-4ca5-91a9-7d44494532ea |
| Jogador 1 | 6-5 | 697 | BUY | ECON | 63.0 | 8 | 104 | 5 | 64.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1739242970943451 | 0.0 | 0.0 | +2b89bd83-8449-4c63-9da2-62a46c68bdf5 / -— |
| Jogador 1 | 6-5 | 698 | BUY | ECON | 63.0 | 8 | 99 | 5 | 64.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20940221846103668 | 0.0 | 0.0 | +bbfa514f-8d07-411b-aa19-4511ae5fb5cd / -— |
| Jogador 1 | 6-5 | 699 | PASS | ECON | 63.0 | 8 | 95 | 5 | 64.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.024759097024798393 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-6 | 709 | SELL | ECON | 45.0 | 8 | 105 | 5 | 64.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003444305621087551 | 0.0 | 0.0 | +— / -bbfa514f-8d07-411b-aa19-4511ae5fb5cd |
| Jogador 1 | 6-6 | 710 | BUY | ECON | 45.0 | 8 | 109 | 5 | 64.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20831109583377838 | 0.0 | 0.0 | +3c5f5211-f30d-44e7-ac68-0ce513a3d614 / -— |
| Jogador 1 | 6-6 | 711 | SELL | ECON | 45.0 | 8 | 105 | 5 | 64.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0034370452631264925 | 0.0 | 0.0 | +— / -3c5f5211-f30d-44e7-ac68-0ce513a3d614 |
| Jogador 1 | 6-6 | 712 | BUY | ECON | 45.0 | 8 | 109 | 5 | 64.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1574980616569519 | 0.0 | 0.0 | +01c587bb-ca4f-4690-9e4b-d1e9c44fd33e / -— |
| Jogador 1 | 6-6 | 713 | PASS | ECON | 45.0 | 8 | 105 | 5 | 64.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03150032460689545 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-7 | 719 | SELL | STABILIZE | 27.0 | 8 | 116 | 5 | 64.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04015384614467621 | 0.0 | 0.0 | +— / -01c587bb-ca4f-4690-9e4b-d1e9c44fd33e |
| Jogador 1 | 6-7 | 720 | BUY | STABILIZE | 27.0 | 8 | 120 | 5 | 64.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5070838928222656 | 0.0 | 0.0 | +0a6e3194-ed55-43ad-ac66-31e08ccda7aa / -— |
| Jogador 1 | 6-7 | 721 | SELL | STABILIZE | 27.0 | 8 | 117 | 5 | 64.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0860000029206276 | 0.0 | 0.0 | +— / -1512b230-15a6-405f-9b6b-4387a3091648 |
| Jogador 1 | 6-7 | 722 | BUY | STABILIZE | 27.0 | 8 | 128 | 5 | 64.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24933508038520813 | 0.0 | 0.0 | +b250e22d-7193-4ea5-879d-5c7b41145719 / -— |
| Jogador 1 | 6-7 | 723 | PASS | STABILIZE | 27.0 | 8 | 124 | 5 | 64.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.044973619282245636 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 7-1 | 729 | EQUIP_FROM_INVENTORY | STABILIZE | 27.0 | 8 | 135 | 5 | 64.0 | Adaptador/DA_18_Diana | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 7-1 | 730 | EQUIP_FROM_INVENTORY | STABILIZE | 27.0 | 8 | 135 | 5 | 64.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 7-1 | 731 | SELL | STABILIZE | 27.0 | 8 | 135 | 5 | 64.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0034442050382494926 | 0.0 | 0.0 | +— / -b250e22d-7193-4ea5-879d-5c7b41145719 |
| Jogador 1 | 7-1 | 732 | BUY | STABILIZE | 27.0 | 8 | 139 | 5 | 64.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4024389386177063 | 0.0 | 0.0 | +27079fe2-8808-47b7-8b10-9fb2834bb6ed / -— |
| Jogador 1 | 7-1 | 733 | PASS | STABILIZE | 27.0 | 8 | 135 | 5 | 64.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0531107597053051 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 7-2 | 741 | SELL | ALL_IN | 4.0 | 8 | 146 | 5 | 64.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04600000008940697 | 0.0 | 0.0 | +— / -27079fe2-8808-47b7-8b10-9fb2834bb6ed |
| Jogador 1 | 7-2 | 742 | BUY | ALL_IN | 4.0 | 8 | 150 | 5 | 64.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22765754163265228 | 0.0 | 0.0 | +9c3b3b78-e99c-4947-b958-cce156ecccb1 / -— |
| Jogador 1 | 7-2 | 743 | SELL | ALL_IN | 4.0 | 8 | 147 | 5 | 64.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2970249354839325 | 0.0 | 0.0 | +— / -9c3b3b78-e99c-4947-b958-cce156ecccb1 |
| Jogador 1 | 7-2 | 744 | BUY | ALL_IN | 4.0 | 8 | 150 | 5 | 64.0 | Adaptador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8548944592475891 | 0.0 | 0.0 | +b311d350-7bab-48ee-9833-0883606b4a2f / -— |
| Jogador 1 | 7-2 | 745 | PASS | ALL_IN | 4.0 | 8 | 147 | 5 | 64.0 | Adaptador/DA_18_Diana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11223086714744568 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.010384615510702133 | 0.0 | 0.0 | +— / -fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.1713879406452179 | 0.0 | 0.0 | +2f83d3d4-5487-4aa7-8831-52a3e3a9035e / -— |
| Jogador 2 | 1-1 | 3 | SELL | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_Karma18 | MOVE_BENCH, SELL, PASS | True | True | -0.5153076648712158 | 0.0 | 0.0 | +— / -2f83d3d4-5487-4aa7-8831-52a3e3a9035e |
| Jogador 2 | 1-1 | 4 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.41038674116134644 | 0.0 | 0.0 | +292ef825-d326-4dd8-9c42-c47cfc62116f / -— |
| Jogador 2 | 1-1 | 5 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.5833139419555664 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 6 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9702869057655334 | 0.0 | 0.0 | +94ede66e-59bc-4c41-aabf-f64372e20f9a / -— |
| Jogador 2 | 1-2 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06559108197689056 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 35 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.10718601942062378 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 36 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.009241865947842598 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 37 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.30475786328315735 | 0.0 | 0.0 | +5a1572b3-8b27-4d87-b885-f342b91c0854 / -— |
| Jogador 2 | 1-2 | 38 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4173470437526703 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 39 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.11149677634239197 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 40 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 41 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.06377681344747543 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 42 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 43 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 57 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.30351880192756653 | 0.0 | 0.0 | +de00430a-8a57-423c-887c-317d53c2cdd3 / -— |
| Jogador 2 | 1-3 | 58 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37570977210998535 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 59 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.036966722458601 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 60 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06377681344747543 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 61 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3681824207305908 | 0.0 | 0.0 | +— / -5a1572b3-8b27-4d87-b885-f342b91c0854 |
| Jogador 2 | 1-3 | 62 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 83 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3472065031528473 | 0.0 | 0.0 | +9a6f90da-bbac-4ba0-b2a3-729a1a2deab5 / -— |
| Jogador 2 | 1-4 | 84 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5028833150863647 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 85 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 10.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7304970622062683 | 0.0 | 0.0 | +— / -94ede66e-59bc-4c41-aabf-f64372e20f9a |
| Jogador 2 | 1-4 | 86 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 109 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.37684470415115356 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 110 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4216909110546112 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 111 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.042908359318971634 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 112 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 113 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.04981626570224762 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 114 | PASS | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 133 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8852248787879944 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 134 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 8 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15891896188259125 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 135 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 8 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4959362745285034 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 136 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 8 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 137 | PASS | STABILIZE | 100.0 | 4 | 8 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 157 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 15 | 1 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2611272931098938 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 158 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 15 | 1 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3987564742565155 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 159 | PASS | STABILIZE | 100.0 | 4 | 15 | 1 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 182 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 21 | 2 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 183 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 21 | 2 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25856566429138184 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 184 | PASS | STABILIZE | 94.0 | 4 | 21 | 2 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 205 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 28 | 2 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1652248650789261 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 206 | SELL | STABILIZE | 94.0 | 4 | 28 | 2 | 16.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27864423394203186 | 0.0 | 0.0 | +— / -9a6f90da-bbac-4ba0-b2a3-729a1a2deab5 |
| Jogador 2 | 2-5 | 207 | BUY | STABILIZE | 94.0 | 4 | 30 | 3 | 16.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.38373860716819763 | 0.0 | 0.0 | +081b684f-5d42-45c5-9a68-12127e5330a7 / -— |
| Jogador 2 | 2-5 | 208 | BUY_XP | STABILIZE | 94.0 | 4 | 27 | 2 | 16.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07959999889135361 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 209 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 23 | 2 | 16.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3576818108558655 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 210 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 23 | 2 | 22.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1468629539012909 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 211 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 23 | 2 | 22.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.014965374022722244 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 212 | BUY_XP | STABILIZE | 94.0 | 5 | 23 | 2 | 22.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 213 | BUY_XP | STABILIZE | 94.0 | 5 | 19 | 1 | 22.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 214 | BUY_XP | STABILIZE | 94.0 | 5 | 15 | 1 | 22.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 215 | PASS | STABILIZE | 94.0 | 5 | 11 | 1 | 22.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 227 | BUY | STABILIZE | 94.0 | 5 | 18 | 1 | 22.0 | Colosso/DA_18_Azir | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1159346103668213 | 0.0 | 0.0 | +6f3f86ec-6928-4032-a1ef-533a68865516 / -561fb9a8-e987-4935-b11c-6c6104ced65d,de00430a-8a57-423c-887c-317d53c2cdd3 |
| Jogador 2 | 2-6 | 228 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 16 | 1 | 14.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2533554434776306 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 229 | BUY | STABILIZE | 94.0 | 5 | 16 | 1 | 22.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2630031406879425 | 0.0 | 0.0 | +97fc5647-5995-4f21-aa03-13454546919a / -— |
| Jogador 2 | 2-6 | 230 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 13 | 1 | 22.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3667159974575043 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 231 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 13 | 1 | 20.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5920451879501343 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 232 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 13 | 1 | 28.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.1877261996269226 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 233 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 13 | 1 | 28.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.2862316966056824 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 234 | PASS | STABILIZE | 94.0 | 5 | 13 | 1 | 28.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 250 | BUY | STABILIZE | 94.0 | 5 | 21 | 2 | 28.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.11281126737594604 | 0.0 | 0.0 | +729ccd5b-adc5-4bca-9523-dcb532e93ecb / -— |
| Jogador 2 | 2-7 | 251 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 18 | 1 | 28.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3762728273868561 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 252 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 18 | 1 | 26.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10181494802236557 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 253 | BUY_XP | STABILIZE | 94.0 | 5 | 18 | 1 | 32.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029200000688433647 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 254 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 14 | 1 | 32.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5246980786323547 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 255 | BUY | STABILIZE | 94.0 | 6 | 14 | 1 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.42015060782432556 | 0.0 | 0.0 | +c96b6357-8134-4e68-af0b-f5695a815597 / -— |
| Jogador 2 | 2-7 | 256 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 12 | 1 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1799057424068451 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 257 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 12 | 1 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1156095415353775 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 258 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 12 | 1 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3393017649650574 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 259 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 12 | 1 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16292668879032135 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 260 | PASS | STABILIZE | 94.0 | 6 | 12 | 1 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 270 | BUY | STABILIZE | 94.0 | 6 | 19 | 1 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2672576904296875 | 0.0 | 0.0 | +e8c696ca-2d5c-4eb0-a8f4-55decc1e21f5 / -— |
| Jogador 2 | 3-1 | 271 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 16 | 1 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09783678501844406 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 272 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 16 | 1 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8017997741699219 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 273 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 16 | 1 | 32.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23843789100646973 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 274 | PASS | STABILIZE | 94.0 | 6 | 16 | 1 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 289 | BUY | STABILIZE | 94.0 | 6 | 24 | 2 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7597029209136963 | 0.0 | 0.0 | +584e7960-a541-4d45-8ea1-8a75e288c387 / -— |
| Jogador 2 | 3-2 | 290 | MOVE_BENCH | STABILIZE | 94.0 | 6 | 23 | 2 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0977979525923729 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 291 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 23 | 2 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11364776641130447 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 292 | SELL | STABILIZE | 94.0 | 6 | 23 | 2 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008161083795130253 | 0.0 | 0.0 | +— / -729ccd5b-adc5-4bca-9523-dcb532e93ecb |
| Jogador 2 | 3-2 | 293 | SELL | STABILIZE | 94.0 | 6 | 26 | 2 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9294107556343079 | 0.0 | 0.0 | +— / -584e7960-a541-4d45-8ea1-8a75e288c387 |
| Jogador 2 | 3-2 | 294 | SELL | STABILIZE | 94.0 | 6 | 27 | 2 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3332808017730713 | 0.0 | 0.0 | +— / -c96b6357-8134-4e68-af0b-f5695a815597 |
| Jogador 2 | 3-2 | 295 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 29 | 2 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.10245084762573242 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 296 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 29 | 2 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.30245909094810486 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 297 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 29 | 2 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17978544533252716 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 298 | MOVE_BOARD | STABILIZE | 94.0 | 6 | 29 | 2 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.3220738172531128 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 299 | PASS | STABILIZE | 94.0 | 6 | 29 | 2 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 306 | BUY | SLOWROLL | 94.0 | 6 | 39 | 3 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0819673165678978 | 0.0 | 0.0 | +4e116bc2-f686-4a17-adb1-a7b80865c159 / -— |
| Jogador 2 | 3-3 | 307 | BUY | SLOWROLL | 94.0 | 6 | 35 | 3 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2547989785671234 | 0.0 | 0.0 | +e658854d-c531-46fc-8978-067953930510 / -— |
| Jogador 2 | 3-3 | 308 | SELL | SLOWROLL | 94.0 | 6 | 32 | 3 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16976922750473022 | 0.0 | 0.0 | +— / -e658854d-c531-46fc-8978-067953930510 |
| Jogador 2 | 3-3 | 309 | MOVE_BENCH | SLOWROLL | 94.0 | 6 | 35 | 3 | 34.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.45584407448768616 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 310 | MOVE_BENCH | SLOWROLL | 94.0 | 6 | 35 | 3 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2182115912437439 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 311 | PASS | SLOWROLL | 94.0 | 6 | 35 | 3 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 323 | BUY | SLOWROLL | 94.0 | 6 | 46 | 4 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2588215470314026 | 0.0 | 0.0 | +8edef2b0-f5b3-4c01-ba2b-851be248676e / -— |
| Jogador 2 | 3-4 | 324 | SELL | SLOWROLL | 94.0 | 6 | 44 | 4 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16776922345161438 | 0.0 | 0.0 | +— / -8edef2b0-f5b3-4c01-ba2b-851be248676e |
| Jogador 2 | 3-4 | 325 | SELL | SLOWROLL | 94.0 | 6 | 46 | 4 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35183393955230713 | 0.0 | 0.0 | +— / -081b684f-5d42-45c5-9a68-12127e5330a7 |
| Jogador 2 | 3-4 | 326 | BUY | SLOWROLL | 94.0 | 6 | 49 | 4 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.2861490547657013 | 0.0 | 0.0 | +ff0d9869-c346-4210-be85-1e802a25dd8b / -— |
| Jogador 2 | 3-4 | 327 | SELL | SLOWROLL | 94.0 | 6 | 47 | 4 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16099999845027924 | 0.0 | 0.0 | +— / -ff0d9869-c346-4210-be85-1e802a25dd8b |
| Jogador 2 | 3-4 | 328 | MOVE_BOARD | SLOWROLL | 94.0 | 6 | 49 | 4 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.3302363157272339 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 329 | MOVE_BOARD | SLOWROLL | 94.0 | 6 | 49 | 4 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17280340194702148 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 330 | BUY_XP | SLOWROLL | 94.0 | 6 | 49 | 4 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 331 | BUY_XP | SLOWROLL | 94.0 | 6 | 45 | 4 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 332 | BUY_XP | SLOWROLL | 94.0 | 6 | 41 | 4 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.1080000028014183 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 333 | PASS | SLOWROLL | 94.0 | 6 | 37 | 3 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 342 | BUY | SLOWROLL | 94.0 | 6 | 47 | 4 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.284101665019989 | 0.0 | 0.0 | +cce8de69-f877-4e86-b720-6aea91e68f47 / -— |
| Jogador 2 | 3-5 | 343 | SELL | SLOWROLL | 94.0 | 6 | 44 | 4 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1589999943971634 | 0.0 | 0.0 | +— / -cce8de69-f877-4e86-b720-6aea91e68f47 |
| Jogador 2 | 3-5 | 344 | MOVE_BOARD | SLOWROLL | 94.0 | 6 | 47 | 4 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10906810313463211 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 345 | BUY | SLOWROLL | 94.0 | 6 | 47 | 4 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.13452529907226562 | 0.0 | 0.0 | +7a6a5238-f799-4f36-b4b2-63c890a83920 / -— |
| Jogador 2 | 3-5 | 346 | BUY_XP | SLOWROLL | 94.0 | 6 | 45 | 4 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 347 | BUY_XP | SLOWROLL | 94.0 | 6 | 41 | 4 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1080000028014183 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 348 | BUY_XP | SLOWROLL | 94.0 | 6 | 37 | 3 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0738999992609024 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 349 | SELL | FAST8 | 94.0 | 7 | 33 | 3 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1739230751991272 | 0.0 | 0.0 | +— / -7a6a5238-f799-4f36-b4b2-63c890a83920 |
| Jogador 2 | 3-5 | 350 | BUY | FAST8 | 94.0 | 7 | 35 | 3 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.1384982168674469 | 0.0 | 0.0 | +b5cec20a-0619-4060-9f1b-e72942ac34dd / -— |
| Jogador 2 | 3-5 | 351 | SELL | FAST8 | 94.0 | 7 | 34 | 3 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17438460886478424 | 0.0 | 0.0 | +— / -b5cec20a-0619-4060-9f1b-e72942ac34dd |
| Jogador 2 | 3-5 | 352 | PASS | FAST8 | 94.0 | 7 | 35 | 3 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 362 | BUY | FAST8 | 94.0 | 7 | 47 | 4 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2883359491825104 | 0.0 | 0.0 | +63304cf5-4aa7-473e-9bfb-ec04cd68ebbd / -— |
| Jogador 2 | 3-6 | 363 | BUY | FAST8 | 94.0 | 7 | 45 | 4 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09791199117898941 | 0.0 | 0.0 | +23157bd6-5e8f-4416-bb7f-2e5d71a06543 / -— |
| Jogador 2 | 3-6 | 364 | BUY | FAST8 | 94.0 | 7 | 41 | 4 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0662200003862381 | 0.0 | 0.0 | +33a860e2-992f-4355-ab24-85b4a2576f90 / -— |
| Jogador 2 | 3-6 | 365 | MOVE_BENCH | FAST8 | 94.0 | 7 | 38 | 3 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5565589666366577 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 366 | MOVE_BOARD | FAST8 | 94.0 | 7 | 38 | 3 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.042065247893333435 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 367 | SELL | FAST8 | 94.0 | 7 | 38 | 3 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11561538279056549 | 0.0 | 0.0 | +— / -33a860e2-992f-4355-ab24-85b4a2576f90 |
| Jogador 2 | 3-6 | 368 | MOVE_BENCH | FAST8 | 94.0 | 7 | 41 | 4 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5688377022743225 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 369 | SELL | FAST8 | 94.0 | 7 | 41 | 4 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35208699107170105 | 0.0 | 0.0 | +— / -4e116bc2-f686-4a17-adb1-a7b80865c159 |
| Jogador 2 | 3-6 | 370 | MOVE_BOARD | FAST8 | 94.0 | 7 | 45 | 4 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10777401924133301 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 371 | MOVE_BOARD | FAST8 | 94.0 | 7 | 45 | 4 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.30232033133506775 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 372 | PASS | FAST8 | 94.0 | 7 | 45 | 4 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 381 | BUY | FAST8 | 94.0 | 7 | 58 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.2438739538192749 | 0.0 | 0.0 | +e0445166-70a5-4135-a45e-ff238a95b228 / -— |
| Jogador 2 | 3-7 | 382 | BUY | FAST8 | 94.0 | 7 | 54 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3111892342567444 | 0.0 | 0.0 | +74b1cd6f-12f4-4287-a5f6-9d016663ccf5 / -— |
| Jogador 2 | 3-7 | 383 | BUY | FAST8 | 94.0 | 7 | 51 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31926313042640686 | 0.0 | 0.0 | +392a7da1-290c-48d8-81c8-206aa6823d5b / -— |
| Jogador 2 | 3-7 | 384 | MOVE_BENCH | FAST8 | 94.0 | 7 | 48 | 4 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6875687837600708 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 385 | MOVE_BOARD | FAST8 | 94.0 | 7 | 48 | 4 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17676235735416412 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 386 | SELL | FAST8 | 94.0 | 7 | 48 | 4 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10715384781360626 | 0.0 | 0.0 | +— / -392a7da1-290c-48d8-81c8-206aa6823d5b |
| Jogador 2 | 3-7 | 387 | MOVE_BOARD | FAST8 | 94.0 | 7 | 51 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 388 | MOVE_BOARD | FAST8 | 94.0 | 7 | 51 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0352528877556324 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 389 | SELL | FAST8 | 94.0 | 7 | 51 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5390703678131104 | 0.0 | 0.0 | +— / -74b1cd6f-12f4-4287-a5f6-9d016663ccf5 |
| Jogador 2 | 3-7 | 390 | BUY_XP | FAST8 | 94.0 | 7 | 54 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 391 | PASS | FAST8 | 94.0 | 7 | 50 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 402 | BUY | FAST8 | 94.0 | 7 | 63 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2734053432941437 | 0.0 | 0.0 | +59304448-26ee-4e38-a52e-014e22ece127 / -— |
| Jogador 2 | 4-1 | 403 | BUY | FAST8 | 94.0 | 7 | 59 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12068317085504532 | 0.0 | 0.0 | +1be0cdcc-ee10-44dc-ad1b-de9b53b25164 / -— |
| Jogador 2 | 4-1 | 404 | SELL | FAST8 | 94.0 | 7 | 56 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18020927906036377 | 0.0 | 0.0 | +— / -1be0cdcc-ee10-44dc-ad1b-de9b53b25164 |
| Jogador 2 | 4-1 | 405 | SELL | FAST8 | 94.0 | 7 | 59 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16561537981033325 | 0.0 | 0.0 | +— / -59304448-26ee-4e38-a52e-014e22ece127 |
| Jogador 2 | 4-1 | 406 | MOVE_BENCH | FAST8 | 94.0 | 7 | 63 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3871157169342041 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 407 | BUY | FAST8 | 94.0 | 7 | 63 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31233274936676025 | 0.0 | 0.0 | +1d7ccf69-9aaa-4f0c-81ed-a94ef995d915 / -— |
| Jogador 2 | 4-1 | 408 | MOVE_BENCH | FAST8 | 94.0 | 7 | 61 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3762657642364502 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 409 | PASS | FAST8 | 94.0 | 7 | 61 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0045661586336791515 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 422 | BUY | FAST8 | 94.0 | 7 | 75 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.832404375076294 | 0.0 | 0.0 | +9cb61b5c-2c8a-43a2-a854-517f4377f6db / -— |
| Jogador 2 | 4-2 | 423 | BUY | FAST8 | 94.0 | 7 | 73 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27220025658607483 | 0.0 | 0.0 | +3fdd5708-2e07-4636-a598-d872f57e1c16 / -— |
| Jogador 2 | 4-2 | 424 | PASS | FAST8 | 94.0 | 7 | 70 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08673300594091415 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 441 | BUY | FAST8 | 94.0 | 7 | 84 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0040572881698608 | 0.0 | 0.0 | +6538f28f-845f-4f45-92bf-120931553bec / -1d7ccf69-9aaa-4f0c-81ed-a94ef995d915,9cb61b5c-2c8a-43a2-a854-517f4377f6db |
| Jogador 2 | 4-3 | 442 | SELL | FAST8 | 94.0 | 7 | 82 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014999999664723873 | 0.0 | 0.0 | +— / -3fdd5708-2e07-4636-a598-d872f57e1c16 |
| Jogador 2 | 4-3 | 443 | SELL | FAST8 | 94.0 | 7 | 85 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4084714353084564 | 0.0 | 0.0 | +— / -6538f28f-845f-4f45-92bf-120931553bec |
| Jogador 2 | 4-3 | 444 | PASS | FAST8 | 94.0 | 7 | 90 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02149570919573307 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 461 | BUY | FAST8 | 94.0 | 7 | 104 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.921637773513794 | 0.0 | 0.0 | +696f53ae-1413-47cc-b491-9870b7bcba51 / -— |
| Jogador 2 | 4-4 | 462 | BUY | FAST8 | 94.0 | 7 | 101 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11217053234577179 | 0.0 | 0.0 | +e1867f53-f97a-4c7a-bce3-24aa037ce27f / -— |
| Jogador 2 | 4-4 | 463 | PASS | FAST8 | 94.0 | 7 | 98 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1364365816116333 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 481 | BUY | FAST8 | 94.0 | 7 | 111 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03974410519003868 | 0.0 | 0.0 | +8995f621-b355-44ec-816e-797184bdc266 / -— |
| Jogador 2 | 4-5 | 482 | PASS | FAST8 | 94.0 | 7 | 108 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15592357516288757 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 500 | PASS | FAST8 | 94.0 | 7 | 122 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1843399703502655 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 512 | PASS | FAST8 | 94.0 | 7 | 136 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05386143550276756 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 531 | EQUIP_FROM_INVENTORY | FAST8 | 94.0 | 7 | 149 | 5 | 40.0 | Colosso/DA_18_Sejuani | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 532 | BUY | FAST8 | 94.0 | 7 | 149 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.03547284007072449 | 0.0 | 0.0 | +8b75555c-d84d-4b8a-8d6c-012585a05b99 / -— |
| Jogador 2 | 5-1 | 533 | PASS | FAST8 | 94.0 | 7 | 144 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.059928473085165024 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 549 | BUY | FAST8 | 94.0 | 7 | 158 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.42657822370529175 | 0.0 | 0.0 | +de8de4b5-48ea-4947-ae08-2b90d94b0fc1 / -— |
| Jogador 2 | 5-2 | 550 | BUY | FAST8 | 94.0 | 7 | 154 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8062605857849121 | 0.0 | 0.0 | +b70671f9-0d78-4ae8-bd13-0267c96e7207 / -— |
| Jogador 2 | 5-2 | 551 | BUY | FAST8 | 94.0 | 7 | 151 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.21922539174556732 | 0.0 | 0.0 | +d633d2d8-1b5e-49cf-ac47-114c6ad29cf8 / -— |
| Jogador 2 | 5-2 | 552 | BUY | FAST8 | 94.0 | 7 | 148 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.04151322320103645 | 0.0 | 0.0 | +24b29fe6-466c-42d5-9f92-5d6114f0f98f / -— |
| Jogador 2 | 5-2 | 553 | PASS | FAST8 | 94.0 | 7 | 146 | 5 | 40.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.06146179884672165 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 562 | SELL | FAST8 | 79.0 | 7 | 156 | 5 | 40.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.025297699496150017 | 0.0 | 0.0 | +— / -24b29fe6-466c-42d5-9f92-5d6114f0f98f |
| Jogador 2 | 5-3 | 563 | BUY | FAST8 | 79.0 | 7 | 158 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8383621573448181 | 0.0 | 0.0 | +0a6546e5-8a3b-461e-ad5d-3dbd49f21e2c / -— |
| Jogador 2 | 5-3 | 564 | SELL | FAST8 | 79.0 | 7 | 156 | 5 | 40.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03799999877810478 | 0.0 | 0.0 | +— / -d633d2d8-1b5e-49cf-ac47-114c6ad29cf8 |
| Jogador 2 | 5-3 | 565 | BUY | FAST8 | 79.0 | 7 | 159 | 5 | 40.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9499820470809937 | 0.0 | 0.0 | +811fcf1f-2023-4c36-a961-d61cb0dd68d0 / -0a6546e5-8a3b-461e-ad5d-3dbd49f21e2c,63304cf5-4aa7-473e-9bfb-ec04cd68ebbd |
| Jogador 2 | 5-3 | 566 | BUY | FAST8 | 79.0 | 7 | 157 | 5 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.11904367059469223 | 0.0 | 0.0 | +952ea2b4-387d-455d-b1ad-fb0de8c46e47 / -— |
| Jogador 2 | 5-3 | 567 | SELL | FAST8 | 79.0 | 7 | 154 | 5 | 36.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.035538461059331894 | 0.0 | 0.0 | +— / -e1867f53-f97a-4c7a-bce3-24aa037ce27f |
| Jogador 2 | 5-3 | 568 | BUY | FAST8 | 79.0 | 7 | 157 | 5 | 36.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2590157389640808 | 0.0 | 0.0 | +685fc2a9-6a67-445e-ab34-59ec1f986f8e / -— |
| Jogador 2 | 5-3 | 569 | PASS | FAST8 | 79.0 | 7 | 154 | 5 | 36.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.06765809655189514 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 573 | MOVE_BENCH | FAST8 | 79.0 | 7 | 154 | 5 | 36.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5784424543380737 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 579 | BUY | FAST8 | 64.0 | 7 | 165 | 5 | 44.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.049226757138967514 | 0.0 | 0.0 | +f32e50e0-1430-4549-a1dd-a8473ffe0bd4 / -— |
| Jogador 2 | 5-4 | 580 | SELL | FAST8 | 64.0 | 7 | 160 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -685fc2a9-6a67-445e-ab34-59ec1f986f8e |
| Jogador 2 | 5-4 | 581 | BUY | FAST8 | 64.0 | 7 | 163 | 5 | 44.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.16992910206317902 | 0.0 | 0.0 | +50b2e4fa-9c04-41a2-a20a-4f7b5af8e2de / -— |
| Jogador 2 | 5-4 | 582 | SELL | FAST8 | 64.0 | 7 | 160 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.029999999329447746 | 0.0 | 0.0 | +— / -50b2e4fa-9c04-41a2-a20a-4f7b5af8e2de |
| Jogador 2 | 5-4 | 583 | BUY | FAST8 | 64.0 | 7 | 163 | 5 | 44.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8442485332489014 | 0.0 | 0.0 | +5a6985d6-5377-425c-b4a3-c53dc138b288 / -— |
| Jogador 2 | 5-4 | 584 | PASS | FAST8 | 64.0 | 7 | 162 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07395055145025253 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 592 | SELL | FAST8 | 64.0 | 7 | 173 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.002850503195077181 | 0.0 | 0.0 | +— / -952ea2b4-387d-455d-b1ad-fb0de8c46e47 |
| Jogador 2 | 5-5 | 593 | BUY | FAST8 | 64.0 | 7 | 176 | 5 | 44.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7146946787834167 | 0.0 | 0.0 | +a492f78e-91f0-48cb-891a-6518551da328 / -— |
| Jogador 2 | 5-5 | 594 | SELL | FAST8 | 64.0 | 7 | 172 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.7260653972625732 | 0.0 | 0.0 | +— / -5a6985d6-5377-425c-b4a3-c53dc138b288 |
| Jogador 2 | 5-5 | 595 | BUY | FAST8 | 64.0 | 7 | 173 | 5 | 44.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04383157938718796 | 0.0 | 0.0 | +2f75fcd7-1405-49fd-8a0c-649c1f8a9f09 / -— |
| Jogador 2 | 5-5 | 596 | SELL | FAST8 | 64.0 | 7 | 170 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.012081043794751167 | 0.0 | 0.0 | +— / -2f75fcd7-1405-49fd-8a0c-649c1f8a9f09 |
| Jogador 2 | 5-5 | 597 | BUY | FAST8 | 64.0 | 7 | 173 | 5 | 44.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.04092985764145851 | 0.0 | 0.0 | +5821f43b-b898-4842-b309-d175f2284a84 / -— |
| Jogador 2 | 5-5 | 598 | PASS | FAST8 | 64.0 | 7 | 171 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.08113761246204376 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 609 | SELL | FAST8 | 49.0 | 7 | 182 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.025303980335593224 | 0.0 | 0.0 | +— / -5821f43b-b898-4842-b309-d175f2284a84 |
| Jogador 2 | 5-6 | 610 | BUY | FAST8 | 49.0 | 7 | 184 | 5 | 44.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.13801531493663788 | 0.0 | 0.0 | +b2566e66-ba8b-4ec9-9875-e08ce45cd7a1 / -— |
| Jogador 2 | 5-6 | 611 | SELL | FAST8 | 49.0 | 7 | 180 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.02476923167705536 | 0.0 | 0.0 | +— / -b2566e66-ba8b-4ec9-9875-e08ce45cd7a1 |
| Jogador 2 | 5-6 | 612 | BUY | FAST8 | 49.0 | 7 | 184 | 5 | 44.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1019749566912651 | 0.0 | 0.0 | +a5deb295-89d5-4573-8ace-e370a0718266 / -— |
| Jogador 2 | 5-6 | 613 | SELL | FAST8 | 49.0 | 7 | 181 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.002851327648386359 | 0.0 | 0.0 | +— / -a5deb295-89d5-4573-8ace-e370a0718266 |
| Jogador 2 | 5-6 | 614 | BUY | FAST8 | 49.0 | 7 | 184 | 5 | 44.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.11411093920469284 | 0.0 | 0.0 | +b701c6c1-2e19-44b9-ad6e-e5d64e1d364c / -— |
| Jogador 2 | 5-6 | 615 | PASS | FAST8 | 49.0 | 7 | 182 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09006758034229279 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 622 | SELL | FAST8 | 49.0 | 7 | 193 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0370769239962101 | 0.0 | 0.0 | +— / -b701c6c1-2e19-44b9-ad6e-e5d64e1d364c |
| Jogador 2 | 5-7 | 623 | BUY | FAST8 | 49.0 | 7 | 195 | 5 | 44.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7634516358375549 | 0.0 | 0.0 | +4e6b6f57-7f94-46ba-b832-c3198d4a5949 / -— |
| Jogador 2 | 5-7 | 624 | SELL | FAST8 | 49.0 | 7 | 192 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.04600000008940697 | 0.0 | 0.0 | +— / -de8de4b5-48ea-4947-ae08-2b90d94b0fc1 |
| Jogador 2 | 5-7 | 625 | BUY | FAST8 | 49.0 | 7 | 196 | 5 | 44.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03230801597237587 | 0.0 | 0.0 | +b6883c6a-7149-4088-8506-20bd8dfed6a5 / -— |
| Jogador 2 | 5-7 | 626 | SELL | FAST8 | 49.0 | 7 | 192 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.014307692646980286 | 0.0 | 0.0 | +— / -b6883c6a-7149-4088-8506-20bd8dfed6a5 |
| Jogador 2 | 5-7 | 627 | BUY | FAST8 | 49.0 | 7 | 196 | 5 | 44.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2668594717979431 | 0.0 | 0.0 | +d22aa2b7-7c7c-4d47-89be-0f1b8755971c / -— |
| Jogador 2 | 5-7 | 628 | PASS | FAST8 | 49.0 | 7 | 192 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09831636399030685 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 638 | EQUIP_FROM_INVENTORY | FAST8 | 49.0 | 7 | 203 | 5 | 44.0 | Colosso/DA_18_Sejuani | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 639 | EQUIP_FROM_INVENTORY | FAST8 | 49.0 | 7 | 203 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY, CRAFT_AND_EQUIP | True | — | 0.1168031096458435 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 640 | SELL | FAST8 | 49.0 | 7 | 203 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04938461631536484 | 0.0 | 0.0 | +— / -d22aa2b7-7c7c-4d47-89be-0f1b8755971c |
| Jogador 2 | 6-1 | 641 | BUY | FAST8 | 49.0 | 7 | 207 | 5 | 44.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.22118304669857025 | 0.0 | 0.0 | +499f10b9-47ba-4cab-add1-31b452acae6d / -— |
| Jogador 2 | 6-1 | 642 | PASS | FAST8 | 49.0 | 7 | 204 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10499999672174454 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 652 | SELL | STABILIZE | 31.0 | 7 | 215 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03799999877810478 | 0.0 | 0.0 | +— / -499f10b9-47ba-4cab-add1-31b452acae6d |
| Jogador 2 | 6-2 | 653 | BUY | STABILIZE | 31.0 | 7 | 218 | 5 | 44.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.038896989077329636 | 0.0 | 0.0 | +95eba9e8-10f5-48d5-86de-3d9a446b2e65 / -— |
| Jogador 2 | 6-2 | 654 | SELL | STABILIZE | 31.0 | 7 | 215 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.035538461059331894 | 0.0 | 0.0 | +— / -95eba9e8-10f5-48d5-86de-3d9a446b2e65 |
| Jogador 2 | 6-2 | 655 | BUY | STABILIZE | 31.0 | 7 | 218 | 5 | 44.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.007395484484732151 | 0.0 | 0.0 | +eb418af1-c963-4da2-b052-86a153fc5ba1 / -— |
| Jogador 2 | 6-2 | 656 | PASS | STABILIZE | 31.0 | 7 | 216 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10499999672174454 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 667 | SELL | ALL_IN | 13.0 | 7 | 228 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.02784615382552147 | 0.0 | 0.0 | +— / -eb418af1-c963-4da2-b052-86a153fc5ba1 |
| Jogador 2 | 6-3 | 668 | BUY | ALL_IN | 13.0 | 7 | 230 | 5 | 44.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.09218582510948181 | 0.0 | 0.0 | +3faf4ab2-44b3-4779-985b-658c64791c28 / -— |
| Jogador 2 | 6-3 | 669 | SELL | ALL_IN | 13.0 | 7 | 226 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.014307692646980286 | 0.0 | 0.0 | +— / -3faf4ab2-44b3-4779-985b-658c64791c28 |
| Jogador 2 | 6-3 | 670 | BUY | ALL_IN | 13.0 | 7 | 230 | 5 | 44.0 | Colosso/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9045729637145996 | 0.0 | 0.0 | +8756c125-e3d6-4f40-80d2-a6bf20e7b1c7 / -— |
| Jogador 2 | 6-3 | 671 | PASS | ALL_IN | 13.0 | 7 | 227 | 5 | 44.0 | Colosso/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.1550000011920929 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 681 | PASS | ALL_IN | 0.0 | 7 | 227 | 5 | 0.0 | Colosso/DA_18_Sejuani | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 695 | PASS | ALL_IN | 0.0 | 7 | 227 | 5 | 0.0 | Colosso/DA_18_Sejuani | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 709 | PASS | ALL_IN | 0.0 | 7 | 227 | 5 | 0.0 | Colosso/DA_18_Sejuani | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-7 | 719 | PASS | ALL_IN | 0.0 | 7 | 227 | 5 | 0.0 | Colosso/DA_18_Sejuani | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-1 | 729 | PASS | ALL_IN | 0.0 | 7 | 227 | 5 | 0.0 | Colosso/DA_18_Sejuani | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-2 | 741 | PASS | ALL_IN | 0.0 | 7 | 227 | 5 | 0.0 | Colosso/DA_18_Sejuani | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 26 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.28737619519233704 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.054392240941524506 | 0.0 | 0.0 | +268b29b3-1068-470f-9fe2-e319d1874787 / -— |
| Jogador 3 | 1-2 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.022582225501537323 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 35 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.17468135058879852 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 36 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.0740484744310379 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 37 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4175858199596405 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 38 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 39 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.13100743293762207 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 40 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 41 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.06377681344747543 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 42 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.22864218056201935 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 43 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 57 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9768147468566895 | 0.0 | 0.0 | +477d3aa4-2130-4a0e-8254-2688ac860569 / -— |
| Jogador 3 | 1-3 | 58 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23320984840393066 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 60 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5320343375205994 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 61 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 62 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 83 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23191846907138824 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 84 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9553731083869934 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 85 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3236399292945862 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 86 | PASS | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 109 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 8 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5486028790473938 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 110 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3096083402633667 | 0.0 | 0.0 | +c70251e8-af44-4466-808f-d49e9e5f57e9 / -— |
| Jogador 3 | 2-1 | 111 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26234421133995056 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 112 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07094134390354156 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 113 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.023469049483537674 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 114 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3232891857624054 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 115 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 116 | PASS | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 133 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 11 | 1 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020842211320996284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 134 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 11 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3232569098472595 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 135 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 11 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06319410353899002 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 136 | PASS | STABILIZE | 96.0 | 4 | 11 | 1 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 157 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 18 | 1 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19612598419189453 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 158 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 18 | 1 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020964087918400764 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 159 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 18 | 1 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7167769074440002 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 160 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 18 | 1 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2296719253063202 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 161 | PASS | STABILIZE | 90.0 | 4 | 18 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 182 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 25 | 2 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02080460451543331 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 183 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 25 | 2 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32325002551078796 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 184 | MOVE_BOARD | STABILIZE | 90.0 | 4 | 25 | 2 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 185 | PASS | STABILIZE | 90.0 | 4 | 25 | 2 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 205 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 32 | 3 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02074502967298031 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 206 | MOVE_BOARD | STABILIZE | 90.0 | 4 | 32 | 3 | 10.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07792959362268448 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 207 | MOVE_BOARD | STABILIZE | 90.0 | 4 | 32 | 3 | 10.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012479945085942745 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 208 | SELL | STABILIZE | 90.0 | 4 | 32 | 3 | 10.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.329153835773468 | 0.0 | 0.0 | +— / -c83ad0c5-f046-4834-8d0e-6dac3e49cdef |
| Jogador 3 | 2-5 | 209 | BUY | STABILIZE | 90.0 | 4 | 33 | 3 | 10.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.04940825328230858 | 0.0 | 0.0 | +cdb48eea-209d-4833-9a68-79df61990332 / -— |
| Jogador 3 | 2-5 | 210 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 30 | 3 | 10.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48834508657455444 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 211 | SELL | STABILIZE | 90.0 | 4 | 30 | 3 | 14.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7630000114440918 | 0.0 | 0.0 | +— / -477d3aa4-2130-4a0e-8254-2688ac860569 |
| Jogador 3 | 2-5 | 212 | BUY | STABILIZE | 90.0 | 4 | 31 | 3 | 14.0 | Fera do Rift/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.010197639465332 | 0.0 | 0.0 | +03a4a455-ebf6-4587-8ab3-acd2b1038822 / -— |
| Jogador 3 | 2-5 | 213 | MOVE_BENCH | STABILIZE | 90.0 | 4 | 30 | 3 | 14.0 | Fera do Rift/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18488559126853943 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 214 | BUY_XP | STABILIZE | 90.0 | 4 | 30 | 3 | 14.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025699999183416367 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 215 | PASS | STABILIZE | 90.0 | 5 | 26 | 2 | 14.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 227 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 35 | 3 | 14.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3993164002895355 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 228 | BUY | SLOWROLL | 90.0 | 5 | 35 | 3 | 16.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8865983486175537 | 0.0 | 0.0 | +07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 / -— |
| Jogador 3 | 2-6 | 229 | MOVE_BENCH | SLOWROLL | 90.0 | 5 | 33 | 3 | 16.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3072105050086975 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 230 | MOVE_BOARD | SLOWROLL | 90.0 | 5 | 33 | 3 | 18.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0024998392909765244 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 231 | MOVE_BOARD | SLOWROLL | 90.0 | 5 | 33 | 3 | 18.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11087857931852341 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 232 | MOVE_BOARD | SLOWROLL | 90.0 | 5 | 33 | 3 | 18.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05787229165434837 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 233 | MOVE_BOARD | SLOWROLL | 90.0 | 5 | 33 | 3 | 18.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 234 | MOVE_BOARD | SLOWROLL | 90.0 | 5 | 33 | 3 | 18.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11087857931852341 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 235 | PASS | SLOWROLL | 90.0 | 5 | 33 | 3 | 18.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 250 | BUY | SLOWROLL | 85.0 | 5 | 41 | 4 | 18.0 | Devastador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9538214206695557 | 0.0 | 0.0 | +bca8862c-5e5b-4a51-9173-79218fbfea3d / -07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0,c70251e8-af44-4466-808f-d49e9e5f57e9 |
| Jogador 3 | 2-7 | 251 | MOVE_BENCH | SLOWROLL | 85.0 | 5 | 39 | 3 | 10.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2233922928571701 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 252 | MOVE_BENCH | SLOWROLL | 85.0 | 5 | 39 | 3 | 18.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4112132489681244 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 253 | BUY | SLOWROLL | 85.0 | 5 | 39 | 3 | 20.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3916921615600586 | 0.0 | 0.0 | +79786887-d318-4836-b2f0-c0f03e86cbe5 / -— |
| Jogador 3 | 2-7 | 254 | MOVE_BENCH | SLOWROLL | 85.0 | 5 | 36 | 3 | 20.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15121199190616608 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 255 | MOVE_BOARD | SLOWROLL | 85.0 | 5 | 36 | 3 | 24.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007495662663131952 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 256 | MOVE_BOARD | SLOWROLL | 85.0 | 5 | 36 | 3 | 24.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03456547111272812 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 257 | MOVE_BOARD | SLOWROLL | 85.0 | 5 | 36 | 3 | 24.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 258 | MOVE_BOARD | SLOWROLL | 85.0 | 5 | 36 | 3 | 24.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11087857931852341 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 259 | PASS | SLOWROLL | 85.0 | 5 | 36 | 3 | 24.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 270 | MOVE_BENCH | SLOWROLL | 85.0 | 5 | 44 | 4 | 24.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7775895595550537 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 271 | MOVE_BENCH | SLOWROLL | 85.0 | 5 | 44 | 4 | 18.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22809135913848877 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 272 | PASS | SLOWROLL | 85.0 | 5 | 44 | 4 | 24.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02250000089406967 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 289 | MOVE_BOARD | SLOWROLL | 76.0 | 5 | 54 | 5 | 24.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 290 | MOVE_BOARD | SLOWROLL | 76.0 | 5 | 54 | 5 | 24.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00998972449451685 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 291 | MOVE_BOARD | SLOWROLL | 76.0 | 5 | 54 | 5 | 24.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 292 | MOVE_BOARD | SLOWROLL | 76.0 | 5 | 54 | 5 | 24.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03215137496590614 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 293 | SELL | SLOWROLL | 76.0 | 5 | 54 | 5 | 24.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7448578476905823 | 0.0 | 0.0 | +— / -03a4a455-ebf6-4587-8ab3-acd2b1038822 |
| Jogador 3 | 3-2 | 294 | BUY | SLOWROLL | 76.0 | 5 | 55 | 5 | 24.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.12894943356513977 | 0.0 | 0.0 | +6a5bf4a0-0a6d-4ee6-9b76-3b4923ba1d97 / -— |
| Jogador 3 | 3-2 | 295 | MOVE_BENCH | SLOWROLL | 76.0 | 5 | 52 | 5 | 24.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2893443703651428 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 296 | SELL | SLOWROLL | 76.0 | 5 | 52 | 5 | 28.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32900670170783997 | 0.0 | 0.0 | +— / -268b29b3-1068-470f-9fe2-e319d1874787 |
| Jogador 3 | 3-2 | 297 | MOVE_BOARD | SLOWROLL | 76.0 | 5 | 53 | 5 | 28.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.04875248298048973 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 298 | MOVE_BOARD | SLOWROLL | 76.0 | 5 | 53 | 5 | 28.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0024998392909765244 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 299 | PASS | SLOWROLL | 76.0 | 5 | 53 | 5 | 28.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.0009603406069800258 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 306 | BUY | SLOWROLL | 65.0 | 5 | 64 | 5 | 28.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.012649482116103172 | 0.0 | 0.0 | +527f78df-1e51-4731-9175-1c4812aa82ad / -— |
| Jogador 3 | 3-3 | 307 | MOVE_BENCH | SLOWROLL | 65.0 | 5 | 60 | 5 | 28.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6356441378593445 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 308 | MOVE_BENCH | SLOWROLL | 65.0 | 5 | 60 | 5 | 30.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9225466847419739 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 309 | PASS | SLOWROLL | 65.0 | 5 | 60 | 5 | 34.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05363621562719345 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 323 | BUY_XP | SLOWROLL | 55.0 | 5 | 71 | 5 | 34.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 324 | BUY_XP | SLOWROLL | 55.0 | 5 | 67 | 5 | 34.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2321999967098236 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 325 | MOVE_BENCH | SLOWROLL | 55.0 | 6 | 63 | 5 | 34.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6390669941902161 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 326 | BUY | SLOWROLL | 55.0 | 6 | 63 | 5 | 36.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08781086653470993 | 0.0 | 0.0 | +f5c14a50-b095-4a36-995f-2a8514e46f1c / -— |
| Jogador 3 | 3-4 | 327 | MOVE_BENCH | SLOWROLL | 55.0 | 6 | 61 | 5 | 36.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4698743522167206 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 328 | MOVE_BOARD | SLOWROLL | 55.0 | 6 | 61 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10906810313463211 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 329 | PASS | SLOWROLL | 55.0 | 6 | 61 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0045661586336791515 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 342 | BUY | SLOWROLL | 55.0 | 6 | 72 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09756132960319519 | 0.0 | 0.0 | +ccdd8153-af58-4fe7-994c-d49f0a7a17f8 / -— |
| Jogador 3 | 3-5 | 343 | BUY | SLOWROLL | 55.0 | 6 | 68 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33944061398506165 | 0.0 | 0.0 | +aaa84ce8-7919-4ec3-92eb-cc03a9decca9 / -— |
| Jogador 3 | 3-5 | 344 | MOVE_BOARD | SLOWROLL | 55.0 | 6 | 65 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04875248298048973 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 345 | MOVE_BOARD | SLOWROLL | 55.0 | 6 | 65 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10906810313463211 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 346 | MOVE_BOARD | SLOWROLL | 55.0 | 6 | 65 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10226842761039734 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 347 | PASS | SLOWROLL | 55.0 | 6 | 65 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.060928720980882645 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 362 | BUY | SLOWROLL | 43.0 | 6 | 77 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3489488363265991 | 0.0 | 0.0 | +0e31b1ec-3ead-480e-8577-f59bb5486d00 / -— |
| Jogador 3 | 3-6 | 363 | BUY | SLOWROLL | 43.0 | 6 | 75 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03806144371628761 | 0.0 | 0.0 | +b75c9bc5-9bc7-465a-a97c-59156e5c482d / -— |
| Jogador 3 | 3-6 | 364 | PASS | SLOWROLL | 43.0 | 6 | 72 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07197222113609314 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 381 | BUY | SLOWROLL | 43.0 | 6 | 83 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4608703553676605 | 0.0 | 0.0 | +9028d514-586b-4d0e-b042-07389323c8cf / -— |
| Jogador 3 | 3-7 | 382 | BUY | SLOWROLL | 43.0 | 6 | 80 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16861900687217712 | 0.0 | 0.0 | +bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed / -— |
| Jogador 3 | 3-7 | 383 | BUY | SLOWROLL | 43.0 | 6 | 77 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1945296972990036 | 0.0 | 0.0 | +cbcde5b6-8f03-4d96-ade5-1ef113ab25bc / -— |
| Jogador 3 | 3-7 | 384 | PASS | SLOWROLL | 43.0 | 6 | 76 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07862517982721329 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 402 | BUY | SLOWROLL | 43.0 | 6 | 86 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7447434067726135 | 0.0 | 0.0 | +f64919a5-eb2c-4e23-91ed-0067b3d90951 / -9028d514-586b-4d0e-b042-07389323c8cf,b75c9bc5-9bc7-465a-a97c-59156e5c482d |
| Jogador 3 | 4-1 | 403 | PASS | SLOWROLL | 43.0 | 6 | 83 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10875604301691055 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 422 | BUY | STABILIZE | 30.0 | 6 | 93 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.691326916217804 | 0.0 | 0.0 | +0534477f-2ff8-47a7-b71b-1a1d5430589e / -— |
| Jogador 3 | 4-2 | 423 | BUY | STABILIZE | 30.0 | 6 | 90 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6964917778968811 | 0.0 | 0.0 | +bd0fdf98-49ca-4e4b-b4ec-72ac9a91e87b / -— |
| Jogador 3 | 4-2 | 424 | PASS | STABILIZE | 30.0 | 6 | 88 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020212503150105476 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 441 | SELL | STABILIZE | 30.0 | 6 | 99 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0008937044185586274 | 0.0 | 0.0 | +— / -bde3843b-3d2b-4ea9-a3f8-ddd1556b61ed |
| Jogador 3 | 4-3 | 442 | BUY | STABILIZE | 30.0 | 6 | 102 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24013113975524902 | 0.0 | 0.0 | +395ae945-c8a2-4d80-98a4-5eb6887b8f78 / -— |
| Jogador 3 | 4-3 | 443 | SELL | STABILIZE | 30.0 | 6 | 98 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29307693243026733 | 0.0 | 0.0 | +— / -cbcde5b6-8f03-4d96-ade5-1ef113ab25bc |
| Jogador 3 | 4-3 | 444 | BUY | STABILIZE | 30.0 | 6 | 99 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005652221851050854 | 0.0 | 0.0 | +3f488391-7117-4e28-b6cc-7416722351d4 / -— |
| Jogador 3 | 4-3 | 445 | PASS | STABILIZE | 30.0 | 6 | 96 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025420797988772392 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 461 | PASS | STABILIZE | 19.0 | 6 | 106 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03218884766101837 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 481 | SELL | STABILIZE | 19.0 | 6 | 116 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03696068003773689 | 0.0 | 0.0 | +— / -3f488391-7117-4e28-b6cc-7416722351d4 |
| Jogador 3 | 4-5 | 482 | BUY | STABILIZE | 19.0 | 6 | 119 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.819455087184906 | 0.0 | 0.0 | +d53646ff-bb49-4f82-b761-faa4657f01cc / -— |
| Jogador 3 | 4-5 | 483 | PASS | STABILIZE | 19.0 | 6 | 116 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.039204191416502 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 500 | SELL | ALL_IN | 8.0 | 6 | 127 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04938461631536484 | 0.0 | 0.0 | +— / -395ae945-c8a2-4d80-98a4-5eb6887b8f78 |
| Jogador 3 | 4-6 | 501 | BUY | ALL_IN | 8.0 | 6 | 131 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8771876096725464 | 0.0 | 0.0 | +d6a00f0c-4823-44d6-b326-67595876998d / -— |
| Jogador 3 | 4-6 | 502 | PASS | ALL_IN | 8.0 | 6 | 129 | 5 | 38.0 | Devastador/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09864433854818344 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 512 | PASS | ALL_IN | 0.0 | 6 | 129 | 5 | 0.0 | Devastador/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 531 | PASS | ALL_IN | 0.0 | 6 | 129 | 5 | 0.0 | Devastador/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 549 | PASS | ALL_IN | 0.0 | 6 | 129 | 5 | 0.0 | Devastador/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 562 | PASS | ALL_IN | 0.0 | 6 | 129 | 5 | 0.0 | Devastador/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 579 | PASS | ALL_IN | 0.0 | 6 | 129 | 5 | 0.0 | Devastador/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 592 | PASS | ALL_IN | 0.0 | 6 | 129 | 5 | 0.0 | Devastador/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 609 | PASS | ALL_IN | 0.0 | 6 | 129 | 5 | 0.0 | Devastador/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 622 | PASS | ALL_IN | 0.0 | 6 | 129 | 5 | 0.0 | Devastador/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 638 | PASS | ALL_IN | 0.0 | 6 | 129 | 5 | 0.0 | Devastador/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-2 | 652 | PASS | ALL_IN | 0.0 | 6 | 129 | 5 | 0.0 | Devastador/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-3 | 667 | PASS | ALL_IN | 0.0 | 6 | 129 | 5 | 0.0 | Devastador/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-4 | 681 | PASS | ALL_IN | 0.0 | 6 | 129 | 5 | 0.0 | Devastador/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-5 | 695 | PASS | ALL_IN | 0.0 | 6 | 129 | 5 | 0.0 | Devastador/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-6 | 709 | PASS | ALL_IN | 0.0 | 6 | 129 | 5 | 0.0 | Devastador/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-7 | 719 | PASS | ALL_IN | 0.0 | 6 | 129 | 5 | 0.0 | Devastador/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 7-1 | 729 | PASS | ALL_IN | 0.0 | 6 | 129 | 5 | 0.0 | Devastador/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 7-2 | 741 | PASS | ALL_IN | 0.0 | 6 | 129 | 5 | 0.0 | Devastador/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.019615383818745613 | 0.0 | 0.0 | +— / -9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +1903eae4-bd37-4ed8-bbae-28177e859592 / -— |
| Jogador 4 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.5989939570426941 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.25464189052581787 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13295239210128784 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 35 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.10718601942062378 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 36 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.009241865947842598 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 37 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.07476295530796051 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 38 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4108360707759857 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 39 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.14372901618480682 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 40 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 41 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 42 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 57 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.012479945085942745 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 58 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 59 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 60 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 83 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9723950624465942 | 0.0 | 0.0 | +cd27dcd8-0a45-4196-be66-fbe6eb4a0793 / -— |
| Jogador 4 | 1-4 | 84 | BUY_XP | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.047200001776218414 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 85 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5216770768165588 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 86 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 87 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 88 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 109 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 110 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 111 | PASS | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 133 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 9 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.051634397357702255 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 134 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 9 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 135 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 9 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 136 | PASS | STABILIZE | 96.0 | 4 | 9 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 157 | BUY | STABILIZE | 96.0 | 4 | 16 | 1 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1179684400558472 | 0.0 | 0.0 | +ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 / -1903eae4-bd37-4ed8-bbae-28177e859592,cd27dcd8-0a45-4196-be66-fbe6eb4a0793 |
| Jogador 4 | 2-3 | 158 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 15 | 1 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.374785840511322 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 159 | BUY | STABILIZE | 96.0 | 4 | 15 | 1 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.015149380080401897 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 4 | 2-3 | 160 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 13 | 1 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9316311478614807 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 161 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 13 | 1 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06435901671648026 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 162 | SELL | STABILIZE | 96.0 | 4 | 13 | 1 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4160713255405426 | 0.0 | 0.0 | +— / -ef8c607c-ca68-44e4-ba2e-ae23d10a1e81 |
| Jogador 4 | 2-3 | 163 | BUY | STABILIZE | 96.0 | 4 | 16 | 1 | 8.0 | —/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9625402092933655 | 0.0 | 0.0 | +095246b2-70a1-44ff-9f62-3752ad86693a / -— |
| Jogador 4 | 2-3 | 164 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 15 | 1 | 8.0 | —/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48897185921669006 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 165 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 15 | 1 | 10.0 | —/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.16832441091537476 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 166 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 15 | 1 | 10.0 | —/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.10989046841859818 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 167 | PASS | STABILIZE | 96.0 | 4 | 15 | 1 | 10.0 | —/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 182 | BUY | STABILIZE | 91.0 | 5 | 21 | 2 | 10.0 | —/DA_18_LeBlanc | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0073251621797680855 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 4 | 2-4 | 183 | MOVE_BENCH | STABILIZE | 91.0 | 5 | 17 | 1 | 10.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4207392930984497 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 184 | BUY | STABILIZE | 91.0 | 5 | 17 | 1 | 18.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.05769207701086998 | 0.0 | 0.0 | +a229cc5e-9f28-4ff3-b652-eab994251c92 / -— |
| Jogador 4 | 2-4 | 185 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 15 | 1 | 18.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10816231369972229 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 186 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 15 | 1 | 18.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2607417404651642 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 187 | PASS | STABILIZE | 91.0 | 5 | 15 | 1 | 18.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 205 | BUY | STABILIZE | 91.0 | 5 | 21 | 2 | 18.0 | —/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37798598408699036 | 0.0 | 0.0 | +a92eca5d-299f-4f4d-a16b-d23981ef719f / -— |
| Jogador 4 | 2-5 | 206 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 18 | 1 | 18.0 | Devastador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10816231369972229 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 207 | MOVE_BOARD | STABILIZE | 91.0 | 5 | 18 | 1 | 18.0 | Devastador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 208 | PASS | STABILIZE | 91.0 | 5 | 18 | 1 | 18.0 | Devastador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 227 | BUY | STABILIZE | 86.0 | 5 | 25 | 2 | 18.0 | Devastador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4791712760925293 | 0.0 | 0.0 | +b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a / -— |
| Jogador 4 | 2-6 | 228 | MOVE_BOARD | STABILIZE | 86.0 | 5 | 22 | 2 | 18.0 | Devastador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007495662663131952 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 229 | MOVE_BOARD | STABILIZE | 86.0 | 5 | 22 | 2 | 18.0 | Devastador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 230 | MOVE_BOARD | STABILIZE | 86.0 | 5 | 22 | 2 | 18.0 | Devastador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1435474157333374 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 231 | MOVE_BOARD | STABILIZE | 86.0 | 5 | 22 | 2 | 18.0 | Devastador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07419530302286148 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 232 | MOVE_BOARD | STABILIZE | 86.0 | 5 | 22 | 2 | 18.0 | Devastador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10497637093067169 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 233 | SELL | STABILIZE | 86.0 | 5 | 22 | 2 | 18.0 | Devastador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3170478940010071 | 0.0 | 0.0 | +— / -a229cc5e-9f28-4ff3-b652-eab994251c92 |
| Jogador 4 | 2-6 | 234 | MOVE_BOARD | STABILIZE | 86.0 | 5 | 24 | 2 | 18.0 | Devastador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23000843822956085 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 235 | MOVE_BOARD | STABILIZE | 86.0 | 5 | 24 | 2 | 18.0 | Devastador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 236 | PASS | STABILIZE | 86.0 | 5 | 24 | 2 | 18.0 | Devastador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 250 | BUY | SLOWROLL | 81.0 | 5 | 32 | 3 | 18.0 | Devastador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12510016560554504 | 0.0 | 0.0 | +5e247068-fe03-467e-9e7d-ab85ade7fdae / -— |
| Jogador 4 | 2-7 | 251 | BUY | STABILIZE | 81.0 | 5 | 29 | 2 | 18.0 | Devastador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.1175481081008911 | 0.0 | 0.0 | +3d4fca52-8f58-4464-8cec-752fa99dbb3c / -095246b2-70a1-44ff-9f62-3752ad86693a,95829f2e-ad17-448d-a385-fdcf81872dc8 |
| Jogador 4 | 2-7 | 252 | BUY | STABILIZE | 81.0 | 5 | 28 | 2 | 14.0 | Devastador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3749900162220001 | 0.0 | 0.0 | +53a27943-148b-4522-9826-3f2e0b8a7858 / -— |
| Jogador 4 | 2-7 | 253 | BUY | STABILIZE | 81.0 | 5 | 27 | 2 | 14.0 | Devastador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44547176361083984 | 0.0 | 0.0 | +764470bb-9820-4e49-98f9-5a5f0ce5ca8f / -— |
| Jogador 4 | 2-7 | 254 | MOVE_BENCH | STABILIZE | 81.0 | 5 | 26 | 2 | 14.0 | Devastador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12587487697601318 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 255 | MOVE_BOARD | STABILIZE | 81.0 | 5 | 26 | 2 | 16.0 | Devastador/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009220493957400322 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 256 | MOVE_BENCH | STABILIZE | 81.0 | 5 | 26 | 2 | 16.0 | Fumegante/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6290122270584106 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 257 | MOVE_BOARD | STABILIZE | 81.0 | 5 | 26 | 2 | 22.0 | Fumegante/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 258 | MOVE_BOARD | STABILIZE | 81.0 | 5 | 26 | 2 | 22.0 | Fumegante/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17477719485759735 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 259 | PASS | STABILIZE | 81.0 | 5 | 26 | 2 | 22.0 | Fumegante/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 270 | BUY | STABILIZE | 81.0 | 5 | 34 | 3 | 22.0 | Fumegante/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03200946003198624 | 0.0 | 0.0 | +31aa0a5f-4d66-48c2-b6d4-b76ac220c752 / -— |
| Jogador 4 | 3-1 | 271 | BUY | STABILIZE | 81.0 | 5 | 31 | 3 | 22.0 | Fumegante/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7795732021331787 | 0.0 | 0.0 | +8052731e-e34c-4de7-84b1-2b986cfeddaa / -— |
| Jogador 4 | 3-1 | 272 | BUY | SLOWROLL | 81.0 | 5 | 30 | 3 | 22.0 | Fumegante/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05049460008740425 | 0.0 | 0.0 | +6bbf1aa9-e129-45c6-8668-699425d97c5d / -— |
| Jogador 4 | 3-1 | 273 | MOVE_BOARD | STABILIZE | 81.0 | 5 | 28 | 2 | 22.0 | Fumegante/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.324389785528183 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 274 | MOVE_BOARD | STABILIZE | 81.0 | 5 | 28 | 2 | 22.0 | Fumegante/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03313230350613594 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 275 | MOVE_BOARD | STABILIZE | 81.0 | 5 | 28 | 2 | 22.0 | Fumegante/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16371430456638336 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 276 | SELL | STABILIZE | 81.0 | 5 | 28 | 2 | 22.0 | Fumegante/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05374028533697128 | 0.0 | 0.0 | +— / -3d4fca52-8f58-4464-8cec-752fa99dbb3c |
| Jogador 4 | 3-1 | 277 | SELL | SLOWROLL | 81.0 | 5 | 31 | 3 | 22.0 | Fumegante/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19466932117938995 | 0.0 | 0.0 | +— / -6bbf1aa9-e129-45c6-8668-699425d97c5d |
| Jogador 4 | 3-1 | 278 | SELL | SLOWROLL | 81.0 | 5 | 33 | 3 | 22.0 | Fumegante/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17100000381469727 | 0.0 | 0.0 | +— / -31aa0a5f-4d66-48c2-b6d4-b76ac220c752 |
| Jogador 4 | 3-1 | 279 | SELL | SLOWROLL | 81.0 | 5 | 36 | 3 | 22.0 | Fumegante/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3435024321079254 | 0.0 | 0.0 | +— / -764470bb-9820-4e49-98f9-5a5f0ce5ca8f |
| Jogador 4 | 3-1 | 280 | PASS | SLOWROLL | 81.0 | 5 | 37 | 3 | 22.0 | Fumegante/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014999999664723873 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 289 | BUY | SLOWROLL | 81.0 | 5 | 46 | 4 | 22.0 | Fumegante/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12446418404579163 | 0.0 | 0.0 | +421bcbcb-ecb2-4af8-88d4-7be6cd284d27 / -— |
| Jogador 4 | 3-2 | 290 | BUY | SLOWROLL | 81.0 | 5 | 43 | 4 | 22.0 | Fumegante/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.729851245880127 | 0.0 | 0.0 | +d71a866d-0c5a-41c2-9996-0e179f062aa2 / -— |
| Jogador 4 | 3-2 | 291 | BUY | SLOWROLL | 81.0 | 5 | 42 | 4 | 22.0 | Fumegante/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8387022018432617 | 0.0 | 0.0 | +d9b43609-2c36-4fea-b26b-ea5bea6609b5 / -9e7d1da0-5190-4348-81b4-3a3f2129a8e5,d71a866d-0c5a-41c2-9996-0e179f062aa2 |
| Jogador 4 | 3-2 | 292 | BUY | SLOWROLL | 81.0 | 5 | 41 | 4 | 20.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27497944235801697 | 0.0 | 0.0 | +bbba5910-d3e3-4cd4-9b74-e308ca124f7c / -— |
| Jogador 4 | 3-2 | 293 | BUY | SLOWROLL | 81.0 | 5 | 40 | 4 | 20.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35493239760398865 | 0.0 | 0.0 | +3f253868-2de5-4189-95a0-705f62682958 / -— |
| Jogador 4 | 3-2 | 294 | SELL | SLOWROLL | 81.0 | 5 | 39 | 3 | 20.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08299999684095383 | 0.0 | 0.0 | +— / -3f253868-2de5-4189-95a0-705f62682958 |
| Jogador 4 | 3-2 | 295 | SELL | SLOWROLL | 81.0 | 5 | 40 | 4 | 20.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16300000250339508 | 0.0 | 0.0 | +— / -bbba5910-d3e3-4cd4-9b74-e308ca124f7c |
| Jogador 4 | 3-2 | 296 | MOVE_BENCH | SLOWROLL | 81.0 | 5 | 41 | 4 | 20.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5417791604995728 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 297 | MOVE_BOARD | SLOWROLL | 81.0 | 5 | 41 | 4 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30963295698165894 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 298 | MOVE_BOARD | SLOWROLL | 81.0 | 5 | 41 | 4 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 299 | PASS | SLOWROLL | 81.0 | 5 | 41 | 4 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 306 | BUY | SLOWROLL | 72.0 | 5 | 50 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21887582540512085 | 0.0 | 0.0 | +409b32b9-5280-4d79-b5b2-871ed597ba56 / -— |
| Jogador 4 | 3-3 | 307 | BUY | SLOWROLL | 72.0 | 5 | 48 | 4 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23483683168888092 | 0.0 | 0.0 | +58c38a13-23c5-4ac1-8601-f0636aeb33ab / -— |
| Jogador 4 | 3-3 | 308 | BUY | SLOWROLL | 72.0 | 5 | 45 | 4 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13972744345664978 | 0.0 | 0.0 | +52018505-08c9-471f-83b9-fd5066efe55a / -— |
| Jogador 4 | 3-3 | 309 | BUY | SLOWROLL | 72.0 | 5 | 43 | 4 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21340644359588623 | 0.0 | 0.0 | +e2ed7625-f3aa-43f0-936b-7322cb9d16f1 / -— |
| Jogador 4 | 3-3 | 310 | BUY | SLOWROLL | 72.0 | 5 | 42 | 4 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024876587092876434 | 0.0 | 0.0 | +ac8f2a7d-1627-4aa4-a35b-805bce651b0e / -— |
| Jogador 4 | 3-3 | 311 | SELL | SLOWROLL | 72.0 | 5 | 41 | 4 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019692307338118553 | 0.0 | 0.0 | +— / -ac8f2a7d-1627-4aa4-a35b-805bce651b0e |
| Jogador 4 | 3-3 | 312 | SELL | SLOWROLL | 72.0 | 5 | 42 | 4 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16776922345161438 | 0.0 | 0.0 | +— / -52018505-08c9-471f-83b9-fd5066efe55a |
| Jogador 4 | 3-3 | 313 | SELL | SLOWROLL | 72.0 | 5 | 44 | 4 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16730768978595734 | 0.0 | 0.0 | +— / -58c38a13-23c5-4ac1-8601-f0636aeb33ab |
| Jogador 4 | 3-3 | 314 | MOVE_BOARD | SLOWROLL | 72.0 | 5 | 47 | 4 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1277538239955902 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 315 | MOVE_BOARD | SLOWROLL | 72.0 | 5 | 47 | 4 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26878622174263 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 316 | PASS | SLOWROLL | 72.0 | 5 | 47 | 4 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 323 | BUY | SLOWROLL | 62.0 | 5 | 57 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2682235836982727 | 0.0 | 0.0 | +2acd0734-f0c3-42b1-9791-5c48e1aa46bc / -— |
| Jogador 4 | 3-4 | 324 | BUY | SLOWROLL | 62.0 | 5 | 55 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13411067426204681 | 0.0 | 0.0 | +7fd03119-ac82-49e1-b3bb-3a0caa31011f / -— |
| Jogador 4 | 3-4 | 325 | BUY | SLOWROLL | 62.0 | 5 | 53 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0501738078892231 | 0.0 | 0.0 | +4cf7dfe2-9d2c-4d45-803e-503eda810357 / -— |
| Jogador 4 | 3-4 | 326 | SELL | SLOWROLL | 62.0 | 5 | 52 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018103457987308502 | 0.0 | 0.0 | +— / -4cf7dfe2-9d2c-4d45-803e-503eda810357 |
| Jogador 4 | 3-4 | 327 | BUY | SLOWROLL | 62.0 | 5 | 53 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026852915063500404 | 0.0 | 0.0 | +d754fcfc-6d22-4bc0-8643-8f4bef9afda5 / -— |
| Jogador 4 | 3-4 | 328 | SELL | SLOWROLL | 62.0 | 5 | 52 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017692307010293007 | 0.0 | 0.0 | +— / -d754fcfc-6d22-4bc0-8643-8f4bef9afda5 |
| Jogador 4 | 3-4 | 329 | BUY | SLOWROLL | 62.0 | 5 | 53 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07986535876989365 | 0.0 | 0.0 | +e01be6cf-34fe-4057-aef3-c08c504794cf / -— |
| Jogador 4 | 3-4 | 330 | SELL | SLOWROLL | 62.0 | 5 | 52 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.032996609807014465 | 0.0 | 0.0 | +— / -e01be6cf-34fe-4057-aef3-c08c504794cf |
| Jogador 4 | 3-4 | 331 | SELL | SLOWROLL | 62.0 | 5 | 53 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17176923155784607 | 0.0 | 0.0 | +— / -7fd03119-ac82-49e1-b3bb-3a0caa31011f |
| Jogador 4 | 3-4 | 332 | SELL | SLOWROLL | 62.0 | 5 | 55 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014999999664723873 | 0.0 | 0.0 | +— / -2acd0734-f0c3-42b1-9791-5c48e1aa46bc |
| Jogador 4 | 3-4 | 333 | PASS | SLOWROLL | 62.0 | 5 | 57 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002654589945450425 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 342 | BUY | SLOWROLL | 62.0 | 5 | 68 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2682235836982727 | 0.0 | 0.0 | +62b9f2fe-f0ec-474d-9b5d-1c589c8fa2b2 / -— |
| Jogador 4 | 3-5 | 343 | BUY | SLOWROLL | 62.0 | 5 | 66 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23411066830158234 | 0.0 | 0.0 | +40f2a32f-1ace-4700-8a79-e6b5d3212036 / -— |
| Jogador 4 | 3-5 | 344 | BUY | SLOWROLL | 62.0 | 5 | 64 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13397902250289917 | 0.0 | 0.0 | +fe6546c3-86ef-40e1-aa7e-ff7e400fe628 / -— |
| Jogador 4 | 3-5 | 345 | SELL | SLOWROLL | 62.0 | 5 | 62 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04323076829314232 | 0.0 | 0.0 | +— / -fe6546c3-86ef-40e1-aa7e-ff7e400fe628 |
| Jogador 4 | 3-5 | 346 | BUY | SLOWROLL | 62.0 | 5 | 64 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2682235836982727 | 0.0 | 0.0 | +805375b9-df52-4342-b581-4b92fcd12033 / -— |
| Jogador 4 | 3-5 | 347 | SELL | SLOWROLL | 62.0 | 5 | 62 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -805375b9-df52-4342-b581-4b92fcd12033 |
| Jogador 4 | 3-5 | 348 | BUY | SLOWROLL | 62.0 | 5 | 64 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026854300871491432 | 0.0 | 0.0 | +661b176a-5963-4715-b9dd-aca29f552fa9 / -— |
| Jogador 4 | 3-5 | 349 | SELL | SLOWROLL | 62.0 | 5 | 63 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017692307010293007 | 0.0 | 0.0 | +— / -661b176a-5963-4715-b9dd-aca29f552fa9 |
| Jogador 4 | 3-5 | 350 | SELL | SLOWROLL | 62.0 | 5 | 64 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17176923155784607 | 0.0 | 0.0 | +— / -40f2a32f-1ace-4700-8a79-e6b5d3212036 |
| Jogador 4 | 3-5 | 351 | SELL | SLOWROLL | 62.0 | 5 | 66 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014999999664723873 | 0.0 | 0.0 | +— / -62b9f2fe-f0ec-474d-9b5d-1c589c8fa2b2 |
| Jogador 4 | 3-5 | 352 | PASS | SLOWROLL | 62.0 | 5 | 68 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008245306089520454 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 362 | BUY | SLOWROLL | 50.0 | 5 | 79 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3037607967853546 | 0.0 | 0.0 | +23f4d10f-2614-47b2-bfb2-4fb276764b5e / -— |
| Jogador 4 | 3-6 | 363 | BUY | SLOWROLL | 50.0 | 5 | 78 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2682235836982727 | 0.0 | 0.0 | +f722cd46-0c4e-42e7-80ff-4b910c28d572 / -— |
| Jogador 4 | 3-6 | 364 | BUY | SLOWROLL | 50.0 | 5 | 76 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26794442534446716 | 0.0 | 0.0 | +8e1a5a7a-d27d-47c9-a197-b383c1c3da3b / -— |
| Jogador 4 | 3-6 | 365 | SELL | SLOWROLL | 50.0 | 5 | 74 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -8e1a5a7a-d27d-47c9-a197-b383c1c3da3b |
| Jogador 4 | 3-6 | 366 | BUY | SLOWROLL | 50.0 | 5 | 76 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0786408931016922 | 0.0 | 0.0 | +320038b5-88c4-48fe-a7fa-a30823d674c0 / -— |
| Jogador 4 | 3-6 | 367 | SELL | SLOWROLL | 50.0 | 5 | 75 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03311554715037346 | 0.0 | 0.0 | +— / -320038b5-88c4-48fe-a7fa-a30823d674c0 |
| Jogador 4 | 3-6 | 368 | BUY | SLOWROLL | 50.0 | 5 | 76 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27236998081207275 | 0.0 | 0.0 | +fe3fea0b-bb55-4236-830e-828a00a9e529 / -— |
| Jogador 4 | 3-6 | 369 | SELL | SLOWROLL | 50.0 | 5 | 75 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -fe3fea0b-bb55-4236-830e-828a00a9e529 |
| Jogador 4 | 3-6 | 370 | SELL | SLOWROLL | 50.0 | 5 | 76 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17299999296665192 | 0.0 | 0.0 | +— / -f722cd46-0c4e-42e7-80ff-4b910c28d572 |
| Jogador 4 | 3-6 | 371 | SELL | SLOWROLL | 50.0 | 5 | 78 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3409265875816345 | 0.0 | 0.0 | +— / -e2ed7625-f3aa-43f0-936b-7322cb9d16f1 |
| Jogador 4 | 3-6 | 372 | PASS | SLOWROLL | 50.0 | 5 | 79 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014613606035709381 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 381 | BUY | SLOWROLL | 50.0 | 6 | 90 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.536288321018219 | 0.0 | 0.0 | +05be69ba-41c7-4dee-9799-dabbd60f0dc9 / -— |
| Jogador 4 | 3-7 | 382 | BUY | SLOWROLL | 50.0 | 6 | 87 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2711395025253296 | 0.0 | 0.0 | +59f588eb-e3f3-4907-ab23-af073a26bd6a / -— |
| Jogador 4 | 3-7 | 383 | BUY | SLOWROLL | 50.0 | 6 | 85 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07605151832103729 | 0.0 | 0.0 | +e9d5f645-4afc-44f4-ae53-bc832c49f451 / -— |
| Jogador 4 | 3-7 | 384 | SELL | SLOWROLL | 50.0 | 6 | 83 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -59f588eb-e3f3-4907-ab23-af073a26bd6a |
| Jogador 4 | 3-7 | 385 | BUY | SLOWROLL | 50.0 | 6 | 85 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23859676718711853 | 0.0 | 0.0 | +eab06dbd-05d4-43b6-88f0-e6abb0e83d34 / -— |
| Jogador 4 | 3-7 | 386 | SELL | SLOWROLL | 50.0 | 6 | 83 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04323076829314232 | 0.0 | 0.0 | +— / -eab06dbd-05d4-43b6-88f0-e6abb0e83d34 |
| Jogador 4 | 3-7 | 387 | BUY | SLOWROLL | 50.0 | 6 | 85 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22015385329723358 | 0.0 | 0.0 | +e3fdce1f-991f-4305-9aaa-fbf72ede6c01 / -— |
| Jogador 4 | 3-7 | 388 | SELL | SLOWROLL | 50.0 | 6 | 84 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03154411539435387 | 0.0 | 0.0 | +— / -e9d5f645-4afc-44f4-ae53-bc832c49f451 |
| Jogador 4 | 3-7 | 389 | SELL | SLOWROLL | 50.0 | 6 | 86 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5197889804840088 | 0.0 | 0.0 | +— / -e3fdce1f-991f-4305-9aaa-fbf72ede6c01 |
| Jogador 4 | 3-7 | 390 | SELL | SLOWROLL | 50.0 | 6 | 87 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3314615488052368 | 0.0 | 0.0 | +— / -05be69ba-41c7-4dee-9799-dabbd60f0dc9 |
| Jogador 4 | 3-7 | 391 | PASS | SLOWROLL | 50.0 | 6 | 90 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02149570919573307 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 402 | BUY | SLOWROLL | 50.0 | 6 | 100 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.21027186512947083 | 0.0 | 0.0 | +9175d2a8-4736-402d-873b-cf4846b04d97 / -— |
| Jogador 4 | 4-1 | 403 | BUY | SLOWROLL | 50.0 | 6 | 97 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07265372574329376 | 0.0 | 0.0 | +5637ca02-9946-4d1a-9679-e5c316ef566b / -— |
| Jogador 4 | 4-1 | 404 | BUY | SLOWROLL | 50.0 | 6 | 95 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.26948440074920654 | 0.0 | 0.0 | +42733dbd-0bc3-461b-95ab-76daf5ad6296 / -— |
| Jogador 4 | 4-1 | 405 | SELL | SLOWROLL | 50.0 | 6 | 93 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -42733dbd-0bc3-461b-95ab-76daf5ad6296 |
| Jogador 4 | 4-1 | 406 | BUY | SLOWROLL | 50.0 | 6 | 95 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.23591159284114838 | 0.0 | 0.0 | +210d2415-663d-4768-bbc2-238766c2b863 / -— |
| Jogador 4 | 4-1 | 407 | SELL | SLOWROLL | 50.0 | 6 | 93 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04323076829314232 | 0.0 | 0.0 | +— / -210d2415-663d-4768-bbc2-238766c2b863 |
| Jogador 4 | 4-1 | 408 | BUY | SLOWROLL | 50.0 | 6 | 95 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.24338917434215546 | 0.0 | 0.0 | +465ecc70-f5da-47f4-a7c0-2005a8ed24c1 / -— |
| Jogador 4 | 4-1 | 409 | SELL | SLOWROLL | 50.0 | 6 | 94 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03154834359884262 | 0.0 | 0.0 | +— / -5637ca02-9946-4d1a-9679-e5c316ef566b |
| Jogador 4 | 4-1 | 410 | SELL | SLOWROLL | 50.0 | 6 | 96 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.1770000010728836 | 0.0 | 0.0 | +— / -9175d2a8-4736-402d-873b-cf4846b04d97 |
| Jogador 4 | 4-1 | 411 | SELL | SLOWROLL | 50.0 | 6 | 99 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.520918071269989 | 0.0 | 0.0 | +— / -465ecc70-f5da-47f4-a7c0-2005a8ed24c1 |
| Jogador 4 | 4-1 | 412 | PASS | SLOWROLL | 50.0 | 6 | 100 | 5 | 22.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.028095955029129982 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 422 | BUY | STABILIZE | 37.0 | 6 | 110 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8977307081222534 | 0.0 | 0.0 | +090f2ba6-5514-49ba-a80d-a0711cd06245 / -— |
| Jogador 4 | 4-2 | 423 | BUY | STABILIZE | 37.0 | 6 | 107 | 5 | 22.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9599392414093018 | 0.0 | 0.0 | +cb216a0d-8bff-41f9-99bd-231ca5186fb5 / -53a27943-148b-4522-9826-3f2e0b8a7858,8052731e-e34c-4de7-84b1-2b986cfeddaa |
| Jogador 4 | 4-2 | 424 | BUY | STABILIZE | 37.0 | 6 | 106 | 5 | 18.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.051358044147491455 | 0.0 | 0.0 | +4363594b-375b-45d4-9b1a-0c1ab96367a1 / -— |
| Jogador 4 | 4-2 | 425 | SELL | STABILIZE | 37.0 | 6 | 104 | 5 | 18.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.032769229263067245 | 0.0 | 0.0 | +— / -4363594b-375b-45d4-9b1a-0c1ab96367a1 |
| Jogador 4 | 4-2 | 426 | BUY | STABILIZE | 37.0 | 6 | 106 | 5 | 18.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2430008351802826 | 0.0 | 0.0 | +55944609-f4df-4e53-a1d1-31c79a148b22 / -— |
| Jogador 4 | 4-2 | 427 | SELL | STABILIZE | 37.0 | 6 | 105 | 5 | 18.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -55944609-f4df-4e53-a1d1-31c79a148b22 |
| Jogador 4 | 4-2 | 428 | BUY | STABILIZE | 37.0 | 6 | 106 | 5 | 18.0 | Fumegante/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.24301567673683167 | 0.0 | 0.0 | +f394f34c-c68b-4213-9eb0-88f302976405 / -— |
| Jogador 4 | 4-2 | 429 | SELL | STABILIZE | 37.0 | 6 | 105 | 5 | 18.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -f394f34c-c68b-4213-9eb0-88f302976405 |
| Jogador 4 | 4-2 | 430 | SELL | STABILIZE | 37.0 | 6 | 106 | 5 | 18.0 | Fumegante/DA_18_Yorick | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.7210000157356262 | 0.0 | 0.0 | +— / -d9b43609-2c36-4fea-b26b-ea5bea6609b5 |
| Jogador 4 | 4-2 | 431 | MOVE_BENCH | STABILIZE | 37.0 | 6 | 109 | 5 | 18.0 | Fumegante/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6200594902038574 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 432 | PASS | STABILIZE | 37.0 | 6 | 109 | 5 | 22.0 | Fumegante/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0342690609395504 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 441 | BUY | STABILIZE | 26.0 | 6 | 120 | 5 | 22.0 | Fumegante/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8841586112976074 | 0.0 | 0.0 | +7bcf9a7f-a7c9-44a7-9d12-e1ba998b23ed / -— |
| Jogador 4 | 4-3 | 442 | BUY | STABILIZE | 26.0 | 6 | 117 | 5 | 22.0 | Fumegante/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.06582225114107132 | 0.0 | 0.0 | +7b3e8122-3b51-46b5-94a8-68fb77156e0e / -— |
| Jogador 4 | 4-3 | 443 | BUY | STABILIZE | 26.0 | 6 | 114 | 5 | 22.0 | Fumegante/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.23820556700229645 | 0.0 | 0.0 | +26462e09-ab6e-4b87-85a8-6bda974b0c45 / -— |
| Jogador 4 | 4-3 | 444 | SELL | STABILIZE | 26.0 | 6 | 111 | 5 | 22.0 | Fumegante/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04169230908155441 | 0.0 | 0.0 | +— / -26462e09-ab6e-4b87-85a8-6bda974b0c45 |
| Jogador 4 | 4-3 | 445 | BUY | STABILIZE | 26.0 | 6 | 114 | 5 | 22.0 | Fumegante/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.27100107073783875 | 0.0 | 0.0 | +60138930-82d5-4f1c-a5fe-a22ea4b70d36 / -— |
| Jogador 4 | 4-3 | 446 | SELL | STABILIZE | 26.0 | 6 | 111 | 5 | 22.0 | Fumegante/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -60138930-82d5-4f1c-a5fe-a22ea4b70d36 |
| Jogador 4 | 4-3 | 447 | BUY | STABILIZE | 26.0 | 6 | 114 | 5 | 22.0 | Fumegante/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07118929177522659 | 0.0 | 0.0 | +3bbd7105-b508-437d-ac84-11e01a499779 / -— |
| Jogador 4 | 4-3 | 448 | SELL | STABILIZE | 26.0 | 6 | 112 | 5 | 22.0 | Fumegante/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04231775552034378 | 0.0 | 0.0 | +— / -3bbd7105-b508-437d-ac84-11e01a499779 |
| Jogador 4 | 4-3 | 449 | SELL | STABILIZE | 26.0 | 6 | 114 | 5 | 22.0 | Fumegante/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.19546154141426086 | 0.0 | 0.0 | +— / -7b3e8122-3b51-46b5-94a8-68fb77156e0e |
| Jogador 4 | 4-3 | 450 | SELL | STABILIZE | 26.0 | 6 | 117 | 5 | 22.0 | Fumegante/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3406684398651123 | 0.0 | 0.0 | +— / -23f4d10f-2614-47b2-bfb2-4fb276764b5e |
| Jogador 4 | 4-3 | 451 | PASS | STABILIZE | 26.0 | 6 | 118 | 5 | 22.0 | Fumegante/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.04063408449292183 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 461 | BUY | ALL_IN | 12.0 | 6 | 129 | 5 | 22.0 | Fumegante/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.089670829474926 | 0.0 | 0.0 | +29a44465-8a09-49e7-abfc-a27e987543f1 / -— |
| Jogador 4 | 4-4 | 462 | BUY | ALL_IN | 12.0 | 6 | 127 | 5 | 22.0 | Fumegante/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.26069530844688416 | 0.0 | 0.0 | +b5b3098f-d48c-42b8-8022-639a25225980 / -— |
| Jogador 4 | 4-4 | 463 | BUY | ALL_IN | 12.0 | 6 | 125 | 5 | 22.0 | Fumegante/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.27689990401268005 | 0.0 | 0.0 | +fb551efa-6ad5-4f97-aa05-bc5eb70943d4 / -— |
| Jogador 4 | 4-4 | 464 | SELL | ALL_IN | 12.0 | 6 | 123 | 5 | 22.0 | Fumegante/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -fb551efa-6ad5-4f97-aa05-bc5eb70943d4 |
| Jogador 4 | 4-4 | 465 | BUY | ALL_IN | 12.0 | 6 | 125 | 5 | 22.0 | Fumegante/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2769150137901306 | 0.0 | 0.0 | +b837d2e1-b93f-4cc2-b9b8-7c3e3582f4e9 / -— |
| Jogador 4 | 4-4 | 466 | SELL | ALL_IN | 12.0 | 6 | 123 | 5 | 22.0 | Fumegante/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -b837d2e1-b93f-4cc2-b9b8-7c3e3582f4e9 |
| Jogador 4 | 4-4 | 467 | BUY | ALL_IN | 12.0 | 6 | 125 | 5 | 22.0 | Fumegante/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.24734756350517273 | 0.0 | 0.0 | +ea88d306-ae6b-4dbe-b559-3371ba39613a / -— |
| Jogador 4 | 4-4 | 468 | CRAFT_AND_EQUIP | ALL_IN | 12.0 | 6 | 123 | 5 | 22.0 | Fumegante/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.03669660538434982 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 469 | PASS | ALL_IN | 12.0 | 6 | 123 | 5 | 22.0 | Fumegante/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0942453071475029 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 475 | MOVE_BENCH | ALL_IN | 12.0 | 6 | 123 | 5 | 22.0 | Fumegante/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42988425493240356 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 481 | BUY | ALL_IN | 12.0 | 6 | 134 | 5 | 28.0 | Fumegante/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8417479395866394 | 0.0 | 0.0 | +11b28280-bb53-4ca7-81b7-5ce8705303a5 / -— |
| Jogador 4 | 4-5 | 482 | SELL | ALL_IN | 12.0 | 6 | 132 | 5 | 28.0 | Fumegante/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04323076829314232 | 0.0 | 0.0 | +— / -ea88d306-ae6b-4dbe-b559-3371ba39613a |
| Jogador 4 | 4-5 | 483 | BUY | ALL_IN | 12.0 | 6 | 134 | 5 | 28.0 | Fumegante/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08245153725147247 | 0.0 | 0.0 | +d1f19609-8b5f-489d-a2cf-d015fe7ed27e / -— |
| Jogador 4 | 4-5 | 484 | SELL | ALL_IN | 12.0 | 6 | 131 | 5 | 28.0 | Fumegante/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2804393768310547 | 0.0 | 0.0 | +— / -29a44465-8a09-49e7-abfc-a27e987543f1 |
| Jogador 4 | 4-5 | 485 | BUY | ALL_IN | 12.0 | 6 | 133 | 5 | 28.0 | Fumegante/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22935430705547333 | 0.0 | 0.0 | +5b96c8f7-bacb-47df-8666-30d30d49549d / -— |
| Jogador 4 | 4-5 | 486 | PASS | ALL_IN | 12.0 | 6 | 130 | 5 | 28.0 | Fumegante/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09938417375087738 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 494 | MOVE_BENCH | ALL_IN | 12.0 | 6 | 130 | 5 | 28.0 | Fumegante/DA_18_Xayah | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5699862837791443 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 500 | BUY | ALL_IN | 12.0 | 6 | 141 | 5 | 32.0 | Fumegante/DA_18_Xayah | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0174686908721924 | 0.0 | 0.0 | +ac547bcb-d285-480d-b50e-3cfba572db5a / -421bcbcb-ecb2-4af8-88d4-7be6cd284d27,7bcf9a7f-a7c9-44a7-9d12-e1ba998b23ed |
| Jogador 4 | 4-6 | 501 | BUY | ALL_IN | 12.0 | 6 | 138 | 5 | 26.0 | Fumegante/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3041391372680664 | 0.0 | 0.0 | +262702a6-b710-4129-9dc6-0c1a04514ff9 / -— |
| Jogador 4 | 4-6 | 502 | SELL | ALL_IN | 12.0 | 6 | 135 | 5 | 26.0 | Fumegante/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04245520010590553 | 0.0 | 0.0 | +— / -b5b3098f-d48c-42b8-8022-639a25225980 |
| Jogador 4 | 4-6 | 503 | BUY | ALL_IN | 12.0 | 6 | 137 | 5 | 26.0 | Fumegante/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17735041677951813 | 0.0 | 0.0 | +8aa832ec-4c09-43bd-ae21-baf7268e468d / -— |
| Jogador 4 | 4-6 | 504 | PASS | ALL_IN | 12.0 | 6 | 134 | 5 | 26.0 | Fumegante/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10236184298992157 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 512 | BUY | ALL_IN | 1.0 | 6 | 144 | 5 | 38.0 | Fumegante/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2822924554347992 | 0.0 | 0.0 | +c65dacb1-5745-49d1-b7d4-e45d8e24aa84 / -— |
| Jogador 4 | 4-7 | 513 | PASS | ALL_IN | 1.0 | 6 | 142 | 5 | 38.0 | Fumegante/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10840165615081787 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 531 | EQUIP_FROM_INVENTORY | ALL_IN | 1.0 | 6 | 152 | 5 | 38.0 | Fumegante/DA_Fiddlesticks18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 532 | SELL | ALL_IN | 1.0 | 6 | 152 | 5 | 38.0 | Fumegante/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.041999999433755875 | 0.0 | 0.0 | +— / -c65dacb1-5745-49d1-b7d4-e45d8e24aa84 |
| Jogador 4 | 5-1 | 533 | BUY | ALL_IN | 1.0 | 6 | 154 | 5 | 38.0 | Fumegante/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.050360530614852905 | 0.0 | 0.0 | +d366508d-f33b-485a-8ff3-e5d0a248ae3e / -— |
| Jogador 4 | 5-1 | 534 | PASS | ALL_IN | 1.0 | 6 | 152 | 5 | 38.0 | Fumegante/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1160997748374939 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 549 | PASS | ALL_IN | 0.0 | 6 | 152 | 5 | 0.0 | Fumegante/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 562 | PASS | ALL_IN | 0.0 | 6 | 152 | 5 | 0.0 | Fumegante/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 579 | PASS | ALL_IN | 0.0 | 6 | 152 | 5 | 0.0 | Fumegante/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 592 | PASS | ALL_IN | 0.0 | 6 | 152 | 5 | 0.0 | Fumegante/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 609 | PASS | ALL_IN | 0.0 | 6 | 152 | 5 | 0.0 | Fumegante/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 622 | PASS | ALL_IN | 0.0 | 6 | 152 | 5 | 0.0 | Fumegante/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 638 | PASS | ALL_IN | 0.0 | 6 | 152 | 5 | 0.0 | Fumegante/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-2 | 652 | PASS | ALL_IN | 0.0 | 6 | 152 | 5 | 0.0 | Fumegante/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-3 | 667 | PASS | ALL_IN | 0.0 | 6 | 152 | 5 | 0.0 | Fumegante/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-4 | 681 | PASS | ALL_IN | 0.0 | 6 | 152 | 5 | 0.0 | Fumegante/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-5 | 695 | PASS | ALL_IN | 0.0 | 6 | 152 | 5 | 0.0 | Fumegante/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-6 | 709 | PASS | ALL_IN | 0.0 | 6 | 152 | 5 | 0.0 | Fumegante/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-7 | 719 | PASS | ALL_IN | 0.0 | 6 | 152 | 5 | 0.0 | Fumegante/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 7-1 | 729 | PASS | ALL_IN | 0.0 | 6 | 152 | 5 | 0.0 | Fumegante/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 7-2 | 741 | PASS | ALL_IN | 0.0 | 6 | 152 | 5 | 0.0 | Fumegante/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 26 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.27265432476997375 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.027269404381513596 | 0.0 | 0.0 | +df7d3860-9b2e-45ed-b564-281d95e64e82 / -— |
| Jogador 5 | 1-2 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3760097920894623 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 35 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.14072515070438385 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 36 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 57 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2778402864933014 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 58 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3737058937549591 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 59 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.11687260121107101 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 60 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | -0.31869131326675415 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 61 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | 0.07093329727649689 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 62 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.07871419936418533 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 63 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.17937226593494415 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 64 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 83 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.295399934053421 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 84 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Elise | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08432820439338684 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 85 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 12.0 | —/DA_18_Elise | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07691293209791183 | 0.0 | 0.0 | +— / -f9c418e0-f8aa-4492-8b97-8855ce3af370 |
| Jogador 5 | 1-4 | 86 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 12.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 109 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2931661605834961 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 110 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 12.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4133998453617096 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 111 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.28957152366638184 | 0.0 | 0.0 | +a5c3f6df-50ac-4f3b-aa9c-6476a055aa53 / -— |
| Jogador 5 | 2-1 | 112 | SELL | STABILIZE | 100.0 | 4 | 1 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3395715355873108 | 0.0 | 0.0 | +— / -a5c3f6df-50ac-4f3b-aa9c-6476a055aa53 |
| Jogador 5 | 2-1 | 113 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.13750514388084412 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 114 | BUY | STABILIZE | 100.0 | 4 | 3 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.35474950075149536 | 0.0 | 0.0 | +4a8986e4-45cf-42bc-866d-01c476dcb55b / -— |
| Jogador 5 | 2-1 | 115 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.40474948287010193 | 0.0 | 0.0 | +— / -4a8986e4-45cf-42bc-866d-01c476dcb55b |
| Jogador 5 | 2-1 | 116 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.32442647218704224 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 117 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 3 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 118 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 133 | BUY | STABILIZE | 95.0 | 4 | 8 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.30259716510772705 | 0.0 | 0.0 | +68cd8ae3-399f-461f-89a8-189d7b0a6b59 / -— |
| Jogador 5 | 2-2 | 134 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 5 | 0 | 18.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19575028121471405 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 135 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 5 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06941301375627518 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 136 | SELL | STABILIZE | 95.0 | 4 | 5 | 0 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004401967860758305 | 0.0 | 0.0 | +— / -1934c7ef-cc22-45b3-bed9-01aea61ffbdb |
| Jogador 5 | 2-2 | 137 | BUY | STABILIZE | 95.0 | 4 | 7 | 0 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.02064775861799717 | 0.0 | 0.0 | +9bb3da58-fe6f-4298-8529-859cceb4857e / -— |
| Jogador 5 | 2-2 | 138 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 4 | 0 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39273229241371155 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 139 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 4 | 0 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14198172092437744 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 140 | PASS | STABILIZE | 95.0 | 4 | 4 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 157 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 10 | 1 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.316780149936676 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 158 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 10 | 1 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7399510145187378 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 159 | PASS | STABILIZE | 89.0 | 4 | 10 | 1 | 20.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 182 | MOVE_BENCH | LOSS_STREAK | 84.0 | 4 | 17 | 1 | 20.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12102767080068588 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 183 | MOVE_BENCH | LOSS_STREAK | 84.0 | 4 | 17 | 1 | 22.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31743913888931274 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 184 | PASS | LOSS_STREAK | 84.0 | 4 | 17 | 1 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 205 | MOVE_BENCH | LOSS_STREAK | 84.0 | 4 | 24 | 2 | 20.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7416125535964966 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 206 | MOVE_BENCH | LOSS_STREAK | 84.0 | 4 | 24 | 2 | 20.0 | Florescer/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2793639898300171 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 207 | PASS | STABILIZE | 84.0 | 4 | 24 | 2 | 22.0 | Florescer/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 227 | BUY | STABILIZE | 78.0 | 5 | 32 | 3 | 22.0 | Florescer/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9674918055534363 | 0.0 | 0.0 | +ae570779-3ae8-49b3-acdb-607fc512fcea / -— |
| Jogador 5 | 2-6 | 228 | MOVE_BENCH | SLOWROLL | 78.0 | 5 | 30 | 3 | 22.0 | Florescer/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4731488525867462 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 229 | BUY | SLOWROLL | 78.0 | 5 | 30 | 3 | 26.0 | Congregação das Bruxas/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3450755178928375 | 0.0 | 0.0 | +fa0e266f-ef5b-48c5-b9a3-511450e97169 / -— |
| Jogador 5 | 2-6 | 230 | MOVE_BOARD | STABILIZE | 78.0 | 5 | 29 | 2 | 26.0 | Congregação das Bruxas/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00998972449451685 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 231 | MOVE_BOARD | STABILIZE | 78.0 | 5 | 29 | 2 | 26.0 | Congregação das Bruxas/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05787229165434837 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 232 | SELL | STABILIZE | 78.0 | 5 | 29 | 2 | 26.0 | Congregação das Bruxas/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06470783799886703 | 0.0 | 0.0 | +— / -7098795b-11bf-4b73-837a-87f5d8aece4c |
| Jogador 5 | 2-6 | 233 | SELL | SLOWROLL | 78.0 | 5 | 31 | 3 | 26.0 | Congregação das Bruxas/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5620769262313843 | 0.0 | 0.0 | +— / -fa0e266f-ef5b-48c5-b9a3-511450e97169 |
| Jogador 5 | 2-6 | 234 | BUY | SLOWROLL | 78.0 | 5 | 32 | 3 | 26.0 | Congregação das Bruxas/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.379177063703537 | 0.0 | 0.0 | +b6a21130-c9dc-45ad-8ddb-9223b0ec8751 / -— |
| Jogador 5 | 2-6 | 235 | BUY_XP | SLOWROLL | 78.0 | 5 | 31 | 3 | 26.0 | Congregação das Bruxas/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1379999965429306 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 236 | BUY_XP | STABILIZE | 78.0 | 5 | 27 | 2 | 26.0 | Congregação das Bruxas/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 237 | PASS | STABILIZE | 78.0 | 5 | 23 | 2 | 26.0 | Congregação das Bruxas/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 250 | SELL | SLOWROLL | 70.0 | 5 | 32 | 3 | 26.0 | Congregação das Bruxas/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3439468741416931 | 0.0 | 0.0 | +— / -b6a21130-c9dc-45ad-8ddb-9223b0ec8751 |
| Jogador 5 | 2-7 | 251 | BUY | SLOWROLL | 70.0 | 5 | 33 | 3 | 26.0 | Congregação das Bruxas/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08038841933012009 | 0.0 | 0.0 | +837b2d09-a207-4830-b36d-29e493bbcc22 / -— |
| Jogador 5 | 2-7 | 252 | MOVE_BENCH | SLOWROLL | 70.0 | 5 | 31 | 3 | 26.0 | Congregação das Bruxas/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6399630308151245 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 253 | MOVE_BENCH | SLOWROLL | 70.0 | 5 | 31 | 3 | 24.0 | Congregação das Bruxas/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26686885952949524 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 254 | MOVE_BENCH | SLOWROLL | 70.0 | 5 | 31 | 3 | 24.0 | Congregação das Bruxas/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2089187502861023 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 255 | BUY_XP | SLOWROLL | 70.0 | 5 | 31 | 3 | 26.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1379999965429306 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 256 | BUY_XP | STABILIZE | 70.0 | 5 | 27 | 2 | 26.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 257 | BUY_XP | STABILIZE | 70.0 | 5 | 23 | 2 | 26.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025599999353289604 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 258 | MOVE_BENCH | STABILIZE | 70.0 | 6 | 19 | 1 | 26.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3652013838291168 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 259 | MOVE_BOARD | STABILIZE | 70.0 | 6 | 19 | 1 | 30.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 260 | PASS | STABILIZE | 70.0 | 6 | 19 | 1 | 30.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 270 | BUY | STABILIZE | 70.0 | 6 | 27 | 2 | 30.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0885188952088356 | 0.0 | 0.0 | +e8c36276-b932-45ba-b350-2d1cb339a019 / -— |
| Jogador 5 | 3-1 | 271 | MOVE_BENCH | STABILIZE | 70.0 | 6 | 24 | 2 | 30.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.056507911533117294 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 272 | MOVE_BOARD | STABILIZE | 70.0 | 6 | 24 | 2 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12026835978031158 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 273 | MOVE_BOARD | STABILIZE | 70.0 | 6 | 24 | 2 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18523558974266052 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 274 | MOVE_BOARD | STABILIZE | 70.0 | 6 | 24 | 2 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06739011406898499 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 275 | MOVE_BOARD | STABILIZE | 70.0 | 6 | 24 | 2 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 276 | MOVE_BOARD | STABILIZE | 70.0 | 6 | 24 | 2 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10906810313463211 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 277 | PASS | STABILIZE | 70.0 | 6 | 24 | 2 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007499999832361937 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 289 | BUY | SLOWROLL | 70.0 | 6 | 32 | 3 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6134201884269714 | 0.0 | 0.0 | +68b28241-1946-4304-8b10-ae24a13a8e60 / -— |
| Jogador 5 | 3-2 | 290 | SELL | STABILIZE | 70.0 | 6 | 29 | 2 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09131962060928345 | 0.0 | 0.0 | +— / -837b2d09-a207-4830-b36d-29e493bbcc22 |
| Jogador 5 | 3-2 | 291 | BUY | SLOWROLL | 70.0 | 6 | 31 | 3 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13159970939159393 | 0.0 | 0.0 | +35a674f6-a230-480b-a93f-f7ec76d78658 / -— |
| Jogador 5 | 3-2 | 292 | MOVE_BOARD | STABILIZE | 70.0 | 6 | 29 | 2 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3192041516304016 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 293 | SELL | STABILIZE | 70.0 | 6 | 29 | 2 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10395930707454681 | 0.0 | 0.0 | +— / -35a674f6-a230-480b-a93f-f7ec76d78658 |
| Jogador 5 | 3-2 | 294 | BUY | SLOWROLL | 70.0 | 6 | 31 | 3 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18921124935150146 | 0.0 | 0.0 | +d218597b-b641-4a4c-867a-41227b83fcff / -— |
| Jogador 5 | 3-2 | 295 | BUY_XP | STABILIZE | 70.0 | 6 | 29 | 2 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 296 | BUY_XP | STABILIZE | 70.0 | 6 | 25 | 2 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 297 | BUY_XP | STABILIZE | 70.0 | 6 | 21 | 2 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 298 | BUY_XP | STABILIZE | 70.0 | 6 | 17 | 1 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 299 | PASS | STABILIZE | 70.0 | 6 | 13 | 1 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 306 | BUY | STABILIZE | 70.0 | 6 | 21 | 2 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.021168258041143417 | 0.0 | 0.0 | +8a4d0946-b80f-4fbb-ab7c-d43c2697c34e / -— |
| Jogador 5 | 3-3 | 307 | BUY | STABILIZE | 70.0 | 6 | 17 | 1 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6529219150543213 | 0.0 | 0.0 | +a12781fd-4d61-4c7e-b439-a6e62bd48dfe / -— |
| Jogador 5 | 3-3 | 308 | PASS | STABILIZE | 70.0 | 6 | 14 | 1 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 323 | BUY | STABILIZE | 70.0 | 6 | 22 | 2 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3488514721393585 | 0.0 | 0.0 | +3a11170d-1b8e-4316-ad59-9a7e60071f12 / -— |
| Jogador 5 | 3-4 | 324 | PASS | STABILIZE | 70.0 | 6 | 20 | 2 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 342 | SELL | STABILIZE | 70.0 | 6 | 28 | 2 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23756839334964752 | 0.0 | 0.0 | +— / -d218597b-b641-4a4c-867a-41227b83fcff |
| Jogador 5 | 3-5 | 343 | BUY | SLOWROLL | 70.0 | 6 | 30 | 3 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0555478110909462 | 0.0 | 0.0 | +9bbd1da9-6a26-472c-912e-165ea4031b90 / -— |
| Jogador 5 | 3-5 | 344 | PASS | STABILIZE | 70.0 | 6 | 27 | 2 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 362 | SELL | SLOWROLL | 70.0 | 6 | 36 | 3 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005321868695318699 | 0.0 | 0.0 | +— / -3a11170d-1b8e-4316-ad59-9a7e60071f12 |
| Jogador 5 | 3-6 | 363 | BUY | SLOWROLL | 70.0 | 6 | 38 | 3 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029658783227205276 | 0.0 | 0.0 | +750eedbe-93d9-46de-b3b8-a88e41f395f0 / -— |
| Jogador 5 | 3-6 | 364 | SELL | SLOWROLL | 70.0 | 6 | 36 | 3 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19562293589115143 | 0.0 | 0.0 | +— / -750eedbe-93d9-46de-b3b8-a88e41f395f0 |
| Jogador 5 | 3-6 | 365 | SELL | SLOWROLL | 70.0 | 6 | 38 | 3 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2621961534023285 | 0.0 | 0.0 | +— / -a12781fd-4d61-4c7e-b439-a6e62bd48dfe |
| Jogador 5 | 3-6 | 366 | SELL | SLOWROLL | 70.0 | 6 | 41 | 4 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3414436876773834 | 0.0 | 0.0 | +— / -9bbd1da9-6a26-472c-912e-165ea4031b90 |
| Jogador 5 | 3-6 | 367 | BUY | SLOWROLL | 70.0 | 6 | 44 | 4 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2569870054721832 | 0.0 | 0.0 | +bb94e33a-4797-47ed-b3cd-6ca12a4d6bd2 / -— |
| Jogador 5 | 3-6 | 368 | PASS | SLOWROLL | 70.0 | 6 | 43 | 4 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 381 | PASS | SLOWROLL | 60.0 | 6 | 52 | 5 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0005903584533371031 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 402 | BUY | SLOWROLL | 60.0 | 6 | 62 | 5 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3327931761741638 | 0.0 | 0.0 | +60255a84-4f78-49f0-a4f1-d598704c7ee7 / -— |
| Jogador 5 | 4-1 | 403 | PASS | SLOWROLL | 60.0 | 6 | 59 | 5 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07025422155857086 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 422 | BUY | FAST8 | 60.0 | 7 | 70 | 5 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6828750967979431 | 0.0 | 0.0 | +fff5cc22-5f1a-47a4-93e3-9772177b0910 / -— |
| Jogador 5 | 4-2 | 423 | BUY | FAST8 | 60.0 | 7 | 67 | 5 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02602863311767578 | 0.0 | 0.0 | +d9fdb961-a3e3-4e39-9970-e46ffd59fc3b / -— |
| Jogador 5 | 4-2 | 424 | BUY | FAST8 | 60.0 | 7 | 63 | 5 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41971611976623535 | 0.0 | 0.0 | +dde5ed69-0fc4-4d15-b12c-a5252a239040 / -— |
| Jogador 5 | 4-2 | 425 | BUY | FAST8 | 60.0 | 7 | 60 | 5 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05088534578680992 | 0.0 | 0.0 | +02c8aff1-803e-42bc-b7c2-f7cd6d986b4f / -— |
| Jogador 5 | 4-2 | 426 | PASS | FAST8 | 60.0 | 7 | 58 | 5 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0031159305945038795 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 435 | MOVE_BENCH | FAST8 | 60.0 | 7 | 58 | 5 | 32.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47112807631492615 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 441 | BUY | FAST8 | 46.0 | 7 | 68 | 5 | 34.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7117502093315125 | 0.0 | 0.0 | +d8ecc66e-097d-4caa-a657-90fcd1286c2b / -68cd8ae3-399f-461f-89a8-189d7b0a6b59,dde5ed69-0fc4-4d15-b12c-a5252a239040 |
| Jogador 5 | 4-3 | 442 | BUY | FAST8 | 46.0 | 7 | 65 | 5 | 28.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08891621977090836 | 0.0 | 0.0 | +27a4bd22-9c1f-4f9f-9192-06ea4933feb5 / -— |
| Jogador 5 | 4-3 | 443 | BUY | FAST8 | 46.0 | 7 | 62 | 5 | 28.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19139817357063293 | 0.0 | 0.0 | +72c247af-bdc3-410c-98dd-dd72b56f2818 / -— |
| Jogador 5 | 4-3 | 444 | SELL | FAST8 | 46.0 | 7 | 59 | 5 | 28.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02784615382552147 | 0.0 | 0.0 | +— / -02c8aff1-803e-42bc-b7c2-f7cd6d986b4f |
| Jogador 5 | 4-3 | 445 | BUY | FAST8 | 46.0 | 7 | 61 | 5 | 28.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1290108859539032 | 0.0 | 0.0 | +16acc555-c819-4f7c-b406-2f48f11ffc87 / -— |
| Jogador 5 | 4-3 | 446 | PASS | FAST8 | 46.0 | 7 | 59 | 5 | 28.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0035889779683202505 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 455 | MOVE_BENCH | FAST8 | 46.0 | 7 | 59 | 5 | 28.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45138809084892273 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 461 | BUY | FAST8 | 46.0 | 7 | 70 | 5 | 40.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8390696048736572 | 0.0 | 0.0 | +ad19ac66-9f86-4c29-8ae7-7222164aece1 / -9bb3da58-fe6f-4298-8529-859cceb4857e,fff5cc22-5f1a-47a4-93e3-9772177b0910 |
| Jogador 5 | 4-4 | 462 | BUY | FAST8 | 46.0 | 7 | 67 | 5 | 34.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.048109035938978195 | 0.0 | 0.0 | +ed23d828-f4bc-4d6c-8cc1-c074047dac8a / -— |
| Jogador 5 | 4-4 | 463 | SELL | FAST8 | 46.0 | 7 | 64 | 5 | 34.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0370769239962101 | 0.0 | 0.0 | +— / -16acc555-c819-4f7c-b406-2f48f11ffc87 |
| Jogador 5 | 4-4 | 464 | BUY | FAST8 | 46.0 | 7 | 66 | 5 | 34.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23473280668258667 | 0.0 | 0.0 | +b80a9778-b2ce-411b-8d08-24549c04367c / -— |
| Jogador 5 | 4-4 | 465 | SELL | FAST8 | 46.0 | 7 | 63 | 5 | 34.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03799999877810478 | 0.0 | 0.0 | +— / -b80a9778-b2ce-411b-8d08-24549c04367c |
| Jogador 5 | 4-4 | 466 | BUY | FAST8 | 46.0 | 7 | 66 | 5 | 34.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15256550908088684 | 0.0 | 0.0 | +b26a039f-581c-4de2-8a75-f7e8a4ef0e4a / -— |
| Jogador 5 | 4-4 | 467 | SELL | FAST8 | 46.0 | 7 | 64 | 5 | 34.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0312722772359848 | 0.0 | 0.0 | +— / -b26a039f-581c-4de2-8a75-f7e8a4ef0e4a |
| Jogador 5 | 4-4 | 468 | BUY | FAST8 | 46.0 | 7 | 66 | 5 | 34.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26103803515434265 | 0.0 | 0.0 | +e4764e13-e26d-4358-980a-c7c625e26726 / -— |
| Jogador 5 | 4-4 | 469 | PASS | FAST8 | 46.0 | 7 | 65 | 5 | 34.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.006625052075833082 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 475 | MOVE_BENCH | FAST8 | 46.0 | 7 | 65 | 5 | 34.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5010272264480591 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 481 | BUY | FAST8 | 46.0 | 7 | 75 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12894655764102936 | 0.0 | 0.0 | +a58767a1-d7c1-48e9-94ae-df46a364ef92 / -— |
| Jogador 5 | 4-5 | 482 | SELL | FAST8 | 46.0 | 7 | 73 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04476923123002052 | 0.0 | 0.0 | +— / -e4764e13-e26d-4358-980a-c7c625e26726 |
| Jogador 5 | 4-5 | 483 | BUY | FAST8 | 46.0 | 7 | 74 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.281462162733078 | 0.0 | 0.0 | +734c25e1-eddf-4452-a04a-1b39db3b94d0 / -— |
| Jogador 5 | 4-5 | 484 | SELL | FAST8 | 46.0 | 7 | 72 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -734c25e1-eddf-4452-a04a-1b39db3b94d0 |
| Jogador 5 | 4-5 | 485 | BUY | FAST8 | 46.0 | 7 | 74 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08764626085758209 | 0.0 | 0.0 | +3a1de7b3-af72-4024-8105-588fa4ec946b / -— |
| Jogador 5 | 4-5 | 486 | SELL | FAST8 | 46.0 | 7 | 73 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0189230777323246 | 0.0 | 0.0 | +— / -3a1de7b3-af72-4024-8105-588fa4ec946b |
| Jogador 5 | 4-5 | 487 | SELL | FAST8 | 46.0 | 7 | 74 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1779230833053589 | 0.0 | 0.0 | +— / -a58767a1-d7c1-48e9-94ae-df46a364ef92 |
| Jogador 5 | 4-5 | 488 | BUY | FAST8 | 46.0 | 7 | 76 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010658124461770058 | 0.0 | 0.0 | +5f9e16e2-0766-403f-a85a-f6a735c04261 / -— |
| Jogador 5 | 4-5 | 489 | PASS | FAST8 | 46.0 | 7 | 75 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012229474261403084 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 500 | BUY | STABILIZE | 33.0 | 7 | 85 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11794647574424744 | 0.0 | 0.0 | +83228c14-cadb-45b4-9893-2fb12c40f4a8 / -— |
| Jogador 5 | 4-6 | 501 | SELL | STABILIZE | 33.0 | 7 | 81 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017692307010293007 | 0.0 | 0.0 | +— / -5f9e16e2-0766-403f-a85a-f6a735c04261 |
| Jogador 5 | 4-6 | 502 | BUY | STABILIZE | 33.0 | 7 | 82 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2750038802623749 | 0.0 | 0.0 | +9717d30c-f073-470c-a6ce-7db8257de559 / -— |
| Jogador 5 | 4-6 | 503 | SELL | STABILIZE | 33.0 | 7 | 79 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -9717d30c-f073-470c-a6ce-7db8257de559 |
| Jogador 5 | 4-6 | 504 | BUY | STABILIZE | 33.0 | 7 | 82 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013677655719220638 | 0.0 | 0.0 | +4c1dab77-0e6d-401b-a341-40117b445957 / -— |
| Jogador 5 | 4-6 | 505 | SELL | STABILIZE | 33.0 | 7 | 81 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028711356222629547 | 0.0 | 0.0 | +— / -4c1dab77-0e6d-401b-a341-40117b445957 |
| Jogador 5 | 4-6 | 506 | BUY | STABILIZE | 33.0 | 7 | 82 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2824702262878418 | 0.0 | 0.0 | +fe12befc-b473-4f91-9e51-558a03efa3ad / -— |
| Jogador 5 | 4-6 | 507 | PASS | STABILIZE | 33.0 | 7 | 81 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.015831198543310165 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 512 | SELL | STABILIZE | 20.0 | 7 | 92 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -fe12befc-b473-4f91-9e51-558a03efa3ad |
| Jogador 5 | 4-7 | 513 | BUY | STABILIZE | 20.0 | 7 | 93 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.992624044418335 | 0.0 | 0.0 | +20821a31-3317-4f82-bbb2-b70cdebdd893 / -ae570779-3ae8-49b3-acdb-607fc512fcea,df7d3860-9b2e-45ed-b564-281d95e64e82 |
| Jogador 5 | 4-7 | 514 | SELL | STABILIZE | 20.0 | 7 | 91 | 5 | 38.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029999999329447746 | 0.0 | 0.0 | +— / -72c247af-bdc3-410c-98dd-dd72b56f2818 |
| Jogador 5 | 4-7 | 515 | BUY | STABILIZE | 20.0 | 7 | 94 | 5 | 38.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2251749485731125 | 0.0 | 0.0 | +6fb9f857-4ee1-4b52-8825-57f514dc2d0f / -— |
| Jogador 5 | 4-7 | 516 | SELL | STABILIZE | 20.0 | 7 | 90 | 5 | 38.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02273385226726532 | 0.0 | 0.0 | +— / -ed23d828-f4bc-4d6c-8cc1-c074047dac8a |
| Jogador 5 | 4-7 | 517 | BUY | STABILIZE | 20.0 | 7 | 93 | 5 | 38.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3806680738925934 | 0.0 | 0.0 | +ec9662c5-0734-41a3-9999-224d7716228b / -— |
| Jogador 5 | 4-7 | 518 | SELL | STABILIZE | 20.0 | 7 | 91 | 5 | 38.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0007692307699471712 | 0.0 | 0.0 | +— / -27a4bd22-9c1f-4f9f-9192-06ea4933feb5 |
| Jogador 5 | 4-7 | 519 | BUY | STABILIZE | 20.0 | 7 | 94 | 5 | 38.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03675977140665054 | 0.0 | 0.0 | +3bfc4626-3226-44b6-a401-ff9c18761448 / -— |
| Jogador 5 | 4-7 | 520 | MOVE_BENCH | STABILIZE | 20.0 | 7 | 92 | 5 | 38.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27909886837005615 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 521 | BUY | STABILIZE | 20.0 | 7 | 92 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24279046058654785 | 0.0 | 0.0 | +023f01af-91d0-4e07-8229-2b7cded83151 / -— |
| Jogador 5 | 4-7 | 522 | PASS | STABILIZE | 20.0 | 7 | 91 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.022142181172966957 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 531 | EQUIP_FROM_INVENTORY | STABILIZE | 20.0 | 7 | 102 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 532 | SELL | STABILIZE | 20.0 | 7 | 102 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04476923123002052 | 0.0 | 0.0 | +— / -023f01af-91d0-4e07-8229-2b7cded83151 |
| Jogador 5 | 5-1 | 533 | BUY | STABILIZE | 20.0 | 7 | 103 | 5 | 46.0 | Congregação das Bruxas/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.019621729850769 | 0.0 | 0.0 | +6eecc806-dcf8-47df-bc1d-bc5bc5f07099 / -68b28241-1946-4304-8b10-ae24a13a8e60,e8c36276-b932-45ba-b350-2d1cb339a019 |
| Jogador 5 | 5-1 | 534 | BUY | STABILIZE | 20.0 | 7 | 100 | 5 | 40.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.04196269437670708 | 0.0 | 0.0 | +3a86599a-ebbe-4e57-8284-69fdd6e2d8a1 / -— |
| Jogador 5 | 5-1 | 535 | SELL | STABILIZE | 20.0 | 7 | 96 | 5 | 40.0 | Congregação das Bruxas/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0370769239962101 | 0.0 | 0.0 | +— / -3bfc4626-3226-44b6-a401-ff9c18761448 |
| Jogador 5 | 5-1 | 536 | BUY | STABILIZE | 20.0 | 7 | 98 | 5 | 40.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.056872740387916565 | 0.0 | 0.0 | +5b97084e-3b94-485f-bc9b-e5c6cbe90dd0 / -— |
| Jogador 5 | 5-1 | 537 | MOVE_BOARD | STABILIZE | 20.0 | 7 | 94 | 5 | 40.0 | Congregação das Bruxas/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1491299569606781 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 538 | SELL | STABILIZE | 20.0 | 7 | 94 | 5 | 40.0 | Congregação das Bruxas/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.02476923167705536 | 0.0 | 0.0 | +— / -5b97084e-3b94-485f-bc9b-e5c6cbe90dd0 |
| Jogador 5 | 5-1 | 539 | BUY | STABILIZE | 20.0 | 7 | 98 | 5 | 40.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.20098364353179932 | 0.0 | 0.0 | +bae938fe-6a1c-4cd1-b700-508dd8adcca4 / -— |
| Jogador 5 | 5-1 | 540 | MOVE_BENCH | STABILIZE | 20.0 | 7 | 95 | 5 | 40.0 | Congregação das Bruxas/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6057687401771545 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 541 | PASS | STABILIZE | 20.0 | 7 | 95 | 5 | 52.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.024759097024798393 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 549 | BUY | ALL_IN | 6.0 | 7 | 106 | 5 | 52.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8114258050918579 | 0.0 | 0.0 | +0fd34229-b814-4580-8651-59e712d5657f / -— |
| Jogador 5 | 5-2 | 550 | MOVE_BOARD | ALL_IN | 6.0 | 7 | 103 | 5 | 52.0 | Congregação das Bruxas/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1207832396030426 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 551 | MOVE_BOARD | ALL_IN | 6.0 | 7 | 103 | 5 | 52.0 | Congregação das Bruxas/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.31047868728637695 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 552 | SELL | ALL_IN | 6.0 | 7 | 103 | 5 | 52.0 | Congregação das Bruxas/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03799999877810478 | 0.0 | 0.0 | +— / -bae938fe-6a1c-4cd1-b700-508dd8adcca4 |
| Jogador 5 | 5-2 | 553 | BUY | ALL_IN | 6.0 | 7 | 106 | 5 | 52.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.21423490345478058 | 0.0 | 0.0 | +80130f72-2d7c-49db-8d6f-4c0a962260e8 / -— |
| Jogador 5 | 5-2 | 554 | CRAFT_AND_EQUIP | ALL_IN | 6.0 | 7 | 103 | 5 | 52.0 | Congregação das Bruxas/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08671097457408905 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 555 | MOVE_BENCH | ALL_IN | 6.0 | 7 | 103 | 5 | 52.0 | Congregação das Bruxas/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5232452750205994 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 556 | BUY | ALL_IN | 6.0 | 7 | 103 | 5 | 58.0 | Congregação das Bruxas/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1043260246515274 | 0.0 | 0.0 | +bcd06176-e1d7-43fb-abd4-b6faea8c7927 / -— |
| Jogador 5 | 5-2 | 557 | MOVE_BOARD | ALL_IN | 6.0 | 7 | 101 | 5 | 58.0 | Congregação das Bruxas/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17991197109222412 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 558 | MOVE_BOARD | ALL_IN | 6.0 | 7 | 101 | 5 | 58.0 | Congregação das Bruxas/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11312521249055862 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 559 | PASS | ALL_IN | 6.0 | 7 | 101 | 5 | 58.0 | Congregação das Bruxas/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07877159863710403 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 562 | PASS | ALL_IN | 0.0 | 7 | 101 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 579 | PASS | ALL_IN | 0.0 | 7 | 101 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 592 | PASS | ALL_IN | 0.0 | 7 | 101 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 609 | PASS | ALL_IN | 0.0 | 7 | 101 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 622 | PASS | ALL_IN | 0.0 | 7 | 101 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 638 | PASS | ALL_IN | 0.0 | 7 | 101 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 652 | PASS | ALL_IN | 0.0 | 7 | 101 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 667 | PASS | ALL_IN | 0.0 | 7 | 101 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 681 | PASS | ALL_IN | 0.0 | 7 | 101 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 695 | PASS | ALL_IN | 0.0 | 7 | 101 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-6 | 709 | PASS | ALL_IN | 0.0 | 7 | 101 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-7 | 719 | PASS | ALL_IN | 0.0 | 7 | 101 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 7-1 | 729 | PASS | ALL_IN | 0.0 | 7 | 101 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 7-2 | 741 | PASS | ALL_IN | 0.0 | 7 | 101 | 5 | 0.0 | Congregação das Bruxas/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0013076922623440623 | 0.0 | 0.0 | +— / -698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +9002992e-4dcd-4fec-939c-87393464a41d / -— |
| Jogador 6 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.5989939570426941 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.04858612269163132 | 0.0 | 0.0 | +4d0bf502-ac30-4cdb-9da7-4f9a7ab054b1 / -— |
| Jogador 6 | 1-2 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.063256859779358 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5112341642379761 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 36 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | 0.16915932297706604 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 37 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | 0.009241865947842598 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 38 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | -0.26040419936180115 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 39 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 57 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yunara | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.00015411031199619174 | 0.0 | 0.0 | +c3c53e80-c8e2-4774-afa2-9b0f4ab3b326 / -— |
| Jogador 6 | 1-3 | 58 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4716953933238983 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 59 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | -0.22886794805526733 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 60 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Yunara | MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 61 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Teemo | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 83 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.019240504130721092 | 0.0 | 0.0 | +c19cf6a8-c66e-4670-b0fc-fb83453f22e7 / -— |
| Jogador 6 | 1-4 | 84 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Teemo | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5099713802337646 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 85 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 12.0 | —/DA_18_Teemo | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23745623230934143 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 86 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 12.0 | —/DA_18_Teemo | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 109 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 12.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12824782729148865 | 0.0 | 0.0 | +75005e9c-56d1-48d6-815e-573e489e3dd7 / -— |
| Jogador 6 | 2-1 | 110 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5472433567047119 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 111 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 18.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16917099058628082 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 112 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 18.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1223379373550415 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 113 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27614808082580566 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 114 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5949190258979797 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 115 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 18.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 133 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 8 | 0 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2702406644821167 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 134 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 8 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.31020140647888184 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 135 | PASS | STABILIZE | 100.0 | 4 | 8 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 157 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 13 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7223007678985596 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 158 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 13 | 1 | 14.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029239356517791748 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 159 | SELL | STABILIZE | 96.0 | 4 | 13 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03880251944065094 | 0.0 | 0.0 | +— / -9002992e-4dcd-4fec-939c-87393464a41d |
| Jogador 6 | 2-3 | 160 | BUY | STABILIZE | 96.0 | 4 | 14 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9668525457382202 | 0.0 | 0.0 | +2ef60eed-d073-41a6-adec-4466c673b313 / -— |
| Jogador 6 | 2-3 | 161 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 12 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12174342572689056 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 162 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 12 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33236923813819885 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 163 | PASS | STABILIZE | 96.0 | 4 | 12 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 182 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 19 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17877012491226196 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 183 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 19 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 184 | PASS | STABILIZE | 89.0 | 4 | 19 | 1 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 205 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 26 | 2 | 18.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12174342572689056 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 206 | MOVE_BOARD | STABILIZE | 89.0 | 4 | 26 | 2 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11845695227384567 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 207 | BUY_XP | STABILIZE | 89.0 | 4 | 26 | 2 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07689999788999557 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 208 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 22 | 2 | 18.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5031178593635559 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 209 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 22 | 2 | 22.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.12869665026664734 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 210 | BUY | STABILIZE | 89.0 | 5 | 22 | 2 | 22.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.006132500246167183 | 0.0 | 0.0 | +c7d30607-e33e-4e6e-902a-3fd37223a8de / -— |
| Jogador 6 | 2-5 | 211 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 20 | 2 | 22.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14721408486366272 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 212 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 20 | 2 | 22.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17873352766036987 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 213 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 20 | 2 | 22.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28802114725112915 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 214 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 20 | 2 | 22.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16020812094211578 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 215 | PASS | STABILIZE | 89.0 | 5 | 20 | 2 | 22.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 227 | BUY | STABILIZE | 89.0 | 5 | 28 | 2 | 22.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.986165463924408 | 0.0 | 0.0 | +2938180d-94e5-4bb7-832e-baa51f820ba2 / -— |
| Jogador 6 | 2-6 | 228 | BUY | STABILIZE | 89.0 | 5 | 25 | 2 | 22.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4910292327404022 | 0.0 | 0.0 | +fee4e511-e40e-4114-a8b6-c2de73117e82 / -— |
| Jogador 6 | 2-6 | 229 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 22 | 2 | 22.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10357164591550827 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 230 | SELL | STABILIZE | 89.0 | 5 | 22 | 2 | 22.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0027083808090537786 | 0.0 | 0.0 | +— / -c7d30607-e33e-4e6e-902a-3fd37223a8de |
| Jogador 6 | 2-6 | 231 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 24 | 2 | 22.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15853549540042877 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 232 | SELL | STABILIZE | 89.0 | 5 | 24 | 2 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7375456094741821 | 0.0 | 0.0 | +— / -c3c53e80-c8e2-4774-afa2-9b0f4ab3b326 |
| Jogador 6 | 2-6 | 233 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 26 | 2 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011000559665262699 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 234 | SELL | STABILIZE | 89.0 | 5 | 26 | 2 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5811881422996521 | 0.0 | 0.0 | +— / -fee4e511-e40e-4114-a8b6-c2de73117e82 |
| Jogador 6 | 2-6 | 235 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 29 | 2 | 24.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1414959728717804 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 236 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 29 | 2 | 24.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.2673241198062897 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 237 | PASS | STABILIZE | 89.0 | 5 | 29 | 2 | 24.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 250 | BUY | SLOWROLL | 89.0 | 5 | 39 | 3 | 24.0 | Vivaz/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.34328514337539673 | 0.0 | 0.0 | +7c4fb31e-7de8-491a-bb02-ef0111cd9ede / -— |
| Jogador 6 | 2-7 | 251 | MOVE_BENCH | SLOWROLL | 89.0 | 5 | 36 | 3 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.44310256838798523 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 252 | MOVE_BENCH | SLOWROLL | 89.0 | 5 | 36 | 3 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 253 | PASS | SLOWROLL | 89.0 | 5 | 36 | 3 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 270 | BUY | SLOWROLL | 89.0 | 5 | 45 | 4 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2643352150917053 | 0.0 | 0.0 | +a04e9818-dfdd-4ed9-ab3a-93d41bb398c5 / -— |
| Jogador 6 | 3-1 | 271 | BUY | SLOWROLL | 89.0 | 5 | 42 | 4 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04218117520213127 | 0.0 | 0.0 | +4eedd873-e4ec-41e5-9f5e-48e443e80f86 / -— |
| Jogador 6 | 3-1 | 272 | BUY | SLOWROLL | 89.0 | 5 | 39 | 3 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.506173849105835 | 0.0 | 0.0 | +01afbfab-8e82-4eb4-9bb8-15b28253f059 / -— |
| Jogador 6 | 3-1 | 273 | BUY | SLOWROLL | 89.0 | 5 | 37 | 3 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49077239632606506 | 0.0 | 0.0 | +ab127012-83d7-46f0-a16c-b20582d1179b / -— |
| Jogador 6 | 3-1 | 274 | BUY | SLOWROLL | 89.0 | 5 | 35 | 3 | 24.0 | Vivaz/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21731925010681152 | 0.0 | 0.0 | +91f05e8c-f467-4f22-9cb0-c814ffa93198 / -— |
| Jogador 6 | 3-1 | 275 | MOVE_BENCH | SLOWROLL | 89.0 | 5 | 33 | 3 | 24.0 | Vivaz/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.001829981803894 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 276 | MOVE_BENCH | SLOWROLL | 89.0 | 5 | 33 | 3 | 22.0 | Vivaz/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20604386925697327 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 277 | PASS | SLOWROLL | 89.0 | 5 | 33 | 3 | 22.0 | Vivaz/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 289 | BUY | SLOWROLL | 78.0 | 5 | 41 | 4 | 22.0 | Vivaz/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7428002953529358 | 0.0 | 0.0 | +6e096b30-0b49-4a98-8596-8b05089793ae / -2938180d-94e5-4bb7-832e-baa51f820ba2,75005e9c-56d1-48d6-815e-573e489e3dd7 |
| Jogador 6 | 3-2 | 290 | BUY | SLOWROLL | 78.0 | 5 | 38 | 3 | 16.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1662198305130005 | 0.0 | 0.0 | +f97943e4-cef9-4576-a33f-f2212ade2ae9 / -— |
| Jogador 6 | 3-2 | 291 | BUY | SLOWROLL | 78.0 | 5 | 37 | 3 | 16.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07581128180027008 | 0.0 | 0.0 | +4278eb73-acda-419d-bf9e-53a29ff6900d / -— |
| Jogador 6 | 3-2 | 292 | BUY | SLOWROLL | 78.0 | 5 | 36 | 3 | 16.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0430024079978466 | 0.0 | 0.0 | +9204a42c-6310-4b08-9bc7-8a2e786b077a / -— |
| Jogador 6 | 3-2 | 293 | SELL | SLOWROLL | 78.0 | 5 | 35 | 3 | 16.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03823234885931015 | 0.0 | 0.0 | +— / -9204a42c-6310-4b08-9bc7-8a2e786b077a |
| Jogador 6 | 3-2 | 294 | BUY | SLOWROLL | 78.0 | 5 | 36 | 3 | 16.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11405069380998611 | 0.0 | 0.0 | +e29364db-c484-4e4d-954d-7f4940131ffc / -— |
| Jogador 6 | 3-2 | 295 | MOVE_BOARD | SLOWROLL | 78.0 | 5 | 35 | 3 | 16.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10523057729005814 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 296 | MOVE_BOARD | SLOWROLL | 78.0 | 5 | 35 | 3 | 16.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04948959872126579 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 297 | SELL | SLOWROLL | 78.0 | 5 | 35 | 3 | 16.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.052000001072883606 | 0.0 | 0.0 | +— / -4278eb73-acda-419d-bf9e-53a29ff6900d |
| Jogador 6 | 3-2 | 298 | MOVE_BOARD | SLOWROLL | 78.0 | 5 | 36 | 3 | 16.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12558716535568237 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 299 | PASS | SLOWROLL | 78.0 | 5 | 36 | 3 | 16.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 306 | BUY | SLOWROLL | 66.0 | 5 | 45 | 4 | 16.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21895179152488708 | 0.0 | 0.0 | +50f9a30c-27db-4ed0-804e-548f87950b17 / -— |
| Jogador 6 | 3-3 | 307 | SELL | SLOWROLL | 66.0 | 5 | 42 | 4 | 16.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03507692366838455 | 0.0 | 0.0 | +— / -e29364db-c484-4e4d-954d-7f4940131ffc |
| Jogador 6 | 3-3 | 308 | BUY | SLOWROLL | 66.0 | 5 | 43 | 4 | 16.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0851529985666275 | 0.0 | 0.0 | +ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b / -— |
| Jogador 6 | 3-3 | 309 | SELL | SLOWROLL | 66.0 | 5 | 40 | 4 | 16.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0033603275660425425 | 0.0 | 0.0 | +— / -f97943e4-cef9-4576-a33f-f2212ade2ae9 |
| Jogador 6 | 3-3 | 310 | BUY | SLOWROLL | 66.0 | 5 | 41 | 4 | 16.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.037605274468660355 | 0.0 | 0.0 | +25b16126-6e41-4649-a47f-42656ffc7a08 / -— |
| Jogador 6 | 3-3 | 311 | SELL | SLOWROLL | 66.0 | 5 | 39 | 3 | 16.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1340000033378601 | 0.0 | 0.0 | +— / -91f05e8c-f467-4f22-9cb0-c814ffa93198 |
| Jogador 6 | 3-3 | 312 | BUY | SLOWROLL | 66.0 | 5 | 41 | 4 | 16.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23189690709114075 | 0.0 | 0.0 | +952adeb2-fe24-47af-9748-5131b91dcc06 / -— |
| Jogador 6 | 3-3 | 313 | SELL | SLOWROLL | 66.0 | 5 | 40 | 4 | 16.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02025681547820568 | 0.0 | 0.0 | +— / -25b16126-6e41-4649-a47f-42656ffc7a08 |
| Jogador 6 | 3-3 | 314 | BUY | SLOWROLL | 66.0 | 5 | 42 | 4 | 16.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22515003383159637 | 0.0 | 0.0 | +31c30451-3999-47b1-8bcf-77e137137b2a / -— |
| Jogador 6 | 3-3 | 315 | SELL | SLOWROLL | 66.0 | 5 | 40 | 4 | 16.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05400000140070915 | 0.0 | 0.0 | +— / -31c30451-3999-47b1-8bcf-77e137137b2a |
| Jogador 6 | 3-3 | 316 | PASS | SLOWROLL | 66.0 | 5 | 42 | 4 | 16.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 323 | BUY | SLOWROLL | 53.0 | 5 | 52 | 5 | 16.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.042392779141664505 | 0.0 | 0.0 | +ea7e2f0c-7dec-42c0-86ac-e66997fb2e6c / -— |
| Jogador 6 | 3-4 | 324 | SELL | SLOWROLL | 53.0 | 5 | 49 | 4 | 16.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.272329717874527 | 0.0 | 0.0 | +— / -01afbfab-8e82-4eb4-9bb8-15b28253f059 |
| Jogador 6 | 3-4 | 325 | BUY | SLOWROLL | 53.0 | 5 | 51 | 5 | 16.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2997433841228485 | 0.0 | 0.0 | +d056a271-6a74-4e71-bde6-087b97d2c527 / -— |
| Jogador 6 | 3-4 | 326 | SELL | SLOWROLL | 53.0 | 5 | 48 | 4 | 16.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1340000033378601 | 0.0 | 0.0 | +— / -d056a271-6a74-4e71-bde6-087b97d2c527 |
| Jogador 6 | 3-4 | 327 | BUY | SLOWROLL | 53.0 | 5 | 51 | 5 | 16.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.039293717592954636 | 0.0 | 0.0 | +333cdd27-0114-4d36-8ffa-e79b0f43b8e8 / -— |
| Jogador 6 | 3-4 | 328 | SELL | SLOWROLL | 53.0 | 5 | 48 | 4 | 16.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09778352081775665 | 0.0 | 0.0 | +— / -333cdd27-0114-4d36-8ffa-e79b0f43b8e8 |
| Jogador 6 | 3-4 | 329 | BUY | SLOWROLL | 53.0 | 5 | 51 | 5 | 16.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2453196793794632 | 0.0 | 0.0 | +2ed895f2-1e83-426c-88fc-b9fb6403835d / -— |
| Jogador 6 | 3-4 | 330 | MOVE_BENCH | SLOWROLL | 53.0 | 5 | 48 | 4 | 16.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6942955255508423 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 331 | BUY | SLOWROLL | 53.0 | 5 | 48 | 4 | 22.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09029845148324966 | 0.0 | 0.0 | +4698e3b3-0833-4895-a1f1-26b372b2f965 / -— |
| Jogador 6 | 3-4 | 332 | MOVE_BOARD | SLOWROLL | 53.0 | 5 | 47 | 4 | 22.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05787229165434837 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 333 | PASS | SLOWROLL | 53.0 | 5 | 47 | 4 | 22.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 342 | SELL | SLOWROLL | 53.0 | 5 | 57 | 5 | 22.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04169230908155441 | 0.0 | 0.0 | +— / -2ed895f2-1e83-426c-88fc-b9fb6403835d |
| Jogador 6 | 3-5 | 343 | BUY | SLOWROLL | 53.0 | 5 | 60 | 5 | 22.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7066000699996948 | 0.0 | 0.0 | +06db3a99-d008-406a-ac86-30884335d7c2 / -— |
| Jogador 6 | 3-5 | 344 | SELL | SLOWROLL | 53.0 | 5 | 58 | 5 | 22.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0022182809188961983 | 0.0 | 0.0 | +— / -ad00d1ae-ec5b-4851-b111-8ae36d2b8d7b |
| Jogador 6 | 3-5 | 345 | BUY | SLOWROLL | 53.0 | 5 | 61 | 5 | 22.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2417730987071991 | 0.0 | 0.0 | +9443e3b5-f0a2-4ab7-8378-907a3d2bccaa / -— |
| Jogador 6 | 3-5 | 346 | SELL | SLOWROLL | 53.0 | 5 | 59 | 5 | 22.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -9443e3b5-f0a2-4ab7-8378-907a3d2bccaa |
| Jogador 6 | 3-5 | 347 | BUY | SLOWROLL | 53.0 | 5 | 61 | 5 | 22.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24175356328487396 | 0.0 | 0.0 | +6db008fd-a1dd-40ad-b3d2-583a4bbff9d4 / -— |
| Jogador 6 | 3-5 | 348 | SELL | SLOWROLL | 53.0 | 5 | 59 | 5 | 22.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -6db008fd-a1dd-40ad-b3d2-583a4bbff9d4 |
| Jogador 6 | 3-5 | 349 | BUY | SLOWROLL | 53.0 | 5 | 61 | 5 | 22.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24174658954143524 | 0.0 | 0.0 | +5b95b64a-b46a-4827-8613-307c8dadc072 / -— |
| Jogador 6 | 3-5 | 350 | SELL | SLOWROLL | 53.0 | 5 | 59 | 5 | 22.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -5b95b64a-b46a-4827-8613-307c8dadc072 |
| Jogador 6 | 3-5 | 351 | BUY | SLOWROLL | 53.0 | 5 | 61 | 5 | 22.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2355312556028366 | 0.0 | 0.0 | +506f7312-07d8-4165-bd67-f7a69cf9a19c / -— |
| Jogador 6 | 3-5 | 352 | PASS | SLOWROLL | 53.0 | 5 | 60 | 5 | 22.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004072675481438637 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 362 | SELL | SLOWROLL | 43.0 | 5 | 71 | 5 | 22.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0027118506841361523 | 0.0 | 0.0 | +— / -7c4fb31e-7de8-491a-bb02-ef0111cd9ede |
| Jogador 6 | 3-6 | 363 | BUY | SLOWROLL | 43.0 | 5 | 74 | 5 | 22.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2411089390516281 | 0.0 | 0.0 | +604cc5dc-6c20-4d5a-b3a7-8862adfe1930 / -— |
| Jogador 6 | 3-6 | 364 | SELL | SLOWROLL | 43.0 | 5 | 72 | 5 | 22.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -604cc5dc-6c20-4d5a-b3a7-8862adfe1930 |
| Jogador 6 | 3-6 | 365 | BUY | SLOWROLL | 43.0 | 5 | 74 | 5 | 22.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6936026811599731 | 0.0 | 0.0 | +171724e7-58bd-404f-820b-2bb32c5c193e / -— |
| Jogador 6 | 3-6 | 366 | SELL | SLOWROLL | 43.0 | 5 | 73 | 5 | 22.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2918461561203003 | 0.0 | 0.0 | +— / -4698e3b3-0833-4895-a1f1-26b372b2f965 |
| Jogador 6 | 3-6 | 367 | BUY | SLOWROLL | 43.0 | 5 | 74 | 5 | 22.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24124957621097565 | 0.0 | 0.0 | +cf68219b-1d38-45a1-98db-495871c932ea / -— |
| Jogador 6 | 3-6 | 368 | SELL | SLOWROLL | 43.0 | 5 | 72 | 5 | 22.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -cf68219b-1d38-45a1-98db-495871c932ea |
| Jogador 6 | 3-6 | 369 | BUY | SLOWROLL | 43.0 | 5 | 74 | 5 | 22.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24126000702381134 | 0.0 | 0.0 | +ab472080-6e4b-4b75-b37d-cf10da9a5a0d / -— |
| Jogador 6 | 3-6 | 370 | SELL | SLOWROLL | 43.0 | 5 | 72 | 5 | 22.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -ab472080-6e4b-4b75-b37d-cf10da9a5a0d |
| Jogador 6 | 3-6 | 371 | BUY | SLOWROLL | 43.0 | 5 | 74 | 5 | 22.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15904852747917175 | 0.0 | 0.0 | +ab050f92-777b-429f-9ed8-9b6c63794641 / -— |
| Jogador 6 | 3-6 | 372 | PASS | SLOWROLL | 43.0 | 5 | 73 | 5 | 22.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01106504537165165 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 381 | SELL | STABILIZE | 32.0 | 6 | 85 | 5 | 22.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00020266631327103823 | 0.0 | 0.0 | +— / -ab050f92-777b-429f-9ed8-9b6c63794641 |
| Jogador 6 | 3-7 | 382 | BUY | STABILIZE | 32.0 | 6 | 86 | 5 | 22.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2668989300727844 | 0.0 | 0.0 | +891aea62-e06a-46d4-8250-a3d4a56e847d / -— |
| Jogador 6 | 3-7 | 383 | SELL | STABILIZE | 32.0 | 6 | 82 | 5 | 22.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6235592365264893 | 0.0 | 0.0 | +— / -506f7312-07d8-4165-bd67-f7a69cf9a19c |
| Jogador 6 | 3-7 | 384 | BUY | STABILIZE | 32.0 | 6 | 83 | 5 | 22.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9390773177146912 | 0.0 | 0.0 | +89cec488-9a0e-4838-b486-2504a0742476 / -06db3a99-d008-406a-ac86-30884335d7c2,2ef60eed-d073-41a6-adec-4466c673b313 |
| Jogador 6 | 3-7 | 385 | BUY | STABILIZE | 32.0 | 6 | 81 | 5 | 18.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17051303386688232 | 0.0 | 0.0 | +665661af-7240-4a65-bf3d-f4ecf3532a85 / -— |
| Jogador 6 | 3-7 | 386 | MOVE_BENCH | STABILIZE | 32.0 | 6 | 78 | 5 | 18.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3225640654563904 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 387 | BUY | STABILIZE | 32.0 | 6 | 78 | 5 | 26.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22948235273361206 | 0.0 | 0.0 | +604a85af-ff68-41a7-8795-73fdc7723c0e / -— |
| Jogador 6 | 3-7 | 388 | MOVE_BOARD | STABILIZE | 32.0 | 6 | 76 | 5 | 26.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12169558554887772 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 389 | MOVE_BOARD | STABILIZE | 32.0 | 6 | 76 | 5 | 26.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06667235493659973 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 390 | SELL | STABILIZE | 32.0 | 6 | 76 | 5 | 26.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -604a85af-ff68-41a7-8795-73fdc7723c0e |
| Jogador 6 | 3-7 | 391 | PASS | STABILIZE | 32.0 | 6 | 78 | 5 | 26.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014011009596288204 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 402 | BUY | STABILIZE | 32.0 | 6 | 90 | 5 | 26.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8089702129364014 | 0.0 | 0.0 | +f6b79583-b2fa-49a2-8adf-9b529a9eb3ae / -— |
| Jogador 6 | 4-1 | 403 | SELL | STABILIZE | 32.0 | 6 | 87 | 5 | 26.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04169230908155441 | 0.0 | 0.0 | +— / -665661af-7240-4a65-bf3d-f4ecf3532a85 |
| Jogador 6 | 4-1 | 404 | BUY | STABILIZE | 32.0 | 6 | 90 | 5 | 26.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10468816757202148 | 0.0 | 0.0 | +a8a8381a-f3a8-45ec-9106-293d73fca0c8 / -— |
| Jogador 6 | 4-1 | 405 | SELL | STABILIZE | 32.0 | 6 | 88 | 5 | 26.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02872636914253235 | 0.0 | 0.0 | +— / -a8a8381a-f3a8-45ec-9106-293d73fca0c8 |
| Jogador 6 | 4-1 | 406 | BUY | STABILIZE | 32.0 | 6 | 90 | 5 | 26.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2295127958059311 | 0.0 | 0.0 | +78525c90-c4d2-425d-ba90-a03664c60a28 / -— |
| Jogador 6 | 4-1 | 407 | SELL | STABILIZE | 32.0 | 6 | 88 | 5 | 26.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -78525c90-c4d2-425d-ba90-a03664c60a28 |
| Jogador 6 | 4-1 | 408 | BUY | STABILIZE | 32.0 | 6 | 90 | 5 | 26.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09404981881380081 | 0.0 | 0.0 | +3d7ba32f-3349-479e-bb6f-9cd1f2006149 / -— |
| Jogador 6 | 4-1 | 409 | MOVE_BENCH | STABILIZE | 32.0 | 6 | 89 | 5 | 26.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5478871464729309 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 410 | BUY | STABILIZE | 32.0 | 6 | 89 | 5 | 32.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10898788273334503 | 0.0 | 0.0 | +45d53a67-4ed4-495d-8751-5ea0f72f91e9 / -— |
| Jogador 6 | 4-1 | 411 | MOVE_BOARD | STABILIZE | 32.0 | 6 | 88 | 5 | 32.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 412 | PASS | STABILIZE | 32.0 | 6 | 88 | 5 | 32.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020212503150105476 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 422 | SELL | STABILIZE | 20.0 | 6 | 101 | 5 | 32.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03144625946879387 | 0.0 | 0.0 | +— / -45d53a67-4ed4-495d-8751-5ea0f72f91e9 |
| Jogador 6 | 4-2 | 423 | BUY | STABILIZE | 20.0 | 6 | 102 | 5 | 32.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22994442284107208 | 0.0 | 0.0 | +86530a1f-5325-45fa-bf43-86419ccfda54 / -— |
| Jogador 6 | 4-2 | 424 | SELL | STABILIZE | 20.0 | 6 | 99 | 5 | 32.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.030637703835964203 | 0.0 | 0.0 | +— / -3d7ba32f-3349-479e-bb6f-9cd1f2006149 |
| Jogador 6 | 4-2 | 425 | BUY | STABILIZE | 20.0 | 6 | 100 | 5 | 32.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17761601507663727 | 0.0 | 0.0 | +7fd8b302-97aa-4373-94f4-adfcad477ed2 / -— |
| Jogador 6 | 4-2 | 426 | MOVE_BOARD | STABILIZE | 20.0 | 6 | 97 | 5 | 32.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08374926447868347 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 427 | MOVE_BOARD | STABILIZE | 20.0 | 6 | 97 | 5 | 32.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04875248298048973 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 428 | SELL | STABILIZE | 20.0 | 6 | 97 | 5 | 32.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04169230908155441 | 0.0 | 0.0 | +— / -7fd8b302-97aa-4373-94f4-adfcad477ed2 |
| Jogador 6 | 4-2 | 429 | BUY | STABILIZE | 20.0 | 6 | 100 | 5 | 32.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17760136723518372 | 0.0 | 0.0 | +93f7279f-b03b-407b-b623-c0a2bd88f877 / -— |
| Jogador 6 | 4-2 | 430 | PASS | STABILIZE | 20.0 | 6 | 97 | 5 | 32.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0260853823274374 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 441 | SELL | ALL_IN | 8.0 | 6 | 110 | 5 | 32.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04169230908155441 | 0.0 | 0.0 | +— / -93f7279f-b03b-407b-b623-c0a2bd88f877 |
| Jogador 6 | 4-3 | 442 | BUY | ALL_IN | 8.0 | 6 | 113 | 5 | 32.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16780412197113037 | 0.0 | 0.0 | +03e5f6e4-e80d-49c1-b5bb-e5b158d96f51 / -— |
| Jogador 6 | 4-3 | 443 | SELL | ALL_IN | 8.0 | 6 | 109 | 5 | 32.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0159563347697258 | 0.0 | 0.0 | +— / -ea7e2f0c-7dec-42c0-86ac-e66997fb2e6c |
| Jogador 6 | 4-3 | 444 | BUY | ALL_IN | 8.0 | 6 | 112 | 5 | 32.0 | Carrasco/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11592376977205276 | 0.0 | 0.0 | +840740a6-45be-4107-a4b7-b10cefe1a667 / -— |
| Jogador 6 | 4-3 | 445 | MOVE_BENCH | ALL_IN | 8.0 | 6 | 110 | 5 | 32.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0017942195991054177 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 446 | PASS | ALL_IN | 8.0 | 6 | 110 | 5 | 34.0 | Carrasco/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0849672332406044 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 461 | PASS | ALL_IN | 0.0 | 6 | 110 | 5 | 0.0 | Carrasco/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 481 | PASS | ALL_IN | 0.0 | 6 | 110 | 5 | 0.0 | Carrasco/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 500 | PASS | ALL_IN | 0.0 | 6 | 110 | 5 | 0.0 | Carrasco/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 512 | PASS | ALL_IN | 0.0 | 6 | 110 | 5 | 0.0 | Carrasco/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 531 | PASS | ALL_IN | 0.0 | 6 | 110 | 5 | 0.0 | Carrasco/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 549 | PASS | ALL_IN | 0.0 | 6 | 110 | 5 | 0.0 | Carrasco/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 562 | PASS | ALL_IN | 0.0 | 6 | 110 | 5 | 0.0 | Carrasco/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 579 | PASS | ALL_IN | 0.0 | 6 | 110 | 5 | 0.0 | Carrasco/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 592 | PASS | ALL_IN | 0.0 | 6 | 110 | 5 | 0.0 | Carrasco/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 609 | PASS | ALL_IN | 0.0 | 6 | 110 | 5 | 0.0 | Carrasco/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 622 | PASS | ALL_IN | 0.0 | 6 | 110 | 5 | 0.0 | Carrasco/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 638 | PASS | ALL_IN | 0.0 | 6 | 110 | 5 | 0.0 | Carrasco/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 652 | PASS | ALL_IN | 0.0 | 6 | 110 | 5 | 0.0 | Carrasco/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-3 | 667 | PASS | ALL_IN | 0.0 | 6 | 110 | 5 | 0.0 | Carrasco/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-4 | 681 | PASS | ALL_IN | 0.0 | 6 | 110 | 5 | 0.0 | Carrasco/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-5 | 695 | PASS | ALL_IN | 0.0 | 6 | 110 | 5 | 0.0 | Carrasco/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-6 | 709 | PASS | ALL_IN | 0.0 | 6 | 110 | 5 | 0.0 | Carrasco/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-7 | 719 | PASS | ALL_IN | 0.0 | 6 | 110 | 5 | 0.0 | Carrasco/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-1 | 729 | PASS | ALL_IN | 0.0 | 6 | 110 | 5 | 0.0 | Carrasco/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-2 | 741 | PASS | ALL_IN | 0.0 | 6 | 110 | 5 | 0.0 | Carrasco/DA_18_Rammus | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.019615383818745613 | 0.0 | 0.0 | +— / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987 |
| Jogador 7 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +c2a4318c-af60-41e2-8e14-c3ad967569a0 / -— |
| Jogador 7 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.5989939570426941 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.0015799786197021604 | 0.0 | 0.0 | +47ec6577-cbf2-4275-b185-c19256223441 / -— |
| Jogador 7 | 1-2 | 34 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0010130808223038912 | 0.0 | 0.0 | +b21d3fc8-71ce-4669-b0ba-931c6e11cb69 / -— |
| Jogador 7 | 1-2 | 35 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16143697500228882 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 36 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11297382414340973 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 37 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3665514886379242 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 38 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.11687260121107101 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 39 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.324565052986145 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 40 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.06377681344747543 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 41 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.1164223775267601 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 42 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.21995483338832855 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 43 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 57 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.31158682703971863 | 0.0 | 0.0 | +734c75dd-d0f3-4b9f-abe8-a228e23557a2 / -— |
| Jogador 7 | 1-3 | 58 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11602666974067688 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21782711148262024 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 60 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013322947546839714 | 0.0 | 0.0 | +— / -47ec6577-cbf2-4275-b185-c19256223441 |
| Jogador 7 | 1-3 | 61 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BOARD, PASS | True | True | 0.04875248298048973 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 62 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 83 | PASS | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 109 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2626096308231354 | 0.0 | 0.0 | +de82e676-8d8b-4437-958e-a8398a3cfade / -— |
| Jogador 7 | 2-1 | 110 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40630507469177246 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 111 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.051634397357702255 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 112 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.14029812812805176 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 113 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.05448774993419647 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 114 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.042908359318971634 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 115 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.12371200323104858 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 116 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 117 | PASS | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 133 | BUY | STABILIZE | 100.0 | 4 | 12 | 1 | 12.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2880861461162567 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 134 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 9 | 0 | 12.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13460886478424072 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 135 | BUY_XP | STABILIZE | 100.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 136 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.047200001776218414 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 137 | SELL | STABILIZE | 100.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Hecarim | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04130205884575844 | 0.0 | 0.0 | +— / -b21d3fc8-71ce-4669-b0ba-931c6e11cb69 |
| Jogador 7 | 2-2 | 138 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 2 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.006247489247471094 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 139 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 2 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.009366531856358051 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 140 | PASS | STABILIZE | 100.0 | 5 | 2 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 157 | BUY | STABILIZE | 100.0 | 5 | 9 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9674413800239563 | 0.0 | 0.0 | +4367c039-e64e-4a3c-a49f-57cb2674a08f / -— |
| Jogador 7 | 2-3 | 158 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49713897705078125 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 159 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.05787229165434837 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 160 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 161 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0024998392909765244 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 162 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.12169558554887772 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 163 | BUY_XP | STABILIZE | 100.0 | 5 | 7 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 164 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.12169558554887772 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 165 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.029725274071097374 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 166 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.1297316998243332 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 167 | PASS | STABILIZE | 100.0 | 5 | 3 | 0 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 182 | BUY | STABILIZE | 100.0 | 5 | 10 | 1 | 20.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3302915096282959 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 183 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 20.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05298372730612755 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 184 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 26.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 185 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 26.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0602034367620945 | 0.0 | 0.0 | +— / -c2a4318c-af60-41e2-8e14-c3ad967569a0 |
| Jogador 7 | 2-4 | 186 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 3 | 0 | 26.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 187 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 3 | 0 | 26.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 188 | PASS | STABILIZE | 100.0 | 5 | 3 | 0 | 26.0 | —/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 205 | BUY | STABILIZE | 100.0 | 5 | 9 | 0 | 26.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4278099238872528 | 0.0 | 0.0 | +599caeca-96ef-4308-b6cd-f65b005879e2 / -— |
| Jogador 7 | 2-5 | 206 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 6 | 0 | 26.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20911607146263123 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 207 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 28.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 208 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 2 | 0 | 28.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01991809904575348 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 209 | SELL | STABILIZE | 100.0 | 5 | 2 | 0 | 28.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7201318144798279 | 0.0 | 0.0 | +— / -4367c039-e64e-4a3c-a49f-57cb2674a08f |
| Jogador 7 | 2-5 | 210 | BUY_XP | STABILIZE | 100.0 | 5 | 4 | 0 | 28.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.026499999687075615 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 211 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 0 | 0 | 28.0 | Sabugueiro/DA_Sentinel18 | MOVE_BOARD, PASS | True | True | -0.11087857931852341 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 212 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 0 | 0 | 28.0 | Sabugueiro/DA_Sentinel18 | MOVE_BOARD, PASS | True | True | -0.322867214679718 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 213 | PASS | STABILIZE | 100.0 | 6 | 0 | 0 | 28.0 | Sabugueiro/DA_Sentinel18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 227 | BUY | STABILIZE | 100.0 | 6 | 7 | 0 | 28.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.36103928089141846 | 0.0 | 0.0 | +6c691ca5-c042-46de-8d64-493514f2d793 / -— |
| Jogador 7 | 2-6 | 228 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 4 | 0 | 28.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4401262700557709 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 229 | BUY | STABILIZE | 100.0 | 6 | 4 | 0 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.47296223044395447 | 0.0 | 0.0 | +a9f7f52e-6619-4669-9b8a-390b99fd73d8 / -— |
| Jogador 7 | 2-6 | 230 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 2 | 0 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03247396647930145 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 231 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 2 | 0 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17403410375118256 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 232 | SELL | STABILIZE | 100.0 | 6 | 2 | 0 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.522962212562561 | 0.0 | 0.0 | +— / -a9f7f52e-6619-4669-9b8a-390b99fd73d8 |
| Jogador 7 | 2-6 | 233 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 4 | 0 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.13391032814979553 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 234 | BUY_XP | STABILIZE | 100.0 | 6 | 4 | 0 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 235 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 0 | 0 | 34.0 | Sabugueiro/DA_Sentinel18 | MOVE_BOARD, PASS | True | True | 0.032957449555397034 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 236 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 0 | 0 | 34.0 | Sabugueiro/DA_Sentinel18 | MOVE_BOARD, PASS | True | True | -0.32208600640296936 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 237 | PASS | STABILIZE | 100.0 | 6 | 0 | 0 | 34.0 | Sabugueiro/DA_Sentinel18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 250 | BUY | STABILIZE | 100.0 | 6 | 8 | 0 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.2640096843242645 | 0.0 | 0.0 | +584991bb-37b3-4ac1-8e29-14e0d74c5e78 / -— |
| Jogador 7 | 2-7 | 251 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 5 | 0 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7508270740509033 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 252 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 5 | 0 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09962999820709229 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 253 | BUY_XP | STABILIZE | 100.0 | 6 | 5 | 0 | 36.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 254 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 1 | 0 | 36.0 | Sabugueiro/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10453628748655319 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 255 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 1 | 0 | 36.0 | Sabugueiro/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06739011406898499 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 256 | SELL | STABILIZE | 100.0 | 6 | 1 | 0 | 36.0 | Sabugueiro/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016127778217196465 | 0.0 | 0.0 | +— / -734c75dd-d0f3-4b9f-abe8-a228e23557a2 |
| Jogador 7 | 2-7 | 257 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 3 | 0 | 36.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 258 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 3 | 0 | 36.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 259 | PASS | STABILIZE | 100.0 | 6 | 3 | 0 | 36.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 270 | BUY | STABILIZE | 100.0 | 6 | 10 | 1 | 36.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.12484398484230042 | 0.0 | 0.0 | +ad1693cd-1ab5-43a9-8164-25929b8bd68e / -— |
| Jogador 7 | 3-1 | 271 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 7 | 0 | 36.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3229232430458069 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 272 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 7 | 0 | 38.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33002007007598877 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 273 | PASS | STABILIZE | 100.0 | 6 | 7 | 0 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 289 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 12 | 1 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1752718836069107 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 290 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 12 | 1 | 36.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7507910132408142 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 291 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 12 | 1 | 38.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5319251418113708 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 292 | PASS | STABILIZE | 90.0 | 6 | 12 | 1 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 306 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 19 | 1 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1752718836069107 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 307 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 19 | 1 | 36.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8552320003509521 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 308 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 19 | 1 | 36.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3472914695739746 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 309 | PASS | STABILIZE | 90.0 | 6 | 19 | 1 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 323 | BUY | STABILIZE | 90.0 | 6 | 28 | 2 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6137334704399109 | 0.0 | 0.0 | +cfe17b3a-c9b6-4e09-9ba1-23e762a72569 / -— |
| Jogador 7 | 3-4 | 324 | BUY | STABILIZE | 90.0 | 6 | 25 | 2 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18937551975250244 | 0.0 | 0.0 | +86c1ac55-598e-426a-86ea-64249f82b085 / -— |
| Jogador 7 | 3-4 | 325 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 22 | 2 | 34.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17575545608997345 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 326 | BUY_XP | STABILIZE | 90.0 | 6 | 22 | 2 | 36.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 327 | BUY_XP | STABILIZE | 90.0 | 6 | 18 | 1 | 36.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 328 | BUY_XP | STABILIZE | 90.0 | 6 | 14 | 1 | 36.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 329 | BUY_XP | STABILIZE | 90.0 | 6 | 10 | 1 | 36.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03790000081062317 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 330 | MOVE_BENCH | STABILIZE | 90.0 | 7 | 6 | 0 | 36.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14625979959964752 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 331 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 6 | 0 | 42.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.033435843884944916 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 332 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 6 | 0 | 42.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 333 | PASS | STABILIZE | 90.0 | 7 | 6 | 0 | 42.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 342 | BUY | STABILIZE | 90.0 | 7 | 12 | 1 | 42.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4468057453632355 | 0.0 | 0.0 | +f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e / -— |
| Jogador 7 | 3-5 | 343 | BUY | STABILIZE | 90.0 | 7 | 9 | 0 | 42.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7453377842903137 | 0.0 | 0.0 | +7c8b3027-1434-4346-95b3-5463e8a4aa9b / -— |
| Jogador 7 | 3-5 | 344 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 7 | 0 | 42.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 345 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 7 | 0 | 42.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.007139110006392002 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 346 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 7 | 0 | 42.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 347 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 7 | 0 | 42.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028333866968750954 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 348 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 7 | 0 | 42.0 | Sabugueiro/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.052043795585632324 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 349 | MOVE_BOARD | STABILIZE | 90.0 | 7 | 7 | 0 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1742371916770935 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 350 | SELL | STABILIZE | 90.0 | 7 | 7 | 0 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7953377962112427 | 0.0 | 0.0 | +— / -7c8b3027-1434-4346-95b3-5463e8a4aa9b |
| Jogador 7 | 3-5 | 351 | SELL | STABILIZE | 90.0 | 7 | 9 | 0 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2513076961040497 | 0.0 | 0.0 | +— / -584991bb-37b3-4ac1-8e29-14e0d74c5e78 |
| Jogador 7 | 3-5 | 352 | PASS | STABILIZE | 90.0 | 7 | 12 | 1 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 362 | BUY | STABILIZE | 90.0 | 7 | 20 | 2 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19626706838607788 | 0.0 | 0.0 | +6caec849-54f8-4ec1-90a4-fc0587510013 / -— |
| Jogador 7 | 3-6 | 363 | BUY | STABILIZE | 90.0 | 7 | 16 | 1 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01391522865742445 | 0.0 | 0.0 | +1726bcae-3006-426c-a6c7-4e317e10b637 / -— |
| Jogador 7 | 3-6 | 364 | BUY | STABILIZE | 90.0 | 7 | 12 | 1 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4478689134120941 | 0.0 | 0.0 | +a1aa0280-2379-4d0b-a475-143c1a2f6c25 / -— |
| Jogador 7 | 3-6 | 365 | SELL | STABILIZE | 90.0 | 7 | 8 | 0 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24626706540584564 | 0.0 | 0.0 | +— / -6caec849-54f8-4ec1-90a4-fc0587510013 |
| Jogador 7 | 3-6 | 366 | SELL | STABILIZE | 90.0 | 7 | 12 | 1 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6609272360801697 | 0.0 | 0.0 | +— / -f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e |
| Jogador 7 | 3-6 | 367 | SELL | STABILIZE | 90.0 | 7 | 15 | 1 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3380429148674011 | 0.0 | 0.0 | +— / -86c1ac55-598e-426a-86ea-64249f82b085 |
| Jogador 7 | 3-6 | 368 | BUY | STABILIZE | 90.0 | 7 | 18 | 1 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08563046902418137 | 0.0 | 0.0 | +d69fa0dc-74b6-4ee7-90f7-aaca5405c59c / -— |
| Jogador 7 | 3-6 | 369 | SELL | STABILIZE | 90.0 | 7 | 14 | 1 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19269230961799622 | 0.0 | 0.0 | +— / -d69fa0dc-74b6-4ee7-90f7-aaca5405c59c |
| Jogador 7 | 3-6 | 370 | SELL | STABILIZE | 90.0 | 7 | 18 | 1 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7831538319587708 | 0.0 | 0.0 | +— / -1726bcae-3006-426c-a6c7-4e317e10b637 |
| Jogador 7 | 3-6 | 371 | SELL | STABILIZE | 90.0 | 7 | 22 | 2 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5403845906257629 | 0.0 | 0.0 | +— / -a1aa0280-2379-4d0b-a475-143c1a2f6c25 |
| Jogador 7 | 3-6 | 372 | PASS | STABILIZE | 90.0 | 7 | 26 | 2 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 381 | BUY | FAST8 | 79.0 | 7 | 33 | 3 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6318921446800232 | 0.0 | 0.0 | +8a52858d-da47-4de9-8e91-8612788cb8fd / -— |
| Jogador 7 | 3-7 | 382 | BUY | STABILIZE | 79.0 | 7 | 29 | 2 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06622111052274704 | 0.0 | 0.0 | +06fb62e5-6766-4156-bf7d-0da443a9b20c / -— |
| Jogador 7 | 3-7 | 383 | MOVE_BENCH | STABILIZE | 79.0 | 7 | 26 | 2 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26331424713134766 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 384 | MOVE_BENCH | STABILIZE | 79.0 | 7 | 26 | 2 | 44.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29550448060035706 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 385 | PASS | STABILIZE | 79.0 | 7 | 26 | 2 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007499999832361937 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 402 | BUY | FAST8 | 79.0 | 7 | 33 | 3 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29545873403549194 | 0.0 | 0.0 | +6a30a366-c631-429d-9523-af769cdf48a4 / -— |
| Jogador 7 | 4-1 | 403 | BUY | FAST8 | 79.0 | 7 | 30 | 3 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029713232070207596 | 0.0 | 0.0 | +97d52b06-365b-44ad-b4f9-63e0f9503c8a / -— |
| Jogador 7 | 4-1 | 404 | MOVE_BENCH | STABILIZE | 79.0 | 7 | 27 | 2 | 42.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02383878082036972 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 405 | BUY_XP | STABILIZE | 79.0 | 7 | 27 | 2 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 406 | BUY_XP | STABILIZE | 79.0 | 7 | 23 | 2 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 407 | BUY_XP | STABILIZE | 79.0 | 7 | 19 | 1 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 408 | BUY_XP | STABILIZE | 79.0 | 7 | 15 | 1 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 409 | BUY_XP | STABILIZE | 79.0 | 7 | 11 | 1 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 410 | BUY_XP | STABILIZE | 79.0 | 7 | 7 | 0 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 411 | SELL | STABILIZE | 79.0 | 7 | 3 | 0 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0122307687997818 | 0.0 | 0.0 | +— / -de82e676-8d8b-4437-958e-a8398a3cfade |
| Jogador 7 | 4-1 | 412 | PASS | STABILIZE | 79.0 | 7 | 5 | 0 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 422 | BUY | STABILIZE | 79.0 | 7 | 11 | 1 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1838427484035492 | 0.0 | 0.0 | +00f38555-1887-4fe2-9930-934055269095 / -— |
| Jogador 7 | 4-2 | 423 | PASS | STABILIZE | 79.0 | 7 | 9 | 0 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 441 | BUY | STABILIZE | 79.0 | 7 | 17 | 1 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005011424887925386 | 0.0 | 0.0 | +80c51b33-0a85-4f21-a797-9551aa10760f / -— |
| Jogador 7 | 4-3 | 442 | SELL | STABILIZE | 79.0 | 7 | 13 | 1 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014384615235030651 | 0.0 | 0.0 | +— / -97d52b06-365b-44ad-b4f9-63e0f9503c8a |
| Jogador 7 | 4-3 | 443 | BUY | STABILIZE | 79.0 | 7 | 16 | 1 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.058599457144737244 | 0.0 | 0.0 | +c7841e00-91da-410b-b00f-62f4bf32f666 / -— |
| Jogador 7 | 4-3 | 444 | PASS | STABILIZE | 79.0 | 7 | 13 | 1 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 461 | BUY | STABILIZE | 79.0 | 7 | 21 | 2 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6787540912628174 | 0.0 | 0.0 | +5b6dec85-6970-4575-b364-21c3123995a5 / -— |
| Jogador 7 | 4-4 | 462 | BUY | STABILIZE | 79.0 | 7 | 18 | 1 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6829758286476135 | 0.0 | 0.0 | +677ea844-e1bf-4c68-a0b0-136abb86ba7b / -— |
| Jogador 7 | 4-4 | 463 | BUY | STABILIZE | 79.0 | 7 | 15 | 1 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7087541222572327 | 0.0 | 0.0 | +15c93ffb-d63e-43e6-aa46-ba2beed9cb53 / -— |
| Jogador 7 | 4-4 | 464 | BUY | STABILIZE | 79.0 | 7 | 12 | 1 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.056616686284542084 | 0.0 | 0.0 | +b755a0c5-f515-4f95-8f58-1e05f40ad302 / -— |
| Jogador 7 | 4-4 | 465 | PASS | STABILIZE | 79.0 | 7 | 10 | 1 | 46.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 481 | SELL | STABILIZE | 79.0 | 7 | 17 | 1 | 46.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029411641880869865 | 0.0 | 0.0 | +— / -b755a0c5-f515-4f95-8f58-1e05f40ad302 |
| Jogador 7 | 4-5 | 482 | BUY | STABILIZE | 79.0 | 7 | 19 | 1 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2503148317337036 | 0.0 | 0.0 | +111acae7-a889-409f-a15e-419d250fccd0 / -— |
| Jogador 7 | 4-5 | 483 | SELL | STABILIZE | 79.0 | 7 | 15 | 1 | 46.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26937881112098694 | 0.0 | 0.0 | +— / -6a30a366-c631-429d-9523-af769cdf48a4 |
| Jogador 7 | 4-5 | 484 | BUY | STABILIZE | 79.0 | 7 | 18 | 1 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0550115741789341 | 0.0 | 0.0 | +c49cf468-6fa4-4d94-bc3a-9dc8f7111626 / -— |
| Jogador 7 | 4-5 | 485 | SELL | STABILIZE | 79.0 | 7 | 15 | 1 | 46.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04153846204280853 | 0.0 | 0.0 | +— / -c49cf468-6fa4-4d94-bc3a-9dc8f7111626 |
| Jogador 7 | 4-5 | 486 | BUY | STABILIZE | 79.0 | 7 | 18 | 1 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009072234854102135 | 0.0 | 0.0 | +9d2d95f2-c079-43eb-a4cd-37b224a473a8 / -— |
| Jogador 7 | 4-5 | 487 | SELL | STABILIZE | 79.0 | 7 | 16 | 1 | 46.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03184615448117256 | 0.0 | 0.0 | +— / -9d2d95f2-c079-43eb-a4cd-37b224a473a8 |
| Jogador 7 | 4-5 | 488 | BUY | STABILIZE | 79.0 | 7 | 18 | 1 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009071899577975273 | 0.0 | 0.0 | +fcc4f620-7b85-40ed-a42c-2eadd37a82fd / -— |
| Jogador 7 | 4-5 | 489 | PASS | STABILIZE | 79.0 | 7 | 16 | 1 | 46.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 500 | SELL | STABILIZE | 79.0 | 7 | 24 | 2 | 46.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03184615448117256 | 0.0 | 0.0 | +— / -fcc4f620-7b85-40ed-a42c-2eadd37a82fd |
| Jogador 7 | 4-6 | 501 | BUY | STABILIZE | 79.0 | 7 | 26 | 2 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4316553473472595 | 0.0 | 0.0 | +ded275a3-9551-4816-8112-f0a25524412c / -— |
| Jogador 7 | 4-6 | 502 | SELL | STABILIZE | 79.0 | 7 | 23 | 2 | 46.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29163655638694763 | 0.0 | 0.0 | +— / -ded275a3-9551-4816-8112-f0a25524412c |
| Jogador 7 | 4-6 | 503 | BUY | STABILIZE | 79.0 | 7 | 26 | 2 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05368843302130699 | 0.0 | 0.0 | +42aa4dc8-e388-40dd-a210-4c59e358afcd / -— |
| Jogador 7 | 4-6 | 504 | SELL | STABILIZE | 79.0 | 7 | 23 | 2 | 46.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.042959585785865784 | 0.0 | 0.0 | +— / -42aa4dc8-e388-40dd-a210-4c59e358afcd |
| Jogador 7 | 4-6 | 505 | BUY | STABILIZE | 79.0 | 7 | 26 | 2 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2347688525915146 | 0.0 | 0.0 | +a5c83255-d413-4d36-92a8-3552e6785108 / -— |
| Jogador 7 | 4-6 | 506 | SELL | STABILIZE | 79.0 | 7 | 23 | 2 | 46.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.045230768620967865 | 0.0 | 0.0 | +— / -a5c83255-d413-4d36-92a8-3552e6785108 |
| Jogador 7 | 4-6 | 507 | SELL | STABILIZE | 79.0 | 7 | 26 | 2 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09315384924411774 | 0.0 | 0.0 | +— / -111acae7-a889-409f-a15e-419d250fccd0 |
| Jogador 7 | 4-6 | 508 | SELL | FAST8 | 79.0 | 7 | 30 | 3 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002230769256129861 | 0.0 | 0.0 | +— / -80c51b33-0a85-4f21-a797-9551aa10760f |
| Jogador 7 | 4-6 | 509 | PASS | FAST8 | 79.0 | 7 | 34 | 3 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 512 | BUY | FAST8 | 79.0 | 7 | 45 | 4 | 46.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8677166700363159 | 0.0 | 0.0 | +5c43307a-6d61-4493-a1ed-cb428d79a254 / -5b6dec85-6970-4575-b364-21c3123995a5,ad1693cd-1ab5-43a9-8164-25929b8bd68e |
| Jogador 7 | 4-7 | 513 | BUY | FAST8 | 79.0 | 7 | 42 | 4 | 40.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32340338826179504 | 0.0 | 0.0 | +5c931416-3aeb-40d4-9e6f-612b0d387226 / -— |
| Jogador 7 | 4-7 | 514 | BUY | FAST8 | 79.0 | 7 | 38 | 3 | 40.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6952765583992004 | 0.0 | 0.0 | +565ff610-fe51-470b-8452-a7eec5e31653 / -— |
| Jogador 7 | 4-7 | 515 | BUY | FAST8 | 79.0 | 7 | 36 | 3 | 40.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09157582372426987 | 0.0 | 0.0 | +db6b2dca-4de1-420e-aadb-943e19b6121a / -— |
| Jogador 7 | 4-7 | 516 | PASS | FAST8 | 79.0 | 7 | 34 | 3 | 40.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 524 | MOVE_BENCH | FAST8 | 79.0 | 7 | 34 | 3 | 40.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3956831693649292 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 531 | EQUIP_FROM_INVENTORY | FAST8 | 79.0 | 7 | 44 | 4 | 44.0 | Emanador/DA_Fiddlesticks18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 532 | BUY | FAST8 | 79.0 | 7 | 44 | 4 | 44.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3589368760585785 | 0.0 | 0.0 | +6722b147-c2a7-4fd0-a943-5036adb3e3a1 / -— |
| Jogador 7 | 5-1 | 533 | SELL | FAST8 | 79.0 | 7 | 39 | 3 | 44.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.09842171519994736 | 0.0 | 0.0 | +— / -db6b2dca-4de1-420e-aadb-943e19b6121a |
| Jogador 7 | 5-1 | 534 | BUY | FAST8 | 79.0 | 7 | 41 | 4 | 44.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8196778893470764 | 0.0 | 0.0 | +3b934078-806c-40f0-b102-e9131220f70e / -00f38555-1887-4fe2-9930-934055269095,565ff610-fe51-470b-8452-a7eec5e31653 |
| Jogador 7 | 5-1 | 535 | BUY | FAST8 | 79.0 | 7 | 39 | 3 | 40.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.24602438509464264 | 0.0 | 0.0 | +755060be-13bb-4686-9ee9-e53fef2d75b2 / -— |
| Jogador 7 | 5-1 | 536 | SELL | FAST8 | 79.0 | 7 | 36 | 3 | 40.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2683076858520508 | 0.0 | 0.0 | +— / -755060be-13bb-4686-9ee9-e53fef2d75b2 |
| Jogador 7 | 5-1 | 537 | BUY | FAST8 | 79.0 | 7 | 39 | 3 | 40.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.23197738826274872 | 0.0 | 0.0 | +04520fe5-4449-4632-b275-e5e28d642007 / -— |
| Jogador 7 | 5-1 | 538 | CRAFT_AND_EQUIP | FAST8 | 79.0 | 7 | 36 | 3 | 40.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.2242811620235443 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 539 | SELL | FAST8 | 79.0 | 7 | 36 | 3 | 40.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.045230768620967865 | 0.0 | 0.0 | +— / -04520fe5-4449-4632-b275-e5e28d642007 |
| Jogador 7 | 5-1 | 540 | BUY | FAST8 | 79.0 | 7 | 39 | 3 | 40.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2781813442707062 | 0.0 | 0.0 | +1388df2e-8cb4-4e29-8b30-776c29406917 / -— |
| Jogador 7 | 5-1 | 541 | PASS | FAST8 | 79.0 | 7 | 37 | 3 | 40.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 549 | SELL | FAST8 | 79.0 | 7 | 49 | 4 | 40.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13199999928474426 | 0.0 | 0.0 | +— / -1388df2e-8cb4-4e29-8b30-776c29406917 |
| Jogador 7 | 5-2 | 550 | BUY | FAST8 | 79.0 | 7 | 51 | 5 | 40.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8542316555976868 | 0.0 | 0.0 | +d6a929d8-6d7c-4bcd-880d-d819daca2ae0 / -15c93ffb-d63e-43e6-aa46-ba2beed9cb53,c7841e00-91da-410b-b00f-62f4bf32f666 |
| Jogador 7 | 5-2 | 551 | BUY | FAST8 | 79.0 | 7 | 48 | 4 | 40.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29400932788848877 | 0.0 | 0.0 | +02d3d068-e592-4f9c-a574-914955401575 / -— |
| Jogador 7 | 5-2 | 552 | BUY | FAST8 | 79.0 | 7 | 46 | 4 | 40.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24602913856506348 | 0.0 | 0.0 | +ee67f5c6-559f-492e-9cc0-6bc19a203d6a / -— |
| Jogador 7 | 5-2 | 553 | SELL | FAST8 | 79.0 | 7 | 43 | 4 | 40.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2683076858520508 | 0.0 | 0.0 | +— / -ee67f5c6-559f-492e-9cc0-6bc19a203d6a |
| Jogador 7 | 5-2 | 554 | BUY | FAST8 | 79.0 | 7 | 46 | 4 | 40.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23201562464237213 | 0.0 | 0.0 | +2f5d8cb8-8ba3-45e9-a345-00e931d34490 / -— |
| Jogador 7 | 5-2 | 555 | SELL | FAST8 | 79.0 | 7 | 43 | 4 | 40.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.045230768620967865 | 0.0 | 0.0 | +— / -2f5d8cb8-8ba3-45e9-a345-00e931d34490 |
| Jogador 7 | 5-2 | 556 | BUY | FAST8 | 79.0 | 7 | 46 | 4 | 40.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07758825272321701 | 0.0 | 0.0 | +2f2ff445-f60a-4a05-b37a-41b8a6d6c7f9 / -— |
| Jogador 7 | 5-2 | 557 | PASS | FAST8 | 79.0 | 7 | 44 | 4 | 40.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 562 | BUY | FAST8 | 79.0 | 7 | 57 | 5 | 50.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0910140872001648 | 0.0 | 0.0 | +18d25cfb-d559-4efa-b708-c9987987590b / -— |
| Jogador 7 | 5-3 | 563 | SELL | FAST8 | 79.0 | 7 | 54 | 5 | 50.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029811618849635124 | 0.0 | 0.0 | +— / -2f2ff445-f60a-4a05-b37a-41b8a6d6c7f9 |
| Jogador 7 | 5-3 | 564 | BUY | FAST8 | 79.0 | 7 | 56 | 5 | 50.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2197132557630539 | 0.0 | 0.0 | +ecc1f543-ff40-40a9-b8a3-5c1af2a54dc3 / -— |
| Jogador 7 | 5-3 | 565 | SELL | FAST8 | 79.0 | 7 | 54 | 5 | 50.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04323076829314232 | 0.0 | 0.0 | +— / -ecc1f543-ff40-40a9-b8a3-5c1af2a54dc3 |
| Jogador 7 | 5-3 | 566 | BUY | FAST8 | 79.0 | 7 | 56 | 5 | 50.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21970216929912567 | 0.0 | 0.0 | +b0c8ce74-5ce1-4ed0-82ac-f95013475f3c / -— |
| Jogador 7 | 5-3 | 567 | PASS | FAST8 | 79.0 | 7 | 54 | 5 | 50.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0013562875101342797 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 579 | SELL | FAST8 | 79.0 | 7 | 68 | 5 | 50.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04323076829314232 | 0.0 | 0.0 | +— / -b0c8ce74-5ce1-4ed0-82ac-f95013475f3c |
| Jogador 7 | 5-4 | 580 | BUY | FAST8 | 79.0 | 7 | 70 | 5 | 50.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9499316811561584 | 0.0 | 0.0 | +2949d735-3c16-4a45-835b-e11a9c12b16a / -6c691ca5-c042-46de-8d64-493514f2d793,cfe17b3a-c9b6-4e09-9ba1-23e762a72569 |
| Jogador 7 | 5-4 | 581 | BUY | FAST8 | 79.0 | 7 | 67 | 5 | 44.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7695422768592834 | 0.0 | 0.0 | +d78561b4-3dcc-42fb-9983-2ed5d62f8606 / -— |
| Jogador 7 | 5-4 | 582 | SELL | FAST8 | 79.0 | 7 | 65 | 5 | 44.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.036813974380493164 | 0.0 | 0.0 | +— / -18d25cfb-d559-4efa-b708-c9987987590b |
| Jogador 7 | 5-4 | 583 | BUY | FAST8 | 79.0 | 7 | 68 | 5 | 44.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008665747940540314 | 0.0 | 0.0 | +c69a2be1-356a-4576-9887-6d1790221a5e / -— |
| Jogador 7 | 5-4 | 584 | SELL | FAST8 | 79.0 | 7 | 64 | 5 | 44.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3273060917854309 | 0.0 | 0.0 | +— / -677ea844-e1bf-4c68-a0b0-136abb86ba7b |
| Jogador 7 | 5-4 | 585 | BUY | FAST8 | 79.0 | 7 | 67 | 5 | 44.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02641633152961731 | 0.0 | 0.0 | +ff181737-4995-4a67-add2-4f55cebabbee / -— |
| Jogador 7 | 5-4 | 586 | SELL | FAST8 | 79.0 | 7 | 65 | 5 | 44.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.028978146612644196 | 0.0 | 0.0 | +— / -ff181737-4995-4a67-add2-4f55cebabbee |
| Jogador 7 | 5-4 | 587 | BUY | FAST8 | 79.0 | 7 | 67 | 5 | 44.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10800155252218246 | 0.0 | 0.0 | +0d120db3-34e2-47e3-a57c-0d65dcc56342 / -— |
| Jogador 7 | 5-4 | 588 | SELL | FAST8 | 79.0 | 7 | 65 | 5 | 44.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04323076829314232 | 0.0 | 0.0 | +— / -0d120db3-34e2-47e3-a57c-0d65dcc56342 |
| Jogador 7 | 5-4 | 589 | PASS | FAST8 | 79.0 | 7 | 67 | 5 | 44.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007698719389736652 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 592 | BUY | WINSTREAK | 79.0 | 8 | 80 | 5 | 44.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08618949353694916 | 0.0 | 0.0 | +986fbe1e-1826-4be7-a5d6-410a4c0a3f2f / -— |
| Jogador 7 | 5-5 | 593 | SELL | WINSTREAK | 79.0 | 8 | 76 | 5 | 44.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02476923167705536 | 0.0 | 0.0 | +— / -5c931416-3aeb-40d4-9e6f-612b0d387226 |
| Jogador 7 | 5-5 | 594 | BUY | WINSTREAK | 79.0 | 8 | 80 | 5 | 44.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24449311196804047 | 0.0 | 0.0 | +45ae38c5-7e69-41bb-9a93-f14db3af3587 / -— |
| Jogador 7 | 5-5 | 595 | SELL | WINSTREAK | 79.0 | 8 | 77 | 5 | 44.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -45ae38c5-7e69-41bb-9a93-f14db3af3587 |
| Jogador 7 | 5-5 | 596 | BUY | WINSTREAK | 79.0 | 8 | 80 | 5 | 44.0 | Emanador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.034341733902692795 | 0.0 | 0.0 | +9414ca8e-930e-4a0e-8cbd-42d8997d8705 / -— |
| Jogador 7 | 5-5 | 597 | MOVE_BENCH | WINSTREAK | 79.0 | 8 | 77 | 5 | 44.0 | Emanador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6260263919830322 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 598 | BUY | WINSTREAK | 79.0 | 8 | 77 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22291968762874603 | 0.0 | 0.0 | +da6c9f59-1fc3-467d-8845-bf7b38b4232c / -— |
| Jogador 7 | 5-5 | 599 | SELL | WINSTREAK | 79.0 | 8 | 74 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04169230908155441 | 0.0 | 0.0 | +— / -da6c9f59-1fc3-467d-8845-bf7b38b4232c |
| Jogador 7 | 5-5 | 600 | BUY | WINSTREAK | 79.0 | 8 | 77 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08014501631259918 | 0.0 | 0.0 | +79b461e3-2c4f-40a2-b967-e0b6d5248bf6 / -— |
| Jogador 7 | 5-5 | 601 | PASS | WINSTREAK | 79.0 | 8 | 75 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012229474261403084 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 609 | SELL | WINSTREAK | 79.0 | 8 | 89 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04323076829314232 | 0.0 | 0.0 | +— / -79b461e3-2c4f-40a2-b967-e0b6d5248bf6 |
| Jogador 7 | 5-6 | 610 | BUY | WINSTREAK | 79.0 | 8 | 91 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4291365146636963 | 0.0 | 0.0 | +b3905667-bcb5-4e23-94fa-25160b14a95e / -— |
| Jogador 7 | 5-6 | 611 | SELL | WINSTREAK | 79.0 | 8 | 87 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029288049787282944 | 0.0 | 0.0 | +— / -9414ca8e-930e-4a0e-8cbd-42d8997d8705 |
| Jogador 7 | 5-6 | 612 | BUY | WINSTREAK | 79.0 | 8 | 90 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37020343542099 | 0.0 | 0.0 | +7313188a-ce84-4a52-b2d0-a94b2c420cdb / -— |
| Jogador 7 | 5-6 | 613 | SELL | WINSTREAK | 79.0 | 8 | 86 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02476923167705536 | 0.0 | 0.0 | +— / -986fbe1e-1826-4be7-a5d6-410a4c0a3f2f |
| Jogador 7 | 5-6 | 614 | BUY | WINSTREAK | 79.0 | 8 | 90 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04509628191590309 | 0.0 | 0.0 | +6c338d19-b3d3-49a7-b61e-4732249ee457 / -— |
| Jogador 7 | 5-6 | 615 | SELL | WINSTREAK | 79.0 | 8 | 87 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.023846153169870377 | 0.0 | 0.0 | +— / -6c338d19-b3d3-49a7-b61e-4732249ee457 |
| Jogador 7 | 5-6 | 616 | BUY | WINSTREAK | 79.0 | 8 | 90 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07609614729881287 | 0.0 | 0.0 | +c7762d7d-bcfa-4694-a3fc-038d7242207f / -— |
| Jogador 7 | 5-6 | 617 | SELL | WINSTREAK | 79.0 | 8 | 88 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04323076829314232 | 0.0 | 0.0 | +— / -c7762d7d-bcfa-4694-a3fc-038d7242207f |
| Jogador 7 | 5-6 | 618 | BUY | WINSTREAK | 79.0 | 8 | 90 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.043218016624450684 | 0.0 | 0.0 | +4688e6f1-26c5-402d-8d27-0f9bce3a9681 / -— |
| Jogador 7 | 5-6 | 619 | PASS | WINSTREAK | 79.0 | 8 | 88 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020212503150105476 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 622 | SELL | WINSTREAK | 79.0 | 8 | 102 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0370769239962101 | 0.0 | 0.0 | +— / -4688e6f1-26c5-402d-8d27-0f9bce3a9681 |
| Jogador 7 | 5-7 | 623 | BUY | WINSTREAK | 79.0 | 8 | 104 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39426636695861816 | 0.0 | 0.0 | +e1055913-2340-4af0-8527-e175c8bc1ccb / -— |
| Jogador 7 | 5-7 | 624 | SELL | WINSTREAK | 79.0 | 8 | 101 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28444182872772217 | 0.0 | 0.0 | +— / -c69a2be1-356a-4576-9887-6d1790221a5e |
| Jogador 7 | 5-7 | 625 | BUY | WINSTREAK | 79.0 | 8 | 105 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.060453955084085464 | 0.0 | 0.0 | +8b8aaa92-8fe0-46ad-857e-af3bae9b26a4 / -— |
| Jogador 7 | 5-7 | 626 | SELL | WINSTREAK | 79.0 | 8 | 101 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04015384614467621 | 0.0 | 0.0 | +— / -8b8aaa92-8fe0-46ad-857e-af3bae9b26a4 |
| Jogador 7 | 5-7 | 627 | BUY | WINSTREAK | 79.0 | 8 | 105 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12188360095024109 | 0.0 | 0.0 | +f84cc827-410f-47eb-bd95-bd650acfdd4b / -— |
| Jogador 7 | 5-7 | 628 | SELL | WINSTREAK | 79.0 | 8 | 101 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013228623196482658 | 0.0 | 0.0 | +— / -f84cc827-410f-47eb-bd95-bd650acfdd4b |
| Jogador 7 | 5-7 | 629 | BUY | WINSTREAK | 79.0 | 8 | 105 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2578027844429016 | 0.0 | 0.0 | +973ba75e-ffa8-41f5-a3fb-e238e34d0216 / -— |
| Jogador 7 | 5-7 | 630 | SELL | WINSTREAK | 79.0 | 8 | 102 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -973ba75e-ffa8-41f5-a3fb-e238e34d0216 |
| Jogador 7 | 5-7 | 631 | BUY | WINSTREAK | 79.0 | 8 | 105 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0032318958546966314 | 0.0 | 0.0 | +4b1f1146-d580-41e9-987f-c32b1eb98b75 / -— |
| Jogador 7 | 5-7 | 632 | PASS | WINSTREAK | 79.0 | 8 | 103 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030130811035633087 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 638 | EQUIP_FROM_INVENTORY | WINSTREAK | 79.0 | 8 | 116 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 639 | EQUIP_FROM_INVENTORY | WINSTREAK | 79.0 | 8 | 116 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | -0.02490120567381382 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 640 | SELL | WINSTREAK | 79.0 | 8 | 116 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029741279780864716 | 0.0 | 0.0 | +— / -4b1f1146-d580-41e9-987f-c32b1eb98b75 |
| Jogador 7 | 6-1 | 641 | BUY | WINSTREAK | 79.0 | 8 | 118 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0588366985321045 | 0.0 | 0.0 | +d8392323-28e4-4e98-a466-5958bf400729 / -02d3d068-e592-4f9c-a574-914955401575,d78561b4-3dcc-42fb-9983-2ed5d62f8606 |
| Jogador 7 | 6-1 | 642 | BUY | WINSTREAK | 79.0 | 8 | 116 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11138981580734253 | 0.0 | 0.0 | +d5c73756-6784-44e9-b521-5c61db813319 / -— |
| Jogador 7 | 6-1 | 643 | BUY | WINSTREAK | 79.0 | 8 | 112 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05962742492556572 | 0.0 | 0.0 | +438ec27b-d901-437b-82b5-64e6d46fccb1 / -— |
| Jogador 7 | 6-1 | 644 | SELL | WINSTREAK | 79.0 | 8 | 108 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04015384614467621 | 0.0 | 0.0 | +— / -438ec27b-d901-437b-82b5-64e6d46fccb1 |
| Jogador 7 | 6-1 | 645 | BUY | WINSTREAK | 79.0 | 8 | 112 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04190251976251602 | 0.0 | 0.0 | +a5e92183-8d5d-434c-9294-47c6b7bfb91b / -— |
| Jogador 7 | 6-1 | 646 | PASS | WINSTREAK | 79.0 | 8 | 109 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0342690609395504 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 647 | MOVE_BENCH | WINSTREAK | 79.0 | 8 | 109 | 5 | 56.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5820180773735046 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 652 | BUY | WINSTREAK | 79.0 | 8 | 123 | 5 | 64.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11454815417528152 | 0.0 | 0.0 | +a267d973-f857-4dda-89e1-209bff42ab6f / -— |
| Jogador 7 | 6-2 | 653 | SELL | WINSTREAK | 79.0 | 8 | 119 | 5 | 64.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.036912404000759125 | 0.0 | 0.0 | +— / -a5e92183-8d5d-434c-9294-47c6b7bfb91b |
| Jogador 7 | 6-2 | 654 | BUY | WINSTREAK | 79.0 | 8 | 122 | 5 | 64.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3593205511569977 | 0.0 | 0.0 | +76fcc4d0-4988-4e99-8ac0-c251f0b99dcd / -— |
| Jogador 7 | 6-2 | 655 | SELL | WINSTREAK | 79.0 | 8 | 119 | 5 | 64.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01168807689100504 | 0.0 | 0.0 | +— / -a267d973-f857-4dda-89e1-209bff42ab6f |
| Jogador 7 | 6-2 | 656 | BUY | WINSTREAK | 79.0 | 8 | 123 | 5 | 64.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08922848850488663 | 0.0 | 0.0 | +d2afd490-f89f-47c9-8279-a88acde5b1b6 / -— |
| Jogador 7 | 6-2 | 657 | SELL | WINSTREAK | 79.0 | 8 | 121 | 5 | 64.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.014419825747609138 | 0.0 | 0.0 | +— / -d2afd490-f89f-47c9-8279-a88acde5b1b6 |
| Jogador 7 | 6-2 | 658 | BUY | WINSTREAK | 79.0 | 8 | 123 | 5 | 64.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23545433580875397 | 0.0 | 0.0 | +f00a538c-0607-4d8b-babe-7c13daf80c42 / -— |
| Jogador 7 | 6-2 | 659 | PASS | WINSTREAK | 79.0 | 8 | 121 | 5 | 64.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04279468208551407 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 667 | SELL | WINSTREAK | 79.0 | 8 | 134 | 5 | 64.0 | Emanador/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04323076829314232 | 0.0 | 0.0 | +— / -f00a538c-0607-4d8b-babe-7c13daf80c42 |
| Jogador 7 | 6-3 | 668 | BUY | WINSTREAK | 79.0 | 8 | 136 | 5 | 64.0 | Emanador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0599943399429321 | 0.0 | 0.0 | +8da82a9e-0746-43e1-81c3-fa22ec3bb863 / -8a52858d-da47-4de9-8e91-8612788cb8fd,fb7c0635-9f86-4c1e-b354-37372f84d656 |
| Jogador 7 | 6-3 | 669 | SELL | WINSTREAK | 79.0 | 8 | 132 | 5 | 48.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02476923167705536 | 0.0 | 0.0 | +— / -d5c73756-6784-44e9-b521-5c61db813319 |
| Jogador 7 | 6-3 | 670 | BUY | WINSTREAK | 79.0 | 8 | 136 | 5 | 48.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8132719397544861 | 0.0 | 0.0 | +ceaf1f61-1aa5-404e-ae3f-17db9137ceb7 / -— |
| Jogador 7 | 6-3 | 671 | SELL | WINSTREAK | 79.0 | 8 | 133 | 5 | 48.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3408564627170563 | 0.0 | 0.0 | +— / -ceaf1f61-1aa5-404e-ae3f-17db9137ceb7 |
| Jogador 7 | 6-3 | 672 | BUY | WINSTREAK | 79.0 | 8 | 136 | 5 | 48.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23924241960048676 | 0.0 | 0.0 | +6fb5e8f1-2656-486b-9478-161c1b430d5f / -— |
| Jogador 7 | 6-3 | 673 | SELL | WINSTREAK | 79.0 | 8 | 133 | 5 | 48.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -6fb5e8f1-2656-486b-9478-161c1b430d5f |
| Jogador 7 | 6-3 | 674 | BUY | WINSTREAK | 79.0 | 8 | 136 | 5 | 48.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23928524553775787 | 0.0 | 0.0 | +91eb044c-6989-4b6a-a9fa-a59f75b56743 / -— |
| Jogador 7 | 6-3 | 675 | MOVE_BENCH | WINSTREAK | 79.0 | 8 | 133 | 5 | 48.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5481072664260864 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 676 | BUY | WINSTREAK | 79.0 | 8 | 133 | 5 | 64.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2631497383117676 | 0.0 | 0.0 | +d30c92eb-1279-4532-b763-7c30826c8430 / -— |
| Jogador 7 | 6-3 | 677 | PASS | WINSTREAK | 79.0 | 8 | 132 | 5 | 64.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.050869375467300415 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 681 | SELL | WINSTREAK | 79.0 | 8 | 146 | 5 | 64.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -d30c92eb-1279-4532-b763-7c30826c8430 |
| Jogador 7 | 6-4 | 682 | BUY | WINSTREAK | 79.0 | 8 | 147 | 5 | 64.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43803104758262634 | 0.0 | 0.0 | +efa7f2f8-94f3-4bcc-9a4e-b5b9e72cc978 / -— |
| Jogador 7 | 6-4 | 683 | SELL | WINSTREAK | 79.0 | 8 | 143 | 5 | 64.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019538462162017822 | 0.0 | 0.0 | +— / -76fcc4d0-4988-4e99-8ac0-c251f0b99dcd |
| Jogador 7 | 6-4 | 684 | BUY | WINSTREAK | 79.0 | 8 | 146 | 5 | 64.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09694188088178635 | 0.0 | 0.0 | +8486b8a9-20fe-4234-bbba-0efa031c3b76 / -— |
| Jogador 7 | 6-4 | 685 | SELL | WINSTREAK | 79.0 | 8 | 142 | 5 | 64.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -91eb044c-6989-4b6a-a9fa-a59f75b56743 |
| Jogador 7 | 6-4 | 686 | BUY | WINSTREAK | 79.0 | 8 | 145 | 5 | 64.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.40047696232795715 | 0.0 | 0.0 | +c07a17cf-e9e7-42be-b925-cb4f699593de / -— |
| Jogador 7 | 6-4 | 687 | SELL | WINSTREAK | 79.0 | 8 | 143 | 5 | 64.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02476923167705536 | 0.0 | 0.0 | +— / -8486b8a9-20fe-4234-bbba-0efa031c3b76 |
| Jogador 7 | 6-4 | 688 | BUY | WINSTREAK | 79.0 | 8 | 147 | 5 | 64.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06445321440696716 | 0.0 | 0.0 | +f087511a-d834-4f41-9b99-00bf0f6dc061 / -— |
| Jogador 7 | 6-4 | 689 | SELL | WINSTREAK | 79.0 | 8 | 145 | 5 | 64.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04323076829314232 | 0.0 | 0.0 | +— / -f087511a-d834-4f41-9b99-00bf0f6dc061 |
| Jogador 7 | 6-4 | 690 | BUY | WINSTREAK | 79.0 | 8 | 147 | 5 | 64.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06444985419511795 | 0.0 | 0.0 | +150a2da3-f559-4a40-a058-005e9c74e11f / -— |
| Jogador 7 | 6-4 | 691 | PASS | WINSTREAK | 79.0 | 8 | 145 | 5 | 64.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06069432944059372 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 695 | SELL | WINSTREAK | 79.0 | 8 | 158 | 5 | 64.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.032769229263067245 | 0.0 | 0.0 | +— / -150a2da3-f559-4a40-a058-005e9c74e11f |
| Jogador 7 | 6-5 | 696 | BUY | WINSTREAK | 79.0 | 8 | 160 | 5 | 64.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8590918183326721 | 0.0 | 0.0 | +0c5adb43-b194-486e-b59c-c0f3b5479d40 / -— |
| Jogador 7 | 6-5 | 697 | SELL | WINSTREAK | 79.0 | 8 | 157 | 5 | 64.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28479960560798645 | 0.0 | 0.0 | +— / -efa7f2f8-94f3-4bcc-9a4e-b5b9e72cc978 |
| Jogador 7 | 6-5 | 698 | BUY | WINSTREAK | 79.0 | 8 | 161 | 5 | 64.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6945962905883789 | 0.0 | 0.0 | +9c07608c-00e1-40f1-9671-6d8bc584a6c9 / -— |
| Jogador 7 | 6-5 | 699 | SELL | WINSTREAK | 79.0 | 8 | 158 | 5 | 64.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3256925344467163 | 0.0 | 0.0 | +— / -9c07608c-00e1-40f1-9671-6d8bc584a6c9 |
| Jogador 7 | 6-5 | 700 | BUY | WINSTREAK | 79.0 | 8 | 161 | 5 | 64.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2003277689218521 | 0.0 | 0.0 | +e5f61076-ec13-419b-a4e8-d91b9975cfd6 / -— |
| Jogador 7 | 6-5 | 701 | SELL | WINSTREAK | 79.0 | 8 | 157 | 5 | 64.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04015384614467621 | 0.0 | 0.0 | +— / -e5f61076-ec13-419b-a4e8-d91b9975cfd6 |
| Jogador 7 | 6-5 | 702 | BUY | WINSTREAK | 79.0 | 8 | 161 | 5 | 64.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42731958627700806 | 0.0 | 0.0 | +83a3ef65-b342-4ec8-b2d1-be99c3602f81 / -— |
| Jogador 7 | 6-5 | 703 | MOVE_BENCH | WINSTREAK | 79.0 | 8 | 160 | 5 | 64.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6921159029006958 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 704 | BUY | WINSTREAK | 79.0 | 8 | 160 | 5 | 66.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2654777765274048 | 0.0 | 0.0 | +e978e901-0a52-4f01-ba52-a83fbcc3b439 / -— |
| Jogador 7 | 6-5 | 705 | PASS | WINSTREAK | 79.0 | 8 | 158 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07079266756772995 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-6 | 709 | SELL | WINSTREAK | 79.0 | 8 | 172 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -e978e901-0a52-4f01-ba52-a83fbcc3b439 |
| Jogador 7 | 6-6 | 710 | BUY | WINSTREAK | 79.0 | 8 | 174 | 5 | 66.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8069531321525574 | 0.0 | 0.0 | +0a29573e-2a7b-4719-9b6e-49c2f476bc04 / -— |
| Jogador 7 | 6-6 | 711 | SELL | WINSTREAK | 79.0 | 8 | 171 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34189096093177795 | 0.0 | 0.0 | +— / -0a29573e-2a7b-4719-9b6e-49c2f476bc04 |
| Jogador 7 | 6-6 | 712 | BUY | WINSTREAK | 79.0 | 8 | 174 | 5 | 66.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21350149810314178 | 0.0 | 0.0 | +54574f38-262f-44ac-83da-03088b8bdea3 / -— |
| Jogador 7 | 6-6 | 713 | SELL | WINSTREAK | 79.0 | 8 | 170 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029692307114601135 | 0.0 | 0.0 | +— / -54574f38-262f-44ac-83da-03088b8bdea3 |
| Jogador 7 | 6-6 | 714 | BUY | WINSTREAK | 79.0 | 8 | 174 | 5 | 66.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21349027752876282 | 0.0 | 0.0 | +f078e755-d142-4dad-99d0-7e7599e3016d / -— |
| Jogador 7 | 6-6 | 715 | SELL | WINSTREAK | 79.0 | 8 | 170 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029692307114601135 | 0.0 | 0.0 | +— / -f078e755-d142-4dad-99d0-7e7599e3016d |
| Jogador 7 | 6-6 | 716 | BUY | WINSTREAK | 79.0 | 8 | 174 | 5 | 66.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23581291735172272 | 0.0 | 0.0 | +2d5214b0-3e0c-4e71-8664-2459bf616650 / -— |
| Jogador 7 | 6-6 | 717 | SELL | WINSTREAK | 79.0 | 8 | 173 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03430769219994545 | 0.0 | 0.0 | +— / -2d5214b0-3e0c-4e71-8664-2459bf616650 |
| Jogador 7 | 6-7 | 719 | BUY | WINSTREAK | 79.0 | 8 | 188 | 5 | 66.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21348902583122253 | 0.0 | 0.0 | +9f1c634e-13c7-4b59-838c-4b676fa059be / -— |
| Jogador 7 | 6-7 | 720 | SELL | WINSTREAK | 79.0 | 8 | 184 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04015384614467621 | 0.0 | 0.0 | +— / -9f1c634e-13c7-4b59-838c-4b676fa059be |
| Jogador 7 | 6-7 | 721 | BUY | WINSTREAK | 79.0 | 8 | 188 | 5 | 66.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03447602689266205 | 0.0 | 0.0 | +85fb6db6-e1b0-4fa1-b99a-2f205305ef0b / -— |
| Jogador 7 | 6-7 | 722 | SELL | WINSTREAK | 79.0 | 8 | 184 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02476923167705536 | 0.0 | 0.0 | +— / -85fb6db6-e1b0-4fa1-b99a-2f205305ef0b |
| Jogador 7 | 6-7 | 723 | BUY | WINSTREAK | 79.0 | 8 | 188 | 5 | 66.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.32955533266067505 | 0.0 | 0.0 | +be1e11e4-dc58-4e75-a402-3a2d831ac7b3 / -— |
| Jogador 7 | 6-7 | 724 | SELL | WINSTREAK | 79.0 | 8 | 185 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27536532282829285 | 0.0 | 0.0 | +— / -be1e11e4-dc58-4e75-a402-3a2d831ac7b3 |
| Jogador 7 | 6-7 | 725 | BUY | WINSTREAK | 79.0 | 8 | 188 | 5 | 66.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22135426104068756 | 0.0 | 0.0 | +864f332a-0446-4995-b7fb-76d48d293501 / -— |
| Jogador 7 | 6-7 | 726 | SELL | WINSTREAK | 79.0 | 8 | 185 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04169230908155441 | 0.0 | 0.0 | +— / -864f332a-0446-4995-b7fb-76d48d293501 |
| Jogador 7 | 6-7 | 727 | BUY | WINSTREAK | 79.0 | 8 | 188 | 5 | 66.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.002223145915195346 | 0.0 | 0.0 | +1bf15a91-4832-4245-9b48-382a27410263 / -— |
| Jogador 7 | 7-1 | 729 | EQUIP_FROM_INVENTORY | WINSTREAK | 79.0 | 8 | 200 | 5 | 66.0 | Emanador/DA_Sentinel18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 7-1 | 730 | EQUIP_FROM_INVENTORY | WINSTREAK | 79.0 | 8 | 200 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07321228086948395 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 7-1 | 731 | SELL | WINSTREAK | 79.0 | 8 | 200 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029384614899754524 | 0.0 | 0.0 | +— / -1bf15a91-4832-4245-9b48-382a27410263 |
| Jogador 7 | 7-1 | 732 | BUY | WINSTREAK | 79.0 | 8 | 201 | 5 | 66.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21348902583122253 | 0.0 | 0.0 | +c2bf43be-e6e1-47ed-bcb4-606e37f26671 / -— |
| Jogador 7 | 7-1 | 733 | SELL | WINSTREAK | 79.0 | 8 | 197 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04015384614467621 | 0.0 | 0.0 | +— / -c2bf43be-e6e1-47ed-bcb4-606e37f26671 |
| Jogador 7 | 7-1 | 734 | BUY | WINSTREAK | 79.0 | 8 | 201 | 5 | 66.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21348902583122253 | 0.0 | 0.0 | +7f7fc4fe-472b-4ddf-9454-b4a669cbcc14 / -— |
| Jogador 7 | 7-1 | 735 | SELL | WINSTREAK | 79.0 | 8 | 197 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04015384614467621 | 0.0 | 0.0 | +— / -7f7fc4fe-472b-4ddf-9454-b4a669cbcc14 |
| Jogador 7 | 7-1 | 736 | BUY | WINSTREAK | 79.0 | 8 | 201 | 5 | 66.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2597682774066925 | 0.0 | 0.0 | +40f48f33-4e11-4a13-a9e8-f6b1e7d97b0b / -— |
| Jogador 7 | 7-1 | 737 | SELL | WINSTREAK | 79.0 | 8 | 198 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -40f48f33-4e11-4a13-a9e8-f6b1e7d97b0b |
| Jogador 7 | 7-1 | 738 | BUY | WINSTREAK | 79.0 | 8 | 201 | 5 | 66.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09919151663780212 | 0.0 | 0.0 | +d58ebcea-d18b-42f8-a6ca-984d15656662 / -— |
| Jogador 7 | 7-1 | 739 | PASS | WINSTREAK | 79.0 | 8 | 199 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10416056215763092 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 7-2 | 741 | SELL | WINSTREAK | 79.0 | 8 | 213 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015564528293907642 | 0.0 | 0.0 | +— / -d58ebcea-d18b-42f8-a6ca-984d15656662 |
| Jogador 7 | 7-2 | 742 | BUY | WINSTREAK | 79.0 | 8 | 215 | 5 | 66.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8656401038169861 | 0.0 | 0.0 | +c5520bc4-3123-40f3-b275-83fa8cb06309 / -— |
| Jogador 7 | 7-2 | 743 | SELL | WINSTREAK | 79.0 | 8 | 211 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012524783611297607 | 0.0 | 0.0 | +— / -b3905667-bcb5-4e23-94fa-25160b14a95e |
| Jogador 7 | 7-2 | 744 | BUY | WINSTREAK | 79.0 | 8 | 215 | 5 | 66.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0593029260635376 | 0.0 | 0.0 | +0a0e7d41-96bf-404f-a3bf-98df0a182b63 / -7313188a-ce84-4a52-b2d0-a94b2c420cdb,c5520bc4-3123-40f3-b275-83fa8cb06309 |
| Jogador 7 | 7-2 | 745 | BUY | WINSTREAK | 79.0 | 8 | 211 | 5 | 66.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21346363425254822 | 0.0 | 0.0 | +5de51369-647a-45bd-95b7-c8efe44c5484 / -— |
| Jogador 7 | 7-2 | 746 | BUY | WINSTREAK | 79.0 | 8 | 207 | 5 | 66.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03158757835626602 | 0.0 | 0.0 | +1f349179-be2a-4738-bda1-072f7fae2147 / -— |
| Jogador 7 | 7-2 | 747 | SELL | WINSTREAK | 79.0 | 8 | 203 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02476923167705536 | 0.0 | 0.0 | +— / -1f349179-be2a-4738-bda1-072f7fae2147 |
| Jogador 7 | 7-2 | 748 | BUY | WINSTREAK | 79.0 | 8 | 207 | 5 | 66.0 | Emanador/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15468710660934448 | 0.0 | 0.0 | +bdee5671-864a-47c9-9576-9e0d8d2a7c6a / -— |
| Jogador 7 | 7-2 | 749 | SELL | WINSTREAK | 79.0 | 8 | 204 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029999999329447746 | 0.0 | 0.0 | +— / -bdee5671-864a-47c9-9576-9e0d8d2a7c6a |
| Jogador 7 | 7-2 | 750 | SELL | WINSTREAK | 79.0 | 8 | 207 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18530769646167755 | 0.0 | 0.0 | +— / -5de51369-647a-45bd-95b7-c8efe44c5484 |
| Jogador 7 | 7-2 | 751 | PASS | WINSTREAK | 79.0 | 8 | 211 | 5 | 66.0 | Emanador/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10499999672174454 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 1 | PASS | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 26 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.28737619519233704 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 33 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.014635218307375908 | 0.0 | 0.0 | +64afe66e-d5a9-466c-a4ff-9d32c9f153ce / -— |
| Jogador 8 | 1-2 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05311587452888489 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 35 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Veigar | BUY, MOVE_BOARD, PASS | True | True | 0.2280149906873703 | 0.0 | 0.0 | +47feb452-27a0-43f6-983f-ea1674f17ab8 / -— |
| Jogador 8 | 1-2 | 36 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.506436288356781 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 37 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | -0.24581173062324524 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 38 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.17907975614070892 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 39 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | -0.29448118805885315 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 40 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.06377681344747543 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 41 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 57 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9528620839118958 | 0.0 | 0.0 | +dfc76a7d-9a2b-4b35-b341-60eefe095b71 / -— |
| Jogador 8 | 1-3 | 58 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6317018866539001 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 59 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.303520143032074 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 60 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Veigar | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 83 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3413054049015045 | 0.0 | 0.0 | +4ea4d9af-5729-414b-a102-b7fc80667118 / -— |
| Jogador 8 | 1-4 | 84 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3559182286262512 | 0.0 | 0.0 | +— / -47feb452-27a0-43f6-983f-ea1674f17ab8 |
| Jogador 8 | 1-4 | 85 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9639362692832947 | 0.0 | 0.0 | +322e9047-623a-4fec-a0f9-d21d2fbcd88a / -— |
| Jogador 8 | 1-4 | 86 | SELL | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Xayah | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0139362812042236 | 0.0 | 0.0 | +— / -322e9047-623a-4fec-a0f9-d21d2fbcd88a |
| Jogador 8 | 1-4 | 87 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5310174226760864 | 0.0 | 0.0 | +— / -4ea4d9af-5729-414b-a102-b7fc80667118 |
| Jogador 8 | 1-4 | 88 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3299667537212372 | 0.0 | 0.0 | +65a4f434-f421-47ab-ae23-86ad8971518d / -— |
| Jogador 8 | 1-4 | 89 | BUY_XP | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Veigar | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.047200001776218414 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 90 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Veigar | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.38113364577293396 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 91 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.1529165357351303 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 92 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Veigar | MOVE_BOARD, PASS | True | True | 0.1782630980014801 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 93 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 109 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0913812518119812 | 0.0 | 0.0 | +a524fad3-c7d3-4fa7-9c62-1803c8e7c865 / -— |
| Jogador 8 | 2-1 | 110 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1042855903506279 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 111 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0080962181091309 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 112 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14356674253940582 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 113 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 8.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1526690274477005 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 114 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2712615728378296 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 115 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 133 | BUY | STABILIZE | 94.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Teemo | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2980678677558899 | 0.0 | 0.0 | +4b4cc4ba-04a0-4e04-88f2-e6913a342285 / -— |
| Jogador 8 | 2-2 | 134 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 4 | 0 | 10.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2853265702724457 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 135 | SELL | STABILIZE | 94.0 | 4 | 4 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04238084331154823 | 0.0 | 0.0 | +— / -65a4f434-f421-47ab-ae23-86ad8971518d |
| Jogador 8 | 2-2 | 136 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 5 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1312565952539444 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 137 | SELL | STABILIZE | 94.0 | 4 | 5 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07473887503147125 | 0.0 | 0.0 | +— / -64afe66e-d5a9-466c-a4ff-9d32c9f153ce |
| Jogador 8 | 2-2 | 138 | BUY | STABILIZE | 94.0 | 4 | 6 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3127423822879791 | 0.0 | 0.0 | +a3df8a2b-03f3-406d-88a0-1df3c7efa789 / -— |
| Jogador 8 | 2-2 | 139 | BUY_XP | STABILIZE | 94.0 | 4 | 4 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03189999982714653 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 140 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 0 | 0 | 14.0 | —/DA_Krug18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5174942016601562 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 141 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 0 | 0 | 18.0 | —/DA_Krug18 | MOVE_BOARD, PASS | True | True | 0.08719376474618912 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 142 | MOVE_BOARD | STABILIZE | 94.0 | 5 | 0 | 0 | 18.0 | —/DA_Krug18 | MOVE_BOARD, PASS | True | True | 0.17799192667007446 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 143 | PASS | STABILIZE | 94.0 | 5 | 0 | 0 | 18.0 | —/DA_Krug18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 157 | BUY | STABILIZE | 94.0 | 5 | 6 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.36082923412323 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 158 | BUY | STABILIZE | 94.0 | 5 | 3 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48037198185920715 | 0.0 | 0.0 | +f16ba193-452a-4c02-bfc0-b9757661a178 / -— |
| Jogador 8 | 2-3 | 159 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 2 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01410010177642107 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 160 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.720193088054657 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 161 | PASS | STABILIZE | 94.0 | 5 | 2 | 0 | 16.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 182 | BUY | STABILIZE | 94.0 | 5 | 9 | 0 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10967991501092911 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 8 | 2-4 | 183 | BUY | STABILIZE | 94.0 | 5 | 6 | 0 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2892548739910126 | 0.0 | 0.0 | +7915a339-3bda-4275-80ae-9941370ea609 / -— |
| Jogador 8 | 2-4 | 184 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 3 | 0 | 16.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.035203494131565094 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 185 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 3 | 0 | 18.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.023598086088895798 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 186 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 3 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.282146155834198 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 187 | PASS | STABILIZE | 94.0 | 5 | 3 | 0 | 16.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 205 | BUY | STABILIZE | 94.0 | 5 | 9 | 0 | 16.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3623197078704834 | 0.0 | 0.0 | +2e656a3d-eed0-40bb-a831-443d972d6588 / -— |
| Jogador 8 | 2-5 | 206 | BUY | STABILIZE | 94.0 | 5 | 6 | 0 | 16.0 | Enfeitiçador/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9040236473083496 | 0.0 | 0.0 | +35e1a0f6-207d-4df2-b096-fc07962d094a / -— |
| Jogador 8 | 2-5 | 207 | BUY | STABILIZE | 94.0 | 5 | 4 | 0 | 16.0 | Enfeitiçador/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19379787147045135 | 0.0 | 0.0 | +c0d8da9e-5ede-4a26-8c5c-e2a908318bfd / -— |
| Jogador 8 | 2-5 | 208 | BUY | STABILIZE | 94.0 | 5 | 2 | 0 | 16.0 | Enfeitiçador/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.018609987571835518 | 0.0 | 0.0 | +cf4575c2-3622-4493-91f1-c5efbe1fbd8b / -— |
| Jogador 8 | 2-5 | 209 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 0 | 0 | 16.0 | Enfeitiçador/DA_Krug18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2832745313644409 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 210 | MOVE_BENCH | STABILIZE | 94.0 | 5 | 0 | 0 | 18.0 | Enfeitiçador/DA_Krug18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.037188395857810974 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 211 | PASS | STABILIZE | 94.0 | 5 | 0 | 0 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 227 | BUY | STABILIZE | 90.0 | 5 | 5 | 0 | 14.0 | Enfeitiçador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1710597425699234 | 0.0 | 0.0 | +87600495-fe90-4832-ab42-9a5cb0ebe3f4 / -— |
| Jogador 8 | 2-6 | 228 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 2 | 0 | 14.0 | Enfeitiçador/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13725456595420837 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 229 | SELL | STABILIZE | 90.0 | 5 | 2 | 0 | 16.0 | Enfeitiçador/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.022248266264796257 | 0.0 | 0.0 | +— / -cf4575c2-3622-4493-91f1-c5efbe1fbd8b |
| Jogador 8 | 2-6 | 230 | BUY | STABILIZE | 90.0 | 5 | 4 | 0 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17878751456737518 | 0.0 | 0.0 | +6a3fff4b-0ae4-4f8f-b64e-c55868db57b2 / -— |
| Jogador 8 | 2-6 | 231 | SELL | STABILIZE | 90.0 | 5 | 1 | 0 | 16.0 | Enfeitiçador/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01817137934267521 | 0.0 | 0.0 | +— / -c0d8da9e-5ede-4a26-8c5c-e2a908318bfd |
| Jogador 8 | 2-6 | 232 | BUY | STABILIZE | 90.0 | 5 | 3 | 0 | 16.0 | Enfeitiçador/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13135823607444763 | 0.0 | 0.0 | +c9a1ea77-662a-469a-ba7f-eac0713c0c52 / -— |
| Jogador 8 | 2-6 | 233 | SELL | STABILIZE | 90.0 | 5 | 1 | 0 | 16.0 | Enfeitiçador/DA_18_Diana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03387761861085892 | 0.0 | 0.0 | +— / -c9a1ea77-662a-469a-ba7f-eac0713c0c52 |
| Jogador 8 | 2-6 | 234 | BUY | STABILIZE | 90.0 | 5 | 3 | 0 | 16.0 | Enfeitiçador/DA_18_Diana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8204953074455261 | 0.0 | 0.0 | +c737e99a-613e-4f1a-a50e-7a865169f90c / -— |
| Jogador 8 | 2-6 | 235 | SELL | STABILIZE | 90.0 | 5 | 2 | 0 | 16.0 | Enfeitiçador/DA_18_Diana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03169230744242668 | 0.0 | 0.0 | +— / -7915a339-3bda-4275-80ae-9941370ea609 |
| Jogador 8 | 2-6 | 236 | SELL | STABILIZE | 90.0 | 5 | 5 | 0 | 16.0 | Enfeitiçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0003846153849735856 | 0.0 | 0.0 | +— / -5f2c89f5-15c2-4a77-943e-4ba5492d925b |
| Jogador 8 | 2-6 | 237 | PASS | STABILIZE | 90.0 | 5 | 8 | 0 | 16.0 | Enfeitiçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 250 | BUY | STABILIZE | 84.0 | 5 | 14 | 1 | 16.0 | Enfeitiçador/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8409801721572876 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 8 | 2-7 | 251 | BUY | STABILIZE | 84.0 | 5 | 11 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06530001014471054 | 0.0 | 0.0 | +57903c42-49ca-43e1-8f86-42429c189fb5 / -— |
| Jogador 8 | 2-7 | 252 | SELL | STABILIZE | 84.0 | 5 | 8 | 0 | 16.0 | Enfeitiçador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08953846246004105 | 0.0 | 0.0 | +— / -57903c42-49ca-43e1-8f86-42429c189fb5 |
| Jogador 8 | 2-7 | 253 | BUY | STABILIZE | 84.0 | 5 | 11 | 1 | 16.0 | Enfeitiçador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9498006105422974 | 0.0 | 0.0 | +60b0249f-e02f-4aca-b90d-75e9bcc822b8 / -0832c739-e0cc-4b9d-9f18-a4dbfa570a02,c737e99a-613e-4f1a-a50e-7a865169f90c |
| Jogador 8 | 2-7 | 254 | BUY | STABILIZE | 84.0 | 5 | 10 | 1 | 14.0 | Enfeitiçador/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06872950494289398 | 0.0 | 0.0 | +f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 / -— |
| Jogador 8 | 2-7 | 255 | SELL | STABILIZE | 84.0 | 5 | 9 | 0 | 14.0 | Enfeitiçador/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09079388529062271 | 0.0 | 0.0 | +— / -f7fd3af2-9c1e-48b5-b940-a5ccc55bb655 |
| Jogador 8 | 2-7 | 256 | BUY | STABILIZE | 84.0 | 5 | 10 | 1 | 14.0 | Enfeitiçador/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22314924001693726 | 0.0 | 0.0 | +d731d71e-fc91-41ae-ab3f-75966dd2c428 / -— |
| Jogador 8 | 2-7 | 257 | MOVE_BENCH | STABILIZE | 84.0 | 5 | 9 | 0 | 14.0 | Enfeitiçador/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6160615682601929 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 258 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 9 | 0 | 20.0 | Vivaz/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1585756540298462 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 259 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 9 | 0 | 20.0 | Vivaz/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09540175646543503 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 260 | PASS | STABILIZE | 84.0 | 5 | 9 | 0 | 20.0 | Vivaz/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 270 | BUY | STABILIZE | 84.0 | 5 | 15 | 1 | 20.0 | Vivaz/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2001141607761383 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 271 | SELL | STABILIZE | 84.0 | 5 | 11 | 1 | 20.0 | Vivaz/DA_18_Rakan | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04676923155784607 | 0.0 | 0.0 | +— / -d731d71e-fc91-41ae-ab3f-75966dd2c428 |
| Jogador 8 | 3-1 | 272 | SELL | STABILIZE | 84.0 | 5 | 12 | 1 | 20.0 | Vivaz/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.009954539127647877 | 0.0 | 0.0 | +— / -b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 8 | 3-1 | 273 | BUY | STABILIZE | 84.0 | 5 | 15 | 1 | 20.0 | Vivaz/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26368415355682373 | 0.0 | 0.0 | +88420167-3841-43dd-b1d0-3e5ab2294c78 / -— |
| Jogador 8 | 3-1 | 274 | SELL | STABILIZE | 84.0 | 5 | 13 | 1 | 20.0 | Vivaz/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16099999845027924 | 0.0 | 0.0 | +— / -88420167-3841-43dd-b1d0-3e5ab2294c78 |
| Jogador 8 | 3-1 | 275 | SELL | STABILIZE | 84.0 | 5 | 15 | 1 | 20.0 | Vivaz/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4208599030971527 | 0.0 | 0.0 | +— / -60b0249f-e02f-4aca-b90d-75e9bcc822b8 |
| Jogador 8 | 3-1 | 276 | SELL | STABILIZE | 84.0 | 5 | 18 | 1 | 20.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5749378204345703 | 0.0 | 0.0 | +— / -a3df8a2b-03f3-406d-88a0-1df3c7efa789 |
| Jogador 8 | 3-1 | 277 | SELL | STABILIZE | 84.0 | 5 | 20 | 2 | 20.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3322257697582245 | 0.0 | 0.0 | +— / -35e1a0f6-207d-4df2-b096-fc07962d094a |
| Jogador 8 | 3-1 | 278 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 22 | 2 | 20.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17477719485759735 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 279 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 22 | 2 | 20.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 280 | PASS | STABILIZE | 84.0 | 5 | 22 | 2 | 20.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 289 | BUY | SLOWROLL | 74.0 | 5 | 30 | 3 | 20.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08924895524978638 | 0.0 | 0.0 | +4ac49c80-f0c3-47ae-a031-96928d244e13 / -— |
| Jogador 8 | 3-2 | 290 | BUY | STABILIZE | 74.0 | 5 | 26 | 2 | 20.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05533408001065254 | 0.0 | 0.0 | +655deca9-2d3f-4e88-827a-5f49da8f3451 / -— |
| Jogador 8 | 3-2 | 291 | MOVE_BENCH | STABILIZE | 74.0 | 5 | 24 | 2 | 20.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.287631094455719 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 292 | MOVE_BOARD | STABILIZE | 74.0 | 5 | 24 | 2 | 22.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.043036337941884995 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 293 | MOVE_BOARD | STABILIZE | 74.0 | 5 | 24 | 2 | 22.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14920157194137573 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 294 | MOVE_BOARD | STABILIZE | 74.0 | 5 | 24 | 2 | 22.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 295 | MOVE_BOARD | STABILIZE | 74.0 | 5 | 24 | 2 | 22.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1721472442150116 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 296 | PASS | STABILIZE | 74.0 | 5 | 24 | 2 | 22.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 306 | BUY | SLOWROLL | 63.0 | 5 | 32 | 3 | 22.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2872101068496704 | 0.0 | 0.0 | +e4605ac7-0b51-4f1c-a658-f7d25f9a9dae / -— |
| Jogador 8 | 3-3 | 307 | MOVE_BOARD | STABILIZE | 63.0 | 5 | 29 | 2 | 22.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23221850395202637 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 308 | MOVE_BOARD | STABILIZE | 63.0 | 5 | 29 | 2 | 22.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14920157194137573 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 309 | MOVE_BOARD | STABILIZE | 63.0 | 5 | 29 | 2 | 22.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 310 | MOVE_BOARD | STABILIZE | 63.0 | 5 | 29 | 2 | 22.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 311 | PASS | STABILIZE | 63.0 | 5 | 29 | 2 | 22.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 323 | BUY | SLOWROLL | 51.0 | 5 | 38 | 3 | 22.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21401871740818024 | 0.0 | 0.0 | +82e109f9-54c8-492d-93e5-7e0dd0034b15 / -— |
| Jogador 8 | 3-4 | 324 | BUY | SLOWROLL | 51.0 | 5 | 35 | 3 | 22.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26689398288726807 | 0.0 | 0.0 | +d5848998-33f3-4632-94c0-60388a7cc6b8 / -— |
| Jogador 8 | 3-4 | 325 | MOVE_BOARD | SLOWROLL | 51.0 | 5 | 33 | 3 | 22.0 | Vivaz/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1721472442150116 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 326 | MOVE_BOARD | SLOWROLL | 51.0 | 5 | 33 | 3 | 22.0 | Vivaz/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 327 | PASS | SLOWROLL | 51.0 | 5 | 33 | 3 | 22.0 | Vivaz/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 342 | MOVE_BENCH | SLOWROLL | 51.0 | 6 | 43 | 4 | 22.0 | Vivaz/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.607593834400177 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 343 | BUY | SLOWROLL | 51.0 | 6 | 43 | 4 | 28.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11884678155183792 | 0.0 | 0.0 | +9af097e2-729d-474a-9a7e-b266c665c606 / -— |
| Jogador 8 | 3-5 | 344 | MOVE_BOARD | SLOWROLL | 51.0 | 6 | 40 | 4 | 28.0 | Vivaz/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.053781770169734955 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 345 | SELL | SLOWROLL | 51.0 | 6 | 40 | 4 | 28.0 | Vivaz/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05400000140070915 | 0.0 | 0.0 | +— / -d5848998-33f3-4632-94c0-60388a7cc6b8 |
| Jogador 8 | 3-5 | 346 | BUY | SLOWROLL | 51.0 | 6 | 42 | 4 | 28.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30612021684646606 | 0.0 | 0.0 | +bd4236f8-c8ff-4536-934a-b12b71012724 / -— |
| Jogador 8 | 3-5 | 347 | MOVE_BOARD | SLOWROLL | 51.0 | 6 | 39 | 3 | 28.0 | Vivaz/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1390107125043869 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 348 | MOVE_BOARD | SLOWROLL | 51.0 | 6 | 39 | 3 | 28.0 | Vivaz/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 349 | PASS | SLOWROLL | 51.0 | 6 | 39 | 3 | 28.0 | Vivaz/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 362 | SELL | SLOWROLL | 40.0 | 6 | 50 | 5 | 28.0 | Vivaz/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -655deca9-2d3f-4e88-827a-5f49da8f3451 |
| Jogador 8 | 3-6 | 363 | BUY | SLOWROLL | 40.0 | 6 | 52 | 5 | 28.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006511294282972813 | 0.0 | 0.0 | +a23ee552-279e-4c6c-aa05-6197043e8f1d / -— |
| Jogador 8 | 3-6 | 364 | SELL | SLOWROLL | 40.0 | 6 | 48 | 4 | 28.0 | Vivaz/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12569230794906616 | 0.0 | 0.0 | +— / -bd4236f8-c8ff-4536-934a-b12b71012724 |
| Jogador 8 | 3-6 | 365 | BUY | SLOWROLL | 40.0 | 6 | 51 | 5 | 28.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16995978355407715 | 0.0 | 0.0 | +23366968-ed3f-43d0-9f24-bb7691bf5d45 / -— |
| Jogador 8 | 3-6 | 366 | MOVE_BENCH | SLOWROLL | 40.0 | 6 | 48 | 4 | 28.0 | Vivaz/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0654113292694092 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 367 | MOVE_BENCH | SLOWROLL | 40.0 | 6 | 48 | 4 | 26.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2662278711795807 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 368 | PASS | SLOWROLL | 40.0 | 6 | 48 | 4 | 28.0 | Vivaz/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 381 | MOVE_BENCH | STABILIZE | 30.0 | 6 | 60 | 5 | 28.0 | Vivaz/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19047978520393372 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 382 | SELL | STABILIZE | 30.0 | 6 | 60 | 5 | 28.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -4b4cc4ba-04a0-4e04-88f2-e6913a342285 |
| Jogador 8 | 3-7 | 383 | BUY | STABILIZE | 30.0 | 6 | 63 | 5 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12612448632717133 | 0.0 | 0.0 | +849ea0fc-7f61-4907-8abb-b25c8cc82efc / -— |
| Jogador 8 | 3-7 | 384 | SELL | STABILIZE | 30.0 | 6 | 60 | 5 | 28.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039230767637491226 | 0.0 | 0.0 | +— / -82e109f9-54c8-492d-93e5-7e0dd0034b15 |
| Jogador 8 | 3-7 | 385 | BUY | STABILIZE | 30.0 | 6 | 63 | 5 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2013607621192932 | 0.0 | 0.0 | +112206a4-c285-4f76-878a-056248cba468 / -— |
| Jogador 8 | 3-7 | 386 | MOVE_BENCH | STABILIZE | 30.0 | 6 | 60 | 5 | 28.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8226906657218933 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 387 | MOVE_BENCH | STABILIZE | 30.0 | 6 | 60 | 5 | 32.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.741450309753418 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 388 | PASS | STABILIZE | 30.0 | 6 | 60 | 5 | 28.0 | Vivaz/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004072675481438637 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 402 | SELL | STABILIZE | 30.0 | 6 | 73 | 5 | 28.0 | Vivaz/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03799999877810478 | 0.0 | 0.0 | +— / -e4605ac7-0b51-4f1c-a658-f7d25f9a9dae |
| Jogador 8 | 4-1 | 403 | BUY | STABILIZE | 30.0 | 6 | 76 | 5 | 28.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.1929371953010559 | 0.0 | 0.0 | +88035b70-61e0-4279-9d55-e451f412f0d3 / -— |
| Jogador 8 | 4-1 | 404 | SELL | STABILIZE | 30.0 | 6 | 73 | 5 | 28.0 | Vivaz/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.039230767637491226 | 0.0 | 0.0 | +— / -88035b70-61e0-4279-9d55-e451f412f0d3 |
| Jogador 8 | 4-1 | 405 | BUY | STABILIZE | 30.0 | 6 | 76 | 5 | 28.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8617653250694275 | 0.0 | 0.0 | +2faa526c-d29e-47a9-9eb3-5030750cb483 / -— |
| Jogador 8 | 4-1 | 406 | SELL | STABILIZE | 30.0 | 6 | 75 | 5 | 28.0 | Vivaz/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03799999877810478 | 0.0 | 0.0 | +— / -112206a4-c285-4f76-878a-056248cba468 |
| Jogador 8 | 4-1 | 407 | BUY | STABILIZE | 30.0 | 6 | 78 | 5 | 28.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.34270021319389343 | 0.0 | 0.0 | +1e81ac95-667f-494d-89eb-2bcdcf887a7e / -— |
| Jogador 8 | 4-1 | 408 | MOVE_BENCH | STABILIZE | 30.0 | 6 | 76 | 5 | 28.0 | Vivaz/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.19047482311725616 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 409 | SELL | STABILIZE | 30.0 | 6 | 76 | 5 | 28.0 | Vivaz/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03729572147130966 | 0.0 | 0.0 | +— / -9af097e2-729d-474a-9a7e-b266c665c606 |
| Jogador 8 | 4-1 | 410 | BUY | STABILIZE | 30.0 | 6 | 79 | 5 | 28.0 | Vivaz/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.03106311336159706 | 0.0 | 0.0 | +2c153083-6c43-425e-90d5-23f7f2058592 / -— |
| Jogador 8 | 4-1 | 411 | MOVE_BOARD | STABILIZE | 30.0 | 6 | 77 | 5 | 28.0 | Vivaz/DA_18_Lillia | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10906810313463211 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 412 | PASS | STABILIZE | 30.0 | 6 | 77 | 5 | 28.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.013412702828645706 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 422 | SELL | STABILIZE | 18.0 | 6 | 90 | 5 | 28.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0370769239962101 | 0.0 | 0.0 | +— / -2c153083-6c43-425e-90d5-23f7f2058592 |
| Jogador 8 | 4-2 | 423 | BUY | STABILIZE | 18.0 | 6 | 92 | 5 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.050004564225673676 | 0.0 | 0.0 | +08a36d54-bb5c-48a6-afb1-e0f9943bf069 / -— |
| Jogador 8 | 4-2 | 424 | SELL | STABILIZE | 18.0 | 6 | 88 | 5 | 28.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.003275449387729168 | 0.0 | 0.0 | +— / -849ea0fc-7f61-4907-8abb-b25c8cc82efc |
| Jogador 8 | 4-2 | 425 | BUY | STABILIZE | 18.0 | 6 | 91 | 5 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2244458645582199 | 0.0 | 0.0 | +dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 / -— |
| Jogador 8 | 4-2 | 426 | SELL | STABILIZE | 18.0 | 6 | 88 | 5 | 28.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04169230908155441 | 0.0 | 0.0 | +— / -dfeacd3b-22c2-4ca5-a90e-c87b79d58ce7 |
| Jogador 8 | 4-2 | 427 | BUY | STABILIZE | 18.0 | 6 | 91 | 5 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.030122006312012672 | 0.0 | 0.0 | +fb7e519a-8419-414a-8bdc-706c584ddeed / -— |
| Jogador 8 | 4-2 | 428 | MOVE_BENCH | STABILIZE | 18.0 | 6 | 89 | 5 | 28.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.7508577108383179 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 429 | SELL | STABILIZE | 18.0 | 6 | 89 | 5 | 34.0 | Vivaz/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0370769239962101 | 0.0 | 0.0 | +— / -fb7e519a-8419-414a-8bdc-706c584ddeed |
| Jogador 8 | 4-2 | 430 | BUY | STABILIZE | 18.0 | 6 | 91 | 5 | 34.0 | Vivaz/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2604556679725647 | 0.0 | 0.0 | +07cc291c-137e-4668-9caf-3a1fa8f09c3d / -— |
| Jogador 8 | 4-2 | 431 | CRAFT_AND_EQUIP | STABILIZE | 18.0 | 6 | 89 | 5 | 34.0 | Vivaz/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.06532470136880875 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 432 | PASS | STABILIZE | 18.0 | 6 | 89 | 5 | 34.0 | Vivaz/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020852461457252502 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 441 | SELL | ALL_IN | 5.0 | 6 | 102 | 5 | 34.0 | Vivaz/DA_18_Sivir | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -07cc291c-137e-4668-9caf-3a1fa8f09c3d |
| Jogador 8 | 4-3 | 442 | BUY | ALL_IN | 5.0 | 6 | 104 | 5 | 34.0 | Vivaz/DA_18_Sivir | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.04817795753479 | 0.0 | 0.0 | +8455b875-27e0-4172-9311-5cbb3e2242b9 / -87600495-fe90-4832-ab42-9a5cb0ebe3f4,d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 8 | 4-3 | 443 | BUY | ALL_IN | 5.0 | 6 | 101 | 5 | 28.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8626104593276978 | 0.0 | 0.0 | +1fa69553-5270-4459-986b-600f748711b7 / -— |
| Jogador 8 | 4-3 | 444 | MOVE_BENCH | ALL_IN | 5.0 | 6 | 98 | 5 | 28.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8689317107200623 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 445 | BUY | ALL_IN | 5.0 | 6 | 98 | 5 | 30.0 | Vivaz/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8879866003990173 | 0.0 | 0.0 | +e85c6ab6-f36c-40b4-88e2-b7380b4c9652 / -— |
| Jogador 8 | 4-3 | 446 | PASS | ALL_IN | 5.0 | 6 | 96 | 5 | 30.0 | Vivaz/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0754207968711853 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 461 | PASS | ALL_IN | 0.0 | 6 | 96 | 5 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 481 | PASS | ALL_IN | 0.0 | 6 | 96 | 5 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 500 | PASS | ALL_IN | 0.0 | 6 | 96 | 5 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 512 | PASS | ALL_IN | 0.0 | 6 | 96 | 5 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 531 | PASS | ALL_IN | 0.0 | 6 | 96 | 5 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 549 | PASS | ALL_IN | 0.0 | 6 | 96 | 5 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 562 | PASS | ALL_IN | 0.0 | 6 | 96 | 5 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 579 | PASS | ALL_IN | 0.0 | 6 | 96 | 5 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 592 | PASS | ALL_IN | 0.0 | 6 | 96 | 5 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 609 | PASS | ALL_IN | 0.0 | 6 | 96 | 5 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 622 | PASS | ALL_IN | 0.0 | 6 | 96 | 5 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 638 | PASS | ALL_IN | 0.0 | 6 | 96 | 5 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 652 | PASS | ALL_IN | 0.0 | 6 | 96 | 5 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-3 | 667 | PASS | ALL_IN | 0.0 | 6 | 96 | 5 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-4 | 681 | PASS | ALL_IN | 0.0 | 6 | 96 | 5 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-5 | 695 | PASS | ALL_IN | 0.0 | 6 | 96 | 5 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-6 | 709 | PASS | ALL_IN | 0.0 | 6 | 96 | 5 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-7 | 719 | PASS | ALL_IN | 0.0 | 6 | 96 | 5 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 7-1 | 729 | PASS | ALL_IN | 0.0 | 6 | 96 | 5 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 7-2 | 741 | PASS | ALL_IN | 0.0 | 6 | 96 | 5 | 0.0 | Vivaz/DA_18_Tristana | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 276 | 308 | 145 | 16 | 16 | 1 | 0 | 0 | 147 | 64.0 |
- Jogador 1 — gasto por ação: BUY: 232g, BUY_XP: 76g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 7g, stage 2: 22g, stage 3: 94g, stage 4: 43g, stage 5: 66g, stage 6: 66g, stage 7: 10g
| Jogador 2 | 227 | 219 | 112 | 8 | 9 | 1 | 0 | 0 | 227 | 0.0 |
- Jogador 2 — gasto por ação: BUY: 171g, BUY_XP: 48g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 8g, stage 2: 38g, stage 3: 68g, stage 4: 25g, stage 5: 65g, stage 6: 15g, stage 7: 0g
| Jogador 3 | 146 | 76 | 15 | 2 | 1 | 1 | 0 | 0 | 129 | 0.0 |
- Jogador 3 — gasto por ação: BUY: 64g, BUY_XP: 12g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 3g, stage 2: 17g, stage 3: 36g, stage 4: 20g, stage 5: 0g, stage 6: 0g, stage 7: 0g
| Jogador 4 | 225 | 148 | 97 | 6 | 0 | 0 | 0 | 0 | 152 | 0.0 |
- Jogador 4 — gasto por ação: BUY: 144g, BUY_XP: 4g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 8g, stage 2: 22g, stage 3: 55g, stage 4: 61g, stage 5: 2g, stage 6: 0g, stage 7: 0g
| Jogador 5 | 191 | 171 | 66 | 10 | 8 | 0 | 0 | 0 | 101 | 0.0 |
- Jogador 5 — gasto por ação: BUY: 135g, BUY_XP: 36g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 6g, stage 2: 38g, stage 3: 41g, stage 4: 64g, stage 5: 22g, stage 6: 0g, stage 7: 0g
| Jogador 6 | 186 | 122 | 71 | 7 | 0 | 0 | 0 | 0 | 110 | 0.0 |
- Jogador 6 — gasto por ação: BUY: 118g, BUY_XP: 4g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 7g, stage 2: 20g, stage 3: 71g, stage 4: 24g, stage 5: 0g, stage 6: 0g, stage 7: 0g
| Jogador 7 | 344 | 411 | 254 | 18 | 15 | 2 | 0 | 0 | 211 | 66.0 |
- Jogador 7 — gasto por ação: BUY: 339g, BUY_XP: 72g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 5g, stage 2: 54g, stage 3: 53g, stage 4: 81g, stage 5: 94g, stage 6: 92g, stage 7: 32g
| Jogador 8 | 185 | 124 | 71 | 8 | 0 | 0 | 0 | 0 | 96 | 0.0 |
- Jogador 8 — gasto por ação: BUY: 116g, BUY_XP: 8g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 10g, stage 2: 48g, stage 3: 39g, stage 4: 27g, stage 5: 0g, stage 6: 0g, stage 7: 0g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 1 | 1 | 0 | 0.0% |
| Jogador 2 | 1 | 1 | 0 | 0.0% |
| Jogador 3 | 3 | 2 | 1 | 33.3% |
| Jogador 4 | 2 | 2 | 0 | 0.0% |
| Jogador 5 | 2 | 2 | 0 | 0.0% |
| Jogador 6 | 2 | 2 | 0 | 0.0% |
| Jogador 7 | 2 | 2 | 0 | 0.0% |
| Jogador 8 | 2 | 2 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ médio qualidade | Estrutural médio | Δ estrutural médio | Posicional médio | Δ qualidade combate + | Δ qualidade combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 276 | 0 | 0 | 276 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ 0.0000 (73 ações), BUY_XP: Δ 0.0000 (19 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (5 ações), MOVE_BENCH: Δ 0.0000 (49 ações), MOVE_BOARD: Δ 0.0000 (45 ações), PASS: Δ 0.0000 (41 ações), SELL: Δ 0.0000 (43 ações)
| Jogador 2 | 227 | 0 | 0 | 227 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ 0.0000 (63 ações), BUY_XP: Δ 0.0000 (12 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0000 (33 ações), MOVE_BOARD: Δ 0.0000 (33 ações), PASS: Δ 0.0000 (41 ações), SELL: Δ 0.0000 (42 ações)
| Jogador 3 | 146 | 0 | 0 | 146 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ 0.0000 (26 ações), BUY_XP: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0000 (39 ações), MOVE_BOARD: Δ 0.0000 (29 ações), PASS: Δ 0.0000 (41 ações), SELL: Δ 0.0000 (8 ações)
| Jogador 4 | 225 | 0 | 0 | 225 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ 0.0000 (76 ações), BUY_XP: Δ 0.0000 (1 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (14 ações), MOVE_BOARD: Δ 0.0000 (39 ações), PASS: Δ 0.0000 (41 ações), SELL: Δ 0.0000 (52 ações)
| Jogador 5 | 191 | 0 | 0 | 191 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ 0.0000 (56 ações), BUY_XP: Δ 0.0000 (9 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (27 ações), MOVE_BOARD: Δ 0.0000 (23 ações), PASS: Δ 0.0000 (41 ações), SELL: Δ 0.0000 (33 ações)
| Jogador 6 | 186 | 0 | 0 | 186 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ 0.0000 (54 ações), BUY_XP: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (27 ações), MOVE_BOARD: Δ 0.0000 (27 ações), PASS: Δ 0.0000 (41 ações), SELL: Δ 0.0000 (36 ações)
| Jogador 7 | 344 | 0 | 0 | 344 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ 0.0000 (117 ações), BUY_XP: Δ 0.0000 (18 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (5 ações), MOVE_BENCH: Δ 0.0000 (31 ações), MOVE_BOARD: Δ 0.0000 (44 ações), PASS: Δ 0.0000 (39 ações), SELL: Δ 0.0000 (89 ações)
| Jogador 8 | 185 | 0 | 0 | 185 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ 0.0000 (50 ações), BUY_XP: Δ 0.0000 (2 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (32 ações), MOVE_BOARD: Δ 0.0000 (27 ações), PASS: Δ 0.0000 (41 ações), SELL: Δ 0.0000 (32 ações)

A pontuação é uma heurística para auditoria, não uma verdade absoluta. Compare-a com recompensas e resultados de combate; correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 317 | OK (317) | 0 | 0 | 0 | 1 | 3 | 1 |
- Jogador 1 — IDs equipados observados: DA_18_EmblemSlayer, TFT_Item_IonicSpark, TFT_Item_UnstableConcoction; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 5, COMPONENT_ANVIL_GRANTED: 5, COMPONENT_LOOT_GRANTED: 16.
| Jogador 2 | 268 | OK (268) | 0 | 0 | 0 | 3 | 1 | 1 |
- Jogador 2 — IDs equipados observados: TFT_Item_IonicSpark; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 5, COMPONENT_ANVIL_GRANTED: 5, COMPONENT_LOOT_GRANTED: 16.
| Jogador 3 | 187 | OK (187) | 0 | 0 | 0 | 2 | 0 | 0 |
- Jogador 3 — IDs equipados observados: nenhum observado; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 5, COMPONENT_ANVIL_GRANTED: 5, COMPONENT_LOOT_GRANTED: 16.
| Jogador 4 | 266 | OK (266) | 0 | 0 | 0 | 1 | 1 | 0 |
- Jogador 4 — IDs equipados observados: TFT_Item_Redemption; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 5, COMPONENT_ANVIL_GRANTED: 5, COMPONENT_LOOT_GRANTED: 16.
| Jogador 5 | 232 | OK (232) | 0 | 0 | 0 | 1 | 1 | 0 |
- Jogador 5 — IDs equipados observados: TFT_Item_TitansResolve; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 5, COMPONENT_ANVIL_GRANTED: 5, COMPONENT_LOOT_GRANTED: 16.
| Jogador 6 | 227 | OK (227) | 0 | 0 | 0 | 2 | 0 | 0 |
- Jogador 6 — IDs equipados observados: nenhum observado; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 5, COMPONENT_ANVIL_GRANTED: 5, COMPONENT_LOOT_GRANTED: 16.
| Jogador 7 | 385 | OK (385) | 3 | 0 | 0 | 1 | 3 | 1 |
- Jogador 7 — IDs equipados observados: TFT_Item_JeweledGauntlet, TFT_Item_TacticiansScepter, TFT_Item_WarmogsArmor; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 5, COMPONENT_ANVIL_GRANTED: 5, COMPONENT_LOOT_GRANTED: 16.
| Jogador 8 | 226 | OK (226) | 0 | 0 | 0 | 0 | 1 | 0 |
- Jogador 8 — IDs equipados observados: TFT_Item_Crownguard; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 5, COMPONENT_ANVIL_GRANTED: 5, COMPONENT_LOOT_GRANTED: 16.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 9 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 3 | 2 → 3 | 0.031 | 0.000 |
| Jogador 1 | 1-2 | 12 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.017 | 0.000 |
| Jogador 1 | 1-3 | 5 | 2.000 | 2.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.120 | 0.000 |
| Jogador 1 | 1-4 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 3 → 7 | 0 | 3 → 4 | -0.031 | 0.000 |
| Jogador 1 | 2-1 | 12 | 6.000 | -2.000 | 0 → 1 | 1 → 0 | 11% → 14% | 7 → 10 | 3 | 4 → 4 | 0.056 | 0.198 |
| Jogador 1 | 2-2 | 12 | 4.000 | 0.000 | 1 → 0 | 0 → 1 | 14% → 14% | 10 → 6 | 13 | 4 → 5 | -0.038 | -0.188 |
| Jogador 1 | 2-3 | 9 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 6 → 9 | 3 | 5 → 5 | 0.004 | 0.299 |
| Jogador 1 | 2-4 | 7 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 18% → 18% | 9 → 11 | 3 | 5 → 5 | -0.040 | 0.000 |
| Jogador 1 | 2-5 | 6 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 11 → 17 | 0 | 5 → 5 | 0.149 | -0.413 |
| Jogador 1 | 2-6 | 12 | 2.000 | -2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 17 → 24 | 0 | 5 → 5 | -0.051 | 0.205 |
| Jogador 1 | 2-7 | 5 | -2.000 | 2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 24 → 31 | 0 | 5 → 5 | 0.001 | 0.000 |
| Jogador 1 | 3-1 | 12 | 8.000 | -6.000 | 0 → 0 | 1 → 2 | 18% → 21% | 31 → 31 | 11 | 5 → 6 | 0.044 | 0.234 |
| Jogador 1 | 3-2 | 12 | 4.000 | 0.000 | 0 → 0 | 2 → 1 | 21% → 21% | 31 → 12 | 28 | 6 → 6 | 0.007 | 0.246 |
| Jogador 1 | 3-3 | 12 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 25% | 12 → 8 | 11 | 6 → 7 | -0.054 | 0.259 |
| Jogador 1 | 3-4 | 11 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 8 → 6 | 11 | 7 → 7 | 0.001 | 0.000 |
| Jogador 1 | 3-5 | 6 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 6 → 10 | 7 | 7 → 7 | 0.007 | 0.514 |
| Jogador 1 | 3-6 | 12 | 8.000 | 0.000 | 0 → 1 | 1 → 0 | 25% → 25% | 10 → 12 | 7 | 7 → 7 | -0.006 | 0.234 |
| Jogador 1 | 3-7 | 12 | 2.000 | 0.000 | 1 → 1 | 0 → 0 | 25% → 25% | 12 → 11 | 19 | 7 → 7 | -0.014 | 0.000 |
| Jogador 1 | 4-1 | 6 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 25% → 25% | 11 → 9 | 11 | 7 → 7 | 0.000 | 0.481 |
| Jogador 1 | 4-2 | 4 | 0.000 | 12.000 | 1 → 1 | 0 → 0 | 25% → 25% | 9 → 12 | 6 | 7 → 7 | 0.000 | 0.740 |
| Jogador 1 | 4-3 | 3 | 0.000 | 6.000 | 1 → 1 | 0 → 1 | 25% → 25% | 12 → 19 | 3 | 7 → 7 | 0.000 | 1.045 |
| Jogador 1 | 4-4 | 3 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 25% → 25% | 19 → 25 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 4-5 | 5 | 0.000 | 22.000 | 1 → 1 | 1 → 2 | 25% → 25% | 25 → 20 | 11 | 7 → 7 | 0.000 | -0.533 |
| Jogador 1 | 4-6 | 3 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 25% → 25% | 20 → 24 | 3 | 7 → 7 | 0.000 | 0.950 |
| Jogador 1 | 4-7 | 6 | 0.000 | 0.000 | 1 → 1 | 3 → 4 | 25% → 25% | 24 → 31 | 6 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 5-1 | 12 | 0.000 | 14.000 | 1 → 1 | 4 → 2 | 25% → 25% | 31 → 24 | 16 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 5-2 | 10 | 6.000 | -6.000 | 1 → 2 | 2 → 1 | 25% → 25% | 24 → 30 | 10 | 7 → 8 | -0.003 | 0.297 |
| Jogador 1 | 5-3 | 9 | 8.000 | 6.000 | 2 → 2 | 1 → 1 | 25% → 29% | 30 → 31 | 11 | 8 → 8 | 0.064 | 0.000 |
| Jogador 1 | 5-4 | 6 | 0.000 | -6.000 | 2 → 2 | 1 → 1 | 29% → 29% | 31 → 43 | 4 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 5-5 | 6 | 0.000 | 4.000 | 2 → 2 | 1 → 1 | 29% → 29% | 43 → 51 | 8 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 5-6 | 8 | 0.000 | 0.000 | 2 → 2 | 1 → 1 | 29% → 29% | 51 → 61 | 11 | 8 → 8 | 0.000 | -0.344 |
| Jogador 1 | 5-7 | 6 | 0.000 | -2.000 | 2 → 2 | 1 → 2 | 29% → 29% | 61 → 72 | 6 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 6-1 | 8 | 0.000 | 2.000 | 2 → 2 | 2 → 3 | 29% → 29% | 72 → 81 | 8 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 6-2 | 8 | -2.000 | 0.000 | 2 → 2 | 3 → 2 | 29% → 29% | 81 → 89 | 11 | 8 → 8 | -0.012 | 0.368 |
| Jogador 1 | 6-3 | 5 | 0.000 | 10.000 | 2 → 2 | 2 → 3 | 29% → 29% | 89 → 94 | 8 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 6-4 | 8 | 0.000 | 2.000 | 2 → 2 | 3 → 2 | 29% → 29% | 94 → 103 | 12 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 6-5 | 6 | 0.000 | 10.000 | 2 → 2 | 2 → 1 | 29% → 29% | 103 → 105 | 12 | 8 → 8 | -0.010 | -0.475 |
| Jogador 1 | 6-6 | 6 | 0.000 | 0.000 | 2 → 2 | 1 → 1 | 29% → 29% | 105 → 116 | 8 | 8 → 8 | 0.000 | -0.475 |
| Jogador 1 | 6-7 | 6 | 0.000 | -10.000 | 2 → 2 | 1 → 1 | 29% → 29% | 116 → 135 | 7 | 8 → 8 | 0.010 | 0.000 |
| Jogador 1 | 7-1 | 6 | 0.000 | 0.000 | 2 → 2 | 1 → 1 | 29% → 29% | 135 → 146 | 4 | 8 → 8 | 0.000 | -0.475 |
| Jogador 1 | 7-2 | 6 | -64.000 | -82.000 | 2 → 0 | 1 → 0 | 29% → 0% | 146 → 147 | 6 | 8 → 8 | -0.038 | -0.475 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 25, COMPOSITION_COMPATIBILITY: 24, IMMEDIATE_UPGRADE: 7, PAIR_POTENTIAL: 17; mudanças de composição: 0; posicionamento melhorou em 45 ações e piorou em 43.
- Jogador 1 — estado final: ouro 147, nível 8, vida 0.0, colocação 2.
| Jogador 2 | 1-1 | 7 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 2 | 2 → 3 | 0.040 | 0.000 |
| Jogador 2 | 1-2 | 12 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.017 | 0.000 |
| Jogador 2 | 1-3 | 7 | 2.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 4 | 2 | 3 → 3 | 0.024 | 0.000 |
| Jogador 2 | 1-4 | 5 | 2.000 | 0.000 | 0 → 0 | 1 → 0 | 11% → 11% | 4 → 7 | 2 | 3 → 4 | -0.141 | 0.000 |
| Jogador 2 | 2-1 | 7 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 7 → 10 | 3 | 4 → 4 | 0.002 | 0.359 |
| Jogador 2 | 2-2 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 14% → 14% | 10 → 15 | 2 | 4 → 4 | 0.001 | 0.397 |
| Jogador 2 | 2-3 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 15 → 21 | 0 | 4 → 4 | 0.000 | -0.632 |
| Jogador 2 | 2-4 | 4 | -2.000 | 2.000 | 0 → 0 | 1 → 1 | 14% → 14% | 21 → 28 | 0 | 4 → 4 | 0.017 | 0.000 |
| Jogador 2 | 2-5 | 12 | 8.000 | -6.000 | 0 → 0 | 1 → 1 | 14% → 18% | 28 → 18 | 19 | 4 → 5 | 0.047 | 0.220 |
| Jogador 2 | 2-6 | 9 | 6.000 | 0.000 | 0 → 1 | 1 → 0 | 18% → 18% | 18 → 21 | 5 | 5 → 5 | -0.097 | 0.279 |
| Jogador 2 | 2-7 | 12 | 6.000 | 4.000 | 1 → 1 | 0 → 0 | 18% → 21% | 21 → 19 | 9 | 5 → 6 | 0.027 | 0.000 |
| Jogador 2 | 3-1 | 6 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 21% → 21% | 19 → 24 | 3 | 6 → 6 | 0.000 | 0.500 |
| Jogador 2 | 3-2 | 12 | 0.000 | -10.000 | 1 → 1 | 0 → 0 | 21% → 21% | 24 → 39 | 1 | 6 → 6 | -0.011 | 0.254 |
| Jogador 2 | 3-3 | 7 | 2.000 | 6.000 | 1 → 1 | 0 → 0 | 21% → 21% | 39 → 46 | 7 | 6 → 6 | 0.121 | 0.416 |
| Jogador 2 | 3-4 | 12 | 0.000 | -6.000 | 1 → 1 | 0 → 0 | 21% → 21% | 46 → 47 | 16 | 6 → 6 | -0.029 | 0.000 |
| Jogador 2 | 3-5 | 12 | 0.000 | 0.000 | 1 → 1 | 0 → 0 | 21% → 21% | 47 → 47 | 18 | 6 → 7 | -0.001 | 0.246 |
| Jogador 2 | 3-6 | 12 | 4.000 | 0.000 | 1 → 1 | 0 → 0 | 21% → 25% | 47 → 58 | 9 | 7 → 7 | -0.044 | 0.238 |
| Jogador 2 | 3-7 | 12 | 0.000 | 8.000 | 1 → 1 | 0 → 0 | 25% → 25% | 58 → 63 | 14 | 7 → 7 | 0.055 | 0.000 |
| Jogador 2 | 4-1 | 9 | 0.000 | 4.000 | 1 → 0 | 0 → 0 | 25% → 25% | 63 → 75 | 9 | 7 → 7 | -0.041 | 0.324 |
| Jogador 2 | 4-2 | 4 | 0.000 | 10.000 | 0 → 0 | 0 → 1 | 25% → 25% | 75 → 84 | 5 | 7 → 7 | 0.000 | 0.746 |
| Jogador 2 | 4-3 | 5 | 0.000 | -14.000 | 0 → 0 | 1 → 0 | 25% → 25% | 84 → 104 | 2 | 7 → 7 | 0.000 | 0.577 |
| Jogador 2 | 4-4 | 4 | 0.000 | 12.000 | 0 → 0 | 0 → 1 | 25% → 25% | 104 → 111 | 6 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 4-5 | 3 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 25% → 25% | 111 → 122 | 3 | 7 → 7 | 0.000 | 0.945 |
| Jogador 2 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 122 → 136 | 0 | 7 → 7 | 0.000 | 1.456 |
| Jogador 2 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 136 → 149 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 5-1 | 4 | 0.000 | 10.000 | 0 → 0 | 1 → 1 | 25% → 25% | 149 → 158 | 5 | 7 → 7 | 0.000 | 0.721 |
| Jogador 2 | 5-2 | 6 | 0.000 | 24.000 | 0 → 0 | 1 → 2 | 25% → 25% | 158 → 156 | 12 | 7 → 7 | 0.000 | -0.475 |
| Jogador 2 | 5-3 | 10 | 4.000 | -4.000 | 0 → 1 | 2 → 2 | 25% → 25% | 156 → 165 | 10 | 7 → 7 | -0.006 | -0.285 |
| Jogador 2 | 5-4 | 7 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 25% → 25% | 165 → 173 | 9 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 5-5 | 8 | 0.000 | 4.000 | 1 → 1 | 3 → 3 | 25% → 25% | 173 → 182 | 9 | 7 → 7 | 0.000 | -0.356 |
| Jogador 2 | 5-6 | 8 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 25% → 25% | 182 → 193 | 9 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 5-7 | 8 | 0.000 | 2.000 | 1 → 1 | 3 → 4 | 25% → 25% | 193 → 203 | 11 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 6-1 | 6 | 0.000 | -2.000 | 1 → 1 | 4 → 4 | 25% → 25% | 203 → 215 | 3 | 7 → 7 | 0.000 | -0.483 |
| Jogador 2 | 6-2 | 6 | 0.000 | -2.000 | 1 → 1 | 4 → 4 | 25% → 25% | 215 → 228 | 5 | 7 → 7 | 0.000 | -0.458 |
| Jogador 2 | 6-3 | 6 | -44.000 | -64.000 | 1 → 0 | 4 → 0 | 25% → 0% | 228 → 227 | 7 | 7 → 7 | -0.016 | -0.475 |
| Jogador 2 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 227 → 227 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 227 → 227 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 6-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 227 → 227 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 6-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 227 → 227 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 7-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 227 → 227 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 7-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 227 → 227 | 0 | 7 → 7 | 0.000 | 0.000 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 24, COMPOSITION_COMPATIBILITY: 25, IMMEDIATE_UPGRADE: 3, PAIR_POTENTIAL: 11; mudanças de composição: 0; posicionamento melhorou em 32 ações e piorou em 37.
- Jogador 2 — estado final: ouro 227, nível 7, vida 0.0, colocação 3.
| Jogador 3 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 3 | 1-2 | 12 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.002 | 0.000 |
| Jogador 3 | 1-3 | 7 | 0.000 | 2.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 4 | 1 | 3 → 3 | 0.022 | 0.000 |
| Jogador 3 | 1-4 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 4 → 8 | 0 | 3 → 4 | -0.028 | 0.000 |
| Jogador 3 | 2-1 | 9 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 14% | 8 → 11 | 2 | 4 → 4 | 0.004 | -0.251 |
| Jogador 3 | 2-2 | 5 | -2.000 | 2.000 | 0 → 0 | 1 → 1 | 14% → 14% | 11 → 18 | 0 | 4 → 4 | -0.021 | -0.486 |
| Jogador 3 | 2-3 | 6 | 2.000 | -2.000 | 0 → 0 | 1 → 1 | 14% → 14% | 18 → 25 | 0 | 4 → 4 | 0.017 | 0.419 |
| Jogador 3 | 2-4 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 25 → 32 | 0 | 4 → 4 | 0.000 | 0.000 |
| Jogador 3 | 2-5 | 12 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 32 → 35 | 8 | 4 → 5 | 0.008 | 0.202 |
| Jogador 3 | 2-6 | 10 | 4.000 | 0.000 | 0 → 0 | 1 → 2 | 14% → 18% | 35 → 41 | 2 | 5 → 5 | 0.000 | -0.237 |
| Jogador 3 | 2-7 | 11 | 6.000 | 0.000 | 0 → 1 | 2 → 1 | 18% → 18% | 41 → 44 | 5 | 5 → 5 | -0.008 | 0.000 |
| Jogador 3 | 3-1 | 4 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 18% → 18% | 44 → 54 | 0 | 5 → 5 | -0.021 | -0.659 |
| Jogador 3 | 3-2 | 12 | 4.000 | -2.000 | 1 → 1 | 1 → 0 | 18% → 18% | 54 → 64 | 3 | 5 → 5 | 0.021 | -0.231 |
| Jogador 3 | 3-3 | 5 | 6.000 | 2.000 | 1 → 1 | 0 → 0 | 18% → 18% | 64 → 71 | 4 | 5 → 5 | -0.053 | -0.527 |
| Jogador 3 | 3-4 | 8 | 4.000 | 0.000 | 1 → 1 | 0 → 0 | 18% → 21% | 71 → 72 | 10 | 5 → 6 | -0.006 | 0.000 |
| Jogador 3 | 3-5 | 7 | 0.000 | 14.000 | 1 → 1 | 0 → 0 | 21% → 21% | 72 → 77 | 7 | 6 → 6 | 0.006 | -0.388 |
| Jogador 3 | 3-6 | 4 | 0.000 | 10.000 | 1 → 1 | 0 → 0 | 21% → 21% | 77 → 83 | 5 | 6 → 6 | 0.000 | 0.738 |
| Jogador 3 | 3-7 | 5 | 0.000 | 14.000 | 1 → 1 | 0 → 1 | 21% → 21% | 83 → 86 | 7 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 4-1 | 3 | 0.000 | 0.000 | 1 → 1 | 1 → 0 | 21% → 21% | 86 → 93 | 3 | 6 → 6 | -0.020 | -0.917 |
| Jogador 3 | 4-2 | 4 | 0.000 | 10.000 | 1 → 1 | 0 → 2 | 21% → 21% | 93 → 99 | 5 | 6 → 6 | 0.000 | 0.750 |
| Jogador 3 | 4-3 | 6 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 21% → 21% | 99 → 106 | 7 | 6 → 6 | 0.000 | -0.438 |
| Jogador 3 | 4-4 | 2 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 21% → 21% | 106 → 116 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 4-5 | 4 | 0.000 | 0.000 | 1 → 1 | 2 → 3 | 21% → 21% | 116 → 127 | 3 | 6 → 6 | 0.000 | -0.669 |
| Jogador 3 | 4-6 | 4 | -38.000 | -56.000 | 1 → 0 | 3 → 0 | 21% → 0% | 127 → 129 | 2 | 6 → 6 | 0.093 | -0.687 |
| Jogador 3 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 129 → 129 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 5-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 129 → 129 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 129 → 129 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 129 → 129 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 129 → 129 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 129 → 129 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 129 → 129 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 129 → 129 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 129 → 129 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 129 → 129 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 129 → 129 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 129 → 129 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 129 → 129 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 6-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 129 → 129 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 6-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 129 → 129 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 7-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 129 → 129 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 7-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 129 → 129 | 0 | 6 → 6 | 0.000 | 0.000 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 4, COMPOSITION_COMPATIBILITY: 12, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 8; mudanças de composição: 2; posicionamento melhorou em 28 ações e piorou em 25.
- Jogador 3 — estado final: ouro 129, nível 6, vida 0.0, colocação 6.
| Jogador 4 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.056 | 0.000 |
| Jogador 4 | 1-2 | 11 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.018 | 0.000 |
| Jogador 4 | 1-3 | 5 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 5 | 0 | 3 → 3 | 0.003 | 0.000 |
| Jogador 4 | 1-4 | 7 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 11% → 14% | 5 → 4 | 5 | 3 → 4 | -0.012 | 0.000 |
| Jogador 4 | 2-1 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 4 → 9 | 0 | 4 → 4 | 0.000 | -0.565 |
| Jogador 4 | 2-2 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 9 → 16 | 0 | 4 → 4 | 0.012 | 0.476 |
| Jogador 4 | 2-3 | 12 | 2.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 16 → 21 | 4 | 4 → 5 | -0.008 | -0.202 |
| Jogador 4 | 2-4 | 7 | 8.000 | 4.000 | 0 → 0 | 1 → 1 | 14% → 18% | 21 → 21 | 6 | 5 → 5 | -0.058 | 0.000 |
| Jogador 4 | 2-5 | 5 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 18% → 18% | 21 → 25 | 3 | 5 → 5 | -0.002 | -0.464 |
| Jogador 4 | 2-6 | 11 | 0.000 | 2.000 | 0 → 0 | 1 → 1 | 18% → 18% | 25 → 32 | 3 | 5 → 5 | 0.027 | -0.211 |
| Jogador 4 | 2-7 | 11 | 4.000 | 6.000 | 0 → 0 | 1 → 0 | 18% → 18% | 32 → 34 | 6 | 5 → 5 | -0.018 | 0.000 |
| Jogador 4 | 3-1 | 12 | 0.000 | -4.000 | 0 → 0 | 0 → 1 | 18% → 18% | 34 → 46 | 6 | 5 → 5 | -0.013 | 0.235 |
| Jogador 4 | 3-2 | 12 | 0.000 | 8.000 | 0 → 0 | 1 → 1 | 18% → 18% | 46 → 50 | 7 | 5 → 5 | -0.063 | -0.211 |
| Jogador 4 | 3-3 | 12 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 18% → 18% | 50 → 57 | 9 | 5 → 5 | -0.005 | -0.228 |
| Jogador 4 | 3-4 | 12 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 57 → 68 | 7 | 5 → 5 | 0.000 | 0.000 |
| Jogador 4 | 3-5 | 12 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 68 → 79 | 9 | 5 → 5 | 0.000 | -0.243 |
| Jogador 4 | 3-6 | 12 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 79 → 90 | 7 | 5 → 6 | 0.000 | 0.238 |
| Jogador 4 | 3-7 | 12 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 90 → 100 | 10 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 4-1 | 12 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 100 → 110 | 10 | 6 → 6 | 0.000 | -0.242 |
| Jogador 4 | 4-2 | 12 | 0.000 | 2.000 | 0 → 1 | 1 → 1 | 18% → 14% | 110 → 120 | 8 | 6 → 6 | 0.071 | -0.235 |
| Jogador 4 | 4-3 | 12 | 0.000 | 4.000 | 1 → 1 | 1 → 2 | 14% → 14% | 120 → 129 | 14 | 6 → 6 | 0.000 | -0.249 |
| Jogador 4 | 4-4 | 11 | 6.000 | 6.000 | 1 → 1 | 2 → 3 | 14% → 18% | 129 → 134 | 10 | 6 → 6 | 0.002 | 0.000 |
| Jogador 4 | 4-5 | 8 | 4.000 | 4.000 | 1 → 1 | 3 → 3 | 18% → 21% | 134 → 141 | 8 | 6 → 6 | 0.002 | 0.356 |
| Jogador 4 | 4-6 | 6 | 6.000 | 2.000 | 1 → 2 | 3 → 3 | 21% → 21% | 141 → 144 | 9 | 6 → 6 | 0.000 | -0.446 |
| Jogador 4 | 4-7 | 3 | 0.000 | 4.000 | 2 → 2 | 3 → 3 | 21% → 21% | 144 → 152 | 2 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-1 | 5 | -38.000 | -50.000 | 2 → 0 | 3 → 0 | 21% → 0% | 152 → 152 | 2 | 6 → 6 | 0.008 | -0.546 |
| Jogador 4 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 152 → 152 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 152 → 152 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 152 → 152 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 152 → 152 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 152 → 152 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 152 → 152 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 152 → 152 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 152 → 152 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 152 → 152 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 152 → 152 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 152 → 152 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 152 → 152 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 152 → 152 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 7-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 152 → 152 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 7-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 152 → 152 | 0 | 6 → 6 | 0.000 | 0.000 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 39, COMPOSITION_COMPATIBILITY: 22, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 10; mudanças de composição: 1; posicionamento melhorou em 29 ações e piorou em 22.
- Jogador 4 — estado final: ouro 152, nível 6, vida 0.0, colocação 5.
| Jogador 5 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 5 | 1-2 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.136 | 0.000 |
| Jogador 5 | 1-3 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | 0.020 | 0.000 |
| Jogador 5 | 1-4 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 6 | 2 | 3 → 4 | 0.019 | 0.000 |
| Jogador 5 | 2-1 | 11 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 6 → 8 | 6 | 4 → 4 | -0.067 | -0.216 |
| Jogador 5 | 2-2 | 9 | 4.000 | 4.000 | 0 → 0 | 0 → 0 | 14% → 14% | 8 → 10 | 6 | 4 → 4 | -0.002 | -0.276 |
| Jogador 5 | 2-3 | 4 | -2.000 | 2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 10 → 17 | 0 | 4 → 4 | 0.000 | -0.593 |
| Jogador 5 | 2-4 | 4 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 17 → 24 | 0 | 4 → 4 | 0.000 | 0.000 |
| Jogador 5 | 2-5 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 24 → 32 | 0 | 4 → 5 | 0.016 | -0.620 |
| Jogador 5 | 2-6 | 12 | 4.000 | -2.000 | 0 → 0 | 0 → 1 | 14% → 18% | 32 → 32 | 12 | 5 → 5 | 0.000 | -0.216 |
| Jogador 5 | 2-7 | 12 | 4.000 | -2.000 | 0 → 0 | 1 → 1 | 18% → 21% | 32 → 27 | 14 | 5 → 6 | 0.040 | 0.000 |
| Jogador 5 | 3-1 | 9 | 2.000 | 4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 27 → 32 | 3 | 6 → 6 | 0.015 | 0.312 |
| Jogador 5 | 3-2 | 12 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 21% → 21% | 32 → 21 | 23 | 6 → 6 | -0.047 | 0.226 |
| Jogador 5 | 3-3 | 4 | 0.000 | 14.000 | 0 → 0 | 2 → 3 | 21% → 21% | 21 → 22 | 7 | 6 → 6 | 0.000 | 0.703 |
| Jogador 5 | 3-4 | 3 | 0.000 | 4.000 | 0 → 0 | 3 → 4 | 21% → 21% | 22 → 28 | 2 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 3-5 | 4 | 0.000 | 2.000 | 0 → 0 | 4 → 3 | 21% → 21% | 28 → 36 | 3 | 6 → 6 | 0.150 | 0.715 |
| Jogador 5 | 3-6 | 8 | 0.000 | -14.000 | 0 → 0 | 3 → 2 | 21% → 21% | 36 → 52 | 3 | 6 → 6 | 0.000 | -0.329 |
| Jogador 5 | 3-7 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 52 → 62 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-1 | 3 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 21% → 21% | 62 → 70 | 3 | 6 → 7 | 0.000 | 0.961 |
| Jogador 5 | 4-2 | 7 | 2.000 | 22.000 | 0 → 0 | 2 → 4 | 21% → 25% | 70 → 68 | 12 | 7 → 7 | -0.012 | -0.405 |
| Jogador 5 | 4-3 | 8 | 6.000 | 6.000 | 0 → 1 | 4 → 3 | 25% → 25% | 68 → 70 | 11 | 7 → 7 | -0.018 | 0.350 |
| Jogador 5 | 4-4 | 11 | 6.000 | -2.000 | 1 → 2 | 3 → 2 | 25% → 25% | 70 → 75 | 12 | 7 → 7 | -0.006 | 0.000 |
| Jogador 5 | 4-5 | 10 | 0.000 | 0.000 | 2 → 2 | 2 → 2 | 25% → 25% | 75 → 85 | 6 | 7 → 7 | 0.000 | -0.280 |
| Jogador 5 | 4-6 | 9 | 0.000 | 8.000 | 2 → 2 | 2 → 2 | 25% → 25% | 85 → 92 | 9 | 7 → 7 | -0.067 | -0.311 |
| Jogador 5 | 4-7 | 12 | 0.000 | -2.000 | 2 → 2 | 2 → 1 | 25% → 21% | 92 → 102 | 11 | 7 → 7 | -0.053 | 0.000 |
| Jogador 5 | 5-1 | 12 | 6.000 | 2.000 | 2 → 3 | 1 → 0 | 21% → 21% | 102 → 106 | 14 | 7 → 7 | 0.037 | -0.228 |
| Jogador 5 | 5-2 | 12 | -52.000 | -56.000 | 3 → 0 | 0 → 0 | 21% → 0% | 106 → 101 | 8 | 7 → 7 | 0.035 | -0.233 |
| Jogador 5 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 6-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 6-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 7-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 7-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 101 → 101 | 0 | 7 → 7 | 0.000 | 0.000 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 22, COMPOSITION_COMPATIBILITY: 23, IMMEDIATE_UPGRADE: 4, PAIR_POTENTIAL: 7; mudanças de composição: 1; posicionamento melhorou em 26 ações e piorou em 23.
- Jogador 5 — estado final: ouro 101, nível 7, vida 0.0, colocação 4.
| Jogador 6 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.056 | 0.000 |
| Jogador 6 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | -0.099 | 0.000 |
| Jogador 6 | 1-3 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.022 | 0.000 |
| Jogador 6 | 1-4 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | -0.034 | 0.000 |
| Jogador 6 | 2-1 | 8 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 5 → 8 | 3 | 4 → 4 | 0.050 | 0.297 |
| Jogador 6 | 2-2 | 4 | -2.000 | 2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 8 → 13 | 0 | 4 → 4 | 0.049 | -0.565 |
| Jogador 6 | 2-3 | 8 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 14% → 14% | 13 → 19 | 2 | 4 → 4 | -0.095 | -0.317 |
| Jogador 6 | 2-4 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 19 → 26 | 0 | 4 → 4 | 0.104 | 0.000 |
| Jogador 6 | 2-5 | 12 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 26 → 28 | 6 | 4 → 5 | 0.040 | 0.220 |
| Jogador 6 | 2-6 | 12 | 2.000 | -4.000 | 0 → 0 | 1 → 1 | 18% → 18% | 28 → 39 | 6 | 5 → 5 | 0.029 | 0.220 |
| Jogador 6 | 2-7 | 5 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 18% → 18% | 39 → 45 | 3 | 5 → 5 | -0.222 | 0.000 |
| Jogador 6 | 3-1 | 9 | -2.000 | 26.000 | 0 → 0 | 1 → 3 | 18% → 18% | 45 → 41 | 12 | 5 → 5 | 0.120 | -0.314 |
| Jogador 6 | 3-2 | 12 | -6.000 | 10.000 | 0 → 0 | 3 → 2 | 18% → 14% | 41 → 45 | 7 | 5 → 5 | -0.052 | -0.243 |
| Jogador 6 | 3-3 | 12 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 14% → 14% | 45 → 52 | 11 | 5 → 5 | 0.000 | -0.246 |
| Jogador 6 | 3-4 | 12 | 6.000 | 4.000 | 0 → 0 | 2 → 1 | 14% → 18% | 52 → 57 | 13 | 5 → 5 | 0.055 | 0.000 |
| Jogador 6 | 3-5 | 12 | 0.000 | -6.000 | 0 → 0 | 1 → 2 | 18% → 18% | 57 → 71 | 9 | 5 → 5 | 0.000 | -0.224 |
| Jogador 6 | 3-6 | 12 | 0.000 | -4.000 | 0 → 0 | 2 → 3 | 18% → 18% | 71 → 85 | 8 | 5 → 6 | 0.000 | -0.231 |
| Jogador 6 | 3-7 | 12 | 4.000 | 6.000 | 0 → 0 | 3 → 1 | 18% → 18% | 85 → 90 | 11 | 6 → 6 | -0.052 | 0.000 |
| Jogador 6 | 4-1 | 12 | 6.000 | -2.000 | 0 → 0 | 1 → 2 | 18% → 21% | 90 → 101 | 9 | 6 → 6 | -0.003 | -0.226 |
| Jogador 6 | 4-2 | 10 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 21% → 21% | 101 → 110 | 9 | 6 → 6 | 0.016 | -0.276 |
| Jogador 6 | 4-3 | 7 | -32.000 | -54.000 | 0 → 0 | 2 → 0 | 21% → 0% | 110 → 110 | 6 | 6 → 6 | 0.035 | -0.388 |
| Jogador 6 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 110 → 110 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 4-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 110 → 110 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 110 → 110 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 110 → 110 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 5-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 110 → 110 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 110 → 110 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 110 → 110 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 110 → 110 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 110 → 110 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 110 → 110 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 110 → 110 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 110 → 110 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 110 → 110 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 110 → 110 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 110 → 110 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 110 → 110 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 6-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 110 → 110 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 6-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 110 → 110 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 7-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 110 → 110 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 7-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 110 → 110 | 0 | 6 → 6 | 0.000 | 0.000 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 24, COMPOSITION_COMPATIBILITY: 21, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 7; mudanças de composição: 1; posicionamento melhorou em 33 ações e piorou em 26.
- Jogador 6 — estado final: ouro 110, nível 6, vida 0.0, colocação 8.
| Jogador 7 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.056 | 0.000 |
| Jogador 7 | 1-2 | 12 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.045 | 0.000 |
| Jogador 7 | 1-3 | 7 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 4 | 2 | 3 → 3 | 0.122 | 0.000 |
| Jogador 7 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 4 → 8 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 7 | 2-1 | 10 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 8 → 12 | 2 | 4 → 4 | 0.001 | 0.269 |
| Jogador 7 | 2-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 12 → 9 | 11 | 4 → 5 | 0.010 | 0.287 |
| Jogador 7 | 2-3 | 12 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 14% → 18% | 9 → 10 | 6 | 5 → 5 | -0.006 | 0.225 |
| Jogador 7 | 2-4 | 8 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 10 → 9 | 8 | 5 → 5 | 0.007 | 0.000 |
| Jogador 7 | 2-5 | 10 | 2.000 | 0.000 | 0 → 0 | 1 → 0 | 18% → 18% | 9 → 7 | 11 | 5 → 6 | -0.065 | 0.246 |
| Jogador 7 | 2-6 | 12 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 21% | 7 → 8 | 9 | 6 → 6 | -0.005 | 0.230 |
| Jogador 7 | 2-7 | 11 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 8 → 10 | 7 | 6 → 6 | 0.007 | 0.000 |
| Jogador 7 | 3-1 | 5 | -2.000 | 8.000 | 0 → 0 | 0 → 0 | 21% → 21% | 10 → 12 | 3 | 6 → 6 | 0.000 | -0.527 |
| Jogador 7 | 3-2 | 5 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 12 → 19 | 0 | 6 → 6 | 0.000 | 0.617 |
| Jogador 7 | 3-3 | 5 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 19 → 28 | 0 | 6 → 6 | 0.000 | 0.597 |
| Jogador 7 | 3-4 | 12 | 8.000 | 4.000 | 0 → 0 | 0 → 1 | 21% → 25% | 28 → 12 | 22 | 6 → 7 | -0.007 | 0.000 |
| Jogador 7 | 3-5 | 12 | 0.000 | 0.000 | 0 → 0 | 1 → 2 | 25% → 25% | 12 → 20 | 5 | 7 → 7 | 0.033 | 0.240 |
| Jogador 7 | 3-6 | 12 | 0.000 | -12.000 | 0 → 0 | 2 → 1 | 25% → 25% | 20 → 33 | 16 | 7 → 7 | 0.000 | -0.223 |
| Jogador 7 | 3-7 | 6 | 0.000 | 14.000 | 0 → 0 | 1 → 2 | 25% → 25% | 33 → 33 | 7 | 7 → 7 | 0.005 | 0.000 |
| Jogador 7 | 4-1 | 12 | 4.000 | 4.000 | 0 → 0 | 2 → 3 | 25% → 25% | 33 → 11 | 30 | 7 → 7 | 0.000 | 0.255 |
| Jogador 7 | 4-2 | 3 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 25% → 25% | 11 → 17 | 2 | 7 → 7 | 0.000 | 0.978 |
| Jogador 7 | 4-3 | 5 | 0.000 | 8.000 | 0 → 0 | 3 → 3 | 25% → 25% | 17 → 21 | 7 | 7 → 7 | 0.000 | 0.577 |
| Jogador 7 | 4-4 | 6 | 0.000 | 22.000 | 0 → 0 | 3 → 6 | 25% → 25% | 21 → 17 | 11 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 4-5 | 10 | 0.000 | 2.000 | 0 → 0 | 6 → 5 | 25% → 25% | 17 → 24 | 11 | 7 → 7 | 0.000 | 0.296 |
| Jogador 7 | 4-6 | 11 | 0.000 | -20.000 | 0 → 0 | 5 → 5 | 25% → 25% | 24 → 45 | 9 | 7 → 7 | 0.000 | 0.269 |
| Jogador 7 | 4-7 | 7 | -2.000 | 18.000 | 0 → 0 | 5 → 5 | 25% → 25% | 45 → 44 | 11 | 7 → 7 | -0.037 | 0.000 |
| Jogador 7 | 5-1 | 12 | -4.000 | 14.000 | 0 → 0 | 5 → 4 | 25% → 21% | 44 → 49 | 15 | 7 → 7 | 0.009 | 0.240 |
| Jogador 7 | 5-2 | 10 | 10.000 | -6.000 | 0 → 0 | 4 → 3 | 21% → 25% | 49 → 57 | 13 | 7 → 7 | -0.022 | 0.301 |
| Jogador 7 | 5-3 | 7 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 25% → 25% | 57 → 68 | 7 | 7 → 7 | 0.000 | 0.429 |
| Jogador 7 | 5-4 | 12 | -6.000 | 2.000 | 0 → 0 | 3 → 2 | 25% → 21% | 68 → 80 | 13 | 7 → 8 | -0.036 | 0.000 |
| Jogador 7 | 5-5 | 11 | 12.000 | -2.000 | 0 → 1 | 2 → 2 | 21% → 25% | 80 → 89 | 15 | 8 → 8 | 0.063 | 0.273 |
| Jogador 7 | 5-6 | 12 | 0.000 | 2.000 | 1 → 1 | 2 → 3 | 25% → 25% | 89 → 102 | 15 | 8 → 8 | 0.000 | 0.242 |
| Jogador 7 | 5-7 | 12 | 0.000 | -2.000 | 1 → 1 | 3 → 2 | 25% → 25% | 102 → 116 | 16 | 8 → 8 | 0.000 | 0.000 |
| Jogador 7 | 6-1 | 11 | 8.000 | 2.000 | 1 → 2 | 2 → 1 | 25% → 29% | 116 → 123 | 13 | 8 → 8 | -0.012 | 0.282 |
| Jogador 7 | 6-2 | 9 | 0.000 | 4.000 | 2 → 2 | 1 → 1 | 29% → 29% | 123 → 134 | 11 | 8 → 8 | 0.000 | 0.000 |
| Jogador 7 | 6-3 | 12 | 0.000 | -4.000 | 2 → 3 | 1 → 0 | 29% → 25% | 134 → 146 | 14 | 8 → 8 | -0.006 | 0.253 |
| Jogador 7 | 6-4 | 12 | 0.000 | 2.000 | 3 → 3 | 0 → 1 | 25% → 25% | 146 → 158 | 14 | 8 → 8 | 0.000 | 0.000 |
| Jogador 7 | 6-5 | 12 | 2.000 | -2.000 | 3 → 3 | 1 → 1 | 25% → 29% | 158 → 172 | 13 | 8 → 8 | 0.003 | 0.254 |
| Jogador 7 | 6-6 | 10 | 0.000 | -4.000 | 3 → 3 | 1 → 1 | 29% → 29% | 172 → 188 | 12 | 8 → 8 | 0.000 | 0.305 |
| Jogador 7 | 6-7 | 10 | 0.000 | 2.000 | 3 → 3 | 1 → 1 | 29% → 29% | 188 → 200 | 15 | 8 → 8 | 0.000 | 0.000 |
| Jogador 7 | 7-1 | 12 | 0.000 | 2.000 | 3 → 3 | 1 → 1 | 29% → 29% | 200 → 213 | 13 | 8 → 8 | 0.000 | 0.257 |
| Jogador 7 | 7-2 | 12 | 0.000 | -4.000 | 3 → 3 | 1 → 1 | 29% → 29% | 213 → 212 | 19 | 8 → 8 | -0.005 | 0.257 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 57, COMPOSITION_COMPATIBILITY: 30, IMMEDIATE_UPGRADE: 7, PAIR_POTENTIAL: 23; mudanças de composição: 1; posicionamento melhorou em 36 ações e piorou em 30.
- Jogador 7 — estado final: ouro 212, nível 8, vida 79.0, colocação 1.
| Jogador 8 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.083 | 0.000 |
| Jogador 8 | 1-2 | 10 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.026 | 0.000 |
| Jogador 8 | 1-3 | 5 | 0.000 | 2.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 4 | 1 | 3 → 3 | 0.000 | 0.000 |
| Jogador 8 | 1-4 | 12 | 2.000 | -2.000 | 0 → 0 | 1 → 0 | 11% → 14% | 4 → 4 | 7 | 3 → 4 | 0.055 | 0.000 |
| Jogador 8 | 2-1 | 8 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 4 → 7 | 2 | 4 → 4 | -0.073 | -0.316 |
| Jogador 8 | 2-2 | 12 | 8.000 | -2.000 | 0 → 0 | 0 → 0 | 14% → 18% | 7 → 6 | 9 | 4 → 5 | 0.064 | 0.220 |
| Jogador 8 | 2-3 | 6 | -2.000 | 10.000 | 0 → 0 | 0 → 0 | 18% → 18% | 6 → 9 | 4 | 5 → 5 | -0.032 | 0.427 |
| Jogador 8 | 2-4 | 7 | 0.000 | 12.000 | 0 → 0 | 0 → 0 | 18% → 18% | 9 → 9 | 6 | 5 → 5 | -0.094 | 0.000 |
| Jogador 8 | 2-5 | 8 | -2.000 | 20.000 | 0 → 0 | 0 → 1 | 18% → 18% | 9 → 5 | 9 | 5 → 5 | -0.066 | -0.289 |
| Jogador 8 | 2-6 | 12 | 2.000 | -8.000 | 0 → 0 | 1 → 2 | 18% → 18% | 5 → 14 | 9 | 5 → 5 | 0.069 | -0.207 |
| Jogador 8 | 2-7 | 12 | 4.000 | 4.000 | 0 → 0 | 2 → 2 | 18% → 18% | 14 → 15 | 9 | 5 → 5 | -0.010 | 0.000 |
| Jogador 8 | 3-1 | 12 | 0.000 | -12.000 | 0 → 0 | 2 → 1 | 18% → 18% | 15 → 30 | 6 | 5 → 5 | -0.007 | -0.219 |
| Jogador 8 | 3-2 | 9 | 2.000 | 10.000 | 0 → 0 | 1 → 1 | 18% → 18% | 30 → 32 | 6 | 5 → 5 | 0.043 | -0.319 |
| Jogador 8 | 3-3 | 7 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 18% → 18% | 32 → 38 | 3 | 5 → 5 | 0.011 | -0.402 |
| Jogador 8 | 3-4 | 6 | 0.000 | 10.000 | 0 → 0 | 1 → 1 | 18% → 18% | 38 → 43 | 5 | 5 → 6 | -0.013 | 0.000 |
| Jogador 8 | 3-5 | 9 | 6.000 | 2.000 | 0 → 0 | 1 → 1 | 18% → 21% | 43 → 50 | 6 | 6 → 6 | 0.017 | -0.308 |
| Jogador 8 | 3-6 | 8 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 21% → 21% | 50 → 60 | 7 | 6 → 6 | -0.083 | -0.335 |
| Jogador 8 | 3-7 | 9 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 60 → 73 | 6 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 4-1 | 12 | 0.000 | -8.000 | 0 → 0 | 1 → 2 | 21% → 21% | 73 → 90 | 8 | 6 → 6 | -0.001 | -0.226 |
| Jogador 8 | 4-2 | 12 | 6.000 | -4.000 | 0 → 0 | 2 → 2 | 21% → 21% | 90 → 102 | 11 | 6 → 6 | 0.000 | -0.233 |
| Jogador 8 | 4-3 | 7 | -34.000 | -46.000 | 0 → 0 | 2 → 0 | 21% → 0% | 102 → 96 | 8 | 6 → 6 | 0.080 | -0.388 |
| Jogador 8 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 96 → 96 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 4-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 96 → 96 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 96 → 96 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 96 → 96 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 96 → 96 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 96 → 96 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 96 → 96 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 96 → 96 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 96 → 96 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 96 → 96 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 96 → 96 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 96 → 96 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 96 → 96 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 96 → 96 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 96 → 96 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 96 → 96 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 6-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 96 → 96 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 6-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 96 → 96 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 7-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 96 → 96 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 7-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 96 → 96 | 0 | 6 → 6 | 0.000 | 0.000 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 23, COMPOSITION_COMPATIBILITY: 17, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 8; mudanças de composição: 1; posicionamento melhorou em 29 ações e piorou em 30.
- Jogador 8 — estado final: ouro 96, nível 6, vida 0.0, colocação 7.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Revertidas ≤1 ação | ≤2 ações | ≤4 ações | Ouro perdido | Upgrades | Vendas core/par | Valor médio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 73 | 43 | 2 | 3 | 3 | 0 | 7 | 8 | 3.2842 |
| Jogador 2 | 63 | 42 | 7 | 7 | 12 | 0 | 3 | 5 | 2.4686 |
| Jogador 3 | 26 | 8 | 0 | 0 | 0 | 0 | 2 | 3 | 2.83 |
| Jogador 4 | 76 | 52 | 1 | 2 | 5 | 0 | 5 | 3 | 1.9589 |
| Jogador 5 | 56 | 33 | 3 | 4 | 5 | 0 | 4 | 3 | 1.1246 |
| Jogador 6 | 54 | 36 | 0 | 0 | 0 | 0 | 2 | 4 | 1.1696 |
| Jogador 7 | 117 | 89 | 1 | 1 | 3 | 0 | 7 | 16 | 1.5087 |
| Jogador 8 | 50 | 32 | 2 | 2 | 3 | 0 | 2 | 2 | 1.7209 |

Vendas de core/pares ignoradas antes da decisão da composição: **10**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Uma venda sem compra correspondente na janela é UNKNOWN; sequências ambíguas não são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| MEDIUM | Jogador 1 | 1-1 | 3 | PURCHASE_REVERSED | Compra de DA_18_Veigar desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 1-1 | 5 | PURCHASE_REVERSED | Compra de DA_Karma18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 1 | 3-2 | 298 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sejuani' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 1 | 3-4 | 325 | SOLD_CORE_UNIT | Venda de 'DA_18_Diana' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 1 | 3-5 | 344 | PURCHASE_REVERSED | Compra de DA_Vi18 desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 1 | 3-7 | 386 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Diana' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 1 | 3-7 | 387 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 1 | 4-7 | 514 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 1 | 5-1 | 532 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 1 | 5-2 | 549 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Krug18' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 1 | 6-4 | 681 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Krug18' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 2 | 1-1 | 3 | PURCHASE_REVERSED | Compra de DA_Karma18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 2 | 2-5 | 206 | SOLD_CORE_UNIT | Venda de 'DA_18_Yunara' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 2 | 3-2 | 293 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 2 | 3-3 | 308 | PURCHASE_REVERSED | Compra de DA_18_Tristana desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 3-4 | 324 | PURCHASE_REVERSED | Compra de DA_18_Shen desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 3-4 | 327 | PURCHASE_REVERSED | Compra de DA_18_Elise desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 3-5 | 343 | PURCHASE_REVERSED | Compra de DA_18_Rammus desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 3-5 | 349 | PURCHASE_REVERSED | Compra de DA_18_Teemo desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 3-5 | 351 | PURCHASE_REVERSED | Compra de DA_18_Sentry desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 3-6 | 367 | PURCHASE_REVERSED | Compra de DA_CrimsonRaptor18 desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 2 | 3-6 | 369 | SOLD_CORE_UNIT | Venda de 'DA_Nidalee18_AP' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 2 | 3-7 | 386 | PURCHASE_REVERSED | Compra de DA_18_Tristana desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 4-1 | 404 | PURCHASE_REVERSED | Compra de DA_18_Rammus desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 4-1 | 405 | PURCHASE_REVERSED | Compra de DA_18_Ezreal desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 4-3 | 442 | PURCHASE_REVERSED | Compra de DA_Krug18 desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 2 | 4-3 | 443 | SOLD_CORE_UNIT | Venda de 'DA_Gromp18_AP' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 2 | 5-5 | 594 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 2 | 6-4 | 694 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Sejuani' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 2 | 6-4 | 694 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Alune' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 2 | 6-4 | 694 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Lux_Sunbeam' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 3 | 2-5 | 208 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 3 | 2-5 | 211 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 3 | 3-2 | 293 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Akali_AD' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 3 | 4-7 | 530 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Scuttlecrab18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 3 | 4-7 | 530 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_KhaZix' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 3 | 4-7 | 530 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Sivir' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 4 | 3-2 | 294 | PURCHASE_REVERSED | Compra de DA_18_Camille desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 4 | 3-2 | 295 | PURCHASE_REVERSED | Compra de DA_Cinderling18 desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 4 | 3-3 | 312 | PURCHASE_REVERSED | Compra de DA_18_Yunara desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 4 | 3-7 | 389 | PURCHASE_REVERSED | Compra de DA_18_Rakan desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 4 | 3-7 | 390 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_MasterYi_AD' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 4 | 4-1 | 411 | PURCHASE_REVERSED | Compra de DA_18_Rakan desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 4 | 4-2 | 430 | SOLD_CORE_UNIT | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 4 | 4-5 | 484 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yunara' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 4 | 5-2 | 561 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Fiddlesticks18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 4 | 5-2 | 561 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Xayah' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 4 | 5-2 | 561 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Aphelios' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 5 | 2-1 | 112 | PURCHASE_REVERSED | Compra de DA_18_LeBlanc desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-1 | 115 | PURCHASE_REVERSED | Compra de DA_18_Veigar desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-6 | 233 | PURCHASE_REVERSED | Compra de DA_18_Camille desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 3-2 | 293 | PURCHASE_REVERSED | Compra de DA_18_Shen desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 5 | 3-5 | 342 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Gromp18_AP' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 5 | 3-6 | 364 | PURCHASE_REVERSED | Compra de DA_18_Teemo desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 5 | 3-6 | 365 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rammus' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 5 | 3-6 | 366 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 5 | 5-3 | 578 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Tristana' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 5 | 5-3 | 578 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_MasterYi_AD' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 5 | 5-3 | 578 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Rammus' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 6 | 2-6 | 232 | SOLD_CORE_UNIT | Venda de 'DA_18_Teemo' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 2-6 | 234 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 3-4 | 324 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yunara' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 3-7 | 383 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Kobuko' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 6 | 4-4 | 480 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Rammus' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 6 | 4-4 | 480 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Sentinel18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 6 | 4-4 | 480 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Teemo' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| HIGH | Jogador 7 | 2-5 | 209 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Alistar' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 7 | 2-6 | 232 | PURCHASE_REVERSED | Compra de DA_18_LeBlanc desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 7 | 3-5 | 350 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Alistar' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 7 | 3-6 | 365 | PURCHASE_REVERSED | Compra de DA_18_Morgana desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 7 | 3-6 | 366 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Diana' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 7 | 3-6 | 369 | PURCHASE_REVERSED | Compra de DA_18_Ezreal desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 7 | 3-6 | 370 | SOLD_CORE_UNIT | Venda de 'DA_18_Aphelios' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 7 | 3-6 | 371 | SOLD_CORE_UNIT | Venda de 'DA_18_Aphelios' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 7 | 4-5 | 483 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 7 | 4-6 | 502 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 7 | 5-1 | 536 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 7 | 5-2 | 553 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 7 | 5-4 | 584 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_CrimsonRaptor18' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 7 | 5-7 | 624 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Brambleback18' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 7 | 6-3 | 671 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_CrimsonRaptor18' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 7 | 6-5 | 697 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Brambleback18' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 7 | 6-5 | 699 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_CrimsonRaptor18' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 7 | 6-6 | 711 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_CrimsonRaptor18' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 7 | 6-7 | 724 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 8 | 1-4 | 86 | PURCHASE_REVERSED | Compra de DA_18_Xayah desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 1-4 | 87 | PURCHASE_REVERSED | Compra de DA_18_Xayah desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 3-1 | 274 | PURCHASE_REVERSED | Compra de DA_18_Elise desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 8 | 3-1 | 275 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 8 | 3-1 | 276 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Warwick' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 8 | 4-4 | 480 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Tristana' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 8 | 4-4 | 480 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Sivir' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 8 | 4-4 | 480 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Diana' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- O JSON estruturado é a fonte primária para estado de decisão, máscaras, política e recompensas; .tft é analisado apenas para jogadores sem sidecar JSON.- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
