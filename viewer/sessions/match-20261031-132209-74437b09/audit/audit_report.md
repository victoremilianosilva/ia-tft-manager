# Auditoria da partida TFT

- Arquivos lidos: **8**
- Jogadores encontrados: **8** (1, 2, 3, 4, 5, 6, 7, 8)
- Registros estruturados analisados: **5893**
- Achados: **129**
- CRITICAL: 0 | HIGH: 73 | MEDIUM: 56 | LOW: 0

## Auditoria decisão por decisão

| Jogador | Ações | Máscaras | Tipo permitido | Tipo bloqueado | Validação completa | Falhas | Estado completo | Recompensas completas | UUIDs observados | Adições/remoções |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 190 | 190 | 190 | 0 | 189 | 0 | 190 | 190 | 172 | 47/33 |
| Jogador 2 | 323 | 323 | 323 | 0 | 317 | 0 | 323 | 323 | 323 | 111/96 |
| Jogador 3 | 177 | 177 | 177 | 0 | 177 | 0 | 177 | 177 | 158 | 46/33 |
| Jogador 4 | 218 | 218 | 218 | 0 | 216 | 0 | 218 | 218 | 202 | 64/51 |
| Jogador 5 | 231 | 231 | 231 | 0 | 230 | 0 | 231 | 231 | 219 | 68/54 |
| Jogador 6 | 336 | 336 | 336 | 0 | 331 | 0 | 336 | 336 | 336 | 130/116 |
| Jogador 7 | 229 | 229 | 229 | 0 | 228 | 0 | 229 | 229 | 217 | 71/57 |
| Jogador 8 | 216 | 216 | 216 | 0 | 212 | 0 | 216 | 216 | 207 | 58/44 |

### Timeline

| Jogador | Round | Step | Ação | Estratégia | HP | Nível | Ouro | Juros | Força | Direção/foco | Tipos legais | Tipo permitido | Parâmetros válidos | Rew ação | Combate | Colocação | UUIDs adicionados/removidos |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| Jogador 1 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5021329522132874 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.13061420619487762 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Ornn | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.29660987854003906 | 0.0 | 0.0 | +2718f555-b782-4fea-a68f-31395ad34232 / -— |
| Jogador 1 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1886446326971054 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.9705333709716797 | 0.0 | 0.0 | +679fe281-674a-438b-bdcf-57229a283d44 / -— |
| Jogador 1 | 1-2 | 14 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 15 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13361181318759918 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5096037983894348 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.024840479716658592 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3182162940502167 | 0.0 | 0.0 | +24247863-54d4-4674-86e9-9a45609a440e / -— |
| Jogador 1 | 1-3 | 22 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36821627616882324 | 0.0 | 0.0 | +— / -24247863-54d4-4674-86e9-9a45609a440e |
| Jogador 1 | 1-3 | 23 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1178959608078003 | 0.0 | 0.0 | +c28def4c-cd00-4010-ac6f-0e6c90648294 / -2718f555-b782-4fea-a68f-31395ad34232,679fe281-674a-438b-bdcf-57229a283d44 |
| Jogador 1 | 1-4 | 32 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10690079629421234 | 0.0 | 0.0 | +— / -c28def4c-cd00-4010-ac6f-0e6c90648294 |
| Jogador 1 | 1-4 | 33 | BUY | STABILIZE | 100.0 | 3 | 7 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.96245938539505 | 0.0 | 0.0 | +6465b229-8025-4e7d-94de-1cd49fa76167 / -— |
| Jogador 1 | 1-4 | 34 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 6 | 0 | 2.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06143278628587723 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 35 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.14140035212039948 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 1-4 | 36 | PASS | STABILIZE | 100.0 | 3 | 6 | 0 | 4.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 4.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0366597175598145 | 0.0 | 0.0 | +c448b2c1-7854-4c8c-a51b-eca2791eb639 / -6465b229-8025-4e7d-94de-1cd49fa76167,ba82e61e-9068-4e02-b710-5419c194d2ff |
| Jogador 1 | 2-1 | 42 | SELL | STABILIZE | 100.0 | 4 | 9 | 0 | 0.0 | —/DA_18_Ornn | BUY, REROLL, BUY_XP, MOVE_BENCH, SELL, PASS | True | True | -0.2801482677459717 | 0.0 | 0.0 | +— / -c448b2c1-7854-4c8c-a51b-eca2791eb639 |
| Jogador 1 | 2-1 | 43 | BUY | STABILIZE | 100.0 | 4 | 12 | 1 | 0.0 | —/— | BUY, REROLL, BUY_XP, PASS | True | True | 0.17775502800941467 | 0.0 | 0.0 | +3a74be8d-bf7c-4449-9f1b-d76521e73e6f / -— |
| Jogador 1 | 2-1 | 44 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 0.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, SELL, PASS | True | True | 0.29821422696113586 | 0.0 | 0.0 | +57652644-f861-47bc-addd-90760a272b22 / -— |
| Jogador 1 | 2-1 | 45 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 0.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, SELL, PASS | True | True | 0.1713879406452179 | 0.0 | 0.0 | +714ff9e9-b401-4609-9304-4fd0767ff49f / -— |
| Jogador 1 | 2-1 | 46 | SELL | STABILIZE | 100.0 | 4 | 8 | 0 | 0.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, SELL, PASS | True | True | -0.4894615411758423 | 0.0 | 0.0 | +— / -714ff9e9-b401-4609-9304-4fd0767ff49f |
| Jogador 1 | 2-1 | 47 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 9 | 0 | 0.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, SELL, PASS | True | True | 0.24261941015720367 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-1 | 48 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 9 | 0 | 2.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3212747275829315 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 50 | BUY | STABILIZE | 94.0 | 4 | 14 | 1 | 6.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.953004777431488 | 0.0 | 0.0 | +7aea963f-f0a4-4fa2-8da0-cc5eb260f665 / -— |
| Jogador 1 | 2-2 | 51 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 12 | 1 | 6.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3044399619102478 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 52 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 12 | 1 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17400141060352325 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 53 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 12 | 1 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 54 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 12 | 1 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.15756447613239288 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 55 | BUY | STABILIZE | 94.0 | 4 | 12 | 1 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2626761198043823 | 0.0 | 0.0 | +3a43ff36-dccd-49a7-92d8-0b01e739ea89 / -— |
| Jogador 1 | 2-2 | 56 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 9 | 0 | 10.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4367840588092804 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 57 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.13701719045639038 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-2 | 58 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 60 | BUY | STABILIZE | 88.0 | 4 | 15 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.1134496927261353 | 0.0 | 0.0 | +6ddacda7-dc9f-4801-98c7-76762cb6d255 / -3a74be8d-bf7c-4449-9f1b-d76521e73e6f,7aea963f-f0a4-4fa2-8da0-cc5eb260f665 |
| Jogador 1 | 2-3 | 61 | BUY | STABILIZE | 88.0 | 4 | 13 | 1 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3958522379398346 | 0.0 | 0.0 | +475e5206-4f54-4bbb-9db9-99d1895f0887 / -— |
| Jogador 1 | 2-3 | 62 | MOVE_BENCH | STABILIZE | 88.0 | 4 | 11 | 1 | 8.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36082860827445984 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 63 | MOVE_BOARD | STABILIZE | 88.0 | 4 | 11 | 1 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15105898678302765 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 64 | MOVE_BENCH | STABILIZE | 88.0 | 4 | 11 | 1 | 12.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49788427352905273 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 65 | MOVE_BOARD | STABILIZE | 88.0 | 4 | 11 | 1 | 20.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.024840479716658592 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 66 | MOVE_BOARD | STABILIZE | 88.0 | 4 | 11 | 1 | 20.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.1500062346458435 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 67 | MOVE_BOARD | STABILIZE | 88.0 | 4 | 11 | 1 | 20.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06010375916957855 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-3 | 68 | MOVE_BOARD | STABILIZE | 88.0 | 4 | 11 | 1 | 20.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 70 | BUY | LOSS_STREAK | 83.0 | 4 | 18 | 1 | 20.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3330889642238617 | 0.0 | 0.0 | +0b62545c-1de0-47d8-bb4c-119f7e1526b3 / -— |
| Jogador 1 | 2-4 | 71 | MOVE_BOARD | LOSS_STREAK | 83.0 | 4 | 15 | 1 | 20.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024840479716658592 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 72 | MOVE_BENCH | LOSS_STREAK | 83.0 | 4 | 15 | 1 | 20.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11572138220071793 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 73 | MOVE_BOARD | LOSS_STREAK | 83.0 | 4 | 15 | 1 | 24.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17727595567703247 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 74 | MOVE_BOARD | LOSS_STREAK | 83.0 | 4 | 15 | 1 | 24.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21587814390659332 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 75 | SELL | LOSS_STREAK | 83.0 | 4 | 15 | 1 | 24.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04486807435750961 | 0.0 | 0.0 | +— / -57652644-f861-47bc-addd-90760a272b22 |
| Jogador 1 | 2-4 | 76 | MOVE_BOARD | LOSS_STREAK | 83.0 | 4 | 16 | 1 | 24.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1782316118478775 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 77 | MOVE_BOARD | LOSS_STREAK | 83.0 | 4 | 16 | 1 | 24.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.30446532368659973 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-4 | 78 | MOVE_BOARD | LOSS_STREAK | 83.0 | 4 | 16 | 1 | 24.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09773150831460953 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 80 | BUY | LOSS_STREAK | 83.0 | 4 | 23 | 2 | 24.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8811041712760925 | 0.0 | 0.0 | +a72d427f-f2f7-46dd-97bf-d28999772db0 / -— |
| Jogador 1 | 2-5 | 81 | MOVE_BENCH | LOSS_STREAK | 83.0 | 4 | 21 | 2 | 24.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.003800456179305911 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 82 | MOVE_BENCH | STABILIZE | 83.0 | 4 | 21 | 2 | 22.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48693498969078064 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 83 | MOVE_BENCH | STABILIZE | 83.0 | 4 | 21 | 2 | 20.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2681412100791931 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-5 | 84 | PASS | STABILIZE | 83.0 | 4 | 21 | 2 | 24.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 89 | BUY | STABILIZE | 75.0 | 5 | 29 | 2 | 24.0 | Inferno/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9520237445831299 | 0.0 | 0.0 | +f84bb43d-db12-46dd-a15c-28ef8fdb7fa2 / -— |
| Jogador 1 | 2-6 | 90 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 26 | 2 | 24.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4655369818210602 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 91 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 26 | 2 | 30.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2894611060619354 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 92 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 26 | 2 | 28.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0948934555053711 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-6 | 93 | PASS | STABILIZE | 75.0 | 5 | 26 | 2 | 26.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 98 | MOVE_BENCH | SLOWROLL | 70.0 | 5 | 35 | 3 | 26.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24499467015266418 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 99 | MOVE_BENCH | SLOWROLL | 70.0 | 5 | 35 | 3 | 30.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2734600305557251 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 2-7 | 100 | PASS | SLOWROLL | 70.0 | 5 | 35 | 3 | 28.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 107 | MOVE_BENCH | SLOWROLL | 70.0 | 5 | 45 | 4 | 28.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0841873362660408 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 108 | MOVE_BENCH | SLOWROLL | 70.0 | 5 | 45 | 4 | 26.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17510750889778137 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-1 | 109 | PASS | SLOWROLL | 70.0 | 5 | 45 | 4 | 28.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 116 | BUY | SLOWROLL | 70.0 | 5 | 55 | 5 | 28.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26972660422325134 | 0.0 | 0.0 | +c30a99f5-ce2d-4bbf-9aab-93017ad40255 / -— |
| Jogador 1 | 3-2 | 117 | BUY | SLOWROLL | 70.0 | 5 | 51 | 5 | 28.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3090759813785553 | 0.0 | 0.0 | +4e116bc2-f686-4a17-adb1-a7b80865c159 / -— |
| Jogador 1 | 3-2 | 118 | REROLL | SLOWROLL | 70.0 | 5 | 48 | 4 | 28.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16095013916492462 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 119 | BUY | SLOWROLL | 70.0 | 5 | 46 | 4 | 28.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1249845027923584 | 0.0 | 0.0 | +e01be6cf-34fe-4057-aef3-c08c504794cf / -— |
| Jogador 1 | 3-2 | 120 | REROLL | SLOWROLL | 70.0 | 5 | 43 | 4 | 28.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05240010842680931 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 121 | REROLL | SLOWROLL | 70.0 | 5 | 41 | 4 | 28.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1889999955892563 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 122 | REROLL | SLOWROLL | 70.0 | 5 | 39 | 3 | 28.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07096321880817413 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-2 | 123 | BUY | SLOWROLL | 70.0 | 5 | 37 | 3 | 28.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8001536726951599 | 0.0 | 0.0 | +c5557e24-8174-4d79-9e22-c2cbbb8225a8 / -475e5206-4f54-4bbb-9db9-99d1895f0887,a72d427f-f2f7-46dd-97bf-d28999772db0 |
| Jogador 1 | 3-3 | 125 | BUY | SLOWROLL | 60.0 | 5 | 43 | 4 | 20.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07202175259590149 | 0.0 | 0.0 | +ccdd8153-af58-4fe7-994c-d49f0a7a17f8 / -— |
| Jogador 1 | 3-3 | 126 | BUY | SLOWROLL | 60.0 | 5 | 39 | 3 | 20.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14722415804862976 | 0.0 | 0.0 | +65a6d68c-90ae-4e31-8bbc-82e8ec75b3de / -— |
| Jogador 1 | 3-3 | 127 | BUY | SLOWROLL | 60.0 | 5 | 37 | 3 | 20.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6018231511116028 | 0.0 | 0.0 | +5a16a58c-7001-4448-8ca5-6293f35e2c94 / -— |
| Jogador 1 | 3-3 | 128 | REROLL | SLOWROLL | 60.0 | 5 | 35 | 3 | 20.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.045167457312345505 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 129 | BUY | SLOWROLL | 60.0 | 5 | 33 | 3 | 20.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2579173445701599 | 0.0 | 0.0 | +d69fa0dc-74b6-4ee7-90f7-aaca5405c59c / -— |
| Jogador 1 | 3-3 | 130 | REROLL | SLOWROLL | 60.0 | 5 | 30 | 3 | 20.0 | Cáustico/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027232719585299492 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-3 | 131 | SELL | STABILIZE | 60.0 | 5 | 28 | 2 | 20.0 | Cáustico/DA_18_Sejuani | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12523077428340912 | 0.0 | 0.0 | +— / -4e116bc2-f686-4a17-adb1-a7b80865c159 |
| Jogador 1 | 3-3 | 132 | MOVE_BENCH | SLOWROLL | 60.0 | 5 | 31 | 3 | 20.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20720700919628143 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 134 | BUY | SLOWROLL | 49.0 | 5 | 40 | 4 | 26.0 | Cáustico/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16375167667865753 | 0.0 | 0.0 | +f8d6cf7b-e18c-4a52-87c6-8858f03eef72 / -— |
| Jogador 1 | 3-4 | 135 | REROLL | SLOWROLL | 49.0 | 5 | 38 | 3 | 26.0 | Cáustico/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07010426372289658 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 136 | BUY | SLOWROLL | 49.0 | 5 | 36 | 3 | 26.0 | Cáustico/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7747560739517212 | 0.0 | 0.0 | +f394f34c-c68b-4213-9eb0-88f302976405 / -5a16a58c-7001-4448-8ca5-6293f35e2c94,65a6d68c-90ae-4e31-8bbc-82e8ec75b3de |
| Jogador 1 | 3-4 | 137 | REROLL | SLOWROLL | 49.0 | 5 | 34 | 3 | 26.0 | Cáustico/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.045226868242025375 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 138 | BUY | SLOWROLL | 49.0 | 5 | 32 | 3 | 26.0 | Cáustico/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1518922597169876 | 0.0 | 0.0 | +26462e09-ab6e-4b87-85a8-6bda974b0c45 / -— |
| Jogador 1 | 3-4 | 139 | REROLL | STABILIZE | 49.0 | 5 | 29 | 2 | 26.0 | Cáustico/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 140 | REROLL | STABILIZE | 49.0 | 5 | 27 | 2 | 26.0 | Cáustico/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-4 | 141 | MOVE_BENCH | STABILIZE | 49.0 | 5 | 25 | 2 | 26.0 | Cáustico/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6915828585624695 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 143 | BUY | SLOWROLL | 49.0 | 5 | 33 | 3 | 30.0 | Cáustico/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3656630218029022 | 0.0 | 0.0 | +83228c14-cadb-45b4-9893-2fb12c40f4a8 / -— |
| Jogador 1 | 3-5 | 144 | REROLL | STABILIZE | 49.0 | 5 | 29 | 2 | 30.0 | Cáustico/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 145 | BUY | STABILIZE | 49.0 | 5 | 27 | 2 | 30.0 | Cáustico/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29255375266075134 | 0.0 | 0.0 | +e60f0b7f-8510-4c67-9ebd-0d8be1b0ff2b / -— |
| Jogador 1 | 3-5 | 146 | REROLL | STABILIZE | 49.0 | 5 | 25 | 2 | 30.0 | Cáustico/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 147 | REROLL | STABILIZE | 49.0 | 5 | 23 | 2 | 30.0 | Cáustico/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 148 | REROLL | STABILIZE | 49.0 | 5 | 21 | 2 | 30.0 | Cáustico/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17900000512599945 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 149 | REROLL | STABILIZE | 49.0 | 5 | 19 | 1 | 30.0 | Cáustico/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-5 | 150 | REROLL | STABILIZE | 49.0 | 5 | 17 | 1 | 30.0 | Cáustico/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 152 | REROLL | STABILIZE | 49.0 | 5 | 22 | 2 | 30.0 | Cáustico/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 153 | REROLL | STABILIZE | 49.0 | 5 | 20 | 2 | 30.0 | Cáustico/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17900000512599945 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 154 | REROLL | STABILIZE | 49.0 | 5 | 18 | 1 | 30.0 | Cáustico/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 155 | REROLL | STABILIZE | 49.0 | 5 | 16 | 1 | 30.0 | Cáustico/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 156 | REROLL | STABILIZE | 49.0 | 5 | 14 | 1 | 30.0 | Cáustico/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 157 | REROLL | STABILIZE | 49.0 | 5 | 12 | 1 | 30.0 | Cáustico/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 158 | REROLL | STABILIZE | 49.0 | 5 | 10 | 1 | 30.0 | Cáustico/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17900000512599945 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 159 | REROLL | STABILIZE | 49.0 | 5 | 8 | 0 | 30.0 | Cáustico/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-6 | 160 | SELL | STABILIZE | 49.0 | 5 | 6 | 0 | 30.0 | Cáustico/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03107692301273346 | 0.0 | 0.0 | +— / -d69fa0dc-74b6-4ee7-90f7-aaca5405c59c |
| Jogador 1 | 3-7 | 162 | BUY | STABILIZE | 39.0 | 5 | 14 | 1 | 30.0 | Cáustico/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01598444953560829 | 0.0 | 0.0 | +3f38fe46-2585-4a0d-8999-ab347f9cd398 / -— |
| Jogador 1 | 3-7 | 163 | REROLL | STABILIZE | 39.0 | 5 | 11 | 1 | 30.0 | Cáustico/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10899999737739563 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 164 | REROLL | STABILIZE | 39.0 | 5 | 9 | 0 | 30.0 | Cáustico/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 165 | REROLL | STABILIZE | 39.0 | 5 | 7 | 0 | 30.0 | Cáustico/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 166 | REROLL | STABILIZE | 39.0 | 5 | 5 | 0 | 30.0 | Cáustico/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 167 | REROLL | STABILIZE | 39.0 | 5 | 3 | 0 | 30.0 | Cáustico/DA_18_Shen | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 168 | MOVE_BOARD | STABILIZE | 39.0 | 5 | 1 | 0 | 30.0 | Cáustico/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2053988128900528 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 169 | MOVE_BOARD | STABILIZE | 39.0 | 5 | 1 | 0 | 30.0 | Cáustico/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09674005955457687 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 3-7 | 170 | MOVE_BOARD | STABILIZE | 39.0 | 5 | 1 | 0 | 30.0 | Cáustico/DA_18_Shen | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3068320155143738 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 172 | SELL | STABILIZE | 39.0 | 5 | 6 | 0 | 30.0 | Cáustico/DA_18_Shen | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.02853740006685257 | 0.0 | 0.0 | +— / -3f38fe46-2585-4a0d-8999-ab347f9cd398 |
| Jogador 1 | 4-1 | 173 | BUY | STABILIZE | 39.0 | 5 | 9 | 0 | 30.0 | Cáustico/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8339201211929321 | 0.0 | 0.0 | +af0f76a0-a86c-4eac-82d6-3ebe914d51f3 / -0b62545c-1de0-47d8-bb4c-119f7e1526b3,f84bb43d-db12-46dd-a15c-28ef8fdb7fa2 |
| Jogador 1 | 4-1 | 174 | SELL | STABILIZE | 39.0 | 5 | 6 | 0 | 18.0 | Cáustico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.12564848363399506 | 0.0 | 0.0 | +— / -ccdd8153-af58-4fe7-994c-d49f0a7a17f8 |
| Jogador 1 | 4-1 | 175 | BUY | STABILIZE | 39.0 | 5 | 10 | 1 | 18.0 | Cáustico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.665186882019043 | 0.0 | 0.0 | +d1464eaa-d2dc-4eef-8bf0-14c704a500e9 / -— |
| Jogador 1 | 4-1 | 176 | MOVE_BENCH | STABILIZE | 39.0 | 5 | 8 | 0 | 18.0 | Cáustico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.26578769087791443 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 177 | REROLL | STABILIZE | 39.0 | 5 | 8 | 0 | 22.0 | Cáustico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.014000000432133675 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 178 | BUY | STABILIZE | 39.0 | 5 | 6 | 0 | 22.0 | Cáustico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.267006516456604 | 0.0 | 0.0 | +4232b4b4-99b2-4af0-b352-13f5b0726727 / -— |
| Jogador 1 | 4-1 | 179 | REROLL | STABILIZE | 39.0 | 5 | 2 | 0 | 22.0 | Cáustico/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-1 | 180 | MOVE_BENCH | STABILIZE | 39.0 | 5 | 0 | 0 | 22.0 | Cáustico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.38677746057510376 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 182 | BUY | STABILIZE | 26.0 | 6 | 6 | 0 | 30.0 | Cáustico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.26263776421546936 | 0.0 | 0.0 | +29eeef02-9b0a-480b-aca7-9e423ecddd3a / -— |
| Jogador 1 | 4-2 | 183 | MOVE_BENCH | STABILIZE | 26.0 | 6 | 2 | 0 | 30.0 | Cáustico/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3731144368648529 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 184 | MOVE_BENCH | STABILIZE | 26.0 | 6 | 2 | 0 | 34.0 | Cáustico/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6026282906532288 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 185 | BUY | STABILIZE | 26.0 | 6 | 2 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.20229963958263397 | 0.0 | 0.0 | +35f90973-e578-4be1-aaa5-9ee8073b0776 / -— |
| Jogador 1 | 4-2 | 186 | CRAFT_AND_EQUIP | STABILIZE | 26.0 | 6 | 0 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.17811815440654755 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 187 | MOVE_BOARD | STABILIZE | 26.0 | 6 | 0 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16033194959163666 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-2 | 188 | PASS | STABILIZE | 26.0 | 6 | 0 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 192 | SELL | ALL_IN | 13.0 | 6 | 6 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13738460838794708 | 0.0 | 0.0 | +— / -c30a99f5-ce2d-4bbf-9aab-93017ad40255 |
| Jogador 1 | 4-3 | 193 | BUY | ALL_IN | 13.0 | 6 | 10 | 1 | 38.0 | Cáustico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.745790421962738 | 0.0 | 0.0 | +ef39d938-bee9-4290-95a4-da8a51088653 / -d1464eaa-d2dc-4eef-8bf0-14c704a500e9,e60f0b7f-8510-4c67-9ebd-0d8be1b0ff2b |
| Jogador 1 | 4-3 | 194 | BUY | ALL_IN | 13.0 | 6 | 8 | 0 | 34.0 | Cáustico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2689092755317688 | 0.0 | 0.0 | +bed1d4a1-8791-49c9-b881-a91b3a35bad3 / -— |
| Jogador 1 | 4-3 | 195 | MOVE_BENCH | ALL_IN | 13.0 | 6 | 5 | 0 | 34.0 | Cáustico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47162243723869324 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 196 | BUY | ALL_IN | 13.0 | 6 | 5 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11713402718305588 | 0.0 | 0.0 | +4945ad21-c93b-4703-8ac3-7750589f4b32 / -— |
| Jogador 1 | 4-3 | 197 | REROLL | ALL_IN | 13.0 | 6 | 2 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 198 | MOVE_BOARD | ALL_IN | 13.0 | 6 | 0 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2249411791563034 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 199 | MOVE_BOARD | ALL_IN | 13.0 | 6 | 0 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17767199873924255 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-3 | 200 | MOVE_BOARD | ALL_IN | 13.0 | 6 | 0 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10861524939537048 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 202 | SELL | ALL_IN | 13.0 | 6 | 6 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.035999998450279236 | 0.0 | 0.0 | +— / -4945ad21-c93b-4703-8ac3-7750589f4b32 |
| Jogador 1 | 4-4 | 203 | BUY | ALL_IN | 13.0 | 6 | 9 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.275596022605896 | 0.0 | 0.0 | +b1961990-e54e-4b17-a1a4-8ba60177fe51 / -— |
| Jogador 1 | 4-4 | 204 | SELL | ALL_IN | 13.0 | 6 | 7 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1127692312002182 | 0.0 | 0.0 | +— / -29eeef02-9b0a-480b-aca7-9e423ecddd3a |
| Jogador 1 | 4-4 | 205 | BUY | ALL_IN | 13.0 | 6 | 11 | 1 | 38.0 | Cáustico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.649280309677124 | 0.0 | 0.0 | +8ff6c170-6b64-4a4e-befb-589225259e5e / -— |
| Jogador 1 | 4-4 | 206 | REROLL | ALL_IN | 13.0 | 6 | 8 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01059036422520876 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 207 | SELL | ALL_IN | 13.0 | 6 | 6 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01569230854511261 | 0.0 | 0.0 | +— / -c5557e24-8174-4d79-9e22-c2cbbb8225a8 |
| Jogador 1 | 4-4 | 208 | BUY | ALL_IN | 13.0 | 6 | 11 | 1 | 38.0 | Cáustico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15636046230793 | 0.0 | 0.0 | +a46790f3-1869-4810-ac23-361875f99dc6 / -— |
| Jogador 1 | 4-4 | 209 | REROLL | ALL_IN | 13.0 | 6 | 7 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010783480480313301 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-4 | 210 | SELL | ALL_IN | 13.0 | 6 | 5 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011037125252187252 | 0.0 | 0.0 | +— / -a46790f3-1869-4810-ac23-361875f99dc6 |
| Jogador 1 | 4-5 | 212 | BUY | ALL_IN | 13.0 | 6 | 14 | 1 | 38.0 | Cáustico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2667355537414551 | 0.0 | 0.0 | +664473b0-3c79-4e05-abe9-9bc271baaa14 / -— |
| Jogador 1 | 4-5 | 213 | SELL | ALL_IN | 13.0 | 6 | 12 | 1 | 38.0 | Cáustico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.603538453578949 | 0.0 | 0.0 | +— / -664473b0-3c79-4e05-abe9-9bc271baaa14 |
| Jogador 1 | 4-5 | 214 | BUY | ALL_IN | 13.0 | 6 | 14 | 1 | 38.0 | Cáustico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7264933586120605 | 0.0 | 0.0 | +abfa799e-235b-4157-a2b9-310ac6a31925 / -— |
| Jogador 1 | 4-5 | 215 | REROLL | ALL_IN | 13.0 | 6 | 12 | 1 | 38.0 | Cáustico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010296453721821308 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 216 | REROLL | ALL_IN | 13.0 | 6 | 10 | 1 | 38.0 | Cáustico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09027882665395737 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 217 | SELL | ALL_IN | 13.0 | 6 | 8 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.54073166847229 | 0.0 | 0.0 | +— / -abfa799e-235b-4157-a2b9-310ac6a31925 |
| Jogador 1 | 4-5 | 218 | BUY | ALL_IN | 13.0 | 6 | 10 | 1 | 38.0 | Cáustico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19399897754192352 | 0.0 | 0.0 | +2f28c2b4-1d0e-4423-80b8-75c3b5d10d7a / -— |
| Jogador 1 | 4-5 | 219 | REROLL | ALL_IN | 13.0 | 6 | 7 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03244709596037865 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-5 | 220 | REROLL | ALL_IN | 13.0 | 6 | 5 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010243336670100689 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 222 | SELL | ALL_IN | 1.0 | 6 | 8 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004272682126611471 | 0.0 | 0.0 | +— / -ef39d938-bee9-4290-95a4-da8a51088653 |
| Jogador 1 | 4-6 | 223 | BUY | ALL_IN | 1.0 | 6 | 13 | 1 | 38.0 | Cáustico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8091861605644226 | 0.0 | 0.0 | +1ea9c3a6-605e-43f3-b0c4-99818a3d85c0 / -26462e09-ab6e-4b87-85a8-6bda974b0c45,e01be6cf-34fe-4057-aef3-c08c504794cf |
| Jogador 1 | 4-6 | 224 | BUY | ALL_IN | 1.0 | 6 | 10 | 1 | 38.0 | Cáustico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.057311415672302246 | 0.0 | 0.0 | +ec6e37dd-4da6-470d-974a-ac4cd8f475db / -— |
| Jogador 1 | 4-6 | 225 | BUY | ALL_IN | 1.0 | 6 | 7 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2504734396934509 | 0.0 | 0.0 | +05dc893a-6d37-42cf-9e48-ca34199b2dd2 / -— |
| Jogador 1 | 4-6 | 226 | REROLL | ALL_IN | 1.0 | 6 | 6 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010401218198239803 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 227 | REROLL | ALL_IN | 1.0 | 6 | 4 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03249499574303627 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 228 | REROLL | ALL_IN | 1.0 | 6 | 2 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-6 | 229 | PASS | ALL_IN | 1.0 | 6 | 0 | 0 | 38.0 | Cáustico/DA_KogMaw18_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 4-7 | 232 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Cáustico/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-1 | 242 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Cáustico/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-2 | 252 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Cáustico/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-3 | 262 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Cáustico/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-4 | 272 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Cáustico/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-5 | 282 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Cáustico/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-6 | 292 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Cáustico/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 5-7 | 302 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Cáustico/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-1 | 312 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Cáustico/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-2 | 322 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Cáustico/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-3 | 332 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Cáustico/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-4 | 342 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Cáustico/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-5 | 352 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Cáustico/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-6 | 362 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Cáustico/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 6-7 | 372 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Cáustico/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 7-1 | 382 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Cáustico/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 7-2 | 392 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Cáustico/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 1 | 7-3 | 402 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Cáustico/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.010384615510702133 | 0.0 | 0.0 | +— / -fb5a6c27-acbe-4d6d-ba91-7a6209d10cf2 |
| Jogador 2 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.22450661659240723 | 0.0 | 0.0 | +292ef825-d326-4dd8-9c42-c47cfc62116f / -— |
| Jogador 2 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Yorick | MOVE_BENCH, SELL, PASS | True | True | 0.5844191908836365 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 4 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.13061420619487762 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-1 | 5 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9710612297058105 | 0.0 | 0.0 | +94ede66e-59bc-4c41-aabf-f64372e20f9a / -— |
| Jogador 2 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0773743987083435 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 13 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-2 | 14 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.18691383302211761 | 0.0 | 0.0 | +de00430a-8a57-423c-887c-317d53c2cdd3 / -— |
| Jogador 2 | 1-3 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24283316731452942 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 23 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Yorick | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15183782577514648 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 24 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 6.0 | —/DA_18_Sejuani | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.718654215335846 | 0.0 | 0.0 | +— / -292ef825-d326-4dd8-9c42-c47cfc62116f |
| Jogador 2 | 1-3 | 25 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.00921564269810915 | 0.0 | 0.0 | +c5dcd3e9-05bb-4466-8d2c-4c35c928cadf / -— |
| Jogador 2 | 1-3 | 26 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Sejuani | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.39060574769973755 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 27 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Sejuani | MOVE_BOARD, PASS | True | True | 0.032957449555397034 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-3 | 28 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 10.0 | —/DA_18_Sejuani | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 1-4 | 31 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Sejuani | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.39092251658439636 | 0.0 | 0.0 | +3eefd13b-5716-4917-a616-c3589f115098 / -— |
| Jogador 2 | 2-1 | 42 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.47663524746894836 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 43 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.027898332104086876 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-1 | 44 | PASS | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 50 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.0018304515397176147 | 0.0 | 0.0 | +561fb9a8-e987-4935-b11c-6c6104ced65d / -— |
| Jogador 2 | 2-2 | 51 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 8 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.345561146736145 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 52 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 8 | 0 | 16.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03629628196358681 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-2 | 53 | PASS | STABILIZE | 100.0 | 4 | 8 | 0 | 18.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 60 | SELL | STABILIZE | 100.0 | 4 | 15 | 1 | 18.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04674573987722397 | 0.0 | 0.0 | +— / -94ede66e-59bc-4c41-aabf-f64372e20f9a |
| Jogador 2 | 2-3 | 61 | BUY | STABILIZE | 100.0 | 4 | 16 | 1 | 18.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08652593940496445 | 0.0 | 0.0 | +89740fc1-ac0c-4a0b-9e85-1832d5c3acc4 / -— |
| Jogador 2 | 2-3 | 62 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 13 | 1 | 18.0 | —/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3914145231246948 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-3 | 63 | SELL | STABILIZE | 100.0 | 4 | 13 | 1 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.360040545463562 | 0.0 | 0.0 | +— / -3eefd13b-5716-4917-a616-c3589f115098 |
| Jogador 2 | 2-3 | 64 | PASS | STABILIZE | 100.0 | 4 | 16 | 1 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-4 | 70 | BUY | STABILIZE | 100.0 | 4 | 24 | 2 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9572309255599976 | 0.0 | 0.0 | +b0190388-bc3b-43af-b782-94490de9d8b1 / -— |
| Jogador 2 | 2-4 | 71 | SELL | STABILIZE | 100.0 | 4 | 22 | 2 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0072308778762817 | 0.0 | 0.0 | +— / -b0190388-bc3b-43af-b782-94490de9d8b1 |
| Jogador 2 | 2-4 | 72 | BUY | STABILIZE | 100.0 | 4 | 24 | 2 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.13945047557353973 | 0.0 | 0.0 | +0f1b15a2-9978-4691-a15e-483ccd03db7f / -— |
| Jogador 2 | 2-4 | 73 | SELL | STABILIZE | 100.0 | 4 | 22 | 2 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20133066177368164 | 0.0 | 0.0 | +— / -0f1b15a2-9978-4691-a15e-483ccd03db7f |
| Jogador 2 | 2-4 | 74 | PASS | STABILIZE | 100.0 | 4 | 24 | 2 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 80 | BUY | STABILIZE | 100.0 | 4 | 32 | 3 | 18.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.21543394029140472 | 0.0 | 0.0 | +361c6f8a-301b-43b0-aace-dec56d04bbf1 / -— |
| Jogador 2 | 2-5 | 81 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 29 | 2 | 18.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09837634861469269 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-5 | 82 | SELL | STABILIZE | 100.0 | 4 | 29 | 2 | 20.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0989999994635582 | 0.0 | 0.0 | +— / -c5dcd3e9-05bb-4466-8d2c-4c35c928cadf |
| Jogador 2 | 2-5 | 83 | PASS | STABILIZE | 100.0 | 4 | 31 | 3 | 20.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 89 | BUY | STABILIZE | 100.0 | 5 | 41 | 4 | 20.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9091627597808838 | 0.0 | 0.0 | +135065df-1ebc-413d-86f1-4df28bd3ee41 / -— |
| Jogador 2 | 2-6 | 90 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 39 | 3 | 20.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5125698447227478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 91 | BUY | SLOWROLL | 100.0 | 5 | 39 | 3 | 24.0 | Colosso/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3077905476093292 | 0.0 | 0.0 | +b6a21130-c9dc-45ad-8ddb-9223b0ec8751 / -— |
| Jogador 2 | 2-6 | 92 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 36 | 3 | 24.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4256269037723541 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 93 | MOVE_BOARD | SLOWROLL | 100.0 | 5 | 36 | 3 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12594178318977356 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 94 | MOVE_BOARD | SLOWROLL | 100.0 | 5 | 36 | 3 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-6 | 95 | SELL | SLOWROLL | 100.0 | 5 | 36 | 3 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7392023801803589 | 0.0 | 0.0 | +— / -135065df-1ebc-413d-86f1-4df28bd3ee41 |
| Jogador 2 | 2-6 | 96 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 38 | 3 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 98 | BUY | STABILIZE | 100.0 | 5 | 49 | 4 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.029581770300865173 | 0.0 | 0.0 | +9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d / -— |
| Jogador 2 | 2-7 | 99 | MOVE_BOARD | STABILIZE | 100.0 | 5 | 46 | 4 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039354316890239716 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 100 | SELL | STABILIZE | 100.0 | 5 | 46 | 4 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18306972086429596 | 0.0 | 0.0 | +— / -9a2e6aa1-9428-40ac-8f98-e3d4995e6a7d |
| Jogador 2 | 2-7 | 101 | BUY | STABILIZE | 100.0 | 5 | 49 | 4 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1273103803396225 | 0.0 | 0.0 | +eafa585a-9474-415b-b46b-d3ce86f4a066 / -— |
| Jogador 2 | 2-7 | 102 | SELL | STABILIZE | 100.0 | 5 | 47 | 4 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18719235062599182 | 0.0 | 0.0 | +— / -eafa585a-9474-415b-b46b-d3ce86f4a066 |
| Jogador 2 | 2-7 | 103 | BUY_XP | STABILIZE | 100.0 | 5 | 49 | 4 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 104 | BUY_XP | STABILIZE | 100.0 | 5 | 45 | 4 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 2-7 | 105 | BUY_XP | STABILIZE | 100.0 | 5 | 41 | 4 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 107 | BUY | STABILIZE | 100.0 | 5 | 47 | 4 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.7845399379730225 | 0.0 | 0.0 | +7b2af6c8-ec0f-4ab5-8913-9b88fc2e0e86 / -— |
| Jogador 2 | 3-1 | 108 | BUY | SLOWROLL | 100.0 | 5 | 44 | 4 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27991291880607605 | 0.0 | 0.0 | +4d995451-2e5c-43c2-93f0-22e074e35ab2 / -— |
| Jogador 2 | 3-1 | 109 | SELL | SLOWROLL | 100.0 | 5 | 43 | 4 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5974677205085754 | 0.0 | 0.0 | +— / -4d995451-2e5c-43c2-93f0-22e074e35ab2 |
| Jogador 2 | 3-1 | 110 | MOVE_BENCH | SLOWROLL | 100.0 | 5 | 44 | 4 | 26.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019440408796072006 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-1 | 111 | SELL | SLOWROLL | 100.0 | 5 | 44 | 4 | 28.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0122307687997818 | 0.0 | 0.0 | +— / -561fb9a8-e987-4935-b11c-6c6104ced65d |
| Jogador 2 | 3-1 | 112 | PASS | SLOWROLL | 100.0 | 5 | 46 | 4 | 28.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.02250000089406967 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-2 | 116 | BUY | SLOWROLL | 90.0 | 5 | 55 | 5 | 28.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.34837204217910767 | 0.0 | 0.0 | +527f78df-1e51-4731-9175-1c4812aa82ad / -— |
| Jogador 2 | 3-2 | 117 | SELL | SLOWROLL | 90.0 | 5 | 54 | 5 | 28.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5875610709190369 | 0.0 | 0.0 | +— / -527f78df-1e51-4731-9175-1c4812aa82ad |
| Jogador 2 | 3-2 | 118 | PASS | SLOWROLL | 90.0 | 5 | 55 | 5 | 28.0 | Colosso/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.047487035393714905 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 125 | BUY | SLOWROLL | 90.0 | 6 | 66 | 5 | 28.0 | Adaptador/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3579724431037903 | 0.0 | 0.0 | +fe6546c3-86ef-40e1-aa7e-ff7e400fe628 / -— |
| Jogador 2 | 3-3 | 126 | MOVE_BENCH | SLOWROLL | 90.0 | 6 | 62 | 5 | 28.0 | Adaptador/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5957183241844177 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 127 | BUY | SLOWROLL | 90.0 | 6 | 62 | 5 | 36.0 | Adaptador/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.22125664353370667 | 0.0 | 0.0 | +40f2a32f-1ace-4700-8a79-e6b5d3212036 / -— |
| Jogador 2 | 3-3 | 128 | REROLL | SLOWROLL | 90.0 | 6 | 59 | 5 | 36.0 | Adaptador/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13285991549491882 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 129 | BUY | SLOWROLL | 90.0 | 6 | 57 | 5 | 36.0 | Adaptador/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22804884612560272 | 0.0 | 0.0 | +b71cd729-4b0b-4276-8a58-aaf1f0c2e4c0 / -— |
| Jogador 2 | 3-3 | 130 | REROLL | SLOWROLL | 90.0 | 6 | 55 | 5 | 36.0 | Adaptador/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24999627470970154 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-3 | 131 | BUY | SLOWROLL | 90.0 | 6 | 53 | 5 | 36.0 | Adaptador/DA_Nidalee18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9220361113548279 | 0.0 | 0.0 | +665661af-7240-4a65-bf3d-f4ecf3532a85 / -7b2af6c8-ec0f-4ab5-8913-9b88fc2e0e86,89740fc1-ac0c-4a0b-9e85-1832d5c3acc4 |
| Jogador 2 | 3-3 | 132 | MOVE_BENCH | SLOWROLL | 90.0 | 6 | 50 | 5 | 24.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25696104764938354 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 134 | BUY | SLOWROLL | 90.0 | 6 | 62 | 5 | 30.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33034560084342957 | 0.0 | 0.0 | +5637ca02-9946-4d1a-9679-e5c316ef566b / -— |
| Jogador 2 | 3-4 | 135 | BUY | SLOWROLL | 90.0 | 6 | 59 | 5 | 30.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5952885746955872 | 0.0 | 0.0 | +210d2415-663d-4768-bbc2-238766c2b863 / -— |
| Jogador 2 | 3-4 | 136 | REROLL | SLOWROLL | 90.0 | 6 | 57 | 5 | 30.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24095727503299713 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 137 | BUY | SLOWROLL | 90.0 | 6 | 55 | 5 | 30.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6705583333969116 | 0.0 | 0.0 | +ba7f039a-929c-4537-9eb6-f1dc4563cca8 / -— |
| Jogador 2 | 3-4 | 138 | REROLL | SLOWROLL | 90.0 | 6 | 52 | 5 | 30.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12717726826667786 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 139 | REROLL | SLOWROLL | 90.0 | 6 | 50 | 5 | 30.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07854277640581131 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 140 | REROLL | SLOWROLL | 90.0 | 6 | 48 | 4 | 30.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08115247637033463 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-4 | 141 | MOVE_BENCH | SLOWROLL | 90.0 | 6 | 46 | 4 | 30.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4937209486961365 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 143 | BUY | SLOWROLL | 90.0 | 6 | 56 | 5 | 36.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3153155744075775 | 0.0 | 0.0 | +a11208a9-96bf-468e-ab92-2ead6308be26 / -— |
| Jogador 2 | 3-5 | 144 | REROLL | SLOWROLL | 90.0 | 6 | 54 | 5 | 36.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13366423547267914 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 145 | REROLL | SLOWROLL | 90.0 | 6 | 52 | 5 | 36.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1486492156982422 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 146 | REROLL | SLOWROLL | 90.0 | 6 | 50 | 5 | 36.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16511043906211853 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 147 | REROLL | SLOWROLL | 90.0 | 6 | 48 | 4 | 36.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09777066111564636 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 148 | REROLL | SLOWROLL | 90.0 | 6 | 46 | 4 | 36.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10899999737739563 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-5 | 149 | BUY | SLOWROLL | 90.0 | 6 | 44 | 4 | 36.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6583348512649536 | 0.0 | 0.0 | +e1055913-2340-4af0-8527-e175c8bc1ccb / -— |
| Jogador 2 | 3-5 | 150 | REROLL | SLOWROLL | 90.0 | 6 | 41 | 4 | 36.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19134771823883057 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 152 | BUY | SLOWROLL | 90.0 | 6 | 50 | 5 | 36.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28293806314468384 | 0.0 | 0.0 | +83a3ef65-b342-4ec8-b2d1-be99c3602f81 / -— |
| Jogador 2 | 3-6 | 153 | BUY | SLOWROLL | 90.0 | 6 | 46 | 4 | 36.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5554589629173279 | 0.0 | 0.0 | +9c07608c-00e1-40f1-9671-6d8bc584a6c9 / -a11208a9-96bf-468e-ab92-2ead6308be26,b71cd729-4b0b-4276-8a58-aaf1f0c2e4c0 |
| Jogador 2 | 3-6 | 154 | BUY | SLOWROLL | 90.0 | 6 | 44 | 4 | 36.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07211542874574661 | 0.0 | 0.0 | +0c5adb43-b194-486e-b59c-c0f3b5479d40 / -— |
| Jogador 2 | 3-6 | 155 | REROLL | SLOWROLL | 90.0 | 6 | 42 | 4 | 36.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16762647032737732 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 156 | REROLL | SLOWROLL | 90.0 | 6 | 40 | 4 | 36.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.009361791424453259 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 157 | BUY | SLOWROLL | 90.0 | 6 | 38 | 3 | 36.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07065625488758087 | 0.0 | 0.0 | +9a2edb0f-a3cd-455c-8406-2a7ca80e3bc6 / -— |
| Jogador 2 | 3-6 | 158 | REROLL | SLOWROLL | 90.0 | 6 | 35 | 3 | 36.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14120522141456604 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-6 | 159 | BUY | SLOWROLL | 90.0 | 6 | 33 | 3 | 36.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010437450371682644 | 0.0 | 0.0 | +280265b0-7892-4e7e-b654-e2cc7b0ea97b / -— |
| Jogador 2 | 3-6 | 160 | REROLL | STABILIZE | 90.0 | 6 | 29 | 2 | 36.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 162 | REROLL | SLOWROLL | 90.0 | 6 | 36 | 3 | 36.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.143833726644516 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 163 | REROLL | SLOWROLL | 90.0 | 6 | 34 | 3 | 36.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06592673063278198 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 164 | SELL | SLOWROLL | 90.0 | 6 | 32 | 3 | 36.0 | Adaptador/DA_18_MasterYi_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04107692465186119 | 0.0 | 0.0 | +— / -0c5adb43-b194-486e-b59c-c0f3b5479d40 |
| Jogador 2 | 3-7 | 165 | BUY | SLOWROLL | 90.0 | 6 | 34 | 3 | 36.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7641322016716003 | 0.0 | 0.0 | +3ac258d2-8fed-4c0d-b6f4-4c64aa4cec3e / -40f2a32f-1ace-4700-8a79-e6b5d3212036,ba7f039a-929c-4537-9eb6-f1dc4563cca8 |
| Jogador 2 | 3-7 | 166 | BUY | SLOWROLL | 90.0 | 6 | 31 | 3 | 30.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7058069109916687 | 0.0 | 0.0 | +3ba5e931-3f4c-410f-bf0b-d9d1a426efa3 / -361c6f8a-301b-43b0-aace-dec56d04bbf1,e1055913-2340-4af0-8527-e175c8bc1ccb |
| Jogador 2 | 3-7 | 167 | BUY | STABILIZE | 90.0 | 6 | 28 | 2 | 24.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.197175994515419 | 0.0 | 0.0 | +22c22c9e-03f7-4ff6-8880-fd8937bec7dc / -— |
| Jogador 2 | 3-7 | 168 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 24 | 2 | 24.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.329971045255661 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 169 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 24 | 2 | 24.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3648066818714142 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 3-7 | 170 | MOVE_BENCH | STABILIZE | 90.0 | 6 | 24 | 2 | 32.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6411117315292358 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 172 | MOVE_BOARD | SLOWROLL | 90.0 | 6 | 32 | 3 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12262872606515884 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 173 | BUY | SLOWROLL | 90.0 | 6 | 32 | 3 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09807391464710236 | 0.0 | 0.0 | +74ac117f-47a6-4d94-b6f7-8d42714571e5 / -— |
| Jogador 2 | 4-1 | 174 | REROLL | SLOWROLL | 90.0 | 6 | 30 | 3 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027256859466433525 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 175 | BUY | STABILIZE | 90.0 | 6 | 28 | 2 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2978612184524536 | 0.0 | 0.0 | +d14fbb79-be91-410c-8ac7-065e9d02620c / -— |
| Jogador 2 | 4-1 | 176 | REROLL | STABILIZE | 90.0 | 6 | 25 | 2 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 177 | SELL | STABILIZE | 90.0 | 6 | 23 | 2 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04432330280542374 | 0.0 | 0.0 | +— / -74ac117f-47a6-4d94-b6f7-8d42714571e5 |
| Jogador 2 | 4-1 | 178 | BUY | STABILIZE | 90.0 | 6 | 25 | 2 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3001812994480133 | 0.0 | 0.0 | +68251e71-5657-42da-9181-7351627204f6 / -— |
| Jogador 2 | 4-1 | 179 | REROLL | STABILIZE | 90.0 | 6 | 22 | 2 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-1 | 180 | SELL | STABILIZE | 90.0 | 6 | 20 | 2 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2770026624202728 | 0.0 | 0.0 | +— / -210d2415-663d-4768-bbc2-238766c2b863 |
| Jogador 2 | 4-2 | 182 | BUY | SLOWROLL | 90.0 | 6 | 32 | 3 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32700425386428833 | 0.0 | 0.0 | +edd9a1f1-6d76-45cd-89a7-2b0fdcb278e9 / -— |
| Jogador 2 | 4-2 | 183 | SELL | STABILIZE | 90.0 | 6 | 28 | 2 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11273003369569778 | 0.0 | 0.0 | +— / -9a2edb0f-a3cd-455c-8406-2a7ca80e3bc6 |
| Jogador 2 | 4-2 | 184 | BUY | SLOWROLL | 90.0 | 6 | 31 | 3 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21106909215450287 | 0.0 | 0.0 | +31f86c34-a81d-4ba0-9136-c9106b0fbec5 / -— |
| Jogador 2 | 4-2 | 185 | REROLL | STABILIZE | 90.0 | 6 | 28 | 2 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 186 | SELL | STABILIZE | 90.0 | 6 | 26 | 2 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.035999998450279236 | 0.0 | 0.0 | +— / -31f86c34-a81d-4ba0-9136-c9106b0fbec5 |
| Jogador 2 | 4-2 | 187 | BUY | STABILIZE | 90.0 | 6 | 29 | 2 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25527477264404297 | 0.0 | 0.0 | +358601f9-8e68-4107-8719-8fdaee776f87 / -— |
| Jogador 2 | 4-2 | 188 | REROLL | STABILIZE | 90.0 | 6 | 27 | 2 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-2 | 189 | SELL | STABILIZE | 90.0 | 6 | 25 | 2 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05400000140070915 | 0.0 | 0.0 | +— / -358601f9-8e68-4107-8719-8fdaee776f87 |
| Jogador 2 | 4-2 | 190 | BUY | STABILIZE | 90.0 | 6 | 27 | 2 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21319620311260223 | 0.0 | 0.0 | +5a9bb50e-c400-49f0-96bf-35de23a5e388 / -— |
| Jogador 2 | 4-3 | 192 | SELL | SLOWROLL | 79.0 | 6 | 32 | 3 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04723076894879341 | 0.0 | 0.0 | +— / -5a9bb50e-c400-49f0-96bf-35de23a5e388 |
| Jogador 2 | 4-3 | 193 | BUY | SLOWROLL | 79.0 | 6 | 34 | 3 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18296340107917786 | 0.0 | 0.0 | +bb616470-4b6d-4736-9b6a-8635fb5680b3 / -— |
| Jogador 2 | 4-3 | 194 | REROLL | SLOWROLL | 79.0 | 6 | 32 | 3 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07039304077625275 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 195 | SELL | SLOWROLL | 79.0 | 6 | 30 | 3 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3186153769493103 | 0.0 | 0.0 | +— / -bb616470-4b6d-4736-9b6a-8635fb5680b3 |
| Jogador 2 | 4-3 | 196 | BUY | SLOWROLL | 79.0 | 6 | 32 | 3 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.636127233505249 | 0.0 | 0.0 | +b070468d-f0e7-4466-8c95-97f72b490e7b / -— |
| Jogador 2 | 4-3 | 197 | REROLL | STABILIZE | 79.0 | 6 | 29 | 2 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-3 | 198 | SELL | STABILIZE | 79.0 | 6 | 27 | 2 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13738460838794708 | 0.0 | 0.0 | +— / -edd9a1f1-6d76-45cd-89a7-2b0fdcb278e9 |
| Jogador 2 | 4-3 | 199 | BUY | SLOWROLL | 79.0 | 6 | 31 | 3 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33345362544059753 | 0.0 | 0.0 | +2fc00de5-c4af-424f-97d3-a9fccd10b6ae / -— |
| Jogador 2 | 4-3 | 200 | SELL | STABILIZE | 79.0 | 6 | 28 | 2 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13600000739097595 | 0.0 | 0.0 | +— / -2fc00de5-c4af-424f-97d3-a9fccd10b6ae |
| Jogador 2 | 4-4 | 202 | BUY | SLOWROLL | 68.0 | 6 | 40 | 4 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04908594861626625 | 0.0 | 0.0 | +edccddac-d1e0-49ad-86e4-edd748549f7a / -— |
| Jogador 2 | 4-4 | 203 | REROLL | SLOWROLL | 68.0 | 6 | 37 | 3 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.048161521553993225 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 204 | SELL | SLOWROLL | 68.0 | 6 | 35 | 3 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04692307859659195 | 0.0 | 0.0 | +— / -83a3ef65-b342-4ec8-b2d1-be99c3602f81 |
| Jogador 2 | 4-4 | 205 | BUY | SLOWROLL | 68.0 | 6 | 39 | 3 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08352801203727722 | 0.0 | 0.0 | +ab80a834-c78a-4d03-9e4b-5e9c1e97ad8b / -— |
| Jogador 2 | 4-4 | 206 | REROLL | SLOWROLL | 68.0 | 6 | 36 | 3 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.048772182315588 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 207 | SELL | SLOWROLL | 68.0 | 6 | 34 | 3 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03273891657590866 | 0.0 | 0.0 | +— / -ab80a834-c78a-4d03-9e4b-5e9c1e97ad8b |
| Jogador 2 | 4-4 | 208 | BUY | SLOWROLL | 68.0 | 6 | 37 | 3 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.23464985191822052 | 0.0 | 0.0 | +f4acf065-f15c-45bf-bce4-9f0c910a272a / -— |
| Jogador 2 | 4-4 | 209 | REROLL | SLOWROLL | 68.0 | 6 | 35 | 3 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06842390447854996 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-4 | 210 | REROLL | SLOWROLL | 68.0 | 6 | 33 | 3 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13659220933914185 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 212 | SELL | SLOWROLL | 68.0 | 6 | 40 | 4 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032769229263067245 | 0.0 | 0.0 | +— / -f4acf065-f15c-45bf-bce4-9f0c910a272a |
| Jogador 2 | 4-5 | 213 | BUY | SLOWROLL | 68.0 | 6 | 42 | 4 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5395114421844482 | 0.0 | 0.0 | +dab6bb13-2a01-483f-92ab-63535c16c9e7 / -— |
| Jogador 2 | 4-5 | 214 | REROLL | SLOWROLL | 68.0 | 6 | 38 | 3 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14317987859249115 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 215 | SELL | SLOWROLL | 68.0 | 6 | 36 | 3 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08692307770252228 | 0.0 | 0.0 | +— / -22c22c9e-03f7-4ff6-8880-fd8937bec7dc |
| Jogador 2 | 4-5 | 216 | BUY | SLOWROLL | 68.0 | 6 | 40 | 4 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21140407025814056 | 0.0 | 0.0 | +5d50b524-451b-42fb-9e21-a3a2f1fa6c7e / -— |
| Jogador 2 | 4-5 | 217 | REROLL | SLOWROLL | 68.0 | 6 | 37 | 3 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12847061455249786 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-5 | 218 | SELL | SLOWROLL | 68.0 | 6 | 35 | 3 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.035999998450279236 | 0.0 | 0.0 | +— / -5d50b524-451b-42fb-9e21-a3a2f1fa6c7e |
| Jogador 2 | 4-5 | 219 | BUY | SLOWROLL | 68.0 | 6 | 38 | 3 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005345182027667761 | 0.0 | 0.0 | +6d7e7613-d64f-4021-a135-09f347111a32 / -— |
| Jogador 2 | 4-5 | 220 | REROLL | SLOWROLL | 68.0 | 6 | 35 | 3 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06414218246936798 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 222 | SELL | SLOWROLL | 68.0 | 6 | 42 | 4 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02184615470468998 | 0.0 | 0.0 | +— / -6d7e7613-d64f-4021-a135-09f347111a32 |
| Jogador 2 | 4-6 | 223 | BUY | SLOWROLL | 68.0 | 6 | 45 | 4 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2958157956600189 | 0.0 | 0.0 | +4206a4cd-c774-452e-96b7-ef69cdbe07b9 / -— |
| Jogador 2 | 4-6 | 224 | REROLL | SLOWROLL | 68.0 | 6 | 42 | 4 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09893777221441269 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 225 | SELL | SLOWROLL | 68.0 | 6 | 40 | 4 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.280923068523407 | 0.0 | 0.0 | +— / -edccddac-d1e0-49ad-86e4-edd748549f7a |
| Jogador 2 | 4-6 | 226 | BUY | SLOWROLL | 68.0 | 6 | 43 | 4 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7247397303581238 | 0.0 | 0.0 | +66bd6f3f-7045-4580-9bb2-42895d646912 / -— |
| Jogador 2 | 4-6 | 227 | REROLL | SLOWROLL | 68.0 | 6 | 40 | 4 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2122412919998169 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-6 | 228 | SELL | SLOWROLL | 68.0 | 6 | 38 | 3 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.051230769604444504 | 0.0 | 0.0 | +— / -665661af-7240-4a65-bf3d-f4ecf3532a85 |
| Jogador 2 | 4-6 | 229 | BUY | SLOWROLL | 68.0 | 6 | 46 | 4 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25260788202285767 | 0.0 | 0.0 | +4cf3206f-ce23-4f02-bfe2-59fdf8e90f67 / -— |
| Jogador 2 | 4-6 | 230 | REROLL | SLOWROLL | 68.0 | 6 | 44 | 4 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09857981652021408 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 232 | REROLL | SLOWROLL | 68.0 | 6 | 53 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2347603440284729 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 233 | SELL | SLOWROLL | 68.0 | 6 | 51 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6229230761528015 | 0.0 | 0.0 | +— / -4cf3206f-ce23-4f02-bfe2-59fdf8e90f67 |
| Jogador 2 | 4-7 | 234 | BUY | SLOWROLL | 68.0 | 6 | 53 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3265572786331177 | 0.0 | 0.0 | +f9077646-3379-4461-9a5c-b9884c7da266 / -— |
| Jogador 2 | 4-7 | 235 | REROLL | SLOWROLL | 68.0 | 6 | 49 | 4 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0961885079741478 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 236 | SELL | SLOWROLL | 68.0 | 6 | 47 | 4 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13538461923599243 | 0.0 | 0.0 | +— / -f9077646-3379-4461-9a5c-b9884c7da266 |
| Jogador 2 | 4-7 | 237 | BUY | SLOWROLL | 68.0 | 6 | 51 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6712054014205933 | 0.0 | 0.0 | +000722c3-cb79-40e1-9455-c7c2e529065a / -— |
| Jogador 2 | 4-7 | 238 | REROLL | SLOWROLL | 68.0 | 6 | 48 | 4 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1660243421792984 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 4-7 | 239 | SELL | SLOWROLL | 68.0 | 6 | 46 | 4 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003457151586189866 | 0.0 | 0.0 | +— / -3ba5e931-3f4c-410f-bf0b-d9d1a426efa3 |
| Jogador 2 | 4-7 | 240 | BUY | SLOWROLL | 68.0 | 6 | 54 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10323101282119751 | 0.0 | 0.0 | +0873cccb-ab25-4538-83eb-24f35138b838 / -— |
| Jogador 2 | 5-1 | 242 | EQUIP_FROM_INVENTORY | SLOWROLL | 68.0 | 6 | 61 | 5 | 44.0 | Adaptador/DA_18_Tristana | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 243 | SELL | SLOWROLL | 68.0 | 6 | 61 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.001076923101209104 | 0.0 | 0.0 | +— / -0873cccb-ab25-4538-83eb-24f35138b838 |
| Jogador 2 | 5-1 | 244 | BUY | SLOWROLL | 68.0 | 6 | 65 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0826556459069252 | 0.0 | 0.0 | +70aae1f6-9ad6-4156-bfd1-2db1fcca0f9e / -— |
| Jogador 2 | 5-1 | 245 | REROLL | SLOWROLL | 68.0 | 6 | 61 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.12947294116020203 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 246 | SELL | SLOWROLL | 68.0 | 6 | 59 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.012733365409076214 | 0.0 | 0.0 | +— / -70aae1f6-9ad6-4156-bfd1-2db1fcca0f9e |
| Jogador 2 | 5-1 | 247 | BUY | SLOWROLL | 68.0 | 6 | 63 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.15075679123401642 | 0.0 | 0.0 | +3c230981-d88b-4158-9cca-629bdf967865 / -— |
| Jogador 2 | 5-1 | 248 | REROLL | SLOWROLL | 68.0 | 6 | 60 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.24999523162841797 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-1 | 249 | SELL | SLOWROLL | 68.0 | 6 | 58 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0007692307699471712 | 0.0 | 0.0 | +— / -3c230981-d88b-4158-9cca-629bdf967865 |
| Jogador 2 | 5-1 | 250 | BUY | SLOWROLL | 68.0 | 6 | 61 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9497301578521729 | 0.0 | 0.0 | +c9d0cdf2-855b-4139-a5ec-73ecc4b4d12f / -000722c3-cb79-40e1-9455-c7c2e529065a,4206a4cd-c774-452e-96b7-ef69cdbe07b9 |
| Jogador 2 | 5-2 | 252 | BUY | SLOWROLL | 53.0 | 6 | 68 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7730228900909424 | 0.0 | 0.0 | +0da327af-055d-4443-a6de-24f7cfab0f26 / -— |
| Jogador 2 | 5-2 | 253 | BUY | SLOWROLL | 53.0 | 6 | 65 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.29811179637908936 | 0.0 | 0.0 | +30b8c1b4-f414-45f5-af93-14ed20789065 / -— |
| Jogador 2 | 5-2 | 254 | REROLL | SLOWROLL | 53.0 | 6 | 63 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.1464318335056305 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 255 | REROLL | SLOWROLL | 53.0 | 6 | 61 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.1029534563422203 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 256 | SELL | SLOWROLL | 53.0 | 6 | 59 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.6229230761528015 | 0.0 | 0.0 | +— / -30b8c1b4-f414-45f5-af93-14ed20789065 |
| Jogador 2 | 5-2 | 257 | BUY | SLOWROLL | 53.0 | 6 | 61 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.07796373963356018 | 0.0 | 0.0 | +799b9c1d-8221-43e2-aaf2-b3aba4bc4433 / -— |
| Jogador 2 | 5-2 | 258 | REROLL | SLOWROLL | 53.0 | 6 | 57 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.24961961805820465 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-2 | 259 | SELL | SLOWROLL | 53.0 | 6 | 55 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0014260656898841262 | 0.0 | 0.0 | +— / -799b9c1d-8221-43e2-aaf2-b3aba4bc4433 |
| Jogador 2 | 5-2 | 260 | BUY | SLOWROLL | 53.0 | 6 | 59 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.14764247834682465 | 0.0 | 0.0 | +29b1d8a9-2998-4ae1-a018-a684e8ffeda6 / -— |
| Jogador 2 | 5-3 | 262 | SELL | SLOWROLL | 53.0 | 6 | 66 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0007692307699471712 | 0.0 | 0.0 | +— / -29b1d8a9-2998-4ae1-a018-a684e8ffeda6 |
| Jogador 2 | 5-3 | 263 | BUY | SLOWROLL | 53.0 | 6 | 69 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9288454651832581 | 0.0 | 0.0 | +d5ef814b-3173-404f-a4bb-dd4c4c44603e / -66bd6f3f-7045-4580-9bb2-42895d646912,68251e71-5657-42da-9181-7351627204f6 |
| Jogador 2 | 5-3 | 264 | BUY | SLOWROLL | 53.0 | 6 | 66 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.15242518484592438 | 0.0 | 0.0 | +f7ea7560-ffda-4a58-80a0-af172f8ea299 / -— |
| Jogador 2 | 5-3 | 265 | REROLL | SLOWROLL | 53.0 | 6 | 63 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.24832843244075775 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 266 | BUY | SLOWROLL | 53.0 | 6 | 61 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.022667599841952324 | 0.0 | 0.0 | +5f64aaee-ddcb-43b6-b368-d8160c3eee67 / -— |
| Jogador 2 | 5-3 | 267 | SELL | SLOWROLL | 53.0 | 6 | 57 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0007692307699471712 | 0.0 | 0.0 | +— / -f7ea7560-ffda-4a58-80a0-af172f8ea299 |
| Jogador 2 | 5-3 | 268 | BUY | SLOWROLL | 53.0 | 6 | 60 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.29053401947021484 | 0.0 | 0.0 | +3aba7766-5c0e-4163-89fe-9075c11f22b2 / -— |
| Jogador 2 | 5-3 | 269 | REROLL | SLOWROLL | 53.0 | 6 | 58 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.14089427888393402 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-3 | 270 | REROLL | SLOWROLL | 53.0 | 6 | 56 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.23704835772514343 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 272 | SELL | SLOWROLL | 53.0 | 6 | 65 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.03676922991871834 | 0.0 | 0.0 | +— / -3aba7766-5c0e-4163-89fe-9075c11f22b2 |
| Jogador 2 | 5-4 | 273 | BUY | SLOWROLL | 53.0 | 6 | 67 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9276301264762878 | 0.0 | 0.0 | +156c9589-cb80-4283-9400-35f62c0a8882 / -280265b0-7892-4e7e-b654-e2cc7b0ea97b,dab6bb13-2a01-483f-92ab-63535c16c9e7 |
| Jogador 2 | 5-4 | 274 | BUY | SLOWROLL | 53.0 | 6 | 63 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.24917039275169373 | 0.0 | 0.0 | +f27569eb-64ae-419a-ad5b-3d1516e04cf6 / -— |
| Jogador 2 | 5-4 | 275 | REROLL | SLOWROLL | 53.0 | 6 | 60 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.24628514051437378 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 276 | BUY | SLOWROLL | 53.0 | 6 | 58 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6513200998306274 | 0.0 | 0.0 | +9e96421d-6c3c-4650-bba8-2e888b0fc678 / -— |
| Jogador 2 | 5-4 | 277 | SELL | SLOWROLL | 53.0 | 6 | 55 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -f27569eb-64ae-419a-ad5b-3d1516e04cf6 |
| Jogador 2 | 5-4 | 278 | BUY | SLOWROLL | 53.0 | 6 | 58 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03210992366075516 | 0.0 | 0.0 | +7b69f42e-fbdc-4bc6-8899-f41971744342 / -— |
| Jogador 2 | 5-4 | 279 | REROLL | SLOWROLL | 53.0 | 6 | 55 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.24999181926250458 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-4 | 280 | SELL | SLOWROLL | 53.0 | 6 | 53 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.02230769209563732 | 0.0 | 0.0 | +— / -5f64aaee-ddcb-43b6-b368-d8160c3eee67 |
| Jogador 2 | 5-5 | 282 | BUY | SLOWROLL | 53.0 | 6 | 67 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2862068712711334 | 0.0 | 0.0 | +4c3e5795-b2a7-4db8-80bb-73689cf0c956 / -— |
| Jogador 2 | 5-5 | 283 | REROLL | SLOWROLL | 53.0 | 6 | 64 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10366498678922653 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 284 | REROLL | SLOWROLL | 53.0 | 6 | 62 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2462516576051712 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 285 | SELL | SLOWROLL | 53.0 | 6 | 60 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.27646154165267944 | 0.0 | 0.0 | +— / -7b69f42e-fbdc-4bc6-8899-f41971744342 |
| Jogador 2 | 5-5 | 286 | BUY | SLOWROLL | 53.0 | 6 | 63 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.06356342881917953 | 0.0 | 0.0 | +b9a773da-3e03-440d-9791-3753006cc514 / -— |
| Jogador 2 | 5-5 | 287 | SELL | SLOWROLL | 53.0 | 6 | 59 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03400000184774399 | 0.0 | 0.0 | +— / -b9a773da-3e03-440d-9791-3753006cc514 |
| Jogador 2 | 5-5 | 288 | BUY | SLOWROLL | 53.0 | 6 | 63 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09942638874053955 | 0.0 | 0.0 | +3a3160c7-cbca-471d-8112-63540ce69c3f / -— |
| Jogador 2 | 5-5 | 289 | REROLL | SLOWROLL | 53.0 | 6 | 59 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.15599855780601501 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-5 | 290 | REROLL | SLOWROLL | 53.0 | 6 | 57 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.24966955184936523 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 292 | SELL | SLOWROLL | 53.0 | 6 | 67 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.02476923167705536 | 0.0 | 0.0 | +— / -3a3160c7-cbca-471d-8112-63540ce69c3f |
| Jogador 2 | 5-6 | 293 | BUY | SLOWROLL | 53.0 | 6 | 71 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2902188003063202 | 0.0 | 0.0 | +d1723c76-35cc-4723-a508-e6fa81a634bb / -— |
| Jogador 2 | 5-6 | 294 | REROLL | SLOWROLL | 53.0 | 6 | 69 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.16792677342891693 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 295 | REROLL | SLOWROLL | 53.0 | 6 | 67 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.24890486896038055 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 296 | REROLL | SLOWROLL | 53.0 | 6 | 65 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.047566089779138565 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 297 | SELL | SLOWROLL | 53.0 | 6 | 63 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.03676922991871834 | 0.0 | 0.0 | +— / -d1723c76-35cc-4723-a508-e6fa81a634bb |
| Jogador 2 | 5-6 | 298 | BUY | SLOWROLL | 53.0 | 6 | 65 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7450438141822815 | 0.0 | 0.0 | +ced24a23-43de-4027-82c8-50e0dd07f7aa / -— |
| Jogador 2 | 5-6 | 299 | REROLL | SLOWROLL | 53.0 | 6 | 62 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.14390432834625244 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-6 | 300 | REROLL | SLOWROLL | 53.0 | 6 | 60 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.24970857799053192 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 302 | SELL | STABILIZE | 37.0 | 7 | 68 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.6221364140510559 | 0.0 | 0.0 | +— / -9e96421d-6c3c-4650-bba8-2e888b0fc678 |
| Jogador 2 | 5-7 | 303 | BUY | STABILIZE | 37.0 | 7 | 71 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.42473432421684265 | 0.0 | 0.0 | +d106cbbf-9108-45c1-91bf-9fec43312b53 / -— |
| Jogador 2 | 5-7 | 304 | SELL | STABILIZE | 37.0 | 7 | 68 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.04938461631536484 | 0.0 | 0.0 | +— / -d5ef814b-3173-404f-a4bb-dd4c4c44603e |
| Jogador 2 | 5-7 | 305 | BUY | STABILIZE | 37.0 | 7 | 76 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0199005603790283 | 0.0 | 0.0 | +7118a9a6-c57b-48a8-81ff-552fb7b8fb12 / -b070468d-f0e7-4466-8c95-97f72b490e7b,b6a21130-c9dc-45ad-8ddb-9223b0ec8751 |
| Jogador 2 | 5-7 | 306 | BUY | STABILIZE | 37.0 | 7 | 73 | 5 | 38.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.46999770402908325 | 0.0 | 0.0 | +be507fbc-5c44-42f8-ad29-74fdf291f541 / -— |
| Jogador 2 | 5-7 | 307 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 70 | 5 | 38.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.1600852906703949 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 308 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 70 | 5 | 36.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2305089384317398 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 5-7 | 309 | BUY | STABILIZE | 37.0 | 7 | 70 | 5 | 44.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.08869998157024384 | 0.0 | 0.0 | +7f3d6e55-8b25-4344-9408-7a7f7a0877f7 / -— |
| Jogador 2 | 5-7 | 310 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 66 | 5 | 44.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.6459740996360779 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 312 | EQUIP_FROM_INVENTORY | STABILIZE | 37.0 | 7 | 76 | 5 | 60.0 | Adaptador/DA_18_Tristana | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 313 | EQUIP_FROM_INVENTORY | STABILIZE | 37.0 | 7 | 76 | 5 | 60.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY, CRAFT_AND_EQUIP | True | — | 0.13770084083080292 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 314 | BUY | STABILIZE | 37.0 | 7 | 76 | 5 | 60.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10470009595155716 | 0.0 | 0.0 | +e154b287-b7f6-4195-bcd3-282ad21630ea / -— |
| Jogador 2 | 6-1 | 315 | REROLL | STABILIZE | 37.0 | 7 | 72 | 5 | 60.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0454706996679306 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 316 | SELL | STABILIZE | 37.0 | 7 | 70 | 5 | 60.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.02476923167705536 | 0.0 | 0.0 | +— / -7f3d6e55-8b25-4344-9408-7a7f7a0877f7 |
| Jogador 2 | 6-1 | 317 | BUY | STABILIZE | 37.0 | 7 | 74 | 5 | 60.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.45435869693756104 | 0.0 | 0.0 | +cb9b8514-6c86-446f-84c5-f4a52b4b2018 / -— |
| Jogador 2 | 6-1 | 318 | REROLL | STABILIZE | 37.0 | 7 | 70 | 5 | 60.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.015021035447716713 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-1 | 319 | SELL | STABILIZE | 37.0 | 7 | 68 | 5 | 60.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.02476923167705536 | 0.0 | 0.0 | +— / -e154b287-b7f6-4195-bcd3-282ad21630ea |
| Jogador 2 | 6-1 | 320 | BUY | STABILIZE | 37.0 | 7 | 72 | 5 | 60.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1444372683763504 | 0.0 | 0.0 | +f71d5711-bb43-41b4-9ed9-9d816bab08b6 / -— |
| Jogador 2 | 6-2 | 322 | SELL | STABILIZE | 37.0 | 7 | 79 | 5 | 60.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.012551638297736645 | 0.0 | 0.0 | +— / -f71d5711-bb43-41b4-9ed9-9d816bab08b6 |
| Jogador 2 | 6-2 | 323 | BUY | STABILIZE | 37.0 | 7 | 83 | 5 | 60.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7212609052658081 | 0.0 | 0.0 | +4f73e8fe-3f1b-42eb-9245-330ce175d2f9 / -— |
| Jogador 2 | 6-2 | 324 | REROLL | STABILIZE | 37.0 | 7 | 80 | 5 | 60.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03984964266419411 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 325 | SELL | STABILIZE | 37.0 | 7 | 78 | 5 | 60.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.611874520778656 | 0.0 | 0.0 | +— / -4f73e8fe-3f1b-42eb-9245-330ce175d2f9 |
| Jogador 2 | 6-2 | 326 | BUY | STABILIZE | 37.0 | 7 | 81 | 5 | 60.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.14446738362312317 | 0.0 | 0.0 | +d94b5aad-b6b0-425d-8a04-addfa27bce41 / -— |
| Jogador 2 | 6-2 | 327 | REROLL | STABILIZE | 37.0 | 7 | 77 | 5 | 60.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04553065076470375 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-2 | 328 | SELL | STABILIZE | 37.0 | 7 | 75 | 5 | 60.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.012557887472212315 | 0.0 | 0.0 | +— / -d94b5aad-b6b0-425d-8a04-addfa27bce41 |
| Jogador 2 | 6-2 | 329 | BUY | STABILIZE | 37.0 | 7 | 79 | 5 | 60.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9899964332580566 | 0.0 | 0.0 | +7037439b-c113-4ca6-85f7-304666e3016b / -— |
| Jogador 2 | 6-2 | 330 | REROLL | STABILIZE | 37.0 | 7 | 76 | 5 | 60.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.02500000037252903 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 332 | SELL | STABILIZE | 37.0 | 7 | 86 | 5 | 60.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.6016923189163208 | 0.0 | 0.0 | +— / -4c3e5795-b2a7-4db8-80bb-73689cf0c956 |
| Jogador 2 | 6-3 | 333 | BUY | STABILIZE | 37.0 | 7 | 89 | 5 | 60.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0793209075927734 | 0.0 | 0.0 | +3950b709-f822-4acf-9769-20017e8d4cdf / -0da327af-055d-4443-a6de-24f7cfab0f26,d14fbb79-be91-410c-8ac7-065e9d02620c |
| Jogador 2 | 6-3 | 334 | BUY | STABILIZE | 37.0 | 7 | 86 | 5 | 54.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7045297622680664 | 0.0 | 0.0 | +0b6b0390-b167-4f31-af9f-bbf459aab1e5 / -— |
| Jogador 2 | 6-3 | 335 | REROLL | STABILIZE | 37.0 | 7 | 83 | 5 | 54.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07904649525880814 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 336 | SELL | STABILIZE | 37.0 | 7 | 81 | 5 | 54.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.6016923189163208 | 0.0 | 0.0 | +— / -0b6b0390-b167-4f31-af9f-bbf459aab1e5 |
| Jogador 2 | 6-3 | 337 | BUY | STABILIZE | 37.0 | 7 | 84 | 5 | 54.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.12691417336463928 | 0.0 | 0.0 | +94a27a89-0bae-43de-a8fe-0f745a9ff489 / -— |
| Jogador 2 | 6-3 | 338 | REROLL | STABILIZE | 37.0 | 7 | 81 | 5 | 54.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04552952200174332 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-3 | 339 | SELL | STABILIZE | 37.0 | 7 | 79 | 5 | 54.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.029999999329447746 | 0.0 | 0.0 | +— / -94a27a89-0bae-43de-a8fe-0f745a9ff489 |
| Jogador 2 | 6-3 | 340 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 82 | 5 | 54.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7296780943870544 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 342 | BUY | STABILIZE | 37.0 | 7 | 94 | 5 | 60.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0799962282180786 | 0.0 | 0.0 | +01e02cb3-0ff0-44ef-928d-fc5364e31bad / -7037439b-c113-4ca6-85f7-304666e3016b,be507fbc-5c44-42f8-ad29-74fdf291f541 |
| Jogador 2 | 6-4 | 343 | BUY | STABILIZE | 37.0 | 7 | 91 | 5 | 54.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.21038812398910522 | 0.0 | 0.0 | +cdbd97c4-dd7d-4582-bedb-eacd759c477e / -— |
| Jogador 2 | 6-4 | 344 | BUY | STABILIZE | 37.0 | 7 | 89 | 5 | 54.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3095687925815582 | 0.0 | 0.0 | +f1710a4b-dd72-4b98-90c5-6e4ea4347cc0 / -— |
| Jogador 2 | 6-4 | 345 | REROLL | STABILIZE | 37.0 | 7 | 87 | 5 | 54.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04552886262536049 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-4 | 346 | SELL | STABILIZE | 37.0 | 7 | 85 | 5 | 54.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2690769135951996 | 0.0 | 0.0 | +— / -cdbd97c4-dd7d-4582-bedb-eacd759c477e |
| Jogador 2 | 6-4 | 347 | BUY | STABILIZE | 37.0 | 7 | 87 | 5 | 54.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9422993063926697 | 0.0 | 0.0 | +bc00e927-3d96-4776-b4b9-d6979c759495 / -— |
| Jogador 2 | 6-4 | 348 | SELL | STABILIZE | 37.0 | 7 | 84 | 5 | 54.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04323076829314232 | 0.0 | 0.0 | +— / -f1710a4b-dd72-4b98-90c5-6e4ea4347cc0 |
| Jogador 2 | 6-4 | 349 | BUY | STABILIZE | 37.0 | 7 | 86 | 5 | 54.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0693441703915596 | 0.0 | 0.0 | +7a3a47d1-433d-4706-a02b-c872bfdd43f1 / -— |
| Jogador 2 | 6-4 | 350 | MOVE_BENCH | STABILIZE | 37.0 | 7 | 83 | 5 | 54.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7777382135391235 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 352 | BUY | STABILIZE | 37.0 | 7 | 94 | 5 | 66.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.012854917906224728 | 0.0 | 0.0 | +efdcefa8-47a9-42f8-9e5f-c303ccb31811 / -— |
| Jogador 2 | 6-5 | 353 | REROLL | STABILIZE | 37.0 | 7 | 90 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04525841772556305 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 354 | SELL | STABILIZE | 37.0 | 7 | 88 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.01584615372121334 | 0.0 | 0.0 | +— / -7a3a47d1-433d-4706-a02b-c872bfdd43f1 |
| Jogador 2 | 6-5 | 355 | BUY | STABILIZE | 37.0 | 7 | 91 | 5 | 66.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4158661663532257 | 0.0 | 0.0 | +a6e80145-da3a-4fd4-822b-2dc60955d46d / -— |
| Jogador 2 | 6-5 | 356 | REROLL | STABILIZE | 37.0 | 7 | 88 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0796412006020546 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 357 | SELL | STABILIZE | 37.0 | 7 | 86 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03400000184774399 | 0.0 | 0.0 | +— / -efdcefa8-47a9-42f8-9e5f-c303ccb31811 |
| Jogador 2 | 6-5 | 358 | BUY | STABILIZE | 37.0 | 7 | 90 | 5 | 66.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2456335723400116 | 0.0 | 0.0 | +8e309aba-8241-43c4-9923-ba615060c2eb / -— |
| Jogador 2 | 6-5 | 359 | REROLL | STABILIZE | 37.0 | 7 | 87 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.042690932750701904 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-5 | 360 | SELL | STABILIZE | 37.0 | 7 | 85 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2918461561203003 | 0.0 | 0.0 | +— / -8e309aba-8241-43c4-9923-ba615060c2eb |
| Jogador 2 | 6-6 | 362 | BUY | STABILIZE | 37.0 | 7 | 100 | 5 | 66.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.25725236535072327 | 0.0 | 0.0 | +bc770f41-e313-4e9e-aef0-2a0e344008b3 / -— |
| Jogador 2 | 6-6 | 363 | SELL | STABILIZE | 37.0 | 7 | 96 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04938461631536484 | 0.0 | 0.0 | +— / -bc770f41-e313-4e9e-aef0-2a0e344008b3 |
| Jogador 2 | 6-6 | 364 | BUY | STABILIZE | 37.0 | 7 | 100 | 5 | 66.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03791316598653793 | 0.0 | 0.0 | +3396040a-80bf-46b6-a3d5-c646781a5835 / -— |
| Jogador 2 | 6-6 | 365 | REROLL | STABILIZE | 37.0 | 7 | 97 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.06608261913061142 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 366 | SELL | STABILIZE | 37.0 | 7 | 95 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.01584615372121334 | 0.0 | 0.0 | +— / -3396040a-80bf-46b6-a3d5-c646781a5835 |
| Jogador 2 | 6-6 | 367 | BUY | STABILIZE | 37.0 | 7 | 98 | 5 | 66.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.15717744827270508 | 0.0 | 0.0 | +4da778b3-0b9a-4caa-8f18-7b850a30c6bc / -— |
| Jogador 2 | 6-6 | 368 | REROLL | STABILIZE | 37.0 | 7 | 95 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.02963528037071228 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-6 | 369 | SELL | STABILIZE | 37.0 | 7 | 93 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.029999999329447746 | 0.0 | 0.0 | +— / -4da778b3-0b9a-4caa-8f18-7b850a30c6bc |
| Jogador 2 | 6-6 | 370 | BUY | STABILIZE | 37.0 | 7 | 96 | 5 | 66.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.12376630306243896 | 0.0 | 0.0 | +bc737550-3d3e-4182-8634-e98ad185d5be / -— |
| Jogador 2 | 6-7 | 372 | SELL | STABILIZE | 37.0 | 7 | 105 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.012905742973089218 | 0.0 | 0.0 | +— / -bc737550-3d3e-4182-8634-e98ad185d5be |
| Jogador 2 | 6-7 | 373 | BUY | STABILIZE | 37.0 | 7 | 109 | 5 | 66.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5262045860290527 | 0.0 | 0.0 | +08b40bd0-91b1-4e25-9670-7223c928b12b / -— |
| Jogador 2 | 6-7 | 374 | SELL | STABILIZE | 37.0 | 7 | 106 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2893846035003662 | 0.0 | 0.0 | +— / -ced24a23-43de-4027-82c8-50e0dd07f7aa |
| Jogador 2 | 6-7 | 375 | BUY | STABILIZE | 37.0 | 7 | 109 | 5 | 66.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.012997923418879509 | 0.0 | 0.0 | +ec7962b3-a2c7-409c-9576-695b3fe77eac / -— |
| Jogador 2 | 6-7 | 376 | REROLL | STABILIZE | 37.0 | 7 | 105 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07003860175609589 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-7 | 377 | SELL | STABILIZE | 37.0 | 7 | 103 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.023538460955023766 | 0.0 | 0.0 | +— / -ec7962b3-a2c7-409c-9576-695b3fe77eac |
| Jogador 2 | 6-7 | 378 | BUY | STABILIZE | 37.0 | 7 | 107 | 5 | 66.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.38457122445106506 | 0.0 | 0.0 | +7c799414-0c08-491b-8be8-6827b2ea84f6 / -— |
| Jogador 2 | 6-7 | 379 | REROLL | STABILIZE | 37.0 | 7 | 105 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0017319178441539407 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 6-7 | 380 | SELL | STABILIZE | 37.0 | 7 | 103 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.03676922991871834 | 0.0 | 0.0 | +— / -7c799414-0c08-491b-8be8-6827b2ea84f6 |
| Jogador 2 | 7-1 | 382 | EQUIP_FROM_INVENTORY | STABILIZE | 37.0 | 7 | 117 | 5 | 66.0 | Adaptador/DA_18_Tristana | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-1 | 383 | EQUIP_FROM_INVENTORY | STABILIZE | 37.0 | 7 | 117 | 5 | 66.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY, CRAFT_AND_EQUIP | True | — | 0.10738283395767212 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-1 | 384 | BUY | STABILIZE | 37.0 | 7 | 117 | 5 | 66.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.38752496242523193 | 0.0 | 0.0 | +518590ac-5edb-45f5-a313-e12ffa83d09d / -— |
| Jogador 2 | 7-1 | 385 | REROLL | STABILIZE | 37.0 | 7 | 115 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.042172424495220184 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-1 | 386 | REROLL | STABILIZE | 37.0 | 7 | 113 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.041732851415872574 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-1 | 387 | SELL | STABILIZE | 37.0 | 7 | 111 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2809268832206726 | 0.0 | 0.0 | +— / -518590ac-5edb-45f5-a313-e12ffa83d09d |
| Jogador 2 | 7-1 | 388 | BUY | STABILIZE | 37.0 | 7 | 113 | 5 | 66.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8895924687385559 | 0.0 | 0.0 | +77a30c01-c6f8-4a60-ac07-b1b63150a951 / -— |
| Jogador 2 | 7-1 | 389 | REROLL | STABILIZE | 37.0 | 7 | 110 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.050137411803007126 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-1 | 390 | REROLL | STABILIZE | 37.0 | 7 | 108 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0455312579870224 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-2 | 392 | SELL | ALL_IN | 15.0 | 7 | 116 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.12569230794906616 | 0.0 | 0.0 | +— / -c9d0cdf2-855b-4139-a5ec-73ecc4b4d12f |
| Jogador 2 | 7-2 | 393 | BUY | ALL_IN | 15.0 | 7 | 124 | 5 | 66.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9042637348175049 | 0.0 | 0.0 | +99a6481c-fe33-46b9-819d-011a14d85e07 / -— |
| Jogador 2 | 7-2 | 394 | REROLL | ALL_IN | 15.0 | 7 | 120 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.06346695870161057 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-2 | 395 | SELL | ALL_IN | 15.0 | 7 | 118 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.15000000596046448 | 0.0 | 0.0 | +— / -7118a9a6-c57b-48a8-81ff-552fb7b8fb12 |
| Jogador 2 | 7-2 | 396 | EQUIP_FROM_INVENTORY | ALL_IN | 15.0 | 7 | 126 | 5 | 66.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY, CRAFT_AND_EQUIP | True | — | 0.12557676434516907 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-2 | 397 | BUY | ALL_IN | 15.0 | 7 | 126 | 5 | 66.0 | Adaptador/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9762271046638489 | 0.0 | 0.0 | +23e7b9f8-1451-4168-bc8b-bb19ecc6d1ca / -— |
| Jogador 2 | 7-2 | 398 | REROLL | ALL_IN | 15.0 | 7 | 123 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.08694445341825485 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-2 | 399 | REROLL | ALL_IN | 15.0 | 7 | 121 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.06077760085463524 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-2 | 400 | REROLL | ALL_IN | 15.0 | 7 | 119 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.06334850192070007 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-3 | 402 | SELL | ALL_IN | 15.0 | 7 | 128 | 5 | 66.0 | Adaptador/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.08295979350805283 | 0.0 | 0.0 | +— / -3950b709-f822-4acf-9769-20017e8d4cdf |
| Jogador 2 | 7-3 | 403 | BUY | ALL_IN | 15.0 | 7 | 136 | 5 | 66.0 | Adaptador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0699923038482666 | 0.0 | 0.0 | +73d056d3-1349-4af4-a2c0-ca19b083cd2e / -08b40bd0-91b1-4e25-9670-7223c928b12b,23e7b9f8-1451-4168-bc8b-bb19ecc6d1ca |
| Jogador 2 | 7-3 | 404 | BUY | ALL_IN | 15.0 | 7 | 133 | 5 | 66.0 | Adaptador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1974812150001526 | 0.0 | 0.0 | +28dd5945-74e2-4d02-a716-3804e7924f60 / -— |
| Jogador 2 | 7-3 | 405 | REROLL | ALL_IN | 15.0 | 7 | 130 | 5 | 66.0 | Adaptador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.02500000037252903 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-3 | 406 | BUY | ALL_IN | 15.0 | 7 | 128 | 5 | 66.0 | Adaptador/DA_18_Sett | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.14415551722049713 | 0.0 | 0.0 | +0ae75f77-b77b-432b-9b28-614adc830420 / -— |
| Jogador 2 | 7-3 | 407 | REROLL | ALL_IN | 15.0 | 7 | 124 | 5 | 66.0 | Adaptador/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.044917427003383636 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-3 | 408 | REROLL | ALL_IN | 15.0 | 7 | 122 | 5 | 66.0 | Adaptador/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.024723656475543976 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-3 | 409 | REROLL | ALL_IN | 15.0 | 7 | 120 | 5 | 66.0 | Adaptador/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05875256657600403 | 0.0 | 0.0 | +— / -— |
| Jogador 2 | 7-3 | 410 | REROLL | ALL_IN | 15.0 | 7 | 118 | 5 | 66.0 | Adaptador/DA_18_Sett | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09676298499107361 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.019615383818745613 | 0.0 | 0.0 | +— / -36f58657-5835-4389-95e9-a7d26464c2aa |
| Jogador 3 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.21530985832214355 | 0.0 | 0.0 | +2cf5ccdc-76f4-4fc8-b12c-7b3b68b1b2c8 / -— |
| Jogador 3 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_RekSai | MOVE_BENCH, SELL, PASS | True | True | 0.5842720866203308 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 4 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_RekSai | MOVE_BOARD, PASS | True | True | 0.13061420619487762 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-1 | 5 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_RekSai | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_RekSai | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.9702640175819397 | 0.0 | 0.0 | +bdef75b2-081b-43df-9efb-fc0bc5ee2935 / -— |
| Jogador 3 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_RekSai | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0773743987083435 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 13 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_RekSai | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-2 | 14 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_RekSai | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_RekSai | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.01711772382259369 | 0.0 | 0.0 | +405de1b8-45c1-4b7f-b044-f12b819507c3 / -— |
| Jogador 3 | 1-3 | 22 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_Murkwolf18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13361181318759918 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 23 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_Murkwolf18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37955379486083984 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 24 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, MOVE_BOARD, PASS | True | True | 0.024840479716658592 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-3 | 25 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08268816769123077 | 0.0 | 0.0 | +d15ca853-2585-49d0-9d7f-339dae104062 / -— |
| Jogador 3 | 1-4 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_Murkwolf18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19816255569458008 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 1-4 | 33 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7090698480606079 | 0.0 | 0.0 | +— / -2cf5ccdc-76f4-4fc8-b12c-7b3b68b1b2c8 |
| Jogador 3 | 1-4 | 34 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9667001366615295 | 0.0 | 0.0 | +c70251e8-af44-4466-808f-d49e9e5f57e9 / -— |
| Jogador 3 | 2-1 | 42 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 5 | 0 | 10.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5143864750862122 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 43 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.036966722458601 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-1 | 44 | PASS | STABILIZE | 100.0 | 4 | 5 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 50 | BUY | STABILIZE | 100.0 | 4 | 11 | 1 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.0332845449447632 | 0.0 | 0.0 | +e5a28bd6-35ef-4cb0-801c-68c64d65b8eb / -c70251e8-af44-4466-808f-d49e9e5f57e9,d15ca853-2585-49d0-9d7f-339dae104062 |
| Jogador 3 | 2-2 | 51 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44067075848579407 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 52 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 9 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.036966722458601 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 53 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 9 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.036966722458601 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 54 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.38663533329963684 | 0.0 | 0.0 | +8a68772c-3f02-4f2e-882b-4fa69fbb6750 / -— |
| Jogador 3 | 2-2 | 55 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 14.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4904933273792267 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 56 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 6 | 0 | 20.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 57 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 6 | 0 | 20.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-2 | 58 | PASS | STABILIZE | 100.0 | 4 | 6 | 0 | 20.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 60 | BUY | STABILIZE | 94.0 | 4 | 11 | 1 | 20.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.07791677117347717 | 0.0 | 0.0 | +0da2c93c-0c62-4fe0-94ff-688f086141e3 / -— |
| Jogador 3 | 2-3 | 61 | MOVE_BENCH | STABILIZE | 94.0 | 4 | 8 | 0 | 20.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06943023204803467 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 62 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 8 | 0 | 22.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10340246558189392 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-3 | 63 | PASS | STABILIZE | 94.0 | 4 | 8 | 0 | 22.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 70 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 14 | 1 | 22.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2885822057723999 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 71 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 14 | 1 | 20.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8074707984924316 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-4 | 72 | PASS | STABILIZE | 89.0 | 4 | 14 | 1 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 80 | MOVE_BENCH | STABILIZE | 89.0 | 4 | 21 | 2 | 18.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18614892661571503 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 81 | SELL | STABILIZE | 89.0 | 4 | 21 | 2 | 22.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39494866132736206 | 0.0 | 0.0 | +— / -405de1b8-45c1-4b7f-b044-f12b819507c3 |
| Jogador 3 | 2-5 | 82 | BUY | STABILIZE | 89.0 | 4 | 23 | 2 | 22.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.22645200788974762 | 0.0 | 0.0 | +1b1964b4-7d5e-4cea-8e83-0692f326b599 / -— |
| Jogador 3 | 2-5 | 83 | SELL | STABILIZE | 89.0 | 4 | 20 | 2 | 22.0 | Vivaz/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29791906476020813 | 0.0 | 0.0 | +— / -1b1964b4-7d5e-4cea-8e83-0692f326b599 |
| Jogador 3 | 2-5 | 84 | MOVE_BOARD | STABILIZE | 89.0 | 4 | 23 | 2 | 22.0 | Vivaz/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.12034890055656433 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 85 | BUY | STABILIZE | 89.0 | 4 | 23 | 2 | 22.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03634410724043846 | 0.0 | 0.0 | +0023f061-5310-4e39-849a-22ad49993d8c / -— |
| Jogador 3 | 2-5 | 86 | MOVE_BOARD | STABILIZE | 89.0 | 4 | 21 | 2 | 22.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01558587234467268 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-5 | 87 | MOVE_BOARD | STABILIZE | 89.0 | 4 | 21 | 2 | 22.0 | Devastador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14029812812805176 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 89 | BUY | STABILIZE | 83.0 | 5 | 29 | 2 | 22.0 | Lutador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5145770907402039 | 0.0 | 0.0 | +53bbd605-d60b-4555-b5e8-29f1cfbb83b4 / -— |
| Jogador 3 | 2-6 | 90 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 27 | 2 | 22.0 | Lutador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5071207284927368 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 91 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 27 | 2 | 26.0 | Lutador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.326675683259964 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 92 | MOVE_BENCH | STABILIZE | 83.0 | 5 | 27 | 2 | 26.0 | Lutador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03647700697183609 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 93 | MOVE_BOARD | STABILIZE | 83.0 | 5 | 27 | 2 | 28.0 | Lutador/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 94 | MOVE_BOARD | STABILIZE | 83.0 | 5 | 27 | 2 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-6 | 95 | PASS | STABILIZE | 83.0 | 5 | 27 | 2 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 98 | BUY | SLOWROLL | 78.0 | 5 | 35 | 3 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.94862300157547 | 0.0 | 0.0 | +536c157d-bb9f-4be0-9847-040530c052fd / -— |
| Jogador 3 | 2-7 | 99 | MOVE_BOARD | SLOWROLL | 78.0 | 5 | 33 | 3 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04875248298048973 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 100 | MOVE_BOARD | SLOWROLL | 78.0 | 5 | 33 | 3 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 101 | MOVE_BOARD | SLOWROLL | 78.0 | 5 | 33 | 3 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 2-7 | 102 | PASS | SLOWROLL | 78.0 | 5 | 33 | 3 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 107 | MOVE_BOARD | SLOWROLL | 78.0 | 5 | 42 | 4 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 108 | MOVE_BOARD | SLOWROLL | 78.0 | 5 | 42 | 4 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04875248298048973 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 109 | MOVE_BOARD | SLOWROLL | 78.0 | 5 | 42 | 4 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 110 | MOVE_BOARD | SLOWROLL | 78.0 | 5 | 42 | 4 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-1 | 111 | PASS | SLOWROLL | 78.0 | 5 | 42 | 4 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02250000089406967 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 116 | BUY | SLOWROLL | 78.0 | 5 | 52 | 5 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7759722471237183 | 0.0 | 0.0 | +409b32b9-5280-4d79-b5b2-871ed597ba56 / -— |
| Jogador 3 | 3-2 | 117 | REROLL | SLOWROLL | 78.0 | 5 | 50 | 5 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0889805480837822 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 118 | BUY | SLOWROLL | 78.0 | 5 | 48 | 4 | 28.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.845635175704956 | 0.0 | 0.0 | +c4c0b136-020d-4c1e-9517-8e0bf4c5a628 / -536c157d-bb9f-4be0-9847-040530c052fd,53bbd605-d60b-4555-b5e8-29f1cfbb83b4 |
| Jogador 3 | 3-2 | 119 | REROLL | SLOWROLL | 78.0 | 5 | 46 | 4 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09893260896205902 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 120 | BUY | SLOWROLL | 78.0 | 5 | 44 | 4 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8425251245498657 | 0.0 | 0.0 | +3a11170d-1b8e-4316-ad59-9a7e60071f12 / -0023f061-5310-4e39-849a-22ad49993d8c,409b32b9-5280-4d79-b5b2-871ed597ba56 |
| Jogador 3 | 3-2 | 121 | BUY | SLOWROLL | 78.0 | 5 | 42 | 4 | 20.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09949763119220734 | 0.0 | 0.0 | +46fc5f36-cf3e-422e-89f3-9501ec9d7d12 / -— |
| Jogador 3 | 3-2 | 122 | REROLL | SLOWROLL | 78.0 | 5 | 40 | 4 | 20.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2227894812822342 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-2 | 123 | MOVE_BENCH | SLOWROLL | 78.0 | 5 | 38 | 3 | 20.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09414055198431015 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 125 | BUY | SLOWROLL | 78.0 | 5 | 48 | 4 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26741135120391846 | 0.0 | 0.0 | +ba3c4e40-b686-40b3-bc40-004a8667f853 / -— |
| Jogador 3 | 3-3 | 126 | REROLL | SLOWROLL | 78.0 | 5 | 46 | 4 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09255211055278778 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 127 | BUY | SLOWROLL | 78.0 | 5 | 44 | 4 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2515054941177368 | 0.0 | 0.0 | +320038b5-88c4-48fe-a7fa-a30823d674c0 / -— |
| Jogador 3 | 3-3 | 128 | REROLL | SLOWROLL | 78.0 | 5 | 41 | 4 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.014709140174090862 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 129 | BUY | SLOWROLL | 78.0 | 5 | 39 | 3 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.020487193018198013 | 0.0 | 0.0 | +68d2cec6-d29b-4173-a696-ac20ccb1f079 / -— |
| Jogador 3 | 3-3 | 130 | BUY | SLOWROLL | 78.0 | 5 | 35 | 3 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1610691398382187 | 0.0 | 0.0 | +7306c9be-466e-498c-819e-274ff070c72b / -— |
| Jogador 3 | 3-3 | 131 | REROLL | SLOWROLL | 78.0 | 5 | 33 | 3 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13134315609931946 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-3 | 132 | MOVE_BENCH | SLOWROLL | 78.0 | 5 | 31 | 3 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4234670400619507 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 134 | BUY | SLOWROLL | 68.0 | 5 | 39 | 3 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24845877289772034 | 0.0 | 0.0 | +f6de9b7d-1373-459e-b34a-7b878d1a1268 / -— |
| Jogador 3 | 3-4 | 135 | BUY | SLOWROLL | 68.0 | 5 | 37 | 3 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.418129563331604 | 0.0 | 0.0 | +6b05a3b6-1a7b-4d8a-b9a7-da29ba14c968 / -— |
| Jogador 3 | 3-4 | 136 | BUY | SLOWROLL | 68.0 | 5 | 34 | 3 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025552639737725258 | 0.0 | 0.0 | +1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 / -— |
| Jogador 3 | 3-4 | 137 | REROLL | SLOWROLL | 68.0 | 5 | 31 | 3 | 26.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2055516391992569 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 138 | REROLL | STABILIZE | 68.0 | 5 | 29 | 2 | 26.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-4 | 139 | SELL | STABILIZE | 68.0 | 5 | 27 | 2 | 26.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029400406405329704 | 0.0 | 0.0 | +— / -46fc5f36-cf3e-422e-89f3-9501ec9d7d12 |
| Jogador 3 | 3-4 | 140 | BUY | STABILIZE | 68.0 | 5 | 29 | 2 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20395363867282867 | 0.0 | 0.0 | +fcd8f4bf-7e1f-42b3-a989-5b3683394c89 / -— |
| Jogador 3 | 3-4 | 141 | SELL | STABILIZE | 68.0 | 5 | 26 | 2 | 26.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28046154975891113 | 0.0 | 0.0 | +— / -7306c9be-466e-498c-819e-274ff070c72b |
| Jogador 3 | 3-5 | 143 | BUY | SLOWROLL | 68.0 | 5 | 35 | 3 | 26.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6716800332069397 | 0.0 | 0.0 | +cba152f4-af54-4d82-a35d-67aa165174be / -0da2c93c-0c62-4fe0-94ff-688f086141e3,6b05a3b6-1a7b-4d8a-b9a7-da29ba14c968 |
| Jogador 3 | 3-5 | 144 | BUY | SLOWROLL | 68.0 | 5 | 32 | 3 | 20.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22624358534812927 | 0.0 | 0.0 | +98b72340-a402-45bc-9493-71263e3168d6 / -— |
| Jogador 3 | 3-5 | 145 | REROLL | SLOWROLL | 68.0 | 5 | 30 | 3 | 20.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02734517678618431 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-5 | 146 | SELL | STABILIZE | 68.0 | 5 | 28 | 2 | 20.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08891467750072479 | 0.0 | 0.0 | +— / -fcd8f4bf-7e1f-42b3-a989-5b3683394c89 |
| Jogador 3 | 3-5 | 147 | BUY | SLOWROLL | 68.0 | 5 | 31 | 3 | 20.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6042380928993225 | 0.0 | 0.0 | +bcd06176-e1d7-43fb-abd4-b6faea8c7927 / -— |
| Jogador 3 | 3-5 | 148 | SELL | STABILIZE | 68.0 | 5 | 28 | 2 | 20.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03799999877810478 | 0.0 | 0.0 | +— / -98b72340-a402-45bc-9493-71263e3168d6 |
| Jogador 3 | 3-5 | 149 | BUY | SLOWROLL | 68.0 | 5 | 30 | 3 | 20.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1735810786485672 | 0.0 | 0.0 | +3c59d736-011d-480c-a9af-1df7a3b4caab / -— |
| Jogador 3 | 3-5 | 150 | REROLL | STABILIZE | 68.0 | 5 | 27 | 2 | 20.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 152 | BUY | SLOWROLL | 57.0 | 5 | 33 | 3 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7045671343803406 | 0.0 | 0.0 | +08731924-b808-4070-8c85-2c747847d835 / -— |
| Jogador 3 | 3-6 | 153 | REROLL | SLOWROLL | 57.0 | 5 | 31 | 3 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.20572398602962494 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 154 | REROLL | STABILIZE | 57.0 | 5 | 29 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 155 | REROLL | STABILIZE | 57.0 | 5 | 27 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 156 | SELL | STABILIZE | 57.0 | 5 | 25 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04399999976158142 | 0.0 | 0.0 | +— / -3c59d736-011d-480c-a9af-1df7a3b4caab |
| Jogador 3 | 3-6 | 157 | BUY | STABILIZE | 57.0 | 5 | 28 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2573350965976715 | 0.0 | 0.0 | +87726d3e-4b0d-41ae-bf43-893d4092bd5b / -— |
| Jogador 3 | 3-6 | 158 | REROLL | STABILIZE | 57.0 | 5 | 26 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 159 | REROLL | STABILIZE | 57.0 | 5 | 24 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-6 | 160 | REROLL | STABILIZE | 57.0 | 5 | 22 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 162 | REROLL | STABILIZE | 46.0 | 5 | 28 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 163 | REROLL | STABILIZE | 46.0 | 5 | 26 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 164 | REROLL | STABILIZE | 46.0 | 5 | 24 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 165 | REROLL | STABILIZE | 46.0 | 5 | 22 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 166 | REROLL | STABILIZE | 46.0 | 5 | 20 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17900000512599945 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 167 | REROLL | STABILIZE | 46.0 | 5 | 18 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 168 | REROLL | STABILIZE | 46.0 | 5 | 16 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 3-7 | 169 | SELL | STABILIZE | 46.0 | 5 | 14 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0398666188120842 | 0.0 | 0.0 | +— / -1ebe5a8f-f63b-44b8-b40b-d9062a1eb6b0 |
| Jogador 3 | 3-7 | 170 | BUY | STABILIZE | 46.0 | 5 | 17 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7417808175086975 | 0.0 | 0.0 | +6f89a47a-1ab1-48ed-ba66-bcbaa3e74231 / -— |
| Jogador 3 | 4-1 | 172 | REROLL | STABILIZE | 46.0 | 5 | 21 | 2 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 173 | REROLL | STABILIZE | 46.0 | 5 | 19 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 174 | REROLL | STABILIZE | 46.0 | 5 | 17 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 175 | REROLL | STABILIZE | 46.0 | 5 | 15 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 176 | REROLL | STABILIZE | 46.0 | 5 | 13 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 177 | REROLL | STABILIZE | 46.0 | 5 | 11 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 178 | REROLL | STABILIZE | 46.0 | 5 | 9 | 0 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-1 | 179 | SELL | STABILIZE | 46.0 | 5 | 7 | 0 | 24.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1127692312002182 | 0.0 | 0.0 | +— / -68d2cec6-d29b-4173-a696-ac20ccb1f079 |
| Jogador 3 | 4-1 | 180 | BUY | STABILIZE | 46.0 | 5 | 11 | 1 | 24.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7559848427772522 | 0.0 | 0.0 | +6375ddab-b4ed-4bec-b6fd-1178b2bc1843 / -08731924-b808-4070-8c85-2c747847d835,c4c0b136-020d-4c1e-9517-8e0bf4c5a628,e5a28bd6-35ef-4cb0-801c-68c64d65b8eb,f6de9b7d-1373-459e-b34a-7b878d1a1268 |
| Jogador 3 | 4-2 | 182 | BUY | STABILIZE | 33.0 | 6 | 15 | 1 | 12.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24506445229053497 | 0.0 | 0.0 | +f2b8bdda-c32d-4840-bfda-f25caf0c83fb / -— |
| Jogador 3 | 4-2 | 183 | BUY | STABILIZE | 33.0 | 6 | 12 | 1 | 12.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0755992904305458 | 0.0 | 0.0 | +6de561d2-7853-4c3f-b971-64a82c3eccd8 / -— |
| Jogador 3 | 4-2 | 184 | SELL | STABILIZE | 33.0 | 6 | 10 | 1 | 12.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04494812339544296 | 0.0 | 0.0 | +— / -6de561d2-7853-4c3f-b971-64a82c3eccd8 |
| Jogador 3 | 4-2 | 185 | BUY | STABILIZE | 33.0 | 6 | 12 | 1 | 12.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24939508736133575 | 0.0 | 0.0 | +2ea16654-a3ca-4b16-a4cd-989264343b5c / -— |
| Jogador 3 | 4-2 | 186 | MOVE_BENCH | STABILIZE | 33.0 | 6 | 10 | 1 | 12.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.44746866822242737 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 187 | REROLL | STABILIZE | 33.0 | 6 | 10 | 1 | 16.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09399999678134918 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-2 | 188 | BUY | STABILIZE | 33.0 | 6 | 8 | 0 | 16.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1637386977672577 | 0.0 | 0.0 | +20b00872-970d-411b-b1d0-9f75e56890cb / -— |
| Jogador 3 | 4-2 | 189 | SELL | STABILIZE | 33.0 | 6 | 5 | 0 | 16.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05400000140070915 | 0.0 | 0.0 | +— / -2ea16654-a3ca-4b16-a4cd-989264343b5c |
| Jogador 3 | 4-2 | 190 | MOVE_BENCH | STABILIZE | 33.0 | 6 | 7 | 0 | 16.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12411656230688095 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 192 | BUY | STABILIZE | 21.0 | 6 | 14 | 1 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.053505536168813705 | 0.0 | 0.0 | +232101ed-2aff-4705-8519-e52953f195b5 / -— |
| Jogador 3 | 4-3 | 193 | BUY | STABILIZE | 21.0 | 6 | 10 | 1 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24162860214710236 | 0.0 | 0.0 | +01cb9abd-4b2d-4758-9ca8-28562ab57551 / -— |
| Jogador 3 | 4-3 | 194 | REROLL | STABILIZE | 21.0 | 6 | 6 | 0 | 22.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010805463418364525 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-3 | 195 | SELL | STABILIZE | 21.0 | 6 | 4 | 0 | 22.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.020615383982658386 | 0.0 | 0.0 | +— / -20b00872-970d-411b-b1d0-9f75e56890cb |
| Jogador 3 | 4-3 | 196 | BUY | STABILIZE | 21.0 | 6 | 7 | 0 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2791212499141693 | 0.0 | 0.0 | +0c78292b-9418-41f0-be15-e359034d670c / -— |
| Jogador 3 | 4-3 | 197 | SELL | STABILIZE | 21.0 | 6 | 4 | 0 | 22.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03769230842590332 | 0.0 | 0.0 | +— / -01cb9abd-4b2d-4758-9ca8-28562ab57551 |
| Jogador 3 | 4-3 | 198 | BUY | STABILIZE | 21.0 | 6 | 8 | 0 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5345862507820129 | 0.0 | 0.0 | +c0f2d118-082b-4ff4-80c2-1bc63db45c07 / -— |
| Jogador 3 | 4-3 | 199 | SELL | STABILIZE | 21.0 | 6 | 5 | 0 | 22.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2800000011920929 | 0.0 | 0.0 | +— / -c0f2d118-082b-4ff4-80c2-1bc63db45c07 |
| Jogador 3 | 4-3 | 200 | MOVE_BENCH | STABILIZE | 21.0 | 6 | 8 | 0 | 22.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.438416987657547 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 202 | BUY | ALL_IN | 9.0 | 6 | 16 | 1 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27598631381988525 | 0.0 | 0.0 | +833043ea-cd10-4ab1-8c1b-9ff9cc02683c / -— |
| Jogador 3 | 4-4 | 203 | BUY | ALL_IN | 9.0 | 6 | 14 | 1 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15043668448925018 | 0.0 | 0.0 | +6f0d0e0e-84ba-49c0-90fb-ac362001c761 / -— |
| Jogador 3 | 4-4 | 204 | REROLL | ALL_IN | 9.0 | 6 | 10 | 1 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09241113811731339 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 205 | REROLL | ALL_IN | 9.0 | 6 | 8 | 0 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010720216669142246 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 206 | REROLL | ALL_IN | 9.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01027765590697527 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 207 | SELL | ALL_IN | 9.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.048153847455978394 | 0.0 | 0.0 | +— / -6f0d0e0e-84ba-49c0-90fb-ac362001c761 |
| Jogador 3 | 4-4 | 208 | BUY | ALL_IN | 9.0 | 6 | 8 | 0 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.18585273623466492 | 0.0 | 0.0 | +1447e7a6-9992-4846-9e37-f097ae0ebe73 / -— |
| Jogador 3 | 4-4 | 209 | REROLL | ALL_IN | 9.0 | 6 | 5 | 0 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-4 | 210 | REROLL | ALL_IN | 9.0 | 6 | 3 | 0 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032912544906139374 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 212 | SELL | ALL_IN | 9.0 | 6 | 9 | 0 | 30.0 | Colosso/DA_Scuttlecrab18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08920685201883316 | 0.0 | 0.0 | +— / -1447e7a6-9992-4846-9e37-f097ae0ebe73 |
| Jogador 3 | 4-5 | 213 | BUY | ALL_IN | 9.0 | 6 | 12 | 1 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7435597777366638 | 0.0 | 0.0 | +1573ec28-c68c-4c59-9059-f2f61997f861 / -320038b5-88c4-48fe-a7fa-a30823d674c0,bcd06176-e1d7-43fb-abd4-b6faea8c7927 |
| Jogador 3 | 4-5 | 214 | BUY | ALL_IN | 9.0 | 6 | 9 | 0 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5279028415679932 | 0.0 | 0.0 | +c12425b2-ec6b-42a0-a420-369fbeef595f / -— |
| Jogador 3 | 4-5 | 215 | REROLL | ALL_IN | 9.0 | 6 | 6 | 0 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 216 | BUY | ALL_IN | 9.0 | 6 | 4 | 0 | 30.0 | Colosso/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2712608575820923 | 0.0 | 0.0 | +e9c315e6-51d2-4eac-ac4f-6f840583e114 / -— |
| Jogador 3 | 4-5 | 217 | MOVE_BOARD | ALL_IN | 9.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13150574266910553 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 218 | MOVE_BOARD | ALL_IN | 9.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13138355314731598 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 219 | MOVE_BOARD | ALL_IN | 9.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1429494172334671 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-5 | 220 | SELL | ALL_IN | 9.0 | 6 | 0 | 0 | 30.0 | Colosso/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00037077980232425034 | 0.0 | 0.0 | +— / -3a11170d-1b8e-4316-ad59-9a7e60071f12 |
| Jogador 3 | 4-6 | 222 | PASS | ALL_IN | 0.0 | 6 | 5 | 0 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 4-7 | 232 | PASS | ALL_IN | 0.0 | 6 | 5 | 0 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-1 | 242 | PASS | ALL_IN | 0.0 | 6 | 5 | 0 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-2 | 252 | PASS | ALL_IN | 0.0 | 6 | 5 | 0 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-3 | 262 | PASS | ALL_IN | 0.0 | 6 | 5 | 0 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-4 | 272 | PASS | ALL_IN | 0.0 | 6 | 5 | 0 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-5 | 282 | PASS | ALL_IN | 0.0 | 6 | 5 | 0 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-6 | 292 | PASS | ALL_IN | 0.0 | 6 | 5 | 0 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 5-7 | 302 | PASS | ALL_IN | 0.0 | 6 | 5 | 0 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-1 | 312 | PASS | ALL_IN | 0.0 | 6 | 5 | 0 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-2 | 322 | PASS | ALL_IN | 0.0 | 6 | 5 | 0 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-3 | 332 | PASS | ALL_IN | 0.0 | 6 | 5 | 0 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-4 | 342 | PASS | ALL_IN | 0.0 | 6 | 5 | 0 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-5 | 352 | PASS | ALL_IN | 0.0 | 6 | 5 | 0 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-6 | 362 | PASS | ALL_IN | 0.0 | 6 | 5 | 0 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 6-7 | 372 | PASS | ALL_IN | 0.0 | 6 | 5 | 0 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 7-1 | 382 | PASS | ALL_IN | 0.0 | 6 | 5 | 0 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 7-2 | 392 | PASS | ALL_IN | 0.0 | 6 | 5 | 0 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 3 | 7-3 | 402 | PASS | ALL_IN | 0.0 | 6 | 5 | 0 | 0.0 | Colosso/DA_Scuttlecrab18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.019615383818745613 | 0.0 | 0.0 | +— / -9614eae9-6f31-48db-a3be-9b4b2c5034c8 |
| Jogador 4 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +1903eae4-bd37-4ed8-bbae-28177e859592 / -— |
| Jogador 4 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Akali_AD | MOVE_BENCH, SELL, PASS | True | True | 0.5990749597549438 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 4 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.13061420619487762 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-1 | 5 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.257247656583786 | 0.0 | 0.0 | +95829f2e-ad17-448d-a385-fdcf81872dc8 / -— |
| Jogador 4 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Akali_AD | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12088774144649506 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 13 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 14 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.0849403440952301 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Akali_AD | BUY, MOVE_BOARD, PASS | True | True | 0.07100427895784378 | 0.0 | 0.0 | +9e7d1da0-5190-4348-81b4-3a3f2129a8e5 / -— |
| Jogador 4 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Akali_AD | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.46193841099739075 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Akali_AD | MOVE_BOARD, PASS | True | True | 0.06377681344747543 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-2 | 18 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3127961754798889 | 0.0 | 0.0 | +a19fc47b-fc81-49b2-bc25-d25d58b8deef / -— |
| Jogador 4 | 1-3 | 22 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Gromp18_AP | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36279618740081787 | 0.0 | 0.0 | +— / -a19fc47b-fc81-49b2-bc25-d25d58b8deef |
| Jogador 4 | 1-3 | 23 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.975904107093811 | 0.0 | 0.0 | +cd27dcd8-0a45-4196-be66-fbe6eb4a0793 / -— |
| Jogador 4 | 1-4 | 32 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0259040594100952 | 0.0 | 0.0 | +— / -cd27dcd8-0a45-4196-be66-fbe6eb4a0793 |
| Jogador 4 | 1-4 | 33 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.975809633731842 | 0.0 | 0.0 | +eddd35aa-7d38-4d71-8984-e4768f06379e / -— |
| Jogador 4 | 1-4 | 34 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.025809645652771 | 0.0 | 0.0 | +— / -eddd35aa-7d38-4d71-8984-e4768f06379e |
| Jogador 4 | 1-4 | 35 | PASS | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.968009889125824 | 0.0 | 0.0 | +0e9aa759-0538-4168-a523-02a5f8e09e0a / -— |
| Jogador 4 | 2-1 | 42 | SELL | STABILIZE | 100.0 | 4 | 8 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.018009901046753 | 0.0 | 0.0 | +— / -0e9aa759-0538-4168-a523-02a5f8e09e0a |
| Jogador 4 | 2-1 | 43 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.294364869594574 | 0.0 | 0.0 | +9819422b-1f51-47b5-89b7-9d6e906ddff2 / -— |
| Jogador 4 | 2-1 | 44 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 7 | 0 | 6.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3087066113948822 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 45 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1797420233488083 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 46 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.009366531856358051 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 47 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-1 | 48 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9630497097969055 | 0.0 | 0.0 | +c05579e6-aa73-434f-8a91-c58d68a81ced / -— |
| Jogador 4 | 2-2 | 50 | SELL | STABILIZE | 100.0 | 4 | 11 | 1 | 10.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0130497217178345 | 0.0 | 0.0 | +— / -c05579e6-aa73-434f-8a91-c58d68a81ced |
| Jogador 4 | 2-2 | 51 | BUY | STABILIZE | 100.0 | 4 | 13 | 1 | 10.0 | —/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09056202322244644 | 0.0 | 0.0 | +4e00fb2f-75c1-4580-bd09-cb73c31af01f / -— |
| Jogador 4 | 2-2 | 52 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 10 | 1 | 10.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3520687520503998 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 53 | SELL | STABILIZE | 100.0 | 4 | 10 | 1 | 12.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08276309818029404 | 0.0 | 0.0 | +— / -9819422b-1f51-47b5-89b7-9d6e906ddff2 |
| Jogador 4 | 2-2 | 54 | REROLL | STABILIZE | 100.0 | 4 | 12 | 1 | 12.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 55 | BUY | STABILIZE | 100.0 | 4 | 10 | 1 | 12.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8951772451400757 | 0.0 | 0.0 | +257a34c3-5cf0-4a26-adb4-6635fda7a29b / -— |
| Jogador 4 | 2-2 | 56 | SELL | STABILIZE | 100.0 | 4 | 9 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9451772570610046 | 0.0 | 0.0 | +— / -257a34c3-5cf0-4a26-adb4-6635fda7a29b |
| Jogador 4 | 2-2 | 57 | REROLL | STABILIZE | 100.0 | 4 | 10 | 1 | 12.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.17900000512599945 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-2 | 58 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 12.0 | —/DA_Krug18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4283410906791687 | 0.0 | 0.0 | +adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 / -— |
| Jogador 4 | 2-3 | 60 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 10 | 1 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10691893100738525 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 61 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 10 | 1 | 12.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.734298050403595 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 62 | SELL | STABILIZE | 96.0 | 4 | 10 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.013090668246150017 | 0.0 | 0.0 | +— / -9e7d1da0-5190-4348-81b4-3a3f2129a8e5 |
| Jogador 4 | 2-3 | 63 | BUY | STABILIZE | 96.0 | 4 | 11 | 1 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.30638396739959717 | 0.0 | 0.0 | +0fff7760-179f-4d7c-8267-08d70cb6c1bd / -— |
| Jogador 4 | 2-3 | 64 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 8 | 0 | 16.0 | —/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22745923697948456 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 65 | SELL | STABILIZE | 96.0 | 4 | 8 | 0 | 16.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2756238877773285 | 0.0 | 0.0 | +— / -adc92aa3-18ee-46c7-b2ab-cad83a0b2ae6 |
| Jogador 4 | 2-3 | 66 | REROLL | STABILIZE | 96.0 | 4 | 11 | 1 | 16.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-3 | 67 | BUY | STABILIZE | 96.0 | 4 | 9 | 0 | 16.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3208385407924652 | 0.0 | 0.0 | +4c8a9a18-68d8-4672-a96d-bb09816257dc / -— |
| Jogador 4 | 2-3 | 68 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 6 | 0 | 16.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8289493322372437 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 70 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 12 | 1 | 16.0 | —/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12631867825984955 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 71 | SELL | STABILIZE | 96.0 | 4 | 12 | 1 | 16.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32823076844215393 | 0.0 | 0.0 | +— / -4e00fb2f-75c1-4580-bd09-cb73c31af01f |
| Jogador 4 | 2-4 | 72 | BUY | STABILIZE | 96.0 | 4 | 15 | 1 | 16.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.975173830986023 | 0.0 | 0.0 | +3280b28e-bd8f-494b-a78d-111744e2178b / -— |
| Jogador 4 | 2-4 | 73 | SELL | STABILIZE | 96.0 | 4 | 14 | 1 | 16.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0251737833023071 | 0.0 | 0.0 | +— / -3280b28e-bd8f-494b-a78d-111744e2178b |
| Jogador 4 | 2-4 | 74 | BUY | STABILIZE | 96.0 | 4 | 15 | 1 | 16.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.02174733206629753 | 0.0 | 0.0 | +2c7e844d-925a-43bb-8be8-65a71d11f964 / -— |
| Jogador 4 | 2-4 | 75 | SELL | STABILIZE | 96.0 | 4 | 13 | 1 | 16.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4910939037799835 | 0.0 | 0.0 | +— / -2c7e844d-925a-43bb-8be8-65a71d11f964 |
| Jogador 4 | 2-4 | 76 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 15 | 1 | 16.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.030939772725105286 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-4 | 77 | BUY | STABILIZE | 96.0 | 4 | 15 | 1 | 16.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9082736372947693 | 0.0 | 0.0 | +22c1a0b0-5d27-406a-b3e1-9e0272a18947 / -— |
| Jogador 4 | 2-4 | 78 | SELL | STABILIZE | 96.0 | 4 | 14 | 1 | 16.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9582736492156982 | 0.0 | 0.0 | +— / -22c1a0b0-5d27-406a-b3e1-9e0272a18947 |
| Jogador 4 | 2-5 | 80 | BUY | STABILIZE | 96.0 | 4 | 21 | 2 | 16.0 | —/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17309309542179108 | 0.0 | 0.0 | +bd48de5d-f06b-401c-83a0-2ca5ba1043a4 / -— |
| Jogador 4 | 2-5 | 81 | SELL | STABILIZE | 96.0 | 4 | 18 | 1 | 16.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.41407692432403564 | 0.0 | 0.0 | +— / -bd48de5d-f06b-401c-83a0-2ca5ba1043a4 |
| Jogador 4 | 2-5 | 82 | BUY | STABILIZE | 96.0 | 4 | 21 | 2 | 16.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3705228269100189 | 0.0 | 0.0 | +1d709136-338f-4fef-90fc-b2aa1b83d879 / -— |
| Jogador 4 | 2-5 | 83 | SELL | STABILIZE | 96.0 | 4 | 19 | 1 | 16.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48662295937538147 | 0.0 | 0.0 | +— / -1d709136-338f-4fef-90fc-b2aa1b83d879 |
| Jogador 4 | 2-5 | 84 | BUY | STABILIZE | 96.0 | 4 | 21 | 2 | 16.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 1.021756887435913 | 0.0 | 0.0 | +67afd567-2757-4206-bb7e-0e5af22093b3 / -— |
| Jogador 4 | 2-5 | 85 | SELL | STABILIZE | 96.0 | 4 | 20 | 2 | 16.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0717568397521973 | 0.0 | 0.0 | +— / -67afd567-2757-4206-bb7e-0e5af22093b3 |
| Jogador 4 | 2-5 | 86 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 21 | 2 | 16.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.11019983887672424 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-5 | 87 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 21 | 2 | 16.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.17477719485759735 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 89 | BUY | STABILIZE | 89.0 | 5 | 28 | 2 | 16.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9810886979103088 | 0.0 | 0.0 | +a9f7f52e-6619-4669-9b8a-390b99fd73d8 / -— |
| Jogador 4 | 2-6 | 90 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 25 | 2 | 16.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5270859003067017 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 91 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 25 | 2 | 22.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.10621310770511627 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 92 | BUY | STABILIZE | 89.0 | 5 | 25 | 2 | 22.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9440769553184509 | 0.0 | 0.0 | +aea66e45-dc49-4efb-ba64-e7961a96e4b7 / -— |
| Jogador 4 | 2-6 | 93 | SELL | STABILIZE | 89.0 | 5 | 24 | 2 | 22.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9940769076347351 | 0.0 | 0.0 | +— / -aea66e45-dc49-4efb-ba64-e7961a96e4b7 |
| Jogador 4 | 2-6 | 94 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 25 | 2 | 22.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.00998972449451685 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 95 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 25 | 2 | 22.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.17945104837417603 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-6 | 96 | MOVE_BOARD | STABILIZE | 89.0 | 5 | 25 | 2 | 22.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.3180747330188751 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 2-7 | 98 | BUY | SLOWROLL | 89.0 | 5 | 33 | 3 | 22.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9088671803474426 | 0.0 | 0.0 | +60b0249f-e02f-4aca-b90d-75e9bcc822b8 / -— |
| Jogador 4 | 2-7 | 99 | SELL | SLOWROLL | 89.0 | 5 | 32 | 3 | 22.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9588671922683716 | 0.0 | 0.0 | +— / -60b0249f-e02f-4aca-b90d-75e9bcc822b8 |
| Jogador 4 | 2-7 | 100 | BUY | SLOWROLL | 89.0 | 5 | 33 | 3 | 22.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.08135303854942322 | 0.0 | 0.0 | +d3fbe91b-4c13-49db-9b9c-8b2879652154 / -— |
| Jogador 4 | 2-7 | 101 | SELL | SLOWROLL | 89.0 | 5 | 30 | 3 | 22.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.49111422896385193 | 0.0 | 0.0 | +— / -d3fbe91b-4c13-49db-9b9c-8b2879652154 |
| Jogador 4 | 2-7 | 102 | BUY | SLOWROLL | 89.0 | 5 | 33 | 3 | 22.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.04850868508219719 | 0.0 | 0.0 | +d731d71e-fc91-41ae-ab3f-75966dd2c428 / -— |
| Jogador 4 | 2-7 | 103 | SELL | SLOWROLL | 89.0 | 5 | 31 | 3 | 22.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5082445740699768 | 0.0 | 0.0 | +— / -d731d71e-fc91-41ae-ab3f-75966dd2c428 |
| Jogador 4 | 2-7 | 104 | BUY | SLOWROLL | 89.0 | 5 | 33 | 3 | 22.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2418089359998703 | 0.0 | 0.0 | +57903c42-49ca-43e1-8f86-42429c189fb5 / -— |
| Jogador 4 | 2-7 | 105 | MOVE_BENCH | SLOWROLL | 89.0 | 5 | 31 | 3 | 22.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.43658125400543213 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 107 | BUY | SLOWROLL | 89.0 | 5 | 39 | 3 | 20.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6961257457733154 | 0.0 | 0.0 | +5489a8f6-2466-4171-b91e-64c367875d3c / -— |
| Jogador 4 | 3-1 | 108 | BUY | SLOWROLL | 89.0 | 5 | 37 | 3 | 20.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2246813327074051 | 0.0 | 0.0 | +e86a4466-cd1f-48a3-a825-cab2e361b72a / -— |
| Jogador 4 | 3-1 | 109 | BUY | SLOWROLL | 89.0 | 5 | 35 | 3 | 20.0 | Flora Fatalis/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7040913701057434 | 0.0 | 0.0 | +e6614d74-9c11-4502-8719-4d49167f44ab / -— |
| Jogador 4 | 3-1 | 110 | REROLL | SLOWROLL | 89.0 | 5 | 34 | 3 | 20.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07099254429340363 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 111 | BUY | SLOWROLL | 89.0 | 5 | 32 | 3 | 20.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7819041013717651 | 0.0 | 0.0 | +daa7f698-2fa2-43d7-ae73-ec616b006db4 / -5489a8f6-2466-4171-b91e-64c367875d3c,57903c42-49ca-43e1-8f86-42429c189fb5 |
| Jogador 4 | 3-1 | 112 | BUY | SLOWROLL | 89.0 | 5 | 30 | 3 | 16.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7253586053848267 | 0.0 | 0.0 | +46320c4e-6bc0-49d6-b150-be378fa422cf / -1903eae4-bd37-4ed8-bbae-28177e859592,e6614d74-9c11-4502-8719-4d49167f44ab |
| Jogador 4 | 3-1 | 113 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 29 | 2 | 14.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4361511766910553 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-1 | 114 | MOVE_BENCH | STABILIZE | 89.0 | 5 | 29 | 2 | 18.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5156795978546143 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 116 | MOVE_BOARD | SLOWROLL | 79.0 | 5 | 36 | 3 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03215137496590614 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 117 | BUY | SLOWROLL | 79.0 | 5 | 36 | 3 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6999162435531616 | 0.0 | 0.0 | +a12781fd-4d61-4c7e-b439-a6e62bd48dfe / -— |
| Jogador 4 | 3-2 | 118 | MOVE_BOARD | SLOWROLL | 79.0 | 5 | 35 | 3 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11087857931852341 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 119 | MOVE_BOARD | SLOWROLL | 79.0 | 5 | 35 | 3 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11359098553657532 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-2 | 120 | PASS | SLOWROLL | 79.0 | 5 | 35 | 3 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 125 | REROLL | SLOWROLL | 70.0 | 5 | 44 | 4 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09132558107376099 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 126 | BUY | SLOWROLL | 70.0 | 5 | 42 | 4 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2976464033126831 | 0.0 | 0.0 | +1489b596-9339-407a-b49f-d01ecfdd6f78 / -— |
| Jogador 4 | 3-3 | 127 | REROLL | SLOWROLL | 70.0 | 5 | 41 | 4 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03477312996983528 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 128 | REROLL | SLOWROLL | 70.0 | 5 | 39 | 3 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.143912211060524 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 129 | REROLL | SLOWROLL | 70.0 | 5 | 37 | 3 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0663808137178421 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 130 | BUY | SLOWROLL | 70.0 | 5 | 35 | 3 | 24.0 | Devastador/DA_18_Akali_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11746899783611298 | 0.0 | 0.0 | +f5ae964e-f157-48d1-8088-8b8a45a398b6 / -— |
| Jogador 4 | 3-3 | 131 | REROLL | SLOWROLL | 70.0 | 5 | 33 | 3 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1355852335691452 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-3 | 132 | REROLL | SLOWROLL | 70.0 | 5 | 31 | 3 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03534196317195892 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 134 | REROLL | SLOWROLL | 62.0 | 5 | 37 | 3 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10899999737739563 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 135 | REROLL | SLOWROLL | 62.0 | 5 | 35 | 3 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14396704733371735 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 136 | REROLL | SLOWROLL | 62.0 | 5 | 33 | 3 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1277967393398285 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 137 | REROLL | SLOWROLL | 62.0 | 5 | 31 | 3 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19765803217887878 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 138 | REROLL | STABILIZE | 62.0 | 5 | 29 | 2 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 139 | REROLL | STABILIZE | 62.0 | 5 | 27 | 2 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 140 | REROLL | STABILIZE | 62.0 | 5 | 25 | 2 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-4 | 141 | REROLL | STABILIZE | 62.0 | 5 | 23 | 2 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 143 | REROLL | STABILIZE | 62.0 | 5 | 29 | 2 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 144 | REROLL | STABILIZE | 62.0 | 5 | 27 | 2 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 145 | REROLL | STABILIZE | 62.0 | 5 | 25 | 2 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 146 | REROLL | STABILIZE | 62.0 | 5 | 23 | 2 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 147 | REROLL | STABILIZE | 62.0 | 5 | 21 | 2 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 148 | REROLL | STABILIZE | 62.0 | 5 | 19 | 1 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 149 | REROLL | STABILIZE | 62.0 | 5 | 17 | 1 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-5 | 150 | REROLL | STABILIZE | 62.0 | 5 | 15 | 1 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 152 | REROLL | STABILIZE | 53.0 | 5 | 20 | 2 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 153 | BUY | STABILIZE | 53.0 | 5 | 18 | 1 | 24.0 | Devastador/DA_18_Yunara | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8315623998641968 | 0.0 | 0.0 | +5de51369-647a-45bd-95b7-c8efe44c5484 / -0fff7760-179f-4d7c-8267-08d70cb6c1bd,a9f7f52e-6619-4669-9b8a-390b99fd73d8 |
| Jogador 4 | 3-6 | 154 | BUY | STABILIZE | 53.0 | 5 | 15 | 1 | 12.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8368374109268188 | 0.0 | 0.0 | +0a0e7d41-96bf-404f-a3bf-98df0a182b63 / -95829f2e-ad17-448d-a385-fdcf81872dc8,a12781fd-4d61-4c7e-b439-a6e62bd48dfe |
| Jogador 4 | 3-6 | 155 | BUY | STABILIZE | 53.0 | 5 | 14 | 1 | 10.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3040941059589386 | 0.0 | 0.0 | +c5520bc4-3123-40f3-b275-83fa8cb06309 / -— |
| Jogador 4 | 3-6 | 156 | MOVE_BENCH | STABILIZE | 53.0 | 5 | 11 | 1 | 10.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3100011348724365 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 157 | MOVE_BENCH | STABILIZE | 53.0 | 5 | 11 | 1 | 12.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24066300690174103 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 158 | REROLL | STABILIZE | 53.0 | 5 | 11 | 1 | 16.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-6 | 159 | BUY | STABILIZE | 53.0 | 5 | 9 | 0 | 16.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2837889492511749 | 0.0 | 0.0 | +23191bf1-a03a-47ab-aa04-1a5b6d86b445 / -— |
| Jogador 4 | 3-6 | 160 | MOVE_BENCH | STABILIZE | 53.0 | 5 | 6 | 0 | 16.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2396329641342163 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 162 | BUY | STABILIZE | 42.0 | 5 | 13 | 1 | 18.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7359884977340698 | 0.0 | 0.0 | +8ac322bc-799c-4d78-a2d5-e76b64ce900f / -— |
| Jogador 4 | 3-7 | 163 | BUY | STABILIZE | 42.0 | 5 | 10 | 1 | 18.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19968020915985107 | 0.0 | 0.0 | +9fd5cb87-62ee-43bc-85db-7f166ac20532 / -— |
| Jogador 4 | 3-7 | 164 | REROLL | STABILIZE | 42.0 | 5 | 7 | 0 | 18.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 165 | BUY | STABILIZE | 42.0 | 5 | 5 | 0 | 18.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.747998058795929 | 0.0 | 0.0 | +77742642-57e8-4594-8bb9-5b2e80a86ba1 / -— |
| Jogador 4 | 3-7 | 166 | REROLL | STABILIZE | 42.0 | 5 | 4 | 0 | 18.0 | Devastador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 3-7 | 167 | SELL | STABILIZE | 42.0 | 5 | 2 | 0 | 18.0 | Devastador/DA_Fiddlesticks18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08153846114873886 | 0.0 | 0.0 | +— / -0a0e7d41-96bf-404f-a3bf-98df0a182b63 |
| Jogador 4 | 3-7 | 168 | BUY | STABILIZE | 42.0 | 5 | 5 | 0 | 18.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7433646321296692 | 0.0 | 0.0 | +b9b2c784-d8ee-4a31-978f-58a686f22af2 / -— |
| Jogador 4 | 3-7 | 169 | SELL | STABILIZE | 42.0 | 5 | 2 | 0 | 18.0 | Devastador/DA_Fiddlesticks18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.008307692594826221 | 0.0 | 0.0 | +— / -daa7f698-2fa2-43d7-ae73-ec616b006db4 |
| Jogador 4 | 3-7 | 170 | MOVE_BENCH | STABILIZE | 42.0 | 5 | 7 | 0 | 18.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.524182915687561 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 172 | BUY | STABILIZE | 42.0 | 5 | 14 | 1 | 24.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.28308409452438354 | 0.0 | 0.0 | +15c32810-3029-4027-abcf-14005de787bf / -— |
| Jogador 4 | 4-1 | 173 | BUY | STABILIZE | 42.0 | 5 | 11 | 1 | 24.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.17871037125587463 | 0.0 | 0.0 | +4bc5b602-fe82-4525-b854-33dc5ab88a32 / -— |
| Jogador 4 | 4-1 | 174 | REROLL | STABILIZE | 42.0 | 5 | 8 | 0 | 24.0 | Devastador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 175 | SELL | STABILIZE | 42.0 | 5 | 6 | 0 | 24.0 | Devastador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05400000140070915 | 0.0 | 0.0 | +— / -f5ae964e-f157-48d1-8088-8b8a45a398b6 |
| Jogador 4 | 4-1 | 176 | BUY | STABILIZE | 42.0 | 5 | 8 | 0 | 24.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8332103490829468 | 0.0 | 0.0 | +97593afb-3c61-420c-ab5c-3bd92e0f1c5f / -23191bf1-a03a-47ab-aa04-1a5b6d86b445,b9b2c784-d8ee-4a31-978f-58a686f22af2 |
| Jogador 4 | 4-1 | 177 | BUY | STABILIZE | 42.0 | 5 | 5 | 0 | 24.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2681017518043518 | 0.0 | 0.0 | +8ef30c1a-60fd-4a11-bee3-08c3aa7baa32 / -— |
| Jogador 4 | 4-1 | 178 | REROLL | STABILIZE | 42.0 | 5 | 2 | 0 | 24.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 179 | CRAFT_AND_EQUIP | STABILIZE | 42.0 | 5 | 0 | 0 | 24.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.030094541609287262 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-1 | 180 | MOVE_BOARD | STABILIZE | 42.0 | 5 | 0 | 0 | 24.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07834406942129135 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 182 | BUY | STABILIZE | 30.0 | 6 | 8 | 0 | 24.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.36224478483200073 | 0.0 | 0.0 | +0088ca46-2bd7-4e4e-a102-8cfdc86bc494 / -— |
| Jogador 4 | 4-2 | 183 | MOVE_BENCH | STABILIZE | 30.0 | 6 | 5 | 0 | 24.0 | Devastador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5266844034194946 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 184 | BUY | STABILIZE | 30.0 | 6 | 5 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2803063690662384 | 0.0 | 0.0 | +28bfd469-8412-4227-af3a-4ac1cf3574ac / -— |
| Jogador 4 | 4-2 | 185 | REROLL | STABILIZE | 30.0 | 6 | 3 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011548471637070179 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 186 | MOVE_BOARD | STABILIZE | 30.0 | 6 | 1 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0800795927643776 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-2 | 187 | SELL | STABILIZE | 30.0 | 6 | 1 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04399999976158142 | 0.0 | 0.0 | +— / -8ef30c1a-60fd-4a11-bee3-08c3aa7baa32 |
| Jogador 4 | 4-2 | 188 | BUY | STABILIZE | 30.0 | 6 | 4 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5933252573013306 | 0.0 | 0.0 | +c5b1e71c-e078-4b1a-b6a9-1c016b1bc434 / -0088ca46-2bd7-4e4e-a102-8cfdc86bc494,c5520bc4-3123-40f3-b275-83fa8cb06309 |
| Jogador 4 | 4-2 | 189 | BUY | STABILIZE | 30.0 | 6 | 1 | 0 | 24.0 | Devastador/DA_Fiddlesticks18 | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22726202011108398 | 0.0 | 0.0 | +71b34398-0b5c-4b1a-8bfc-60ca14137847 / -— |
| Jogador 4 | 4-2 | 190 | MOVE_BENCH | STABILIZE | 30.0 | 6 | 0 | 0 | 24.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5240960121154785 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 192 | BUY | STABILIZE | 30.0 | 6 | 6 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05782901868224144 | 0.0 | 0.0 | +e90a9d02-3a67-45e5-aa87-11852bb4d172 / -— |
| Jogador 4 | 4-3 | 193 | REROLL | STABILIZE | 30.0 | 6 | 3 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03201870992779732 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 194 | MOVE_BOARD | STABILIZE | 30.0 | 6 | 1 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08623386919498444 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 195 | MOVE_BOARD | STABILIZE | 30.0 | 6 | 1 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 196 | MOVE_BOARD | STABILIZE | 30.0 | 6 | 1 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22443953156471252 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-3 | 197 | PASS | STABILIZE | 30.0 | 6 | 1 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 202 | SELL | STABILIZE | 19.0 | 6 | 6 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.032307691872119904 | 0.0 | 0.0 | +— / -e90a9d02-3a67-45e5-aa87-11852bb4d172 |
| Jogador 4 | 4-4 | 203 | BUY | STABILIZE | 19.0 | 6 | 9 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21900101006031036 | 0.0 | 0.0 | +69c7d1a0-a671-4a27-ac21-f8c65814a58f / -— |
| Jogador 4 | 4-4 | 204 | REROLL | STABILIZE | 19.0 | 6 | 6 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03250845894217491 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 205 | SELL | STABILIZE | 19.0 | 6 | 4 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01928982138633728 | 0.0 | 0.0 | +— / -4bc5b602-fe82-4525-b854-33dc5ab88a32 |
| Jogador 4 | 4-4 | 206 | BUY | STABILIZE | 19.0 | 6 | 7 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2079298496246338 | 0.0 | 0.0 | +cb56fa2e-fc68-4e3a-8bfa-99559ac5e882 / -— |
| Jogador 4 | 4-4 | 207 | REROLL | STABILIZE | 19.0 | 6 | 3 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.012596694752573967 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-4 | 208 | SELL | STABILIZE | 19.0 | 6 | 1 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34087932109832764 | 0.0 | 0.0 | +— / -71b34398-0b5c-4b1a-8bfc-60ca14137847 |
| Jogador 4 | 4-4 | 209 | BUY | STABILIZE | 19.0 | 6 | 2 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12189338356256485 | 0.0 | 0.0 | +fd9710d0-9c98-45e0-99e2-afb23f2de5b6 / -— |
| Jogador 4 | 4-4 | 210 | MOVE_BENCH | STABILIZE | 19.0 | 6 | 0 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11988131701946259 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 212 | SELL | STABILIZE | 19.0 | 6 | 5 | 0 | 28.0 | Devastador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.019026124849915504 | 0.0 | 0.0 | +— / -fd9710d0-9c98-45e0-99e2-afb23f2de5b6 |
| Jogador 4 | 4-5 | 213 | BUY | STABILIZE | 19.0 | 6 | 7 | 0 | 28.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8296948075294495 | 0.0 | 0.0 | +db4d17fd-b034-4363-9f4e-ee858ab141ce / -4c8a9a18-68d8-4672-a96d-bb09816257dc,8ac322bc-799c-4d78-a2d5-e76b64ce900f |
| Jogador 4 | 4-5 | 214 | BUY | STABILIZE | 19.0 | 6 | 4 | 0 | 22.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.043971315026283264 | 0.0 | 0.0 | +e0e6e609-efaf-4c37-b5f7-5204f65b0328 / -— |
| Jogador 4 | 4-5 | 215 | MOVE_BENCH | STABILIZE | 19.0 | 6 | 0 | 0 | 22.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6419395208358765 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 216 | MOVE_BOARD | STABILIZE | 19.0 | 6 | 0 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17400141060352325 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 217 | MOVE_BOARD | STABILIZE | 19.0 | 6 | 0 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.040938060730695724 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 218 | MOVE_BENCH | STABILIZE | 19.0 | 6 | 0 | 0 | 30.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03224485367536545 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 219 | MOVE_BOARD | STABILIZE | 19.0 | 6 | 0 | 0 | 26.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00416592275723815 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-5 | 220 | MOVE_BOARD | STABILIZE | 19.0 | 6 | 0 | 0 | 26.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10906810313463211 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 222 | BUY | STABILIZE | 19.0 | 6 | 6 | 0 | 26.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7450923323631287 | 0.0 | 0.0 | +1313ce0e-7069-44c1-a73e-25f180914bc5 / -— |
| Jogador 4 | 4-6 | 223 | SELL | STABILIZE | 19.0 | 6 | 4 | 0 | 26.0 | Devastador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3090203106403351 | 0.0 | 0.0 | +— / -e86a4466-cd1f-48a3-a825-cab2e361b72a |
| Jogador 4 | 4-6 | 224 | BUY | STABILIZE | 19.0 | 6 | 6 | 0 | 26.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27549535036087036 | 0.0 | 0.0 | +96188979-1f27-43e4-8e24-9ca5c3e3c8b3 / -— |
| Jogador 4 | 4-6 | 225 | REROLL | STABILIZE | 19.0 | 6 | 3 | 0 | 26.0 | Devastador/DA_Fiddlesticks18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.011889837682247162 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 226 | SELL | STABILIZE | 19.0 | 6 | 1 | 0 | 26.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04399999976158142 | 0.0 | 0.0 | +— / -96188979-1f27-43e4-8e24-9ca5c3e3c8b3 |
| Jogador 4 | 4-6 | 227 | BUY | STABILIZE | 19.0 | 6 | 4 | 0 | 26.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2836896777153015 | 0.0 | 0.0 | +4a5f3148-49c8-41e0-a6f3-d692eb52f11f / -— |
| Jogador 4 | 4-6 | 228 | REROLL | STABILIZE | 19.0 | 6 | 2 | 0 | 26.0 | Devastador/DA_Fiddlesticks18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-6 | 229 | SELL | STABILIZE | 19.0 | 6 | 0 | 0 | 26.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34969231486320496 | 0.0 | 0.0 | +— / -4a5f3148-49c8-41e0-a6f3-d692eb52f11f |
| Jogador 4 | 4-6 | 230 | BUY | STABILIZE | 19.0 | 6 | 2 | 0 | 26.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2567816972732544 | 0.0 | 0.0 | +63bbb476-c82b-4bd6-a317-96d26497272f / -— |
| Jogador 4 | 4-7 | 232 | SELL | ALL_IN | 7.0 | 6 | 5 | 0 | 26.0 | Devastador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028225192800164223 | 0.0 | 0.0 | +— / -63bbb476-c82b-4bd6-a317-96d26497272f |
| Jogador 4 | 4-7 | 233 | BUY | ALL_IN | 7.0 | 6 | 7 | 0 | 26.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27466022968292236 | 0.0 | 0.0 | +1e7aa6cb-56c4-4368-85c1-93d995fb2329 / -— |
| Jogador 4 | 4-7 | 234 | REROLL | ALL_IN | 7.0 | 6 | 4 | 0 | 26.0 | Devastador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032860517501831055 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 235 | REROLL | ALL_IN | 7.0 | 6 | 2 | 0 | 26.0 | Devastador/DA_Fiddlesticks18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 236 | MOVE_BOARD | ALL_IN | 7.0 | 6 | 0 | 0 | 26.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11359098553657532 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 237 | MOVE_BOARD | ALL_IN | 7.0 | 6 | 0 | 0 | 26.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12034890055656433 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 4-7 | 238 | PASS | ALL_IN | 7.0 | 6 | 0 | 0 | 26.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 242 | EQUIP_FROM_INVENTORY | ALL_IN | 7.0 | 6 | 5 | 0 | 26.0 | Devastador/DA_Fiddlesticks18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 243 | SELL | ALL_IN | 7.0 | 6 | 5 | 0 | 26.0 | Devastador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04399999976158142 | 0.0 | 0.0 | +— / -1e7aa6cb-56c4-4368-85c1-93d995fb2329 |
| Jogador 4 | 5-1 | 244 | BUY | ALL_IN | 7.0 | 6 | 8 | 0 | 26.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8256312608718872 | 0.0 | 0.0 | +ddbd72e5-1c12-4bf3-9af7-07dfcb4209d0 / -1313ce0e-7069-44c1-a73e-25f180914bc5,28bfd469-8412-4227-af3a-4ac1cf3574ac |
| Jogador 4 | 5-1 | 245 | BUY | ALL_IN | 7.0 | 6 | 6 | 0 | 22.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.008911370299756527 | 0.0 | 0.0 | +ab6ca634-da56-4578-90d4-d33a8f50fdbc / -— |
| Jogador 4 | 5-1 | 246 | REROLL | ALL_IN | 7.0 | 6 | 4 | 0 | 22.0 | Devastador/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010161650367081165 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 247 | REROLL | ALL_IN | 7.0 | 6 | 2 | 0 | 22.0 | Devastador/DA_Fiddlesticks18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-1 | 248 | SELL | ALL_IN | 7.0 | 6 | 0 | 0 | 22.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016827121376991272 | 0.0 | 0.0 | +— / -ab6ca634-da56-4578-90d4-d33a8f50fdbc |
| Jogador 4 | 5-1 | 249 | BUY | ALL_IN | 7.0 | 6 | 2 | 0 | 22.0 | Devastador/DA_Fiddlesticks18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2993342876434326 | 0.0 | 0.0 | +ce187695-1692-4144-8966-dcd791cf848c / -— |
| Jogador 4 | 5-1 | 250 | MOVE_BENCH | ALL_IN | 7.0 | 6 | 0 | 0 | 22.0 | Devastador/DA_Fiddlesticks18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.42180442810058594 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-2 | 252 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Devastador/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-3 | 262 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Devastador/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-4 | 272 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Devastador/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-5 | 282 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Devastador/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-6 | 292 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Devastador/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 5-7 | 302 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Devastador/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-1 | 312 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Devastador/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-2 | 322 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Devastador/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-3 | 332 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Devastador/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-4 | 342 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Devastador/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-5 | 352 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Devastador/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-6 | 362 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Devastador/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 6-7 | 372 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Devastador/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 7-1 | 382 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Devastador/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 7-2 | 392 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Devastador/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 4 | 7-3 | 402 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Devastador/DA_Fiddlesticks18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5562254786491394 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.13061420619487762 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Yorick | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.031732626259326935 | 0.0 | 0.0 | +df7d3860-9b2e-45ed-b564-281d95e64e82 / -— |
| Jogador 5 | 1-2 | 12 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24274566769599915 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 13 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.02016500011086464 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 14 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.14752550423145294 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-2 | 15 | PASS | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.2863394021987915 | 0.0 | 0.0 | +7098795b-11bf-4b73-837a-87f5d8aece4c / -— |
| Jogador 5 | 1-3 | 22 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33633941411972046 | 0.0 | 0.0 | +— / -7098795b-11bf-4b73-837a-87f5d8aece4c |
| Jogador 5 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.010312281548976898 | 0.0 | 0.0 | +4a7ac9c5-c110-4566-80e5-25d9e6033799 / -— |
| Jogador 5 | 1-3 | 24 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Elise | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.48899999260902405 | 0.0 | 0.0 | +— / -4a7ac9c5-c110-4566-80e5-25d9e6033799 |
| Jogador 5 | 1-3 | 25 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.32418757677078247 | 0.0 | 0.0 | +1934c7ef-cc22-45b3-bed9-01aea61ffbdb / -— |
| Jogador 5 | 1-4 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 3 | 0 | 6.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41819366812705994 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 33 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.032957449555397034 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 1-4 | 34 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Elise | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Elise | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2625862658023834 | 0.0 | 0.0 | +df330dae-9fc1-440f-896d-a733d052e5ba / -— |
| Jogador 5 | 2-1 | 42 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3568122684955597 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 43 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.17877088487148285 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 44 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.036966722458601 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-1 | 45 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2760005295276642 | 0.0 | 0.0 | +a5c3f6df-50ac-4f3b-aa9c-6476a055aa53 / -— |
| Jogador 5 | 2-1 | 46 | SELL | STABILIZE | 100.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.32600054144859314 | 0.0 | 0.0 | +— / -a5c3f6df-50ac-4f3b-aa9c-6476a055aa53 |
| Jogador 5 | 2-1 | 47 | PASS | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 50 | BUY | STABILIZE | 95.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.28175175189971924 | 0.0 | 0.0 | +68cd8ae3-399f-461f-89a8-189d7b0a6b59 / -— |
| Jogador 5 | 2-2 | 51 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 6 | 0 | 16.0 | —/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.047868456691503525 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 52 | SELL | STABILIZE | 95.0 | 4 | 6 | 0 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08015337586402893 | 0.0 | 0.0 | +— / -f9c418e0-f8aa-4492-8b97-8855ce3af370 |
| Jogador 5 | 2-2 | 53 | BUY | STABILIZE | 95.0 | 4 | 7 | 0 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.04468565061688423 | 0.0 | 0.0 | +9bb3da58-fe6f-4298-8529-859cceb4857e / -— |
| Jogador 5 | 2-2 | 54 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 4 | 0 | 20.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3722340166568756 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-2 | 55 | SELL | STABILIZE | 95.0 | 4 | 4 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.025188023224473 | 0.0 | 0.0 | +— / -df7d3860-9b2e-45ed-b564-281d95e64e82 |
| Jogador 5 | 2-2 | 56 | PASS | STABILIZE | 95.0 | 4 | 6 | 0 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-3 | 60 | BUY | STABILIZE | 95.0 | 4 | 12 | 1 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.44438719749450684 | 0.0 | 0.0 | +4367c039-e64e-4a3c-a49f-57cb2674a08f / -— |
| Jogador 5 | 2-3 | 61 | SELL | STABILIZE | 95.0 | 4 | 11 | 1 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4943871796131134 | 0.0 | 0.0 | +— / -4367c039-e64e-4a3c-a49f-57cb2674a08f |
| Jogador 5 | 2-3 | 62 | PASS | STABILIZE | 95.0 | 4 | 12 | 1 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-4 | 70 | BUY | STABILIZE | 95.0 | 4 | 20 | 2 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.36630773544311523 | 0.0 | 0.0 | +5f2c89f5-15c2-4a77-943e-4ba5492d925b / -— |
| Jogador 5 | 2-4 | 71 | SELL | STABILIZE | 95.0 | 4 | 17 | 1 | 22.0 | —/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47069230675697327 | 0.0 | 0.0 | +— / -5f2c89f5-15c2-4a77-943e-4ba5492d925b |
| Jogador 5 | 2-4 | 72 | BUY | STABILIZE | 95.0 | 4 | 20 | 2 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.229414701461792 | 0.0 | 0.0 | +82e3ae1b-a015-4fac-8624-f3b73ec1d90c / -— |
| Jogador 5 | 2-4 | 73 | SELL | STABILIZE | 95.0 | 4 | 18 | 1 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27941471338272095 | 0.0 | 0.0 | +— / -82e3ae1b-a015-4fac-8624-f3b73ec1d90c |
| Jogador 5 | 2-4 | 74 | PASS | STABILIZE | 95.0 | 4 | 20 | 2 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-5 | 80 | BUY | STABILIZE | 95.0 | 4 | 28 | 2 | 22.0 | —/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9545939564704895 | 0.0 | 0.0 | +cf4575c2-3622-4493-91f1-c5efbe1fbd8b / -— |
| Jogador 5 | 2-5 | 81 | SELL | STABILIZE | 95.0 | 4 | 25 | 2 | 22.0 | Defendente/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0045939683914185 | 0.0 | 0.0 | +— / -cf4575c2-3622-4493-91f1-c5efbe1fbd8b |
| Jogador 5 | 2-5 | 82 | PASS | STABILIZE | 95.0 | 4 | 28 | 2 | 22.0 | Defendente/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 89 | BUY | STABILIZE | 90.0 | 5 | 35 | 3 | 22.0 | Defendente/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.09157237410545349 | 0.0 | 0.0 | +b482ecdd-cc1a-40fa-8c21-cd1cac92b594 / -— |
| Jogador 5 | 2-6 | 90 | MOVE_BENCH | STABILIZE | 90.0 | 5 | 33 | 3 | 22.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45517125725746155 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 91 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 33 | 3 | 26.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.11952661722898483 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 92 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 33 | 3 | 26.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.01198225375264883 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 93 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 33 | 3 | 26.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 94 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 33 | 3 | 26.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.039354316890239716 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 95 | MOVE_BOARD | STABILIZE | 90.0 | 5 | 33 | 3 | 26.0 | Adaptador/DA_18_MasterYi_AD | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.05787229165434837 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-6 | 96 | BUY_XP | STABILIZE | 90.0 | 5 | 33 | 3 | 26.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 98 | BUY | STABILIZE | 84.0 | 5 | 37 | 3 | 26.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.02223614975810051 | 0.0 | 0.0 | +8980fd33-79c8-4825-95e9-9298680cbc6d / -— |
| Jogador 5 | 2-7 | 99 | SELL | STABILIZE | 84.0 | 5 | 35 | 3 | 26.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1923331469297409 | 0.0 | 0.0 | +— / -8980fd33-79c8-4825-95e9-9298680cbc6d |
| Jogador 5 | 2-7 | 100 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 37 | 3 | 26.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.32203829288482666 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 101 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 37 | 3 | 26.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1721227467060089 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 102 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 37 | 3 | 26.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.14391498267650604 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 103 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 37 | 3 | 26.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.19811506569385529 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 104 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 37 | 3 | 26.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.23221850395202637 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 2-7 | 105 | PASS | STABILIZE | 84.0 | 5 | 37 | 3 | 26.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 107 | BUY | STABILIZE | 84.0 | 5 | 46 | 4 | 26.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8079551458358765 | 0.0 | 0.0 | +fd3ab6e7-a3e5-4a03-8aa6-a80f6c0c1f47 / -— |
| Jogador 5 | 3-1 | 108 | SELL | SLOWROLL | 84.0 | 5 | 44 | 4 | 26.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.8885064125061035 | 0.0 | 0.0 | +— / -fd3ab6e7-a3e5-4a03-8aa6-a80f6c0c1f47 |
| Jogador 5 | 3-1 | 109 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 46 | 4 | 26.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.15327805280685425 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 110 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 46 | 4 | 26.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 111 | MOVE_BOARD | STABILIZE | 84.0 | 5 | 46 | 4 | 26.0 | Adaptador/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.27005159854888916 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-1 | 112 | PASS | STABILIZE | 84.0 | 5 | 46 | 4 | 26.0 | Adaptador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 116 | BUY | STABILIZE | 75.0 | 5 | 56 | 5 | 26.0 | Adaptador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8853447437286377 | 0.0 | 0.0 | +25b16126-6e41-4649-a47f-42656ffc7a08 / -— |
| Jogador 5 | 3-2 | 117 | MOVE_BOARD | SLOWROLL | 75.0 | 5 | 54 | 5 | 26.0 | Adaptador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15562081336975098 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 118 | MOVE_BOARD | SLOWROLL | 75.0 | 5 | 54 | 5 | 26.0 | Adaptador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06667235493659973 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 119 | SELL | SLOWROLL | 75.0 | 5 | 54 | 5 | 26.0 | Adaptador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9353447556495667 | 0.0 | 0.0 | +— / -25b16126-6e41-4649-a47f-42656ffc7a08 |
| Jogador 5 | 3-2 | 120 | BUY | STABILIZE | 75.0 | 5 | 56 | 5 | 26.0 | Adaptador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3743864893913269 | 0.0 | 0.0 | +952adeb2-fe24-47af-9748-5131b91dcc06 / -— |
| Jogador 5 | 3-2 | 121 | SELL | STABILIZE | 75.0 | 5 | 54 | 5 | 26.0 | Adaptador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5265682935714722 | 0.0 | 0.0 | +— / -952adeb2-fe24-47af-9748-5131b91dcc06 |
| Jogador 5 | 3-2 | 122 | MOVE_BOARD | STABILIZE | 75.0 | 5 | 56 | 5 | 26.0 | Adaptador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.108271025121212 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-2 | 123 | MOVE_BOARD | STABILIZE | 75.0 | 5 | 56 | 5 | 26.0 | Adaptador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.16555269062519073 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 125 | BUY | STABILIZE | 75.0 | 5 | 67 | 5 | 26.0 | Adaptador/DA_18_Cassiopeia | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.08409363031387329 | 0.0 | 0.0 | +7c8b3027-1434-4346-95b3-5463e8a4aa9b / -— |
| Jogador 5 | 3-3 | 126 | BUY | STABILIZE | 75.0 | 5 | 63 | 5 | 26.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.680317759513855 | 0.0 | 0.0 | +42f739bb-e676-4a27-a96f-c09d09d592bb / -— |
| Jogador 5 | 3-3 | 127 | MOVE_BENCH | STABILIZE | 75.0 | 5 | 60 | 5 | 26.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7407709956169128 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 128 | MOVE_BENCH | SLOWROLL | 75.0 | 5 | 60 | 5 | 26.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2918044626712799 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-3 | 129 | PASS | SLOWROLL | 75.0 | 5 | 60 | 5 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.004412064794450998 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 134 | BUY | SLOWROLL | 75.0 | 5 | 72 | 5 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8467825651168823 | 0.0 | 0.0 | +97d52b06-365b-44ad-b4f9-63e0f9503c8a / -— |
| Jogador 5 | 3-4 | 135 | REROLL | SLOWROLL | 75.0 | 5 | 70 | 5 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24987687170505524 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 136 | BUY | SLOWROLL | 75.0 | 5 | 68 | 5 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3775463104248047 | 0.0 | 0.0 | +86530a1f-5325-45fa-bf43-86419ccfda54 / -— |
| Jogador 5 | 3-4 | 137 | REROLL | SLOWROLL | 75.0 | 5 | 65 | 5 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17459018528461456 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 138 | REROLL | SLOWROLL | 75.0 | 5 | 63 | 5 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03971191123127937 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 139 | BUY | SLOWROLL | 75.0 | 5 | 61 | 5 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025829344987869263 | 0.0 | 0.0 | +b837d2e1-b93f-4cc2-b9b8-7c3e3582f4e9 / -— |
| Jogador 5 | 3-4 | 140 | REROLL | SLOWROLL | 75.0 | 5 | 58 | 5 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2141987681388855 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-4 | 141 | BUY | SLOWROLL | 75.0 | 5 | 56 | 5 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23042277991771698 | 0.0 | 0.0 | +3a1de7b3-af72-4024-8105-588fa4ec946b / -— |
| Jogador 5 | 3-5 | 143 | BUY | SLOWROLL | 75.0 | 5 | 64 | 5 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10702511668205261 | 0.0 | 0.0 | +50edcbf1-13cd-4f98-bf35-d5a474fbe20c / -— |
| Jogador 5 | 3-5 | 144 | BUY | SLOWROLL | 75.0 | 5 | 61 | 5 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20087160170078278 | 0.0 | 0.0 | +51a5a5d7-c5ea-43e2-a521-22fe0275c231 / -— |
| Jogador 5 | 3-5 | 145 | REROLL | SLOWROLL | 75.0 | 5 | 59 | 5 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24999485909938812 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 146 | BUY | SLOWROLL | 75.0 | 5 | 57 | 5 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7349117994308472 | 0.0 | 0.0 | +a64cf09b-42bf-494e-9603-d387b6740200 / -— |
| Jogador 5 | 3-5 | 147 | REROLL | SLOWROLL | 75.0 | 5 | 54 | 5 | 28.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24887511134147644 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-5 | 148 | SELL | SLOWROLL | 75.0 | 5 | 52 | 5 | 28.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026307692751288414 | 0.0 | 0.0 | +— / -b837d2e1-b93f-4cc2-b9b8-7c3e3582f4e9 |
| Jogador 5 | 3-5 | 149 | BUY | SLOWROLL | 75.0 | 5 | 55 | 5 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8296383619308472 | 0.0 | 0.0 | +9f445115-49cc-4647-91a0-a80e347e9c62 / -97d52b06-365b-44ad-b4f9-63e0f9503c8a,b482ecdd-cc1a-40fa-8c21-cd1cac92b594 |
| Jogador 5 | 3-5 | 150 | BUY | SLOWROLL | 75.0 | 5 | 53 | 5 | 28.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6593601703643799 | 0.0 | 0.0 | +b701c6c1-2e19-44b9-ad6e-e5d64e1d364c / -— |
| Jogador 5 | 3-6 | 152 | BUY | SLOWROLL | 65.0 | 5 | 61 | 5 | 28.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25992530584335327 | 0.0 | 0.0 | +b250e22d-7193-4ea5-879d-5c7b41145719 / -— |
| Jogador 5 | 3-6 | 153 | REROLL | SLOWROLL | 65.0 | 5 | 60 | 5 | 28.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24988457560539246 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 154 | SELL | SLOWROLL | 65.0 | 5 | 58 | 5 | 28.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -3a1de7b3-af72-4024-8105-588fa4ec946b |
| Jogador 5 | 3-6 | 155 | BUY | SLOWROLL | 65.0 | 5 | 61 | 5 | 28.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2528354525566101 | 0.0 | 0.0 | +17279599-f3fc-4cf2-874f-da62a23ac238 / -— |
| Jogador 5 | 3-6 | 156 | SELL | SLOWROLL | 65.0 | 5 | 58 | 5 | 28.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.013431495055556297 | 0.0 | 0.0 | +— / -50edcbf1-13cd-4f98-bf35-d5a474fbe20c |
| Jogador 5 | 3-6 | 157 | BUY | SLOWROLL | 65.0 | 5 | 61 | 5 | 28.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7199203372001648 | 0.0 | 0.0 | +9af00d66-f862-45b7-98d4-93fbd69fedba / -— |
| Jogador 5 | 3-6 | 158 | REROLL | SLOWROLL | 65.0 | 5 | 60 | 5 | 28.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04199417307972908 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 159 | REROLL | SLOWROLL | 65.0 | 5 | 58 | 5 | 28.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.047979749739170074 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-6 | 160 | REROLL | SLOWROLL | 65.0 | 5 | 56 | 5 | 28.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03500000014901161 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 162 | SELL | SLOWROLL | 65.0 | 6 | 65 | 5 | 28.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6853220462799072 | 0.0 | 0.0 | +— / -b250e22d-7193-4ea5-879d-5c7b41145719 |
| Jogador 5 | 3-7 | 163 | BUY | SLOWROLL | 65.0 | 6 | 66 | 5 | 28.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060856521129608154 | 0.0 | 0.0 | +50d7d851-387f-449e-8456-45a445f89cb7 / -— |
| Jogador 5 | 3-7 | 164 | SELL | SLOWROLL | 65.0 | 6 | 64 | 5 | 28.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02677985653281212 | 0.0 | 0.0 | +— / -50d7d851-387f-449e-8456-45a445f89cb7 |
| Jogador 5 | 3-7 | 165 | BUY | SLOWROLL | 65.0 | 6 | 66 | 5 | 28.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0693608969449997 | 0.0 | 0.0 | +bf2246f7-4b73-4b2b-92ad-56849f783dfb / -— |
| Jogador 5 | 3-7 | 166 | REROLL | SLOWROLL | 65.0 | 6 | 64 | 5 | 28.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.16287440061569214 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 167 | SELL | SLOWROLL | 65.0 | 6 | 62 | 5 | 28.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025567052885890007 | 0.0 | 0.0 | +— / -bf2246f7-4b73-4b2b-92ad-56849f783dfb |
| Jogador 5 | 3-7 | 168 | BUY | SLOWROLL | 65.0 | 6 | 64 | 5 | 28.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06148625165224075 | 0.0 | 0.0 | +23181987-d0b2-4e8c-a1a7-48a1e28179f7 / -— |
| Jogador 5 | 3-7 | 169 | MOVE_BENCH | SLOWROLL | 65.0 | 6 | 61 | 5 | 28.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5948286056518555 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 3-7 | 170 | BUY | SLOWROLL | 65.0 | 6 | 61 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07193759828805923 | 0.0 | 0.0 | +a920ed77-ca29-4616-afba-e4c7759b2d68 / -— |
| Jogador 5 | 4-1 | 172 | SELL | SLOWROLL | 65.0 | 6 | 69 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04221884161233902 | 0.0 | 0.0 | +— / -a920ed77-ca29-4616-afba-e4c7759b2d68 |
| Jogador 5 | 4-1 | 173 | BUY | SLOWROLL | 65.0 | 6 | 71 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.660650372505188 | 0.0 | 0.0 | +d4fd64a7-2945-4d09-ab2e-5bd475ff0f04 / -— |
| Jogador 5 | 4-1 | 174 | SELL | SLOWROLL | 65.0 | 6 | 67 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029999999329447746 | 0.0 | 0.0 | +— / -23181987-d0b2-4e8c-a1a7-48a1e28179f7 |
| Jogador 5 | 4-1 | 175 | BUY | SLOWROLL | 65.0 | 6 | 70 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3263404369354248 | 0.0 | 0.0 | +c8f70274-150a-4de3-8eb3-5a635e03ab3a / -— |
| Jogador 5 | 4-1 | 176 | REROLL | SLOWROLL | 65.0 | 6 | 68 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21999293565750122 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 177 | REROLL | SLOWROLL | 65.0 | 6 | 66 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11699417233467102 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 178 | REROLL | SLOWROLL | 65.0 | 6 | 64 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24990420043468475 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-1 | 179 | SELL | SLOWROLL | 65.0 | 6 | 62 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3775668442249298 | 0.0 | 0.0 | +— / -9af00d66-f862-45b7-98d4-93fbd69fedba |
| Jogador 5 | 4-1 | 180 | BUY | SLOWROLL | 65.0 | 6 | 63 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13633406162261963 | 0.0 | 0.0 | +fe064601-d4d8-4f7d-860d-cae70b1d7ee8 / -— |
| Jogador 5 | 4-2 | 182 | SELL | SLOWROLL | 65.0 | 6 | 71 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.00938461534678936 | 0.0 | 0.0 | +— / -fe064601-d4d8-4f7d-860d-cae70b1d7ee8 |
| Jogador 5 | 4-2 | 183 | BUY | SLOWROLL | 65.0 | 6 | 75 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5460801124572754 | 0.0 | 0.0 | +48db898e-cf31-47c7-aab7-fd47be1938a1 / -— |
| Jogador 5 | 4-2 | 184 | REROLL | SLOWROLL | 65.0 | 6 | 72 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11408593505620956 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 185 | SELL | SLOWROLL | 65.0 | 6 | 70 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2979937493801117 | 0.0 | 0.0 | +— / -48db898e-cf31-47c7-aab7-fd47be1938a1 |
| Jogador 5 | 4-2 | 186 | BUY | SLOWROLL | 65.0 | 6 | 73 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.053160425275564194 | 0.0 | 0.0 | +9c63f663-15d2-40da-b542-1c25db09445d / -— |
| Jogador 5 | 4-2 | 187 | SELL | SLOWROLL | 65.0 | 6 | 69 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02476923167705536 | 0.0 | 0.0 | +— / -9c63f663-15d2-40da-b542-1c25db09445d |
| Jogador 5 | 4-2 | 188 | BUY | SLOWROLL | 65.0 | 6 | 73 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05314755439758301 | 0.0 | 0.0 | +993e2955-9769-4af0-b3c4-6bc092f8e221 / -— |
| Jogador 5 | 4-2 | 189 | REROLL | SLOWROLL | 65.0 | 6 | 69 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24979524314403534 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-2 | 190 | SELL | SLOWROLL | 65.0 | 6 | 67 | 5 | 32.0 | Adaptador/DA_Gromp18_AP | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13267895579338074 | 0.0 | 0.0 | +— / -9f445115-49cc-4647-91a0-a80e347e9c62 |
| Jogador 5 | 4-3 | 192 | BUY | SLOWROLL | 65.0 | 6 | 84 | 5 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.43610915541648865 | 0.0 | 0.0 | +65c7d421-db2b-4d8c-bd60-ca83bd7a8826 / -— |
| Jogador 5 | 4-3 | 193 | REROLL | SLOWROLL | 65.0 | 6 | 82 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16222810745239258 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 194 | SELL | SLOWROLL | 65.0 | 6 | 80 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28446152806282043 | 0.0 | 0.0 | +— / -65c7d421-db2b-4d8c-bd60-ca83bd7a8826 |
| Jogador 5 | 4-3 | 195 | BUY | SLOWROLL | 65.0 | 6 | 82 | 5 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14375610649585724 | 0.0 | 0.0 | +9a402e82-9805-4215-8de7-78f6563682e1 / -— |
| Jogador 5 | 4-3 | 196 | SELL | SLOWROLL | 65.0 | 6 | 79 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3444615304470062 | 0.0 | 0.0 | +— / -c8f70274-150a-4de3-8eb3-5a635e03ab3a |
| Jogador 5 | 4-3 | 197 | BUY | SLOWROLL | 65.0 | 6 | 81 | 5 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6452247500419617 | 0.0 | 0.0 | +abcf299e-8cd5-4da6-abf8-6fc8af7b615b / -— |
| Jogador 5 | 4-3 | 198 | REROLL | SLOWROLL | 65.0 | 6 | 78 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2499467432498932 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-3 | 199 | SELL | SLOWROLL | 65.0 | 6 | 76 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2743076980113983 | 0.0 | 0.0 | +— / -abcf299e-8cd5-4da6-abf8-6fc8af7b615b |
| Jogador 5 | 4-3 | 200 | BUY | SLOWROLL | 65.0 | 6 | 79 | 5 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8890296220779419 | 0.0 | 0.0 | +710a9371-d633-4712-9f22-48c3d95a2e1a / -51a5a5d7-c5ea-43e2-a521-22fe0275c231,b701c6c1-2e19-44b9-ad6e-e5d64e1d364c |
| Jogador 5 | 4-4 | 202 | BUY | SLOWROLL | 65.0 | 6 | 89 | 5 | 28.0 | Adaptador/DA_18_Shen | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8898690342903137 | 0.0 | 0.0 | +e94c2568-704b-45c7-a095-9a52bc5a3de6 / -7c8b3027-1434-4346-95b3-5463e8a4aa9b,d4fd64a7-2945-4d09-ab2e-5bd475ff0f04 |
| Jogador 5 | 4-4 | 203 | BUY | SLOWROLL | 65.0 | 6 | 85 | 5 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2943178713321686 | 0.0 | 0.0 | +a8a17076-c60b-498a-916c-fbe4b621fe2c / -— |
| Jogador 5 | 4-4 | 204 | BUY | SLOWROLL | 65.0 | 6 | 83 | 5 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19603492319583893 | 0.0 | 0.0 | +12d2321e-ca91-470c-8432-1604d2fd292d / -— |
| Jogador 5 | 4-4 | 205 | REROLL | SLOWROLL | 65.0 | 6 | 79 | 5 | 28.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2018408328294754 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-4 | 206 | SELL | SLOWROLL | 65.0 | 6 | 77 | 5 | 28.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03799999877810478 | 0.0 | 0.0 | +— / -9a402e82-9805-4215-8de7-78f6563682e1 |
| Jogador 5 | 4-4 | 207 | BUY | SLOWROLL | 65.0 | 6 | 80 | 5 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2879990041255951 | 0.0 | 0.0 | +c3ffcc8c-9d09-4d3e-ba6a-16a833a9217c / -— |
| Jogador 5 | 4-4 | 208 | SELL | SLOWROLL | 65.0 | 6 | 78 | 5 | 28.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04938461631536484 | 0.0 | 0.0 | +— / -12d2321e-ca91-470c-8432-1604d2fd292d |
| Jogador 5 | 4-4 | 209 | BUY | SLOWROLL | 65.0 | 6 | 82 | 5 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2030874490737915 | 0.0 | 0.0 | +8986ba29-bec2-4d88-82a7-1838d4609407 / -— |
| Jogador 5 | 4-4 | 210 | MOVE_BENCH | SLOWROLL | 65.0 | 6 | 80 | 5 | 28.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5978365540504456 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 212 | BUY | SLOWROLL | 65.0 | 6 | 91 | 5 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7732216715812683 | 0.0 | 0.0 | +38acd55a-2e81-4974-a4ff-e7d2b4df1895 / -— |
| Jogador 5 | 4-5 | 213 | SELL | SLOWROLL | 65.0 | 6 | 89 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.042192257940769196 | 0.0 | 0.0 | +— / -8986ba29-bec2-4d88-82a7-1838d4609407 |
| Jogador 5 | 4-5 | 214 | BUY | SLOWROLL | 65.0 | 6 | 91 | 5 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29564225673675537 | 0.0 | 0.0 | +bbb318f2-3202-4b04-9dd4-27d1c6f7fa94 / -— |
| Jogador 5 | 4-5 | 215 | REROLL | SLOWROLL | 65.0 | 6 | 87 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2491859644651413 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 216 | SELL | SLOWROLL | 65.0 | 6 | 85 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02476923167705536 | 0.0 | 0.0 | +— / -993e2955-9769-4af0-b3c4-6bc092f8e221 |
| Jogador 5 | 4-5 | 217 | BUY | SLOWROLL | 65.0 | 6 | 89 | 5 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8739455342292786 | 0.0 | 0.0 | +e64dae56-8784-4981-a9df-66ebc6752033 / -42f739bb-e676-4a27-a96f-c09d09d592bb,9bb3da58-fe6f-4298-8529-859cceb4857e |
| Jogador 5 | 4-5 | 218 | MOVE_BENCH | SLOWROLL | 65.0 | 6 | 86 | 5 | 20.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.37107962369918823 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-5 | 219 | BUY | SLOWROLL | 65.0 | 6 | 86 | 5 | 28.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08409540355205536 | 0.0 | 0.0 | +40d482e2-24f1-4682-aa20-37c097d7a764 / -— |
| Jogador 5 | 4-5 | 220 | MOVE_BENCH | SLOWROLL | 65.0 | 6 | 83 | 5 | 28.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.554271399974823 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 222 | BUY | SLOWROLL | 54.0 | 6 | 93 | 5 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2660377323627472 | 0.0 | 0.0 | +c1dcff8f-5911-4db4-b328-63a6e151d037 / -— |
| Jogador 5 | 4-6 | 223 | REROLL | SLOWROLL | 54.0 | 6 | 90 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2499968707561493 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 224 | SELL | SLOWROLL | 54.0 | 6 | 88 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2730769217014313 | 0.0 | 0.0 | +— / -c1dcff8f-5911-4db4-b328-63a6e151d037 |
| Jogador 5 | 4-6 | 225 | BUY | SLOWROLL | 54.0 | 6 | 91 | 5 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8899465203285217 | 0.0 | 0.0 | +4fbb6900-3a31-4ec9-81d1-cf87cb3b61ad / -86530a1f-5325-45fa-bf43-86419ccfda54,a64cf09b-42bf-494e-9603-d387b6740200 |
| Jogador 5 | 4-6 | 226 | BUY | SLOWROLL | 54.0 | 6 | 88 | 5 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.755036473274231 | 0.0 | 0.0 | +78aae25e-f89f-474e-802a-61c7508d96b0 / -— |
| Jogador 5 | 4-6 | 227 | BUY | SLOWROLL | 54.0 | 6 | 85 | 5 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25269609689712524 | 0.0 | 0.0 | +90f92c4e-6ab5-4513-8515-60f179cd057a / -— |
| Jogador 5 | 4-6 | 228 | REROLL | SLOWROLL | 54.0 | 6 | 83 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15459290146827698 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 229 | REROLL | SLOWROLL | 54.0 | 6 | 81 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03500000014901161 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-6 | 230 | REROLL | SLOWROLL | 54.0 | 6 | 79 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12395352125167847 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 232 | REROLL | SLOWROLL | 42.0 | 6 | 88 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03500000014901161 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 233 | REROLL | SLOWROLL | 42.0 | 6 | 86 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12380678206682205 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 234 | REROLL | SLOWROLL | 42.0 | 6 | 84 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19203367829322815 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 235 | REROLL | SLOWROLL | 42.0 | 6 | 82 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.25692689418792725 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 236 | SELL | SLOWROLL | 42.0 | 6 | 80 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -90f92c4e-6ab5-4513-8515-60f179cd057a |
| Jogador 5 | 4-7 | 237 | BUY | SLOWROLL | 42.0 | 6 | 82 | 5 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15646351873874664 | 0.0 | 0.0 | +bf42dcf7-f690-4a8c-89ab-9b10a4eb826f / -— |
| Jogador 5 | 4-7 | 238 | REROLL | SLOWROLL | 42.0 | 6 | 78 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18196441233158112 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 239 | REROLL | SLOWROLL | 42.0 | 6 | 76 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15697135031223297 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 4-7 | 240 | REROLL | SLOWROLL | 42.0 | 6 | 74 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03500000014901161 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 242 | EQUIP_FROM_INVENTORY | SLOWROLL | 42.0 | 6 | 83 | 5 | 32.0 | Adaptador/DA_18_Ahri | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 243 | REROLL | SLOWROLL | 42.0 | 6 | 83 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.25687023997306824 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 244 | SELL | SLOWROLL | 42.0 | 6 | 81 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.039230767637491226 | 0.0 | 0.0 | +— / -40d482e2-24f1-4682-aa20-37c097d7a764 |
| Jogador 5 | 5-1 | 245 | BUY | SLOWROLL | 42.0 | 6 | 84 | 5 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9491018652915955 | 0.0 | 0.0 | +f7df2469-9148-4844-8503-b6cd8096b5fc / -38acd55a-2e81-4974-a4ff-e7d2b4df1895,a8a17076-c60b-498a-916c-fbe4b621fe2c |
| Jogador 5 | 5-1 | 246 | MOVE_BENCH | SLOWROLL | 42.0 | 6 | 82 | 5 | 24.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.21415244042873383 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 247 | MOVE_BENCH | SLOWROLL | 42.0 | 6 | 82 | 5 | 24.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3379420042037964 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 248 | BUY | SLOWROLL | 42.0 | 6 | 82 | 5 | 32.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7814750075340271 | 0.0 | 0.0 | +7b8a1dbd-1935-4c49-bbfd-1a450e17f6d9 / -— |
| Jogador 5 | 5-1 | 249 | REROLL | SLOWROLL | 42.0 | 6 | 80 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.16816170513629913 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-1 | 250 | MOVE_BENCH | SLOWROLL | 42.0 | 6 | 78 | 5 | 32.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8782570362091064 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 252 | BUY | SLOWROLL | 42.0 | 6 | 89 | 5 | 44.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.36540403962135315 | 0.0 | 0.0 | +2f666573-57c7-46db-9be8-2f04c00686b0 / -— |
| Jogador 5 | 5-2 | 253 | REROLL | SLOWROLL | 42.0 | 6 | 87 | 5 | 44.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0873151645064354 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 254 | REROLL | SLOWROLL | 42.0 | 6 | 85 | 5 | 44.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2569884657859802 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 255 | SELL | SLOWROLL | 42.0 | 6 | 83 | 5 | 44.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.01582220382988453 | 0.0 | 0.0 | +— / -e64dae56-8784-4981-a9df-66ebc6752033 |
| Jogador 5 | 5-2 | 256 | BUY | SLOWROLL | 42.0 | 6 | 91 | 5 | 44.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7921391725540161 | 0.0 | 0.0 | +5b26cffc-a739-41f1-acf8-d454592ff9a0 / -— |
| Jogador 5 | 5-2 | 257 | REROLL | SLOWROLL | 42.0 | 6 | 88 | 5 | 44.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.15944720804691315 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-2 | 258 | SELL | SLOWROLL | 42.0 | 6 | 86 | 5 | 44.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0006773684290237725 | 0.0 | 0.0 | +— / -bf42dcf7-f690-4a8c-89ab-9b10a4eb826f |
| Jogador 5 | 5-2 | 259 | BUY | SLOWROLL | 42.0 | 6 | 90 | 5 | 44.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9495987296104431 | 0.0 | 0.0 | +440f683c-14ad-4a65-8a2c-55219797b67b / -68cd8ae3-399f-461f-89a8-189d7b0a6b59,78aae25e-f89f-474e-802a-61c7508d96b0 |
| Jogador 5 | 5-2 | 260 | MOVE_BENCH | SLOWROLL | 42.0 | 6 | 87 | 5 | 38.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5387346744537354 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 262 | BUY | STABILIZE | 26.0 | 6 | 97 | 5 | 42.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0191800594329834 | 0.0 | 0.0 | +ca61694e-189a-45e8-ac5e-98aacdc4ddae / -7b8a1dbd-1935-4c49-bbfd-1a450e17f6d9,c3ffcc8c-9d09-4d3e-ba6a-16a833a9217c |
| Jogador 5 | 5-3 | 263 | REROLL | STABILIZE | 26.0 | 6 | 95 | 5 | 42.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05448434501886368 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 264 | REROLL | STABILIZE | 26.0 | 6 | 93 | 5 | 42.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.08948473632335663 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 265 | REROLL | STABILIZE | 26.0 | 6 | 91 | 5 | 42.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0610036700963974 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 266 | REROLL | STABILIZE | 26.0 | 6 | 89 | 5 | 42.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03458549827337265 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 267 | REROLL | STABILIZE | 26.0 | 6 | 87 | 5 | 42.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05432296544313431 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 268 | BUY | STABILIZE | 26.0 | 6 | 85 | 5 | 42.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.47099369764328003 | 0.0 | 0.0 | +2483483f-7d4d-4f51-a31b-b2b771a1598d / -— |
| Jogador 5 | 5-3 | 269 | REROLL | STABILIZE | 26.0 | 6 | 83 | 5 | 42.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.007432020269334316 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-3 | 270 | REROLL | STABILIZE | 26.0 | 6 | 81 | 5 | 42.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.02977997064590454 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 272 | REROLL | ALL_IN | 13.0 | 6 | 90 | 5 | 42.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.053546831011772156 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 273 | REROLL | ALL_IN | 13.0 | 6 | 88 | 5 | 42.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.02500000037252903 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 274 | REROLL | ALL_IN | 13.0 | 6 | 86 | 5 | 42.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03395148739218712 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 275 | REROLL | ALL_IN | 13.0 | 6 | 84 | 5 | 42.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.05972040072083473 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 276 | REROLL | ALL_IN | 13.0 | 6 | 82 | 5 | 42.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.02730274386703968 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 277 | REROLL | ALL_IN | 13.0 | 6 | 80 | 5 | 42.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.06510721892118454 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 278 | BUY | ALL_IN | 13.0 | 6 | 78 | 5 | 42.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8670437335968018 | 0.0 | 0.0 | +6786e33c-e226-4ff2-b5b1-b1abb5669b2a / -— |
| Jogador 5 | 5-4 | 279 | REROLL | ALL_IN | 13.0 | 6 | 76 | 5 | 42.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.05799382925033569 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-4 | 280 | REROLL | ALL_IN | 13.0 | 6 | 74 | 5 | 42.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.06511390954256058 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 282 | BUY | ALL_IN | 13.0 | 6 | 83 | 5 | 42.0 | Adaptador/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8752342462539673 | 0.0 | 0.0 | +6e1edeac-0328-4a50-a0d9-69246483f00d / -— |
| Jogador 5 | 5-5 | 283 | REROLL | ALL_IN | 13.0 | 6 | 81 | 5 | 42.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07152508944272995 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 284 | REROLL | ALL_IN | 13.0 | 6 | 79 | 5 | 42.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.02500000037252903 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 285 | REROLL | ALL_IN | 13.0 | 6 | 77 | 5 | 42.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03651219978928566 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 286 | REROLL | ALL_IN | 13.0 | 6 | 75 | 5 | 42.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10011815279722214 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 287 | REROLL | ALL_IN | 13.0 | 6 | 73 | 5 | 42.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.04712328687310219 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 288 | REROLL | ALL_IN | 13.0 | 6 | 71 | 5 | 42.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03630366176366806 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 289 | REROLL | ALL_IN | 13.0 | 6 | 69 | 5 | 42.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07147101312875748 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-5 | 290 | REROLL | ALL_IN | 13.0 | 6 | 67 | 5 | 42.0 | Adaptador/DA_18_Ahri | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.008255108259618282 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-6 | 292 | PASS | ALL_IN | 0.0 | 6 | 65 | 5 | 0.0 | Adaptador/DA_18_Ahri | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 5-7 | 302 | PASS | ALL_IN | 0.0 | 6 | 65 | 5 | 0.0 | Adaptador/DA_18_Ahri | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-1 | 312 | PASS | ALL_IN | 0.0 | 6 | 65 | 5 | 0.0 | Adaptador/DA_18_Ahri | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-2 | 322 | PASS | ALL_IN | 0.0 | 6 | 65 | 5 | 0.0 | Adaptador/DA_18_Ahri | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-3 | 332 | PASS | ALL_IN | 0.0 | 6 | 65 | 5 | 0.0 | Adaptador/DA_18_Ahri | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-4 | 342 | PASS | ALL_IN | 0.0 | 6 | 65 | 5 | 0.0 | Adaptador/DA_18_Ahri | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-5 | 352 | PASS | ALL_IN | 0.0 | 6 | 65 | 5 | 0.0 | Adaptador/DA_18_Ahri | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-6 | 362 | PASS | ALL_IN | 0.0 | 6 | 65 | 5 | 0.0 | Adaptador/DA_18_Ahri | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 6-7 | 372 | PASS | ALL_IN | 0.0 | 6 | 65 | 5 | 0.0 | Adaptador/DA_18_Ahri | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 7-1 | 382 | PASS | ALL_IN | 0.0 | 6 | 65 | 5 | 0.0 | Adaptador/DA_18_Ahri | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 7-2 | 392 | PASS | ALL_IN | 0.0 | 6 | 65 | 5 | 0.0 | Adaptador/DA_18_Ahri | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 5 | 7-3 | 402 | PASS | ALL_IN | 0.0 | 6 | 65 | 5 | 0.0 | Adaptador/DA_18_Ahri | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.0013076922623440623 | 0.0 | 0.0 | +— / -698cc451-66f5-4a58-901b-20de596311c9 |
| Jogador 6 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +9002992e-4dcd-4fec-939c-87393464a41d / -— |
| Jogador 6 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.5990749597549438 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 4 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.13061420619487762 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-1 | 5 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.05254174768924713 | 0.0 | 0.0 | +4d0bf502-ac30-4cdb-9da7-4f9a7ab054b1 / -— |
| Jogador 6 | 1-2 | 12 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 2.0 | —/DA_18_Yunara | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21062685549259186 | 0.0 | 0.0 | +— / -4d0bf502-ac30-4cdb-9da7-4f9a7ab054b1 |
| Jogador 6 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.3395138382911682 | 0.0 | 0.0 | +3f36fd3d-e557-4f66-92c9-8800b482a6d2 / -— |
| Jogador 6 | 1-2 | 14 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.38951385021209717 | 0.0 | 0.0 | +— / -3f36fd3d-e557-4f66-92c9-8800b482a6d2 |
| Jogador 6 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.33910518884658813 | 0.0 | 0.0 | +908afab9-748c-4057-a2a9-d2686c5d52e0 / -— |
| Jogador 6 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15336990356445312 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0849403440952301 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Yorick | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.023336518555879593 | 0.0 | 0.0 | +f29b0444-8dd6-44a6-9a04-824febf737a0 / -— |
| Jogador 6 | 1-3 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Caitlyn | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2686740756034851 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 23 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Caitlyn | BUY, MOVE_BOARD, PASS | True | True | 0.0021665620151907206 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-3 | 24 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_18_Caitlyn | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_18_Caitlyn | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.001331782783381641 | 0.0 | 0.0 | +c19cf6a8-c66e-4670-b0fc-fb83453f22e7 / -— |
| Jogador 6 | 1-4 | 32 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_18_Caitlyn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5110357403755188 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 1-4 | 33 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 10.0 | —/DA_18_Caitlyn | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07221514731645584 | 0.0 | 0.0 | +— / -9002992e-4dcd-4fec-939c-87393464a41d |
| Jogador 6 | 1-4 | 34 | PASS | STABILIZE | 100.0 | 3 | 3 | 0 | 10.0 | —/DA_18_Caitlyn | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 7 | 0 | 10.0 | —/DA_18_Caitlyn | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.042241379618644714 | 0.0 | 0.0 | +75005e9c-56d1-48d6-815e-573e489e3dd7 / -— |
| Jogador 6 | 2-1 | 42 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 4 | 0 | 10.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5705530643463135 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 43 | BUY | STABILIZE | 100.0 | 4 | 4 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4107455313205719 | 0.0 | 0.0 | +c8b72b14-11a4-48e6-8135-41efdbc347cb / -— |
| Jogador 6 | 2-1 | 44 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2481900155544281 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 45 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 2 | 0 | 14.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.39238330721855164 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-1 | 46 | PASS | STABILIZE | 100.0 | 4 | 2 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 50 | MOVE_BOARD | STABILIZE | 96.0 | 4 | 7 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024840479716658592 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 51 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 7 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6746034026145935 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 52 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 7 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24232007563114166 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-2 | 53 | PASS | STABILIZE | 96.0 | 4 | 7 | 0 | 14.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 60 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 13 | 1 | 14.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18404053151607513 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 61 | SELL | STABILIZE | 96.0 | 4 | 13 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0017692308174446225 | 0.0 | 0.0 | +— / -f29b0444-8dd6-44a6-9a04-824febf737a0 |
| Jogador 6 | 2-3 | 62 | BUY | STABILIZE | 96.0 | 4 | 15 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9682763814926147 | 0.0 | 0.0 | +b280845c-ba0a-4ef6-95ae-eae11f4882a1 / -— |
| Jogador 6 | 2-3 | 63 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 13 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 64 | MOVE_BENCH | STABILIZE | 96.0 | 4 | 13 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03312404081225395 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 65 | BUY_XP | STABILIZE | 96.0 | 4 | 13 | 1 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11800000071525574 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 66 | BUY_XP | STABILIZE | 96.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04550499841570854 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 67 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 5 | 0 | 16.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4177028238773346 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-3 | 68 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 5 | 0 | 20.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.13239096105098724 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 70 | BUY | STABILIZE | 96.0 | 5 | 12 | 1 | 20.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.04292844608426094 | 0.0 | 0.0 | +f44d5eea-6187-4ea9-ab49-79077393b7de / -— |
| Jogador 6 | 2-4 | 71 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 9 | 0 | 20.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.35190293192863464 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 72 | MOVE_BENCH | STABILIZE | 96.0 | 5 | 9 | 0 | 22.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.055862896144390106 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 73 | BUY_XP | STABILIZE | 96.0 | 5 | 9 | 0 | 22.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 74 | BUY_XP | STABILIZE | 96.0 | 5 | 5 | 0 | 22.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 75 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 1 | 0 | 22.0 | —/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.039354316890239716 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 76 | SELL | STABILIZE | 96.0 | 5 | 1 | 0 | 22.0 | —/DA_18_Rammus | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.033307693898677826 | 0.0 | 0.0 | +— / -c19cf6a8-c66e-4670-b0fc-fb83453f22e7 |
| Jogador 6 | 2-4 | 77 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 3 | 0 | 22.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-4 | 78 | MOVE_BOARD | STABILIZE | 96.0 | 5 | 3 | 0 | 22.0 | —/DA_18_Rammus | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.039354316890239716 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 80 | BUY | STABILIZE | 96.0 | 5 | 9 | 0 | 22.0 | —/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9686676263809204 | 0.0 | 0.0 | +15893185-b1a5-4725-9e46-964e149ec287 / -— |
| Jogador 6 | 2-5 | 81 | SELL | STABILIZE | 96.0 | 5 | 8 | 0 | 22.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -1.0186675786972046 | 0.0 | 0.0 | +— / -15893185-b1a5-4725-9e46-964e149ec287 |
| Jogador 6 | 2-5 | 82 | BUY | STABILIZE | 96.0 | 5 | 9 | 0 | 22.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.21591557562351227 | 0.0 | 0.0 | +f095cd70-c807-4086-a3f1-ddda4f6aa574 / -— |
| Jogador 6 | 2-5 | 83 | BUY_XP | STABILIZE | 96.0 | 5 | 7 | 0 | 22.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03799999877810478 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 84 | SELL | STABILIZE | 96.0 | 5 | 3 | 0 | 22.0 | Colosso/DA_18_Rammus | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26591557264328003 | 0.0 | 0.0 | +— / -f095cd70-c807-4086-a3f1-ddda4f6aa574 |
| Jogador 6 | 2-5 | 85 | BUY_XP | STABILIZE | 96.0 | 5 | 5 | 0 | 22.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.023274999111890793 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-5 | 86 | BUY | STABILIZE | 96.0 | 6 | 1 | 0 | 22.0 | Colosso/DA_18_Rammus | BUY, MOVE_BOARD, PASS | True | True | 0.3967251777648926 | 0.0 | 0.0 | +2fd4f2d8-6e40-439a-a96d-3e49e05779ad / -— |
| Jogador 6 | 2-5 | 87 | MOVE_BENCH | STABILIZE | 96.0 | 6 | 0 | 0 | 22.0 | Colosso/DA_18_Rammus | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31465429067611694 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 89 | BUY | STABILIZE | 96.0 | 6 | 7 | 0 | 24.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.8856552839279175 | 0.0 | 0.0 | +3fc2815d-c456-47c3-bb27-783336b3cdfa / -— |
| Jogador 6 | 2-6 | 90 | MOVE_BENCH | STABILIZE | 96.0 | 6 | 4 | 0 | 24.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 91 | MOVE_BENCH | STABILIZE | 96.0 | 6 | 4 | 0 | 24.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6394047141075134 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-6 | 92 | PASS | STABILIZE | 96.0 | 6 | 4 | 0 | 26.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 98 | BUY | STABILIZE | 96.0 | 6 | 11 | 1 | 26.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3786226212978363 | 0.0 | 0.0 | +bbdd0918-bfda-49bc-9ae0-8894eaf11a5c / -— |
| Jogador 6 | 2-7 | 99 | SELL | STABILIZE | 96.0 | 6 | 8 | 0 | 26.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47266367077827454 | 0.0 | 0.0 | +— / -bbdd0918-bfda-49bc-9ae0-8894eaf11a5c |
| Jogador 6 | 2-7 | 100 | MOVE_BENCH | STABILIZE | 96.0 | 6 | 11 | 1 | 26.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09814281016588211 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 101 | MOVE_BENCH | STABILIZE | 96.0 | 6 | 11 | 1 | 24.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 102 | MOVE_BENCH | STABILIZE | 96.0 | 6 | 11 | 1 | 24.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6397161483764648 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 2-7 | 103 | PASS | STABILIZE | 96.0 | 6 | 11 | 1 | 26.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 107 | BUY | STABILIZE | 96.0 | 6 | 18 | 1 | 26.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.039797477424144745 | 0.0 | 0.0 | +d71a866d-0c5a-41c2-9996-0e179f062aa2 / -— |
| Jogador 6 | 3-1 | 108 | BUY | STABILIZE | 96.0 | 6 | 14 | 1 | 26.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.201700821518898 | 0.0 | 0.0 | +bbba5910-d3e3-4cd4-9b74-e308ca124f7c / -— |
| Jogador 6 | 3-1 | 109 | MOVE_BENCH | STABILIZE | 96.0 | 6 | 11 | 1 | 26.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.47116783261299133 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 110 | MOVE_BENCH | STABILIZE | 96.0 | 6 | 11 | 1 | 28.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-1 | 111 | PASS | STABILIZE | 96.0 | 6 | 11 | 1 | 28.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 116 | BUY | STABILIZE | 96.0 | 6 | 20 | 2 | 28.0 | Colosso/DA_18_Ahri | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7572333216667175 | 0.0 | 0.0 | +ac1c8000-a262-4fb1-9cfb-9ac071e5e10f / -3fc2815d-c456-47c3-bb27-783336b3cdfa,75005e9c-56d1-48d6-815e-573e489e3dd7 |
| Jogador 6 | 3-2 | 117 | MOVE_BENCH | STABILIZE | 96.0 | 6 | 17 | 1 | 22.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6786088347434998 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 118 | MOVE_BOARD | STABILIZE | 96.0 | 6 | 17 | 1 | 28.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30669307708740234 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 119 | MOVE_BENCH | STABILIZE | 96.0 | 6 | 17 | 1 | 28.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.15497854351997375 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-2 | 120 | PASS | STABILIZE | 96.0 | 6 | 17 | 1 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 125 | BUY | STABILIZE | 96.0 | 6 | 27 | 2 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2746427357196808 | 0.0 | 0.0 | +9af097e2-729d-474a-9a7e-b266c665c606 / -— |
| Jogador 6 | 3-3 | 126 | BUY | STABILIZE | 96.0 | 6 | 24 | 2 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10883467644453049 | 0.0 | 0.0 | +6e2d02c6-9aae-4ad9-92f3-05cf4a31dbc1 / -— |
| Jogador 6 | 3-3 | 127 | REROLL | STABILIZE | 96.0 | 6 | 21 | 2 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 128 | BUY | STABILIZE | 96.0 | 6 | 19 | 1 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0467667281627655 | 0.0 | 0.0 | +ab472080-6e4b-4b75-b37d-cf10da9a5a0d / -— |
| Jogador 6 | 3-3 | 129 | BUY | STABILIZE | 96.0 | 6 | 15 | 1 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28306758403778076 | 0.0 | 0.0 | +ab050f92-777b-429f-9ed8-9b6c63794641 / -— |
| Jogador 6 | 3-3 | 130 | BUY | STABILIZE | 96.0 | 6 | 12 | 1 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19480538368225098 | 0.0 | 0.0 | +cf68219b-1d38-45a1-98db-495871c932ea / -— |
| Jogador 6 | 3-3 | 131 | REROLL | STABILIZE | 96.0 | 6 | 9 | 0 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-3 | 132 | BUY | STABILIZE | 96.0 | 6 | 7 | 0 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7368844151496887 | 0.0 | 0.0 | +844f869e-0e0e-423a-8507-27efd66131f5 / -— |
| Jogador 6 | 3-4 | 134 | BUY | STABILIZE | 96.0 | 6 | 13 | 1 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14885978400707245 | 0.0 | 0.0 | +1e81ac95-667f-494d-89eb-2bcdcf887a7e / -— |
| Jogador 6 | 3-4 | 135 | REROLL | STABILIZE | 96.0 | 6 | 10 | 1 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 136 | SELL | STABILIZE | 96.0 | 6 | 8 | 0 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10061538219451904 | 0.0 | 0.0 | +— / -1e81ac95-667f-494d-89eb-2bcdcf887a7e |
| Jogador 6 | 3-4 | 137 | BUY | STABILIZE | 96.0 | 6 | 11 | 1 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.19791428744792938 | 0.0 | 0.0 | +bf0751f0-8094-4441-adb3-e5f8b4158426 / -— |
| Jogador 6 | 3-4 | 138 | SELL | STABILIZE | 96.0 | 6 | 7 | 0 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10553846508264542 | 0.0 | 0.0 | +— / -6e2d02c6-9aae-4ad9-92f3-05cf4a31dbc1 |
| Jogador 6 | 3-4 | 139 | BUY | STABILIZE | 96.0 | 6 | 10 | 1 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6623034477233887 | 0.0 | 0.0 | +f384fea6-9b6f-4f9c-81ec-a8284d5ba140 / -— |
| Jogador 6 | 3-4 | 140 | REROLL | STABILIZE | 96.0 | 6 | 7 | 0 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-4 | 141 | SELL | STABILIZE | 96.0 | 6 | 5 | 0 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6580225229263306 | 0.0 | 0.0 | +— / -c8b72b14-11a4-48e6-8135-41efdbc347cb |
| Jogador 6 | 3-5 | 143 | BUY | STABILIZE | 96.0 | 6 | 15 | 1 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7421484589576721 | 0.0 | 0.0 | +ec9662c5-0734-41a3-9999-224d7716228b / -— |
| Jogador 6 | 3-5 | 144 | SELL | STABILIZE | 96.0 | 6 | 12 | 1 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.031876090914011 | 0.0 | 0.0 | +— / -d71a866d-0c5a-41c2-9996-0e179f062aa2 |
| Jogador 6 | 3-5 | 145 | BUY | STABILIZE | 96.0 | 6 | 16 | 1 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05267466604709625 | 0.0 | 0.0 | +6fb9f857-4ee1-4b52-8825-57f514dc2d0f / -— |
| Jogador 6 | 3-5 | 146 | REROLL | STABILIZE | 96.0 | 6 | 13 | 1 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 147 | SELL | STABILIZE | 96.0 | 6 | 11 | 1 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024678613990545273 | 0.0 | 0.0 | +— / -6fb9f857-4ee1-4b52-8825-57f514dc2d0f |
| Jogador 6 | 3-5 | 148 | BUY | STABILIZE | 96.0 | 6 | 14 | 1 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2791365683078766 | 0.0 | 0.0 | +0d120db3-34e2-47e3-a57c-0d65dcc56342 / -— |
| Jogador 6 | 3-5 | 149 | REROLL | STABILIZE | 96.0 | 6 | 10 | 1 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-5 | 150 | SELL | STABILIZE | 96.0 | 6 | 8 | 0 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.038923077285289764 | 0.0 | 0.0 | +— / -0d120db3-34e2-47e3-a57c-0d65dcc56342 |
| Jogador 6 | 3-6 | 152 | BUY | STABILIZE | 96.0 | 6 | 22 | 2 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5995109677314758 | 0.0 | 0.0 | +be1e11e4-dc58-4e75-a402-3a2d831ac7b3 / -— |
| Jogador 6 | 3-6 | 153 | REROLL | STABILIZE | 96.0 | 6 | 21 | 2 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 154 | SELL | STABILIZE | 96.0 | 6 | 19 | 1 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.1153520941734314 | 0.0 | 0.0 | +— / -ab472080-6e4b-4b75-b37d-cf10da9a5a0d |
| Jogador 6 | 3-6 | 155 | BUY | STABILIZE | 96.0 | 6 | 23 | 2 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8488932847976685 | 0.0 | 0.0 | +78adfe0a-b6d8-4cc4-a482-26451f95e788 / -ab050f92-777b-429f-9ed8-9b6c63794641,ec9662c5-0734-41a3-9999-224d7716228b |
| Jogador 6 | 3-6 | 156 | BUY | STABILIZE | 96.0 | 6 | 20 | 2 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.27282989025115967 | 0.0 | 0.0 | +5098782d-1ec1-4a5b-a435-f3c84ab1be0d / -— |
| Jogador 6 | 3-6 | 157 | REROLL | STABILIZE | 96.0 | 6 | 17 | 1 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-6 | 158 | BUY | STABILIZE | 96.0 | 6 | 15 | 1 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8267670273780823 | 0.0 | 0.0 | +24d03668-5dc4-4b40-9439-a1d67522d0a3 / -844f869e-0e0e-423a-8507-27efd66131f5,9af097e2-729d-474a-9a7e-b266c665c606 |
| Jogador 6 | 3-6 | 159 | BUY | STABILIZE | 96.0 | 6 | 12 | 1 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7449854612350464 | 0.0 | 0.0 | +e903e009-8dae-4fc9-b0ec-bc028c3f9f3e / -— |
| Jogador 6 | 3-6 | 160 | BUY | STABILIZE | 96.0 | 6 | 10 | 1 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.11387911438941956 | 0.0 | 0.0 | +7fd34ef6-a124-4d23-a166-9f7ad919c826 / -— |
| Jogador 6 | 3-7 | 162 | SELL | STABILIZE | 96.0 | 6 | 16 | 1 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04399999976158142 | 0.0 | 0.0 | +— / -5098782d-1ec1-4a5b-a435-f3c84ab1be0d |
| Jogador 6 | 3-7 | 163 | BUY | STABILIZE | 96.0 | 6 | 19 | 1 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07845716178417206 | 0.0 | 0.0 | +509928e4-3f42-4b0d-a71c-1a45fa23a781 / -— |
| Jogador 6 | 3-7 | 164 | SELL | STABILIZE | 96.0 | 6 | 15 | 1 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02230769209563732 | 0.0 | 0.0 | +— / -509928e4-3f42-4b0d-a71c-1a45fa23a781 |
| Jogador 6 | 3-7 | 165 | BUY | STABILIZE | 96.0 | 6 | 19 | 1 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5636003017425537 | 0.0 | 0.0 | +e22ad17a-827b-42f7-95a6-9e334471b0b9 / -— |
| Jogador 6 | 3-7 | 166 | REROLL | STABILIZE | 96.0 | 6 | 16 | 1 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 167 | SELL | STABILIZE | 96.0 | 6 | 14 | 1 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2892307639122009 | 0.0 | 0.0 | +— / -e22ad17a-827b-42f7-95a6-9e334471b0b9 |
| Jogador 6 | 3-7 | 168 | BUY | STABILIZE | 96.0 | 6 | 17 | 1 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5634346008300781 | 0.0 | 0.0 | +14a36be6-92b0-4c1a-8c3c-d3fdeb425992 / -— |
| Jogador 6 | 3-7 | 169 | REROLL | STABILIZE | 96.0 | 6 | 14 | 1 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 3-7 | 170 | SELL | STABILIZE | 96.0 | 6 | 12 | 1 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2892307639122009 | 0.0 | 0.0 | +— / -14a36be6-92b0-4c1a-8c3c-d3fdeb425992 |
| Jogador 6 | 4-1 | 172 | BUY | STABILIZE | 96.0 | 6 | 24 | 2 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07845980674028397 | 0.0 | 0.0 | +09e28e26-f7f0-4d8a-acca-f768d9205f14 / -— |
| Jogador 6 | 4-1 | 173 | SELL | STABILIZE | 96.0 | 6 | 20 | 2 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.032769229263067245 | 0.0 | 0.0 | +— / -09e28e26-f7f0-4d8a-acca-f768d9205f14 |
| Jogador 6 | 4-1 | 174 | BUY | STABILIZE | 96.0 | 6 | 24 | 2 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17618265748023987 | 0.0 | 0.0 | +38b4cb27-ddc9-4488-9d22-eca4612a4bd8 / -— |
| Jogador 6 | 4-1 | 175 | REROLL | STABILIZE | 96.0 | 6 | 20 | 2 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.164000004529953 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-1 | 176 | SELL | STABILIZE | 96.0 | 6 | 18 | 1 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.29630768299102783 | 0.0 | 0.0 | +— / -be1e11e4-dc58-4e75-a402-3a2d831ac7b3 |
| Jogador 6 | 4-1 | 177 | BUY | STABILIZE | 96.0 | 6 | 19 | 1 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7351808547973633 | 0.0 | 0.0 | +233643ca-941f-4ffe-8d9a-f1ff0f64d1d2 / -— |
| Jogador 6 | 4-1 | 178 | SELL | STABILIZE | 96.0 | 6 | 16 | 1 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04352478310465813 | 0.0 | 0.0 | +— / -78adfe0a-b6d8-4cc4-a482-26451f95e788 |
| Jogador 6 | 4-1 | 179 | BUY | STABILIZE | 96.0 | 6 | 24 | 2 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7692838907241821 | 0.0 | 0.0 | +f5419ca3-b123-4d9e-8aa9-58b288a186c2 / -— |
| Jogador 6 | 4-1 | 180 | REROLL | STABILIZE | 96.0 | 6 | 23 | 2 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 182 | SELL | SLOWROLL | 96.0 | 6 | 32 | 3 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6846153736114502 | 0.0 | 0.0 | +— / -f5419ca3-b123-4d9e-8aa9-58b288a186c2 |
| Jogador 6 | 4-2 | 183 | BUY | SLOWROLL | 96.0 | 6 | 33 | 3 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.18847772479057312 | 0.0 | 0.0 | +4220ac7e-adb0-4526-9413-9d8704585228 / -— |
| Jogador 6 | 4-2 | 184 | SELL | SLOWROLL | 96.0 | 6 | 30 | 3 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04769230633974075 | 0.0 | 0.0 | +— / -4220ac7e-adb0-4526-9413-9d8704585228 |
| Jogador 6 | 4-2 | 185 | BUY | SLOWROLL | 96.0 | 6 | 33 | 3 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.048181530088186264 | 0.0 | 0.0 | +e14dbc54-2ddf-4a4a-afce-49045a4c34ac / -— |
| Jogador 6 | 4-2 | 186 | REROLL | SLOWROLL | 96.0 | 6 | 30 | 3 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.205704465508461 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 187 | SELL | STABILIZE | 96.0 | 6 | 28 | 2 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12153846025466919 | 0.0 | 0.0 | +— / -e14dbc54-2ddf-4a4a-afce-49045a4c34ac |
| Jogador 6 | 4-2 | 188 | BUY | SLOWROLL | 96.0 | 6 | 31 | 3 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05822707340121269 | 0.0 | 0.0 | +c98cd1bc-3288-4d7e-a9f7-f31408df3d85 / -— |
| Jogador 6 | 4-2 | 189 | REROLL | STABILIZE | 96.0 | 6 | 28 | 2 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-2 | 190 | SELL | STABILIZE | 96.0 | 6 | 26 | 2 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010153845883905888 | 0.0 | 0.0 | +— / -c98cd1bc-3288-4d7e-a9f7-f31408df3d85 |
| Jogador 6 | 4-3 | 192 | BUY | SLOWROLL | 96.0 | 6 | 41 | 4 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.24484457075595856 | 0.0 | 0.0 | +31b8f77b-a5e2-4a86-b937-6cfe7b282e6d / -— |
| Jogador 6 | 4-3 | 193 | REROLL | SLOWROLL | 96.0 | 6 | 38 | 3 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07087915390729904 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 194 | SELL | SLOWROLL | 96.0 | 6 | 36 | 3 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04399999976158142 | 0.0 | 0.0 | +— / -31b8f77b-a5e2-4a86-b937-6cfe7b282e6d |
| Jogador 6 | 4-3 | 195 | BUY | SLOWROLL | 96.0 | 6 | 39 | 3 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10276492685079575 | 0.0 | 0.0 | +8502f13e-1ff7-4595-b9c5-27f22bd20357 / -— |
| Jogador 6 | 4-3 | 196 | SELL | SLOWROLL | 96.0 | 6 | 36 | 3 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.024666255339980125 | 0.0 | 0.0 | +— / -8502f13e-1ff7-4595-b9c5-27f22bd20357 |
| Jogador 6 | 4-3 | 197 | BUY | SLOWROLL | 96.0 | 6 | 39 | 3 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.717830240726471 | 0.0 | 0.0 | +d692f8c0-9734-4c1d-b9dd-051e85b63945 / -— |
| Jogador 6 | 4-3 | 198 | REROLL | SLOWROLL | 96.0 | 6 | 38 | 3 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.060921959578990936 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-3 | 199 | SELL | SLOWROLL | 96.0 | 6 | 36 | 3 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6846153736114502 | 0.0 | 0.0 | +— / -d692f8c0-9734-4c1d-b9dd-051e85b63945 |
| Jogador 6 | 4-3 | 200 | BUY | SLOWROLL | 96.0 | 6 | 37 | 3 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09538597613573074 | 0.0 | 0.0 | +25be98ec-41f1-46a6-af0a-f6a0dd131384 / -— |
| Jogador 6 | 4-4 | 202 | SELL | SLOWROLL | 96.0 | 6 | 46 | 4 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.010153845883905888 | 0.0 | 0.0 | +— / -25be98ec-41f1-46a6-af0a-f6a0dd131384 |
| Jogador 6 | 4-4 | 203 | BUY | SLOWROLL | 96.0 | 6 | 49 | 4 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7327566742897034 | 0.0 | 0.0 | +736abf5b-a118-4174-964a-c264be63a40f / -— |
| Jogador 6 | 4-4 | 204 | REROLL | SLOWROLL | 96.0 | 6 | 45 | 4 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0989060029387474 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 205 | SELL | SLOWROLL | 96.0 | 6 | 43 | 4 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06262220442295074 | 0.0 | 0.0 | +— / -24d03668-5dc4-4b40-9439-a1d67522d0a3 |
| Jogador 6 | 4-4 | 206 | BUY | SLOWROLL | 96.0 | 6 | 51 | 5 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11694930493831635 | 0.0 | 0.0 | +9d82f378-3205-48fd-8a2a-c2c408a744b5 / -— |
| Jogador 6 | 4-4 | 207 | SELL | SLOWROLL | 96.0 | 6 | 49 | 4 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21353939175605774 | 0.0 | 0.0 | +— / -9d82f378-3205-48fd-8a2a-c2c408a744b5 |
| Jogador 6 | 4-4 | 208 | BUY | SLOWROLL | 96.0 | 6 | 51 | 5 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.30617982149124146 | 0.0 | 0.0 | +fff4164b-1d28-4671-80ba-96108332f833 / -— |
| Jogador 6 | 4-4 | 209 | REROLL | SLOWROLL | 96.0 | 6 | 50 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.12104667723178864 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-4 | 210 | SELL | SLOWROLL | 96.0 | 6 | 48 | 4 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37324976921081543 | 0.0 | 0.0 | +— / -fff4164b-1d28-4671-80ba-96108332f833 |
| Jogador 6 | 4-5 | 212 | BUY | SLOWROLL | 96.0 | 6 | 61 | 5 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29055821895599365 | 0.0 | 0.0 | +88f632bd-bfc1-4a30-8ce2-c27e8a707835 / -— |
| Jogador 6 | 4-5 | 213 | SELL | SLOWROLL | 96.0 | 6 | 58 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6620730757713318 | 0.0 | 0.0 | +— / -e903e009-8dae-4fc9-b0ec-bc028c3f9f3e |
| Jogador 6 | 4-5 | 214 | BUY | SLOWROLL | 96.0 | 6 | 60 | 5 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09315802901983261 | 0.0 | 0.0 | +26bea05f-2971-438c-977c-261078de92f7 / -— |
| Jogador 6 | 4-5 | 215 | REROLL | SLOWROLL | 96.0 | 6 | 57 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08430477976799011 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 216 | REROLL | SLOWROLL | 96.0 | 6 | 55 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13360121846199036 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 217 | SELL | SLOWROLL | 96.0 | 6 | 53 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029999999329447746 | 0.0 | 0.0 | +— / -26bea05f-2971-438c-977c-261078de92f7 |
| Jogador 6 | 4-5 | 218 | BUY | SLOWROLL | 96.0 | 6 | 56 | 5 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.14949922263622284 | 0.0 | 0.0 | +8dfa090e-ec6b-408c-93f7-6aa740d37923 / -— |
| Jogador 6 | 4-5 | 219 | REROLL | SLOWROLL | 96.0 | 6 | 53 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2499370574951172 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-5 | 220 | SELL | SLOWROLL | 96.0 | 6 | 51 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03799999877810478 | 0.0 | 0.0 | +— / -8dfa090e-ec6b-408c-93f7-6aa740d37923 |
| Jogador 6 | 4-6 | 222 | BUY | SLOWROLL | 96.0 | 6 | 68 | 5 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09333888441324234 | 0.0 | 0.0 | +f515e44c-513b-4877-bdfb-e6c0ef498492 / -— |
| Jogador 6 | 4-6 | 223 | REROLL | SLOWROLL | 96.0 | 6 | 65 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.12545524537563324 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 224 | SELL | SLOWROLL | 96.0 | 6 | 63 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029999999329447746 | 0.0 | 0.0 | +— / -f515e44c-513b-4877-bdfb-e6c0ef498492 |
| Jogador 6 | 4-6 | 225 | BUY | SLOWROLL | 96.0 | 6 | 66 | 5 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7510604858398438 | 0.0 | 0.0 | +aaa16c13-8911-4d92-a579-9d728db3de03 / -— |
| Jogador 6 | 4-6 | 226 | REROLL | SLOWROLL | 96.0 | 6 | 64 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24044178426265717 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 227 | SELL | SLOWROLL | 96.0 | 6 | 62 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.662009060382843 | 0.0 | 0.0 | +— / -aaa16c13-8911-4d92-a579-9d728db3de03 |
| Jogador 6 | 4-6 | 228 | BUY | SLOWROLL | 96.0 | 6 | 64 | 5 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6294746994972229 | 0.0 | 0.0 | +fdc60b5c-31f1-4356-a662-c966d04f9c9d / -— |
| Jogador 6 | 4-6 | 229 | REROLL | SLOWROLL | 96.0 | 6 | 61 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2295316755771637 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-6 | 230 | SELL | SLOWROLL | 96.0 | 6 | 59 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6521538496017456 | 0.0 | 0.0 | +— / -f384fea6-9b6f-4f9c-81ec-a8284d5ba140 |
| Jogador 6 | 4-7 | 232 | BUY | SLOWROLL | 96.0 | 6 | 76 | 5 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2526179552078247 | 0.0 | 0.0 | +d8052e34-b223-47b7-8ef1-c0127e6289ac / -— |
| Jogador 6 | 4-7 | 233 | SELL | SLOWROLL | 96.0 | 6 | 73 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.33861538767814636 | 0.0 | 0.0 | +— / -cf68219b-1d38-45a1-98db-495871c932ea |
| Jogador 6 | 4-7 | 234 | BUY | SLOWROLL | 96.0 | 6 | 76 | 5 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7503436207771301 | 0.0 | 0.0 | +6c0c8c09-397b-40be-9394-1981e1f50d92 / -— |
| Jogador 6 | 4-7 | 235 | SELL | SLOWROLL | 96.0 | 6 | 73 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6267153024673462 | 0.0 | 0.0 | +— / -233643ca-941f-4ffe-8d9a-f1ff0f64d1d2 |
| Jogador 6 | 4-7 | 236 | BUY | SLOWROLL | 96.0 | 6 | 76 | 5 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19035404920578003 | 0.0 | 0.0 | +2c594775-7f0b-4db9-bf3b-08e5a050376c / -— |
| Jogador 6 | 4-7 | 237 | REROLL | SLOWROLL | 96.0 | 6 | 73 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06263254582881927 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 4-7 | 238 | SELL | SLOWROLL | 96.0 | 6 | 71 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04169230908155441 | 0.0 | 0.0 | +— / -2c594775-7f0b-4db9-bf3b-08e5a050376c |
| Jogador 6 | 4-7 | 239 | BUY | SLOWROLL | 96.0 | 6 | 74 | 5 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23189817368984222 | 0.0 | 0.0 | +5bed8e42-ebb4-43d3-83bf-7cba91b8874b / -— |
| Jogador 6 | 4-7 | 240 | REROLL | SLOWROLL | 96.0 | 6 | 70 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2493857890367508 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 242 | EQUIP_FROM_INVENTORY | FAST8 | 96.0 | 7 | 81 | 5 | 32.0 | Colosso/DA_18_Rammus | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 243 | SELL | FAST8 | 96.0 | 7 | 81 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04938461631536484 | 0.0 | 0.0 | +— / -5bed8e42-ebb4-43d3-83bf-7cba91b8874b |
| Jogador 6 | 5-1 | 244 | BUY | FAST8 | 96.0 | 7 | 85 | 5 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.409137099981308 | 0.0 | 0.0 | +8e743364-ec05-46cd-b8f1-634d0f8ce8cc / -— |
| Jogador 6 | 5-1 | 245 | SELL | FAST8 | 96.0 | 7 | 82 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.28600001335144043 | 0.0 | 0.0 | +— / -8e743364-ec05-46cd-b8f1-634d0f8ce8cc |
| Jogador 6 | 5-1 | 246 | BUY | FAST8 | 96.0 | 7 | 85 | 5 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.18103714287281036 | 0.0 | 0.0 | +787814cb-4e88-427b-b468-f6d4f6115772 / -— |
| Jogador 6 | 5-1 | 247 | SELL | FAST8 | 96.0 | 7 | 82 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03799999877810478 | 0.0 | 0.0 | +— / -787814cb-4e88-427b-b468-f6d4f6115772 |
| Jogador 6 | 5-1 | 248 | BUY | FAST8 | 96.0 | 7 | 85 | 5 | 32.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.19867493212223053 | 0.0 | 0.0 | +38944289-07c3-4081-944c-89c1c3f2fe09 / -— |
| Jogador 6 | 5-1 | 249 | REROLL | FAST8 | 96.0 | 7 | 83 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0373578779399395 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-1 | 250 | MOVE_BENCH | FAST8 | 96.0 | 7 | 81 | 5 | 32.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5199284553527832 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 252 | BUY | FAST8 | 96.0 | 7 | 95 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03721075877547264 | 0.0 | 0.0 | +e0c240ff-691e-4ce1-a236-02c67d63bb3c / -— |
| Jogador 6 | 5-2 | 253 | SELL | FAST8 | 96.0 | 7 | 91 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.023418230935931206 | 0.0 | 0.0 | +— / -e0c240ff-691e-4ce1-a236-02c67d63bb3c |
| Jogador 6 | 5-2 | 254 | BUY | FAST8 | 96.0 | 7 | 95 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.17825263738632202 | 0.0 | 0.0 | +5d774bab-dde7-4e5d-bf14-a9b96ffcb2ed / -— |
| Jogador 6 | 5-2 | 255 | SELL | FAST8 | 96.0 | 7 | 91 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04015384614467621 | 0.0 | 0.0 | +— / -5d774bab-dde7-4e5d-bf14-a9b96ffcb2ed |
| Jogador 6 | 5-2 | 256 | BUY | FAST8 | 96.0 | 7 | 95 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.18768824636936188 | 0.0 | 0.0 | +0e623277-0fad-43d3-8b8e-8e13008ed102 / -— |
| Jogador 6 | 5-2 | 257 | SELL | FAST8 | 96.0 | 7 | 92 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04169230908155441 | 0.0 | 0.0 | +— / -0e623277-0fad-43d3-8b8e-8e13008ed102 |
| Jogador 6 | 5-2 | 258 | BUY | FAST8 | 96.0 | 7 | 95 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2838939130306244 | 0.0 | 0.0 | +0adce8d6-fb0a-4ddf-bf53-fcca5e832977 / -— |
| Jogador 6 | 5-2 | 259 | REROLL | FAST8 | 96.0 | 7 | 92 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.025098595768213272 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-2 | 260 | REROLL | FAST8 | 96.0 | 7 | 90 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.04016583785414696 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 262 | SELL | FAST8 | 96.0 | 7 | 102 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3280276954174042 | 0.0 | 0.0 | +— / -38944289-07c3-4081-944c-89c1c3f2fe09 |
| Jogador 6 | 5-3 | 263 | BUY | FAST8 | 96.0 | 7 | 104 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.15408483147621155 | 0.0 | 0.0 | +e7a0570f-d3a7-474c-b14b-2f75013d36ba / -— |
| Jogador 6 | 5-3 | 264 | SELL | FAST8 | 96.0 | 7 | 101 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0007621151162311435 | 0.0 | 0.0 | +— / -e7a0570f-d3a7-474c-b14b-2f75013d36ba |
| Jogador 6 | 5-3 | 265 | BUY | FAST8 | 96.0 | 7 | 104 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.15423734486103058 | 0.0 | 0.0 | +b26fc433-a92f-4fc4-9ae6-68a252182dd5 / -— |
| Jogador 6 | 5-3 | 266 | REROLL | FAST8 | 96.0 | 7 | 101 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.021158229559659958 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-3 | 267 | SELL | FAST8 | 96.0 | 7 | 99 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.001935267704539001 | 0.0 | 0.0 | +— / -b26fc433-a92f-4fc4-9ae6-68a252182dd5 |
| Jogador 6 | 5-3 | 268 | BUY | FAST8 | 96.0 | 7 | 102 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07270269840955734 | 0.0 | 0.0 | +9668ab9e-ebde-4592-bf0a-f4ba4191f578 / -— |
| Jogador 6 | 5-3 | 269 | SELL | FAST8 | 96.0 | 7 | 98 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.02476923167705536 | 0.0 | 0.0 | +— / -9668ab9e-ebde-4592-bf0a-f4ba4191f578 |
| Jogador 6 | 5-3 | 270 | BUY | FAST8 | 96.0 | 7 | 102 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.42697879672050476 | 0.0 | 0.0 | +af417326-9143-4f88-900b-a27b261e71df / -— |
| Jogador 6 | 5-4 | 272 | SELL | FAST8 | 96.0 | 7 | 113 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.28600001335144043 | 0.0 | 0.0 | +— / -af417326-9143-4f88-900b-a27b261e71df |
| Jogador 6 | 5-4 | 273 | BUY | FAST8 | 96.0 | 7 | 116 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7366815805435181 | 0.0 | 0.0 | +5a69e9ce-79ff-4c56-a49b-dfb458ecc74c / -— |
| Jogador 6 | 5-4 | 274 | SELL | FAST8 | 96.0 | 7 | 113 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.33861538767814636 | 0.0 | 0.0 | +— / -0adce8d6-fb0a-4ddf-bf53-fcca5e832977 |
| Jogador 6 | 5-4 | 275 | BUY | FAST8 | 96.0 | 7 | 116 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.18827885389328003 | 0.0 | 0.0 | +b24c598a-61b3-40a2-bf7c-7aeb00417958 / -— |
| Jogador 6 | 5-4 | 276 | SELL | FAST8 | 96.0 | 7 | 113 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04169230908155441 | 0.0 | 0.0 | +— / -b24c598a-61b3-40a2-bf7c-7aeb00417958 |
| Jogador 6 | 5-4 | 277 | BUY | FAST8 | 96.0 | 7 | 116 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.04870555177330971 | 0.0 | 0.0 | +27cd546c-d67b-45cd-a449-31eb5847e2b0 / -— |
| Jogador 6 | 5-4 | 278 | REROLL | FAST8 | 96.0 | 7 | 113 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.005165839102119207 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-4 | 279 | SELL | FAST8 | 96.0 | 7 | 111 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.035538461059331894 | 0.0 | 0.0 | +— / -27cd546c-d67b-45cd-a449-31eb5847e2b0 |
| Jogador 6 | 5-4 | 280 | BUY | FAST8 | 96.0 | 7 | 114 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4274618923664093 | 0.0 | 0.0 | +f39f2a91-b130-4dea-8ebd-e6516f57cdcf / -— |
| Jogador 6 | 5-5 | 282 | SELL | FAST8 | 96.0 | 7 | 124 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.28600001335144043 | 0.0 | 0.0 | +— / -f39f2a91-b130-4dea-8ebd-e6516f57cdcf |
| Jogador 6 | 5-5 | 283 | BUY | FAST8 | 96.0 | 7 | 127 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4274612069129944 | 0.0 | 0.0 | +854b8fe1-3716-4c52-b26f-48d3221bf376 / -— |
| Jogador 6 | 5-5 | 284 | SELL | FAST8 | 96.0 | 7 | 124 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.28600001335144043 | 0.0 | 0.0 | +— / -854b8fe1-3716-4c52-b26f-48d3221bf376 |
| Jogador 6 | 5-5 | 285 | BUY | FAST8 | 96.0 | 7 | 127 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.18789318203926086 | 0.0 | 0.0 | +890ef27d-4865-4c22-898c-20ae0e891421 / -— |
| Jogador 6 | 5-5 | 286 | SELL | FAST8 | 96.0 | 7 | 124 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04169230908155441 | 0.0 | 0.0 | +— / -890ef27d-4865-4c22-898c-20ae0e891421 |
| Jogador 6 | 5-5 | 287 | BUY | FAST8 | 96.0 | 7 | 127 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.008656812831759453 | 0.0 | 0.0 | +bb5fb98d-bd1f-4e58-943d-c61197e9a743 / -— |
| Jogador 6 | 5-5 | 288 | REROLL | FAST8 | 96.0 | 7 | 124 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0002189523947890848 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-5 | 289 | SELL | FAST8 | 96.0 | 7 | 122 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.029833802953362465 | 0.0 | 0.0 | +— / -bb5fb98d-bd1f-4e58-943d-c61197e9a743 |
| Jogador 6 | 5-5 | 290 | BUY | FAST8 | 96.0 | 7 | 125 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.017999082803726196 | 0.0 | 0.0 | +a617f370-2ac4-4ca3-a91b-e2dfe927a5af / -— |
| Jogador 6 | 5-6 | 292 | SELL | FAST8 | 96.0 | 7 | 135 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.027246080338954926 | 0.0 | 0.0 | +— / -a617f370-2ac4-4ca3-a91b-e2dfe927a5af |
| Jogador 6 | 5-6 | 293 | BUY | FAST8 | 96.0 | 7 | 139 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.037070468068122864 | 0.0 | 0.0 | +97127383-6315-49ad-b176-749bde8f8d2f / -— |
| Jogador 6 | 5-6 | 294 | SELL | FAST8 | 96.0 | 7 | 135 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.023383336141705513 | 0.0 | 0.0 | +— / -97127383-6315-49ad-b176-749bde8f8d2f |
| Jogador 6 | 5-6 | 295 | BUY | FAST8 | 96.0 | 7 | 139 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.048702750355005264 | 0.0 | 0.0 | +d8a049d6-486e-49c9-8a00-9db55b29995d / -— |
| Jogador 6 | 5-6 | 296 | REROLL | FAST8 | 96.0 | 7 | 136 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03898107260465622 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-6 | 297 | SELL | FAST8 | 96.0 | 7 | 134 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.035538461059331894 | 0.0 | 0.0 | +— / -d8a049d6-486e-49c9-8a00-9db55b29995d |
| Jogador 6 | 5-6 | 298 | BUY | FAST8 | 96.0 | 7 | 137 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3050392270088196 | 0.0 | 0.0 | +eda9a9c1-f741-46fd-8df5-929cf2b25baa / -— |
| Jogador 6 | 5-6 | 299 | SELL | FAST8 | 96.0 | 7 | 135 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3264743387699127 | 0.0 | 0.0 | +— / -eda9a9c1-f741-46fd-8df5-929cf2b25baa |
| Jogador 6 | 5-6 | 300 | BUY | FAST8 | 96.0 | 7 | 137 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8106495141983032 | 0.0 | 0.0 | +00446e9e-8f48-4571-ac9b-181ab1079cba / -— |
| Jogador 6 | 5-7 | 302 | SELL | FAST8 | 96.0 | 7 | 150 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.6874778866767883 | 0.0 | 0.0 | +— / -00446e9e-8f48-4571-ac9b-181ab1079cba |
| Jogador 6 | 5-7 | 303 | BUY | FAST8 | 96.0 | 7 | 151 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.1878114491701126 | 0.0 | 0.0 | +8e3c46cc-be5b-4b25-b954-8ab03b7b4290 / -— |
| Jogador 6 | 5-7 | 304 | SELL | FAST8 | 96.0 | 7 | 148 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04169230908155441 | 0.0 | 0.0 | +— / -8e3c46cc-be5b-4b25-b954-8ab03b7b4290 |
| Jogador 6 | 5-7 | 305 | BUY | FAST8 | 96.0 | 7 | 151 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3050396144390106 | 0.0 | 0.0 | +5af9eff4-ceca-4ef6-8aa0-2f247331fe37 / -— |
| Jogador 6 | 5-7 | 306 | SELL | FAST8 | 96.0 | 7 | 149 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3264842629432678 | 0.0 | 0.0 | +— / -5af9eff4-ceca-4ef6-8aa0-2f247331fe37 |
| Jogador 6 | 5-7 | 307 | BUY | FAST8 | 96.0 | 7 | 151 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.16462519764900208 | 0.0 | 0.0 | +c1c2c608-3f0f-4730-a6e4-365c888f2532 / -— |
| Jogador 6 | 5-7 | 308 | REROLL | FAST8 | 96.0 | 7 | 148 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03575785085558891 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 5-7 | 309 | SELL | FAST8 | 96.0 | 7 | 146 | 5 | 40.0 | Colosso/DA_18_Rammus | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03799999877810478 | 0.0 | 0.0 | +— / -c1c2c608-3f0f-4730-a6e4-365c888f2532 |
| Jogador 6 | 5-7 | 310 | BUY | FAST8 | 96.0 | 7 | 149 | 5 | 40.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9497994780540466 | 0.0 | 0.0 | +4967f37a-57c3-45b3-a638-975597231371 / -736abf5b-a118-4174-964a-c264be63a40f,bf0751f0-8094-4441-adb3-e5f8b4158426 |
| Jogador 6 | 6-1 | 312 | EQUIP_FROM_INVENTORY | FAST8 | 96.0 | 7 | 158 | 5 | 40.0 | Colosso/DA_Sentinel18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 313 | EQUIP_FROM_INVENTORY | FAST8 | 96.0 | 7 | 158 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY, CRAFT_AND_EQUIP | True | — | -0.029999999329447746 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 314 | BUY | FAST8 | 96.0 | 7 | 158 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03738304227590561 | 0.0 | 0.0 | +c91aedba-ac47-48c1-8ef1-925051b4cfe1 / -— |
| Jogador 6 | 6-1 | 315 | BUY | FAST8 | 96.0 | 7 | 154 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10994011908769608 | 0.0 | 0.0 | +4d9b2798-5fdb-43e7-8b5d-c0088454ff08 / -— |
| Jogador 6 | 6-1 | 316 | SELL | FAST8 | 96.0 | 7 | 151 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.019538462162017822 | 0.0 | 0.0 | +— / -4d9b2798-5fdb-43e7-8b5d-c0088454ff08 |
| Jogador 6 | 6-1 | 317 | BUY | FAST8 | 96.0 | 7 | 154 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.16513490676879883 | 0.0 | 0.0 | +6ec72923-e3cb-4b92-a04e-e127568ad17a / -— |
| Jogador 6 | 6-1 | 318 | REROLL | FAST8 | 96.0 | 7 | 151 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.022040123119950294 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-1 | 319 | SELL | FAST8 | 96.0 | 7 | 149 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03799999877810478 | 0.0 | 0.0 | +— / -6ec72923-e3cb-4b92-a04e-e127568ad17a |
| Jogador 6 | 6-1 | 320 | BUY | FAST8 | 96.0 | 7 | 152 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.22913560271263123 | 0.0 | 0.0 | +8c407eca-a320-4908-8570-b21237f0131d / -— |
| Jogador 6 | 6-2 | 322 | SELL | FAST8 | 96.0 | 7 | 161 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04938461631536484 | 0.0 | 0.0 | +— / -8c407eca-a320-4908-8570-b21237f0131d |
| Jogador 6 | 6-2 | 323 | BUY | FAST8 | 96.0 | 7 | 165 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.19694457948207855 | 0.0 | 0.0 | +58aeb76d-9024-4efb-8835-422eb057f1e6 / -— |
| Jogador 6 | 6-2 | 324 | REROLL | FAST8 | 96.0 | 7 | 163 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03854765743017197 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 325 | SELL | FAST8 | 96.0 | 7 | 161 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04323076829314232 | 0.0 | 0.0 | +— / -58aeb76d-9024-4efb-8835-422eb057f1e6 |
| Jogador 6 | 6-2 | 326 | BUY | FAST8 | 96.0 | 7 | 163 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7532325983047485 | 0.0 | 0.0 | +86cfaabc-2926-49fd-a1fd-d76aa9ff2dc8 / -— |
| Jogador 6 | 6-2 | 327 | SELL | FAST8 | 96.0 | 7 | 159 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.02337079495191574 | 0.0 | 0.0 | +— / -c91aedba-ac47-48c1-8ef1-925051b4cfe1 |
| Jogador 6 | 6-2 | 328 | BUY | FAST8 | 96.0 | 7 | 163 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.09109039604663849 | 0.0 | 0.0 | +85fb4d27-57b1-4dca-a83d-03e3d2e3d470 / -— |
| Jogador 6 | 6-2 | 329 | REROLL | FAST8 | 96.0 | 7 | 160 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03898013010621071 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-2 | 330 | SELL | FAST8 | 96.0 | 7 | 158 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.014615384861826897 | 0.0 | 0.0 | +— / -85fb4d27-57b1-4dca-a83d-03e3d2e3d470 |
| Jogador 6 | 6-3 | 332 | BUY | FAST8 | 79.0 | 7 | 171 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0097216367721558 | 0.0 | 0.0 | +50c44a76-ab39-44b8-af51-7dda2dc7b8b4 / -6c0c8c09-397b-40be-9394-1981e1f50d92,88f632bd-bfc1-4a30-8ce2-c27e8a707835 |
| Jogador 6 | 6-3 | 333 | BUY | FAST8 | 79.0 | 7 | 168 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.15982264280319214 | 0.0 | 0.0 | +d0312d75-2176-4d6c-a822-da3c2fa6de8c / -— |
| Jogador 6 | 6-3 | 334 | BUY | FAST8 | 79.0 | 7 | 165 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.06563002616167068 | 0.0 | 0.0 | +d4ed529b-8665-4702-88d1-7160966d3ee0 / -— |
| Jogador 6 | 6-3 | 335 | REROLL | FAST8 | 79.0 | 7 | 162 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.04609214514493942 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-3 | 336 | SELL | FAST8 | 79.0 | 7 | 160 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.01837722398340702 | 0.0 | 0.0 | +— / -d4ed529b-8665-4702-88d1-7160966d3ee0 |
| Jogador 6 | 6-3 | 337 | BUY | FAST8 | 79.0 | 7 | 163 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.029533836990594864 | 0.0 | 0.0 | +f01fa40a-992e-42b7-a7f8-211118ffa76c / -— |
| Jogador 6 | 6-3 | 338 | SELL | FAST8 | 79.0 | 7 | 159 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0017308148089796305 | 0.0 | 0.0 | +— / -d0312d75-2176-4d6c-a822-da3c2fa6de8c |
| Jogador 6 | 6-3 | 339 | BUY | FAST8 | 79.0 | 7 | 162 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.09556712210178375 | 0.0 | 0.0 | +35e1d5ed-0853-4ccd-9453-2ada283adcb0 / -— |
| Jogador 6 | 6-3 | 340 | REROLL | FAST8 | 79.0 | 7 | 159 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.01672324910759926 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-4 | 342 | SELL | FAST8 | 62.0 | 7 | 168 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.014615384861826897 | 0.0 | 0.0 | +— / -35e1d5ed-0853-4ccd-9453-2ada283adcb0 |
| Jogador 6 | 6-4 | 343 | BUY | FAST8 | 62.0 | 7 | 171 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.18588872253894806 | 0.0 | 0.0 | +c46a6b77-2f90-4b4c-8def-6a0be7578d2e / -— |
| Jogador 6 | 6-4 | 344 | SELL | FAST8 | 62.0 | 7 | 168 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.04169230908155441 | 0.0 | 0.0 | +— / -c46a6b77-2f90-4b4c-8def-6a0be7578d2e |
| Jogador 6 | 6-4 | 345 | BUY | FAST8 | 62.0 | 7 | 171 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.00829549040645361 | 0.0 | 0.0 | +77c008a4-e922-48ea-98f7-c8f3057a58e7 / -— |
| Jogador 6 | 6-4 | 346 | REROLL | FAST8 | 62.0 | 7 | 169 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03861326724290848 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-4 | 347 | SELL | FAST8 | 62.0 | 7 | 167 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.02784615382552147 | 0.0 | 0.0 | +— / -77c008a4-e922-48ea-98f7-c8f3057a58e7 |
| Jogador 6 | 6-4 | 348 | BUY | FAST8 | 62.0 | 7 | 169 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7702077031135559 | 0.0 | 0.0 | +81220581-f631-426d-a412-9215e458f6d0 / -— |
| Jogador 6 | 6-4 | 349 | SELL | FAST8 | 62.0 | 7 | 166 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.02476923167705536 | 0.0 | 0.0 | +— / -f01fa40a-992e-42b7-a7f8-211118ffa76c |
| Jogador 6 | 6-4 | 350 | BUY | FAST8 | 62.0 | 7 | 170 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.1630086749792099 | 0.0 | 0.0 | +df8c986d-1d20-4704-afa6-022514df3fd5 / -— |
| Jogador 6 | 6-5 | 352 | SELL | FAST8 | 62.0 | 7 | 178 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03799999877810478 | 0.0 | 0.0 | +— / -df8c986d-1d20-4704-afa6-022514df3fd5 |
| Jogador 6 | 6-5 | 353 | BUY | FAST8 | 62.0 | 7 | 181 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.039359986782073975 | 0.0 | 0.0 | +65bcdf99-1b5c-4715-8a9c-f722814f6a97 / -— |
| Jogador 6 | 6-5 | 354 | SELL | FAST8 | 62.0 | 7 | 177 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.023380372673273087 | 0.0 | 0.0 | +— / -65bcdf99-1b5c-4715-8a9c-f722814f6a97 |
| Jogador 6 | 6-5 | 355 | BUY | FAST8 | 62.0 | 7 | 181 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.16300731897354126 | 0.0 | 0.0 | +f7b8096e-ed25-4c3d-8709-5467fdcb2621 / -— |
| Jogador 6 | 6-5 | 356 | REROLL | FAST8 | 62.0 | 7 | 178 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0389714278280735 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-5 | 357 | SELL | FAST8 | 62.0 | 7 | 176 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03799999877810478 | 0.0 | 0.0 | +— / -f7b8096e-ed25-4c3d-8709-5467fdcb2621 |
| Jogador 6 | 6-5 | 358 | BUY | FAST8 | 62.0 | 7 | 179 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0064630508422852 | 0.0 | 0.0 | +8af301f3-b957-4c14-90f0-13aad5e4447a / -7fd34ef6-a124-4d23-a166-9f7ad919c826,81220581-f631-426d-a412-9215e458f6d0 |
| Jogador 6 | 6-5 | 359 | BUY | FAST8 | 62.0 | 7 | 176 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.06516554951667786 | 0.0 | 0.0 | +4b958b2c-5f37-4f5b-bdb0-fa9635476cbd / -— |
| Jogador 6 | 6-5 | 360 | BUY | FAST8 | 62.0 | 7 | 173 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.49167120456695557 | 0.0 | 0.0 | +89167539-62f9-49c5-ab29-d2f4f94a5879 / -— |
| Jogador 6 | 6-6 | 362 | SELL | FAST8 | 45.0 | 7 | 181 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.29461637139320374 | 0.0 | 0.0 | +— / -4b958b2c-5f37-4f5b-bdb0-fa9635476cbd |
| Jogador 6 | 6-6 | 363 | BUY | FAST8 | 45.0 | 7 | 184 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.15584510564804077 | 0.0 | 0.0 | +30e10fda-97d0-40bf-9061-e73c2a4ac09e / -— |
| Jogador 6 | 6-6 | 364 | REROLL | FAST8 | 45.0 | 7 | 181 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0386207178235054 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-6 | 365 | SELL | FAST8 | 45.0 | 7 | 179 | 5 | 40.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.01825411431491375 | 0.0 | 0.0 | +— / -89167539-62f9-49c5-ab29-d2f4f94a5879 |
| Jogador 6 | 6-6 | 366 | BUY | FAST8 | 45.0 | 7 | 182 | 5 | 40.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9997742772102356 | 0.0 | 0.0 | +045f77f4-361f-4745-be79-c43a97085133 / -bbba5910-d3e3-4cd4-9b74-e308ca124f7c,fdc60b5c-31f1-4356-a662-c966d04f9c9d |
| Jogador 6 | 6-6 | 367 | BUY | FAST8 | 45.0 | 7 | 179 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.059366170316934586 | 0.0 | 0.0 | +ede337e2-6783-4887-a053-6112b4757363 / -— |
| Jogador 6 | 6-6 | 368 | SELL | FAST8 | 45.0 | 7 | 176 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.017984261736273766 | 0.0 | 0.0 | +— / -ede337e2-6783-4887-a053-6112b4757363 |
| Jogador 6 | 6-6 | 369 | BUY | FAST8 | 45.0 | 7 | 179 | 5 | 34.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3342709541320801 | 0.0 | 0.0 | +ade1a097-0623-4f32-b741-144a427db485 / -— |
| Jogador 6 | 6-6 | 370 | MOVE_BENCH | FAST8 | 45.0 | 7 | 177 | 5 | 34.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.7921959161758423 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-7 | 372 | BUY | STABILIZE | 29.0 | 7 | 188 | 5 | 50.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.1892712414264679 | 0.0 | 0.0 | +67127cb0-b09d-4db4-b7ef-db49b3ce453e / -— |
| Jogador 6 | 6-7 | 373 | REROLL | STABILIZE | 29.0 | 7 | 185 | 5 | 50.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.052054889500141144 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-7 | 374 | SELL | STABILIZE | 29.0 | 7 | 183 | 5 | 50.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03799999877810478 | 0.0 | 0.0 | +— / -67127cb0-b09d-4db4-b7ef-db49b3ce453e |
| Jogador 6 | 6-7 | 375 | BUY | STABILIZE | 29.0 | 7 | 186 | 5 | 50.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5207539200782776 | 0.0 | 0.0 | +ececf0e3-aef2-4482-b287-a8b68287e13c / -— |
| Jogador 6 | 6-7 | 376 | REROLL | STABILIZE | 29.0 | 7 | 183 | 5 | 50.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.003200070932507515 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-7 | 377 | SELL | STABILIZE | 29.0 | 7 | 181 | 5 | 50.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.00041577895171940327 | 0.0 | 0.0 | +— / -30e10fda-97d0-40bf-9061-e73c2a4ac09e |
| Jogador 6 | 6-7 | 378 | BUY | STABILIZE | 29.0 | 7 | 184 | 5 | 50.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1515594869852066 | 0.0 | 0.0 | +c33a1243-2cbd-475f-a0f3-12a776a3df2f / -— |
| Jogador 6 | 6-7 | 379 | REROLL | STABILIZE | 29.0 | 7 | 180 | 5 | 50.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05206574127078056 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 6-7 | 380 | SELL | STABILIZE | 29.0 | 7 | 178 | 5 | 50.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.052468154579401016 | 0.0 | 0.0 | +— / -045f77f4-361f-4745-be79-c43a97085133 |
| Jogador 6 | 7-1 | 382 | EQUIP_FROM_INVENTORY | STABILIZE | 29.0 | 7 | 197 | 5 | 50.0 | Colosso/DA_Sentinel18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-1 | 383 | EQUIP_FROM_INVENTORY | STABILIZE | 29.0 | 7 | 197 | 5 | 50.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY, CRAFT_AND_EQUIP | True | — | 0.10828304290771484 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-1 | 384 | BUY | STABILIZE | 29.0 | 7 | 197 | 5 | 50.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4365510046482086 | 0.0 | 0.0 | +f6f673a1-1393-4aae-96da-bb4a82fed760 / -— |
| Jogador 6 | 7-1 | 385 | REROLL | STABILIZE | 29.0 | 7 | 194 | 5 | 50.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05192916840314865 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-1 | 386 | SELL | STABILIZE | 29.0 | 7 | 192 | 5 | 50.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.012171576730906963 | 0.0 | 0.0 | +— / -c33a1243-2cbd-475f-a0f3-12a776a3df2f |
| Jogador 6 | 7-1 | 387 | BUY | STABILIZE | 29.0 | 7 | 196 | 5 | 50.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9108431339263916 | 0.0 | 0.0 | +255538ed-7042-4dd6-b37c-03832400c786 / -— |
| Jogador 6 | 7-1 | 388 | REROLL | STABILIZE | 29.0 | 7 | 194 | 5 | 50.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05204033851623535 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-1 | 389 | SELL | STABILIZE | 29.0 | 7 | 192 | 5 | 50.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2983076870441437 | 0.0 | 0.0 | +— / -d8052e34-b223-47b7-8ef1-c0127e6289ac |
| Jogador 6 | 7-1 | 390 | BUY | STABILIZE | 29.0 | 7 | 195 | 5 | 50.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8650809526443481 | 0.0 | 0.0 | +923bacb6-c6c7-46b6-8d5b-35c3e00bcca8 / -— |
| Jogador 6 | 7-2 | 392 | SELL | STABILIZE | 29.0 | 7 | 204 | 5 | 50.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.2983076870441437 | 0.0 | 0.0 | +— / -5a69e9ce-79ff-4c56-a49b-dfb458ecc74c |
| Jogador 6 | 7-2 | 393 | BUY | STABILIZE | 29.0 | 7 | 207 | 5 | 50.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.49271637201309204 | 0.0 | 0.0 | +dceb496a-7218-494c-8c8b-1e9f6a9364e0 / -— |
| Jogador 6 | 7-2 | 394 | SELL | STABILIZE | 29.0 | 7 | 203 | 5 | 50.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.6413846015930176 | 0.0 | 0.0 | +— / -ade1a097-0623-4f32-b741-144a427db485 |
| Jogador 6 | 7-2 | 395 | BUY | STABILIZE | 29.0 | 7 | 205 | 5 | 50.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.02261871099472046 | 0.0 | 0.0 | +d4c6349b-b63b-46b6-a0fa-0ca93a53fa41 / -— |
| Jogador 6 | 7-2 | 396 | REROLL | STABILIZE | 29.0 | 7 | 201 | 5 | 50.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.052051883190870285 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-2 | 397 | SELL | STABILIZE | 29.0 | 7 | 199 | 5 | 50.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0217377170920372 | 0.0 | 0.0 | +— / -d4c6349b-b63b-46b6-a0fa-0ca93a53fa41 |
| Jogador 6 | 7-2 | 398 | BUY | STABILIZE | 29.0 | 7 | 203 | 5 | 50.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4434671998023987 | 0.0 | 0.0 | +b3a88636-9c4c-42e6-a0cd-44758a304ea1 / -— |
| Jogador 6 | 7-2 | 399 | SELL | STABILIZE | 29.0 | 7 | 198 | 5 | 50.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3288252353668213 | 0.0 | 0.0 | +— / -923bacb6-c6c7-46b6-8d5b-35c3e00bcca8 |
| Jogador 6 | 7-2 | 400 | BUY | STABILIZE | 29.0 | 7 | 200 | 5 | 50.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0798596143722534 | 0.0 | 0.0 | +016bc780-9f02-4131-bb7a-98c8dce61647 / -255538ed-7042-4dd6-b37c-03832400c786,b280845c-ba0a-4ef6-95ae-eae11f4882a1 |
| Jogador 6 | 7-3 | 402 | BUY | ALL_IN | 7.0 | 7 | 208 | 5 | 46.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9591106176376343 | 0.0 | 0.0 | +e488a8ec-30f5-49e0-95fb-d7042159a49e / -— |
| Jogador 6 | 7-3 | 403 | SELL | ALL_IN | 7.0 | 7 | 205 | 5 | 46.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.12421867996454239 | 0.0 | 0.0 | +— / -016bc780-9f02-4131-bb7a-98c8dce61647 |
| Jogador 6 | 7-3 | 404 | BUY | ALL_IN | 7.0 | 7 | 210 | 5 | 46.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.43603625893592834 | 0.0 | 0.0 | +06c04d09-3849-4cbd-8cd4-a4a9ab3afe67 / -— |
| Jogador 6 | 7-3 | 405 | REROLL | ALL_IN | 7.0 | 7 | 209 | 5 | 46.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.07003306597471237 | 0.0 | 0.0 | +— / -— |
| Jogador 6 | 7-3 | 406 | SELL | ALL_IN | 7.0 | 7 | 207 | 5 | 46.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.3707977533340454 | 0.0 | 0.0 | +— / -06c04d09-3849-4cbd-8cd4-a4a9ab3afe67 |
| Jogador 6 | 7-3 | 407 | BUY | ALL_IN | 7.0 | 7 | 208 | 5 | 46.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 1.0699923038482666 | 0.0 | 0.0 | +fe3c8cf1-056c-4686-9110-e9eb6ff8254c / -e488a8ec-30f5-49e0-95fb-d7042159a49e,ececf0e3-aef2-4482-b287-a8b68287e13c |
| Jogador 6 | 7-3 | 408 | BUY | ALL_IN | 7.0 | 7 | 205 | 5 | 46.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5855429768562317 | 0.0 | 0.0 | +c5f55003-2085-497b-9d38-807038eae8d2 / -— |
| Jogador 6 | 7-3 | 409 | BUY | ALL_IN | 7.0 | 7 | 204 | 5 | 46.0 | Colosso/DA_Sentinel18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.24951499700546265 | 0.0 | 0.0 | +d1c53583-f52b-4037-a047-7bd8d987970a / -— |
| Jogador 6 | 7-3 | 410 | MOVE_BENCH | ALL_IN | 7.0 | 7 | 202 | 5 | 46.0 | Colosso/DA_Sentinel18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5587138533592224 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 1 | SELL | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | -0.019615383818745613 | 0.0 | 0.0 | +— / -66b7d7c5-62d3-49aa-b8f4-b3f936b1f987 |
| Jogador 7 | 1-1 | 2 | BUY | STABILIZE | 100.0 | 2 | 1 | 0 | 0.0 | —/— | BUY, PASS | True | True | 0.40001964569091797 | 0.0 | 0.0 | +c2a4318c-af60-41e2-8e14-c3ad967569a0 / -— |
| Jogador 7 | 1-1 | 3 | MOVE_BENCH | STABILIZE | 100.0 | 2 | 0 | 0 | 0.0 | —/DA_18_Rakan | MOVE_BENCH, SELL, PASS | True | True | 0.5990749597549438 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 4 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.13061420619487762 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-1 | 5 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.006489977240562439 | 0.0 | 0.0 | +47ec6577-cbf2-4275-b185-c19256223441 / -— |
| Jogador 7 | 1-2 | 12 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22031916677951813 | 0.0 | 0.0 | +— / -47ec6577-cbf2-4275-b185-c19256223441 |
| Jogador 7 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.005868818145245314 | 0.0 | 0.0 | +b21d3fc8-71ce-4669-b0ba-931c6e11cb69 / -— |
| Jogador 7 | 1-2 | 14 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14956119656562805 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 15 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 16 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.0849403440952301 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 17 | BUY | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.9622653722763062 | 0.0 | 0.0 | +a529e9b4-89c2-47e0-b821-7269b112f8ef / -— |
| Jogador 7 | 1-2 | 18 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 4.0 | —/DA_18_Rakan | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05244371294975281 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-2 | 19 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.06377681344747543 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.307613343000412 | 0.0 | 0.0 | +734c75dd-d0f3-4b9f-abe8-a228e23557a2 / -— |
| Jogador 7 | 1-3 | 22 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 0 | 0 | 6.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37080299854278564 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-3 | 23 | SELL | STABILIZE | 100.0 | 3 | 0 | 0 | 8.0 | —/DA_Scuttlecrab18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.37869876623153687 | 0.0 | 0.0 | +— / -c2a4318c-af60-41e2-8e14-c3ad967569a0 |
| Jogador 7 | 1-3 | 24 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.05522426590323448 | 0.0 | 0.0 | +a179e7d4-31e2-4a74-9905-0daede16517e / -— |
| Jogador 7 | 1-4 | 32 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4940348267555237 | 0.0 | 0.0 | +— / -a179e7d4-31e2-4a74-9905-0daede16517e |
| Jogador 7 | 1-4 | 33 | PASS | STABILIZE | 100.0 | 3 | 4 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.3034904897212982 | 0.0 | 0.0 | +de82e676-8d8b-4437-958e-a8398a3cfade / -— |
| Jogador 7 | 2-1 | 42 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 6 | 0 | 8.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4476790428161621 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 43 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_Scuttlecrab18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.024840479716658592 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-1 | 44 | PASS | STABILIZE | 100.0 | 4 | 6 | 0 | 12.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 50 | BUY | STABILIZE | 100.0 | 4 | 12 | 1 | 12.0 | —/DA_18_Alistar | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.15488873422145844 | 0.0 | 0.0 | +0cf5c315-d2f3-4854-a95b-07912b83ea81 / -— |
| Jogador 7 | 2-2 | 51 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 9 | 0 | 12.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07004614919424057 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-2 | 52 | SELL | STABILIZE | 100.0 | 4 | 9 | 0 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2992396056652069 | 0.0 | 0.0 | +— / -a529e9b4-89c2-47e0-b821-7269b112f8ef |
| Jogador 7 | 2-2 | 53 | PASS | STABILIZE | 100.0 | 4 | 10 | 1 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 60 | BUY | STABILIZE | 100.0 | 4 | 18 | 1 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9679856896400452 | 0.0 | 0.0 | +801687e6-da6a-4ab1-8032-a45daf0e6554 / -— |
| Jogador 7 | 2-3 | 61 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 16 | 1 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02516235038638115 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 62 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 16 | 1 | 14.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21871235966682434 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-3 | 63 | PASS | STABILIZE | 100.0 | 4 | 16 | 1 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 70 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 22 | 2 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3515869975090027 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 71 | BUY | STABILIZE | 95.0 | 4 | 22 | 2 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9548003673553467 | 0.0 | 0.0 | +0c15e414-bc67-46de-a087-fb7708db0dfe / -— |
| Jogador 7 | 2-4 | 72 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 20 | 2 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 73 | MOVE_BENCH | STABILIZE | 95.0 | 4 | 20 | 2 | 16.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05673341453075409 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 74 | SELL | STABILIZE | 95.0 | 4 | 20 | 2 | 18.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05567524954676628 | 0.0 | 0.0 | +— / -b21d3fc8-71ce-4669-b0ba-931c6e11cb69 |
| Jogador 7 | 2-4 | 75 | BUY_XP | STABILIZE | 95.0 | 4 | 21 | 2 | 18.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030220000073313713 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 76 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 17 | 1 | 18.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.452711284160614 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 77 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 17 | 1 | 22.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-4 | 78 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 17 | 1 | 22.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 80 | BUY | STABILIZE | 95.0 | 5 | 23 | 2 | 22.0 | —/DA_18_Hecarim | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.426085889339447 | 0.0 | 0.0 | +8ea1c095-e10b-46d0-8097-a70a211e2881 / -— |
| Jogador 7 | 2-5 | 81 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 20 | 2 | 22.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3476698100566864 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 82 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 20 | 2 | 24.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-5 | 83 | PASS | STABILIZE | 95.0 | 5 | 20 | 2 | 24.0 | Sabugueiro/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 89 | MOVE_BOARD | STABILIZE | 95.0 | 5 | 28 | 2 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30979663133621216 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 90 | MOVE_BENCH | STABILIZE | 95.0 | 5 | 28 | 2 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6380575895309448 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-6 | 91 | PASS | STABILIZE | 95.0 | 5 | 28 | 2 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 98 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 37 | 3 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09998553991317749 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 99 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 37 | 3 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 100 | MOVE_BOARD | SLOWROLL | 95.0 | 5 | 37 | 3 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05787229165434837 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 101 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 37 | 3 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6382801532745361 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 102 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 37 | 3 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.4000000059604645 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 2-7 | 103 | PASS | SLOWROLL | 95.0 | 5 | 37 | 3 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 107 | MOVE_BENCH | SLOWROLL | 95.0 | 5 | 46 | 4 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09998560696840286 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 108 | SELL | SLOWROLL | 95.0 | 5 | 46 | 4 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34519514441490173 | 0.0 | 0.0 | +— / -801687e6-da6a-4ab1-8032-a45daf0e6554 |
| Jogador 7 | 3-1 | 109 | MOVE_BOARD | SLOWROLL | 95.0 | 5 | 48 | 4 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 110 | MOVE_BOARD | SLOWROLL | 95.0 | 5 | 48 | 4 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-1 | 111 | PASS | SLOWROLL | 95.0 | 5 | 48 | 4 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 116 | BUY | SLOWROLL | 86.0 | 5 | 57 | 5 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.32974016666412354 | 0.0 | 0.0 | +8df39648-f588-452a-b234-32da76c43aff / -— |
| Jogador 7 | 3-2 | 117 | SELL | SLOWROLL | 86.0 | 5 | 55 | 5 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.5540270805358887 | 0.0 | 0.0 | +— / -8df39648-f588-452a-b234-32da76c43aff |
| Jogador 7 | 3-2 | 118 | MOVE_BOARD | SLOWROLL | 86.0 | 5 | 57 | 5 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1792120337486267 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 119 | MOVE_BOARD | SLOWROLL | 86.0 | 5 | 57 | 5 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.1616162657737732 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 120 | MOVE_BOARD | SLOWROLL | 86.0 | 5 | 57 | 5 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.28826963901519775 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 121 | MOVE_BOARD | SLOWROLL | 86.0 | 5 | 57 | 5 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-2 | 122 | PASS | SLOWROLL | 86.0 | 5 | 57 | 5 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.002875805599614978 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 125 | BUY | SLOWROLL | 76.0 | 5 | 68 | 5 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.02376081980764866 | 0.0 | 0.0 | +4518ad1d-87e7-4110-830a-96183c533201 / -— |
| Jogador 7 | 3-3 | 126 | MOVE_BENCH | SLOWROLL | 76.0 | 5 | 65 | 5 | 24.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3007229268550873 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 127 | SELL | SLOWROLL | 76.0 | 5 | 65 | 5 | 26.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7280652523040771 | 0.0 | 0.0 | +— / -0c15e414-bc67-46de-a087-fb7708db0dfe |
| Jogador 7 | 3-3 | 128 | BUY | STABILIZE | 76.0 | 5 | 67 | 5 | 26.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4339751601219177 | 0.0 | 0.0 | +da5abe09-7f54-4361-8d82-84427a9da9e1 / -— |
| Jogador 7 | 3-3 | 129 | SELL | STABILIZE | 76.0 | 5 | 65 | 5 | 26.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.577923059463501 | 0.0 | 0.0 | +— / -da5abe09-7f54-4361-8d82-84427a9da9e1 |
| Jogador 7 | 3-3 | 130 | MOVE_BOARD | STABILIZE | 76.0 | 5 | 67 | 5 | 26.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.06667235493659973 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 131 | BUY_XP | STABILIZE | 76.0 | 5 | 67 | 5 | 26.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-3 | 132 | BUY_XP | STABILIZE | 76.0 | 5 | 63 | 5 | 26.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.2682250142097473 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 134 | BUY | FAST8 | 76.0 | 6 | 70 | 5 | 26.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.33870959281921387 | 0.0 | 0.0 | +301afc05-ad23-4ed2-a835-108235c399e0 / -— |
| Jogador 7 | 3-4 | 135 | BUY | FAST8 | 76.0 | 6 | 67 | 5 | 26.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.056336045265197754 | 0.0 | 0.0 | +b750b244-a898-479e-9a8e-f30a3f4b0005 / -— |
| Jogador 7 | 3-4 | 136 | MOVE_BENCH | FAST8 | 76.0 | 6 | 64 | 5 | 26.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.41660648584365845 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 137 | MOVE_BOARD | FAST8 | 76.0 | 6 | 64 | 5 | 32.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26218318939208984 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 138 | MOVE_BOARD | FAST8 | 76.0 | 6 | 64 | 5 | 32.0 | Fera do Rift/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13750514388084412 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 139 | MOVE_BOARD | FAST8 | 76.0 | 6 | 64 | 5 | 32.0 | Fera do Rift/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.032957449555397034 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 140 | REROLL | FAST8 | 76.0 | 6 | 64 | 5 | 32.0 | Fera do Rift/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.015549849718809128 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-4 | 141 | BUY | FAST8 | 76.0 | 6 | 62 | 5 | 32.0 | Fera do Rift/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8144598603248596 | 0.0 | 0.0 | +f444bf9a-0e92-4a76-b4d0-9e1bac73cb77 / -— |
| Jogador 7 | 3-5 | 143 | BUY | SLOWROLL | 76.0 | 6 | 69 | 5 | 32.0 | Fera do Rift/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.832526683807373 | 0.0 | 0.0 | +db6b2dca-4de1-420e-aadb-943e19b6121a / -— |
| Jogador 7 | 3-5 | 144 | BUY | SLOWROLL | 76.0 | 6 | 66 | 5 | 32.0 | Fera do Rift/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.08664898574352264 | 0.0 | 0.0 | +5c931416-3aeb-40d4-9e6f-612b0d387226 / -— |
| Jogador 7 | 3-5 | 145 | BUY | SLOWROLL | 76.0 | 6 | 62 | 5 | 32.0 | Fera do Rift/DA_18_Diana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7759490609169006 | 0.0 | 0.0 | +673bda2e-1343-4894-8005-c3ee2c90f1b7 / -— |
| Jogador 7 | 3-5 | 146 | BUY | SLOWROLL | 76.0 | 6 | 58 | 5 | 32.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31201478838920593 | 0.0 | 0.0 | +565ff610-fe51-470b-8452-a7eec5e31653 / -— |
| Jogador 7 | 3-5 | 147 | REROLL | SLOWROLL | 76.0 | 6 | 55 | 5 | 32.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2499469816684723 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-5 | 148 | BUY | SLOWROLL | 76.0 | 6 | 53 | 5 | 32.0 | Fera do Rift/DA_18_Aphelios | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8652055263519287 | 0.0 | 0.0 | +4688e6f1-26c5-402d-8d27-0f9bce3a9681 / -4518ad1d-87e7-4110-830a-96183c533201,db6b2dca-4de1-420e-aadb-943e19b6121a |
| Jogador 7 | 3-5 | 149 | BUY | SLOWROLL | 76.0 | 6 | 50 | 5 | 26.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.20460498332977295 | 0.0 | 0.0 | +6c338d19-b3d3-49a7-b61e-4732249ee457 / -— |
| Jogador 7 | 3-5 | 150 | BUY | SLOWROLL | 76.0 | 6 | 48 | 4 | 26.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.25981783866882324 | 0.0 | 0.0 | +7313188a-ce84-4a52-b2d0-a94b2c420cdb / -— |
| Jogador 7 | 3-6 | 152 | BUY | SLOWROLL | 76.0 | 6 | 56 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5202544331550598 | 0.0 | 0.0 | +27079fe2-8808-47b7-8b10-9fb2834bb6ed / -— |
| Jogador 7 | 3-6 | 153 | REROLL | SLOWROLL | 76.0 | 6 | 54 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.07449887692928314 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 154 | BUY | SLOWROLL | 76.0 | 6 | 52 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026587797328829765 | 0.0 | 0.0 | +92bac611-1820-42eb-8243-499f20058673 / -— |
| Jogador 7 | 3-6 | 155 | REROLL | SLOWROLL | 76.0 | 6 | 50 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13502061367034912 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 156 | SELL | SLOWROLL | 76.0 | 6 | 48 | 4 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11184615641832352 | 0.0 | 0.0 | +— / -92bac611-1820-42eb-8243-499f20058673 |
| Jogador 7 | 3-6 | 157 | BUY | SLOWROLL | 76.0 | 6 | 50 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19303907454013824 | 0.0 | 0.0 | +ab6bd13e-9d3a-4a6e-8f99-cd46f301e1d4 / -— |
| Jogador 7 | 3-6 | 158 | REROLL | SLOWROLL | 76.0 | 6 | 46 | 4 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09887565672397614 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-6 | 159 | SELL | SLOWROLL | 76.0 | 6 | 44 | 4 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30630770325660706 | 0.0 | 0.0 | +— / -27079fe2-8808-47b7-8b10-9fb2834bb6ed |
| Jogador 7 | 3-6 | 160 | BUY | SLOWROLL | 76.0 | 6 | 46 | 4 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.22823777794837952 | 0.0 | 0.0 | +db79d601-4b72-43c1-a8e3-4755c3442aa0 / -— |
| Jogador 7 | 3-7 | 162 | SELL | SLOWROLL | 66.0 | 6 | 52 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -7313188a-ce84-4a52-b2d0-a94b2c420cdb |
| Jogador 7 | 3-7 | 163 | BUY | SLOWROLL | 66.0 | 6 | 55 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.523146390914917 | 0.0 | 0.0 | +c5f81113-0e4a-4d08-beab-f19d808ef10c / -— |
| Jogador 7 | 3-7 | 164 | SELL | SLOWROLL | 66.0 | 6 | 52 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06078440696001053 | 0.0 | 0.0 | +— / -565ff610-fe51-470b-8452-a7eec5e31653 |
| Jogador 7 | 3-7 | 165 | BUY | SLOWROLL | 66.0 | 6 | 55 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.026658717542886734 | 0.0 | 0.0 | +45bb5798-7b34-48ad-b40b-a871e20a4e62 / -— |
| Jogador 7 | 3-7 | 166 | REROLL | SLOWROLL | 66.0 | 6 | 53 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24994619190692902 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 3-7 | 167 | SELL | SLOWROLL | 66.0 | 6 | 51 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.017384614795446396 | 0.0 | 0.0 | +— / -45bb5798-7b34-48ad-b40b-a871e20a4e62 |
| Jogador 7 | 3-7 | 168 | BUY | SLOWROLL | 66.0 | 6 | 53 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.704009473323822 | 0.0 | 0.0 | +2ed60268-d2b1-4e41-bae7-43a89060e325 / -— |
| Jogador 7 | 3-7 | 169 | SELL | SLOWROLL | 66.0 | 6 | 50 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30034396052360535 | 0.0 | 0.0 | +— / -c5f81113-0e4a-4d08-beab-f19d808ef10c |
| Jogador 7 | 3-7 | 170 | BUY | SLOWROLL | 66.0 | 6 | 53 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.723395824432373 | 0.0 | 0.0 | +0650ed76-f3bb-4dce-bd04-2ed294039e6d / -— |
| Jogador 7 | 4-1 | 172 | SELL | SLOWROLL | 66.0 | 6 | 61 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02476923167705536 | 0.0 | 0.0 | +— / -ab6bd13e-9d3a-4a6e-8f99-cd46f301e1d4 |
| Jogador 7 | 4-1 | 173 | BUY | SLOWROLL | 66.0 | 6 | 65 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.45488181710243225 | 0.0 | 0.0 | +aa6b7c66-6aa1-4cd5-9005-449e37829ad8 / -— |
| Jogador 7 | 4-1 | 174 | SELL | SLOWROLL | 66.0 | 6 | 62 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30013930797576904 | 0.0 | 0.0 | +— / -aa6b7c66-6aa1-4cd5-9005-449e37829ad8 |
| Jogador 7 | 4-1 | 175 | BUY | SLOWROLL | 66.0 | 6 | 65 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2514338791370392 | 0.0 | 0.0 | +cdd76540-e76c-41e9-ac02-253f5ba2e75e / -— |
| Jogador 7 | 4-1 | 176 | REROLL | SLOWROLL | 66.0 | 6 | 62 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15078376233577728 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-1 | 177 | SELL | SLOWROLL | 66.0 | 6 | 60 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05000000074505806 | 0.0 | 0.0 | +— / -cdd76540-e76c-41e9-ac02-253f5ba2e75e |
| Jogador 7 | 4-1 | 178 | BUY | SLOWROLL | 66.0 | 6 | 63 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2455068975687027 | 0.0 | 0.0 | +c6cfacad-08af-4690-9ef3-7751f1aa7a30 / -— |
| Jogador 7 | 4-1 | 179 | SELL | SLOWROLL | 66.0 | 6 | 59 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04938461631536484 | 0.0 | 0.0 | +— / -c6cfacad-08af-4690-9ef3-7751f1aa7a30 |
| Jogador 7 | 4-1 | 180 | BUY | SLOWROLL | 66.0 | 6 | 63 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08269966393709183 | 0.0 | 0.0 | +8d23f5c9-fc15-4a57-ae3b-07922bd3fb0a / -— |
| Jogador 7 | 4-2 | 182 | SELL | SLOWROLL | 66.0 | 6 | 72 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026615384966135025 | 0.0 | 0.0 | +— / -8d23f5c9-fc15-4a57-ae3b-07922bd3fb0a |
| Jogador 7 | 4-2 | 183 | BUY | SLOWROLL | 66.0 | 6 | 74 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7805687189102173 | 0.0 | 0.0 | +663c9fe5-55b8-4c50-b544-aba5b6e02070 / -— |
| Jogador 7 | 4-2 | 184 | SELL | SLOWROLL | 66.0 | 6 | 71 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6882284879684448 | 0.0 | 0.0 | +— / -6c338d19-b3d3-49a7-b61e-4732249ee457 |
| Jogador 7 | 4-2 | 185 | BUY | SLOWROLL | 66.0 | 6 | 73 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3031640648841858 | 0.0 | 0.0 | +3d5d6bd5-f830-482c-97a0-370f00a5768f / -— |
| Jogador 7 | 4-2 | 186 | SELL | SLOWROLL | 66.0 | 6 | 71 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36646175384521484 | 0.0 | 0.0 | +— / -3d5d6bd5-f830-482c-97a0-370f00a5768f |
| Jogador 7 | 4-2 | 187 | BUY | SLOWROLL | 66.0 | 6 | 73 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19359128177165985 | 0.0 | 0.0 | +873a048e-aacb-4628-8a0b-7b3fc3558ca6 / -— |
| Jogador 7 | 4-2 | 188 | REROLL | SLOWROLL | 66.0 | 6 | 70 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.14428861439228058 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-2 | 189 | SELL | SLOWROLL | 66.0 | 6 | 68 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03799999877810478 | 0.0 | 0.0 | +— / -873a048e-aacb-4628-8a0b-7b3fc3558ca6 |
| Jogador 7 | 4-2 | 190 | BUY | SLOWROLL | 66.0 | 6 | 71 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.003734726458787918 | 0.0 | 0.0 | +1ffb7115-2f25-4625-80c4-37c853de7ea2 / -— |
| Jogador 7 | 4-3 | 192 | SELL | SLOWROLL | 55.0 | 6 | 79 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.025025924667716026 | 0.0 | 0.0 | +— / -1ffb7115-2f25-4625-80c4-37c853de7ea2 |
| Jogador 7 | 4-3 | 193 | BUY | SLOWROLL | 55.0 | 6 | 81 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016222937032580376 | 0.0 | 0.0 | +fee6781d-6d63-44f2-bd1b-a58de5aa3ae4 / -— |
| Jogador 7 | 4-3 | 194 | SELL | SLOWROLL | 55.0 | 6 | 78 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026307692751288414 | 0.0 | 0.0 | +— / -fee6781d-6d63-44f2-bd1b-a58de5aa3ae4 |
| Jogador 7 | 4-3 | 195 | BUY | SLOWROLL | 55.0 | 6 | 81 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.027120275422930717 | 0.0 | 0.0 | +18bfe549-f0cb-4125-8b75-ebd2609417ce / -— |
| Jogador 7 | 4-3 | 196 | REROLL | SLOWROLL | 55.0 | 6 | 79 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.15078376233577728 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-3 | 197 | SELL | SLOWROLL | 55.0 | 6 | 77 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02784615382552147 | 0.0 | 0.0 | +— / -18bfe549-f0cb-4125-8b75-ebd2609417ce |
| Jogador 7 | 4-3 | 198 | BUY | SLOWROLL | 55.0 | 6 | 79 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.19362156093120575 | 0.0 | 0.0 | +8bff8eff-1e6b-4571-8300-ec2ba05f4d16 / -— |
| Jogador 7 | 4-3 | 199 | SELL | SLOWROLL | 55.0 | 6 | 76 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03799999877810478 | 0.0 | 0.0 | +— / -8bff8eff-1e6b-4571-8300-ec2ba05f4d16 |
| Jogador 7 | 4-3 | 200 | BUY | SLOWROLL | 55.0 | 6 | 79 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.02723926305770874 | 0.0 | 0.0 | +a6e53d47-9d41-405c-bf79-812548fcd9c0 / -— |
| Jogador 7 | 4-4 | 202 | SELL | SLOWROLL | 55.0 | 6 | 88 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02784615382552147 | 0.0 | 0.0 | +— / -a6e53d47-9d41-405c-bf79-812548fcd9c0 |
| Jogador 7 | 4-4 | 203 | BUY | SLOWROLL | 55.0 | 6 | 90 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2862132489681244 | 0.0 | 0.0 | +be744302-6d5a-43de-b670-727cb9597305 / -— |
| Jogador 7 | 4-4 | 204 | SELL | SLOWROLL | 55.0 | 6 | 87 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06023353710770607 | 0.0 | 0.0 | +— / -be744302-6d5a-43de-b670-727cb9597305 |
| Jogador 7 | 4-4 | 205 | BUY | SLOWROLL | 55.0 | 6 | 90 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.016323106363415718 | 0.0 | 0.0 | +33cbde1a-eb0d-481b-86a4-6c8b27854a79 / -— |
| Jogador 7 | 4-4 | 206 | REROLL | SLOWROLL | 55.0 | 6 | 87 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24999839067459106 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-4 | 207 | SELL | SLOWROLL | 55.0 | 6 | 85 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.026307692751288414 | 0.0 | 0.0 | +— / -33cbde1a-eb0d-481b-86a4-6c8b27854a79 |
| Jogador 7 | 4-4 | 208 | BUY | SLOWROLL | 55.0 | 6 | 88 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8899894952774048 | 0.0 | 0.0 | +f223dc33-7214-4bcf-af0f-1d5ee4a9c2ca / -663c9fe5-55b8-4c50-b544-aba5b6e02070,8ea1c095-e10b-46d0-8097-a70a211e2881 |
| Jogador 7 | 4-4 | 209 | BUY | SLOWROLL | 55.0 | 6 | 85 | 5 | 26.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1024186983704567 | 0.0 | 0.0 | +ff6a3945-c881-47b7-a6ae-85ef6640487d / -— |
| Jogador 7 | 4-4 | 210 | MOVE_BENCH | SLOWROLL | 55.0 | 6 | 82 | 5 | 26.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6615050435066223 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 212 | BUY | SLOWROLL | 55.0 | 6 | 92 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.544475793838501 | 0.0 | 0.0 | +0b8fa4cd-2707-4ec8-8ce0-c200efbc31e5 / -— |
| Jogador 7 | 4-5 | 213 | REROLL | SLOWROLL | 55.0 | 6 | 89 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17161361873149872 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 214 | SELL | SLOWROLL | 55.0 | 6 | 87 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029999999329447746 | 0.0 | 0.0 | +— / -ff6a3945-c881-47b7-a6ae-85ef6640487d |
| Jogador 7 | 4-5 | 215 | BUY | SLOWROLL | 55.0 | 6 | 90 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2723501920700073 | 0.0 | 0.0 | +e0be1ac4-4735-4814-aae2-78f95befc63f / -— |
| Jogador 7 | 4-5 | 216 | REROLL | SLOWROLL | 55.0 | 6 | 87 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24955764412879944 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-5 | 217 | SELL | SLOWROLL | 55.0 | 6 | 85 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.044320590794086456 | 0.0 | 0.0 | +— / -e0be1ac4-4735-4814-aae2-78f95befc63f |
| Jogador 7 | 4-5 | 218 | BUY | SLOWROLL | 55.0 | 6 | 88 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8844907283782959 | 0.0 | 0.0 | +e5a3d517-4225-49b8-8675-286557e75b93 / -b750b244-a898-479e-9a8e-f30a3f4b0005,f444bf9a-0e92-4a76-b4d0-9e1bac73cb77 |
| Jogador 7 | 4-5 | 219 | BUY | SLOWROLL | 55.0 | 6 | 85 | 5 | 26.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.28251171112060547 | 0.0 | 0.0 | +e0f5f5d7-888c-4cc2-bfb0-47fb6a11c6d2 / -— |
| Jogador 7 | 4-5 | 220 | MOVE_BENCH | SLOWROLL | 55.0 | 6 | 83 | 5 | 26.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.13343137502670288 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 222 | BUY | SLOWROLL | 55.0 | 6 | 95 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3316820561885834 | 0.0 | 0.0 | +518304a8-a259-4779-95b1-89403e4e332d / -— |
| Jogador 7 | 4-6 | 223 | SELL | SLOWROLL | 55.0 | 6 | 92 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.28261539340019226 | 0.0 | 0.0 | +— / -5c931416-3aeb-40d4-9e6f-612b0d387226 |
| Jogador 7 | 4-6 | 224 | BUY | SLOWROLL | 55.0 | 6 | 96 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.1695028394460678 | 0.0 | 0.0 | +a99b9c50-8ad2-4863-94fd-5c8a80ae86b2 / -— |
| Jogador 7 | 4-6 | 225 | REROLL | SLOWROLL | 55.0 | 6 | 93 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2374594360589981 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 226 | SELL | SLOWROLL | 55.0 | 6 | 91 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03799999877810478 | 0.0 | 0.0 | +— / -a99b9c50-8ad2-4863-94fd-5c8a80ae86b2 |
| Jogador 7 | 4-6 | 227 | BUY | SLOWROLL | 55.0 | 6 | 94 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7495060563087463 | 0.0 | 0.0 | +d944061b-eef5-40d5-8b9a-a1b4b2dbb9e2 / -— |
| Jogador 7 | 4-6 | 228 | REROLL | SLOWROLL | 55.0 | 6 | 92 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.24692365527153015 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-6 | 229 | SELL | SLOWROLL | 55.0 | 6 | 90 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.04600000008940697 | 0.0 | 0.0 | +— / -0650ed76-f3bb-4dce-bd04-2ed294039e6d |
| Jogador 7 | 4-6 | 230 | BUY | SLOWROLL | 55.0 | 6 | 92 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8892921805381775 | 0.0 | 0.0 | +16dc2385-4023-4ce6-a090-fd8dc59d0888 / -d944061b-eef5-40d5-8b9a-a1b4b2dbb9e2,e0f5f5d7-888c-4cc2-bfb0-47fb6a11c6d2 |
| Jogador 7 | 4-7 | 232 | BUY | SLOWROLL | 55.0 | 6 | 101 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05032223090529442 | 0.0 | 0.0 | +2d1485b0-91be-4bf3-aa68-9fa599b8313b / -— |
| Jogador 7 | 4-7 | 233 | BUY | SLOWROLL | 55.0 | 6 | 98 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.16710001230239868 | 0.0 | 0.0 | +faf4e579-8c95-4fa0-bc1a-c2619c7fdb57 / -— |
| Jogador 7 | 4-7 | 234 | REROLL | SLOWROLL | 55.0 | 6 | 95 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.2499370574951172 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 235 | SELL | SLOWROLL | 55.0 | 6 | 93 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.035538461059331894 | 0.0 | 0.0 | +— / -2d1485b0-91be-4bf3-aa68-9fa599b8313b |
| Jogador 7 | 4-7 | 236 | BUY | SLOWROLL | 55.0 | 6 | 96 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.753532886505127 | 0.0 | 0.0 | +478395b3-8de6-4599-90ea-f3315a0de63c / -— |
| Jogador 7 | 4-7 | 237 | SELL | SLOWROLL | 55.0 | 6 | 94 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03799999877810478 | 0.0 | 0.0 | +— / -faf4e579-8c95-4fa0-bc1a-c2619c7fdb57 |
| Jogador 7 | 4-7 | 238 | BUY | SLOWROLL | 55.0 | 6 | 97 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29941773414611816 | 0.0 | 0.0 | +9ac2f739-7903-45cc-9b8c-11602c4141d2 / -— |
| Jogador 7 | 4-7 | 239 | REROLL | SLOWROLL | 55.0 | 6 | 95 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05584390461444855 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 4-7 | 240 | SELL | SLOWROLL | 55.0 | 6 | 93 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.09830769151449203 | 0.0 | 0.0 | +— / -16dc2385-4023-4ce6-a090-fd8dc59d0888 |
| Jogador 7 | 5-1 | 242 | EQUIP_FROM_INVENTORY | SLOWROLL | 55.0 | 6 | 109 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 243 | BUY | SLOWROLL | 55.0 | 6 | 109 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.9484195709228516 | 0.0 | 0.0 | +3d460466-65ca-4415-b12f-5dfd54e73a7e / -2ed60268-d2b1-4e41-bae7-43a89060e325,301afc05-ad23-4ed2-a835-108235c399e0 |
| Jogador 7 | 5-1 | 244 | BUY | SLOWROLL | 55.0 | 6 | 106 | 5 | 26.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8737311363220215 | 0.0 | 0.0 | +a7871336-b876-48af-804e-a4af0b835dbd / -0b8fa4cd-2707-4ec8-8ce0-c200efbc31e5,0cf5c315-d2f3-4854-a95b-07912b83ea81 |
| Jogador 7 | 5-1 | 245 | MOVE_BENCH | SLOWROLL | 55.0 | 6 | 103 | 5 | 14.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.432955265045166 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 246 | BUY | SLOWROLL | 55.0 | 6 | 103 | 5 | 26.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.08353827148675919 | 0.0 | 0.0 | +18c6da8d-fcbd-4939-85e8-c619216902cf / -— |
| Jogador 7 | 5-1 | 247 | REROLL | SLOWROLL | 55.0 | 6 | 102 | 5 | 26.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.1963673084974289 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-1 | 248 | SELL | SLOWROLL | 55.0 | 6 | 100 | 5 | 26.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.006149466149508953 | 0.0 | 0.0 | +— / -18c6da8d-fcbd-4939-85e8-c619216902cf |
| Jogador 7 | 5-1 | 249 | BUY | SLOWROLL | 55.0 | 6 | 101 | 5 | 26.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.05620477348566055 | 0.0 | 0.0 | +6e1981b6-51e6-4177-9383-8e9af58a8cf6 / -— |
| Jogador 7 | 5-1 | 250 | MOVE_BENCH | SLOWROLL | 55.0 | 6 | 98 | 5 | 26.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.45087650418281555 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 252 | BUY | SLOWROLL | 42.0 | 6 | 108 | 5 | 32.0 | Fera do Rift/DA_CrimsonRaptor18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.3576236963272095 | 0.0 | 0.0 | +f77233ea-3942-4543-80ab-d53e69f5cba8 / -— |
| Jogador 7 | 5-2 | 253 | SELL | SLOWROLL | 42.0 | 6 | 105 | 5 | 32.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.00029076775535941124 | 0.0 | 0.0 | +— / -a7871336-b876-48af-804e-a4af0b835dbd |
| Jogador 7 | 5-2 | 254 | BUY | SLOWROLL | 42.0 | 6 | 113 | 5 | 32.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.31841495633125305 | 0.0 | 0.0 | +350b71be-3cdb-4da2-aeef-0be87772e418 / -— |
| Jogador 7 | 5-2 | 255 | REROLL | SLOWROLL | 42.0 | 6 | 110 | 5 | 32.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.2569802403450012 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 256 | SELL | SLOWROLL | 42.0 | 6 | 108 | 5 | 32.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.024155301973223686 | 0.0 | 0.0 | +— / -6e1981b6-51e6-4177-9383-8e9af58a8cf6 |
| Jogador 7 | 5-2 | 257 | BUY | SLOWROLL | 42.0 | 6 | 111 | 5 | 32.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8336615562438965 | 0.0 | 0.0 | +b3a61b8a-9288-4309-8426-fde1d0600b4c / -— |
| Jogador 7 | 5-2 | 258 | REROLL | SLOWROLL | 42.0 | 6 | 108 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.11920814961194992 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-2 | 259 | SELL | SLOWROLL | 42.0 | 6 | 106 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.06292307376861572 | 0.0 | 0.0 | +— / -350b71be-3cdb-4da2-aeef-0be87772e418 |
| Jogador 7 | 5-2 | 260 | MOVE_BENCH | SLOWROLL | 42.0 | 6 | 109 | 5 | 32.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.5161339044570923 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 262 | BUY | STABILIZE | 28.0 | 6 | 120 | 5 | 38.0 | Fera do Rift/DA_Fiddlesticks18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.8926534652709961 | 0.0 | 0.0 | +874c674c-2608-4ae4-8d63-1dc3a091f635 / -— |
| Jogador 7 | 5-3 | 263 | BUY | STABILIZE | 28.0 | 6 | 117 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07280075550079346 | 0.0 | 0.0 | +a42bf7ae-86c7-4a8c-bbe6-4b9d1ad0c7a0 / -— |
| Jogador 7 | 5-3 | 264 | REROLL | STABILIZE | 28.0 | 6 | 114 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05206690728664398 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 265 | SELL | STABILIZE | 28.0 | 6 | 112 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.02507692389190197 | 0.0 | 0.0 | +— / -a42bf7ae-86c7-4a8c-bbe6-4b9d1ad0c7a0 |
| Jogador 7 | 5-3 | 266 | BUY | STABILIZE | 28.0 | 6 | 115 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.884125292301178 | 0.0 | 0.0 | +960df220-42b3-42b0-ab7e-d89acfd2b46c / -— |
| Jogador 7 | 5-3 | 267 | REROLL | STABILIZE | 28.0 | 6 | 113 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.07152002304792404 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 268 | REROLL | STABILIZE | 28.0 | 6 | 111 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.03652002289891243 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 269 | REROLL | STABILIZE | 28.0 | 6 | 109 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.052686192095279694 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-3 | 270 | SELL | STABILIZE | 28.0 | 6 | 107 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.02476923167705536 | 0.0 | 0.0 | +— / -673bda2e-1343-4894-8005-c3ee2c90f1b7 |
| Jogador 7 | 5-4 | 272 | BUY | ALL_IN | 13.0 | 6 | 122 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.4309826195240021 | 0.0 | 0.0 | +e62f734a-7d31-4689-9534-78bedd338a6d / -— |
| Jogador 7 | 5-4 | 273 | REROLL | ALL_IN | 13.0 | 6 | 118 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.02574542723596096 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 274 | REROLL | ALL_IN | 13.0 | 6 | 116 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.06438698619604111 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 275 | REROLL | ALL_IN | 13.0 | 6 | 114 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09982899576425552 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 276 | REROLL | ALL_IN | 13.0 | 6 | 112 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.036186229437589645 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 277 | REROLL | ALL_IN | 13.0 | 6 | 110 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.06504553556442261 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 278 | REROLL | ALL_IN | 13.0 | 6 | 108 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05015787482261658 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 279 | REROLL | ALL_IN | 13.0 | 6 | 106 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10012274235486984 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-4 | 280 | REROLL | ALL_IN | 13.0 | 6 | 104 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09413918107748032 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 282 | REROLL | ALL_IN | 13.0 | 6 | 113 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.020585063844919205 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 283 | REROLL | ALL_IN | 13.0 | 6 | 111 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.06377893686294556 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 284 | REROLL | ALL_IN | 13.0 | 6 | 109 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09969375282526016 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 285 | REROLL | ALL_IN | 13.0 | 6 | 107 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.0031591926235705614 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 286 | REROLL | ALL_IN | 13.0 | 6 | 105 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.06512992829084396 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 287 | REROLL | ALL_IN | 13.0 | 6 | 103 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.05840323492884636 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 288 | REROLL | ALL_IN | 13.0 | 6 | 101 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.10009817034006119 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 289 | REROLL | ALL_IN | 13.0 | 6 | 99 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.09967976808547974 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-5 | 290 | REROLL | ALL_IN | 13.0 | 6 | 97 | 5 | 38.0 | Fera do Rift/DA_KogMaw18_AD | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | 0.06513320654630661 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-6 | 292 | PASS | ALL_IN | 0.0 | 6 | 95 | 5 | 0.0 | Fera do Rift/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 5-7 | 302 | PASS | ALL_IN | 0.0 | 6 | 95 | 5 | 0.0 | Fera do Rift/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-1 | 312 | PASS | ALL_IN | 0.0 | 6 | 95 | 5 | 0.0 | Fera do Rift/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-2 | 322 | PASS | ALL_IN | 0.0 | 6 | 95 | 5 | 0.0 | Fera do Rift/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-3 | 332 | PASS | ALL_IN | 0.0 | 6 | 95 | 5 | 0.0 | Fera do Rift/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-4 | 342 | PASS | ALL_IN | 0.0 | 6 | 95 | 5 | 0.0 | Fera do Rift/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-5 | 352 | PASS | ALL_IN | 0.0 | 6 | 95 | 5 | 0.0 | Fera do Rift/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-6 | 362 | PASS | ALL_IN | 0.0 | 6 | 95 | 5 | 0.0 | Fera do Rift/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 6-7 | 372 | PASS | ALL_IN | 0.0 | 6 | 95 | 5 | 0.0 | Fera do Rift/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 7-1 | 382 | PASS | ALL_IN | 0.0 | 6 | 95 | 5 | 0.0 | Fera do Rift/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 7-2 | 392 | PASS | ALL_IN | 0.0 | 6 | 95 | 5 | 0.0 | Fera do Rift/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 7 | 7-3 | 402 | PASS | ALL_IN | 0.0 | 6 | 95 | 5 | 0.0 | Fera do Rift/DA_KogMaw18_AD | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 1 | MOVE_BENCH | ECON | 100.0 | 2 | 0 | 0 | 0.0 | —/— | MOVE_BENCH, SELL, PASS | True | True | 0.5824994444847107 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 2 | MOVE_BOARD | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.13061420619487762 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-1 | 3 | PASS | STABILIZE | 100.0 | 2 | 0 | 0 | 2.0 | —/DA_18_Rakan | MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 11 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.00949109811335802 | 0.0 | 0.0 | +64afe66e-d5a9-466c-a4ff-9d32c9f153ce / -— |
| Jogador 8 | 1-2 | 12 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22278070449829102 | 0.0 | 0.0 | +— / -64afe66e-d5a9-466c-a4ff-9d32c9f153ce |
| Jogador 8 | 1-2 | 13 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.05369825288653374 | 0.0 | 0.0 | +47feb452-27a0-43f6-983f-ea1674f17ab8 / -— |
| Jogador 8 | 1-2 | 14 | SELL | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.21128375828266144 | 0.0 | 0.0 | +— / -47feb452-27a0-43f6-983f-ea1674f17ab8 |
| Jogador 8 | 1-2 | 15 | BUY | STABILIZE | 100.0 | 3 | 2 | 0 | 2.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | -0.057432711124420166 | 0.0 | 0.0 | +fddba3f3-87f3-4c97-a7b2-e5d1ef789709 / -— |
| Jogador 8 | 1-2 | 16 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 1 | 0 | 2.0 | —/DA_18_Rakan | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.11924687772989273 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 17 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 18 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.0849403440952301 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-2 | 19 | PASS | STABILIZE | 100.0 | 3 | 1 | 0 | 4.0 | —/DA_18_Rakan | BUY, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 21 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.37918275594711304 | 0.0 | 0.0 | +74c2d7f0-8d5d-460e-88fc-5407b717144a / -— |
| Jogador 8 | 1-3 | 22 | SELL | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.429182767868042 | 0.0 | 0.0 | +— / -74c2d7f0-8d5d-460e-88fc-5407b717144a |
| Jogador 8 | 1-3 | 23 | BUY | STABILIZE | 100.0 | 3 | 3 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.37864211201667786 | 0.0 | 0.0 | +a349fd40-8d8c-4de8-9ff0-b3263fd120bc / -— |
| Jogador 8 | 1-3 | 24 | MOVE_BENCH | STABILIZE | 100.0 | 3 | 2 | 0 | 4.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.49908143281936646 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 25 | MOVE_BOARD | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Rakan | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.024840479716658592 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-3 | 26 | PASS | STABILIZE | 100.0 | 3 | 2 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 1-4 | 31 | BUY | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9496492743492126 | 0.0 | 0.0 | +64f24363-3325-4538-972e-a6d8260b3787 / -— |
| Jogador 8 | 1-4 | 32 | SELL | STABILIZE | 100.0 | 3 | 4 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.9996492862701416 | 0.0 | 0.0 | +— / -64f24363-3325-4538-972e-a6d8260b3787 |
| Jogador 8 | 1-4 | 33 | PASS | STABILIZE | 100.0 | 3 | 5 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 41 | BUY | STABILIZE | 100.0 | 4 | 9 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.9521782994270325 | 0.0 | 0.0 | +630d9254-3856-4d88-b981-43a8270b4b3d / -— |
| Jogador 8 | 2-1 | 42 | MOVE_BENCH | STABILIZE | 100.0 | 4 | 8 | 0 | 6.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.06028486788272858 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 43 | MOVE_BOARD | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-1 | 44 | PASS | STABILIZE | 100.0 | 4 | 8 | 0 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 50 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 13 | 1 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 51 | MOVE_BOARD | STABILIZE | 94.0 | 4 | 13 | 1 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-2 | 52 | PASS | STABILIZE | 94.0 | 4 | 13 | 1 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 60 | MOVE_BOARD | STABILIZE | 88.0 | 4 | 20 | 2 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.009366531856358051 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 61 | MOVE_BOARD | STABILIZE | 88.0 | 4 | 20 | 2 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 62 | MOVE_BOARD | STABILIZE | 88.0 | 4 | 20 | 2 | 8.0 | —/DA_18_Rakan | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-3 | 63 | PASS | STABILIZE | 88.0 | 4 | 20 | 2 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 70 | BUY | LOSS_STREAK | 84.0 | 4 | 28 | 2 | 8.0 | —/DA_18_Yorick | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.15762493014335632 | 0.0 | 0.0 | +492fa74a-22b8-4f7d-a4f9-346fdcf565be / -— |
| Jogador 8 | 2-4 | 71 | MOVE_BENCH | LOSS_STREAK | 84.0 | 4 | 25 | 2 | 8.0 | —/DA_18_KhaZix | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.10160063952207565 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 72 | SELL | LOSS_STREAK | 84.0 | 4 | 25 | 2 | 12.0 | —/DA_18_KhaZix | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.36986759305000305 | 0.0 | 0.0 | +— / -fddba3f3-87f3-4c97-a7b2-e5d1ef789709 |
| Jogador 8 | 2-4 | 73 | MOVE_BOARD | LOSS_STREAK | 84.0 | 4 | 26 | 2 | 12.0 | —/DA_18_KhaZix | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | -0.10000000149011612 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 74 | MOVE_BOARD | LOSS_STREAK | 84.0 | 4 | 26 | 2 | 12.0 | —/DA_18_KhaZix | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.03994898498058319 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-4 | 75 | PASS | LOSS_STREAK | 84.0 | 4 | 26 | 2 | 12.0 | —/DA_18_KhaZix | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 80 | BUY | LOSS_STREAK | 84.0 | 4 | 34 | 3 | 12.0 | —/DA_18_KhaZix | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.27473387122154236 | 0.0 | 0.0 | +07ecc7d0-150a-4bf9-8c9d-dc15bdd854b0 / -— |
| Jogador 8 | 2-5 | 81 | MOVE_BENCH | LOSS_STREAK | 84.0 | 4 | 31 | 3 | 12.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.01025717705488205 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 82 | MOVE_BENCH | STABILIZE | 84.0 | 4 | 31 | 3 | 12.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2579984664916992 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 83 | SELL | STABILIZE | 84.0 | 4 | 31 | 3 | 16.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34707918763160706 | 0.0 | 0.0 | +— / -630d9254-3856-4d88-b981-43a8270b4b3d |
| Jogador 8 | 2-5 | 84 | BUY | STABILIZE | 84.0 | 4 | 32 | 3 | 16.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BOARD, PASS | True | True | 0.4802725911140442 | 0.0 | 0.0 | +0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb / -— |
| Jogador 8 | 2-5 | 85 | MOVE_BENCH | STABILIZE | 84.0 | 4 | 30 | 3 | 16.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04713040217757225 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 86 | MOVE_BENCH | STABILIZE | 84.0 | 4 | 30 | 3 | 14.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7163372039794922 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-5 | 87 | MOVE_BENCH | STABILIZE | 84.0 | 4 | 30 | 3 | 14.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.320454865694046 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 89 | BUY | STABILIZE | 84.0 | 5 | 39 | 3 | 16.0 | Colosso/DA_18_Rammus | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.34926122426986694 | 0.0 | 0.0 | +432bc6b0-03a8-42f3-a147-d165f4172a8f / -— |
| Jogador 8 | 2-6 | 90 | BUY | STABILIZE | 84.0 | 5 | 36 | 3 | 16.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.33751603960990906 | 0.0 | 0.0 | +e2f28d51-690c-476e-b097-e5c69258f933 / -— |
| Jogador 8 | 2-6 | 91 | BUY | STABILIZE | 84.0 | 5 | 33 | 3 | 16.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.9967538714408875 | 0.0 | 0.0 | +bca8862c-5e5b-4a51-9173-79218fbfea3d / -— |
| Jogador 8 | 2-6 | 92 | MOVE_BENCH | SLOWROLL | 84.0 | 5 | 32 | 3 | 16.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3775271773338318 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 93 | REROLL | SLOWROLL | 84.0 | 5 | 32 | 3 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.058710724115371704 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-6 | 94 | BUY | SLOWROLL | 84.0 | 5 | 30 | 3 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8293906450271606 | 0.0 | 0.0 | +764470bb-9820-4e49-98f9-5a5f0ce5ca8f / -— |
| Jogador 8 | 2-6 | 95 | BUY | STABILIZE | 84.0 | 5 | 27 | 2 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4375511407852173 | 0.0 | 0.0 | +3d4fca52-8f58-4464-8cec-752fa99dbb3c / -— |
| Jogador 8 | 2-6 | 96 | BUY | STABILIZE | 84.0 | 5 | 24 | 2 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.3747929632663727 | 0.0 | 0.0 | +53a27943-148b-4522-9826-3f2e0b8a7858 / -— |
| Jogador 8 | 2-7 | 98 | BUY | SLOWROLL | 76.0 | 5 | 30 | 3 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09964536875486374 | 0.0 | 0.0 | +cf421cf5-8e22-4dd1-8aa5-5cb3bda86c88 / -— |
| Jogador 8 | 2-7 | 99 | BUY | STABILIZE | 76.0 | 5 | 26 | 2 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.17335225641727448 | 0.0 | 0.0 | +74fe48c1-d955-4b0d-b832-39d4c86049dc / -— |
| Jogador 8 | 2-7 | 100 | REROLL | STABILIZE | 76.0 | 5 | 24 | 2 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 101 | BUY | STABILIZE | 76.0 | 5 | 22 | 2 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2827593684196472 | 0.0 | 0.0 | +79ed9815-7667-4e50-86a3-420599ce8c79 / -— |
| Jogador 8 | 2-7 | 102 | SELL | STABILIZE | 76.0 | 5 | 18 | 1 | 22.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.09663597494363785 | 0.0 | 0.0 | +— / -74fe48c1-d955-4b0d-b832-39d4c86049dc |
| Jogador 8 | 2-7 | 103 | BUY | STABILIZE | 76.0 | 5 | 20 | 2 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.07925202697515488 | 0.0 | 0.0 | +ae9f0b1e-4654-43eb-ae65-4f16dff93765 / -— |
| Jogador 8 | 2-7 | 104 | REROLL | STABILIZE | 76.0 | 5 | 18 | 1 | 22.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 2-7 | 105 | SELL | STABILIZE | 76.0 | 5 | 16 | 1 | 22.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30343198776245117 | 0.0 | 0.0 | +— / -53a27943-148b-4522-9826-3f2e0b8a7858 |
| Jogador 8 | 3-1 | 107 | BUY | STABILIZE | 76.0 | 5 | 23 | 2 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.13974179327487946 | 0.0 | 0.0 | +9204a42c-6310-4b08-9bc7-8a2e786b077a / -— |
| Jogador 8 | 3-1 | 108 | SELL | STABILIZE | 76.0 | 5 | 20 | 2 | 22.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.016105998307466507 | 0.0 | 0.0 | +— / -9204a42c-6310-4b08-9bc7-8a2e786b077a |
| Jogador 8 | 3-1 | 109 | BUY | STABILIZE | 76.0 | 5 | 23 | 2 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.26749563217163086 | 0.0 | 0.0 | +e29364db-c484-4e4d-954d-7f4940131ffc / -— |
| Jogador 8 | 3-1 | 110 | REROLL | STABILIZE | 76.0 | 5 | 21 | 2 | 22.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17900000512599945 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 111 | SELL | STABILIZE | 76.0 | 5 | 19 | 1 | 22.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06261538714170456 | 0.0 | 0.0 | +— / -e29364db-c484-4e4d-954d-7f4940131ffc |
| Jogador 8 | 3-1 | 112 | BUY | STABILIZE | 76.0 | 5 | 21 | 2 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.34171998500823975 | 0.0 | 0.0 | +655deca9-2d3f-4e88-827a-5f49da8f3451 / -— |
| Jogador 8 | 3-1 | 113 | REROLL | STABILIZE | 76.0 | 5 | 18 | 1 | 22.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-1 | 114 | SELL | STABILIZE | 76.0 | 5 | 16 | 1 | 22.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0560000017285347 | 0.0 | 0.0 | +— / -655deca9-2d3f-4e88-827a-5f49da8f3451 |
| Jogador 8 | 3-2 | 116 | BUY | STABILIZE | 76.0 | 5 | 27 | 2 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04487994313240051 | 0.0 | 0.0 | +7a60e1b2-fc20-4070-b163-2f9fb6f93264 / -— |
| Jogador 8 | 3-2 | 117 | REROLL | STABILIZE | 76.0 | 5 | 25 | 2 | 22.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 118 | SELL | STABILIZE | 76.0 | 5 | 23 | 2 | 22.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02040529064834118 | 0.0 | 0.0 | +— / -7a60e1b2-fc20-4070-b163-2f9fb6f93264 |
| Jogador 8 | 3-2 | 119 | BUY | STABILIZE | 76.0 | 5 | 25 | 2 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.06342106312513351 | 0.0 | 0.0 | +f5c14a50-b095-4a36-995f-2a8514e46f1c / -— |
| Jogador 8 | 3-2 | 120 | REROLL | STABILIZE | 76.0 | 5 | 22 | 2 | 22.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-2 | 121 | SELL | STABILIZE | 76.0 | 5 | 20 | 2 | 22.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.029846154153347015 | 0.0 | 0.0 | +— / -f5c14a50-b095-4a36-995f-2a8514e46f1c |
| Jogador 8 | 3-2 | 122 | BUY | STABILIZE | 76.0 | 5 | 23 | 2 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7501251101493835 | 0.0 | 0.0 | +86c1ac55-598e-426a-86ea-64249f82b085 / -— |
| Jogador 8 | 3-2 | 123 | SELL | STABILIZE | 76.0 | 5 | 20 | 2 | 22.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.698505163192749 | 0.0 | 0.0 | +— / -bca8862c-5e5b-4a51-9173-79218fbfea3d |
| Jogador 8 | 3-3 | 125 | BUY | STABILIZE | 66.0 | 5 | 28 | 2 | 22.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8489024639129639 | 0.0 | 0.0 | +23157bd6-5e8f-4416-bb7f-2e5d71a06543 / -432bc6b0-03a8-42f3-a147-d165f4172a8f,764470bb-9820-4e49-98f9-5a5f0ce5ca8f |
| Jogador 8 | 3-3 | 126 | BUY | STABILIZE | 66.0 | 5 | 25 | 2 | 16.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7459341287612915 | 0.0 | 0.0 | +8fb80cc8-4120-41a0-bc96-35f81a466ed9 / -— |
| Jogador 8 | 3-3 | 127 | SELL | STABILIZE | 66.0 | 5 | 22 | 2 | 16.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.057384613901376724 | 0.0 | 0.0 | +— / -79ed9815-7667-4e50-86a3-420599ce8c79 |
| Jogador 8 | 3-3 | 128 | BUY | STABILIZE | 66.0 | 5 | 26 | 2 | 16.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7607893347740173 | 0.0 | 0.0 | +63304cf5-4aa7-473e-9bfb-ec04cd68ebbd / -— |
| Jogador 8 | 3-3 | 129 | REROLL | STABILIZE | 66.0 | 5 | 25 | 2 | 16.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-3 | 130 | SELL | STABILIZE | 66.0 | 5 | 23 | 2 | 16.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.7124364972114563 | 0.0 | 0.0 | +— / -63304cf5-4aa7-473e-9bfb-ec04cd68ebbd |
| Jogador 8 | 3-3 | 131 | BUY | STABILIZE | 66.0 | 5 | 24 | 2 | 16.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.29056766629219055 | 0.0 | 0.0 | +05be69ba-41c7-4dee-9799-dabbd60f0dc9 / -— |
| Jogador 8 | 3-3 | 132 | MOVE_BENCH | STABILIZE | 66.0 | 5 | 21 | 2 | 16.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.4405597448348999 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 134 | BUY | STABILIZE | 56.0 | 5 | 29 | 2 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26203200221061707 | 0.0 | 0.0 | +23793b7b-2dab-48f0-a8ba-db85fc14c1c5 / -— |
| Jogador 8 | 3-4 | 135 | REROLL | STABILIZE | 56.0 | 5 | 27 | 2 | 20.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 136 | REROLL | STABILIZE | 56.0 | 5 | 25 | 2 | 20.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 137 | REROLL | STABILIZE | 56.0 | 5 | 23 | 2 | 20.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 138 | SELL | STABILIZE | 56.0 | 5 | 21 | 2 | 20.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.05400000140070915 | 0.0 | 0.0 | +— / -23793b7b-2dab-48f0-a8ba-db85fc14c1c5 |
| Jogador 8 | 3-4 | 139 | BUY | STABILIZE | 56.0 | 5 | 23 | 2 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8487001657485962 | 0.0 | 0.0 | +579b987a-fedf-45d8-92fc-634a041d3d4f / -3d4fca52-8f58-4464-8cec-752fa99dbb3c,86c1ac55-598e-426a-86ea-64249f82b085 |
| Jogador 8 | 3-4 | 140 | REROLL | STABILIZE | 56.0 | 5 | 20 | 2 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17900000512599945 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-4 | 141 | REROLL | STABILIZE | 56.0 | 5 | 18 | 1 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 143 | REROLL | STABILIZE | 56.0 | 5 | 23 | 2 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 144 | BUY | STABILIZE | 56.0 | 5 | 21 | 2 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.21324394643306732 | 0.0 | 0.0 | +d1bc6c5b-74a5-46db-b00f-e91265546f5d / -— |
| Jogador 8 | 3-5 | 145 | REROLL | STABILIZE | 56.0 | 5 | 19 | 1 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 146 | REROLL | STABILIZE | 56.0 | 5 | 17 | 1 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 147 | REROLL | STABILIZE | 56.0 | 5 | 15 | 1 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 148 | REROLL | STABILIZE | 56.0 | 5 | 13 | 1 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 149 | REROLL | STABILIZE | 56.0 | 5 | 11 | 1 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17900000512599945 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-5 | 150 | REROLL | STABILIZE | 56.0 | 5 | 9 | 0 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 152 | REROLL | STABILIZE | 46.0 | 5 | 13 | 1 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 153 | REROLL | STABILIZE | 46.0 | 5 | 11 | 1 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.17900000512599945 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 154 | REROLL | STABILIZE | 46.0 | 5 | 9 | 0 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 155 | REROLL | STABILIZE | 46.0 | 5 | 7 | 0 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 156 | REROLL | STABILIZE | 46.0 | 5 | 5 | 0 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 157 | REROLL | STABILIZE | 46.0 | 5 | 3 | 0 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-6 | 158 | PASS | STABILIZE | 46.0 | 5 | 1 | 0 | 20.0 | Colosso/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 162 | REROLL | STABILIZE | 46.0 | 5 | 7 | 0 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 163 | REROLL | STABILIZE | 46.0 | 5 | 5 | 0 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 164 | REROLL | STABILIZE | 46.0 | 5 | 3 | 0 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.08399999886751175 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 3-7 | 165 | PASS | STABILIZE | 46.0 | 5 | 1 | 0 | 20.0 | Colosso/DA_18_Tristana | BUY, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 172 | REROLL | STABILIZE | 46.0 | 5 | 6 | 0 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 173 | REROLL | STABILIZE | 46.0 | 5 | 4 | 0 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 174 | REROLL | STABILIZE | 46.0 | 5 | 2 | 0 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | True | -0.0989999994635582 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 175 | CRAFT_AND_EQUIP | STABILIZE | 46.0 | 5 | 0 | 0 | 20.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS, CRAFT_AND_EQUIP | True | — | 0.08763276040554047 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-1 | 176 | PASS | STABILIZE | 46.0 | 5 | 0 | 0 | 20.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 182 | BUY | STABILIZE | 35.0 | 6 | 5 | 0 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.10902514308691025 | 0.0 | 0.0 | +a10be0a5-aca9-4c6f-bb3d-c98b5b99d431 / -— |
| Jogador 8 | 4-2 | 183 | SELL | STABILIZE | 35.0 | 6 | 1 | 0 | 20.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02138461545109749 | 0.0 | 0.0 | +— / -ae9f0b1e-4654-43eb-ae65-4f16dff93765 |
| Jogador 8 | 4-2 | 184 | BUY | STABILIZE | 35.0 | 6 | 3 | 0 | 20.0 | Colosso/DA_18_Tristana | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.74784255027771 | 0.0 | 0.0 | +a2af07ad-0ed1-489f-ab19-506b76647e17 / -— |
| Jogador 8 | 4-2 | 185 | REROLL | STABILIZE | 35.0 | 6 | 2 | 0 | 20.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 186 | PASS | STABILIZE | 35.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-2 | 190 | MOVE_BENCH | STABILIZE | 35.0 | 6 | 0 | 0 | 20.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6815181970596313 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 192 | BUY | STABILIZE | 35.0 | 6 | 6 | 0 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.2296648621559143 | 0.0 | 0.0 | +1fda1dc3-4a4f-4822-987f-a89da298605a / -— |
| Jogador 8 | 4-3 | 193 | REROLL | STABILIZE | 35.0 | 6 | 3 | 0 | 32.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-3 | 194 | SELL | STABILIZE | 35.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03723077103495598 | 0.0 | 0.0 | +— / -1fda1dc3-4a4f-4822-987f-a89da298605a |
| Jogador 8 | 4-3 | 195 | BUY | STABILIZE | 35.0 | 6 | 4 | 0 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.547721803188324 | 0.0 | 0.0 | +2e405015-7d97-4346-83bd-ca0773c613f2 / -— |
| Jogador 8 | 4-3 | 196 | PASS | STABILIZE | 35.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 202 | SELL | STABILIZE | 24.0 | 6 | 6 | 0 | 32.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.3017688989639282 | 0.0 | 0.0 | +— / -2e405015-7d97-4346-83bd-ca0773c613f2 |
| Jogador 8 | 4-4 | 203 | BUY | STABILIZE | 24.0 | 6 | 9 | 0 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.5475311279296875 | 0.0 | 0.0 | +02e6980b-3072-4687-a3f2-1810c231ae99 / -— |
| Jogador 8 | 4-4 | 204 | REROLL | STABILIZE | 24.0 | 6 | 6 | 0 | 32.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03230740502476692 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 205 | REROLL | STABILIZE | 24.0 | 6 | 4 | 0 | 32.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010692596435546875 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-4 | 206 | SELL | STABILIZE | 24.0 | 6 | 2 | 0 | 32.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.005230769049376249 | 0.0 | 0.0 | +— / -05be69ba-41c7-4dee-9799-dabbd60f0dc9 |
| Jogador 8 | 4-4 | 207 | BUY | STABILIZE | 24.0 | 6 | 5 | 0 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27996131777763367 | 0.0 | 0.0 | +e8618b3e-5d21-4e4a-b5cf-9c00959cc688 / -— |
| Jogador 8 | 4-4 | 208 | SELL | STABILIZE | 24.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.30176669359207153 | 0.0 | 0.0 | +— / -02e6980b-3072-4687-a3f2-1810c231ae99 |
| Jogador 8 | 4-4 | 209 | BUY | STABILIZE | 24.0 | 6 | 4 | 0 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22192566096782684 | 0.0 | 0.0 | +50f41c93-cec1-4dc1-b5d2-c29d744fec9c / -— |
| Jogador 8 | 4-4 | 210 | SELL | STABILIZE | 24.0 | 6 | 0 | 0 | 32.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.032769229263067245 | 0.0 | 0.0 | +— / -a10be0a5-aca9-4c6f-bb3d-c98b5b99d431 |
| Jogador 8 | 4-5 | 212 | BUY | STABILIZE | 24.0 | 6 | 9 | 0 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8314003944396973 | 0.0 | 0.0 | +a5573a7e-ab6f-485d-8da6-654a9c820871 / -8fb80cc8-4120-41a0-bc96-35f81a466ed9,e2f28d51-690c-476e-b097-e5c69258f933 |
| Jogador 8 | 4-5 | 213 | BUY | STABILIZE | 24.0 | 6 | 6 | 0 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.007246579043567181 | 0.0 | 0.0 | +61ebc6c6-fe85-456a-b9b6-458d4720fd48 / -— |
| Jogador 8 | 4-5 | 214 | BUY | STABILIZE | 24.0 | 6 | 4 | 0 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.23496916890144348 | 0.0 | 0.0 | +5be4c98b-88ed-4c40-a801-9ba4483f0639 / -— |
| Jogador 8 | 4-5 | 215 | REROLL | STABILIZE | 24.0 | 6 | 2 | 0 | 32.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-5 | 216 | PASS | STABILIZE | 24.0 | 6 | 0 | 0 | 32.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 222 | REROLL | ALL_IN | 12.0 | 6 | 6 | 0 | 32.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010219160467386246 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 223 | SELL | ALL_IN | 12.0 | 6 | 4 | 0 | 32.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04723076894879341 | 0.0 | 0.0 | +— / -5be4c98b-88ed-4c40-a801-9ba4483f0639 |
| Jogador 8 | 4-6 | 224 | BUY | ALL_IN | 12.0 | 6 | 6 | 0 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.729874849319458 | 0.0 | 0.0 | +349ea3e0-4bb8-454e-bdaa-bc3fbeb02a0b / -— |
| Jogador 8 | 4-6 | 225 | REROLL | ALL_IN | 12.0 | 6 | 2 | 0 | 32.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-6 | 226 | PASS | ALL_IN | 12.0 | 6 | 0 | 0 | 32.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 232 | REROLL | ALL_IN | 12.0 | 6 | 6 | 0 | 32.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01026829518377781 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 233 | REROLL | ALL_IN | 12.0 | 6 | 4 | 0 | 32.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03276124969124794 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 234 | REROLL | ALL_IN | 12.0 | 6 | 2 | 0 | 32.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 4-7 | 235 | PASS | ALL_IN | 12.0 | 6 | 0 | 0 | 32.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 242 | EQUIP_FROM_INVENTORY | ALL_IN | 12.0 | 6 | 5 | 0 | 32.0 | Colosso/DA_18_Tristana | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 243 | SELL | ALL_IN | 12.0 | 6 | 5 | 0 | 32.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03676922991871834 | 0.0 | 0.0 | +— / -61ebc6c6-fe85-456a-b9b6-458d4720fd48 |
| Jogador 8 | 5-1 | 244 | BUY | ALL_IN | 12.0 | 6 | 7 | 0 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7334067821502686 | 0.0 | 0.0 | +a1848184-da18-4e8e-b7a5-41cde2673904 / -— |
| Jogador 8 | 5-1 | 245 | REROLL | ALL_IN | 12.0 | 6 | 5 | 0 | 32.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01021484937518835 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 246 | SELL | ALL_IN | 12.0 | 6 | 3 | 0 | 32.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03769230842590332 | 0.0 | 0.0 | +— / -50f41c93-cec1-4dc1-b5d2-c29d744fec9c |
| Jogador 8 | 5-1 | 247 | BUY | ALL_IN | 12.0 | 6 | 7 | 0 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.00445748632773757 | 0.0 | 0.0 | +0cf34e7c-4d2b-46ca-a202-d84310c906c5 / -— |
| Jogador 8 | 5-1 | 248 | REROLL | ALL_IN | 12.0 | 6 | 3 | 0 | 32.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-1 | 249 | SELL | ALL_IN | 12.0 | 6 | 1 | 0 | 32.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03769230842590332 | 0.0 | 0.0 | +— / -0cf34e7c-4d2b-46ca-a202-d84310c906c5 |
| Jogador 8 | 5-1 | 250 | BUY | ALL_IN | 12.0 | 6 | 5 | 0 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7311510443687439 | 0.0 | 0.0 | +02a24cad-0b52-4e01-a7d0-23c2e113a401 / -— |
| Jogador 8 | 5-2 | 252 | SELL | ALL_IN | 12.0 | 6 | 10 | 1 | 32.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.006125841289758682 | 0.0 | 0.0 | +— / -cf421cf5-8e22-4dd1-8aa5-5cb3bda86c88 |
| Jogador 8 | 5-2 | 253 | BUY | ALL_IN | 12.0 | 6 | 14 | 1 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.8248785138130188 | 0.0 | 0.0 | +c316c846-85b4-4436-b3d1-b3d96b0b68aa / -0ecbbc00-30d3-4043-bbf7-dd03a80ec3eb,a1848184-da18-4e8e-b7a5-41cde2673904 |
| Jogador 8 | 5-2 | 254 | BUY | ALL_IN | 12.0 | 6 | 12 | 1 | 28.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.22743454575538635 | 0.0 | 0.0 | +546abd27-1523-4416-bc79-500b2b3a404e / -— |
| Jogador 8 | 5-2 | 255 | REROLL | ALL_IN | 12.0 | 6 | 8 | 0 | 28.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.030447842553257942 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 256 | REROLL | ALL_IN | 12.0 | 6 | 6 | 0 | 28.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.01296411082148552 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 257 | SELL | ALL_IN | 12.0 | 6 | 4 | 0 | 28.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.032769229263067245 | 0.0 | 0.0 | +— / -546abd27-1523-4416-bc79-500b2b3a404e |
| Jogador 8 | 5-2 | 258 | BUY | ALL_IN | 12.0 | 6 | 8 | 0 | 28.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.31635409593582153 | 0.0 | 0.0 | +34b959ad-0aed-4a33-b3d4-de76927f8592 / -— |
| Jogador 8 | 5-2 | 259 | REROLL | ALL_IN | 12.0 | 6 | 5 | 0 | 28.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010202515870332718 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-2 | 260 | MOVE_BENCH | ALL_IN | 12.0 | 6 | 3 | 0 | 28.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.512845516204834 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 262 | BUY | ALL_IN | 12.0 | 6 | 10 | 1 | 32.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7448402047157288 | 0.0 | 0.0 | +dae5841a-89a1-4244-8e90-0a16aa25a8bd / -02a24cad-0b52-4e01-a7d0-23c2e113a401,d1bc6c5b-74a5-46db-b00f-e91265546f5d |
| Jogador 8 | 5-3 | 263 | BUY | ALL_IN | 12.0 | 6 | 8 | 0 | 28.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03172629326581955 | 0.0 | 0.0 | +36515a99-9447-4e75-b211-b884be4256e9 / -— |
| Jogador 8 | 5-3 | 264 | REROLL | ALL_IN | 12.0 | 6 | 5 | 0 | 28.0 | Colosso/DA_18_Tristana | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010202527977526188 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 265 | SELL | ALL_IN | 12.0 | 6 | 3 | 0 | 28.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.03723077103495598 | 0.0 | 0.0 | +— / -36515a99-9447-4e75-b211-b884be4256e9 |
| Jogador 8 | 5-3 | 266 | BUY | ALL_IN | 12.0 | 6 | 6 | 0 | 28.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27399003505706787 | 0.0 | 0.0 | +fac7104c-0b60-4291-b463-851e0cc58503 / -— |
| Jogador 8 | 5-3 | 267 | REROLL | ALL_IN | 12.0 | 6 | 3 | 0 | 28.0 | Colosso/DA_18_Tristana | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03135591372847557 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-3 | 268 | SELL | ALL_IN | 12.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.26972660422325134 | 0.0 | 0.0 | +— / -34b959ad-0aed-4a33-b3d4-de76927f8592 |
| Jogador 8 | 5-3 | 269 | BUY | ALL_IN | 12.0 | 6 | 4 | 0 | 28.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.059785060584545135 | 0.0 | 0.0 | +abcbf6e6-cad5-4f9a-b870-bb410c6a78df / -— |
| Jogador 8 | 5-3 | 270 | MOVE_BENCH | ALL_IN | 12.0 | 6 | 1 | 0 | 28.0 | Colosso/DA_18_Tristana | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.6368476748466492 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 272 | BUY | ALL_IN | 12.0 | 6 | 7 | 0 | 36.0 | Colosso/DA_18_Tristana | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7339732646942139 | 0.0 | 0.0 | +fe5fb2f1-bb03-4522-97d5-082e04d87549 / -— |
| Jogador 8 | 5-4 | 273 | REROLL | ALL_IN | 12.0 | 6 | 4 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 274 | REROLL | ALL_IN | 12.0 | 6 | 2 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-4 | 275 | PASS | ALL_IN | 12.0 | 6 | 0 | 0 | 36.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 282 | REROLL | ALL_IN | 12.0 | 6 | 6 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010207836516201496 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 283 | SELL | ALL_IN | 12.0 | 6 | 4 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.04289808124303818 | 0.0 | 0.0 | +— / -abcbf6e6-cad5-4f9a-b870-bb410c6a78df |
| Jogador 8 | 5-5 | 284 | BUY | ALL_IN | 12.0 | 6 | 7 | 0 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.27545610070228577 | 0.0 | 0.0 | +c550b17d-57ad-4c47-b873-bd6124600cef / -— |
| Jogador 8 | 5-5 | 285 | REROLL | ALL_IN | 12.0 | 6 | 5 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010933256708085537 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 286 | REROLL | ALL_IN | 12.0 | 6 | 3 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.0327974334359169 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-5 | 287 | SELL | ALL_IN | 12.0 | 6 | 1 | 0 | 36.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.6846153736114502 | 0.0 | 0.0 | +— / -a2af07ad-0ed1-489f-ab19-506b76647e17 |
| Jogador 8 | 5-5 | 288 | BUY | ALL_IN | 12.0 | 6 | 2 | 0 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.005016335751861334 | 0.0 | 0.0 | +1c15cf96-6fae-4edf-989b-76cd532cf682 / -— |
| Jogador 8 | 5-5 | 289 | PASS | ALL_IN | 12.0 | 6 | 0 | 0 | 36.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 292 | REROLL | ALL_IN | 12.0 | 6 | 6 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03279661387205124 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 293 | REROLL | ALL_IN | 12.0 | 6 | 4 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010202904231846333 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 294 | REROLL | ALL_IN | 12.0 | 6 | 2 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-6 | 295 | PASS | ALL_IN | 12.0 | 6 | 0 | 0 | 36.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 302 | REROLL | ALL_IN | 12.0 | 6 | 6 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010202879086136818 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 303 | SELL | ALL_IN | 12.0 | 6 | 4 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.02138461545109749 | 0.0 | 0.0 | +— / -1c15cf96-6fae-4edf-989b-76cd532cf682 |
| Jogador 8 | 5-7 | 304 | BUY | ALL_IN | 12.0 | 6 | 6 | 0 | 36.0 | Colosso/DA_Vi18 | BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | 0.7354243993759155 | 0.0 | 0.0 | +37ed07ea-4642-4a68-848f-2c239f5d8c61 / -— |
| Jogador 8 | 5-7 | 305 | REROLL | ALL_IN | 12.0 | 6 | 4 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.032680924981832504 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 306 | REROLL | ALL_IN | 12.0 | 6 | 2 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 5-7 | 307 | PASS | ALL_IN | 12.0 | 6 | 0 | 0 | 36.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 312 | EQUIP_FROM_INVENTORY | ALL_IN | 12.0 | 6 | 6 | 0 | 36.0 | Colosso/DA_Vi18 | EQUIP_FROM_INVENTORY | True | — | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 313 | EQUIP_FROM_INVENTORY | ALL_IN | 12.0 | 6 | 6 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS, EQUIP_FROM_INVENTORY | True | — | 0.07802509516477585 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 314 | REROLL | ALL_IN | 12.0 | 6 | 6 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.03279712051153183 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 315 | REROLL | ALL_IN | 12.0 | 6 | 4 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.010203064419329166 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 316 | REROLL | ALL_IN | 12.0 | 6 | 2 | 0 | 36.0 | Colosso/DA_Vi18 | REROLL, MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.028999999165534973 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-1 | 317 | PASS | ALL_IN | 12.0 | 6 | 0 | 0 | 36.0 | Colosso/DA_Vi18 | MOVE_BENCH, MOVE_BOARD, SELL, PASS | True | True | -0.05000000074505806 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-2 | 322 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Colosso/DA_Vi18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-3 | 332 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Colosso/DA_Vi18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-4 | 342 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Colosso/DA_Vi18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-5 | 352 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Colosso/DA_Vi18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-6 | 362 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Colosso/DA_Vi18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 6-7 | 372 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Colosso/DA_Vi18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 7-1 | 382 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Colosso/DA_Vi18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 7-2 | 392 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Colosso/DA_Vi18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |
| Jogador 8 | 7-3 | 402 | PASS | ALL_IN | 0.0 | 6 | 0 | 0 | 0.0 | Colosso/DA_Vi18 | PASS | True | True | 0.0 | 0.0 | 0.0 | +— / -— |

Os dados estruturados de origem preservam máscaras, diagnósticos da política, estados antes/depois, componentes de recompensa e mudanças por UUID. Campo ausente não significa zero.

## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 190 | 195 | 52 | 21 | 0 | 0 | 41 | 1 | 0 | 0.0 |
- Jogador 1 — gasto por ação: BUY: 113g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 82g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 6g, stage 2: 22g, stage 3: 97g, stage 4: 70g, stage 5: 0g, stage 6: 0g, stage 7: 0g
| Jogador 2 | 323 | 507 | 239 | 22 | 3 | 0 | 85 | 0 | 116 | 66.0 |
- Jogador 2 — gasto por ação: BUY: 325g, BUY_XP: 12g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 170g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 6g, stage 2: 37g, stage 3: 91g, stage 4: 104g, stage 5: 114g, stage 6: 107g, stage 7: 48g
| Jogador 3 | 177 | 194 | 52 | 18 | 0 | 0 | 38 | 0 | 5 | 0.0 |
- Jogador 3 — gasto por ação: BUY: 118g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 76g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 6g, stage 2: 19g, stage 3: 94g, stage 4: 75g, stage 5: 0g, stage 6: 0g, stage 7: 0g
| Jogador 4 | 218 | 221 | 71 | 15 | 0 | 0 | 42 | 0 | 0 | 0.0 |
- Jogador 4 — gasto por ação: BUY: 137g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 84g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 7g, stage 2: 46g, stage 3: 86g, stage 4: 72g, stage 5: 10g, stage 6: 0g, stage 7: 0g
| Jogador 5 | 231 | 296 | 102 | 3 | 1 | 0 | 59 | 0 | 65 | 0.0 |
- Jogador 5 — gasto por ação: BUY: 174g, BUY_XP: 4g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 118g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 8g, stage 2: 28g, stage 3: 72g, stage 4: 112g, stage 5: 76g, stage 6: 0g, stage 7: 0g
| Jogador 6 | 336 | 494 | 293 | 19 | 4 | 0 | 49 | 0 | 202 | 48.0 |
- Jogador 6 — gasto por ação: BUY: 372g, BUY_XP: 24g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 98g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 9g, stage 2: 44g, stage 3: 94g, stage 4: 100g, stage 5: 98g, stage 6: 109g, stage 7: 40g
| Jogador 7 | 229 | 277 | 119 | 5 | 1 | 1 | 40 | 0 | 95 | 0.0 |
- Jogador 7 — gasto por ação: BUY: 185g, BUY_XP: 12g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 80g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 8g, stage 2: 16g, stage 3: 79g, stage 4: 95g, stage 5: 79g, stage 6: 0g, stage 7: 0g
| Jogador 8 | 216 | 270 | 80 | 12 | 0 | 0 | 63 | 10 | 0 | 0.0 |
- Jogador 8 — gasto por ação: BUY: 144g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 126g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 6g, stage 2: 41g, stage 3: 85g, stage 4: 59g, stage 5: 73g, stage 6: 6g, stage 7: 0g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 2 | 2 | 0 | 0.0% |
| Jogador 2 | 2 | 2 | 0 | 0.0% |
| Jogador 3 | 4 | 1 | 3 | 75.0% |
| Jogador 4 | 3 | 3 | 0 | 0.0% |
| Jogador 5 | 2 | 2 | 0 | 0.0% |
| Jogador 6 | 1 | 1 | 0 | 0.0% |
| Jogador 7 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 1 | 1 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ médio qualidade | Estrutural médio | Δ estrutural médio | Posicional médio | Δ qualidade combate + | Δ qualidade combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 190 | 0 | 0 | 190 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ 0.0000 (47 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (28 ações), MOVE_BOARD: Δ 0.0000 (28 ações), PASS: Δ 0.0000 (28 ações), REROLL: Δ 0.0000 (41 ações), SELL: Δ 0.0000 (17 ações)
| Jogador 2 | 323 | 0 | 0 | 323 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ 0.0000 (111 ações), BUY_XP: Δ 0.0000 (3 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (6 ações), MOVE_BENCH: Δ 0.0000 (23 ações), MOVE_BOARD: Δ 0.0000 (10 ações), PASS: Δ 0.0000 (11 ações), REROLL: Δ 0.0000 (85 ações), SELL: Δ 0.0000 (74 ações)
| Jogador 3 | 177 | 0 | 0 | 177 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ 0.0000 (46 ações), MOVE_BENCH: Δ 0.0000 (19 ações), MOVE_BOARD: Δ 0.0000 (25 ações), PASS: Δ 0.0000 (30 ações), REROLL: Δ 0.0000 (38 ações), SELL: Δ 0.0000 (19 ações)
| Jogador 4 | 218 | 0 | 0 | 218 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ 0.0000 (64 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (24 ações), MOVE_BOARD: Δ 0.0000 (28 ações), PASS: Δ 0.0000 (23 ações), REROLL: Δ 0.0000 (42 ações), SELL: Δ 0.0000 (35 ações)
| Jogador 5 | 231 | 0 | 0 | 231 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ 0.0000 (68 ações), BUY_XP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (17 ações), MOVE_BOARD: Δ 0.0000 (23 ações), PASS: Δ 0.0000 (24 ações), REROLL: Δ 0.0000 (59 ações), SELL: Δ 0.0000 (38 ações)
| Jogador 6 | 336 | 0 | 0 | 336 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ 0.0000 (130 ações), BUY_XP: Δ 0.0000 (6 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (5 ações), MOVE_BENCH: Δ 0.0000 (28 ações), MOVE_BOARD: Δ 0.0000 (10 ações), PASS: Δ 0.0000 (10 ações), REROLL: Δ 0.0000 (49 ações), SELL: Δ 0.0000 (98 ações)
| Jogador 7 | 229 | 0 | 0 | 229 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ 0.0000 (71 ações), BUY_XP: Δ 0.0000 (3 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0000 (27 ações), MOVE_BOARD: Δ 0.0000 (19 ações), PASS: Δ 0.0000 (23 ações), REROLL: Δ 0.0000 (40 ações), SELL: Δ 0.0000 (45 ações)
| Jogador 8 | 216 | 0 | 0 | 216 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ 0.0000 (58 ações), CRAFT_AND_EQUIP: Δ 0.0000 (1 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0000 (15 ações), MOVE_BOARD: Δ 0.0000 (12 ações), PASS: Δ 0.0000 (30 ações), REROLL: Δ 0.0000 (63 ações), SELL: Δ 0.0000 (34 ações)

A pontuação é uma heurística para auditoria, não uma verdade absoluta. Compare-a com recompensas e resultados de combate; correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 232 | OK (232) | 0 | 0 | 0 | 0 | 1 | 0 |
- Jogador 1 — IDs equipados observados: TFT_Item_IonicSpark; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 5, COMPONENT_ANVIL_GRANTED: 6, COMPONENT_LOOT_GRANTED: 16.
| Jogador 2 | 365 | OK (365) | 2 | 0 | 0 | 3 | 2 | 1 |
- Jogador 2 — IDs equipados observados: TFT_Item_GuardianAngel, TFT_Item_IonicSpark; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 5, COMPONENT_ANVIL_GRANTED: 6, COMPONENT_LOOT_GRANTED: 16.
| Jogador 3 | 219 | OK (219) | 0 | 0 | 0 | 2 | 0 | 0 |
- Jogador 3 — IDs equipados observados: nenhum observado; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 5, COMPONENT_ANVIL_GRANTED: 6, COMPONENT_LOOT_GRANTED: 16.
| Jogador 4 | 260 | OK (260) | 0 | 0 | 0 | 1 | 1 | 0 |
- Jogador 4 — IDs equipados observados: TFT_Item_Redemption; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 5, COMPONENT_ANVIL_GRANTED: 6, COMPONENT_LOOT_GRANTED: 16.
| Jogador 5 | 273 | OK (273) | 0 | 0 | 0 | 3 | 0 | 0 |
- Jogador 5 — IDs equipados observados: nenhum observado; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 5, COMPONENT_ANVIL_GRANTED: 6, COMPONENT_LOOT_GRANTED: 16.
| Jogador 6 | 378 | OK (378) | 0 | 0 | 0 | 3 | 2 | 1 |
- Jogador 6 — IDs equipados observados: DA_18_EmblemSpellweaver, TFT_Item_NightHarvester; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 5, COMPONENT_ANVIL_GRANTED: 6, COMPONENT_LOOT_GRANTED: 16.
| Jogador 7 | 271 | OK (271) | 0 | 0 | 0 | 3 | 0 | 0 |
- Jogador 7 — IDs equipados observados: nenhum observado; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 5, COMPONENT_ANVIL_GRANTED: 6, COMPONENT_LOOT_GRANTED: 16.
| Jogador 8 | 258 | OK (258) | 0 | 0 | 0 | 1 | 2 | 1 |
- Jogador 8 — IDs equipados observados: TFT_Item_Crownguard, TFT_Item_LastWhisper; eventos: COMPLETED_ITEM_ANVIL_GRANTED: 5, COMPONENT_ANVIL_GRANTED: 6, COMPONENT_LOOT_GRANTED: 16.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.115 | 0.000 |
| Jogador 1 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.005 | 0.000 |
| Jogador 1 | 1-3 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 5 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 1 | 1-4 | 7 | -2.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 7% | 5 → 10 | 2 | 3 → 4 | 0.008 | 0.000 |
| Jogador 1 | 2-1 | 9 | 2.000 | 0.000 | 0 → 0 | 1 → 0 | 7% → 7% | 10 → 14 | 5 | 4 → 4 | -0.142 | -0.281 |
| Jogador 1 | 2-2 | 10 | 10.000 | 0.000 | 0 → 0 | 0 → 1 | 7% → 14% | 14 → 15 | 5 | 4 → 4 | 0.058 | -0.243 |
| Jogador 1 | 2-3 | 10 | 4.000 | 0.000 | 0 → 1 | 1 → 0 | 14% → 14% | 15 → 18 | 4 | 4 → 4 | 0.006 | -0.232 |
| Jogador 1 | 2-4 | 10 | 4.000 | 0.000 | 1 → 1 | 0 → 0 | 14% → 14% | 18 → 23 | 3 | 4 → 4 | 0.063 | 0.000 |
| Jogador 1 | 2-5 | 6 | 0.000 | 4.000 | 1 → 1 | 0 → 1 | 14% → 14% | 23 → 29 | 2 | 4 → 5 | -0.107 | -0.456 |
| Jogador 1 | 2-6 | 6 | 2.000 | 4.000 | 1 → 0 | 1 → 2 | 14% → 18% | 29 → 35 | 3 | 5 → 5 | -0.046 | -0.395 |
| Jogador 1 | 2-7 | 4 | 2.000 | -2.000 | 0 → 1 | 2 → 2 | 18% → 18% | 35 → 45 | 0 | 5 → 5 | 0.058 | 0.000 |
| Jogador 1 | 3-1 | 4 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 18% → 18% | 45 → 55 | 0 | 5 → 5 | 0.089 | 0.679 |
| Jogador 1 | 3-2 | 9 | -8.000 | 28.000 | 1 → 1 | 2 → 1 | 18% → 11% | 55 → 43 | 20 | 5 → 5 | -0.028 | -0.304 |
| Jogador 1 | 3-3 | 9 | 6.000 | 10.000 | 1 → 1 | 1 → 2 | 11% → 14% | 43 → 40 | 15 | 5 → 5 | -0.023 | -0.314 |
| Jogador 1 | 3-4 | 9 | 4.000 | 6.000 | 1 → 1 | 2 → 2 | 14% → 18% | 40 → 33 | 15 | 5 → 5 | 0.015 | 0.000 |
| Jogador 1 | 3-5 | 9 | 0.000 | 12.000 | 1 → 1 | 2 → 2 | 18% → 18% | 33 → 22 | 18 | 5 → 5 | 0.000 | 0.307 |
| Jogador 1 | 3-6 | 10 | 0.000 | -6.000 | 1 → 1 | 2 → 2 | 18% → 18% | 22 → 14 | 16 | 5 → 5 | 0.000 | -0.263 |
| Jogador 1 | 3-7 | 10 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 18% → 18% | 14 → 6 | 13 | 5 → 5 | -0.042 | 0.000 |
| Jogador 1 | 4-1 | 10 | 0.000 | -2.000 | 1 → 1 | 2 → 2 | 18% → 18% | 6 → 6 | 13 | 5 → 6 | 0.030 | -0.280 |
| Jogador 1 | 4-2 | 8 | 8.000 | 4.000 | 1 → 1 | 2 → 2 | 18% → 21% | 6 → 6 | 6 | 6 → 6 | 0.028 | -0.350 |
| Jogador 1 | 4-3 | 10 | 0.000 | 4.000 | 1 → 1 | 2 → 1 | 21% → 21% | 6 → 6 | 10 | 6 → 6 | 0.019 | 0.285 |
| Jogador 1 | 4-4 | 10 | 0.000 | -12.000 | 1 → 1 | 1 → 2 | 21% → 21% | 6 → 14 | 13 | 6 → 6 | 0.006 | 0.000 |
| Jogador 1 | 4-5 | 10 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 21% → 21% | 14 → 8 | 15 | 6 → 6 | 0.000 | -0.276 |
| Jogador 1 | 4-6 | 9 | -38.000 | -62.000 | 1 → 0 | 2 → 0 | 21% → 0% | 8 → 0 | 13 | 6 → 6 | -0.027 | -0.307 |
| Jogador 1 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 5-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 6-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 6-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 7-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 7-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 1 | 7-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 10, COMPOSITION_COMPATIBILITY: 19, IMMEDIATE_UPGRADE: 8, PAIR_POTENTIAL: 10; mudanças de composição: 1; posicionamento melhorou em 32 ações e piorou em 35.
- Jogador 1 — estado final: ouro 0, nível 6, vida 0.0, colocação 7.
| Jogador 2 | 1-1 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.077 | 0.000 |
| Jogador 2 | 1-2 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | -0.018 | 0.000 |
| Jogador 2 | 1-3 | 9 | 6.000 | 0.000 | 0 → 0 | 1 → 0 | 7% → 11% | 3 → 3 | 4 | 3 → 3 | 0.033 | 0.000 |
| Jogador 2 | 1-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 7 | 0 | 3 → 4 | 0.000 | 0.000 |
| Jogador 2 | 2-1 | 5 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 7 → 10 | 3 | 4 → 4 | -0.011 | 0.502 |
| Jogador 2 | 2-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 10 → 15 | 2 | 4 → 4 | 0.015 | 0.517 |
| Jogador 2 | 2-3 | 6 | 0.000 | -2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 15 → 24 | 3 | 4 → 4 | 0.009 | 0.410 |
| Jogador 2 | 2-4 | 6 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 24 → 32 | 4 | 4 → 4 | 0.000 | 0.000 |
| Jogador 2 | 2-5 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 32 → 41 | 3 | 4 → 5 | 0.000 | 0.502 |
| Jogador 2 | 2-6 | 9 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 18% | 41 → 49 | 5 | 5 → 5 | -0.018 | 0.279 |
| Jogador 2 | 2-7 | 9 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 49 → 47 | 17 | 5 → 5 | 0.005 | 0.000 |
| Jogador 2 | 3-1 | 7 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 18% → 18% | 47 → 55 | 4 | 5 → 5 | 0.000 | -0.383 |
| Jogador 2 | 3-2 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 55 → 66 | 1 | 5 → 6 | 0.000 | 0.728 |
| Jogador 2 | 3-3 | 9 | 2.000 | 16.000 | 0 → 0 | 1 → 0 | 18% → 18% | 66 → 62 | 16 | 6 → 6 | -0.034 | 0.296 |
| Jogador 2 | 3-4 | 9 | 6.000 | 10.000 | 0 → 0 | 0 → 2 | 18% → 21% | 62 → 56 | 16 | 6 → 6 | -0.008 | 0.000 |
| Jogador 2 | 3-5 | 9 | 0.000 | 10.000 | 0 → 0 | 2 → 4 | 21% → 21% | 56 → 50 | 17 | 6 → 6 | 0.000 | 0.318 |
| Jogador 2 | 3-6 | 10 | 0.000 | 26.000 | 0 → 0 | 4 → 3 | 21% → 21% | 50 → 36 | 23 | 6 → 6 | -0.006 | 0.281 |
| Jogador 2 | 3-7 | 10 | 8.000 | -4.000 | 0 → 2 | 3 → 1 | 21% → 21% | 36 → 32 | 14 | 6 → 6 | -0.004 | 0.000 |
| Jogador 2 | 4-1 | 10 | 0.000 | 8.000 | 2 → 2 | 1 → 0 | 21% → 21% | 32 → 32 | 14 | 6 → 6 | 0.017 | 0.311 |
| Jogador 2 | 4-2 | 10 | 0.000 | 6.000 | 2 → 2 | 0 → 0 | 21% → 21% | 32 → 32 | 15 | 6 → 6 | 0.000 | -0.268 |
| Jogador 2 | 4-3 | 10 | 0.000 | -6.000 | 2 → 2 | 0 → 1 | 21% → 21% | 32 → 40 | 12 | 6 → 6 | 0.000 | -0.263 |
| Jogador 2 | 4-4 | 10 | 0.000 | 2.000 | 2 → 2 | 1 → 1 | 21% → 21% | 40 → 40 | 16 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 4-5 | 10 | 0.000 | 2.000 | 2 → 2 | 1 → 2 | 21% → 21% | 40 → 42 | 16 | 6 → 6 | 0.000 | 0.293 |
| Jogador 2 | 4-6 | 10 | 0.000 | -8.000 | 2 → 2 | 2 → 3 | 21% → 21% | 42 → 53 | 14 | 6 → 6 | 0.006 | 0.293 |
| Jogador 2 | 4-7 | 10 | 0.000 | -2.000 | 2 → 2 | 3 → 4 | 21% → 21% | 53 → 61 | 17 | 6 → 6 | 0.006 | 0.000 |
| Jogador 2 | 5-1 | 10 | 0.000 | -8.000 | 2 → 2 | 4 → 3 | 21% → 21% | 61 → 68 | 14 | 6 → 6 | -0.006 | -0.280 |
| Jogador 2 | 5-2 | 10 | 0.000 | 12.000 | 2 → 2 | 3 → 4 | 21% → 21% | 68 → 66 | 18 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 5-3 | 10 | 0.000 | 6.000 | 2 → 2 | 4 → 3 | 21% → 21% | 66 → 65 | 18 | 6 → 6 | -0.006 | 0.286 |
| Jogador 2 | 5-4 | 10 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 21% → 21% | 65 → 67 | 17 | 6 → 6 | -0.006 | 0.000 |
| Jogador 2 | 5-5 | 10 | 0.000 | 8.000 | 2 → 2 | 3 → 3 | 21% → 21% | 67 → 67 | 19 | 6 → 6 | 0.000 | 0.286 |
| Jogador 2 | 5-6 | 10 | 0.000 | -2.000 | 2 → 2 | 3 → 4 | 21% → 21% | 67 → 68 | 15 | 6 → 7 | 0.000 | -0.285 |
| Jogador 2 | 5-7 | 10 | 16.000 | -14.000 | 2 → 3 | 4 → 2 | 21% → 25% | 68 → 76 | 13 | 7 → 7 | -0.024 | 0.000 |
| Jogador 2 | 6-1 | 10 | 0.000 | 8.000 | 3 → 3 | 2 → 2 | 25% → 25% | 76 → 79 | 16 | 7 → 7 | 0.000 | 0.304 |
| Jogador 2 | 6-2 | 10 | 0.000 | -2.000 | 3 → 3 | 2 → 3 | 25% → 25% | 79 → 86 | 16 | 7 → 7 | 0.000 | 0.304 |
| Jogador 2 | 6-3 | 10 | 0.000 | -6.000 | 3 → 3 | 3 → 1 | 25% → 25% | 86 → 94 | 13 | 7 → 7 | -0.005 | 0.299 |
| Jogador 2 | 6-4 | 10 | 6.000 | 6.000 | 3 → 4 | 1 → 1 | 25% → 25% | 94 → 94 | 15 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 6-5 | 10 | 0.000 | 0.000 | 4 → 4 | 1 → 1 | 25% → 25% | 94 → 100 | 16 | 7 → 7 | 0.000 | 0.299 |
| Jogador 2 | 6-6 | 10 | 0.000 | 8.000 | 4 → 4 | 1 → 1 | 25% → 25% | 100 → 105 | 18 | 7 → 7 | 0.000 | 0.292 |
| Jogador 2 | 6-7 | 10 | 0.000 | -8.000 | 4 → 4 | 1 → 1 | 25% → 25% | 105 → 117 | 13 | 7 → 7 | 0.000 | 0.000 |
| Jogador 2 | 7-1 | 10 | 0.000 | 6.000 | 4 → 4 | 1 → 2 | 25% → 25% | 117 → 116 | 13 | 7 → 7 | 0.000 | -0.280 |
| Jogador 2 | 7-2 | 10 | 0.000 | -10.000 | 4 → 4 | 2 → 4 | 25% → 25% | 116 → 128 | 15 | 7 → 7 | 0.012 | 0.303 |
| Jogador 2 | 7-3 | 10 | 0.000 | 2.000 | 4 → 4 | 4 → 3 | 25% → 25% | 128 → 117 | 20 | 7 → 7 | 0.000 | 0.303 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 41, COMPOSITION_COMPATIBILITY: 35, IMMEDIATE_UPGRADE: 11, PAIR_POTENTIAL: 24; mudanças de composição: 1; posicionamento melhorou em 25 ações e piorou em 23.
- Jogador 2 — estado final: ouro 117, nível 7, vida 15.0, colocação 1.
| Jogador 3 | 1-1 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.077 | 0.000 |
| Jogador 3 | 1-2 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 7% | 2 → 3 | 1 | 3 → 3 | -0.018 | 0.000 |
| Jogador 3 | 1-3 | 6 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 7% → 11% | 3 → 4 | 2 | 3 → 3 | 0.023 | 0.000 |
| Jogador 3 | 1-4 | 5 | 2.000 | 0.000 | 0 → 0 | 1 → 0 | 11% → 11% | 4 → 7 | 2 | 3 → 4 | 0.019 | 0.000 |
| Jogador 3 | 2-1 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 11% → 14% | 7 → 11 | 2 | 4 → 4 | 0.003 | 0.476 |
| Jogador 3 | 2-2 | 10 | 6.000 | 0.000 | 0 → 1 | 1 → 0 | 14% → 14% | 11 → 11 | 5 | 4 → 4 | -0.010 | -0.248 |
| Jogador 3 | 2-3 | 5 | 2.000 | 4.000 | 1 → 1 | 0 → 0 | 14% → 14% | 11 → 14 | 3 | 4 → 4 | 0.010 | -0.464 |
| Jogador 3 | 2-4 | 4 | -4.000 | 4.000 | 1 → 0 | 0 → 0 | 14% → 14% | 14 → 21 | 0 | 4 → 4 | -0.028 | 0.000 |
| Jogador 3 | 2-5 | 9 | 4.000 | -4.000 | 0 → 1 | 0 → 0 | 14% → 14% | 21 → 29 | 5 | 4 → 5 | 0.007 | -0.276 |
| Jogador 3 | 2-6 | 8 | 6.000 | -2.000 | 1 → 1 | 0 → 0 | 14% → 18% | 29 → 35 | 2 | 5 → 5 | -0.001 | -0.296 |
| Jogador 3 | 2-7 | 6 | 0.000 | 4.000 | 1 → 1 | 0 → 1 | 18% → 18% | 35 → 42 | 2 | 5 → 5 | 0.009 | 0.000 |
| Jogador 3 | 3-1 | 6 | 0.000 | 0.000 | 1 → 1 | 1 → 1 | 18% → 18% | 42 → 52 | 0 | 5 → 5 | 0.009 | 0.469 |
| Jogador 3 | 3-2 | 9 | -6.000 | 14.000 | 1 → 1 | 1 → 0 | 18% → 14% | 52 → 48 | 14 | 5 → 5 | -0.048 | 0.324 |
| Jogador 3 | 3-3 | 9 | 4.000 | 18.000 | 1 → 1 | 0 → 1 | 14% → 18% | 48 → 39 | 17 | 5 → 5 | -0.023 | -0.298 |
| Jogador 3 | 3-4 | 9 | 0.000 | 14.000 | 1 → 1 | 1 → 1 | 18% → 18% | 39 → 35 | 15 | 5 → 5 | 0.000 | 0.000 |
| Jogador 3 | 3-5 | 9 | -2.000 | 8.000 | 1 → 1 | 1 → 1 | 18% → 18% | 35 → 33 | 15 | 5 → 5 | -0.018 | -0.303 |
| Jogador 3 | 3-6 | 10 | 0.000 | 2.000 | 1 → 1 | 1 → 2 | 18% → 18% | 33 → 28 | 16 | 5 → 5 | 0.000 | -0.278 |
| Jogador 3 | 3-7 | 10 | 0.000 | 0.000 | 1 → 1 | 2 → 3 | 18% → 18% | 28 → 21 | 17 | 5 → 5 | 0.000 | 0.000 |
| Jogador 3 | 4-1 | 10 | -12.000 | -8.000 | 1 → 0 | 3 → 2 | 18% → 11% | 21 → 15 | 16 | 5 → 6 | -0.000 | -0.295 |
| Jogador 3 | 4-2 | 10 | 10.000 | 2.000 | 0 → 0 | 2 → 2 | 11% → 18% | 15 → 14 | 12 | 6 → 6 | 0.031 | -0.281 |
| Jogador 3 | 4-3 | 10 | 8.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 21% | 14 → 16 | 16 | 6 → 6 | -0.008 | -0.271 |
| Jogador 3 | 4-4 | 10 | 0.000 | 10.000 | 0 → 0 | 2 → 2 | 21% → 21% | 16 → 9 | 19 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 4-5 | 10 | -30.000 | -66.000 | 0 → 0 | 2 → 0 | 21% → 0% | 9 → 5 | 12 | 6 → 6 | -0.005 | -0.263 |
| Jogador 3 | 4-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 5 → 5 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 4-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 5 → 5 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 5-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 5 → 5 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 5 → 5 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 5 → 5 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 5 → 5 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 5 → 5 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 5 → 5 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 5 → 5 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 5 → 5 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 5 → 5 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 5 → 5 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 5 → 5 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 5 → 5 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 6-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 5 → 5 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 6-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 5 → 5 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 7-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 5 → 5 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 7-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 5 → 5 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 3 | 7-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 5 → 5 | 0 | 6 → 6 | 0.000 | 0.000 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 10, COMPOSITION_COMPATIBILITY: 19, IMMEDIATE_UPGRADE: 5, NO_IDENTIFIED_STRATEGIC_GAIN: 1, PAIR_POTENTIAL: 11; mudanças de composição: 4; posicionamento melhorou em 23 ações e piorou em 30.
- Jogador 3 — estado final: ouro 5, nível 6, vida 0.0, colocação 8.
| Jogador 4 | 1-1 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.077 | 0.000 |
| Jogador 4 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.007 | 0.000 |
| Jogador 4 | 1-3 | 4 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 5 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 4 | 1-4 | 6 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 5 → 9 | 2 | 3 → 4 | 0.000 | 0.000 |
| Jogador 4 | 2-1 | 9 | 4.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 14% | 9 → 11 | 5 | 4 → 4 | -0.013 | 0.299 |
| Jogador 4 | 2-2 | 10 | 2.000 | 2.000 | 0 → 0 | 1 → 0 | 14% → 14% | 11 → 10 | 11 | 4 → 4 | 0.009 | -0.231 |
| Jogador 4 | 2-3 | 10 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 10 → 12 | 8 | 4 → 4 | -0.015 | 0.238 |
| Jogador 4 | 2-4 | 10 | 0.000 | -6.000 | 0 → 0 | 0 → 0 | 14% → 14% | 12 → 21 | 4 | 4 → 4 | 0.024 | 0.000 |
| Jogador 4 | 2-5 | 9 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 21 → 28 | 6 | 4 → 5 | -0.010 | -0.298 |
| Jogador 4 | 2-6 | 9 | 6.000 | 0.000 | 0 → 0 | 0 → 1 | 14% → 18% | 28 → 33 | 4 | 5 → 5 | -0.061 | 0.279 |
| Jogador 4 | 2-7 | 9 | -2.000 | 6.000 | 0 → 0 | 1 → 1 | 18% → 18% | 33 → 39 | 8 | 5 → 5 | 0.022 | 0.000 |
| Jogador 4 | 3-1 | 9 | 4.000 | 6.000 | 0 → 1 | 1 → 1 | 18% → 18% | 39 → 36 | 10 | 5 → 5 | -0.071 | -0.293 |
| Jogador 4 | 3-2 | 6 | 0.000 | 2.000 | 1 → 1 | 1 → 2 | 18% → 18% | 36 → 44 | 1 | 5 → 5 | 0.002 | -0.431 |
| Jogador 4 | 3-3 | 9 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 18% → 18% | 44 → 37 | 15 | 5 → 5 | 0.000 | -0.276 |
| Jogador 4 | 3-4 | 9 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 18% → 18% | 37 → 29 | 16 | 5 → 5 | 0.000 | 0.000 |
| Jogador 4 | 3-5 | 9 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 18% → 18% | 29 → 20 | 16 | 5 → 5 | 0.000 | -0.287 |
| Jogador 4 | 3-6 | 10 | -6.000 | 18.000 | 1 → 1 | 2 → 0 | 18% → 14% | 20 → 13 | 14 | 5 → 5 | -0.033 | -0.278 |
| Jogador 4 | 3-7 | 10 | 6.000 | 2.000 | 1 → 1 | 0 → 3 | 14% → 18% | 13 → 14 | 14 | 5 → 5 | 0.022 | 0.000 |
| Jogador 4 | 4-1 | 10 | 0.000 | 14.000 | 1 → 1 | 3 → 2 | 18% → 18% | 14 → 8 | 16 | 5 → 6 | 0.003 | -0.276 |
| Jogador 4 | 4-2 | 10 | 6.000 | 0.000 | 1 → 1 | 2 → 2 | 18% → 21% | 8 → 6 | 11 | 6 → 6 | -0.028 | 0.298 |
| Jogador 4 | 4-3 | 7 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 21% → 21% | 6 → 6 | 5 | 6 → 6 | -0.006 | -0.382 |
| Jogador 4 | 4-4 | 10 | -2.000 | 6.000 | 1 → 1 | 2 → 2 | 21% → 21% | 6 → 5 | 13 | 6 → 6 | 0.084 | 0.000 |
| Jogador 4 | 4-5 | 10 | -2.000 | 6.000 | 1 → 1 | 2 → 1 | 21% → 21% | 5 → 6 | 7 | 6 → 6 | 0.010 | 0.280 |
| Jogador 4 | 4-6 | 10 | 0.000 | 4.000 | 1 → 1 | 1 → 2 | 21% → 21% | 6 → 5 | 13 | 6 → 6 | -0.006 | -0.281 |
| Jogador 4 | 4-7 | 8 | 0.000 | 2.000 | 1 → 1 | 2 → 2 | 21% → 21% | 5 → 5 | 7 | 6 → 6 | 0.003 | 0.000 |
| Jogador 4 | 5-1 | 10 | -26.000 | -78.000 | 1 → 0 | 2 → 0 | 21% → 0% | 5 → 0 | 10 | 6 → 6 | -0.001 | -0.290 |
| Jogador 4 | 5-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 6-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 7-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 7-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 7-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 6, COMPOSITION_COMPATIBILITY: 31, IMMEDIATE_UPGRADE: 8, PAIR_POTENTIAL: 19; mudanças de composição: 2; posicionamento melhorou em 33 ações e piorou em 38.
- Jogador 4 — estado final: ouro 0, nível 6, vida 0.0, colocação 6.
| Jogador 5 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.115 | 0.000 |
| Jogador 5 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.041 | 0.000 |
| Jogador 5 | 1-3 | 6 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 7% | 2 → 5 | 4 | 3 → 3 | 0.000 | 0.000 |
| Jogador 5 | 1-4 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 5 → 7 | 2 | 3 → 4 | -0.007 | 0.000 |
| Jogador 5 | 2-1 | 8 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 14% | 7 → 9 | 5 | 4 → 4 | -0.009 | -0.296 |
| Jogador 5 | 2-2 | 8 | 6.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 9 → 12 | 6 | 4 → 4 | 0.009 | 0.336 |
| Jogador 5 | 2-3 | 4 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 12 → 20 | 1 | 4 → 4 | 0.000 | 0.616 |
| Jogador 5 | 2-4 | 6 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 20 → 28 | 5 | 4 → 4 | 0.000 | 0.000 |
| Jogador 5 | 2-5 | 4 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 14% | 28 → 35 | 3 | 4 → 5 | 0.000 | -0.593 |
| Jogador 5 | 2-6 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 14% → 18% | 35 → 37 | 6 | 5 → 5 | -0.002 | -0.270 |
| Jogador 5 | 2-7 | 9 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 37 → 46 | 2 | 5 → 5 | -0.030 | 0.000 |
| Jogador 5 | 3-1 | 7 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 46 → 56 | 2 | 5 → 5 | 0.001 | -0.362 |
| Jogador 5 | 3-2 | 9 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 18% → 18% | 56 → 67 | 4 | 5 → 5 | -0.006 | 0.307 |
| Jogador 5 | 3-3 | 6 | 2.000 | 12.000 | 0 → 0 | 0 → 1 | 18% → 18% | 67 → 72 | 7 | 5 → 5 | -0.058 | 0.477 |
| Jogador 5 | 3-4 | 9 | 0.000 | 22.000 | 0 → 0 | 1 → 2 | 18% → 18% | 72 → 64 | 19 | 5 → 5 | 0.000 | 0.000 |
| Jogador 5 | 3-5 | 9 | 0.000 | 14.000 | 0 → 0 | 2 → 3 | 18% → 18% | 64 → 61 | 16 | 5 → 5 | -0.007 | -0.287 |
| Jogador 5 | 3-6 | 10 | 0.000 | -2.000 | 0 → 0 | 3 → 4 | 18% → 18% | 61 → 65 | 13 | 5 → 6 | 0.000 | 0.281 |
| Jogador 5 | 3-7 | 10 | 4.000 | 4.000 | 0 → 0 | 4 → 3 | 18% → 21% | 65 → 69 | 11 | 6 → 6 | -0.005 | 0.000 |
| Jogador 5 | 4-1 | 10 | 0.000 | 8.000 | 0 → 0 | 3 → 4 | 21% → 21% | 69 → 71 | 16 | 6 → 6 | 0.000 | 0.280 |
| Jogador 5 | 4-2 | 10 | 0.000 | -8.000 | 0 → 0 | 4 → 4 | 21% → 21% | 71 → 84 | 15 | 6 → 6 | 0.006 | 0.285 |
| Jogador 5 | 4-3 | 10 | -4.000 | 6.000 | 0 → 0 | 4 → 3 | 21% → 18% | 84 → 89 | 14 | 6 → 6 | -0.001 | 0.288 |
| Jogador 5 | 4-4 | 10 | 4.000 | 2.000 | 0 → 0 | 3 → 2 | 18% → 21% | 89 → 91 | 16 | 6 → 6 | -0.015 | 0.000 |
| Jogador 5 | 4-5 | 10 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 21% → 21% | 91 → 93 | 14 | 6 → 6 | -0.049 | -0.268 |
| Jogador 5 | 4-6 | 10 | 0.000 | 10.000 | 0 → 0 | 2 → 2 | 21% → 21% | 93 → 88 | 19 | 6 → 6 | -0.006 | -0.276 |
| Jogador 5 | 4-7 | 10 | 0.000 | 4.000 | 0 → 0 | 2 → 2 | 21% → 21% | 88 → 83 | 18 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-1 | 10 | 12.000 | -14.000 | 0 → 2 | 2 → 2 | 21% → 21% | 83 → 89 | 8 | 6 → 6 | 0.077 | 0.286 |
| Jogador 5 | 5-2 | 10 | -2.000 | -8.000 | 2 → 2 | 2 → 2 | 21% → 21% | 89 → 97 | 14 | 6 → 6 | -0.021 | -0.290 |
| Jogador 5 | 5-3 | 10 | 0.000 | 4.000 | 2 → 2 | 2 → 1 | 21% → 21% | 97 → 90 | 18 | 6 → 6 | -0.006 | -0.270 |
| Jogador 5 | 5-4 | 10 | 0.000 | 4.000 | 2 → 2 | 1 → 2 | 21% → 21% | 90 → 83 | 18 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-5 | 10 | -42.000 | -64.000 | 2 → 0 | 2 → 0 | 21% → 0% | 83 → 65 | 18 | 6 → 6 | 0.027 | -0.270 |
| Jogador 5 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 65 → 65 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 65 → 65 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 65 → 65 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 65 → 65 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 65 → 65 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 65 → 65 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 65 → 65 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 65 → 65 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 6-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 65 → 65 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 7-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 65 → 65 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 7-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 65 → 65 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 7-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 65 → 65 | 0 | 6 → 6 | 0.000 | 0.000 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 12, COMPOSITION_COMPATIBILITY: 29, IMMEDIATE_UPGRADE: 8, PAIR_POTENTIAL: 19; mudanças de composição: 1; posicionamento melhorou em 25 ações e piorou em 27.
- Jogador 5 — estado final: ouro 65, nível 6, vida 0.0, colocação 5.
| Jogador 6 | 1-1 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.077 | 0.000 |
| Jogador 6 | 1-2 | 10 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 4 | 3 → 3 | 0.001 | 0.000 |
| Jogador 6 | 1-3 | 5 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 3 → 4 | 2 | 3 → 3 | -0.132 | 0.000 |
| Jogador 6 | 1-4 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 4 → 7 | 2 | 3 → 4 | 0.000 | 0.000 |
| Jogador 6 | 2-1 | 7 | 6.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 14% | 7 → 7 | 5 | 4 → 4 | 0.016 | -0.323 |
| Jogador 6 | 2-2 | 5 | -2.000 | 2.000 | 0 → 0 | 0 → 0 | 14% → 14% | 7 → 13 | 0 | 4 → 4 | -0.004 | 0.486 |
| Jogador 6 | 2-3 | 10 | 6.000 | -6.000 | 0 → 0 | 0 → 1 | 14% → 18% | 13 → 12 | 10 | 4 → 5 | 0.063 | 0.251 |
| Jogador 6 | 2-4 | 10 | 2.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 12 → 9 | 11 | 5 → 5 | 0.013 | 0.000 |
| Jogador 6 | 2-5 | 9 | 2.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 21% | 9 → 7 | 12 | 5 → 6 | -0.040 | 0.324 |
| Jogador 6 | 2-6 | 5 | 2.000 | 4.000 | 0 → 0 | 1 → 2 | 21% → 21% | 7 → 11 | 3 | 6 → 6 | 0.000 | 0.563 |
| Jogador 6 | 2-7 | 7 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 21% → 21% | 11 → 18 | 3 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 3-1 | 6 | 2.000 | 12.000 | 0 → 0 | 2 → 2 | 21% → 21% | 18 → 20 | 7 | 6 → 6 | -0.044 | 0.477 |
| Jogador 6 | 3-2 | 6 | 4.000 | -4.000 | 0 → 1 | 2 → 1 | 21% → 21% | 20 → 27 | 3 | 6 → 6 | 0.042 | 0.469 |
| Jogador 6 | 3-3 | 9 | 0.000 | 38.000 | 1 → 1 | 1 → 2 | 21% → 21% | 27 → 13 | 23 | 6 → 6 | 0.000 | 0.333 |
| Jogador 6 | 3-4 | 9 | 0.000 | 4.000 | 1 → 1 | 2 → 2 | 21% → 21% | 13 → 15 | 14 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 3-5 | 9 | 0.000 | -2.000 | 1 → 1 | 2 → 3 | 21% → 21% | 15 → 22 | 14 | 6 → 6 | 0.000 | 0.307 |
| Jogador 6 | 3-6 | 10 | 0.000 | 10.000 | 1 → 1 | 3 → 3 | 21% → 21% | 22 → 16 | 19 | 6 → 6 | -0.012 | 0.295 |
| Jogador 6 | 3-7 | 10 | 0.000 | -6.000 | 1 → 1 | 3 → 3 | 21% → 21% | 16 → 24 | 14 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 4-1 | 10 | 0.000 | 2.000 | 1 → 1 | 3 → 4 | 21% → 21% | 24 → 32 | 16 | 6 → 6 | 0.006 | 0.296 |
| Jogador 6 | 4-2 | 10 | 0.000 | -2.000 | 1 → 1 | 4 → 3 | 21% → 21% | 32 → 41 | 13 | 6 → 6 | 0.000 | 0.280 |
| Jogador 6 | 4-3 | 10 | 0.000 | 6.000 | 1 → 1 | 3 → 3 | 21% → 21% | 41 → 46 | 14 | 6 → 6 | 0.000 | 0.280 |
| Jogador 6 | 4-4 | 10 | 0.000 | -10.000 | 1 → 1 | 3 → 4 | 21% → 21% | 46 → 61 | 11 | 6 → 6 | 0.006 | 0.000 |
| Jogador 6 | 4-5 | 10 | 0.000 | 2.000 | 1 → 1 | 4 → 3 | 21% → 21% | 61 → 68 | 15 | 6 → 6 | 0.000 | 0.293 |
| Jogador 6 | 4-6 | 10 | 0.000 | 0.000 | 1 → 1 | 3 → 3 | 21% → 21% | 68 → 76 | 14 | 6 → 6 | 0.000 | 0.298 |
| Jogador 6 | 4-7 | 10 | 0.000 | 8.000 | 1 → 1 | 3 → 3 | 21% → 21% | 76 → 81 | 17 | 6 → 7 | 0.000 | 0.000 |
| Jogador 6 | 5-1 | 10 | 8.000 | -12.000 | 1 → 1 | 3 → 3 | 21% → 25% | 81 → 95 | 10 | 7 → 7 | -0.014 | 0.309 |
| Jogador 6 | 5-2 | 10 | 0.000 | 6.000 | 1 → 1 | 3 → 3 | 25% → 25% | 95 → 102 | 18 | 7 → 7 | 0.000 | 0.307 |
| Jogador 6 | 5-3 | 10 | 0.000 | 2.000 | 1 → 1 | 3 → 4 | 25% → 25% | 102 → 113 | 15 | 7 → 7 | 0.000 | 0.301 |
| Jogador 6 | 5-4 | 10 | 0.000 | 0.000 | 1 → 1 | 4 → 5 | 25% → 25% | 113 → 124 | 14 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 5-5 | 10 | 0.000 | 2.000 | 1 → 1 | 5 → 4 | 25% → 25% | 124 → 135 | 15 | 7 → 7 | 0.000 | 0.301 |
| Jogador 6 | 5-6 | 10 | 0.000 | -6.000 | 1 → 1 | 4 → 5 | 25% → 25% | 135 → 150 | 12 | 7 → 7 | 0.000 | 0.302 |
| Jogador 6 | 5-7 | 10 | 0.000 | -2.000 | 1 → 1 | 5 → 3 | 25% → 25% | 150 → 158 | 14 | 7 → 7 | -0.006 | 0.000 |
| Jogador 6 | 6-1 | 10 | 0.000 | 16.000 | 1 → 1 | 3 → 3 | 25% → 25% | 158 → 161 | 16 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 6-2 | 10 | 0.000 | -8.000 | 1 → 1 | 3 → 4 | 25% → 25% | 161 → 171 | 13 | 7 → 7 | 0.000 | -0.285 |
| Jogador 6 | 6-3 | 10 | 0.000 | 14.000 | 1 → 1 | 4 → 3 | 25% → 25% | 171 → 168 | 20 | 7 → 7 | -0.006 | -0.280 |
| Jogador 6 | 6-4 | 10 | 0.000 | -2.000 | 1 → 1 | 3 → 4 | 25% → 25% | 168 → 178 | 13 | 7 → 7 | 0.000 | 0.000 |
| Jogador 6 | 6-5 | 10 | 0.000 | 6.000 | 1 → 1 | 4 → 4 | 25% → 25% | 178 → 181 | 18 | 7 → 7 | -0.006 | -0.280 |
| Jogador 6 | 6-6 | 10 | 10.000 | -12.000 | 1 → 2 | 4 → 2 | 25% → 25% | 181 → 188 | 13 | 7 → 7 | 0.008 | -0.275 |
| Jogador 6 | 6-7 | 10 | 0.000 | -4.000 | 2 → 2 | 2 → 2 | 25% → 25% | 188 → 197 | 16 | 7 → 7 | 0.006 | 0.000 |
| Jogador 6 | 7-1 | 10 | 0.000 | 0.000 | 2 → 2 | 2 → 3 | 25% → 25% | 197 → 204 | 11 | 7 → 7 | 0.000 | 0.303 |
| Jogador 6 | 7-2 | 10 | -4.000 | 8.000 | 2 → 2 | 3 → 1 | 25% → 21% | 204 → 208 | 17 | 7 → 7 | -0.010 | -0.280 |
| Jogador 6 | 7-3 | 10 | -46.000 | -70.000 | 2 → 0 | 1 → 0 | 21% → 0% | 208 → 202 | 12 | 7 → 7 | -0.001 | -0.280 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 45, COMPOSITION_COMPATIBILITY: 46, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 30; mudanças de composição: 0; posicionamento melhorou em 23 ações e piorou em 24.
- Jogador 6 — estado final: ouro 202, nível 7, vida 0.0, colocação 2.
| Jogador 7 | 1-1 | 6 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 1 | 2 → 3 | 0.077 | 0.000 |
| Jogador 7 | 1-2 | 10 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 3 | 3 → 3 | 0.006 | 0.000 |
| Jogador 7 | 1-3 | 5 | 2.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 2 → 4 | 2 | 3 → 3 | 0.014 | 0.000 |
| Jogador 7 | 1-4 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 11% | 4 → 8 | 2 | 3 → 4 | 0.000 | 0.000 |
| Jogador 7 | 2-1 | 5 | 4.000 | 0.000 | 0 → 0 | 1 → 1 | 11% → 14% | 8 → 12 | 2 | 4 → 4 | 0.000 | 0.527 |
| Jogador 7 | 2-2 | 5 | 4.000 | 0.000 | 0 → 0 | 1 → 0 | 14% → 14% | 12 → 18 | 3 | 4 → 4 | 0.014 | 0.527 |
| Jogador 7 | 2-3 | 5 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 14% → 14% | 18 → 22 | 2 | 4 → 4 | 0.000 | -0.474 |
| Jogador 7 | 2-4 | 10 | 6.000 | -4.000 | 0 → 0 | 1 → 2 | 14% → 18% | 22 → 23 | 6 | 4 → 5 | -0.003 | 0.000 |
| Jogador 7 | 2-5 | 5 | 2.000 | 4.000 | 0 → 0 | 2 → 2 | 18% → 18% | 23 → 28 | 3 | 5 → 5 | -0.045 | 0.571 |
| Jogador 7 | 2-6 | 4 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 28 → 37 | 0 | 5 → 5 | -0.112 | 0.647 |
| Jogador 7 | 2-7 | 7 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 37 → 46 | 0 | 5 → 5 | 0.010 | 0.000 |
| Jogador 7 | 3-1 | 6 | 0.000 | -4.000 | 0 → 0 | 2 → 1 | 18% → 18% | 46 → 57 | 0 | 5 → 5 | 0.000 | -0.423 |
| Jogador 7 | 3-2 | 8 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 57 → 68 | 2 | 5 → 5 | 0.074 | -0.329 |
| Jogador 7 | 3-3 | 9 | 2.000 | 0.000 | 0 → 0 | 1 → 0 | 18% → 18% | 68 → 70 | 13 | 5 → 6 | 0.009 | 0.318 |
| Jogador 7 | 3-4 | 9 | 6.000 | 12.000 | 0 → 0 | 0 → 1 | 18% → 21% | 70 → 69 | 11 | 6 → 6 | -0.008 | 0.000 |
| Jogador 7 | 3-5 | 9 | 0.000 | 38.000 | 0 → 0 | 1 → 2 | 21% → 21% | 69 → 56 | 24 | 6 → 6 | -0.023 | 0.322 |
| Jogador 7 | 3-6 | 10 | 0.000 | 14.000 | 0 → 0 | 2 → 2 | 21% → 21% | 56 → 52 | 17 | 6 → 6 | 0.000 | -0.263 |
| Jogador 7 | 3-7 | 10 | 0.000 | -2.000 | 0 → 0 | 2 → 4 | 21% → 21% | 52 → 61 | 12 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 4-1 | 10 | 0.000 | -4.000 | 0 → 0 | 4 → 4 | 21% → 21% | 61 → 72 | 14 | 6 → 6 | 0.000 | 0.293 |
| Jogador 7 | 4-2 | 10 | 0.000 | 2.000 | 0 → 0 | 4 → 4 | 21% → 21% | 72 → 79 | 12 | 6 → 6 | 0.000 | -0.263 |
| Jogador 7 | 4-3 | 10 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 21% → 21% | 79 → 88 | 12 | 6 → 6 | 0.000 | 0.285 |
| Jogador 7 | 4-4 | 10 | 0.000 | 2.000 | 0 → 0 | 4 → 3 | 21% → 21% | 88 → 92 | 14 | 6 → 6 | -0.014 | 0.000 |
| Jogador 7 | 4-5 | 10 | 0.000 | 4.000 | 0 → 0 | 3 → 3 | 21% → 21% | 92 → 95 | 15 | 6 → 6 | -0.010 | 0.285 |
| Jogador 7 | 4-6 | 10 | 0.000 | -2.000 | 0 → 0 | 3 → 2 | 21% → 21% | 95 → 101 | 14 | 6 → 6 | -0.006 | 0.000 |
| Jogador 7 | 4-7 | 10 | 0.000 | 0.000 | 0 → 0 | 2 → 3 | 21% → 21% | 101 → 109 | 14 | 6 → 6 | 0.006 | 0.000 |
| Jogador 7 | 5-1 | 10 | 0.000 | 6.000 | 0 → 1 | 3 → 1 | 21% → 18% | 109 → 108 | 12 | 6 → 6 | -0.031 | -0.270 |
| Jogador 7 | 5-2 | 10 | 6.000 | -12.000 | 1 → 1 | 1 → 2 | 18% → 21% | 108 → 120 | 13 | 6 → 6 | 0.006 | -0.273 |
| Jogador 7 | 5-3 | 10 | 0.000 | 2.000 | 1 → 1 | 2 → 4 | 21% → 21% | 120 → 122 | 16 | 6 → 6 | 0.000 | -0.285 |
| Jogador 7 | 5-4 | 10 | 0.000 | 8.000 | 1 → 1 | 4 → 4 | 21% → 21% | 122 → 113 | 20 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 5-5 | 10 | -38.000 | -68.000 | 1 → 0 | 4 → 0 | 21% → 0% | 113 → 95 | 18 | 6 → 6 | 0.007 | -0.285 |
| Jogador 7 | 5-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 95 → 95 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 5-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 95 → 95 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 6-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 95 → 95 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 95 → 95 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 95 → 95 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 95 → 95 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 95 → 95 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 6-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 95 → 95 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 6-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 95 → 95 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 7-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 95 → 95 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 7-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 95 → 95 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 7-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 95 → 95 | 0 | 6 → 6 | 0.000 | 0.000 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 19, COMPOSITION_COMPATIBILITY: 28, IMMEDIATE_UPGRADE: 6, PAIR_POTENTIAL: 18; mudanças de composição: 1; posicionamento melhorou em 21 ações e piorou em 21.
- Jogador 7 — estado final: ouro 95, nível 6, vida 0.0, colocação 4.
| Jogador 8 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.115 | 0.000 |
| Jogador 8 | 1-2 | 10 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 3 | 3 | 3 → 3 | 0.001 | 0.000 |
| Jogador 8 | 1-3 | 7 | 2.000 | 0.000 | 0 → 0 | 0 → 0 | 7% → 11% | 3 → 5 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 8 | 1-4 | 4 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 11% → 11% | 5 → 9 | 1 | 3 → 4 | 0.000 | 0.000 |
| Jogador 8 | 2-1 | 5 | 2.000 | 0.000 | 0 → 0 | 0 → 1 | 11% → 14% | 9 → 13 | 1 | 4 → 4 | -0.008 | -0.496 |
| Jogador 8 | 2-2 | 4 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 13 → 20 | 0 | 4 → 4 | 0.000 | -0.632 |
| Jogador 8 | 2-3 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 14% → 14% | 20 → 28 | 0 | 4 → 4 | 0.002 | -0.452 |
| Jogador 8 | 2-4 | 7 | 4.000 | 0.000 | 0 → 0 | 1 → 0 | 14% → 14% | 28 → 34 | 3 | 4 → 4 | 0.014 | 0.000 |
| Jogador 8 | 2-5 | 9 | 4.000 | 4.000 | 0 → 0 | 0 → 0 | 14% → 14% | 34 → 39 | 5 | 4 → 5 | 0.008 | 0.293 |
| Jogador 8 | 2-6 | 9 | 6.000 | 22.000 | 0 → 0 | 0 → 2 | 14% → 18% | 39 → 30 | 16 | 5 → 5 | -0.034 | -0.293 |
| Jogador 8 | 2-7 | 9 | 0.000 | 18.000 | 0 → 0 | 2 → 2 | 18% → 18% | 30 → 23 | 16 | 5 → 5 | 0.000 | 0.000 |
| Jogador 8 | 3-1 | 9 | 0.000 | 0.000 | 0 → 0 | 2 → 2 | 18% → 18% | 23 → 27 | 12 | 5 → 5 | 0.000 | 0.302 |
| Jogador 8 | 3-2 | 9 | 0.000 | 4.000 | 0 → 0 | 2 → 2 | 18% → 18% | 27 → 28 | 12 | 5 → 5 | 0.000 | -0.304 |
| Jogador 8 | 3-3 | 9 | -2.000 | 6.000 | 0 → 0 | 2 → 2 | 18% → 18% | 28 → 29 | 12 | 5 → 5 | 0.015 | -0.298 |
| Jogador 8 | 3-4 | 9 | 0.000 | 0.000 | 0 → 0 | 2 → 1 | 18% → 18% | 29 → 23 | 15 | 5 → 5 | -0.007 | 0.000 |
| Jogador 8 | 3-5 | 9 | 0.000 | 4.000 | 0 → 0 | 1 → 1 | 18% → 18% | 23 → 13 | 16 | 5 → 5 | 0.000 | -0.298 |
| Jogador 8 | 3-6 | 8 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 13 → 7 | 12 | 5 → 5 | 0.000 | 0.369 |
| Jogador 8 | 3-7 | 5 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 7 → 6 | 6 | 5 → 5 | 0.000 | 0.000 |
| Jogador 8 | 4-1 | 6 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 6 → 5 | 6 | 5 → 6 | 0.000 | -0.438 |
| Jogador 8 | 4-2 | 7 | 12.000 | -6.000 | 0 → 1 | 1 → 2 | 18% → 21% | 5 → 6 | 7 | 6 → 6 | -0.010 | 0.423 |
| Jogador 8 | 4-3 | 6 | 0.000 | 6.000 | 1 → 1 | 2 → 3 | 21% → 21% | 6 → 6 | 8 | 6 → 6 | 0.000 | -0.446 |
| Jogador 8 | 4-4 | 10 | 0.000 | -4.000 | 1 → 1 | 3 → 2 | 21% → 21% | 6 → 9 | 15 | 6 → 6 | 0.006 | 0.000 |
| Jogador 8 | 4-5 | 6 | 0.000 | 8.000 | 1 → 1 | 2 → 1 | 21% → 21% | 9 → 6 | 9 | 6 → 6 | -0.030 | -0.461 |
| Jogador 8 | 4-6 | 6 | 0.000 | 4.000 | 1 → 1 | 1 → 2 | 21% → 21% | 6 → 6 | 8 | 6 → 6 | 0.010 | 0.489 |
| Jogador 8 | 4-7 | 5 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 21% → 21% | 6 → 5 | 6 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-1 | 10 | 0.000 | -4.000 | 1 → 1 | 2 → 4 | 21% → 21% | 5 → 10 | 12 | 6 → 6 | 0.006 | 0.296 |
| Jogador 8 | 5-2 | 10 | 0.000 | -2.000 | 1 → 1 | 4 → 4 | 21% → 21% | 10 → 10 | 15 | 6 → 6 | -0.006 | 0.289 |
| Jogador 8 | 5-3 | 10 | 4.000 | 2.000 | 1 → 2 | 4 → 2 | 21% → 21% | 10 → 7 | 15 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-4 | 5 | 0.000 | 6.000 | 2 → 2 | 2 → 3 | 21% → 21% | 7 → 6 | 7 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-5 | 9 | 0.000 | 0.000 | 2 → 2 | 3 → 2 | 21% → 21% | 6 → 6 | 10 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-6 | 5 | 0.000 | 0.000 | 2 → 2 | 2 → 2 | 21% → 21% | 6 → 6 | 6 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-7 | 7 | 0.000 | 0.000 | 2 → 2 | 2 → 3 | 21% → 21% | 6 → 6 | 8 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 6-1 | 7 | -36.000 | -68.000 | 2 → 0 | 3 → 0 | 21% → 0% | 6 → 0 | 6 | 6 → 6 | -0.036 | -0.407 |
| Jogador 8 | 6-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 6-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 6-4 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 6-5 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 6-6 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 6-7 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 7-1 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 7-2 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 7-3 | 2 | 0.000 | 0.000 | 0 → 0 | 0 → 0 | 0% → 0% | 0 → 0 | 0 | 6 → 6 | 0.000 | 0.000 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 14, COMPOSITION_COMPATIBILITY: 23, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 16; mudanças de composição: 0; posicionamento melhorou em 20 ações e piorou em 22.
- Jogador 8 — estado final: ouro 0, nível 6, vida 0.0, colocação 3.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Revertidas ≤1 ação | ≤2 ações | ≤4 ações | Ouro perdido | Upgrades | Vendas core/par | Valor médio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 47 | 17 | 2 | 2 | 2 | 0 | 8 | 4 | 3.3277 |
| Jogador 2 | 111 | 74 | 4 | 5 | 5 | 0 | 11 | 14 | 3.4379 |
| Jogador 3 | 46 | 19 | 1 | 1 | 1 | 0 | 5 | 3 | 4.2893 |
| Jogador 4 | 64 | 35 | 6 | 6 | 6 | 0 | 8 | 8 | 4.6726 |
| Jogador 5 | 68 | 38 | 8 | 8 | 8 | 0 | 8 | 9 | 3.9721 |
| Jogador 6 | 130 | 98 | 3 | 4 | 4 | 0 | 9 | 22 | 2.6363 |
| Jogador 7 | 71 | 45 | 4 | 4 | 4 | 0 | 6 | 7 | 3.7987 |
| Jogador 8 | 58 | 34 | 3 | 3 | 3 | 0 | 5 | 6 | 4.2791 |

Vendas de core/pares ignoradas antes da decisão da composição: **34**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Uma venda sem compra correspondente na janela é UNKNOWN; sequências ambíguas não são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| MEDIUM | Jogador 1 | 1-3 | 22 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 1 | 2-1 | 46 | PURCHASE_REVERSED | Compra de DA_18_Sentry desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 1 | 4-4 | 207 | SOLD_CORE_UNIT | Venda de 'DA_18_Shen' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 1 | 4-5 | 213 | SOLD_CORE_UNIT | Venda de 'DA_18_Sejuani' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 1 | 4-5 | 217 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Teemo' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 1 | 4-6 | 222 | SOLD_CORE_UNIT | Venda de 'DA_18_Elise' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 1 | 4-7 | 241 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_KogMaw18_AD' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 1 | 4-7 | 241 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Rengar' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 1 | 4-7 | 241 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Elise' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 2 | 2-4 | 73 | PURCHASE_REVERSED | Compra de DA_18_Kayle desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 2 | 2-6 | 95 | SOLD_CORE_UNIT | Venda de 'DA_18_Sejuani' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 2 | 2-7 | 100 | PURCHASE_REVERSED | Compra de DA_18_KhaZix desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 2-7 | 102 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 3-1 | 109 | PURCHASE_REVERSED | Compra de DA_18_Yorick desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 2 | 3-2 | 117 | PURCHASE_REVERSED | Compra de DA_18_Yorick desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 2 | 4-1 | 180 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sejuani' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 2 | 4-6 | 228 | SOLD_CORE_UNIT | Venda de 'DA_18_MasterYi_AD' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 2 | 4-7 | 233 | SOLD_CORE_UNIT | Venda de 'DA_18_Shen' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 2 | 4-7 | 239 | SOLD_CORE_UNIT | Venda de 'DA_18_Rengar' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 2 | 5-2 | 256 | SOLD_CORE_UNIT | Venda de 'DA_18_Shen' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 2 | 5-7 | 302 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Vi18' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 2 | 6-2 | 325 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Vi18' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 2 | 6-3 | 332 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 2 | 6-3 | 336 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rengar' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 2 | 6-4 | 346 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Warwick' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 2 | 7-1 | 387 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sejuani' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 2 | 7-2 | 395 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 2 | 7-3 | 402 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 3 | 2-5 | 83 | SOLD_CORE_UNIT | Venda de 'DA_18_Tristana' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 3 | 2-5 | 83 | PURCHASE_REVERSED | Compra de DA_18_Tristana desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 3 | 3-4 | 141 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Kayle' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 3 | 4-3 | 199 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Cassiopeia' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 3 | 2-6 | 93 | COMP_DIRECTION_CHANGES_WITHOUT_GAIN | Três mudanças consecutivas de composição sem ganho mensurável nos campos registrados; revisar se a IA está perseguindo comps sem evidência. |
| MEDIUM | Jogador 3 | 4-6 | 231 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Scuttlecrab18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 3 | 4-6 | 231 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Vi18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 3 | 4-6 | 231 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Rammus' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 3 | 2-5 | 88 | COMP_DIRECTION_CHURN | Episódio de mudanças repetidas de composição; revisar as transições listadas. |
| MEDIUM | Jogador 3 | 2-6 | 97 | COMP_DIRECTION_CHURN | Episódio de mudanças repetidas de composição; revisar as transições listadas. |
| MEDIUM | Jogador 3 | 3-4 | 137 | COMP_DIRECTION_CHURN | Episódio de mudanças repetidas de composição; revisar as transições listadas. |
| MEDIUM | Jogador 3 | 3-5 | 146 | COMP_DIRECTION_CHURN | Episódio de mudanças repetidas de composição; revisar as transições listadas. |
| MEDIUM | Jogador 4 | 1-3 | 22 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 4 | 2-4 | 75 | PURCHASE_REVERSED | Compra de DA_18_Sejuani desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 4 | 2-5 | 81 | SOLD_CORE_UNIT | Venda de 'DA_18_KhaZix' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 4 | 2-5 | 81 | PURCHASE_REVERSED | Compra de DA_18_KhaZix desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 4 | 2-5 | 83 | SOLD_CORE_UNIT | Venda de 'DA_Gromp18_AP' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 4 | 2-5 | 83 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 4 | 2-5 | 85 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 4 | 2-6 | 93 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Camille' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 4 | 2-7 | 99 | SOLD_CORE_UNIT | Venda de 'DA_18_Akali_AD' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 4 | 2-7 | 101 | SOLD_CORE_UNIT | Venda de 'DA_Vi18' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 4 | 2-7 | 101 | PURCHASE_REVERSED | Compra de DA_Vi18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 4 | 2-7 | 103 | SOLD_CORE_UNIT | Venda de 'DA_18_Kayle' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 4 | 2-7 | 103 | PURCHASE_REVERSED | Compra de DA_18_Kayle desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 4 | 3-7 | 169 | SOLD_CORE_UNIT | Venda de 'DA_18_Yunara' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 4 | 5-2 | 261 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Fiddlesticks18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 4 | 5-2 | 261 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_CrimsonRaptor18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 4 | 5-2 | 261 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Hecarim' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 5 | 1-3 | 22 | PURCHASE_REVERSED | Compra de DA_18_Yunara desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 1-3 | 24 | PURCHASE_REVERSED | Compra de DA_Murkwolf18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-1 | 46 | PURCHASE_REVERSED | Compra de DA_18_LeBlanc desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-3 | 61 | PURCHASE_REVERSED | Compra de DA_18_Rakan desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-4 | 71 | PURCHASE_REVERSED | Compra de DA_KogMaw18_AD desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 5 | 2-4 | 73 | PURCHASE_REVERSED | Compra de DA_18_LeBlanc desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 5 | 2-5 | 81 | SOLD_CORE_UNIT | Venda de 'DA_18_Rammus' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 5 | 2-7 | 99 | PURCHASE_REVERSED | Compra de DA_18_Yunara desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 5 | 3-1 | 108 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Gromp18_AP' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 5 | 3-2 | 119 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Gromp18_AP' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 5 | 3-2 | 121 | PURCHASE_REVERSED | Compra de DA_18_Shen desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 5 | 3-7 | 162 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Akali_AD' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 5 | 4-2 | 185 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Cassiopeia' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 5 | 4-2 | 190 | SOLD_CORE_UNIT | Venda de 'DA_Gromp18_AP' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 5 | 4-3 | 194 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sejuani' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 5 | 4-3 | 199 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 5 | 4-6 | 224 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Tristana' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 5 | 5-6 | 301 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Ahri' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 5 | 5-6 | 301 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Shen' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 5 | 5-6 | 301 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_KogMaw18_AD' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 6 | 1-2 | 12 | PURCHASE_REVERSED | Compra de DA_18_Yunara desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 6 | 1-2 | 14 | PURCHASE_REVERSED | Compra de DA_18_Xayah desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 6 | 2-5 | 81 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 6 | 2-5 | 84 | PURCHASE_REVERSED | Compra de DA_18_Shen desfeita em 2 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 6 | 2-7 | 99 | SOLD_CORE_UNIT | Venda de 'DA_Vi18' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 6 | 2-7 | 99 | PURCHASE_REVERSED | Compra de DA_Vi18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 6 | 3-4 | 141 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Scuttlecrab18' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 3-7 | 167 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 3-7 | 170 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 4-1 | 176 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Varus' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 4-1 | 178 | SOLD_CORE_UNIT | Venda de 'DA_CrimsonRaptor18' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 4-2 | 182 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 4-3 | 199 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 4-4 | 205 | SOLD_CORE_UNIT | Venda de 'DA_18_Rammus' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 4-5 | 213 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Scuttlecrab18' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 4-6 | 227 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Scuttlecrab18' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 4-6 | 230 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Vi18' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 4-7 | 235 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_KogMaw18_AD' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 5-1 | 245 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 5-4 | 272 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 5-5 | 282 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 5-5 | 284 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 5-7 | 302 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 6-6 | 362 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Tristana' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 7-1 | 389 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rammus' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 6 | 7-2 | 394 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Sejuani' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 7 | 1-2 | 12 | PURCHASE_REVERSED | Compra de DA_18_Varus desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 7 | 1-4 | 32 | PURCHASE_REVERSED | Compra de DA_18_Elise desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 7 | 3-1 | 108 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Alistar' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 7 | 3-2 | 117 | PURCHASE_REVERSED | Compra de DA_Murkwolf18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 7 | 3-3 | 127 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Scuttlecrab18' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 7 | 3-3 | 129 | PURCHASE_REVERSED | Compra de DA_Gromp18_AP desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 7 | 3-6 | 159 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Alistar' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 7 | 3-7 | 169 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 7 | 4-1 | 174 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Hecarim' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 7 | 4-2 | 184 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Gromp18_AP' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 7 | 4-6 | 223 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Aphelios' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 7 | 5-6 | 301 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_KogMaw18_AD' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 7 | 5-6 | 301 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Fiddlesticks18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 7 | 5-6 | 301 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_CrimsonRaptor18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 8 | 1-2 | 12 | PURCHASE_REVERSED | Compra de DA_18_Veigar desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 1-2 | 14 | PURCHASE_REVERSED | Compra de DA_Karma18 desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| MEDIUM | Jogador 8 | 1-3 | 22 | PURCHASE_REVERSED | Compra de DA_18_Xayah desfeita em 1 ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado. |
| HIGH | Jogador 8 | 3-2 | 123 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 8 | 3-3 | 130 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 8 | 4-4 | 202 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rammus' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 8 | 4-4 | 208 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rammus' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 8 | 5-3 | 268 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_KhaZix' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| HIGH | Jogador 8 | 5-5 | 287 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma unidade core ou reduziu pares após a decisão da composição; verificar se houve substituição/upgrade que compense. |
| MEDIUM | Jogador 8 | 6-2 | 331 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_Vi18' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 8 | 6-2 | 331 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Tristana' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |
| MEDIUM | Jogador 8 | 6-2 | 331 | CORE_UNIT_MISSING_REPEATEDLY | Unidade core 'DA_18_Diana' ficou ausente do tabuleiro e banco em 3 snapshots consecutivos. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
