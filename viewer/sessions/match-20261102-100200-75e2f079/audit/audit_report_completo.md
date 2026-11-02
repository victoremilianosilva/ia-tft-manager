# Auditoria da partida TFT

- Arquivos lidos: **8**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **3847**
- Achados: **12**
- CRITICAL: 0 | HIGH: 6 | MEDIUM: 6 | LOW: 0

- Decisões analisadas enquanto os jogadores estavam vivos: **3022**
- Entradas posteriores à eliminação ignoradas: **825**
- A ação que causa a eliminação permanece válida; o estado terminal não é usado como economia final.

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 111 | 111 | 111 | 0 | 107 | 0 | 111 | 111 | 111 | 19/7 |
| Jogador 2 | 143 | 143 | 143 | 0 | 137 | 0 | 143 | 143 | 143 | 20/9 |
| Jogador 3 | 91 | 91 | 91 | 0 | 89 | 0 | 91 | 91 | 91 | 11/1 |
| Jogador 4 | 131 | 131 | 131 | 0 | 125 | 0 | 131 | 131 | 131 | 22/8 |
| Jogador 5 | 81 | 81 | 81 | 0 | 80 | 0 | 81 | 81 | 81 | 11/2 |
| Jogador 6 | 65 | 65 | 65 | 0 | 65 | 0 | 65 | 65 | 65 | 9/2 |
| Jogador 7 | 79 | 79 | 79 | 0 | 77 | 0 | 79 | 79 | 79 | 11/2 |
| Jogador 8 | 100 | 100 | 100 | 0 | 98 | 0 | 100 | 100 | 100 | 14/3 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5151995420455933 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.23749256134033203 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 28 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.298336386680603 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31793826818466187 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | -0.2122882902622223 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 31 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 55 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.21527843177318573 | 0.0 | 0.0 | +24247863-54d4-4674-86e9-9a45609a440e / -— |
| Jogador 1 | 1-3 | 56 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.284513384103775 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 57 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 82 | PASS | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 112 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.083440862596035 | 0.0 | 0.0 | +3a74be8d-bf7c-4449-9f1b-d76521e73e6f / -— |
| Jogador 1 | 2-1 | 113 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21305309236049652 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 114 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4024493396282196 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 115 | BUY_XP | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 116 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 138 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0183663368225098 | 0.0 | 0.0 | +7aea963f-f0a4-4fa2-8da0-cc5eb260f665 / -— |
| Jogador 1 | 2-2 | 139 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 140 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2228272259235382 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 141 | PASS | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 164 | SELL | STABILIZE | 94.0 | 4 | 11 | 1 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4277545213699341 | 0.0 | 0.0 | +— / -24247863-54d4-4674-86e9-9a45609a440e |
| Jogador 1 | 2-3 | 165 | BUY | STABILIZE | 94.0 | 4 | 13 | 1 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.113450288772583 | 0.0 | 0.0 | +ff10e482-7085-4e73-8a0c-fdd3f4938128 / -3a74be8d-bf7c-4449-9f1b-d76521e73e6f,7aea963f-f0a4-4fa2-8da0-cc5eb260f665 |
| Jogador 1 | 2-3 | 166 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 11 | 1 | 4.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.153359055519104 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 167 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 11 | 1 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2690463662147522 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 168 | BUY | STABILIZE | 94.0 | 4 | 11 | 1 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.269020676612854 | 0.0 | 0.0 | +73185d11-22d3-4a1d-803a-b37e82272098 / -— |
| Jogador 1 | 2-3 | 169 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 9 | 0 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5346230268478394 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 170 | BUY_XP | STABILIZE | 94.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0403750017285347 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 171 | BUY_XP | SLOWROLL | 94.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.17800000309944153 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 172 | MOVE_BOARD | SLOWROLL | 94.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Sejuani | BUY, MOVE_BOARD, PASS | True | True | 0.04875248298048973 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 173 | PASS | SLOWROLL | 94.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Sejuani | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 189 | BUY | SLOWROLL | 89.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.29823264479637146 | 0.0 | 0.0 | +d01cae02-d8ba-491e-841f-bf3120953933 / -— |
| Jogador 1 | 2-4 | 190 | MOVE_BENCH | SLOWROLL | 89.0 | 5 | 4 | 0 | 16.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8184829950332642 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 191 | BUY_XP | SLOWROLL | 89.0 | 5 | 4 | 0 | 22.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 192 | PASS | SLOWROLL | 89.0 | 5 | 0 | 0 | 22.0 | —/DA_18_Sejuani | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 212 | BUY | SLOWROLL | 89.0 | 5 | 6 | 0 | 22.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9661996364593506 | 0.0 | 0.0 | +f44d5eea-6187-4ea9-ab49-79077393b7de / -— |
| Jogador 1 | 2-5 | 213 | BUY_XP | SLOWROLL | 89.0 | 5 | 4 | 0 | 22.0 | Defendente/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 214 | MOVE_BOARD | SLOWROLL | 89.0 | 5 | 0 | 0 | 22.0 | Defendente/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23413696885108948 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 215 | MOVE_BOARD | SLOWROLL | 89.0 | 5 | 0 | 0 | 22.0 | Defendente/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09808357805013657 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 216 | PASS | SLOWROLL | 89.0 | 5 | 0 | 0 | 22.0 | Defendente/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 236 | MOVE_BENCH | SLOWROLL | 83.0 | 6 | 6 | 0 | 22.0 | Defendente/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0002918661630246788 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 237 | MOVE_BENCH | SLOWROLL | 83.0 | 6 | 6 | 0 | 18.0 | Defendente/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5310449004173279 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 238 | BUY | FAST8 | 83.0 | 6 | 6 | 0 | 26.0 | Defendente/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.965160608291626 | 0.0 | 0.0 | +2fd4f2d8-6e40-439a-a96d-3e49e05779ad / -— |
| Jogador 1 | 2-6 | 239 | PASS | FAST8 | 83.0 | 6 | 3 | 0 | 26.0 | Defendente/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 262 | BUY_XP | FAST8 | 83.0 | 6 | 9 | 0 | 26.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 263 | BUY_XP | FAST8 | 83.0 | 6 | 5 | 0 | 26.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 264 | PASS | FAST8 | 83.0 | 6 | 1 | 0 | 26.0 | Inferno/DA_18_Sejuani | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 289 | BUY_XP | FAST8 | 83.0 | 6 | 6 | 0 | 26.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 290 | PASS | FAST8 | 83.0 | 6 | 2 | 0 | 26.0 | Inferno/DA_18_Sejuani | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 312 | BUY_XP | FAST8 | 83.0 | 6 | 9 | 0 | 26.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 313 | BUY_XP | FAST8 | 83.0 | 6 | 5 | 0 | 26.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 314 | PASS | FAST8 | 83.0 | 6 | 1 | 0 | 26.0 | Inferno/DA_18_Sejuani | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 338 | BUY_XP | FAST8 | 83.0 | 6 | 8 | 0 | 26.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 339 | BUY_XP | FAST8 | 83.0 | 6 | 4 | 0 | 26.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08860000222921371 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 340 | MOVE_BENCH | FAST8 | 83.0 | 7 | 0 | 0 | 26.0 | Inferno/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4055789113044739 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 341 | PASS | FAST8 | 83.0 | 7 | 0 | 0 | 32.0 | Inferno/DA_18_Sejuani | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 362 | PASS | FAST8 | 83.0 | 7 | 7 | 0 | 32.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 384 | BUY | FAST8 | 83.0 | 7 | 13 | 1 | 32.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7659604549407959 | 0.0 | 0.0 | +9aa6122c-e49a-48a2-ba24-7adcd3b7cb56 / -73185d11-22d3-4a1d-803a-b37e82272098,f44d5eea-6187-4ea9-ab49-79077393b7de |
| Jogador 1 | 3-5 | 385 | MOVE_BENCH | STABILIZE | 83.0 | 7 | 11 | 1 | 24.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5331472754478455 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 386 | BUY | FAST8 | 83.0 | 7 | 11 | 1 | 32.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.16279558837413788 | 0.0 | 0.0 | +727765c8-7f02-491e-a6da-12b0dab59f6d / -— |
| Jogador 1 | 3-5 | 387 | BUY_XP | FAST8 | 83.0 | 7 | 8 | 0 | 32.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 388 | BUY_XP | FAST8 | 83.0 | 7 | 4 | 0 | 32.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 389 | MOVE_BENCH | FAST8 | 83.0 | 7 | 0 | 0 | 32.0 | Inferno/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2825818955898285 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 390 | MOVE_BENCH | FAST8 | 83.0 | 7 | 0 | 0 | 32.0 | Inferno/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9985873103141785 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 391 | PASS | FAST8 | 83.0 | 7 | 0 | 0 | 30.0 | Inferno/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 401 | MOVE_BENCH | FAST8 | 83.0 | 7 | 0 | 0 | 30.0 | Inferno/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6685819625854492 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 405 | BUY | FAST8 | 72.0 | 7 | 5 | 0 | 38.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.21597982943058014 | 0.0 | 0.0 | +9d94c68e-2af2-49f8-a7ab-8a7f3b8e08d8 / -— |
| Jogador 1 | 3-6 | 406 | MOVE_BENCH | FAST8 | 72.0 | 7 | 3 | 0 | 38.0 | Inferno/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029191622510552406 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 407 | PASS | FAST8 | 72.0 | 7 | 3 | 0 | 36.0 | Inferno/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 425 | BUY | FAST8 | 72.0 | 7 | 9 | 0 | 36.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7635959386825562 | 0.0 | 0.0 | +227dbcdb-af5c-4318-94d1-f01a7847d100 / -2fd4f2d8-6e40-439a-a96d-3e49e05779ad,d01cae02-d8ba-491e-841f-bf3120953933 |
| Jogador 1 | 3-7 | 426 | MOVE_BENCH | STABILIZE | 72.0 | 7 | 6 | 0 | 24.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24974578619003296 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 427 | MOVE_BENCH | FAST8 | 72.0 | 7 | 6 | 0 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.330080509185791 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 428 | MOVE_BENCH | FAST8 | 72.0 | 7 | 6 | 0 | 38.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14523598551750183 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 429 | MOVE_BENCH | FAST8 | 72.0 | 7 | 6 | 0 | 30.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.046363234519958496 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 430 | BUY_XP | FAST8 | 72.0 | 7 | 6 | 0 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 431 | MOVE_BOARD | FAST8 | 72.0 | 7 | 2 | 0 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17594940960407257 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 432 | PASS | FAST8 | 72.0 | 7 | 2 | 0 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 441 | MOVE_BENCH | FAST8 | 72.0 | 7 | 2 | 0 | 36.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41801685094833374 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 445 | CRAFT_AND_EQUIP | FAST8 | 72.0 | 7 | 7 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS, CRAFT_AND_EQUIP | True | — | 0.12902489304542542 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 446 | BUY | FAST8 | 72.0 | 7 | 7 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.49997416138648987 | 0.0 | 0.0 | +844f869e-0e0e-423a-8507-27efd66131f5 / -— |
| Jogador 1 | 4-1 | 447 | BUY_XP | FAST8 | 72.0 | 7 | 4 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 448 | PASS | FAST8 | 72.0 | 7 | 0 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 465 | BUY_XP | FAST8 | 72.0 | 7 | 7 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 466 | PASS | FAST8 | 72.0 | 7 | 3 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 485 | BUY_XP | FAST8 | 60.0 | 7 | 8 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 486 | BUY_XP | FAST8 | 60.0 | 7 | 4 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 487 | PASS | FAST8 | 60.0 | 7 | 0 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 506 | BUY_XP | FAST8 | 49.0 | 7 | 6 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 507 | PASS | FAST8 | 49.0 | 7 | 2 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 527 | BUY_XP | FAST8 | 49.0 | 7 | 8 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 528 | BUY_XP | FAST8 | 49.0 | 7 | 4 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08269374817609787 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 529 | MOVE_BENCH | ECON | 49.0 | 8 | 0 | 0 | 42.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13475874066352844 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 530 | PASS | ECON | 49.0 | 8 | 0 | 0 | 48.0 | Inferno/DA_KogMaw18_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 543 | BUY | ECON | 49.0 | 8 | 6 | 0 | 48.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.1409652680158615 | 0.0 | 0.0 | +4c1dab77-0e6d-401b-a341-40117b445957 / -— |
| Jogador 1 | 4-6 | 544 | PASS | ECON | 49.0 | 8 | 2 | 0 | 48.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 562 | BUY | ECON | 49.0 | 8 | 9 | 0 | 48.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21158292889595032 | 0.0 | 0.0 | +6ea982ab-292d-42fc-99e6-d67c89f9f4fe / -— |
| Jogador 1 | 4-7 | 563 | BUY_XP | ECON | 49.0 | 8 | 5 | 0 | 48.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 564 | PASS | ECON | 49.0 | 8 | 1 | 0 | 48.0 | Inferno/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 582 | ANVIL_CHOICE | ECON | 49.0 | 8 | 7 | 0 | 48.0 | Inferno/DA_KogMaw18_AD | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 583 | BUY | ECON | 49.0 | 8 | 7 | 0 | 48.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21383365988731384 | 0.0 | 0.0 | +aaebedb3-18bf-4ae6-948e-7b326b573f1c / -— |
| Jogador 1 | 5-1 | 584 | PASS | ECON | 49.0 | 8 | 4 | 0 | 48.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 602 | PASS | ECON | 49.0 | 8 | 10 | 1 | 48.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 622 | BUY | STABILIZE | 34.0 | 8 | 16 | 1 | 48.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8600475788116455 | 0.0 | 0.0 | +7a48aa2d-a43b-4e49-8230-77f4f2860cb2 / -— |
| Jogador 1 | 5-3 | 623 | PASS | STABILIZE | 34.0 | 8 | 12 | 1 | 48.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 642 | PASS | STABILIZE | 34.0 | 8 | 19 | 1 | 48.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1250961869955063 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 662 | PASS | STABILIZE | 34.0 | 8 | 25 | 2 | 48.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13411270081996918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 682 | PASS | STABILIZE | 19.0 | 8 | 32 | 3 | 48.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2321430742740631 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 702 | PASS | ALL_IN | 2.0 | 8 | 41 | 4 | 48.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3360174596309662 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 722 | ANVIL_CHOICE | ALL_IN | 2.0 | 8 | 51 | 5 | 48.0 | Inferno/DA_KogMaw18_AD | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 723 | EQUIP_FROM_INVENTORY | ALL_IN | 2.0 | 8 | 51 | 5 | 48.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.05595584958791733 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 724 | BUY | ALL_IN | 2.0 | 8 | 51 | 5 | 48.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0375893115997314 | 0.0 | 0.0 | +54574f38-262f-44ac-83da-03088b8bdea3 / -— |
| Jogador 1 | 6-1 | 725 | PASS | ALL_IN | 2.0 | 8 | 49 | 4 | 48.0 | Inferno/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.368876188993454 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.01586153917014599 | 0.0 | 0.0 | +— / -fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3124316334724426 | 0.0 | 0.0 | +292ef825-d326-4dd8-9c42-c47cfc62116f / -— |
| Jogador 2 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.5974857807159424 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0390512943267822 | 0.0 | 0.0 | +94ede66e-59bc-4c41-aabf-f64372e20f9a / -— |
| Jogador 2 | 1-2 | 28 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.35926106572151184 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 30 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 55 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.1336853951215744 | 0.0 | 0.0 | +de00430a-8a57-423c-887c-317d53c2cdd3 / -— |
| Jogador 2 | 1-3 | 56 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21953977644443512 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 57 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46338286995887756 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 58 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 82 | PASS | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 112 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3188048303127289 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 113 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 8.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44037294387817383 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 114 | BUY_XP | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 115 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 14.0 | —/DA_Vi18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 138 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 14.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0403750017285347 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 139 | BUY | SLOWROLL | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_Vi18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.038872815668582916 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 140 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3064689636230469 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 141 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 1 | 0 | 12.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3062528967857361 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 142 | PASS | SLOWROLL | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 159 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 1 | 0 | 14.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17107005417346954 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 164 | BUY | SLOWROLL | 100.0 | 5 | 8 | 0 | 18.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.24767930805683136 | 0.0 | 0.0 | +8c364966-f97c-4f54-b087-ddd182a9f8ea / -— |
| Jogador 2 | 2-3 | 165 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 5 | 0 | 18.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07599292695522308 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 166 | BUY_XP | SLOWROLL | 100.0 | 5 | 5 | 0 | 20.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 167 | MOVE_BOARD | SLOWROLL | 100.0 | 5 | 1 | 0 | 20.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024840479716658592 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 168 | PASS | SLOWROLL | 100.0 | 5 | 1 | 0 | 20.0 | —/DA_Vi18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 189 | BUY_XP | SLOWROLL | 100.0 | 5 | 8 | 0 | 20.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 190 | BUY_XP | SLOWROLL | 100.0 | 5 | 4 | 0 | 20.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 191 | PASS | SLOWROLL | 100.0 | 5 | 0 | 0 | 20.0 | —/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 212 | BUY_XP | SLOWROLL | 100.0 | 5 | 6 | 0 | 20.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011409999802708626 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 213 | MOVE_BENCH | SLOWROLL | 100.0 | 6 | 2 | 0 | 20.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4464481770992279 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 214 | PASS | SLOWROLL | 100.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 236 | BUY | SLOWROLL | 100.0 | 6 | 9 | 0 | 24.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.964647114276886 | 0.0 | 0.0 | +6f3f86ec-6928-4032-a1ef-533a68865516 / -— |
| Jogador 2 | 2-6 | 237 | MOVE_BENCH | SLOWROLL | 100.0 | 6 | 6 | 0 | 24.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 238 | MOVE_BENCH | SLOWROLL | 100.0 | 6 | 6 | 0 | 24.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02349487878382206 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 239 | BUY_XP | FAST8 | 100.0 | 6 | 6 | 0 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 240 | PASS | FAST8 | 100.0 | 6 | 2 | 0 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 262 | BUY_XP | FAST8 | 100.0 | 6 | 10 | 1 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 263 | BUY_XP | FAST8 | 100.0 | 6 | 6 | 0 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 264 | PASS | FAST8 | 100.0 | 6 | 2 | 0 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 289 | BUY_XP | FAST8 | 100.0 | 6 | 9 | 0 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 290 | BUY_XP | FAST8 | 100.0 | 6 | 5 | 0 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 291 | PASS | FAST8 | 100.0 | 6 | 1 | 0 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 312 | BUY_XP | FAST8 | 100.0 | 6 | 10 | 1 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 313 | BUY_XP | FAST8 | 100.0 | 6 | 6 | 0 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07689999788999557 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 314 | MOVE_BENCH | FAST8 | 100.0 | 7 | 2 | 0 | 26.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32382357120513916 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 315 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 2 | 0 | 24.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35604196786880493 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 316 | PASS | FAST8 | 100.0 | 7 | 2 | 0 | 28.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 331 | MOVE_BENCH | FAST8 | 100.0 | 7 | 2 | 0 | 28.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5461198091506958 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 338 | BUY | FAST8 | 100.0 | 7 | 11 | 1 | 30.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1255544126033783 | 0.0 | 0.0 | +3880fbd9-322b-4375-b855-fbb779a0cb47 / -— |
| Jogador 2 | 3-3 | 339 | MOVE_BENCH | FAST8 | 100.0 | 7 | 7 | 0 | 30.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14571718871593475 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 340 | SELL | FAST8 | 100.0 | 7 | 7 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008493784815073013 | 0.0 | 0.0 | +— / -561fb9a8-e987-4935-b11c-6c6104ced65d |
| Jogador 2 | 3-3 | 341 | BUY | FAST8 | 100.0 | 7 | 9 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.20345762372016907 | 0.0 | 0.0 | +4e116bc2-f686-4a17-adb1-a7b80865c159 / -— |
| Jogador 2 | 3-3 | 342 | BUY_XP | FAST8 | 100.0 | 7 | 5 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 343 | MOVE_BOARD | FAST8 | 100.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_Amumu18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010701649822294712 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 344 | MOVE_BOARD | FAST8 | 100.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_Amumu18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.047093361616134644 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 345 | PASS | FAST8 | 100.0 | 7 | 1 | 0 | 34.0 | Colosso/DA_Amumu18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 362 | BUY_XP | FAST8 | 100.0 | 7 | 10 | 1 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 363 | BUY_XP | FAST8 | 100.0 | 7 | 6 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 364 | PASS | FAST8 | 100.0 | 7 | 2 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 384 | BUY_XP | FAST8 | 100.0 | 7 | 10 | 1 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 385 | BUY_XP | FAST8 | 100.0 | 7 | 6 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 386 | PASS | FAST8 | 100.0 | 7 | 2 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 405 | SELL | FAST8 | 100.0 | 7 | 11 | 1 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47464242577552795 | 0.0 | 0.0 | +— / -4e116bc2-f686-4a17-adb1-a7b80865c159 |
| Jogador 2 | 3-6 | 406 | BUY | FAST8 | 100.0 | 7 | 15 | 1 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2023088037967682 | 0.0 | 0.0 | +23157bd6-5e8f-4416-bb7f-2e5d71a06543 / -— |
| Jogador 2 | 3-6 | 407 | BUY_XP | FAST8 | 100.0 | 7 | 11 | 1 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 408 | BUY_XP | FAST8 | 100.0 | 7 | 7 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 409 | PASS | FAST8 | 100.0 | 7 | 3 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 425 | BUY_XP | FAST8 | 100.0 | 7 | 12 | 1 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 426 | BUY_XP | FAST8 | 100.0 | 7 | 8 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 427 | BUY_XP | FAST8 | 100.0 | 7 | 4 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 428 | PASS | FAST8 | 100.0 | 7 | 0 | 0 | 34.0 | Colosso/DA_Amumu18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 445 | BUY_XP | FAST8 | 100.0 | 7 | 8 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0853937491774559 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 446 | MOVE_BENCH | ECON | 100.0 | 8 | 4 | 0 | 34.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6816802620887756 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 447 | BUY | WINSTREAK | 100.0 | 8 | 4 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.2873739004135132 | 0.0 | 0.0 | +59304448-26ee-4e38-a52e-014e22ece127 / -— |
| Jogador 2 | 4-1 | 448 | PASS | WINSTREAK | 100.0 | 8 | 0 | 0 | 42.0 | Colosso/DA_Amumu18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 465 | SELL | WINSTREAK | 100.0 | 8 | 9 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2746615409851074 | 0.0 | 0.0 | +— / -59304448-26ee-4e38-a52e-014e22ece127 |
| Jogador 2 | 4-2 | 466 | BUY | WINSTREAK | 100.0 | 8 | 13 | 1 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.16872823238372803 | 0.0 | 0.0 | +3fdd5708-2e07-4636-a598-d872f57e1c16 / -— |
| Jogador 2 | 4-2 | 467 | BUY_XP | WINSTREAK | 100.0 | 8 | 9 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 468 | BUY_XP | WINSTREAK | 100.0 | 8 | 5 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 469 | PASS | WINSTREAK | 100.0 | 8 | 1 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 485 | BUY_XP | WINSTREAK | 100.0 | 8 | 10 | 1 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 486 | BUY_XP | WINSTREAK | 100.0 | 8 | 6 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 487 | PASS | WINSTREAK | 100.0 | 8 | 2 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 506 | PASS | WINSTREAK | 100.0 | 8 | 11 | 1 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 527 | BUY_XP | WINSTREAK | 100.0 | 8 | 20 | 2 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 528 | BUY_XP | WINSTREAK | 100.0 | 8 | 16 | 1 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 529 | BUY_XP | WINSTREAK | 100.0 | 8 | 12 | 1 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 530 | BUY_XP | WINSTREAK | 100.0 | 8 | 8 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 531 | BUY_XP | WINSTREAK | 100.0 | 8 | 4 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 532 | PASS | WINSTREAK | 100.0 | 8 | 0 | 0 | 42.0 | Colosso/DA_Amumu18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 543 | BUY_XP | ECON | 88.0 | 8 | 5 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 544 | PASS | ECON | 88.0 | 8 | 1 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 562 | BUY_XP | ECON | 76.0 | 8 | 7 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 563 | PASS | ECON | 76.0 | 8 | 3 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 582 | ANVIL_CHOICE | ECON | 76.0 | 8 | 9 | 0 | 42.0 | Colosso/DA_Amumu18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 583 | BUY_XP | ECON | 76.0 | 8 | 9 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.002374999923631549 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 584 | BUY_XP | ECON | 76.0 | 8 | 5 | 0 | 42.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05848750099539757 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 585 | CRAFT_AND_EQUIP | ECON | 76.0 | 9 | 1 | 0 | 42.0 | Colosso/DA_Amumu18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.05668513476848602 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 586 | PASS | ECON | 76.0 | 9 | 1 | 0 | 42.0 | Colosso/DA_Amumu18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 600 | MOVE_BENCH | ECON | 76.0 | 9 | 1 | 0 | 42.0 | Colosso/DA_Amumu18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49353882670402527 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 602 | BUY | ECON | 76.0 | 9 | 7 | 0 | 50.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.026282761245965958 | 0.0 | 0.0 | +89ef75a2-6ac2-4c6c-b2b8-492aec985a01 / -— |
| Jogador 2 | 5-2 | 603 | PASS | ECON | 76.0 | 9 | 2 | 0 | 50.0 | Colosso/DA_18_Ashe | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 622 | SELL | ECON | 76.0 | 9 | 9 | 0 | 50.0 | Colosso/DA_18_Ashe | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3772202730178833 | 0.0 | 0.0 | +— / -89ef75a2-6ac2-4c6c-b2b8-492aec985a01 |
| Jogador 2 | 5-3 | 623 | BUY | ECON | 76.0 | 9 | 14 | 1 | 50.0 | Colosso/DA_Amumu18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8200662136077881 | 0.0 | 0.0 | +7313188a-ce84-4a52-b2d0-a94b2c420cdb / -6f3f86ec-6928-4032-a1ef-533a68865516,8c364966-f97c-4f54-b087-ddd182a9f8ea |
| Jogador 2 | 5-3 | 624 | MOVE_BENCH | ECON | 76.0 | 9 | 11 | 1 | 38.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5453389883041382 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 625 | BUY | ECON | 76.0 | 9 | 11 | 1 | 50.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09406352788209915 | 0.0 | 0.0 | +4688e6f1-26c5-402d-8d27-0f9bce3a9681 / -— |
| Jogador 2 | 5-3 | 626 | BUY_XP | ECON | 76.0 | 9 | 7 | 0 | 50.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 627 | PASS | ECON | 76.0 | 9 | 3 | 0 | 50.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 642 | BUY | WINSTREAK | 76.0 | 9 | 10 | 1 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.23504231870174408 | 0.0 | 0.0 | +ad363fca-33b7-4257-99d6-7093df66caf6 / -— |
| Jogador 2 | 5-4 | 643 | BUY_XP | WINSTREAK | 76.0 | 9 | 7 | 0 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 644 | PASS | WINSTREAK | 76.0 | 9 | 3 | 0 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 662 | PASS | WINSTREAK | 76.0 | 9 | 9 | 0 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 682 | PASS | WINSTREAK | 76.0 | 9 | 17 | 1 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08957143127918243 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 702 | BUY | WINSTREAK | 76.0 | 9 | 26 | 2 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8578424453735352 | 0.0 | 0.0 | +0c5adb43-b194-486e-b59c-c0f3b5479d40 / -— |
| Jogador 2 | 5-7 | 703 | PASS | WINSTREAK | 76.0 | 9 | 22 | 2 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09350000321865082 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 722 | ANVIL_CHOICE | WINSTREAK | 76.0 | 9 | 31 | 3 | 58.0 | Colosso/DA_18_MasterYi_AD | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 723 | EQUIP_FROM_INVENTORY | WINSTREAK | 76.0 | 9 | 31 | 3 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.13128811120986938 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 724 | PASS | WINSTREAK | 76.0 | 9 | 31 | 3 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1817142814397812 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 742 | PASS | WINSTREAK | 76.0 | 9 | 41 | 4 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19028571248054504 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 762 | BUY | ECON | 59.0 | 9 | 50 | 5 | 58.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 1.0816560983657837 | 0.0 | 0.0 | +b311d350-7bab-48ee-9833-0883606b4a2f / -0c5adb43-b194-486e-b59c-c0f3b5479d40,4688e6f1-26c5-402d-8d27-0f9bce3a9681 |
| Jogador 2 | 6-3 | 763 | BUY_XP | ECON | 59.0 | 9 | 46 | 4 | 50.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 764 | BUY_XP | ECON | 59.0 | 9 | 42 | 4 | 50.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 765 | BUY_XP | ECON | 59.0 | 9 | 38 | 3 | 50.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 766 | BUY_XP | ECON | 59.0 | 9 | 34 | 3 | 50.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 767 | BUY_XP | ECON | 59.0 | 9 | 30 | 3 | 50.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 768 | BUY_XP | ECON | 59.0 | 9 | 26 | 2 | 50.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 769 | BUY_XP | ECON | 59.0 | 9 | 22 | 2 | 50.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 770 | BUY_XP | ECON | 59.0 | 9 | 18 | 1 | 50.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 771 | BUY_XP | ECON | 59.0 | 9 | 14 | 1 | 50.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 772 | PASS | ECON | 59.0 | 9 | 10 | 1 | 50.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 782 | BUY | ECON | 40.0 | 9 | 17 | 1 | 50.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2731935381889343 | 0.0 | 0.0 | +194da7dc-39b4-40e3-869d-326ace65137b / -— |
| Jogador 2 | 6-4 | 783 | PASS | ECON | 40.0 | 9 | 13 | 1 | 50.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 802 | PASS | ECON | 40.0 | 9 | 20 | 2 | 56.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10384126752614975 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 822 | BUY | STABILIZE | 23.0 | 10 | 28 | 2 | 56.0 | Colosso/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.349636048078537 | 0.0 | 0.0 | +6b7f5603-ce44-4b91-8a3e-939c4fbb26ac / -— |
| Jogador 2 | 6-6 | 823 | PASS | STABILIZE | 23.0 | 10 | 23 | 2 | 56.0 | Colosso/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12319491803646088 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 840 | MOVE_BENCH | STABILIZE | 23.0 | 10 | 23 | 2 | 56.0 | Colosso/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5469343662261963 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-7 | 842 | PASS | STABILIZE | 23.0 | 10 | 31 | 3 | 66.0 | Colosso/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2145676165819168 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-1 | 862 | ANVIL_CHOICE | STABILIZE | 23.0 | 10 | 39 | 3 | 66.0 | Colosso/DA_18_Ahri | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-1 | 863 | EQUIP_FROM_INVENTORY | STABILIZE | 23.0 | 10 | 39 | 3 | 66.0 | Colosso/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.09887944906949997 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-1 | 864 | PASS | STABILIZE | 23.0 | 10 | 39 | 3 | 66.0 | Colosso/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23394031822681427 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5955660343170166 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.09741609543561935 | 0.0 | 0.0 | +c83ad0c5-f046-4834-8d0e-6dac3e49cdef / -— |
| Jogador 3 | 1-2 | 28 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7487250566482544 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4381335377693176 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | -0.2122882902622223 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 31 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 55 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0395768880844116 | 0.0 | 0.0 | +5f61fad0-e2c4-4bef-add4-0eab1d93b4df / -— |
| Jogador 3 | 1-3 | 56 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6609311699867249 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 57 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 82 | BUY_XP | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0403750017285347 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 83 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 112 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3084385097026825 | 0.0 | 0.0 | +f19f9e7f-f189-47fe-b571-be5065c6eb39 / -— |
| Jogador 3 | 2-1 | 113 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2092488408088684 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 114 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 3 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5100665092468262 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 115 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 138 | PASS | STABILIZE | 100.0 | 4 | 9 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 164 | BUY_XP | STABILIZE | 96.0 | 4 | 14 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.023274999111890793 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 165 | BUY | SLOWROLL | 96.0 | 5 | 10 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.02192854695022106 | 0.0 | 0.0 | +29f10cb7-6575-47ca-b583-057992a08253 / -— |
| Jogador 3 | 2-3 | 166 | MOVE_BENCH | SLOWROLL | 96.0 | 5 | 7 | 0 | 10.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.48488110303878784 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 167 | BUY_XP | SLOWROLL | 96.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 168 | PASS | SLOWROLL | 96.0 | 5 | 3 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 189 | BUY_XP | SLOWROLL | 91.0 | 5 | 9 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 190 | BUY_XP | SLOWROLL | 91.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 191 | PASS | SLOWROLL | 91.0 | 5 | 1 | 0 | 16.0 | —/DA_18_Rammus | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 212 | BUY_XP | SLOWROLL | 91.0 | 5 | 7 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.006550000049173832 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 213 | BUY | SLOWROLL | 91.0 | 6 | 3 | 0 | 16.0 | Inferno/DA_18_Rammus | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.06018447503447533 | 0.0 | 0.0 | +cdb48eea-209d-4833-9a68-79df61990332 / -— |
| Jogador 3 | 2-5 | 214 | MOVE_BENCH | SLOWROLL | 91.0 | 6 | 0 | 0 | 16.0 | Inferno/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.42814770340919495 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 215 | PASS | SLOWROLL | 91.0 | 6 | 0 | 0 | 20.0 | Inferno/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 231 | MOVE_BENCH | SLOWROLL | 91.0 | 6 | 0 | 0 | 20.0 | Inferno/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5158814191818237 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 236 | BUY | SLOWROLL | 85.0 | 6 | 6 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9613057374954224 | 0.0 | 0.0 | +0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb / -— |
| Jogador 3 | 2-6 | 237 | BUY_XP | SLOWROLL | 85.0 | 6 | 5 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 238 | PASS | SLOWROLL | 85.0 | 6 | 1 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 262 | BUY_XP | SLOWROLL | 78.0 | 6 | 7 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 263 | PASS | SLOWROLL | 78.0 | 6 | 3 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 289 | BUY_XP | SLOWROLL | 78.0 | 6 | 9 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 290 | BUY_XP | SLOWROLL | 78.0 | 6 | 5 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 291 | PASS | SLOWROLL | 78.0 | 6 | 1 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 312 | BUY_XP | SLOWROLL | 68.0 | 6 | 8 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 313 | BUY_XP | SLOWROLL | 68.0 | 6 | 4 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 314 | PASS | SLOWROLL | 68.0 | 6 | 0 | 0 | 22.0 | Inferno/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 338 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 8 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2303842008113861 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 339 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 8 | 0 | 18.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48808667063713074 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 340 | PASS | STABILIZE | 57.0 | 7 | 8 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 355 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 8 | 0 | 22.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5558575391769409 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 362 | BUY | STABILIZE | 57.0 | 7 | 14 | 1 | 24.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2769834101200104 | 0.0 | 0.0 | +f5c14a50-b095-4a36-995f-2a8514e46f1c / -— |
| Jogador 3 | 3-4 | 363 | MOVE_BENCH | STABILIZE | 57.0 | 7 | 11 | 1 | 24.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1842237114906311 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 364 | BUY_XP | FAST8 | 57.0 | 7 | 11 | 1 | 28.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 365 | BUY_XP | FAST8 | 57.0 | 7 | 7 | 0 | 28.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 366 | PASS | FAST8 | 57.0 | 7 | 3 | 0 | 28.0 | Inferno/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 384 | SELL | FAST8 | 57.0 | 7 | 8 | 0 | 28.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8229384422302246 | 0.0 | 0.0 | +— / -0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb |
| Jogador 3 | 3-5 | 385 | BUY | FAST8 | 57.0 | 7 | 9 | 0 | 28.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.052714861929416656 | 0.0 | 0.0 | +a9c52953-4532-455b-851f-04079adfd354 / -— |
| Jogador 3 | 3-5 | 386 | BUY_XP | FAST8 | 57.0 | 7 | 5 | 0 | 28.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 387 | MOVE_BENCH | FAST8 | 57.0 | 7 | 1 | 0 | 28.0 | Inferno/DA_18_Zyra | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7169683575630188 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 388 | MOVE_BENCH | FAST8 | 57.0 | 7 | 1 | 0 | 30.0 | Inferno/DA_18_Zyra | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17501762509346008 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 389 | PASS | FAST8 | 57.0 | 7 | 1 | 0 | 30.0 | Inferno/DA_18_Zyra | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 405 | BUY_XP | FAST8 | 57.0 | 7 | 8 | 0 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 406 | BUY_XP | FAST8 | 57.0 | 7 | 4 | 0 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 407 | PASS | FAST8 | 57.0 | 7 | 0 | 0 | 30.0 | Inferno/DA_18_Zyra | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 425 | BUY_XP | FAST8 | 57.0 | 7 | 7 | 0 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 426 | PASS | FAST8 | 57.0 | 7 | 3 | 0 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 445 | BUY_XP | FAST8 | 57.0 | 7 | 9 | 0 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 446 | BUY_XP | FAST8 | 57.0 | 7 | 5 | 0 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 447 | PASS | FAST8 | 57.0 | 7 | 1 | 0 | 30.0 | Inferno/DA_18_Zyra | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 465 | BUY_XP | FAST8 | 43.0 | 7 | 6 | 0 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 466 | PASS | FAST8 | 43.0 | 7 | 2 | 0 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 485 | PASS | STABILIZE | 32.0 | 7 | 8 | 0 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 506 | BUY_XP | STABILIZE | 32.0 | 7 | 14 | 1 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07291624695062637 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 507 | MOVE_BENCH | STABILIZE | 32.0 | 8 | 10 | 1 | 30.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3476741909980774 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 508 | MOVE_BENCH | STABILIZE | 32.0 | 8 | 10 | 1 | 28.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.504921555519104 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 509 | PASS | STABILIZE | 32.0 | 8 | 10 | 1 | 36.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 527 | BUY | STABILIZE | 32.0 | 8 | 16 | 1 | 36.0 | Inferno/DA_18_Zyra | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8401278257369995 | 0.0 | 0.0 | +45da6d00-829e-4e2e-a1a5-318498fd007b / -— |
| Jogador 3 | 4-5 | 528 | BUY_XP | STABILIZE | 32.0 | 8 | 13 | 1 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 529 | BUY_XP | STABILIZE | 32.0 | 8 | 9 | 0 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 530 | BUY_XP | STABILIZE | 32.0 | 8 | 5 | 0 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 531 | PASS | STABILIZE | 32.0 | 8 | 1 | 0 | 36.0 | Inferno/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-6 | 543 | PASS | STABILIZE | 19.0 | 8 | 6 | 0 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 562 | PASS | STABILIZE | 19.0 | 8 | 12 | 1 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 582 | ANVIL_CHOICE | STABILIZE | 19.0 | 8 | 18 | 1 | 36.0 | Inferno/DA_18_Tristana | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 583 | CRAFT_AND_EQUIP | STABILIZE | 19.0 | 8 | 18 | 1 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.182429701089859 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 584 | BUY_XP | STABILIZE | 19.0 | 8 | 18 | 1 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 585 | BUY_XP | STABILIZE | 19.0 | 8 | 14 | 1 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 586 | BUY_XP | STABILIZE | 19.0 | 8 | 10 | 1 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 587 | BUY_XP | STABILIZE | 19.0 | 8 | 6 | 0 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 588 | PASS | STABILIZE | 19.0 | 8 | 2 | 0 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 602 | PASS | STABILIZE | 19.0 | 8 | 9 | 0 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 622 | PASS | STABILIZE | 19.0 | 8 | 15 | 1 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12397407740354538 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 642 | BUY | ALL_IN | 1.0 | 8 | 21 | 2 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7371037006378174 | 0.0 | 0.0 | +987e61e4-0d34-49cf-b1ef-a95a7a5dfb21 / -— |
| Jogador 3 | 5-4 | 643 | PASS | ALL_IN | 1.0 | 8 | 18 | 1 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19080232083797455 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 662 | BUY | ALL_IN | 1.0 | 8 | 24 | 2 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9163362979888916 | 0.0 | 0.0 | +f6000a82-1241-4220-9362-c8d788472db0 / -— |
| Jogador 3 | 5-5 | 663 | PASS | ALL_IN | 1.0 | 8 | 21 | 2 | 36.0 | Inferno/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20176391303539276 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5955660343170166 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2717767059803009 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 28 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7398668527603149 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4561019539833069 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | -0.2122882902622223 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 31 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 55 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.05959159508347511 | 0.0 | 0.0 | +a19fc47b-fc81-49b2-bc25-d25d58b8deef / -— |
| Jogador 4 | 1-3 | 56 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.268403023481369 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 57 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 82 | PASS | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 112 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0137526988983154 | 0.0 | 0.0 | +9819422b-1f51-47b5-89b7-9d6e906ddff2 / -— |
| Jogador 4 | 2-1 | 113 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0066289901733398 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 114 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 10.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4847169816493988 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 115 | BUY | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1147739887237549 | 0.0 | 0.0 | +c05579e6-aa73-434f-8a91-c58d68a81ced / -9819422b-1f51-47b5-89b7-9d6e906ddff2,a19fc47b-fc81-49b2-bc25-d25d58b8deef |
| Jogador 4 | 2-1 | 116 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 4.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03310026600956917 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 117 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.02891405299305916 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 118 | PASS | STABILIZE | 100.0 | 4 | 4 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 138 | BUY | STABILIZE | 94.0 | 4 | 9 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.13617181777954102 | 0.0 | 0.0 | +4e00fb2f-75c1-4580-bd09-cb73c31af01f / -— |
| Jogador 4 | 2-2 | 139 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 6 | 0 | 12.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5587080717086792 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 140 | BUY_XP | STABILIZE | 94.0 | 4 | 6 | 0 | 18.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 141 | PASS | STABILIZE | 94.0 | 4 | 2 | 0 | 18.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 164 | BUY_XP | STABILIZE | 89.0 | 4 | 8 | 0 | 18.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0403750017285347 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 165 | BUY | SLOWROLL | 89.0 | 5 | 4 | 0 | 18.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0035226738546043634 | 0.0 | 0.0 | +9db562a0-c8a9-4291-8623-b7b6afbf2606 / -— |
| Jogador 4 | 2-3 | 166 | MOVE_BENCH | SLOWROLL | 89.0 | 5 | 2 | 0 | 18.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5427255034446716 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 167 | PASS | SLOWROLL | 89.0 | 5 | 2 | 0 | 22.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 189 | BUY | SLOWROLL | 83.0 | 5 | 8 | 0 | 22.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3265019953250885 | 0.0 | 0.0 | +a229cc5e-9f28-4ff3-b652-eab994251c92 / -— |
| Jogador 4 | 2-4 | 190 | BUY_XP | SLOWROLL | 83.0 | 5 | 6 | 0 | 22.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 191 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 2 | 0 | 22.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05004698410630226 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 192 | PASS | SLOWROLL | 83.0 | 5 | 2 | 0 | 22.0 | —/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 212 | SELL | SLOWROLL | 83.0 | 5 | 8 | 0 | 22.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2985999882221222 | 0.0 | 0.0 | +— / -9db562a0-c8a9-4291-8623-b7b6afbf2606 |
| Jogador 4 | 2-5 | 213 | BUY | SLOWROLL | 83.0 | 5 | 10 | 1 | 22.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8898846507072449 | 0.0 | 0.0 | +3825a7ba-319f-48f8-ad2d-8c24eabbc1cc / -— |
| Jogador 4 | 2-5 | 214 | MOVE_BENCH | SLOWROLL | 83.0 | 5 | 7 | 0 | 22.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6645073294639587 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 215 | BUY_XP | SLOWROLL | 83.0 | 5 | 7 | 0 | 24.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 216 | PASS | SLOWROLL | 83.0 | 5 | 3 | 0 | 24.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 236 | BUY_XP | SLOWROLL | 76.0 | 5 | 9 | 0 | 24.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.011409999802708626 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 237 | MOVE_BENCH | SLOWROLL | 76.0 | 6 | 5 | 0 | 24.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4406343400478363 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 238 | BUY | FAST8 | 76.0 | 6 | 5 | 0 | 28.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.33182042837142944 | 0.0 | 0.0 | +b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a / -— |
| Jogador 4 | 2-6 | 239 | MOVE_BOARD | FAST8 | 76.0 | 6 | 2 | 0 | 28.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020740801468491554 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 240 | PASS | FAST8 | 76.0 | 6 | 2 | 0 | 28.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 262 | BUY_XP | FAST8 | 69.0 | 6 | 9 | 0 | 28.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 263 | BUY_XP | FAST8 | 69.0 | 6 | 5 | 0 | 28.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 264 | PASS | FAST8 | 69.0 | 6 | 1 | 0 | 28.0 | Fera do Rift/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 289 | MOVE_BENCH | FAST8 | 69.0 | 6 | 8 | 0 | 28.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27285516262054443 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 290 | SELL | FAST8 | 69.0 | 6 | 8 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48100000619888306 | 0.0 | 0.0 | +— / -a229cc5e-9f28-4ff3-b652-eab994251c92 |
| Jogador 4 | 3-1 | 291 | BUY | FAST8 | 69.0 | 6 | 10 | 1 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1359814703464508 | 0.0 | 0.0 | +74fe48c1-d955-4b0d-b832-39d4c86049dc / -— |
| Jogador 4 | 3-1 | 292 | BUY_XP | FAST8 | 69.0 | 6 | 8 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 293 | BUY_XP | FAST8 | 69.0 | 6 | 4 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 294 | PASS | FAST8 | 69.0 | 6 | 0 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 312 | SELL | FAST8 | 69.0 | 6 | 6 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5609999895095825 | 0.0 | 0.0 | +— / -74fe48c1-d955-4b0d-b832-39d4c86049dc |
| Jogador 4 | 3-2 | 313 | BUY | FAST8 | 69.0 | 6 | 8 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2105724811553955 | 0.0 | 0.0 | +3f253868-2de5-4189-95a0-705f62682958 / -— |
| Jogador 4 | 3-2 | 314 | BUY_XP | FAST8 | 69.0 | 6 | 6 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 315 | PASS | FAST8 | 69.0 | 6 | 2 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 338 | BUY_XP | FAST8 | 60.0 | 6 | 7 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 339 | PASS | FAST8 | 60.0 | 6 | 3 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 362 | BUY_XP | FAST8 | 48.0 | 6 | 9 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07689999788999557 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 363 | MOVE_BENCH | FAST8 | 48.0 | 7 | 5 | 0 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4734247922897339 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 364 | BUY_XP | FAST8 | 48.0 | 7 | 5 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 365 | PASS | FAST8 | 48.0 | 7 | 1 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 384 | PASS | FAST8 | 48.0 | 7 | 7 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 405 | BUY | FAST8 | 48.0 | 7 | 13 | 1 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7351539731025696 | 0.0 | 0.0 | +fe3fea0b-bb55-4236-830e-828a00a9e529 / -— |
| Jogador 4 | 3-6 | 406 | BUY_XP | FAST8 | 48.0 | 7 | 11 | 1 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 407 | BUY_XP | FAST8 | 48.0 | 7 | 7 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 408 | MOVE_BOARD | FAST8 | 48.0 | 7 | 3 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010701649822294712 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 409 | MOVE_BOARD | FAST8 | 48.0 | 7 | 3 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 410 | PASS | FAST8 | 48.0 | 7 | 3 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 425 | BUY_XP | FAST8 | 48.0 | 7 | 10 | 1 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 426 | BUY_XP | FAST8 | 48.0 | 7 | 6 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 427 | MOVE_BOARD | FAST8 | 48.0 | 7 | 2 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.047093361616134644 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 428 | PASS | FAST8 | 48.0 | 7 | 2 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 445 | BUY_XP | FAST8 | 48.0 | 7 | 8 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 446 | BUY_XP | FAST8 | 48.0 | 7 | 4 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 447 | CRAFT_AND_EQUIP | FAST8 | 48.0 | 7 | 0 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.112228624522686 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 448 | PASS | FAST8 | 48.0 | 7 | 0 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 465 | BUY_XP | FAST8 | 48.0 | 7 | 7 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 466 | PASS | FAST8 | 48.0 | 7 | 3 | 0 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 485 | MOVE_BENCH | FAST8 | 48.0 | 7 | 10 | 1 | 34.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2906254529953003 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 486 | SELL | FAST8 | 48.0 | 7 | 10 | 1 | 32.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5323702692985535 | 0.0 | 0.0 | +— / -b0ebdf40-a5bf-4ee6-b58a-a89ac9e3fb8a |
| Jogador 4 | 4-3 | 487 | BUY | FAST8 | 48.0 | 7 | 13 | 1 | 32.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2469419687986374 | 0.0 | 0.0 | +60138930-82d5-4f1c-a5fe-a22ea4b70d36 / -— |
| Jogador 4 | 4-3 | 488 | BUY_XP | FAST8 | 48.0 | 7 | 10 | 1 | 32.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 489 | BUY_XP | FAST8 | 48.0 | 7 | 6 | 0 | 32.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 490 | PASS | FAST8 | 48.0 | 7 | 2 | 0 | 32.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 506 | MOVE_BENCH | ECON | 48.0 | 8 | 10 | 1 | 32.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7069312334060669 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 507 | BUY | ECON | 48.0 | 8 | 10 | 1 | 38.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.17952725291252136 | 0.0 | 0.0 | +ea88d306-ae6b-4dbe-b559-3371ba39613a / -— |
| Jogador 4 | 4-4 | 508 | BUY_XP | ECON | 48.0 | 8 | 7 | 0 | 38.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 509 | PASS | ECON | 48.0 | 8 | 3 | 0 | 38.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 527 | BUY | ECON | 48.0 | 8 | 10 | 1 | 38.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5496470332145691 | 0.0 | 0.0 | +111acae7-a889-409f-a15e-419d250fccd0 / -— |
| Jogador 4 | 4-5 | 528 | BUY_XP | ECON | 48.0 | 8 | 7 | 0 | 38.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 529 | PASS | ECON | 48.0 | 8 | 3 | 0 | 38.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 543 | BUY | ECON | 48.0 | 8 | 12 | 1 | 38.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8046576380729675 | 0.0 | 0.0 | +4a885bc0-41b4-43f1-94d3-8e755a10645c / -3f253868-2de5-4189-95a0-705f62682958,fe3fea0b-bb55-4236-830e-828a00a9e529 |
| Jogador 4 | 4-6 | 544 | MOVE_BENCH | ECON | 48.0 | 8 | 10 | 1 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7500684857368469 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 545 | MOVE_BENCH | ECON | 48.0 | 8 | 10 | 1 | 30.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25524526834487915 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 546 | BUY_XP | ECON | 48.0 | 8 | 10 | 1 | 36.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11299999803304672 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 547 | BUY_XP | ECON | 48.0 | 8 | 6 | 0 | 36.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 548 | PASS | ECON | 48.0 | 8 | 2 | 0 | 36.0 | Fera do Rift/DA_Gromp18_AP | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 560 | MOVE_BENCH | ECON | 48.0 | 8 | 2 | 0 | 36.0 | Fera do Rift/DA_Gromp18_AP | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.205258309841156 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 562 | PASS | ECON | 48.0 | 8 | 11 | 1 | 42.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 582 | ANVIL_CHOICE | ECON | 48.0 | 8 | 20 | 2 | 42.0 | Fera do Rift/DA_Gromp18_AP | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 583 | BUY | ECON | 48.0 | 8 | 20 | 2 | 42.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7525385618209839 | 0.0 | 0.0 | +02e125a0-3563-47ec-a82a-cba5178731dd / -— |
| Jogador 4 | 5-1 | 584 | BUY_XP | ECON | 48.0 | 8 | 17 | 1 | 42.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002374999923631549 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 585 | BUY_XP | ECON | 48.0 | 8 | 13 | 1 | 42.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08237499743700027 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 586 | BUY_XP | ECON | 48.0 | 8 | 9 | 0 | 42.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.002374999923631549 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 587 | BUY_XP | ECON | 48.0 | 8 | 5 | 0 | 42.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 588 | PASS | ECON | 48.0 | 8 | 1 | 0 | 42.0 | Fera do Rift/DA_Gromp18_AP | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 602 | PASS | STABILIZE | 33.0 | 8 | 6 | 0 | 42.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 622 | BUY_XP | STABILIZE | 33.0 | 8 | 12 | 1 | 42.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 623 | BUY_XP | STABILIZE | 33.0 | 8 | 8 | 0 | 42.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 624 | BUY_XP | STABILIZE | 33.0 | 8 | 4 | 0 | 42.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.027000000700354576 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 625 | PASS | STABILIZE | 33.0 | 8 | 0 | 0 | 42.0 | Fera do Rift/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 642 | PASS | STABILIZE | 33.0 | 8 | 5 | 0 | 42.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 662 | PASS | STABILIZE | 33.0 | 8 | 10 | 1 | 42.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 682 | PASS | STABILIZE | 33.0 | 8 | 18 | 1 | 42.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12411492317914963 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 702 | PASS | STABILIZE | 33.0 | 8 | 25 | 2 | 42.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13509047031402588 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 722 | ANVIL_CHOICE | STABILIZE | 33.0 | 8 | 33 | 3 | 42.0 | Fera do Rift/DA_Gromp18_AP | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 723 | EQUIP_FROM_INVENTORY | STABILIZE | 33.0 | 8 | 33 | 3 | 42.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.01118707749992609 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 724 | BUY_XP | STABILIZE | 33.0 | 8 | 33 | 3 | 42.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03964437544345856 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 725 | PASS | STABILIZE | 33.0 | 9 | 29 | 2 | 42.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1242133304476738 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-2 | 742 | BUY | STABILIZE | 33.0 | 9 | 39 | 3 | 48.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23248957097530365 | 0.0 | 0.0 | +7f7fc4fe-472b-4ddf-9454-b4a669cbcc14 / -— |
| Jogador 4 | 6-2 | 743 | PASS | STABILIZE | 33.0 | 9 | 34 | 3 | 48.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2047657072544098 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-3 | 762 | BUY | STABILIZE | 33.0 | 9 | 44 | 4 | 48.0 | Fera do Rift/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5332233905792236 | 0.0 | 0.0 | +c5520bc4-3123-40f3-b275-83fa8cb06309 / -— |
| Jogador 4 | 6-3 | 763 | PASS | STABILIZE | 33.0 | 9 | 42 | 4 | 48.0 | Fera do Rift/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2167428582906723 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-4 | 782 | PASS | STABILIZE | 33.0 | 9 | 54 | 5 | 48.0 | Fera do Rift/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23820920288562775 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-5 | 802 | PASS | STABILIZE | 33.0 | 9 | 66 | 5 | 48.0 | Fera do Rift/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24758876860141754 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-6 | 822 | BUY | STABILIZE | 33.0 | 9 | 80 | 5 | 48.0 | Fera do Rift/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14182306826114655 | 0.0 | 0.0 | +aa803972-8af8-46d7-b430-079819730c36 / -— |
| Jogador 4 | 6-6 | 823 | PASS | STABILIZE | 33.0 | 9 | 75 | 5 | 48.0 | Fera do Rift/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25518739223480225 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-7 | 842 | BUY | ALL_IN | 15.0 | 9 | 85 | 5 | 48.0 | Fera do Rift/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015551228076219559 | 0.0 | 0.0 | +663beb45-28d7-42de-b6b8-a81e8676f55f / -— |
| Jogador 4 | 6-7 | 843 | PASS | ALL_IN | 15.0 | 9 | 81 | 5 | 48.0 | Fera do Rift/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34881648421287537 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 7-1 | 862 | ANVIL_CHOICE | ALL_IN | 15.0 | 9 | 91 | 5 | 48.0 | Fera do Rift/DA_Scuttlecrab18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 7-1 | 863 | EQUIP_FROM_INVENTORY | ALL_IN | 15.0 | 9 | 91 | 5 | 48.0 | Fera do Rift/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.04199742153286934 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 7-1 | 864 | BUY | ALL_IN | 15.0 | 9 | 91 | 5 | 48.0 | Fera do Rift/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4463649392127991 | 0.0 | 0.0 | +04ebf9b8-7683-4270-b98a-a3bfb342dcf8 / -— |
| Jogador 4 | 7-1 | 865 | PASS | ALL_IN | 15.0 | 9 | 87 | 5 | 48.0 | Fera do Rift/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35414841771125793 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5692920684814453 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.05371737480163574 | 0.0 | 0.0 | +df7d3860-9b2e-45ed-b564-281d95e64e82 / -— |
| Jogador 5 | 1-2 | 28 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28482919931411743 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3110044598579407 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 30 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | -0.17335718870162964 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 31 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 55 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.22251269221305847 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 56 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3631879687309265 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 57 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 82 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2367689460515976 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 83 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Elise | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2980057895183563 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 84 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Sejuani | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37272217869758606 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 85 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 10.0 | —/DA_18_Sejuani | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 112 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3678376078605652 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 113 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.20524701476097107 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 114 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 14.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03013305738568306 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 115 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10373874753713608 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 116 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 138 | SELL | STABILIZE | 95.0 | 4 | 7 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03702181577682495 | 0.0 | 0.0 | +— / -df7d3860-9b2e-45ed-b564-281d95e64e82 |
| Jogador 5 | 2-2 | 139 | BUY | STABILIZE | 95.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3406416177749634 | 0.0 | 0.0 | +68cd8ae3-399f-461f-89a8-189d7b0a6b59 / -— |
| Jogador 5 | 2-2 | 140 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 6 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1325257271528244 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 141 | BUY_XP | STABILIZE | 95.0 | 4 | 6 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 142 | PASS | STABILIZE | 95.0 | 4 | 2 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 164 | BUY_XP | STABILIZE | 90.0 | 4 | 8 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04550499841570854 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 165 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 4 | 0 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4037194848060608 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 166 | BUY_XP | STABILIZE | 90.0 | 5 | 4 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 167 | PASS | STABILIZE | 90.0 | 5 | 0 | 0 | 22.0 | —/DA_18_MasterYi_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 189 | BUY | STABILIZE | 90.0 | 5 | 6 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.22657425701618195 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 5 | 2-4 | 190 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 3 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08961579203605652 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 191 | PASS | STABILIZE | 90.0 | 5 | 3 | 0 | 24.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 212 | BUY_XP | STABILIZE | 90.0 | 5 | 8 | 0 | 24.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 213 | BUY_XP | STABILIZE | 90.0 | 5 | 4 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 214 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 0 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12118527293205261 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 215 | PASS | STABILIZE | 90.0 | 5 | 0 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 236 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 5 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26699453592300415 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 237 | BUY_XP | STABILIZE | 83.0 | 6 | 5 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 238 | PASS | STABILIZE | 83.0 | 6 | 1 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 256 | MOVE_BENCH | STABILIZE | 83.0 | 6 | 1 | 0 | 24.0 | Florescer/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5009992122650146 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 262 | BUY | FAST8 | 78.0 | 6 | 7 | 0 | 28.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9671581983566284 | 0.0 | 0.0 | +837b2d09-a207-4830-b36d-29e493bbcc22 / -— |
| Jogador 5 | 2-7 | 263 | BUY_XP | FAST8 | 78.0 | 6 | 5 | 0 | 28.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 264 | PASS | FAST8 | 78.0 | 6 | 1 | 0 | 28.0 | Florescer/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 289 | BUY_XP | FAST8 | 78.0 | 6 | 7 | 0 | 28.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 290 | PASS | FAST8 | 78.0 | 6 | 3 | 0 | 28.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 312 | BUY_XP | FAST8 | 68.0 | 6 | 9 | 0 | 28.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 313 | BUY_XP | FAST8 | 68.0 | 6 | 5 | 0 | 28.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 314 | PASS | FAST8 | 68.0 | 6 | 1 | 0 | 28.0 | Florescer/DA_18_MasterYi_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 338 | SELL | FAST8 | 68.0 | 6 | 7 | 0 | 28.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8578464388847351 | 0.0 | 0.0 | +— / -837b2d09-a207-4830-b36d-29e493bbcc22 |
| Jogador 5 | 3-3 | 339 | BUY | FAST8 | 68.0 | 6 | 9 | 0 | 28.0 | Florescer/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2086285799741745 | 0.0 | 0.0 | +8a4d0946-b80f-4fbb-ab7c-d43c2697c34e / -— |
| Jogador 5 | 3-3 | 340 | BUY_XP | FAST8 | 68.0 | 6 | 5 | 0 | 28.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 341 | PASS | FAST8 | 68.0 | 6 | 1 | 0 | 28.0 | Florescer/DA_18_Ahri | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 362 | BUY_XP | FAST8 | 58.0 | 6 | 6 | 0 | 28.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09130000323057175 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 363 | MOVE_BENCH | FAST8 | 58.0 | 7 | 2 | 0 | 28.0 | Florescer/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09852169454097748 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 364 | PASS | FAST8 | 58.0 | 7 | 2 | 0 | 30.0 | Florescer/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 381 | MOVE_BENCH | FAST8 | 58.0 | 7 | 2 | 0 | 30.0 | Florescer/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3406100273132324 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 384 | PASS | FAST8 | 58.0 | 7 | 7 | 0 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 405 | PASS | FAST8 | 58.0 | 7 | 13 | 1 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 425 | BUY | FAST8 | 47.0 | 7 | 19 | 1 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6487359404563904 | 0.0 | 0.0 | +bd0feb3d-9ff5-4678-862f-202b3bf74d5c / -— |
| Jogador 5 | 3-7 | 426 | BUY_XP | FAST8 | 47.0 | 7 | 16 | 1 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 427 | BUY_XP | FAST8 | 47.0 | 7 | 12 | 1 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 428 | BUY_XP | FAST8 | 47.0 | 7 | 8 | 0 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 429 | BUY_XP | FAST8 | 47.0 | 7 | 4 | 0 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 430 | PASS | FAST8 | 47.0 | 7 | 0 | 0 | 36.0 | Florescer/DA_18_Ahri | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 445 | PASS | FAST8 | 47.0 | 7 | 5 | 0 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 465 | BUY_XP | FAST8 | 47.0 | 7 | 11 | 1 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 466 | BUY_XP | FAST8 | 47.0 | 7 | 7 | 0 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 467 | PASS | FAST8 | 47.0 | 7 | 3 | 0 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 485 | PASS | STABILIZE | 33.0 | 7 | 8 | 0 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 506 | PASS | STABILIZE | 22.0 | 7 | 14 | 1 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 527 | BUY_XP | STABILIZE | 22.0 | 7 | 21 | 2 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 528 | BUY_XP | STABILIZE | 22.0 | 7 | 17 | 1 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 529 | BUY_XP | STABILIZE | 22.0 | 7 | 13 | 1 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 530 | BUY_XP | STABILIZE | 22.0 | 7 | 9 | 0 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3885537385940552 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 531 | PASS | STABILIZE | 22.0 | 8 | 5 | 0 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 541 | MOVE_BENCH | STABILIZE | 22.0 | 8 | 5 | 0 | 36.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4398605227470398 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 543 | PASS | STABILIZE | 22.0 | 8 | 11 | 1 | 42.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 562 | BUY | ALL_IN | 10.0 | 8 | 17 | 1 | 42.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.31891384720802307 | 0.0 | 0.0 | +1388df2e-8cb4-4e29-8b30-776c29406917 / -— |
| Jogador 5 | 4-7 | 563 | PASS | ALL_IN | 10.0 | 8 | 14 | 1 | 42.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 582 | ANVIL_CHOICE | ALL_IN | 10.0 | 8 | 20 | 2 | 42.0 | Florescer/DA_18_Ahri | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 583 | BUY | ALL_IN | 10.0 | 8 | 20 | 2 | 42.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.047966428101062775 | 0.0 | 0.0 | +d381c462-a17f-4192-b694-66a7c3aaee4f / -— |
| Jogador 5 | 5-1 | 584 | PASS | ALL_IN | 10.0 | 8 | 16 | 1 | 42.0 | Florescer/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.17997460067272186 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.0018307692371308804 | 0.0 | 0.0 | +— / -698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.3409023582935333 | 0.0 | 0.0 | +9002992e-4dcd-4fec-939c-87393464a41d / -— |
| Jogador 6 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.6121415495872498 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 4 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2717767059803009 | 0.0 | 0.0 | +425b1e77-5887-40b3-875e-c1f60dc6c513 / -— |
| Jogador 6 | 1-2 | 28 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7398668527603149 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4561019539833069 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 30 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 1.036318302154541 | 0.0 | 0.0 | +908afab9-748c-4057-a2a9-d2686c5d52e0 / -— |
| Jogador 6 | 1-2 | 31 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4104852080345154 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 33 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 55 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.039830125868320465 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 56 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 82 | BUY_XP | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0403750017285347 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 83 | PASS | STABILIZE | 100.0 | 4 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 112 | BUY | STABILIZE | 100.0 | 4 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.039658546447754 | 0.0 | 0.0 | +185ee377-0917-4209-905b-9486d5be0193 / -— |
| Jogador 6 | 2-1 | 113 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06300000101327896 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 114 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 131 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14709660410881042 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 138 | BUY | SLOWROLL | 95.0 | 5 | 5 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09231401234865189 | 0.0 | 0.0 | +43da0d73-facd-488b-b856-94e9496a97f9 / -— |
| Jogador 6 | 2-2 | 139 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 2 | 0 | 8.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34071388840675354 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 140 | PASS | SLOWROLL | 95.0 | 5 | 2 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 164 | BUY | SLOWROLL | 95.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.009702815674245358 | 0.0 | 0.0 | +8d5fe8a4-6e8b-4dbf-9460-8abe2d4481d1 / -— |
| Jogador 6 | 2-3 | 165 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29354503750801086 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 166 | BUY_XP | SLOWROLL | 95.0 | 5 | 5 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 167 | PASS | SLOWROLL | 95.0 | 5 | 1 | 0 | 14.0 | —/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 189 | SELL | SLOWROLL | 95.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33336836099624634 | 0.0 | 0.0 | +— / -43da0d73-facd-488b-b856-94e9496a97f9 |
| Jogador 6 | 2-4 | 190 | BUY | SLOWROLL | 95.0 | 5 | 11 | 1 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8748189806938171 | 0.0 | 0.0 | +a1c62c5f-385c-49ba-ac65-9dff28493faf / -— |
| Jogador 6 | 2-4 | 191 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 192 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 8 | 0 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33349624276161194 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 193 | PASS | SLOWROLL | 95.0 | 5 | 8 | 0 | 18.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 212 | BUY_XP | SLOWROLL | 95.0 | 5 | 14 | 1 | 18.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 213 | BUY_XP | SLOWROLL | 95.0 | 5 | 10 | 1 | 18.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1379999965429306 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 214 | BUY_XP | SLOWROLL | 95.0 | 5 | 6 | 0 | 18.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017079999670386314 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 215 | PASS | SLOWROLL | 95.0 | 6 | 2 | 0 | 18.0 | Colosso/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 231 | MOVE_BENCH | SLOWROLL | 95.0 | 6 | 2 | 0 | 18.0 | Colosso/DA_18_Hecarim | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5278261303901672 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 236 | BUY | SLOWROLL | 95.0 | 6 | 9 | 0 | 20.0 | Colosso/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.28535327315330505 | 0.0 | 0.0 | +fee4e511-e40e-4114-a8b6-c2de73117e82 / -— |
| Jogador 6 | 2-6 | 237 | BUY_XP | SLOWROLL | 95.0 | 6 | 6 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 238 | PASS | SLOWROLL | 95.0 | 6 | 2 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 262 | BUY_XP | SLOWROLL | 89.0 | 6 | 7 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 263 | MOVE_BOARD | SLOWROLL | 89.0 | 6 | 3 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.032957449555397034 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 264 | PASS | SLOWROLL | 89.0 | 6 | 3 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 289 | BUY_XP | SLOWROLL | 89.0 | 6 | 8 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 290 | BUY_XP | SLOWROLL | 89.0 | 6 | 4 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 291 | PASS | SLOWROLL | 89.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 312 | BUY_XP | SLOWROLL | 78.0 | 6 | 6 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 313 | PASS | SLOWROLL | 78.0 | 6 | 2 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 338 | BUY_XP | SLOWROLL | 69.0 | 6 | 8 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04383999854326248 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 339 | BUY_XP | STABILIZE | 69.0 | 7 | 4 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 340 | PASS | STABILIZE | 69.0 | 7 | 0 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 355 | MOVE_BENCH | STABILIZE | 69.0 | 7 | 0 | 0 | 20.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6717224717140198 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 362 | PASS | FAST8 | 59.0 | 7 | 6 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 384 | BUY | FAST8 | 59.0 | 7 | 12 | 1 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.6513188481330872 | 0.0 | 0.0 | +9443e3b5-f0a2-4ab7-8378-907a3d2bccaa / -— |
| Jogador 6 | 3-5 | 385 | BUY_XP | FAST8 | 59.0 | 7 | 9 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 386 | BUY_XP | FAST8 | 59.0 | 7 | 5 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 387 | PASS | FAST8 | 59.0 | 7 | 1 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 405 | BUY_XP | FAST8 | 47.0 | 7 | 8 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 406 | BUY_XP | FAST8 | 47.0 | 7 | 4 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 407 | PASS | FAST8 | 47.0 | 7 | 0 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 425 | PASS | STABILIZE | 35.0 | 7 | 8 | 0 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 445 | PASS | STABILIZE | 35.0 | 7 | 16 | 1 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10926984250545502 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 465 | PASS | STABILIZE | 24.0 | 7 | 25 | 2 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13080953061580658 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 485 | PASS | STABILIZE | 24.0 | 7 | 33 | 3 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20647937059402466 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 506 | PASS | ALL_IN | 10.0 | 7 | 41 | 4 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29579365253448486 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 527 | PASS | ALL_IN | 10.0 | 7 | 50 | 5 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33222222328186035 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5955660343170166 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2574339807033539 | 0.0 | 0.0 | +47ec6577-cbf2-4275-b185-c19256223441 / -— |
| Jogador 7 | 1-2 | 28 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9932671189308167 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5648271441459656 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 30 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 55 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 1.0491724014282227 | 0.0 | 0.0 | +96fb1ff5-06a8-439b-af2b-8700d7be8524 / -— |
| Jogador 7 | 1-3 | 56 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2016574591398239 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 57 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34841933846473694 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 58 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.32221969962120056 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 59 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 82 | PASS | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 112 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.26712700724601746 | 0.0 | 0.0 | +5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef / -— |
| Jogador 7 | 2-1 | 113 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1945178210735321 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 114 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 8.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5199708342552185 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 115 | BUY_XP | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 116 | PASS | STABILIZE | 100.0 | 4 | 3 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 138 | PASS | STABILIZE | 95.0 | 4 | 8 | 0 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 164 | PASS | STABILIZE | 95.0 | 4 | 14 | 1 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 189 | BUY | SLOWROLL | 89.0 | 5 | 20 | 2 | 10.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.02225729450583458 | 0.0 | 0.0 | +fb7c0635-9f86-4c1e-b354-37372f84d656 / -— |
| Jogador 7 | 2-4 | 190 | MOVE_BENCH | SLOWROLL | 89.0 | 5 | 16 | 1 | 10.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6115437150001526 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 191 | BUY_XP | SLOWROLL | 89.0 | 5 | 16 | 1 | 18.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 192 | BUY_XP | SLOWROLL | 89.0 | 5 | 12 | 1 | 18.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.1379999965429306 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 193 | BUY_XP | SLOWROLL | 89.0 | 5 | 8 | 0 | 18.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 194 | BUY_XP | SLOWROLL | 89.0 | 5 | 4 | 0 | 18.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 195 | PASS | SLOWROLL | 89.0 | 5 | 0 | 0 | 18.0 | —/DA_Sentinel18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 212 | BUY_XP | SLOWROLL | 89.0 | 5 | 5 | 0 | 18.0 | —/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.022749999538064003 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 213 | BUY | SLOWROLL | 89.0 | 6 | 1 | 0 | 18.0 | Inferno/DA_Sentinel18 | BUY, MOVE_BOARD, PASS | True | True | 0.2820035517215729 | 0.0 | 0.0 | +caf48a0a-39fe-4cd0-ac66-ff8dac91ed3e / -— |
| Jogador 7 | 2-5 | 214 | MOVE_BOARD | SLOWROLL | 89.0 | 6 | 0 | 0 | 18.0 | Inferno/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024840479716658592 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 215 | PASS | SLOWROLL | 89.0 | 6 | 0 | 0 | 18.0 | Inferno/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 231 | MOVE_BENCH | SLOWROLL | 89.0 | 6 | 0 | 0 | 18.0 | Inferno/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3601122796535492 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 236 | BUY | SLOWROLL | 89.0 | 6 | 6 | 0 | 20.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9923102855682373 | 0.0 | 0.0 | +a146f2d5-4da5-4c0e-bb09-de3177c72417 / -— |
| Jogador 7 | 2-6 | 237 | MOVE_BENCH | SLOWROLL | 89.0 | 6 | 4 | 0 | 20.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3232693076133728 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 238 | BUY_XP | SLOWROLL | 89.0 | 6 | 4 | 0 | 22.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 239 | PASS | SLOWROLL | 89.0 | 6 | 0 | 0 | 22.0 | Inferno/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 262 | BUY_XP | SLOWROLL | 89.0 | 6 | 7 | 0 | 22.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057999998331069946 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 263 | PASS | SLOWROLL | 89.0 | 6 | 3 | 0 | 22.0 | Inferno/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 289 | BUY_XP | SLOWROLL | 89.0 | 6 | 9 | 0 | 22.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 290 | BUY_XP | SLOWROLL | 89.0 | 6 | 5 | 0 | 22.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 291 | PASS | SLOWROLL | 89.0 | 6 | 1 | 0 | 22.0 | Inferno/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 312 | BUY_XP | SLOWROLL | 79.0 | 6 | 6 | 0 | 22.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02800000086426735 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 313 | PASS | SLOWROLL | 79.0 | 6 | 2 | 0 | 22.0 | Inferno/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 338 | BUY_XP | SLOWROLL | 79.0 | 6 | 8 | 0 | 22.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03897999972105026 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 339 | BUY_XP | STABILIZE | 79.0 | 7 | 4 | 0 | 22.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032999999821186066 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 340 | MOVE_BENCH | STABILIZE | 79.0 | 7 | 0 | 0 | 22.0 | Inferno/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5454941391944885 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 341 | PASS | STABILIZE | 79.0 | 7 | 0 | 0 | 24.0 | Inferno/DA_Sentinel18 | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 362 | BUY | STABILIZE | 79.0 | 7 | 7 | 0 | 24.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8358715772628784 | 0.0 | 0.0 | +94d1da64-f0c8-4fd8-a610-b7e86f10378e / -5e5e26d8-72ac-4e99-bb6f-2e8de4a415ef,a146f2d5-4da5-4c0e-bb09-de3177c72417 |
| Jogador 7 | 3-4 | 363 | MOVE_BENCH | STABILIZE | 79.0 | 7 | 5 | 0 | 16.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5623994469642639 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 364 | BUY | STABILIZE | 79.0 | 7 | 5 | 0 | 24.0 | Inferno/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.28176185488700867 | 0.0 | 0.0 | +cfe17b3a-c9b6-4e09-9ba1-23e762a72569 / -— |
| Jogador 7 | 3-4 | 365 | MOVE_BENCH | STABILIZE | 79.0 | 7 | 2 | 0 | 24.0 | Inferno/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23010224103927612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 366 | MOVE_BENCH | STABILIZE | 79.0 | 7 | 2 | 0 | 22.0 | Inferno/DA_18_Shen | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8075828552246094 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 367 | MOVE_BENCH | STABILIZE | 79.0 | 7 | 2 | 0 | 22.0 | Inferno/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21300958096981049 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 368 | MOVE_BENCH | STABILIZE | 79.0 | 7 | 2 | 0 | 24.0 | Inferno/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07574915885925293 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 369 | MOVE_BOARD | FAST8 | 79.0 | 7 | 2 | 0 | 28.0 | Inferno/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15319235622882843 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 370 | PASS | FAST8 | 79.0 | 7 | 2 | 0 | 28.0 | Inferno/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 381 | MOVE_BENCH | FAST8 | 79.0 | 7 | 2 | 0 | 28.0 | Inferno/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6026951670646667 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 384 | BUY | FAST8 | 79.0 | 7 | 8 | 0 | 30.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1903543770313263 | 0.0 | 0.0 | +f2fa6abf-e020-4aaf-ac0e-35e7642e9d2e / -— |
| Jogador 7 | 3-5 | 385 | MOVE_BOARD | FAST8 | 79.0 | 7 | 5 | 0 | 30.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.012479945085942745 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 386 | BUY_XP | FAST8 | 79.0 | 7 | 5 | 0 | 30.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 387 | PASS | FAST8 | 79.0 | 7 | 1 | 0 | 30.0 | Inferno/DA_Sentinel18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 405 | BUY | FAST8 | 68.0 | 7 | 6 | 0 | 30.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19014306366443634 | 0.0 | 0.0 | +a1aa0280-2379-4d0b-a475-143c1a2f6c25 / -— |
| Jogador 7 | 3-6 | 406 | PASS | FAST8 | 68.0 | 7 | 2 | 0 | 30.0 | Inferno/DA_Sentinel18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 425 | PASS | FAST8 | 57.0 | 7 | 8 | 0 | 30.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 445 | BUY_XP | FAST8 | 57.0 | 7 | 14 | 1 | 30.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0019249999895691872 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 446 | BUY_XP | FAST8 | 57.0 | 7 | 10 | 1 | 30.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08799999952316284 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 447 | BUY_XP | FAST8 | 57.0 | 7 | 6 | 0 | 30.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 448 | PASS | FAST8 | 57.0 | 7 | 2 | 0 | 30.0 | Inferno/DA_Sentinel18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 465 | BUY_XP | FAST8 | 46.0 | 7 | 8 | 0 | 30.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 466 | BUY_XP | FAST8 | 46.0 | 7 | 4 | 0 | 30.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 467 | PASS | FAST8 | 46.0 | 7 | 0 | 0 | 30.0 | Inferno/DA_Sentinel18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 485 | PASS | STABILIZE | 35.0 | 7 | 6 | 0 | 30.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 506 | PASS | STABILIZE | 22.0 | 7 | 13 | 1 | 30.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 527 | PASS | STABILIZE | 22.0 | 7 | 21 | 2 | 30.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12427830696105957 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 543 | BUY | ALL_IN | 10.0 | 7 | 31 | 3 | 30.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8319785594940186 | 0.0 | 0.0 | +023f01af-91d0-4e07-8229-2b7cded83151 / -— |
| Jogador 7 | 4-6 | 544 | PASS | ALL_IN | 10.0 | 7 | 28 | 2 | 30.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20161904394626617 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 562 | PASS | ALL_IN | 10.0 | 7 | 38 | 3 | 30.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28950265049934387 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 582 | ANVIL_CHOICE | ALL_IN | 10.0 | 7 | 49 | 4 | 30.0 | Inferno/DA_Sentinel18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 583 | CRAFT_AND_EQUIP | ALL_IN | 10.0 | 7 | 49 | 4 | 30.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.20254960656166077 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 584 | PASS | ALL_IN | 10.0 | 7 | 49 | 4 | 30.0 | Inferno/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3266587257385254 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5955660343170166 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 2 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 27 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.011937879957258701 | 0.0 | 0.0 | +fddba3f3-87f3-4c97-a7b2-e5d1ef789709 / -— |
| Jogador 8 | 1-2 | 28 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8217591643333435 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 29 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5140626430511475 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 30 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 55 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.30620744824409485 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 56 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09315773844718933 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 57 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.820324182510376 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 58 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25168919563293457 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 59 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 76 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4024536609649658 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 82 | PASS | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 112 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0226327180862427 | 0.0 | 0.0 | +630d9254-3856-4d88-b981-43a8270b4b3d / -— |
| Jogador 8 | 2-1 | 113 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 8 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06297934055328369 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 114 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.030939772725105286 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 115 | BUY_XP | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 116 | BUY_XP | STABILIZE | 100.0 | 4 | 4 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 117 | PASS | STABILIZE | 100.0 | 4 | 0 | 0 | 8.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 138 | BUY | SLOWROLL | 100.0 | 5 | 6 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.008194129914045334 | 0.0 | 0.0 | +4b4cc4ba-04a0-4e04-88f2-e6913a342285 / -— |
| Jogador 8 | 2-2 | 139 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 3 | 0 | 8.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4703453481197357 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 140 | PASS | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 164 | BUY | STABILIZE | 100.0 | 5 | 10 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03280214965343475 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 8 | 2-3 | 165 | BUY_XP | STABILIZE | 100.0 | 5 | 7 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 166 | PASS | STABILIZE | 100.0 | 5 | 3 | 0 | 14.0 | —/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 189 | SELL | STABILIZE | 100.0 | 5 | 10 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37844616174697876 | 0.0 | 0.0 | +— / -b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 8 | 2-4 | 190 | BUY | STABILIZE | 100.0 | 5 | 13 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.180484801530838 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 8 | 2-4 | 191 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 10 | 1 | 14.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21564379334449768 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 192 | BUY_XP | STABILIZE | 100.0 | 5 | 10 | 1 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 193 | BUY_XP | STABILIZE | 100.0 | 5 | 6 | 0 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 194 | PASS | STABILIZE | 100.0 | 5 | 2 | 0 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 212 | MOVE_BENCH | STABILIZE | 100.0 | 5 | 8 | 0 | 14.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03914641588926315 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 213 | BUY_XP | STABILIZE | 100.0 | 5 | 8 | 0 | 18.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04293999820947647 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 214 | SELL | SLOWROLL | 100.0 | 6 | 4 | 0 | 18.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7992685437202454 | 0.0 | 0.0 | +— / -fddba3f3-87f3-4c97-a7b2-e5d1ef789709 |
| Jogador 8 | 2-5 | 215 | BUY | STABILIZE | 100.0 | 6 | 5 | 0 | 18.0 | Colosso/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.37384042143821716 | 0.0 | 0.0 | +c0d8da9e-5ede-4a26-8c5c-e2a908318bfd / -— |
| Jogador 8 | 2-5 | 216 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 3 | 0 | 18.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04119361191987991 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 217 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 3 | 0 | 16.0 | Colosso/DA_Krug18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3262769877910614 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 218 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 3 | 0 | 16.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3900880515575409 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 219 | PASS | STABILIZE | 100.0 | 6 | 3 | 0 | 18.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 231 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 3 | 0 | 18.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5545377731323242 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 236 | BUY | STABILIZE | 100.0 | 6 | 10 | 1 | 22.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.28909602761268616 | 0.0 | 0.0 | +87600495-fe90-4832-ab42-9a5cb0ebe3f4 / -— |
| Jogador 8 | 2-6 | 237 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 6 | 0 | 22.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16662822663784027 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 238 | BUY_XP | STABILIZE | 100.0 | 6 | 6 | 0 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 239 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016619199886918068 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 240 | MOVE_BOARD | STABILIZE | 100.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06559108197689056 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 241 | PASS | STABILIZE | 100.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 262 | BUY_XP | STABILIZE | 100.0 | 6 | 10 | 1 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 263 | BUY_XP | STABILIZE | 100.0 | 6 | 6 | 0 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 264 | PASS | STABILIZE | 100.0 | 6 | 2 | 0 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 289 | SELL | STABILIZE | 100.0 | 6 | 9 | 0 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30052220821380615 | 0.0 | 0.0 | +— / -4b4cc4ba-04a0-4e04-88f2-e6913a342285 |
| Jogador 8 | 3-1 | 290 | BUY | STABILIZE | 100.0 | 6 | 12 | 1 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.053144682198762894 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 8 | 3-1 | 291 | MOVE_BENCH | STABILIZE | 100.0 | 6 | 8 | 0 | 24.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7407817840576172 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 292 | BUY_XP | STABILIZE | 100.0 | 6 | 8 | 0 | 24.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 293 | BUY_XP | STABILIZE | 100.0 | 6 | 4 | 0 | 24.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 294 | PASS | STABILIZE | 100.0 | 6 | 0 | 0 | 24.0 | Colosso/DA_18_Lillia | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 312 | BUY_XP | STABILIZE | 100.0 | 6 | 9 | 0 | 24.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 313 | BUY_XP | STABILIZE | 100.0 | 6 | 5 | 0 | 24.0 | Colosso/DA_18_Lillia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06353499740362167 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 314 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 1 | 0 | 24.0 | Colosso/DA_18_Lillia | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05483737960457802 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 315 | MOVE_BENCH | FAST8 | 100.0 | 7 | 1 | 0 | 26.0 | Colosso/DA_18_Soraka | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5592636466026306 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 316 | PASS | STABILIZE | 100.0 | 7 | 1 | 0 | 24.0 | Colosso/DA_18_Soraka | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 331 | MOVE_BENCH | STABILIZE | 100.0 | 7 | 1 | 0 | 24.0 | Colosso/DA_18_Soraka | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47689089179039 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 338 | BUY_XP | FAST8 | 88.0 | 7 | 6 | 0 | 32.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 339 | PASS | FAST8 | 88.0 | 7 | 2 | 0 | 32.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 362 | BUY | FAST8 | 77.0 | 7 | 8 | 0 | 32.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7077818512916565 | 0.0 | 0.0 | +d5848998-33f3-4632-94c0-60388a7cc6b8 / -— |
| Jogador 8 | 3-4 | 363 | MOVE_BENCH | FAST8 | 77.0 | 7 | 5 | 0 | 32.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 364 | BUY_XP | FAST8 | 77.0 | 7 | 5 | 0 | 32.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 365 | MOVE_BENCH | FAST8 | 77.0 | 7 | 1 | 0 | 32.0 | Colosso/DA_18_Soraka | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08766289055347443 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 366 | PASS | FAST8 | 77.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 384 | BUY_XP | FAST8 | 77.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 385 | PASS | FAST8 | 77.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 405 | BUY_XP | FAST8 | 66.0 | 7 | 9 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 406 | BUY_XP | FAST8 | 66.0 | 7 | 5 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 407 | PASS | FAST8 | 66.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 425 | BUY_XP | FAST8 | 55.0 | 7 | 7 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 426 | PASS | FAST8 | 55.0 | 7 | 3 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 445 | BUY_XP | FAST8 | 55.0 | 7 | 9 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 446 | BUY_XP | FAST8 | 55.0 | 7 | 5 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 447 | CRAFT_AND_EQUIP | FAST8 | 55.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.13279996812343597 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 448 | PASS | FAST8 | 55.0 | 7 | 1 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 465 | BUY_XP | FAST8 | 43.0 | 7 | 8 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 466 | BUY_XP | FAST8 | 43.0 | 7 | 4 | 0 | 36.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0772937536239624 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 467 | PASS | ECON | 43.0 | 8 | 0 | 0 | 36.0 | Colosso/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 481 | MOVE_BENCH | ECON | 43.0 | 8 | 0 | 0 | 36.0 | Colosso/DA_18_Soraka | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4165984094142914 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 485 | BUY | ECON | 43.0 | 8 | 6 | 0 | 38.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.20728321373462677 | 0.0 | 0.0 | +1fa69553-5270-4459-986b-600f748711b7 / -— |
| Jogador 8 | 4-3 | 486 | PASS | ECON | 43.0 | 8 | 2 | 0 | 38.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 506 | BUY_XP | ECON | 43.0 | 8 | 9 | 0 | 38.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 507 | BUY_XP | ECON | 43.0 | 8 | 5 | 0 | 38.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 508 | PASS | ECON | 43.0 | 8 | 1 | 0 | 38.0 | Colosso/DA_18_Soraka | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 527 | BUY | ECON | 43.0 | 8 | 7 | 0 | 38.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7314941883087158 | 0.0 | 0.0 | +715d5bfc-c8c3-4dec-a247-9e07ee2755e8 / -— |
| Jogador 8 | 4-5 | 528 | PASS | ECON | 43.0 | 8 | 3 | 0 | 38.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 543 | BUY | ECON | 43.0 | 8 | 10 | 1 | 38.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12884196639060974 | 0.0 | 0.0 | +5c931416-3aeb-40d4-9e6f-612b0d387226 / -— |
| Jogador 8 | 4-6 | 544 | BUY_XP | ECON | 43.0 | 8 | 6 | 0 | 38.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 545 | PASS | ECON | 43.0 | 8 | 2 | 0 | 38.0 | Colosso/DA_18_Soraka | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 562 | PASS | STABILIZE | 30.0 | 8 | 7 | 0 | 38.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 582 | ANVIL_CHOICE | STABILIZE | 30.0 | 8 | 12 | 1 | 38.0 | Colosso/DA_18_Soraka | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 583 | BUY | STABILIZE | 30.0 | 8 | 12 | 1 | 38.0 | Colosso/DA_18_Soraka | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23016633093357086 | 0.0 | 0.0 | +f32e50e0-1430-4549-a1dd-a8473ffe0bd4 / -— |
| Jogador 8 | 5-1 | 584 | BUY_XP | STABILIZE | 30.0 | 8 | 7 | 0 | 38.0 | Colosso/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00800000037997961 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 585 | PASS | STABILIZE | 30.0 | 8 | 3 | 0 | 38.0 | Colosso/DA_18_Lux_Elderwood | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 602 | PASS | STABILIZE | 30.0 | 8 | 9 | 0 | 38.0 | Colosso/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 622 | PASS | ALL_IN | 14.0 | 8 | 14 | 1 | 38.0 | Colosso/DA_18_Lux_Elderwood | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 111 | 141 | 2 | 3 | 20 | 1 | 0 | 0 | 49 | 48.0 |
- Jogador 1 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 49g, BUY_XP: 92g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 3g, stage 2: 44g, stage 3: 42g, stage 4: 43g, stage 5: 7g, stage 6: 2g
| Jogador 2 | 143 | 259 | 16 | 17 | 43 | 3 | 0 | 0 | 39 | 66.0 |
- Jogador 2 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 67g, BUY_XP: 192g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 4g, stage 2: 47g, stage 3: 68g, stage 4: 56g, stage 5: 35g, stage 6: 49g, stage 7: 0g
| Jogador 3 | 91 | 143 | 1 | 5 | 25 | 2 | 0 | 0 | 21 | 36.0 |
- Jogador 3 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 27g, BUY_XP: 116g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 6g, stage 2: 37g, stage 3: 47g, stage 4: 31g, stage 5: 22g
| Jogador 4 | 131 | 196 | 9 | 12 | 30 | 1 | 0 | 0 | 87 | 48.0 |
- Jogador 4 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 60g, BUY_XP: 136g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 3g, stage 2: 45g, stage 3: 46g, stage 4: 47g, stage 5: 31g, stage 6: 20g, stage 7: 4g
| Jogador 5 | 81 | 119 | 4 | 5 | 19 | 2 | 0 | 0 | 16 | 42.0 |
- Jogador 5 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 31g, BUY_XP: 88g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 6g, stage 2: 39g, stage 3: 43g, stage 4: 27g, stage 5: 4g
| Jogador 6 | 65 | 87 | 4 | 3 | 14 | 3 | 0 | 0 | 50 | 26.0 |
- Jogador 6 — gasto por ação: BUY: 19g, BUY_XP: 68g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 7g, stage 2: 41g, stage 3: 39g, stage 4: 0g
| Jogador 7 | 79 | 102 | 0 | 4 | 17 | 1 | 0 | 0 | 49 | 30.0 |
- Jogador 7 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 26g, BUY_XP: 76g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g
- Jogador 7 — gasto por estágio: stage 1: 2g, stage 2: 41g, stage 3: 36g, stage 4: 23g, stage 5: 0g
| Jogador 8 | 100 | 150 | 7 | 7 | 24 | 3 | 0 | 0 | 14 | 38.0 |
- Jogador 8 — gasto por ação: ANVIL_CHOICE: 0g, BUY: 42g, BUY_XP: 108g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 2g, stage 2: 52g, stage 3: 47g, stage 4: 40g, stage 5: 9g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 2 | 2 | 0 | 0.0% |
| Jogador 2 | 1 | 1 | 0 | 0.0% |
| Jogador 3 | 1 | 1 | 0 | 0.0% |
| Jogador 4 | 1 | 1 | 0 | 0.0% |
| Jogador 5 | 1 | 1 | 0 | 0.0% |
| Jogador 6 | 1 | 1 | 0 | 0.0% |
| Jogador 7 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 1 | 1 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ médio qualidade | Estrutural médio | Δ estrutural médio | Posicional médio | Δ qualidade combate + | Δ qualidade combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 111 | 16 | 20 | 75 | 0.0051 | 0.0272 | 0.0014 | 0.4914 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (2 ações), BUY: Δ -0.0317 (19 ações), BUY_XP: Δ 0.0000 (23 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0297 (26 ações), MOVE_BOARD: Δ 0.0667 (5 ações), PASS: Δ 0.0000 (33 ações), SELL: Δ 0.0600 (1 ações)
| Jogador 2 | 143 | 11 | 11 | 121 | 0.0016 | -0.0105 | -0.0012 | 0.4033 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (3 ações), BUY: Δ -0.0360 (20 ações), BUY_XP: Δ 0.0000 (48 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (2 ações), MOVE_BENCH: Δ 0.0410 (21 ações), MOVE_BOARD: Δ 0.0311 (3 ações), PASS: Δ 0.0000 (40 ações), SELL: Δ 0.0000 (5 ações)
| Jogador 3 | 91 | 9 | 9 | 73 | -0.0024 | -0.3565 | -0.0057 | 0.3954 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (1 ações), BUY: Δ -0.0109 (11 ações), BUY_XP: Δ 0.0000 (29 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0019 (17 ações), MOVE_BOARD: Δ -0.1286 (1 ações), PASS: Δ 0.0000 (30 ações), SELL: Δ 0.0000 (1 ações)
| Jogador 4 | 131 | 12 | 15 | 104 | -0.0071 | -0.8538 | -0.0102 | 0.3393 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (3 ações), BUY: Δ 0.0263 (22 ações), BUY_XP: Δ 0.0000 (34 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (2 ações), MOVE_BENCH: Δ -0.0792 (19 ações), MOVE_BOARD: Δ -0.0013 (6 ações), PASS: Δ 0.0000 (40 ações), SELL: Δ 0.0000 (4 ações)
| Jogador 5 | 81 | 8 | 10 | 63 | 0.0070 | -0.1407 | -0.0009 | 0.5619 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (1 ações), BUY: Δ 0.0364 (11 ações), BUY_XP: Δ 0.0000 (22 ações), MOVE_BENCH: Δ -0.0032 (16 ações), MOVE_BOARD: Δ 0.0721 (3 ações), PASS: Δ 0.0000 (26 ações), SELL: Δ 0.0000 (2 ações)
| Jogador 6 | 65 | 8 | 7 | 50 | 0.0089 | -0.0231 | 0.0025 | 0.3879 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ -0.0200 (9 ações), BUY_XP: Δ 0.0000 (17 ações), MOVE_BENCH: Δ 0.0512 (12 ações), MOVE_BOARD: Δ 0.0410 (2 ações), PASS: Δ 0.0000 (23 ações), SELL: Δ 0.0300 (2 ações)
| Jogador 7 | 79 | 12 | 12 | 55 | -0.0025 | -0.6523 | -0.0081 | 0.4377 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (1 ações), BUY: Δ -0.0375 (11 ações), BUY_XP: Δ 0.0000 (19 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0488 (17 ações), MOVE_BOARD: Δ -0.1540 (4 ações), PASS: Δ 0.0000 (26 ações)
| Jogador 8 | 100 | 11 | 11 | 78 | -0.0020 | -0.2142 | -0.0052 | 0.3638 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: ANVIL_CHOICE: Δ 0.0000 (1 ações), BUY: Δ -0.0129 (14 ações), BUY_XP: Δ 0.0000 (27 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), MOVE_BENCH: Δ -0.0092 (23 ações), MOVE_BOARD: Δ 0.0432 (3 ações), PASS: Δ 0.0000 (28 ações), SELL: Δ 0.0200 (3 ações)

A pontuação é uma heurística para auditoria, não uma verdade absoluta. Compare-a com recompensas e resultados de combate; correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 143 | OK (143) | 2 | 0 | 0 | 1 | 2 | 1 |
- Jogador 1 — IDs equipados observados: TFT_Item_IonicSpark, TFT_Item_UnstableConcoction; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 3, COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
| Jogador 2 | 183 | OK (183) | 3 | 0 | 0 | 1 | 3 | 1 |
- Jogador 2 — IDs equipados observados: TFT_Item_BlueBuff, TFT_Item_GuardianAngel, TFT_Item_IonicSpark; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 5, COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
| Jogador 3 | 120 | OK (120) | 1 | 0 | 0 | 1 | 1 | 0 |
- Jogador 3 — IDs equipados observados: TFT_Item_JeweledGauntlet; eventos: COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
| Jogador 4 | 170 | OK (170) | 3 | 0 | 0 | 1 | 3 | 1 |
- Jogador 4 — IDs equipados observados: TFT_Item_Deathblade, TFT_Item_Redemption; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 5, COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
| Jogador 5 | 106 | OK (106) | 0 | 0 | 0 | 3 | 0 | 0 |
- Jogador 5 — IDs equipados observados: nenhum observado; eventos: COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
| Jogador 6 | 87 | OK (87) | 0 | 0 | 0 | 2 | 0 | 0 |
- Jogador 6 — IDs equipados observados: nenhum observado; eventos: COMPONENT_LOOT_GRANTED: 16.
| Jogador 7 | 104 | OK (104) | 1 | 0 | 0 | 1 | 1 | 0 |
- Jogador 7 — IDs equipados observados: TFT_Item_JeweledGauntlet; eventos: COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.
| Jogador 8 | 127 | OK (127) | 1 | 0 | 0 | 1 | 1 | 0 |
- Jogador 8 — IDs equipados observados: TFT_Item_Crownguard; eventos: COMPONENT_ANVIL_GRANTED: 7, COMPONENT_LOOT_GRANTED: 16.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.126 | 0.000 |
| Jogador 1 | 1-2 | 6 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | 0.002 | 0.000 |
| Jogador 1 | 1-3 | 4 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 3 → 4 | 2 | 3 → 3 | -0.170 | 0.000 |
| Jogador 1 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 4 → 8 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 1 | 2-1 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 8 → 8 | 6 | 4 → 4 | 0.095 | 0.456 |
| Jogador 1 | 2-2 | 5 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 14% → 14% | 8 → 11 | 2 | 4 → 4 | 0.027 | -0.506 |
| Jogador 1 | 2-3 | 11 | 4.000 | -4.000 | 0 → 1 | 1 → 0 | 14% → 14% | 11 → 7 | 12 | 4 → 5 | 0.011 | -0.216 |
| Jogador 1 | 2-4 | 5 | 6.000 | 0.000 | 1 → 1 | 0 → 0 | 14% → 18% | 7 → 6 | 7 | 5 → 5 | 0.053 | 0.000 |
| Jogador 1 | 2-5 | 6 | 0.000 | 4.000 | 1 → 1 | 0 → 1 | 18% → 18% | 6 → 6 | 6 | 5 → 6 | -0.007 | -0.413 |
| Jogador 1 | 2-6 | 5 | 4.000 | 2.000 | 1 → 1 | 1 → 2 | 18% → 21% | 6 → 9 | 3 | 6 → 6 | 0.008 | 0.541 |
| Jogador 1 | 2-7 | 4 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 21% → 21% | 9 → 6 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 3-1 | 3 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 21% → 21% | 6 → 9 | 4 | 6 → 6 | 0.000 | 0.937 |
| Jogador 1 | 3-2 | 4 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 21% → 21% | 9 → 8 | 8 | 6 → 6 | 0.000 | 0.725 |
| Jogador 1 | 3-3 | 5 | 6.000 | -6.000 | 1 → 1 | 2 → 2 | 21% → 25% | 8 → 7 | 8 | 6 → 7 | -0.027 | 0.552 |
| Jogador 1 | 3-4 | 2 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 7 → 13 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 3-5 | 10 | 6.000 | 0.000 | 1 → 2 | 2 → 1 | 25% → 25% | 13 → 5 | 13 | 7 → 7 | -0.032 | -0.268 |
| Jogador 1 | 3-6 | 4 | -2.000 | 6.000 | 2 → 2 | 1 → 1 | 25% → 25% | 5 → 9 | 2 | 7 → 7 | 0.001 | 0.713 |
| Jogador 1 | 3-7 | 10 | 6.000 | -6.000 | 2 → 3 | 1 → 0 | 25% → 25% | 9 → 7 | 7 | 7 → 7 | 0.025 | 0.000 |
| Jogador 1 | 4-1 | 5 | 0.000 | 6.000 | 3 → 3 | 0 → 1 | 25% → 25% | 7 → 7 | 7 | 7 → 7 | 0.000 | 0.560 |
| Jogador 1 | 4-2 | 3 | 0.000 | 0.000 | 3 → 3 | 1 → 1 | 25% → 25% | 7 → 8 | 4 | 7 → 7 | 0.000 | -0.938 |
| Jogador 1 | 4-3 | 4 | 0.000 | 0.000 | 3 → 3 | 1 → 1 | 25% → 25% | 8 → 6 | 8 | 7 → 7 | 0.000 | -0.669 |
| Jogador 1 | 4-4 | 3 | 0.000 | 0.000 | 3 → 3 | 1 → 1 | 25% → 25% | 6 → 8 | 4 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 4-5 | 5 | 6.000 | -6.000 | 3 → 3 | 1 → 1 | 25% → 29% | 8 → 6 | 8 | 7 → 8 | -0.008 | 0.577 |
| Jogador 1 | 4-6 | 3 | 0.000 | 8.000 | 3 → 3 | 1 → 1 | 29% → 29% | 6 → 9 | 4 | 8 → 8 | 0.000 | 0.961 |
| Jogador 1 | 4-7 | 4 | 0.000 | 8.000 | 3 → 3 | 1 → 1 | 29% → 29% | 9 → 7 | 8 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 5-1 | 4 | 0.000 | 6.000 | 3 → 3 | 1 → 1 | 29% → 29% | 7 → 10 | 3 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 5-2 | 2 | 0.000 | 0.000 | 3 → 3 | 1 → 1 | 29% → 29% | 10 → 16 | 0 | 8 → 8 | 0.000 | -1.375 |
| Jogador 1 | 5-3 | 3 | 0.000 | 8.000 | 3 → 3 | 1 → 2 | 29% → 29% | 16 → 19 | 4 | 8 → 8 | 0.000 | 0.991 |
| Jogador 1 | 5-4 | 2 | 0.000 | 0.000 | 3 → 3 | 2 → 2 | 29% → 29% | 19 → 25 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 5-5 | 2 | 0.000 | 0.000 | 3 → 3 | 2 → 2 | 29% → 29% | 25 → 32 | 0 | 8 → 8 | 0.000 | -1.425 |
| Jogador 1 | 5-6 | 2 | 0.000 | 0.000 | 3 → 3 | 2 → 2 | 29% → 29% | 32 → 41 | 0 | 8 → 8 | 0.000 | -1.375 |
| Jogador 1 | 5-7 | 2 | 0.000 | 0.000 | 3 → 3 | 2 → 2 | 29% → 29% | 41 → 51 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 1 | 6-1 | 5 | -48.000 | -30.000 | 3 → 0 | 2 → 0 | 29% → 0% | 51 → 49 | 2 | 8 → 8 | -0.113 | -0.580 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 2, COMPOSITION_COMPATIBILITY: 8, IMMEDIATE_UPGRADE: 3, PAIR_POTENTIAL: 6; mudanças de composição: 1; posicionamento melhorou em 16 ações e piorou em 21.
- Jogador 1 — estado final: ouro 49, nível 8, vida 2.0, colocação None.
| Jogador 2 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.076 | 0.000 |
| Jogador 2 | 1-2 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | 0.028 | 0.000 |
| Jogador 2 | 1-3 | 5 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 7% → 11% | 3 → 4 | 2 | 3 → 3 | -0.006 | 0.000 |
| Jogador 2 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 4 → 8 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 2 | 2-1 | 5 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 14% | 8 → 7 | 7 | 4 → 4 | -0.002 | 0.512 |
| Jogador 2 | 2-2 | 7 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 7 → 8 | 6 | 4 → 5 | -0.014 | 0.384 |
| Jogador 2 | 2-3 | 6 | 2.000 | 4.000 | 0 → 0 | 1 → 1 | 18% → 18% | 8 → 8 | 7 | 5 → 5 | 0.005 | 0.419 |
| Jogador 2 | 2-4 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 8 → 6 | 8 | 5 → 5 | 0.000 | 0.000 |
| Jogador 2 | 2-5 | 4 | 4.000 | -4.000 | 0 → 0 | 1 → 1 | 18% → 21% | 6 → 9 | 4 | 5 → 6 | -0.008 | 0.701 |
| Jogador 2 | 2-6 | 6 | 2.000 | 4.000 | 0 → 0 | 1 → 2 | 21% → 21% | 9 → 10 | 7 | 6 → 6 | 0.000 | 0.459 |
| Jogador 2 | 2-7 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 10 → 9 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 3-1 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 9 → 10 | 8 | 6 → 6 | 0.000 | 0.738 |
| Jogador 2 | 3-2 | 7 | 4.000 | -4.000 | 0 → 0 | 2 → 2 | 21% → 25% | 10 → 11 | 8 | 6 → 7 | -0.000 | 0.426 |
| Jogador 2 | 3-3 | 9 | 4.000 | 8.000 | 0 → 0 | 2 → 2 | 25% → 25% | 11 → 10 | 12 | 7 → 7 | 0.007 | 0.337 |
| Jogador 2 | 3-4 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 10 → 10 | 8 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 3-5 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 10 → 11 | 8 | 7 → 7 | 0.000 | 0.738 |
| Jogador 2 | 3-6 | 6 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 11 → 12 | 12 | 7 → 7 | -0.010 | 0.492 |
| Jogador 2 | 3-7 | 5 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 25% | 12 → 8 | 12 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 4-1 | 5 | 8.000 | 0.000 | 0 → 0 | 2 → 2 | 25% → 29% | 8 → 9 | 8 | 7 → 8 | 0.063 | 0.607 |
| Jogador 2 | 4-2 | 6 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 9 → 10 | 12 | 8 → 8 | 0.000 | 0.506 |
| Jogador 2 | 4-3 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 10 → 11 | 8 | 8 → 8 | 0.000 | 0.746 |
| Jogador 2 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 11 → 20 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 4-5 | 7 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 20 → 5 | 20 | 8 → 8 | 0.000 | -0.388 |
| Jogador 2 | 4-6 | 3 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 5 → 7 | 4 | 8 → 8 | 0.000 | -0.905 |
| Jogador 2 | 4-7 | 3 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 7 → 9 | 4 | 8 → 8 | 0.000 | 0.000 |
| Jogador 2 | 5-1 | 7 | 8.000 | -8.000 | 0 → 0 | 2 → 2 | 29% → 32% | 9 → 7 | 8 | 8 → 9 | -0.006 | 0.436 |
| Jogador 2 | 5-2 | 3 | 0.000 | 10.000 | 0 → 0 | 2 → 2 | 32% → 32% | 7 → 9 | 5 | 9 → 9 | 0.000 | 0.968 |
| Jogador 2 | 5-3 | 7 | 8.000 | -10.000 | 0 → 1 | 2 → 1 | 32% → 32% | 9 → 10 | 11 | 9 → 9 | -0.082 | 0.435 |
| Jogador 2 | 5-4 | 4 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 32% → 32% | 10 → 9 | 7 | 9 → 9 | 0.000 | 0.000 |
| Jogador 2 | 5-5 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 32% → 32% | 9 → 17 | 0 | 9 → 9 | 0.000 | 1.523 |
| Jogador 2 | 5-6 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 32% → 32% | 17 → 26 | 0 | 9 → 9 | 0.000 | 1.468 |
| Jogador 2 | 5-7 | 3 | 0.000 | 8.000 | 1 → 1 | 1 → 2 | 32% → 32% | 26 → 31 | 4 | 9 → 9 | 0.000 | 0.000 |
| Jogador 2 | 6-1 | 4 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 32% → 32% | 31 → 41 | 0 | 9 → 9 | 0.000 | 0.000 |
| Jogador 2 | 6-2 | 2 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 32% → 32% | 41 → 50 | 0 | 9 → 9 | 0.000 | -1.375 |
| Jogador 2 | 6-3 | 12 | -8.000 | 8.000 | 1 → 1 | 2 → 1 | 32% → 29% | 50 → 17 | 40 | 9 → 9 | 0.004 | -0.237 |
| Jogador 2 | 6-4 | 3 | 6.000 | 2.000 | 1 → 1 | 1 → 1 | 29% → 32% | 17 → 20 | 4 | 9 → 9 | 0.016 | 0.000 |
| Jogador 2 | 6-5 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 32% → 32% | 20 → 28 | 0 | 9 → 10 | 0.000 | -1.375 |
| Jogador 2 | 6-6 | 4 | 10.000 | 0.000 | 1 → 1 | 1 → 1 | 32% → 36% | 28 → 31 | 5 | 10 → 10 | -0.002 | 0.749 |
| Jogador 2 | 6-7 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 36% → 36% | 31 → 39 | 0 | 10 → 10 | 0.000 | 0.000 |
| Jogador 2 | 7-1 | 4 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 36% → 36% | 39 → 40 | 0 | 10 → 10 | 0.000 | 0.758 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 2, COMPOSITION_COMPATIBILITY: 13, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 3; mudanças de composição: 0; posicionamento melhorou em 12 ações e piorou em 12.
- Jogador 2 — estado final: ouro 40, nível 10, vida 23.0, colocação 1.
| Jogador 3 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.126 | 0.000 |
| Jogador 3 | 1-2 | 6 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | 0.002 | 0.000 |
| Jogador 3 | 1-3 | 4 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 7% → 11% | 3 → 5 | 1 | 3 → 3 | 0.022 | 0.000 |
| Jogador 3 | 1-4 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 5 → 5 | 4 | 3 → 4 | 0.000 | 0.000 |
| Jogador 3 | 2-1 | 5 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 14% | 5 → 9 | 2 | 4 → 4 | -0.003 | 0.502 |
| Jogador 3 | 2-2 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 9 → 14 | 0 | 4 → 4 | 0.000 | -1.155 |
| Jogador 3 | 2-3 | 6 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 14 → 9 | 11 | 4 → 5 | 0.006 | -0.395 |
| Jogador 3 | 2-4 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 9 → 7 | 8 | 5 → 5 | 0.000 | 0.000 |
| Jogador 3 | 2-5 | 6 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 21% | 7 → 6 | 7 | 5 → 6 | -0.053 | -0.405 |
| Jogador 3 | 2-6 | 4 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 21% → 21% | 6 → 7 | 5 | 6 → 6 | 0.000 | -0.646 |
| Jogador 3 | 2-7 | 3 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 7 → 9 | 4 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 3-1 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 9 → 8 | 8 | 6 → 6 | 0.000 | -0.658 |
| Jogador 3 | 3-2 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 8 → 8 | 8 | 6 → 7 | 0.000 | -0.681 |
| Jogador 3 | 3-3 | 5 | 2.000 | -2.000 | 0 → 0 | 2 → 2 | 21% → 25% | 8 → 14 | 0 | 7 → 7 | -0.083 | 0.572 |
| Jogador 3 | 3-4 | 6 | 4.000 | 2.000 | 0 → 0 | 2 → 2 | 25% → 25% | 14 → 8 | 11 | 7 → 7 | 0.001 | 0.000 |
| Jogador 3 | 3-5 | 7 | 2.000 | 4.000 | 0 → 0 | 2 → 1 | 25% → 25% | 8 → 8 | 8 | 7 → 7 | -0.012 | 0.414 |
| Jogador 3 | 3-6 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 8 → 7 | 8 | 7 → 7 | 0.000 | 0.733 |
| Jogador 3 | 3-7 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 7 → 9 | 4 | 7 → 7 | 0.000 | 0.000 |
| Jogador 3 | 4-1 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 9 → 6 | 8 | 7 → 7 | 0.000 | -0.721 |
| Jogador 3 | 4-2 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 6 → 8 | 4 | 7 → 7 | 0.000 | -0.875 |
| Jogador 3 | 4-3 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 8 → 14 | 0 | 7 → 7 | 0.000 | 1.400 |
| Jogador 3 | 4-4 | 5 | 6.000 | -6.000 | 0 → 0 | 1 → 1 | 25% → 29% | 14 → 16 | 4 | 7 → 8 | 0.019 | 0.000 |
| Jogador 3 | 4-5 | 6 | 0.000 | 6.000 | 0 → 0 | 1 → 2 | 29% → 29% | 16 → 6 | 15 | 8 → 8 | 0.000 | -0.458 |
| Jogador 3 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 6 → 12 | 0 | 8 → 8 | 0.000 | 1.442 |
| Jogador 3 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 12 → 18 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 3 | 5-1 | 8 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 18 → 9 | 16 | 8 → 8 | 0.000 | 0.369 |
| Jogador 3 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 9 → 15 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 3 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 15 → 21 | 0 | 8 → 8 | 0.000 | -1.425 |
| Jogador 3 | 5-4 | 3 | 0.000 | 6.000 | 0 → 0 | 2 → 3 | 29% → 29% | 21 → 24 | 3 | 8 → 8 | 0.000 | 0.000 |
| Jogador 3 | 5-5 | 3 | -36.000 | -12.000 | 0 → 0 | 3 → 0 | 29% → 0% | 24 → 21 | 3 | 8 → 8 | 0.072 | -0.950 |
- Jogador 3 — valor marginal das compras: COMPOSITION_COMPATIBILITY: 6, PAIR_POTENTIAL: 5; mudanças de composição: 0; posicionamento melhorou em 10 ações e piorou em 9.
- Jogador 3 — estado final: ouro 21, nível 8, vida 1.0, colocação None.
| Jogador 4 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.126 | 0.000 |
| Jogador 4 | 1-2 | 6 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | 0.002 | 0.000 |
| Jogador 4 | 1-3 | 4 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 3 → 4 | 2 | 3 → 3 | -0.170 | 0.000 |
| Jogador 4 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 4 → 8 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 4 | 2-1 | 8 | 4.000 | 0.000 | 0 → 1 | 0 → 0 | 11% → 11% | 8 → 9 | 4 | 4 → 4 | -0.029 | -0.322 |
| Jogador 4 | 2-2 | 5 | 6.000 | 0.000 | 1 → 1 | 0 → 0 | 11% → 14% | 9 → 8 | 7 | 4 → 4 | 0.017 | -0.494 |
| Jogador 4 | 2-3 | 5 | 4.000 | 0.000 | 1 → 1 | 0 → 0 | 14% → 18% | 8 → 8 | 6 | 4 → 5 | 0.023 | -0.496 |
| Jogador 4 | 2-4 | 5 | 0.000 | 4.000 | 1 → 1 | 0 → 0 | 18% → 18% | 8 → 8 | 6 | 5 → 5 | 0.000 | 0.000 |
| Jogador 4 | 2-5 | 6 | 2.000 | 0.000 | 1 → 1 | 0 → 1 | 18% → 18% | 8 → 9 | 7 | 5 → 5 | -0.024 | -0.439 |
| Jogador 4 | 2-6 | 6 | 4.000 | 2.000 | 1 → 1 | 1 → 1 | 18% → 21% | 9 → 9 | 7 | 5 → 6 | -0.033 | -0.423 |
| Jogador 4 | 2-7 | 4 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 21% → 21% | 9 → 8 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 3-1 | 7 | 2.000 | -2.000 | 1 → 1 | 1 → 1 | 21% → 21% | 8 → 6 | 10 | 6 → 6 | 0.000 | 0.402 |
| Jogador 4 | 3-2 | 5 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 21% → 21% | 6 → 7 | 6 | 6 → 6 | -0.012 | -0.507 |
| Jogador 4 | 3-3 | 3 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 21% → 21% | 7 → 9 | 4 | 6 → 6 | 0.000 | -0.955 |
| Jogador 4 | 3-4 | 5 | 4.000 | -4.000 | 1 → 1 | 1 → 1 | 21% → 25% | 9 → 7 | 8 | 6 → 7 | 0.010 | 0.000 |
| Jogador 4 | 3-5 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 7 → 13 | 0 | 7 → 7 | 0.000 | 1.425 |
| Jogador 4 | 3-6 | 7 | 0.000 | 4.000 | 1 → 1 | 1 → 2 | 25% → 25% | 13 → 10 | 10 | 7 → 7 | 0.002 | 0.407 |
| Jogador 4 | 3-7 | 5 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 10 → 8 | 8 | 7 → 7 | 0.011 | 0.000 |
| Jogador 4 | 4-1 | 5 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 8 → 7 | 8 | 7 → 7 | 0.000 | 0.560 |
| Jogador 4 | 4-2 | 3 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 7 → 10 | 4 | 7 → 7 | 0.000 | 0.933 |
| Jogador 4 | 4-3 | 7 | -2.000 | 2.000 | 1 → 1 | 2 → 2 | 25% → 25% | 10 → 10 | 11 | 7 → 8 | 0.063 | 0.407 |
| Jogador 4 | 4-4 | 5 | 6.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 29% | 10 → 10 | 7 | 8 → 8 | 0.011 | 0.000 |
| Jogador 4 | 4-5 | 4 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 29% → 29% | 10 → 12 | 7 | 8 → 8 | 0.000 | 0.728 |
| Jogador 4 | 4-6 | 8 | 4.000 | -4.000 | 1 → 1 | 3 → 2 | 29% → 29% | 12 → 11 | 10 | 8 → 8 | -0.081 | 0.370 |
| Jogador 4 | 4-7 | 2 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 29% → 29% | 11 → 20 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 4 | 5-1 | 8 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 29% → 29% | 20 → 6 | 19 | 8 → 8 | -0.000 | -0.363 |
| Jogador 4 | 5-2 | 2 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 29% → 29% | 6 → 12 | 0 | 8 → 8 | 0.000 | 1.511 |
| Jogador 4 | 5-3 | 5 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 29% → 29% | 12 → 5 | 12 | 8 → 8 | 0.000 | 0.000 |
| Jogador 4 | 5-4 | 2 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 29% → 29% | 5 → 10 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 4 | 5-5 | 2 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 29% → 29% | 10 → 18 | 0 | 8 → 8 | 0.000 | 1.503 |
| Jogador 4 | 5-6 | 2 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 29% → 29% | 18 → 25 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 4 | 5-7 | 2 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 29% → 29% | 25 → 33 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 4 | 6-1 | 5 | 6.000 | -6.000 | 1 → 1 | 3 → 3 | 29% → 32% | 33 → 39 | 4 | 8 → 9 | 0.009 | 0.619 |
| Jogador 4 | 6-2 | 3 | 0.000 | 10.000 | 1 → 1 | 3 → 3 | 32% → 32% | 39 → 44 | 5 | 9 → 9 | 0.000 | 0.978 |
| Jogador 4 | 6-3 | 3 | 0.000 | 4.000 | 1 → 1 | 3 → 3 | 32% → 32% | 44 → 54 | 2 | 9 → 9 | -0.020 | 1.019 |
| Jogador 4 | 6-4 | 2 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 32% → 32% | 54 → 66 | 0 | 9 → 9 | 0.000 | 0.000 |
| Jogador 4 | 6-5 | 2 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 32% → 32% | 66 → 80 | 0 | 9 → 9 | 0.000 | 1.468 |
| Jogador 4 | 6-6 | 3 | 0.000 | 10.000 | 1 → 1 | 3 → 3 | 32% → 32% | 80 → 85 | 5 | 9 → 9 | 0.000 | -0.933 |
| Jogador 4 | 6-7 | 3 | 0.000 | 8.000 | 1 → 1 | 3 → 3 | 32% → 32% | 85 → 91 | 4 | 9 → 9 | -0.020 | 0.000 |
| Jogador 4 | 7-1 | 5 | -48.000 | -40.000 | 1 → 0 | 3 → 0 | 32% → 0% | 91 → 87 | 4 | 9 → 9 | 0.166 | -0.560 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 1, COMPOSITION_COMPATIBILITY: 14, IMMEDIATE_UPGRADE: 2, PAIR_POTENTIAL: 5; mudanças de composição: 0; posicionamento melhorou em 14 ações e piorou em 15.
- Jogador 4 — estado final: ouro 87, nível 9, vida 15.0, colocação None.
| Jogador 5 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.126 | 0.000 |
| Jogador 5 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.014 | 0.000 |
| Jogador 5 | 1-3 | 4 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.066 | 0.000 |
| Jogador 5 | 1-4 | 5 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.016 | 0.000 |
| Jogador 5 | 2-1 | 6 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 5 → 7 | 3 | 4 → 4 | -0.060 | -0.404 |
| Jogador 5 | 2-2 | 6 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 7 → 8 | 7 | 4 → 4 | 0.000 | -0.404 |
| Jogador 5 | 2-3 | 5 | 4.000 | -4.000 | 0 → 0 | 0 → 0 | 14% → 18% | 8 → 6 | 8 | 4 → 5 | -0.012 | 0.502 |
| Jogador 5 | 2-4 | 4 | 2.000 | 4.000 | 0 → 0 | 0 → 0 | 18% → 18% | 6 → 8 | 3 | 5 → 5 | 0.130 | 0.000 |
| Jogador 5 | 2-5 | 5 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 8 → 5 | 8 | 5 → 6 | 0.033 | -0.527 |
| Jogador 5 | 2-6 | 5 | 4.000 | -4.000 | 0 → 0 | 0 → 0 | 18% → 21% | 5 → 7 | 4 | 6 → 6 | 0.027 | -0.464 |
| Jogador 5 | 2-7 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 21% → 21% | 7 → 7 | 6 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 3-1 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 7 → 9 | 4 | 6 → 6 | 0.000 | -0.894 |
| Jogador 5 | 3-2 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 21% → 21% | 9 → 7 | 8 | 6 → 6 | 0.000 | 0.679 |
| Jogador 5 | 3-3 | 5 | 0.000 | 4.000 | 0 → 0 | 1 → 0 | 21% → 21% | 7 → 6 | 8 | 6 → 6 | 0.000 | -0.537 |
| Jogador 5 | 3-4 | 5 | 8.000 | -8.000 | 0 → 0 | 0 → 0 | 21% → 25% | 6 → 7 | 4 | 6 → 7 | -0.028 | 0.000 |
| Jogador 5 | 3-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 7 → 13 | 0 | 7 → 7 | 0.000 | 1.442 |
| Jogador 5 | 3-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 13 → 19 | 0 | 7 → 7 | 0.000 | -1.338 |
| Jogador 5 | 3-7 | 7 | 0.000 | 6.000 | 0 → 0 | 0 → 1 | 25% → 25% | 19 → 5 | 19 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 4-1 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 5 → 11 | 0 | 7 → 7 | 0.000 | 1.442 |
| Jogador 5 | 4-2 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 11 → 8 | 8 | 7 → 7 | 0.000 | -0.721 |
| Jogador 5 | 4-3 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 8 → 14 | 0 | 7 → 7 | 0.000 | -1.313 |
| Jogador 5 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 14 → 21 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 4-5 | 7 | 6.000 | -6.000 | 0 → 0 | 1 → 1 | 25% → 29% | 21 → 11 | 16 | 7 → 8 | 0.004 | 0.426 |
| Jogador 5 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 11 → 17 | 0 | 8 → 8 | 0.000 | -1.357 |
| Jogador 5 | 4-7 | 3 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 29% → 29% | 17 → 20 | 3 | 8 → 8 | 0.000 | 0.000 |
| Jogador 5 | 5-1 | 4 | -42.000 | -6.000 | 0 → 0 | 1 → 0 | 29% → 0% | 20 → 16 | 4 | 8 → 8 | -0.141 | -0.700 |
- Jogador 5 — valor marginal das compras: COMPOSITION_COMPATIBILITY: 9, PAIR_POTENTIAL: 2; mudanças de composição: 0; posicionamento melhorou em 8 ações e piorou em 11.
- Jogador 5 — estado final: ouro 16, nível 8, vida 10.0, colocação None.
| Jogador 6 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.076 | 0.000 |
| Jogador 6 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.003 | 0.000 |
| Jogador 6 | 1-3 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 5 | 0 | 3 → 3 | 0.015 | 0.000 |
| Jogador 6 | 1-4 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 5 → 5 | 4 | 3 → 4 | 0.000 | 0.000 |
| Jogador 6 | 2-1 | 5 | 2.000 | 0.000 | 0 → 0 | 1 → 2 | 11% → 14% | 5 → 5 | 5 | 4 → 5 | -0.024 | -0.474 |
| Jogador 6 | 2-2 | 4 | 6.000 | 0.000 | 0 → 0 | 2 → 2 | 14% → 18% | 5 → 8 | 3 | 5 → 5 | -0.067 | 0.653 |
| Jogador 6 | 2-3 | 5 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 18% → 18% | 8 → 8 | 7 | 5 → 5 | 0.033 | 0.537 |
| Jogador 6 | 2-4 | 6 | 4.000 | -4.000 | 0 → 0 | 2 → 3 | 18% → 18% | 8 → 14 | 3 | 5 → 5 | 0.019 | 0.000 |
| Jogador 6 | 2-5 | 6 | 2.000 | -2.000 | 0 → 0 | 3 → 3 | 18% → 21% | 14 → 9 | 12 | 5 → 6 | -0.009 | 0.440 |
| Jogador 6 | 2-6 | 4 | 0.000 | 6.000 | 0 → 0 | 3 → 3 | 21% → 21% | 9 → 7 | 7 | 6 → 6 | -0.015 | -0.607 |
| Jogador 6 | 2-7 | 4 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 21% → 21% | 7 → 8 | 4 | 6 → 6 | 0.009 | 0.000 |
| Jogador 6 | 3-1 | 4 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 21% → 21% | 8 → 6 | 8 | 6 → 6 | 0.000 | -0.694 |
| Jogador 6 | 3-2 | 3 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 21% → 21% | 6 → 8 | 4 | 6 → 6 | 0.000 | -0.846 |
| Jogador 6 | 3-3 | 5 | 6.000 | -6.000 | 0 → 0 | 3 → 3 | 21% → 25% | 8 → 6 | 8 | 6 → 7 | 0.063 | -0.517 |
| Jogador 6 | 3-4 | 2 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 25% → 25% | 6 → 12 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 3-5 | 5 | 0.000 | 6.000 | 0 → 0 | 3 → 4 | 25% → 25% | 12 → 8 | 11 | 7 → 7 | 0.000 | -0.543 |
| Jogador 6 | 3-6 | 4 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 8 → 8 | 8 | 7 → 7 | 0.000 | -0.691 |
| Jogador 6 | 3-7 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 8 → 16 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 4-1 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 16 → 25 | 0 | 7 → 7 | 0.000 | -1.313 |
| Jogador 6 | 4-2 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 25 → 33 | 0 | 7 → 7 | 0.000 | 1.400 |
| Jogador 6 | 4-3 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 33 → 41 | 0 | 7 → 7 | 0.000 | -1.416 |
| Jogador 6 | 4-4 | 2 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 25% → 25% | 41 → 50 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 4-5 | 2 | -26.000 | -6.000 | 0 → 0 | 4 → 0 | 25% → 0% | 50 → 50 | 0 | 7 → 7 | -0.288 | -1.400 |
- Jogador 6 — valor marginal das compras: COMPOSITION_COMPATIBILITY: 5, PAIR_POTENTIAL: 4; mudanças de composição: 0; posicionamento melhorou em 8 ações e piorou em 8.
- Jogador 6 — estado final: ouro 50, nível 7, vida 10.0, colocação None.
| Jogador 7 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.126 | 0.000 |
| Jogador 7 | 1-2 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | -0.146 | 0.000 |
| Jogador 7 | 1-3 | 6 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 7% → 11% | 3 → 5 | 1 | 3 → 3 | 0.004 | 0.000 |
| Jogador 7 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 5 → 9 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 7 | 2-1 | 6 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 14% | 9 → 8 | 6 | 4 → 4 | 0.001 | -0.404 |
| Jogador 7 | 2-2 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 8 → 14 | 0 | 4 → 4 | 0.000 | 1.215 |
| Jogador 7 | 2-3 | 2 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 14 → 20 | 0 | 4 → 5 | 0.000 | -1.265 |
| Jogador 7 | 2-4 | 8 | 8.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 20 → 5 | 20 | 5 → 5 | 0.024 | 0.000 |
| Jogador 7 | 2-5 | 6 | 2.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 21% | 5 → 6 | 5 | 5 → 6 | -0.021 | 0.467 |
| Jogador 7 | 2-6 | 5 | 2.000 | 2.000 | 0 → 0 | 1 → 2 | 21% → 21% | 6 → 7 | 6 | 6 → 6 | 0.009 | 0.492 |
| Jogador 7 | 2-7 | 3 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 7 → 9 | 4 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 3-1 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 9 → 6 | 8 | 6 → 6 | 0.000 | -0.658 |
| Jogador 7 | 3-2 | 3 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 6 → 8 | 4 | 6 → 6 | 0.000 | 0.905 |
| Jogador 7 | 3-3 | 5 | 2.000 | -2.000 | 0 → 0 | 2 → 2 | 21% → 25% | 8 → 7 | 8 | 6 → 7 | -0.011 | 0.570 |
| Jogador 7 | 3-4 | 11 | 6.000 | 0.000 | 0 → 1 | 2 → 1 | 25% → 25% | 7 → 8 | 5 | 7 → 7 | 0.005 | 0.000 |
| Jogador 7 | 3-5 | 5 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 25% → 25% | 8 → 6 | 7 | 7 → 7 | 0.003 | -0.545 |
| Jogador 7 | 3-6 | 3 | 0.000 | 8.000 | 1 → 1 | 1 → 1 | 25% → 25% | 6 → 8 | 4 | 7 → 7 | 0.000 | -0.925 |
| Jogador 7 | 3-7 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 8 → 14 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 4-1 | 5 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 14 → 8 | 12 | 7 → 7 | 0.000 | -0.525 |
| Jogador 7 | 4-2 | 4 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 8 → 6 | 8 | 7 → 7 | 0.000 | -0.656 |
| Jogador 7 | 4-3 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 6 → 13 | 0 | 7 → 7 | 0.000 | -1.400 |
| Jogador 7 | 4-4 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 13 → 21 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 4-5 | 2 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 25% → 25% | 21 → 31 | 0 | 7 → 7 | 0.000 | -1.407 |
| Jogador 7 | 4-6 | 3 | 0.000 | 6.000 | 1 → 1 | 1 → 2 | 25% → 25% | 31 → 38 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 4-7 | 2 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 25% → 25% | 38 → 49 | 0 | 7 → 7 | 0.000 | 0.000 |
| Jogador 7 | 5-1 | 4 | -30.000 | -20.000 | 1 → 0 | 2 → 0 | 25% → 0% | 49 → 49 | 0 | 7 → 7 | 0.050 | -0.712 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 1, COMPOSITION_COMPATIBILITY: 6, IMMEDIATE_UPGRADE: 1, PAIR_POTENTIAL: 3; mudanças de composição: 0; posicionamento melhorou em 13 ações e piorou em 12.
- Jogador 7 — estado final: ouro 49, nível 7, vida 10.0, colocação None.
| Jogador 8 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.126 | 0.000 |
| Jogador 8 | 1-2 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | 0.028 | 0.000 |
| Jogador 8 | 1-3 | 7 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 3 → 5 | 1 | 3 → 3 | -0.023 | 0.000 |
| Jogador 8 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 5 → 9 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 8 | 2-1 | 7 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 11% → 14% | 9 → 6 | 9 | 4 → 5 | -0.002 | 0.366 |
| Jogador 8 | 2-2 | 4 | 6.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 18% | 6 → 10 | 3 | 5 → 5 | 0.005 | 0.641 |
| Jogador 8 | 2-3 | 4 | 0.000 | 6.000 | 0 → 0 | 1 → 1 | 18% → 18% | 10 → 10 | 7 | 5 → 5 | -0.015 | 0.659 |
| Jogador 8 | 2-4 | 7 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 10 → 8 | 11 | 5 → 5 | 0.015 | 0.000 |
| Jogador 8 | 2-5 | 10 | 8.000 | -6.000 | 0 → 0 | 1 → 0 | 18% → 21% | 8 → 10 | 6 | 5 → 6 | -0.004 | 0.259 |
| Jogador 8 | 2-6 | 7 | 2.000 | 6.000 | 0 → 0 | 0 → 0 | 21% → 21% | 10 → 10 | 8 | 6 → 6 | 0.012 | 0.370 |
| Jogador 8 | 2-7 | 4 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 21% → 21% | 10 → 9 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 3-1 | 7 | 0.000 | 2.000 | 0 → 0 | 0 → 0 | 21% → 21% | 9 → 9 | 12 | 6 → 6 | -0.002 | 0.409 |
| Jogador 8 | 3-2 | 7 | 8.000 | -8.000 | 0 → 0 | 0 → 0 | 21% → 25% | 9 → 6 | 8 | 6 → 7 | -0.092 | -0.402 |
| Jogador 8 | 3-3 | 3 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 25% → 25% | 6 → 8 | 4 | 7 → 7 | 0.000 | -0.892 |
| Jogador 8 | 3-4 | 6 | 4.000 | 2.000 | 0 → 0 | 0 → 1 | 25% → 25% | 8 → 7 | 7 | 7 → 7 | 0.007 | 0.000 |
| Jogador 8 | 3-5 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 7 → 9 | 4 | 7 → 7 | 0.000 | -0.925 |
| Jogador 8 | 3-6 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 9 → 7 | 8 | 7 → 7 | 0.000 | -0.669 |
| Jogador 8 | 3-7 | 3 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 7 → 9 | 4 | 7 → 7 | 0.000 | 0.000 |
| Jogador 8 | 4-1 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 25% → 25% | 9 → 8 | 8 | 7 → 7 | 0.000 | -0.543 |
| Jogador 8 | 4-2 | 5 | 2.000 | -2.000 | 0 → 0 | 1 → 1 | 25% → 29% | 8 → 6 | 8 | 7 → 8 | -0.007 | 0.597 |
| Jogador 8 | 4-3 | 3 | 0.000 | 8.000 | 0 → 0 | 1 → 1 | 29% → 29% | 6 → 9 | 4 | 8 → 8 | 0.000 | 0.987 |
| Jogador 8 | 4-4 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 29% → 29% | 9 → 7 | 8 | 8 → 8 | 0.000 | 0.000 |
| Jogador 8 | 4-5 | 3 | 0.000 | 8.000 | 0 → 0 | 1 → 2 | 29% → 29% | 7 → 10 | 4 | 8 → 8 | 0.000 | 0.987 |
| Jogador 8 | 4-6 | 4 | 0.000 | 8.000 | 0 → 0 | 2 → 2 | 29% → 29% | 10 → 7 | 8 | 8 → 8 | 0.000 | -0.700 |
| Jogador 8 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 7 → 12 | 0 | 8 → 8 | 0.000 | 0.000 |
| Jogador 8 | 5-1 | 5 | 0.000 | 10.000 | 0 → 0 | 2 → 2 | 29% → 29% | 12 → 9 | 9 | 8 → 8 | 0.000 | 0.604 |
| Jogador 8 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 29% → 29% | 9 → 14 | 0 | 8 → 8 | 0.000 | -1.425 |
| Jogador 8 | 5-3 | 2 | -38.000 | -34.000 | 0 → 0 | 2 → 0 | 29% → 0% | 14 → 14 | 0 | 8 → 8 | 0.101 | -1.400 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 2, COMPOSITION_COMPATIBILITY: 9, PAIR_POTENTIAL: 3; mudanças de composição: 0; posicionamento melhorou em 12 ações e piorou em 11.
- Jogador 8 — estado final: ouro 14, nível 8, vida 14.0, colocação None.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Revertidas ≤1 ação | ≤2 ações | ≤4 ações | Ouro perdido | Upgrades | Vendas core/par | Valor médio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 19 | 1 | 0 | 0 | 0 | 0 | 3 | 0 | 6.2447 |
| Jogador 2 | 20 | 5 | 0 | 0 | 2 | 0 | 2 | 3 | 3.4124 |
| Jogador 3 | 11 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 2.9234 |
| Jogador 4 | 22 | 4 | 0 | 0 | 0 | 0 | 2 | 2 | 6.2154 |
| Jogador 5 | 11 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 3.0515 |
| Jogador 6 | 9 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 4.6551 |
| Jogador 7 | 11 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 5.1042 |
| Jogador 8 | 14 | 3 | 0 | 0 | 1 | 0 | 0 | 2 | 2.9075 |

Vendas de core/pares ignoradas antes da decisão da composição: **3**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Uma venda sem compra correspondente na janela é UNKNOWN; sequências ambíguas não são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| HIGH | Jogador 2 | 3-6 | 405 | SOLD_CORE_UNIT | Venda de 'DA_Nidalee18_AP' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 2 | 4-2 | 465 | SOLD_CORE_UNIT | Venda de 'DA_18_Ezreal' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 4-2 | 465 | PURCHASE_REVERSED | Compra de DA_18_Ezreal desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 2 | 5-3 | 622 | SOLD_CORE_UNIT | Venda de 'DA_18_Ashe' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 2 | 5-3 | 622 | PURCHASE_REVERSED | Compra de DA_18_Ashe desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 3 | 3-5 | 384 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 4 | 2-5 | 212 | SOLD_CORE_UNIT | Venda de 'DA_18_LeBlanc' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 4 | 4-3 | 486 | SOLD_CORE_UNIT | Venda de 'DA_CrimsonRaptor18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 3-3 | 338 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yunara' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 2-4 | 189 | PURCHASE_REVERSED | Compra de DA_18_Cassiopeia desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 2-5 | 214 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Leona' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 8 | 3-1 | 289 | SOLD_CORE_UNIT | Venda de 'DA_Krug18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
\n\n---\n\n## Evidências resumidas dos achados\n\nO relatório apresenta métricas agregadas e a timeline em tabelas. Esta seção complementa apenas os achados com o contexto mínimo da decisão; snapshots, máscaras brutas e diagnósticos completos não são duplicados em Markdown.\n\n### HIGH · SOLD_CORE_UNIT · Jogador 2 · 3-6 · step 405\n\nVenda de 'DA_Nidalee18_AP' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 100.0, nível 7, ouro 11, força 34.0\n- Composição: Colosso / DA_Amumu18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.47464242577552795, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_Nidalee18_AP, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 2 · 4-2 · step 465\n\nVenda de 'DA_18_Ezreal' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia WINSTREAK · motivo WINSTREAK: preservar vantagem atual\n- Estado: HP 100.0, nível 8, ouro 9, força 42.0\n- Composição: Colosso / DA_Amumu18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.2746615409851074, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Ezreal, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 2 · 4-2 · step 465\n\nCompra de DA_18_Ezreal desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia WINSTREAK · motivo WINSTREAK: preservar vantagem atual\n- Estado: HP 100.0, nível 8, ouro 9, força 42.0\n- Composição: Colosso / DA_Amumu18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.2746615409851074, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=447, cost=4, sale_gold_delta=4, net_gold_lost=0, fit_score=0.0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 2 · 5-3 · step 622\n\nVenda de 'DA_18_Ashe' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia ECON · motivo ECON: acumular até o limite de juros de 50\n- Estado: HP 76.0, nível 9, ouro 9, força 50.0\n- Composição: Colosso / DA_18_Ashe\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3772202730178833, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Ashe, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 2 · 5-3 · step 622\n\nCompra de DA_18_Ashe desfeita em 3 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia ECON · motivo ECON: acumular até o limite de juros de 50\n- Estado: HP 76.0, nível 9, ouro 9, força 50.0\n- Composição: Colosso / DA_18_Ashe\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.3772202730178833, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=602, cost=5, sale_gold_delta=5, net_gold_lost=0, fit_score=0.2237\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 3 · 3-5 · step 384\n\nVenda de 'DA_18_Yorick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 57.0, nível 7, ouro 8, força 28.0\n- Composição: Inferno / DA_18_Tristana\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.8229384422302246, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Yorick, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 4 · 2-5 · step 212\n\nVenda de 'DA_18_LeBlanc' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia SLOWROLL · motivo SLOWROLL: composição tem alvo de 3 estrelas\n- Estado: HP 83.0, nível 5, ouro 8, força 22.0\n- Composição: — / DA_Gromp18_AP\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.2985999882221222, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_LeBlanc, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 4 · 4-3 · step 486\n\nVenda de 'DA_CrimsonRaptor18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 48.0, nível 7, ouro 10, força 32.0\n- Composição: Fera do Rift / DA_Gromp18_AP\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.5323702692985535, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_CrimsonRaptor18, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 5 · 3-3 · step 338\n\nVenda de 'DA_18_Yunara' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia FAST8 · motivo FAST8: composição planejada exige nível 8\n- Estado: HP 68.0, nível 6, ouro 7, força 28.0\n- Composição: Florescer / DA_18_MasterYi_AD\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.8578464388847351, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Yunara, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### MEDIUM · PURCHASE_REVERSED · Jogador 8 · 2-4 · step 189\n\nCompra de DA_18_Cassiopeia desfeita em 4 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 5, ouro 10, força 14.0\n- Composição: — / DA_Krug18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.37844616174697876, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: buy_step=164, cost=3, sale_gold_delta=3, net_gold_lost=0, fit_score=0.0\n\n### MEDIUM · SOLD_UPGRADE_PAIR_COPY · Jogador 8 · 2-5 · step 214\n\nVenda de 'DA_18_Leona' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia SLOWROLL · motivo SLOWROLL: composição tem alvo de 3 estrelas\n- Estado: HP 100.0, nível 6, ouro 4, força 18.0\n- Composição: Colosso / DA_Krug18\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.7992685437202454, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_18_Leona, core_sale=False, pair_lost=True, composition_decision_round=2-5, same_star_copies_before=2, same_star_copies_after=1, higher_star_copies_before=0, higher_star_copies_after=0\n\n### HIGH · SOLD_CORE_UNIT · Jogador 8 · 3-1 · step 289\n\nVenda de 'DA_Krug18' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas.\n- Decisão: **SELL** · estratégia STABILIZE · motivo STABILIZE: tabuleiro fraco sob pressão\n- Estado: HP 100.0, nível 6, ouro 9, força 24.0\n- Composição: Colosso / DA_18_Soraka\n- Legalidade: tipo permitido True, ação validada True\n- Recompensas: ação -0.30052220821380615, combate 0.0, colocação 0.0\n- Unidades: +0 itens / -1 itens\n- Evidência adicional: champion=DA_Krug18, core_sale=True, pair_lost=False, composition_decision_round=2-5, same_star_copies_before=1, same_star_copies_after=0, higher_star_copies_before=0, higher_star_copies_after=0\n\n## Arquivos e rastreabilidade\n\n- Jogadores analisados: 8\n- Entradas analisadas: 3847\n- Decisões com timeline: 801\n- Achados: 12\n- Os arquivos estruturados de origem permanecem separados deste relatório.\n- Campos ausentes são exibidos como “—”; não são inferidos como zero.\n